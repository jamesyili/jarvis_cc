#!/usr/bin/env python3
"""
Re-scrape aman.ai articles — replaces 9-line stubs with full HTML-to-markdown content.

Reads existing stub files to get URLs, fetches actual page content,
converts HTML to markdown, and overwrites the stubs.

Usage:
    python scripts/rescrape_aman.py              # Re-scrape all stubs
    python scripts/rescrape_aman.py --dry-run    # Show what would be scraped
    python scripts/rescrape_aman.py --status     # Count stubs vs real content
    python scripts/rescrape_aman.py --limit 10   # Scrape only N articles
"""
import sys
import re
import time
import argparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


AMAN_DIR = Path(__file__).parent.parent / "kb" / "hard" / "raw" / "aman-ai"
RATE_LIMIT = 1.5  # seconds between requests
STUB_LINE_THRESHOLD = 12  # files with <= this many lines are stubs
TIMEOUT = 30


def parse_stub(filepath: Path) -> dict | None:
    """Extract metadata from an existing stub file."""
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


def fetch_and_convert(url: str) -> str | None:
    """Fetch an aman.ai page and convert to markdown."""
    try:
        r = requests.get(url, timeout=TIMEOUT, headers={
            "User-Agent": "Mozilla/5.0 (compatible; KBBot/1.0)"
        })
        r.raise_for_status()
    except Exception as e:
        print(f"  FETCH ERROR: {e}")
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    article = soup.find("article")
    if not article:
        # Try fallback selectors
        article = soup.select_one(".post-content") or soup.find("main")
    if not article:
        print(f"  NO CONTENT FOUND")
        return None

    # Remove non-content elements
    for tag in article.find_all(["script", "style", "nav"]):
        tag.decompose()
    for el in article.find_all(id="toc"):
        el.decompose()
    for el in article.find_all(class_="toc"):
        el.decompose()

    # Convert to markdown
    content = md(
        str(article),
        heading_style="ATX",
        strip=["img"],  # strip images (they're broken without hosting)
    )

    # Clean up
    content = re.sub(r"\n{3,}", "\n\n", content)
    content = content.strip()

    if len(content) < 200:
        print(f"  CONTENT TOO SHORT ({len(content)} chars)")
        return None

    return content


def write_article(meta: dict, content: str):
    """Write the full article file, preserving metadata."""
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


def get_stubs() -> list[dict]:
    """Find all stub files in aman-ai directory."""
    stubs = []
    for f in sorted(AMAN_DIR.glob("*.md")):
        if f.name.startswith("_"):
            continue
        meta = parse_stub(f)
        if meta and meta["lines"] <= STUB_LINE_THRESHOLD:
            stubs.append(meta)
    return stubs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    stubs = get_stubs()
    real = len(list(AMAN_DIR.glob("*.md"))) - len(stubs)

    if args.status:
        print(f"aman-ai directory: {AMAN_DIR}")
        print(f"  Stub files (≤{STUB_LINE_THRESHOLD} lines): {len(stubs)}")
        print(f"  Real content files: {real}")
        return

    if args.dry_run:
        print(f"Would re-scrape {len(stubs)} stub files:")
        for s in stubs[:20]:
            print(f"  {s['path'].name} → {s['url']}")
        if len(stubs) > 20:
            print(f"  ... and {len(stubs) - 20} more")
        return

    target = stubs[:args.limit] if args.limit > 0 else stubs
    print(f"=== Re-scraping {len(target)} aman.ai stubs ===\n")

    success = 0
    failed = 0

    for i, meta in enumerate(target):
        name = meta["path"].name
        url = meta["url"]
        print(f"[{i+1}/{len(target)}] {name}")
        print(f"  URL: {url}")

        content = fetch_and_convert(url)
        if content:
            lines = len(content.split("\n"))
            chars = len(content)
            write_article(meta, content)
            print(f"  OK: {lines} lines, {chars:,} chars")
            success += 1
        else:
            failed += 1

        if i < len(target) - 1:
            time.sleep(RATE_LIMIT)

    print(f"\n=== Done: {success} scraped, {failed} failed ===")


if __name__ == "__main__":
    main()
