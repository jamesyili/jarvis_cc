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

## Related

- `upp/cfm_technical.md` §6 (CFM model scaling, in-flight) · `upp/upp_retrieval_assessment.md` §What's Missing · `upp/ubr_design.md`
- `retentive_recs/retentive_recs.md` §2026-08-27 (RR focus-areas snapshot incl. LLM pUIC)
- `reflex/program_state.md` · `reflex/eval/`
- `cost_investigation_2026.md`
- `../career/compounding_assets.md` (#1 ML Day theme, #2 Reflex eval as a standard)
- KB: `kb/hard/wiki/llm-recsys.md`, `kb/hard/wiki/generative-recommendation.md`, `kb/hard/raw/louis-wang/` (HSTU/OneRec/PLUM in production; TurboQuant), `kb/hard/raw/arxiv/evorec-self-evolving-agentic-recommender-systems.md`
