#!/usr/bin/env python3
"""检查花叔系 skills 是否有新版本。

识别两类安装方式：
- git clone 安装：目录带 .git，且 origin 指向 github.com/alchaincyf
- 复制安装：目录带 .huashu-skill-meta.json（含来源仓库与安装时 commit）

用法：
  python3 check_updates.py                        # 检查 ~/.claude/skills
  python3 check_updates.py --skills-dir <目录>     # 检查其他 skills 目录
  python3 check_updates.py --mark-checked         # 检查并回写 last_checked

exit code：0 = 全部最新；1 = 有可更新项；2 = 出错。
"""

import argparse
import datetime
import json
import os
import subprocess
import sys

OWNER = "alchaincyf"


def run(cmd, cwd=None, timeout=60):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return 1, "", str(e)


def remote_head(repo):
    """repo 形如 'alchaincyf/huashu-skills' 或裸仓库名。返回远程 HEAD sha 或 None。"""
    if "/" not in repo:
        repo = f"{OWNER}/{repo}"
    code, out, _ = run(["git", "ls-remote", f"https://github.com/{repo}.git", "HEAD"])
    if code == 0 and out:
        return out.split()[0]
    return None


def check_git_install(path):
    code, url, _ = run(["git", "-C", path, "config", "--get", "remote.origin.url"])
    if code != 0 or OWNER not in url:
        return None  # 不是花叔系，跳过
    _, local, _ = run(["git", "-C", path, "rev-parse", "HEAD"])
    repo = url.rstrip("/").removesuffix(".git").split("github.com")[-1].lstrip("/:")
    remote = remote_head(repo)
    if not remote:
        return ("unknown", f"无法访问远程仓库 {repo}", None)
    if remote == local:
        return ("ok", f"最新（{local[:7]}）", None)
    return ("outdated", f"本地 {local[:7]} → 远端 {remote[:7]}",
            f"git -C {path} pull --ff-only")


def check_copy_install(path, meta_file, mark_checked):
    try:
        meta = json.load(open(meta_file, encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        return ("unknown", f"meta 文件损坏：{e}", None)
    repo = meta.get("repo", "")
    local = meta.get("commit", "")
    remote = remote_head(repo) if repo else None
    if not remote:
        return ("unknown", f"无法访问远程仓库 {repo or '（meta 缺 repo 字段）'}", None)
    if mark_checked:
        meta["last_checked"] = datetime.date.today().isoformat()
        json.dump(meta, open(meta_file, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
    if remote == local:
        return ("ok", f"最新（{local[:7]}，装于 {meta.get('installed_at', '?')}）", None)
    return ("outdated", f"安装时 {local[:7] or '未知'} → 远端 {remote[:7]}",
            f"重新复制来源仓库 {repo} 的 {meta.get('subdir', '?')}/ 子目录（见 huashu-skill-updater/SKILL.md）")


def main():
    p = argparse.ArgumentParser(description="检查花叔系 skills 更新")
    p.add_argument("--skills-dir", default=os.path.expanduser("~/.claude/skills"))
    p.add_argument("--mark-checked", action="store_true",
                   help="检查后把 .huashu-skill-meta.json 的 last_checked 更新为今天")
    args = p.parse_args()

    skills_dir = os.path.abspath(os.path.expanduser(args.skills_dir))
    if not os.path.isdir(skills_dir):
        print(f"skills 目录不存在：{skills_dir}", file=sys.stderr)
        return 2

    results = []
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name)
        if not os.path.isdir(path):
            continue
        meta_file = os.path.join(path, ".huashu-skill-meta.json")
        if os.path.isdir(os.path.join(path, ".git")):
            r = check_git_install(path)
        elif os.path.isfile(meta_file):
            r = check_copy_install(path, meta_file, args.mark_checked)
        else:
            continue  # 非花叔系或无法识别，跳过
        if r:
            results.append((name, *r))

    if not results:
        print(f"{skills_dir} 下没有找到可识别的花叔系 skill。")
        return 0

    icons = {"ok": "✅", "outdated": "⬆️ ", "unknown": "❓"}
    outdated = 0
    for name, status, detail, fix in results:
        print(f"{icons[status]} {name} · {detail}")
        if fix:
            print(f"    更新：{fix}")
        if status == "outdated":
            outdated += 1

    print(f"\n共检查 {len(results)} 个，{outdated} 个有更新。")
    return 1 if outdated else 0


if __name__ == "__main__":
    sys.exit(main())
