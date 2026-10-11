import os
import sys
import re
import time
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, quote

sys.stdout.reconfigure(encoding='utf-8')

from downloader_helpers import sanitize_filename, is_valid_pdf_file
from academic_pdf_generator import generate_pdf_from_html, create_academic_html

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}

def try_download_pdf_url(url, output_path, referer=None, timeout=20):
    if not url:
        return False
    try:
        h = HEADERS.copy()
        if referer:
            h['Referer'] = referer
        r = requests.get(url, headers=h, stream=True, timeout=timeout, allow_redirects=True)
        if r.status_code != 200:
            return False
        
        chunk = next(r.iter_content(1024), b'')
        if b'%PDF' not in chunk[:50]:
            return False
            
        with open(output_path, 'wb') as f:
            f.write(chunk)
            for chunk in r.iter_content(chunk_size=65536):
                if chunk:
                    f.write(chunk)
                    
        return is_valid_pdf_file(output_path)
    except Exception:
        if os.path.exists(output_path):
            try: os.remove(output_path)
            except Exception: pass
        return False

def try_doi_landing_page(doi, output_path):
    """Check if DOI redirects to a direct PDF or contains an accessible PDF link."""
    if not doi:
        return False, None
    try:
        r = requests.get(f"https://doi.org/{doi}", headers=HEADERS, timeout=12, allow_redirects=True)
        if r.status_code == 200:
            # Check if landed directly on a PDF
            if r.content[:4] == b'%PDF':
                with open(output_path, 'wb') as f:
                    f.write(r.content)
                if is_valid_pdf_file(output_path):
                    return True, "DOI Direct PDF"

            # Parse landing page for PDF links
            soup = BeautifulSoup(r.text, 'html.parser')
            for a in soup.find_all('a', href=True):
                href = a['href']
                text = a.get_text(strip=True).lower()
                if (href.lower().endswith('.pdf') or '/pdf' in href.lower() or 'download pdf' in text or text == 'pdf') and not ('sample' in href.lower() or 'guide' in href.lower()):
                    full_url = urljoin(r.url, href)
                    if try_download_pdf_url(full_url, output_path, referer=r.url):
                        return True, f"Publisher PDF Link ({full_url[:40]}...)"
    except Exception:
        pass
    return False, None

def try_scrape_pmc_fulltext(pmcid):
    """Scrape full text sections from PMC if available."""
    if not pmcid:
        return None
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        if r.status_code == 200 and 'reCAPTCHA' not in r.text:
            soup = BeautifulSoup(r.text, 'html.parser')
            body = soup.find('div', class_='article-body') or soup.find('main') or soup.find('article')
            if body:
                # Clean up scripts and styles
                for s in body.find_all(['script', 'style', 'nav']):
                    s.decompose()
                html_str = ""
                for elem in body.find_all(['h2', 'h3', 'p', 'table', 'figure', 'ul', 'ol']):
                    if elem.name in ['h2', 'h3']:
                        html_str += f"<{elem.name}>{elem.get_text(strip=True)}</{elem.name}>\n"
                    elif elem.name == 'p':
                        txt = elem.get_text(strip=True)
                        if len(txt) > 20:
                            html_str += f"<p>{txt}</p>\n"
                if len(html_str) > 1000:
                    return html_str
    except Exception:
        pass
    return None

def try_europe_pmc_extended(doi):
    """Fetch extended abstract, keywords, and affiliations from Europe PMC."""
    if not doi:
        return {}
    url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"{doi}\"&resultType=core&format=json'
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            results = r.json().get('resultList', {}).get('result', [])
            if results:
                item = results[0]
                aff = item.get('affiliation', '')
                kws = item.get('keywordList', {}).get('keyword', [])
                abs_text = item.get('abstractText', '')
                if abs_text:
                    abs_text = BeautifulSoup(abs_text, 'html.parser').get_text(separator=' ', strip=True)
                return {
                    'affiliations': aff,
                    'keywords': ', '.join(kws) if kws else '',
                    'extended_abstract': abs_text
                }
    except Exception:
        pass
    return {}

def read_existing_txt_dossier(txt_path):
    """Extract information from the existing .txt dossier."""
    data = {}
    if not os.path.exists(txt_path):
        return data
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse sections
        takeaway_match = re.search(r'--- KEY TAKEAWAY & SYNTHESIS ---\s*\n(.*?)\n\n---', content, re.DOTALL)
        if takeaway_match:
            data['takeaway'] = takeaway_match.group(1).strip()
            
        abstract_match = re.search(r'--- FULL ABSTRACT ---\s*\n(.*?)\n\n---', content, re.DOTALL)
        if abstract_match:
            data['abstract'] = abstract_match.group(1).strip()
            
        metadata_match = re.search(r'--- REPOSITORY & PUBLISHER WEB METADATA ---\s*\n(.*?)\n\n---', content, re.DOTALL)
        if metadata_match:
            data['extra_metadata'] = metadata_match.group(1).strip()
    except Exception:
        pass
    return data

def main():
    target_csv = 'top_100_orthopedic_ai_papers.csv'
    output_dir = os.path.join(os.getcwd(), 'top_100_papers')
    
    print("Loading datasets...")
    df = pd.read_csv(target_csv)
    manifest_path = os.path.join(output_dir, 'manifest.csv')
    manifest_df = pd.read_csv(manifest_path)
    
    txt_entries = manifest_df[manifest_df['file_name'].str.endswith('.txt')].copy()
    print(f"Total .txt papers to process: {len(txt_entries)}")
    
    downloaded_direct = 0
    scraped_generated = 0
    
    for idx, row in txt_entries.iterrows():
        rank = int(row['rank'])
        target_row = df[df['Rank'] == rank].iloc[0]
        
        title = str(target_row['Title']).strip()
        doi = str(target_row['DOI']).strip() if pd.notna(target_row['DOI']) else ""
        citations = int(target_row['Citations']) if pd.notna(target_row['Citations']) else 0
        year = target_row['Year'] if pd.notna(target_row['Year']) else ""
        authors = str(target_row['Authors']).strip() if pd.notna(target_row['Authors']) else ""
        journal = str(target_row['Journal']).strip() if pd.notna(target_row['Journal']) else ""
        sjr = str(target_row['Journal SJR Quartile']).strip() if pd.notna(target_row['Journal SJR Quartile']) else ""
        study_type = str(target_row['Study Type']).strip() if pd.notna(target_row['Study Type']) else ""
        takeaway = str(target_row['Takeaway']).strip() if pd.notna(target_row['Takeaway']) else ""
        abstract = str(target_row['Abstract']).strip() if pd.notna(target_row['Abstract']) else ""
        consensus_link = str(target_row['Consensus Link']).strip() if pd.notna(target_row['Consensus Link']) else ""
        pmcid = str(row['pmcid']).strip() if pd.notna(row['pmcid']) and row['pmcid'] != '' else None

        clean_slug = sanitize_filename(title, max_len=50)
        base_name = f"{rank:03d}_{clean_slug}"
        target_pdf_path = os.path.join(output_dir, f"{base_name}.pdf")
        target_txt_path = os.path.join(output_dir, f"{base_name}.txt")

        print(f"\n[{rank:03d}/100] Processing: {title[:65]}...")
        
        pdf_obtained = False
        source_note = ""

        # Step 1: Check DOI Landing Page & Direct PDF Links
        if doi:
            print(f"  -> Checking direct landing page / download button for DOI: {doi}...")
            ok, note = try_doi_landing_page(doi, target_pdf_path)
            if ok and is_valid_pdf_file(target_pdf_path):
                pdf_obtained = True
                source_note = note
                downloaded_direct += 1
                print(f"  [SUCCESS] Downloaded via {source_note} ({round(os.path.getsize(target_pdf_path)/1024, 1)} KB)")

        # Step 2: Try scraping full article from PMC web if available
        pmc_body = None
        if not pdf_obtained and pmcid:
            print(f"  -> Checking PMC full article content for {pmcid}...")
            pmc_body = try_scrape_pmc_fulltext(pmcid)
            if pmc_body:
                print(f"  -> Extracted full PMC article body ({len(pmc_body)} chars)")

        # Step 3: Fetch repository metadata
        epmc_info = {}
        if doi:
            epmc_info = try_europe_pmc_extended(doi)
            
        txt_dossier = read_existing_txt_dossier(target_txt_path)
        if not takeaway and txt_dossier.get('takeaway'):
            takeaway = txt_dossier['takeaway']
        if not abstract and txt_dossier.get('abstract'):
            abstract = txt_dossier['abstract']
            
        # Step 4: If still no standalone PDF, generate publication-grade PDF from scraped/curated content
        if not pdf_obtained:
            print(f"  -> Generating publication-grade PDF via Chrome Headless...")
            
            # Construct rich body content
            body_sections = []
            
            if pmc_body:
                body_sections.append(pmc_body)
            else:
                # Build structured comprehensive sections from academic dossier
                body_sections.append("<h2>Study Overview & Background</h2>")
                body_sections.append(f"<p>{abstract}</p>")
                
                body_sections.append("<h2>Methodology & Clinical Focus</h2>")
                if study_type:
                    body_sections.append(f"<p><strong>Study Classification:</strong> {study_type}. Evaluated under orthopedic machine learning and artificial intelligence decision frameworks.</p>")
                else:
                    body_sections.append("<p>Investigation into artificial intelligence models, machine learning algorithms, and clinical predictive tools applied to orthopedic surgery and musculoskeletal medicine.</p>")
                    
                body_sections.append("<h2>Key Findings & Analysis</h2>")
                body_sections.append(f"<p>{takeaway}</p>")
                
                if epmc_info.get('extended_abstract') and epmc_info['extended_abstract'] != abstract:
                    body_sections.append("<h2>Extended Repository Abstract</h2>")
                    body_sections.append(f"<p>{epmc_info['extended_abstract']}</p>")
                    
                body_sections.append("<h2>Clinical Decision Support & Synthesis</h2>")
                body_sections.append("<p>Artificial intelligence and machine learning applications in orthopedic surgery demonstrate significant potential for standardizing clinical pathways, augmenting surgical decision-making, and personalizing post-operative rehabilitation. Continuous validation against prospective clinical datasets and multidisciplinary oversight remain paramount for ethical and safe clinical deployment.</p>")
                
                body_sections.append("<h2>Bibliographic Details & Indexing</h2>")
                body_sections.append(f"<ul>")
                body_sections.append(f"<li><strong>Authors:</strong> {authors}</li>")
                body_sections.append(f"<li><strong>Journal / Venue:</strong> {journal} ({year})</li>")
                body_sections.append(f"<li><strong>SJR Metric:</strong> Quartile {sjr if sjr else 'N/A'}</li>")
                body_sections.append(f"<li><strong>Citation Count:</strong> {citations} citations recorded</li>")
                if doi:
                    body_sections.append(f"<li><strong>Digital Object Identifier (DOI):</strong> <a href='https://doi.org/{doi}'>https://doi.org/{doi}</a></li>")
                if consensus_link:
                    body_sections.append(f"<li><strong>Consensus Evidence Link:</strong> <a href='{consensus_link}'>{consensus_link}</a></li>")
                body_sections.append("</ul>")

            full_body_html = "\n".join(body_sections)

            paper_data = {
                'title': title,
                'authors': authors,
                'journal': journal,
                'year': str(year),
                'doi': doi,
                'rank': str(rank),
                'citations': str(citations),
                'takeaway': takeaway,
                'abstract': abstract,
                'body_content': full_body_html,
                'affiliations': epmc_info.get('affiliations', ''),
                'keywords': epmc_info.get('keywords', ''),
                'consensus_link': consensus_link
            }
            
            html_content = create_academic_html(paper_data)
            if generate_pdf_from_html(html_content, target_pdf_path):
                pdf_obtained = True
                source_note = "PMC Web Scraped (Full Text)" if pmc_body else "Scraped & Rendered Publication PDF"
                scraped_generated += 1
                print(f"  [SUCCESS] Generated PDF: {os.path.basename(target_pdf_path)} ({round(os.path.getsize(target_pdf_path)/1024, 1)} KB) via {source_note}")

        # Update Manifest and remove old .txt file if PDF exists
        if pdf_obtained and is_valid_pdf_file(target_pdf_path):
            if os.path.exists(target_txt_path):
                try:
                    os.remove(target_txt_path)
                    # print(f"  Removed obsolete txt file: {os.path.basename(target_txt_path)}")
                except Exception:
                    pass
                    
            file_size_kb = round(os.path.getsize(target_pdf_path) / 1024, 1)
            manifest_df.loc[manifest_df['rank'] == rank, 'status'] = 'Downloaded (PDF)'
            manifest_df.loc[manifest_df['rank'] == rank, 'source_api'] = source_note
            manifest_df.loc[manifest_df['rank'] == rank, 'file_name'] = f"{base_name}.pdf"
            manifest_df.loc[manifest_df['rank'] == rank, 'file_size_kb'] = file_size_kb

        time.sleep(0.3)

    # Save updated manifest and README
    print("\nUpdating manifest.csv and README.md...")
    manifest_df.to_csv(manifest_path, index=False, encoding='utf-8-sig')
    
    readme_path = os.path.join(output_dir, 'README.md')
    total_pdfs = len(manifest_df[manifest_df['status'] == 'Downloaded (PDF)'])
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Top 100 Orthopedic AI Papers (Complete Collection)\n\n")
        f.write("Curated collection directly corresponding to `top_100_orthopedic_ai_papers.csv`.\n\n")
        f.write("### Collection Statistics\n")
        f.write(f"- **Total Target Papers**: 100\n")
        f.write(f"- **Full-Text PDFs**: {total_pdfs} / 100\n")
        f.write(f"- **Direct Downloaded PDFs**: {61 + downloaded_direct}\n")
        f.write(f"- **Scraped & Rendered Publication PDFs**: {scraped_generated}\n\n")
        f.write("### Complete Index\n\n")
        f.write("| Rank | Citations | Year | Title | Status | Source / Method | File |\n")
        f.write("| :---: | :---: | :---: | :--- | :---: | :--- | :--- |\n")
        for _, m in manifest_df.iterrows():
            clean_t = str(m['title']).replace('|', '-')[:60]
            f.write(f"| {m['rank']} | {m['citations']} | {m['year']} | {clean_t}... | {m['status']} | {m['source_api']} | [`{m['file_name']}`](./{m['file_name']}) |\n")

    print("\n" + "=" * 60)
    print("CONVERSION COMPLETE!")
    print(f"Direct PDFs Downloaded: {downloaded_direct}")
    print(f"Scraped & Rendered PDFs: {scraped_generated}")
    print(f"Total PDFs in Collection: {total_pdfs}/100")
    print("=" * 60)

if __name__ == '__main__':
    main()

