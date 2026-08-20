#!/usr/bin/env bash
# Copy each root skill directory into plugins/huashu-skills/skills/<name>/ as regular files.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/plugins/huashu-skills/skills"
CHECK=0
[ "${1:-}" = "--check" ] && CHECK=1

stage() {
  local dest="$1"
  rm -rf "$dest"
  mkdir -p "$dest"
  local d
  for d in "$ROOT"/huashu-*; do
    [ -d "$d" ] || continue
    [ -f "$d/SKILL.md" ] || continue
    rsync -a --copy-links --exclude node_modules --exclude __pycache__ --exclude .DS_Store \
      "$d/" "$dest/$(basename "$d")/"
  done
  mkdir -p "$dest/huashu-slides/agents"
  cp "$ROOT/plugins/huashu-skills/.codex-plugin/openai.yaml" "$dest/huashu-slides/agents/openai.yaml"
  if find "$dest" -type l | grep -q .; then
    echo "error: symlinks in plugin leaf" >&2
    find "$dest" -type l >&2
    exit 1
  fi
}

if [ "$CHECK" = 1 ]; then
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' EXIT
  stage "$tmp/skills"
  if [ ! -d "$DEST" ]; then
    echo "plugin leaf missing — run scripts/build-plugin-leaf.sh" >&2
    exit 1
  fi
  if ! diff -rq "$tmp/skills" "$DEST" >/dev/null; then
    echo "plugin leaf is stale — run scripts/build-plugin-leaf.sh" >&2
    diff -rq "$tmp/skills" "$DEST" || true
    exit 1
  fi
  echo "plugin leaf is fresh"
else
  stage "$DEST"
  echo "wrote $DEST ($(find "$DEST" -mindepth 1 -maxdepth 1 -type d | wc -l) skills)"
fi
