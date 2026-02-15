# HTML可视化模板库

> 即用型HTML模板，用Playwright截图生成高品质数据可视化图片。
> 所有模板已适配深色模式（避免纯白/纯黑），遵循Neo-Brutalism和Warm Narrative双风格体系。

---

## 使用方法

1. 复制模板，替换数据和标题
2. 保存为 `.html` 文件
3. 用 Playwright 截图：

```bash
npx playwright screenshot "file:///path/to/template.html" output.png \
  --viewport-size=[宽],[高] --wait-for-timeout=2000
```

---

## 模板1：KPI指标看板（4指标）

**尺寸**：1200×400 | **风格**：Neo-Brutalism

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 400px; background: #F5E6D3;
  padding: 30px; font-family: "PingFang SC", Arial, sans-serif;
  display: flex; flex-direction: column;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
.row { display: flex; gap: 20px; flex: 1; }
.card {
  flex: 1; background: #FFFDF7; border: 4px solid #1A1A1A;
  border-radius: 12px; padding: 20px;
  box-shadow: 6px 6px 0 #1A1A1A;
  display: flex; flex-direction: column; justify-content: center;
  text-align: center;
}
.card-value { font-size: 52px; font-weight: 900; }
.card-label { font-size: 16px; color: #888; margin-top: 6px; }
.card-change { font-size: 14px; margin-top: 4px; }
.v-coral { color: #E17055; }
.v-mint { color: #45B7AA; }
.v-gold { color: #D4A017; }
.v-olive { color: #5B8C5A; }
.up { color: #4CAF50; }
.down { color: #FF3B4F; }
.neutral { color: #888; }
</style>
</head>
<body>
  <p class="title">2026年1月 投放数据概览</p>
  <div class="row">
    <div class="card">
      <p class="card-value v-coral">3.2</p>
      <p class="card-label">整体ROI</p>
      <p class="card-change up">↑ 0.4 vs 上月</p>
    </div>
    <div class="card">
      <p class="card-value v-mint">730万</p>
      <p class="card-label">总GMV</p>
      <p class="card-change up">↑ 12%</p>
    </div>
    <div class="card">
      <p class="card-value v-gold">16%</p>
      <p class="card-label">消耗占比</p>
      <p class="card-change up">↓ 2pt</p>
    </div>
    <div class="card">
      <p class="card-value v-olive">28%</p>
      <p class="card-label">退货率</p>
      <p class="card-change down">↑ 3pt</p>
    </div>
  </div>
</body>
</html>
```

截图：`--viewport-size=1200,400`

---

## 模板2：多板块对比表格

**尺寸**：1200×600 | **风格**：Neo-Brutalism

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 600px; background: #F5E6D3;
  padding: 30px; font-family: "PingFang SC", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
table {
  width: 100%; border-collapse: separate; border-spacing: 0;
  border: 4px solid #1A1A1A; border-radius: 12px;
  overflow: hidden; box-shadow: 6px 6px 0 #1A1A1A;
  background: #FFFDF7;
}
th {
  background: #1A1A1A; color: #FFD700;
  padding: 14px 20px; font-size: 16px; font-weight: 700;
  text-align: left;
}
td {
  padding: 14px 20px; font-size: 15px; color: #1A1A1A;
  border-bottom: 2px solid #E8DDD0;
}
tr:last-child td { border-bottom: none; }
tr:hover td { background: #FFF8E7; }
.tag {
  display: inline-block; padding: 3px 10px;
  border-radius: 6px; font-size: 13px; font-weight: 700;
}
.tag-good { background: #D4EDDA; color: #155724; }
.tag-warn { background: #FFF3CD; color: #856404; }
.tag-bad { background: #F8D7DA; color: #721C24; }
.num-highlight { font-weight: 900; font-size: 18px; }
</style>
</head>
<body>
  <p class="title">各板块ROI与盈亏分析</p>
  <table>
    <tr>
      <th><p>板块</p></th>
      <th><p>GMV</p></th>
      <th><p>消耗</p></th>
      <th><p>ROI</p></th>
      <th><p>退货率</p></th>
      <th><p>状态</p></th>
    </tr>
    <tr>
      <td><p>美妆·护肤</p></td>
      <td><p class="num-highlight">200万</p></td>
      <td><p>45万</p></td>
      <td><p class="num-highlight" style="color: #4CAF50;">3.8</p></td>
      <td><p>28%</p></td>
      <td><p><span class="tag tag-good">盈利</span></p></td>
    </tr>
    <tr>
      <td><p>食品</p></td>
      <td><p class="num-highlight">150万</p></td>
      <td><p>30万</p></td>
      <td><p class="num-highlight" style="color: #45B7AA;">2.5</p></td>
      <td><p>15%</p></td>
      <td><p><span class="tag tag-good">盈利</span></p></td>
    </tr>
    <tr>
      <td><p>服饰</p></td>
      <td><p class="num-highlight">300万</p></td>
      <td><p>80万</p></td>
      <td><p class="num-highlight" style="color: #FF3B4F;">1.1</p></td>
      <td><p style="color: #FF3B4F; font-weight: 700;">45%</p></td>
      <td><p><span class="tag tag-bad">亏损</span></p></td>
    </tr>
    <tr>
      <td><p>个护</p></td>
      <td><p class="num-highlight">120万</p></td>
      <td><p>25万</p></td>
      <td><p class="num-highlight" style="color: #D4A017;">2.0</p></td>
      <td><p>20%</p></td>
      <td><p><span class="tag tag-warn">持平</span></p></td>
    </tr>
  </table>
</body>
</html>
```

截图：`--viewport-size=1200,600`

---

## 模板3：趋势折线图（CSS纯实现）

**尺寸**：1200×500 | **风格**：Warm Narrative

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 500px; background: #FDF6EC;
  padding: 40px; font-family: "PingFang SC", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 700; color: #3D3D3D; margin-bottom: 6px; }
.subtitle { font-size: 14px; color: #999; margin-bottom: 30px; }
.chart-area {
  background: #FFFFFF; border: 1px solid #E8DDD0;
  border-radius: 16px; padding: 30px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  height: 340px; position: relative;
}
/* 简单柱状图用CSS实现 */
.bar-chart { display: flex; align-items: flex-end; gap: 20px; height: 250px; padding-top: 20px; }
.bar-group { flex: 1; display: flex; flex-direction: column; align-items: center; }
.bar {
  width: 60px; border-radius: 8px 8px 0 0;
  transition: height 0.3s;
}
.bar-label { font-size: 13px; color: #888; margin-top: 8px; }
.bar-value { font-size: 12px; font-weight: 700; color: #3D3D3D; margin-bottom: 4px; }
.baseline {
  position: absolute; left: 30px; right: 30px; bottom: 70px;
  border-bottom: 2px dashed #E8DDD0;
}
.baseline-label {
  position: absolute; right: 30px; bottom: 73px;
  font-size: 11px; color: #E17055;
}
</style>
</head>
<body>
  <p class="title">各板块ROI表现</p>
  <p class="subtitle">2026年1月 | 目标线：3.0</p>
  <div class="chart-area">
    <div class="baseline"></div>
    <p class="baseline-label">目标 3.0</p>
    <div class="bar-chart">
      <div class="bar-group">
        <p class="bar-value">3.8</p>
        <div class="bar" style="height: 190px; background: #4CAF50;"></div>
        <p class="bar-label">美妆</p>
      </div>
      <div class="bar-group">
        <p class="bar-value">2.5</p>
        <div class="bar" style="height: 125px; background: #45B7AA;"></div>
        <p class="bar-label">食品</p>
      </div>
      <div class="bar-group">
        <p class="bar-value">1.1</p>
        <div class="bar" style="height: 55px; background: #FF3B4F;"></div>
        <p class="bar-label">服饰</p>
      </div>
      <div class="bar-group">
        <p class="bar-value">2.0</p>
        <div class="bar" style="height: 100px; background: #D4A017;"></div>
        <p class="bar-label">个护</p>
      </div>
    </div>
  </div>
</body>
</html>
```

截图：`--viewport-size=1200,500`

---

## 模板4：问题诊断卡片

**尺寸**：1200×700 | **风格**：Neo-Brutalism

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 700px; background: #F5E6D3;
  padding: 30px; font-family: "PingFang SC", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
.cards { display: flex; gap: 20px; }
.diagnosis-card {
  flex: 1; border: 4px solid #1A1A1A; border-radius: 12px;
  overflow: hidden; box-shadow: 6px 6px 0 #1A1A1A;
}
.card-header {
  padding: 16px 20px;
}
.header-red { background: #FF3B4F; }
.header-gold { background: #FFD700; }
.header-green { background: #4CAF50; }
.card-header h2 { color: #1A1A1A; font-size: 18px; font-weight: 800; }
.header-red h2 { color: #FFFDF7; }
.card-body {
  background: #FFFDF7; padding: 20px;
}
.card-body ul { list-style: none; padding: 0; }
.card-body li {
  font-size: 14px; color: #1A1A1A; line-height: 1.8;
  padding: 6px 0; border-bottom: 1px solid #F0E8DD;
}
.card-body li:last-child { border-bottom: none; }
.priority-tag {
  display: inline-block; background: #1A1A1A; color: #FFD700;
  padding: 2px 8px; border-radius: 4px; font-size: 11px;
  font-weight: 700; margin-right: 6px;
}
</style>
</head>
<body>
  <p class="title">投放问题诊断与优化建议</p>
  <div class="cards">
    <div class="diagnosis-card">
      <div class="card-header header-red">
        <h2>问题（需立即处理）</h2>
      </div>
      <div class="card-body">
        <ul>
          <li><p><span class="priority-tag">P0</span>服饰板块ROI 1.1，低于盈亏线</p></li>
          <li><p><span class="priority-tag">P0</span>退货率45%导致实际GMV缩水近半</p></li>
          <li><p><span class="priority-tag">P1</span>晚8-10点时段CPM偏高，ROI反而最低</p></li>
        </ul>
      </div>
    </div>
    <div class="diagnosis-card">
      <div class="card-header header-gold">
        <h2>建议（本周执行）</h2>
      </div>
      <div class="card-body">
        <ul>
          <li><p><span class="priority-tag">1</span>服饰板块暂停ROI&lt;1的计划，预计月省8万</p></li>
          <li><p><span class="priority-tag">2</span>美妆板块预算上调20%（ROI有余量）</p></li>
          <li><p><span class="priority-tag">3</span>测试避开晚8-10点，转投午间12-14点</p></li>
        </ul>
      </div>
    </div>
    <div class="diagnosis-card">
      <div class="card-header header-green">
        <h2>亮点（继续保持）</h2>
      </div>
      <div class="card-body">
        <ul>
          <li><p>美妆ROI 3.8，超目标27%</p></li>
          <li><p>食品退货率仅15%，利润率最高</p></li>
          <li><p>整体消耗占比16%，控制在18%红线内</p></li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
```

截图：`--viewport-size=1200,700`

---

## 模板5：流程/工作流图

**尺寸**：1200×400 | **风格**：Neo-Brutalism

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 400px; background: #F5E6D3;
  padding: 30px; font-family: "PingFang SC", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 25px; }
.flow { display: flex; align-items: center; gap: 0; }
.step {
  border: 4px solid #1A1A1A; border-radius: 12px;
  padding: 20px; width: 200px; text-align: center;
  box-shadow: 4px 4px 0 #1A1A1A;
}
.step-num {
  font-size: 32px; font-weight: 900; margin-bottom: 6px;
}
.step-title { font-size: 16px; font-weight: 700; color: #1A1A1A; margin-bottom: 4px; }
.step-desc { font-size: 12px; color: #666; line-height: 1.4; }
.s1 { background: #FF3B4F; }
.s1 .step-num, .s1 .step-title { color: #FFFDF7; }
.s1 .step-desc { color: rgba(255,255,255,0.8); }
.s2 { background: #FFD700; }
.s3 { background: #45B7AA; }
.s3 .step-num, .s3 .step-title { color: #FFFDF7; }
.s3 .step-desc { color: rgba(255,255,255,0.8); }
.s4 { background: #FFFDF7; }
.arrow {
  font-size: 36px; color: #1A1A1A; font-weight: 900;
  padding: 0 15px;
}
</style>
</head>
<body>
  <p class="title">投放数据分析工作流</p>
  <div class="flow">
    <div class="step s1">
      <p class="step-num">01</p>
      <p class="step-title">拉数据</p>
      <p class="step-desc">导出千川后台数据到Excel</p>
    </div>
    <p class="arrow">→</p>
    <div class="step s2">
      <p class="step-num">02</p>
      <p class="step-title">AI分析</p>
      <p class="step-desc">DeepSeek做关联分析和异常检测</p>
    </div>
    <p class="arrow">→</p>
    <div class="step s3">
      <p class="step-num">03</p>
      <p class="step-title">生成报告</p>
      <p class="step-desc">AI撰写复盘报告初稿</p>
    </div>
    <p class="arrow">→</p>
    <div class="step s4">
      <p class="step-num">04</p>
      <p class="step-title">人工校验</p>
      <p class="step-desc">核对数据、补充业务判断</p>
    </div>
  </div>
</body>
</html>
```

截图：`--viewport-size=1200,400`

---

## 模板6：Before / After 对比

**尺寸**：1200×500 | **风格**：Neo-Brutalism

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  width: 1200px; height: 500px; background: #F5E6D3;
  padding: 30px; font-family: "PingFang SC", Arial, sans-serif;
}
.title { font-size: 24px; font-weight: 800; color: #1A1A1A; margin-bottom: 20px; }
.compare { display: flex; gap: 30px; }
.panel {
  flex: 1; border: 4px solid #1A1A1A; border-radius: 12px;
  overflow: hidden; box-shadow: 6px 6px 0 #1A1A1A;
}
.panel-header { padding: 14px 20px; }
.before-header { background: #888888; }
.after-header { background: #4CAF50; }
.panel-header h2 { font-size: 20px; font-weight: 800; color: #FFFDF7; }
.panel-body {
  background: #FFFDF7; padding: 20px;
}
.panel-body ul { list-style: none; padding: 0; }
.panel-body li {
  font-size: 15px; color: #1A1A1A; line-height: 2;
  padding-left: 24px; position: relative;
}
.before-item::before { content: "✗"; position: absolute; left: 0; color: #FF3B4F; font-weight: 700; }
.after-item::before { content: "✓"; position: absolute; left: 0; color: #4CAF50; font-weight: 700; }
.vs-label {
  display: flex; align-items: center; justify-content: center;
  font-size: 48px; font-weight: 900; color: #1A1A1A;
  width: 60px;
}
</style>
</head>
<body>
  <p class="title">AI提效前后对比：周度复盘流程</p>
  <div class="compare">
    <div class="panel">
      <div class="panel-header before-header"><h2>Before（传统方式）</h2></div>
      <div class="panel-body">
        <ul>
          <li class="before-item"><p>手动从后台导出4个板块数据（30min）</p></li>
          <li class="before-item"><p>Excel透视表逐个做分析（2h）</p></li>
          <li class="before-item"><p>手写复盘报告（1.5h）</p></li>
          <li class="before-item"><p>做PPT汇报材料（2h）</p></li>
          <li class="before-item"><p>总计：约6小时</p></li>
        </ul>
      </div>
    </div>
    <div class="vs-label"><p>→</p></div>
    <div class="panel">
      <div class="panel-header after-header"><h2>After（AI辅助）</h2></div>
      <div class="panel-body">
        <ul>
          <li class="after-item"><p>导出数据 + AI自动分析（30min）</p></li>
          <li class="after-item"><p>AI生成复盘报告初稿（10min）</p></li>
          <li class="after-item"><p>人工校验 + 补充判断（30min）</p></li>
          <li class="after-item"><p>AI生成PPT + 微调（30min）</p></li>
          <li class="after-item"><p>总计：约1.5小时（省75%）</p></li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
```

截图：`--viewport-size=1200,500`

---

## 模板使用建议

| 场景 | 推荐模板 | 截图尺寸 |
|------|---------|---------|
| 数据概览/周报开头 | 模板1：KPI看板 | 1200×400 |
| 多维度对比 | 模板2：对比表格 | 1200×600 |
| 趋势展示 | 模板3：柱状/折线图 | 1200×500 |
| 问题诊断 | 模板4：诊断卡片 | 1200×700 |
| 流程说明 | 模板5：工作流图 | 1200×400 |
| 方案展示 | 模板6：Before/After | 1200×500 |

### 标准底部PDF导出提示

每个HTML报告页面底部添加PDF导出提示。要求：不干扰主体内容，极细小，仅浏览器查看时注意到。

```html
<!-- 放在 </body> 前 -->
<p style="position:fixed;bottom:2pt;right:12pt;font-size:6.5pt;color:#BBB;margin:0;letter-spacing:0.3pt;">
  Ctrl/Cmd + P 导出PDF
</p>
```

特点：
- `position:fixed` 固定在视口底部，不占文档流
- 6.5pt + #BBB 极低存在感，不影响截图视觉效果
- 打印时浏览器自带PDF功能，无需额外JS

### 自定义提示

- 替换数据时保持颜色语义（红=问题、绿=正常、金=关注）
- 标题始终是**结论**而非描述
- 中文字体用 `"PingFang SC", Arial, sans-serif`
- 深色模式：背景避免纯白（用 #F5F5F5）和纯黑（用 #1A1A2E）
