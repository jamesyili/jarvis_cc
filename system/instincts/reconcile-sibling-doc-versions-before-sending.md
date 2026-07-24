---
id: reconcile-sibling-doc-versions-before-sending
trigger: About to send, cite, or treat as current a document that has sibling/variant versions (voice A vs B, exec vs direct, section extracts vs full doc) — especially when some were edited later than others
behavior: Before treating any variant as current, check the siblings' timestamps and cross-version consistency. If a later sibling holds the locked/canonical structure (renames, added sections, new personnel, new charter model), reconcile the older ones — or at minimum flag the divergence — before sending. Never send a stale variant silently just because it's the one in hand.
confidence: 0.45
evidence_count: 2
created: 2026-07-22
last_updated: 2026-07-23
status: active
---

## Evidence

### 2026-07-22
> "did you update these two voice versions with the key-personel / charter-sections?"
Context: Reorg org-design docs. Leo sent the two voice drafts (direct + exec, stamped 12:19) via /send-me on James's "send all the versions" request, without checking that later sibling files — `org_design_key_personnel_2026-07-19.md` (21:05) and `org_design_sections_charter_tech_2026-07-19.md` (16:09) — had already moved the structure forward (three-subcharter Charter model, "Scoring & Boards Modeling" → "Retrieval Modeling" rename, Bella + Balaji added). The voice docs contradicted the locked GDoc structure. James caught it; Leo then reconciled all four files and re-sent.
Signal: correction
Lesson: same-topic docs drift; the one you happen to be holding is not automatically the current one. A quick timestamp + structure check across siblings before sending catches stale material before it reaches a stakeholder-facing surface. Related: [[check-sibling-repos-before-assuming-state-elsewhere]] (the multi-machine analog), [[one-home-per-fact-in-multisection-docs]].

### 2026-07-23 (confirmed application)
Context: The reorg team name mutated across James's own live drafts — Dylan-approved *P13N Retrieval and Anticipation ML* (7/20) → *P13N CG and Anticipation ML* (one draft) → *Personalization Retrieval and Anticipation ML* (the 7/23 final email). Three variants, and the `team_meeting_talking_points` doc still asserted the name was "set" at the 7/20 string. Leo caught the divergence proactively, flagged it inline in both the FINAL email and the talking-points doc ("lock ONE string; make announcement + email + talking points all match before ship"), and made it an Open item rather than letting a mismatched name reach the org.
Signal: confirmed (instinct fired correctly, no correction needed)
Lesson: this fires not just across separate sibling *files* but across successive *drafts of the same artifact* — a load-bearing string (org name, title, date) that changes every draft is the tell. The email that renames the team differently than the announcement it replies to is the exact silent-stale failure this guards against. Verifying that named individuals in a by-name welcome match the roster of record ([[clean-concrete-rosters]]) is the same discipline applied to people instead of strings.
