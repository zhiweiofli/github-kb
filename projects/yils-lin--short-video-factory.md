---
status: "indexed"
source: "https://github.com/YILS-LIN/short-video-factory"
repository: "YILS-LIN/short-video-factory"
summary: "一个 AGPL-3.0 的开源跨平台桌面端工具，宣称可用提示词与视频素材自动完成短视频的文案生成、语音合成、剪辑与字幕添加。"
topics: ["短视频自动剪辑", "AI 文案生成", "文本转语音", "EdgeTTS", "桌面端跨平台应用", "批量视频生成"]
assessment: "not-tested"
---

# YILS-LIN/short-video-factory

- GitHub: https://github.com/YILS-LIN/short-video-factory
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/19
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 916bc52060bceb1d9528aad490b8bab23e1fe84b；输入截断: False
- License: AGPL-3.0

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

一个 AGPL-3.0 的开源跨平台桌面端工具，宣称可用提示词与视频素材自动完成短视频的文案生成、语音合成、剪辑与字幕添加。

## 适用场景

- 需要批量制作产品营销或泛内容短视频、且希望使用桌面端本地处理素材的个人或小团队（推断：README 的“关于项目”称其面向产品营销与泛内容短视频，但未列出实际用户案例）
- 需要接入通用 OpenAI 接口格式进行文案生成、并使用 EdgeTTS 语音合成的场景（README 路线图已实现项）
- 需要 Windows/macOS/Linux 多平台使用、开箱即用下载安装包的场景（README 开始使用与多平台支持条目）

## 项目宣称的能力

- README 称集成了 AI 驱动的文案生成、语音合成、视频剪辑、字幕特效等功能（“关于项目-核心功能”）
- 路线图已勾选实现：文案生成兼容通用 OpenAI 接口格式、语音合成支持 EdgeTTS、文案/视频/音频/字幕合成与自动混剪、批量处理、多语言支持、完善使用手册（“路线图”）
- README 宣称完全本地化运行以确保用户数据安全（“核心功能-安全可靠”）
- README 宣称支持批量任务按预设自动持续合成视频（“核心功能-批量处理”）

## 限制与待验证

- README 未提供任何 benchmark、生成质量或性能指标，实际输出质量需自行测试
- 路线图显示字幕特效的多字幕样式与特效、更多语音合成 API、更全面参数调整尚未完成（“路线图”未勾选项）
- README 未说明素材格式、分辨率、时长等具体支持范围，需查阅官方文档或源码验证
- AGPL-3.0 对分发与网络服务使用有传染性约束，商用前需确认许可义务
- 未提供运行环境依赖、硬件要求与已知 issue 说明，需查看 issues 与 release 信息
- 关注原因字段为空，无法推断使用者具体动机

## 什么情况下重新考虑

- 需要批量、自动化地由文案与素材生成短视频，且愿意自行验证输出质量时
- 需要评估 AGPL-3.0 许可是否与自身商业分发或 SaaS 模式兼容时
- 需要了解字幕特效、更多语音合成 API、更全面参数调整等未完成路线图功能是否落地时

## 检索关键词

- 短视频自动剪辑
- AI 文案生成
- 文本转语音
- EdgeTTS
- 桌面端跨平台应用
- 批量视频生成
