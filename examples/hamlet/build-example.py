#!/usr/bin/env python3
"""Build the public-domain Hamlet Git-history teaching example."""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE / "hamlet-history-source"
BUNDLE = HERE / "hamlet-history.bundle"


def run(*args: str, cwd: Path = REPO, env: dict[str, str] | None = None) -> None:
    command = [str(arg) for arg in args]
    subprocess.run(command, cwd=cwd, env=env, check=True)


def put(relative: str, content: str) -> None:
    path = REPO / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")


def remove_tree(path: Path) -> None:
    def make_writable_and_retry(function, target, _error) -> None:
        os.chmod(target, stat.S_IWRITE)
        function(target)

    shutil.rmtree(path, onexc=make_writable_and_retry)


def remove(relative: str) -> None:
    path = REPO / relative
    if path.is_dir():
        remove_tree(path)
    elif path.exists():
        path.unlink()


def commit(number: int, message: str, tag_message: str) -> None:
    date = f"2026-01-{number:02d}T12:00:00+00:00"
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_DATE"] = date
    run("git", "add", "-A", env=env)
    run("git", "commit", "-m", message, env=env)
    run(
        "git",
        "tag",
        "-a",
        f"lesson-snapshot-{number:02d}",
        "-m",
        tag_message,
        env=env,
    )


V1_MAIN = r"""
\documentclass{article}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: A Short Classroom Extract}
\author{Public-domain text; course edition}
\date{}
\begin{document}
\maketitle

\section*{Act I, Scene I: The Platform}

Elsinore. A platform before the castle.

\speaker{Bernardo} Who's there?
\speaker{Francisco} Nay, answer me. Stand, and unfold yourself.
\speaker{Bernardo} Long live the king!
\speaker{Francisco} Bernardo?
\speaker{Bernardo} He.
\speaker{Francisco} You come most carefully upon your hour.

\end{document}
"""

V2_MAIN = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: A Short Classroom Edition}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle

\section*{Editorial Context}
This teaching edition follows a small set of public-domain excerpts.
Punctuation is lightly normalized, and the surrounding notes are written for
Git and LaTeX exercises rather than textual scholarship.

\section*{Dramatis Personae for the Extract}
\begin{itemize}
  \item Bernardo and Francisco, sentinels at Elsinore;
  \item Marcellus, an officer;
  \item Horatio, Hamlet's friend;
  \item Hamlet, Prince of Denmark.
\end{itemize}

\section*{Act I, Scene I: The Platform}
\emph{Elsinore. A platform before the castle.}

\speaker{Bernardo} Who's there?
\speaker{Francisco} Nay, answer me. Stand, and unfold yourself.
\speaker{Bernardo} Long live the king!
\speaker{Francisco} Bernardo?
\speaker{Bernardo} He.
\speaker{Francisco} You come most carefully upon your hour.

\end{document}
"""

V3_MAIN = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: A Short Classroom Edition}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle

\section*{Editorial Context}
This teaching edition follows a small set of public-domain excerpts.
Punctuation is lightly normalized, and the surrounding notes are written for
Git and LaTeX exercises rather than textual scholarship. The opening scene
establishes uncertainty before Hamlet himself appears.

\section*{Dramatis Personae for the Extract}
\begin{itemize}
  \item Bernardo and Francisco, sentinels at Elsinore;
  \item Marcellus, an officer;
  \item Horatio, Hamlet's friend;
  \item Hamlet, Prince of Denmark.
\end{itemize}

\section*{Act I, Scene I: The Platform}
\emph{Elsinore. A platform before the castle.}

\speaker{Bernardo} Who's there?
\speaker{Francisco} Nay, answer me. Stand, and unfold yourself.
\speaker{Bernardo} Long live the king!
\speaker{Francisco} Bernardo?
\speaker{Bernardo} He.
\speaker{Francisco} You come most carefully upon your hour.

\subsection*{The apparition}

\speaker{Marcellus} Thou art a scholar; speak to it, Horatio.
\speaker{Horatio} What art thou that usurp'st this time of night,
Together with that fair and warlike form
In which the majesty of buried Denmark
Did sometimes march?

\paragraph{Teaching note.}
The question ``Who's there?'' begins a pattern of uncertain identity that
continues when the sentinels attempt to identify the Ghost.

\end{document}
"""

V4_MAIN = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: Selected Scenes for the Classroom}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle

\section*{Editorial Context}
This teaching edition contains public-domain excerpts from the opening scene
and Hamlet's Act III soliloquy. Punctuation is lightly normalized. Editorial
notes are included to demonstrate visible prose changes in Git.

\section*{Dramatis Personae for the Extract}
\begin{itemize}
  \item Bernardo and Francisco, sentinels at Elsinore;
  \item Marcellus, an officer;
  \item Horatio, Hamlet's friend;
  \item Hamlet, Prince of Denmark.
\end{itemize}

\section*{Act I, Scene I: The Platform}
\emph{Elsinore. A platform before the castle.}

\speaker{Bernardo} Who's there?
\speaker{Francisco} Nay, answer me. Stand, and unfold yourself.
\speaker{Bernardo} Long live the king!
\speaker{Francisco} Bernardo?
\speaker{Bernardo} He.
\speaker{Francisco} You come most carefully upon your hour.

\subsection*{The apparition}
\speaker{Marcellus} Thou art a scholar; speak to it, Horatio.
\speaker{Horatio} What art thou that usurp'st this time of night,
Together with that fair and warlike form
In which the majesty of buried Denmark
Did sometimes march?

\section*{Act III, Scene I: The Soliloquy}
\speaker{Hamlet} To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them.

\paragraph{Teaching note.}
The two excerpts move from uncertainty about an external apparition to an
inward debate about action, endurance, and mortality.

\end{document}
"""

MAIN_SPLIT_V5 = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: Selected Scenes for the Classroom}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle
\input{frontmatter/editor-note}
\input{scenes/act-1-scene-1}
\input{scenes/act-3-scene-1}
\end{document}
"""

EDITOR_V5 = r"""
\section*{Editorial Context}
This teaching edition contains public-domain excerpts from the opening scene
and Hamlet's Act III soliloquy. Punctuation is lightly normalized. Editorial
notes are included to demonstrate visible prose changes in Git.

\subsection*{Dramatis Personae for the Extract}
\begin{itemize}
  \item Bernardo and Francisco, sentinels at Elsinore;
  \item Marcellus, an officer;
  \item Horatio, Hamlet's friend;
  \item Hamlet, Prince of Denmark.
\end{itemize}
"""

ACT1_V5 = r"""
\section*{Act I, Scene I: The Platform}
\emph{Elsinore. A platform before the castle.}

\speaker{Bernardo} Who's there?
\speaker{Francisco} Nay, answer me. Stand, and unfold yourself.
\speaker{Bernardo} Long live the king!
\speaker{Francisco} Bernardo?
\speaker{Bernardo} He.
\speaker{Francisco} You come most carefully upon your hour.

\subsection*{The apparition}
\speaker{Marcellus} Thou art a scholar; speak to it, Horatio.
\speaker{Horatio} What art thou that usurp'st this time of night,
Together with that fair and warlike form
In which the majesty of buried Denmark
Did sometimes march?
"""

ACT3_V5 = r"""
\section*{Act III, Scene I: The Soliloquy}
\speaker{Hamlet} To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them.

\paragraph{Teaching note.}
The two excerpts move from uncertainty about an external apparition to an
inward debate about action, endurance, and mortality.
"""

MAIN_V6 = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: Selected Scenes for the Classroom}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle
\input{frontmatter/editor-note}
\input{frontmatter/cast}
\input{text/act-1-scene-1}
\input{text/act-3-scene-1}
\input{notes/editorial-notes}
\end{document}
"""

EDITOR_V6 = r"""
\section*{Editorial Context}
This compact edition uses three kinds of material: dramatic excerpts,
editorial context, and teaching notes. Keeping them in separate files makes
structural changes visible without duplicating the complete document.
"""

CAST_V6 = r"""
\section*{Dramatis Personae for the Extract}
\begin{itemize}
  \item Bernardo and Francisco, sentinels at Elsinore;
  \item Marcellus, an officer;
  \item Horatio, Hamlet's friend;
  \item Hamlet, Prince of Denmark.
\end{itemize}
"""

NOTES_V6 = r"""
\section*{Editorial Notes}
The opening question, ``Who's there?'', introduces uncertainty about
identity. The later soliloquy turns uncertainty inward by weighing endurance
against action. These comments are teaching prompts, not claims about a
single authoritative edition.
"""

MAIN_V7 = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: Selected Scenes for the Classroom}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle
\input{frontmatter/editor-note}
\input{frontmatter/cast}
\input{text/act-1-scene-1}
\input{text/act-3-scene-1}
\input{text/act-5-scene-2}
\input{notes/editorial-notes}
\end{document}
"""

EDITOR_V7 = r"""
\section*{Editorial Context}
This compact edition follows uncertainty across three moments: the guarded
opening at Elsinore, Hamlet's inward deliberation, and the final return to
silence. Dramatic excerpts, context, and teaching notes remain in separate
files so that Git can display both structural and local textual revisions.
"""

ACT5_V7 = r"""
\section*{Act V, Scene II: The Close}
\speaker{Hamlet} The rest is silence.
\speaker{Horatio} Now cracks a noble heart. Good night, sweet prince,
And flights of angels sing thee to thy rest!
"""

NOTES_V7 = r"""
\section*{Editorial Notes}
The opening question, ``Who's there?'', introduces uncertainty about
identity. The Act III soliloquy turns uncertainty inward by weighing
endurance against action. The final exchange replaces deliberation with
silence and Horatio's act of remembrance.

These comments are teaching prompts, not claims about a single authoritative
edition.
"""

HAMLET_V8 = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: Selected Scenes for the Classroom}
\author{William Shakespeare}
\date{}
\begin{document}
\maketitle
\input{frontmatter/editor-note}
\input{frontmatter/cast}
\input{text/act-1-scene-1}
\input{text/act-3-scene-1}
\input{text/act-5-scene-2}
\input{notes/editorial-notes}
\ifdefined\instructorversion
  \appendix
  \input{appendices/teaching-notes}
\fi
\end{document}
"""

READER_WRAPPER = r"""
% Reader build: dramatic excerpts and shared editorial notes.
\input{hamlet.tex}
"""

INSTRUCTOR_WRAPPER = r"""
% Instructor build: reader material plus the teaching appendix.
\def\instructorversion{1}
\input{hamlet.tex}
"""

TEACHING_V8 = r"""
\section{Suggested Git Exercises}
\begin{enumerate}
  \item Compare the monolithic fourth snapshot with the split fifth snapshot.
  \item Follow the rename from \texttt{scenes/} to \texttt{text/}.
  \item Compare the reader and instructor wrappers.
  \item Create a branch that revises one teaching note, then review and merge it.
\end{enumerate}
"""

HAMLET_V9 = r"""
\documentclass{article}
\usepackage[margin=1in]{geometry}
\newcommand{\speaker}[1]{\par\noindent\textsc{#1}. }
\title{Hamlet: Selected Scenes for Git and LaTeX Practice}
\author{William Shakespeare; teaching apparatus by the course authors}
\date{}
\begin{document}
\maketitle
\begin{abstract}
This short public-domain classroom edition is designed for learning Git-based
version control with LaTeX. Its history contains both textual revisions and
source-tree reorganizations.
\end{abstract}
\input{frontmatter/editor-note}
\input{frontmatter/cast}
\input{text/act-1-scene-1}
\input{text/act-3-scene-1}
\input{text/act-5-scene-2}
\input{notes/editorial-notes}
\ifdefined\instructorversion
  \appendix
  \input{appendices/teaching-notes}
\fi
\end{document}
"""

EDITOR_V9 = r"""
\section*{Editorial Context}
This compact edition follows uncertainty across three moments: the guarded
opening at Elsinore, Hamlet's inward deliberation, and the final return to
silence. Dramatic excerpts, editorial context, and teaching notes remain in
separate files so that Git can display both structural revisions and precise
line-level changes.

The dramatic text is public domain. Punctuation is lightly normalized for the
limited pedagogical purpose of this example.
"""

NOTES_V9 = r"""
\section*{Editorial Notes}
The opening question, ``Who's there?'', introduces uncertainty about identity
and authority. The Act III soliloquy turns uncertainty inward by weighing
endurance against action. The final exchange replaces deliberation with
silence, followed by Horatio's act of remembrance.

These notes demonstrate editorial revision in Git. They do not claim to
replace textual scholarship or a critical edition.
"""

TEACHING_V9 = r"""
\section{Suggested Git Exercises}
\begin{enumerate}
  \item Compare \texttt{lesson-snapshot-04} with
        \texttt{lesson-snapshot-05} to inspect the monolithic-to-split change.
  \item Follow the rename from \texttt{scenes/} to \texttt{text/} in
        \texttt{lesson-snapshot-06}.
  \item Compare \texttt{lesson-snapshot-08} with
        \texttt{lesson-snapshot-09} for local editorial changes.
  \item Create a branch that revises one teaching note, inspect the Diff,
        compile both wrappers, and merge only after approval.
  \item Create and resolve a controlled conflict in one editorial sentence.
\end{enumerate}
"""


def build(force: bool) -> None:
    if REPO.exists() or BUNDLE.exists():
        if not force:
            raise SystemExit(
                "Generated example already exists. Re-run with --force to rebuild it."
            )
        remove_path = REPO
        if remove_path.exists():
            remove_tree(remove_path)
        if BUNDLE.exists():
            BUNDLE.unlink()

    REPO.mkdir(parents=True)
    run("git", "init", "-b", "main")
    run("git", "config", "user.name", "Hamlet Course Builder")
    run("git", "config", "user.email", "course@example.invalid")

    put(".gitignore", "/build/\n*.aux\n*.fdb_latexmk\n*.fls\n*.log\n*.out\n*.synctex.gz")
    put(".gitattributes", "*.tex text eol=lf\n*.md text eol=lf\n.gitignore text eol=lf")
    put("main.tex", V1_MAIN)
    put("SNAPSHOT.md", "# Snapshot 01\n\nMinimal monolithic Act I opening extract.")
    commit(1, "Start with a minimal monolithic Hamlet extract", "Minimal Act I opening extract")

    put("main.tex", V2_MAIN)
    put("SNAPSHOT.md", "# Snapshot 02\n\nAdd editorial context and a dramatis personae list.")
    commit(2, "Add editorial context and dramatis personae", "Context and cast added")

    put("main.tex", V3_MAIN)
    put("SNAPSHOT.md", "# Snapshot 03\n\nExpand Act I with the apparition and an identity note.")
    commit(3, "Expand the opening scene and add an identity note", "Ghost excerpt and teaching note")

    put("main.tex", V4_MAIN)
    put("SNAPSHOT.md", "# Snapshot 04\n\nAdd the Act III soliloquy and revise the teaching frame.")
    commit(4, "Add the Act III soliloquy and revise presentation", "Second scene added to monolithic source")

    put("main.tex", MAIN_SPLIT_V5)
    put("frontmatter/editor-note.tex", EDITOR_V5)
    put("scenes/act-1-scene-1.tex", ACT1_V5)
    put("scenes/act-3-scene-1.tex", ACT3_V5)
    put("README.md", "# Split Hamlet source\n\nCompile `main.tex` from this directory.")
    put("SNAPSHOT.md", "# Snapshot 05\n\nSplit the monolithic source into front matter and scene files.")
    commit(5, "Split the monolithic source into component files", "Monolithic-to-split source transition")

    run("git", "mv", "scenes", "text")
    put("main.tex", MAIN_V6)
    put("frontmatter/editor-note.tex", EDITOR_V6)
    put("frontmatter/cast.tex", CAST_V6)
    put("notes/editorial-notes.tex", NOTES_V6)
    put("README.md", "# Organized Hamlet source\n\n`main.tex` inputs front matter, dramatic text, and editorial notes.")
    put("SNAPSHOT.md", "# Snapshot 06\n\nRename the scene directory and separate cast and notes.")
    commit(6, "Reorganize dramatic text and editorial apparatus", "Directory rename and source reorganization")

    put("main.tex", MAIN_V7)
    put("frontmatter/editor-note.tex", EDITOR_V7)
    put("text/act-5-scene-2.tex", ACT5_V7)
    put("notes/editorial-notes.tex", NOTES_V7)
    put("SNAPSHOT.md", "# Snapshot 07\n\nAdd the closing scene and synchronize the editorial context.")
    commit(7, "Add the closing scene and synchronize context", "Three-scene classroom selection")

    run("git", "mv", "main.tex", "hamlet.tex")
    put("hamlet.tex", HAMLET_V8)
    put("hamlet-reader.tex", READER_WRAPPER)
    put("hamlet-instructor.tex", INSTRUCTOR_WRAPPER)
    put("appendices/teaching-notes.tex", TEACHING_V8)
    put("README.md", "# Hamlet classroom builds\n\nCompile `hamlet-reader.tex` or `hamlet-instructor.tex`.")
    put("SNAPSHOT.md", "# Snapshot 08\n\nIntroduce canonical source plus reader and instructor wrappers.")
    commit(8, "Introduce reader and instructor build wrappers", "Two build modes from one canonical source")

    put("hamlet.tex", HAMLET_V9)
    put("frontmatter/editor-note.tex", EDITOR_V9)
    put("notes/editorial-notes.tex", NOTES_V9)
    put("appendices/teaching-notes.tex", TEACHING_V9)
    put(
        "README.md",
        "# Hamlet Git and LaTeX classroom edition\n\n"
        "Compile `hamlet-reader.tex` for the reader edition or "
        "`hamlet-instructor.tex` for the instructor edition.\n",
    )
    put(
        "SOURCE_NOTE.md",
        "# Source note\n\n"
        "The dramatic text is a short public-domain Hamlet extract with lightly "
        "normalized punctuation. Editorial notes and the Git history are original "
        "course materials.\n",
    )
    put(
        "VERSION.md",
        "# Classroom release\n\n"
        "This is the final course snapshot. The Git tags are the authoritative "
        "version identifiers; filenames are not used as version numbers.\n",
    )
    put("SNAPSHOT.md", "# Snapshot 09\n\nFinalize the Git and LaTeX classroom edition.")
    commit(9, "Finalize the Hamlet Git and LaTeX classroom edition", "Final classroom edition")

    run("git", "bundle", "create", str(BUNDLE), "--all")
    run("git", "bundle", "verify", str(BUNDLE))
    print(f"Created repository: {REPO}")
    print(f"Created bundle:     {BUNDLE}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="replace generated example")
    args = parser.parse_args()
    build(args.force)
