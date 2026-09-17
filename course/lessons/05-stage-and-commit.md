# Lesson 05 — Stage and Commit

## Goal

从一个可审查的修改创建清晰 Commit。

## Exercise

On a practice branch, add a harmless editorial note to a Hamlet source file.

Workflow:

```text
save
→ inspect Diff
→ Stage the intended file
→ write a focused Commit message
→ Commit
```

Suggested message:

```text
Practice: clarify the scene introduction
```

## COMMIT_EDITMSG

If Source Control keeps spinning, Git may be waiting for the commit-message editor:

1. open `COMMIT_EDITMSG`;
2. write the message on the first line;
3. save;
4. close the tab.

## Commit quality

A good Commit should be:

- coherent;
- reviewable;
- compilable when relevant;
- described by an action-oriented message.

## Completion check

The practice branch advances by one Commit, `main` does not move, and the working tree is clean.
