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

## 审美原则总结

1. **配色**：暖色为主（奶油、珊瑚、金）+ 高对比黑，避免冷色系
2. **字体**：超大标题（占15-30%），无衬线粗体，信息优先于装饰
3. **空间**：色块分区组织信息，留白适度（不空也不挤）
4. **一致性**：同一文档/PPT内风格统一，图表配色统一
5. **核心理念**：用最简单的方式传达最多信息
