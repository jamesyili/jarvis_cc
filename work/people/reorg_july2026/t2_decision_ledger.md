# T2 Decision Ledger — what's decided, what's undecided

*Living ledger, dated entries newest-first. Created 2026-08-21 at James's instruction ("write down what's decided and what's undecided"). Scenario analysis stays in `t2_team_setup_scenarios_2026-08-11.md`; the boards themselves in `scenario_boards/`; process discipline in `t2_ownership_ask_timeline_2026-08.md`. This file is the running answer to "where are we?"*

---

## Entry 2026-09-03 (Thu, remote session, evening) — five own-voice placement reads in one day; Roderick stays with Daniel

**DECIDED (the people's own voices, James's 1:1s 9/3):** **Roderick → stays Daniel** (closes the 8/19 "his own voice" gate; supersedes "UEB → Alim in every scenario") · **Yongwoo** — fine with anything, even outside Daniel's scope; meaningful work over promotion · **Felix** — happy with whatever; Unity-layer (serving) experience, not ML infra · **Balaji** — either manager, LWS or CLR "equally interesting," one criterion = no mid-project change three months in → **Alim + Daniel decide, James brings him the recommendation** · **Ryan (+Rui)** — LWS lean, willing to carry retrieval ML infra (Manas).

**UNDECIDED / re-foot before the next board:** UEB's landing (does the charter follow Roderick to Daniel, or does Roderick leave it?) · Esteban (follows Roderick per the 8/23 pairing rule) · **Daniel's ≤12 cap** with Roderick + Esteban + Ryan/Rui + Yongwoo/Felix all on his line · Balaji's seat = the LWS-vs-CLR balance lever (LWS over-supplied, CLR thin) · Kim 9/11 (last open input) · Shopping owner (#3 in the 9/1 entry — urgent per Dylan's "TP Load and Impact," Fri 9/4). Per-person detail: `../team_members_scope.md` 9/3 entries.

**BOARD — Sc 9 (James, 9/3 evening, phone): "start with scenario 6, then…"** Ryan → Daniel (LWS, with Rui) · Roderick + Esteban stay Daniel · Richard Wang (REQ-2, SWE II IC14, starts 9/21) → Alim · Yuke + Hanlin (RecGPT/GenRet) → James · Zili → James (PIP case; backfill unknown). Saved as `scenario_boards/scenario_9_2026-09-03.json`; checker (rulebook vintage 8/21): **James 7 / Alim 10 / Daniel 11 — 0 blockers, 5 forks, 7 watches.** Forks: LWS at 3–4 vs target 5 (the real gap, and it's MLE-shaped) · GenRet on James (park vs end-state — say which) · Roderick → Daniel (own voice now in; the 8/10 UEB word still needs a walk-back or UEB moves with him) · UPP+CLR pool at 5 (Yiping left on Daniel from Sc 6 — 8/21 ruling says Alim; with Yiping + Richard the pool is back to 7, which is what makes the Ryan-for-Richard swap balance). Watches: UEB split (Lionel on Alim, Roderick + Esteban on Daniel) · James at 7 directs incl. both perf cases · Yang mid-leave to Alim (Dylan accepted 9/1). **James's undecided list (Notion, 9/3):** who joins LWS/L1 Utility · who joins CLR · how much to keep funding Collection P13N · UEB (charter vs ad hoc) · what we're actually doing for IB · for LLM pUIC · Zili backfill (ping Amanda Gomes). Leo's adds: Yiping's line · RecGPT's November home vs park · Shopping/MDD owner (#3, urgent) · Nima's day-one lane (9/8) · the announcement date (9/14 vs 9/21). Leo reads → session log 9/3.

**RULED 2026-09-03 (James, evening, after the Sc 9 checker read):**
1. **Yiping stays with Daniel** — supersedes 8/21c (CLR pool 7th). Sc 9 as saved is the intended board. ⟨LWS's 5th by the 8/21 interchangeability rule, or RB — confirm⟩. UPP+CLR pool = 6 with Richard; pool-7 target retired unless re-stated.
2. **If Balaji chooses Alim, Ling does not travel with him** — the 8/15 IB pairing is broken by ruling; Ling stays Daniel (Chuxi's delivery partner in practice). Branch arithmetic: Alim 11 / Daniel 10 — fits with headroom.
3. **RecGPT (Yuke + Hanlin) stays with James in the interim through EOY** — *"there's a lot of context behind CLR and I want him to do well, so I don't want him to take on the context for RecGPT in addition to CLR."* → **Alim once Yuke's case settles, if it settles well.** James's framing: not ideal, temporary; the load shed (CLR, LWS, Retentive Recs all off his line) is what makes Hanlin + Yuke manageable and gives "a bit more flexibility" on RecGPT. Ledger undecided #1 (GenRet owner) → **resolved as a dated park: James through EOY, Alim conditional.**

---

## Entry 2026-09-01 (Tue, remote session) — Dylan ratified the structure; her four clicks; Yang → Alim accepted; 🔒 freeze

**RATIFIED (Dylan, structure 1:1, her words):** *"Overall, glad for focus under each manager and thank you for leading the discussions. This looks good to me."* The shape shown was the 8/29 work-side Org Setup summary (areas + rough people). Nothing in the DECIDED spine below was challenged. Full 1:1 record → `../dylan_wang_archive.md` 9/1.

**Her four questions — all ownership-coverage, none direction — and the answers now on record with her:**
1. **Heuristic CGs** → get rid of them → **CLR owns the sunset.** (decision, in the room)
2. **L0/L1 split** → **a primary EM + a TL POC per top-down project.** (mechanism, in the room — the routing-table exercise, restated as a rule)
3. **MDD + Shopping** → "figure out," likely Daniel's team. ⟨**open**; as dictated — confirm what MDD expands to and land the owner before Oct 1; this is the E-3 class of gap: an ownership question that reached her desk⟩ **9/3: now urgent — Dylan's "TP Load and Impact" (Search free-to-paid spillover into Core; Fri 9/4 11:30, James + Dhruvil) is about organic shopping pins. Walk in with a TL POC per her own 9/1 rule (Leo rec, unratified: JJ on measurement + the retrieval-efficiency POV, Devin on shopping-CG consolidation) — `../dylan_wang_archive.md` 9/3.**
4. **Why Yang under Alim** → James: Balaji may switch, more senior people under Alim → Dylan: **Alim already has IC15s, fine with the transfer.** → **Undecided #4 (Yang's T2 line) is effectively settled: Alim**, with her OK. ⚠️ On the 8/21 arithmetic that puts Alim at 13; the 8/29 work-side board presumably re-footed (invisible here) — check before the next scenario run. The people-care flag (returning to a manager he's never met) still applies; Alim should be the one to reach him before the announcement.

**Also on her radar now (from James's own mouth, as the Yang rationale):** "Balaji may switch." That is a *maybe*, offered as pre-wire for the ~Oct L16 line move that needs her sign-off (undecided #2). The 8/30 Dylan-facing rule holds: the wavering ("Jan/Feb yes, now unsure") stays unshared; with her it is scope, never the choice.

**🔒 Hiring freeze is coming** (Dylan, "don't tell anyone" — Code Red from monetization). REQ-2 has a verbal accept (Richard) → sign this week. Consequence for this ledger: **undecided #5 (the UPP hedge req) is effectively closed** unless it opens before the freeze; every board from here assumes no new reqs — REQ-2 is the last seat that fills. Nima 9/8 and Yiping ~9/14 are in-seat moves, unaffected.

**The three people-side asks — MADE, AGREED (Dylan, 9/1).** She'll do the 1:1s and asked James to **schedule them through her EA "when you think it's the right time."** Timing is James's lever — which is the guard the 8/30 Balaji rule needed. Sequence (Leo rec, unratified): **Chuxi first, soon** (recognition; burnout-adjacent) → **Kim after the ~9/14 announcement** (never before 9/11) → **Balaji last, after the ~Oct IB gate or after his own answer lands** — scope, never the reporting line; no senior gaze mid-deliberation. Pending-not-contested list: add "schedule Dylan×Chuxi via EA" as the first move.

---

## Entry 2026-08-30 (Sun, remote session) — Balaji own-voice datapoint (first-hand)

**Balaji → James directly (week of 8/24):** if James had asked in Jan/Feb whether he wanted to switch managers, "definitely yes" — now he's not so sure and needs to think about it. He noted Daniel also had a hard time during the friction period ("it's not entirely his problem" — Balaji's own framing, holding both sides). Separately: he wants scope that is **less 0-to-1, more incremental**.

Weight: this is **first-hand own-voice**, unlike the Roderick relays — but it's a *deliberation in progress*, not an answer. Treat as: tension with Daniel partially resolved and cooling; the reporting-line question stays open at Balaji's pace. Do not force a read; the ~Oct gate (undecided question 2) remains the decision point. The scope-flavor want (incremental, at-scale) is the actionable part now — it constrains what a good landing looks like for him regardless of line.

Dylan-facing rule (James, 8/30, prepping the structure 1:1): if Dylan engages Balaji, it must be about **scope, never the reporting-line choice** — senior gaze mid-deliberation hardens whatever gets said. The wavering itself ("Jan/Feb yes, now unsure") is not shared with Dylan; only the stable parts (wants incremental scope; friction easing, situational on both sides).

---

## Entry 2026-08-28 (Fri, remote session) — preferences only, nothing decided

**Nothing in this entry is a decision.** These are stated preferences — inputs under published criterion 3 ("preferences are inputs, not claims; everything goes into the design, nothing said now is a commitment"). Recorded here so they can't quietly harden into expectations, and so the trail shows what was known when the fall calls get made.

### STATED PREFERENCES (inputs, not commitments)

| Who | Preference | Source | Weight |
|---|---|---|---|
| **Ryan + Rui** | Want to work together on **LWS + L1 utility** | James-heard | Two-person, mutual. Continuity-flavoured: Ryan's 7/15 workstream line is already "CLR · LWS (dev-velocity focused)" and Rui owns L1/Real-Time, which is where LWS's obligation load runs. |
| **Yichi** | Happy on **CLR**; **eventually wants more UPP**; **fine with Alim** | James-heard | First preference datapoint on file for him. Costs nothing today — it agrees with the settled board. The UPP want is the part to hold. |
| **Roderick** | **Wants to keep reporting to Daniel** | **JJ → James (secondhand)** | Second independent relay pointing the same way as Daniel's 8/19 report. Confound reduced (JJ has no stake in the answer), **not** removed. Own voice still the gate. |

**Roderick — explicit stance (James, 8/28): let him come to James himself.** No summons, no prompting. Undecided question 3 below is unchanged; the 8/10 word ("your deepest priority will always be UEB") still stands, and Roderick → Daniel remains cap-blocked at 13 regardless of what he wants.

### Board work (exploratory)

- **`scenario_boards/scenario_8_2026-08-28.json`** — Sc 6 with Ryan → Daniel/LWS and the Zili backfill seat → Alim, to test whether the Ryan+Rui preference can be honoured inside the caps. It can: **James 4 / Alim 12 / Daniel 12**, LWS lands exactly on its target of 5 (Yali, Hedi, Rui, Ryan, REQ-2) with Ryan replacing the backfill 1-for-1. Costs: UPP+CLR pool 6 → 5 (worst of the eight boards; CLR drops to Devin/Yichi/Nima), and Alim's 12th becomes a req whose existence is dated by Zili's PIP/severance outcome rather than a body. **A scenario, not a proposal.**
- `check_scenarios.py` — fixed a hardcoded absolute path, now auto-discovers `scenario_*.json`, and honours a per-board `workstreams` override so a board that moves someone *into* a workstream is scored on its real shape. Fresh run of all eight boards: `issues_report_2026-08-28.txt`.

### Open capture item

- The **Tue 8/25 1:30 Roderick "choice conversation"** outcome has never been filed (carried unfiled from the 8/25 log). If it happened, an own-voice datapoint may already exist and simply be uncaptured — worth checking before treating JJ's relay as the newest information.

---

## Entry 2026-08-21 (Fri morning, remote session)

### DECIDED — workstreams (the spine)

| Workstream | Owner | People |
|---|---|---|
| UPP | **James** | Piyush, Zihao |
| Reflex | **James** | JJ · Bella (Reflex 1° / RecGPT 2°) |
| LWS | **Daniel** *(settled 8/21; T1 grant confirmed)* | Yali, Hedi, Zili-seat/backfill, Rui, + REQ-2 |
| CLR | **Alim** *(settled 8/21; his own 8/20 lean confirmed)* | Devin, Yichi, Ryan, Nima, Yiping (~9/14) |
| RR | **Alim** *(confirmed 8/21; incumbent-blessed since 8/11)* | Chuxi (ws-TL), Yidi, Alok, Kim (pencil) |
| RB / Collection P13N | **Daniel** *(confirmed 8/21)* | Yongwoo, Felix |

### DECIDED — people & mechanics

- **Bella stays James-direct** on every board (rating-handoff hold); if GenRet moves, the charter matrixes without her.
- **Kim → RR under Alim** (8/21 pencil, her lean). Structure finalized: her choice RR-vs-CLR by **9/11**; reports to a line EM either way; announcement ~9/14 (slide-to-9/21 rec open).
- **Yiping out of RB → the UPP+CLR pool as its 7th** (8/21). Execution = the 8/19 joint decision with Daniel: RB ramp from 8/24, James meets her week 1, transition ~9/14. No promise-ledger cost.
- **Zili's line stays James through the PIP case**; she is severance-seeking — her LWS seat is planned as **backfill (open)**.
- **Rui rides with LWS** · **Nima rides with CLR** · **Ryan full-time CLR** (was secondary).
- **Staffing targets:** UPP+CLR = **7** (Piyush, Zihao + Devin, Yichi, Ryan, Nima + Yiping) · LWS = **5** (Yali, Hedi, Zili/backfill, Rui, +1).

### RULED 2026-08-21 (James)

1. **REQ-2 ↔ Yiping are interchangeable** — both new, both IC13 MLE. One fills the UPP+CLR 7th, one fills the LWS 5th; default assignment = Yiping → CLR pool (her standing want + the 8/19 joint decision), REQ-2 → LWS. Swappable without redesign.
2. **The ≤12 cap counts everything:** a person on leave (Yang) counts, and open reqs count.

### THE ARITHMETIC CONSEQUENCE (falls out of the rulings — check before any move)

With the spine + rulings, the working board is **exactly James 4 / Alim 12 / Daniel 12** (Alim: RR 4 + UEB 3 + CLR 5 · Daniel: LWS 5 + GenRet 2 + IB 2 + RB 2 + Yang). **Both EMs at cap, zero headroom.** Therefore:

- **Roderick → Daniel is arithmetically blocked** (13) unless something displaces — realistically only if the IB gate misses *and* Balaji/Ling redeploy off his line, or a Daniel want yields.
- **GenRet → Alim is arithmetically blocked** (14) — the fork is effectively *Daniel vs. continued park*, no longer Daniel vs. Alim.
- **Any new hedge req must land on James's line** (no cap) — which is where a UPP hedge would sit anyway.
- Kim choosing CLR instead of RR changes nothing: Alim stays 12.

### UNDECIDED — the five questions

1. **GenRet/RecGPT owner.** Daniel wants the scope (senior-growth motivation; not Bella — carve standing). Alim's stated preference "probably isn't RecGPT" — a lean away, **not** a decline (James's 8/21 correction of an earlier overread). Park with James stands procedurally; **November decides** on evidence + the published criteria. Under the cap ruling the live fork is Daniel-vs-park. Yuke's line moves ≥9/14 regardless (peer-validation Aug–Sept).
2. **IB · LLM-pUIC.** Two nested questions at the **~Oct gains-origin gate**: does IB carry forward, and which EM's LLM lane does the Area 9 capability attach to. Balaji + Ling travel as one group; Balaji's L16 line move needs **Dylan sign-off**. This is also where Daniel's cap trade resolves: his wants (LWS-5 + GenRet + RB + Roderick + IB + Yang) sum to 13–14 vs his own ≤12 — the gate decides which want yields.
3. **Roderick.** Contested both directions: Daniel wants to keep him (all 3 of his scenarios); the off-UEB-post-Q3 preference is Daniel-sourced and uncorroborated; moving him off UEB requires James to explicitly walk back the 8/10 word ("your deepest priority will always be UEB") and guts UEB's systems spine on Alim's weakest axis. **Gate: Roderick's own voice — the pending skip-level is the highest-information move left.** *(8/28: JJ relays that Roderick wants to stay with Daniel — a second secondhand source agreeing with Daniel's, which reduces but does not remove the confound. Gate unchanged; James is letting Roderick come to him. See Entry 2026-08-28.)* UEB's shape (intact under Alim vs. split) and Esteban follow his answer. Note: keeping him on Daniel is also cap-blocked at current counts (see above).
4. **Yang's T2 line.** Undecided. Under the strict-count ruling he consumes a cap slot wherever he lands — currently penciled on Daniel (his day-1 line, fits at exactly 12); moving him to Alim would breach. Mid-leave manager changes also carry a people-care flag (he'd return to a manager he's never met).
5. **The UPP hedge.** Piyush is an unhedged SPOF at UPP = 2. Does James open a new req (lands on his own line, no cap issue) — and does it happen inside the free-quota window (~400 candidates, LR mid-Aug, zero L2 cost) before it closes?

### PENDING, NOT CONTESTED (dated waits, no open argument)

- Kim's **9/11** confirmation → announcement **9/14** (Leo rec to slide to Mon 9/21, unratified).
- **Chuxi/Kim named-lanes charter** (Chuxi ws-TL · Kim explorative-pUIC spine) — due before the announcement; Olafur anchor ask attached.
- **Phase-1 symmetric ownership ask** ~9/15 (Leo rec: slide to wk of 9/21 given the offsite collision + Daniel's China-remote window, unratified).
- **LLM×Recs lane sizing/naming** for October brokering: Daniel's bet sized from his own can-merge list; Alim's grant scoped to *LLM-pUIC inside RR*, never "LLM stuff."
- GenRet park comms + Yuke ≥9/14 transfer mechanics, whichever way the fork resolves.
- November = the settle-as-summary, per the published process.
