# AI 辅助 LaTeX 与 Git 工作流

> 仓库名称：`ai-latex-git-workflow`

这是一个面向研究人员、研究生和 AI Agent 使用者的中文实践仓库：通过 **VS Code + Git + 模块化 LaTeX** 管理 ChatGPT、OpenCode、Pi 等 Agent 参与修改的论文。

当前版本以普通 Markdown、`AGENTS.md`、Prompt、可复现 Git 示例和单篇论文模板为核心，**暂不实现 Agent Skill 或自动 Commit 工具**。

## 1. 目的

本项目解决以下问题：

- AI 修改论文后，很难知道具体改了哪些位置；
- 通过 `final-v2.tex`、`final-final.tex` 保存版本，历史混乱；
- ChatGPT、OpenCode、Pi 的聊天记录彼此独立，不能作为统一版本依据；
- PDF 难以逐行比较；
- Agent 可能修改无关内容、重新排版全文或创建大量副本；
- 未发表论文需要本地历史、私人远程备份和明确的人类审批流程。

推荐流程：

```text
main 上存在可靠 Commit
→ 创建任务分支
→ Agent 只修改明确范围
→ VS Code 审查全部 Diff
→ 编译并检查 PDF
→ 在任务分支 Commit
→ 与 main 比较
→ 人工批准后 Merge，或删除分支
```

Git 文件和 Commit 是权威记录；聊天历史只作为辅助上下文。

## 2. Lesson 0：Clone 本仓库并开始课程

首先把 public 仓库 clone 到本地：

```powershell
git clone https://github.com/sinplay20/ai-latex-git-workflow.git
Set-Location .\ai-latex-git-workflow
code .
```

在 VS Code 中确认：

- 打开的是整个仓库目录；
- 左下角显示 `main`；
- Source Control 的 `Changes` 为空。

然后让 Agent 读取教学规则：

```text
请先完整读取根目录 AGENTS.md、course/COURSE.md、
course/instructor/AGENT-INSTRUCTOR-PROTOCOL.md 和
course/lessons/00-course-orientation.md。
从 Lesson 0 开始，一次只给我一个可验证步骤。
所有 Git 写操作只在 Hamlet 示例中练习，不要修改真实论文。
```

创建 Hamlet 学习仓库：

```powershell
Set-Location .\examples\hamlet
.\setup-example.ps1
Set-Location .\hamlet-history-work
code .
```

预期状态：

```text
branch: main
working tree: clean
commits: 9
tags: lesson-snapshot-01 ... lesson-snapshot-09
remote: none
```

## 3. 课程体系

课程地图位于 [`course/COURSE.md`](course/COURSE.md)。

### Module A — Foundations

- Git mental model；
- VS Code Source Control；
- Graph、Commit、tag；
- 文件级 Diff 与 Timeline。

### Module B — Daily manuscript work

- Checkout 与 branch；
- Stage 与 Commit；
- Discard 与 Restore；
- Review 与 Merge；
- Revert；
- milestone tags。

### Module C — Backup and collaboration

- Private Remote；
- Push、Fetch、Pull；
- Merge Conflict；
- 多设备与多人协作。

### Module D — Agent and LaTeX workflow

- `AGENTS.md`；
- 限定 Agent 修改范围；
- 人工审核权；
- 模块化 LaTeX；
- full/submit wrappers；
- 可复现构建。

## 4. 未来发展

当前阶段优先验证教学方法和人工可控工作流。未来可以逐步增加：

1. **Agent Skill**：自动选择课程、检查当前步骤并加载对应材料；
2. **只读诊断工具**：统一报告仓库根目录、branch、status、remote 和 LaTeX build 状态；
3. **安全 Git Tool/MCP**：封装 status、diff、checkpoint 和 branch 操作，并对破坏性动作要求确认；
4. **VS Code 扩展**：提供“开始任务”“审查 AI 修改”“批准版本”“恢复文件”等按钮；
5. **课程状态文件**：经学习者授权后记录学习进度；
6. **CI 构建**：在 GitHub Actions 中验证 reader/submit PDF；
7. **latexdiff 集成**：生成面向合作者或审稿人的可视化差异 PDF；
8. **多 Agent worktree 支持**：让不同 Agent 在隔离工作树中并行处理不同章节。

自动化的目标不是替代作者决策，而是减少重复操作并提高可审计性。

## 5. 推荐“分布式”写 LaTeX

这里的“分布式”主要指 **模块化、分文件写作**，不是让多个 Agent 同时修改同一个工作目录。

推荐结构：

```text
paper.tex
paper-working.tex
paper-submit.tex
sections/
  01_introduction.tex
  02_preliminaries.tex
  03_main_results.tex
  04_proofs.tex
  05_discussion.tex
appendices/
figures/
references.bib
```

优点：

- Diff 更集中；
- Agent 可以被限制在单个 section；
- 降低全文重排造成的噪声；
- working 和 submission 共用同一权威源文件；
- 更容易定位冲突；
- 允许未来通过 Git worktree 安全并行。

不推荐：

```text
main-v2.tex
main-new.tex
final.tex
final-final.tex
```

不同历史状态应由 Commit 和 tag 表示，而不是文件名。

## 6. 推荐加入项目 `AGENTS.md` 的 Prompt

完整模板位于 [`template/single-paper/AGENTS.md`](template/single-paper/AGENTS.md)。最小版本如下：

```markdown
# Manuscript Agent Rules

- `paper.tex` is the canonical shared source.
- Edit only the files and sections explicitly named by the user.
- Do not create versioned copies such as `v2`, `new`, or `final-final`.
- Preserve labels, citations, theorem environments, notation, and semantic line breaks.
- Do not rewrap unrelated prose.
- Ask before creating, deleting, renaming, or moving source files.
- Put generated output under `build/`.
- Do not Commit, Merge, Revert, Reset, Clean, Push, or modify tags/branches without explicit authorization.
- After editing, report every changed file, mathematical changes, editorial changes, build results, and unresolved questions.
```

推荐的任务 Prompt：

```text
请先读取 AGENTS.md 和相关 LaTeX 文件。
只修改我明确指定的文件与章节。
不要创建版本副本，不要执行 Git 写操作。
保持 labels、citations、notation 和现有 semantic line breaks。
完成后列出全部文件变化，分别总结数学与文字修改，并运行约定的 LaTeX build。
```

## 7. 仓库内容

```text
course/                     课程、教学协议、检查清单和 Prompt 模板
examples/hamlet/            九版本公版 Hamlet 示例及 Git bundle
template/single-paper/      可直接复制的单篇论文模板
AGENTS.md                   本仓库的 Agent 使用规范
ROADMAP.md                  后续开发路线
```

## 8. Hamlet 示例

Hamlet 示例包含九个 Commit 和九个 annotated tags，覆盖：

- 普通文本修改；
- 文件新增和删除；
- 单文件拆分；
- 目录和文件重命名；
- 多文件同步修改；
- reader/instructor wrappers；
- 最终课堂版。

详见 [`examples/hamlet/VERSION-MAP.md`](examples/hamlet/VERSION-MAP.md)。

## 9. 单篇论文模板

复制：

```text
template/single-paper/
```

或者使用独立模板目录：

```text
H:\AI-LaTeX-Single-Paper-Template
```

模板已经过 working 和 submission 两种实际编译验证。

## 10. 隐私、可见性与许可证

- 目标 GitHub 仓库已确认为 Public；
- 本仓库不包含私人研究论文；
- Hamlet 文本为公版短节选；
- 上传真实论文前必须另建并确认 Private 的远程仓库；
- 不要提交 API key、OAuth token、密码或其他凭据；
- 本项目当前不附带开源许可证，许可证将在以后单独决定。
