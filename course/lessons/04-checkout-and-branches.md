# Lesson 04 — Checkout and Branches

## Goal

安全查看旧版本，并建立隔离的实验分支。

## Detached Checkout

Use a historical tag such as `lesson-snapshot-05` and choose `Checkout (Detached)`.

Expected effects:

- files change to that historical tree;
- the status bar no longer shows an ordinary working branch;
- ordinary new work should not begin here.

Return to `main` before continuing.

## Task branch

From `main`, create:

```text
practice/branch-basics
```

A new branch initially points to the same Commit as `main`. It diverges only after a new Commit.

## Rule

```text
view history with detached checkout
perform work on a named branch
```

## Completion check

The learner can return from detached HEAD and can show that edits on a practice branch do not alter `main`.
