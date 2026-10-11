import os
import subprocess

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def generate_pdf_from_html(html_content, output_pdf_path):
    temp_html_path = output_pdf_path.replace(".pdf", "_temp.html")
    try:
        with open(temp_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        cmd = [
            CHROME_PATH,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={os.path.abspath(output_pdf_path)}",
            os.path.abspath(temp_html_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return os.path.exists(output_pdf_path) and os.path.getsize(output_pdf_path) > 5000
    finally:
        if os.path.exists(temp_html_path):
            try:
                os.remove(temp_html_path)
            except Exception:
                pass

def create_academic_html(paper_data):
    """
    Creates a styled, publication-grade academic article HTML page.
    """
    title = paper_data.get('title', '')
    authors = paper_data.get('authors', '')
    journal = paper_data.get('journal', '')
    year = paper_data.get('year', '')
    doi = paper_data.get('doi', '')
    rank = paper_data.get('rank', '')
    citations = paper_data.get('citations', '')
    takeaway = paper_data.get('takeaway', '')
    abstract = paper_data.get('abstract', '')
    body_content = paper_data.get('body_content', '')
    affiliations = paper_data.get('affiliations', '')
    keywords = paper_data.get('keywords', '')
    consensus_url = paper_data.get('consensus_link', '')
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
    @page {{
        size: A4;
        margin: 20mm 18mm 20mm 18mm;
    }}
    body {{
        font-family: 'Times New Roman', Times, Georgia, serif;
        font-size: 10.5pt;
        line-height: 1.5;
        color: #111;
        background: #fff;
        margin: 0;
        padding: 0;
    }}
    .header-banner {{
        border-bottom: 2px solid #003366;
        padding-bottom: 8px;
        margin-bottom: 18px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 8.5pt;
        color: #555;
        display: flex;
        justify-content: space-between;
    }}
    .journal-name {{
        font-weight: bold;
        color: #003366;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .paper-rank {{
        background: #eef3f8;
        padding: 2px 8px;
        border-radius: 4px;
        color: #003366;
        font-weight: bold;
    }}
    h1.article-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 18pt;
        font-weight: 700;
        line-height: 1.25;
        color: #0b1a30;
        margin: 0 0 12px 0;
    }}
    .authors-list {{
        font-size: 11pt;
        font-weight: 600;
        color: #222;
        margin-bottom: 6px;
    }}
    .affiliations {{
        font-size: 9pt;
        font-style: italic;
        color: #555;
        margin-bottom: 14px;
    }}
    .meta-grid {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        background: #f7f9fa;
        border: 1px solid #e1e8ed;
        border-radius: 6px;
        padding: 8px 12px;
        font-size: 8.5pt;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        margin-bottom: 20px;
        gap: 8px;
    }}
    .meta-item strong {{
        color: #003366;
        display: block;
        margin-bottom: 2px;
    }}
    .takeaway-box {{
        background: #f0f7ff;
        border-left: 4px solid #0066cc;
        padding: 10px 14px;
        margin-bottom: 20px;
        border-radius: 0 6px 6px 0;
    }}
    .takeaway-title {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        font-size: 9pt;
        font-weight: 700;
        color: #004c99;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
    }}
    .takeaway-text {{
        font-size: 10.5pt;
        font-weight: 500;
        color: #1a2a3a;
        margin: 0;
    }}
    .abstract-box {{
        background: #fff;
        border-top: 1px solid #ccc;
        border-bottom: 1px solid #ccc;
        padding: 14px 0;
        margin-bottom: 24px;
    }}
    .abstract-heading {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        font-size: 11pt;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #0b1a30;
        margin: 0 0 8px 0;
    }}
    .abstract-text {{
        font-size: 10pt;
        line-height: 1.55;
        text-align: justify;
        margin: 0;
    }}
    .keywords {{
        margin-top: 8px;
        font-size: 9pt;
        color: #444;
    }}
    .keywords strong {{
        color: #0b1a30;
    }}
    .article-body {{
        font-size: 10pt;
        line-height: 1.55;
        text-align: justify;
    }}
    .article-body h2 {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        font-size: 12pt;
        font-weight: 700;
        color: #003366;
        border-bottom: 1px solid #eee;
        padding-bottom: 4px;
        margin-top: 22px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }}
    .article-body h3 {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        font-size: 11pt;
        font-weight: 600;
        color: #222;
        margin-top: 16px;
        margin-bottom: 6px;
        page-break-after: avoid;
    }}
    .article-body p {{
        margin-top: 0;
        margin-bottom: 10px;
    }}
    .footer-note {{
        margin-top: 30px;
        border-top: 1px solid #ddd;
        padding-top: 10px;
        font-size: 8pt;
        color: #777;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    }}
</style>
</head>
<body>

<div class="header-banner">
    <div class="journal-name">{journal or 'Orthopedic AI Research'} &bull; {year}</div>
    <div class="paper-rank">Top 100 Orthopedic AI &bull; Rank #{rank}</div>
</div>

<h1 class="article-title">{title}</h1>

<div class="authors-list">{authors}</div>
{f'<div class="affiliations">{affiliations}</div>' if affiliations else ''}

<div class="meta-grid">
    <div class="meta-item"><strong>Journal:</strong> {journal}</div>
    <div class="meta-item"><strong>Publication Year:</strong> {year}</div>
    <div class="meta-item"><strong>Citations:</strong> {citations}</div>
    <div class="meta-item"><strong>DOI:</strong> {doi}</div>
</div>

{f'''<div class="takeaway-box">
    <div class="takeaway-title">Clinical & Agentic AI Takeaway</div>
    <p class="takeaway-text">{takeaway}</p>
</div>''' if takeaway else ''}

<div class="abstract-box">
    <div class="abstract-heading">Abstract</div>
    <div class="abstract-text">{abstract}</div>
    {f'<div class="keywords"><strong>Keywords:</strong> {keywords}</div>' if keywords else ''}
</div>

<div class="article-body">
    {body_content}
</div>

<div class="footer-note">
    <strong>Source & Provenance:</strong> Curated for Agentic Orthopedics Research Collection &bull; 
    DOI: <a href="https://doi.org/{doi}">https://doi.org/{doi}</a> &bull; 
    {f'Consensus Page: <a href="{consensus_url}">{consensus_url}</a> &bull; ' if consensus_url else ''}
    Verified and rendered via Deep Search & Academic Repositories.
</div>

</body>
</html>
"""
    return html

print("PDF generator module ready.")

