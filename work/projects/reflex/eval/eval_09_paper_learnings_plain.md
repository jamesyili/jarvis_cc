# The eight papers behind the Curator/Skeptic work — plain-language learnings

**James Li · 2026-08-28 · a reading doc, not a proposal.** Eight papers: the four most relevant from the 8/15 batch and today's four. Each one: what they built, what they found (with the number), and what it means for Reflex's two quality agents. Vocabulary: the **Curator** is the memory writer (turns expert comments into dead ends and analytical checks); the **Skeptic** is the gate (red-teams a card before a human sees it); the **DS Agent** is the card author. Full entries with citations are in `eval_06`; the synthesis is `eval_08`. Read this first.

---

## 1. SkillOS — Google Cloud AI Research / UIUC / MIT

**What they built.** An agent that does tasks, plus a separate "curator" model whose only job is to maintain a library of skills — it can insert a new skill, update an existing one, or delete one. The agent is frozen; only the curator learns. They trained the curator with reinforcement learning on whether the agent did better after its edits.

**What they found.**
- The trained curator lifted the agent from 47.9% to 61.2% task success (ALFWorld). A frontier model used directly as the curator did *worse* than their small trained one — being smart isn't the same as being a good librarian.
- **An untrained curator mostly inserts. A trained one mostly updates.** As it got better, "add a new skill" fell and "revise an existing skill" rose. Their words: the dominant form of learning is revising what you already have.
- The better curator's library was used *more* (72.9% of entries retrieved, up from 53.6%) while the agent pulled *fewer* entries per task (1.95, down from 2.24). Precision, not volume.
- They needed an explicit penalty on library size to stop the curator from pasting whole transcripts in as "skills."

**What it means for Reflex.** The Curator is this component. Right now nobody measures it. The four numbers above (what share of the store ever gets used; how many entries a card pulls; whether it's inserting or revising) are the health check, and they can be computed from existing files. A patterns file that keeps growing, with cards citing more and more of it, is what an *immature* curator looks like in this paper.

---

## 2. EvoHarness-RL — Meta AI / UIUC

**What they built.** They noticed a long-horizon agent forgets three different kinds of things, so they gave it three separate external notepads: **Belief** (facts it has learned about the current situation), **Progress** (a list of sub-goals with a status on each), and **Experience** (lessons carried across tasks). The agent reads and writes these through a few simple actions. Then they trained a policy for *when* to use them.

**What they found.**
- Just adding the three notepads, with no training at all, took the agent from 50.0% to 77.6% on unseen tasks. Training added nine more points (86.6%). **Most of the value was the structure, not the learning.**
- Fine-tuning on examples of good notepad use made things *worse* than doing nothing (69.4%). Imitating the behavior isn't the same as knowing when it's worth it.
- Removing the **Progress** notepad hurt most on tasks with dependent sub-goals — do A, then use A's result to do B.
- After training, the agent touched the notepads *less* — about once per task. A mature system uses its scaffolding sparingly.

**What it means for Reflex.** Map the three notepads: Experience = the patterns and dead ends (exists). Belief = `context.md`, a hand-maintained file (exists, but it's a summary nobody keeps current — the World Store proposal fixes that). **Progress = nothing.** A Detect investigation is exactly a dependent-sub-goal task (form a hypothesis, check a surface, pull a number, cross-check it, decide), and the DS Agent keeps no running list of what it has actually verified.

---

## 3. EvoRec — Alibaba

**What they built.** Four agents that improve a production recommender model in rounds: one proposes research ideas, one writes the code, and a "Skill Evolver" periodically reads the memory of past experiments and distills reusable methodology from it.

**What they found.**
- +1.85% advertising revenue and +1.02% CTR in a live A/B test — both significant. Up to 5.5% offline improvement over the strongest baseline.
- Their critique of earlier systems: they used the agent "only as a code translator that accumulates no methodology." The Skill Evolver exists to fix that.

**What it means for Reflex.** This is the production existence proof that a component whose job is distilling lessons from past work pays off in money. When someone asks whether the Curator deserves engineering investment, this is the citation.

---

## 4. AutoHarness — Google DeepMind

**What they built.** They had a model write its own guard-rail code around itself — one function to propose a move, one to check whether a move is legal — and searched over versions of that code using the real environment (chess, and other games) as the judge.

**What they found.**
- **78% of Gemini-Flash's chess losses were illegal moves, not bad strategy.** The model understood chess and couldn't reliably follow the rules.
- After the harness handled legality in code: 100% legal moves in 145 games, and the small model beat the large one 56.3% to 38.2%.
- Credit assignment came from the error pattern: if the checker said "legal" and the move was illegal, fix the checker; if the checker said "illegal," fix the proposer. No judgment call needed.
- The harness didn't make chess easier. It removed the part that never needed judgment so the model only faced the part that did.

**What it means for Reflex.** Rejected cards split into two kinds: things a program could have caught (a table that doesn't exist, a column with the wrong name, a claim with no query behind it) and things that need a human's judgment (is this worth doing?). Nobody has measured the split. The Skeptic's checks 1–4 are the "legal move" checks; check 6 is judgment. If most rejections are the first kind, the leverage is in plumbing, not in a smarter Skeptic.

---

## 5. Recuris — NUS / Stanford / Oxford / Princeton *(today)*

**What they built.** A memory layer around a frozen model with four pieces they can evolve separately: a **skill library** (lessons across tasks), a **working memory** (a per-task list of goals, each with a status, the evidence for it, and any blocker), a **rule for when a skill gets pulled into context** (keyed on the working state, not left to the model), and **checkers** that mark a goal done only when the tool output proves it — never when the model *says* it's done. Between tasks, a meta-agent reads a structured trace of what happened, decides which of the four pieces caused a failure, and patches only that piece.

**What they found.**
- **The working memory alone was worth +23.9 points. The skill library alone was worth +2.0** (statistically zero). This is the biggest number in the whole set.
- Why: the model never had trouble *finding* information (88–98% recall at every task length). It had trouble *finishing* — the base agent ended 42% of tasks that needed a write without ever writing. The working memory fixed that.
- **Putting all ten skills into context every turn and letting the model decide what applies scored 65.6% — worse than having no skills at all (82.0%) — and cost 46% more tokens.** Keying which skill enters context off the working state scored 83.6%. Same skills. The difference is who decides what applies.
- Figuring out *which component* caused a failure from the outcome alone: 13% accurate. From a structured trace that logs which skill was invoked and which goal was committed: 64.8%. "The skill existed but wasn't pulled in" is *invisible* without that trace.
- Their library grew 51 added / 2 revised / 0 deleted, with 17 near-duplicates, and it didn't hurt — because the invocation rule kept the bloat out of context.
- Their acceptance gate, run on 12 test cases, had error bars ±30 points and rejected an improvement that later proved worth +12 on a bigger set. Running the same system twice with no change gave ±7 points. Small test sets can't see real gains.

**What it means for Reflex.**
- The DS Agent has no working memory. A card that *claims* a VLM check or a query it never ran is the Reflex version of "ended the task without writing." The Skeptic catches it afterward; a goal list with receipts would prevent it.
- The Skeptic reads the whole store — registry, dead ends, patterns file, audit logs — and decides what applies. That is the 65.6% row. The registry already has "applies to" and "mandatory when" fields; nothing uses them to pick what the Skeptic reads.
- The verdict log records that a card was wrong, never *which piece of memory* failed — was the pattern missing, present but not pulled, or pulled and misread? That's the 13% condition.
- The "growing patterns file is bad" worry from SkillOS is conditional: it's bad *when the reader takes everything in wholesale*. Fix the reading and growth stops mattering.

---

## 6. WikiSkill — Google Research / Virginia Tech *(today)*

**What they built.** Three layers instead of two: raw execution traces, a **wiki** of lessons (one page per failure mode or working strategy, plus an index), and the skills themselves. A "maintainer" edits the wiki every round by patching pages — never rolled back. A "proposer" reads the wiki, a ledger of past accepted/rejected skill edits, and at least four raw traces before proposing one change to a skill. The change is accepted only if it improves a validation score. The task-doing agent reads skills only — it is deliberately kept away from the wiki.

**What they found.**
- Letting the proposer read the wiki: 48.7% → 63.7% average across four benchmarks (Gemini Flash). Gains held across five models and five benchmarks, three runs each.
- **Letting the task agent read the wiki made things worse** (63.7% → 60.9%). Their read: the agent solved tasks from the wiki instead of the skill, so its traces stopped showing what the skill was missing.
- Untrained maintainer, given the rule "don't create duplicates, update existing pages" and the whole wiki as context, made *more edits than creates* for every model. Softens SkillOS's "untrained curators append."
- The ledger of past proposals is written by the harness, not the model — target, the diff, the score, accepted or rejected — and the proposer is told "do not repeat rejected approaches." A rejected abstract skill informed an accepted concrete one a round later.
- Skills written by a small model to work around its own weaknesses *hurt* a stronger model (50.5% → 18.1% on one benchmark). Domain knowledge transferred; model workarounds inverted.
- The wiki is never pruned or deprecated, and `replace` silently overwrites. They list pruning as future work.

**What it means for Reflex.**
- The Curator already does what the maintainer does, with better rules (conflict reports, never-silent retirement) — this paper can't be cited against the human gate.
- Reflex has nothing like the rejection ledger for Evolve's playbook edits. It's one programmatic append per run.
- The one-line index entry ("problem + root cause + fix") is what decides whether a page gets read. Reflex's dead-end labels carry only the problem.
- Tag every dead end as "fact about Pinterest's tables" vs "workaround for the current model." The next model upgrade then has a retirement list instead of a mystery regression.
- The Curator captures corrections; it doesn't capture what *approved* cards did right. WikiSkill harvests both.

---

## 7. Scroll — "Context as an Environment", Alibaba / Columbia *(today)*

**What they built.** Instead of summarizing old context when the window fills, they keep the entire history *outside* the prompt in a searchable log with stable addresses, plus a Python kernel whose variables persist across model calls. The model writes small programs to search the log, expand a record, compute over results, and print — and only what it prints enters the next call. When the window fills, old spans are evicted from view but never from the record, and every evicted region stays addressable through a model-written one-line headline (task, verified state, next action, status).

**What they found.**
- The controlled result: same model, same tools, only the context strategy differs. Going from 128K to 256K of history, **summarize-when-full lost 21 points; binding tool results to variables lost 2.6.**
- Summarizing tool outputs at ingestion scored 19.9% overall and near zero wherever the answer needed an exact value.
- Their failure analysis: outcomes were often decided by how the model *framed* the query before any retrieval ran; "read everything" silently became "read the first three and last two turns" under budget; and successful runs issued a *disconfirming* search before submitting while failed runs never did.
- Same harness, six different models: 22.7% to 86.7% on the hardest benchmark. A harness result on one model says nothing about another.

**What it means for Reflex.**
- The wrong-column and made-up-number dead ends are exactly what a lossy summary produces. Worth checking whether they cluster in cycles that ran long.
- The per-step headline is the cheapest possible Progress record — a spec for the missing DS Agent working memory.
- The Curator's "read ALL comments on ALL cards" rule is a good rule with a known failure: under a budget it quietly samples. Make Phase 0 a program that groups the judgment records and prints the count.
- "Ask whether you read the Cycle Learnings" is the disconfirming search as prose. Log it as a field so a PASS with zero findings can show what it looked for.

---

## 8. Perplexity Brain *(today — product post, reconstructed from coverage; the post itself is paywalled to this network)*

**What they built.** A work-memory layer for their agent: every completed task is logged (actions, connectors used, which sources validated, failed attempts, user corrections) into a context graph. Overnight, a synthesis pass turns the graph into lessons in a wiki with one page per entity (project, data source, contact, workflow step). At the start of each run the agent loads the *relevant* pages as a starting map. Every entry links back to the session that produced it. Corrections are stored as "avoid this route in this context."

**What they found.** Self-reported, no baseline: +25% correctness on repeated tasks, +16% recall, −13% cost. Don't cite the numbers.

**What it means for Reflex.** Reflex already has the harder half — capture with provenance, conflict handling, retirement rules — and Brain doesn't describe any of that. Two things worth borrowing: the split into cheap per-session capture plus one scheduled consolidation pass (the Curator currently does a full re-read on every trigger), and logging *which sources validated* — nothing in Detect records which tables or dashboards a card's evidence came from and whether a human accepted them.

---

## The six ideas that keep recurring

1. **A running list of what the agent has actually verified is worth more than any library of lessons.** (Recuris +23.9 vs +2.0; EvoHarness Progress ablation; Scroll headlines.) Reflex's DS Agent has none.
2. **Don't hand the reader the whole store and let it decide what applies.** Pick by rule — the entry's own "applies when" — and log what was picked. (Recuris 65.6 vs 83.6; WikiSkill walled the executor off; EvoHarness annealed to one call per task.) Reflex's Skeptic reads wholesale.
3. **Log which piece of memory was used or missed, or you can't tell why a failure happened.** (Recuris 13% → 64.8%; AutoHarness credit from the error pattern.) Reflex's verdict log says the card was wrong, not why.
4. **Keep the raw record; compress only the summary; never let the summary be the only copy.** (Scroll; WikiSkill three layers; EvoRec Memory vs Skill Evolver.) Reflex's judgment log and dead-end file are already in this order — the Skeptic just can't get from one to the other.
5. **Keep a ledger of what was tried and rejected, written by the harness, read by the proposer.** (WikiSkill.) Reflex has it for Curator proposals, not for Evolve.
6. **Write every lesson with a one-line index, a scope, and a tag for "fact" vs "workaround."** (WikiSkill index + negative transfer; Brain's scoped corrections.) Reflex's entries have scope, mostly; not the other two.

None of these need training. All of them are prompt-and-schema changes. Every one comes with a number you can read off `verdict_log.jsonl` or `expert_judgments.jsonl` before and after.
