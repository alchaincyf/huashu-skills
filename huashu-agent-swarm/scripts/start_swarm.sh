#!/bin/bash
# start_swarm.sh - 启动Agent蜂群（tmux多pane）
# 用法: bash start_swarm.sh [agent数量] [项目目录]
# 示例: bash start_swarm.sh 8 /path/to/project

set -e

NUM_AGENTS="${1:-8}"
PROJECT_DIR="${2:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"
SESSION="swarm-${PROJECT_NAME}"
LOG_DIR="${PROJECT_DIR}/agent_logs"

# ===== 前置检查 =====

if ! command -v tmux >/dev/null 2>&1; then
    echo "错误: 请先安装tmux"
    echo "  macOS: brew install tmux"
    echo "  Ubuntu: sudo apt install tmux"
    exit 1
fi

if ! command -v claude >/dev/null 2>&1; then
    echo "错误: 请先安装 claude CLI"
    exit 1
fi

if [ ! -f "$PROJECT_DIR/AGENT_PROMPT.md" ]; then
    echo "错误: 找不到 AGENT_PROMPT.md"
    echo "请先运行: bash $SKILL_DIR/scripts/setup_project.sh $PROJECT_DIR"
    exit 1
fi

if [ ! -d "$PROJECT_DIR/.git" ]; then
    echo "错误: $PROJECT_DIR 不是git仓库"
    exit 1
fi

echo "=== 启动蜂群模式 ==="
echo "项目: $PROJECT_DIR"
echo "Agent数量: $NUM_AGENTS"
echo "tmux session: $SESSION"
echo ""

# ===== 创建日志目录 =====
mkdir -p "$LOG_DIR"

# ===== 确保main分支存在且有至少一个commit =====
cd "$PROJECT_DIR"
MAIN_BRANCH=$(git branch --show-current)

# ===== 创建 git worktrees =====
echo "创建 git worktrees..."
for i in $(seq 1 "$NUM_AGENTS"); do
    AGENT_DIR="${PROJECT_DIR}-agent-${i}"
    BRANCH_NAME="agent-${i}-work"

    if [ -d "$AGENT_DIR" ]; then
        echo "  Agent-${i}: worktree已存在，跳过"
    else
        # 创建agent专用分支的worktree
        git worktree add "$AGENT_DIR" -b "$BRANCH_NAME" "$MAIN_BRANCH" 2>/dev/null || \
        git worktree add "$AGENT_DIR" "$BRANCH_NAME" 2>/dev/null || {
            echo "  Agent-${i}: 创建worktree失败，尝试清理后重试..."
            git worktree prune
            git branch -D "$BRANCH_NAME" 2>/dev/null || true
            git worktree add "$AGENT_DIR" -b "$BRANCH_NAME" "$MAIN_BRANCH"
        }
        echo "  Agent-${i}: worktree 创建完成 → $AGENT_DIR"
    fi

    # 同步AGENT_PROMPT.md和TASKS.md到worktree
    cp "$PROJECT_DIR/AGENT_PROMPT.md" "$AGENT_DIR/AGENT_PROMPT.md"
    [ -f "$PROJECT_DIR/TASKS.md" ] && cp "$PROJECT_DIR/TASKS.md" "$AGENT_DIR/TASKS.md"
done

echo ""

# ===== 创建tmux session =====
echo "创建 tmux session..."
tmux kill-session -t "$SESSION" 2>/dev/null || true

# 创建session并启动第一个agent
AGENT_DIR="${PROJECT_DIR}-agent-1"
tmux new-session -d -s "$SESSION" -x 200 -y 50 \
    "AGENT_ID=1 WORK_DIR='$AGENT_DIR' LOG_DIR='$LOG_DIR' bash '$SKILL_DIR/scripts/agent_loop.sh'; read"

# 为后续agent创建新pane
for i in $(seq 2 "$NUM_AGENTS"); do
    AGENT_DIR="${PROJECT_DIR}-agent-${i}"
    tmux split-window -t "$SESSION" \
        "AGENT_ID=$i WORK_DIR='$AGENT_DIR' LOG_DIR='$LOG_DIR' bash '$SKILL_DIR/scripts/agent_loop.sh'; read"
    # 重新排列布局
    tmux select-layout -t "$SESSION" tiled
done

echo ""
echo "=== 蜂群已启动！==="
echo ""
echo "查看agent工作:"
echo "  tmux attach -t $SESSION"
echo ""
echo "查看状态:"
echo "  bash $SKILL_DIR/scripts/status.sh $PROJECT_DIR"
echo ""
echo "停止所有agent:"
echo "  bash $SKILL_DIR/scripts/stop_swarm.sh $PROJECT_DIR"
echo ""

# 自动attach到tmux session
tmux attach -t "$SESSION"
