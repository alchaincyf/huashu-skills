---
name: prompt-classification-save
description: Automatically identifies prompt type, saves to corresponding category (technical/content/teaching/product/general), and updates index. Use when user says save prompt, record, or organize prompt. Supports 5 major classifications with automatic file naming and indexing.
---

# Prompt分类保存

自动识别Prompt类型、保存到对应分类、更新索引的专业能力。

## 何时使用

- 用户说"保存这个prompt"、"记录一下"、"存起来"
- 用户粘贴prompt并说"帮我整理"

## 核心功能

1. **自动识别类型**：5大分类（技术开发/内容创作/教学设计/产品咨询/通用工具）
2. **提取信息**：用途、来源、适用场景、关键特点
3. **自动保存**：`对应分类/prompt-[序号]-[标题].md`
4. **更新索引**：在 `INDEX.md` 中添加条目

## 5大分类规则

| 分类 | 关键词 | 示例 |
|-----|--------|------|
| 技术开发类 | 编程、调试、代码、优化 | "Python代码优化Prompt" |
| 内容创作类 | 写作、文案、脚本、创作 | "公众号文章生成器" |
| 教学设计类 | 课程、教学、讲解、训练 | "知识点拆解Prompt" |
| 产品咨询类 | 需求、产品、用户、增长 | "用户需求分析Prompt" |
| 通用工具类 | 通用、效率、助手 | "通用翻译工具" |

## 保存格式

```markdown
# [一句话标题]

**来源**: 自创 / 网络 / 修改自xxx
**标签**: #标签1 #标签2 #标签3
**适用场景**: xxx

## Prompt 内容
[完整 prompt，保持原格式]

## 使用示例
[如果有示例或使用心得]

## 效果/备注
[使用效果、注意事项]
```

## 执行流程

1. **识别类型**：根据关键词和内容判断分类
2. **提取信息**：用途、来源、标签、适用场景
3. **生成文件名**：`prompt-[自动递增序号]-[简短标题].md`
4. **保存文件**：到 `/Prompt梳理/[分类]/` 目录
5. **更新索引**：在 `/Prompt梳理/INDEX.md` 中添加条目

## 注意事项

- 如果分类不明确，询问用户意图
- 标题要实用，一眼看懂用途（不超过15字）
- 标签用于快速检索，3-5个为宜
- 保持原prompt的格式和结构
- 网络来源的尽量记录出处

## 参考资源

- `/Prompt梳理/CLAUDE.md` - Prompt管理规则

**最后更新**: 2025-11-07
