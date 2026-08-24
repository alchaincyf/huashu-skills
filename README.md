# huashu-skills · 花叔开源Skills总目录

<p align="center">
  <img src="assets/hero.gif" alt="huashu-skills Hero Animation" />
  <br/>
  <sub>动画由 <a href="https://github.com/alchaincyf/huashu-design">huashu-design</a> skill制作</sub>
</p>

这里是花叔在GitHub上全部开源Skill的总目录，共52个，分三层收录。全部是标准Agent Skills格式（`SKILL.md`），Claude Code / Codex / Kimi Code等支持该格式的agent通用。

> 花叔 | AI Native Coder · 独立开发者 · 全网50万+读者
> 代表作：小猫补光灯（App Store付费榜Top1）·《一本书玩转DeepSeek》· 女娲Skill生态
> CCTV《焦点访谈》报道的「手搓经济」代表人物

## 目录

- [30秒上手](#30秒上手)
- [全景一览](#全景一览)
- [按需求找Skill](#按需求找skill)
- [旗舰Skills](#旗舰skills)（16个独立仓库）
- [人物视角Skills](#人物视角skills)（14个独立仓库）
- [内置Skills](#内置skills)（22个，本仓库）
- [安装指南](#安装指南)
- [保持更新](#保持更新)
- [给AI Agent的协议](#给ai-agent的协议)
- [这三个不是Skill](#这三个不是skill)

## 30秒上手

最省事的方式：把这句话发给你的AI agent——

> 读 https://github.com/alchaincyf/huashu-skills 的README和skills.json，帮我安装（某个skill / 按我的需求推荐）

自己动手也只要一条命令（独立仓库skill）：

```bash
git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/skills/huashu-design
```

装完重启agent会话即生效。其余安装方式见[安装指南](#安装指南)。

## 全景一览

| 层 | 数量 | 是什么 | 怎么装 |
|---|---|---|---|
| [旗舰Skills](#旗舰skills) | 16 | 各自深耕一个领域的完整系统，独立仓库 | git clone一条命令 |
| [人物视角Skills](#人物视角skills) | 14 | 女娲蒸馏的人物思维操作系统，独立仓库 | git clone一条命令 |
| [内置Skills](#内置skills) | 22 | 轻量内容创作技能+更新检查工具，就在本仓库 | 复制子目录 |

机器可读版目录在[`skills.json`](skills.json)，AI agent优先读它。

## 按需求找Skill

| 你想做的事 | 用这个 |
|---|---|
| 高保真原型 / 幻灯片 / 动画 / 「做个好看的页面」 | [huashu-design](https://github.com/alchaincyf/huashu-design) |
| AI生图的prompt（封面 / 海报 / 信息图） | [huashu-gpt-image](https://github.com/alchaincyf/huashu-gpt-image) |
| 数据分析、Excel清洗对账、让数字经得起追问 | [huashu-excel](https://github.com/alchaincyf/huashu-excel) |
| 任意文件（PDF/DOCX/EPUB/网页）转Markdown，md出精美HTML / DOCX | [huashu-md-html](https://github.com/alchaincyf/huashu-md-html) |
| Markdown转专业PDF白皮书 | 内置[huashu-md-to-pdf](huashu-md-to-pdf/) |
| AI视频生成（白模驱动，画面可控） | [seedance-skill](https://github.com/alchaincyf/seedance-skill) |
| 给文章去AI味 | [tramstop-skill](https://github.com/alchaincyf/tramstop-skill)（重装备）或内置[huashu-proofreading](huashu-proofreading/)（轻量） |
| 公众号文章分发到X Articles / B站专栏 | [dukou](https://github.com/alchaincyf/dukou) |
| 把某个人的思维方式蒸馏成skill | [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) |
| 优化、进化一个已有的skill | [darwin-skill](https://github.com/alchaincyf/darwin-skill) |
| 诊断prompt / skill为什么不好使 | [freud-skill](https://github.com/alchaincyf/freud-skill) |
| 学习怎么写skill | [skills-guide](https://github.com/alchaincyf/skills-guide) |
| X / Twitter运营增长 | [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) |
| 微信读书荐书、书单、读书笔记 | [huashu-weread](https://github.com/alchaincyf/huashu-weread) |
| 借乔布斯 / 芒格 / 费曼……的视角思考 | [人物视角Skills](#人物视角skills)任选一位 |
| 选题、大纲、审校、配图等内容创作流水线 | [内置Skills](#内置skills) |
| 检查装过的skill有没有新版本 | 内置[huashu-skill-updater](huashu-skill-updater/) |

## 旗舰Skills

16个独立仓库，每个都是完整系统。安装：`git clone https://github.com/alchaincyf/<仓库名>.git ~/.claude/skills/<仓库名>`（dukou除外，见表格备注）。

### 设计与视觉

| Skill | Stars | 干什么的 |
|---|---|---|
| [huashu-design](https://github.com/alchaincyf/huashu-design) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-design?style=flat&label=%E2%98%85) | HTML原生设计系统：高保真原型 / 幻灯片 / 动画 / 可视化，20种设计哲学+5维专家评审+MP4导出 |
| [huashu-gpt-image](https://github.com/alchaincyf/huashu-gpt-image) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-gpt-image?style=flat&label=%E2%98%85) | GPT-image的prompt工程方法论：用真实参考名替代形容词，含单图playbook、批量网格生成、失败模式树 |
| [huashu-icon-set](https://github.com/alchaincyf/huashu-icon-set) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-icon-set?style=flat&label=%E2%98%85) | 端到端为项目生成风格统一的图标集：4×4网格批量生成+逐个精度兜底+智能抠图（豆包环境专用，依赖内置image_gen） |
| [huashu-slide-doubao](https://github.com/alchaincyf/huashu-slide-doubao) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-slide-doubao?style=flat&label=%E2%98%85) | 豆包环境专用视觉物料生产：slides+公众号封面+视频封面，走内置image_gen零API费用 |
| [huashu-slide-codex](https://github.com/alchaincyf/huashu-slide-codex) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-slide-codex?style=flat&label=%E2%98%85) | Codex环境专用视觉物料生产：同上，走Codex内置image_gen |

### 数据与文档

| Skill | Stars | 干什么的 |
|---|---|---|
| [huashu-excel](https://github.com/alchaincyf/huashu-excel) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-excel?style=flat&label=%E2%98%85) | 数据分析全流程：体检脏表 → 清洗 → 定口径 → 算指标 → 对账 → 报告，依赖仅openpyxl |
| [huashu-md-html](https://github.com/alchaincyf/huashu-md-html) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-md-html?style=flat&label=%E2%98%85) | md流水线：万物（PDF/DOCX/EPUB/网页/音频）转干净md，md加工成出版级HTML / DOCX，四套反AI slop主题 |

### 视频

| Skill | Stars | 干什么的 |
|---|---|---|
| [seedance-skill](https://github.com/alchaincyf/seedance-skill) | ![](https://img.shields.io/github/stars/alchaincyf/seedance-skill?style=flat&label=%E2%98%85) | 白模驱动的AI视频工作台：白模参考视频与提示词出自同一份scene.json，渲染前做几何体检 |

### 写作与分发

| Skill | Stars | 干什么的 |
|---|---|---|
| [tramstop-skill](https://github.com/alchaincyf/tramstop-skill) | ![](https://img.shields.io/github/stars/alchaincyf/tramstop-skill?style=flat&label=%E2%98%85) | 电车站.skill：证据驱动的去AI味，四层AI味模型+真实素材注入，来自四版本盲测实验 |
| [dukou](https://github.com/alchaincyf/dukou) | ![](https://img.shields.io/github/stars/alchaincyf/dukou?style=flat&label=%E2%98%85) | 渡口：公众号文章一键渡到X Articles / B站专栏，Chrome插件+本地桥+skill（⚠️ skill在`skill/dukou/`子目录，按[复制子目录方式](#安装指南)安装） |
| [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) | ![](https://img.shields.io/github/stars/alchaincyf/x-mentor-skill?style=flat&label=%E2%98%85) | X导师：蒸馏6位顶级X创作者方法论+开源算法数据，完整的选题-写作-增长手册 |

### 阅读

| Skill | Stars | 干什么的 |
|---|---|---|
| [huashu-weread](https://github.com/alchaincyf/huashu-weread) | ![](https://img.shields.io/github/stars/alchaincyf/huashu-weread?style=flat&label=%E2%98%85) | 微信读书高阶顾问：书架+笔记交叉分析，个性化荐书 / 阶梯书单 / 笔记提炼 / 年度阅读复盘 |

### Skill工程（造skill的skill）

| Skill | Stars | 干什么的 |
|---|---|---|
| [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | ![](https://img.shields.io/github/stars/alchaincyf/nuwa-skill?style=flat&label=%E2%98%85) | 女娲：蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA，产出可运行的人物skill |
| [darwin-skill](https://github.com/alchaincyf/darwin-skill) | ![](https://img.shields.io/github/stars/alchaincyf/darwin-skill?style=flat&label=%E2%98%85) | 达尔文：让skill无限进化——评估 → 改进 → 测试 → 保留或回滚，全程git留痕 |
| [freud-skill](https://github.com/alchaincyf/freud-skill) | ![](https://img.shields.io/github/stars/alchaincyf/freud-skill?style=flat&label=%E2%98%85) | 弗洛伊德：给AI做心理分析，基于Anthropic可解释性研究，诊断prompt / skill的身份冲突并重写 |
| [skills-guide](https://github.com/alchaincyf/skills-guide) | ![](https://img.shields.io/github/stars/alchaincyf/skills-guide?style=flat&label=%E2%98%85) | Claude Code Skills完整指南：理解、查找和创建skills |

## 人物视角Skills

14个独立仓库，全部由[nuwa-skill（女娲）](https://github.com/alchaincyf/nuwa-skill)蒸馏生成。不是语录合集，是可运行的思维框架：心智模型+决策启发式+表达DNA。安装：`git clone https://github.com/alchaincyf/<仓库名>.git ~/.claude/skills/<仓库名>`。大部分同时收录在`nuwa-skill/examples/`里作为示例，安装以独立仓库为准。

| Skill | 人物 | Stars | 擅长的问题 |
|---|---|---|---|
| [zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | 张雪峰 | ![](https://img.shields.io/github/stars/alchaincyf/zhangxuefeng-skill?style=flat&label=%E2%98%85) | 高考志愿 / 考研 / 职业规划 |
| [steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | 乔布斯 | ![](https://img.shields.io/github/stars/alchaincyf/steve-jobs-skill?style=flat&label=%E2%98%85) | 产品判断、砍需求、品味 |
| [elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | 马斯克 | ![](https://img.shields.io/github/stars/alchaincyf/elon-musk-skill?style=flat&label=%E2%98%85) | 第一性原理、成本结构、激进迭代 |
| [munger-skill](https://github.com/alchaincyf/munger-skill) | 查理·芒格 | ![](https://img.shields.io/github/stars/alchaincyf/munger-skill?style=flat&label=%E2%98%85) | 逆向思考、认知偏误、投资决策 |
| [karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | Andrej Karpathy | ![](https://img.shields.io/github/stars/alchaincyf/karpathy-skill?style=flat&label=%E2%98%85) | AI技术可靠性、学习方法、行业判断 |
| [trump-skill](https://github.com/alchaincyf/trump-skill) | 特朗普 | ![](https://img.shields.io/github/stars/alchaincyf/trump-skill?style=flat&label=%E2%98%85) | 谈判、权力、传播 |
| [feynman-skill](https://github.com/alchaincyf/feynman-skill) | 理查德·费曼 | ![](https://img.shields.io/github/stars/alchaincyf/feynman-skill?style=flat&label=%E2%98%85) | 真懂vs记住名词、货物崇拜检测 |
| [naval-skill](https://github.com/alchaincyf/naval-skill) | Naval Ravikant | ![](https://img.shields.io/github/stars/alchaincyf/naval-skill?style=flat&label=%E2%98%85) | 杠杆、特定知识、财富路径 |
| [sun-yuchen-perspective](https://github.com/alchaincyf/sun-yuchen-perspective) | 孙宇晨 | ![](https://img.shields.io/github/stars/alchaincyf/sun-yuchen-perspective?style=flat&label=%E2%98%85) | 注意力经济、营销、危机公关 |
| [zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | 张一鸣 | ![](https://img.shields.io/github/stars/alchaincyf/zhang-yiming-skill?style=flat&label=%E2%98%85) | 产品、组织、全球化、延迟满足 |
| [taleb-skill](https://github.com/alchaincyf/taleb-skill) | 塔勒布 | ![](https://img.shields.io/github/stars/alchaincyf/taleb-skill?style=flat&label=%E2%98%85) | 尾部风险、反脆弱、质疑主流叙事 |
| [mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | MrBeast | ![](https://img.shields.io/github/stars/alchaincyf/mrbeast-skill?style=flat&label=%E2%98%85) | 视频标题 / 封面 / 钩子 / 留存 |
| [paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | Paul Graham | ![](https://img.shields.io/github/stars/alchaincyf/paul-graham-skill?style=flat&label=%E2%98%85) | 创业、写作、做用户真正要的东西 |
| [ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | Ilya Sutskever | ![](https://img.shields.io/github/stars/alchaincyf/ilya-sutskever-skill?style=flat&label=%E2%98%85) | 深度学习直觉、Scaling、AI本质 |

## 内置Skills

22个轻量技能，就在本仓库，覆盖公众号 / 视频 / 小红书从选题到发布的工作流。安装：按[复制子目录方式](#安装指南)。

### 端到端工作流

| Skill | 干什么的 |
|---|---|
| [huashu-slides](huashu-slides/) | 从一句话到成品PPTX：内容结构化 → 设计选型 → AI插画 → 组装，18种设计风格 |
| [huashu-data-pro](huashu-data-pro/) | Excel原始数据到专业分析报告：5种报告风格库，交互式HTML+PDF |
| [huashu-douyin-script](huashu-douyin-script/) | 抖音爆款脚本：竞品视频下载 → AI 7维分析 → 公式提炼 → 脚本+分镜 |
| [huashu-design](huashu-design/)（内置轻量版） | 设计哲学顾问：20种设计哲学推荐3个方向+AI提示词。⚠️与独立仓库huashu-design同名不同物，见[协议](#给ai-agent的协议) |

### 写作与审校

| Skill | 干什么的 |
|---|---|
| [huashu-proofreading](huashu-proofreading/) | 三遍审校降AI味：内容 → 6大类AI腔改写 → 节奏打磨 |
| [huashu-material-search](huashu-material-search/) | 个人素材库搜索：从真实记录中检索经历和案例，给内容加人味 |
| [huashu-article-edit](huashu-article-edit/) | 标准化文章编辑：先列修改项确认范围，增量保存，变更有记录 |
| [huashu-article-to-x](huashu-article-to-x/) | 长文转社交媒体：3000-5000字浓缩成200-500字，3种开头风格 |

### 选题与调研

| Skill | 干什么的 |
|---|---|
| [huashu-topic-gen](huashu-topic-gen/) | 选题生成：3-4个方案，每个含标题、大纲、优劣分析和工作量评估 |
| [huashu-research](huashu-research/) | 结构化调研：每搜一轮存一轮，不怕会话截断丢成果 |
| [huashu-info-search](huashu-info-search/) | 信息搜索与知识管理：多渠道交叉验证，自动存知识库 |

### 视频创作

| Skill | 干什么的 |
|---|---|
| [huashu-video-check](huashu-video-check/) | 视频封标检查：MrBeast策略，5种强对比标题公式+封面与承接检查 |
| [huashu-video-outline](huashu-video-outline/) | 视频大纲：2-3个方案对比，含标题、封面建议、时长预估 |
| [huashu-script-polish](huashu-script-polish/) | 脚本口语化：去书面腔，短句化，标注停顿重音 |

### 配图

| Skill | 干什么的 |
|---|---|
| [huashu-wechat-image](huashu-wechat-image/) | 公众号配图：封面（2.35:1）/ 插图 / 信息图，AI生成与HTML渲染双路径 |
| [huashu-xhs-image](huashu-xhs-image/) | 小红书配图：先出设计提案再生成，中文渲染验证+设计评分 |
| [huashu-image-upload](huashu-image-upload/) | 通用配图上传：生成 → 图床 → Markdown链接一条龙 |

### 文档与效率

| Skill | 干什么的 |
|---|---|
| [huashu-md-to-pdf](huashu-md-to-pdf/) | Markdown转苹果风专业PDF：书籍级排版、自动封面目录 |
| [huashu-speech-coach](huashu-speech-coach/) | 演讲教练：Patrick Winston「How to Speak」方法论 |
| [huashu-agent-swarm](huashu-agent-swarm/) | 蜂群模式：多Agent并行协作，无master，纯git自组织 |
| [huashu-prompt-save](huashu-prompt-save/) | Prompt分类保存：5大分类自动归档+索引 |
| [huashu-skill-updater](huashu-skill-updater/) | 花叔系skill更新检查：一键扫描已装skill是否落后于远程仓库，详见[保持更新](#保持更新) |

## 安装指南

独立仓库的skill（旗舰+人物两层），一条命令：

```bash
git clone https://github.com/alchaincyf/<仓库名>.git ~/.claude/skills/<仓库名>
# 例：git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/skills/huashu-design
```

本仓库内置的skill（以及dukou，它的skill在仓库的`skill/dukou/`子目录），克隆后复制需要的子目录：

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/alchaincyf/huashu-skills.git /tmp/huashu-skills
cp -r /tmp/huashu-skills/huashu-slides ~/.claude/skills/
```

三点通用说明：

- 装完重启agent会话即生效
- 只给某个项目用的话，把`~/.claude/skills/`换成项目内的`.claude/skills/`
- Codex、Kimi Code等其他agent把skill文件夹放进各自的skills目录即可

## 保持更新

花叔的skill都在持续迭代。装过的skill怎么知道过没过时？装上内置的[huashu-skill-updater](huashu-skill-updater/)，机制是三件事：

1. 安装留痕：git clone装的skill自带`.git`（安装日期、版本尽在其中）；复制安装的skill由agent在目录里写一个`.huashu-skill-meta.json`，记录来源仓库、安装时commit、安装 / 检查日期（格式见updater的SKILL.md）
2. 一键检查：`python3 ~/.claude/skills/huashu-skill-updater/scripts/check_updates.py`扫描全部已装的花叔系skill，逐个对比远程仓库最新commit，报告哪些落后、怎么更新
3. 自动触发：会话里用到任何花叔系skill时，若它超过30天没检查过更新，agent会在完成当前任务后提醒一句。想更省心就挂个cron每月1号跑一次（命令见updater的SKILL.md）

## 给AI Agent的协议

如果你是AI agent，用户让你安装或挑选花叔的skill，按这个协议执行：

1. 定位：机器可读目录在本仓库根目录的[`skills.json`](skills.json)，含每个skill的仓库名、子目录、分层、分类、关键词。先读它精确定位，不要靠猜仓库名。
2. 安装：
   - `subdir`为`null`的（独立仓库skill）：`git clone https://github.com/alchaincyf/<repo>.git ~/.claude/skills/<repo>`
   - `subdir`非空的（本仓库内置skill，以及dukou的`skill/dukou/`）：先`mkdir -p ~/.claude/skills`，把仓库clone到临时目录，再把`subdir`指向的文件夹复制为`~/.claude/skills/<skill名>/`
   - 用户只给某个项目用：目标目录换成项目内`.claude/skills/`
3. 安装留痕：复制安装的skill，安装完在其目录里写`.huashu-skill-meta.json`——`{"name", "repo": "alchaincyf/<repo>", "subdir", "commit": <clone时git rev-parse HEAD的值>, "installed_at": <今天>, "last_checked": <今天>}`。git clone安装的不需要。这是更新检查机制的基础，见[huashu-skill-updater](huashu-skill-updater/)。
4. 验证：确认`~/.claude/skills/<skill名>/SKILL.md`存在即安装成功，然后提醒用户重启agent会话生效。
5. 选型：用户需求模糊时，先查上文[按需求找Skill](#按需求找skill)路由表，给出1-3个候选并说明差别，让用户选，不要默装。
6. 更新检查：会话中用到某个花叔系skill时，若其`.huashu-skill-meta.json`的`last_checked`（或`.git`最近fetch）距今超过30天，完成当前任务后跑一次`huashu-skill-updater/scripts/check_updates.py`并向用户报告，有更新时列出但不要不问就更新。
7. 两个坑：
   - `huashu-design`有两个：用户说「花叔的设计skill」默认指独立仓库的完整设计系统；本仓库内置的同名skill只是轻量设计哲学顾问。两者目录名冲突，不能同时装在`~/.claude/skills/huashu-design/`，都要装时把内置版目录和其SKILL.md frontmatter里的`name`一起改名（如`huashu-design-philosophy`）。
   - 人物skill在独立仓库和`nuwa-skill/examples/`里各有一份，装独立仓库那份即可，不要重复安装。

## 这三个不是Skill

容易混淆、但不该往skills目录装的仓库：

- [huashu-doubao-search](https://github.com/alchaincyf/huashu-doubao-search)是MCP server（联网搜索），按MCP方式配置
- [fanbox](https://github.com/alchaincyf/fanbox)是桌面App（vibe coding驾驶舱）
- 橙皮书系列（[claude-code-orange-book](https://github.com/alchaincyf/claude-code-orange-book)等）是免费电子书

## 关注花叔

公众号「花叔」| AI工具与效率提升 | 全网50万+读者

更多项目见 [github.com/alchaincyf](https://github.com/alchaincyf)

---

**English**: This repo is the master index of all of Huashu's open-source Agent Skills — 52 skills in three tiers: 16 flagship skills (standalone repos, e.g. [huashu-design](https://github.com/alchaincyf/huashu-design), [nuwa-skill](https://github.com/alchaincyf/nuwa-skill), [darwin-skill](https://github.com/alchaincyf/darwin-skill)), 14 persona skills distilled by nuwa-skill, and 22 lightweight skills bundled in this repo, including an update checker ([huashu-skill-updater](huashu-skill-updater/)) that compares installed skills against their upstream repos. All skills use the standard `SKILL.md` format and work with Claude Code, Codex, Kimi Code and other agents. Standalone skills install with one command: `git clone https://github.com/alchaincyf/<repo>.git ~/.claude/skills/<repo>`. A machine-readable catalog for AI agents lives in [`skills.json`](skills.json).
