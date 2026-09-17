# Scoped AI Edit Request

Repository: `[path]`
Expected branch: `[task branch]`
Allowed files: `[explicit list]`
Allowed sections: `[explicit headings or labels]`

## Task

`[Describe the requested mathematical or editorial work.]`

## Constraints

- Do not modify unrelated text.
- Do not create version-numbered copies.
- Preserve notation, labels, citations, and semantic line breaks.
- Do not perform Git mutations.
- Ask before making an ambiguous mathematical or editorial choice.

## Verification

Run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper-working.tex
```

Also build `paper-submit.tex` if the change affects shared article content.

## Report

List changed files, mathematical changes, editorial changes, build results,
and unresolved questions.
