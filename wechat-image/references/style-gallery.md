# 公众号配图风格库

> 为微信公众号文章优化的风格库。核心原则：**描述情绪和美学参考，不要微操布局。** 特别注意深色模式兼容性。

## 第一梯队：强烈推荐

### 1. 极简专业 Clean Professional

**一句话**：白底 + 结构化布局 + 科技蓝，专业可信。

**封面 Base Style：**
```
VISUAL REFERENCE: Apple product page meets Monocle editorial — clean, authoritative, premium.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Center square (766x766) contains all key text and visuals.
COLOR SYSTEM: Soft light gray (#F5F5F5) background (NOT pure white), tech blue (#2563EB) accent, charcoal (#374151) text. Clean and breathable.
```

**正文 Base Style：**
```
VISUAL REFERENCE: Apple product page meets Monocle editorial.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Soft light gray (#F5F5F5) background, tech blue (#2563EB) accent. Information hierarchy is king.
DARK MODE: Use #F5F5F5 background instead of pure white for WeChat dark mode compatibility.
```

**适用**：教程、指南、工具对比、技术分享
**深色模式**：用 #F5F5F5 而非 #FFFFFF 可以缓解，但仍偏亮

---

### 2. 编辑杂志 Editorial Magazine

**一句话**：Kinfolk × Wired，高级感编辑排版。

**封面 Base Style：**
```
VISUAL REFERENCE: Kinfolk magazine cover meets Wired feature spread — sophisticated editorial design.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Center square (766x766) contains all key text and visuals.
COLOR SYSTEM: Muted sophisticated palette — warm cream, soft charcoal, one distinctive accent color. Feels curated and expensive.
```

**正文 Base Style：**
```
VISUAL REFERENCE: Long-form editorial feature from Wired or The Atlantic.
CANVAS: 4:3 landscape, 1440x1080 pixels, high quality rendering.
COLOR SYSTEM: Warm neutral background (#F5F0EB), dark charcoal (#2D2D2D) text areas, one muted accent. Premium editorial feel.
```

**适用**：深度分析、产品发布、行业观察、人物故事
**深色模式**：暖灰底天然友好

---

### 3. Snoopy 温暖漫画

**一句话**：Peanuts 风格，温暖有差异化，适合个人 IP。

**封面 Base Style：**
```
VISUAL REFERENCE: Charles Schulz Peanuts comic strip — warm, philosophical, charming.
Characters include round-headed kids, a lovable beagle dog, and a small yellow bird.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Center square (766x766) contains characters and title.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines. Sunday morning comic page feeling.
```

**正文 Base Style：**
```
VISUAL REFERENCE: Peanuts comic strip — warm, philosophical, charming.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Warm cream background, soft pastels, warm ink lines. Cozy and inviting.
```

**适用**：个人 IP、品牌故事、教育培训、温暖话题
**深色模式**：暖色调在深色模式下观感良好
**详细指南**：`image-to-slides/references/proven-styles-snoopy.md`

---

### 4. 大字报 Bold Statement

**一句话**：文字即画面，观点输出利器。

**封面 Base Style：**
```
VISUAL REFERENCE: Brutalist editorial magazine cover — text as primary visual element.
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Title must be centered in the 766x766 safe zone.
COLOR SYSTEM: Stark high contrast — dark background with light text, or vice versa. Minimal decoration.
```

**正文 Base Style：**
```
VISUAL REFERENCE: Brutalist editorial statement, typography-driven design.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: High contrast. Text is the hero element. Minimal background decoration.
```

**适用**：观点文、争议话题、金句、行业呼吁
**深色模式**：暗色底版本天然兼容

---

## 第二梯队：特定场景推荐

### 5. 数据信息图 Data Infographic

**一句话**：结构化数据展示，正文插图首选。

**正文 Base Style：**
```
VISUAL REFERENCE: The Economist data visualization meets Information is Beautiful.
CANVAS: 4:3 landscape, 1440x1080 pixels, high quality rendering.
COLOR SYSTEM: Clean neutral background, one primary data color, one accent for highlights. Information clarity above all.
```

**适用**：对比分析、数据展示、流程说明
**注意**：文字多的信息图推荐用 HTML → Playwright 截图路径

---

### 6. 手绘白板 Whiteboard Sketch

**正文 Base Style：**
```
VISUAL REFERENCE: xkcd meets professor's whiteboard — extreme minimalism, humor, insight.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: White background, black ink, ONE accent color (red or blue). 85% white space.
```

**适用**：技术解释、概念科普、架构图、流程图

---

### 7. 温暖叙事 Warm Narrative

**正文 Base Style：**
```
VISUAL REFERENCE: Airbnb brand presentation meets Mailchimp editorial — approachable, human, warm.
CANVAS: 16:9 landscape, 1920x1080 pixels, high quality rendering.
COLOR SYSTEM: Warm cream (#FDF6EC) background, coral (#E17055) accent, charcoal text. People-centric imagery.
```

**适用**：个人故事、用户案例、品牌内容

---

## 第三梯队：偶尔使用

| 风格 | 适用场景 | 封面/正文 |
|------|---------|----------|
| 苏联构成主义 | 产品发布、keynote 风 | 封面 |
| 新波普 Neo-Pop | 年轻受众、潮流科技 | 封面 |
| 学習漫画 Manga | 教程、培训 | 正文 |
| 清线 Ligne Claire | 流程说明、产品图 | 正文 |
| 等轴测 Isometric | 技术架构、系统图 | 正文 |

---

## 封面 vs 正文的风格搭配

同一篇文章中，封面和正文可以用不同但互补的风格：

| 封面风格 | 正文搭配 | 效果 |
|---------|---------|------|
| 极简专业 | 手绘白板 + 信息图 | 专业中有趣味 |
| 编辑杂志 | 温暖叙事 + 信息图 | 高级深度感 |
| Snoopy 漫画 | Snoopy 漫画（统一） | 强 IP 一致性 |
| 大字报 | 数据信息图 + 截图 | 冲击力 + 干货 |

---

## 公众号特有的 Prompt 注意事项

### 封面图专属
- 必须声明 `2.35:1 ultra-wide landscape`
- 必须提及 `center square safe zone`
- 标题放在中央区域（朋友圈裁切为正方形）
- 两侧可有装饰但不能放文字

### 正文图专属
- 声明 `DARK MODE: Use medium-tone backgrounds`
- 避免纯白 #FFFFFF 和纯黑 #000000
- 正文图文字可以少或没有（配合文章正文）
- 氛围/情感图 > 信息图（正文已有足够文字）

### 信息图专属
- 推荐 HTML → Playwright 路径（文字精确）
- AI 生成适合没有或少量文字的氛围图
- 4:3 比例更适合信息密集的内容
- 16:9 适合宽幅场景/全景

### 反模式

| 反模式 | 为什么不好 | 替代方案 |
|--------|-----------|---------|
| 纯白底正文图 | 深色模式下刺眼 | 用 #F5F5F5 或 #F0F4FF |
| 纯黑底封面 | 深色模式下融入背景消失 | 用 #1A1A2E 或 #2D2D2D |
| 封面边缘放标题 | 朋友圈裁切丢失 | 标题居中 |
| 一篇文章 3 种风格 | 视觉混乱 | 封面 + 正文最多 2 种互补风格 |
| "professional modern clean" | AI 生成毫无特色 | 引用具体出版物/品牌美学 |
