# Course Map

## Audience

研究人员、研究生和使用 AI Agent 编辑 LaTeX 的作者。课程不假设已有 Git 经验。

## Learning model

课程采用“解释—操作—观察—确认”的循环。每课只在 Hamlet 示例中改变状态，学习者确认后再进入下一步。

## Module A — Foundations

| Lesson | Topic | Outcome |
|---|---|---|
| 00 | Clone and orientation | Clone 课程仓库、建立安全边界并准备 Hamlet 示例 |
| 01 | Git mental model | 区分文件、stage、Commit、branch、tag、remote |
| 02 | VS Code Source Control | 识别仓库、分支和变化状态 |
| 03 | History and Diff | 比较版本并阅读文件级修改 |

## Module B — Daily manuscript work

| Lesson | Topic | Outcome |
|---|---|---|
| 04 | Checkout and branches | 安全查看旧版本并创建实验分支 |
| 05 | Stage and Commit | 创建可解释的版本节点 |
| 06 | Discard and Restore | 按修改阶段选择正确恢复方法 |
| 07 | Review and Merge | 审核 Agent 分支并合并批准内容 |
| 08 | Revert | 不改写历史地撤销已提交错误 |
| 09 | Tags | 标记导师稿、投稿稿和接受稿 |

## Module C — Backup and collaboration

| Lesson | Topic | Outcome |
|---|---|---|
| 10 | Private remotes | 安全建立远程备份 |
| 11 | Push, Fetch, Pull | 理解本地与远程同步 |
| 12 | Merge conflicts | 在 VS Code 中解决受控冲突 |

## Module D — AI and LaTeX practice

| Lesson | Topic | Outcome |
|---|---|---|
| 13 | Agent manuscript workflow | 约束 Agent、审查改动并保留决定权 |
| 14 | Reproducible LaTeX | 追踪完整源文件并隔离生成物 |

## Recommended sequence

按 00–14 顺序学习。已有 Git 经验的学习者可以通过 Lesson 00 的诊断跳过基础课，但必须完成安全规则确认。

## Completion criteria

学习者应能独立完成：

```text
create task branch
→ ask an Agent to edit scoped LaTeX files
→ inspect all changes
→ compile
→ stage and commit
→ compare with main
→ merge or discard
→ push to a confirmed private remote
```

并能说明：

- 为什么聊天历史不能替代 Git；
- 为什么 PDF 通常不是日常 Diff 的主体；
- Discard、Restore、Revert 和 Reset 的差别；
- 为什么 AI 修改必须在明确的仓库和分支中进行。
