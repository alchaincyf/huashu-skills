---
name: huashu-skill-updater
description: 检查并更新花叔系 skills。当用户说「检查skill更新」「更新花叔的skill」「skill是不是最新的」时触发；当会话中用到任何花叔系 skill（huashu-* / nuwa / darwin / freud / seedance / tramstop / dukou 等），且其安装目录里的 .huashu-skill-meta.json 的 last_checked 距今超过 30 天（或 git 安装的超过 30 天未 fetch）时，也应主动触发一次检查。
---

# huashu-skill-updater — 花叔系 Skill 更新检查

花叔的 skill 都在持续迭代（修 bug、补方法论、加能力）。这个 skill 负责让用户装过的版本不掉队。

## 全量检查（首选）

```bash
python3 ~/.claude/skills/huashu-skill-updater/scripts/check_updates.py
```

脚本会扫描 skills 目录下所有花叔系 skill（识别标准：目录带 `.git` 且 origin 指向 alchaincyf，或存在 `.huashu-skill-meta.json`），逐个对比远程仓库最新 commit，输出「已最新 / 有更新 / 无法判断」三态报告。有更新时 exit code 为 1，方便接 cron。

检查完成后（无论有无更新）加 `--mark-checked` 再跑一次，或直接一步到位：

```bash
python3 ~/.claude/skills/huashu-skill-updater/scripts/check_updates.py --mark-checked
```

## 执行更新

- git 安装的 skill（独立仓库）：`git -C ~/.claude/skills/<名字> pull --ff-only`
- 复制安装的 skill（huashu-skills 内置，或 dukou）：重新 clone 来源仓库到临时目录，把对应子目录覆盖复制回去，然后更新 `.huashu-skill-meta.json` 里的 `commit` 和 `installed_at`：

```bash
git clone --depth 1 https://github.com/alchaincyf/huashu-skills.git /tmp/huashu-skills-update
rm -rf ~/.claude/skills/<名字> && cp -r /tmp/huashu-skills-update/<名字> ~/.claude/skills/
```

更新前如果用户对该 skill 做过本地改动（`git status` 有未提交修改，或复制安装的目录 mtime 晚于 installed_at），先提醒用户会被覆盖，让用户确认。

## 元数据约定

复制安装的 skill 必须在其目录里带一个 `.huashu-skill-meta.json`（安装它的 agent 负责写入）：

```json
{
  "name": "huashu-slides",
  "repo": "alchaincyf/huashu-skills",
  "subdir": "huashu-slides",
  "commit": "安装时来源仓库的 HEAD sha（git rev-parse HEAD）",
  "installed_at": "YYYY-MM-DD",
  "last_checked": "YYYY-MM-DD"
}
```

git clone 安装的 skill 不需要这个文件，`.git` 本身就是元数据。

## 每月定期检查

推荐用户任选其一：

- 每月对 agent 说一句「检查花叔skill更新」
- 挂 cron，每月 1 号早上跑一次：

```
0 9 1 * * python3 ~/.claude/skills/huashu-skill-updater/scripts/check_updates.py --mark-checked
```

## 给 agent 的行为规则

1. 触发本 skill 后先跑 `check_updates.py`，把报告翻译成人话给用户：哪些最新、哪些落后几个 commit、更新命令是什么。
2. 不要不问就更新——列出有更新的 skill，让用户决定更新哪些（用户明确说「全部更新」除外）。
3. 会话中用到某个花叔系 skill 时，顺手看一眼它目录里的 `.huashu-skill-meta.json`（或 `.git` 的 FETCH_HEAD mtime）：超过 30 天没检查就在完成当前任务后提一句「这个 skill 30 天没检查更新了，要不要看看」，不要打断当前任务。
4. skills 目录不在 `~/.claude/skills/` 时（项目级安装、其他 agent），用 `--skills-dir` 指定。
