# 小红书配图风格库

> 经过调研和适配的小红书配图风格。核心原则与 image-to-slides 一致：**描述情绪和美学参考，不要微操布局细节。**

## 第一梯队：强烈推荐

### 1. 极简信息图 Clean Infographic

**一句话**：干净白底 + 结构化布局 + 色块强调，干货之王。

**Base Style Prompt：**
```
VISUAL REFERENCE: Clean data dashboard meets editorial infographic from Monocle magazine.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: Crisp white or light gray background, tech blue (#4A90D9) as primary accent, warm orange (#FF6B35) for emphasis, charcoal (#333333) for text. Clean, breathable, professional.
TEXT RENDERING: Clear typographic hierarchy — large bold heading, medium subheading, small body text. Information is king.
```

**封面 Prompt 示例：**
```
Create a clean infographic-style Xiaohongshu cover.

[Base Style]

DESIGN INTENT: The viewer should think "this looks organized and useful, I need to save this."

TEXT TO RENDER:
- Title: "Claude vs GPT"
- Subtitle: "重度用户的真实对比"

Structured layout with clear visual hierarchy. Data feels trustworthy and well-organized.
```

**适用**：教程、对比、数据、工具推荐
**注意**：信息密度要高，但不能杂乱

---

### 2. 大字报 Bold Typography

**一句话**：文字就是画面，高对比，一眼抓住注意力。

**Base Style Prompt：**
```
VISUAL REFERENCE: Brutalist magazine cover meets street poster typography.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: High contrast — either dark background with bright text, or bright background with dark text. Color is used sparingly but dramatically. The text IS the design.
TEXT RENDERING: Title occupies 50-70% of the image area. Typography is the primary visual element, not decoration.
```

**封面 Prompt 示例：**
```
Create a bold typography-driven Xiaohongshu cover.

[Base Style]

DESIGN INTENT: Stop the scroll. The viewer reads the title before they even decide to look at the image.

TEXT TO RENDER:
- Title: "别再用ChatGPT了"
- Subtitle: "这3个平替更强"

The title should hit like a headline. Minimal decoration — the words carry all the weight.
```

**适用**：观点输出、标题党、金句、争议性话题
**注意**：文字越少越好（3-5字最佳），留白很重要

---

### 3. 杂志排版 Magazine Layout

**一句话**：高级感编辑排版，留白考究，字体层级清晰。

**Base Style Prompt：**
```
VISUAL REFERENCE: Kinfolk magazine meets Apple product page — elegant, minimal, editorial.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: Muted sophisticated palette — warm whites, soft grays, one muted accent color. Feels expensive and curated.
TEXT RENDERING: Elegant typography with clear hierarchy — display title, deck text, body. Generous letter-spacing and line-height.
```

**适用**：知识分享、生活方式、品牌内容
**注意**：内容要精炼，不能塞太多信息

---

### 4. Snoopy 温暖漫画

**一句话**：Peanuts 风格温暖插画，亲和力强，适合个人 IP。

**Base Style Prompt：**
```
VISUAL REFERENCE: Charles Schulz Peanuts comic strip — warm, philosophical, charming.
Characters include round-headed kids, a lovable beagle dog, and a small yellow bird.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines. Sunday morning comic page feeling.
TEXT RENDERING: Hand-lettered style title, warm and inviting.
```

**适用**：个人 IP 打造、故事分享、温暖话题
**详细指南**：参见 `image-to-slides/references/proven-styles-snoopy.md`

---

## 第二梯队：特定场景推荐

### 5. 新波普 Neo-Pop

**一句话**：高饱和色块 + 粗边框，潮流年轻感。

**Base Style Prompt：**
```
VISUAL REFERENCE: Supreme lookbook meets HYPEBEAST editorial — bold, playful, street.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: Cream background with aggressive color blocking — hot pink, cyan, yellow. Thick black borders frame everything. Typography is the visual.
TEXT RENDERING: Headlines as graphic art — oversized, bold, with thick black outlines.
```

**适用**：年轻受众、潮流科技、品牌联名
**注意**：信息量不能太高，以视觉冲击为主

---

### 6. 手绘白板 Whiteboard Sketch

**一句话**：xkcd/手绘风，极简但有趣。

**Base Style Prompt：**
```
VISUAL REFERENCE: xkcd meets a professor's whiteboard — extreme minimalism, humor, clarity.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: White background, black ink, ONE accent color for emphasis (red or blue). 85% white space.
TEXT RENDERING: Hand-drawn/handwritten feel, rough baselines, arrows and annotations.
```

**适用**：技术解释、概念科普、趣味教程

---

### 7. 学习漫画 Educational Manga

**一句话**：日式学习漫画，角色引导理解概念。

**Base Style Prompt：**
```
VISUAL REFERENCE: Japanese educational manga (学習漫画) — a character guides you through the concept.
CANVAS: 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.
COLOR SYSTEM: Bright warm palette, white background with selective color panels, screen-tone gray.
TEXT RENDERING: Bold manga-style titles, speech bubbles for key points, onomatopoeia as decoration.
```

**适用**：教程、培训、知识科普

---

## 第三梯队：偶尔使用

| 风格 | 一句话 | 适用 |
|------|--------|------|
| 苏联构成主义 | 革命海报风，几何+有限色彩 | 产品发布、keynote风 |
| 像素画 | 8-bit复古游戏感 | 游戏相关、怀旧 |
| 孔版印刷 | 错版套色、纸张质感 | 文艺、设计 |
| 浮世绘 | 日本传统木版画 | 东方美学 |
| 达达拼贴 | 混搭拼贴、反主流 | 创意、实验性 |

---

## 轮播套图的一致性规则

1. **同一 Base Style** — 所有页面共享同一个 Base Style Prompt
2. **色板固定** — 整组不超过 4 种颜色
3. **布局框架一致** — 标题位置、字号层级保持一致
4. **封面最抢眼** — 第1张信息密度最高、视觉冲击最强
5. **末页做引导** — 最后一张放互动引导（关注/收藏/评论）
6. **序号感** — 如果是步骤类，每页标注页码（01/02/03...）

## Prompt 反模式（小红书特有）

| 反模式 | 为什么不好 | 替代方案 |
|--------|-----------|---------|
| "professional modern clean" | AI 生成出来毫无特色 | 引用具体美学/出版物 |
| 指定文字像素位置 | AI 不按坐标放 | 描述信息层级 |
| 横版构图描述 | 生成出来是横图 | 明确写 "3:4 portrait" |
| 一次渲染超过 30 字 | 中文乱码概率大增 | 分拆成多行短文字 |
| 封面和内页用不同风格 | 套图观感割裂 | 统一 Base Style |
