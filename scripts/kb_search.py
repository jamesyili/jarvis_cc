#!/usr/bin/env python3
"""
KB search — TF-IDF keyword search across all raw and wiki content.

Usage:
    python scripts/kb_search.py "attention mechanism"
    python scripts/kb_search.py "how do recommender systems work" --top 10
    python scripts/kb_search.py --rebuild          # Force index rebuild
    python scripts/kb_search.py --stats            # Show index stats

Output: ranked results as JSON (for skill consumption) or human-readable table.
"""
import json
import math
import re
import sys
import time
from collections import Counter
from pathlib import Path

KB = Path(__file__).parent.parent / "kb"
CACHE_DIR = KB / ".kb"
INDEX_PATH = CACHE_DIR / "search_index.json"

TITLE_BOOST = 3.0
TAG_BOOST = 2.0
DEFAULT_TOP = 5
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", "of",
    "with", "by", "from", "is", "it", "as", "be", "was", "are", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could", "should",
    "may", "might", "shall", "can", "this", "that", "these", "those", "not", "no",
    "so", "if", "then", "than", "when", "what", "which", "who", "how", "where",
    "why", "all", "each", "every", "both", "few", "more", "most", "other", "some",
    "such", "only", "own", "same", "also", "just", "about", "above", "after",
    "again", "any", "because", "before", "between", "during", "into", "its",
    "once", "our", "out", "over", "through", "under", "until", "up", "very",
    "we", "they", "them", "their", "you", "your", "he", "she", "him", "her",
    "i", "me", "my", "s", "t", "re", "ve", "ll", "d", "m",
}


def tokenize(text):
    """Lowercase, split on non-alphanumeric, remove stop words."""
    tokens = re.findall(r'[a-z0-9]+', text.lower())
    return [t for t in tokens if t not in STOP_WORDS and len(t) > 1]


def scan_articles():
    """Scan all raw and wiki articles, return list of document dicts."""
    docs = []
    for domain in ("hard", "soft"):
        # Raw articles
        raw_dir = KB / domain / "raw"
        if raw_dir.exists():
            for slug_dir in sorted(raw_dir.iterdir()):
                if not slug_dir.is_dir() or slug_dir.name in ("do_not_index_sources",):
                    continue
                for f in sorted(slug_dir.glob("*.md")):
                    if f.name == "_index.md":
                        continue
                    docs.append(_parse_doc(f, domain, "raw", slug_dir.name))

        # Wiki articles
        wiki_dir = KB / domain / "wiki"
        if wiki_dir.exists():
            for f in sorted(wiki_dir.glob("*.md")):
                if f.name.startswith("_"):
                    continue
                docs.append(_parse_doc(f, domain, "wiki", None))

    return docs


def _parse_doc(filepath, domain, layer, source_slug):
    """Parse a markdown file into a document dict."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        text = ""

    title = filepath.stem.replace("-", " ").title()
    tags = ""
    body_start = 0
    lines = text.splitlines()

    # Parse frontmatter / header metadata
    for i, line in enumerate(lines[:20]):
        if line.startswith("# "):
            title = line[2:].strip()
        if line.startswith("**Tags:**"):
            tags = line.replace("**Tags:**", "").strip()
        if line.strip() == "---" and i > 0:
            body_start = i + 1

    # YAML frontmatter tags
    if lines and lines[0].strip() == "---":
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("tags:"):
                tags = line.replace("tags:", "").strip().strip("[]")

    body = " ".join(lines[body_start:])
    rel_path = str(filepath.relative_to(KB))

    return {
        "path": rel_path,
        "title": title,
        "tags": tags,
        "source": source_slug or "",
        "domain": domain,
        "layer": layer,
        "title_tokens": tokenize(title),
        "tag_tokens": tokenize(tags),
        "body_tokens": tokenize(body),
    }


def build_index(docs):
    """Build TF-IDF index from document list."""
    n = len(docs)
    # Document frequency: how many docs contain each term
    df = Counter()
    for doc in docs:
        all_terms = set(doc["title_tokens"] + doc["tag_tokens"] + doc["body_tokens"])
        for term in all_terms:
            df[term] += 1

    # IDF
    idf = {term: math.log(n / count) for term, count in df.items()}

    # Per-document TF vectors (weighted by field)
    for doc in docs:
        tf = Counter()
        for t in doc["body_tokens"]:
            tf[t] += 1.0
        for t in doc["title_tokens"]:
            tf[t] += TITLE_BOOST
        for t in doc["tag_tokens"]:
            tf[t] += TAG_BOOST
        doc["tf"] = dict(tf)

    return idf


def search(query, docs, idf, top=DEFAULT_TOP):
    """Score documents against query, return top results."""
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    results = []
    for doc in docs:
        score = 0.0
        tf = doc.get("tf", {})
        for token in query_tokens:
            if token in tf and token in idf:
                score += tf[token] * idf[token]
        if score > 0:
            results.append({
                "path": doc["path"],
                "title": doc["title"],
                "source": doc["source"],
                "domain": doc["domain"],
                "layer": doc["layer"],
                "tags": doc["tags"],
                "score": round(score, 3),
            })

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top]


def save_index(docs, idf):
    """Cache index to disk."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = {
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "doc_count": len(docs),
        "idf": idf,
        "docs": [
            {
                "path": d["path"],
                "title": d["title"],
                "tags": d["tags"],
                "source": d["source"],
                "domain": d["domain"],
                "layer": d["layer"],
                "tf": d["tf"],
                "title_tokens": d["title_tokens"],
                "tag_tokens": d["tag_tokens"],
            }
            for d in docs
        ],
    }
    INDEX_PATH.write_text(json.dumps(cache, separators=(",", ":")), encoding="utf-8")
    return cache


def load_index():
    """Load cached index, return (docs, idf) or None if stale/missing."""
    if not INDEX_PATH.exists():
        return None
    try:
        cache = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        return cache["docs"], cache["idf"]
    except Exception:
        return None


def get_or_build_index(force_rebuild=False):
    """Load cached index or build fresh."""
    if not force_rebuild:
        cached = load_index()
        if cached:
            return cached

    docs = scan_articles()
    idf = build_index(docs)
    save_index(docs, idf)
    return docs, idf


def main():
    if "--rebuild" in sys.argv:
        print("Rebuilding search index...")
        docs = scan_articles()
        idf = build_index(docs)
        cache = save_index(docs, idf)
        print(f"Indexed {cache['doc_count']} documents at {cache['built_at']}")
        return

    if "--stats" in sys.argv:
        cached = load_index()
        if cached:
            docs, idf = cached
            domains = Counter(d["domain"] for d in docs)
            layers = Counter(d["layer"] for d in docs)
            sources = Counter(d["source"] for d in docs if d["source"])
            print(f"Index: {len(docs)} documents, {len(idf)} unique terms")
            print(f"Domains: {dict(domains)}")
            print(f"Layers: {dict(layers)}")
            print(f"Top sources: {sources.most_common(10)}")
        else:
            print("No index found. Run --rebuild first.")
        return

    # Parse args
    top = DEFAULT_TOP
    query_parts = []
    skip_next = False
    for i, arg in enumerate(sys.argv[1:], 1):
        if skip_next:
            skip_next = False
            continue
        if arg == "--top" and i < len(sys.argv) - 1:
            top = int(sys.argv[i + 1])
            skip_next = True
        elif arg == "--json":
            pass  # default output is already structured
        elif not arg.startswith("--"):
            query_parts.append(arg)

    query = " ".join(query_parts)
    if not query:
        print(__doc__)
        sys.exit(1)

    docs, idf = get_or_build_index()
    results = search(query, docs, idf, top=top)

    if not results:
        print(f"No results for: {query}")
        sys.exit(0)

    # Human-readable output
    print(f"\nResults for: \"{query}\" (top {top})\n")
    for i, r in enumerate(results, 1):
        print(f"  {i}. [{r['score']:6.1f}] {r['title']}")
        print(f"          {r['domain']}/{r['layer']}/{r['source']} — {r['path']}")
        if r["tags"]:
            print(f"          tags: {r['tags']}")
    print()


if __name__ == "__main__":
    main()
