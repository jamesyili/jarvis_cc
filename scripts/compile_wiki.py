#!/usr/bin/env python3
"""
Wiki compiler — scans raw content, identifies cross-cutting concepts,
and produces synthesized wiki articles.

Usage:
    python scripts/compile_wiki.py scan --domain hard      # Identify concepts from raw content
    python scripts/compile_wiki.py plan --domain hard      # Generate reviewable concept plan
    python scripts/compile_wiki.py compile --domain hard --all        # Compile all concepts from plan
    python scripts/compile_wiki.py compile --domain hard --concept X  # Compile single concept
    python scripts/compile_wiki.py incremental --domain hard          # Recompile changed content
"""
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_index import build_raw_index, build_wiki_index, parse_article_metadata

KB = Path(__file__).parent.parent / "kb"
MODEL = "claude-sonnet-4-6"


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def claude_prompt(prompt, timeout=300):
    """Call Claude CLI and return response text."""
    result = subprocess.run(
        ["claude", "-p", prompt, "--model", MODEL],
        capture_output=True, text=True, timeout=timeout,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude error: {result.stderr[:500]}")
    return result.stdout.strip()


def strip_code_fences(text):
    """Remove markdown code fences from Claude responses."""
    text = re.sub(r'^```(?:json)?\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n```\s*$', '', text, flags=re.MULTILINE)
    return text.strip()


def get_content_preview(filepath, max_chars=500):
    """Read first N chars of content after frontmatter."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""
    # Skip frontmatter
    lines = text.splitlines()
    body_start = 0
    if lines and lines[0].strip() == "---":
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                body_start = i + 1
                break
    # Skip title and metadata lines
    for i, line in enumerate(lines[body_start:], body_start):
        if line.strip() and not line.startswith("#") and not line.startswith("**") and line.strip() != "---":
            body_start = i
            break
    body = "\n".join(lines[body_start:])
    return body[:max_chars]


def file_hash(filepath):
    """SHA256 of file contents."""
    return hashlib.sha256(filepath.read_bytes()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Scan: identify concepts from raw content
# ---------------------------------------------------------------------------

def scan_concepts(domain):
    """Scan raw content and ask Claude to identify cross-cutting concepts."""
    raw_dir = KB / domain / "raw"

    articles = []
    for slug_dir in sorted(raw_dir.iterdir()):
        if not slug_dir.is_dir() or slug_dir.name == "sources":
            continue
        for f in sorted(slug_dir.glob("*.md")):
            if f.name == "_index.md":
                continue
            title, tags = parse_article_metadata(f)
            preview = get_content_preview(f, 300)
            articles.append({
                "path": str(f.relative_to(KB)),
                "title": title,
                "tags": tags,
                "preview": preview[:200],
                "source": slug_dir.name,
            })

    print(f"Scanning {len(articles)} articles in {domain}...")

    # Batch into chunks to stay within context limits
    batch_size = 150
    all_concepts = []

    for i in range(0, len(articles), batch_size):
        batch = articles[i:i + batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(articles) + batch_size - 1) // batch_size
        print(f"  Processing batch {batch_num}/{total_batches} ({len(batch)} articles)...")

        catalog = json.dumps(batch, indent=1)
        prompt = f"""You are building a concept index for a personal knowledge base wiki in the "{domain} skills" domain.

Below is a catalog of {len(batch)} raw articles. Each has a title, source, tags, and content preview.

Identify cross-cutting CONCEPTS that span multiple articles. A concept is a topic that at least 2 articles contribute to meaningfully. Aim for 20-40 concepts per batch — not too granular, not too broad.

For each concept, output:
- concept_slug: kebab-case identifier (e.g. "two-tower-models", "managing-up")
- concept_name: human-readable name
- description: 1-sentence description of what this concept covers
- source_articles: list of article paths from the catalog that should be synthesized
- related_concepts: list of other concept slugs this relates to
- tags: list of relevant tags

Output ONLY valid JSON: {{"concepts": [...]}}

CATALOG:
{catalog}"""

        try:
            response = claude_prompt(prompt, timeout=600)
            parsed = json.loads(strip_code_fences(response))
            concepts = parsed.get("concepts", [])
            all_concepts.extend(concepts)
            print(f"    Found {len(concepts)} concepts")
        except (json.JSONDecodeError, RuntimeError) as e:
            error_dir = KB / domain / "wiki" / ".errors"
            error_dir.mkdir(parents=True, exist_ok=True)
            error_file = error_dir / f"scan_batch_{batch_num}.txt"
            error_file.write_text(str(e) + "\n\n" + (response if 'response' in dir() else "no response"), encoding="utf-8")
            print(f"    ERROR in batch {batch_num}: {e}")
            continue

    # Deduplicate concepts by slug
    seen = {}
    for c in all_concepts:
        slug = c.get("concept_slug", "")
        if slug in seen:
            # Merge source articles
            existing_paths = set(seen[slug].get("source_articles", []))
            new_paths = set(c.get("source_articles", []))
            seen[slug]["source_articles"] = list(existing_paths | new_paths)
        else:
            seen[slug] = c

    deduped = list(seen.values())
    print(f"\nTotal: {len(deduped)} unique concepts identified")

    # Save raw scan results
    scan_path = KB / domain / "wiki" / ".scan_results.json"
    with open(scan_path, "w") as f:
        json.dump({"concepts": deduped, "scanned_date": date.today().isoformat()}, f, indent=2)
    print(f"Saved to {scan_path}")

    return deduped


# ---------------------------------------------------------------------------
# Plan: generate human-reviewable concept list
# ---------------------------------------------------------------------------

def generate_plan(domain, concepts=None):
    """Write _plan.md for human review before compilation."""
    if concepts is None:
        scan_path = KB / domain / "wiki" / ".scan_results.json"
        if not scan_path.exists():
            print(f"No scan results found. Run 'scan --domain {domain}' first.")
            sys.exit(1)
        with open(scan_path) as f:
            concepts = json.load(f).get("concepts", [])

    plan_path = KB / domain / "wiki" / "_plan.md"
    domain_label = "Hard Skills" if domain == "hard" else "Soft Skills"

    lines = [
        f"# Wiki Compilation Plan — {domain_label}\n",
        f"> Generated: {date.today().isoformat()}",
        f"> {len(concepts)} concepts identified\n",
        "Review this plan. Edit or remove concepts before compiling.",
        "Mark concepts with `[x]` to approve, `[ ]` to skip.\n",
    ]
    for c in sorted(concepts, key=lambda x: x.get("concept_name", "")):
        slug = c.get("concept_slug", "unknown")
        name = c.get("concept_name", "Unknown")
        desc = c.get("description", "")
        sources = c.get("source_articles", [])
        related = c.get("related_concepts", [])

        lines.append(f"- [x] **{name}** (`{slug}`)")
        lines.append(f"  - {desc}")
        lines.append(f"  - Sources: {len(sources)} articles")
        for path in sources[:10]:  # Show first 10
            lines.append(f"    - [[{path}]]")
        if len(sources) > 10:
            lines.append(f"    - ... and {len(sources) - 10} more")
        if related:
            lines.append(f"  - Related: {', '.join(related)}")
        lines.append("")

    plan_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Plan written to {plan_path} ({len(concepts)} concepts)")
    return plan_path


# ---------------------------------------------------------------------------
# Compile: generate wiki articles from plan
# ---------------------------------------------------------------------------

def load_plan(domain):
    """Load concepts from _plan.md, respecting [x]/[ ] checkboxes."""
    plan_path = KB / domain / "wiki" / "_plan.md"
    scan_path = KB / domain / "wiki" / ".scan_results.json"

    if not scan_path.exists():
        print(f"No scan results found. Run 'scan --domain {domain}' first.")
        sys.exit(1)

    with open(scan_path) as f:
        all_concepts = {c["concept_slug"]: c for c in json.load(f).get("concepts", [])}

    # If plan exists, filter by checkboxes
    if plan_path.exists():
        plan_text = plan_path.read_text(encoding="utf-8")
        approved = set()
        for line in plan_text.splitlines():
            match = re.match(r'- \[x\] \*\*.*?\*\* \(`(.+?)`\)', line)
            if match:
                approved.add(match.group(1))
        return [all_concepts[slug] for slug in approved if slug in all_concepts]

    return list(all_concepts.values())


def compile_concept(domain, concept):
    """Read source articles and synthesize a wiki article for one concept."""
    source_texts = []
    for path in concept.get("source_articles", []):
        full_path = KB / path
        if full_path.exists():
            try:
                text = full_path.read_text(encoding="utf-8", errors="replace")
                # Truncate very long articles
                if len(text) > 8000:
                    text = text[:8000] + "\n\n[... truncated ...]"
                source_texts.append({"path": path, "content": text})
            except Exception:
                continue

    if not source_texts:
        print(f"    No source files found for {concept.get('concept_slug', '?')}")
        return None

    name = concept.get("concept_name", "")
    desc = concept.get("description", "")
    tags = concept.get("tags", [])
    related = concept.get("related_concepts", [])

    # Build source content block
    sources_block = ""
    for s in source_texts:
        sources_block += f"\n--- SOURCE: {s['path']} ---\n{s['content']}\n"

    prompt = f"""You are writing a concept article for a personal knowledge base wiki.

CONCEPT: {name}
DESCRIPTION: {desc}
TAGS: {", ".join(tags)}
RELATED CONCEPTS: {", ".join(related)}

Below are the source articles to synthesize. Write a standalone reference article that:
1. Defines the concept clearly
2. Synthesizes key ideas across all sources (do NOT just summarize each source sequentially)
3. Highlights practical applications and nuances
4. Uses [[wikilinks]] when referencing related concepts: [[{domain}/wiki/{{concept-slug}}.md|Concept Name]]
5. Is 300-1500 words — dense and useful, not padded

Do NOT include YAML frontmatter — I will add that programmatically.
Start with a # heading, then the article body, then a ## Sources section.
In the Sources section, list each source as: - [[{{source-path}}]]

SOURCES:
{sources_block}"""

    try:
        body = claude_prompt(prompt, timeout=300)
    except RuntimeError as e:
        error_dir = KB / domain / "wiki" / ".errors"
        error_dir.mkdir(parents=True, exist_ok=True)
        slug = concept.get("concept_slug", "unknown")
        (error_dir / f"{slug}.txt").write_text(str(e), encoding="utf-8")
        print(f"    ERROR compiling {slug}: {e}")
        return None

    # Build frontmatter
    source_paths = [s["path"] for s in source_texts]
    frontmatter = f"""---
concept: {name}
tags: [{", ".join(tags)}]
sources: [{", ".join(source_paths)}]
last_compiled: {date.today().isoformat()}
related: [{", ".join(related)}]
---

"""
    slug = concept.get("concept_slug", "unknown")
    article_path = KB / domain / "wiki" / f"{slug}.md"
    article_path.write_text(frontmatter + body, encoding="utf-8")
    return article_path


def compile_all(domain):
    """Compile all approved concepts."""
    concepts = load_plan(domain)
    print(f"Compiling {len(concepts)} concepts for {domain}...")

    compiled = 0
    errors = 0
    for i, concept in enumerate(concepts):
        slug = concept.get("concept_slug", "?")
        print(f"  [{i+1}/{len(concepts)}] {slug}...")
        result = compile_concept(domain, concept)
        if result:
            compiled += 1
        else:
            errors += 1

    # Update indexes
    print("\nRebuilding indexes...")
    build_raw_index(domain)
    build_wiki_index(domain)

    # Save compile state
    save_compile_state(domain, concepts)

    print(f"\nDone. {compiled} compiled, {errors} errors.")


def compile_single(domain, target_slug):
    """Compile a single concept by slug."""
    scan_path = KB / domain / "wiki" / ".scan_results.json"
    if not scan_path.exists():
        print(f"No scan results. Run 'scan --domain {domain}' first.")
        sys.exit(1)

    with open(scan_path) as f:
        concepts = {c["concept_slug"]: c for c in json.load(f).get("concepts", [])}

    if target_slug not in concepts:
        print(f"Concept '{target_slug}' not found. Available: {', '.join(sorted(concepts.keys()))}")
        sys.exit(1)

    concept = concepts[target_slug]
    print(f"Compiling {target_slug}...")
    result = compile_concept(domain, concept)
    if result:
        print(f"  Written to {result}")
        build_wiki_index(domain)
    else:
        print("  Failed.")


# ---------------------------------------------------------------------------
# Incremental compilation
# ---------------------------------------------------------------------------

def save_compile_state(domain, concepts):
    """Save compilation state for incremental updates."""
    state_path = KB / domain / "wiki" / ".compile_state.json"
    raw_dir = KB / domain / "raw"

    file_hashes = {}
    for slug_dir in raw_dir.iterdir():
        if not slug_dir.is_dir() or slug_dir.name == "sources":
            continue
        for f in slug_dir.glob("*.md"):
            if f.name == "_index.md":
                continue
            rel = str(f.relative_to(KB))
            file_hashes[rel] = file_hash(f)

    concept_sources = {}
    for c in concepts:
        concept_sources[c["concept_slug"]] = c.get("source_articles", [])

    state = {
        "last_compile": date.today().isoformat(),
        "raw_file_hashes": file_hashes,
        "concept_sources": concept_sources,
    }
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)


def incremental_compile(domain):
    """Detect changed raw files and recompile affected concepts."""
    state_path = KB / domain / "wiki" / ".compile_state.json"
    if not state_path.exists():
        print("No compile state found. Run a full compile first.")
        sys.exit(1)

    with open(state_path) as f:
        state = json.load(f)

    old_hashes = state.get("raw_file_hashes", {})
    concept_sources = state.get("concept_sources", {})

    # Find changed/new files
    raw_dir = KB / domain / "raw"
    changed_files = set()
    for slug_dir in raw_dir.iterdir():
        if not slug_dir.is_dir() or slug_dir.name == "sources":
            continue
        for f in slug_dir.glob("*.md"):
            if f.name == "_index.md":
                continue
            rel = str(f.relative_to(KB))
            current_hash = file_hash(f)
            if rel not in old_hashes or old_hashes[rel] != current_hash:
                changed_files.add(rel)

    if not changed_files:
        print("No changes detected.")
        return

    print(f"Found {len(changed_files)} changed/new files")

    # Find affected concepts
    affected_slugs = set()
    for slug, sources in concept_sources.items():
        if any(s in changed_files for s in sources):
            affected_slugs.add(slug)

    # New files might not be in any concept yet
    orphan_files = changed_files - {s for sources in concept_sources.values() for s in sources}
    if orphan_files:
        print(f"  {len(orphan_files)} new files not in any concept — consider re-scanning")

    if affected_slugs:
        scan_path = KB / domain / "wiki" / ".scan_results.json"
        with open(scan_path) as f:
            all_concepts = {c["concept_slug"]: c for c in json.load(f).get("concepts", [])}

        print(f"  Recompiling {len(affected_slugs)} affected concepts...")
        for slug in sorted(affected_slugs):
            if slug in all_concepts:
                print(f"    {slug}...")
                compile_concept(domain, all_concepts[slug])

        build_wiki_index(domain)

    print("Done.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(__doc__)
        sys.exit(1)

    command = args[0]
    domain = None
    if "--domain" in args:
        idx = args.index("--domain")
        if idx + 1 < len(args):
            domain = args[idx + 1]

    if not domain:
        print("--domain required (hard or soft)")
        sys.exit(1)

    if command == "scan":
        concepts = scan_concepts(domain)
        generate_plan(domain, concepts)

    elif command == "plan":
        generate_plan(domain)

    elif command == "compile":
        if "--all" in args:
            compile_all(domain)
        elif "--concept" in args:
            idx = args.index("--concept")
            if idx + 1 < len(args):
                compile_single(domain, args[idx + 1])
            else:
                print("--concept requires a slug")
                sys.exit(1)
        else:
            print("compile requires --all or --concept <slug>")
            sys.exit(1)

    elif command == "incremental":
        incremental_compile(domain)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
