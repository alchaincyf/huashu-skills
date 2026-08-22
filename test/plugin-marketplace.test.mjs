import { test } from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  copyableTrackedSkillPath,
  discoverSkillNames,
  stageAllSkills,
  stageCleanSkill,
} from '../scripts/stage-clean-skill.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');
const pluginRoot = path.join(repoRoot, 'plugins', 'huashu-skills');
const leafRoot = path.join(pluginRoot, 'skills');
const pluginVersion = '0.1.0';

function read(relativePath) {
  return fs.readFileSync(path.join(repoRoot, relativePath), 'utf8');
}

function json(relativePath) {
  return JSON.parse(read(relativePath));
}

function assertRegularFile(filePath) {
  const stat = fs.lstatSync(filePath);
  assert.equal(stat.isSymbolicLink(), false, `${filePath} must not be a symlink`);
  assert.equal(stat.isFile(), true, `${filePath} must be a regular file`);
}

function git(cwd, args) {
  const result = spawnSync('git', args, { cwd, encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr || result.error?.message);
  return result;
}

function initSkillFixture(skillName) {
  const source = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-skill-fixture-'));
  const skillDir = path.join(source, skillName);
  fs.mkdirSync(skillDir, { recursive: true });
  fs.writeFileSync(path.join(skillDir, 'SKILL.md'), `# ${skillName}\n`);
  git(source, ['init']);
  git(source, ['add', '.']);
  git(source, ['-c', 'user.email=huashu-test@example.com', '-c', 'user.name=huashu-test', 'commit', '-m', 'fixture']);
  return source;
}

test('Claude, Grok, and Codex marketplaces point at the generated plugin leaf', () => {
  const claude = json('.claude-plugin/marketplace.json');
  const grok = json('.grok-plugin/marketplace.json');
  const codex = json('.agents/plugins/marketplace.json');

  assert.equal(claude.name, 'huashu-skills');
  assert.equal(grok.name, 'huashu-skills');
  assert.equal(codex.name, 'huashu-skills');
  assert.equal(claude.plugins[0].source, './plugins/huashu-skills');
  assert.deepEqual(grok.plugins[0].source, { type: 'local', path: './plugins/huashu-skills' });
  assert.deepEqual(codex.plugins[0].source, { source: 'local', path: './plugins/huashu-skills' });
  assert.equal(claude.plugins[0].version, pluginVersion);
  assert.equal(grok.plugins[0].version, pluginVersion);
});

test('host plugin manifests use an independent plugin version', () => {
  const claude = json('plugins/huashu-skills/.claude-plugin/plugin.json');
  const grok = json('plugins/huashu-skills/plugin.json');
  const codex = json('plugins/huashu-skills/.codex-plugin/plugin.json');

  assert.equal(claude.version, pluginVersion);
  assert.equal(grok.version, pluginVersion);
  assert.equal(codex.version, pluginVersion);
  assert.equal(codex.skills, './skills/');
});

test('the generated Skill leaf is real files with Codex agent card on huashu-slides', () => {
  const skillNames = discoverSkillNames(repoRoot);
  assert.ok(skillNames.length >= 21);
  for (const skillName of skillNames) {
    assertRegularFile(path.join(leafRoot, skillName, 'SKILL.md'));
  }
  assertRegularFile(path.join(leafRoot, 'huashu-slides', 'agents', 'openai.yaml'));
  assert.equal(fs.existsSync(path.join(pluginRoot, 'agents')), false);
});

test('the plugin leaf stays fresh against the Skill SSoT', () => {
  const check = spawnSync(process.execPath, [path.join(repoRoot, 'scripts', 'build-plugin-leaf.mjs'), '--check'], {
    cwd: repoRoot,
    encoding: 'utf8',
  });
  assert.equal(check.status, 0, check.stderr || check.stdout);
  assert.match(check.stdout, /plugin leaf is fresh/);
});

test('the plugin release receipt matches host-visible bytes', () => {
  const check = spawnSync(process.execPath, [path.join(repoRoot, 'scripts', 'check-plugin-release.mjs')], {
    cwd: repoRoot,
    encoding: 'utf8',
  });
  assert.equal(check.status, 0, check.stderr || check.stdout);
  assert.match(check.stdout, /plugin release identity ok: 0\.1\.0/);
});

test('the plugin release gate rejects changed bytes without a version bump', () => {
  const fixture = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-skills-plugin-release-'));
  const gate = path.join(repoRoot, 'scripts', 'check-plugin-release.mjs');
  const writeJson = (relative, value) => {
    const target = path.join(fixture, relative);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, `${JSON.stringify(value, null, 2)}\n`);
  };
  try {
    writeJson('.claude-plugin/marketplace.json', { plugins: [{ version: pluginVersion }] });
    writeJson('.grok-plugin/marketplace.json', { plugins: [{ version: pluginVersion }] });
    writeJson('.agents/plugins/marketplace.json', { plugins: [] });
    for (const relative of [
      'plugins/huashu-skills/plugin.json',
      'plugins/huashu-skills/.claude-plugin/plugin.json',
      'plugins/huashu-skills/.codex-plugin/plugin.json',
    ]) {
      writeJson(relative, { name: 'huashu-skills', version: pluginVersion });
    }
    fs.writeFileSync(path.join(fixture, 'plugins/huashu-skills/.codex-plugin/openai.yaml'), 'name: huashu-skills\n');
    fs.mkdirSync(path.join(fixture, 'plugins/huashu-skills/skills/huashu-slides'), { recursive: true });
    const payload = path.join(fixture, 'plugins/huashu-skills/skills/huashu-slides/SKILL.md');
    fs.writeFileSync(payload, '# huashu-slides\n');

    const receipt = spawnSync(process.execPath, [gate, '--root', fixture, '--write'], { encoding: 'utf8' });
    assert.equal(receipt.status, 0, receipt.stderr || receipt.stdout);
    fs.appendFileSync(payload, 'changed\n');
    const check = spawnSync(process.execPath, [gate, '--root', fixture], { encoding: 'utf8' });
    assert.notEqual(check.status, 0);
    assert.match(check.stderr, /plugin bytes changed without a version increment/);
  } finally {
    fs.rmSync(fixture, { recursive: true, force: true });
  }
});

test('Pi package declares every root skill directory', () => {
  const root = json('package.json');
  assert.equal(root.private, true);
  assert.ok(root.keywords.includes('pi-package'));
  const expected = discoverSkillNames(repoRoot).map((name) => `./${name}`);
  assert.deepEqual(root.pi.skills.sort(), expected.sort());
});

test('stageCleanSkill copies tracked files only and skips untracked Skill paths', () => {
  const source = initSkillFixture('huashu-slides');
  const destRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-clean-skill-'));
  const markerName = 'review-untracked-marker.txt';
  fs.writeFileSync(path.join(source, 'huashu-slides', markerName), 'should-not-pack\n');
  try {
    stageCleanSkill(source, 'huashu-slides', path.join(destRoot, 'huashu-slides'));
    assert.equal(fs.existsSync(path.join(destRoot, 'huashu-slides', 'SKILL.md')), true);
    assert.equal(fs.existsSync(path.join(destRoot, 'huashu-slides', markerName)), false);
  } finally {
    fs.rmSync(source, { recursive: true, force: true });
    fs.rmSync(destRoot, { recursive: true, force: true });
  }
});

test('stageCleanSkill refuses to follow a tracked file symlink', () => {
  const source = initSkillFixture('huashu-slides');
  const destRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-symlink-file-'));
  try {
    const secret = path.join(source, 'huashu-slides', 'secret.txt');
    fs.writeFileSync(secret, 'secret\n');
    fs.rmSync(path.join(source, 'huashu-slides', 'SKILL.md'));
    fs.symlinkSync(secret, path.join(source, 'huashu-slides', 'SKILL.md'));
    git(source, ['add', 'huashu-slides/SKILL.md']);
    git(source, ['-c', 'user.email=huashu-test@example.com', '-c', 'user.name=huashu-test', 'commit', '-m', 'symlink']);
    assert.throws(
      () => stageCleanSkill(source, 'huashu-slides', path.join(destRoot, 'huashu-slides')),
      /refusing to follow source symlink: huashu-slides\/SKILL.md/,
    );
  } finally {
    fs.rmSync(source, { recursive: true, force: true });
    fs.rmSync(destRoot, { recursive: true, force: true });
  }
});

test('copyableTrackedSkillPath refuses a leaf symlink without following it', () => {
  const source = initSkillFixture('huashu-slides');
  try {
    const target = path.join(source, 'huashu-slides', 'secret.txt');
    fs.writeFileSync(target, 'secret\n');
    fs.rmSync(path.join(source, 'huashu-slides', 'SKILL.md'));
    fs.symlinkSync(target, path.join(source, 'huashu-slides', 'SKILL.md'));
    assert.throws(
      () => copyableTrackedSkillPath(source, 'huashu-slides/SKILL.md'),
      /refusing to follow source symlink: huashu-slides\/SKILL.md/,
    );
  } finally {
    fs.rmSync(source, { recursive: true, force: true });
  }
});

test('stageAllSkills materializes every discovered skill directory', () => {
  const source = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-multi-skill-'));
  const destRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'huashu-multi-dest-'));
  try {
    for (const skillName of ['huashu-slides', 'huashu-research']) {
      const skillDir = path.join(source, skillName);
      fs.mkdirSync(skillDir, { recursive: true });
      fs.writeFileSync(path.join(skillDir, 'SKILL.md'), `# ${skillName}\n`);
    }
    git(source, ['init']);
    git(source, ['add', '.']);
    git(source, ['-c', 'user.email=huashu-test@example.com', '-c', 'user.name=huashu-test', 'commit', '-m', 'fixture']);
    stageAllSkills(source, destRoot);
    assert.equal(fs.existsSync(path.join(destRoot, 'huashu-slides', 'SKILL.md')), true);
    assert.equal(fs.existsSync(path.join(destRoot, 'huashu-research', 'SKILL.md')), true);
  } finally {
    fs.rmSync(source, { recursive: true, force: true });
    fs.rmSync(destRoot, { recursive: true, force: true });
  }
});
