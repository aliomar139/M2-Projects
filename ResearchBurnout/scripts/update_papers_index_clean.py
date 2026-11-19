import os
import json

TARGET_DIR = os.path.join(os.getcwd(), "ExplainableAIBurnoutPapers")
index_json_path = os.path.join(TARGET_DIR, "processed_papers_index.json")
with open(index_json_path, "r", encoding="utf-8") as f:
    processed_records = json.load(f)

papers_index_md = os.path.join(TARGET_DIR, "PAPERS_INDEX.md")

lines = [
    "# Explainable AI in Student Burnout Research Papers Index",
    "",
    f"This directory contains **{len(processed_records)}** curated research papers on **Explainable AI (XAI)**, **Machine Learning**, and **Predictive Modeling** for **student burnout, academic stress, and mental well-being** published in the last two years (**2024–2026**).",
    "",
    "All files are organized into two dedicated folders:",
    "- [`md/`](./md/): High-fidelity, clean Markdown (`.md`) text copies for direct agent/LLM ingestion with zero OCR overhead.",
    "- [`pdfs/`](./pdfs/): Standardized, verified PDF source files.",
    "",
    "| # | Paper Title | Year | Venue / Journal | Markdown File | PDF File |",
    "|---|-------------|------|-----------------|---------------|----------|"
]

for rec in processed_records:
    idx = rec["index"]
    title = rec["title"]
    year = rec["year"]
    venue = rec["venue"]
    md_fn = rec["md_file"]
    pdf_fn = rec["pdf_file"]
    
    md_link = f"[{md_fn}](./md/{md_fn})"
    pdf_link = f"[{pdf_fn}](./pdfs/{pdf_fn})"
    
    lines.append(f"| {idx} | **{title}** | {year} | {venue} | {md_link} | {pdf_link} |")

lines.extend([
    "",
    "---",
    "",
    "## 🔬 Detailed Paper Abstracts & Metadata",
    ""
])

for rec in processed_records:
    idx = rec["index"]
    title = rec["title"]
    year = rec["year"]
    venue = rec["venue"]
    md_fn = rec["md_file"]
    pdf_fn = rec["pdf_file"]
    pdf_size_kb = rec["pdf_size"] // 1024
    md_size_kb = rec["md_size"] // 1024
    char_count = rec["char_count"]
    doi = rec.get("doi", "N/A")
    authors = ", ".join(rec.get("authors", [])) if rec.get("authors") else "Research Authors"
    abstract = rec.get("abstract", "Full text available in Markdown and PDF.")
    if len(abstract) > 650:
        abstract = abstract[:647] + "..."
        
    lines.append(f"### {idx}. {title} ({year})")
    lines.append(f"- **Authors**: {authors}")
    lines.append(f"- **Venue / Publisher**: {venue}")
    lines.append(f"- **DOI**: [{doi}]({doi})" if str(doi).startswith("http") else f"- **DOI / Citation**: {doi}")
    lines.append(f"- **Files**: [`./md/{md_fn}`](./md/{md_fn}) (`{md_size_kb} KB`, `{char_count:,} chars`) | [`./pdfs/{pdf_fn}`](./pdfs/{pdf_fn}) (`{pdf_size_kb} KB`)")
    lines.append(f"- **Abstract / Summary**:")
    lines.append(f"  > {abstract}")
    lines.append("")

with open(papers_index_md, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Updated {papers_index_md} with clean identical formatting to KassemDanachPapers.")
