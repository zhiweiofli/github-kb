---
status: "indexed"
source: "https://github.com/apache/maka"
repository: "apache/maka"
summary: "Apache Maka（孵化中）是一个本地优先的 agent 工作区，把每次运行的模型消息、工具调用、权限决策和终止都记录为只追加的 RuntimeEvent 日志，并以该日志作为运行、UI 与崩溃恢复的事实来源。"
topics: ["agent harness", "agent workspace", "runtime event log", "local-first agent", "agent evaluation", "Apache Incubator"]
assessment: "not-tested"
---

# apache/maka

- GitHub: https://github.com/apache/maka
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/8
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 02140941d57716a15ddbd3be6f55ed563fe84255；输入截断: False
- License: Apache-2.0

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

Apache Maka（孵化中）是一个本地优先的 agent 工作区，把每次运行的模型消息、工具调用、权限决策和终止都记录为只追加的 RuntimeEvent 日志，并以该日志作为运行、UI 与崩溃恢复的事实来源。

## 适用场景

- 需要本地保存会话、设置和运行记录，并自带模型（云 API、本地模型或兼容网关）的个人或团队 agent 使用场景（README「Your machine, your model」）。
- 想基于同一 Runtime Host 同时使用 Desktop、TUI 和 CLI 客户端的开发或测试（README「One Runtime Host」及「Terminal entry points」）。
- 需要在隔离 Git worktree 中运行图式多分支任务（--graph）的实验性工作流；README 明确要求源项目为干净 Git worktree（推断：需先满足该前提）。
- 需要对 agent 运行做可复现评测，使用仓库内 Eval 规格与适配器的场景（README「packages/eval」及 docs/eval）。

## 项目宣称的能力

- README 宣称以追加日志 RuntimeEvent 作为运行时：UI、下一轮提示和崩溃恢复均为该日志的投影（「The log is the runtime」）。
- README 宣称在相同模型和官方 verifier 下与其他 harness 对比，并随每次报告提供逐任务结果，位于 docs/eval（「Measured, not claimed」）。
- README 宣称会话、设置和运行记录保留在本地，模型由用户自带（「Your machine, your model」）。
- README 宣称 Desktop、TUI/CLI 与 Eval 是同一个执行权威 Runtime Host 的瘦客户端（「One Runtime Host」）。
- README 提供从源码构建的完整步骤、Node.js 与 ripgrep 等依赖，以及桌面/TUI/CLI 入口命令（「Build from source」「Terminal entry points」）。

## 限制与待验证

- 尚未发布 Apache release，当前只能从源码构建或使用开发测试版本；开发构建未获 Apache 批准（「Get Maka」「IMPORTANT」提示）。
- 项目处于 Apache 孵化阶段，README 明确数据格式、CLI 命令和实验能力仍可能变化（DISCLAIMER-WIP 与 IMPORTANT 提示）。
- Windows 与 Linux 平台标注为 preview，macOS 为正式支持；平台成熟度需进一步验证（README 平台徽章）。
- 本地凭证以明文文件 credential-vault.json 保存，仅依赖操作系统账户权限保护（「Local data and recovery」）。
- 升级不会导入旧 JSONL 记录和 Electron safeStorage 凭证，可能出现空线程并需重新输入凭证（「Local data and recovery」）。
- Direct Peer 与 Peer Mesh 开发需要 Rust stable 1.98+ 及平台链接器，增加构建与使用成本（「Build from source」）。
- README 的 benchmark 说法未在输入中给出具体数值，需查看 docs/eval 的逐任务报告核实。

## 什么情况下重新考虑

- 当项目发布首个 Apache release 并需要正式分发的签名源码包时。
- 当需要 Windows 或 Linux 正式支持而非 preview 时。
- 当需要评估其与其他 agent harness 的可复现逐任务 benchmark 结果时，可查看 docs/eval 更新。
- 当需要本地 agent 运行日志审计、恢复或持久化事件流能力时。
- 当需要稳定的数据格式、CLI 命令或实验能力 API 时，等 README 的「under active development」提示消除后再评估。

## 检索关键词

- agent harness
- agent workspace
- runtime event log
- local-first agent
- agent evaluation
- Apache Incubator
