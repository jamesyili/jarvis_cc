#!/usr/bin/env python3
"""
Build _index.md catalogs for all raw and wiki content in kb/.

Usage:
    python scripts/build_index.py              # Rebuild all indexes
    python scripts/build_index.py --domain hard  # Rebuild hard only
    python scripts/build_index.py --domain soft  # Rebuild soft only
"""
import re
import sys
from datetime import date
from pathlib import Path

KB = Path(__file__).parent.parent / "kb"


def parse_article_metadata(filepath):
    """Extract title and tags from a raw article file."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return filepath.stem.replace("-", " ").title(), ""

    lines = text.splitlines()
    title = filepath.stem.replace("-", " ").title()  # fallback
    tags = ""

    for line in lines[:15]:
        if line.startswith("# "):
            title = line[2:].strip()
        if line.startswith("**Tags:**"):
            tags = line.replace("**Tags:**", "").strip()

    # Also check YAML frontmatter
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("tags:"):
                tags = line.replace("tags:", "").strip().strip("[]")

    # Escape pipe characters for markdown table
    title = title.replace("|", "\\|")
    tags = tags.replace("|", "\\|")

    return title, tags


def build_raw_index(domain):
    """Build _index.md for kb/{domain}/raw/."""
    raw_dir = KB / domain / "raw"
    index_path = raw_dir / "_index.md"

    entries = []
    for slug_dir in sorted(raw_dir.iterdir()):
        if not slug_dir.is_dir() or slug_dir.name in ("do_not_index_sources",):
            continue
        for f in sorted(slug_dir.glob("*.md")):
            if f.name == "_index.md":
                continue
            title, tags = parse_article_metadata(f)
            rel_path = f.relative_to(KB)
            entries.append((title, slug_dir.name, tags, str(rel_path)))

    domain_label = "Hard Skills" if domain == "hard" else "Soft Skills"
    source_count = len(set(e[1] for e in entries))

    lines = [
        f"# {domain_label} — Raw Content Index\n",
        f"> Auto-generated. {len(entries)} articles across {source_count} sources. "
        f"Last updated: {date.today().isoformat()}\n",
        "| Title | Source | Tags | Path | Wiki Concepts |",
        "|-------|--------|------|------|---------------|",
    ]
    for title, source, tags, path in entries:
        lines.append(f"| {title} | {source} | {tags} | [[{path}]] | |")

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  {domain}/raw/_index.md: {len(entries)} entries")
    return len(entries)


def build_wiki_index(domain):
    """Build _index.md for kb/{domain}/wiki/. Reads from existing wiki articles."""
    wiki_dir = KB / domain / "wiki"
    index_path = wiki_dir / "_index.md"

    entries = []
    for f in sorted(wiki_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        concept = f.stem.replace("-", " ").title()
        description = ""
        source_count = 0
        related = ""

        if text.startswith("---"):
            try:
                fm_end = text.index("---", 3)
                fm = text[3:fm_end]
                for line in fm.splitlines():
                    if line.startswith("concept:"):
                        concept = line.split(":", 1)[1].strip()
                    if line.startswith("sources:"):
                        source_count = line.count(",") + 1
                    if line.startswith("related:"):
                        related_items = re.findall(r'[\w-]+', line.split(":", 1)[1])
                        related = ", ".join(
                            f"[[{domain}/wiki/{r}.md|{r}]]" for r in related_items
                        )
            except ValueError:
                pass

        # First paragraph after heading as description
        heading_match = re.search(r'\n# .+\n\n(.+)', text)
        if heading_match:
            description = heading_match.group(1).strip()[:100]
            if len(heading_match.group(1).strip()) > 100:
                description += "..."

        rel_path = f.relative_to(KB)
        entries.append((concept, description, source_count, related, str(rel_path)))

    domain_label = "Hard Skills" if domain == "hard" else "Soft Skills"
    lines = [
        f"# {domain_label} — Wiki Index\n",
        f"> Auto-generated. {len(entries)} concept articles. Last updated: {date.today().isoformat()}\n",
        "| Concept | Description | Sources | Related |",
        "|---------|-------------|---------|---------|",
    ]
    for concept, desc, src_count, related, path in entries:
        lines.append(f"| [[{path}|{concept}]] | {desc} | {src_count} | {related} |")

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  {domain}/wiki/_index.md: {len(entries)} entries")
    return len(entries)


def main():
    domains = ["hard", "soft"]

    if "--domain" in sys.argv:
        idx = sys.argv.index("--domain")
        if idx + 1 < len(sys.argv):
            domains = [sys.argv[idx + 1]]

    print("Building indexes...")
    for domain in domains:
        build_raw_index(domain)
        build_wiki_index(domain)

    # Rebuild search index too
    from kb_search import scan_articles, build_index, save_index
    docs = scan_articles()
    idf = build_index(docs)
    save_index(docs, idf)
    print(f"  search index: {len(docs)} documents")
    print("Done.")


if __name__ == "__main__":
    main()
