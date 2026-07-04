---
id: check-sibling-repos-before-assuming-state-elsewhere
trigger: James references a side project's state as unknown, elsewhere, or "on the other computer" (Folio, PF, or any named build)
behavior: Before recording that state is inaccessible, check ~/src/ for a sibling repo (ls ~/src, then read its CONTEXT/BACKLOG/session logs). Side projects often live on this machine with self-documenting repos — read them directly instead of asking James to reconstruct.
confidence: 0.4
evidence_count: 1
created: 2026-07-03
last_updated: 2026-07-03
status: active
---

## Evidence

### 2026-07-03
> "check out @../pf/ for PF"
Context: The 7/3 afternoon session logged "the actual state lives on his other computer" for both Folio and PF. Evening session: PF was at `~/src/pf` on this machine the whole time, with a fully self-documenting repo (CONTEXT.md, BACKLOG.md, LAB.md, session logs) — the planned "James walks Leo through the state" was unnecessary; reading the repo answered everything. Known sibling repos: `~/src/pf` (PF), `~/src/viral_remix` (Folio, pre-extraction).
Signal: observed inefficiency (wrong fact recorded in the afternoon log; walkthrough session mis-scoped)
