---
id: bulk-reorg-disposition-table
trigger: A bulk file/folder reorg or any multi-item change needs James's approval (many files, each needing a keep/move/merge/archive/kill call)
behavior: Recon the actual files first (sizes, staleness, duplicates, what's already synthesized) so most calls answer themselves, then converge via ONE complete per-item disposition table — every file accounted for, a recommendation on every row, ⚠ flags on the calls Leo is least sure of with the reasoning visible. One approval ("Lg") beats serial per-file questions. Execute only after approval; flagged calls he doesn't overrule are approved as recommended.
confidence: 0.3
evidence_count: 1
created: 2026-08-15
last_updated: 2026-08-15
status: active
---

## Evidence

### 2026-08-15
> James: "Lg" — approving the full reflex-folder disposition table (35 docs → 4 buckets + archive) unchanged, including all four ⚠-flagged judgment calls (curator `_prompts` twin → archive, org-research raws → archive with synthesis kept live, redesign pair → archive, tim_friday/epd pairs archived unmerged).
Context: `/start-session` with the reorg task + `/grill-me`. The grill converged in three questions (merge scope → workstream taxonomy → disposition table) because file recon (wc, diff, heads) answered the rest — e.g. the `full_funnel_logging.md` duplicate was proven byte-identical rather than asked about, and `key_points.md` was discovered to already be the org-research synthesis.
Signal: confirmation

## Related

- `no-questions-by-default` (the general rule; this is its shape for bulk approvals — batch into one decision artifact)
- `repoint-structure-docs-on-file-moves` (what execution looks like after the table is approved)
- `todo-reviews-one-item-at-a-time` (the OPPOSITE default for todo reviews — there, depth-first per item; the difference is reorg calls are cheap to batch-read, todo items need live status from James)
