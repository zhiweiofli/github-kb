---
status: "indexed"
source: "https://github.com/tw93/Pake"
repository: "tw93/Pake"
summary: "把任意网页用一条命令打包成 macOS/Windows/Linux 桌面应用。"
topics: ["Tauri", "Rust", "网页转桌面应用", "跨平台打包", "pake-cli", "GitHub Actions 构建"]
assessment: "not-tested"
---

# tw93/Pake

- GitHub: https://github.com/tw93/Pake
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/7
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: b45671977677cc94a3949e56f6b1eacf999f740d；输入截断: False
- License: GPL-3.0

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

把任意网页用一条命令打包成 macOS/Windows/Linux 桌面应用。

## 适用场景

- 需要给某个网页版服务（如 ChatGPT、Notion）做轻量桌面客户端，且可接受以 Tauri/Rust 打包为前提（推断）
- 开发者用 CLI 一键打包网页并自定义图标、窗口尺寸，或用 GitHub Actions 在线构建免本地环境（README《Getting Started》《Command-Line Packaging》）
- 在脚本或 AI agent 中以 --json 或 --config app.json 声明式批量生成桌面应用（README《Command-Line Packaging》）
- 对已有本地前端构建产物（如 ./dist）直接打包为桌面应用（README《Command-Line Packaging》）
- 需要快捷键、沉浸式窗口、拖拽、样式自定义、去广告等桌面外壳功能（README《Features》，具体实现需查 docs/advanced-usage.md）

## 项目宣称的能力

- README《Features》宣称安装包比 Electron 小近 20 倍、磁盘占用通常低于 10M
- README《Features》宣称基于 Rust Tauri，比传统 JS 框架更快、内存占用更低
- README《Features》宣称一条命令即可打包，无需复杂配置，并支持在线构建
- README《Features》宣称支持快捷键、沉浸式窗口、拖拽、样式定制与去广告
- README《Command-Line Packaging》提供 CLI 参数文档、--json 机器可读输出、--config app.json 与本地 dist 打包入口
- README《License》中的 Pake Output Exception 宣称用 Pake 构建的应用归用户所有并可自由分发

## 限制与待验证

- GPL-3.0 传染性约束与 Output Exception 的实际边界需查阅 LICENSE 与 LICENSE-EXCEPTION 原文确认
- 未运行代码，也未验证安装包体积、性能、内存占用的宣称，需自行构建对比
- 体积/速度对比仅针对 Electron，无第三方 benchmark
- Development 段要求 Rust &gt;=1.85、Node &gt;=22（推荐 LTS，&gt;=20 亦可），首次打包需配置环境且可能较慢
- 未说明对需要登录态、Service Worker、原生 API 或反爬网页的兼容程度，需查 docs/faq.md
- 未提供 docs、schema、llms.txt 等被引用文件内容，CLI 参数与配置细节存在 UNKNOWN

## 什么情况下重新考虑

- 需要为某个网页快速产出跨平台桌面客户端时
- 需要评估在 CI 或 AI agent 中批量/自动化打包桌面应用时
- 需要确认 GPL-3.0 与 Output Exception 对商业分发的影响时
- 需要体积与内存远小于 Electron 的桌面外壳方案时

## 检索关键词

- Tauri
- Rust
- 网页转桌面应用
- 跨平台打包
- pake-cli
- GitHub Actions 构建
