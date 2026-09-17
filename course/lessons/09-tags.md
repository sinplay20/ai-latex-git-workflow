# Lesson 09 — Tags

## Goal

使用稳定名称标记导师稿、投稿稿和接受稿。

## Branch versus tag

- Branch moves when new work is committed.
- An annotated tag remains attached to the chosen milestone.

## Suggested manuscript tags

```text
advisor-draft-01
submission-v1
revision-v1
accepted-version
```

## Exercise

Create an annotated practice tag on a Hamlet milestone:

```powershell
git tag -a practice-release -m "Practice classroom release"
```

Inspect it:

```powershell
git show practice-release --no-patch
```

Delete only the practice tag after verification:

```powershell
git tag -d practice-release
```

## Remote note

Pushing a branch does not always push tags. Tags may require a separate `Git: Push Tags` or:

```powershell
git push origin --tags
```

## Completion check

The learner explains why a tag is better than a filename such as `final-final.tex` for a milestone.
