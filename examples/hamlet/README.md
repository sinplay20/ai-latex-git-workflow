# Hamlet Git History Example

这是课程的公共练习仓库。它使用 Shakespeare 公版作品 *Hamlet* 的短节选和原创教学说明，不包含任何私人研究材料。

## Included assets

- `hamlet-history-source/`：构建后的参考 Git 仓库；
- `hamlet-history.bundle`：包含完整分支、九个 Commit 和九个 annotated tags；
- `setup-example.ps1`：从 bundle 创建干净的学习工作副本；
- `build-example.py`：可读、可重复运行的示例构建脚本；
- `VERSION-MAP.md`：九个版本的结构和内容演化。

## Create a learner working copy

在 PowerShell 中：

```powershell
Set-Location "H:\Latex\AI-LaTeX-Git-Course\examples\hamlet"
.\setup-example.ps1
```

默认创建：

```text
hamlet-history-work/
```

脚本会移除 bundle 自动生成的 `origin`，使远程课程从无 remote 状态开始。

## Verify

```powershell
Set-Location .\hamlet-history-work
git status --short --branch
git log --graph --oneline --decorate --all --reverse
```

Expected:

```text
branch: main
working tree: clean
tags: lesson-snapshot-01 ... lesson-snapshot-09
```

## Final builds

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build hamlet-reader.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build hamlet-instructor.tex
```

## Rebuild the reference history

This deletes and recreates only the generated example paths. Review the script, then run:

```powershell
python .\build-example.py --force
```
