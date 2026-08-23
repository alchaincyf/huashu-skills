#!/usr/bin/env node

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  assertNoSymlinks,
  diffTrees,
  discoverSkillNames,
  stageAllSkills,
} from './stage-clean-skill.mjs';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const pluginRoot = path.join(repoRoot, 'plugins', 'huashu-skills');
const leafRoot = path.join(pluginRoot, 'skills');
const openaiYaml = path.join(pluginRoot, '.codex-plugin', 'openai.yaml');

function installHostExtras(destSkillsRoot) {
  const stat = fs.lstatSync(openaiYaml);
  if (stat.isSymbolicLink() || !stat.isFile()) {
    throw new Error(`refusing to follow source symlink: ${openaiYaml}`);
  }
  const agentsDir = path.join(destSkillsRoot, 'huashu-slides', 'agents');
  fs.mkdirSync(agentsDir, { recursive: true });
  fs.copyFileSync(openaiYaml, path.join(agentsDir, 'openai.yaml'));
}

function materialize(destSkillsRoot) {
  fs.rmSync(destSkillsRoot, { recursive: true, force: true });
  stageAllSkills(repoRoot, destSkillsRoot);
  installHostExtras(destSkillsRoot);
  assertNoSymlinks(destSkillsRoot);
}

const check = process.argv.includes('--check');

if (!fs.existsSync(openaiYaml)) {
  throw new Error(`missing Codex agent card: ${openaiYaml}`);
}

if (check) {
  const staged = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-skills-plugin-leaf-'));
  try {
    const expected = path.join(staged, 'skills');
    materialize(expected);
    if (!fs.existsSync(leafRoot)) {
      throw new Error('plugins/huashu-skills/skills is missing — run node scripts/build-plugin-leaf.mjs');
    }
    assertNoSymlinks(leafRoot);
    const { missing, extra, changed } = diffTrees(expected, leafRoot);
    if (missing.length || extra.length || changed.length) {
      const lines = [
        'plugin leaf is stale — run node scripts/build-plugin-leaf.mjs',
        missing.length ? `missing:\n  ${missing.join('\n  ')}` : '',
        extra.length ? `extra:\n  ${extra.join('\n  ')}` : '',
        changed.length ? `changed:\n  ${changed.join('\n  ')}` : '',
      ].filter(Boolean);
      throw new Error(lines.join('\n'));
    }
    const skillCount = discoverSkillNames(repoRoot).length;
    const leafCount = fs.readdirSync(leafRoot, { withFileTypes: true }).filter((e) => e.isDirectory()).length;
    if (skillCount !== leafCount) {
      throw new Error(`plugin leaf skill count mismatch: expected ${skillCount}, found ${leafCount}`);
    }
  } finally {
    fs.rmSync(staged, { recursive: true, force: true });
  }
  process.stdout.write('plugin leaf is fresh\n');
} else {
  materialize(leafRoot);
  const skillCount = discoverSkillNames(repoRoot).length;
  process.stdout.write(`wrote ${leafRoot} (${skillCount} skills)\n`);
}
