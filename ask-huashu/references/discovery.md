# 发现与安装

仅在成员缺失、名称不清、安装或更新时读。日常路由使用已安装版本，先完成当前任务。

## 找到准确入口

1. 读取 [skills.json](https://github.com/alchaincyf/huashu-skills/blob/master/skills.json)。`repo` 和 `subdir` 指向来源，`name` 是目录使用的安装标识；实际调用名以目标 `SKILL.md` 的 frontmatter 为准。
2. 核对当前仓库的入口和依赖。新项目可能先出现在作者仓库或原帖里，再进入目录；原帖用来发现线索，源文件确定实际能力。`curated: false` 表示待整理条目，不能单凭它判断质量。
3. 安装只处理用户要求的范围。独立发布的人物仓库优先于 Nuwa 的示例副本；同名冲突先查明来源和差异。

两个目录外入口：

- [huashu-cad / SKILL.md](https://github.com/alchaincyf/huashu-cad/blob/main/SKILL.md)：独立 CAD skill。
- [fanbox / skills/fanbox-agent/SKILL.md](https://github.com/alchaincyf/fanbox/blob/master/skills/fanbox-agent/SKILL.md)：应用内嵌指令。

安装规范见总目录的[安装指南](https://github.com/alchaincyf/huashu-skills#安装指南)。嵌套目录需要额外看仓库边界：`huashu-motion` 的 `bin/om` 会调用仓库外层 CLI，保留整个仓库或按其官方包方式安装；不能假定复制一个子目录就包含全部运行文件。

## 被动使用

`ask-huashu` 是用户指派入口。Claude Code 使用 frontmatter 的 `disable-model-invocation: true`；Codex 使用 `agents/openai.yaml`：

```yaml
policy:
  allow_implicit_invocation: false
```

成员是否自动匹配是各自的安装策略。本入口不批量更改它们。用户要求整个系列被动安装时，在本机成员上应用相同语义，保留原来的其它元数据；检查宿主实际识别结果。

被动成员仍是可读取的流程文档。用户明确要求本入口执行任务后，按选定路径读取即可。直接点名成员也是明确使用，不属于自动匹配。

## 更新与验证

记录源仓库、commit、子目录、安装别名及本地策略。更新时先比较上游与本地改动，再恢复被动策略；避免让更新覆盖用户选择。

验证分三层：入口和引用完整；宿主能发现且识别调用策略；所需运行环境和实际任务执行通过。只做了哪层，就报告哪层。没有在每个成员上运行真实任务时，不能把“已安装”写成“全系列可用”。
