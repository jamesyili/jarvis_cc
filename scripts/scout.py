#!/usr/bin/env python3
"""
Web scout — checks RSS feeds for new content across all tracked sources.
Deposits into kb/{hard|soft}/raw/{slug}/. Designed for cron.

Usage:
    python scripts/scout.py                    # Full scout (all RSS sources)
    python scripts/scout.py --source eugene-yan # Scout single source
    python scripts/scout.py --status           # Show last scout times
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ingest import RSS_SOURCES, check_rss_sources, load_manifest
from build_index import build_raw_index


def main():
    if "--status" in sys.argv:
        manifest = load_manifest()
        print("Last scout times:")
        for slug, _, _ in RSS_SOURCES:
            last = manifest.get("last_synced", {}).get(slug, "never")
            print(f"  {slug}: {last}")
        return

    sources = None
    if "--source" in sys.argv:
        idx = sys.argv.index("--source")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]
            sources = [s for s in RSS_SOURCES if s[0] == target]
            if not sources:
                print(f"Unknown source: {target}")
                print(f"Available: {', '.join(s[0] for s in RSS_SOURCES)}")
                sys.exit(1)

    print("=== Web Scout ===")
    try:
        created = check_rss_sources(sources)
        if created:
            # Rebuild indexes for affected domains
            hard_touched = any(
                slug in {"aman-ai", "chip-huyen", "eugene-yan", "lilian-weng", "karpathy",
                          "cameron-wolfe", "sebastian-raschka", "nathan-lambert",
                          "jay-alammar", "louis-wang"}
                for slug in created.keys()
            )
            soft_touched = any(
                slug in {"wes-kao", "jefferson-fisher", "ethan-evans", "lennys-podcast"}
                for slug in created.keys()
            )
            if hard_touched:
                print("\nRebuilding hard skills index...")
                build_raw_index("hard")
            if soft_touched:
                print("\nRebuilding soft skills index...")
                build_raw_index("soft")

        total = sum(len(v) for v in created.values())
        print(f"\nDone. {total} new articles across {len(created)} sources.")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
