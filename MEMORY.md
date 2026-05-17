# github-kb / MEMORY（长期记忆）

> 这里记录“可复用的结论”，不是流水账。
> 建议格式：每条结论都尽量包含证据来源（repo/文件/commit/链接）与适用边界。

## 主题 1：agent-framework
### Key takeaways
- 通过研究 [claw-code](https://github.com/ultraworkers/claw-code)，可以发现下一代高性能 Agent Harness 正在向 Rust 等系统级语言迁移，其核心包含隔离的 runtime、MCP 编排以及标准化的 tools 规范，有利于规避动态语言在复杂并行上下文下的性能瓶颈。[已内化]
- [serena](https://github.com/oraios/serena) 提供了 IDE 级别的语义代码工具（`find_symbol`, `find_referencing_symbols`, `insert_after_symbol`），通过 LSP 协议支持 19 种语言，以 MCP server 形式对接任意 LLM/Agent。核心洞察：symbol-level 操作远优于 grep + 字符串替换，大幅降低 token 消耗。[已内化]
- [superpowers](https://github.com/obra/superpowers) 展示了"可组合 Skills + Subagent 驱动开发"范式：Agent 不直接写代码，而是先引导用户对齐 spec → 生成实现计划 → 启动子 Agent 逐任务执行并自检。强调 TDD、YAGNI、DRY，可实现数小时自主编码。[已内化]

### Reusable patterns
- **MCP 作为通用工具注入协议**：serena 和 superpowers 均通过 MCP 与 coding agent 集成，说明 MCP 正在成为 agent-tool 交互的事实标准。[已内化]
- **Spec-first → Plan → Subagent execution**：superpowers 的三阶段流程（规格确认→计划分解→子代理执行）可复用于任何需要长时间自主执行的 agent 工作流。[已内化]

### Risks / gotchas
- serena 对 LSP 有强依赖，语言服务器崩溃时需自动重启（已内置恢复机制），但新语言接入成本较高（需实现 language server class + 测试仓库）。[已内化]
- superpowers 的 subagent 链过长时可能出现 plan drift（计划偏移），需定期与人类对齐。[已内化]

### When to use / when not to use
- **serena 适用**：需要在大型代码库上做精确符号级操作（跳转、重命名、引用查找）时，比 grep+sed 方案效率高一个数量级。不适用：纯文本/配置文件操作，或 LSP 未覆盖的语言。[已内化]
- **superpowers 适用**：中大型功能开发需要结构化规划和多步自主执行时。不适用：快速单文件 bug fix 或 hotfix。[已内化]

### Comparisons
- serena vs Claude Code 内置工具：serena 提供更精细的 symbol-level 操作（类似 IDE），而 Claude Code 的 Read/Edit/Grep 是文件级操作。两者通过 MCP 可互补。[已内化]
- superpowers vs 手动提示工程：superpowers 将 spec → plan → execute 流程固化为自动触发的 skills，减少人工提示工程开销。[已内化]

---

## 主题 2：content-pipeline
### Key takeaways
- [bili2text](https://github.com/lanbinleo/bili2text) 实现了"B 站视频 URL → 下载 → 音频提取/分割 → Whisper 转写"的端到端自动化管线。核心依赖 Whisper 模型做语音识别，支持多 P 视频批量处理。[已内化]
- [markitdown](https://github.com/microsoft/markitdown)（109K★，AutoGen 团队出品）是「任何文件 → Markdown」的工业级默认方案：覆盖 PDF / Office / 图片（EXIF+OCR）/ 音频（ASR）/ HTML / CSV / JSON / ZIP / YouTube URL / EPub，重心在「保留结构（headings/lists/tables/links）」而非高保真外观，恰好匹配 LLM 消费语料的需要。已有官方 MCP server 包（markitdown-mcp）。[已内化]
- [voicebox](https://github.com/jamiepine/voicebox)（18K★）是 ElevenLabs 的本地优先替代：Tauri(Rust) 原生应用 + 5 个 TTS 引擎（Qwen3-TTS / LuxTTS / Chatterbox / HumeAI TADA）+ 23 语言 + paralinguistic tags(`[laugh]`/`[sigh]`) + 自动分块 crossfade 合成长文本 + 多轨时间线 + REST API。完整补齐「文本资产 → 配音/播客」这一段的离线链路。[已内化]
- [GEOFlow](https://github.com/yaojingang/GEOFlow) 把 GEO/SEO 内容运营做成完整后台：模型配置 → 素材库（标题/关键词/图片/知识库/提示词）→ 任务调度（定时/队列/重试）→ 草稿审核发布 → 前台 SEO 输出（OG/结构化数据）。PHP + PostgreSQL + Docker Compose，OpenAI 风格接口兼容多家模型。[已内化]
- [youtube-to-notebooklm](https://github.com/azuma520/youtube-to-notebooklm) 展示「Skills 组合 + 自然语言调度」做研究工作流：yt-search（yt-dlp 封装）+ anything-to-notebooklm（notebooklm-py 推进 NotebookLM 生成播客/脑图/测验）+ whisper-transcribe（faster-whisper），一条自然语言命令跨多 Skill 流转。[已内化]

### Reusable patterns
- **URL → Download → Extract → Transform** 四步管线模式在 bili2text、hacker-podcast 中都有体现，可抽象为通用的内容资产化框架。[已内化]
- **Any-file → Markdown 作为 ingest 归一层**：本项目 `wiki/0_Raw/` 当前处理 PDF/图片/md 混杂，若在 `/wiki-ingest-raw` 前置统一用 markitdown 做二进制 → markdown 归一化，可显著降低下游解析分支复杂度。对比 defuddle（网页文本清洗）——markitdown 负责「结构重建」而 defuddle 负责「噪声剥离」，二者互补。[已内化]
- **审核-发布工作流即分发层脚手架**：GEOFlow 的「草稿 → 审核 → 发布」三段式 + 队列 Worker 是当前知识库完全缺失的一段（`3_Synthesis/` 止步于生成报告，未接分发）。若未来补齐「分发 & 个人品牌」维度，这套三段式 + 调度器可直接借鉴。[已内化]
- **终端 Skills 编排研究工作流**：youtube-to-notebooklm 把「研究」解成 3 个高内聚低耦合的 Skill，靠自然语言 router 串联；比一个大而全的 "research-agent" 更可维护。对本项目 Skills 重构的启示——把 `wiki-synthesize-report` 这种复合 Skill 拆成更原子的 ingest/query/format 子 Skill。[已内化]

### Risks / gotchas
- bili2text 依赖 B 站视频下载接口，存在合规与接口变更风险（API 封禁、cookie 失效）。[已内化]
- Whisper 转写在嘈杂音频或方言场景下精度下降明显，需人工校验或后处理。[已内化]

### When to use / when not to use
- **适用**：需要将视频/音频内容转化为可检索文本资产（笔记、知识库入料）时。不适用：实时转写或低延迟场景。[已内化]

### Comparisons
- bili2text vs 商业转写服务（讯飞/百度）：开源免费但精度依赖本地算力和模型选择；商业服务精度更高但有成本和隐私顾虑。[已内化]

---

## 主题 3：llm-inference
### Key takeaways
- [omlx](https://github.com/jundot/omlx) 为 Apple Silicon 环境提供了极具启发性的 KV Cache 分层架构（内存 + SSD），实现了 Copy-on-Write 和统一的前缀共享，这种针对长上下文 coding agent（如 Claude Code）的架构能够大幅优化本地任务执行的切换延迟。[已内化]

---

## 主题 4：claude-code-skills-ecosystem

### Key takeaways
- Anthropic 官方 [skills](https://github.com/anthropics/skills)（113K★）确立了 Agent Skills 的标准规范——每个 Skill 一个文件夹 + `SKILL.md`，遵循 [agentskills.io](http://agentskills.io) 标准。这个规范已被 Claude Code、Codex、OpenCode 等多个 Agent 采纳。[已内化]
- **Plugin = Skills + Hooks + MCP Servers** 的完整包。[claude-plugins-official](https://github.com/anthropics/claude-plugins-official) 展示了 Plugin 作为 Skills 超集的架构——可以包含 hooks 脚本（PreToolUse/PostToolUse 等事件）和 MCP server 配置，实现比纯 Skill 更深的运行时集成。[已内化]
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)（21K★）由 Obsidian 创始人出品，提供 5 个关键 Skills：obsidian-markdown（wikilinks/embeds/callouts）、obsidian-bases（views/filters/formulas）、json-canvas（可视画布）、obsidian-cli（Vault CLI 交互）、defuddle（网页清洁提取，去广告/去杂物以节省 token）。**对本 PKM 项目的 Obsidian 集成有直接价值**。[已内化]
- [web-access](https://github.com/eze-is/web-access)（4.3K★）补齐了 Claude Code 原生 WebSearch/WebFetch 的不足：**三层通道调度**（WebSearch → WebFetch → curl → Jina → CDP 按场景自主判断）+ **CDP Proxy**（直连用户日常 Chrome，天然携带登录态，支持动态页面和交互操作）+ **并行分治**（多目标时分发子 Agent 并行执行，tab 级隔离）。含站点经验积累机制（类似 muscle memory）。[已内化]
- [khazix-skills](https://github.com/KKKKhazix/khazix-skills)（4.6K★，数字生命卡兹克）是「**个人方法论 → Agent Skills**」的高质量样本：同一资产双层发布——Prompts（复制粘贴式轻量）+ Skills（遵循 agentskills.io 标准的结构化）。两个 Skills：hv-analysis（横纵分析法深度研究，自动联网 + 输出 PDF 报告）和 khazix-writer（长文写作 Skill，含四层自检体系 + 风格示例库）。[已内化]

### Reusable patterns
- **Skill 分层架构**：基础 Skills（文件格式理解）→ 功能 Skills（特定任务执行）→ Workflow Skills（多步骤编排）。本项目的 6 个 Skills 可按此分层重新审视。[已内化]
- **defuddle 模式**：在 ingest 前用 defuddle 类工具清洗网页内容（去广告/导航/footer），可大幅降低 token 消耗和噪声。本项目的 `/wiki-ingest-raw` 可考虑集成。[已内化]
- **ClawFlows 工作流定义**：[clawflows](https://github.com/nikilster/clawflows) 用纯文本定义 113 个预建工作流（含 cron 触发），展示了 Agent 从"编程工具"扩展到"生活助手"的可能性（邮件处理、早间简报、睡眠模式、会议准备等）。[已内化]
- **双层资产（Prompt + Skill）发布策略**：khazix-skills 的模式启示——同一方法论以 Prompt（零门槛传播）和 Skill（重工具加载）双形态发布，既覆盖非 Claude Code 用户，又保留高级用户的结构化能力。本项目未来若要把「五大维度 + 杠杆公式」打包成可复用资产，可参考此模式分别输出 Prompt 版（Deep Research 用）+ Skill 版（Claude Code 用）。[已内化]

### Risks / gotchas
- web-access 的 CDP 直连 Chrome 需要用户安装浏览器扩展并启动 daemon，有一定配置门槛。[已内化]

---

## 主题 5：agent-harness-best-practices

### Key takeaways
- [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)（33K★）系统性梳理了 10+ 个顶级工作流框架的对比矩阵。核心发现：所有主流框架都收敛到 **Research → Plan → Execute → Review → Ship** 这一通用模式，差异仅在编排层的具体实现。[已内化]
- [pro-workflow](https://github.com/rohitg00/pro-workflow)（1.7K★）实现了**自纠错记忆系统**：Claude Code 每次被用户纠正后，纠正内容持久化到 SQLite（FTS5 全文搜索），下次会话自动加载。50 次会话后纠正率趋近于零。**这是"知识复利"在 Agent 自身行为上的应用**。[已内化]
- pro-workflow 的 **LLM Gates** 是第一个实现 `type: "prompt"` hooks 的插件——用 AI 在 commit 前做验证和 secret 检测，将人类审查的一部分自动化。[已内化]
- [OpenHarness](https://github.com/HKUDS/OpenHarness)（7.6K★）是港大出品的开源 Agent Harness，核心特性：43+ 内置工具、CLAUDE.md 发现注入、上下文自动压缩（Auto-Compact）、MEMORY.md 持久记忆、Session Resume、多 Agent Swarm 协调。**架构上与本项目高度共鸣**。[已内化]
- [harness-engineering-from-cc-to-ai-coding](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding)（860★）是从 Claude Code 源码逆向分析 Harness 工程的中文教程。[已内化]

### Reusable patterns
- **自纠错记忆 → 知识库反馈循环**：pro-workflow 的 SQLite 持久化纠正 → 会话自动加载模式，可启发本 PKM 的 feedback memory 机制。当前本项目的 CLAUDE.md 是静态的；若能像 pro-workflow 那样动态积累用户纠正，Agent 行为会持续改善。[已内化]
- **Compact Guard（上下文压缩保护）**：pro-workflow 在上下文压缩时保留关键文件（5 文件限制、50K 预算），防止压缩导致的信息丢失。本项目的长会话场景可参考。[已内化]

---

## 主题 6：code-intelligence

### Key takeaways
- [GitNexus](https://github.com/abhigyanpatwari/GitNexus)（25K★）将代码库索引为**知识图谱**（依赖、调用链、集群、执行流），通过 MCP 暴露给 Agent。核心价值：即使小模型也能获得完整架构视野——"Like DeepWiki, but deeper"。`npx gitnexus analyze` 一键完成索引 + Skills 安装 + hooks 注册 + CLAUDE.md 生成。[已内化]
- GitNexus 的 Claude Code hooks（PreToolUse + PostToolUse）可自动在每次工具调用前后注入架构上下文，实现**无感增强**而非需要用户主动查询。[已内化]
- [DeepTutor](https://github.com/HKUDS/DeepTutor)（13K★）是 Agent-Native 的个性化学习助手，多 Agent RAG 架构（检索 Agent + 分析 Agent + 教学 Agent），展示了 Agent 在教育场景的深度应用。[已内化]

### Reusable patterns
- **知识图谱 + MCP 暴露**：GitNexus 的模式（索引 → 图谱 → MCP → Agent 消费）可推广到非代码领域——本 PKM 的概念卡片网络本质上也是一个知识图谱，若能通过 MCP 暴露给 Agent，检索效率会大幅提升。[已内化]

---

## 主题 7：dev-tools

### Key takeaways
- [OpenCLI](https://github.com/jackwener/OpenCLI)（14K★）将网站/Electron App/本地工具统一 CLI 化——79+ 内置适配器（B站/知乎/小红书/Reddit/HN/Twitter 等），通过 CDP 复用用户 Chrome 登录态，**零 LLM 成本**（运行时不消耗 token）。Agent 从"自己去网站操作"变为"调用确定性 CLI"。[已内化]
- [pretext](https://github.com/chenglou/pretext)（41K★）是 chenglou 出品的高性能文本测量与排版引擎，与 Agent/PKM 关系较远。[已内化]

### Reusable patterns
- **网站 → 确定性 CLI** 模式（OpenCLI）：对本 PKM 项目的启发——内容采集层可以从"Agent 访问网页"升级为"Agent 调用确定性 CLI 获取结构化数据"，降低网页解析的不确定性。[已内化]

---

## 主题 8：agent-harness & orchestration

### Key takeaways
- [ClawX](https://github.com/ValueCell-ai/ClawX) 和 [AionUi](https://github.com/iOfficeAI/AionUi) 共同推进了 Agent 的 GUI 增强交互。它们将以往仅能在终端运行的助手（如 Claude Code, OpenClaw, Dex 等）进行整合，提供全局视角的工作台界面。[已内化]
- [paseo](https://github.com/getpaseo/paseo) 进一步将这些 Agent 的操作面推向移动端，支持对桌面并行的 Agent 流水线进行远程语音控制调度。[已内化]
- [long-running-coding-loop](https://github.com/zalan159/long-running-coding-loop) 体现了纯 CLI 下的“设计 -> 测试 -> 自纠修复”死循环自治。这是保障代理稳定跑通复杂任务的不可缺失一环。[已内化]
- 谷歌的 [gallery](https://github.com/google-ai-edge/gallery) 则演示了通过 FunctionGemma 在纯离线移动设备上本地运行 AI Skills 流的可行性。[已内化]

### Reusable patterns
- **移动端代理遥控与离线自治**: paseo 这种通过移动端连入代理编排池的形式，可以融入当前自己的 Agentic 工作流中，使得个人知识管理可以随时离线查阅并触发新的收集提纯。[已内化]

---

## 主题 9：knowledge-retention & embedding

### Key takeaways
- [gbrain](https://github.com/garrytan/gbrain) 为“纯文本系统大脑”提供了一个极低依赖的解决方案——使用 PGLite（嵌入式浏览器级或本地 Postgres 向量存储）实现长程 Markdown 记忆保留，无需起笨重的外围数据库服务。[已内化]
- [FastCode](https://github.com/HKUDS/FastCode) 采取“混合索引和多层图建模”进行高效代码知识抓取。在大幅缩减 token 消耗和匹配延迟的基础上，还能适应小参数量模型。[已内化]

### Reusable patterns
- **长效轻量本地库架构**: 将 gbrain 使用的 PGLite 向量保留机制用于本构架的 `2_Concepts` 之中：所有内容依然维持 .md 不变，但在读取/索引面上提供一个 PGLite + FastCode 多层图混引的服务常驻做快速响应检索。[已内化]

---

## 主题 10：multi-agent-education

### Key takeaways
- [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) 应用多 Agent 到复杂长尾教育领域（构建包含教师/个性同学的沉浸式场景）。[已内化]

---

## 其他主题（未来可能纳入）
- sandboxing / agent-security
- device-agent（手机自动化）
- rag-search
- downloader-tools
- product-app
- intel-trends
- osint-crawler (如 social-analyzer)

---

## 主题 11：screenshot-github-feeder-2026-05-17

### Key takeaways
- **agent-framework / workflow-infra**：该批工具补充了 Agent 工作流的外围工程底座，包括 AI 应用后端、代理自我进化、typed agent workflow、异步子代理和系统提示词语料，可作为未来构建 Agent OS 时的候选池。代表项目：[InsForge/InsForge](https://github.com/InsForge/InsForge), [OpenSpace](https://github.com/HKUDS/OpenSpace), [PydanticAI内容工作流](https://github.com/pydantic/pydantic-ai), [code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode), [x1xh1ol/system-prompts-and-models-of-ai-tools](https://github.com/x1xh1ol/system-prompts-and-models-of-ai-tools)。[已内化]
- **agent-runtime / security / provenance**：代码执行沙箱、内容盲水印、虚拟手机与终端输出管理共同指向一个底层趋势：Agent 越能行动，越需要可审计、可隔离、可追溯、可复用的执行边界。代表项目：[Ariestar/sivtr](https://github.com/Ariestar/sivtr), [ei9987/blind_watermark](https://github.com/ei9987/blind_watermark), [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark), [lakr233/vphone-cli](https://github.com/lakr233/vphone-cli), [vndee/llm-sandbox](https://github.com/vndee/llm-sandbox)。[已内化]
- **agent-skills / ecosystem**：截图批次显示 Skills 生态从规范文档扩展到 API 转换、个人方法论、工程最佳实践与 UI/UX 专项能力，Skill 正成为可分发的方法论容器。代表项目：[agent-skills](https://github.com/addyosmani/agent-skills), [openapi-to-skills](https://github.com/neutree-ai/openapi-to-skills), [slavingia/skills](https://github.com/slavingia/skills), [mattpocock/skills](https://github.com/mattpocock/skills), [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)。[已内化]
- **code-intelligence / knowledge-retrieval**：代码库记忆、架构可视化、RAG 教程与个人知识助手说明：Agent 编程的核心瓶颈正在从生成代码转向获得正确上下文。 代表项目：[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), [CodeFlow](https://github.com/braedonsaunders/codeflow), [khoj-ai/khoj](https://github.com/khoj-ai/khoj), [theaiautomators/claude-code-agentic-rag-series](https://github.com/theaiautomators/claude-code-agentic-rag-series), [safishamsi/graphify](https://github.com/safishamsi/graphify)。[已内化]
- **content-pipeline / media-generation**：AI 视频、语音、图数据可视化工具扩展了内容资产化管线，从文本/网页采集推进到多模态生成与再加工。 代表项目：[AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video), [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk), [jamiepine/voicebox](https://github.com/jamiepine/voicebox)。[已内化]
- **product-app / open-source-apps**：开源产品型应用覆盖金融终端、文件传输、个人数据迁移、阅读器、GitHub 客户端与硬件项目，适合用于观察摩擦套利、本地优先和数据主权产品封装。代表项目：[NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR), [AltSendme](https://github.com/tonyantony300/alt-sendme), [FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal), [OpenHub-Store/Github-Store](https://github.com/OpenHub-Store/Github-Store), [Thunderbolt](https://github.com/thunderbird/thunderbolt), [mihonapp/mihon](https://github.com/mihonapp/mihon)。[已内化]
- **web-automation / agent-browser**：浏览器自动化正在从本地 headless 脚本升级为云浏览器、轻量浏览器、CLI 与抗封爬虫工具组合，成为 Agent Web 接入层的基础设施。 代表项目：[Agent-Reach](https://github.com/Panniantong/Agent-Reach), [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling), [lightpanda-io/browser](https://github.com/lightpanda-io/browser), [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli), [steel-dev/steel](https://github.com/steel-dev/steel)。[已内化]
- **developer-education / design-resources / llm-foundations**：并非所有 feeder 都是可直接接入工具链的工程组件；GitHub 互动课程、设计资源库和 LLM 底层教程更适合作为能力训练与素材库。代表项目：[GitHub Skills](https://github.com/skills), [VoltAgent/awesome-design](https://github.com/VoltAgent/awesome-design), [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)。[已内化]

### Reusable patterns
- **feeder-to-concept**：GitHub 项目不直接进入概念层，而是先在 `github-kb` 聚类成能力模式，再由 `wiki-extract-concept` 提炼 evergreen cards。[已内化]
- **verification-before-action**：凡涉及 Agent 执行、浏览器控制、代码运行、金融工具的项目，先记录边界与适用条件，再决定是否进入工具链。[已内化]
- **repo-as-signal**：星标/截图不是结论，只是信号；真正要沉淀的是工具背后的能力缺口、架构模式和可复用 SOP。[已内化]
