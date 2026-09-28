---
status: "indexed"
source: "https://github.com/firecrawl/anydoc"
repository: "firecrawl/anydoc"
summary: "将 Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF 等办公文档统一转换为 GitHub 风格 Markdown，核心为 Rust 库并提供 Node.js、Python、WASM 绑定。"
topics: ["document-to-markdown", "office-document-conversion", "docx-to-markdown", "pdf-to-markdown", "rust document parser", "LLM data ingestion"]
assessment: "not-tested"
---

# firecrawl/anydoc

- GitHub: https://github.com/firecrawl/anydoc
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/18
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 760d3f1800c50be70099bba0343d27daa0ed93eb；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

将 Word、PowerPoint、Excel、OpenDocument、RTF、EPUB、CSV、PDF 等办公文档统一转换为 GitHub 风格 Markdown，核心为 Rust 库并提供 Node.js、Python、WASM 绑定。

## 适用场景

- 需要把多种办公/电子文档批量或在线转成 Markdown 喂给 LLM 或做检索入库的管道，前提是输入为文本型文档（推断，基于 README 的 LLM-ready 定位与格式列表）
- 同一流程要处理格式混杂的文档并希望输出风格一致，避免为每种格式各写一套转换逻辑（README 明确宣称统一文档模型与单一序列化器）
- Node.js 或 Python 服务端需要非阻塞转换；或浏览器端本地转换且文件不出本机（README 宣称 Node 走 libuv 线程池、Python 释放 GIL、WASM 本地转换）
- 把文档转换能力接入 AI Agent，通过 Agent Skill 让 agent 读取办公文档（README 的 Agent skill 章节）
- 需要在 Markdown 中保留标题锚点、表格合并单元格、脚注、任务列表、公式（LaTeX）等结构（README Features 章节）
- 扫描件 PDF 需要 OCR：可选用托管 OCR 把整份文档发往 Firecrawl Parse（README OCR 章节，注意数据外发）

## 项目宣称的能力

- README 宣称支持 14 种格式（doc/docx/docm、ppt/pps/pot/pptx/pptm/ppsx/ppsm、xls/xlsx/xlsm/xlsb、odt/ods/odp、rtf、epub、csv、pdf），覆盖 Word/PPT/Excel/OpenDocument/RTF/EPUB/CSV/PDF（Supported formats 章节）
- README 宣称所有格式经共享文档模型和单一 Markdown 序列化器输出，转义、表格、锚点、脚注行为一致（Features 第一项）
- README 宣称支持完整文档结构：标题锚点、粗斜体/删除线、代码块、链接与内部交叉引用、多层/任务列表、合并单元格表格、引用、脚注尾注、演讲者备注（Features 第二项）
- README 宣称 Word/PowerPoint 的 OMML、OpenDocument/EPUB 的 MathML、RTF 公式可转为 LaTeX 数学（Features 第三项）
- README 宣称按文件内容（PDF 头、RTF open group、OLE 流名、ZIP mimetype）识别格式，错扩展名仍可正确转换（Features 第五项、Format detection 章节）
- README 宣称纯 Rust、无 ML 模型与外部服务，中位转换时间低于 5ms，并提供 bench/ 基准与快照/变异/fuzz 测试（Features 第六项、Benchmark、Development 章节）

## 限制与待验证

- README 的基准（score 81、中位 4.4ms 及逐格式对比）由作者自建、LLM 裁判口径且语料不可再分发，属 README 宣称而非独立验证，需检查 bench/ 复现条件与语料代表性
- 本地不做 OCR，扫描/纯图片 PDF 会以 NeedsOcr 失败；启用托管 OCR 需把整份文档发往 Firecrawl Parse 并依赖外部服务/API key（README OCR 章节、Errors 章节）
- 托管 OCR 无页面选择性，只能整份文档外发；失败时 Node 返回 code 为 hosted、Python 抛 HostedError（README OCR 章节）
- Rust crate 没有 ocr 选项且从不发起网络请求，OCR 能力仅 Node/Python/CLI 具备（README OCR 章节）
- 虽然 README 称转换错误仅在无法产出完整 Markdown 时发生，但对“部分页面提取失败”等低质量输出的判定标准未知，需以真实文档验证
- README 未给出各格式解析的已知边界（复杂版式、图表、宏、OLE 嵌入对象的具体还原程度），需针对目标文档抽样验证
- 仓库未见实际使用方或生态信息，README 中的托管服务与 Agent Skill 属同一厂商宣传，需检查第三方采用情况

## 什么情况下重新考虑

- 需要把多种办公文档统一转 Markdown 并接入 LLM/检索管道，且希望用 Rust 或 Node/Python 绑定时
- 现有转换工具在某类格式（如 old .doc/.ppt/.xls、ODF、RTF、EPUB）质量不足，需按格式逐一对比时
- 需要在浏览器端本地转换文档、避免文件上传服务器时
- 需要扫描 PDF 的 OCR 且可接受把文档交给托管服务时
- 需要公式转 LaTeX、表格合并单元格、脚注等结构保真度，需实测与现用工具对比时

## 检索关键词

- document-to-markdown
- office-document-conversion
- docx-to-markdown
- pdf-to-markdown
- rust document parser
- LLM data ingestion
