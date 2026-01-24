---
name: image-illustration-upload
description: Automatically generates illustrations for articles, uploads to image hosting (ImgBB), and inserts Markdown links. Use when adding images to articles, when user requests illustration, or when article proofreading is complete and needs visuals. Supports AI generation, public domain images, and free stock photos.
---

# 图片配图与上传

为公众号文章自动生成配图、上传到图床、插入Markdown链接的专业能力。

## 何时使用此Skill

当检测到以下场景时，自动加载此skill：
- 用户说"现在配图"、"帮我配图"、"添加图片"
- 文章审校完成后提到配图需求
- 检测到文章内容完整但缺少图片

## 核心功能

1. **分析配图需求**：根据文章内容确定需要5-8张配图
2. **获取图片源**：
   - 公共领域作品（Wikimedia Commons、Google Arts & Culture）
   - AI生成图片（火山引擎 doubao-seedream API）
   - 免费图库（Unsplash、Pexels）
3. **自动上传图床**：调用ImgBB图床，获取永久链接
4. **插入Markdown**：将图片链接插入文章对应位置
5. **验证显示**：确保所有图片链接有效

## 配图数量规范

- **推荐**：5-8张
- **最少**：3张（题图 + 2张正文图）
- **最多**：不超过10张（避免过度打断阅读）

## 配图位置策略

**必配图位置**：
- ✅ 题图（封面图）：标题下方，必须
- ✅ 核心章节：每个重点章节配1张

**可选配图位置**：
- 理论支撑（如引用经典著作）
- 数据可视化（对比图、图表）
- 案例补充（产品截图、示例）

## 图片来源优先级

### 1️⃣ 公共领域作品（最优先）
- **来源**：Wikimedia Commons、Google Arts & Culture
- **适用**：经典艺术作品、历史人物肖像、古籍封面
- **优点**：免费、无版权问题、高质量
- **示例**：梵高《星空》、康德肖像
- **操作**：WebFetch获取Wikimedia Commons图片链接

### 2️⃣ AI生成（推荐）
- **来源**：火山引擎 doubao-seedream-4-0-250828
- **适用**：题图、概念图、抽象主题
- **优点**：原创、可定制、快速
- **操作**：调用API生成图片，返回临时URL

### 3️⃣ 免费图库
- **来源**：Unsplash、Pexels、Pixabay
- **适用**：题图、概念图、背景图
- **优点**：免费、高质量、商业可用（CC0）
- **操作**：WebFetch搜索 + 下载

### 4️⃣ 截图/官方素材（需注明来源）
- **来源**：YouTube、B站、产品官网、电影海报
- **适用**：案例图（产品截图、视频截图）
- **注意**：注明来源，合理使用原则
- **操作**：提醒用户自行截图，或生成AI概念图替代

## 图床上传流程

### 核心脚本
使用项目已有的 `/tools/upload_image.py` 脚本

### 上传方式
```python
# 调用上传脚本（在Bash中）
python3 /Users/alchain/Documents/写作/tools/upload_image.py <图片URL或本地路径>

# 处理网络图片（如AI生成的临时链接）
python3 /Users/alchain/Documents/写作/tools/upload_image.py "https://example.com/ai-generated.jpg"

# 处理本地图片
python3 /Users/alchain/Documents/写作/tools/upload_image.py "/Users/alchain/Pictures/image.png"

# 脚本自动返回ImgBB永久链接
```

### 容错机制
- ✅ 优先上传到ImgBB图床（永久有效）
- ⚠️ 上传失败时，自动使用原链接作为fallback
- 📌 详见 `/tools/README.md` - 图片上传脚本说明

## Markdown插入格式

```markdown
![图片描述](https://i.ibb.co/xxxxx/image.jpg)
```

- 使用永久网络链接（不是本地路径）
- 填写有意义的图片描述（alt text）
- 图片描述要简洁，突出图片内容

## 图片规范

### 尺寸规范
- 封面图：1200x600px (16:9)
- 正文图：800-1200px宽
- 人物/产品：800x800px (1:1)

### 文件规范
- 格式：JPG（照片）/ PNG（插画）
- 大小：< 500KB
- 命名：小写、语义化、英文（如 `mrbeast.jpg`, `starry-night.jpg`）

### 路径规范
- ✅ 网络链接：`https://i.ibb.co/xxxxx/image.jpg`（推荐，永久有效）
- ❌ 本地路径：不再使用本地路径（复制到公众号会失效）

## 版权注意事项

- ✅ 公共领域作品（作者去世70年以上）
- ✅ CC0许可的图片（Unsplash等）
- ✅ AI生成的图片（确认工具许可）
- ⚠️ 截图/官方素材需注明来源

## 配图检查清单

执行配图任务前，确认以下事项：
- [ ] 文章已审校完成，内容稳定
- [ ] 确定配图数量（5-8张）
- [ ] 确定配图位置（题图+核心章节）
- [ ] 所有图片已获取（AI生成/公共领域/免费图库）
- [ ] 所有图片已上传到ImgBB图床
- [ ] 图片链接为永久网络链接（https:// 开头）
- [ ] 已在Markdown中插入图片（使用网络链接）
- [ ] 图片描述（alt text）已填写
- [ ] 所有图片链接验证通过（可正常访问）

## 执行步骤（5步标准流程）

### Step 1: 分析文章，确定配图需求
- 通读全文，标记重点章节
- 列出配图需求清单（6-8项）
- 确定每张图的位置和作用

### Step 2: 获取/生成图片
根据图片来源优先级获取图片：
1. 公共领域作品 → WebFetch获取
2. AI生成 → 调用API生成
3. 免费图库 → WebFetch搜索
4. 截图素材 → 提醒用户提供

### Step 3: 上传到图床，获取永久链接
```bash
# 对每张图片调用上传脚本
python3 /Users/alchain/Documents/写作/tools/upload_image.py <图片URL>
```

### Step 4: 在文章中插入图片
```markdown
![图片描述](https://i.ibb.co/xxxxx/image.jpg)
```

### Step 5: 验证显示
```bash
# 检查所有图片引用
grep -n "!\[" "文章路径.md"
# 所有图片链接应该是 https:// 开头的网络链接
```

## 参考资源

- `/tools/README.md` - 图片上传脚本使用说明
- `/tools/upload_image.py` - 图片上传脚本
- `/公众号写作/AI文生图API调用.md` - AI文生图API说明
- `/公众号写作/images/useless-content/配图Best Practice总结.md` - 配图最佳实践

## 常见问题

### Q1: AI生成的图片临时链接会失效吗？
**A**: 会。所以必须调用`upload_image.py`上传到ImgBB，获取永久链接。

### Q2: 如果图床上传失败怎么办？
**A**: 脚本有容错机制，会自动fallback到原URL。但建议检查ImgBB API配置。

### Q3: 每篇文章必须配图吗？
**A**: 推荐配图，特别是长文（3000字以上）。但短文（1000字以下）可以只配题图。

### Q4: 可以使用本地图片路径吗？
**A**: 不推荐。本地路径在复制到公众号编辑器后会失效，必须使用网络链接。

## 技术依赖

- **Python脚本**: `/tools/upload_image.py`（已有）
- **API配置**: ImgBB API key（已配置在 `~/.zshrc`）
- **AI生成API**: 火山引擎 doubao-seedream（可选）
- **工具**: WebFetch（获取公共领域图片）

## 成功案例

- **《为什么最好的内容都是无用的》**：6张配图（2张公共领域 + 4张AI生成）
- **《DeepSeek-OCR深度评测》**：5张配图，全部上传到ImgBB，复制到公众号无压力

---

**最后更新**: 2025-11-07
**适用项目**: 公众号写作
**维护者**: 花生
