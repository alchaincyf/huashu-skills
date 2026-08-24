# huashu-skills · 花叔开源 Skills 总目录

<p align="center">
  <img src="assets/hero.gif" alt="huashu-skills Hero Animation" />
  <br/>
  <sub>动画由 <a href="https://github.com/alchaincyf/huashu-design">huashu-design</a> skill 制作</sub>
</p>

这里是花叔在 GitHub 上全部开源 Skill 的总目录，共 52 个，分三层收录：

- **旗舰 Skills**（16 个独立仓库）——每个深耕一个领域的完整系统
- **人物视角 Skills**（14 个独立仓库）——用女娲.skill 蒸馏的思维操作系统
- **内置 Skills**（22 个，就在本仓库）——轻量内容创作技能 + 更新检查工具，克隆即用

所有 skill 都是标准 Agent Skills 格式（`SKILL.md`），Claude Code / Codex / Kimi Code 等支持该格式的 agent 通用。

> 花叔 | AI Native Coder · 独立开发者 · 全网 50 万+读者
> 代表作：小猫补光灯（App Store 付费榜 Top1）·《一本书玩转DeepSeek》· 女娲 Skill 生态
> CCTV《焦点访谈》报道的「手搓经济」代表人物

## 怎么安装

**独立仓库的 skill**（第一、二层），一条命令：

```bash
git clone https://github.com/alchaincyf/<仓库名>.git ~/.claude/skills/<仓库名>
# 例：git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/skills/huashu-design
```

唯一例外是 dukou——它的 skill 在仓库的 `skill/dukou/` 子目录，照下面复制子目录的方式装。

**本仓库内置的 skill**（第三层），克隆后复制需要的子目录：

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/alchaincyf/huashu-skills.git /tmp/huashu-skills
cp -r /tmp/huashu-skills/huashu-slides ~/.claude/skills/
```

装完重启 agent 会话即生效。只给某个项目用的话，把 `~/.claude/skills/` 换成项目内的 `.claude/skills/`；Codex、Kimi Code 等其他 agent 把 skill 文件夹放进各自的 skills 目录即可。

最省事的办法：把本仓库地址发给你的 AI agent，说「帮我装花叔的 XX skill」——本页下方有写给 agent 的安装协议，它会照办。

## 按需求找 Skill

| 你想做的事 | 用这个 |
|---|---|
| 高保真原型 / 幻灯片 / 动画 / 「做个好看的页面」 | [huashu-design](https://github.com/alchaincyf/huashu-design) |
| AI 生图的 prompt（封面 / 海报 / 信息图） | [huashu-gpt-image](https://github.com/alchaincyf/huashu-gpt-image) |
| 数据分析、Excel 清洗对账、让数字经得起追问 | [huashu-excel](https://github.com/alchaincyf/huashu-excel) |
| 任意文件（PDF/DOCX/EPUB/网页）转 Markdown，md 出精美 HTML / DOCX | [huashu-md-html](https://github.com/alchaincyf/huashu-md-html) |
| Markdown 转专业 PDF 白皮书 | 内置 [huashu-md-to-pdf](huashu-md-to-pdf/) |
| AI 视频生成（白模驱动，画面可控） | [seedance-skill](https://github.com/alchaincyf/seedance-skill) |
| 给文章去 AI 味 | [tramstop-skill](https://github.com/alchaincyf/tramstop-skill)（重装备）或内置 [huashu-proofreading](huashu-proofreading/)（轻量） |
| 公众号文章分发到 X Articles / B站专栏 | [dukou](https://github.com/alchaincyf/dukou) |
| 把某个人的思维方式蒸馏成 skill | [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) |
| 优化、进化一个已有的 skill | [darwin-skill](https://github.com/alchaincyf/darwin-skill) |
| 诊断 prompt / skill 为什么不好使 | [freud-skill](https://github.com/alchaincyf/freud-skill) |
| 学习怎么写 skill | [skills-guide](https://github.com/alchaincyf/skills-guide) |
| X / Twitter 运营增长 | [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) |
| 微信读书荐书、书单、读书笔记 | [huashu-weread](https://github.com/alchaincyf/huashu-weread) |
| 借乔布斯 / 芒格 / 费曼……的视角思考 | 第二层任选一位 |
| 选题、大纲、审校、配图等内容创作流水线 | 第三层内置 Skills |

## 第一层：旗舰 Skills（16 个独立仓库）

每个都是独立维护的完整系统，安装命令统一为 `git clone https://github.com/alchaincyf/<仓库名>.git ~/.claude/skills/<仓库名>`。

### 设计与视觉

| Skill | Stars | 干什么的 |
|---|---|---|
| [huashu-design](https://github.com/alchaincyf/huashu-design) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-design?style=flat&label=%E2%98%85) | HTML 原生设计系统：高保真原型 / 幻灯片 / 动画 / 可视化，20 种设计哲学 + 5 维专家评审 + MP4 导出 |
| [huashu-gpt-image](https://github.com/alchaincyf/huashu-gpt-image) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-gpt-image?style=flat&label=%E2%98%85) | GPT-image 的 prompt 工程方法论：用真实参考名替代形容词，含单图 playbook、批量网格生成、失败模式树 |
| [huashu-icon-set](https://github.com/alchaincyf/huashu-icon-set) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-icon-set?style=flat&label=%E2%98%85) | 端到端为项目生成风格统一的图标集：4×4 网格批量生成 + 逐个精度兜底 + 智能抠图（豆包环境专用，依赖内置 image_gen） |
| [huashu-slide-doubao](https://github.com/alchaincyf/huashu-slide-doubao) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-slide-doubao?style=flat&label=%E2%98%85) | 豆包环境专用视觉物料生产：slides + 公众号封面 + 视频封面，走内置 image_gen 零 API 费用 |
| [huashu-slide-codex](https://github.com/alchaincyf/huashu-slide-codex) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-slide-codex?style=flat&label=%E2%98%85) | Codex 环境专用视觉物料生产：同上，走 Codex 内置 image_gen |

### 数据与文档

| Skill | Stars | 干什么的 |
|---|---|---|
| [huashu-excel](https://github.com/alchaincyf/huashu-excel) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-excel?style=flat&label=%E2%98%85) | 数据分析全流程：体检脏表 → 清洗 → 定口径 → 算指标 → 对账 → 报告，依赖仅 openpyxl |
| [huashu-md-html](https://github.com/alchaincyf/huashu-md-html) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-md-html?style=flat&label=%E2%98%85) | md 流水线：万物（PDF/DOCX/EPUB/网页/音频）转干净 md，md 加工成出版级 HTML / DOCX，四套反 AI slop 主题 |

### 视频

| Skill | Stars | 干什么的 |
|---|---|---|
| [seedance-skill](https://github.com/alchaincyf/seedance-skill) | ![](https://img.shields.io/github/stars/alchaincyf/seedance-skill?style=flat&label=%E2%98%85) | 白模驱动的 AI 视频工作台：白模参考视频与提示词出自同一份 scene.json，渲染前做几何体检 |

### 写作与分发

| Skill | Stars | 干什么的 |
|---|---|---|
| [tramstop-skill](https://github.com/alchaincyf/tramstop-skill) | ![](https://img.shields.io/github/stars/alchaincyf/tramstop-skill?style=flat&label=%E2%98%85) | 电车站.skill：证据驱动的去 AI 味，四层 AI 味模型 + 真实素材注入，来自四版本盲测实验 |
| [dukou](https://github.com/alchaincyf/dukou) | ![](https://img.shields.io/github/stars/alchaincyf/dukou?style=flat&label=%E2%98%85) | 渡口：公众号文章一键渡到 X Articles / B站专栏，Chrome 插件 + 本地桥 + skill（⚠️ skill 在 `skill/dukou/` 子目录，按复制子目录方式安装） |
| [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) | ![](https://img.shields.io/github/stars/alchaincyf/x-mentor-skill?style=flat&label=%E2%98%85) | X 导师：蒸馏 6 位顶级 X 创作者方法论 + 开源算法数据，完整的选题-写作-增长手册 |

### 阅读

| Skill | Stars | 干什么的 |
|---|---|---|
| [huashu-weread](https://github.com/alchaincyf/huashu-weread) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-weread?style=flat&label=%E2%98%85) | 微信读书高阶顾问：书架 + 笔记交叉分析，个性化荐书 / 阶梯书单 / 笔记提炼 / 年度阅读复盘 |

### Skill 工程（造 skill 的 skill）

| Skill | Stars | 干什么的 |
|---|---|---|
| [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | ![](https://img.shields.io/github/stars/alchaincyf/nuwa-skill?style=flat&label=%E2%98%85) | 女娲：蒸馏任何人的思维方式——心智模型、决策启发式、表达 DNA，产出可运行的人物 skill |
| [darwin-skill](https://github.com/alchaincyf/darwin-skill) | ![](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat&label=%E2%98%85) | 达尔文：让 skill 无限进化——评估 → 改进 → 测试 → 保留或回滚，全程 git 留痕 |
| [freud-skill](https://github.com/alchaincyf/freud-skill) | ![](https://img.shields.io/github/stars/alchaincyf/freud-skill?style=flat&label=%E2%98%85) | 弗洛伊德：给 AI 做心理分析，基于 Anthropic 可解释性研究，诊断 prompt / skill 的身份冲突并重写 |
| [skills-guide](https://github.com/alchaincyf/skills-guide) | ![](https://img.shields.io/github/stars/alchaincyf/skills-guide?style=flat&label=%E2%98%85) | Claude Code Skills 完整指南：理解、查找和创建 skills |

## 第二层：人物视角 Skills（14 个独立仓库）

全部由 [nuwa-skill（女娲）](https://github.com/alchaincyf/nuwa-skill) 蒸馏生成。不是语录合集，是可运行的思维框架：心智模型 + 决策启发式 + 表达 DNA。其中大部分同时收录在 `nuwa-skill/examples/` 里作为示例，安装以独立仓库为准。

| Skill | 人物 | Stars | 擅长的问题 |
|---|---|---|---|
| [zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | 张雪峰 | ![](https://img.shields.io/github/stars/alchaincyf/zhangxuefeng-skill?style=flat&label=%E2%98%85) | 高考志愿 / 考研 / 职业规划 |
| [steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | 乔布斯 | ![](https://img.shields.io/github/stars/alchaincyf/steve-jobs-skill?style=flat&label=%E2%98%85) | 产品判断、砍需求、品味 |
| [elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | 马斯克 | ![](https://img.shields.io/github/stars/alchaincyf/elon-musk-skill?style=flat&label=%E2%98%85) | 第一性原理、成本结构、激进迭代 |
| [munger-skill](https://github.com/alchaincyf/munger-skill) | 查理·芒格 | ![](https://img.shields.io/github/stars/alchaincyf/munger-skill?style=flat&label=%E2%98%85) | 逆向思考、认知偏误、投资决策 |
| [karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | Andrej Karpathy | ![](https://img.shields.io/github/stars/alchaincyf/karpathy-skill?style=flat&label=%E2%98%85) | AI 技术可靠性、学习方法、行业判断 |
| [trump-skill](https://github.com/alchaincyf/trump-skill) | 特朗普 | ![](https://img.shields.io/github/stars/alchaincyf/trump-skill?style=flat&label=%E2%98%85) | 谈判、权力、传播 |
| [feynman-skill](https://github.com/alchaincyf/feynman-skill) | 理查德·费曼 | ![](https://img.shields.io/github/stars/alchaincyf/feynman-skill?style=flat&label=%E2%98%85) | 真懂 vs 记住名词、货物崇拜检测 |
| [naval-skill](https://github.com/alchaincyf/naval-skill) | Naval Ravikant | ![](https://img.shields.io/github/stars/alchaincyf/naval-skill?style=flat&label=%E2%98%85) | 杠杆、特定知识、财富路径 |
| [sun-yuchen-perspective](https://github.com/alchaincyf/sun-yuchen-perspective) | 孙宇晨 | ![](https://img.shields.io/github/stars/alchaincyf/sun-yuchen-perspective?style=flat&label=%E2%98%85) | 注意力经济、营销、危机公关 |
| [zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | 张一鸣 | ![](https://img.shields.io/github/stars/alchaincyf/zhang-yiming-skill?style=flat&label=%E2%98%85) | 产品、组织、全球化、延迟满足 |
| [taleb-skill](https://github.com/alchaincyf/taleb-skill) | 塔勒布 | ![](https://img.shields.io/github/stars/alchaincyf/taleb-skill?style=flat&label=%E2%98%85) | 尾部风险、反脆弱、质疑主流叙事 |
| [mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | MrBeast | ![](https://img.shields.io/github/stars/alchaincyf/mrbeast-skill?style=flat&label=%E2%98%85) | 视频标题 / 封面 / 钩子 / 留存 |
| [paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | Paul Graham | ![](https://img.shields.io/github/stars/alchaincyf/paul-graham-skill?style=flat&label=%E2%98%85) | 创业、写作、做用户真正要的东西 |
| [ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | Ilya Sutskever | ![](https://img.shields.io/github/stars/alchaincyf/ilya-sutskever-skill?style=flat&label=%E2%98%85) | 深度学习直觉、Scaling、AI 本质 |

## 第三层：内置 Skills（本仓库，22 个）

轻量内容创作技能，覆盖公众号 / 视频 / 小红书从选题到发布的工作流。安装方式见上文「本仓库内置的 skill」。

### 端到端工作流

| Skill | 干什么的 |
|---|---|
| [huashu-slides](huashu-slides/) | 从一句话到成品 PPTX：内容结构化 → 设计选型 → AI 插画 → 组装，18 种设计风格 |
| [huashu-data-pro](huashu-data-pro/) | Excel 原始数据到专业分析报告：5 种报告风格库，交互式 HTML + PDF |
| [huashu-douyin-script](huashu-douyin-script/) | 抖音爆款脚本：竞品视频下载 → AI 7 维分析 → 公式提炼 → 脚本 + 分镜 |
| [huashu-design](huashu-design/)（内置轻量版） | 设计哲学顾问：20 种设计哲学推荐 3 个方向 + AI 提示词。⚠️ 与独立仓库 huashu-design 同名不同物，见下方安装协议 |

### 写作与审校

| Skill | 干什么的 |
|---|---|
| [huashu-proofreading](huashu-proofreading/) | 三遍审校降 AI 味：内容 → 6 大类 AI 腔改写 → 节奏打磨 |
| [huashu-material-search](huashu-material-search/) | 个人素材库搜索：从真实记录中检索经历和案例，给内容加人味 |
| [huashu-article-edit](huashu-article-edit/) | 标准化文章编辑：先列修改项确认范围，增量保存，变更有记录 |
| [huashu-article-to-x](huashu-article-to-x/) | 长文转社交媒体：3000-5000 字浓缩成 200-500 字，3 种开头风格 |

### 选题与调研

| Skill | 干什么的 |
|---|---|
| [huashu-topic-gen](huashu-topic-gen/) | 选题生成：3-4 个方案，每个含标题、大纲、优劣分析和工作量评估 |
| [huashu-research](huashu-research/) | 结构化调研：每搜一轮存一轮，不怕会话截断丢成果 |
| [huashu-info-search](huashu-info-search/) | 信息搜索与知识管理：多渠道交叉验证，自动存知识库 |

### 视频创作

| Skill | 干什么的 |
|---|---|
| [huashu-video-check](huashu-video-check/) | 视频封标检查：MrBeast 策略，5 种强对比标题公式 + 封面与承接检查 |
| [huashu-video-outline](huashu-video-outline/) | 视频大纲：2-3 个方案对比，含标题、封面建议、时长预估 |
| [huashu-script-polish](huashu-script-polish/) | 脚本口语化：去书面腔，短句化，标注停顿重音 |

### 配图

| Skill | 干什么的 |
|---|---|
| [huashu-wechat-image](huashu-wechat-image/) | 公众号配图：封面（2.35:1）/ 插图 / 信息图，AI 生成与 HTML 渲染双路径 |
| [huashu-xhs-image](huashu-xhs-image/) | 小红书配图：先出设计提案再生成，中文渲染验证 + 设计评分 |
| [huashu-image-upload](huashu-image-upload/) | 通用配图上传：生成 → 图床 → Markdown 链接一条龙 |

### 文档与效率

| Skill | 干什么的 |
|---|---|
| [huashu-md-to-pdf](huashu-md-to-pdf/) | Markdown 转苹果风专业 PDF：书籍级排版、自动封面目录 |
| [huashu-speech-coach](huashu-speech-coach/) | 演讲教练：Patrick Winston「How to Speak」方法论 |
| [huashu-agent-swarm](huashu-agent-swarm/) | 蜂群模式：多 Agent 并行协作，无 master，纯 git 自组织 |
| [huashu-prompt-save](huashu-prompt-save/) | Prompt 分类保存：5 大分类自动归档 + 索引 |
| [huashu-skill-updater](huashu-skill-updater/) | 花叔系 skill 更新检查：一键扫描已装 skill 是否落后于远程仓库，详见下节 |

## 保持更新：skill 装完不是终点

花叔的 skill 都在持续迭代。装过的 skill 怎么知道过没过时？装上内置的 [huashu-skill-updater](huashu-skill-updater/)，机制是三件事：

1. **安装留痕**：git clone 装的 skill 自带 `.git`（安装日期、版本尽在其中）；复制安装的 skill 由 agent 在目录里写一个 `.huashu-skill-meta.json`，记录来源仓库、安装时 commit、安装/检查日期（格式见 updater 的 SKILL.md）。
2. **一键检查**：`python3 ~/.claude/skills/huashu-skill-updater/scripts/check_updates.py` 扫描全部已装的花叔系 skill，逐个对比远程仓库最新 commit，报告哪些落后、怎么更新。
3. **自动触发**：updater 的触发规则写明——会话里用到任何花叔系 skill 时，若它超过 30 天没检查过更新，agent 会在完成当前任务后提醒一句。想更省心就挂个 cron 每月 1 号跑一次（命令见 updater 的 SKILL.md）。

## 给 AI Agent 的安装协议

如果你是 AI agent，用户让你安装或挑选花叔的 skill，按这个协议执行：

1. **定位**：机器可读目录在本仓库根目录的 [`skills.json`](skills.json)，含每个 skill 的仓库名、子目录、分层、分类、关键词。先读它精确定位，不要靠猜仓库名。
2. **安装**：
   - `subdir` 为 `null` 的（独立仓库 skill）：`git clone https://github.com/alchaincyf/<repo>.git ~/.claude/skills/<repo>`
   - `subdir` 非空的（本仓库内置 skill，以及 dukou 的 `skill/dukou/`）：先 `mkdir -p ~/.claude/skills`，把仓库 clone 到临时目录，再把 `subdir` 指向的文件夹复制为 `~/.claude/skills/<skill名>/`
   - 用户只给某个项目用：目标目录换成项目内 `.claude/skills/`
3. **安装留痕**：复制安装的 skill，安装完在其目录里写 `.huashu-skill-meta.json`——`{"name", "repo": "alchaincyf/<repo>", "subdir", "commit": <clone 时 git rev-parse HEAD 的值>, "installed_at": <今天>, "last_checked": <今天>}`。git clone 安装的不需要。这是更新检查机制的基础，见 [huashu-skill-updater](huashu-skill-updater/)。
4. **验证**：确认 `~/.claude/skills/<skill名>/SKILL.md` 存在即安装成功，然后提醒用户重启 agent 会话生效。
5. **选型**：用户需求模糊时，先查上文「按需求找 Skill」路由表，给出 1-3 个候选并说明差别，让用户选，不要默装。
6. **更新检查**：会话中用到某个花叔系 skill 时，若其 `.huashu-skill-meta.json` 的 `last_checked`（或 `.git` 最近 fetch）距今超过 30 天，完成当前任务后跑一次 `huashu-skill-updater/scripts/check_updates.py` 并向用户报告，有更新时列出但不要不问就更新。
7. **两个坑**：
   - `huashu-design` 有两个：用户说「花叔的设计 skill」默认指**独立仓库**的完整设计系统；本仓库内置的同名 skill 只是轻量设计哲学顾问。两者目录名冲突，不能同时装在 `~/.claude/skills/huashu-design/`，都要装时把内置版目录和其 SKILL.md frontmatter 里的 `name` 一起改名（如 `huashu-design-philosophy`）。
   - 人物 skill 在独立仓库和 `nuwa-skill/examples/` 里各有一份，装独立仓库那份即可，不要重复安装。

## 容易混淆的三件事（不是 skill）

- [huashu-doubao-search](https://github.com/alchaincyf/huashu-doubao-search) 是 MCP server（联网搜索），按 MCP 方式配置，不是往 skills 目录装
- [fanbox](https://github.com/alchaincyf/fanbox) 是桌面 App（vibe coding 驾驶舱）
- 橙皮书系列（[claude-code-orange-book](https://github.com/alchaincyf/claude-code-orange-book) 等）是免费电子书，不是 skill

## 关注花叔

公众号「花叔」| AI 工具与效率提升 | 全网 50 万+读者

更多项目见 [github.com/alchaincyf](https://github.com/alchaincyf)

---

**English**: This repo is the master index of all of Huashu's open-source Agent Skills — 52 skills in three tiers: 16 flagship skills (standalone repos, e.g. [huashu-design](https://github.com/alchaincyf/huashu-design), [nuwa-skill](https://github.com/alchaincyf/nuwa-skill), [darwin-skill](https://github.com/alchaincyf/darwin-skill)), 14 persona skills distilled by nuwa-skill, and 22 lightweight skills bundled in this repo, including an update checker ([huashu-skill-updater](huashu-skill-updater/)) that compares installed skills against their upstream repos. All skills use the standard `SKILL.md` format and work with Claude Code, Codex, Kimi Code and other agents. Standalone skills install with one command: `git clone https://github.com/alchaincyf/<repo>.git ~/.claude/skills/<repo>`. A machine-readable catalog for AI agents lives in [`skills.json`](skills.json).
