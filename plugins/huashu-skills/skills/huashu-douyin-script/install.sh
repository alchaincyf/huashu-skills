#!/bin/bash
# douyin-viral-script skill 安装脚本
# 用法：bash <(curl -fsSL https://raw.githubusercontent.com/alchaincyf/Write-Prompt/master/.claude/skills/douyin-viral-script/install.sh)

set -e

SKILL_NAME="douyin-viral-script"
REPO="alchaincyf/Write-Prompt"
BRANCH="master"
SRC_PATH=".claude/skills/$SKILL_NAME"
TARGET_DIR="$HOME/.claude/skills/$SKILL_NAME"

echo "📦 安装 $SKILL_NAME skill..."
echo ""

# 检查依赖
check_dep() {
    if ! command -v "$1" &>/dev/null; then
        echo "❌ 需要 $1，请先安装：$2"
        exit 1
    fi
}

check_dep git "https://git-scm.com"
check_dep uv "curl -LsSf https://astral.sh/uv/install.sh | sh"

if ! command -v yt-dlp &>/dev/null; then
    echo "⚠️  未检测到 yt-dlp（下载抖音视频需要）"
    echo "   安装方式：brew install yt-dlp 或 pip install yt-dlp"
    echo ""
fi

# 创建目标目录
mkdir -p "$TARGET_DIR"

# 用临时目录做 sparse checkout
TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

echo "⬇️  从 GitHub 下载 skill 文件..."
cd "$TMPDIR"
git init -q
git remote add origin "https://github.com/$REPO.git"
git config core.sparseCheckout true
echo "$SRC_PATH/" > .git/info/sparse-checkout
git pull -q origin "$BRANCH" --depth=1

# 复制到目标位置
if [ -d "$TMPDIR/$SRC_PATH" ]; then
    cp -R "$TMPDIR/$SRC_PATH/"* "$TARGET_DIR/"
    echo ""
    echo "✅ 安装成功！"
    echo ""
    echo "📁 安装位置：$TARGET_DIR"
    echo ""
    echo "📋 文件清单："
    find "$TARGET_DIR" -type f | while read f; do
        echo "   $(echo "$f" | sed "s|$TARGET_DIR/||")"
    done
    echo ""
    echo "🔧 使用前请确保："
    echo "   1. 设置 GEMINI_API_KEY 环境变量（用于视频分析）"
    echo "   2. Chrome 浏览器已登录抖音（用于视频下载）"
    echo ""
    echo "🚀 在 Claude Code 中输入 /douyin-viral-script 即可使用"
else
    echo "❌ 下载失败，请检查网络连接"
    exit 1
fi
