#!/bin/bash
# stop_swarm.sh - 停止所有Agent并清理worktrees
# 用法: bash stop_swarm.sh [项目目录]

PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"
SESSION="swarm-${PROJECT_NAME}"

echo "=== 停止蜂群: $SESSION ==="

# ===== 停止tmux session =====
if tmux has-session -t "$SESSION" 2>/dev/null; then
    tmux kill-session -t "$SESSION"
    echo "tmux session 已停止"
else
    echo "tmux session 不存在（可能已停止）"
fi

# ===== 合并agent分支的成果到main =====
echo ""
echo "检查agent分支的未合并提交..."
cd "$PROJECT_DIR"
MAIN_BRANCH=$(git branch --show-current 2>/dev/null || echo "main")

for dir in "${PROJECT_DIR}"-agent-*; do
    [ -d "$dir" ] || continue
    AGENT_NUM=$(echo "$dir" | grep -o '[0-9]*$')
    BRANCH_NAME="agent-${AGENT_NUM}-work"

    # 检查分支是否有未合并的提交
    AHEAD=$(git log "${MAIN_BRANCH}..${BRANCH_NAME}" --oneline 2>/dev/null | wc -l | tr -d ' ')
    if [ "$AHEAD" -gt 0 ]; then
        echo "  Agent-${AGENT_NUM}: 有 ${AHEAD} 个未合并提交"
        echo "  合并 ${BRANCH_NAME} → ${MAIN_BRANCH}..."
        git merge "$BRANCH_NAME" --no-edit 2>/dev/null || {
            echo "  警告: 合并冲突，请手动解决"
            echo "  运行: git merge $BRANCH_NAME"
        }
    fi
done

# ===== 清理worktrees =====
echo ""
echo "清理 worktrees..."
for dir in "${PROJECT_DIR}"-agent-*; do
    if [ -d "$dir" ]; then
        AGENT_NUM=$(echo "$dir" | grep -o '[0-9]*$')
        git -C "$PROJECT_DIR" worktree remove "$dir" --force 2>/dev/null || {
            echo "  警告: 无法清理 $dir，尝试强制删除..."
            rm -rf "$dir"
            git -C "$PROJECT_DIR" worktree prune
        }
        echo "  Agent-${AGENT_NUM}: worktree 已清理"

        # 删除agent分支
        BRANCH_NAME="agent-${AGENT_NUM}-work"
        git -C "$PROJECT_DIR" branch -D "$BRANCH_NAME" 2>/dev/null || true
    fi
done

git -C "$PROJECT_DIR" worktree prune 2>/dev/null

# ===== 清理lock文件 =====
echo ""
echo "清理 lock 文件..."
rm -f "$PROJECT_DIR/current_tasks/"*.lock 2>/dev/null
echo "lock 文件已清理"

echo ""
echo "=== 蜂群已完全停止 ==="
echo ""
echo "查看成果:"
echo "  git -C $PROJECT_DIR log --oneline -20"
echo ""
echo "日志在: $PROJECT_DIR/agent_logs/"
