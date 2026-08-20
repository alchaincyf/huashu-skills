---
name: huashu-slides
description: 从内容到成品PPTX的端到端演示文稿制作，含AI插画生成和18种设计风格。当用户提到"做PPT"、"做幻灯片"、"演示文稿"、"Keynote"、"slides"时使用。
---

# AI Presentation Workflow

Create professional presentations: Content → Design → Build → Assembly → Polish.

## Step 0: Choose Workflow Settings

**At the start of every presentation task, ask the user TWO choices:**

### 0-A. Collaboration Mode

| Mode | Description | Checkpoints |
|------|-------------|-------------|
| **Full Auto** | Minimal interaction. Confirm topic only, deliver final PPTX. | 1 checkpoint |
| **Guided** (recommended) | Confirm outline, pick design, preview before assembly. | 3 checkpoints |
| **Collaborative** | Review every slide, approve every illustration, full control. | Per-slide |

If the user doesn't specify, default to **Guided** mode.

### 0-B. Assembly Method

| Method | How it works | Best for |
|--------|-------------|----------|
| **Editable HTML** (Path A) | HTML slides + selective AI illustrations → html2pptx → editable PPTX | Need to edit text later, precise layout, corporate decks |
| **Full AI Visual** (Path B) | Every slide as a complete AI-generated image → create_slides.py → image PPTX | Maximum visual impact, artistic presentations, quick drafts |

**Trade-offs:**

| | Path A: Editable HTML | Path B: Full AI Visual |
|---|---|---|
| Text | Editable in PPT | Baked into image (not editable) |
| Visual quality | Good with illustrations | Excellent — cohesive design |
| Layout control | Pixel-precise | AI-interpreted |
| File size | Smaller (~5-25MB) | Larger (~30-80MB) |
| Chinese text | Perfect (font rendering) | Usually good (AI may occasionally misrender) |
| Speed | Faster (HTML creation) | Slower (image generation per slide) |

If the user doesn't specify, default to **Path A** (Editable HTML).

---

## Step 1: Content Structuring

Turn raw material into a slide-by-slide outline.

**Per slide, define:**
- **Title** — a complete assertion sentence (not a topic word)
- **Key points** — 3-4 maximum
- **Visual type** — illustration / chart / diagram / icon / quote
- **Path A:** Illustration needed? — Yes/No. If yes, one-line description.
- **Path B:** Visual scene description — one paragraph describing the complete slide visual (layout + imagery + mood).

**Assertion-Evidence rule:**

| Bad title | Good title |
|-----------|-----------|
| Q3 Sales | Q3销售增长23%，新用户是主要驱动力 |
| Methodology | 我们通过双盲实验验证了这个结论 |

**语言规则：slide内容一律用中文，仅保留必要的英文术语（人名、品牌名、技术专有名词）。** Section label（如 INSIGHT、TAKEAWAY）可用英文作为设计元素。

### ✅ Checkpoint 1 (Guided + Collaborative)

Present the outline as a table:

**Path A:**
```
| # | Title (assertion) | Key Points | Visual Type | Illustration? |
|---|-------------------|------------|-------------|---------------|
| 1 | Cover: ... | — | Decorative | Yes: ... |
| 2 | ... | 1. ... 2. ... | Chart | No |
| 3 | ... | 1. ... 2. ... | Illustration | Yes: ... |
```

**Path B:**
```
| # | Title (assertion) | Key Points | Visual Scene Description |
|---|-------------------|------------|--------------------------|
| 1 | Cover: ... | — | Dark gradient bg, large title centered, abstract network nodes |
| 2 | ... | 1. ... 2. ... | Split layout: text left, bar chart right, clean white bg |
| 3 | ... | 1. ... 2. ... | Full illustration: person at crossroads with floating clocks |
```

**Ask the user:**
- Approve / adjust slide count
- Path A: Approve / adjust which slides get illustrations
- Path B: Approve / adjust visual scene descriptions
- Any content to add or remove

---

## Step 2: Design System

**Present 3 design system options for the user to choose from.** Each is a complete visual language, not just a color palette.

**CRITICAL: A design system is NOT just colors.** It defines visual philosophy, typography ratios, composition rules, and emotional intent. This is the difference between "boring PPT" and "magazine-quality deck."

### 🗣️ Style Discussion (Optional, if user wants to explore)

**If the user says things like:**
- "我想要XX风格"（田中一光、瑞士国际主义、包豪斯、蒙德里安...）
- "我不确定想要什么风格"
- "能给我看看不同风格的例子吗"

**Then consult the design movements reference:**
`references/design-movements.md` — 设计运动与风格参考库

This file maps classic design movements (Neo-Brutalism, Swiss Style, Bauhaus, etc.) to our AI-ready style presets. Use it to:
1. Translate user's aesthetic language into actionable prompts
2. Build shared vocabulary ("这个方向偏田中一光" vs "那个偏构成主义")
3. Reference when designing new custom styles from scratch

**After discussing movements, proceed to recommend 3 concrete presets below.**

---

### Design System Presets

**⚠️ CRITICAL INSIGHT: 插画/漫画类风格的AI生成效果远好于「专业极简」类风格。**
漫画/插画风格有明确的视觉语言（线条、角色、色块），AI可以充分发挥；极简风格（暗色底+发光文字+大量留白）缺乏视觉元素，生成出来「空」且「平」。

Pick 3 that match the topic/mood. Use the **topic recommendation table** below, then present each with its full description.

**按主题自动推荐（优先从此表选）：**

| 主题类型 | 第一推荐 | 第二推荐 | 第三推荐 |
|---------|---------|---------|---------|
| 品牌/产品介绍 | Snoopy温暖漫画 | Neo-Pop新波普 | 浮世绘/敦煌（东方品牌） |
| 教育/培训 | Neo-Brutalism | 学習漫画 | Snoopy温暖漫画 |
| 技术分享 | xkcd白板 | Neo-Brutalism | Ligne Claire |
| 数据报告 | **Pentagram编辑** | **Fathom数据** | Ligne Claire |
| 年轻受众 | Neo-Pop | 像素画 | 孔版印刷 |
| 创意/艺术 | 达达拼贴 | 孔版印刷 | The Oatmeal |
| 国风/东方 | 敦煌壁画 | 浮世绘 | **Takram思辨** |
| 正式商务 | **Pentagram编辑** | **Müller-Brockmann网格** | **Build极简** |
| 产品发布/keynote | 苏联构成主义 | Neo-Pop | **Pentagram编辑** |
| 内部分享 | Neo-Brutalism | The Oatmeal | xkcd白板 |
| 行业分析/咨询 | **Fathom数据** | **Pentagram编辑** | **Müller-Brockmann网格** |
| 培训课件/教材 | **Takram思辨** | 温暖叙事 | 学習漫画 |
| 投资/融资路演 | **Build极简** | **Pentagram编辑** | 苏联构成主义 |

**完整18种风格详细参考：** `references/proven-styles-gallery.md`
**风格样例图片：** `assets/style-samples/` 目录

---

**第一梯队（强烈推荐，效果极好）：**

**1. Warm Comic Strip** — Snoopy温暖漫画风
- Philosophy: Peanuts漫画的温暖与哲理感——简单的角色说着深刻的话，日常场景中蕴含人生智慧
- Visual world: 圆头小孩、小狗、小鸟组成一个温暖的小世界。背景极简（草地、天空、狗屋、树）。色调像泛黄的报纸漫画
- Reference: "Like a Peanuts comic strip — warm, philosophical, charming"
- **Style guide:** `references/proven-styles-snoopy.md`
- **⚠️ 关键经验：** 不要在prompt中过度约束视觉细节（颜色比例、构图位置、角色姿势），否则会严重降低多样性。只描述情绪和内容，让AI自由发挥

**2. Manga Educational** — 学習漫画风
- Philosophy: Japanese educational manga (学習漫画) — a character GUIDES you through the concept with reactions and drama
- Colors: Bright and warm palette, white bg with selective color panels, screen-tone gray for emphasis areas
- Ratio: 60% illustration / 30% text (in bubbles) / 10% effects
- Typography: Bold manga-style titles with impact, body text in speech/thought bubbles, onomatopoeia as decorative elements. Size contrast 3:1
- Composition: Dynamic manga panel layouts (3-5 panels per slide), character reactions drive emphasis, speed lines for energy, dramatic angles
- Visual language: Expressive anime-style characters, reaction faces (surprise, confusion, eureka!), manga effects (sweat drops, sparkles, speed lines), panel borders with varied thickness
- Reference: "Like a 'Manga Guide to Statistics' page — a character walks you through the concept, reacting with surprise and delight"

**3. Ligne Claire Comics** — 清线漫画风
- Philosophy: Hergé's Tintin tradition — maximum information clarity through visual restraint
- Colors: White/cream (#FFFDF7) bg, black (#000000) outlines, flat saturated fills (3-5 solid colors, no gradients)
- Ratio: 70% clean bg / 20% illustration / 10% text
- Typography: Hand-lettered feel for titles, clean sans-serif for body. Speech bubbles for key quotes. Title:body = 2.5:1
- Composition: Panel-based layouts (2-4 panels per slide), sequential left-to-right reading flow, clear gutters between panels
- Visual language: Uniform-weight outlines, flat colors without shading or hatching, no gradients, precise details but zero visual noise
- Reference: "Like a Tintin page explaining a concept — every panel advances understanding, nothing is decorative"

**4. Neo-Pop Magazine** — 新波普杂志风
- Philosophy: Youth media / streetwear brand aesthetic, bold and playful
- Colors: Cream (#FFF8E7) bg, black (#000000) text, color-blocking with hot pink (#FF1493) + cyan (#00CED1) + yellow (#FFD700)
- Ratio: 50% bg / 25% color blocks / 25% content
- Typography: Headlines 40-50% of slide area (typography AS the visual), thick black borders around text blocks, 10:1 size ratio vs body
- Composition: Modular color blocks with "controlled chaos", stacked asymmetric layouts, thick borders
- Visual language: Pixel-art 8-bit icons, cutout photography, speech bubbles, bold graphic surfaces
- Reference: "Like a Supreme lookbook meets a HYPEBEAST article — treats typography as graphic art"

**第二梯队（推荐，特定场景效果好）：**

**5. Whiteboard Sketch** — xkcd白板手绘风
- Philosophy: xkcd meets a professor's whiteboard — extreme minimalism forces focus on the idea itself
- Colors: White (#FFFFFF) bg, black (#000000) ink, ONE accent color for emphasis (red #FF4444 or blue #4488FF)
- Ratio: 85% white space / 10% sketch / 5% accent highlight
- Typography: Hand-drawn/handwritten feel for everything, rough uneven baselines, arrows and annotations everywhere. Key numbers can be large (60pt+)
- Composition: Freeform whiteboard layout, hand-drawn arrows connecting concepts, diagrams and stick figures, informal and alive
- Visual language: Stick figures, hand-drawn charts and graphs, wobbly lines, annotation arrows, circled keywords, equation-style layouts
- Reference: "Like an xkcd 'What If?' explanation — simple drawings that make complex ideas instantly click"

**6. Soviet Constructivism** — 苏联构成主义
- Philosophy: Revolutionary propaganda poster — power through geometry and limited color
- Colors: Revolutionary red (#CC0000) 40% + black (#1A1A1A) 25% + cream white (#F5E6D3) 30%
- Typography: All text rotated 15-30 degrees, NO horizontal lines, bold condensed
- Composition: Diagonal wedge from bottom-left to top-right, geometric shapes growing small to large (visual crescendo)
- Visual language: NO gradients, pure flat fills + sharp edges, three-color limit, propaganda poster energy
- Reference: "Like a 1920s Rodchenko poster — power, urgency, and geometric precision"

**7. Warm Narrative** — 温暖叙事风
- Philosophy: Friendly storytelling, like a TED talk visual or Airbnb pitch deck
- Colors: Warm cream (#FDF6EC) bg, dark charcoal (#3D3D3D) text, coral (#E17055) accent
- Ratio: 60% warm bg / 25% content / 15% illustration
- Typography: Headlines bold and warm, 3:1 ratio to body. Short sentences, not bullets
- Composition: Illustration occupies 40-50% of slide, text wraps around visuals, rounded shapes
- Visual language: Flat vector illustrations with warm palette, people-centric imagery, storytelling flow
- Reference: "Like a Mailchimp or Notion brand presentation — approachable and human"

**更多风格（第二/三梯队）** 详见 `references/proven-styles-gallery.md`，包括：The Oatmeal信息图漫画、敦煌壁画、浮世绘、孔版印刷Risograph、等轴测Isometric、Bauhaus包豪斯、工程蓝图Blueprint、复古广告Vintage Ad、达达拼贴Collage、像素画Pixel Art

---

**第四类：Professional / Editorial 设计系统（Path A 专用）**

> ⚠️ 以下风格 **强烈建议使用 Path A（HTML→PPTX）**。它们依赖精确排版、数据可视化和网格系统，AI图片生成无法达到所需精度。口腔行业分析案例已验证 Path A + Pentagram编辑风格的出色效果。

**8. Pentagram Editorial** — 编辑杂志风（信息建筑派）
- Philosophy: Pentagram/Michael Bierut — 字体即语言，网格即思想。用极度克制的设计让数据和内容自己说话
- Colors: 奶油白(#FFFDF7) bg, 近黑(#1A1A1A) text, ONE accent color (如橙红#D4480B或品牌色)
- Ratio: 60% whitespace / 30% content / 10% accent
- Typography: 粗黑标题(28pt+) + 轻正文(10-13pt), 英文section label作为设计元素 (INSIGHT / PART 03)
- Composition: 瑞士网格系统, 2px黑色边框卡片, 精确的水平分隔线, 数据可视化内嵌
- Visual language: 极简图标, 条形图/饼图/趋势线, callout框, tag标签
- Reference: "Like a McKinsey insight report meets Monocle magazine — data-rich but editorially elegant"
- **执行路径: Path A only（HTML→PPTX）**
- **实战验证**: 口腔行业分析15页deck（`_temp/口腔行业分析/slides/`）

**9. Fathom Data Narrative** — 数据叙事风（科学期刊派）
- Philosophy: Fathom Information Design — 每一个像素都必须承载信息。科学严谨+设计优雅
- Colors: 白(#FFFFFF) bg, 深灰(#333) text, 海军蓝(#1A365D) primary + 一个highlight color
- Ratio: 50% charts/data / 30% text / 20% whitespace
- Typography: GT America/Graphik风格的sans-serif, 大数字(60pt+)作为视觉锚点, 精确的脚注/来源标注
- Composition: 高信息密度但不拥挤, 注释系统嵌入布局, small multiples图表阵列, 精确的时间线
- Visual language: 散点图, 热力图, timeline, 带注释的图表, 数据标签精确到小数
- Reference: "Like a Nature paper's data supplement meets a Bloomberg data feature"
- **执行路径: Path A only（HTML→PPTX）**

**10. Müller-Brockmann Grid** — 瑞士网格风（纯粹主义派）
- Philosophy: Josef Müller-Brockmann — 客观性即美。数学精确的网格系统让任何混乱的信息变得有序
- Colors: 白(#FFFFFF) bg, 黑(#000) text, 最多一个强调色
- Ratio: 70% structured grid / 20% text / 10% accent
- Typography: Akzidenz-Grotesk/Helvetica, 严格的8pt基线网格, 绝对左对齐, 字重对比(300 vs 700)
- Composition: 8列数学网格, 所有元素对齐到网格线, 绝对不允许装饰元素, 功能主义至上
- Visual language: 纯几何图形, 黑色线条表格, 精确对齐的列表, 无图标无插画
- Reference: "Like the original Swiss Style poster — timeless, rational, zero decoration"
- **执行路径: Path A only（HTML→PPTX）**

**11. Build Luxury Minimal** — 奢侈极简风（当代品牌派）
- Philosophy: Build Studio — 精致的简单比复杂更难。用大量留白和微妙字重变化传达高端感
- Colors: 纯白(#FFFFFF) bg, 深灰(#2D2D2D) text, 单一accent(品牌色)极少量使用
- Ratio: 75% whitespace / 15% text / 10% accent
- Typography: 字重变化极微妙(200-600), 标题巨大(48pt+)但轻, 正文小而精(12pt), 字间距宽松
- Composition: 黄金比例构图, 元素极少, 每页只说一件事, 呼吸感优先
- Visual language: 高端产品图(如果有), 极简图标线条, 大面积纯色块, 圆角卡片
- Reference: "Like an Apple keynote meets a Celine lookbook — confident restraint"
- **执行路径: Path A（HTML→PPTX）**

**12. Takram Speculative** — 日式思辨风（东方哲学派）
- Philosophy: Takram — 技术是思考的媒介。用柔和的科技感和概念原型图传达深度思考
- Colors: 暖灰(#F5F3EF) bg, 深灰(#3D3D3D) text, 鼠尾草绿(#8B9D77) accent
- Ratio: 55% warm bg / 25% diagrams / 20% text
- Typography: 圆润的sans-serif, 标题不用粗体而用大尺寸(36pt+), 正文温暖(14pt), 行高宽松(1.8)
- Composition: 柔和阴影(blur 20px+), 圆角(16px+), 概念图/流程图作为核心视觉, 卡片式布局
- Visual language: 概念原型图, 柔和渐变, 流程图即艺术, 手绘感图标, 自然色调
- Reference: "Like a Takram project page — where technology feels thoughtful, not aggressive"
- **执行路径: Path A（HTML→PPTX，配图可AI辅助生成）**

**更深入的风格细节**：参考 `design-philosophy` skill 的 `references/design-styles.md`，包含20种设计哲学的完整提示词DNA

### 🎨 Custom Character Style (User-Defined)

Users may want to reference specific cartoon/anime aesthetics. When a user says "do it in Doraemon style" or "like Studio Ghibli", treat this as a **style reference**, not a request to draw copyrighted characters. Build a custom Design System by extracting the visual DNA of that style.

**How to convert a character reference into a Design System:**

| User says | Extract these visual traits |
|-----------|---------------------------|
| "Doraemon style" | Round shapes, bright primary blue + white + red, simple backgrounds, cute proportions, magical gadget reveals |
| "Studio Ghibli" | Watercolor textures, natural greens and sky blues, detailed backgrounds with simple characters, warmth and wonder |
| "Calvin and Hobbes" | Dynamic ink brushwork, expressive motion lines, philosophical contrast between fantasy and reality, lush outdoor scenes |
| "One Piece manga" | Bold dynamic lines, exaggerated proportions, dramatic action poses, high energy, thick outlines |
| "Crayon Shin-chan" | Crude crayon-like lines, flat bright colors, comedic proportions, everyday scenarios made absurd |
| "Adventure Time" | Geometric simple shapes, pastel candy colors, thin outlines, whimsical surreal backgrounds |

**Template for custom style:**
```
[User Style]: "[reference name]"
→ Shape language: [round/angular/geometric/organic]
→ Line quality: [thin uniform / thick varied / sketchy / brushwork]
→ Color palette: [specific colors extracted from that aesthetic]
→ Character style: [proportions, expressiveness level]
→ Background treatment: [detailed/minimal/abstract]
→ Emotional tone: [warm/energetic/philosophical/surreal]
```

### Typography Rules (All Presets)

- Max 2 font families (1 heading + 1 body)
- Heading: bold, personality — ≥36pt (trend: even larger, as graphic surface)
- Body: clean, readable — ≥18pt
- Chinese: system default (PingFang SC / Microsoft YaHei)
- **Key principle**: Typography is a DESIGN ELEMENT, not just an information container

### ✅ Checkpoint 2 (Guided + Collaborative)

**Ask the user to pick one of the 3 proposed design systems**, or describe their own preference. Show the full description including philosophy, visual language, and reference.

---

## Step 3: Build Slides

---

### Step 3-A: HTML + Selective Illustrations (Path A)

Generate AI illustrations for key slides, then create HTML slide files.

**Which slides need illustrations?** Prioritize:
1. **Cover slide** — always. Sets the visual tone.
2. **Key insight slides** — the "aha moment" slides benefit most.
3. **Closing slide** — optional but impactful.
4. **Data-heavy slides** — charts/diagrams instead of AI art.

**Illustration Generation** — use `nano-banana-pro` skill:

> ⚠️ `nano-banana-pro` 是一个独立的外部 skill，**不随本仓库分发**。如果你的 `~/.claude/skills/` 下没有它，直接用本仓库自带的等价脚本（同样调用 Gemini 3 Pro Image API，默认 16:9，正好适配 slides）：
> `uv run <本仓库路径>/huashu-wechat-image/scripts/generate_image.py --prompt "..." --filename "..." --resolution 2K`

```bash
export $(grep GEMINI_API_KEY ~/.claude/.env) && \
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "[description]" \
  --filename "[timestamp]-slide-[N]-[name].png" \
  --resolution 2K
```

**Base Style Prompt** — define ONE style suffix, append to every illustration:

```
[Base Style]: flat vector illustration, [palette background color] background,
[accent color] highlight elements, clean minimalist aesthetic,
professional presentation style, no text in image
```

**Per-slide prompt = [specific content] + [Base Style]**

**Key rules:**
- Always include "no text in image" — text will be added as editable elements
- Use descriptive paragraphs, not keyword lists
- Specify hex colors explicitly
- Use "flat vector" / "flat illustration" for consistency

**Embedding in HTML slides:**

```html
<!-- Side illustration (recommended) -->
<div class="left"><!-- text content --></div>
<div class="right"><img src="illustration.png" style="width: 280pt; height: 280pt;"></div>

<!-- Background illustration -->
<body style="background-image: url('illustration.png'); background-size: cover;">
```

**✅ Checkpoint 3-A** (Guided: preview 2-3 key illustrations; Collaborative: every one)

Show generated illustrations. Ask: Approve / regenerate / style consistent?

---

### Step 3-B: Full AI Slide Generation (Path B)

Generate EVERY slide as a complete AI image — layout, text, visuals, all in one.

**⚠️ THE #1 MISTAKE: Over-constraining the prompt with layout details and visual restrictions.**
More constraints = LESS creativity and diversity. The AI generates best when given mood + reference + content, NOT specific positions, color ratios, or character restrictions.

#### The Golden Rule of AI Image Prompts

**SHORT prompts > LONG prompts.** A 3-sentence prompt describing mood and content produces better results than a 30-line prompt specifying every visual detail. Specifically:

| DON'T (kills diversity) | DO (enables creativity) |
|---|---|
| Specify color ratios (60%/25%/15%) | Describe the mood ("warm like a Sunday comic page") |
| Dictate layout positions ("title centered, image on right") | Reference a specific aesthetic ("Peanuts comic strip") |
| Restrict characters ("NOT Snoopy — an original character") | Let AI interpret the style naturally |
| List every visual element to include | Describe what the viewer should FEEL |
| Repeat the base style in every per-slide prompt | Define base style once, keep per-slide prompts short |

#### Base Style Prompt — Keep it SHORT

Define a base style once, append to every slide. **Keep it under 5 lines.** The base style sets the mood; per-slide prompts add the content.

```
[Base Style]:
VISUAL REFERENCE: [Specific art/design aesthetic in one sentence]
CANVAS: 16:9 aspect ratio, 2048x1152 pixels, high quality rendering.
COLOR SYSTEM: [Describe the mood/feel of colors, not exact ratios]
```

**Example (good — concise):**
```
VISUAL REFERENCE: Charles Schulz Peanuts comic strip — warm, philosophical, charming.
Characters include round-headed kids, a lovable beagle dog, and a small yellow bird.
CANVAS: 16:9 aspect ratio, 2048x1152 pixels, high quality rendering.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines.
```

**Anti-pattern (bad — over-specified):** Do NOT include typography sizes, color ratios, composition percentages, margin specifications, or visual weight distributions in the base style. These constraints reduce diversity without improving quality.

#### Per-Slide Prompt Structure

Keep per-slide prompts **short and focused**. Do NOT repeat base style details or over-specify visual layout.

```
Create a [style] slide about [topic].

[Base Style]

DESIGN INTENT: [1 sentence — what the viewer should FEEL]

TEXT TO RENDER:
- Title: "[exact text]"
- Body: "[exact text]"

[Optional: 1-2 sentences describing mood or scene. Let AI decide composition.]
```

#### Example — GOOD vs BAD

**BAD (traditional PPT — boring):**
```
Design a professional presentation slide.
Professional presentation slide, 16:9 aspect ratio, 2048x1152 pixels.
Dark navy background, light gray text, gold accent.
Slide type: content. Layout: Title at top-left, two columns below.
Title: "看涨期权收益结构"
Body: "行权价: 100元, 权利金: 10元"
Visual: a line chart showing call option payoff
```
→ Result: Generic PPT that could come from any template

**GOOD (magazine-level — stunning):**
```
Create a slide that feels like a Bloomberg terminal data visualization
brought to life as editorial art.

VISUAL REFERENCE: Bloomberg Businessweek data feature meets cinematic lighting.
CANVAS: 16:9, 2048x1152, sharp rendering.
COLOR SYSTEM: Deep black (#0A0A0A) background 75%, white text 15%,
gold (#BF9A4A) accent 10%. The gold represents profit — it should GLOW.
TYPOGRAPHY: The number "110" rendered at 100pt as the dominant visual anchor
(the break-even point IS the story). Supporting text at 14pt, muted gray.

DESIGN INTENT: The viewer should instantly FEEL the asymmetry of options —
limited downside, unlimited upside. The visual must make this visceral,
not just informational.

TEXT TO RENDER:
- Hero metric: "110" (giant, gold, the break-even price)
- Title: "盈亏平衡点" (medium, white, above the number)
- Left data: "行权价 100" "权利金 10" (small, gray, understated)
- Insight: "亏损有底 盈利无限" (accent color, bottom)

VISUAL NARRATIVE: A single golden curve emerges from the left side of the slide,
flat and muted in gray at -10 (the maximum loss), then suddenly bending upward
at the strike price, transitioning from gray to brilliant gold as it rises
into the profit zone. The curve should feel like a ray of light breaking
through darkness. The profitable area above zero glows with warm gold
atmospheric lighting, like sunrise. The chart has NO grid lines, NO axes labels
cluttering the visual — just the pure, dramatic curve and the giant "110"
floating at the inflection point.
```
→ Result: An editorial data visualization that tells a story

#### Key Rules for Path B Prompts

**Prompt Quality Checklist (verify before every generation):**

1. **Visual Reference** — Does the prompt name a specific art style or publication? (NOT just "professional" or "modern")
2. **Mood, not Layout** — Does the prompt describe what the viewer should FEEL, not where elements should be PLACED?
3. **Text Content** — Are all texts to render listed clearly and accurately?
4. **Short Enough** — Is the prompt concise? Long prompts with detailed specs REDUCE diversity. Remove anything the AI can decide on its own.
5. **NO Micro-Management** — No hex color ratios, no typography sizes, no composition percentages, no character pose instructions.

**Technical Rules:**
- **Always specify resolution**: `2048x1152` (2K, 16:9) for crisp text
- **Include ALL text verbatim** — AI must render exact words
- **中文优先**: slide上的文字一律用中文，仅保留必要英文术语
- **Chinese text tip**: Keep titles short (≤8 characters) for best rendering
- **Use descriptive paragraphs**, not keyword lists
- **Generate in parallel**: Run 3-5 slide generations concurrently for speed
- **Consistency**: The Base Style is applied to EVERY slide. It's a system, not a suggestion

**Generation command** (same tool, but full-slide prompts):

```bash
export $(grep GEMINI_API_KEY ~/.claude/.env) && \
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "[full slide prompt]" \
  --filename "slide-[NN]-[name].png" \
  --resolution 2K
```

> 没有 `nano-banana-pro` 时同样可换用本仓库的 `huashu-wechat-image/scripts/generate_image.py`（见 Step 3-A 的说明）。

**Quality check after generation:**
1. **Text accuracy** — verify all Chinese/English text rendered correctly
2. **Layout** — elements positioned as described
3. **Style consistency** — colors and design language match across slides
4. If a slide has text errors → regenerate with adjusted prompt (simplify text or shorten)

**✅ Checkpoint 3-B** (Guided: preview all slides as a set; Collaborative: approve each)

Show ALL generated slide images to the user. Ask:
- Text readable and accurate?
- Visual style consistent across slides?
- Any slides to regenerate?

---

## Step 4: PPTX Assembly

### 4-A: html2pptx Workflow (Path A)

Create HTML files per slide, convert with `html2pptx.js`:

```javascript
const pptxgen = require('pptxgenjs');
const html2pptx = require(process.env.HOME + '/.agents/skills/pptx/scripts/html2pptx.js');

const pptx = new pptxgen();
pptx.layout = 'LAYOUT_16x9';
await html2pptx('slide1.html', pptx);
await html2pptx('slide2.html', pptx);
await pptx.writeFile({ fileName: 'output.pptx' });
```

**HTML rules** (from pptx skill):
- Body dimensions: `width: 720pt; height: 405pt` (16:9)
- ALL text must be in `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>` tags
- Backgrounds/borders only on `<div>` elements
- No CSS gradients — pre-render as PNG with Sharp
- Use web-safe fonts only (Arial, Helvetica, Georgia, etc.)
- Images: `<img src="illustration.png" style="width: Xpt; height: Ypt;">`

**Known issue:** Chinese characters in file paths can break image loading. Use symlinks to ASCII paths if needed:
```bash
ln -sf "/path/with/中文/" /tmp/ascii-path
```

### 4-B: Image Assembly (Path B)

Assemble generated slide images into PPTX using `create_slides.py`:

```bash
uv run ~/.claude/skills/image-to-slides/scripts/create_slides.py \
  slide-01-cover.png slide-02-intro.png slide-03-definition.png ... \
  --layout fullscreen \
  --bg-color 000000 \
  -o output.pptx
```

**Recommended layout for Path B: `fullscreen`** — images fill the entire slide since they already contain all layout, text, and visuals.

| Layout | Use case |
|--------|----------|
| `fullscreen` | AI-generated full-page slides (Path B default) |
| `title_above` | Image + editable title (hybrid approach) |
| `title_left` | Split: text + visual |
| `center` | Centered image with padding |
| `grid` | Multiple images per slide |

---

## Step 5: Preview & Polish

### Preview

**Path A:** Screenshot 3-4 key HTML slides with Playwright:
```bash
npx playwright screenshot "file:///path/to/slide.html" preview.png \
  --viewport-size=960,540 --wait-for-timeout=1000
```

**Path B:** Show the generated slide images directly (they ARE the slides). Use `Read` tool to display 3-4 key PNGs.

### ✅ Checkpoint 4 (All modes)

**Show preview to the user.** The PPTX file is ready — ask:
- Any slides to adjust?
- Ready to open in Keynote/PowerPoint?

### Final Polish (in Keynote/PowerPoint)
- Transitions and animations
- Speaker notes
- Brand logo placement
- Path A: Final text adjustments (editable)
- Path B: Text NOT editable — if text errors found, regenerate the slide image

---

## Design Quick Reference

**5/5/5 rule:** ≤5 words/line, ≤5 bullets/slide, ≤5 text-heavy slides in a row

**Cognitive load:** One idea per slide. ~1 min per slide. Slides complement speech, never duplicate it.

**Visual hierarchy:** F/Z-pattern reading flow. Title:body size ≈ 3:1. Every slide should have a visual element.

**Detailed references:**
- `references/proven-styles-gallery.md` — 17 tested visual styles with tiered recommendations
- `references/proven-styles-snoopy.md` — Snoopy/Peanuts style detailed per-slide templates
- `references/prompt-templates.md` — Content generation and image prompts
- `references/design-principles.md` — Full design framework, color palettes, typography

## Related Skills

| Skill | Role |
|-------|------|
| `pptx` | Advanced PPTX creation/editing (html2pptx, templates) |
| `nano-banana-pro` | AI illustration generation (Gemini 3 Pro Image)。外部 skill 不随本仓库分发，未安装时用本仓库 `huashu-wechat-image/scripts/generate_image.py` 代替 |
| `multi-model` | External AI for content drafting |
| `design-philosophy` | 20种设计哲学深度参考（风格DNA + 场景模板 + 评审标准）。Professional/Editorial风格的详细提示词和评审指南在此 |

## Output

- `.pptx` files compatible with PowerPoint, Keynote, Google Slides
- Web-safe fonts for cross-platform compatibility
- AI illustrations as separate PNG files (reusable)

---

> **花叔出品** | AI Native Coder · 独立开发者
> 公众号「花叔」| 30万+粉丝 | AI工具与效率提升
> 代表作：小猫补光灯（AppStore付费榜Top1）·《一本书玩转DeepSeek》
