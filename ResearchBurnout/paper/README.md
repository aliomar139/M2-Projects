# Edit the existing Overleaf project

Open the same Overleaf project and use the code editor. Each file in `tex/` has a same-named counterpart in the project. Edit the section you want in its existing file, or copy in just the revised passage from the local version. For this revision, update `abstract.tex`, `introduction.tex`, and `conclusion.tex`, then click **Recompile**. You do not need to change `main.tex` or reimport the ZIP.

For future edits, `main.tex` holds the title, authors, affiliation, and keywords. The other `.tex` files hold the individual sections, and `references.bib` holds the bibliography. The complete Markdown manuscript in `md/manuscript.md` is a reading copy, not an Overleaf input. The ZIP is an older snapshot.

If your Overleaf plan includes Git integration, select **Git** under **Integrations** in the existing project and clone it as a separate, paper-only checkout. Pull before editing and push the reviewed manuscript changes back when ready. Do not push the entire research repository: it contains survey data and other files that do not belong in Overleaf.
