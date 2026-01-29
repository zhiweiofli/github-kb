---
description: Update the knowledge base catalog (CLAUDE.md) with new or modified entries
---

# /update-catalog

更新知识库索引文件 CLAUDE.md。

## Usage

```
/update-catalog [repo-name]
```

## Examples

```
/update-catalog                    # 扫描所有仓库，更新整个 catalog
/update-catalog claude-code        # 只更新指定仓库的条目
```

## Workflow

1. 读取当前 CLAUDE.md
2. 扫描 `./github-kb/repos/` 目录
3. 对比现有条目和实际仓库
4. 生成新条目或更新现有条目
5. 保持分类结构

## Catalog Entry Format

```markdown
### [project-name](./repos/project-name)
一句话描述。

- 关键特性
- 技术栈
- 入口命令
```

## Rules

- 保持条目简洁（1-3 行）
- 按类别组织
- 不写长篇说明
- 保持人类可读
