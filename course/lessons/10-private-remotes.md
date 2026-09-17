# Lesson 10 — Private Remotes

## Goal

建立不公开未发表论文的远程备份。

## Concepts

```text
Commit = local history
Push = transfer history to remote
origin = conventional remote name
origin/main = remote-tracking reference
```

## Safe learning order

1. Practice with a local bare remote.
2. Inspect `git remote -v`.
3. Push and clone locally.
4. Only then connect a hosting service.

## Hosting checklist

Before uploading research material:

- visibility explicitly says Private;
- repository owner and collaborators are correct;
- no credentials or unrelated private files are tracked;
- remote URL is correct;
- branch and tags to upload are understood.

## Local bare-remote exercise

Create a disposable bare repository outside the working tree:

```powershell
git init --bare ..\hamlet-remote.git
git remote add origin ..\hamlet-remote.git
git push -u origin main
git push origin --tags
```

The instructor must adapt paths and verify that no existing `origin` will be overwritten.

## Completion check

The learner distinguishes the working repository from the bare remote and can explain why local Git alone is not a hardware-loss backup.
