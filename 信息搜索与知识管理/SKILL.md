---
name: information-search-knowledge-management
description: Automatically performs multi-channel search, verifies information, and saves to knowledge base when dealing with new products/technologies. Use when discussing new products (released within 3 months), need latest information verification, or user requests search. Prioritizes authoritative tech media and ignores outdated sources.
---

# 信息搜索与知识管理

涉及新产品/新技术时，自动执行多渠道搜索、验证信息、保存知识库。

## 何时使用

- 涉及新产品/新技术（3个月内发布）
- 需要最新信息验证
- 用户说"搜索一下"、"查最新信息"

## 核心功能

1. **多渠道搜索**：官方+媒体+社区
2. **信息源优先级**：权威媒体优先，忽略知乎/百度2025年前
3. **知识管理**：保存到 `_knowledge_base/`，标注来源和时间

## 搜索策略

### 搜索内容
- 产品/技术的官方信息（发布时间、特性、定价）
- 科技媒体报道（TechCrunch, The Verge, Medium等）
- 社区讨论（Reddit, Hacker News, X/Twitter）
- 竞品对比信息
- 相关概念解释

### 信息源优先级

**✅ 优先采信（半年内）**：
1. 权威科技媒体（TechCrunch, The Verge, MIT Tech Review）
2. 社区论坛（Reddit, Hacker News）
3. 官方文档和研究

**❌ 完全忽略**：
- 知乎、百度：2025年之前的信息全部忽略
- 过时内容：超过半年（6个月）
- 营销软文

### 关键词组合
- 主题 + 年份：`"AI detection 2025"`
- 主题 + best practice：`"AI text humanization best practices"`
- 主题 + Reddit：`"AI writing detection reddit 2025"`

## 知识管理

### 保存格式
文件命名：`[主题]-[时间].md`

```markdown
# [主题]相关信息

**信息收集时间**：2025-XX-XX
**下次更新建议**：2025-XX-XX

## 核心发现
- 发现1
- 发现2

## 数据和链接
- 官方文档：xxx
- 媒体报道：xxx

## 信息来源
1. [来源1](链接)
2. [来源2](链接)
```

### 保存位置
- 公众号写作：`/公众号写作/_knowledge_base/`
- 视频创作：`/视频创作/_knowledge_base/`

## 注意事项

- 所有信息必须标注来源和时间
- 不确定的信息向用户说明
- 信息冲突时，优先采信权威来源

**最后更新**: 2025-11-07
