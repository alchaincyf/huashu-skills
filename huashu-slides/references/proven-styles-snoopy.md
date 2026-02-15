# Proven Style Guide: Snoopy / Peanuts 温暖漫画风

> 实战验证的风格指南。核心原则：**描述情绪和世界观，不要微操构图细节。让AI自由发挥。**

## 核心风格（只需要记住这些）

**一句话描述：** Peanuts漫画的温暖与哲理感——简单的角色说着深刻的话，日常场景中蕴含人生智慧。

**视觉世界观：**
- 角色包括圆头小孩、小狗、小鸟，它们组成一个温暖的小世界
- 背景极简——草地、天空、狗屋、树就是全部世界
- 色调温暖柔和，像泛黄的报纸漫画
- 哲学感来自「简单角色 × 深刻话语」的反差

## Base Style Prompt

每张slide附加这段即可，**不要在per-slide prompt中重复约束视觉细节**：

```
VISUAL REFERENCE: Charles Schulz Peanuts comic strip — warm, philosophical, charming.
Characters include round-headed kids, a lovable beagle dog, and a small yellow bird.
The world is simple (grass, sky, doghouse, trees) but the ideas are deep.
CANVAS: 16:9 aspect ratio, 2048x1152 pixels, high quality rendering.
COLOR SYSTEM: Warm cream/newspaper tone background, soft muted pastels, warm ink lines (not harsh black). Everything feels like a Sunday morning comic page.
```

## Per-Slide Prompt原则

**DO：**
- 只描述「这页想传达什么感受」+「需要渲染的文字」
- 用一两句话描述画面情绪（"角色在狗屋顶上看星空，若有所思"）
- 让AI自己决定构图、角色数量、背景细节

**DON'T：**
- ❌ 不要指定具体颜色hex值的比例（60%/25%/15%）
- ❌ 不要写CSS式的布局指令（"标题居中偏上"、"副标题放在speech bubble中"）
- ❌ 不要限制角色数量或具体姿势（"角色坐在草地上仰望"）
- ❌ 不要限制"NOT Snoopy or Charlie Brown"——这种反面约束反而让AI生成的角色更单调

## Prompt示例（好 vs 坏）

**坏（过度约束）：**
```
A cute round-headed cartoon character (NOT Snoopy or Charlie Brown — an original
simple character with Peanuts proportions) sits on a simple zigzag grass line,
gazing up at the large hand-lettered title floating above. Background: soft warm
cream (#FFF8E8) 60%. Ink color: warm brown-black (#333333). A speech bubble extends
from the character with subtitle text. Small puffy clouds dot the sky. Bottom:
small text in 10pt.
```
→ 结果：只有一个generic圆头小人，没有狗，没有鸟，构图死板

**好（描述情绪，给AI空间）：**
```
Create a warm Peanuts-style cover slide.

[Base Style]

The cover should feel inviting and curious — like the opening panel of a
Sunday comic strip where something interesting is about to happen.

TEXT TO RENDER:
- Title: "企业AI实战培训"
- Subtitle: "Day 2 — 数据分析与办公提效"
- Footer: "讲师：花生 | 2026年2月"

Let the characters and scene naturally complement the topic.
```
→ 结果：Charlie Brown坐在桌前工作，Snoopy趴在旁边陪伴，自然温馨

## 适用场景

| 场景 | 匹配度 |
|------|--------|
| 产品/品牌介绍 | 极佳 |
| 教育/培训 | 极佳 |
| 个人分享/演讲 | 极佳 |
| 数据报告 | 好 |
| 严肃商业提案 | 一般 |
| 复杂技术架构 | 不推荐 |

## 实战经验

- **2026-02-08 Day1课件（原版prompt）：** 10张slides，角色多样（小孩+狗+鸟），构图丰富，效果极佳
- **2026-02-08 Day2测试（过度约束版prompt）：** 5张slides，只有一个圆头角色，无狗无鸟，多样性差
- **教训：** few-shot越多、限制越细，生成多样性越差。信任AI的创造力。
