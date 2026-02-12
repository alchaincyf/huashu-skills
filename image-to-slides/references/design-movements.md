# 设计运动与风格参考库

> 基于花叔审美偏好整理。用于风格讨论时建立共同语言——当我们说「田中一光风格」或「瑞士国际主义」时，双方都知道在说什么。
>
> 这不是直接的AI prompt模板（那些在 `prompt-templates.md` 和 `proven-styles-gallery.md` 中），而是设计决策的上游参考。

---

## 花叔审美画像

**喜欢**：大字、色块、冲击力、温暖色调、有质感、功能主义（每个元素都有存在理由）
**不喜欢**：赛博霓虹、冷色系（深蓝/紫底）、扁平无聊的企业模板、过度装饰

**核心偏好**：用最简单的方式传达最多信息（费曼思维在视觉上的投射）

---

## 设计运动 → Skill风格 对照表

这张表连接了「设计史上的运动」和「我们skill中已有的AI生成风格」，帮助在讨论时快速定位。

| 设计运动 | skill中对应风格 | 关系说明 |
|---------|----------------|---------|
| Neo-Brutalism（新粗野主义） | Neo-Pop新波普 + **Neo-Brutalism**（新增#18） | 粗边框、色块、大字——小红书官方PPT就是这个 |
| 田中一光 / 日本图形设计 | Ligne Claire清线 | 极简几何+东方美学，限色克制 |
| 瑞士国际主义 | Bauhaus包豪斯 | 网格系统+功能主义+无衬线大字 |
| 蒙德里安 / De Stijl | Neo-Pop新波普 | 原色块分割、几何秩序 |
| 包豪斯 | Bauhaus包豪斯 | 直接对应 |
| 孟菲斯设计 | Neo-Pop新波普 | 高饱和混搭，但孟菲斯更「吵」 |
| 俄国构成主义 | 苏联构成主义 | 直接对应 |
| Apple Keynote | —（skill中故意不做极简风） | 太冷太克制，缺少冲击力 |
| Sagmeister & Walsh | 达达拼贴Collage | 实验性、大胆用色、每项目不同风格 |
| Information is Beautiful | Ligne Claire清线 | 数据→美学、复杂信息简化 |
| Giorgia Lupi（数据人文主义） | 温暖叙事Warm Narrative | 有温度的数据可视化 |

---

## 第一梯队：最可能喜欢的风格

### 1. Neo-Brutalism（新粗野主义）

**代表**：Gumroad、Figma社区、小红书官方PPT
**视觉特征**：粗黑边框(3-6px)、高饱和色块、无渐变、偏移阴影、大字排版
**配色**：高对比原色——红黄黑米白是典型组合
**适合PPT**：非常适合。信息层次清晰，远距离可读性强
**与skill的关系**：已验证，2026-02-09蕴煜AI培训项目完成了Day1(67页)+Day2(64页)全套HTML渲染

**核心CSS特征（已验证）**：
```css
/* 配色 */
--cream: #F5E6D3;
--red: #FF3B4F;
--yellow: #FFD700;
--black: #1A1A1A;

/* 布局 */
border: 4-6px solid #1A1A1A;  /* 粗黑边框 */
font-size: 3-6vw;             /* 超大字 */
overflow: hidden;              /* 无溢出 */
```

**搜索关键词**：`Neo Brutalism presentation design`、`Neubrutalism UI`

### 2. 田中一光 / 日本图形设计（Ikko Tanaka）

**代表**：田中一光、横尾忠则、佐藤卓
**视觉特征**：极简几何形状、大面积留白、有限配色（2-3色）、网格结构、东方美学+西方现代主义
**配色**：红+黑+白 或 金+黑+白，极度克制
**为什么推荐**：和费曼偏好（用最简单的方式解释复杂事物）完全一致。田中一光的海报就是「用几何形状讲故事」
**适合PPT**：非常适合金句页、概念页。信息密集页需要调整
**搜索关键词**：`Ikko Tanaka poster`、`Japanese graphic design minimalist`

### 3. 瑞士国际主义（Swiss/International Typographic Style）

**代表**：Josef Müller-Brockmann、Armin Hofmann、Ernst Keller
**视觉特征**：严格网格系统、无衬线大字（Helvetica/Akzidenz）、不对称布局、几何图形、照片蒙版
**配色**：通常黑白红，或单色+强调色
**为什么推荐**：功能主义的极致——每个元素都有存在理由。网格系统天然适合幻灯片
**搜索关键词**：`Swiss Style poster`、`Josef Müller-Brockmann grid`

### 4. 蒙德里安 / De Stijl（风格派）

**代表**：Piet Mondrian、Theo van Doesburg
**视觉特征**：水平+垂直线条分割、原色块（红黄蓝+黑白）、绝对的几何秩序
**配色**：红、黄、蓝、黑、白——经典五色
**适合PPT**：适合封面、过渡页。内容页需要灵活变体
**搜索关键词**：`Mondrian layout design`、`De Stijl graphic design`

---

## 第二梯队：值得参考的风格

### 5. 包豪斯（Bauhaus）

**代表**：Herbert Bayer、László Moholy-Nagy、Joost Schmidt
**视觉特征**：几何图形（圆三角方）、功能主义、原色+黑白、实验性排版
**与skill的关系**：skill中已有Bauhaus包豪斯风格（第三梯队#13）

### 6. 孟菲斯设计（Memphis Design）

**代表**：Ettore Sottsass、Michele De Lucchi
**视觉特征**：鲜艳色彩、几何图案混搭、波点/条纹/锯齿、刻意的「不协调」
**注意**：视觉冲击力极强，但可能太「吵」——培训PPT需要让人集中注意力
**适合PPT**：适合做装饰元素和图案纹理，不适合做主布局

### 7. 俄国构成主义（Constructivism）

**代表**：El Lissitzky、Alexander Rodchenko
**视觉特征**：对角线构图、红+黑+白、几何形状叠加、政治宣传海报感
**与skill的关系**：skill中已有苏联构成主义风格（第二梯队#7）

---

## 第三梯队：顶级公司的Deck设计

### 8. Apple Keynote 风格

**视觉特征**：极简、大量留白、超大单词、深色/浅色两极、高质量产品摄影
**配色**：黑+白为主，偶尔一个强调色
**注意**：可能太「冷」太「克制」，缺少冲击力和温度。skill中故意不做此类极简风格（AI生成效果差）

### 9. Stripe / Linear 设计系统

**视觉特征**：柔和渐变、3D插画、精致排版、大量数据可视化
**配色**：紫+蓝渐变（Stripe）、极简黑白（Linear）
**注意**：Stripe的蓝紫渐变不符合暖色偏好

### 10. Sagmeister & Walsh

**代表**：Stefan Sagmeister、Jessica Walsh
**视觉特征**：实验性极强、大胆用色、材质混搭、每个项目风格完全不同
**为什么参考**：「Beauty」项目用大胆色彩和几何构成探索什么是美——和花叔审美高度重合
**启发**：每套PPT不必只有一个风格，可以按章节切换「情绪」

---

## 第四梯队：数据可视化/信息设计

### 11. Information is Beautiful（David McCandless）

**视觉特征**：数据→美学、复杂信息简化、干净的信息图表
**适合PPT**：数据展示页、效率对比页、工具矩阵页

### 12. Giorgia Lupi（数据人文主义）

**视觉特征**：手绘质感+数据、有温度的信息图、个人叙事+数据结合
**为什么参考**：「数据人文主义」理念和花叔的「有人味」风格完全对应

---

## 2026年演示设计趋势

| 趋势 | 描述 | 是否推荐 |
|------|------|---------|
| Bento Grid布局 | 模块化方格（像Apple推广视频） | 推荐——和色块风格兼容 |
| 超大字排版 | 标题字占幻灯片50%面积 | 已在用 |
| 竖版幻灯片 | 9:16给手机阅读优化 | 线下培训不需要 |
| 非线性演示 | 可点击跳转的交互式菜单 | 线下培训不需要 |
| Glassmorphism | 毛玻璃+透明效果 | 不推荐——偏冷偏科技感 |

---

## 使用场景

### 场景1：用户说「我想要XX风格」

1. 在本文件中找到对应的设计运动
2. 查看「与skill的关系」列，找到skill中已有的最近风格
3. 用该已有风格的prompt模板作为起点
4. 根据设计运动的特征做调整

### 场景2：用户不确定想要什么风格

1. 用花叔审美画像作为默认偏好
2. 按主题在 `proven-styles-gallery.md` 的推荐表中选3个
3. 用本文件中的设计运动名称作为讨论锚点（如「这个方向偏田中一光，那个偏构成主义」）

### 场景3：需要从零设计一个新风格

1. 在本文件中选择1-2个设计运动作为视觉DNA
2. 提取其核心视觉特征（配色、构图、字体、元素）
3. 写成Base Style prompt
4. 在 `proven-styles-gallery.md` 中增加为新风格

---

## 搜索这些风格的最佳渠道

| 渠道 | 适合找什么 |
|------|-----------|
| Behance | 设计师完整项目展示 |
| Dribbble | 单张设计灵感 |
| Pinterest | 按风格聚合的情绪板 |
| Poster House (posterhouse.org) | 经典海报展览 |
| It's Nice That (itsnicethat.com) | 设计趋势和设计师访谈 |
| Fonts In Use (fontsinuse.com) | 看字体在真实设计中的应用 |
| SlidesGo / SlidesCarnival | 免费PPT模板看趋势 |

---

*整理于 2026-02-09 | 基于花叔审美偏好定制*
