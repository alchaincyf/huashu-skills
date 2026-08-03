#!/usr/bin/env python3
"""
Markdown to PDF 转换器 - 苹果设计风格

使用方法:
  python convert.py input.md
  python convert.py input.md -o output.pdf
  python convert.py input.md --title "标题" --author "作者"
"""

import argparse
import markdown2
from weasyprint import HTML, CSS
import re
import os
from pathlib import Path

def extract_metadata(md_content):
    """提取文档元数据"""
    metadata = {
        'title': None,
        'subtitle': None,
        'author': None,
        'date': None,
        'created_for': None,  # 为谁创建
        'based_on': None,     # 基于
    }

    # 尝试提取第一个 h1 作为标题
    h1_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    if h1_match:
        metadata['title'] = h1_match.group(1).strip()

    # 提取 **字段**: 值 格式的元数据
    # 创建者
    creator_match = re.search(r'\*\*创建者\*\*:\s*(.+?)$', md_content, re.MULTILINE)
    if creator_match:
        metadata['author'] = creator_match.group(1).strip()

    # 为谁创建
    for_match = re.search(r'\*\*为谁创建\*\*:\s*(.+?)$', md_content, re.MULTILINE)
    if for_match:
        # 提取链接文本和URL
        link_match = re.search(r'\[(.+?)\]\((.+?)\)', for_match.group(1))
        if link_match:
            metadata['created_for'] = link_match.group(1)
            metadata['created_for_url'] = link_match.group(2)
        else:
            metadata['created_for'] = for_match.group(1).strip()

    # 基于
    based_match = re.search(r'\*\*基于\*\*:\s*(.+?)$', md_content, re.MULTILINE)
    if based_match:
        metadata['based_on'] = based_match.group(1).strip()

    # 最后更新
    date_match = re.search(r'\*\*最后更新\*\*:\s*(.+?)$', md_content, re.MULTILINE)
    if date_match:
        metadata['date'] = date_match.group(1).strip()

    return metadata

def extract_toc_structure(md_content):
    """提取带序号的章节目录"""
    lines = md_content.split('\n')
    toc = []

    for line in lines:
        # 主章节：## 1. 标题
        match_h2 = re.match(r'^## (\d+)\.\s+(.+)$', line)
        if match_h2:
            num = match_h2.group(1)
            title = match_h2.group(2).strip()
            # 移除 emoji
            title = re.sub(r'[\U0001F300-\U0001F9FF]', '', title).strip()
            toc.append({
                'level': 2,
                'number': num,
                'title': title,
                'id': f"{num}-{title}".replace(' ', '-').replace(':', '').lower()
            })

        # 子章节：### 1.1 标题
        match_h3 = re.match(r'^### (\d+\.\d+)\s+(.+)$', line)
        if match_h3:
            num = match_h3.group(1)
            title = match_h3.group(2).strip()
            title = re.sub(r'[\U0001F300-\U0001F9FF]', '', title).strip()
            # 截断过长标题
            if len(title) > 50:
                title = title[:47] + '...'
            toc.append({
                'level': 3,
                'number': num,
                'title': title,
                'id': f"{num}-{title}".replace(' ', '-').replace(':', '').replace('.', '-').lower()
            })

    return toc

def generate_toc_html(toc_items):
    """生成目录 HTML"""
    if not toc_items:
        return ""

    toc_html = ""
    for item in toc_items:
        if item['level'] == 2:
            toc_html += f'''
            <div class="toc-item toc-h2">
                <a href="#{item['id']}" class="toc-link">
                    <span class="toc-number">{item['number']}</span>
                    <span class="toc-title">{item['title']}</span>
                </a>
            </div>
            '''
        else:
            toc_html += f'''
            <div class="toc-item toc-h3">
                <a href="#{item['id']}" class="toc-link">
                    <span class="toc-number">{item['number']}</span>
                    <span class="toc-title">{item['title']}</span>
                </a>
            </div>
            '''

    return toc_html

def create_cover_and_toc(metadata, toc_html):
    """创建封面和目录页"""
    title = metadata.get('title', '文档标题')
    subtitle = metadata.get('subtitle', '')
    author = metadata.get('author', '')
    date = metadata.get('date', '')
    created_for = metadata.get('created_for', '')
    created_for_url = metadata.get('created_for_url', '')
    based_on = metadata.get('based_on', '')

    toc_section = ""
    if toc_html:
        toc_section = f"""
        <!-- 目录 -->
        <div class="toc-page">
            <h2 class="toc-header">目录</h2>
            <div class="toc-content">
                {toc_html}
            </div>
        </div>
        """

    # 构建元信息区域
    meta_items = []
    if subtitle:
        meta_items.append(f'<p class="cover-subtitle">{subtitle}</p>')
    if based_on:
        meta_items.append(f'<p class="cover-based">{based_on}</p>')
    if created_for:
        if created_for_url:
            meta_items.append(f'<p class="cover-for">为 <a href="{created_for_url}">{created_for}</a> 用户创建</p>')
        else:
            meta_items.append(f'<p class="cover-for">为 {created_for} 用户创建</p>')
    if author:
        meta_items.append(f'<p class="cover-author">{author}</p>')
    if date:
        meta_items.append(f'<p class="cover-date">{date}</p>')

    meta_html = '\n'.join(meta_items)

    return f"""
    <!-- 封面 -->
    <div class="apple-cover">
        <div class="cover-main">
            <h1 class="cover-title">{title}</h1>
            <div class="cover-meta">
                {meta_html}
            </div>
        </div>
    </div>

    {toc_section}
    """

def process_markdown(md_content):
    """处理 Markdown 内容"""

    # 移除第一个 h1（已用于封面）
    md_content = re.sub(r'^# .+?\n', '', md_content, count=1, flags=re.MULTILINE)

    # 移除开头的元数据行（**字段**: 值 格式）
    # 这些信息已经提取到封面，不需要在正文中重复显示
    metadata_patterns = [
        r'^\*\*创建者\*\*:.+?$',
        r'^\*\*为谁创建\*\*:.+?$',
        r'^\*\*基于\*\*:.+?$',
        r'^\*\*最后更新\*\*:.+?$',
        r'^\*\*适用场景\*\*:.+?$',
    ]
    for pattern in metadata_patterns:
        md_content = re.sub(pattern, '', md_content, flags=re.MULTILINE)

    # 移除 emoji
    md_content = re.sub(r'[\U0001F300-\U0001F9FF]', '', md_content)

    # 处理 h2 主章节 - 添加 ID 和分页
    def add_h2_id(match):
        num = match.group(1)
        title = match.group(2).strip()
        id_str = f"{num}-{title}".replace(' ', '-').replace(':', '').lower()
        full_title = f"{num}. {title}"
        return f'\n<div class="chapter-break"></div>\n\n<h2 id="{id_str}">{full_title}</h2>\n'

    md_content = re.sub(r'\n## (\d+)\.\s+(.+?)\n', add_h2_id, md_content)

    # 处理 h3 子章节 - 添加 ID
    def add_h3_id(match):
        num = match.group(1)
        title = match.group(2).strip()
        id_str = f"{num}-{title}".replace(' ', '-').replace(':', '').replace('.', '-').lower()
        full_title = f"{num} {title}"
        return f'\n<h3 id="{id_str}">{full_title}</h3>\n'

    md_content = re.sub(r'\n### (\d+\.\d+)\s+(.+?)\n', add_h3_id, md_content)

    # 转换 Markdown
    extras = [
        'fenced-code-blocks',
        'tables',
        'break-on-newline',
        'code-friendly',
        'cuddled-lists',
        'strike',
        'task_list',
    ]

    html = markdown2.markdown(md_content, extras=extras)

    # 修复渲染
    html = re.sub(r'<table>', r'<table class="content-table">', html)
    html = re.sub(r'<pre><code', r'<pre class="code-block"><code', html)
    html = re.sub(r'<blockquote>', r'<blockquote class="quote-block">', html)

    return html

def get_apple_css():
    """获取苹果设计风格 CSS"""
    return """
    @page {
        size: A4;
        margin: 2.5cm 2cm 2cm 2cm;

        @top-left {
            content: string(doc-title);
            font-size: 8.5pt;
            color: #86868b;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }

        @top-right {
            content: counter(page);
            font-size: 8.5pt;
            color: #86868b;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }
    }

    @page:first {
        margin: 0;
        @top-left { content: none; }
        @top-right { content: none; }
    }

    @page:nth(2) {
        @top-left { content: none; }
        @top-right { content: none; }
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif;
        font-size: 11pt;
        line-height: 1.7;
        color: #1d1d1f;
        background: white;
        -webkit-font-smoothing: antialiased;
    }

    /* 封面 */
    .apple-cover {
        height: 100vh;
        background: linear-gradient(135deg, #f5f5f7 0%, #ffffff 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        page-break-after: always;
    }

    .cover-main {
        text-align: center;
        padding: 60px;
    }

    .cover-title {
        font-size: 64pt;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 24px;
        letter-spacing: -2px;
        font-family: -apple-system, 'SF Pro Display', sans-serif;
        string-set: doc-title content();
    }

    .cover-subtitle {
        font-size: 24pt;
        font-weight: 400;
        color: #1d1d1f;
        margin-bottom: 24px;
    }

    .cover-meta {
        font-size: 12pt;
        color: #86868b;
        line-height: 2;
        margin-top: 36px;
    }

    .cover-based {
        font-size: 11pt;
        color: #86868b;
        margin-bottom: 8px;
    }

    .cover-for {
        font-size: 13pt;
        color: #1d1d1f;
        font-weight: 500;
        margin-bottom: 8px;
    }

    .cover-for a {
        color: #06c;
        text-decoration: none;
    }

    .cover-author {
        font-size: 11pt;
        color: #86868b;
        margin-bottom: 8px;
    }

    .cover-date {
        font-size: 11pt;
        color: #86868b;
        font-weight: 500;
    }

    /* 目录 */
    .toc-page {
        padding: 60px 50px;
        page-break-after: always;
        min-height: 100vh;
    }

    .toc-header {
        font-size: 28pt;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 32px;
    }

    .toc-content {
        column-count: 2;
        column-gap: 40px;
    }

    .toc-item {
        break-inside: avoid;
        margin-bottom: 6px;
    }

    .toc-h2 {
        margin-top: 14px;
        margin-bottom: 4px;
    }

    .toc-h2 .toc-link {
        font-size: 11.5pt;
        font-weight: 600;
        color: #1d1d1f;
    }

    .toc-h2 .toc-number {
        color: #06c;
        font-weight: 700;
        margin-right: 8px;
    }

    .toc-h3 {
        margin-left: 16px;
    }

    .toc-h3 .toc-link {
        font-size: 10pt;
        font-weight: 400;
        color: #424245;
    }

    .toc-h3 .toc-number {
        color: #86868b;
        margin-right: 6px;
        font-size: 9.5pt;
    }

    .toc-link {
        display: block;
        text-decoration: none;
        padding: 4px 0;
    }

    .toc-number {
        font-feature-settings: "tnum";
    }

    /* 标题 */
    .chapter-break {
        page-break-before: always;
        height: 0;
    }

    h2 {
        font-size: 22pt;
        font-weight: 600;
        color: #1d1d1f;
        margin-top: 0;
        margin-bottom: 28px;
        padding-bottom: 12px;
        border-bottom: 2px solid #d2d2d7;
        page-break-after: avoid;
    }

    h3 {
        font-size: 17pt;
        font-weight: 600;
        color: #1d1d1f;
        margin-top: 36px;
        margin-bottom: 18px;
        page-break-after: avoid;
    }

    h4 {
        font-size: 13pt;
        font-weight: 600;
        color: #424245;
        margin-top: 24px;
        margin-bottom: 12px;
        page-break-after: avoid;
    }

    /* 正文 */
    p {
        margin-bottom: 16px;
    }

    ul, ol {
        margin-left: 24px;
        margin-bottom: 20px;
    }

    li {
        margin-bottom: 10px;
    }

    /* 代码块 */
    .code-block {
        background: #f5f5f7;
        border: 1px solid #d2d2d7;
        border-radius: 8px;
        padding: 20px;
        margin: 24px 0;
        overflow-x: auto;
        font-family: 'SF Mono', 'Monaco', monospace;
        font-size: 10pt;
        line-height: 1.6;
        page-break-inside: avoid;
    }

    .code-block code {
        background: none;
        padding: 0;
        color: #1d1d1f;
    }

    code {
        background: #f5f5f7;
        padding: 3px 6px;
        border-radius: 4px;
        font-family: 'SF Mono', monospace;
        font-size: 10pt;
        color: #d70050;
        font-weight: 500;
    }

    /* 表格 */
    .content-table {
        width: 100%;
        border-collapse: collapse;
        margin: 28px 0;
        font-size: 10.5pt;
    }

    .content-table thead {
        background: #f5f5f7;
    }

    .content-table th {
        padding: 14px 16px;
        text-align: left;
        font-weight: 600;
        border-bottom: 2px solid #d2d2d7;
    }

    .content-table td {
        padding: 12px 16px;
        border-bottom: 1px solid #d2d2d7;
        color: #424245;
        page-break-inside: avoid;
    }

    /* 引用 */
    .quote-block {
        border-left: 3px solid #06c;
        padding-left: 20px;
        margin: 24px 0;
        color: #424245;
        page-break-inside: avoid;
    }

    /* 图片：不写 max-width 会让宽图横向溢出页面 */
    img {
        max-width: 100%;
        height: auto;
        page-break-inside: avoid;
    }

    /* 强调 */
    strong {
        color: #1d1d1f;
        font-weight: 600;
    }

    a {
        color: #06c;
        text-decoration: none;
    }

    hr {
        border: none;
        border-top: 1px solid #d2d2d7;
        margin: 36px 0;
    }

    /* 印刷质量 */
    p, li, .quote-block {
        orphans: 3;
        widows: 3;
    }

    h2, h3, h4 {
        page-break-after: avoid;
    }

    .code-block, .content-table, .quote-block {
        page-break-inside: avoid;
    }
    """

def warn_missing_images(html, base_dir):
    """检查 HTML 里的本地图片能不能找到，找不到就出声

    weasyprint 解析不到图片时是静默跳过的，PDF 照样生成、只是图没了。
    这里提前扫一遍，让失败可见。
    """
    import html as html_mod
    from urllib.parse import unquote, urlparse

    missing = []
    # 单引号和双引号都要收：markdown2 会把手写的 <img src='...'> 原样透传，
    # 只认双引号会漏掉它们——漏报比误报更糟，那正是这个函数要消灭的静默。
    for src_raw in re.findall(r'<img[^>]+\bsrc=(?:"([^"]*)"|\'([^\']*)\')', html):
        src = src_raw[0] or src_raw[1]
        # HTML 实体要先还原再查文件：weasyprint 拿到的是解码后的路径，
        # 不解码会把 a&amp;b.png 这种真实存在的文件误报成缺失。
        src = html_mod.unescape(src)
        parsed = urlparse(src)
        if parsed.scheme in ('http', 'https', 'data'):
            continue
        path = unquote(parsed.path)
        candidate = Path(path) if parsed.scheme == 'file' else base_dir / path
        if not candidate.exists():
            missing.append(src)

    if missing:
        print(f"⚠️  有 {len(missing)} 张图片找不到，PDF 里会缺失：")
        for src in missing:
            print(f"     - {src}")
        print(f"   （相对路径是相对于 {base_dir} 解析的）")


def convert_markdown_to_pdf(input_file, output_file=None, title=None, author=None,
                            subtitle=None):
    """主转换函数"""

    # 读取输入文件
    print(f"📖 读取文件: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 提取元数据
    print("📑 提取元数据...")
    metadata = extract_metadata(md_content)

    # 命令行参数覆盖
    if title:
        metadata['title'] = title
    if author:
        metadata['author'] = author
    if subtitle:
        metadata['subtitle'] = subtitle

    # 提取目录
    print("📂 提取目录结构...")
    toc_structure = extract_toc_structure(md_content)
    print(f"   ✓ 找到 {len([t for t in toc_structure if t['level'] == 2])} 个主章节")
    print(f"   ✓ 找到 {len([t for t in toc_structure if t['level'] == 3])} 个子章节")

    # 生成目录 HTML
    toc_html = generate_toc_html(toc_structure)

    # 处理 Markdown
    print("🎨 处理 Markdown 内容...")
    html_content = process_markdown(md_content)

    # 生成完整 HTML
    print("📄 生成 HTML...")
    full_html = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>{metadata.get('title', '文档')}</title>
    </head>
    <body>
        {create_cover_and_toc(metadata, toc_html)}
        <div class="content">
            {html_content}
        </div>
    </body>
    </html>
    """

    # 生成 PDF
    print("📝 生成 PDF...")
    if not output_file:
        output_file = str(Path(input_file).with_suffix('.pdf'))

    # base_url 必须给：不给的话 markdown 里的相对路径图片（含中文目录名）
    # 一张都解析不到，weasyprint 还不报错，PDF 静默少图。
    # 用输入文件自身的 file:// URI，相对路径就从它所在目录开始算。
    source_path = Path(input_file).resolve()
    base_url = source_path.as_uri()
    warn_missing_images(full_html, source_path.parent)

    css = CSS(string=get_apple_css())
    HTML(string=full_html, base_url=base_url).write_pdf(output_file, stylesheets=[css])

    print(f"✅ 成功生成: {output_file}")

    # 显示文件大小
    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"📊 文件大小: {size_mb:.1f} MB")

def main():
    parser = argparse.ArgumentParser(
        description='将 Markdown 转换为苹果设计风格的 PDF 白皮书'
    )
    parser.add_argument('input', help='输入的 Markdown 文件')
    parser.add_argument('-o', '--output', help='输出的 PDF 文件（默认：与输入文件同名）')
    parser.add_argument('--title', help='自定义文档标题')
    parser.add_argument('--subtitle', help='自定义副标题')
    parser.add_argument('--author', help='自定义作者')

    args = parser.parse_args()

    try:
        convert_markdown_to_pdf(
            args.input,
            args.output,
            args.title,
            args.author,
            args.subtitle
        )
    except Exception as e:
        print(f"❌ 转换失败: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == '__main__':
    exit(main())
