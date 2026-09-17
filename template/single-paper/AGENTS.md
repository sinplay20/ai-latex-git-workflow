# Manuscript Agent Instructions

## Authority

The human author retains final authority over mathematics, wording, file structure, Commit, Merge, Revert, tags, and publication.

## Source of truth

- `paper.tex` is the canonical shared master.
- `paper-working.tex` and `paper-submit.tex` are thin wrappers.
- Article content lives under `sections/`.
- Working-only material lives under `appendices/`.
- Do not create versioned manuscript copies such as `paper-v2.tex`, `new.tex`, or `final-final.tex`.

## Before editing

1. Read the relevant source files completely.
2. Confirm the requested files and sections.
3. Check for unresolved ambiguity in mathematical or editorial intent.
4. Do not overwrite concurrent human changes.

## Editing rules

- Modify only the requested scope.
- Preserve labels, citations, theorem environments, notation, and semantic line breaks.
- Do not rewrap unrelated prose.
- Do not silently change theorem hypotheses or proof strategy.
- Ask before creating, deleting, renaming, or moving source files.
- Put generated output under `build/`.

## Git rules

Do not run Git mutation commands unless explicitly authorized. In particular, do not autonomously:

```text
Commit
Merge
Revert
Reset
Clean
Push
Force push
Create or delete tags
Create or delete branches
```

Read-only Git inspection is allowed within the requested task.

## Verification

Use the relevant command:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper-working.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper-submit.tex
```

## Completion report

Report:

1. every changed, added, deleted, or renamed file;
2. mathematical changes;
3. editorial changes;
4. build results;
5. warnings, unresolved references, or open questions;
6. any decision still requiring human approval.
