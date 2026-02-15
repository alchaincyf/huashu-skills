#!/bin/bash
# setup_project.sh - 初始化项目结构，为蜂群模式做准备
# 用法: bash setup_project.sh <项目目录>

set -e

PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== 初始化蜂群项目: $PROJECT_DIR ==="

# 检查是否是git仓库
if [ ! -d "$PROJECT_DIR/.git" ]; then
    echo "初始化git仓库..."
    git -C "$PROJECT_DIR" init
    git -C "$PROJECT_DIR" add -A
    git -C "$PROJECT_DIR" commit -m "Initial commit" --allow-empty
fi

# 确保有main分支
CURRENT_BRANCH=$(git -C "$PROJECT_DIR" branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    # 检查是否存在main分支
    if git -C "$PROJECT_DIR" show-ref --verify --quiet refs/heads/main 2>/dev/null; then
        echo "注意: 当前在 $CURRENT_BRANCH 分支，main分支已存在"
    else
        echo "创建main分支..."
        git -C "$PROJECT_DIR" branch -M main
    fi
fi

# 创建目录结构
mkdir -p "$PROJECT_DIR/current_tasks"
mkdir -p "$PROJECT_DIR/agent_logs"

# 创建.gitkeep
touch "$PROJECT_DIR/current_tasks/.gitkeep"

# agent_logs加入gitignore
if [ ! -f "$PROJECT_DIR/.gitignore" ]; then
    echo "agent_logs/" > "$PROJECT_DIR/.gitignore"
else
    if ! grep -q "agent_logs/" "$PROJECT_DIR/.gitignore" 2>/dev/null; then
        echo "agent_logs/" >> "$PROJECT_DIR/.gitignore"
    fi
fi

# 复制AGENT_PROMPT模板（如果不存在）
if [ ! -f "$PROJECT_DIR/AGENT_PROMPT.md" ]; then
    cp "$SKILL_DIR/references/agent-prompt-template.md" "$PROJECT_DIR/AGENT_PROMPT.md"
    echo "已创建 AGENT_PROMPT.md（模板），请根据项目需求定制内容"
fi

# 创建HUMAN_INPUT.md（人类指令通道）
if [ ! -f "$PROJECT_DIR/HUMAN_INPUT.md" ]; then
    touch "$PROJECT_DIR/HUMAN_INPUT.md"
    echo "已创建 HUMAN_INPUT.md（人类指令通道）"
fi

# 创建初始TASKS.md（如果不存在）
if [ ! -f "$PROJECT_DIR/TASKS.md" ]; then
    cat > "$PROJECT_DIR/TASKS.md" << 'EOF'
# 任务清单

## 状态说明
- [ ] 待完成
- [x] 已完成
- [~] 进行中（查看 current_tasks/ 目录确认谁在做）

## 任务列表

<!-- Agent会自行维护这个列表 -->
<!-- 在这里添加初始任务 -->

EOF
    echo "已创建 TASKS.md，请添加初始任务"
fi

# 提交初始结构
cd "$PROJECT_DIR"
git add -A
git diff --cached --quiet || git commit -m "Setup swarm project structure

- Added current_tasks/ for task claiming
- Added agent_logs/ (gitignored)
- Added AGENT_PROMPT.md template
- Added TASKS.md"

echo ""
echo "=== 初始化完成 ==="
echo ""
echo "下一步:"
echo "1. 编辑 AGENT_PROMPT.md - 填入项目目标、代码规范、测试命令"
echo "2. 编辑 TASKS.md - 添加初始任务"
echo "3. 运行 start_swarm.sh 启动蜂群"
