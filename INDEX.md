# GitHub KB Index

> Repo 索引（从 CLAUDE.md 分离）。
> 约定：除非明确提升优先级，否则新收录 repo 的 Status 默认 `LATER`。

## Index

### [bili2text](https://github.com/lanbinleo/bili2text)
- GitHub: https://github.com/lanbinleo/bili2text
- Local: `github-kb/repos/bili2text`
- Category: content-pipeline / speech-to-text
- Status: LATER
- Why: B 站视频快速转写成文本资产，便于归档与二次加工。
- Notes: 下载视频→提取/分割音频→Whisper 转写。
- 最后讨论时间：2026年2月7日

### [wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter)
- GitHub: https://github.com/wechat-article/wechat-article-exporter
- Local: not cloned
- Category: content-pipeline / export
- Status: LATER
- Why: 批量导出公众号文章与数据（阅读量/评论），形成可离线保存的资料库。
- Notes: 支持在线站点使用；亦支持 Docker 私有化与 Cloudflare 部署；可导出 html/json/excel/txt/md/docx。
- 最后讨论时间：2026年2月7日

### [hacker-podcast](https://github.com/miantiao-me/hacker-podcast)
- GitHub: https://github.com/miantiao-me/hacker-podcast
- Local: not cloned
- Category: content-pipeline / summarization
- Status: LATER
- Why: 关注“信息→总结→音频分发”的自动化内容生产链路。
- Notes: 自动抓取 Hacker News 热门文章→AI 生成中文总结→转换为播客内容。
- 最后讨论时间：2026年2月7日

### [trendFinder](https://github.com/ericciarla/trendFinder)
- GitHub: https://github.com/ericciarla/trendFinder
- Local: not cloned
- Category: intel-trends
- Status: LATER
- Why: 获取上游趋势信号，为内容管线/选题提供输入。
- Notes: README 描述为聚合趋势话题的工具（“Stay on top of trending topics…”）。
- 最后讨论时间：2026年2月7日

---

### [serena](https://github.com/oraios/serena)
- GitHub: https://github.com/oraios/serena
- Local: `github-kb/repos/serena`
- Category: agent-framework / coding-agent
- Status: LATER
- Why: 把 LLM 变成可直接在代码库上工作的 agent，评估其工具化能力与可控性。
- Notes: Coding agent toolkit（对接代码库的执行/工具体系）。
- 最后讨论时间：2026年2月7日

### [superpowers](https://github.com/obra/superpowers)
- GitHub: https://github.com/obra/superpowers
- Local: `github-kb/repos/superpowers`
- Category: agent-framework / workflow
- Status: LATER
- Why: 关注“可组合 skills + 工作流”的 agent 开发范式。
- Notes: 面向 coding agents 的完整软件开发工作流。
- 最后讨论时间：2026年2月7日

### [SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- GitHub: https://github.com/SuperClaude-Org/SuperClaude_Framework
- Local: not cloned
- Category: agent-framework / instruction-injection
- Status: LATER
- Why: 研究“行为指令注入 + 组件编排”如何让 Claude Code 形成结构化开发平台。
- Notes: 提供多命令/多模式/集成的框架化配置与文档体系。
- 最后讨论时间：2026年2月7日

### [openskills](https://github.com/numman-ali/openskills)
- GitHub: https://github.com/numman-ali/openskills
- Local: not cloned
- Category: agent-framework / skills-loader
- Status: LATER
- Why: 关注 skills 的加载/分发/可复用机制，作为 agent 工具链的底座候选。
- Notes: Universal skills loader for AI coding agents。
- 最后讨论时间：2026年2月7日

### [vibe](https://github.com/lynaghk/vibe)
- GitHub: https://github.com/lynaghk/vibe
- Local: not cloned
- Category: sandboxing / agent-security
- Status: LATER
- Why: 想把 agent 执行环境隔离出主机，降低越权读取与环境污染风险。
- Notes: 在 macOS 上快速启动零配置 Linux VM，用于沙箱化/隔离 LLM agents。
- 最后讨论时间：2026年2月7日

---

### [NyRAG](https://github.com/vespaai-playground/NyRAG)
- GitHub: https://github.com/vespaai-playground/NyRAG
- Local: not cloned
- Category: rag-search
- Status: LATER
- Why: 关注从抓取/处理→索引→混合检索→Chat UI 的一体化 RAG 工具链。
- Notes: 支持爬网站或处理文档，并部署到 Vespa 做 hybrid search。
- 最后讨论时间：2026年2月7日

---

### [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)
- GitHub: https://github.com/zai-org/Open-AutoGLM
- Local: not cloned
- Category: device-agent
- Status: LATER
- Why: 关注手机端 agent（多模态理解屏幕 + 自动化执行）的可行性与安全机制。
- Notes: ADB/HDC 控制设备；支持敏感操作确认与人工接管。
- 最后讨论时间：2026年2月7日

### [ai-auto-touch](https://github.com/github653224/ai-auto-touch)
- GitHub: https://github.com/github653224/ai-auto-touch
- Local: not cloned
- Category: device-agent / android-automation
- Status: LATER
- Why: 关注“自然语言→多设备控制”的平台化落地。
- Notes: FastAPI + React；支持实时屏幕镜像（scrcpy）与批量设备管理。
- 最后讨论时间：2026年2月7日

### [Operit](https://github.com/AAswordman/Operit)
- GitHub: https://github.com/AAswordman/Operit
- Local: not cloned
- Category: device-agent / on-device
- Status: LATER
- Why: 关注端侧助手（工具调用/工作流/记忆）在 Android 上的产品形态。
- Notes: 强调设备端运行（除 API 调用），支持工具调用、深度搜索、工作流与定制。
- 最后讨论时间：2026年2月7日

---

### [Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3)
- GitHub: https://github.com/XiaoYouChR/Ghost-Downloader-3
- Local: not cloned
- Category: downloader-tools
- Status: LATER
- Why: 关注下载与资源整合工具（可能可接入内容管线的“获取层”）。
- Notes: AI-powered cross-platform multithreaded downloader；IDM 类智能分片等。
- 最后讨论时间：2026年2月7日

### [sure](https://github.com/we-promise/sure)
- GitHub: https://github.com/we-promise/sure
- Local: not cloned
- Category: product-app / personal-finance
- Status: LATER
- Why: 关注开源产品级应用（自托管、性能、协作维护）的工程实践。
- Notes: Maybe Finance 社区维护 fork；可用 Docker 自托管；AGPLv3。
- 最后讨论时间：2026年2月7日

### [omlx](https://github.com/jundot/omlx)
- GitHub: https://github.com/jundot/omlx
- Local: not cloned
- Category: llm-inference
- Status: LATER
- Why: 探索在 Apple Silicon 上提供连续批处理和冷热分层 KV Cache 的最佳本地推理服务架构。
- Notes: 支持从内存到 SSD 的 Tiered KV Cache，避免切换模型或者长上下文断开时的重算成本，对本地 coding workflow 帮助巨大。
- 最后讨论时间：2026年4月4日

### [claw-code](https://github.com/ultraworkers/claw-code)
- GitHub: https://github.com/ultraworkers/claw-code
- Local: not cloned
- Category: agent-framework / scoring-harness
- Status: LATER
- Why: 探索 Agent 基础脚手架（Harness）的高性能机制，了解通过 Rust 管理 MCP、插件系统与并发多会话的实现。
- Notes: 历史上最快达到 100K Stars 的开源项目，展示了从 TypeScript 到 Rust 移植的架构演进。
- 最后讨论时间：2026年4月4日

---

### [BetterDisplay](https://github.com/waydabber/BetterDisplay)
- GitHub: https://github.com/waydabber/BetterDisplay
- Local: `github-kb/repos/BetterDisplay`
- Category: macos-tools / display-management
- Status: LATER
- Why: macOS 显示器管理瑞士军刀，对多屏开发工作流有直接帮助。
- Notes: 支持自定义分辨率、XDR/HDR 亮度提升、虚拟屏幕、DDC 控制、PiP 窗口；闭源商业软件（Pro 付费）；支持 Homebrew 安装与 CLI 集成。
- 最后讨论时间：2026年4月4日

### [nann](https://github.com/alibaba/nann)
- GitHub: https://github.com/alibaba/nann
- Local: `github-kb/repos/nann`
- Category: ml-infra / nearest-neighbor-search
- Status: LATER
- Why: 阿里巴巴开源的大规模最近邻搜索框架，可作为向量检索/推荐系统底层引擎参考。
- Notes: 本地克隆不完整（仅 `.git` 目录无源码），需重新克隆后补充分析。来源：`https://github.com/alibaba/nann`。
- 最后讨论时间：2026年4月4日

### [openclaw](https://github.com/openclaw/openclaw)
- GitHub: https://github.com/openclaw/openclaw
- Local: `github-kb/repos/openclaw`
- Category: personal-ai / multi-channel-assistant
- Status: LATER
- Why: 自托管个人 AI 助手 + 多渠道消息网关，关注产品形态与集成能力。
- Notes: 支持 WhatsApp/Telegram/Slack/Discord/Signal/iMessage 等渠道统一接入；TypeScript（ESM），Node 22+；CLI `openclaw onboard` 一键部署；推荐 Anthropic Opus 模型；MIT 协议。
- 最后讨论时间：2026年4月4日

---

### [skills](https://github.com/anthropics/skills)
- GitHub: https://github.com/anthropics/skills
- Local: not cloned
- Category: claude-code-ecosystem / official-skills
- Status: LATER
- Why: Anthropic 官方 Agent Skills 仓库（113K★），定义了 Skills 标准规范与参考实现，是理解 Skill 设计模式的第一来源。
- Notes: 覆盖创意（art, music, design）、技术（web app testing, MCP server generation）、企业工作流（communications, branding）等领域。每个 Skill 独立文件夹 + SKILL.md。遵循 agentskills.io 规范。
- 最后讨论时间：2026年4月9日

### [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- GitHub: https://github.com/anthropics/claude-plugins-official
- Local: not cloned
- Category: claude-code-ecosystem / official-plugins
- Status: LATER
- Why: Anthropic 官方高质量 Plugin 目录（16K★），Plugin = Skills + Hooks + MCP Servers 的完整包。
- Notes: Plugin 是 Skills 的超集——可包含 hooks 脚本和 MCP server 配置。Marketplace 安装：`/plugin marketplace add`。
- 最后讨论时间：2026年4月9日

### [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)
- GitHub: https://github.com/anthropics/knowledge-work-plugins
- Local: not cloned
- Category: claude-code-ecosystem / knowledge-work
- Status: LATER
- Why: Anthropic 面向知识工作者的开源 Plugin 集（11K★），为 Claude Cowork 场景设计。
- Notes: 侧重非编程场景：文档写作、研究分析、沟通协作等。Python 为主。
- 最后讨论时间：2026年4月9日

### [obsidian-skills](https://github.com/kepano/obsidian-skills)
- GitHub: https://github.com/kepano/obsidian-skills
- Local: not cloned
- Category: claude-code-ecosystem / obsidian-integration
- Status: LATER
- Why: Obsidian 创始人 kepano 出品（21K★），教 Agent 理解 Obsidian 特有语法（wikilinks, Bases, JSON Canvas, CLI）。**与本 PKM 项目直接相关**。
- Notes: 包含 5 个 Skills：obsidian-markdown、obsidian-bases、json-canvas、obsidian-cli、defuddle（网页清洁提取）。遵循 agentskills.io 规范，兼容 Claude Code / Codex / OpenCode。
- 最后讨论时间：2026年4月9日

### [axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills)
- GitHub: https://github.com/axtonliu/axton-obsidian-visual-skills
- Local: not cloned
- Category: claude-code-ecosystem / visualization
- Status: LATER
- Why: 从文本生成 Canvas / Excalidraw / Mermaid 图表的 Skill 包（2.2K★），增强 Agent 可视化输出能力。
- Notes: 与本项目的 mermaid 图表输出需求直接互补。
- 最后讨论时间：2026年4月9日

### [smart-illustrator](https://github.com/axtonliu/smart-illustrator)
- GitHub: https://github.com/axtonliu/smart-illustrator
- Local: not cloned
- Category: claude-code-ecosystem / content-creation
- Status: LATER
- Why: AI 文章配图 Skill（435★），智能检测插图位置 + 封面学习系统。
- Notes: 使用 Gemini API 生成图片，支持 Mermaid 图表和 YouTube 缩略图。Claude Code Skill 形态。
- 最后讨论时间：2026年4月9日

### [erduo-skills](https://github.com/rookie-ricardo/erduo-skills)
- GitHub: https://github.com/rookie-ricardo/erduo-skills
- Local: not cloned
- Category: claude-code-ecosystem / community-skills
- Status: LATER
- Why: 社区 Skills 集合（764★），可参考其 Skill 设计模式。
- Notes: JavaScript 实现。
- 最后讨论时间：2026年4月9日

### [cc-excalidraw-skill](https://github.com/rnjn/cc-excalidraw-skill)
- GitHub: https://github.com/rnjn/cc-excalidraw-skill
- Local: not cloned
- Category: claude-code-ecosystem / visualization
- Status: LATER
- Why: Claude Code Excalidraw 绘图 Skill（68★），将文本描述转为 Excalidraw 图表。
- Notes: 轻量实现，可参考其 Skill 结构。
- 最后讨论时间：2026年4月9日

### [web-access](https://github.com/eze-is/web-access)
- GitHub: https://github.com/eze-is/web-access
- Local: not cloned
- Category: claude-code-ecosystem / web-capability
- Status: LATER
- Why: 给 Claude Code 装上完整联网能力的 Skill（4.3K★），三层通道调度 + 浏览器 CDP + 并行分治。**直接增强本项目的 Anti-Decay 语义验证能力**。
- Notes: 补齐 WebSearch/WebFetch 的不足：联网策略自动选择、CDP 直连用户 Chrome（携带登录态）、支持动态页面/交互操作/视频截帧、子 Agent 并行分治。含站点经验积累机制。
- 最后讨论时间：2026年4月9日

### [clawflows](https://github.com/nikilster/clawflows)
- GitHub: https://github.com/nikilster/clawflows
- Local: not cloned
- Category: claude-code-ecosystem / workflow-automation
- Status: LATER
- Why: 113 个预建 Agent 工作流（1.4K★），覆盖智能家居、日常事务、健康、财务等生活场景。展示了 Agent 从"编程工具"到"生活助手"的范式转变。
- Notes: 纯文本工作流定义，易创建/分享/版本化。支持定时触发（cron）。社区驱动。
- 最后讨论时间：2026年4月9日

---

### [OpenHarness](https://github.com/HKUDS/OpenHarness)
- GitHub: https://github.com/HKUDS/OpenHarness
- Local: not cloned
- Category: agent-harness / open-infrastructure
- Status: LATER
- Why: 港大开源 Agent Harness 基础设施（7.6K★），提供 tool-use、skills、memory、multi-agent coordination 的轻量化实现。
- Notes: Python ≥3.10 + React Ink TUI；43+ 内置工具；支持 CLAUDE.md 发现注入、上下文压缩、MEMORY.md 持久记忆；兼容 anthropics/skills & plugins；多 Agent 协调（Swarm）；MIT 协议。
- 最后讨论时间：2026年4月9日

### [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
- GitHub: https://github.com/shanraisshan/claude-code-best-practice
- Local: not cloned
- Category: agent-harness / best-practices-curation
- Status: LATER
- Why: 最全面的 Claude Code 最佳实践汇编（33K★），系统性梳理了 10+ 个顶级工作流框架的对比矩阵。
- Notes: 覆盖 Everything Claude Code、Superpowers、Spec Kit、gstack、GSD、BMAD-METHOD 等框架的 Skills/Agents/Commands 数量对比。含 Boris Cherny（Claude Code 创始人）的多期实践 Tips。Cross-Model Workflow（Claude + Codex 协作）。
- 最后讨论时间：2026年4月9日

### [pro-workflow](https://github.com/rohitg00/pro-workflow)
- GitHub: https://github.com/rohitg00/pro-workflow
- Local: not cloned
- Category: agent-harness / self-correcting-memory
- Status: LATER
- Why: 自纠错记忆系统（1.7K★），Claude Code 每次被纠正后持久化到 SQLite，跨会话复合学习。**直接启发本 PKM 的反馈记忆机制**。
- Notes: 24 Skills + 8 Agents + 21 Commands + 29 Hook 脚本。亮点：LLM Gates（AI 驱动的 commit 验证）、Permission Tuner、Compact Guard（上下文压缩保护）、Cost Tracker。SQLite + FTS5 全文搜索。
- 最后讨论时间：2026年4月9日

### [harness-engineering-from-cc-to-ai-coding](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding)
- GitHub: https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding
- Local: not cloned
- Category: agent-harness / educational-guide
- Status: LATER
- Why: 张汉东的 Harness 工程实践指南（860★），从 Claude Code 源码出发讲解 AI Coding 的 Harness 设计。
- Notes: 中文内容，与本项目关注点高度重合。
- 最后讨论时间：2026年4月9日

---

### [hermes-agent](https://github.com/NousResearch/hermes-agent)
- GitHub: https://github.com/NousResearch/hermes-agent
- Local: not cloned
- Category: agent-framework / full-stack-agent
- Status: LATER
- Why: Nous Research 出品的全栈 Agent 框架（36K★），OpenClaw 的精神继承者，支持从 OpenClaw 一键迁移。
- Notes: 自带 setup 向导；支持 memories、skills、API keys 迁移；Python 实现；完整文档站点。
- 最后讨论时间：2026年4月9日

### [GitNexus](https://github.com/abhigyanpatwari/GitNexus)
- GitHub: https://github.com/abhigyanpatwari/GitNexus
- Local: not cloned
- Category: code-intelligence / knowledge-graph
- Status: LATER
- Why: 代码库知识图谱引擎（25K★），将代码库索引为知识图谱（依赖、调用链、集群、执行流），通过 MCP 暴露给 Agent。**让小模型也能获得完整架构视野**。
- Notes: CLI + MCP 和 Web UI 两种模式；Tree-sitter 解析；LadybugDB 存储；支持 Claude Code hooks 自动增强。`npx gitnexus analyze` 一键索引。
- 最后讨论时间：2026年4月9日

### [DeepTutor](https://github.com/HKUDS/DeepTutor)
- GitHub: https://github.com/HKUDS/DeepTutor
- Local: not cloned
- Category: ai-education / personalized-learning
- Status: LATER
- Why: Agent-Native 个性化学习助手（13K★），多 Agent RAG 架构实现论文深度辅导。
- Notes: 港大出品；支持论文上传 + 交互式学习；多 Agent 系统（检索、分析、教学）；CLI 工具。
- 最后讨论时间：2026年4月9日

### [OpenCLI](https://github.com/jackwener/OpenCLI)
- GitHub: https://github.com/jackwener/OpenCLI
- Local: not cloned
- Category: dev-tools / universal-cli
- Status: LATER
- Why: 万物 CLI 化引擎（14K★），将网站/Electron App/本地工具统一转化为确定性 CLI 接口，专为 AI Agent 设计。
- Notes: 79+ 内置适配器（B站/知乎/小红书/Reddit/HN/Twitter 等）；CDP 浏览器自动化（复用登录态）；反检测内置；零 LLM 成本（运行时不消耗 token）。
- 最后讨论时间：2026年4月9日

### [pretext](https://github.com/chenglou/pretext)
- GitHub: https://github.com/chenglou/pretext
- Local: not cloned
- Category: dev-tools / text-rendering
- Status: LATER
- Why: chenglou 出品的高性能文本测量与排版引擎（41K★），TypeScript 实现。
- Notes: 快速、精确、全面的文本测量和布局库。与 Agent/PKM 关系较远，偏底层基础设施。
- 最后讨论时间：2026年4月9日

---

### [gallery](https://github.com/google-ai-edge/gallery)
- GitHub: https://github.com/google-ai-edge/gallery
- Local: not cloned
- Category: agent-harness / mobile-ai
- Status: LATER
- Why: 边缘设备 AI 用例集合，包含针对移动端的 Agent Skills，展示大模型在手机端本地化的执行能力与潜力，无需联网。
- Notes: Google AI Edge 出品。
- 最后讨论时间：2026年4月12日

### [FastCode](https://github.com/HKUDS/FastCode)
- GitHub: https://github.com/HKUDS/FastCode
- Local: not cloned
- Category: code-intelligence / efficient-indexing
- Status: LATER
- Why: 高效的代码理解框架，采用混合索引和多层图建模架构。对比传统 RAG 消耗 Token 更低，小模型可用。
- Notes: 启发点：可用来增强当前知识库或代理池的深层结构化索引查询能力。
- 最后讨论时间：2026年4月12日

### [paseo](https://github.com/getpaseo/paseo)
- GitHub: https://github.com/getpaseo/paseo
- Local: not cloned
- Category: agent-harness / remote-orchestration
- Status: LATER
- Why: 支持从手机或 CLI 远程调度协同编码代理（如 Claude Code、Codex）并原生支持语音控制。
- Notes: 将编程代理无缝延展至移动端场景的极佳范例。
- 最后讨论时间：2026年4月12日

### [gbrain](https://github.com/garrytan/gbrain)
- GitHub: https://github.com/garrytan/gbrain
- Local: not cloned
- Category: personal-knowledge-management / embedded-vector-db
- Status: LATER
- Why: Garry Tan 的基于 Markdown + 嵌入式 Postgres (PGLite) 的知识代理大脑。
- Notes: 这非常契合本项目“纯文本库”的形态，PGLite 零外部依赖部署非常具有复用价值。
- 最后讨论时间：2026年4月12日

### [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)
- GitHub: https://github.com/THU-MAIC/OpenMAIC
- Local: not cloned
- Category: ai-education / multi-agent
- Status: LATER
- Why: 清华出品的沉浸式多智能体交互课堂，基于 MetaGPT。
- Notes: 包含虚拟教师和 AI 同学。可探究其多角色协同在长程学习中对信息吸纳的帮助。
- 最后讨论时间：2026年4月12日

### [ClawX](https://github.com/ValueCell-ai/ClawX)
- GitHub: https://github.com/ValueCell-ai/ClawX
- Local: not cloned
- Category: agent-framework / gui-orchestration
- Status: LATER
- Why: 提供 OpenClaw 等 AI Agent 的图形界面桌面版，让命令行式调度变成更直观且友好的桌面体验。
- Notes: CLI-to-GUI 交互进阶范式参考。
- 最后讨论时间：2026年4月12日

### [long-running-coding-loop](https://github.com/zalan159/long-running-coding-loop)
- GitHub: https://github.com/zalan159/long-running-coding-loop
- Local: not cloned
- Category: agent-framework / autonomous-loop
- Status: LATER
- Why: 长时效的自治编码循环框架：实现 -> 测试 -> 修复。
- Notes: 虽然实现简单，但展示了自动化工作中极重要的 Auto-Fix 回环机制设计。
- 最后讨论时间：2026年4月12日

### [AionUi](https://github.com/iOfficeAI/AionUi)
- GitHub: https://github.com/iOfficeAI/AionUi
- Local: not cloned
- Category: agent-harness / unified-gui
- Status: LATER
- Why: 提供针对多个底层基座（如 Claude Code, Codex, Goose 等）的统一桌面级交互界面。
- Notes: 将分散的代理和工具集成在了一个协同工作的应用入口内。
- 最后讨论时间：2026年4月12日

### [social-analyzer](https://github.com/qeeqbox/social-analyzer)
- GitHub: https://github.com/qeeqbox/social-analyzer
- Local: not cloned
- Category: dev-tools / osint
- Status: LATER
- Why: 面向 1000 多种社交平台的自动化分析和指纹收集工具 (OSINT)。
- Notes: 工具集极广，后期或可封装为 Agent 暴露用于做社交图谱知识挖掘。
- 最后讨论时间：2026年4月12日

---

### [khazix-skills](https://github.com/KKKKhazix/khazix-skills)
- GitHub: https://github.com/KKKKhazix/khazix-skills
- Local: not cloned
- Category: agent-framework / skills-ecosystem
- Status: LATER
- Why: 数字生命卡兹克开源的个人 AI Skills 合集，包含「横纵分析法」深度研究 Skill 与「khazix-writer」长文写作 Skill，是验证「个人方法论 → Agent Skills」落地范式的高质量样本。
- Notes: 遵循 Agent Skills (agentskills.io) 开放标准；同时提供 Prompts（轻量复用）+ Skills（重量结构化）双层资产；支持 Claude Code / OpenClaw / Codex。4.6K★。
- 最后讨论时间：2026年4月16日

### [voicebox](https://github.com/jamiepine/voicebox)
- GitHub: https://github.com/jamiepine/voicebox
- Local: not cloned
- Category: content-pipeline / tts-voice-cloning
- Status: LATER
- Why: 本地优先的开源声音克隆/合成工作室，是 ElevenLabs 的离线替代，可嵌入内容资产管线承担「文本 → 配音」一段。
- Notes: Tauri (Rust) 原生桌面应用；内置 5 个 TTS 引擎（Qwen3-TTS / LuxTTS / Chatterbox Multilingual/Turbo / HumeAI TADA），23 语言；支持 REST API、多轨时间线编辑、paralinguistic tags。18K★。
- 最后讨论时间：2026年4月16日

### [youtube-to-notebooklm](https://github.com/azuma520/youtube-to-notebooklm)
- GitHub: https://github.com/azuma520/youtube-to-notebooklm
- Local: not cloned
- Category: content-pipeline / research-workflow
- Status: LATER
- Why: 把 YouTube 搜索、字幕抓取、NotebookLM 生成（播客/摘要/脑图/测验）串成自然语言驱动的终端 Skills 流水线，是「Agent Skills 组合解决真实研究任务」的参照实现。
- Notes: 三个 Skills（yt-search / anything-to-notebooklm / whisper-transcribe）分别封装 yt-dlp / notebooklm-py / faster-whisper；一行自然语言触发多步链路；支持 Claude Code / Cursor / Windsurf。
- 最后讨论时间：2026年4月16日

### [GEOFlow](https://github.com/yaojingang/GEOFlow)
- GitHub: https://github.com/yaojingang/GEOFlow
- Local: not cloned
- Category: content-pipeline / content-ops
- Status: LATER
- Why: 面向 GEO/SEO 场景的开源内容生产系统，把模型配置、素材库、任务调度、审核、发布打通成完整后台——对研究「AI 内容 → 分发」链路工程化有直接参考价值。
- Notes: PHP + PostgreSQL + Docker Compose；含任务队列/Worker、草稿审核/发布工作流、SEO 结构化数据、OpenAI 风格接口适配。Apache 2.0。
- 最后讨论时间：2026年4月16日

### [markitdown](https://github.com/microsoft/markitdown)
- GitHub: https://github.com/microsoft/markitdown
- Local: not cloned
- Category: content-pipeline / doc-to-md
- Status: LATER
- Why: 微软官方的「任何文件 → Markdown」工具，是内容摄取管线 (wiki/0_Raw/) 中 PDF/Office/图片/音频/HTML 归一化的工业级默认选择。
- Notes: 支持 PDF / PPT / Word / Excel / 图片（EXIF+OCR）/ 音频（ASR）/ HTML / CSV / JSON / ZIP / YouTube URL / EPub；提供 CLI、Python API、MCP server。109K★。AutoGen 团队出品。
- 最后讨论时间：2026年4月16日

---

## 2026-05-17 截图 feeder 批量导入

> 来源：GitHub 截屏 feeder 旧批次。原 `wiki/0_Raw/archive/AI工程/github项目工具/` source-card 目录已按新规则删除；GitHub URL + MEMORY 聚类是长期记录。Status 默认 `LATER`，作为工程 feeder 进入后续概念聚类。

### [AIDC-AI-Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video)
- GitHub: https://github.com/AIDC-AI/Pixelle-Video
- Local: not cloned
- Category: content-pipeline / media-generation
- Status: LATER
- Why: 一个开源的AI全自动短视频引擎，通过自动化脚本与AI能力实现短视频的一键生成，降低视频创作门槛并提升生产效率。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/AIDC-AI/Pixelle-Video
- 最后讨论时间：2026年5月17日

### [Ariestar-sivtr](https://github.com/Ariestar/sivtr)
- GitHub: https://github.com/Ariestar/sivtr
- Local: not cloned
- Category: agent-runtime / terminal-output-management
- Status: LATER
- Why: sivtr是一个AI时代的终端输出工作区工具，可将嘈杂的终端流转换为可复用的文本资产，帮助开发者在不同shell、构建日志、AI代理回复和Codex会话中捕获、筛选、浏览、搜索、选择和重用终端输出。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/Ariestar/sivtr
- 最后讨论时间：2026年5月17日

### [DeusData-codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
- GitHub: https://github.com/DeusData/codebase-memory-mcp
- Local: not cloned
- Category: code-intelligence / knowledge-retrieval
- Status: LATER
- Why: 基于MCP协议的代码库记忆与语义检索工具，通过建立结构化索引实现对155种编程语言代码库的亚毫秒级上下文查询，核心解决AI编码助手在处理大型多语言项目时的检索延迟与上下文缺失问题。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/DeusData/codebase-memory-mcp
- 最后讨论时间：2026年5月17日

### [InsForge-InsForge](https://github.com/InsForge/InsForge)
- GitHub: https://github.com/InsForge/InsForge
- Local: not cloned
- Category: ai-app-infra / backend-platform
- Status: LATER
- Why: InsForge是一个基于Postgres的开源后端平台，为AI原生应用构建者提供集成认证、存储、计算、托管和AI网关的一体化后端服务，专为编码智能体和AI应用开发而设计。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/InsForge/InsForge
- 最后讨论时间：2026年5月17日

### [NawfalMotii79-PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)
- GitHub: https://github.com/NawfalMotii79/PLFM_RADAR
- Local: not cloned
- Category: open-hardware / radar-system
- Status: LATER
- Why: 一个开源PLFM雷达硬件项目的GitHub仓库，提供从项目文档、功能框图、电源管理到原理图、PCB布局及机械结构的完整工程设计文件，支持雷达系统的开源协作开发与硬件制造。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/NawfalMotii79/PLFM_RADAR
- 最后讨论时间：2026年5月17日

### [Panniantong-Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- GitHub: https://github.com/Panniantong/Agent-Reach
- Local: not cloned
- Category: web-automation / social-web-access
- Status: LATER
- Why: 给 AI Agent 装上社交 Web 访问层，可读取和搜索 X、Reddit、YouTube 等平台内容。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/Panniantong/Agent-Reach
- 最后讨论时间：2026年5月17日

### [tonyantony300-alt-sendme](https://github.com/tonyantony300/alt-sendme)
- GitHub: https://github.com/tonyantony300/alt-sendme
- Local: not cloned
- Category: product-app / file-transfer
- Status: LATER
- Why: AltSendme 是开源文件传输工具，关注低配置成本的个人/团队文件传输体验，可作为本地优先工具封装案例。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/tonyantony300/alt-sendme
- 最后讨论时间：2026年5月17日

### [braedonsaunders-codeflow](https://github.com/braedonsaunders/codeflow)
- GitHub: https://github.com/braedonsaunders/codeflow
- Local: not cloned
- Category: code-intelligence / architecture-visualization
- Status: LATER
- Why: CodeFlow是一款GitHub开源工具，可一键可视化项目代码架构与依赖关系，支持代码健康评分、本地离线分析、密钥扫描及多格式导出，帮助开发者快速梳理项目结构。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/braedonsaunders/codeflow
- 最后讨论时间：2026年5月17日

### [D4Vinci-Scrapling](https://github.com/D4Vinci/Scrapling)
- GitHub: https://github.com/D4Vinci/Scrapling
- Local: not cloned
- Category: web-automation / scraping
- Status: LATER
- Why: Scrapling 是轻量级 Python 爬虫库，定位于简化网页数据抓取任务，可作为 Agent Web 采集层的候选工具。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/D4Vinci/Scrapling
- 最后讨论时间：2026年5月17日

### [Fincept-Corporation-FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)
- GitHub: https://github.com/Fincept-Corporation/FinceptTerminal
- Local: not cloned
- Category: finance-tools / research-terminal
- Status: LATER
- Why: FinceptTerminal 是开源 Bloomberg-like 金融终端，可作为投资研究与金融数据产品形态的参考。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/Fincept-Corporation/FinceptTerminal
- 最后讨论时间：2026年5月17日

### [GitHub-Skills](https://github.com/skills)
- GitHub: https://github.com/skills
- Local: not cloned
- Category: developer-education / github-workflow
- Status: LATER
- Why: GitHub官方提供的交互式技能学习课程平台
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/skills
- 最后讨论时间：2026年5月17日

### [MeiGen-AI-InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk)
- GitHub: https://github.com/MeiGen-AI/InfiniteTalk
- Local: not cloned
- Category: content-pipeline / media-generation
- Status: LATER
- Why: InfiniteTalk 是 MeiGen-AI 维护的开源 AI 视频项目，关注长时长/无限时长视频生成，可补充多模态内容生产链路。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/MeiGen-AI/InfiniteTalk
- 最后讨论时间：2026年5月17日

### [OpenHub-Store-Github-Store](https://github.com/OpenHub-Store/Github-Store)
- GitHub: https://github.com/OpenHub-Store/Github-Store
- Local: not cloned
- Category: dev-tools / github-client
- Status: LATER
- Why: GitHub-Store 是围绕 GitHub 用户与项目信息展示的开源工具，可作为 GitHub 生态信息可视化/客户端产品参考。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/OpenHub-Store/Github-Store
- 最后讨论时间：2026年5月17日

### [HKUDS-OpenSpace](https://github.com/HKUDS/OpenSpace)
- GitHub: https://github.com/HKUDS/OpenSpace
- Local: not cloned
- Category: agent-framework / tooling
- Status: LATER
- Why: OpenSpace是一个GitHub开源项目，支持一键进化Claude Code、Codex、Cursor等多种AI代理。它通过自我进化与代理间经验共享机制，在降低46%代币消耗的同时提升AI智能。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/HKUDS/OpenSpace
- 最后讨论时间：2026年5月17日

### [pydantic-pydantic-ai](https://github.com/pydantic/pydantic-ai)
- GitHub: https://github.com/pydantic/pydantic-ai
- Local: not cloned
- Category: agent-framework / typed-agent-workflow
- Status: LATER
- Why: 这是一套基于PydanticAI Agent的自动化内容工作流系统架构，涵盖从RSS/网页/GitHub采集、AI生成与汇总、质量检查到飞书/邮件/Webhook多通道投递的完整链路，并支持CLI、FastAPI Web及独立调度进程多种入口。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/pydantic/pydantic-ai
- 最后讨论时间：2026年5月17日

### [thunderbird-thunderbolt](https://github.com/thunderbird/thunderbolt)
- GitHub: https://github.com/thunderbird/thunderbolt
- Local: not cloned
- Category: product-app / data-sovereignty
- Status: LATER
- Why: Thunderbolt 主打打破厂商数据锁定、让用户数据回归自己，可作为个人数据主权与迁移工具产品参考。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/thunderbird/thunderbolt
- 最后讨论时间：2026年5月17日

### [VoltAgent-awesome-design](https://github.com/VoltAgent/awesome-design)
- GitHub: https://github.com/VoltAgent/awesome-design
- Local: not cloned
- Category: design-resources / ui-system
- Status: LATER
- Why: VoltAgent/awesome-design 是设计资源仓库，包含天枢设计系统相关内容，可为 AI 生成 UI/UX 与设计规范沉淀提供参考素材。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/VoltAgent/awesome-design
- 最后讨论时间：2026年5月17日

### [addyosmani-agent-skills](https://github.com/addyosmani/agent-skills)
- GitHub: https://github.com/addyosmani/agent-skills
- Local: not cloned
- Category: agent-skills / ecosystem
- Status: LATER
- Why: agent-skills 是面向 AI Agent 的 Skills 资源库，关注可复用能力单元如何组织、发布与复用。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/addyosmani/agent-skills
- 最后讨论时间：2026年5月17日

### [code-yeongyu-oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
- GitHub: https://github.com/code-yeongyu/oh-my-opencode
- Local: not cloned
- Category: agent-framework / async-subagent
- Status: LATER
- Why: oh-my-opencode 是 OpenCode 插件，支持类似 Claude Code 的异步子代理（Async Subagent）模式，适合观察 coding agent 并行执行范式。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/code-yeongyu/oh-my-opencode
- 最后讨论时间：2026年5月17日

### [ei9987-blind_watermark](https://github.com/ei9987/blind_watermark)
- GitHub: https://github.com/ei9987/blind_watermark
- Local: not cloned
- Category: content-security / watermarking
- Status: LATER
- Why: 图片盲水印工具，能够在无需原图的情况下提取水印，可用于内容溯源、版权保护与生成内容治理场景。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/ei9987/blind_watermark
- 最后讨论时间：2026年5月17日

### [guofei9987-blind_watermark](https://github.com/guofei9987/blind_watermark)
- GitHub: https://github.com/guofei9987/blind_watermark
- Local: not cloned
- Category: content-security / watermarking
- Status: LATER
- Why: Python实现的图片盲水印添加与提取工具
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/guofei9987/blind_watermark
- 最后讨论时间：2026年5月17日

### [khoj-ai-khoj](https://github.com/khoj-ai/khoj)
- GitHub: https://github.com/khoj-ai/khoj
- Local: not cloned
- Category: personal-knowledge-management / ai-assistant
- Status: LATER
- Why: Khoj 是开源 AI 个人助手，支持本地文档搜索与自托管智能对话，可作为个人知识库智能入口参考。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/khoj-ai/khoj
- 最后讨论时间：2026年5月17日

### [lakr233-vphone-cli](https://github.com/lakr233/vphone-cli)
- GitHub: https://github.com/lakr233/vphone-cli
- Local: not cloned
- Category: device-agent / virtual-phone-cli
- Status: LATER
- Why: vphone-cli 是命令行虚拟手机工具项目，可作为移动端 Agent、设备自动化与隔离测试环境的候选基础设施。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/lakr233/vphone-cli
- 最后讨论时间：2026年5月17日

### [lightpanda-io-browser](https://github.com/lightpanda-io/browser)
- GitHub: https://github.com/lightpanda-io/browser
- Local: not cloned
- Category: web-automation / lightweight-browser
- Status: LATER
- Why: Lightpanda 是轻量浏览器项目，兼容 Puppeteer、Playwright 和 CDP 协议，可降低 Agent 浏览器自动化的运行成本。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/lightpanda-io/browser
- 最后讨论时间：2026年5月17日

### [microsoft-playwright-cli](https://github.com/microsoft/playwright-cli)
- GitHub: https://github.com/microsoft/playwright-cli
- Local: not cloned
- Category: web-automation / cli
- Status: LATER
- Why: Microsoft Playwright CLI 是浏览器自动化测试命令行工具，可作为 Agent Web 交互验证与脚本化浏览器控制入口。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/microsoft/playwright-cli
- 最后讨论时间：2026年5月17日

### [mihonapp-mihon](https://github.com/mihonapp/mihon)
- GitHub: https://github.com/mihonapp/mihon
- Local: not cloned
- Category: product-app / reader
- Status: LATER
- Why: Mihon 是开源漫画阅读器，支持多源插件与离线阅读，可作为内容消费类开源产品和插件生态案例。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/mihonapp/mihon
- 最后讨论时间：2026年5月17日

### [neutree-ai-openapi-to-skills](https://github.com/neutree-ai/openapi-to-skills)
- GitHub: https://github.com/neutree-ai/openapi-to-skills
- Local: not cloned
- Category: agent-skills / api-to-skill
- Status: LATER
- Why: GitHub项目openapi-to-skills支持将OpenAPI规范自动转换为LLM可用的Skills，旨在解决大语言模型理解并高效调用现有API与软件系统交互的难点。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/neutree-ai/openapi-to-skills
- 最后讨论时间：2026年5月17日

### [rasbt-LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)
- GitHub: https://github.com/rasbt/LLMs-from-scratch
- Local: not cloned
- Category: llm-education / fundamentals
- Status: LATER
- Why: 《Build a Large Language Model (From Scratch)》配套开源仓库，包含从零构建、预训练和微调大语言模型的代码，适合补齐 LLM 底层机制理解。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/rasbt/LLMs-from-scratch
- 最后讨论时间：2026年5月17日

### [slavingia-skills](https://github.com/slavingia/skills)
- GitHub: https://github.com/slavingia/skills
- Local: not cloned
- Category: agent-skills / ecosystem
- Status: LATER
- Why: slavingia/skills 是基于 Sahil Lavingia《极简主义企业家》方法论的 Claude Code 技能插件仓库，可作为个人方法论 Skill 化样本。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/slavingia/skills
- 最后讨论时间：2026年5月17日

### [steel-dev-steel](https://github.com/steel-dev/steel)
- GitHub: https://github.com/steel-dev/steel
- Local: not cloned
- Category: web-automation / cloud-browser
- Status: LATER
- Why: Steel.dev 是面向 AI 爬虫/Agent 的云端浏览器工具库，用云浏览器缓解本地 Headless Chrome/Puppeteer 的封禁、资源占用与稳定性问题。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/steel-dev/steel
- 最后讨论时间：2026年5月17日

### [theaiautomators-claude-code-agentic-rag-series](https://github.com/theaiautomators/claude-code-agentic-rag-series)
- GitHub: https://github.com/theaiautomators/claude-code-agentic-rag-series
- Local: not cloned
- Category: code-intelligence / agentic-rag-tutorial
- Status: LATER
- Why: Claude Code 与 Agentic RAG 系列教程仓库，适合沉淀 coding agent 的检索增强开发范式。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/theaiautomators/claude-code-agentic-rag-series
- 最后讨论时间：2026年5月17日

### [nextlevelbuilder-ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- GitHub: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Local: not cloned
- Category: agent-skills / ui-ux-workflow
- Status: LATER
- Why: ui-ux-pro-max-skill 是 AI UI/UX Skill 项目，旨在提供设计智能以构建专业多平台应用，包含 agent/workflows 工作流。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- 最后讨论时间：2026年5月17日

### [vndee-llm-sandbox](https://github.com/vndee/llm-sandbox)
- GitHub: https://github.com/vndee/llm-sandbox
- Local: not cloned
- Category: agent-security / sandboxing
- Status: LATER
- Why: LLM Sandbox 是用于安全隔离执行大语言模型生成代码的轻量级 Python 沙箱工具，是 Agent 执行边界的重要候选组件。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/vndee/llm-sandbox
- 最后讨论时间：2026年5月17日

### [x1xh1ol-system-prompts-and-models-of-ai-tools](https://github.com/x1xh1ol/system-prompts-and-models-of-ai-tools)
- GitHub: https://github.com/x1xh1ol/system-prompts-and-models-of-ai-tools
- Local: not cloned
- Category: prompt-intelligence / ai-tool-system-prompts
- Status: LATER
- Why: 汇集 Cursor、Devin、Claude Code、Manus 等 AI 工具的系统提示词与模型信息，可用于研究 Agent 产品的行为约束与提示结构。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/x1xh1ol/system-prompts-and-models-of-ai-tools
- 最后讨论时间：2026年5月17日

### [jamiepine-voicebox](https://github.com/jamiepine/voicebox)
- GitHub: https://github.com/jamiepine/voicebox
- Local: not cloned
- Category: content-pipeline / media-generation
- Status: LATER
- Why: 一个开源的AI语音工作室，支持在本地机器上克隆任何声音、生成语音并提供完整的语音输入输出栈，无需联网即可实现语音合成与口述。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/jamiepine/voicebox
- 最后讨论时间：2026年5月17日

### [mattpocock-skills](https://github.com/mattpocock/skills)
- GitHub: https://github.com/mattpocock/skills
- Local: not cloned
- Category: agent-skills / ecosystem
- Status: LATER
- Why: 一个提供结构化AI技能配置的GitHub仓库，旨在通过工程最佳实践引导Claude等AI助手生成更规范、可靠的代码，解决AI瞎写代码的问题。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/mattpocock/skills
- 最后讨论时间：2026年5月17日

### [safishamsi-graphify](https://github.com/safishamsi/graphify)
- GitHub: https://github.com/safishamsi/graphify
- Local: not cloned
- Category: code-intelligence / knowledge-retrieval
- Status: LATER
- Why: 一个用于处理大型图数据并支持 HTML 可视化与多语言扩展的开源项目。
- Notes: 来源: GitHub 截屏 feeder（原 source-card 目录已按规则删除）；URL: https://github.com/safishamsi/graphify
- 最后讨论时间：2026年5月17日

### [chenhg5-cc-connect](https://github.com/chenhg5/cc-connect)
- GitHub: https://github.com/chenhg5/cc-connect
- Local: not cloned
- Category: agent-communication / claude-code-bridge
- Status: LATER
- Why: cc-connect 是 Claude Code 与 IM/外部消息系统的桥接工具线索，适合纳入 Agent 远程协作、移动端遥控和消息入口体系候选池。
- Notes: 来源: GitHub 截屏 feeder；canonical URL 已从截图笔记识别；后续由 github-kb-indexer/调研补齐 README、功能边界、安装方式和适配渠道。
- 最后讨论时间：2026年5月30日

---

## 2026-05-31 批量导入

### [hunk](https://github.com/modem-dev/hunk)
- GitHub: https://github.com/modem-dev/hunk
- Local: not cloned
- Category: dev-tools / code-review-tui
- Status: LATER
- Why: 专为 agentic coder 设计的终端 diff 查看器，"review-first" 理念与 Agent 工作流深度契合，可补齐 Agent 提交前 diff 审查环节。
- Notes: TypeScript；CLI + TUI；4.5K★；Git diff 可视化 + code review 体验。
- 最后讨论时间：2026年5月31日

### [awesome-generative-ui](https://github.com/narrowin/awesome-generative-ui)
- GitHub: https://github.com/narrowin/awesome-generative-ui
- Local: not cloned
- Category: design-resources / generative-ui
- Status: LATER
- Why: LLM 动态生成/组合/渲染 UI 组件的资源精选列表，研究 Generative UI 趋势的一手信号源。
- Notes: 38★；无主编程语言（纯文档）；覆盖前端+生成式 AI+UI 设计实验。
- 最后讨论时间：2026年5月31日

### [gelab-zero](https://github.com/stepfun-ai/gelab-zero)
- GitHub: https://github.com/stepfun-ai/gelab-zero
- Local: not cloned
- Category: device-agent / gui-agent
- Status: LATER
- Why: 阶跃星辰 GELab 出品的 GUI Agent 旗舰方案（2.2K★），定位"银河系最强 GUI Agent"，支持 phone use agent，是端侧 GUI 自动化的产业级参照。
- Notes: Python；包含 PUA（Phone Use Agent）能力；2.2K★。
- 最后讨论时间：2026年5月31日

### [MiroThinker](https://github.com/MiroMindAI/MiroThinker)
- GitHub: https://github.com/MiroMindAI/MiroThinker
- Local: not cloned
- Category: agent-framework / deep-research
- Status: LATER
- Why: 深度研究 Agent，在 BrowseComp/BrowseComp-Zh 上达到 74.0/75.3 SOTA（8.2K★），是 web 搜索增强研究 Agent 的顶级开源参照。
- Notes: Python；支持 GAIA / HLE / xBench 多项评测；MiroThinker-1.7 最新模型；topics 包含 browsecomp、deep-research、search-agent。
- 最后讨论时间：2026年5月31日

### [supercheck](https://github.com/supercheck-io/supercheck)
- GitHub: https://github.com/supercheck-io/supercheck
- Local: not cloned
- Category: dev-tools / testing-monitoring
- Status: LATER
- Why: 开源测试 + 监控 + 可靠性平台（"as Code"），可作为 Agent 工作流持续验证层的候选基础设施。
- Notes: TypeScript；Playwright + k6 + HTTP 监控 + Status Page；203★；CI/CD 集成。
- 最后讨论时间：2026年5月31日

### [claude-container](https://github.com/nezhar/claude-container)
- GitHub: https://github.com/nezhar/claude-container
- Local: not cloned
- Category: agent-harness / containerization
- Status: LATER
- Why: 预装 Claude Code 的 Docker 容器，降低 Claude Code 沙箱化部署门槛，可参考其容器配置方案。
- Notes: Shell；164★；开发已迁移至 VibePod；适合研究 Claude Code 容器化最小配置。
- 最后讨论时间：2026年5月31日

### [ouroboros](https://github.com/Q00/ouroboros)
- GitHub: https://github.com/Q00/ouroboros
- Local: not cloned
- Category: agent-framework / agent-os
- Status: LATER
- Why: "Agent OS: Stop prompting. Start specifying."——定位从提示词转向规范驱动的 Agent 操作系统，4.4K★，是 Spec-first Agent 范式的代表项目。
- Notes: Python；MCP 支持；topics 包含 agent-os、ai-agent、mcp；4.4K★。
- 最后讨论时间：2026年5月31日

### [remotion](https://github.com/remotion-dev/remotion)
- GitHub: https://github.com/remotion-dev/remotion
- Local: not cloned
- Category: content-pipeline / programmatic-video
- Status: LATER
- Why: 用 React + 代码驱动视频生成（48.5K★），是 AI 内容资产管线中"程序化视频渲染"环节的工业级方案，可与 LLM 生成脚本协同。
- Notes: TypeScript；React 驱动；48.5K★；支持云端渲染；与 AI 脚本生成 + 自动化发布流结合潜力大。
- 最后讨论时间：2026年5月31日

### [Mano-P](https://github.com/Mininglamp-AI/Mano-P)
- GitHub: https://github.com/Mininglamp-AI/Mano-P
- Local: not cloned
- Category: device-agent / gui-vla
- Status: LATER
- Why: OSWorld 专项榜 #1（58.2%）的开源 GUI-VLA Agent，可在 Apple M4 Mac 本地运行，纯视觉驱动桌面自动化，数据完全不出设备（2.2K★）。
- Notes: 无主语言（多模态模型驱动）；支持 Mac mini/MacBook 本地推理；topics 包含 computer-use-agents、gui-automation、on-device-ai、osworld。
- 最后讨论时间：2026年5月31日

### [mano-afk](https://github.com/Mininglamp-AI/mano-afk)
- GitHub: https://github.com/Mininglamp-AI/mano-afk
- Local: not cloned
- Category: agent-framework / autonomous-builder
- Status: LATER
- Why: 全自主全栈应用构建 Agent：自然语言 → 开发 → 测试（GUI 测试 by mano-cua）→ bug 修复 → 部署，多 Agent 架构 + 对抗 code review，关注"AFK 自治开发"范式。
- Notes: Python；10★（早期项目）；含 adversary code review 机制；每个项目后会进化。
- 最后讨论时间：2026年5月31日

### [mempalace](https://github.com/MemPalace/mempalace)
- GitHub: https://github.com/MemPalace/mempalace
- Local: not cloned
- Category: agent-framework / memory-system
- Status: LATER
- Why: 基准测试排名最高的开源 AI 记忆系统（53K★），免费，MCP 支持，ChromaDB 向量存储，是 Agent 持久化记忆模块的顶级候选。
- Notes: Python；ChromaDB + MCP；53K★；与本 PKM 的 MEMORY.md 机制高度相关。
- 最后讨论时间：2026年5月31日

### [financial-services](https://github.com/anthropics/financial-services)
- GitHub: https://github.com/anthropics/financial-services
- Local: not cloned
- Category: finance-tools / anthropic-official
- Status: LATER
- Why: Anthropic 官方金融服务示例仓库（28.9K★），研究 Claude 在金融场景应用的官方参考实现。
- Notes: Python；28.9K★；无公开 description，需读 README 补充细节。
- 最后讨论时间：2026年5月31日

### [daisy-financial-research](https://github.com/Agents365-ai/daisy-financial-research)
- GitHub: https://github.com/Agents365-ai/daisy-financial-research
- Local: not cloned
- Category: finance-tools / research-skill
- Status: LATER
- Why: 面向 AI Agent 的股票研究 Skill（A 股/港股/美股），Plan → fetch → validate → report 四段式流程，是「Agent Skills 直接服务投资研究」的可复用参照。
- Notes: Python；21★；daisy-skill 标准；支持三市场；含验证和报告生成环节。
- 最后讨论时间：2026年5月31日
