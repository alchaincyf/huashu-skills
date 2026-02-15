#!/bin/bash
# send_input.sh - 向蜂群发送人类指令
# 用法: bash send_input.sh <项目目录> "你的指令"
# 示例: bash send_input.sh /path/to/project "停止重构，优先修复登录bug"

PROJECT_DIR="${1:-.}"
PROJECT_DIR="$(cd "$PROJECT_DIR" && pwd)"
MESSAGE="$2"

if [ -z "$MESSAGE" ]; then
    echo "用法: bash send_input.sh <项目目录> \"你的指令\""
    echo ""
    echo "示例:"
    echo "  bash send_input.sh . \"优先修复登录页面的bug\""
    echo "  bash send_input.sh . \"不要动 config/ 目录下的文件\""
    echo "  bash send_input.sh . \"所有agent停止当前工作，先跑一遍完整测试\""
    exit 1
fi

# 写入指令
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
cat > "$PROJECT_DIR/HUMAN_INPUT.md" << EOF
# 人类指令 - ${TIMESTAMP}

${MESSAGE}
EOF

# 提交并推送
cd "$PROJECT_DIR"
git add HUMAN_INPUT.md
git commit -m "HUMAN: ${MESSAGE:0:50}" 2>/dev/null
git push origin main 2>/dev/null || true

echo "指令已发送: $MESSAGE"
echo "下一个启动session的agent会优先执行此指令"
