# 详细工作流参考

> SKILL.md 的执行层。按需查阅，不必全读。

## 数据分析工作流

### Step 1: 读取数据

```python
# Excel（推荐pandas）
import pandas as pd
df = pd.read_excel('数据.xlsx', sheet_name='Sheet1')
print(f"维度：{df.shape[0]}行 × {df.shape[1]}列")
print(df.describe())

# CSV（注意编码）
df = pd.read_csv('数据.csv', encoding='utf-8')  # 中文Windows试 encoding='gbk'
```

也可用内置脚本：
```bash
SKILL_DIR="$(dirname "$(find ~/.claude/skills -name 'SKILL.md' -path '*/data-office-pro/*' 2>/dev/null | head -1)")"
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --summary
```

### Step 2: 数据概览（拿到数据后自动执行）

输出5项：
1. 数据维度（行×列）
2. 字段清单（名称、类型、缺失率）
3. 基础统计（均值/中位数/极值）
4. 数据质量问题（缺失值、异常值、格式不一致）
5. 初步发现（1-2个趋势或问题）

然后问用户分析方向，给出2-3个建议供选。

### Step 3: 执行分析

输出格式：
```
核心结论（1-3句）
→ 数据支撑（具体数字、对比、趋势）
→ 异常/风险
→ 可执行建议（3-5条，按优先级）
→ 下一步（多想一步）
```

### Step 4: 可视化

分析完成后主动询问是否需要可视化。选择路径见「数据可视化工作流」。

---

## Excel操作工作流

### 公式生成

始终包含错误处理（IFERROR）。输出格式：
```
公式：=IFERROR(D2/C2, 0)
含义：计算ROI（GMV÷消耗），除零时返回0
适用范围：H2:H[最后一行]
```

### 模板设计

```
Sheet 1: 原始数据 — 字段定义、数据验证规则
Sheet 2: 计算层 — 衍生指标公式、条件格式
Sheet 3: 汇总视图 — 透视表、关键指标看板
Sheet 4: 图表 — 数据可视化
```

### 数据处理脚本

当公式无法满足时（大数据量、复杂逻辑），用Python处理。
原则：优先用Excel公式（用户可维护），复杂场景才用脚本。

---

## 报告生成工作流

### 管理层汇报（1页纸原则）
1. 核心结论（3句以内）
2. 关键指标汇总（表格）
3. 问题诊断（数据支撑）
4. 优化建议（按优先级）
5. 风险提示

### 详细分析报告
1. 摘要（半页）
2. 数据概览（关键指标面板）
3. 分维度分析（每个维度一节）
4. 异常值与风险
5. 建议与行动计划
6. 附录：数据来源与方法论

---

## HTML交互报告工作流

默认输出格式。使用ECharts（内联，非CDN）+ 分析文字 + PDF导出。

### 关键约束
- **零CDN依赖** — 所有JS/CSS内联或纯SVG，Playwright离线截图不会白屏
- 图表用SVG/Canvas绑定数据，不用CSS absolute定位模拟
- 每页底部加PDF导出提示（见 `html-templates.md` 标准组件）
- 风格参数 → `visual-design-system.md`
- 模板 → `html-templates.md`

### 截图命令
```bash
# 标准图表
npx playwright screenshot "file:///path/to/chart.html" output.png \
  --viewport-size=1200,675 --wait-for-timeout=2000

# 宽幅信息图
npx playwright screenshot "file:///path/to/infographic.html" output.png \
  --viewport-size=1920,1080 --wait-for-timeout=2000
```

---

## PPT制作工作流（HTML→PPTX）

### 流程
```
确认受众与风格 → 生成大纲 → 逐页创建HTML → 转PPTX → 预览确认
```

### 必须问清楚的3个问题
1. 受众是谁？（管理层/客户/内部团队）
2. 用途是什么？（汇报/比稿/培训/记录）
3. 时间多长？（约1分钟/页）

### 断言式标题

| 差标题 | 好标题 |
|--------|--------|
| Q1投放数据 | Q1整体ROI达3.2，超目标7% |
| 问题分析 | 服饰板块退货率45%是亏损主因 |

### HTML幻灯片规则

画布：`width: 720pt; height: 405pt`（16:9）

关键：
- 文字必须在 `<p>`/`<h1>`-`<h6>`/`<ul>`/`<ol>` 内 — `<div>` 裸文字不进PPT
- 背景/边框/阴影只用在 `<div>` 上
- 禁止CSS渐变（需渐变先用Sharp渲染PNG）
- 只用web安全字体：Arial, Helvetica, Georgia, Verdana, Tahoma
- 列表用 `<ul>`/`<ol>`，禁止手动 •/-/* 符号
- 图表颜色hex**不带#前缀**（PptxGenJS规则）

### 构建命令

```bash
SKILL_DIR="$(dirname "$(find ~/.claude/skills -name 'SKILL.md' -path '*/data-office-pro/*' 2>/dev/null | head -1)")"

# 从多个HTML构建
node "$SKILL_DIR/scripts/build_pptx.js" --slides slide1.html slide2.html --output report.pptx

# 从目录加载
node "$SKILL_DIR/scripts/build_pptx.js" --dir ./slides/ --output report.pptx

# 带图表
node "$SKILL_DIR/scripts/build_pptx.js" --slides slide1.html --output report.pptx --chart 0:col:chart_data.json
```

### 图表数据JSON格式
```json
{
  "title": "各板块ROI对比",
  "catAxisTitle": "板块",
  "valAxisTitle": "ROI",
  "colors": ["E17055", "45B7AA", "5B8C5A", "FFD700"],
  "series": [{"name": "ROI", "labels": ["美妆","食品","服饰"], "values": [3.8, 2.5, 1.1]}]
}
```

### 预览
```bash
npx playwright screenshot "file:///path/to/slide.html" preview.png \
  --viewport-size=960,540 --wait-for-timeout=1000
```

---

## 数据可视化工作流

| 场景 | 方式 |
|------|------|
| 快速看趋势 | Python matplotlib |
| 放进报告/PPT | HTML → Playwright截图 |
| PPT内原生图表 | PptxGenJS |
| 独立分享 | HTML → 截图 → 上传图床 |

模板 → `html-templates.md`，风格参数 → `visual-design-system.md`

---

## PPTX/Excel读取

```bash
SKILL_DIR="$(dirname "$(find ~/.claude/skills -name 'SKILL.md' -path '*/data-office-pro/*' 2>/dev/null | head -1)")"

# 读取PPT
python3 "$SKILL_DIR/scripts/read_pptx.py" presentation.pptx --format markdown
python3 "$SKILL_DIR/scripts/read_pptx.py" presentation.pptx --inventory  # 仅结构

# 读取Excel
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --summary
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --sheet "Sheet1" --head 20
python3 "$SKILL_DIR/scripts/read_excel.py" data.xlsx --format csv
```

---

## 依赖管理

缺失时自动安装，不让用户手动处理。

```bash
# Node.js（PPT制作）
npm install pptxgenjs playwright sharp
npx playwright install chromium

# Python（Excel/PPT读取）
pip install openpyxl pandas python-pptx Pillow
```

遇到版本冲突时用uv隔离：
```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas>=2.0", "openpyxl>=3.1"]
# ///
```
执行：`uv run script.py`

---

## 文件输出约定

| 类型 | 命名规范 |
|------|---------|
| 分析报告 | `分析报告-[主题]-[YYYYMMDD].md` |
| 可视化图片 | `chart-[描述].png` |
| PPT文件 | `[主题]-[YYYYMMDD].pptx` |
| 处理后的Excel | `[原文件名]-processed.xlsx` |
| HTML临时文件 | `/tmp/`，自动清理 |
