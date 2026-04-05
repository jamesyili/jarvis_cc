#!/usr/bin/env python3
"""
One-time full-content scrape of Louis Wang's blog posts.
The RSS feed only provides descriptions; this fetches the full HTML from each post URL,
converts to markdown, and overwrites the stub articles in kb/hard/raw/louis-wang/.

Usage:
    python scripts/scrape_louis.py              # Scrape all posts
    python scripts/scrape_louis.py --dry-run    # Preview only
"""
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ingest import fetch_url, parse_feed, strip_html, slugify, KB_DIR
from build_index import build_raw_index

FEED_URL = "https://louiswang524.github.io/rss.xml"
OUTPUT_DIR = KB_DIR / "hard" / "raw" / "louis-wang"
DEFAULT_TAGS = ["llms", "recsys", "ai-agents", "ml-systems"]


def extract_blog_content(html):
    """Extract main article content from Louis Wang's blog HTML."""
    # Try to find the article/main content area
    # Look for <article> or <main> tags first
    article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    if article_match:
        content = article_match.group(1)
    else:
        main_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
        if main_match:
            content = main_match.group(1)
        else:
            # Fallback: look for the content div
            content_match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>\s*(?:<footer|<div[^>]*class="[^"]*footer)', html, re.DOTALL | re.IGNORECASE)
            if content_match:
                content = content_match.group(1)
            else:
                # Last resort: strip everything
                content = html

    # Convert to markdown
    md = strip_html(content)

    # Clean up excessive whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def scrape_all(dry_run=False):
    print("Fetching Louis Wang RSS feed...")
    xml = fetch_url(FEED_URL, timeout=30)
    entries = parse_feed(xml)
    print(f"Found {len(entries)} posts\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    updated = 0

    for title, url, description, pub_date in entries:
        slug = slugify(title)
        if not slug:
            continue
        filepath = OUTPUT_DIR / f"{slug}.md"

        print(f"  {title}")
        if dry_run:
            print(f"    → {filepath}")
            continue

        try:
            html = fetch_url(url, timeout=30)
            content = extract_blog_content(html)

            if len(content) < 100:
                print(f"    WARN: extracted content too short ({len(content)} chars), keeping description")
                content = description

            # Derive better tags from title
            tags = list(DEFAULT_TAGS)
            title_lower = title.lower()
            tag_keywords = {
                'recommend': 'recsys', 'retrieval': 'retrieval', 'attention': 'attention',
                'transformer': 'transformers', 'llm': 'llms', 'agent': 'ai-agents',
                'diffusion': 'generative-models', 'quantiz': 'quantization',
                'claude': 'claude-code', 'inference': 'inference',
            }
            for kw, tag in tag_keywords.items():
                if kw in title_lower and tag not in tags:
                    tags.append(tag)

            from datetime import date
            tags_str = ", ".join(tags)
            md = f"# {title}\n\n**Source:** {url}\n**Ingested:** {date.today().isoformat()}\n**Tags:** {tags_str}\n\n---\n\n{content}\n"

            filepath.write_text(md, encoding='utf-8')
            updated += 1
            print(f"    OK ({len(content)} chars)")

        except Exception as e:
            print(f"    ERROR: {e}")

        time.sleep(1)  # Rate limiting

    if not dry_run and updated > 0:
        print(f"\nRebuilding hard skills index...")
        build_raw_index("hard")

    print(f"\nDone. {updated} posts scraped.")


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    scrape_all(dry_run)
