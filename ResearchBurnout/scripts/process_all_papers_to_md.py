import os
import sys
import json
import re
import urllib.parse
import pymupdf4llm

sys.stdout.reconfigure(line_buffering=True)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD_DIR = os.path.join(ROOT_DIR, "ExplainableAI_Student_Burnout_Papers")
TARGET_DIR = os.path.join(ROOT_DIR, "ExplainableAIBurnoutPapers")

# Rename if OLD_DIR exists and TARGET_DIR does not
if os.path.exists(OLD_DIR) and not os.path.exists(TARGET_DIR):
    os.rename(OLD_DIR, TARGET_DIR)
    print(f"Renamed {OLD_DIR} -> {TARGET_DIR}")

PDF_DIR = os.path.join(TARGET_DIR, "pdfs")
MD_DIR = os.path.join(TARGET_DIR, "md")
os.makedirs(MD_DIR, exist_ok=True)

# Load verified_papers.json
verified_json_path = os.path.join(TARGET_DIR, "verified_papers.json")
with open(verified_json_path, "r", encoding="utf-8") as f:
    verified_papers = json.load(f)

print(f"Loaded {len(verified_papers)} papers to process.")

processed_records = []

for i, p in enumerate(verified_papers, 1):
    pdf_filename = p["pdf_filename"]
    pdf_path = os.path.join(PDF_DIR, pdf_filename)
    
    # Base name for markdown
    base_name = os.path.splitext(pdf_filename)[0]
    md_filename = f"{base_name}.md"
    md_path = os.path.join(MD_DIR, md_filename)
    
    print(f"[{i}/{len(verified_papers)}] Converting: {pdf_filename[:60]}...")
    
    md_text = ""
    try:
        md_text = pymupdf4llm.to_markdown(pdf_path)
    except Exception as e:
        print(f"  Warning: pymupdf4llm error on {pdf_filename}: {e}. Trying fallback...")
        import fitz
        doc = fitz.open(pdf_path)
        pages = []
        for page in doc:
            pages.append(page.get_text("text"))
        md_text = "\n\n".join(pages)
        
    # Write MD file
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
        
    pdf_size = os.path.getsize(pdf_path)
    md_size = os.path.getsize(md_path)
    char_count = len(md_text)
    
    print(f"  -> Generated {md_filename} ({md_size // 1024} KB, {char_count:,} characters)")
    
    processed_records.append({
        "index": i,
        "title": p["title"],
        "year": str(p["year"]),
        "venue": p.get("source", "Peer-Reviewed / Open-Access"),
        "pdf_file": pdf_filename,
        "md_file": md_filename,
        "pdf_size": pdf_size,
        "md_size": md_size,
        "char_count": char_count,
        "doi": p.get("doi", ""),
        "authors": p.get("authors", []),
        "abstract": p.get("abstract", "")
    })

# Save processed_papers_index.json
index_json_path = os.path.join(TARGET_DIR, "processed_papers_index.json")
with open(index_json_path, "w", encoding="utf-8") as f:
    json.dump(processed_records, f, indent=2, ensure_ascii=False)
print(f"Saved {index_json_path}")

# Generate PAPERS_INDEX.md
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
    
    md_link = f"[{md_fn}](./md/{urllib.parse.quote(md_fn)})"
    pdf_link = f"[{pdf_fn}](./pdfs/{urllib.parse.quote(pdf_fn)})"
    
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
    lines.append(f"- **Files**: [`./md/{md_fn}`](./md/{urllib.parse.quote(md_fn)}) (`{md_size_kb} KB`, `{char_count:,} chars`) | [`./pdfs/{pdf_fn}`](./pdfs/{urllib.parse.quote(pdf_fn)}) (`{pdf_size_kb} KB`)")
    lines.append(f"- **Abstract / Summary**:")
    lines.append(f"  > {abstract}")
    lines.append("")

with open(papers_index_md, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated {papers_index_md}")
