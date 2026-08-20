#!/bin/bash
# agent_loop.sh - 单个Agent的无限循环逻辑
# 环境变量: AGENT_ID, WORK_DIR, LOG_DIR
# 用法: AGENT_ID=1 WORK_DIR=/path/to/worktree LOG_DIR=/path/to/logs bash agent_loop.sh

set -e

AGENT_ID="${AGENT_ID:-1}"
WORK_DIR="${WORK_DIR:-.}"
LOG_DIR="${LOG_DIR:-./agent_logs}"
SLEEP_INTERVAL="${SLEEP_INTERVAL:-5}"
MODEL="${MODEL:-claude-opus-4-6}"
MAX_SESSIONS="${MAX_SESSIONS:-0}"  # 0=无限

mkdir -p "$LOG_DIR"

SESSION_COUNT=0

echo "[Agent-${AGENT_ID}] 启动，工作目录: $WORK_DIR"
echo "[Agent-${AGENT_ID}] 模型: $MODEL, 休息间隔: ${SLEEP_INTERVAL}s"

while true; do
    SESSION_COUNT=$((SESSION_COUNT + 1))

    # 检查最大session限制
    if [ "$MAX_SESSIONS" -gt 0 ] && [ "$SESSION_COUNT" -gt "$MAX_SESSIONS" ]; then
        echo "[Agent-${AGENT_ID}] 已达到最大session数 ($MAX_SESSIONS)，退出"
        break
    fi

    echo ""
    echo "================================================"
    echo "[Agent-${AGENT_ID}] Session #${SESSION_COUNT} 开始 - $(date '+%Y-%m-%d %H:%M:%S')"
    echo "================================================"

    cd "$WORK_DIR"

    # 同步最新代码
    echo "[Agent-${AGENT_ID}] 同步最新代码..."
    git pull --rebase origin main 2>/dev/null || true

    COMMIT=$(git rev-parse --short=6 HEAD 2>/dev/null || echo "unknown")
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    LOGFILE="${LOG_DIR}/agent_${AGENT_ID}_session_${SESSION_COUNT}_${TIMESTAMP}.log"

    echo "[Agent-${AGENT_ID}] 当前HEAD: $COMMIT"
    echo "[Agent-${AGENT_ID}] 日志: $LOGFILE"

    # 启动Claude会话
    echo "[Agent-${AGENT_ID}] 启动Claude会话..."
    claude --dangerously-skip-permissions \
           -p "$(cat AGENT_PROMPT.md)

你是 Agent-${AGENT_ID}，这是你的第 ${SESSION_COUNT} 个session。
当前时间: $(date '+%Y-%m-%d %H:%M:%S')
当前HEAD: ${COMMIT}

请按照 AGENT_PROMPT.md 的工作流程执行任务。" \
           --model "$MODEL" \
           2>&1 | tee "$LOGFILE"

    EXIT_CODE=${PIPESTATUS[0]}
    echo "[Agent-${AGENT_ID}] Claude退出，状态码: $EXIT_CODE"

    # 推送成果（如果有新commit）
    NEW_COMMIT=$(git rev-parse --short=6 HEAD 2>/dev/null || echo "unknown")
    if [ "$NEW_COMMIT" != "$COMMIT" ]; then
        echo "[Agent-${AGENT_ID}] 有新提交，推送中..."
        git push origin HEAD:main 2>/dev/null || {
            echo "[Agent-${AGENT_ID}] 推送失败，尝试rebase后重推..."
            git fetch origin main 2>/dev/null && git rebase origin/main 2>/dev/null || true
            git push origin HEAD:main 2>/dev/null || echo "[Agent-${AGENT_ID}] 推送仍失败，跳过"
        }
    else
        echo "[Agent-${AGENT_ID}] 无新提交"
    fi

    # 休息，避免API限流
    echo "[Agent-${AGENT_ID}] 休息 ${SLEEP_INTERVAL}s..."
    sleep "$SLEEP_INTERVAL"
done

echo "[Agent-${AGENT_ID}] 循环结束"
