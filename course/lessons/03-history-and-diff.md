# Lesson 03 — History and Diff

## Goal

比较版本，并阅读具体文件和单词的变化。

## Graph comparison

VS Code Graph comparison is directional. To inspect changes from an older version to a newer version:

1. Right-click the newer Commit or branch.
2. Choose `Compare with...`.
3. Select the older tag.

## Suggested comparisons

```text
lesson-snapshot-08 → lesson-snapshot-09
lesson-snapshot-04 → lesson-snapshot-05
lesson-snapshot-01 → lesson-snapshot-09
```

The second comparison demonstrates a monolithic-to-split source restructuring.

## Diff reading

- Left: older content.
- Right: newer content.
- Red: removed or replaced.
- Green: added or replaced.
- Word-level highlighting: changed fragments within a line.

Use the Diff Editor arrows to jump among changes.

## Timeline

Open a current file and expand Timeline to see commits that touched that path. Timeline may not follow content across a major file split automatically.

## Completion check

The learner can explain why a large structural Commit may show additions, deletions, and renames simultaneously.
