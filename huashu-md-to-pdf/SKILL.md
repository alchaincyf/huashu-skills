---
name: huashu-md-to-pdf
description: |
  将 Markdown 文档转换为专业的 PDF 白皮书，采用苹果设计风格。
  支持完整的 Markdown 语法（代码块、表格、引用、列表等）。
  自动生成封面、目录、页眉页脚。
  使用场景：技术文档、白皮书、教程、报告等需要专业排版的 Markdown 文档。
---

# Markdown to PDF Skill

将 Markdown 文档转换为专业的苹果设计风格 PDF 白皮书。

## 核心功能

1. **专业排版**：书籍级排版质量，自动处理分页、孤行寡行
2. **苹果设计**：SF 字体系统、现代简洁风格、专业配色
3. **完整目录**：自动提取章节结构，双列布局，可点击跳转
4. **Markdown 完美支持**：代码块、表格、引用、列表等全部正确渲染

## 使用方法

### 基础用法

```bash
# 转换单个文件
python scripts/convert.py input.md

# 指定输出文件名
python scripts/convert.py input.md -o "我的白皮书.pdf"

# 自定义标题和作者
python scripts/convert.py input.md --title "技术白皮书" --author "花叔"
```

### 图片路径

Markdown 里的相对路径图片，是**相对 md 文件自身所在目录**解析的，目录名和文件名带中文都可以：

```markdown
![示意图](图片/架构图.png)     ← 和 md 文件同级的「图片」目录
![示意图](./assets/arch.png)
```

找不到的图片会在转换时打印警告并列出路径。以前这种情况是静默跳过的，PDF 照样生成、只是没有图。

### 已知未解决：某些环境下 macOS「预览」打开是乱码

有用户报告生成的 PDF 在 macOS「预览」里是乱码，浏览器打开正常。**这个问题还没有解决办法**，原因也还没定位——在一台用 Arial Unicode MS 渲染中文的机器上复现不出来，而报告者的字体环境和 weasyprint 版本都不清楚。

**不要试图用 weasyprint 的 `full_fonts=True` 绕过它。** 实测：macOS 上的中文字体（PingFang.ttc、Songti.ttc、Hiragino Sans GB.ttc）都是 TrueType Collection，`full_fonts=True` 会把整个 collection 的原始字节塞进 PDF 的 `/FontFile2`（magic 是 `ttcf` 而不是合法的 `\x00\x01\x00\x00`），结果是**文件暴涨到几十 MB，而且照样乱码**——实测一段中文从 10 KB 变成 43 MB，渲染出来是「Oě 据⊤」。它让问题更糟，不是逃生出口。

碰到乱码时可以先试：升级 weasyprint、或在 CSS 里换一个非 collection 的字体。

### Markdown 文档要求

你的 Markdown 文档应该遵循以下结构：

```markdown
# 文档标题

## 1. 第一章
### 1.1 第一节
### 1.2 第二节

## 2. 第二章
### 2.1 第一节
```

**关键规则**：
- 主章节：`## 1. 标题`（数字 + 点 + 空格 + 标题）
- 子章节：`### 1.1 标题`（数字.数字 + 空格 + 标题）
- 这样才能正确提取目录

## 设计特点

### 封面设计
- 淡灰色渐变背景
- 大标题：64pt，简洁现代
- 副标题和元信息

### 目录设计
- 双列布局，单页展示
- 主章节粗体，子章节缩进
- 可点击跳转到对应章节

### 正文排版
- SF 字体系列（苹果设计语言）
- 行高 1.7，舒适阅读
- 章节自动分页
- 孤行寡行控制

### 代码块
- 浅灰背景 + 细边框
- 圆角 8px
- SF Mono 等宽字体
- 自动避免分页

### 表格
- 清晰网格线
- 浅灰表头
- 自动保留表头（长表格分页时）

## 配置选项

如果需要自定义样式，可以修改 `scripts/convert.py` 中的 CSS 变量：

```python
# 主色调
PRIMARY_COLOR = '#06c'      # 苹果蓝
TEXT_COLOR = '#1d1d1f'      # 主文本黑色
GRAY_COLOR = '#86868b'      # 浅灰色

# 字体大小
COVER_TITLE_SIZE = '64pt'
H2_SIZE = '22pt'
H3_SIZE = '17pt'
BODY_SIZE = '11pt'
```

## 常见问题

### Q: 目录为什么是空的？
A: 确保你的 Markdown 使用了正确的章节格式：
- `## 1. 标题` 而不是 `## 标题`
- `### 1.1 标题` 而不是 `### 标题`

### Q: 代码块显示不正确？
A: 确保使用三个反引号包裹：
````markdown
```python
def hello():
    print("Hello")
```
````

### Q: 表格格式乱了？
A: 使用标准的 Markdown 表格语法：
```markdown
| 列1 | 列2 |
|-----|-----|
| 值1 | 值2 |
```

### Q: 如何修改字体？
A: 编辑 `scripts/convert.py` 中的 CSS，修改 `font-family` 属性。

### Q: 生成的 PDF 太大？
A: 检查是否有大量图片，考虑压缩图片或使用外链。

## 依赖安装

首次使用需要安装 Python 依赖：

```bash
pip3 install markdown2 weasyprint
```

如果遇到 WeasyPrint 安装问题（macOS）：
```bash
brew install pango
pip3 install weasyprint
```

## 示例

### 生成技术文档
```bash
python scripts/convert.py tech-guide.md -o "技术指南.pdf"
```

### 生成白皮书
```bash
python scripts/convert.py whitepaper.md --title "产品白皮书" --author "团队"
```

## 脚本说明

- `scripts/convert.py` - 主转换脚本
- `scripts/styles.css` - CSS 样式定义（已嵌入脚本）
- `templates/cover.html` - 封面模板（已嵌入脚本）

## 技术实现

本 Skill 使用：
- **markdown2**：Markdown 解析（支持扩展语法）
- **WeasyPrint**：HTML to PDF 转换（支持 CSS3）
- **苹果设计系统**：SF 字体、专业配色、现代排版

## 更新日志

### v1.0 (2025-12-24)
- 初始版本
- 支持完整 Markdown 语法
- 苹果设计风格
- 自动目录生成
- 书籍级排版质量

---

> **花叔出品** | AI Native Coder · 独立开发者
> 公众号「花叔」| 30万+粉丝 | AI工具与效率提升
> 代表作：小猫补光灯（AppStore付费榜Top1）·《一本书玩转DeepSeek》
