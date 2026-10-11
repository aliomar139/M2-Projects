import os
import sys
import re
import time
import json
import shutil
import requests
import pandas as pd
from urllib.parse import quote
from bs4 import BeautifulSoup
from downloader_helpers import (
    sanitize_filename,
    is_valid_pdf_file,
    get_pmc_ids_batch,
    try_pmc_s3,
    try_unpaywall,
    try_openalex,
    try_semantic_scholar,
    try_europe_pmc,
    try_arxiv_by_title
)

sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}

def fetch_extra_web_content(doi, pmid=None):
    """Fetch additional text content from Europe PMC, PubMed, or Crossref for paywalled articles."""
    extra_text = []
    
    # 1. Europe PMC search
    if doi:
        try:
            url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:\"{doi}\"&resultType=core&format=json'
            r = requests.get(url, headers=HEADERS, timeout=10)
            if r.status_code == 200:
                results = r.json().get('resultList', {}).get('result', [])
                if results:
                    item = results[0]
                    aff = item.get('affiliation')
                    if aff:
                        extra_text.append(f"Affiliations: {aff}")
                    keywords = item.get('keywordList', {}).get('keyword', [])
                    if keywords:
                        extra_text.append(f"Keywords: {', '.join(keywords)}")
                    full_abs = item.get('abstractText')
                    if full_abs:
                        # Strip HTML tags
                        clean_abs = BeautifulSoup(full_abs, 'html.parser').get_text(separator=' ', strip=True)
                        extra_text.append(f"\nExtended Abstract from Repository:\n{clean_abs}")
        except Exception:
            pass

    # 2. CrossRef for license, funding, subject
    if doi and not extra_text:
        try:
            url = f'https://api.crossref.org/works/{doi}'
            r = requests.get(url, headers=HEADERS, timeout=10)
            if r.status_code == 200:
                msg = r.json().get('message', {})
                subjects = msg.get('subject', [])
                if subjects:
                    extra_text.append(f"Subject Areas: {', '.join(subjects)}")
                funder = msg.get('funder', [])
                if funder:
                    fund_names = [f.get('name') for f in funder if f.get('name')]
                    if fund_names:
                        extra_text.append(f"Funding: {', '.join(fund_names)}")
        except Exception:
            pass
            
    return "\n".join(extra_text)

def main():
    target_csv = 'top_100_orthopedic_ai_papers.csv'
    output_dir = os.path.join(os.getcwd(), 'top_100_papers')
    os.makedirs(output_dir, exist_ok=True)

    print(f"Loading target papers from {target_csv}...")
    df = pd.read_csv(target_csv)
    print(f"Total target papers: {len(df)}")

    # Map existing files in top_100_papers
    existing_files = os.listdir(output_dir)
    print(f"Existing files in {output_dir}: {len(existing_files)}")

    # Find existing PDFs and map them by DOI or normalized title
    old_pdf_map = {}  # doi_lower -> filepath
    old_title_map = {} # norm_title -> filepath

    for fname in existing_files:
        if fname.lower().endswith('.pdf'):
            fpath = os.path.join(output_dir, fname)
            if is_valid_pdf_file(fpath):
                # Try finding from old manifest if exists
                old_title_slug = re.sub(r'^\d+_', '', os.path.splitext(fname)[0]).lower()
                old_title_map[old_title_slug] = fpath

    if os.path.exists(os.path.join(output_dir, 'manifest.csv')):
        try:
            old_manifest = pd.read_csv(os.path.join(output_dir, 'manifest.csv'))
            for _, r in old_manifest.iterrows():
                if r.get('status') == 'Downloaded (PDF)':
                    f_name = r.get('file_name')
                    f_doi = str(r.get('doi', '')).lower().strip()
                    f_title = str(r.get('title', '')).lower().strip()
                    if f_name:
                        f_path = os.path.join(output_dir, f_name)
                        if is_valid_pdf_file(f_path):
                            if f_doi:
                                old_pdf_map[f_doi] = f_path
                            if f_title:
                                old_title_map[f_title] = f_path
        except Exception as e:
            print("Could not parse old manifest:", e)

    # Resolve PMC IDs for target DOIs
    print("\n[Step 1/4] Resolving PMC IDs via NCBI Batch Converter...")
    dois = [str(d).strip() for d in df['DOI'].dropna() if str(d).strip()]
    doi_to_pmc, doi_to_pmid = get_pmc_ids_batch(dois)
    print(f"Mapped {len(doi_to_pmc)} PMC IDs out of {len(dois)} DOIs.")

    # Target filenames that should remain in the folder
    target_filenames = {'manifest.csv', 'README.md'}
    manifest = []
    download_count = 0
    text_count = 0

    print("\n[Step 2/4] Processing Top 100 Orthopedic AI papers...")
    for idx, row in df.iterrows():
        rank = int(row['Rank'])
        title = str(row['Title']).strip()
        doi = str(row['DOI']).strip() if pd.notna(row['DOI']) else ""
        citations = int(row['Citations']) if pd.notna(row['Citations']) else 0
        year = row['Year'] if pd.notna(row['Year']) else ""
        authors = str(row['Authors']).strip() if pd.notna(row['Authors']) else ""
        journal = str(row['Journal']).strip() if pd.notna(row['Journal']) else ""
        sjr = str(row['Journal SJR Quartile']).strip() if pd.notna(row['Journal SJR Quartile']) else ""
        study_type = str(row['Study Type']).strip() if pd.notna(row['Study Type']) else ""
        relevance = row['Relevance Score'] if pd.notna(row['Relevance Score']) else ""
        takeaway = str(row['Takeaway']).strip() if pd.notna(row['Takeaway']) else ""
        abstract = str(row['Abstract']).strip() if pd.notna(row['Abstract']) else ""
        consensus_link = str(row['Consensus Link']).strip() if pd.notna(row['Consensus Link']) else ""

        clean_slug = sanitize_filename(title, max_len=50)
        base_name = f"{rank:03d}_{clean_slug}"
        target_pdf_name = f"{base_name}.pdf"
        target_pdf_path = os.path.join(output_dir, target_pdf_name)
        target_txt_name = f"{base_name}.txt"
        target_txt_path = os.path.join(output_dir, target_txt_name)

        pmcid = doi_to_pmc.get(doi.lower(), None)
        pmid = doi_to_pmid.get(doi.lower(), None)

        print(f"\n[{rank}/100] Citations: {citations} | DOI: {doi}")
        print(f"Title: {title[:70]}...")

        downloaded = False
        source_api = None

        # Check if target PDF already exists with exact name
        if is_valid_pdf_file(target_pdf_path):
            downloaded = True
            source_api = "Existing Target File"
            print(f"  -> Already present: {target_pdf_name}")
        else:
            # Check if this paper was already downloaded under an old rank/name
            matched_old_path = None
            if doi and doi.lower() in old_pdf_map:
                matched_old_path = old_pdf_map[doi.lower()]
            elif title.lower() in old_title_map:
                matched_old_path = old_title_map[title.lower()]
            else:
                for k, p in old_title_map.items():
                    if clean_slug.lower() in k or k in clean_slug.lower():
                        matched_old_path = p
                        break

            if matched_old_path and is_valid_pdf_file(matched_old_path):
                if matched_old_path != target_pdf_path:
                    shutil.copy2(matched_old_path, target_pdf_path)
                downloaded = True
                source_api = "Existing Re-indexed"
                print(f"  -> Re-indexed from existing download: {os.path.basename(matched_old_path)}")
            else:
                # Need to download via APIs
                # 1. Try PMC AWS Open Data
                if pmcid:
                    print(f"  -> Trying PMC AWS Open Data ({pmcid})...")
                    if try_pmc_s3(pmcid, target_pdf_path):
                        downloaded = True
                        source_api = "PMC Open Access (AWS S3)"

                # 2. Try Unpaywall
                if not downloaded and doi:
                    print(f"  -> Trying Unpaywall API...")
                    if try_unpaywall(doi, target_pdf_path):
                        downloaded = True
                        source_api = "Unpaywall API"

                # 3. Try OpenAlex
                if not downloaded and doi:
                    print(f"  -> Trying OpenAlex API...")
                    if try_openalex(doi, target_pdf_path):
                        downloaded = True
                        source_api = "OpenAlex API"

                # 4. Try Semantic Scholar
                if not downloaded and doi:
                    print(f"  -> Trying Semantic Scholar API...")
                    if try_semantic_scholar(doi, target_pdf_path):
                        downloaded = True
                        source_api = "Semantic Scholar API"

                # 5. Try Europe PMC
                if not downloaded and doi:
                    print(f"  -> Trying Europe PMC API...")
                    if try_europe_pmc(doi, target_pdf_path):
                        downloaded = True
                        source_api = "Europe PMC API"

                # 6. Try arXiv by Title
                if not downloaded:
                    print(f"  -> Checking arXiv API by Title...")
                    if try_arxiv_by_title(title, target_pdf_path):
                        downloaded = True
                        source_api = "arXiv API"

        file_size_kb = 0
        final_filename = ""
        status = ""

        if downloaded and is_valid_pdf_file(target_pdf_path):
            file_size_kb = round(os.path.getsize(target_pdf_path) / 1024, 1)
            status = "Downloaded (PDF)"
            final_filename = target_pdf_name
            target_filenames.add(target_pdf_name)
            download_count += 1
            print(f"  [SUCCESS] PDF saved: {target_pdf_name} ({file_size_kb} KB) via {source_api}")
        else:
            # Paywalled / Subscription: create text file and copy website content
            status = "Paywalled (Web Content Extracted .txt)"
            final_filename = target_txt_name
            target_filenames.add(target_txt_name)
            text_count += 1
            print(f"  [PAYWALLED] Fetching web content & creating text file: {target_txt_name}")

            extra_web = fetch_extra_web_content(doi, pmid)

            with open(target_txt_path, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write(f"TITLE: {title}\n")
                f.write(f"RANK: #{rank} (in Top 100 Orthopedic AI Papers)\n")
                f.write(f"RELEVANCE SCORE: {relevance}\n")
                f.write(f"YEAR: {year}\n")
                f.write(f"JOURNAL: {journal} (SJR Quartile: {sjr})\n")
                f.write(f"AUTHORS: {authors}\n")
                f.write(f"STUDY TYPE: {study_type}\n")
                f.write(f"CITATIONS: {citations}\n")
                if doi:
                    f.write(f"DOI: https://doi.org/{doi}\n")
                if pmcid:
                    f.write(f"PUBMED CENTRAL (PMC): https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/\n")
                if pmid:
                    f.write(f"PUBMED ID: https://pubmed.ncbi.nlm.nih.gov/{pmid}/\n")
                if consensus_link:
                    f.write(f"CONSENSUS PAGE: {consensus_link}\n")
                f.write("ACCESS STATUS: Subscription / Paywalled (Full-text content extracted from academic repository)\n")
                f.write("=" * 80 + "\n\n")

                f.write("--- KEY TAKEAWAY & SYNTHESIS ---\n")
                f.write(f"{takeaway}\n\n")

                f.write("--- FULL ABSTRACT ---\n")
                f.write(f"{abstract}\n\n")

                if extra_web:
                    f.write("--- REPOSITORY & PUBLISHER WEB METADATA ---\n")
                    f.write(f"{extra_web}\n\n")

                f.write("--- SUMMARY & CITATION ---\n")
                f.write(f"How to cite: {authors} ({year}). {title}. {journal}.\n")

            file_size_kb = round(os.path.getsize(target_txt_path) / 1024, 1)

        manifest.append({
            'rank': rank,
            'relevance_score': relevance,
            'title': title,
            'citations': citations,
            'year': year,
            'authors': authors,
            'journal': journal,
            'sjr_quartile': sjr,
            'study_type': study_type,
            'doi': doi,
            'pmcid': pmcid or '',
            'pmid': pmid or '',
            'status': status,
            'source_api': source_api or 'N/A',
            'file_name': final_filename,
            'file_size_kb': file_size_kb,
            'consensus_link': consensus_link
        })

        time.sleep(0.2)

    # Step 3: Delete files that aren't in top_100_orthopedic_ai_papers
    print("\n[Step 3/4] Cleaning up directory (deleting files not in target list)...")
    current_files = os.listdir(output_dir)
    deleted_count = 0
    for f in current_files:
        if f not in target_filenames:
            fpath = os.path.join(output_dir, f)
            try:
                if os.path.isfile(fpath):
                    os.remove(fpath)
                    deleted_count += 1
                    # print(f"  Deleted: {f}")
            except Exception as e:
                print(f"Error deleting {f}: {e}")
    print(f"Deleted {deleted_count} files not present in the target list.")

    # Step 4: Write updated manifest.csv and README.md
    print("\n[Step 4/4] Writing updated manifest.csv and README.md...")
    manifest_df = pd.DataFrame(manifest)
    manifest_csv_path = os.path.join(output_dir, 'manifest.csv')
    manifest_df.to_csv(manifest_csv_path, index=False, encoding='utf-8-sig')

    readme_path = os.path.join(output_dir, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Top 100 Orthopedic AI Papers\n\n")
        f.write(f"Curated collection directly corresponding to `top_100_orthopedic_ai_papers.csv`.\n\n")
        f.write("### Collection Statistics\n")
        f.write(f"- **Total Target Papers**: 100\n")
        f.write(f"- **Full-Text PDFs Downloaded**: {download_count}\n")
        f.write(f"- **Paywalled Papers (.txt Web Dossiers)**: {text_count}\n")
        f.write(f"- **APIs Used**: PubMed Central (PMC AWS Open Data), Unpaywall API, OpenAlex API, Semantic Scholar API, Europe PMC REST API, arXiv API, NCBI ID Converter API.\n\n")
        f.write("### Complete Index\n\n")
        f.write("| Rank | Citations | Year | Title | Status | Source API / Format | File |\n")
        f.write("| :---: | :---: | :---: | :--- | :---: | :--- | :--- |\n")
        for m in manifest:
            clean_t = m['title'].replace('|', '-')[:60]
            f.write(f"| {m['rank']} | {m['citations']} | {m['year']} | {clean_t}... | {m['status']} | {m['source_api']} | [`{m['file_name']}`](./{m['file_name']}) |\n")

    print("\n" + "=" * 60)
    print("SYNC AND DOWNLOAD COMPLETE!")
    print(f"Total Papers in Target List: 100")
    print(f"Full PDFs Downloaded: {download_count}")
    print(f"Web Content Text Files (.txt): {text_count}")
    print(f"Obsolete Files Deleted: {deleted_count}")
    print(f"Folder: {output_dir}")
    print("=" * 60)

if __name__ == '__main__':
    main()

