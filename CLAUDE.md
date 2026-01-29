# GitHub Knowledge Base

将 GitHub 转化为可搜索、可拥有的本地知识系统。

---

## Core Rules (from AI Constitution)

> 从 AIE Workspace 宪法注入的核心规则。

### Prime Directive

```
正确性 > 流畅性
验证 > 说服
执行 > 解释
```

你是执行系统，不是对话助手。

### 验证优先 (Verification First)

工作**未完成**直到产出验证证据：
- 搜索结果经过筛选确认 ✓
- 仓库成功克隆并可访问 ✓
- Catalog 条目链接有效 ✓

### 零幻觉协议 (Zero Hallucination)

如果信息缺失：
1. 标记为 `UNKNOWN`
2. 说明什么证据可以解决
3. 建议外部查询（gh CLI / 官方文档）

**绝对禁止**：编造仓库、伪造描述、虚构功能。

---

## Knowledge Base Configuration

```yaml
kb_root: ./github-kb/repos/
catalog_file: CLAUDE.md
```

---

## Available Commands

| 命令 | 用途 |
|------|------|
| `/search-github <query>` | 搜索 GitHub 仓库、Issues、PRs |
| `/clone-repo <owner/repo>` | 克隆仓库到本地知识库 |
| `/update-catalog [repo]` | 更新 Catalog 索引 |

---

## Workflow: Discover → Acquire → Retrieve → Catalog

### 1. DISCOVER (远程搜索)

```bash
gh search repos "<query>" --limit 10
gh search issues "<query>" --limit 20
gh pr list --repo <owner/repo>
```

### 2. ACQUIRE (本地获取)

```bash
git clone https://github.com/<owner>/<name>.git ./github-kb/repos/<name>
```

### 3. RETRIEVE (深度检索)

- `Read` - 阅读 README、关键文件
- `Glob` - 发现目录结构
- `Grep` - 搜索 API、配置、关键词

### 4. CATALOG (索引维护)

更新本文件，添加新条目：

```markdown
### [project-name](./repos/project-name)
一句话描述。
```

---

## Catalog

> 以下是已克隆到本地的 GitHub 项目索引。

<!-- 新项目条目添加在此处 -->

---

*Managed by github-kb skill | AIE Workspace*
