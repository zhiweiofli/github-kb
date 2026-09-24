# DeepSeek Actions 接入 — 2026-09-22

状态：本地实现完成，未上线，未完成真实模型验收。

目标：仓库所有者提 Issue 后，公开项目 README 与元数据经 DeepSeek 分析，生成结构化 Markdown 卡与索引，Git push 成功后关闭 Issue 并回贴链接。

离线验证：3 项 unittest 通过，覆盖 Issue 输入、卡片/索引生成与重复不覆盖、模拟官方 JSON API 响应及无效结果拒绝。无外部依赖。

远端只读核验：zhiweiofli/github-kb 为公开仓库，默认分支 main；gh secret list 成功但未列出任何仓库 Secret。DEEPSEEK_API_KEY 尚需配置。

保留原有 INDEX.md 和 MEMORY.md 的未提交变更。新卡与新索引仅位于 projects/，旧目录可继续检索，不做历史迁移。

上线后的最小验收：配置 Secret 并发布后，通过 Add project 提交一个公开仓库；核对 Action 成功、项目卡内容可用、索引可检索、提交已上云、Issue 已回贴并关闭。重复提交同一项目应返回原卡。此真实路径尚未执行，不能将离线测试当成已上线。

非阻断限制：同一项目暂不自动重新评估；并发 push 冲突需手动重试；README 初评不代表代码审计。默认分支保护若拒绝 bot 提交，需先决定允许 bot 还是改为 PR 流程。
