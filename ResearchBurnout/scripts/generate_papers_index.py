import os
import json
import re
import urllib.parse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT_DIR, "ExplainableAI_Student_Burnout_Papers")
PDF_DIR = os.path.join(OUT_DIR, "pdfs")
INDEX_PATH = os.path.join(OUT_DIR, "PAPERS_INDEX.md")

with open(os.path.join(OUT_DIR, "verified_papers.json"), "r", encoding="utf-8") as f:
    papers = json.load(f)

md_lines = [
    "# Explainable AI in Predicting Student Burnout - Research Literature Repository",
    "",
    "This curated repository contains **20 verified, full-text research papers published in the last two years (2024–2026)** investigating **Explainable AI (XAI)**, **Machine Learning**, and **Predictive Modeling** for **student burnout, academic stress, depression, and learning exhaustion**.",
    "",
    f"All 20 papers have been downloaded, verified for PDF integrity, and saved in the [`pdfs/`](file:///{PDF_DIR.replace('\\\\', '/').replace('\\', '/')}) directory.",
    "",
    "---",
    "",
    "## 📊 Summary Table of Downloaded Papers",
    "",
    "| # | Year | Paper Title | Methods / XAI Techniques | Target Cohort & Focus | Venue / Source | PDF File |",
    "|---|------|-------------|--------------------------|-----------------------|----------------|----------|"
]

for p in papers:
    num = p["number"]
    title = p["title"]
    year = p["year"]
    source = p.get("source", "Peer-Reviewed / Open-Access")
    pdf_fn = p["pdf_filename"]
    pdf_path = os.path.join(PDF_DIR, pdf_fn).replace('\\', '/')
    
    title_lower = title.lower()
    abstract_lower = p.get("abstract", "").lower()
    
    # Identify XAI / ML methods
    methods = []
    if "shap" in title_lower or "shap" in abstract_lower:
        methods.append("SHAP")
    if "lime" in title_lower or "lime" in abstract_lower:
        methods.append("LIME")
    if "c5.0" in title_lower or "c5.0" in abstract_lower:
        methods.append("C5.0 Decision Trees")
    if "lightgbm" in title_lower or "lightgbm" in abstract_lower:
        methods.append("LightGBM")
    if "xgboost" in title_lower or "xgboost" in abstract_lower:
        methods.append("XGBoost")
    if "random forest" in title_lower or "random forest" in abstract_lower:
        methods.append("Random Forest")
    if "ensemble" in title_lower or "ensemble" in abstract_lower:
        methods.append("Ensemble Learning")
    if "deep learning" in title_lower or "deep learning" in abstract_lower:
        methods.append("Deep Learning")
    if "epidemic" in title_lower or "differential" in title_lower:
        methods.append("Epidemic Modeling + ML")
    if "latent profile" in title_lower:
        methods.append("Latent Profile Analysis")
    if not methods:
        methods.append("Explainable ML Classifiers")
    methods_str = ", ".join(methods[:2])
    
    # Cohort
    if "medical student" in title_lower or "medical student" in abstract_lower:
        cohort = "Medical Students"
    elif "high school" in title_lower or "high school" in abstract_lower:
        cohort = "High School Students"
    elif "postgraduate" in title_lower or "phd" in title_lower:
        cohort = "Postgrad / PhD Students"
    elif "foreign language" in title_lower:
        cohort = "Foreign Language Learners"
    elif "university student" in title_lower or "college student" in title_lower:
        cohort = "University Students"
    else:
        cohort = "Students & Youth"
        
    pdf_link = f"[{pdf_fn}](file:///{pdf_path})"
    md_lines.append(f"| {num} | {year} | **{title}** | {methods_str} | {cohort} | {source} | {pdf_link} |")

md_lines.extend([
    "",
    "---",
    "",
    "## 🔬 Detailed Profiles of the 20 Papers",
    ""
])

for p in papers:
    num = p["number"]
    title = p["title"]
    year = p["year"]
    source = p.get("source", "Open Access / Academic Publication")
    pdf_fn = p["pdf_filename"]
    pdf_path = os.path.join(PDF_DIR, pdf_fn).replace('\\', '/')
    pdf_size = p.get("pdf_size_kb", 0)
    doi = p.get("doi", "N/A")
    authors = ", ".join(p.get("authors", [])) if p.get("authors") else "Research Authors"
    abstract = p.get("abstract", "Abstract available in the local PDF document.")
    if len(abstract) > 650:
        abstract = abstract[:647] + "..."
        
    md_lines.append(f"### {num}. {title} ({year})")
    md_lines.append(f"- **Authors**: {authors}")
    md_lines.append(f"- **Venue / Publisher**: {source}")
    md_lines.append(f"- **DOI**: [{doi}]({doi})" if doi.startswith("http") else f"- **DOI / Citation**: {doi}")
    md_lines.append(f"- **Local File**: [{pdf_fn}](file:///{pdf_path}) (`{pdf_size} KB`)")
    md_lines.append(f"- **Abstract / Synthesis**:")
    md_lines.append(f"  > {abstract}")
    md_lines.append("")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Index successfully regenerated at: {INDEX_PATH}")
