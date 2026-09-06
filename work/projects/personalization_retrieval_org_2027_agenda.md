# P13N Retrieval as a research arm — 2027 agenda (working doc)

**Created:** 2026-09-05 (Saturday, Labor Day weekend, remote session)
**Owner:** James · **Scribe:** Leo
**Status:** live working doc — we keep adding to it in the course of the conversation. Dated additions go in §Running additions at the bottom; the v0 text above it stays as written.

## Origin

Opened as a comparison-engine firing (the xAI parent, "they're in AI, I'm not really"). James's one-sentence answer to "what do you build": *"I'm working on the most innovative and exciting field in recommendation systems today: how to scale user sequence and LLMs."* Within the hour the question became: **if I treat my 30-person engineering org as a research arm working on retrieval × LLMs, what are the most exciting and important things to invest in?** James flagged that the deep research he'd commissioned earlier did not consider the intersection with LLMs, and in particular how to scale LLM research, inference, and training. That research is to be merged into this doc when he passes it.

Context Leo grounded this in: `upp/cfm_technical.md` (CFM + the in-flight CFM scaling study, serving-GPU headroom fact), `upp/upp_retrieval_assessment.md` (what's built / what's missing, esp. gap #4 offline-online correlation), `upp/ubr_design.md`, `retentive_recs/retentive_recs.md` (RR focus-areas snapshot: LLM pUIC, RecGPT novel loss, Explore module), `team_members_scope.md` (RecGPT/GenRet staffing, 9/3 rulings), `cost_investigation_2026.md`, `reflex/`, and a KB sweep of `kb/hard/` on generative retrieval, scaling laws, user foundation models, inference efficiency, agentic recsys, and eval.

---

## v0 — Leo's answer, verbatim (2026-09-05)

Here's the thinking. Grounded in your stack, not a survey, and organized around the gap you named.

**The thesis**

The recsys frontier right now is the convergence of three things: user-sequence models scaling like LLMs (Alibaba's LUM and ByteDance's TokenMixer show the power law still holding at 7B+ parameters), generative retrieval collapsing the retrieval-ranking split (OneRec), and LLM semantics entering item and user representations through semantic IDs (PLUM, HLLM). Your org already has a foot in all three: UBR is the cross-surface conditional retriever, RecGPT is the generative line, LLM pUIC is nascent.

What decides who wins is not the modeling ideas. Those are published. It's whether the training and serving systems make scale affordable at request time. That is exactly what a frontier lab's real asset is, and exactly what your research missed. A lab spends a third of its effort on the systems half. Your org spends roughly none of its explicit charter on it. That gap is where a 30-person research arm can stand somewhere nobody at Pinterest is standing.

So the organizing question for the arm: **how far can the user model be scaled before the serving cost curve breaks, and how do we bend that curve?** Everything below hangs off it.

**The bets, ranked**

1. **Bend the serving cost curve for long sequences.** This is the LLM inference research mapped one-to-one onto recsys. The user's history is a prefix that barely changes between requests. Cache its attention state and only compute over new events, the recsys version of prompt caching. Add KV-cache quantization (TurboQuant gets 3-bit with no loss by preserving dot products rather than MSE), linear-complexity attention in the HSTU style, and fixing the fact your own CFM doc records: serving GPUs are host-CPU-bottlenecked with low SM activity, so the headroom is already paid for. This bet is also Jeff's GPU-cost priority wearing a research hat. "We scaled the user model 10× at flat serving cost" is one sentence that pays both the AI story and the budget story.

2. **Publish the retrieval scaling curve on your own data.** The CFM team is running the scaling study for ranking with fixed fine-tune compute. Nobody is running it for retrieval. Parameters × sequence length × data, y-axis a fine-tuned surface metric under a fixed FT budget, never pretrain loss. A curve is the artifact that turns "we do AI" into "we know the scaling law of our user model." Uses the trainer you already have. Position it as the retrieval leg of the UPP hierarchy, which already says FM → base models → surfaces, so it complements Dhruvil's and ATG's work rather than colliding with it. Remember OneTrans.

3. **Scale the teacher, not the student.** Your CFM doc already states the principle: a teacher needn't be serveable, so it can be arbitrarily better. Bella's H2 criteria already include teacher distillation. The research-arm version is a LUM-scale offline user model, 1B to 7B, that never runs at query time, distilled into the serveable two-tower and GenRet. PLUM cut serving cost over 95% by exactly this precomputation. This is the honest answer to "how do we scale LLM training here": it requires the LLM training toolkit, multi-node, sequence packing, FSDP, mixed precision. That's the training half of your question.

4. **Own the item tokenizer.** RecGPT's strategic value isn't whether it beats the L1 model. It's that the semantic-ID codebook is the shared vocabulary between your user model and any LLM. Once items are tokens, an LLM can read a user history. Whoever owns the codebook owns the interface. Invest in codebook stability under item churn (the documented brittleness of every production deployment) and cold-start via prefix generalization. Yuke, Hanlin and Bella are already here. This needs a lens, not headcount.

5. **LLMs as offline annotators for interests, not in the hot path.** Where a text LLM actually helps: cold interests, novelty, interest summaries in the EmbSum style, pseudo-labels for the exploration module. That's where LLM pUIC goes, and it is the Anna LLM-backbone thread you parked for Q4. Keep it offline.

6. **Reflex eval as the lab bench.** Alibaba's EvoRec shows agents iterating recommender models with a 1.85% revenue lift. You already run the eval lane. The unsolved upstream problem is UPP gap #4, offline-to-online correlation. Without a trusted offline-to-online map, none of the scaling curves in bets 1 to 3 mean anything. Eval is upstream of everything else, and it's compounding asset #2.

**What makes it a research arm rather than a rename**

- A compute budget managed like headcount. Labs allocate GPU-hours deliberately. Your cost investigation gives you the numbers to do this as a first-class artifact.
- Dated kill criteria per bet, in the template you handed Alim: if by X we don't see Y, we Z.
- Curves and negative results as deliverables, not just launches.
- Two places where the literature is thin and you could produce knowledge nobody has: pretraining objectives for user foundation models, and evaluation for generative recommenders beyond accuracy. The KB confirms both are gaps.

**Honest constraints**

Thirty people cannot run six bets. Bets 3, 4, 5, 6 are already in motion and need framing. The new lanes are 1 and 2, and I'd start with 1, because the first win is likely systems, not modeling, and it's the one that pays the budget. The org is mid-landing with two new EMs and a perf cluster, and Chuxi is in five of six RR areas. This agenda has to come off her plate, not onto it. And your ML Day theme, how recommendation systems learn about users and improve themselves, is this agenda: bets 1 to 4 are the learning half, bet 6 is the improving half.

When you pass the deep research, I'll merge it against this, mark where it agrees and where it missed the systems half, and file a v0 agenda doc in the projects folder. Not today unless you want it. Weekend's still off.

---

## Open

- **Merge James's earlier deep research** into this doc when he passes it: mark where it agrees with v0, where it missed the systems half (LLM inference / training scale), and anything it has that v0 lacks.
- Staffing: which of bets 1 and 2 gets a named owner first, and whose plate it comes off (not Chuxi's).
- Seam check for bet 2 with the CFM scaling group (Lawhon, Poska, Rajesh, Kelly He, Jaewon Yang) and ATG before anything is written up.
- Compute-budget artifact: what the cost investigation numbers look like recast as a GPU-hours allocation.

## Running additions

*(Dated entries, newest at the bottom. Add here as the conversation continues.)*

### 2026-09-05 (evening) — research filed, three maps built, preliminary read on who leads (Leo, unratified; adversarial verification NOT run)

**What happened.** James passed the deep-research synthesis; it is filed verbatim at `retrieval_preranking_research_synthesis_2026-09-05.md`. Leo launched a multi-agent analysis (roster/strengths → investments → research-vs-agenda diff → seams → per-lane leader candidates → adversarial verification → memo). The remote box caps the run at 2 agents at a time and the subscription hit its session limit partway: **three of four maps completed; the seams map, the five lane-candidate agents, the portfolio agent, and the synthesis did not run.** The completed maps are saved as JSON under `personalization_retrieval_org_2027/` (`map_roster_2026-09-05.json` — 34 people; `map_investments_2026-09-05.json` — 17 workstreams with keep/pivot/stop calls; `map_research_diff_2026-09-05.json`). Everything below is Leo reading those three maps directly. The leader recommendations have **not** been through the refute pass; treat them as a first read.

**1. What the research changes in v0 (from the diff map)**
- Agrees with the thesis and with bets 2, 4, 6 and the organizing question of bet 1 (its §12.7 cost-per-request formula is the same idea).
- Adds five things v0 lacked: candidate logging at retrieval/L1 as a first-class data project (rec #6); SID tokenizer SLAs (rec #7); the dense-fallback hybrid as the grounding choice (rec #8); the multi-interest A/B measured on downstream L2 acceptance (rec #9); a written L1 exit criterion (rec #10). Plus the HSTU/OneRec caveats and the 2025–26 tokenizer literature.
- Misses exactly what James said it would: user-state / cross-request KV caching, the serving-GPU headroom fact from `cfm_technical.md` §6, scale-the-teacher distillation, the fixed-FT-compute framing, the dense-LLM training toolkit, and LLMs as offline annotators.
- **Four reframes that matter for us specifically:** (a) rec #2 (L1↔L2 consistency + full-space sampling) is *already done and published* by this org — the LWS 2025 alignment campaign and the RecSys 2026 preranking oral (Hedi lead author); it is a credential, not a to-do. (b) rec #8 is RecGPT's existing architecture — PinRec *is* RecGPT (generate a representation, retrieve via ANN). (c) rec #9 has effectively been run as a portfolio decision (Multi-Embedding LR vs RecGPT for one candidate budget), never as a designed experiment. (d) "Reflex eval" and "recsys eval" are two different things — the Reflex eval lane is agent evaluation (Judge V1, GEPA calibration); UPP gap #4 is a recsys offline→online calibration problem and v0 conflated them.
- **Revised bet order (diff map's suggestion):** 1 serving-cost curve (unchanged) · 2 retrieval offline→online calibration, extending Hedi's L1 offline-replay method to retrieval recall@K (up from 6) · 3 the retrieval scaling curve, gated on #2 · 4 tokenizer as a platform service with the four SLAs (bigger than "a lens") · 5 write the L1 exit criterion (new, small, timely — the org already runs GR-as-L1 on BMI) · 6 scale the teacher (down; Bella's H2 criterion and ATG's Next-Gen Teacher already cover the first step) · 7 LLMs as offline annotators (lowest; RR prioritization sits with Alim/Anna/Krystal).

**2. The team's real strengths for this agenda (roster map)**
- Two reliable gains engines with proven TLs: LWS (Yali — 8 LRs, +0.31 SSv2 in H1, GPU serving at 100% traffic; Hedi — RecSys 2026 oral) and CLR (Devin — GPU serving via attached data, $650k saved, FM + 16k-sequence foundations).
- UPP shipped: v0 beat OneTrans head-to-head (8/1), launched on P2P 8/25; Piyush is the only IC Dylan names as able to scale her judgment; Zihao + Piyush own the cross-surface pretraining infra and the V1 FM component.
- Generative retrieval is in production: official HF-RecGPT CG, Faiss→Manas migration and the 150-sizer transfer (Hanlin), the first RecGPT L0+L1 proving-out (Bella, 8/22).
- A systems-execution culture at the IC level: GPU serving productionized across LWS, Multi-Embedding, CLR, and model-pUIC (Yidi: TorchScript, Scorpion, int8/fp16).
- Publication track: RecSys 2026 oral, KDD 2025 (Multi-Embedding), ML Symposium 2026 (Hanlin on productionizing generative retrieval).
- Eval rigor in pockets: Chuxi's LLM-judge + human-eval grounding; Yidi's train/eval consistency; Hedi's offline replay (Nov 2025) — the org's existing offline→online calibration method, for L1.
- Two experienced M16 EMs with complementary postures ("bets lean Alim, engines lean Daniel").

**Gaps, per lane (roster map):** systems — no one's charter is GPU-serving efficiency or inference research; JJ is the only IC16-grade systems owner and the most over-subscribed IC. Scaling — UPP is two people (Piyush SPOF, Zihao "not there yet"); the hedge req is closed by the **hiring freeze (Dylan 9/1, Jeff 9/2)**. Tokenizer — the three people already there (Bella, Yuke, Hanlin) are the org's most fragile cluster. Evaldata — gap #4 documented and unowned; candidate logging exists only as Alok's full-funnel logging. Armlead — Dylan 8/19: only Piyush clears "in the room when I am not"; no IC17 in the org.

**3. Where we are already invested (investments map, 17 workstreams).** Everything is a reframe; the freeze means no new headcount.
- KEEP + bounded pivot: UPP (make V1/FM work *the* retrieval scaling study with gap #4 as its first deliverable) · RecGPT/GenRet (pivot framing from "raise impression share" to "own the item tokenizer + hybrid nominator" with a dated kill criterion) · LWS + L1 Utility (convert Yali's one-pager into the rec-#10 L1 exit criterion) · Reflex (point Eval & Evolve's first measurable target at gap #4) · Foundations & Efficiency + cost investigation (pivot the remaining artifact into the GPU-hours allocation the agenda asks for) · RR/pUIC (keep as-is under Alim; agenda stays off Chuxi's plate) · CLR (dense arm of the rec-#9 A/B).
- PIVOT: Hedi's CFM comparison + V1/FM retrieval work → one fixed-FT-budget retrieval scaling study, seam-checked with the CFM group · LLM-pUIC → offline interest annotation for LFU/cold-start under the NLFU frame, tied to the ~Oct IB gate.
- STOP/SHRINK (already the direction): Learned Dynamic Triggering (cite as prior art) · Multi-Embedding LR → maintenance, reuse as the rec-#9 dense baseline · Recommended Boards → KTLO after 9/11.
- Cost facts to carry: serving GPUs host-CPU-bottlenecked (headroom already paid for); ranking cost exposure ~$6.5M/yr scaling with candidates sent; Dylan's org >$1.8M/yr over budget; $2M savings top-line on the org charter.

**4. Who leads the charge — preliminary read, unverified.**
- **Lane 1, serving-cost curve:** Yali (LWS TL; productionized GPU serving at 100% traffic; owns the L1 where the cost exposure lives) as lead, Devin as the CLR-side counterpart, JJ as architect/reviewer *not* owner. Risk: LWS is thin through September; JJ is over-subscribed. Runner-up: Devin.
- **Lane 2, calibration + scaling curve:** Hedi leads the offline→online calibration extension (his method, his paper); Piyush leads the scaling curve with Zihao running it, positioned as the retrieval leg of the CFM study and seam-checked with Lawhon's group. This is IC17 evidence for Piyush. Risk: Piyush SPOF, no hedge.
- **Lane 3, tokenizer as platform:** Hanlin as day-to-day owner (ANN migration, sizer transfer, the ML Symposium talk), with the ATG partnership; the TL question stays open until Yuke's case settles; RecGPT stays parked with James through EOY per the 9/3 ruling.
- **Lane 4, candidate logging + eval:** Hedi (calibration) + Alok (full-funnel logging seed); Chuxi's eval rigor stays inside RR. Reflex eval is *not* this lane.
- **Lane 5, the arm itself:** James holds the seat through Q4 — sets the compute budget, chairs one cross-lane review, owns the curves — with Piyush as the technical lead-in-waiting. EM sponsor: Alim ("bets lean Alim"), and the compute-budget/agenda charter doc is the natural "written thing James didn't write" for the end-of-September test. Rationale from the roster map: no IC17 in the org; Piyush is the only one Dylan names.

**5. Cheap moves for the week of 9/8 (Leo rec, unratified).** Read the three JSON maps (phone-friendly enough). Ask Hedi whether the offline-replay method extends to retrieval recall@K — one conversation. Ask Yali whether the L1 one-pager can carry an exit-criterion line. Nothing else this week: Zili/Karli Tue, Nima day one, Daniel back ~9/21.

**Owed next session:** the seams map (external owners, Dylan/Jeff priorities, seam risks) and the adversarial verification of the five leader picks — re-run the workflow trimmed to what a 2-agent box finishes (resume id and script are in the session log).

### 2026-09-06 — LLM-scaling research filed and judged; the seams map; final bet order; the leader slate (Leo, unratified; adversarial verification results appended below as they land)

**Filed:** `llm_scaling_research_synthesis_2026-09-06.md` (James's second deep-research synthesis, verbatim) and `personalization_retrieval_org_2027/map_seams_2026-09-06.md` (the fourth map, completing the 9/5 set).

**1. The LLM-scaling research, judged for a retrieval org.** James asked for discretion on relevance. Roughly a third is directly actionable; the rest is background.
- *Directly actionable → bet 1.* The serving primitives map one-to-one: user-state/prefix KV caching (its own #1 intersection), prefill/decode disaggregation, FP8/INT4 + KV quantization, speculative decoding/MTP for SID beam search. One detail matters: **UBR already runs the viewer tower on GPU and the pin tower on CPU** (`upp/upp_retrieval_assessment.md` §deploy path) — that *is* the prefill/decode split, so lane 1 starts from a structure we own, not a paper. LWS's Unified Tower + TransAct on GPU is the natural first KV-caching prototype (the research's own Stage-1 test: cache-hit rate >50% on session candidates).
- *Sharpens bet 2.* The Chinchilla inversion: recsys is data-rich and compute-starved, so the scaling question is how to convert unlimited interaction data into compute-absorbing architecture, and **the embedding-vs-dense compute allocation is the recsys-specific scaling question with no LLM analog.** That is the x-axis the retrieval scaling study should vary. MoE is the way to add capacity without serving FLOPs; overtraining-like regimes are the default, not a deviation. µP-style hyperparameter transfer makes the small-to-large sweep cheaper.
- *One genuinely new idea, reframed.* The FineWeb-Edu lesson (a cheap quality classifier beat 10× the raw data at fixed compute) applied to interaction logs. For retrieval this is an extension of work the org already does — the unimpressed dataset, Yidi's label redefinition, Hedi's pairwise-distillation blocking — so it is a cheap ablation on an existing track, not a lane.
- *The metric for the compute-budget artifact:* **model FLOPs utilization.** OneRec reports 24–29% against <5% for a classic cascade; top LLM runs reach ~40%. Instrumenting MFU on our GPU serving and training is how the GPU-hours allocation becomes a number rather than a spreadsheet.
- *Background for us, not lanes:* FP8 training, DualPipe, reliability-at-scale (only matter if a teacher gets to 1B+, and ATG owns that leg); RLHF→DPO→RLVR, test-time compute, "thinking" recommenders (ranking's and Reflex's territory, not a ~10 ms retrieval budget; OneRec's DPO lift is a ranking-surface result); foundation-model unification (strategic, not 2027).
- *Two disanalogies it names that we should carry:* item corpora change daily, so the SID space must be continually re-minted (that is exactly the codebook-stability SLA in bet 4, and the strongest argument for the dense-fallback hybrid); and 10–100 ms at 10^5+ QPS means constrained beam search, caching, and sparsity are the levers, never raw model size.
- *Its own caveats hold:* DeepSeek's margins are theoretical, vendor multipliers are best cases, and only DPO-in-OneRec, HSTU/Wukong scaling laws, 360Brew, and LLM content features are production-proven transfers.

**2. What the seams map changed.**
- **Lane 1 is the only lane with a stated executive priority behind it** (Jeff 7/22: AI/GPU usage down, cost tracking; Core ~$5M/yr over, >$1.8M under Dylan). Neither Dylan nor Jeff has said anything about scaling laws, curves, or research arms. Dylan went skeptical-technical on RecGPT as L1/L0 on 8/24. That settles the order and the framing: the agenda is presented as cost and capability, never as research.
- **Correction to v0 and to my own phrasing:** "as few models as possible" does not appear in the repo. The real direction is Dylan's CG consolidation (heuristic CG sunset 9/1; three CLR corpora as one CG; five shopping CGs → two) and Jaewon's naming doctrine (8/22). Same wind, different words. **Matthew Lawhon reports to Dhruvil, not ATG** (stale line corrected; `l1_flashpoint_2026-08.md` 8/22).
- **Lanes 2 and 3 cannot be led internally.** The fixed-fine-tune-compute framing is the CFM group's central question; a retrieval curve published without Lawhon or Jaewon as co-author reads as a race (the OneTrans pattern, pointed at us). The tokenizer SLAs run through ATG and Dinesh; joint artifact or land grab.
- **Lane 4's written L1 exit criterion lands on the August flashpoint.** Yali as single L1 POC plus a unilateral criterion is the shape that reopened it; co-sign with Dhruvil under the relay-race doctrine.
- Allies unchanged: Roberto's Jeff door (feed him the half-page on what GPU serving unblocks), ML Day chair and theme as the external legibility vehicle, Anna at Principal, Jaewon's DE, Dinesh considering Q4 UPP funding.

**3. Final bet order (supersedes v0's numbering; the diff map's order, confirmed by the LLM research):**
1. Bend the serving-cost curve for long sequences (KV/user-state caching in LWS + UBR viewer tower; quantization; the CPU-host bottleneck; MFU instrumented).
2. Retrieval offline→online calibration — extend Hedi's L1 offline-replay method to retrieval recall@K; closes UPP gap #4; gates everything below.
3. The retrieval scaling curve under fixed FT compute, with embedding-vs-dense allocation as an axis — **co-authored with the CFM group from day one.**
4. Semantic-ID tokenizer as a platform service with the four SLAs, RecGPT as the dense-fallback hybrid nominator it already is — **joint artifact with ATG.**
5. Write the L1 exit criterion — inside Daniel's LWS×UPP recommendation, co-signed with Dhruvil.
6. Scale the teacher — ATG's Next-Gen Teacher owns it; our slice is Bella's H2 distillation criterion. Do not build a second teacher.
7. LLMs as offline annotators (LLM-pUIC under the NLFU frame) — lowest; RR prioritization sits with Alim/Anna/Krystal.
- Cheap ablation on an existing track: interaction-log quality filtering/reweighting (the FineWeb lesson) on one LWS or UBR training slice.

**4. Who leads the charge — the slate (Leo; refute pass running, results in §6).**
- **Lane 1, serving-cost curve.** JJ owns the architecture and the exec story now (cost line, ISR caching paradigm, Roberto's half-page for Jeff). **Balaji** becomes the hands-on lane TL from ~Oct, landing in LWS after the IB gains-origin gate — which also answers his open LWS-vs-CLR placement with "a project that doesn't change on him." Yali (LWS GPU serving) and Devin (CLR GPU serving) own their engines; Hanlin's GQA/batch-size work and Yidi's quantization debugging as hands. EM sponsor: Daniel. Off plates: JJ drops the Shopping/MDD POC candidacy and the RR feedback-loop analysis; Balaji drops IB at the gate. Runner-up as TL: JJ himself, if Reflex Build actually folds into Shifu.
- **Lane 2, calibration then curve.** **Hedi** leads the calibration extension (his method, his paper) as the gate. **Piyush** leads the scaling-study design and the seam — Lawhon or Jaewon named co-author before anything is written; **Zihao** runs it; **Nima** shadows Zihao on UPP pretraining as third hands (the Tuesday decision; also the only hedge left for the Piyush SPOF under the freeze). EM sponsor: Alim. Runner-up for the curve: Devin (CLR FM + 16k sequence).
- **Lane 3, tokenizer as platform.** **Hanlin** as day-to-day owner (HF-RecGPT production owner, Faiss→Manas migration, the 150-sizer transfer, the ML Symposium talk; the most stable of the three RecGPT people), with Jaewon/ATG as co-owner so the SLAs are joint. Bella remains RecGPT modeling TL of record; Chuxi's 2-in-1 design is a consumer, not an owner. James holds the seat through EOY per the 9/3 ruling; the SLA doc is the Q1 handoff artifact to Alim once Yuke's case settles.
- **Lane 4, logging + eval + exit criterion.** **Alok** owns candidate logging at retrieval/L1 (extends his full-funnel logging; live thread with Karthik; one scoped deliverable, which is how he works best and what his promo case lacks). Hedi owns the calibration method (shared with lane 2). **Daniel** writes the L1 exit criterion inside his assigned LWS×UPP recommendation after ~9/21, co-signed with Dhruvil — and that is his written thing James didn't write. Kim Toy owns a quality/evaluation flywheel only if she picks RR by 9/11; not pre-assigned. JJ succeeds James on the Reflex eval thread by ~Nov (agent eval, a different thing). EM sponsor: Daniel.
- **Lane 5, the arm.** **James holds the seat through Q4:** sets the compute budget (the GPU-hours artifact recast from the cost investigation, MFU as its unit), chairs one monthly cross-lane review, owns the curves. **Piyush** is the technical lead-in-waiting (Dylan 8/19: the only one who can be in the room when she isn't; the IC17 case), with the scaling-study seam memo as his first arm-level artifact. **EM sponsorship splits by lane:** Alim sponsors 2 and 3 (bets), Daniel sponsors 1 and 4 (engines) — "bets lean Alim, engines lean Daniel." End-of-September written things: Alim = the filled-in RR focus-areas snapshot (assigned 8/27), with the scaling-study charter as his Q4 artifact; Daniel = the LWS×UPP recommendation carrying the exit criterion. External legibility comes from the ML Day chair and theme, not a title.

**5. This week (Leo rec, unratified; cheap first).**
- **Tue 9/8, Nima's lane:** UPP pretraining under Zihao, not CLR. Cost named honestly: CLR loses the senior hire it was designed around and Alim's operating model still wants a pushback TL; Richard (9/21) and Yichi are CLR's bodies. The agenda's scaling lane and the Piyush SPOF both argue for UPP.
- Ask Hedi whether offline replay extends to retrieval recall@K (one conversation, after his oncall week).
- Ask Yali, when he is back 9/18, whether the L1 one-pager can carry an exit-criterion line — then hand the line to Daniel's recommendation, not Yali's doc.
- Feed Roberto the half-page on what GPU serving unblocks (lane 1's exec story) — the ammo agreed 8/14 and still owed.
- Nothing else. Zili/Karli Tue, Bella re-entry ~9/8, Daniel dark to 9/21.

**6. Verification results.** *(pending — refute pass running; to be appended.)*

## Related

- `upp/cfm_technical.md` §6 (CFM model scaling, in-flight) · `upp/upp_retrieval_assessment.md` §What's Missing · `upp/ubr_design.md`
- `retentive_recs/retentive_recs.md` §2026-08-27 (RR focus-areas snapshot incl. LLM pUIC)
- `reflex/program_state.md` · `reflex/eval/`
- `cost_investigation_2026.md`
- `../career/compounding_assets.md` (#1 ML Day theme, #2 Reflex eval as a standard)
- `retrieval_preranking_research_synthesis_2026-09-05.md` · `llm_scaling_research_synthesis_2026-09-06.md` (James's two deep-research syntheses, verbatim)
- `personalization_retrieval_org_2027/` (the four maps: roster, investments, research diff — 9/5; seams — 9/6)
- KB: `kb/hard/wiki/llm-recsys.md`, `kb/hard/wiki/generative-recommendation.md`, `kb/hard/raw/louis-wang/` (HSTU/OneRec/PLUM in production; TurboQuant), `kb/hard/raw/arxiv/evorec-self-evolving-agentic-recommender-systems.md`
