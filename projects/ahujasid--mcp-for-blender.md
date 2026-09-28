---
status: "indexed"
source: "https://github.com/ahujasid/mcp-for-blender"
repository: "ahujasid/mcp-for-blender"
summary: "通过 MCP 协议把任意 LLM 客户端与 Blender 3D 连接起来，让 AI 以提示词方式驱动建模、材质与场景操作（README 宣称）。"
topics: ["MCP", "Blender", "LLM 3D 建模", "Blender Python 脚本", "Poly Haven", "AI 生成 3D 模型"]
assessment: "not-tested"
---

# ahujasid/mcp-for-blender

- GitHub: https://github.com/ahujasid/mcp-for-blender
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/14
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 4e4626c6c3d5180b58c0c2eda1761591043e2e9e；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

通过 MCP 协议把任意 LLM 客户端与 Blender 3D 连接起来，让 AI 以提示词方式驱动建模、材质与场景操作（README 宣称）。

## 适用场景

- 用 Claude Desktop/Claude Code/Cursor/VS Code/Codex 等 MCP 客户端，通过自然语言在 Blender 中创建与修改对象、材质、灯光和场景（README「Quickstart」「Capabilities」）。前提：本机安装 Blender 3.0+、Python 3.10+ 与 uv，并在 Blender 内启用插件并启动 socket 服务。
- 从 Poly Haven、Sketchfab、Poly Pizza 检索并导入 CC0/免费资产，或用 Hyper3D Rodin、Hunyuan3D 生成 3D 模型（README「Capabilities」，部分需自备 API Key）。
- 把场景、选区或指定对象导出为 GLB/FBX 供其他应用使用（README「Capabilities」中的 export_scene）。
- 让 AI 直接执行 Blender Python 代码以完成脚本化/批量化操作（README「Features」「Limitations &amp; Security Considerations」；风险高，须先保存工程）。
- 在隔离或受限环境部署：用 Docker 只承载 MCP server 或 pipx 替代 uvx（README「Run with Docker」「Install without uv」）；推断可用于服务器/无 GUI 客户端场景，但 Blender 本身仍需运行在可访问的主机上。
- 推断：多 Blender 实例并行操作时，可通过 --port 为每个客户端条目指定不同端口（README「Environment Variables」示例，需自行验证稳定性）。

## 项目宣称的能力

- README「Features」宣称：基于 socket 的双向通信，支持对象创建/修改/删除、材质与颜色控制、场景信息查询、在 Blender 中执行任意 Python 代码。
- README「Capabilities」宣称：可导出场景/选区/指定对象为 GLB/FBX，可查询 bpy API 与节点 schema 以减少字段猜测。
- README「Capabilities」「Poly Haven」章节宣称：接入 Poly Haven（约 2400 个 CC0 HDRI/贴图/模型，无需 API Key），并在导入对象上写入来源与许可自定义属性。
- README「Poly Pizza」章节宣称：接入约 10600 个低多边形模型，可按许可（如 CC0）与类别过滤，并写入 attribution 自定义属性。
- README「Capabilities」宣称：支持 Sketchfab 模型检索与 Hyper3D Rodin、Hunyuan3D 的 AI 生成 3D 模型，凭据可持久化在插件偏好或环境变量（README「Persistent API Credentials」）。
- README「Safe mode」「Telemetry Control」宣称：提供脚本执行前安全校验开关，以及默认关闭内容采集、可整体禁用的遥测设置。

## 限制与待验证

- 安全：README「Limitations &amp; Security Considerations」「Environment Variables」明确 execute_blender_code 可执行任意 Python，socket 服务无认证与加密，任何能访问该端口的人都可在 Blender 内运行代码；须限定 localhost 并优先用 SSH 隧道。
- 性能：README「Troubleshooting」指出 Poly Haven 下载运行在 Blender 主线程，UI 会卡住；文件体积随分辨率约四倍增长，建议 1k/2k。
- 网络限制：README「Troubleshooting」指出 static.poly.pizza 有 Cloudflare 机器人防护，会屏蔽数据中心、VPN 与云 IP，下载失败需换普通网络或手动导入。
- 复杂度：README「Troubleshooting」提示复杂操作需拆成小步骤，否则可能超时；且同一时间只应运行一个 MCP server 实例。
- 外部依赖：Sketchfab、Poly Pizza、Hyper3D、Hunyuan3D 需自备 API Key/凭据，Hunyuan3D 还区分大陆与国际账号端点（README「Hunyuan3D on Tencent Cloud」）；另有付费 Premium 选项（README「Premium」），其可用性与条款未在输入中说明。
- 未知项：真实稳定性、跨版本 Blender 兼容性、遥测实际行为、issue 与维护响应速度均未在输入中体现，需检查 issue 列表、发布记录与 TERMS_AND_CONDITIONS.md；README 未提供性能基准，也无第三方对比证据。

## 什么情况下重新考虑

- 需要在 Blender 中批量或脚本化完成建模/材质/导出任务，希望用 LLM 生成并执行 bpy 脚本时。
- 团队选定 MCP 客户端（如 Claude Desktop、Cursor、VS Code）并希望把 Blender 纳入 AI 工作流时。
- 需要从 Poly Haven、Poly Pizza、Sketchfab 自动检索并导入资产，或有 CC0 许可合规取数需求时。
- 需要在无 GUI 或隔离环境部署 MCP server（Docker/pipx），或需要并行控制多个 Blender 实例时。
- 关注点转向安全审计、遥测政策或商业支持时，重新查看其安全模式、T&amp;C 与 Premium 说明。

## 检索关键词

- MCP
- Blender
- LLM 3D 建模
- Blender Python 脚本
- Poly Haven
- AI 生成 3D 模型
