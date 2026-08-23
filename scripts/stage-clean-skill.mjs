#!/usr/bin/env node

import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

export const CLEAN_SKILL_EXCLUDED_NAMES = new Set([
  'node_modules',
  '__pycache__',
  '.DS_Store',
  '.git',
]);

function posixRelative(from, to) {
  return path.relative(from, to).split(path.sep).join('/');
}

export function discoverSkillNames(sourceRoot = repoRoot) {
  return fs
    .readdirSync(sourceRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && !entry.isSymbolicLink() && entry.name.startsWith('huashu-'))
    .filter((entry) => fs.existsSync(path.join(sourceRoot, entry.name, 'SKILL.md')))
    .map((entry) => entry.name)
    .sort();
}

export function shouldExcludeFromCleanSkill(relative) {
  const parts = relative.split('/');
  if (parts.some((part) => CLEAN_SKILL_EXCLUDED_NAMES.has(part))) return true;
  return false;
}

function walkTree(root, visit) {
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    const full = path.join(root, entry.name);
    visit(full, entry);
    if (entry.isDirectory() && !entry.isSymbolicLink()) walkTree(full, visit);
  }
}

export function listTrackedSkillFiles(sourceRoot, skillName) {
  const tracked = spawnSync('git', ['ls-files', '-z', '--', `${skillName}/`], {
    cwd: sourceRoot,
    encoding: 'utf8',
  });
  if (tracked.error) {
    throw new Error(`unable to enumerate tracked Skill files for ${skillName}: ${tracked.error.message}`);
  }
  if (tracked.status !== 0) {
    throw new Error(
      `unable to enumerate tracked Skill files for ${skillName}: ${tracked.stderr || `git ls-files exited ${tracked.status}`}`,
    );
  }
  return tracked.stdout.split('\0').filter(Boolean);
}

function isInsideRoot(root, candidate) {
  const relative = path.relative(root, candidate);
  return relative === '' || (relative !== '..' && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative));
}

export function copyableTrackedSkillPath(sourceRoot, relative) {
  const sourceResolved = path.resolve(sourceRoot);
  const src = path.resolve(sourceRoot, ...relative.split('/'));
  if (!isInsideRoot(sourceResolved, src)) {
    throw new Error(`tracked Skill path escapes source root: ${relative}`);
  }
  if (shouldExcludeFromCleanSkill(relative)) return null;

  let stat;
  try {
    stat = fs.lstatSync(src);
  } catch (error) {
    if (error && error.code === 'ENOENT') {
      throw new Error(`tracked Skill file is missing on disk: ${relative}`);
    }
    throw error;
  }

  if (stat.isSymbolicLink()) {
    throw new Error(`refusing to follow source symlink: ${relative}`);
  }
  if (!stat.isFile()) return null;

  const fileReal = fs.realpathSync(src);
  const sourceReal = fs.realpathSync(sourceRoot);
  if (!isInsideRoot(sourceReal, fileReal)) {
    throw new Error(`refusing to follow source symlink: ${relative}`);
  }
  return src;
}

export function stageCleanSkill(sourceRoot, skillName, destRoot) {
  fs.mkdirSync(destRoot, { recursive: true });

  for (const relative of listTrackedSkillFiles(sourceRoot, skillName)) {
    const src = copyableTrackedSkillPath(sourceRoot, relative);
    if (!src) continue;
    const destination = path.join(destRoot, posixRelative(path.join(sourceRoot, skillName), src));
    fs.mkdirSync(path.dirname(destination), { recursive: true });
    fs.copyFileSync(src, destination);
  }
}

export function stageAllSkills(sourceRoot, destSkillsRoot) {
  fs.mkdirSync(destSkillsRoot, { recursive: true });
  for (const skillName of discoverSkillNames(sourceRoot)) {
    stageCleanSkill(sourceRoot, skillName, path.join(destSkillsRoot, skillName));
  }
}

export function collectRegularFiles(root) {
  const files = [];
  walkTree(root, (full, entry) => {
    if (entry.isDirectory()) return;
    files.push(posixRelative(root, full));
  });
  return files.sort();
}

export function assertNoSymlinks(root) {
  const links = [];
  walkTree(root, (full, entry) => {
    if (entry.isSymbolicLink()) links.push(posixRelative(root, full));
  });
  if (links.length > 0) {
    throw new Error(`symlinks are not allowed under ${root}:\n${links.join('\n')}`);
  }
}

export function diffTrees(leftRoot, rightRoot) {
  const left = collectRegularFiles(leftRoot);
  const right = collectRegularFiles(rightRoot);
  const missing = left.filter((file) => !right.includes(file));
  const extra = right.filter((file) => !left.includes(file));
  const changed = [];
  for (const file of left) {
    if (!right.includes(file)) continue;
    const leftBytes = fs.readFileSync(path.join(leftRoot, file));
    const rightBytes = fs.readFileSync(path.join(rightRoot, file));
    if (!leftBytes.equals(rightBytes)) changed.push(file);
  }
  return { missing, extra, changed };
}
