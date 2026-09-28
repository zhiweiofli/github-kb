---
status: "indexed"
source: "https://github.com/vernesong/OpenClash"
repository: "vernesong/OpenClash"
summary: "面向 OpenWrt 路由器的 Mihomo(Clash) 图形化客户端插件，用 LuCI 界面管理多协议代理与规则分流。"
topics: ["OpenWrt", "LuCI", "Clash", "Mihomo", "透明代理", "规则分流"]
assessment: "not-tested"
---

# vernesong/OpenClash

- GitHub: https://github.com/vernesong/OpenClash
- Local: not cloned
- Status: LATER（初评，未试用）
- 来源 Issue: https://github.com/zhiweiofli/github-kb/issues/12
- 评估日期: 2026-09-28
- 模型: deepseek-flash
- README blob: 39519390eb874d29bb9247e452f9d0b6c0914df2；输入截断: False
- License: MIT

## 我关注的原因

未提供，不推测个人偏好

## 一句话说明

面向 OpenWrt 路由器的 Mihomo(Clash) 图形化客户端插件，用 LuCI 界面管理多协议代理与规则分流。

## 适用场景

- 在 OpenWrt 路由器上做全屋流量分流代理，需自行准备订阅/节点与规则配置
- 通过 LuCI 图形界面管理代理内核，适合不想直接用命令行的 OpenWrt 用户（推断）
- 自定义固件编译集成：将 luci-app-openclash 放入 OpenWrt 源码 Package 目录随固件编译
- 需要在路由器侧使用 TUN 模式或 TProxy 透明代理的场景（README 依赖列出 kmod-tun、iptables-mod-tproxy、kmod-nft-tproxy）

## 项目宣称的能力

- README 宣称兼容 Shadowsocks、ShadowsocksR、Vmess、Trojan、Snell 等协议
- README 宣称可根据灵活的规则配置实现策略代理
- README 说明可运行在 OpenWrt 上并基于 Mihomo(Clash) 内核
- README 提供 Wiki 使用手册与 IPK/APK 下载地址
- README 列出完整依赖清单，便于提前核对固件环境
- README 声明采用 MIT License，并注明代码基于 Luci For Clash

## 限制与待验证

- README 未提供性能、稳定性或 benchmark 数据
- 依赖列表较长（luci、dnsmasq-full、bash、ruby、ipset、iptables/nftables 相关模块等），对固件版本与架构有要求，需验证目标设备是否满足
- 仅提供 OpenWrt 场景，非 OpenWrt 环境不适用
- README 未说明支持的 OpenWrt 版本范围，需查 releases 与 Wiki 确认
- README 提到的编译方式示例基于较旧的 chaos_calmer 15.05.1 SDK，实际可用性需验证
- 内核为外部项目 Mihomo，插件本身不包含内核能力，实际代理效果与内核版本相关
- 未提供用户关注原因，无法判断社区采纳动机与使用反馈

## 什么情况下重新考虑

- 需要在 OpenWrt 路由器上部署图形化 Clash/Mihomo 代理时
- 目标固件缺少某个依赖模块、需确认兼容性时
- 需要 TUN/TProxy 透明代理或多协议分流方案时
- 需要把该插件集成进自编译固件时

## 检索关键词

- OpenWrt
- LuCI
- Clash
- Mihomo
- 透明代理
- 规则分流
