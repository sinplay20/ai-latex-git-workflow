# Lesson 00 — Clone the Course and Prepare the Sandbox

## Goal

把本课程仓库 clone 到本地，在 VS Code 中确认其状态，并从 bundle 创建独立 Hamlet 学习仓库。

## Step 1: Clone this repository

Clone the confirmed public GitHub repository:

```powershell
git clone https://github.com/sinplay20/ai-latex-git-workflow.git
Set-Location .\ai-latex-git-workflow
code .
```

The repository is public. Do not substitute a different URL or destination without learner confirmation.

## Step 2: Verify the course repository

In VS Code, confirm:

```text
repository root: ai-latex-git-workflow
branch: main
working tree: clean
```

Read-only diagnostics:

```powershell
Get-Location
git rev-parse --show-toplevel
git status --short --branch
```

## Step 3: Load the teaching instructions

The Agent must read:

```text
AGENTS.md
README.md
course/COURSE.md
course/instructor/AGENT-INSTRUCTOR-PROTOCOL.md
this lesson
```

The learner confirms that all state-changing exercises will use Hamlet rather than a real manuscript.

## Step 4: Create the Hamlet learner repository

From the course root:

```powershell
Set-Location .\examples\hamlet
.\setup-example.ps1
Set-Location .\hamlet-history-work
code .
```

The setup script clones `hamlet-history.bundle`, switches to `main`, and removes the bundle remote so remote lessons begin from a clean state.

## Step 5: Verify the sandbox

```powershell
git status --short --branch
git rev-list --count main
git tag --list
```

Expected:

```text
branch: main
working tree: clean
commits: 9
tags: lesson-snapshot-01 through lesson-snapshot-09
remote: none
```

## Safety agreement

Before continuing, the learner confirms:

- no real manuscript will be used for exercises;
- destructive commands are outside the basic workflow;
- remote publication requires explicit Private visibility confirmation;
- Git files and Commit history, not chat transcripts, are authoritative.

## Completion check

The learner can identify both the course repository and the separate Hamlet repository, and can explain why exercises occur only in the latter.
