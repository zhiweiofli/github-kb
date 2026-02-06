# GitHub KB Index

> Repo 索引（从 CLAUDE.md 分离）。
> 约定：除非明确提升优先级，否则新收录 repo 的 Status 默认 `LATER`。

## Index

### [bili2text](./repos/bili2text)
- Category: content-pipeline / speech-to-text
- Status: LATER
- Why: B 站视频快速转写成文本资产，便于归档与二次加工。
- Notes: 下载视频→提取/分割音频→Whisper 转写。
- 最后讨论时间：2026年2月7日

### [wechat-article-exporter](./repos/wechat-article-exporter)
- Category: content-pipeline / export
- Status: LATER
- Why: 批量导出公众号文章与数据（阅读量/评论），形成可离线保存的资料库。
- Notes: 支持在线站点使用；亦支持 Docker 私有化与 Cloudflare 部署；可导出 html/json/excel/txt/md/docx。
- 最后讨论时间：2026年2月7日

### [hacker-podcast](./repos/hacker-podcast)
- Category: content-pipeline / summarization
- Status: LATER
- Why: 关注“信息→总结→音频分发”的自动化内容生产链路。
- Notes: 自动抓取 Hacker News 热门文章→AI 生成中文总结→转换为播客内容。
- 最后讨论时间：2026年2月7日

### [trendFinder](./repos/trendFinder)
- Category: intel-trends
- Status: LATER
- Why: 获取上游趋势信号，为内容管线/选题提供输入。
- Notes: README 描述为聚合趋势话题的工具（“Stay on top of trending topics…”）。
- 最后讨论时间：2026年2月7日

---

### [serena](./repos/serena)
- Category: agent-framework / coding-agent
- Status: LATER
- Why: 把 LLM 变成可直接在代码库上工作的 agent，评估其工具化能力与可控性。
- Notes: Coding agent toolkit（对接代码库的执行/工具体系）。
- 最后讨论时间：2026年2月7日

### [superpowers](./repos/superpowers)
- Category: agent-framework / workflow
- Status: LATER
- Why: 关注“可组合 skills + 工作流”的 agent 开发范式。
- Notes: 面向 coding agents 的完整软件开发工作流。
- 最后讨论时间：2026年2月7日

### [SuperClaude_Framework](./repos/SuperClaude_Framework)
- Category: agent-framework / instruction-injection
- Status: LATER
- Why: 研究“行为指令注入 + 组件编排”如何让 Claude Code 形成结构化开发平台。
- Notes: 提供多命令/多模式/集成的框架化配置与文档体系。
- 最后讨论时间：2026年2月7日

### [openskills](./repos/openskills)
- Category: agent-framework / skills-loader
- Status: LATER
- Why: 关注 skills 的加载/分发/可复用机制，作为 agent 工具链的底座候选。
- Notes: Universal skills loader for AI coding agents。
- 最后讨论时间：2026年2月7日

### [vibe](./repos/vibe)
- Category: sandboxing / agent-security
- Status: LATER
- Why: 想把 agent 执行环境隔离出主机，降低越权读取与环境污染风险。
- Notes: 在 macOS 上快速启动零配置 Linux VM，用于沙箱化/隔离 LLM agents。
- 最后讨论时间：2026年2月7日

---

### [NyRAG](./repos/NyRAG)
- Category: rag-search
- Status: LATER
- Why: 关注从抓取/处理→索引→混合检索→Chat UI 的一体化 RAG 工具链。
- Notes: 支持爬网站或处理文档，并部署到 Vespa 做 hybrid search。
- 最后讨论时间：2026年2月7日

---

### [Open-AutoGLM](./repos/Open-AutoGLM)
- Category: device-agent
- Status: LATER
- Why: 关注手机端 agent（多模态理解屏幕 + 自动化执行）的可行性与安全机制。
- Notes: ADB/HDC 控制设备；支持敏感操作确认与人工接管。
- 最后讨论时间：2026年2月7日

### [ai-auto-touch](./repos/ai-auto-touch)
- Category: device-agent / android-automation
- Status: LATER
- Why: 关注“自然语言→多设备控制”的平台化落地。
- Notes: FastAPI + React；支持实时屏幕镜像（scrcpy）与批量设备管理。
- 最后讨论时间：2026年2月7日

### [Operit](./repos/Operit)
- Category: device-agent / on-device
- Status: LATER
- Why: 关注端侧助手（工具调用/工作流/记忆）在 Android 上的产品形态。
- Notes: 强调设备端运行（除 API 调用），支持工具调用、深度搜索、工作流与定制。
- 最后讨论时间：2026年2月7日

---

### [Ghost-Downloader-3](./repos/Ghost-Downloader-3)
- Category: downloader-tools
- Status: LATER
- Why: 关注下载与资源整合工具（可能可接入内容管线的“获取层”）。
- Notes: AI-powered cross-platform multithreaded downloader；IDM 类智能分片等。
- 最后讨论时间：2026年2月7日

### [sure](./repos/sure)
- Category: product-app / personal-finance
- Status: LATER
- Why: 关注开源产品级应用（自托管、性能、协作维护）的工程实践。
- Notes: Maybe Finance 社区维护 fork；可用 Docker 自托管；AGPLv3。
- 最后讨论时间：2026年2月7日

