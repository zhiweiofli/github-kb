---
status: "indexed"
source: "https://github.com/andrewyng/context-hub"
repository: "andrewyng/context-hub"
summary: "为编码智能体提供可检索、带版本和语言变体的 markdown 文档与技能目录，减少 API 幻觉并在会话间保留注释。"
topics: ["coding-agent", "API documentation", "agent skills", "CLI", "npm", "markdown docs"]
assessment: "not-tested"
---

# andrewyng/context-hub

- GitHub: https://github.com/andrewyng/context-hub
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/9
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 946455a8cc7e1e8d7c0013a17c7303b1378230ae；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

为编码智能体提供可检索、带版本和语言变体的 markdown 文档与技能目录，减少 API 幻觉并在会话间保留注释。

## 适用场景

- 已使用支持 CLI 调用的编码智能体（如 Claude Code），希望在检索 API 文档前先取用经过整理的版本化文档；README 的 Quick Start 与 How It Works 描述了该流程。
- 需要按语言（--lang py/js）获取同一 API 的对应文档变体；README 的 Content Types 章节宣称支持。
- 需要把多次会话中发现的使用缺口以本地注释保存并在后续拉取时重新注入（--with-annotations）；README 的 Self-Improving Agents 与 Commands 宣称。
- 希望用 up/down 反馈把使用情况回流给文档作者；README 的 Annotations &amp; Feedback 宣称。
- 作为文档或技能内容的贡献者，以 markdown + YAML frontmatter 形式提交 PR；README 的 Contributing 章节宣称。

## 项目宣称的能力

- README 宣称提供“curated, versioned docs”，内容以 markdown 存于仓库，可检查智能体实际读取的内容（开头段落）。
- README 的 Content Types 宣称文档按语言区分，支持 --lang py/js。
- README 的 Incremental Fetch 宣称可按 --file 拉取单个引用文件或用 --full 拉取全部，减少 token 消耗。
- README 的 Annotations &amp; Feedback 宣称注释跨会话持久，且默认视为不可信输入，需显式 --with-annotations 才注入。
- README 宣称反馈（up/down）会回流给文档作者以改进内容。
- README 宣称任何人可贡献文档与技能，格式为 markdown + YAML frontmatter，通过 PR 提交。

## 限制与待验证

- README 宣称的“减少幻觉、代码更可能可用”无 benchmark 或对照数据支撑，需实际使用验证；输入中也无用户关注原因，无法判断真实适用度。
- 实现形态为全局 npm 包 @aisuite/chub，宣称依赖 Node.js &gt;=18；未在输入中提供离线可用性、私有文档支持或数据外传范围的说明，需查看 CLI Reference 与包元数据确认。
- 智能体集成依赖提示词或 SKILL.md（如 Claude Code 的 ~/.claude/skills 目录），属于约定式集成，具体兼容的智能体清单 UNKNOWN，需查阅文档与 skill 文件。
- 注释默认被当作不可信输入，能起作用的范围和重注入行为细节 UNKNOWN，需查 docs/feedback-and-annotations.md。
- 内容覆盖面、更新频率与作者响应情况 UNKNOWN；仓库 pushed_at 为 2026-05-31，无法据此判断文档时效。
- 反馈机制是否匿名、是否携带使用数据等隐私细节 UNKNOWN，需查 CLI Reference 与实现。

## 什么情况下重新考虑

- 当团队需要在智能体会话间复用 API 使用经验、且当前依赖的文档源频繁出现 API 幻觉时。
- 当目标 API 或框架需要按语言提供文档变体，并存在明确的分层引用文件可增量拉取时。
- 当需要让反馈回流到文档维护方形成闭环，且愿意参与内容贡献时。

## 检索关键词

- coding-agent
- API documentation
- agent skills
- CLI
- npm
- markdown docs
