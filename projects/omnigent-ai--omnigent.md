---
status: "indexed"
source: "https://github.com/omnigent-ai/omnigent"
repository: "omnigent-ai/omnigent"
summary: "面向多种编码型 AI Agent 的统一编排层（meta-harness），在不重写 agent 的前提下切换/组合 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi 及自写 agent，并叠加策略、沙箱与多端实时协作。"
topics: ["AI agent 编排", "meta-harness", "Claude Code", "Codex", "Cursor", "agent 沙箱与策略治理"]
assessment: "not-tested"
---

# omnigent-ai/omnigent

- GitHub: https://github.com/omnigent-ai/omnigent
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/20
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: af2ac539f041fcb4dc201365da43130e05eede35；输入截断: False
- License: Apache-2.0

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

面向多种编码型 AI Agent 的统一编排层（meta-harness），在不重写 agent 的前提下切换/组合 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi 及自写 agent，并叠加策略、沙箱与多端实时协作。

## 适用场景

- 需要在同一会话内混用多个厂商的编码 agent（如 Claude Code + Codex），并让一个 agent 审查另一个 agent 产出——前提是接受 alpha 状态并按 README 要求装好 uv、git、Node 22+/pnpm、tmux 等工具链
- 团队多人协作同一 agent 会话：共享会话观看/对话、co-drive（消息在 owner 机器执行）、fork 对话独立续跑——前提是部署可被内网/公网访问的服务器，或仅在局域网访问本机 6767 端口
- 从手机/浏览器/桌面端接力同一会话（termimal→浏览器→手机状态同步）——前提是运行 omnigent 服务器并完成登录与 host 注册
- 对 agent 行为做治理：审批 shell/文件写入、限制工具调用次数、设置美元成本上限与阈值告警——前提是接受 README 描述的 policy 三级（server/agent/session）配置模型
- 在云沙箱或 K8s 中按会话隔离运行 agent，避免依赖个人电脑常开——前提是安装对应 sandbox extra（Modal、Daytona、E2B、Kubernetes 等）并接受其外部服务依赖
- 用简短 YAML 定义自写 agent（本地 Python 函数、MCP server、子 agent 委派）并通过 CLI 或 web UI 运行——前提是接受 alpha 阶段 API/YAML 规范可能变动

## 项目宣称的能力

- README 宣称提供跨 harness 的统一编排层，可切换或组合 Claude Code、Codex、Cursor、OpenCode、Hermes、Pi 与自写 YAML agent（Why Omnigent?、Write your own agent）
- README 宣称会话跨设备同步：终端、浏览器、手机、桌面 app 中消息/子 agent/终端/文件保持一致（Why Omnigent? 第一条、Quick start 第 2 步）
- README 宣称支持任意模型接入：厂商 API key、Claude Pro/Max 或 ChatGPT 订阅、OpenAI/Anthropic 兼容网关（OpenRouter、LiteLLM、Ollama、vLLM、Azure），以及 Databricks（第 3 步 Choose &amp; switch models 表格）
- README 宣称可协作：分享会话、co-drive（attach）、fork 会话，并支持邀请制多用户与 OIDC（Google/GitHub/Okta/Microsoft）单点登录（第 5 步 Collaborate）
- README 宣称以内置 policy 做治理：操作前审批、会话工具调用上限、美元成本硬上限与软阈值，且 server/agent/session 三级叠加（第 6 步 Govern your agents）
- README 宣称支持多类云沙箱按会话运行与 managed hosts（Modal、Daytona、Blaxel、E2B、Kubernetes、OpenShell、Databricks 等），另有 macOS seatbelt 与 Linux bwrap 本地隔离（Why Omnigent?、Toolchain and prerequisites）

## 限制与待验证

- README 自标 status: alpha，功能与接口稳定性未获证明，需查 release 记录与 CHANGELOG 判断
- LICENSE 字段显示 Apache-2.0，但未核验仓库实际 LICENSE 文件与依赖的许可证兼容性，需检查 LICENSE 与第三方依赖清单
- 安装与运行门槛高：需 Python 3.12+、uv、git、Node.js 22+/npm/pnpm；Linux 缺 bwrap 会导致 native harness 终端启动失败；Windows 为 degraded 模式，无 tmux/PTY 包装与文件系统/网络沙箱，需查各平台文档与 issue
- README 宣称 cloud sandbox、managed hosts、子 agent 并行 worktree、成本 policy 等能力，但无 benchmark、无稳定性/资源开销数据，需自行在目标规模下压测并查看 docs/POLICIES.md 与 harness test bench
- 默认开启匿名 telemetry，需按文档主动关闭；自托管多用户需自行保障服务器可达性与认证配置，安全性未获独立验证
- README 未给出并发上限、会话规模、成本精度、沙箱启动延迟等量化指标，均属 UNKNOWN，需查 issue、release notes 或自行实测
- 文档中提及的多个集成（Degvin、Kiro、Grok Build、OpenClaw、多种 sandbox 供应商）依赖外部 CLI 或服务，其可用性受第三方影响，需逐个验证

## 什么情况下重新考虑

- 需要把团队现有编码 agent 统一到单一编排/审批/成本控制面时
- 需要让非本机设备（手机、平板、浏览器）接力同一 agent 会话时
- 需要为 agent 引入合规级策略（操作审批、成本上限、工具白名单）时
- 需要在云沙箱或 K8s 中按会话隔离运行 agent 而不依赖常开笔记本时
- 需要在同一任务中让不同厂商的 agent 互相审查或分工时
- 项目脱离 alpha、出现稳定 API/版本承诺或明确生产案例时

## 检索关键词

- AI agent 编排
- meta-harness
- Claude Code
- Codex
- Cursor
- agent 沙箱与策略治理
