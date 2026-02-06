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
- 索引条目链接有效 ✓

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
index_file: INDEX.md
focus_file: FOCUS.md
memory_file: MEMORY.md
```

---

## Available Commands

| 命令 | 用途 |
|------|------|
| `/search-github <query>` | 搜索 GitHub 仓库、Issues、PRs |
| `/clone-repo <owner/repo>` | 克隆仓库到本地知识库 |
| `/update-index [repo]` | 更新 INDEX.md（repo 索引） |

---

## Workflow: Discover → Acquire → Retrieve → Index

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

### 4. INDEX (索引维护)

#### Repo 索引（结构化条目）
更新 [`INDEX.md`](./INDEX.md)，条目模板：

```markdown
### [project-name](./repos/project-name)
- Category: <category>
- Status: LATER
- Why: <why-you-care>
- Notes: <one-or-two-notes>
- 最后讨论时间：YYYY年M月D日
```

#### 短期关注（以主题为中心）
更新 [`FOCUS.md`](./FOCUS.md) 的 NOW/NEXT 与两个主题的下一步。

#### 长期记忆（结论沉淀）
更新 [`MEMORY.md`](./MEMORY.md) 的 takeaways / patterns / gotchas / decisions。

---

## Index Entry Points

- 结构化 repo 索引：[`INDEX.md`](./INDEX.md)
- 短期主题看板：[`FOCUS.md`](./FOCUS.md)
- 长期结论沉淀：[`MEMORY.md`](./MEMORY.md)

---

*Managed by github-kb skill | AIE Workspace*
