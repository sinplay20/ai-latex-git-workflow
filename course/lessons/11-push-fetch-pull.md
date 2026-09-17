# Lesson 11 — Push, Fetch, and Pull

## Goal

理解本地分支与远程跟踪分支的同步。

## Push

```powershell
git push
```

Transfers local commits to the configured upstream remote branch.

## Fetch

```powershell
git fetch origin
```

Updates remote-tracking references without modifying the current working branch.

## Pull

```powershell
git pull
```

Fetches and then integrates remote changes according to configuration. It can create a merge or require a rebase policy, so inspect status first.

## Recommended cautious workflow

```text
commit or clean local work
→ fetch
→ inspect incoming history
→ pull or merge intentionally
→ resolve if necessary
→ push
```

## Exercise

Use two local clones of the Hamlet bare remote to simulate two collaborators. Make a Commit in clone A, push it, fetch from clone B, inspect `origin/main`, then integrate it.

## Completion check

The learner explains why Fetch is safer than immediately Pulling when the remote state is unknown.
