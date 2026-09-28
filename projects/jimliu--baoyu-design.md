---
status: "indexed"
source: "https://github.com/JimLiu/baoyu-design"
repository: "JimLiu/baoyu-design"
summary: "一个把 claude.ai/design 的设计流程打包成本地 Agent Skill 的开源项目，让 Cursor、Claude Code、Codex 等文件型编码代理在本地生成自包含 HTML 的 UI 稿、原型、线框和幻灯片。"
topics: ["Agent Skill", "Claude Design", "本地 UI 稿生成", "HTML 原型", "设计系统", "Figma 导入", "PPTX 导出", "Cursor", "Claude Code", "Codex"]
assessment: "not-tested"
---

# JimLiu/baoyu-design

- GitHub: https://github.com/JimLiu/baoyu-design
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/5
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 9533c495fb2a661040f58b7df13fc7ec0ed9169a；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

一个把 claude.ai/design 的设计流程打包成本地 Agent Skill 的开源项目，让 Cursor、Claude Code、Codex 等文件型编码代理在本地生成自包含 HTML 的 UI 稿、原型、线框和幻灯片。

## 适用场景

- 在 Cursor / Claude Code / Codex 等本地编码代理中生成 hi-fi UI 稿、交互原型、线框图或落地页，产物为可版本管理的自包含 HTML（README：Why run it locally、What it can make）。
- 需要把设计稿导出为可编辑 PPTX、PDF、MP4 或独立 HTML 以便交付（README：Export &amp; handoff、Decks &amp; PPTX export）。推断：适合已有本地代理且希望设计产物不离开代码库的团队。
- 需要把 Figma .fig、GitHub 仓库或现有 HTML/CSS 导入为设计系统或设计参考，再在其上继续设计（README：Import design sources）。
- 需要把品牌设计系统（tokens、字体、组件、UI kit）绑定到项目，约束后续页面风格一致（README：Design systems）。
- 需要为演示生成带逐元素动画并保留为 PowerPoint 原生动画的幻灯片（README：Decks &amp; PPTX export）。

## 项目宣称的能力

- README 宣称把 Claude Design 的设计流程打包成可移植 Agent Skill，支持 Cursor、Claude Code、Claude Desktop、Codex 及 70+ 代理（README：标题、Why run it locally、Quick start 前置条件）。
- README 宣称覆盖核心设计、Deck、移动与动效、Web/营销、数据与研究、文档/3D/插画、设计系统、导入源、导出与交接、AI 资产与集成等内置技能（README：What it can make 表格）。
- README 宣称输出为 designs/&lt;project&gt;/ 下的自包含 HTML，可用 localhost 预览并借助代理浏览器/标注工具对元素指点修改（README：Why run it locally、Use it、Preview server）。
- README 宣称支持从 Figma .fig 完全离线解码并导入为设计系统，产物为单个自包含交互式 preview.html（README：Import design sources）。
- README 宣称内置本地 gen-pptx CLI，通过 Playwright + 无头 Chromium 把 HTML deck 导出为可编辑 PPTX，并把 data-anim 属性写成 PowerPoint 原生动画（README：Decks &amp; PPTX export）。
- README 宣称技能由纯 Markdown 与少量 JSX/JS 脚手架构成，无构建步骤、无运行时（README：How it works）。

## 限制与待验证

- README 自称是社区对 Claude Design 的重新打包，与 Anthropic 无关联或认可（README：Credits &amp; license）；功能完整性、与网页版的差距未在输入中量化。
- README 建议搭配 Claude Opus 4.8 获得最佳效果，暗示模型能力不足时输出质量可能下降（README：Why run it locally）；未提供任何 benchmark 证明效果。
- PPTX 导出依赖本地 CLI，需运行 npm install、npx playwright install chromium 和 npm run build，且有环境/运行成本（README：Decks &amp; PPTX export）。
- 多文件原型无法从 file:// 加载，必须启动 HTTP 预览服务（README：Preview server）；推断：静态文件直接双击打开不可用。
- README 宣称‘你得到 claude.ai/design 的绝大部分能力’与‘大部分相同方法、工艺标准、输出格式’，这是宣传性表述，实际差距需自行验证。
- 输入未提供 star 数、issue 状态、发布历史或 CI 证据；维护活跃度与长期稳定性为 UNKNOWN，需检查仓库提交频率、issue 响应和 release 记录。

## 什么情况下重新考虑

- 当团队需要在本地编码代理中统一生成 UI 稿/原型/线框，并希望产物以自包含 HTML 进入仓库版本管理时。
- 当需要把现有 Figma UI kit 或现有前端代码库转换为可复用设计系统，并让代理按该系统约束继续设计时。
- 当需要从 HTML 幻灯片导出带原生动画的可编辑 PPTX，用于工程评审或对外演示时。
- 当使用的代理或模型发生变化（例如换成更强的模型或更换代理平台）而需要重新评估输出质量时。
- 当发现需要更严格的许可、供应链或外部依赖审查（Playwright、Chromium、PptxGenJS）时，可重新查看其依赖与许可状况。

## 检索关键词

- Agent Skill
- Claude Design
- 本地 UI 稿生成
- HTML 原型
- 设计系统
- Figma 导入
- PPTX 导出
- Cursor
- Claude Code
- Codex
