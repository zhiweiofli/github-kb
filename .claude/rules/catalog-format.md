# Catalog Format Rules

知识库索引文件 (CLAUDE.md) 的格式规范。

## Structure

```markdown
# GitHub Knowledge Base

简短描述本知识库的用途和范围。

---

## Category Name

### [project-name](./repos/project-name)
一句话描述。

可选备注（1-2 行）。
```

## Rules

### 1. 分类组织

- 按领域/用途分类，不按语言或技术
- 分类名称简洁明确
- 相关项目放在同一分类下

### 2. 条目格式

每个条目必须包含：

| 元素 | 要求 |
|------|------|
| 标题链接 | `### [name](./repos/name)` |
| 描述 | 一句话，说明项目做什么 |
| 备注 | 可选，关键特性或使用提示 |

### 3. 内容规范

**DO**:
- 保持简洁，便于扫描
- 使用一致的描述风格
- 提供相对路径链接

**DON'T**:
- 写长篇介绍
- 复制 README 内容
- 包含安装步骤

### 4. 更新规则

- 新仓库克隆后必须添加条目
- 删除仓库后必须移除条目
- 定期检查链接有效性

## Example

```markdown
## AI & LLM Tools

### [claude-code](./repos/claude-code)
Anthropic 官方 CLI，用于 AI 辅助编程。

- 支持多种模型（Opus/Sonnet/Haiku）
- 内置工具系统（Read/Edit/Bash 等）

### [langchain](./repos/langchain)
LLM 应用开发框架，提供链式调用和 Agent 能力。

## MCP Servers

### [mcp-server-github](./repos/mcp-server-github)
GitHub API 的 MCP 服务器封装。
```
