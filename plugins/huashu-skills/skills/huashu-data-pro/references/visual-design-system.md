# 视觉设计系统 — 数据分析与办公场景

> 经过131页PPT实战验证的设计系统。用于数据可视化、报告、PPT制作。

---

## 风格A：Neo-Brutalism（数据密集场景首选）

### 核心CSS变量

```css
:root {
  /* 配色 */
  --bg-cream: #F5E6D3;
  --accent-red: #FF3B4F;
  --accent-gold: #FFD700;
  --text-black: #1A1A1A;
  --card-white: #FFFDF7;

  /* 边框 */
  --border-thick: 4px solid #1A1A1A;
  --border-extra: 6px solid #1A1A1A;

  /* 阴影（纯实色，无模糊） */
  --shadow-sm: 4px 4px 0 #1A1A1A;
  --shadow-md: 8px 8px 0 #1A1A1A;
  --shadow-lg: 12px 12px 0 #1A1A1A;

  /* 圆角 */
  --radius: 12pt;

  /* 字体 */
  --font-heading: 'Arial Black', 'Helvetica Neue', Arial, sans-serif;
  --font-body: Arial, Helvetica, sans-serif;
}
```

### PPT幻灯片模板

```html
<!DOCTYPE html>
<html>
<head>
<style>
html { background: #F5E6D3; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 30pt;
  background: #F5E6D3;
  font-family: Arial, Helvetica, sans-serif;
  display: flex; flex-direction: column;
}

/* 标题区 */
.title-bar {
  background: #FF3B4F; border: 4px solid #1A1A1A;
  border-radius: 12pt; padding: 15pt 25pt;
  box-shadow: 6px 6px 0 #1A1A1A;
  margin-bottom: 20pt;
}
.title-bar h1 {
  color: #FFFDF7; font-size: 28pt; font-weight: 900;
  margin: 0;
}

/* 内容卡片 */
.card {
  background: #FFFDF7; border: 4px solid #1A1A1A;
  border-radius: 12pt; padding: 20pt;
  box-shadow: 6px 6px 0 #1A1A1A;
  flex: 1;
}

/* 数据高亮 */
.metric {
  background: #FFD700; border: 3px solid #1A1A1A;
  border-radius: 8pt; padding: 8pt 16pt;
  display: inline-block; box-shadow: 4px 4px 0 #1A1A1A;
}
.metric p {
  font-size: 24pt; font-weight: 900; color: #1A1A1A; margin: 0;
}

/* 列表 */
.card ul { list-style: none; padding: 0; margin: 0; }
.card li {
  font-size: 14pt; color: #1A1A1A; line-height: 1.8;
  padding-left: 20pt; position: relative;
}
.card li::before {
  content: "▸"; position: absolute; left: 0;
  color: #FF3B4F; font-weight: bold;
}
</style>
</head>
<body>
  <div class="title-bar">
    <h1>Q1投放ROI达3.2，超目标7%</h1>
  </div>
  <div class="card">
    <div style="display: flex; gap: 15pt; margin-bottom: 15pt;">
      <div class="metric"><p>ROI 3.2</p></div>
      <div class="metric"><p>GMV 730万</p></div>
      <div class="metric"><p>消耗占比 16%</p></div>
    </div>
    <ul>
      <li><p>美妆板块ROI 3.8，贡献整体GMV的35%</p></li>
      <li><p>服饰板块退货率45%，实际ROI仅1.1，是主要拖累</p></li>
      <li><p>建议：服饰板块缩减20%预算，转投美妆和食品</p></li>
    </ul>
    <!-- 图表预留区域 -->
    <div id="roi-chart" class="placeholder" style="width: 300pt; height: 150pt; margin-top: 10pt;"></div>
  </div>
</body>
</html>
```

### Neo-Brutalism设计要点

1. **粗黑边框** — 所有卡片/按钮/模块都有 4-6px 黑色实线边框
2. **高饱和色块** — 每个模块一个主色，色块面积大
3. **超大字排版** — 标题占幅面15-30%
4. **偏移实色阴影** — 向右下偏移6-10px，无模糊
5. **无渐变** — 纯色填充 + 锐利边缘

### Neo-Brutalism注意事项

- 避免蓝色或紫色底（容易变成赛博风）
- 文字必须黑色或深色，不要白色文字在彩色底上（除了标题栏）
- 内容溢出时减少内容，不缩小字号 — 大字是灵魂
- 色块之间边界清晰，无模糊过渡

---

## 风格B：Warm Narrative（客户汇报场景）

### 核心CSS变量

```css
:root {
  --bg-warm: #FDF6EC;
  --accent-coral: #E17055;
  --accent-mint: #45B7AA;
  --accent-olive: #5B8C5A;
  --text-dark: #3D3D3D;
  --text-light: #666666;
  --card-white: #FFFFFF;
  --border-subtle: 1px solid #E8DDD0;
  --shadow-soft: 0 4px 12px rgba(0, 0, 0, 0.08);
  --radius: 16pt;
}
```

### PPT幻灯片模板

```html
<!DOCTYPE html>
<html>
<head>
<style>
html { background: #FDF6EC; }
body {
  width: 720pt; height: 405pt; margin: 0; padding: 40pt;
  background: #FDF6EC;
  font-family: Arial, Helvetica, sans-serif;
  display: flex; flex-direction: column;
}

.header {
  margin-bottom: 25pt;
}
.header h1 {
  color: #3D3D3D; font-size: 26pt; font-weight: 700;
  margin: 0 0 8pt 0;
}
.header p {
  color: #999999; font-size: 11pt; margin: 0;
}

.content {
  display: flex; gap: 20pt; flex: 1;
}
.main-card {
  background: #FFFFFF; border: 1px solid #E8DDD0;
  border-radius: 16pt; padding: 25pt;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  flex: 2;
}
.side-card {
  background: #E17055; border-radius: 16pt;
  padding: 25pt; flex: 1;
}
.side-card h2 { color: #FFFFFF; font-size: 16pt; margin: 0 0 10pt 0; }
.side-card p { color: rgba(255,255,255,0.9); font-size: 12pt; line-height: 1.6; margin: 0; }

.main-card h2 { color: #E17055; font-size: 16pt; margin: 0 0 15pt 0; }
.main-card ul { padding-left: 18pt; margin: 0; }
.main-card li { font-size: 12pt; color: #3D3D3D; line-height: 1.8; }
</style>
</head>
<body>
  <div class="header">
    <h1>1月投放效果复盘</h1>
    <p>2026年1月 | 数据截至1月31日</p>
  </div>
  <div class="content">
    <div class="main-card">
      <h2>核心发现</h2>
      <ul>
        <li><p>整体ROI 2.2，距目标3.0仍有差距</p></li>
        <li><p>美妆板块表现最优（ROI 3.8），建议加大投入</p></li>
        <li><p>服饰板块退货率偏高（45%），建议调整素材策略</p></li>
      </ul>
    </div>
    <div class="side-card">
      <h2>关键行动</h2>
      <p>1. 美妆预算上调20%</p>
      <p>2. 服饰暂停ROI&lt;1的计划</p>
      <p>3. 下周出素材A/B测试方案</p>
    </div>
  </div>
</body>
</html>
```

---

## 风格C：极简专业（内部快速分享）

### 核心CSS变量

```css
:root {
  --bg-light: #F5F5F5;
  --accent-blue: #4A90D9;
  --accent-orange: #FF6B35;
  --text-dark: #333333;
  --text-gray: #888888;
  --card-white: #FFFFFF;
  --border-light: 1px solid #E0E0E0;
  --shadow-minimal: 0 2px 8px rgba(0, 0, 0, 0.06);
  --radius: 8pt;
}
```

---

## 图表设计规范

### 配色方案

```
系列1（主）：  #E17055  珊瑚（PptxGenJS: "E17055"）
系列2（对比）：#45B7AA  薄荷绿（PptxGenJS: "45B7AA"）
系列3：       #5B8C5A  橄榄绿（PptxGenJS: "5B8C5A"）
系列4：       #FFD700  金色（PptxGenJS: "FFD700"）
系列5：       #9B7EDE  薰衣草紫（PptxGenJS: "9B7EDE"）
负面/警告：    #FF3B4F  红色（PptxGenJS: "FF3B4F"）
正面/增长：    #4CAF50  绿色（PptxGenJS: "4CAF50"）
参考线/轴线：  #CCCCCC  浅灰
网格线：      #EEEEEE  极淡灰（或不显示）
```

### 图表类型选择指南

| 要讲的故事 | 推荐图表 | 不推荐 |
|-----------|---------|--------|
| 比较大小 | 柱状图（bar/col） | 饼图（>5个类别时） |
| 时间趋势 | 折线图（line） | 柱状图（>12个时间点） |
| 占比构成 | 饼图（≤5类）/ 堆叠柱状图 | 折线图 |
| 两变量关系 | 散点图（scatter） | 柱状图 |
| 排名 | 水平柱状图（bar） | 折线图 |
| 分布 | 直方图 / 箱线图 | 饼图 |

### PptxGenJS图表配置速查

```javascript
// 柱状图
slide.addChart(pptx.charts.BAR, [{
    name: "ROI", labels: ["美妆","食品","服饰","个护"],
    values: [3.8, 2.5, 1.1, 2.0]
}], {
    ...placeholders[0],
    barDir: 'col',
    chartColors: ["E17055"],  // 无#前缀！
    showTitle: true, title: '各板块ROI对比',
    showCatAxisTitle: true, catAxisTitle: '板块',
    showValAxisTitle: true, valAxisTitle: 'ROI',
    valAxisMinVal: 0, valAxisMaxVal: 5,
    dataLabelPosition: 'outEnd', dataLabelColor: '333333'
});

// 折线图
slide.addChart(pptx.charts.LINE, [{
    name: "整体ROI",
    labels: ["W1","W2","W3","W4"],
    values: [2.1, 2.3, 2.0, 2.4]
}], {
    ...placeholders[0],
    lineSize: 3, lineSmooth: true,
    chartColors: ["E17055"],
    showTitle: true, title: '周度ROI趋势',
    showCatAxisTitle: true, catAxisTitle: '周',
    showValAxisTitle: true, valAxisTitle: 'ROI'
});

// 饼图
slide.addChart(pptx.charts.PIE, [{
    name: "GMV占比",
    labels: ["美妆","食品","服饰","个护"],
    values: [35, 20, 30, 15]
}], {
    ...placeholders[0],
    showPercent: true, showLegend: true, legendPos: 'r',
    chartColors: ["E17055", "45B7AA", "5B8C5A", "FFD700"]
});
```

---

## HTML信息图截图模板

### 数据看板卡片（1200×900）

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 900px;
  background: #F5F0EB; padding: 40px;
  font-family: "PingFang SC", Arial, sans-serif;
}
.dashboard-title {
  font-size: 32px; font-weight: 800; color: #1A1A1A;
  margin-bottom: 30px;
}
.metrics-row {
  display: flex; gap: 20px; margin-bottom: 30px;
}
.metric-card {
  background: #FFFDF7; border: 4px solid #1A1A1A;
  border-radius: 12px; padding: 24px;
  box-shadow: 6px 6px 0 #1A1A1A; flex: 1;
  text-align: center;
}
.metric-value {
  font-size: 48px; font-weight: 900; color: #E17055;
}
.metric-label {
  font-size: 16px; color: #888; margin-top: 8px;
}
.metric-change {
  font-size: 14px; margin-top: 4px;
}
.up { color: #4CAF50; }
.down { color: #FF3B4F; }
</style>
</head>
<body>
  <p class="dashboard-title">1月投放数据看板</p>
  <div class="metrics-row">
    <div class="metric-card">
      <p class="metric-value">3.2</p>
      <p class="metric-label">整体ROI</p>
      <p class="metric-change up">↑ 0.4 vs 上月</p>
    </div>
    <div class="metric-card">
      <p class="metric-value">730万</p>
      <p class="metric-label">总GMV</p>
      <p class="metric-change up">↑ 12%</p>
    </div>
    <div class="metric-card">
      <p class="metric-value">16%</p>
      <p class="metric-label">消耗占比</p>
      <p class="metric-change up">↓ 2pt（健康）</p>
    </div>
    <div class="metric-card">
      <p class="metric-value">28%</p>
      <p class="metric-label">退货率</p>
      <p class="metric-change down">↑ 3pt（注意）</p>
    </div>
  </div>
  <!-- 下方区域放图表或详细数据 -->
</body>
</html>
```

截图命令：
```bash
npx playwright screenshot "file:///path/to/dashboard.html" dashboard.png \
  --viewport-size=1200,900 --wait-for-timeout=2000
```

---

## HTML数据报告设计规范（实战验证）

> 基于7份金融数据报告（共22页HTML）的视觉审查，提炼的设计规范。
> 适用于：1200×675pt 数据报告页、信息图、数据看板等 Playwright 截图场景。

### 画布与基础

| 属性 | 规范 | 说明 |
|------|------|------|
| 画布尺寸 | `1200pt × 675pt`（16:9报告页） | 或 `1200px × 900px`（信息图） |
| body padding | 同一系列统一，推荐 `24pt` | 禁止同系列报告不同padding（如20pt vs 28pt） |
| 卡片背景 | 统一用 `#FFFAF5` 或 `#FFFDF7` | 同系列不混用 `#fff` 和 `#FFFAF5` |
| 字体栈 | `Arial, "PingFang SC", Helvetica, sans-serif` | 全系列统一，不能有的页面有PingFang有的没有 |
| CSS单位 | 同一文件只用 `pt` 或只用 `px` | 禁止 pt 和 px 混用 |

### 必须做（DO）

**图表实现**
1. **所有图表用纯SVG或内联JS** — 禁止依赖外部CDN（Chart.js/ECharts等），Playwright离线截图时CDN不可用，图表会完全空白
2. **SVG标注必须在viewBox范围内** — 检查所有文字/标注的x/y坐标不为负值、不超出viewBox边界，否则Playwright截图会裁剪
3. **标注文字做避让处理** — 当两个标注水平距离<80pt时，错开垂直位置或合并。密集数据区域（如牛市顶部）尤其注意
4. **散点图/气泡图用SVG精确坐标** — 不用CSS `position: absolute`手动定位，精度不足会导致气泡重叠

**柱状图/条形图**
5. **Y轴基线从0开始**（金额/数量/占比场景） — 如果数据范围很小（如评分4.25~4.39），必须在图表标题或注脚说明「非零基线」，否则会过度放大差异误导观众
6. **条形图用绝对比例** — 19.5%的市占率就应该是46%宽度的42%。如果用相对排名比例（第一名=满宽），必须在图表中明确标注
7. **堆叠图<3%的segment合并为「其他」** — 或不在极小segment上显示百分比标签，避免文字不可见/重叠
8. **柱状图柱子宽度≥12pt** — 低于12pt在截图后肉眼无法辨识，29组柱子就需要更大的图表宽度

**排版与空间**
9. **flex容器与内容匹配** — 如果表格只有7行数据，不要用 `flex:1` 撑满整个卡片再留出50%空白。宁可缩小卡片高度
10. **同系列报告header风格统一** — 全部用黑底金字，或全部用明底大字，不混用
11. **表格必须有斑马纹** — `tr:nth-child(even) { background: #FDF6EC; }` 或高亮当前焦点行，防止串行
12. **条形图极小值设最小宽度** — `min-width: 6pt`，避免1.1%的值在视觉上完全消失

**字号（投影/培训场景）**
13. **辅助文字最小10pt** — 图例、轴标签、数据来源、气泡缩写等，<10pt在投影时不可读
14. **表头最小10pt** — 不要用8pt表头
15. **洞察/分析文字最小11pt** — insight-box内的解读文字行高≥1.6

**配色细节**
16. **金色在白底/浅底用暗金 `#D4A017` 或 `#B8860B`** — `#FFD700` 在白底对比度仅1.94:1，不符WCAG标准
17. **品类/系列配色保持语义一致** — 同一报告系列中，NVDA始终是同一个颜色，不要在不同页面换色

### 禁止做（DON'T）

| 编号 | 禁止事项 | 原因 |
|------|---------|------|
| D1 | 引用CDN资源（Chart.js/ECharts/D3等） | 离线截图白屏 |
| D2 | SVG坐标超出viewBox（负值y/超宽x） | 截图裁剪 |
| D3 | CSS `position: absolute` 定位数据点 | 精度不足，重叠不可控 |
| D4 | 同系列报告混用不同padding/字体/卡片背景 | 视觉不统一 |
| D5 | 同一文件混用pt和px单位 | 渲染不一致 |
| D6 | 辅助文字<10pt（图例/轴标签/来源/缩写） | 投影不可读 |
| D7 | 不说明的非零基线柱状图 | 误导观众 |
| D8 | 条形图极小值无最小宽度保护 | 视觉消失 |
| D9 | flex:1撑满容器但内容只占40% | 大面积空白 |
| D10 | `#FFD700`金色直接用在白底文字上 | 对比度不足 |
| D11 | 堆叠图在<3%的segment上放标签 | 文字不可见 |
| D12 | 气泡图内用缩写代替品牌全名且无图例对照 | 辨识度差 |
| D13 | 表格无斑马纹、无高亮行 | 容易串行 |
| D14 | 市值/排名从小到大排列 | 反直觉，应从大到小 |

### 数据报告画布模板（1200×675pt）

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html { background: #F5E6D3; }
body {
  width: 1200pt; height: 675pt; margin: 0; padding: 24pt;
  background: #F5E6D3;
  font-family: Arial, "PingFang SC", Helvetica, sans-serif;
  display: flex; flex-direction: column;
}

/* 标题栏 */
.header {
  background: #1A1A1A; border-radius: 12pt;
  padding: 14pt 24pt; margin-bottom: 16pt;
  display: flex; align-items: center; justify-content: space-between;
}
.header h1 { color: #FFD700; font-size: 22pt; font-weight: 800; }
.header .subtitle { color: rgba(255,255,255,0.6); font-size: 10pt; }

/* 内容卡片 */
.card {
  background: #FFFAF5; border: 3pt solid #1A1A1A;
  border-radius: 12pt; padding: 18pt;
  box-shadow: 5pt 5pt 0 #1A1A1A;
}

/* KPI行 */
.kpi-row { display: flex; gap: 12pt; margin-bottom: 14pt; }
.kpi-box {
  flex: 1; background: #FFFAF5; border: 2pt solid #1A1A1A;
  border-radius: 8pt; padding: 10pt 14pt; text-align: center;
  box-shadow: 3pt 3pt 0 #1A1A1A;
}
.kpi-value { font-size: 24pt; font-weight: 900; }
.kpi-label { font-size: 10pt; color: #888; margin-top: 4pt; }

/* 表格 */
table { width: 100%; border-collapse: collapse; }
th {
  background: #1A1A1A; color: #FFD700;
  padding: 10pt 14pt; font-size: 11pt; text-align: left;
}
td { padding: 8pt 14pt; font-size: 11pt; border-bottom: 1pt solid #E8DDD0; }
tr:nth-child(even) td { background: #FDF6EC; }
tr.highlight td { background: #FFF3CD; }

/* 洞察区 */
.insight-box {
  background: #1A1A1A; border-radius: 10pt;
  padding: 14pt 20pt; margin-top: 12pt;
}
.insight-box p { color: #FFFAF5; font-size: 11pt; line-height: 1.65; }
.insight-box .highlight-text { color: #FFD700; font-weight: 700; }

/* 底部来源 */
.footer {
  margin-top: auto; padding-top: 8pt;
  font-size: 8pt; color: #999; text-align: right;
}
</style>
</head>
<body>
  <div class="header">
    <h1>报告标题</h1>
    <p class="subtitle">数据来源 · 日期</p>
  </div>
  <!-- 内容区域 -->
  <div class="footer"><p>数据来源：XXX · 截至YYYY-MM-DD</p></div>
</body>
</html>
```

截图命令：
```bash
npx playwright screenshot "file:///path/to/report.html" output.png \
  --viewport-size=1200,675 --wait-for-timeout=2000
```

### SVG图表实现要点

```html
<!-- 正确：内联SVG折线图 -->
<svg viewBox="0 0 800 300" width="800pt" height="300pt">
  <!-- 网格线 -->
  <line x1="60" y1="20" x2="60" y2="270" stroke="#DDD" stroke-width="1"/>

  <!-- 数据线 -->
  <polyline points="60,250 160,220 260,180 360,100 460,60"
    fill="none" stroke="#E17055" stroke-width="3"/>

  <!-- 面积填充 -->
  <polygon points="60,250 160,220 260,180 360,100 460,60 460,270 60,270"
    fill="#E17055" fill-opacity="0.1"/>

  <!-- 标注（确保在viewBox内） -->
  <circle cx="460" cy="60" r="5" fill="#E17055"/>
  <text x="460" y="50" text-anchor="middle" font-size="11"
    font-weight="700" fill="#1A1A1A">最高点 $950</text>

  <!-- 轴标签（≥10pt） -->
  <text x="60" y="290" font-size="10" fill="#888">2020</text>
</svg>
```

**标注避让算法（伪代码）**：
```
for each annotation:
  检查与其他标注的距离
  if 水平距离 < 80pt:
    if 当前标注在上方: 上移20pt
    else: 下移20pt
  if y < 0 或 y > viewBox.height:
    翻转到数据点另一侧
```

---

## 审美原则总结

1. **配色**：暖色为主（奶油、珊瑚、暗金）+ 高对比黑，避免冷色系
2. **字体**：超大标题（占15-30%），无衬线粗体，辅助文字≥10pt
3. **空间**：色块分区组织信息，内容填满容器（不空也不挤）
4. **一致性**：同系列报告的padding/字体/卡片背景/header/footer全部统一
5. **图表**：纯SVG内联实现，禁止CDN依赖，标注不重叠不溢出
6. **数据诚实**：柱状图零基线、条形图绝对比例、极小值有保护
7. **核心理念**：用最简单的方式传达最多信息，在投影场景10米外仍可读
