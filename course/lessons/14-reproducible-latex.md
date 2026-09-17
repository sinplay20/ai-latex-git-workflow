# Lesson 14 — Reproducible LaTeX Projects

## Goal

确保历史版本能够从完整源文件重新构建。

## Track

- `.tex`;
- `.bib`;
- custom `.sty`, `.cls`, `.bst`;
- source figures;
- `latexmkrc` or documented build commands;
- README and submission instructions.

## Ignore

- auxiliary files;
- logs;
- synchronization data;
- ordinary build output under `build/`.

Do not broadly ignore `*.pdf` when PDF figures are source assets.

## Suggested layout

```text
main.tex
sections/
figures/
references.bib
build/
README.md
AGENTS.md
.gitignore
```

## Build

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

Use the correct engine when required, such as `-xelatex`.

## Multiple outputs

Use thin wrappers for working and submission builds rather than duplicated manuscripts. Both wrappers should input the same canonical source.

## Milestone PDFs

Daily PDFs can remain generated artifacts. Preserve submission PDFs separately through release storage or explicitly named milestone artifacts when required.

## Completion check

Clone the Hamlet example from its bundle into a fresh directory and reproduce the final PDF from tracked source only.
