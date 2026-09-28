---
status: "indexed"
source: "https://github.com/ilang-ai/Imprint"
repository: "ilang-ai/Imprint"
summary: "一个基于 SKILL.md 的便携个人工作画像（imprint）技能，宣称通过一次访谈提取用户的工作风格并编码为可跨 AI 代理移植的纯文本配置，为记忆、压缩、代码审查、调试、规划、Git 工作流等场景提供个性化上下文。"
topics: ["AI agent skill", "portable profile", "SKILL.md", "memory compression", "code review personalization", "iLang protocol"]
assessment: "not-tested"
---

# ilang-ai/Imprint

- GitHub: https://github.com/ilang-ai/Imprint
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/11
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: bb208527256f9e6e6d4d627c888d54997e2da889；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

一个基于 SKILL.md 的便携个人工作画像（imprint）技能，宣称通过一次访谈提取用户的工作风格并编码为可跨 AI 代理移植的纯文本配置，为记忆、压缩、代码审查、调试、规划、Git 工作流等场景提供个性化上下文。

## 适用场景

- 使用支持 SKILL.md 的多款 AI 编码代理（如 Claude Code、Cursor、Copilot、Windsurf 等），希望统一个人偏好与项目规则的场景；前提是代理确实按文档路径读取技能文件。
- 需要为 AI 提供稳定、可版本化的个人编码/审查/提交偏好，而非每次都重述上下文的场景；前提是接受其自定义 ::DNA 结构。
- 希望把项目约束、经验教训与进度检查点以纯文本文件随代码一起管理，并在团队内共享工作风格；推断需验证共享实践是否可行。
- 在 VS Code 或 Claude Code 等平台通过市场/扩展一键安装，想快速试用统一技能包的场景。

## 项目宣称的能力

- README“What this is”和“Schema at a glance”宣称用一次简短对话生成便携画像，核心保持在 500 token 以内，包含 CORE/CORE/FACT/PROJECT/LESSONS/PROGRESS/RUNTIME/DECAY 分层结构。
- README“Your imprint is yours”宣称画像为纯文本、可读可编辑可版本化、无厂商锁定，可跨 SKILL.md 兼容代理移植。
- README“What It Overlaps With”宣称单个文件覆盖记忆、压缩、入职、代码审查、调试、规划、进度跟踪、测试、Git 工作流、SEO 等 11 个能力域。
- README Changelog v2.3.0 宣称新增判断层，可按用户与项目差异决定执行/确认/建议/停止，并支持用户设定的硬边界；但未提供可验证实现。
- README 宣称 MIT 许可、有 Zenodo DOI、并提供 karpathy-mode 等预设模板，方便以模板为起点。

## 限制与待验证

- README 宣称的能力（跨代理行为一致性、判断层效果、11 个领域深度）均缺少可复现评测或基准，需查看实际 SKILL.md 内容与个人试用验证。
- 没有提供具体 token 计量证据，500 token 上限与 PROGRESS/LESSONS 增长后的实际开销需实测。
- README 多次提及 iLang 协议与向量空间、11 维判断等概念，但未给出该协议在本项目中的可验证实现细节，需查 iLang spec 与代码。
- interest 字段为空，无法判断实际用户反馈与采用程度，需查看 issues、star 变化与真实使用报告。
- 不同代理的安装路径与市场条目（VS Code Marketplace、Open VSX、Cursor Directory）真实可用性需逐一验证。
- 项目标注未归档，最近推送时间为 2026-09-22，是否持续维护需观察后续提交。

## 什么情况下重新考虑

- 当需要在多个 AI 编码代理间迁移并保持个人工作偏好一致时。
- 当希望把项目约束、经验教训与进度检查点纳入版本控制并共享给团队时。
- 当需要评估该技能的实际 token 开销与判断层在真实任务中的行为时。
- 当发现 SKILL.md 或 iLang 协议生态出现可验证的评测或第三方集成时。

## 检索关键词

- AI agent skill
- portable profile
- SKILL.md
- memory compression
- code review personalization
- iLang protocol
