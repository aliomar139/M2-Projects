"""Check report completeness and preserve reproducible full-text search results."""
from pathlib import Path
import hashlib
import re
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
SOURCES = ROOT / "sources"
REPORT = ROOT / "10_Review_Papers_Dimension_Analysis.md"

COMMON_GROUPS = ["causal", "support", "confounding", "dropout", "sets"]
PAPERS = [(paper_id, filename, COMMON_GROUPS) for paper_id, filename in [
    ("R1", "PMC12816537.body.txt"),
    ("R2", "PMC11265144.body.txt"),
    ("R3", "PMC12616488.body.txt"),
    ("R4", "PMC12985454.body.txt"),
    ("R5", "PMC13047823.body.txt"),
    ("R6", "002.txt"),
    ("R7", "PMC10654618.body.txt"),
    ("R8", "PMC12747601.body.txt"),
    ("R9", "Han_2025.body.txt"),
    ("R10", "PMC9797865.body.txt"),
]]

TERMS = {
    "causal": [r"causal\w*", r"counterfactual\w*", r"propensity", r"confound\w*", r"doubly robust", r"treatment effects?"],
    "utility": [r"preferences?", r"utilit\w*", r"trade.?offs?", r"multi.?objective", r"priorities"],
    "retrieval": [r"retrieval", r"retriev\w*", r"ground\w*", r"citations?", r"guidelines?", r"provenance"],
    "abstain": [r"abstain\w*", r"abstention", r"selective prediction", r"reject option", r"defer\w*", r"withhold\w*", r"refus\w*"],
    "policy": [r"reinforcement learning", r"off.?policy", r"policy value", r"dynamic treatment", r"treatment polic\w*", r"sequential decision"],
    "dropout": [r"missing not at random", r"mnar", r"informative missing\w*", r"drop.?out", r"loss to follow", r"lost to follow", r"missing\w*"],
    "sets": [r"conformal", r"prediction sets?", r"treatment sets?", r"near.?optimal", r"multiple optimal", r"statistical coverage", r"equivalen\w*", r"indifference", r"non.?significan\w*"],
    "information": [r"value of information", r"value.of.information", r"information gain", r"active feature", r"next.?test", r"decision.theoretic", r"adaptive acquisition"],
    "economic": [r"cost\w*", r"economic\w*", r"quality.adjusted", r"qalys?", r"incremental cost"],
    "support": [r"positivity", r"common support", r"propensity", r"treatment overlap", r"overlap\w*", r"identifiab\w*", r"abstain\w*", r"abstention"],
    "confounding": [r"hidden confound\w*", r"unmeasured confound\w*", r"unobserved confound\w*", r"sensitivity analys\w*", r"confound\w*"],
    "ranking": [r"rank\w*", r"perturb\w*", r"stability", r"rank reversal", r"robust\w*"],
    "arbitration": [r"multi.?agent", r"disagree\w*", r"arbitrat\w*", r"conflicts?", r"consensus"],
    "mcid": [r"mcid", r"proms?", r"patient.reported outcome", r"minim\w* clinically important", r"meaningful improvement"],
}


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"(?<=\w)[-\u2010-\u2015]\s*\n\s*(?=\w)", "", text)
    return re.sub(r"\s+", " ", text).lower()


def main_article_text(filename):
    """Use JATS scientific sections; omit back matter and supplementary stubs."""
    xml_path = SOURCES / filename.replace(".body.txt", ".xml")
    if filename.endswith(".body.txt") and xml_path.exists():
        body = ET.parse(xml_path).find(".//body")
        excluded = {"references", "abbreviations", "associated data", "supplementary materials",
                    "supplemental material", "supporting information", "contributor information"}

        def walk(element):
            title = element.find("title")
            if title is not None and "".join(title.itertext()).strip().lower() in excluded:
                return []
            if element.tag in {"p", "title", "table", "caption"}:
                return ["".join(element.itertext())]
            parts = []
            for child in element:
                parts.extend(walk(child))
            return parts

        return "\n\n".join(walk(body))
    # R6 is corroborated against the full PMC HTML article; remove repository additions.
    text = (SOURCES / filename).read_text(encoding="utf-8")
    start = text.find("Introduction")
    end = text.find("Supplemental Material", start)
    return text[start:end]


def main():
    report = REPORT.read_text(encoding="utf-8")
    sections = re.split(r"\n## (R\d+)\. ", report)
    paper_sections = {sections[i]: sections[i + 1] for i in range(1, len(sections), 2)}
    assert len(paper_sections) == 10
    for paper_id, text in paper_sections.items():
        assert len(re.findall(r"^\| (?:10|[1-9]) \|", text, re.M)) == 10, paper_id
        assert not re.findall(r"^\| N[1-5] \|", text, re.M), paper_id
    shared_rows = re.findall(r"^\| (N[1-5]) \| ([^|]+) \|", report, re.M)
    assert len(shared_rows) == 5
    assert {key for key, _ in shared_rows} == {f"N{i}" for i in range(1, 6)}
    notes = list((ROOT.parent / "review papers").glob("*.md"))
    assert len(notes) == 10
    for note in notes:
        text = note.read_text(encoding="utf-8")
        assert len(re.findall(r"^\| (?:10|[1-9]) \|", text, re.M)) == 10, note
        assert re.findall(r"^\| (N[1-5]) \| ([^|]+) \|", text, re.M) == shared_rows, note
    shared_document = (ROOT / "Five_Shared_New_Dimensions.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^## N[1-5]\. ", shared_document, re.M)) == 5
    assert len(re.findall(r"^\| R\d+ .*?\| ND \| ND \| ND \| ND \| ND \|$", shared_document, re.M)) == 10

    lines = [
        "# Full-text verification audit",
        "",
        "Date: 24 October 2026. Corrected scope: 10 reviews, 100 covered dimensions, FIVE shared proposed additions. The same five concepts are checked in every review, giving 50 paper-by-dimension coverage checks, not 50 new dimensions.",
        "",
        "## What this audit establishes",
        "",
        "The searches below support the conceptual reading recorded in Five_Shared_New_Dimensions.md. They do not independently prove absence. Nonzero hits require context review; zero hits do not rule out synonyms or implicit coverage. The shared report's nearest-topic explanation is the interpretation of those checks.",
        "",
        "Search scope: main article body, embedded tables, and available figure captions. Bibliographies and separately hosted supplements are excluded. R6 was checked against full PMC HTML as well as its repository rendering. Extracted PDF page numbers, where present, are file page numbers rather than journal pagination.",
        "",
        "Publisher/PMC metadata and review labels were checked online. Nine reviews also have downloaded Europe PMC JATS XML; R6's Europe PMC XML endpoint returned an error, so the complete PMC HTML and local body were used.",
        "",
        "Search expressions are case-insensitive and normalized for whitespace/ligatures. Context excerpts are short audit aids, not a substitute for the source.",
        "",
        "## Important rejected absence claims",
        "",
        "- R1: nonsurgical alternatives, psychosocial outcomes, cost, and generic value of information already appear. Its value-of-information wording concerns decision-aid evaluation, not mathematical next-test selection; the latter was nevertheless not assigned as a new R1 dimension.",
        "- R5: retrieval grounding, prompt injection, lifecycle monitoring, and preferences in clinical notes already appear.",
        "- R8: adaptive rehabilitation and cost-effectiveness already appear.",
        "- R9: multiobjective surgical optimization and Bayesian uncertainty already appear. Legal causality is not causal treatment-effect identification.",
        "- Generic agent handoff quality is explicitly discussed in R5 and is excluded from the five shared additions.",
        "- R1 and R2 mention generic missing values. These mentions do not discuss outcome-dependent follow-up loss. R1 also reports a nonsignificant study result, which is not a clinical-equivalence treatment-set criterion.",
        "",
    ]
    for paper_id, filename, groups in PAPERS:
        source = SOURCES / filename
        raw = source.read_bytes()
        article = main_article_text(filename)
        text = normalize(article)
        (SOURCES / f"{paper_id}_checked_main_text.txt").write_text(article, encoding="utf-8")
        lines += [f"## {paper_id}", "", f"Source extraction: [full text](sources/{filename}).",
                  f"SHA-256 of extraction: `{hashlib.sha256(raw).hexdigest()}`.",
                  f"Checked main-text length: {len(article):,} characters.", "",
                  "| Proposal | Concept searches | Main-text matches |",
                  "|---|---|---|"]
        for index, group in enumerate(groups, 1):
            expressions = TERMS[group]
            matches = [(term, list(re.finditer(r"\b(?:" + term + r")\b", text))) for term in expressions]
            counts = "; ".join(f"{term}: {len(hits)}" for term, hits in matches)
            lines.append(f"| N{index} | {group} | {counts} |")
        lines += ["", "Nonzero-match context notes (interpret alongside the report):", ""]
        seen = set()
        for group in groups:
            for term in TERMS[group]:
                hits = list(re.finditer(r"\b(?:" + term + r")\b", text))
                if not hits or term in seen:
                    continue
                seen.add(term)
                # Limit quotation: at most 8 words per example and 3 examples per paper.
                if len(seen) > 3:
                    continue
                hit = hits[0]
                snippet = " ".join(text[max(0, hit.start() - 20):hit.end() + 55].split()[:8])
                lines.append(f'- `{term}` occurs; example: "{snippet}". A related word is not automatically the proposed capability.')
        if not seen:
            lines.append("- No search-expression hits for the selected proposals; conceptual boundaries are documented in the report.")
        lines.append("")
    (ROOT / "verification_audit.md").write_text("\n".join(lines), encoding="utf-8")
    print("PASS: 10 reviews; 100 covered dimensions; five shared additions; identical N1-N5 definitions in all ten notes; 50 cross-paper coverage checks.")
    print("Wrote verification_audit.md and ten checked-main-text extracts.")


if __name__ == "__main__":
    main()
