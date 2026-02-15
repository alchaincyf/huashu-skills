---
name: huashu-xhs-image
description: |
  为小红书笔记生成高质量配图。默认AI生成（Gemini），仅精确数据表格用HTML兜底。当用户提到"小红书配图"、"小红书封面"、"小红书图片"、"做张小红书图"、"笔记配图"时使用此技能。
---

# 小红书配图工作流

## ⚠️ 核心原则：先提案，后生成

**绝对不能跳过设计提案直接出图。** 正确流程：

```
理解内容 → 设计提案（2-3个方向）→ 用户选择 → 生成 → 预览确认 → 上传
```

---

## 花叔设计审美画像

### 喜欢的
- **质感和温度** — 纸张褶皱、手写笔触、印章、胶带等有机元素
- **手绘/书法字体** — 笔记感、个人分享场景尤其适合
- **文字撑满画面** — 小红书是手机竖屏，文字要大到一眼看清
- **核心元素强化** — 关键数字/关键词做视觉hero（放大3倍、变色、加装饰）
- **结构清晰** — 主标题 > 副标题 > 列表，层次分明
- **暖色调** — 奶油色、暖橙、暖金表现好

### 不喜欢的
- **HTML截图** — 太平面、像PPT模板、没有灵魂（仅精确数据表格兜底）
- **赛博霓虹/深蓝底** — #0D1117等深蓝色底属于审美禁区
- **署名/水印** — 封面图不出现「花生」「花叔」「@花生」
- **过度留白** — 宁可满一点，不要空荡荡

### 验证过的好风格
| 风格 | 表现 | 适用 |
|------|------|------|
| 手绘笔记（暖色纸张+书法字+手绘图标） | ⭐⭐⭐⭐⭐ | 教程、干货、个人分享 |
| 暗金海报（深色底+金色大字） | ⭐⭐⭐⭐ | 产品发布、震撼标题（需搭配好内容） |
| 极简信息图（浅底+大数字+简洁层次） | ⭐⭐⭐⭐ | 数据驱动、对比 |

---

## 核心参数

| 参数 | 值 |
|------|-----|
| 标准尺寸 | 1080 x 1440 px (3:4) |
| AI 生成分辨率 | `--resolution 2K` |
| AI Prompt 长宽比声明 | `3:4 portrait aspect ratio, 1080x1440 pixels` |
| HTML viewport（兜底用） | `--viewport-size=1080,1440` |

---

## Step 1: 理解内容

读取用户提供的内容，快速提炼：
- **主题**：这篇讲什么？
- **核心关键词**：哪些词/数字需要做视觉hero？
- **情绪/调性**：悬念？干货？温暖？震撼？
- **图片数量和类型**：单封面 / 轮播套图 / 信息图？

不需要向用户展示分析结果，直接进入Step 2。

---

## Step 2: 设计提案 ✅ 必须等用户选择

**这是整个流程最关键的一步。禁止跳过。**

### 提案格式

向用户展示 **2-3个设计方向**，每个方向包含：

```
### 方向A：[风格名]
- 视觉风格：[一句话描述画面感，如"暖色笔记本纸张+毛笔书法大字+手绘小图标"]
- 色彩：[底色 + 主色 + 强调色]
- 文案布局：[哪些文字放大做hero、哪些做副标题、整体排列方式]
- 情绪：[用户看到后的第一感受]
```

### 提案原则

1. **每个方向要有明确差异**（风格、情绪、色彩至少有一个完全不同）
2. **标注推荐**（基于内容特征说明为什么推荐某个方向）
3. **文案要具体**（不是"标题放大"，而是「"28"做200px的hero元素，橙色强调」）
4. **不要超过3个方向**（选择太多反而难选）

### 提案示例

> **方向A：手绘笔记风（推荐）**
> - 视觉风格：奶油色方格纸底 + 毛笔书法大标题 + 手绘科技小图标
> - 色彩：底色#FDF6EC + 主色#D97706（暖橙）+ 强调圈线
> - 文案布局：「阿里C4楼」「来了一群广东人」撑满上半区做hero，「AI开源冠军」橙色高亮做视觉锚点，右下角「千问APP」印章
> - 情绪：亲切、真实、像朋友分享内幕
>
> **方向B：暗金揭秘风**
> - 视觉风格：深色磨砂底 + 金色大字 + 徽章装饰
> - 色彩：底色#1A1A1A + 主色#E2B714（金）+ 白色辅助
> - 文案布局：「全球AI开源冠军」金色巨字撑满画面，上方「大厂内幕」金色徽章，下方副标题白色
> - 情绪：震撼、内幕、有分量感

**等用户选择后才进入 Step 3。** 用户可能会：
- 直接选一个 → 进入生成
- 要求混合/调整 → 修改方向后再确认
- 都不满意 → 追问偏好后重新提案

---

## Step 3: 生成图片

### 构建 Prompt

基于用户选择的方向，构建完整prompt。

**Prompt 模板：**
```
Create a [style] cover for a Xiaohongshu post. 3:4 portrait aspect ratio, 1080x1440 pixels, high quality rendering.

VISUAL STYLE: [从提案中的视觉风格描述展开]
COLOR PALETTE: [具体色彩描述]
TYPOGRAPHY: text fills most of the canvas, oversized bold typography, clear visual hierarchy.

TEXT TO RENDER:
- [主标题 — hero元素，视觉dominant]
- [副标题]
- [其他文字元素]

The word/number "[核心关键词]" is visually dominant, 3x larger than other text, with decorative emphasis.

IMPORTANT: Do NOT include any personal signature, watermark, or author name like "花生" or "花叔".

[1-2句画面情绪描述]
```

**花叔偏好 Prompt 关键词（按需加入）：**
- 文字大 → `text fills most of the canvas, oversized bold typography`
- 核心强化 → `the word/number "XX" is visually dominant, 3x larger than other text, with decorative emphasis`
- 手写体 → `handwritten style Chinese text / brush calligraphy lettering`
- 纸张质感 → `warm cream paper texture with subtle grid lines, notebook page feel`
- 结构清晰 → `clear visual hierarchy with distinct heading, subheading, and list levels`
- 无署名 → `Do NOT include any personal signature, watermark, or author name`

### 两条生成路径（每次都出）

| 路径 | 工具 | 优势 | 劣势 | 成本 |
|------|------|------|------|------|
| **AI生成** | Gemini nano-banana-pro | 质感好、有温度、视觉丰富 | 中文可能渲染错误 | 有API费用 |
| **HTML截图** | Playwright | 文字100%精确、零成本、可批量 | 偏平面、缺少质感 | 免费 |

**每次两条路径都出，方便用户对比选择。** HTML零成本，可以每个方向多出几种变体（配色/布局），给用户更多选择空间。AI路径每个方向出1张即可。

### 文件组织规范（必遵守）

多版本生成时，所有相关文件（png + html源文件）放在**同一个子文件夹**内：

```
文章所在目录/
├── 文章.md
└── [文章简称]-小红书配图/          ← 子文件夹
    ├── A-笔记风-AI.png
    ├── A1-笔记风-HTML-暖色.png
    ├── A1-笔记风-HTML-暖色.html
    ├── B-报纸风-AI.png
    └── ...
```

**命名规则**：`[方向字母][变体序号]-[风格中文名]-[路径AI/HTML]-[变体描述].png`
- 方向字母：A/B/C（对应设计提案的方向）
- AI路径无序号：`A-笔记风-AI.png`
- HTML变体带序号：`A1-笔记风-HTML-暖色.png`、`A2-笔记风-HTML-绿色.png`
- 文件夹名用文章关键词：`[关键词]-小红书配图/`

### AI生成命令

```bash
export $(grep GEMINI_API_KEY ~/.claude/.env) && \
uv run /Users/alchain/Documents/写作/.claude/skills/xhs-image/scripts/generate_image.py \
  --prompt "[完整prompt]" \
  --filename "[方向]-[风格]-AI.png" \
  --resolution 2K
```

生成后移动到配图子文件夹内。套图可并行生成（`run_in_background=true`）。

---

## Step 4: 预览确认

### 浏览器预览（必做）
生成完成后，用 `open` 命令打开所有图片，方便用户并排对比：
```bash
open "[图片路径1]" "[图片路径2]" "[图片路径3]"
```

### 内联预览
同时用 Read 工具在终端中展示生成结果。

**基础检查项：**
1. 中文文字渲染正确吗？
2. 比例是3:4竖版吗？
3. 风格符合选定方向吗？
4. 没有出现署名/水印吗？

### 设计审查（必做）

对每张图从两个维度评分（10分制），并给出优化方向：

| 维度 | 评判标准 |
|------|---------|
| **设计评分** | 视觉层次、排版、色彩搭配、质感、创意 |
| **小红书吸引力** | 信息流中是否抢眼、文字是否够大、信息密度、情绪传达、是否引发好奇 |

**审查输出格式：**
- 每张图：综合评分 + 1句核心评价 + 1条优化方向
- 最后给出总结排名表，标注推荐
- 用户可自行决定是否采纳优化建议

**用户反馈处理：**
- 满意 → Step 5 上传
- 文字有误 → 该张改用HTML兜底渲染
- 风格不对 → 调整prompt重新生成
- 大改方向 → 回到Step 2重新提案

---

## Step 5: 上传图床

```bash
python3 /Users/alchain/Documents/写作/tools/upload_image.py "[图片路径]"
```

返回 ImgBB 永久链接。

---

## HTML截图路径（AI文字渲染失败、精确数据表格、或用户要求对比时使用）

```bash
npx playwright screenshot "file:///path/to/card.html" output.png \
  --viewport-size=1080,1440 --wait-for-timeout=1000
```

HTML模板要求：
- 画布：`width: 1080px; height: 1440px`
- 字体：`font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`
- 安全区：上下各 80px、左右各 60px

---

## 快速参考

### 中文文字渲染限制（AI路径）
- 主标题 ≤ 7 字
- 副标题 ≤ 15 字
- 正文每行 ≤ 20 字
- 必须逐张验证

### 花叔科技账号配色

| 方案名 | 底色 | 主色 | 强调色 | 适用 |
|--------|------|------|--------|------|
| 暖灰专业 | #F5F0EB | #D97706 | #4A90D9 | AI工具、分享 |
| 极简专业 | #F5F5F5 | #4A90D9 | #FF6B35 | 教程、对比 |
| 暗夜金 | #1A1A2E | #E2B714 | #FFFFFF | 产品发布 |
| 终端绿 | #1A1A1A | #00FF41 | #888888 | 编程相关 |

### Golden Rules
- 标题大、粗、醒目（占画面 30-50%）
- 核心数字/关键词做视觉强化（放大、变色、加装饰）
- 封面信息量大 → 引发好奇
- 套图风格统一
- 竖版 3:4，充分利用屏幕空间
- 不加署名/水印

---

## 相关 Skills

| Skill | 作用 |
|-------|------|
| `wechat-image` | 公众号配图（姊妹 skill） |
| `image-to-slides` | PPT 配图（风格库来源） |

## 参考文件

- `references/style-gallery.md` — 完整风格库与 prompt 模板
- `references/design-guidelines.md` — 小红书平台设计规范

---

> **花叔出品** | AI Native Coder · 独立开发者
> 公众号「花叔」| 30万+粉丝 | AI工具与效率提升
> 代表作：小猫补光灯（AppStore付费榜Top1）·《一本书玩转DeepSeek》
