# Recsplanations Magic Dimensions — Dylan's product-direction note + prep

**Source:** Dylan's 1:1 doc (2026-05-24). She wrote down what she sees as the four important parts of the magical Recsplanations / Anticipation experience.

**Scope:** Product-direction thinking. **NOT** load-bearing evidence for the team-design / reorg case — that conversation stays clean. See `work/people/dylan_archive.md` Appendices III-C / III-D for the team-design workstream.

**Owner:** James. Working doc. Grows into a 1-page eval framework for next Dylan 1:1.

---

## The four dimensions (verbatim from Dylan's note)

1. Cohesion of the "origin pins" in recsplanations ("origin theme")
2. Cohesion of the recommended pins in the cluster ("recs theme")
3. Aesthetics of the pins we recommend
4. Big enough jump from the rest of the feed to feel distinct

---

## What she means — three jobs underneath

Four dimensions, but they decompose into three jobs: **premise**, **polish**, **staging**.

### Premise (D1 + D2 — the cohesion pair)
Does the recommendation MAKE SENSE to the Pinner?
- If origin pins look random → *"we noticed you like X"* premise breaks
- If recs scatter across themes → cluster breaks
- Cohesion is upstream of everything else. Nothing downstream saves an incoherent cluster.
- **Substrate-level levers:** UIC for cluster identification, pUIC for cluster-conditioned prediction, RR feedback loop for cluster fatigue / elevation.

### Polish (D3 — aesthetics)
The pins must look good.
- Underrated lever. Most ranking optimizes for engagement signals, not visual quality.
- Dylan is naming aesthetics as a **first-class** product dimension. That's unusual.
- **Substrate-level levers:** CLR / LWS quality ranking; Pinkerton VLM visual-signature work (extract user's aesthetic preference, score candidates against it).

### Staging (D4 — feed-jump distinctness)
The Pinner must perceptually register "this is different."
- Mini-grid + reference-pin stack + explanatory copy only works if the perceptual contrast is large enough.
- Combination of UI/UX (rendering, layout, typography) + product-side density decision (how often to surface, what fraction of feed).
- **NOT in my team's substrate.** Surface engineering wedge — Tim partnership required; Mira on design.

### Implicit hierarchy
Premise → polish → staging. Pinner has to **believe it**, then **trust the pins**, then **perceive the differentiation**.

---

## The subtraction signal (also revealing)

NOT on her list:
- CTR / engagement / NDCG
- LLM-generated explanation copy
- Personalization depth
- Latency / coverage / operational metrics

**Read:** She's operating at product-experience altitude, not metric altitude. Standard ML lever set is downstream of these four. If we chase CTR, we may miss the magic; if we land these four, CTR follows. Hold this as how she will likely evaluate the work — and as a quiet warning if the team's current optimization defaults toward engagement metrics.

---

## Team workstream mapping — current coverage + gaps

| Dim | Workstream | Owner(s) | Coverage | Gap |
|---|---|---|---|---|
| D1: Origin theme cohesion | UIC clustering | Yuke | Substrate exists | Origin-set coherence eval probably missing |
| D2: Recs theme cohesion | Cluster-conditioned retrieval, CG quota tuning | Yidi, Yuke | Partial — quota tuning live, conditioning evolving | Intra-cluster coherence metric for retrieval not formalized |
| D3: Aesthetics | CLR / LWS quality ranking; Pinkerton VLM signature | Devin / Yali, Hedi, Zili / cross-team Anna | Partial — quality features exist, aesthetics not primary objective | Aesthetics as a *primary* objective is under-invested. VLM-extracted user aesthetic preference V0 done (5/23) but not yet feeding production. |
| D4: Feed-jump distinctness | UI/UX rendering, density logic | NOT in my team | None on my side | Tim's team owns rendering; product-side density decision is Anna's. My team contributes nothing here directly. |

---

## Eval framework sketch

Don't optimize what you can't measure. Per dimension:

### D1: Origin-set coherence eval
- UIC cluster silhouette score on the origin pin set
- Intra-set semantic similarity (embedding-based)
- Origin-set "intent coherence" — VLM-driven check (is this a coherent intent, or a grab-bag?)

### D2: Recs-cluster coherence eval
- Intra-cluster semantic similarity for retrieved candidates
- Right kind of diversity — intra-cluster low-diversity (cohesive), cross-cluster high-diversity (varied feed). Standard recsys diversity metrics will mislead here.
- Drift metric — how far does the recs cluster drift from the origin cluster?

### D3: Aesthetic eval
- VLM-scored pin aesthetic quality (taste score)
- On-trend / contemporary scoring (avoiding stale aesthetic)
- User-conditional aesthetic alignment — given this user's aesthetic preference (Pinkerton VLM signature), how aligned is the recommendation?

### D4: Distinctness eval (collaboration with Tim's team + Anna)
- Perceptual contrast vs surrounding pins (visual + layout)
- Frequency / density — how often does Recsplanations show vs feed coverage
- A/B perceived-distinctness rating (qualitative user studies)

**Cross-cutting:** all four evals feed a composite *magical experience* score that's not reducible to engagement. The composite is the leading indicator; CTR / engagement are lagging indicators. Worth naming this explicitly to Dylan — gives her a frame to evaluate the work without re-anchoring on metrics.

---

## Prep moves

### 1. Build the 1-page eval framework for next Dylan 1:1
Right altitude: *"Here's how I'm operationalizing your four dimensions — four evals, current coverage, gaps. Want to refine before we sequence work?"* Fast, light, conversational. Demonstrates I heard her and am already building. **Don't show up with 20 pages — wrong altitude.**

Suggested 1-page structure:
- The four dimensions verbatim, credited to her
- Premise / polish / staging frame
- One eval per dimension (sketch — refine in conversation)
- Current coverage + named gaps
- Three questions (priority order? tension with engagement metrics? sequencing recommendation?)

### 2. Questions to deepen understanding with Dylan
- Are these four in priority order, or all need to land together?
- Any in tension with engagement metrics? Which wins?
- Who else has these four written down? (Anna? Mira? Design?)
- What's "magical" benchmarked against — a competitor surface, an internal reference, a Pinterest-of-the-future vision?
- Launch criteria — when does Recsplanations *feel* magical enough to ship broadly?

### 3. Quietly map for sequencing
Once dimensions are operationalized, the work sequences as:
- **Premise first (D1 + D2)** — substrate work, my team owns end-to-end
- **Polish second (D3)** — quality ranking + Pinkerton VLM signature integration
- **Staging third (D4)** — Tim partnership, requires alignment on density + rendering with Anna

This sequencing matches the hierarchy AND the team-shape. Don't pitch this — let it emerge from operationalizing the evals.

### 4. Pinkerton VLM signature as the bridge
D3 (aesthetics) — and the aesthetic-continuity slice of D2 — is exactly where Pinkerton VLM visual-signature work pays off. V0 done per 5/23 RR update. Phase 1 (cohort mode + MCP wrapper) is post-China. This is the load-bearing technical bet behind D3, and it's already in-flight. Worth naming to Dylan as the substrate piece that earns D3.

### 5. Loop Anna and Yuke / Yidi before the 1:1
- Anna — does she have her own dimension list? PMs often have parallel framings. Reconcile before going back to Dylan with the composite.
- Yuke + Yidi — frame cluster-coherence as their owned metric. Gets buy-in early; they'll be the ones running it.

---

## Strategic note (sponsor-coded)

Operationalizing these four well IS the sponsor-coded behavior — separate from any reorg ask. Mastery of Dylan's product direction = natural product-direction owner positioning. The team-design conversation stays clean; this builds in parallel.

**Hold the org-shape map and the product-direction map separately.** They overlap structurally (most dimensions land in my team) but they are NOT the same conversation. Conflating them = opportunistic. Doing both well, separately = Director-altitude.

---

## Open

- Confirm dimension priority with Dylan
- Confirm tension-with-engagement-metrics policy
- Validate premise / polish / staging frame — is this how she'd carve it?
- Anna's product-direction view vs Dylan's — same four, or PM frame differs?
- Mira (design) — own dimension list? Worth asking.

## Next

- Compress this into 1-page version for next Dylan 1:1 (cut workstream table; keep premise / polish / staging + per-dim eval sketches + gaps + Qs)
- Discuss cluster-coherence eval framing with Yuke and Yidi — get their take, frame as their owned metric
- Loop Anna informally — does she have a parallel dimension list?
- Bring back into Anticipation Foundations workstream as the eval north-star
