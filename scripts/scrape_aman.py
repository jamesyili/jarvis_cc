#!/usr/bin/env python3
"""
Aman.ai scraper — fetches new content and deposits into kb/hard/raw/aman-ai/.
Designed for cron. Idempotent, no interactive prompts, logs to stdout.

Usage:
    python scripts/scrape_aman.py          # Scrape new content
    python scripts/scrape_aman.py --status # Show last scrape info
"""
import sys
from pathlib import Path

# Reuse ingest infrastructure
sys.path.insert(0, str(Path(__file__).parent))
from ingest import ingest_aman, load_manifest, show_status
from build_index import build_raw_index


def main():
    if "--status" in sys.argv:
        manifest = load_manifest()
        last = manifest.get("last_synced", {}).get("aman-ai", "never")
        urls = len(manifest.get("ingested_urls", []))
        print(f"aman-ai last scraped: {last}")
        print(f"Total ingested URLs (all sources): {urls}")
        return

    print("=== Aman.ai Scraper ===")
    try:
        created = ingest_aman(check_only=False)
        if created:
            print(f"\nRebuilding hard skills index...")
            build_raw_index("hard")
        print(f"\nDone. {len(created)} new articles.")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
