---
id: check-existing-context-before-analyzing
trigger: When about to analyze or recommend anything about a known stakeholder, project, dynamic, or recurring situation that has documented history in the repo (stakeholders.md, projects/, dylan_1on1_log.md, etc.)
behavior: Before reasoning from first principles, GREP or read the existing context files for documented playbooks, prior decisions, historical incidents, or relationship analysis. Work WITH existing context, not around it. Surface the existing playbook first; only propose reinventing if James explicitly asks OR if new information genuinely invalidates the prior playbook.
confidence: 0.85
evidence_count: 5
created: 2026-04-23
last_updated: 2026-07-13
status: active
---

## Evidence

### 2026-04-23
> "You should already look back at Roberto's incidents to get a context on how he has reacted to potential collaboration attempts in the past, which is to say that he was very actively against it. Take a look at that context so you should know."

Context: James asked about the Roberto-vs-Pinkerton dynamic. Leo proposed a "compete / cede / negotiate joint ownership" framework, recommending Option C (negotiate). James corrected directly: existing context at `stakeholders.md:913` and `projects/pinkerton/strategic_next_steps_april.md:27` was already explicit. The documented playbook (from 2026-04-09) was: do NOT re-outreach to Roberto, structural Kurchi-Dylan proxy not peer-fixable, bypass via Reflex. James had explicitly tried collaboration in March 2026 (warm peer DM congratulating Roberto on Search Debugger). Roberto went silent for 9 days. Then territorially interrupted James's pitch at Brian Lee's forum 4/09 PM. The playbook concluded: "direct peer outreach is unlikely to resolve the friction." Leo's Option C recommendation was functionally re-proposing the March 2026 move that already failed — visible only by reading the context.

Signal: correction (explicit redirect to existing documented context; Leo's analysis was proposing something that contradicted the known playbook).

### 2026-04-25
> "And I have already demonstrated PINvestigator"

Context: James was preparing for Jeff office hours. Leo recommended *"open PINvestigator and demo it on a real investigation"* as the lead move for the OH. James corrected with one short sentence — he'd already demoed PINvestigator to Jeff (per `backlog.md` item: *"PINvestigator — 5 next steps from Jeff demo — all done as of 2026-04-17"*). Leo had not grepped the backlog before recommending the demo. Same pattern as the Roberto incident — analyzing without checking documented history. Caused Leo to revise the entire Jeff OH strategy (no PINvestigator re-demo; lead with three NEW associations: RR business impact + Pinkerton cross-org adoption + Reflex-CTO demo teaser).

Signal: correction (terse but unambiguous). Two evidence points in 2 days on the same pattern. Heuristic: when proposing concrete tactical moves on known stakeholders, GREP the backlog + relevant project files + recent session logs first.

### 2026-04-25c
> "How do you not have context on Raymond?"

Context: James asked Leo to surface stakeholder context behind the Akshanta + Lili Li tone-feedback episode. Leo synthesized cleanly. James later mentioned Raymond as the "real source of tension" with the PMs. Leo claimed "no Raymond context found in stakeholders.md or org files" — and proposed adding Raymond as a "new stakeholder I should add (#24)." James corrected: Raymond IS in the files, as a 3-line "Notable: Raymond Su" sub-entry under Tim Leung at `stakeholders.md:1089` and in `organization.md:85`. Leo's grep had searched for top-level stakeholder profiles and missed the sub-entry pattern.

Signal: correction (mild but third in 2 days on the same root pattern). Refinement: existing-context grep must search for **surface-form names** (e.g., `grep -i "raymond"`), not just top-level section headers or exact-match file references. Sub-entries, notable mentions, and inline references all count as "context exists."

### 2026-05-07
> "Do you have two files on the same candidate? If so, merge them into one." (followed by) "The em_backfill_bowen_ one is likely the same as bharath."

Context: James asked Leo to write a hiring evaluation for Bharath R after his 5/7 onsite interview. Leo wrote `frontline_mgr_bharath_r_2026-05-07.md` without first checking the existing `work/people/hiring/` folder for prior Bharath references. The folder contained `em_backfill_bowen_2026-04-16.md` — which was actually Bharath's earlier interview round mis-named (the candidate's audio-expertise hiring + multitask learning + ML community engagement + evaded-specifics-on-60-day-TL-example pattern matched Bharath's 5/7 interview unmistakably). Leo had access to all of this — could have grepped the folder first, recognized the existing 4/16 evaluation, and merged on creation rather than after-the-fact correction.

Signal: correction (mild but explicit — fourth in this pattern).

Refinement for hiring/evaluation files specifically: before writing a NEW per-candidate / per-stakeholder / per-project evaluation file, grep the relevant folder (`work/people/hiring/`, `work/people/`, `work/projects/`) for surface-form name matches. A first-round interview note from weeks ago is still context. The duplicate-file pattern is a special case of analytical laziness — Leo created a new artifact when an existing one already documented the prior data.

**Add to heuristic 5:** also check sibling files in the relevant folder before creating a new evaluation file. `ls + grep` on the folder, not just the canonical files.

### 2026-07-13
> "Not Jiaxing, Jiajing the ATG Sr. Director."

Context: James said "Jiajing has been asking me to go talk to Dinesh (Ads Sr. EM)." Leo pattern-matched "Jiajing" onto the known "Jiaxing Qu" (P2P engineer, Sai's team) — encouraged by a prior in-file note that "Jiaqing/Jiaxing" were transliteration variants of one person — and built a strategic read on the conflation ("SSJ co-option working") before James corrected. The real broker was a *different, undocumented* person: Jiajing, Sr. Director in ATG — which inverts the read (ATG leadership routing Ads to James, not SSJ evangelizing outward). **Inverse failure mode of 2026-04-25c:** there Leo missed a documented person; here Leo force-merged an undocumented person onto a documented one. Repo precedents for name collisions: "Daniel Liu (contractor)" mis-record (different Daniel), Jiaqing/Jiaxing variance.

Signal: correction (immediate, factual). Refinement → heuristic 6.

## Pattern

This is distinct from `corrections-interrupt-by-design` (which is about factual corrections that interrupt workflow). This instinct is about **analytical laziness that reinvents what's already documented.** Symptom: Leo reasons from first principles when existing context contains a better-grounded answer. Cost: James has to redirect, and in high-stakes strategic conversations (like stakeholder strategy), the wrong framework wastes decision cycles.

**Heuristics for when this fires:**

1. **Known-stakeholder questions** ("what should I do about Roberto / Andrew / Dylan / Rajat / Jeff?") — always grep `work/people/stakeholders.md` + `dylan_archive.md` first.
2. **Ongoing-project dynamics** ("how should I position Pinkerton / RR / UPP?") — grep `work/projects/` + recent session logs.
3. **Recurring-situation patterns** ("how should I handle this 1:1 / skip-level / office hours?") — check `communication.md` playbooks and `dylan_1on1_log.md` for prior instances.
4. **When about to offer a multi-option framework** (A / B / C) on a known topic — pause and verify no option is known-failed. Leo's Option C re-proposed the March 2026 failed move.
5. **Before claiming "no context found" on a name or topic** — run `grep -rn -i "<name>" work/ self/ --include="*.md"` (case-insensitive, surface-form, no extension). Sub-entries, notable mentions, inline references all count as "context exists." A 3-line note under another stakeholder is still context. Top-level-only search fails this pattern.
6. **Near-match names are unverified identities, not variants.** When a name James uses is a close-but-not-exact match to a documented person (Jiajing≠Jiaxing, two Daniel Lius), do NOT silently merge — check role/org consistency, and if anything mismatches (or the merged read becomes load-bearing), ask James one disambiguation question before building on it. Chinese-name romanizations collide often; a one-character difference is a different person until confirmed.

**What Leo should do instead when the pattern might fire:**

- Spend one Grep before the analysis, not after.
- If documented playbook exists, SURFACE it first: "Existing playbook in `stakeholders.md:913` says [X]. Does that still apply, or has something changed?"
- If the playbook feels stale, name the staleness: "The 4/09 playbook assumed [X]. Given [new info], worth updating?"
- Only propose reinvention if James explicitly asks OR the existing playbook is obviously broken by new data.

## Absorbed from auto-memory (2026-06-26)

Migrated feedback memories — same root ("read/verify what exists before reasoning"):
- **check_team_context_first** — read `work/people/team_members.md` before analyzing any Slack exchange or interaction involving James's reports; don't assume roles or pronouns.
- **read_recent_files_before_critiquing_artifacts** — before critiquing a stakeholder artifact (1:1 notes, draft memo, talking points), `ls -lat` the dir for the longer companion doc the compressed version usually sits on top of.
- **verify_load_bearing_facts** — before anchoring a multi-turn analysis on a strategic fact (level, timing, manager-state, role-arc), surface it for verification. Hold a higher staleness prior on old `.md` / auto-loaded context; verify the load-bearing ones specifically, not every detail.
- **dont_over_fortify_on_sensitive_intel** — when James shares sensitive stakeholder intel, check whether a structural fix is already happening at someone else's altitude before posturing defensive scripts; don't over-build alarm-bell rules.
