# Markdown to PDF Skill

将 Markdown 文档转换为专业的苹果设计风格 PDF 白皮书。

## 快速开始

### 1. 安装依赖（仅首次）

```bash
pip3 install markdown2 weasyprint
```

### 2. 基础使用

```bash
# 转换 Markdown 文件
python .claude/skills/markdown-to-pdf/scripts/convert.py your-file.md

# 指定输出文件名
python .claude/skills/markdown-to-pdf/scripts/convert.py your-file.md -o "我的白皮书.pdf"

# 自定义标题和作者
python .claude/skills/markdown-to-pdf/scripts/convert.py your-file.md --title "技术白皮书" --author "花叔"
```

## Markdown 格式要求

你的文档应该使用带序号的章节格式：

```markdown
# 文档标题

## 1. 第一章
### 1.1 第一节
内容...

### 1.2 第二节
内容...

## 2. 第二章
### 2.1 第一节
...
```

**关键点**：
- ✅ `## 1. 标题` - 正确（数字.空格标题）
- ❌ `## 标题` - 错误（无序号）
- ✅ `### 1.1 标题` - 正确
- ❌ `### 标题` - 错误

## 设计特点

- 📖 **书籍级排版**：自动分页、孤行寡行控制
- 🎨 **苹果设计语言**：SF 字体、现代简洁
- 📑 **自动目录**：双列布局、可点击跳转
- 💻 **完美代码块**：语法高亮、圆角边框
- 📊 **专业表格**：清晰网格、自动表头

## 文件结构

```
.claude/skills/markdown-to-pdf/
├── SKILL.md              # Skill 说明文档
├── README.md             # 本文件
└── scripts/
    └── convert.py        # 转换脚本
```

## 示例

在 Claude Code 中使用：

```
用户：帮我把这个 Markdown 文档转成 PDF
Claude：好的，我使用 markdown-to-pdf skill 来转换
       [执行] python .claude/skills/markdown-to-pdf/scripts/convert.py document.md
       ✅ 已生成 document.pdf
```

## 常见问题

**Q: WeasyPrint 安装失败？**
```bash
# macOS
brew install pango
pip3 install weasyprint

# Linux
sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0
pip3 install weasyprint
```

**Q: 目录为空？**
确保使用 `## 1.` 和 `### 1.1` 格式。

**Q: 代码块显示不正确？**
使用三个反引号包裹代码。

## 更新日志

- **v1.0** (2025-12-24): 初始版本
