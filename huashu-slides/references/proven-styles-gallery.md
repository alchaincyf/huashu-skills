# Proven Styles Gallery: 18 Tested Visual Styles for AI Slides + 5 Professional Editorial Styles

> 实战验证的风格画廊。基于2026-02-08小红书介绍PPT项目，同一页slide（种草链路：发现→种草→搜索→购买）在17种风格下全部一次生成成功。
> 2026-02-09蕴煜AI培训项目验证Neo-Brutalism风格（Day1 67页 + Day2 64页全部HTML渲染成功）。
> 样例图片见 `assets/style-samples/` 目录。

## 风格推荐策略

**核心发现：插画/漫画类风格的AI生成效果远好于「专业极简」类风格。**

原因分析：
- 漫画/插画风格有明确的视觉语言（线条、角色、色块），AI可以充分发挥
- 极简风格（暗色底+发光文字+大量留白）缺乏视觉元素，生成出来「空」且「平」
- 有角色/场景的风格信息传达更生动，观众更容易记住

### 推荐优先级

**第一梯队（强烈推荐，效果极好）：**

| 风格 | 适合场景 | 核心特点 |
|------|---------|---------|
| Snoopy温暖漫画 | 品牌介绍、教育、个人IP | 温暖治愈，角色引导，信息量充足 |
| 学習漫画 Manga | 教程、培训、知识分享 | 角色反应驱动理解，趣味性强 |
| Ligne Claire清线 | 产品说明、流程解释 | 信息清晰度最高，面板叙事 |
| Neo-Pop新波普 | 年轻品牌、社交平台、活动 | 潮流感强，视觉冲击力大 |

**第二梯队（推荐，特定场景效果好）：**

| 风格 | 适合场景 | 核心特点 |
|------|---------|---------|
| Neo-Brutalism新粗野主义 | 企业培训、线下分享、信息密集 | 粗边框+色块+大字，远距离可读 |
| xkcd白板手绘 | 技术分享、极客受众、课堂 | 极简幽默，复杂概念秒懂 |
| The Oatmeal信息图漫画 | 科普、社交传播、内部培训 | 搞笑夸张，信息密度适中 |
| 苏联构成主义 | campaign、动员、品牌宣言 | 力量感强，辨识度极高 |
| 敦煌壁画 | 国风品牌、文化项目、高端场合 | 东方美学，庄重诗意 |
| 浮世绘 | 日本/东方市场、跨境品牌 | 浪潮隐喻天然表达递进 |

**第三梯队（可用，需要合适场景）：**

| 风格 | 适合场景 | 核心特点 |
|------|---------|---------|
| 温暖叙事 | 用户故事、品牌故事 | 人物场景生动自然 |
| 孔版印刷Risograph | 独立品牌、创意行业、音乐 | 双色叠印独特美学 |
| 等轴测Isometric | 科技产品、SaaS流程 | 2.5D游戏世界感 |
| Bauhaus包豪斯 | 设计行业、建筑、教育 | 几何=逻辑 |
| 工程蓝图Blueprint | 技术架构、工程方案 | 精密机器隐喻 |
| 复古广告Vintage Ad | 消费品、零售、怀旧 | 乐观复古好感 |
| 达达拼贴Collage | 创意行业、广告、破冰 | 反规则，最另类 |
| 像素画Pixel Art | 游戏、年轻群体、gamification | RPG任务隐喻 |

### 按主题自动推荐

在Step 2推荐3个风格时，优先从下表的推荐池中选：

| 主题类型 | 第一推荐 | 第二推荐 | 第三推荐 |
|---------|---------|---------|---------|
| 品牌/产品介绍 | Snoopy温暖漫画 | Neo-Pop新波普 | 浮世绘/敦煌（东方品牌） |
| 教育/培训 | Neo-Brutalism | 学習漫画 | Snoopy温暖漫画 |
| 技术分享 | xkcd白板 | Neo-Brutalism | Ligne Claire |
| 数据报告 | Ligne Claire | 苏联构成主义 | Neo-Brutalism |
| 年轻受众 | Neo-Pop | 像素画 | 孔版印刷 |
| 创意/艺术 | 达达拼贴 | 孔版印刷 | The Oatmeal |
| 国风/东方 | 敦煌壁画 | 浮世绘 | 温暖叙事 |
| 正式商务 | **Pentagram Editorial** | Neo-Brutalism | Ligne Claire |
| 行业分析/咨询 | **Pentagram Editorial** | **Fathom Data** | Ligne Claire |
| 培训课件/教材 | Neo-Brutalism | **Müller-Brockmann Grid** | 学習漫画 |
| 投资/融资路演 | **Build Luxury Minimal** | **Pentagram Editorial** | **Takram Speculative** |
| 产品发布/keynote | 苏联构成主义 | Neo-Pop | Neo-Brutalism |
| 内部分享 | Neo-Brutalism | The Oatmeal | xkcd白板 |

---

## 第一梯队详细参考

### 1. Snoopy温暖漫画 (Warm Comic Strip)

详细指南见 → `proven-styles-snoopy.md`

**快速参考：**
- 视觉参考：Peanuts / Charles Schulz
- 背景：暖米色(#FFF8E8) | 墨线：暖深色(#333333) | 强调：天蓝(#87CEEB) + 草绿(#8FBC8F) + 日落橙(#F4A460)
- 核心元素：大圆头小身体角色 + 锯齿草地线 + speech bubble + 极简背景
- 关键：始终指定"NOT Snoopy or Charlie Brown — an original character with Peanuts proportions"

### 2. 学習漫画 Manga Educational

**Base Style已在prompt-templates.md中。**

**实测关键发现：**
- 角色反应驱动学习——惊讶脸、闪光效果让重点「活」起来
- 3-5面板布局最佳，太多面板会拥挤
- 速度线、星光等漫画特效增强信息优先级
- 对话泡是天然的信息容器

### 3. Ligne Claire 清线漫画

**Base Style已在prompt-templates.md中。**

**实测关键发现：**
- 信息清晰度最高——均匀线条+平涂色块=零视觉噪音
- 2-4面板按需分配，不必强制四格
- 适合需要精确传达信息的场景
- 缺点：情感张力较弱，不如Snoopy温暖

### 4. Neo-Pop Magazine 新波普杂志

**Base Style已在prompt-templates.md中。**

**实测关键发现：**
- 字体大小对比(10:1)是核心——标题占据50%画面
- 色块分区帮助信息组织
- 注意：prompt中避免出现字号数字（如20pt），会被当做文字渲染

---

## 第二梯队详细参考

### 5. xkcd白板手绘 (Whiteboard Sketch)

**Base Style已在prompt-templates.md中。适合极客受众。**

### 6. The Oatmeal信息图漫画

**配色：** 浅灰白(#F8F8F8) + 亮橙(#FF6B35) + 深灰(#333333) + 品牌红(#FF2442)
**核心：** 大头角色极度夸张表情 + 粗线条手绘风 + 信息图式数据

### 7. 苏联构成主义 (Soviet Constructivism)

**配色：** 革命红(#CC0000) 40% + 黑(#1A1A1A) 25% + 米白(#F5E6D3) 30%
**核心prompt要素：**
- 对角线楔形从左下到右上——核心视觉元素
- 所有文字旋转15-30度——没有水平线
- 几何形状代表不同步骤，从小到大（视觉crescendo）
- NO gradients，纯色填充+锐利边缘
- 三色限定——限制就是力量

### 8. 敦煌壁画 (Dunhuang Mural)

**配色：** 赭石底(#D4A574) + 石青(#2E86AB) + 朱砂(#C53D43) + 石绿(#5DAE8B) + 金(#C4A35A)
**核心prompt要素：**
- 卷轴叙事从左到右
- 飞天飘带贯穿四阶段
- 受敦煌飞天启发的优雅人物（NOT直接佛教形象）
- 祥云、莲花、金箔边框
- 矿物质颜料感——略哑光，不数码亮

### 9. 浮世绘 (Ukiyo-e)

**配色：** 和纸米白(#F5F0E1) + 靛蓝(#1B4B7A) + 朱红(#C53D43) + 金(#C4A35A)
**核心prompt要素：**
- 浪潮隐喻：涟漪→涌浪→巨浪→破浪（对应4步）
- 浮世绘cartouche标签
- 日式云纹装饰
- 木版画质感——平涂无渐变

---

## 第三梯队详细参考

### 10. 温暖叙事 (Warm Narrative)

**配色：** 暖奶油(#FDF6EC) + 深灰(#3D3D3D) + 珊瑚(#E17055)
**核心：** 暖色人物插画 + 生活场景 + 最有「人情味」

### 11. 孔版印刷 (Risograph)

**配色：** 纸色(#FAF3E0) + 荧光粉(#FF6B9D) + 蓝(#0077B6) → 叠印紫(#6B3FA0)
**核心：** 严格双色叠印 + 套色错位2-3px + 半色调网点 + 粗糙纸感

### 12. 等轴测 (Isometric)

**配色：** 浅灰蓝(#DDE1E7) + 薰衣草/薄荷绿/珊瑚/柔黄 各平台一色
**核心：** 2.5D视角 + 4个递升平台 + 小人物走楼梯 + Monument Valley美学

### 13. Bauhaus包豪斯

**配色：** 纸白(#FAFAFA) + 红(#E53935) + 蓝(#1E88E5) + 黄(#FDD835) + 黑(#212121)
**核心：** 圆/三角/方/星代表4步 + 色彩有心理学意义 + 形式跟随功能

### 14. 工程蓝图 (Blueprint)

**配色：** 蓝图蓝(#1B3A5C) 75% + 白线(#FFFFFF) 20% + 红标注(#FF2442) 5%
**核心：** 白色线条图on深蓝底 + 工程方格纸网格 + 尺寸标注线 + 技术标题栏

### 15. 复古广告 (1950s Vintage Ad)

**配色：** 奶油白(#FFF8E7) + 复古红(#C0392B) + 薄荷绿(#1ABC9C) + 暖棕金(#8B6914)
**核心：** 乐观美式插画 + 半色调网点 + 复古丝带横幅 + 美好生活叙事

### 16. 达达拼贴 (Dada Collage)

**配色：** 无固定——混搭就是风格。纸白(#F5F5F5) + 墨黑 + 品牌红 + 胶带黄(#FFEAA7) + 随机彩色
**核心：** 撕纸碎片 + 混搭字体+角度 + 胶带别针 + 有序的混乱 + 橡皮印章数据

### 17. 像素画RPG (Pixel Art)

**配色：** 16-bit调色板。天空蓝 + 草地绿(#4CAF50) + UI深蓝(#1A237E) + 金(#FFD700)
**核心：** 横版RPG世界地图 + 像素角色4个区域 + RPG进度条 + 文字框 + QUEST隐喻

### 18. Neo-Brutalism 新粗野主义

**视觉参考：** Gumroad官网、Figma社区模板、小红书官方PPT、Figma品牌设计
**验证项目：** 2026-02-09 蕴煜AI培训项目（Day1 67页 + Day2 64页全部HTML渲染成功）

**配色：** 奶油(#F5E6D3) 40% + 革命红(#FF3B4F) 25% + 金黄(#FFD700) 20% + 深黑(#1A1A1A) 15%
**配色原则：** 高对比原色搭配——暖色底+强调色块+黑色边框，无渐变

**核心prompt要素：**

1. **粗黑边框** (CSS: `border: 4-6px solid #1A1A1A`)
   - 所有重要元素都有粗黑边框
   - 边框宽度4-6px，绝不细于3px
   - 边框必须完整，不能断裂或缺失

2. **高饱和色块分区**
   - 色块之间边界清晰，无模糊过渡
   - 每个模块一个主色，不混色
   - 色块面积大，留白少

3. **超大字排版** (CSS: `font-size: 3-6vw`)
   - 标题字号占幻灯片15-30%面积
   - 无衬线粗体字（Helvetica Neue Bold、Arial Black）
   - 文字对齐：左对齐或居中，不右对齐

4. **偏移阴影** (CSS: `box-shadow: 8px 8px 0 #1A1A1A`)
   - 阴影完全实色，无模糊
   - 向右下偏移6-10px
   - 阴影颜色必须是黑色

5. **扁平化图标**
   - 几何形状图标（圆、方、三角）
   - 图标有粗边框
   - 无立体感、无渐变

**实测关键发现（蕴煜AI培训项目131页验证）：**

- **远距离可读性极强** — 粗边框+大字让投影效果远超其他风格，10米外仍清晰
- **信息层次天然清晰** — 色块分区自带视觉分组，无需额外设计
- **HTML渲染稳定性高** — 相比漫画风格，Neo-Brutalism的CSS非常简单（无复杂SVG、无曲线），渲染成功率接近100%
- **适合信息密集场景** — 每页可容纳3-5个模块，互不干扰
- **无需AI生成** — 纯CSS即可完美实现，不依赖AI图片生成（这是关键优势）

**最佳适用场景：**
- 企业内训（信息量大、需远距离可读）
- 线下技术分享（投影仪环境）
- 数据密集报告（多模块并存）
- Workshop工作坊（需要清晰的步骤指引）

**注意事项：**
- 避免使用蓝色或紫色底（容易变成赛博风）
- 文字必须黑色或深色，不要白色（Neo-Brutalism的核心是「强对比」而非「反白」）
- 如果出现溢出，减少内容而非缩小字号——大字是灵魂

**与其他风格的区别：**
- vs Bauhaus：Neo-Brutalism更「粗暴」，边框更粗，色彩更饱和
- vs Neo-Pop：Neo-Pop有杂志感和装饰元素，Neo-Brutalism完全功能主义
- vs 苏联构成主义：构成主义有对角线和动态感，Neo-Brutalism是正交网格

**搜索关键词（灵感参考）：**
- `neubrutalism web design`
- `brutalist poster design`
- `Gumroad brand design`
- `flat design with thick borders`

---

## 第四类：Professional / Editorial 设计系统（Path A 专用）

> 以下5种风格使用 HTML→PPTX 路径，依赖精确排版和网格系统。详细 preset 定义见 SKILL.md「第四类」章节。

| # | 风格 | 适合场景 | 核心特点 | 执行路径 |
|---|------|---------|---------|---------|
| P1 | **Pentagram Editorial** | 行业分析、咨询报告、数据驱动 | 字体即语言，瑞士网格，ONE accent color | Path A |
| P2 | **Fathom Data Narrative** | 数据报告、科学展示、研究汇报 | 高信息密度+设计优雅，图表即叙事 | Path A |
| P3 | **Müller-Brockmann Grid** | 培训课件、技术架构、流程说明 | 数学精确网格，功能主义至上 | Path A |
| P4 | **Build Luxury Minimal** | 投资路演、品牌高管汇报、奢侈品 | 75%留白，微妙字重变化，高端克制 | Path A |
| P5 | **Takram Speculative** | 设计思维、产品愿景、战略规划 | 柔和科技感，概念原型图作为核心视觉 | Path A（配图可AI辅助） |

**实战验证**：Pentagram Editorial 在口腔行业分析15页deck中验证成功（`_temp/口腔行业分析/slides/`）
**更深入的风格细节**：参考 `design-philosophy` skill 的 `references/design-styles.md`

---

## 完整Prompt模板存档

第二轮10种扩展风格的完整可复制prompt，详见：
`/Users/alchain/Documents/写作/_temp/xiaohongshu-ppt-compare/风格对比-Prompt记录.md`

Snoopy风格的详细per-slide模板，详见：
`proven-styles-snoopy.md`

Neo-Brutalism的完整HTML模板（131页验证版本），详见：
`/Users/alchain/Documents/写作/自媒体经验梳理/蕴煜AI培训-202602/Day1-AI认知与工作流/`
`/Users/alchain/Documents/写作/自媒体经验梳理/蕴煜AI培训-202602/Day2-AI编程与Claude生态/`
