# Lesson 02 — VS Code Source Control

## Goal

通过图形界面识别仓库和当前变化。

## Interface

Open the repository folder, then use:

```text
Ctrl+Shift+G
```

Identify:

- repository name;
- branch indicator in the lower-left status bar;
- Changes;
- Staged Changes;
- Source Control Graph.

## Status letters

| Letter | Meaning |
|---|---|
| M | Modified |
| A | Added |
| D | Deleted |
| R | Renamed |
| U | Untracked |

A letter under a historical Commit describes that Commit. The same letter under current Changes describes uncommitted work.

## Exercise

Open `manuscript/sections/01_context.tex`, add a harmless comment on a practice branch, save it, inspect `M`, and then discard it after verifying the Diff.

## Completion check

The learner can distinguish historical status from current uncommitted status.
