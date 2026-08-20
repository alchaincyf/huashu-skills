---
name: huashu-agent-swarm
description: 多Agent蜂群并行协作，纯git自组织，适合大型项目开发。当用户提到"蜂群模式"、"多agent"、"并行开发"、"agent swarm"时使用。
---

# Infinite Agent Loop - 无限Agent蜂群模式

> 受Nicholas Carlini用16个Claude实例自主构建C编译器的启发。
> 没有master agent，纯git自组织，每个agent独立认领任务、写代码、推送。

## 触发条件

当用户提到「蜂群模式」「多agent并行」「infinite loop」「agent swarm」「启动蜂群」时使用此技能。

## 前置要求

- tmux（`brew install tmux`）
- claude CLI（已安装）
- git 仓库（已有或新建）

## 使用流程

### Step 1: 描述项目

用户告诉我：
- 项目目录路径（必须是git仓库）
- 项目目标和总体描述
- 初始任务列表（或让agent自行拆解）
- agent数量（默认8个）
- 代码规范和测试命令

### Step 2: 初始化项目

```bash
bash SKILL_DIR/scripts/setup_project.sh <项目目录>
```

这会在项目中创建：
- `AGENT_PROMPT.md` - 从模板生成，需要我根据用户需求定制
- `TASKS.md` - 初始任务清单
- `current_tasks/` - 任务认领目录
- `agent_logs/` - 日志目录

然后我根据 `references/agent-prompt-template.md` 定制 `AGENT_PROMPT.md`，填入项目具体信息。

### Step 3: 启动蜂群

```bash
bash SKILL_DIR/scripts/start_swarm.sh <agent数量> <项目目录>
```

这会：
1. 为每个agent创建 git worktree（共享.git对象库，不浪费磁盘）
2. 创建 tmux session，每个pane一个agent
3. 每个agent进入无限循环：pull → 认领任务 → 执行 → push → 下一个

### Step 4: 打开观测台

```bash
python3 SKILL_DIR/scripts/dashboard.py <项目目录> 8420
```

浏览器打开 http://localhost:8420，可以：
- 实时查看所有agent状态、git log、任务进度
- 查看每个agent的最新日志
- 输入框直接发送指令给agent（写入HUMAN_INPUT.md）
- 一键停止所有agent

也可以用命令行监控：
```bash
# 终端状态
bash SKILL_DIR/scripts/status.sh <项目目录>

# 发送指令
bash SKILL_DIR/scripts/send_input.sh <项目目录> "你的指令"

# 直接进入tmux观察
tmux attach -t swarm-<项目名>
```

### Step 5: 停止

```bash
bash SKILL_DIR/scripts/stop_swarm.sh <项目目录>
```

自动停止所有agent + 合并分支 + 清理worktrees。

## 核心机制

### Git自组织协调
- 每个agent通过 `current_tasks/*.lock` 文件认领任务
- 通过 `TASKS.md` 了解全局进度
- 通过 `git log` 了解其他agent的工作
- 冲突由agent自行解决

### Git Worktree隔离
- 不用多份clone，用 `git worktree` 实现隔离
- 所有worktree共享同一个 `.git` 对象库
- 每个agent在自己的worktree独立工作

### 无限循环
- 每个agent完成一个session后自动开始下一个
- 通过 `git pull` 获取其他agent的最新成果
- 通过 sleep 间隔避免API限流

## 关键配置

| 参数 | 默认值 | 说明 |
|------|--------|------|
| agent数量 | 8 | 可在启动时指定 |
| sleep间隔 | 5秒 | agent_loop.sh中可调 |
| 模型 | claude-opus-4-6 | agent_loop.sh中可调 |

## 风险和应对

| 风险 | 应对 |
|------|------|
| API限流 | sleep间隔 + 可调agent数量 |
| 合并冲突 | AGENT_PROMPT指导小粒度commit |
| 死循环无用功 | 日志监控 + 停止条件 |
| 磁盘空间 | stop_swarm.sh自动清理 |
| 成本失控 | 可在AGENT_PROMPT中限制session数 |

---

> **花叔出品** | AI Native Coder · 独立开发者
> 公众号「花叔」| 30万+粉丝 | AI工具与效率提升
> 代表作：小猫补光灯（AppStore付费榜Top1）·《一本书玩转DeepSeek》
