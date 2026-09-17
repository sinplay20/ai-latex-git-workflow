# Troubleshooting Guide

## Source Control keeps spinning after Commit

Likely cause: Git opened `COMMIT_EDITMSG` and is waiting for the editor to close.

Action:

1. Find the `COMMIT_EDITMSG` tab.
2. Put the Commit message on the first line.
3. Save with `Ctrl+S`.
4. Close the tab with `Ctrl+W`.
5. Do not click Commit repeatedly.

## Graph says there are no changes between an old Commit and main

VS Code Graph comparison can be directional. To inspect changes from old to new:

1. Right-click the newer Commit or branch.
2. Choose `Compare with...`.
3. Select the older tag.

If the old Commit is selected as the comparison head, the merge-base view may report no unique changes.

## `M` appears beside a file

- Under a historical Commit: the file was modified by that Commit.
- Under current `Changes`: the working file has uncommitted modifications.

## Commit was made on the wrong branch

Stop. Do not reset immediately. Record:

```powershell
git status --short --branch
git log -5 --oneline --decorate
```

If the Commit has not been pushed, create or move an appropriate branch only after explaining the exact state. If shared, prefer Revert.

## Cannot delete a branch

Git does not delete the currently checked-out branch. Switch to `main` first. If Git warns that the branch is unmerged, verify that it is an intentionally disposable practice branch before force deletion.

## Revert command absent from VS Code

Do not use `Revert Selected Changes`; that command usually applies to selected uncommitted Diff lines. In PowerShell use:

```powershell
git revert --no-edit <commit-id>
```

## Wrong folder opened

Check:

```powershell
Get-Location
git rev-parse --show-toplevel
```

Never initialize Git in a system directory or an unintended parent folder.

## PDF figure is ignored

A broad rule such as `*.pdf` also ignores source figures. Prefer output-specific rules such as:

```gitignore
/build/
/manuscript.pdf
```

## Remote visibility is uncertain

Do not push additional content. Open the hosting service and explicitly verify that the repository visibility is Private.
