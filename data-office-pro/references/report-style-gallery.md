# 可视化报告风格库

> 5种经实战验证的数据报告视觉风格。用于 HTML 数据报告、分析报告、研究报告等场景。
> 每种风格都有完整的色彩、字体、布局、图表规范，可直接用于生成。

## 使用方式

当用户需要生成可视化数据报告（非PPT）时：
1. 如果用户指定了风格 → 使用指定风格
2. 如果用户未指定 → **从以下5种风格中随机选择一种**，让每次产出都有新鲜感
3. 选择后在回复开头简短说明所用风格（如「本次使用 Financial Times 风格」）

所有风格均适用于 `1200×675pt`（16:9报告页）或 `1200×900px`（信息图）的 Playwright 截图场景。

---

## 风格 1：Financial Times（三文鱼粉）

> 一句话：「我们不需要花哨的视觉来证明自己的价值，信息本身就是价值。」

### 色彩

| 用途 | 色值 | 说明 |
|------|------|------|
| 页面背景 | `#FFF1E5` | FT标志性三文鱼粉 |
| 卡片/内容区 | `#FFFFFF` | 纯白，与粉色背景柔和对比 |
| 主要文字 | `#33302E` | 深棕灰，非纯黑 |
| 次要文字 | `#6B6B6B` | 中灰色，标注/来源/元信息 |
| 强调蓝 | `#0F5499` | FT品牌蓝，链接/标签/重点数据 |
| 警告红 | `#CC0000` | 负面数据、风险提示 |
| 正向绿 | `#09823A` | 正面数据、增长指标 |
| 边框 | `#E0D3C3` | 暖色调细边框 |
| 图表辅助 | `#996600` | 金棕色，第三数据系列 |

### 字体

| 场景 | 字体 |
|------|------|
| 标题/章节名 | `Georgia, 'Times New Roman', serif` |
| 正文/数据 | `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` |
| 数字 | `font-variant-numeric: tabular-nums` |

### 关键设计元素

- **4px蓝色顶线**（`#0F5499`）：页面最顶部，FT最标志性的视觉元素
- **边框**：1px实线 `#E0D3C3`，不用box-shadow，不用粗线
- **圆角**：无或极小（最多4px）
- **间距**：大量留白。Section间距48px，段落16px，卡片内边距24px
- **分隔线**：40px短线或全宽1px细线
- **衬线标题 + 无衬线正文**：传递传统金融媒体的权威感
- **数据内嵌叙事**：关键数字嵌入文字段落，不孤立在图表里

### ECharts配置

- 关闭动画（`animation: false`）
- 线条宽度2px
- 网格线虚线 `#F5EDE3`
- 图例矩形小方块（`icon: 'rect'`），12px
- 图表下方必须有source line，11px灰色字
- Tooltip白色背景 + 细边框，不用阴影

---

## 风格 2：McKinsey Consulting（深蓝权威）

> 一句话：每个图表都是「证据」，每个标题都是「结论」。

### 色彩

| 用途 | 色值 |
|------|------|
| 页面背景 | `#FFFFFF` |
| Header | `#003366`（McKinsey深蓝） |
| 主文字 | `#1A1A2E` |
| 次文字 | `#666680` |
| 强调蓝 | `#4472C4` |
| 强调橙 | `#ED7D31`（警告/风险） |
| 强调绿 | `#70AD47`（正向） |
| 弱化填充 | `#A5B4C8` |
| 边框 | `#D6D6D6` |
| 斑马纹行 | `#F7F8FA` |
| Takeaway框 | `#F4F6F9` |

### 字体

全部使用 `'Helvetica Neue', Arial, sans-serif`

### 关键设计元素

- **Exhibit编号**：图表标注为「Exhibit 1:」「Exhibit 2:」，不是「图1」
- **结论式标题**：标题是结论不是描述（如「Cloud revenue drives 60% of incremental growth」而非「Revenue by segment」）
- **Key Takeaway框**：4px左边框 `#003366`，浅灰背景 `#F4F6F9`，「KEY TAKEAWAY」大写标签
- **KPI Strip**：紧贴Header下方，同色深蓝背景，5个指标并排
- **Source Line**：每个Exhibit必须有来源标注
- **无渐变、无阴影、无圆角**

### 页面结构

```
[深蓝Header: 标题 + 副标题 + Confidential]
[深蓝KPI Strip: 5个指标并排]
[白色内容区]
  Exhibit 1: [结论式标题]
    [图表]
    [Source Line]
    [Key Takeaway框]
  ─────────────
  Exhibit 2: ...
[深蓝结论框]
[Footer: Disclaimer]
```

### ECharts色板

```javascript
['#003366', '#4472C4', '#70AD47', '#ED7D31', '#A5B4C8']
```

---

## 风格 3：The Economist（杂志红线）

> 一句话：红色是信号不是装饰，每个图表标题都带观点和态度。

### 色彩

| 用途 | 色值 |
|------|------|
| 页面背景 | `#FFFFFF` |
| Header标识线 | `#E3120B`（6px红线） |
| 主文字 | `#1D1D1B` |
| 次文字 | `#616161` |
| 强调红 | `#E3120B`（图表主线、KPI强调） |
| 辅助蓝绿 | `#0A5E87` |
| 正向绿 | `#3B7A57` |
| 边框 | `#DBDBDB` |
| 浅背景 | `#F5F5F5` / `#FAFAFA` |

### 字体

| 场景 | 字体 |
|------|------|
| 标题 | `Georgia, 'Times New Roman', serif` |
| 正文 | `'Helvetica Neue', Arial, sans-serif` |

### 关键设计元素

- **6px红色顶线**：页面和KPI区顶部
- **3px红色细线**：每个图表区块顶部，The Economist图表的视觉签名
- **Editorial标题**：图表标题带观点（「AI的胃口」而非「资本开支趋势」）
- **副标题**：通俗语言解释图表内容
- **Pull Quote**：大号衬线字体 + 左侧红色竖线
- **信息密度高如杂志**：双栏布局优先，图表紧凑（260-280px高度）
- **Small Multiples**：多个小图表优于一个巨型图表

### 红色使用原则

- 每个section最多一个红色元素作为焦点
- 用于顶线、图表thin bar、最重要数据线、关键数字强调、Pull quote竖线
- **不滥用**：作为焦点而非填充

### ECharts色板

```javascript
['#E3120B', '#0A5E87', '#3B7A57', '#B8B8B8']
```

---

## 风格 4：Goldman Sachs（投行报告）

> 一句话：Tables are king — 数据表格承载分析，图表只是辅助。

### 色彩

| 用途 | 色值 |
|------|------|
| 页面背景 | `#F8F9FA` |
| 卡片/表格 | `#FFFFFF` |
| Header | `#00338D`（GS深蓝） |
| 主文字 | `#1B1B1B` |
| 次文字 | `#5F6368` |
| 强调金 | `#D4AF37`（投资论点、Base Case） |
| 负面红 | `#C62828` |
| 正向绿 | `#2E7D32` |
| 边框 | `#DEE2E6` |
| 斑马纹行 | `#FAFBFC` |
| Bottom Line | `#F0F4F8` |

### 字体

全部使用 `'Helvetica Neue', Arial, sans-serif`
- 表头：11px, 600, 白色, 大写, 0.5px letter-spacing
- 行标签：11px, 500, 灰色, 大写, 0.3px spacing
- 数据：12px, 400

### 关键设计元素

- **Rating Strip**：BUY(绿)/NEUTRAL(金)/SELL(红) 评级徽章，报告顶部最先看到
- **Investment Thesis框**：白色卡片 + 4px金色左边框 `#D4AF37`
- **密集金融表格**：深蓝表头、斑马纹、hover态、关键值高亮
- **Bottom Line Strip**：浅灰蓝背景 + 3px深蓝左边框，一句话总结
- **DCF Sensitivity Table**：Base Case用金色边框高亮，高于/低于现价分别用绿/红
- **Risk Badges**：HIGH(红边框), MED(金边框), LOW(绿边框)
- **无渐变、无阴影、无圆角**：锐利边缘传递机构权威感

### GS设计原则

1. Tables are king — 数据表格承载分析
2. Navy + Gold 双色签名 — 深蓝是结构，金色是强调
3. Bottom line clarity — 每个section都以一句话结论收尾
4. Dense but scannable — 数据密集但层级清晰
5. Rating-first — 评级判断最先呈现

### ECharts色板

```javascript
['#00338D', '#5B9BD5', '#A5A5A5', '#C62828']
```

---

## 风格 5：Swiss / NZZ Minimal（瑞士极简）

> 一句话：只用黑白灰红四种色彩、Helvetica一种字体、极端字号对比和大量留白，让数据自己说话。

### 色彩

| 用途 | 色值 |
|------|------|
| 页面背景 | `#FFFFFF`（纯白，不接受其他底色） |
| 主文字 | `#000000` |
| 次文字 | `#767676` |
| 强调红 | `#FF0000`（Swiss Red，极度克制使用） |
| 边框主 | `#000000`（1px黑线） |
| 边框次 | `#E5E5E5` |

### 色彩使用原则

- 红色是「信号」不是「装饰」— 每个section最多一个红色元素
- 整页红色元素不超过3-5个
- 图表用 黑+深灰+中灰，仅一个系列用红色强调
- 永远不使用渐变、阴影、发光效果

### 字体

全部使用 `'Helvetica Neue', Helvetica, Arial, sans-serif`

| 层级 | 字号 | 字重 |
|------|------|------|
| Display | 72px | 900 (Black) |
| Section Title | 48px | 900 (Black) |
| Key Number | 36-64px | 700-900 |
| Subtitle | 24px | 300 (Light) |
| Body | 16px | 400 (Regular) |
| Label | 13-14px | 400 |

- 标题与正文字号比至少 4:1
- 大字号 letter-spacing 负值（-1px 到 -4px），小字号正值（0.5px-2px）

### 关键设计元素

- **极端字号对比**：72px标题 vs 13px标签
- **黑色分隔线**：`1px solid #000000`，章节间的唯一分隔手段
- **严格网格**：5列等分指标条，4列护城河，3列判断区间
- **Grid列间分隔**：`border-right: 1px solid #E5E5E5`
- **大量留白**：页面内边距60-80px，Section间距60-64px

### 绝对禁止

圆角、阴影、渐变、背景色块（除纯白）、图标/Emoji、装饰性元素、动画

### ECharts色板

```javascript
['#000000', '#444444', '#999999', '#FF0000']
```

---

## 风格速查对比

| 维度 | FT | McKinsey | Economist | Goldman Sachs | Swiss/NZZ |
|------|-----|----------|-----------|---------------|-----------|
| 背景色 | 三文鱼粉 | 纯白 | 纯白 | 浅灰 | 纯白 |
| 品牌色 | 蓝 #0F5499 | 深蓝 #003366 | 红 #E3120B | 深蓝+金 | 红 #FF0000 |
| 标题字体 | 衬线(Georgia) | 无衬线(Helvetica) | 衬线(Georgia) | 无衬线(Helvetica) | 无衬线(Helvetica) |
| 装饰度 | 极简 | 结构化 | 杂志感 | 机构感 | 极度克制 |
| 信息密度 | 中等 | 中高 | 高 | 高 | 中等 |
| 最适场景 | 金融分析、叙事报告 | 战略分析、框架评估 | 行业洞察、观点报告 | 财务建模、估值报告 | 数据展示、设计感报告 |
| 标志元素 | 4px蓝色顶线 | Exhibit编号+结论标题 | 3px红色thin bar | Rating徽章+金色边框 | 72px黑色大字 |
