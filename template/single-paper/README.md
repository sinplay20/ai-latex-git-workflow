# Single-Paper LaTeX and Git Template

这是一个面向单篇学术论文的模块化 LaTeX 模板。它适合通过 VS Code、Git 和 AI Agent 协作，但不包含自动 Commit、后台 watcher 或 Skill。

## Structure

```text
paper.tex                 canonical shared source
paper-working.tex         working build with internal appendix
paper-submit.tex          submission build
sections/                 article sections
appendices/               working-only material
figures/                  source figures
references.bib            bibliography
AGENTS.md                  project rules for Agents
prompts/                   reusable edit request
checklists/                human review checklist
.vscode/                   compile tasks
build/                     generated output; ignored by Git
```

## First use

1. Copy this directory and rename the copy for the paper.
2. Open the copied folder in VS Code.
3. Review and replace all bracketed placeholders.
4. Open Source Control with `Ctrl+Shift+G`.
5. Choose `Initialize Repository`.
6. Stage the source files and create `Initial manuscript structure`.
7. Keep one canonical source tree; do not create `v2` or `final-final` copies.

## Build

Working version:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper-working.tex
```

Submission version:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper-submit.tex
```

VS Code users can run `Tasks: Run Task` and choose `LaTeX: Build Working` or `LaTeX: Build Submission`.

## Recommended Agent workflow

```text
clean main
→ create task branch
→ give Agent a scoped request from prompts/ai-edit-request.md
→ inspect every Diff
→ compile both relevant outputs
→ Commit on task branch
→ compare with main
→ merge only after human approval
```

## PDF policy

Daily PDFs belong under `build/` and are not tracked. PDF figures under `figures/` are source assets and may be tracked. Do not use a blanket `*.pdf` ignore rule.

## Before publication

- replace author metadata;
- choose and add a license if this template or derivative repository will be public;
- confirm remote repository visibility;
- remove internal notes from the submission build;
- perform a clean build from tracked source only.
