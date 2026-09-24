---
status: "indexed"
source: "https://github.com/tt-a1i/archify"
repository: "tt-a1i/archify"
summary: "一个面向 AI Agent 的 Skill，把描述或仓库分析结果转成自带交互、可校验、可导出图片的自包含 HTML 架构/工作流/时序/数据流/生命周期图。"
topics: ["AI Agent Skill", "架构图生成", "交互式 HTML 图", "系统架构可视化", "时序图/工作流图", "MIT 开源"]
assessment: "not-tested"
---

# tt-a1i/archify

- GitHub: https://github.com/tt-a1i/archify
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/1
- 评估日期: 2026-09-24
- 模型: deepseek-flash
- README blob: a0dbaf7d2ad941dc0ca2e09404d44a3de5deaeb9；输入截断: False
- License: MIT

## 我关注的原因

本次由用户指定作为 GitHub Actions 真实收录验收项目；其他个人关注原因未提供。

## 一句话说明

一个面向 AI Agent 的 Skill，把描述或仓库分析结果转成自带交互、可校验、可导出图片的自包含 HTML 架构/工作流/时序/数据流/生命周期图。

## 适用场景

- 需要把系统架构、CI/CD 流程、API 调用链、数据血缘或状态流转讲给他人听时，让 Agent 生成可点击、可追踪路径的交互式 HTML（README 宣称支持 Cursor、Claude Code、Codex CLI、OpenCode 等 Agent）。
- 设计或 PR 评审中比较前后架构快照：README 宣称提供 Architecture Delta，对比已验证的 Before/Delta/After 并输出机器可读回执（属 README 宣称，是否实用需自行用 compare 命令验证）。
- 让 Agent 阅读公开仓库并生成带源码证据的架构图，节点标注 SRC 并打开固定 commit 的文件与行范围（需网络与对应公开仓库）。
- 把图作为自包含 HTML 分发给不安装 Archify 的同事，或用导出功能生成 PNG/视频/1200×630 分享卡用于 README 与发布说明。
- 需要中英文界面或深浅色主题切换的展示材料（README 称 meta.locale 与主题切换仅影响界面文案，不改作者内容）。

## 项目宣称的能力

- README 宣称支持五类图（Architecture/Workflow/Sequence/Data Flow/Lifecycle）并给出各自适用的提示词模板（Choose the right diagram 章节）。
- 输出为单文件自包含 HTML，查看方无需安装；导出含 PNG、动图与分享卡（Download it. Open it. Explore it. / Preview 章节）。
- 交付前有校验与原子替换：schema、布局、HTML/SVG、route 与标签避让需全部通过，失败不覆盖上一版可用产物（The engineering behind the experience / How it works）。
- 失败返回机器可读的稳定规则码与修复建议，而非 Node 堆栈（validate --json / deliver --json 描述）。
- 交互声称忠于作者绘制的节点与关系（focus/reach/route/lens/story），且不宣称运行时影响（Truthful interaction 章节）。
- MIT 许可，README 提供安装命令与多 Agent 安装路径表（License / Installation options 章节）。

## 限制与待验证

- 未实际试用，无法验证生成质量、布局观感与校验规则的实际拦截效果；README 自称的“验证通过”需按 Proof Lab 与 validate 命令自行复核。
- README 明确不包含 Mermaid 自动解析、通用自动布局、托管分享与 WYSIWYG 编辑（Reference and scope），这些需求需另找工具。
- 依赖 Agent 与 Node.js 运行环境（CLI 示例为 node archify/bin/archify.mjs；Claude.ai 沙箱能力取决于是否有 Node），本地无 Node 时无法生成。
- 版本为开发版 v2.17.0-dev.1，接口与行为可能变动；未提供稳定性承诺，需查看 CHANGELOG/ROADMAP。
- README 提及可选更新检查会发起 HTTP GET（可设 ARCHIFY_UPDATE_CHECK_DISABLED=1 关闭），对离线或严格网络环境需评估；其数据收集声明仅为 README 宣称，需自行审计代码验证。
- 仓库分析、外部链接与地图跳转需网络；社区案例（如行程、合同审阅）为个别用户自行扩展，不代表内置能力。

## 什么情况下重新考虑

- 需要让 AI Agent 直接产出可交互、可校验并导出的架构或流程图时。
- 需要对比 PR/设计前后架构差异并要求机器可读回执时。
- 需要把图嵌进文档或分享卡、且要求单文件无外部依赖分发时。
- 需要在 CI 或脚本中对图源做 schema 校验时。
- 有 Node 环境并希望接入 Claude Code/Codex/Cursor 等 Agent 工作流时。

## 检索关键词

- AI Agent Skill
- 架构图生成
- 交互式 HTML 图
- 系统架构可视化
- 时序图/工作流图
- MIT 开源
