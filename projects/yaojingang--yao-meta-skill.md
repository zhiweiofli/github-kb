---
status: "indexed"
source: "https://github.com/yaojingang/yao-meta-skill"
repository: "yaojingang/yao-meta-skill"
summary: "把重复性工作流转化为可跨平台打包、评估与治理的复用型 agent skill 包，并提供技能生命周期（IR、编译器、评估、发布门禁、运营）工具链。"
topics: ["agent skill 工程化", "skill 打包与跨平台适配", "skill 评估与触发测试", "skill 生命周期治理", "Skill IR 中间表示", "治理门禁与发布证据"]
assessment: "not-tested"
---

# yaojingang/yao-meta-skill

- GitHub: https://github.com/yaojingang/yao-meta-skill
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/6
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 26531d7064fea5bfedf989cafa0aa880cbd4067f；输入截断: True
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

把重复性工作流转化为可跨平台打包、评估与治理的复用型 agent skill 包，并提供技能生命周期（IR、编译器、评估、发布门禁、运营）工具链。

## 适用场景

- 将反复出现的 workflow/prompt/transcript/runbook 整理为可安装、可读、跨平台的 skill 包（README『2.0 Use Cases』宣称，需按实际输入验证）
- 把个人 skill 升级为团队资产：加入接口契约、manifest、target adapter、trust 检查、output eval 与发布证据（README 宣称）
- 发布前跑包验证、安装模拟、兼容性检查、运行时权限探测与证据一致性检查（README 宣称，需本地执行确认）
- 发布后用量采纳漂移、反馈日志、SkillOps 周报判断下一步是文档、eval、修补还是治理更新（README 宣称）
- 需要显式边界、触发评估、治理与可移植性的团队级复用能力包（推断，基于 README 定位）
- 作为与 Anthropic/OpenAI 式对话创建流程并用的加固/打包环节（README 宣称的混合模式）

## 项目宣称的能力

- Skill OS 2.0 引入 Skill IR（平台中立的意图/触发/输入输出/边界/引用/产物中间表示）与 target compilers/adapters（章节 Skill OS 2.0 Upgrade）
- Output Eval Lab：触发检查、输出断言、执行/耗时/token 证据、盲评包与裁定报告（章节 Capability Surface）
- Review Studio 2.0：单页 HTML 门禁汇总意图、触发、输出 eval、上下文成本、运行时、信任、漂移、豁免与发布证据（章节 Capability Surface）
- 发布治理：证据一致性检查、包验证、安装模拟、运行时权限探测、公开声明守门（章节 Skill OS 2.0 Upgrade / Evidence and release governance）
- 可移植性：为 OpenAI、Claude、generic、Agent Skills、VS Code 等目标生成适配面并附带兼容性记录（章节 Skill OS 2.0 Upgrade）
- 默认流程内置治理、晋升与可移植性检查，且提供统一 CLI scripts/yao.py 与 make test/ci-test（章节 Quick Start、5-Minute Workflow）

## 限制与待验证

- README 自评加权质量分 91.5/100 及对 Anthropic/OpenAI Skill Creator 的对比评分属项目自身方法学，非独立第三方基准
- 单评审人盲评 5/5 属单人偏好证据，README 自述非 provider 独立模型执行证据且逐案理由为空
- README 自述当前仅为 beta 与外部测试就绪，provider 后端生产证据、人工盲评证据、原生权限执行、真实客户端 telemetry 仍为待办证据任务
- 运行时权限探测报告显示 0 个原生强制适配器、4 个元数据回退并附带残余风险，权限约束未被原生强制
- 上下文预算接近上限（root 944/1000），Onboarding/Review 自评 6.5 为最弱维度，首次创建与评审摩擦仍高
- README 被截断（readme_truncated 为 true），命令清单、文档与许可之外的维护承诺、依赖与兼容细节需查仓库原文与 CI 配置确认

## 什么情况下重新考虑

- 需要把团队内反复出现的 workflow 固化为可安装、可评审、可治理的 skill 包时
- 需要同一语义契约向多个 agent 客户端（OpenAI/Claude/generic/VS Code）导出并保持语义一致时
- 需要为 skill 引入触发评估、输出断言、发布门禁与证据账本以支撑他人依赖时
- 需要用量采纳漂移与维护队列来决定下一步文档/eval/修补/治理动作时
- 当项目补齐 provider 与人工外部证据、原生权限执行与真实客户端 telemetry 后，可重新评估其世界级声明

## 检索关键词

- agent skill 工程化
- skill 打包与跨平台适配
- skill 评估与触发测试
- skill 生命周期治理
- Skill IR 中间表示
- 治理门禁与发布证据
