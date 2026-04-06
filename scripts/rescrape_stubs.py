#!/usr/bin/env python3
"""
Re-scrape stub articles across all KB sources.
Replaces 9-line stubs with full HTML-to-markdown content.

Usage:
    python scripts/rescrape_stubs.py                    # Re-scrape all stubs
    python scripts/rescrape_stubs.py --source lilian-weng
    python scripts/rescrape_stubs.py --source eugene-yan
    python scripts/rescrape_stubs.py --dry-run
    python scripts/rescrape_stubs.py --status
    python scripts/rescrape_stubs.py --limit 10
"""
import sys
import re
import time
import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


KB_RAW = Path(__file__).parent.parent / "kb" / "hard" / "raw"
RATE_LIMIT = 1.5
STUB_LINE_THRESHOLD = 12
TIMEOUT = 30

# Site-specific content selectors (ordered by priority)
SITE_SELECTORS = {
    "aman-ai": ["article", ".post-content"],
    "lilian-weng": ["article", ".post-content"],
    "eugene-yan": [".notebody", ".note", "article"],
    "karpathy": ["article", ".post-content"],
    "jay-alammar": ["article", ".post-content", ".entry-content"],
    "simon-willison": [".entry", "article", ".entry-content", ".post-content"],
    # Fallback for unknown sites
    "_default": ["article", ".post-content", ".entry-content", "main"],
}


def parse_stub(filepath: Path) -> dict | None:
    lines = filepath.read_text().strip().split("\n")
    meta = {"path": filepath, "lines": len(lines)}
    for line in lines:
        if line.startswith("**Source:**"):
            meta["url"] = line.replace("**Source:**", "").strip()
        elif line.startswith("**Ingested:**"):
            meta["ingested"] = line.replace("**Ingested:**", "").strip()
        elif line.startswith("**Tags:**"):
            meta["tags"] = line.replace("**Tags:**", "").strip()
        elif line.startswith("# "):
            meta["title"] = line.replace("# ", "").strip()
    return meta if "url" in meta else None


def get_selectors(source: str) -> list[str]:
    return SITE_SELECTORS.get(source, SITE_SELECTORS["_default"])


def fetch_and_convert(url: str, source: str) -> str | None:
    # Strip URL fragments
    url = url.split("#")[0]
    try:
        r = requests.get(url, timeout=TIMEOUT, headers={
            "User-Agent": "Mozilla/5.0 (compatible; KBBot/1.0)"
        })
        r.raise_for_status()
    except Exception as e:
        print(f"  FETCH ERROR: {e}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    content_el = None
    for sel in get_selectors(source):
        if sel.startswith("."):
            content_el = soup.select_one(sel)
        else:
            content_el = soup.find(sel)
        if content_el:
            break

    if not content_el:
        print(f"  NO CONTENT FOUND (tried: {get_selectors(source)})")
        return None

    for tag in content_el.find_all(["script", "style", "nav"]):
        tag.decompose()
    for el in content_el.find_all(id="toc"):
        el.decompose()
    for el in content_el.find_all(class_="toc"):
        el.decompose()

    content = md(str(content_el), heading_style="ATX", strip=["img"])
    content = re.sub(r"\n{3,}", "\n\n", content)
    content = content.strip()

    if len(content) < 200:
        print(f"  CONTENT TOO SHORT ({len(content)} chars)")
        return None

    return content


def write_article(meta: dict, content: str):
    title = meta.get("title", "Untitled")
    url = meta["url"]
    tags = meta.get("tags", "")
    ingested = meta.get("ingested", "2026-04-02")

    output = f"""# {title}

**Source:** {url}
**Ingested:** {ingested}
**Re-scraped:** 2026-04-05
**Tags:** {tags}

---

{content}
"""
    meta["path"].write_text(output)


def get_stubs(source_dir: Path) -> list[dict]:
    stubs = []
    for f in sorted(source_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        meta = parse_stub(f)
        if meta and meta["lines"] <= STUB_LINE_THRESHOLD:
            stubs.append(meta)
    return stubs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="Specific source to rescrape")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--reformat", action="store_true",
                        help="Re-scrape ALL files (not just stubs) for a source — use to fix bad formatting")
    args = parser.parse_args()

    # Find sources with stubs (or all files if --reformat)
    sources = {}
    for d in sorted(KB_RAW.iterdir()):
        if not d.is_dir() or d.name.startswith("_") or d.name == "do_not_index_sources":
            continue
        if args.source and d.name != args.source:
            continue
        if args.reformat:
            # Get ALL files with URLs, not just stubs
            all_files = []
            for f in sorted(d.glob("*.md")):
                if f.name.startswith("_"):
                    continue
                meta = parse_stub(f)
                if meta:
                    all_files.append(meta)
            if all_files:
                sources[d.name] = all_files
        else:
            stubs = get_stubs(d)
            if stubs:
                sources[d.name] = stubs

    if args.status:
        for name, stubs in sources.items():
            total = len(list((KB_RAW / name).glob("*.md")))
            print(f"{name}: {len(stubs)} stubs / {total} total")
        if not sources:
            print("No stubs found.")
        return

    if args.dry_run:
        for name, stubs in sources.items():
            print(f"\n{name}: {len(stubs)} stubs to re-scrape")
            for s in stubs[:5]:
                print(f"  {s['path'].name} → {s['url']}")
            if len(stubs) > 5:
                print(f"  ... and {len(stubs) - 5} more")
        return

    total_success = 0
    total_failed = 0

    for source_name, stubs in sources.items():
        target = stubs[:args.limit] if args.limit > 0 else stubs
        print(f"\n=== Re-scraping {len(target)} {source_name} stubs ===\n")

        for i, meta in enumerate(target):
            name = meta["path"].name
            url = meta["url"]
            print(f"[{i+1}/{len(target)}] {name}")
            print(f"  URL: {url}")

            content = fetch_and_convert(url, source_name)
            if content:
                lines = len(content.split("\n"))
                chars = len(content)
                write_article(meta, content)
                print(f"  OK: {lines} lines, {chars:,} chars")
                total_success += 1
            else:
                total_failed += 1

            if i < len(target) - 1:
                time.sleep(RATE_LIMIT)

    print(f"\n=== Done: {total_success} scraped, {total_failed} failed ===")


if __name__ == "__main__":
    main()
