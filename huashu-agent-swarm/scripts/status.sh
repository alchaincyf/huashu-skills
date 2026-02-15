#!/bin/bash
# status.sh - 查看蜂群状态
# 用法: bash status.sh [项目目录]

PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"
SESSION="swarm-${PROJECT_NAME}"

echo "=== 蜂群状态: $PROJECT_NAME ==="
echo ""

# ===== tmux状态 =====
echo "--- tmux session ---"
if tmux has-session -t "$SESSION" 2>/dev/null; then
    PANE_COUNT=$(tmux list-panes -t "$SESSION" 2>/dev/null | wc -l | tr -d ' ')
    echo "运行中: $SESSION ($PANE_COUNT 个agent)"
else
    echo "未运行"
fi
echo ""

# ===== worktree状态 =====
echo "--- Worktrees ---"
WORKTREE_COUNT=0
for dir in "${PROJECT_DIR}"-agent-*; do
    if [ -d "$dir" ]; then
        WORKTREE_COUNT=$((WORKTREE_COUNT + 1))
        AGENT_NUM=$(echo "$dir" | grep -o '[0-9]*$')
        LAST_COMMIT=$(git -C "$dir" log --oneline -1 2>/dev/null || echo "无提交")
        echo "  Agent-${AGENT_NUM}: $LAST_COMMIT"
    fi
done
[ "$WORKTREE_COUNT" -eq 0 ] && echo "  无（蜂群未启动或已清理）"
echo ""

# ===== 当前任务认领 =====
echo "--- 当前任务认领 ---"
LOCK_COUNT=0
for lock in "$PROJECT_DIR/current_tasks/"*.lock; do
    [ -f "$lock" ] || continue
    LOCK_COUNT=$((LOCK_COUNT + 1))
    TASK_NAME=$(basename "$lock" .lock)
    OWNER=$(cat "$lock" 2>/dev/null || echo "unknown")
    echo "  $TASK_NAME → $OWNER"
done
[ "$LOCK_COUNT" -eq 0 ] && echo "  无（没有进行中的任务）"
echo ""

# ===== 最近提交 =====
echo "--- 最近20条提交 ---"
git -C "$PROJECT_DIR" log --oneline --all -20 2>/dev/null || echo "  无提交记录"
echo ""

# ===== TASKS.md概要 =====
echo "--- 任务清单 (TASKS.md) ---"
if [ -f "$PROJECT_DIR/TASKS.md" ]; then
    # 统计任务状态
    TOTAL=$(grep -c '^\- \[' "$PROJECT_DIR/TASKS.md" 2>/dev/null || echo "0")
    DONE=$(grep -c '^\- \[x\]' "$PROJECT_DIR/TASKS.md" 2>/dev/null || echo "0")
    IN_PROGRESS=$(grep -c '^\- \[\~\]' "$PROJECT_DIR/TASKS.md" 2>/dev/null || echo "0")
    TODO=$((TOTAL - DONE - IN_PROGRESS))
    echo "  总计: $TOTAL | 完成: $DONE | 进行中: $IN_PROGRESS | 待做: $TODO"
    echo ""
    cat "$PROJECT_DIR/TASKS.md"
else
    echo "  TASKS.md 不存在"
fi
echo ""

# ===== 日志摘要 =====
echo "--- 最近日志 ---"
if [ -d "$PROJECT_DIR/agent_logs" ]; then
    LATEST_LOG=$(ls -t "$PROJECT_DIR/agent_logs/"*.log 2>/dev/null | head -1)
    if [ -n "$LATEST_LOG" ]; then
        LOG_COUNT=$(ls "$PROJECT_DIR/agent_logs/"*.log 2>/dev/null | wc -l | tr -d ' ')
        echo "  共 $LOG_COUNT 个日志文件"
        echo "  最新: $(basename "$LATEST_LOG")"
        echo "  最后几行:"
        tail -5 "$LATEST_LOG" 2>/dev/null | sed 's/^/    /'
    else
        echo "  暂无日志"
    fi
else
    echo "  日志目录不存在"
fi
