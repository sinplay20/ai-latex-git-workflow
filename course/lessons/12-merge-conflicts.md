# Lesson 12 — Merge Conflicts

## Goal

在受控 Hamlet 文件中识别并解决冲突。

## Setup

Create two branches from the same base and edit the same sentence differently. Commit both changes, then merge one into the other.

## Conflict markers

```text
<<<<<<< HEAD
current branch content
=======
incoming branch content
>>>>>>> other-branch
```

VS Code may offer:

```text
Accept Current
Accept Incoming
Accept Both
Compare Changes
```

For mathematical writing, never choose automatically without reading the full surrounding argument.

## Resolution sequence

1. Read both versions and surrounding text.
2. Decide the correct combined content.
3. Remove all conflict markers.
4. Save and compile.
5. Stage the resolved file.
6. Complete the merge Commit.

## Abort option

If the merge should not proceed and no resolution work must be kept:

```powershell
git merge --abort
```

Use only after confirming that a merge is in progress.

## Completion check

The learner resolves one controlled conflict and explains which branch supplied each competing change.
