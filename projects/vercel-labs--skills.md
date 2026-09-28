---
status: "indexed"
source: "https://github.com/vercel-labs/skills"
repository: "vercel-labs/skills"
summary: "一个 npm 命令行工具（npx skills），用于发现、安装、使用、更新和移除遵循 SKILL.md 规范的 AI 编码代理技能（Agent Skills），并将其分发到多种编码代理的技能目录。"
topics: ["agent skills", "SKILL.md", "coding agent CLI", "skills installer", "AI 编码代理技能分发", "npx skills"]
assessment: "not-tested"
---

# vercel-labs/skills

- GitHub: https://github.com/vercel-labs/skills
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/4
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: ac7372a0d64b1731ef331f991a480704bfe6cbfb；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

一个 npm 命令行工具（npx skills），用于发现、安装、使用、更新和移除遵循 SKILL.md 规范的 AI 编码代理技能（Agent Skills），并将其分发到多种编码代理的技能目录。

## 适用场景

- 需要把团队约定的技能（如生成发布说明、按约定开 PR）以 SKILL.md 形式在多个编码代理间共享：用 npx skills add 安装到项目 ./&lt;agent&gt;/skills/ 并随项目提交。
- 需要跨所有项目复用一个技能集合：用 -g/--global 安装到用户目录 ~/&lt;agent&gt;/skills/。
- CI/CD 或脚本化环境中批量安装：用 --skill、-a、-y 非交互装到指定代理。
- 不安装而临时使用某个技能：npx skills use &lt;source&gt; 生成提示词或直接以指定代理交互启动。
- 从私有仓库分发技能（前提是本地 Git 凭据、GitHub CLI 或 SSH 已配置，或显式设置 GITHUB_TOKEN/GH_TOKEN）：按 README 的 Private Repositories 一节命令安装。
- （推断）维护跨 Git 主机（GitHub、GitLab、Azure Repos、任意 git URL、本地路径）的技能来源：README 声明支持这些来源格式。

## 项目宣称的能力

- README 宣称支持 80+ 个编码代理（含 OpenCode、Claude Code、Codex、Cursor 等），并列出各代理的项目/全局路径（Supported Agents 小节），详见其表格。
- 提供完整生命周期命令：add、use、list/ls、find、remove/rm、update、init（Other Commands 小节）。
- 支持多种来源格式：GitHub 短写、完整 URL、仓库内直接路径、GitLab、Azure Repos、任意 git URL、本地路径（Source Formats 小节）。
- 支持私有仓库，复用既有 Git/gh/SSH 认证，并可显式设 GITHUB_TOKEN/GH_TOKEN（Private Repositories 小节）。
- 支持交互式选择安装范围（项目/全局）与安装方式（symlink 单源更新、copy 兼容不支持符号链接的环境）（Installation Scope、Installation Methods 小节）。
- 支持技能发现的多级目录（含 .curated/.experimental/.system 等）及 --full-depth、Claude 插件 manifest 发现（Skill Discovery、Plugin Manifest Discovery 小节）；并提供遥测开关与下载/解压体积限制相关环境变量。

## 限制与待验证

- README 宣称的跨代理性与兼容性差异：部分能力（allowed-tools、context: fork、Hooks）按代理不同支持不一致（Compatibility 表格），需按目标代理核对。
- 私有仓库与更新检查依赖本地 Git 凭据/gh/SSH 或显式 token 配置；不配置时可能失败（Private Repositories 小节描述）。
- 直接从 URL 下载时受大小与文件数限制（默认 10 MiB 下载/25 MiB 解压/1000 文件），需用环境变量放宽（Direct download URLs 段落）。
- 默认收集匿名遥测，需显式设置 DISABLE_TELEMETRY=1 或 DO_NOT_TRACK=1 关闭（Telemetry 小节）。
- README 未提供性能、成功率或安全审计等 benchmark/测试数据；实际效果与兼容性需以试用和文档为准。
- 输入未提供 star 数、用户关注原因与 issue 统计；无法据此判断社区使用与维护活跃度。

## 什么情况下重新考虑

- 需要在多个编码代理之间统一管理、共享或版本化技能时。
- 计划在 CI/CD 中自动安装技能或批量分发到指定代理时。
- 遇到从私有仓库、GitLab/Azure/本地路径安装技能失败，需要排查认证或来源解析时。
- 需要判断某技能特性（allowed-tools、hooks、context: fork）在目标代理是否可用时。
- 需要关闭遥测或调整下载/解压上限时。

## 检索关键词

- agent skills
- SKILL.md
- coding agent CLI
- skills installer
- AI 编码代理技能分发
- npx skills
