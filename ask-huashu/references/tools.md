# 工具与方法

这些分支各自完整，按请求直接进入。

| 安装标识 | 何时用 / 必要边界 |
|---|---|
| `nuwa-skill` | 从可核实材料提炼人物的思考框架、决策方式与表达，产出人物 skill |
| `darwin-skill` | 现有 skill 效果不好，需要基于真实案例评估、修改和对照测试 |
| `freud-skill` | 提示词或 skill 的角色、目标与指令彼此冲突，需要诊断 |
| `skills-guide` | 理解 skills、查找或安装合适的技能 |
| `huashu-skill-updater` | 查已装花叔技能的来源和更新情况；更新操作按用户授权执行 |
| `huashu-prompt-save` | 保存已验证或用户指定的提示词，归类并建立索引 |
| `huashu-agent-swarm` | 用户明确要 Git 蜂群协作且具备 tmux、Claude CLI 等环境 |
| `huashu-flash` | 网站或应用性能问题：先测基线，定位瓶颈，再用同一指标验证 |
| `huashu-mac-use` | 操作没有合适 API 的原生 macOS 应用；能力探测后选择控制层 |
| `huashu-weread` | 微信读书书架、笔记、推荐与复盘；实际 name 是 `huashu-weread-advisor`，检查基础 weread 能力与用户授权 |
| `mcstomach` | 从本人订单或明确标注的问卷整理口味偏好；入口在 `mcstomach/` 子目录 |
| `huashu-cad` | 自然语言到可编辑 CAD、装配与相关演示；检查所选 2D/3D 后端 |
| `fanbox-agent` | FanBox 内嵌协作指令，依赖应用注入的环境和控制接口；普通终端中的文件安装不代表 FanBox 可用 |

后两项来自独立仓库实查；总目录尚未收录时，用[发现与安装](discovery.md)里的准确来源定位。

`huashu-chrome`、`huashu-doubao-search` 是工具服务；FanBox 是应用，橙皮书是读物。需要这些能力时按对应项目的安装与运行方式处理。`fanbox-agent` 只是 FanBox 中的一个嵌入技能，不能替代应用。
