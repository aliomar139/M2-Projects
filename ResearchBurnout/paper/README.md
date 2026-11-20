# Edit the existing Overleaf project

Open the existing Overleaf project and update `main.tex`, `introduction.tex`, `related-work.tex`, `study-design-and-evaluation.tex`, `results-and-discussion.tex`, and `conclusion.tex` from `tex/`. Copy the three PDFs from `tex/figures/` into a `figures/` folder in the Overleaf project, next to `main.tex`. If the project still has the earlier abstract, update `abstract.tex` too. Click **Recompile**.

For future edits, `main.tex` holds the title, authors, affiliation, and keywords. The other `.tex` files hold the individual sections, and `references.bib` holds the bibliography. The complete Markdown manuscript in `md/manuscript.md` is a reading copy, not an Overleaf input. The ZIP is an older snapshot.

To regenerate the figures, run `python paper/make_figures.py` from the ResearchBurnout workspace. The script uses Matplotlib and NumPy and reads the aggregate CSVs in `results/`.

The [complete warning metrics](../results/25-model-comparison-summary.csv) include the additional reference rules.

If your Overleaf plan includes Git integration, select **Git** under **Integrations** in the existing project and clone it as a separate, paper-only checkout. Pull before editing and push the reviewed manuscript changes back when ready. Do not push the entire research repository: it contains survey data and other files that do not belong in Overleaf.
