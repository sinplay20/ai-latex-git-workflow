# Lesson 07 — Review and Merge

## Goal

审核 Agent 分支，并把批准的内容合并到接收分支。

## Review sequence

1. Confirm both branches and clean status.
2. Right-click the newer Agent branch Commit.
3. Compare with the receiving branch.
4. Review every changed file.
5. Compile the intended wrapper.
6. Approve or reject explicitly.

## Merge sequence

```text
checkout receiving branch
→ Git: Merge Branch...
→ select Agent branch
→ verify result
```

The receiving branch is the branch that moves.

## Fast-forward

If the receiving branch has not changed since the Agent branch was created, Git may fast-forward without creating a merge Commit.

## Rejection

If the entire experiment is unwanted and isolated on its own branch, return to the receiving branch and delete the experiment branch after confirmation.

## Completion check

The learner explains which branch must be checked out before Merge and verifies that the working tree is clean afterward.
