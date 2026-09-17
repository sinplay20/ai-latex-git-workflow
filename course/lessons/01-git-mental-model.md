# Lesson 01 — Git Mental Model

## Goal

区分 Git 的六个层次：工作文件、stage、Commit、branch、tag、remote。

## Model

```text
working files → stage/index → Commit
                              ↑
                           branch
                              ↑
                             tag

local repository ↔ remote repository
```

## Key distinctions

- Saving a file is not a Commit.
- Staging selects content for the next Commit.
- A Commit is a local snapshot with parents and metadata.
- A branch is a movable name pointing to a Commit.
- A tag is normally a stable milestone name.
- Push transfers local history to a remote; Commit does not upload anything.

## Exercise

In VS Code, identify:

1. current branch `main`;
2. latest tag `lesson-snapshot-09`;
3. nine history commits;
4. absence of current Changes.

## Completion check

The learner explains where a Commit is stored and why Git does not ask for a remote when committing.
