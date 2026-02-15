---
name: huashu-wechat-image
description: |
  为微信公众号文章生成高质量配图。支持封面图（2.35:1）、正文插图（16:9/4:3）、信息图。提供两条路径：AI生成（视觉创意型）和HTML渲染（文字精确型）。当用户提到"公众号配图"、"公众号封面"、"文章配图"、"正文插图"、"公众号图片"时使用此技能。
---

# 公众号配图工作流

## ⚠️ 核心原则：先提案，后生成

**绝对不能跳过设计提案直接出图。** 正确流程：

```
理解内容 → 设计提案（2-3个方向）→ 用户选择 → 生成 → 预览确认 → 上传
```

设计审美画像和提案格式见姊妹skill `xhs-image/SKILL.md`，公众号配图同样适用。

## 核心参数

| 图片类型 | 尺寸 | 比例 | Playwright viewport | AI Prompt 长宽比声明 |
|---------|------|------|---------------------|---------------------|
| 头条封面 | 1800 x 766 px | 2.35:1 | `--viewport-size=1800,766` | `2.35:1 ultra-wide landscape, 1800x766 pixels` |
| 正文宽图 | 1920 x 1080 px | 16:9 | `--viewport-size=1920,1080` | `16:9 landscape, 1920x1080 pixels` |
| 正文方图 | 1440 x 1080 px | 4:3 | `--viewport-size=1440,1080` | `4:3 landscape, 1440x1080 pixels` |
| 信息图 | 1080 x 自由 | 自由 | `--viewport-size=1080,N` | 按内容定 |

---

## Step 0: 确定配图需求 ✅ 用户确认

**向用户展示选项，等待确认：**

| 类型 | 说明 | 图片数量 | 推荐路径 |
|------|------|---------|---------|
| **A. 仅封面** | 头条封面图 | 1张 | AI 生成 |
| **B. 正文配图** | 章节配图，辅助阅读理解 | 3-8张 | AI 生成为主 |
| **C. 全套配图** | 封面 + 正文全部 | 4-10张 | AI 生成为主 |
| **D. 纯信息图** | 数据对比、流程图、清单 | 1-5张 | AI 生成（精确数据表格用HTML兜底） |

**问用户**：
1. 做封面、正文插图、还是全套？
2. 文章路径/内容是什么？（分析内容确定配图位置）
3. 总共需要几张图？

### 配图数量建议

| 文章长度 | 推荐配图数 | 包含 |
|---------|-----------|------|
| < 1500字 | 2-3张 | 封面 + 1-2张正文 |
| 1500-3000字 | 4-6张 | 封面 + 每个核心章节1张 |
| 3000-5000字 | 6-8张 | 封面 + 章节图 + 信息图 |
| > 5000字 | 8-10张 | 不超过10张，避免过度打断 |

---

## Step 1: 风格选择 ✅ 用户确认

**根据用户的文章类型，推荐 3 种风格供选择。**

### 按文章类型自动推荐

| 文章类型 | 第一推荐 | 第二推荐 | 第三推荐 |
|---------|---------|---------|---------|
| AI工具评测 | 极简专业 | 编辑杂志 | 数据信息图 |
| 技术教程 | 极简专业 | 手绘白板 | 编辑杂志 |
| 产品发布 | 编辑杂志 | 大字报 | 极简专业 |
| 深度分析 | 编辑杂志 | 数据信息图 | 极简专业 |
| 个人故事 | Snoopy温暖漫画 | 温暖叙事 | 编辑杂志 |
| 行业观察 | 大字报 | 编辑杂志 | 数据信息图 |

**向用户展示 3 个推荐风格**，每个包含：
- 风格名 + 一句话描述
- 适用场景
- 色彩倾向

**问用户**：选哪个风格？或者你有自己想要的参考？

**完整风格库：** `references/style-gallery.md`

---

## Step 2: 选择生成路径 ✅ 用户确认

**根据内容特征推荐路径，向用户展示对比：**

| | Path A: HTML → 截图 | Path B: AI 生成 |
|---|---|---|
| **文字准确度** | 100%（代码控制） | 中文可能出错（需验证） |
| **布局控制** | 像素级精确 | AI 自由发挥 |
| **视觉创意** | 中（靠设计能力） | 高（AI 有创造力） |
| **API 成本** | 零（纯本地） | 每张消耗 Gemini API |
| **速度** | 快（几秒） | 慢（10-30秒/张） |
| **适合** | 文字多、数据多、清单、信息图 | 封面、氛围图、创意插画 |
| **可编辑性** | 改 HTML 重新截图即可 | 需要重新生成 |
| **深色模式** | CSS 直接控制配色 | 需在 prompt 中声明 |

### ⚠️ 花叔偏好：AI生成优先

> HTML截图效果太平面、像PPT模板，缺少质感和设计感。AI生成的图片有丰富的视觉细节，品质远胜HTML。
> **默认走AI生成路径，只有「必须逐字精确的复杂数据表格」才用HTML兜底。**

### 路径推荐规则

| 图片类型 | 推荐路径 | 理由 |
|---------|---------|------|
| 头条封面 | **AI** | 视觉冲击力强，质感好 |
| 正文氛围/场景图 | **AI** | 创意性强 |
| 正文信息图 | **AI** | AI能做出设计感的信息图 |
| 流程图/步骤图 | **AI** | AI能加入视觉层次 |
| 对比图 | **AI** | 视觉品质更高 |
| 精确数据表格（10+单元格） | **HTML** | 唯一需要HTML的场景：大量精确数字 |

**默认推荐AI路径，不再逐次询问路径选择。**

---

## Step 3: 生成图片

### Path A: HTML → Playwright 截图

#### 3-A-1. 创建 HTML

根据选定风格和用户提供的内容，生成 HTML 文件。

**HTML 模板要求：**
- 画布尺寸：根据图片类型选择（封面 1800x766，正文宽图 1920x1080，正文方图 1440x1080）
- 字体：`font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`
- 深色模式友好：用 #F5F5F5 代替纯白，用 #1A1A2E 代替纯黑
- 封面安全区：核心信息集中在中央正方形区域（766x766）

**封面大字报模板示例（2.35:1）：**
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1800px; height: 766px;
    background: #1A1A2E;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    padding: 60px 400px; /* 左右大padding确保内容在安全区 */
    font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  }
  .title {
    font-size: 96px; font-weight: 900;
    color: #FFFFFF; text-align: center;
    line-height: 1.3; letter-spacing: 4px;
  }
  .subtitle {
    font-size: 36px; font-weight: 400;
    color: #E2B714; text-align: center;
    margin-top: 30px;
  }
  .accent-line {
    width: 200px; height: 4px;
    background: #E2B714;
    margin: 30px auto;
  }
</style>
</head>
<body>
  <div class="title">Claude vs Codex</div>
  <div class="accent-line"></div>
  <div class="subtitle">重度用户的20分钟实战对比</div>
</body>
</html>
```

**正文信息图模板示例（4:3）：**
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1440px; height: 1080px;
    background: #F5F5F5;
    padding: 60px 80px;
    font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  }
  .heading {
    font-size: 56px; font-weight: 800;
    color: #1A1A1A; margin-bottom: 40px;
    line-height: 1.3;
  }
  .item {
    display: flex; align-items: flex-start;
    margin-bottom: 28px; gap: 20px;
  }
  .num {
    font-size: 40px; font-weight: 900;
    color: #4A90D9; min-width: 50px;
  }
  .text {
    font-size: 32px; color: #333;
    line-height: 1.5;
  }
  .highlight { color: #FF6B35; font-weight: 700; }
</style>
</head>
<body>
  <div class="heading">Claude Code 五大优势</div>
  <div class="item"><span class="num">01</span><span class="text"><span class="highlight">Agent模式</span>自主规划执行复杂任务</span></div>
  <div class="item"><span class="num">02</span><span class="text">原生<span class="highlight">终端集成</span>直接操作文件系统</span></div>
  <div class="item"><span class="num">03</span><span class="text"><span class="highlight">多文件编辑</span>一次修改整个项目</span></div>
</body>
</html>
```

#### 3-A-2. 截图

```bash
npx playwright screenshot "file:///path/to/card.html" output.png \
  --viewport-size=[宽],[高] --wait-for-timeout=1000
```

- 封面：`--viewport-size=1800,766`
- 正文宽图：`--viewport-size=1920,1080`
- 正文方图：`--viewport-size=1440,1080`

#### 3-A-3. ✅ 预览确认

用 Read 工具向用户展示截图结果。

**问用户**：
- 文字内容对吗？
- 布局和配色满意吗？
- 封面的核心信息在安全区内吗？（封面图特有）
- 需要调整什么？

**如需调整**：修改 HTML → 重新截图 → 再次确认。（HTML 路径迭代成本极低）

---

### Path B: AI 生成（Gemini 3 Pro Image）

#### 3-B-1. 构建 Prompt

**封面 Base Style Prompt：**
```
[Base Style]:
VISUAL REFERENCE: [一句话描述具体风格美学]
CANVAS: 2.35:1 ultra-wide landscape, 1800x766 pixels, high quality rendering.
SAFE ZONE: Center square (766x766) contains all key text and visuals.
COLOR SYSTEM: [描述色彩情绪，不指定比例]
TEXT RENDERING: Chinese text must be large, clear, readable. Title in center safe zone.
```

**正文 Base Style Prompt：**
```
[Base Style]:
VISUAL REFERENCE: [一句话描述具体风格美学]
CANVAS: [16:9 landscape, 1920x1080 pixels / 4:3 landscape, 1440x1080 pixels], high quality rendering.
COLOR SYSTEM: [描述色彩情绪]
DARK MODE: Use medium-tone backgrounds, avoid pure white (#FFFFFF) and pure black (#000000).
```

**Per-Image Prompt：**
```
Create a [style] [cover/illustration] for a WeChat article about [topic].

[Base Style]

DESIGN INTENT: [用户看到后应该产生什么情绪/行为]

TEXT TO RENDER:
- Title: "[标题，封面≤10字，正文可少或无]"
- [其他文字]

[1-2句画面情绪描述，让 AI 自由发挥构图]
```

#### 3-B-2. ✅ Prompt 确认

**向用户展示即将使用的 prompt**，等待确认或修改。特别确认：
- 要渲染的文字内容是否正确
- 设计意图是否准确
- 是否有其他要求

#### 3-B-3. 生成

```bash
export $(grep GEMINI_API_KEY ~/.claude/.env) && \
uv run /Users/alchain/Documents/写作/.claude/skills/wechat-image/scripts/generate_image.py \
  --prompt "[完整prompt]" \
  --filename "[timestamp]-wechat-[类型]-[描述].png" \
  --aspect [cover|wide|standard|square]
```

- `--aspect cover` → 2.35:1 头条封面
- `--aspect wide` → 16:9 正文宽图（默认）
- `--aspect standard` → 4:3 正文方图
- `--aspect square` → 1:1 方图

多张图可并行生成（`run_in_background=true`）。

#### 3-B-4. ✅ 预览确认

用 Read 工具向用户展示生成结果。

**检查项：**
1. 文字准确吗？（中文无乱码/错字）
2. 比例正确吗？（封面 2.35:1、正文 16:9 或 4:3）
3. 封面安全区：核心信息在中央正方形内？（封面特有）
4. 深色模式：是否避免了纯白底和纯黑底？
5. 风格满意吗？

**问用户**：满意 / 重新生成 / 调整 prompt？

---

### Path C: 混合路径（全套配图推荐）

适用于全套配图：**封面用 AI 生成（抓眼球），正文信息图用 HTML 渲染（信息精确），正文氛围图用 AI 生成**。

执行顺序：
1. 先按 Path B 生成封面 → 用户确认
2. 从封面的配色/氛围提取一致的风格
3. 正文氛围图用 Path B → 用户确认
4. 正文信息图/数据图用 Path A → 用户确认

---

## Step 4: 上传图床

```bash
python3 /Users/alchain/Documents/写作/tools/upload_image.py "[图片路径]"
```

返回 ImgBB 永久链接。**公众号文章必须使用网络链接**，本地路径在发布后失效。

---

## 快速参考

### 封面安全区域

```
┌─────────────────────────────────────┐
│         │ 766x766  │               │
│  装饰区  │ 安全区域  │  装饰区       │ 1800 x 766
│         │ （核心）  │               │
└─────────────────────────────────────┘
           ↑ 朋友圈裁切区域 ↑
```

### 深色模式适配要点
- 底色用 #F5F5F5（浅灰）代替纯白
- 底色用 #1A1A2E（暗紫灰）代替纯黑
- 正文字色用 #595959 或 #3F3F3F，不用纯黑 #000000
- 避免阴影效果、白色边框
- 使用低饱和度配色

### 中文文字渲染（AI 路径特有）
- 封面标题 ≤ 10 字
- 正文图上文字 ≤ 20 字/行
- 信息图文字用 HTML 渲染更可靠
- 必须逐张验证

### 字体推荐（HTML 路径特有）
- 标题：`"PingFang SC"` Bold / `"Microsoft YaHei"` Bold
- 正文：`"PingFang SC"` Regular
- 商用安全替代：阿里巴巴普惠体、思源黑体

### 花叔科技账号配色

| 方案名 | 底色 | 主色 | 强调色 | 适用 | 深色模式 |
|--------|------|------|--------|------|---------|
| 暖灰专业 | #F5F0EB | #D97706 | #4A90D9 | AI工具、分享 | 好 |
| 极简专业 | #F5F5F5 | #4A90D9 | #FF6B35 | 教程、对比 | 中 |
| 暗夜金 | #1A1A2E | #E2B714 | #FFFFFF | 产品发布 | 好 |
| 终端绿 | #1A1A1A | #00FF41 | #888888 | 编程相关 | 好 |

### Golden Rules
- 封面核心信息放在中央正方形安全区
- 正文图用中间色调背景（适配深色模式）
- 信息图优先 HTML → 截图（文字精确）
- 氛围图优先 AI 生成（创意性强）
- 图片上传到图床获取永久链接
- 同一文章插图风格统一
- 每 800-1200 字配一张图
- 每个 H2 章节至少一张

### 配图位置策略

| 位置 | 必要性 | 类型 |
|------|--------|------|
| 标题下方（封面） | 必须 | 封面图 / 氛围图 |
| 每个 H2 标题后 | 推荐 | 章节插图 |
| 数据/对比处 | 推荐 | 信息图 |
| 产品/工具介绍处 | 可选 | 截图 / AI 概念图 |
| 文末总结前 | 可选 | 收尾插图 |

### 决策流程图

```
用户需求 → Step 0 确定需求
                ↓
         Step 1 选风格（展示3个选项）
                ↓
         Step 2 默认AI生成（仅精确数据表格走HTML）
                ↓
         Step 3 生成 → 预览 → 用户确认
           ├→ 满意 → Step 4 上传
           ├→ 文字渲染有误 → 该张改用HTML兜底
           └→ 不满意 → 调整prompt重新生成
```

## 相关 Skills

| Skill | 作用 |
|-------|------|
| `xhs-image` | 小红书配图（姊妹 skill） |
| `image-to-slides` | PPT 配图（风格库来源） |

## 参考文件

- `references/style-gallery.md` — 完整风格库与 prompt 模板
- `references/design-guidelines.md` — 公众号平台设计规范

---

> **花叔出品** | AI Native Coder · 独立开发者
> 公众号「花叔」| 30万+粉丝 | AI工具与效率提升
> 代表作：小猫补光灯（AppStore付费榜Top1）·《一本书玩转DeepSeek》
