# Lesson 06 — Discard and Restore

## Goal

按错误所处阶段选择恢复工具。

## Uncommitted change

After inspecting the Diff, `Discard Changes` restores a file to the latest Commit on the current branch. This can permanently remove uncommitted work.

## Staged change

Unstage first if the selection is wrong, then inspect the working-tree Diff before discarding.

## Historical file restore

To recover one file without rolling back the project:

```powershell
git restore --source <tag-or-commit> -- path/to/file.tex
```

This puts historical content into the current working tree as a new uncommitted change. Review and Commit it normally.

## Do not confuse

- Restore changes file content.
- Revert creates a new inverse Commit.
- Reset moves branch/history pointers and is not the default recovery tool.

## Completion check

The learner restores one Hamlet file from an older tag, inspects the resulting Diff, and then either commits or discards it intentionally.
