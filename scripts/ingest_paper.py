#!/usr/bin/env python3
"""Ingest one paper James passes into kb/hard/raw/arxiv/ (design ratified 2026-09-07).

Accepts an arXiv id/URL, a local PDF, or a local .md translation. Writes a standard raw
article (# Title / **Source** / **Ingested** / **Tags** / --- / body), records it in the
ingest manifest, reports which learner-model concepts it inherits from, optionally marks
the evidence James's understanding gives (authored / discussed), and rebuilds the search
index. Stdlib only, apart from optional PDF extractors; works from Codex and Claude Code.

  python3 scripts/ingest_paper.py 2507.22224 --tags semantic-ids,generative-retrieval
  python3 scripts/ingest_paper.py https://arxiv.org/abs/2305.05065
  python3 scripts/ingest_paper.py ~/Downloads/paper.pdf --title "..." --tags ...
  python3 scripts/ingest_paper.py notes/paper.md --url https://... --tags ...
  python3 scripts/ingest_paper.py 2507.22224 --evidence discussed --note "walked Leo through the codebook trade-offs"
  python3 scripts/ingest_paper.py 2507.22224 --dry-run

PDF text: tries `pdftotext` (poppler), then `pypdf`, then `fitz` (PyMuPDF). If none works
the article carries the arXiv abstract plus a note, and the PDF can be re-run later with
`--pdf` once an extractor is installed (pip install pypdf).
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import ingest  # noqa: E402  (create_article_md, manifest, slugify)
import kb_knowledge_state as ks  # noqa: E402

SOURCE_SLUG = "arxiv"
ARXIV_API = "https://export.arxiv.org/api/query?id_list={id}"
ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")
USER_AGENT = "leo-kb-ingest/1.0 (+personal knowledge base)"


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_arxiv_id(text):
    m = ARXIV_ID_RE.search(text)
    return (m.group(1) + (m.group(2) or "")) if m else None


def arxiv_metadata(arxiv_id):
    """title, authors, abstract, published, categories, pdf_url, abs_url"""
    try:
        raw = http_get(ARXIV_API.format(id=arxiv_id))
    except Exception as exc:
        sys.exit(f"Could not reach export.arxiv.org ({exc.__class__.__name__}: {exc}). "
                 "If this machine's network blocks arXiv, download the PDF or an .md translation and pass the file instead.")
    root = ET.fromstring(raw)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = root.find("a:entry", ns)
    if entry is None or entry.find("a:title", ns) is None:
        sys.exit(f"arXiv API returned no entry for {arxiv_id}")
    title = re.sub(r"\s+", " ", entry.find("a:title", ns).text).strip()
    if title.lower().startswith("error"):
        sys.exit(f"arXiv API error for {arxiv_id}: {title}")
    authors = [a.find("a:name", ns).text for a in entry.findall("a:author", ns)]
    abstract = re.sub(r"\s+", " ", entry.find("a:summary", ns).text).strip()
    published = (entry.find("a:published", ns).text or "")[:10]
    cats = [c.get("term") for c in entry.findall("a:category", ns)]
    pdf_url = next((l.get("href") for l in entry.findall("a:link", ns) if l.get("title") == "pdf"), None)
    return {"title": title, "authors": authors, "abstract": abstract, "published": published,
            "categories": cats, "pdf_url": pdf_url or f"https://arxiv.org/pdf/{arxiv_id}",
            "abs_url": f"https://arxiv.org/abs/{arxiv_id}"}


# ---------------------------------------------------------------------------
# PDF text
# ---------------------------------------------------------------------------

def pdf_to_text(pdf_path):
    """Return (text, extractor) or (None, reason)."""
    pdf_path = str(pdf_path)
    if shutil.which("pdftotext"):
        try:
            out = subprocess.run(["pdftotext", "-layout", pdf_path, "-"], capture_output=True, text=True, timeout=180)
            if out.returncode == 0 and out.stdout.strip():
                return out.stdout, "pdftotext"
        except Exception:
            pass
    try:
        import pypdf  # type: ignore
        reader = pypdf.PdfReader(pdf_path)
        text = "\n".join((p.extract_text() or "") for p in reader.pages)
        if text.strip():
            return text, "pypdf"
    except Exception:
        pass
    try:
        import fitz  # type: ignore
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text() for page in doc)
        if text.strip():
            return text, "pymupdf"
    except Exception:
        pass
    return None, "no working PDF extractor (install poppler's pdftotext or `pip install pypdf`)"


def clean_text(text):
    text = text.replace("\f", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Article assembly
# ---------------------------------------------------------------------------

def body_from_arxiv(meta, fulltext, extractor_note):
    parts = [
        f"**Authors:** {', '.join(meta['authors'])}  ",
        f"**Published:** {meta['published']}  ",
        f"**arXiv categories:** {', '.join(meta['categories'])}  ",
        f"**PDF:** {meta['pdf_url']}",
        "",
        "## Abstract",
        "",
        meta["abstract"],
        "",
    ]
    if fulltext:
        parts += ["## Full text", "", f"*Extracted with {extractor_note} on {date.today().isoformat()}.*", "", fulltext]
    else:
        parts += [f"> Full text not extracted: {extractor_note}. Re-run with `--pdf <file>` once an extractor is available."]
    return "\n".join(parts)


def title_from_text(text, fallback):
    for line in text.splitlines():
        line = line.strip().lstrip("# ").strip()
        if len(line) > 8 and not line.lower().startswith(("abstract", "arxiv")):
            return line[:200]
    return fallback


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="arXiv id/URL, local .pdf, or local .md")
    ap.add_argument("--title", help="override title (required for a PDF whose first line is not the title)")
    ap.add_argument("--url", help="source URL to record for a local file")
    ap.add_argument("--tags", default="", help="comma-separated; concept slugs and wiki tags make inheritance exact")
    ap.add_argument("--pdf", help="local PDF to extract full text from (for an arXiv id when auto-download fails)")
    ap.add_argument("--evidence", choices=["authored", "discussed"],
                    help="mark James's understanding of the matched concepts as proven depth (>=3)")
    ap.add_argument("--note", default="", help="evidence note (with --evidence)")
    ap.add_argument("--by", default="claude", help="codex | claude | james")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-rebuild", action="store_true", help="skip the search-index rebuild")
    args = ap.parse_args(argv)

    tags = [ks.normalize_tag(t) for t in args.tags.split(",") if t.strip()]
    src = args.source
    src_path = Path(src).expanduser()
    fulltext, extractor = None, None

    if src_path.exists() and src_path.suffix.lower() == ".md":
        text = src_path.read_text(encoding="utf-8", errors="replace")
        title = args.title or title_from_text(text, src_path.stem)
        url = args.url or f"local://{src_path.name}"
        body = re.sub(r"^#\s+.*\n", "", text, count=1).strip()
        tags = tags or ["paper"]
    elif src_path.exists() and src_path.suffix.lower() == ".pdf":
        text, extractor = pdf_to_text(src_path)
        if text is None:
            sys.exit(f"Could not extract text from {src_path}: {extractor}")
        text = clean_text(text)
        title = args.title or title_from_text(text, src_path.stem)
        url = args.url or f"local://{src_path.name}"
        body = f"*Extracted with {extractor} on {date.today().isoformat()}.*\n\n{text}"
        tags = tags or ["paper"]
    else:
        arxiv_id = parse_arxiv_id(src)
        if not arxiv_id:
            sys.exit(f"Not an existing file and not an arXiv id/URL: {src}")
        meta = arxiv_metadata(arxiv_id)
        title = args.title or meta["title"]
        url = meta["abs_url"]
        pdf_source = Path(args.pdf).expanduser() if args.pdf else None
        if pdf_source is None:
            try:
                data = http_get(meta["pdf_url"], timeout=120)
                tmp = Path(tempfile.gettempdir()) / f"arxiv-{arxiv_id.replace('/', '_')}.pdf"
                tmp.write_bytes(data)
                pdf_source = tmp
            except Exception as exc:  # network or proxy issue — abstract-only article
                extractor = f"PDF download failed ({exc.__class__.__name__})"
        if pdf_source is not None:
            fulltext, extractor = pdf_to_text(pdf_source)
            if fulltext:
                fulltext = clean_text(fulltext)
        body = body_from_arxiv(meta, fulltext, extractor)
        tags = tags or ["paper"] + [c.lower().replace(".", "-") for c in meta["categories"][:2]]

    manifest = ingest.load_manifest()
    if url in manifest.get("ingested_urls", []) and not args.dry_run:
        print(f"already in manifest: {url}")

    if args.dry_run:
        print(f"[dry-run] title: {title}\n[dry-run] url:   {url}\n[dry-run] tags:  {', '.join(tags)}")
        print(f"[dry-run] body:  {len(body)} chars; full text: {'yes (' + extractor + ')' if fulltext else 'no'}")
        print("[dry-run] first lines:\n" + "\n".join(body.splitlines()[:8]))
        return

    path, created = ingest.create_article_md(title, SOURCE_SLUG, url, body, tags=tags)
    rel = path.relative_to(ROOT)
    if not created:
        print(f"exists, not overwritten: {rel}")
    else:
        manifest.setdefault("ingested_urls", []).append(url)
        ingest.save_manifest(manifest)
        print(f"wrote {rel} ({len(body)} chars; full text: {'yes' if fulltext else 'abstract only'})")

    state = ks.load_state()
    if state:
        inh = ks.inherit(state, path)
        print(f"inherits: understanding {inh['understanding']}, relevance {inh['relevance']}; concepts: {', '.join(inh['matched']) or 'none matched — add tags'}")
        if args.evidence and inh["matched"]:
            kind = "authored" if args.evidence == "authored" else "dialogue"
            note = args.note or f"{args.evidence}: {title}"
            for slug in inh["matched"]:
                cur = state["concepts"][slug]["understanding"]
                ks.set_levels(state, slug, understanding=max(cur, 3), note=note, kind=kind, by=args.by)
            ks.save_state(state)
            ks.render(state)
            ks.export(state)
            print(f"marked proven depth (>=3) on: {', '.join(inh['matched'])}")

    if not args.no_rebuild and created:
        import kb_search
        docs = kb_search.scan_articles()
        idf = kb_search.build_index(docs)
        kb_search.save_index(docs, idf)
        print(f"search index rebuilt: {len(docs)} documents")


if __name__ == "__main__":
    main()
