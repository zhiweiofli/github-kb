---
status: "indexed"
source: "https://github.com/tw93/Waza"
repository: "tw93/Waza"
summary: "面向 AI 编码代理的一组通用工程习惯技能包，把思考、UI、审查、调试、写作、研究、阅读与代理健康检查固化为可安装的 skill 触发指令。"
topics: ["AI coding agent skills", "Claude Code skills", "Codex plugin", "agent workflow", "engineering habits", "prompt chaining"]
assessment: "not-tested"
---

# tw93/Waza

- GitHub: https://github.com/tw93/Waza
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/22
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 7eea2d9d5bce00baf3fbbee6dfc65ef741acc8ce；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

面向 AI 编码代理的一组通用工程习惯技能包，把思考、UI、审查、调试、写作、研究、阅读与代理健康检查固化为可安装的 skill 触发指令。

## 适用场景

- 在 Claude Code / Codex / Cursor 等支持 skill 目录的代理中安装，用斜杠命令触发固定的工程工作流（README 安装章节）
- 新功能开工前用 /think 做设计压测并产出可实施计划；合并前用 /check 审查 diff（README Skills 表）
- 遇到回归或异常行为时用 /hunt 要求先确认根因再修复（README Skills 表）
- 把 /read → /learn → /write 串成资料阅读、整理与润色的研究写作流程（README Chaining Skills 章节）
- 审计本机代理配置、项目指令与可维护性（README 所述 /health 技能，适用前提是已安装并可读取对应项目公开上下文）
- 需要为代理配置状态栏显示上下文窗口与配额用量（README Extras 章节）

## 项目宣称的能力

- README 宣称提供 8 个边界清晰的技能，每个只有一个职责和明确触发条件（Skills 表、Why 章节）
- 安装方式覆盖 npx skills、宿主插件市场、Claude Desktop ZIP 与 npm 包，并给出对应卸载方式（Install / Uninstall 章节）
- /check 在运行时读取目标仓库公开上下文（README、包清单、Makefile、CI 工作流）做项目感知审查，宣称不触碰私有路径、凭据或 token（Project Context 章节）
- README 宣称技能源自真实项目、经 300+ 会话与 7 个项目打磨，每条 gotcha 对应真实失败（Why 章节）
- 声明 MIT 许可，仓库未归档，且 README 明确支持自定义技能链式调用（License / Chaining Skills）

## 限制与待验证

- README 宣称的效果（如 UI 审美迭代、调试到根因、代理健康评分）均为自述，未提供可复现的 benchmark 或第三方评测，需自行在小项目验证
- /check 依赖读取目标仓库公开文件，对私有仓库或以非标准布局组织的项目可能失效或覆盖面不足，需实测
- 技能的实际可用性取决于宿主代理是否支持对应 skill 目录与斜杠命令，且不同代理（Codex、Cursor、Gemini CLI、Copilot、Amp、Kimi 等）行为差异需逐个验证
- README 提到部分能力依赖上游尚未暴露的字段（如 Codex 无 five-hour-used / weekly-used），说明存在上游限制导致的功能缺口
- 安装脚本通过 curl 管道执行 release 资产，README 也提示需先 review，存在供应链与信任成本
- 未提供性能、延迟、token 消耗、误触发率等量化数据，也未说明与同类技能集合（如 Superpowers、gstack，仅被 README 提及）的客观对比

## 什么情况下重新考虑

- 需要在团队内为多个 AI 编码代理统一工程流程与审查标准时
- 需要为新项目建立可复用的设计压测、调试根因与合并前审查清单时
- 需要审计已配置代理（Codex、Claude Code）的健康度与项目指令质量时
- 宿主代理新增 skill 机制或上游补齐配额字段，使状态栏与技能能力发生变化时

## 检索关键词

- AI coding agent skills
- Claude Code skills
- Codex plugin
- agent workflow
- engineering habits
- prompt chaining
