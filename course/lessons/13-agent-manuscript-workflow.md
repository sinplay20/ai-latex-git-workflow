# Lesson 13 — Agent Manuscript Workflow

## Goal

把 Git 技术转化为可重复的 ChatGPT、OpenCode、Pi 协作流程。

## Before editing

Use `checklists/before-agent-edit.md` and create a task branch for substantial work.

## Prompt contract

Use `templates/ai-edit-request.md`. Specify:

- exact repository and expected branch;
- allowed files and sections;
- mathematical or editorial objective;
- forbidden unrelated changes;
- build command;
- required completion report.

## Tool-specific notes

- OpenCode/Pi should run from the repository root.
- ChatGPT Desktop changes are traceable only after content is actually saved into the repository.
- Do not let two Agents modify the same working tree concurrently.
- Use separate Git worktrees for deliberate parallel work.

## Authority boundary

The Agent may analyze, edit within scope, compile, and report. The learner decides:

- whether a mathematical claim is accepted;
- whether wording is authoritative;
- whether to Commit, Merge, tag, restore, or publish.

## Completion check

The learner performs one scoped Hamlet edit through an Agent and independently verifies every changed file before Commit.
