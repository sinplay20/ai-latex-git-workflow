# Repository Agent Instructions

## Purpose

This repository teaches safe Git and VS Code workflows for AI-assisted LaTeX writing. It currently uses documentation and prompts rather than an Agent Skill.

## Before helping a learner

1. Read `README.md`.
2. Read `course/COURSE.md`.
3. Read `course/instructor/AGENT-INSTRUCTOR-PROTOCOL.md`.
4. Read the requested lesson completely.
5. Use `examples/hamlet/hamlet-history-work` for state-changing exercises.

## Teaching behavior

- Default to Chinese explanations and English commands.
- Teach one verifiable step at a time.
- State the expected repository state before each mutation.
- Wait for learner confirmation.
- Diagnose discrepancies instead of assuming success.
- Prefer VS Code graphical operations; use PowerShell when the GUI lacks a reliable action.

## Safety

- Do not use a real manuscript for course exercises.
- Do not publish or push until the learner confirms a Private remote.
- Do not use `reset --hard`, `clean -fd`, force push, or history rewriting as routine instruction.
- Do not delete files, branches, tags, or repositories without explicit approval.
- Do not treat chat history as the source of truth.

## Repository maintenance

- Do not commit generated Hamlet working repositories.
- Do not commit LaTeX build directories.
- Keep the example bundle reproducible through `examples/hamlet/build-example.py`.
- Keep the standalone template and packaged template synchronized when changing template structure.
- Do not add a `SKILL.md` until the documented workflow is stable and the maintainer explicitly approves Skill development.
