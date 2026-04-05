#!/usr/bin/env python3
"""
KB lint — health checks for the knowledge base.

Usage:
    python scripts/kb_lint.py              # Full lint
    python scripts/kb_lint.py --domain hard  # Lint hard only
    python scripts/kb_lint.py --json       # Machine-readable output

Checks:
  1. Thin articles (< 3 substantive lines of content)
  2. Missing metadata (no title heading or no tags)
  3. Broken wikilinks (referenced files that don't exist)
  4. Near-duplicate slugs (edit distance <= 2)
  5. Empty source directories
"""
import json
import re
import sys
from pathlib import Path

KB = Path(__file__).parent.parent / "kb"

THIN_THRESHOLD = 3  # minimum substantive content lines


def _is_substantive(line):
    """Check if a line is substantive content (not metadata, frontmatter, or blank)."""
    stripped = line.strip()
    if not stripped:
        return False
    if stripped == "---":
        return False
    if stripped.startswith("**Source:**") or stripped.startswith("**Ingested:**") or stripped.startswith("**Tags:**"):
        return False
    if stripped.startswith("# "):
        return False
    if re.match(r'^(tags|source|ingested_at|type|status|concept|last_compiled|related|sources):', stripped):
        return False
    return True


def _edit_distance(a, b):
    """Levenshtein distance between two strings."""
    if len(a) < len(b):
        return _edit_distance(b, a)
    if len(b) == 0:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            cost = 0 if ca == cb else 1
            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[len(b)]


def check_thin_articles(domains):
    """Find articles with fewer than THIN_THRESHOLD substantive lines."""
    issues = []
    for domain in domains:
        raw_dir = KB / domain / "raw"
        if not raw_dir.exists():
            continue
        for slug_dir in sorted(raw_dir.iterdir()):
            if not slug_dir.is_dir() or slug_dir.name in ("do_not_index_sources",):
                continue
            for f in sorted(slug_dir.glob("*.md")):
                if f.name == "_index.md":
                    continue
                try:
                    lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
                except Exception:
                    continue
                substantive = [l for l in lines if _is_substantive(l)]
                if len(substantive) < THIN_THRESHOLD:
                    issues.append({
                        "check": "thin_article",
                        "path": str(f.relative_to(KB)),
                        "detail": f"{len(substantive)} substantive lines",
                    })
    return issues


def check_missing_metadata(domains):
    """Find articles missing title heading or tags."""
    issues = []
    for domain in domains:
        raw_dir = KB / domain / "raw"
        if not raw_dir.exists():
            continue
        for slug_dir in sorted(raw_dir.iterdir()):
            if not slug_dir.is_dir() or slug_dir.name in ("do_not_index_sources",):
                continue
            for f in sorted(slug_dir.glob("*.md")):
                if f.name == "_index.md":
                    continue
                try:
                    text = f.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                lines = text.splitlines()[:20]
                has_title = any(l.startswith("# ") for l in lines)
                has_tags = any("**Tags:**" in l or l.strip().startswith("tags:") for l in lines)
                missing = []
                if not has_title:
                    missing.append("title")
                if not has_tags:
                    missing.append("tags")
                if missing:
                    issues.append({
                        "check": "missing_metadata",
                        "path": str(f.relative_to(KB)),
                        "detail": f"missing: {', '.join(missing)}",
                    })
    return issues


def check_broken_wikilinks(domains):
    """Find wikilinks that point to nonexistent files."""
    issues = []
    wikilink_re = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]')
    for domain in domains:
        for layer in ("raw", "wiki"):
            layer_dir = KB / domain / layer
            if not layer_dir.exists():
                continue
            for f in layer_dir.rglob("*.md"):
                if f.name == "_index.md":
                    continue
                try:
                    text = f.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                for match in wikilink_re.finditer(text):
                    target = match.group(1).strip()
                    # Resolve relative to KB root
                    target_path = KB / target
                    if not target_path.exists():
                        issues.append({
                            "check": "broken_wikilink",
                            "path": str(f.relative_to(KB)),
                            "detail": f"[[{target}]] not found",
                        })
    return issues


def check_near_duplicates(domains):
    """Find article slugs within edit distance 2 in the same source directory."""
    issues = []
    seen_pairs = set()
    for domain in domains:
        raw_dir = KB / domain / "raw"
        if not raw_dir.exists():
            continue
        for slug_dir in sorted(raw_dir.iterdir()):
            if not slug_dir.is_dir() or slug_dir.name in ("do_not_index_sources",):
                continue
            slugs = sorted(f.stem for f in slug_dir.glob("*.md") if f.name != "_index.md")
            for i, a in enumerate(slugs):
                for b in slugs[i + 1:]:
                    if _edit_distance(a, b) <= 2:
                        pair_key = (slug_dir.name, min(a, b), max(a, b))
                        if pair_key not in seen_pairs:
                            seen_pairs.add(pair_key)
                            issues.append({
                                "check": "near_duplicate",
                                "path": f"{domain}/raw/{slug_dir.name}/",
                                "detail": f"'{a}' ≈ '{b}'",
                            })
    return issues


def check_empty_sources(domains):
    """Find source directories with zero articles."""
    issues = []
    for domain in domains:
        raw_dir = KB / domain / "raw"
        if not raw_dir.exists():
            continue
        for slug_dir in sorted(raw_dir.iterdir()):
            if not slug_dir.is_dir() or slug_dir.name in ("do_not_index_sources",):
                continue
            articles = list(slug_dir.glob("*.md"))
            articles = [a for a in articles if a.name != "_index.md"]
            if not articles:
                issues.append({
                    "check": "empty_source",
                    "path": str(slug_dir.relative_to(KB)),
                    "detail": "no articles",
                })
    return issues


def run_lint(domains, as_json=False):
    """Run all lint checks and report."""
    all_issues = []
    checks = [
        ("thin_article", check_thin_articles),
        ("missing_metadata", check_missing_metadata),
        ("broken_wikilink", check_broken_wikilinks),
        ("near_duplicate", check_near_duplicates),
        ("empty_source", check_empty_sources),
    ]

    for name, check_fn in checks:
        issues = check_fn(domains)
        all_issues.extend(issues)

    if as_json:
        print(json.dumps(all_issues, indent=2))
        return all_issues

    # Group by check type
    by_check = {}
    for issue in all_issues:
        by_check.setdefault(issue["check"], []).append(issue)

    print(f"\nKB Lint — {len(all_issues)} issues found\n")

    check_labels = {
        "thin_article": "Thin articles (< 3 substantive lines)",
        "missing_metadata": "Missing metadata",
        "broken_wikilink": "Broken wikilinks",
        "near_duplicate": "Near-duplicate slugs",
        "empty_source": "Empty source directories",
    }

    for check_name, label in check_labels.items():
        issues = by_check.get(check_name, [])
        if issues:
            print(f"  {label}: {len(issues)}")
            for issue in issues[:10]:
                print(f"    {issue['path']} — {issue['detail']}")
            if len(issues) > 10:
                print(f"    ... and {len(issues) - 10} more")
        else:
            print(f"  {label}: OK")

    print()
    return all_issues


def main():
    domains = ["hard", "soft"]
    as_json = "--json" in sys.argv

    if "--domain" in sys.argv:
        idx = sys.argv.index("--domain")
        if idx + 1 < len(sys.argv):
            domains = [sys.argv[idx + 1]]

    run_lint(domains, as_json=as_json)


if __name__ == "__main__":
    main()
