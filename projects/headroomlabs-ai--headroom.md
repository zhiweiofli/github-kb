---
status: "indexed"
source: "https://github.com/headroomlabs-ai/headroom"
repository: "headroomlabs-ai/headroom"
summary: "面向 AI agent 的本地上下文压缩层，在提示词送进 LLM 前压缩工具输出、日志、RAG 片段、文件与会话历史，并以库、代理或 MCP server 形式接入。"
topics: ["LLM context compression", "agent token optimization", "MCP server", "LLM proxy", "RAG chunk compression", "reversible compression CCR"]
assessment: "not-tested"
---

# headroomlabs-ai/headroom

- GitHub: https://github.com/headroomlabs-ai/headroom
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/2
- 评估日期: 2026-09-27
- 模型: deepseek-flash
- README blob: 912e426c8f483b07533798a4939441a030ff2ad2；输入截断: False
- License: Apache-2.0

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

面向 AI agent 的本地上下文压缩层，在提示词送进 LLM 前压缩工具输出、日志、RAG 片段、文件与会话历史，并以库、代理或 MCP server 形式接入。

## 适用场景

- 日常运行编码类 agent 且工具输出/日志/JSON 体量很大，希望通过代理或 wrap 在不改代码的前提下降低输入 token（推断，基于 README 的 Good fit 段）
- 跨 Claude、Codex、Gemini、Grok 等多个 agent 需要共享一份去重的记忆存储（README 宣称 Cross-agent memory）
- 需要可逆压缩，模型可在需要时通过 headroom_retrieve 取回原文（README 宣称 CCR，需验证 TTL 与检索行为）
- 把压缩接入自有 Python/TypeScript 应用，用 compress(messages) 或 withHeadroom 包装 Anthropic/OpenAI SDK（README 宣称 Integrations 表）
- 企业内网/离线环境下自托管代理做压缩，避免把内容发给第三方压缩 API（README 宣称本地运行、数据不外发；需验证遥测与模型下载路径）

## 项目宣称的能力

- README『Proof』给出四个场景的 token 节省表（SRE 调试 55,957→24,340，代码库探索 42%，GitHub issue 分诊 30%），并附可复现命令与固定 seed
- README 宣称压缩延迟低（10K JSON 约 0.21 ms p50，100K 约 1.4 ms），不影响 agent 延迟
- README『What it does / Agent compatibility』列出库、代理、agent wrap、MCP server 四种接入方式，覆盖 Claude Code、Codex、Cursor、Aider 等大量工具
- README 宣称按内容类型路由：SmartCrusher（JSON）、CodeCompressor（AST，多语言）、Kompress-v2-base（文本，HuggingFace 模型）
- README『CacheAligner / Live-zone compression』宣称只压缩新增字节、保持前缀逐字节不变以保住 provider KV-cache
- Apache-2.0 许可，仓库未 archived，README 与推送时间较新

## 限制与待验证

- 压缩收益高度依赖内容重复度：README『Proof』自述散文与已密集输出几乎不压缩，短对话收益很小；具体数字需用 headroom savings 在自有流量上验证
- README 宣称的准确率评测 N=100，自承 ±0.03 落在置信区间内，无法据此确认无质量损失；需检查评测方法学文档与更大样本
- 输出 token 节省为反事实估计（README 自述 estimated），虽有 holdout 机制但需自行配置验证
- 安装依赖较多：Python 3.10+、可选 ONNX Runtime（x86 需 AVX2）、Kompress 模型从 HuggingFace 下载、Intel macOS 无预编译 ONNX 需系统库；企业 SSL 检查环境有额外配置成本
- 遥测 beacon 默认开启（README『Telemetry』），需显式关闭；wrap 会安装并注册 Serena 到用户级配置，unwrap 前会影响其他项目
- README 未说明 CCR 本地缓存的原文件数量/大小上限、加密方式与 TTL 细节，需查 docs/ccr 与配置文档；压缩效果、兼容性与多 agent 行为均未在本环境实际运行验证

## 什么情况下重新考虑

- 当 agent 会话因工具输出/日志/JSON 撑爆上下文窗口，且需要在不改应用代码的前提下降低 token 成本时
- 当需要跨多个编码 agent 共享记忆或统一管理上下文时
- 当需要可逆压缩并希望模型能按需取回原文时
- 当组织需要在 VPC/内网自托管压缩代理并集中管理配置与用量统计时（README 的团队版为商业支持路径）

## 检索关键词

- LLM context compression
- agent token optimization
- MCP server
- LLM proxy
- RAG chunk compression
- reversible compression CCR
