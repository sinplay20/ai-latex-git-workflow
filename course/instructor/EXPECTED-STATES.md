# Expected Repository States

Use this file to verify lesson outcomes in the Hamlet example.

## Fresh example

```text
branch: main
working tree: clean
HEAD tag: lesson-snapshot-09
history: nine milestone commits
remote: none
```

## After branch creation

```text
current branch: practice/<task>
working tree: clean
practice branch and main initially point to the same Commit
```

## After editing but before Stage

```text
working tree: modified
file appears under Changes with M
index: unchanged
```

## After Stage

```text
file appears under Staged Changes
working-tree Diff may be empty
cached Diff contains the intended edit
```

## After Commit

```text
current branch advances by one Commit
working tree: clean
main remains at its previous Commit
```

## After fast-forward Merge into a practice base

```text
receiving branch advances to the source branch Commit
working tree: clean
no merge Commit is created
```

## After Revert

```text
original error Commit remains in history
new Revert Commit follows it
net file content matches the pre-error state
working tree: clean
```

## After Detached Checkout

```text
HEAD is detached at a tag or Commit
files match that historical tree
learner must return to main before ordinary work
```

## Before remote publication

```text
working tree: clean
current branch: main
remote URL reviewed
visibility: explicitly confirmed Private
credentials/secrets scan: passed
```
