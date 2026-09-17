# Lesson 08 — Revert

## Goal

撤销已提交内容，同时保留历史。

## Exercise

1. Create `practice/revert` from `main`.
2. Add a harmless line and Commit it.
3. Record the Commit ID.
4. Run in PowerShell:

```powershell
git revert --no-edit <commit-id>
```

## Expected history

```text
Revert "Practice: introduce a change to revert"
Practice: introduce a change to revert
original base Commit
```

The final file content matches the base, but the history records both the mistake and correction.

## Important distinction

`Git: Revert Selected Changes` in the editor may apply only to selected uncommitted lines. It is not necessarily Commit Revert.

## When to use

Use Revert for a Commit already shared or retained in meaningful history. Use branch deletion when a disposable experiment branch is entirely unwanted.

## Completion check

The learner can show a clean tree, two additional commits, and no net file difference from the base.
