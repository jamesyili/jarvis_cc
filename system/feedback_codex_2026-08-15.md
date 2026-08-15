# Feedback for Codex / Leo — Three High-Leverage System Fixes

**Written:** 2026-08-15  
**Status:** proposal — no implementation started  
**Thesis:** Do not add more agents, skills, source material, or autonomous behavior first. Leo has a strong context base and a growing workflow library. Its next gains come from making quality measurable, context trustworthy, and external expertise composable.

---

## Executive summary

Leo is already unusually capable at context-rich thinking partnership, writing, coaching, and producing durable artifacts. Its limiting constraint is no longer the absence of instructions or information.

The next three fixes should be:

1. **A compact, human-owned evaluation harness for Leo.** Make changes to skills, prompts, and instincts prove that they improve important behavior rather than merely sounding sensible.
2. **A context compiler and freshness system.** Make current operational truth easy to retrieve, source-linked, dated, and explicitly superseded when it changes.
3. **An external-expert intake workflow.** Treat high-value systems outside Leo—starting with the Ethan Evans Custom GPT—as specialist inputs that Leo can contextualize and preserve, rather than trying to clone them blindly.

The ordering is deliberate:

```text
Measure quality  →  stabilize context  →  add outside intelligence
```

Adding more capabilities before the first two increases the chance that Leo becomes an impressive but increasingly inconsistent prompt pile.

---

## 1. Build a small evaluation harness for Leo

### Problem

Leo is modified continuously through changes to `AGENTS.md`, portable workflows under `prompts/`, Claude-specific skills, system instincts, source files, and integration code. Today those changes are mostly judged by intuition and a single live interaction.

That is enough to catch obvious failures, but not enough to reliably detect regressions:

- A rule that prevents premature questions can make an agent over-act when it should wait for an irreversible decision.
- A rule that improves executive communication can make an emotional-support response feel cold or overly strategic.
- A new instinct can resolve one past correction while conflicting with another one in a different setting.
- A workflow can become more thorough while becoming too slow, verbose, or artifact-heavy for James's actual use.
- A tool transition (for example Claude Code → Codex) can subtly change which context is available, which hooks run, and what behavior is preserved.

The system already has the raw material for this: session logs, corrections, durable instincts, approved outputs, and repeated task categories. What it lacks is a repeatable way to ask, **“Did this change improve Leo where it matters?”**

### Target behavior

For any meaningful change to Leo's behavior, an operator should be able to run a small set of representative scenarios and answer:

1. Did Leo load the correct context and distinguish current fact from stale or uncertain context?
2. Did it select the correct mode: fast drafting, thinking partner, coach, builder, or operational capture?
3. Did it match James's requested altitude, directness, and level of detail?
4. Did it make the right call about acting versus asking versus pausing?
5. Did it preserve critical constraints: confidentiality, source-of-truth routing, no invented facts, no unwanted external sends, and no unnecessary scope expansion?
6. Was the output actually useful—not merely polished or framework-heavy?

This must be **small, decision-relevant, and human-owned**. The goal is not an academic benchmark or an automated pass/fail machine.

### Minimal design

Create a versioned eval corpus with approximately **20–30 canonical cases**. Each case is a compact bundle:

```text
case_id
task category
input prompt / situation
required context files or facts
expected moves
failure modes to avoid
human scoring rubric
one or more approved reference outputs or outcome notes (when available)
```

Do not create a separate case for every historic interaction. Select cases that represent recurring, costly decisions.

Suggested initial case families:

| Family | Example | What it tests |
|---|---|---|
| Stakeholder prep | Dylan 1:1 with a scope or trust ambiguity | Context retrieval, theory-of-mind, managing-up altitude, say-able talk track |
| Executive writing | Decision memo or note to senior leadership | Brevity, clear ask, option pricing, James's voice |
| Reactive coaching | A status/comparison trigger or vent | Acknowledge without indulging rumination; redirect to agency without flattening emotion |
| Strategic thinking | Fork between two career or org-design moves | Org-needs-first framing, decision quality, useful pushback |
| Technical critique | Reflex eval or system-design proposal | Causal reasoning, evidence bar, identify a decisive control rather than metric sprawl |
| Context update | New stakeholder or reorg information | Correct file routing, provenance, propagation of changed facts, uncertainty markers |
| Session opening | `/start-session` with no stated task | Cheap orientation only; do not self-select expensive work |
| Scope containment | James says “that is too much” or redirects | Stop expansion immediately and serve the contained ask |
| Artifact delivery | A durable document is requested | Correct source-of-truth placement, no false claim of completion, verification |
| Tool portability | Same task in Codex rather than Claude Code | Use `AGENTS.md` and `prompts/`; do not assume Claude hooks or memory exist |

### Scoring rubric

Score each case on a 0–2 or 0–3 scale rather than trying to force fake precision.

| Dimension | Passing standard |
|---|---|
| Context and factual integrity | Uses the right source; carries uncertainty and does not invent missing facts. |
| Decision quality | Identifies the actual decision and gives a move that changes it. |
| Audience and voice | Calibrated to James and the stated recipient; neither corporate-safe nor needlessly combative. |
| Scope discipline | Does not create an unrequested doc, plan, tool run, or question sequence. |
| Coaching / altitude | Applies the relevant pattern only when it helps; does not turn every task into a career lecture. |
| Operational correctness | Uses the correct file, workflow, permissions, and verification bar. |
| Utility | James could use the output or act on it with minimal translation. |

The initial judge should be James, supported by Leo's self-critique and, where useful, a second model. A model score is a diagnostic; it must not become the truth criterion for an agent built to serve one specific person.

### Change-control workflow

Use the harness only for meaningful changes: new workflows, promoted instincts, substantial `AGENTS.md` edits, tool-portability work, or large integration changes. Do not impose it on every tiny artifact edit.

```text
Proposed behavioral change
        ↓
Name the expected improvement and likely regression
        ↓
Select 3–8 affected canonical cases
        ↓
Run baseline / changed behavior when feasible
        ↓
Human review of deltas
        ↓
Ship, revise, or reject change
        ↓
Record the result and update a case only when the new learning is durable
```

The evaluation set should deliberately include contradiction cases—for example, where `no-questions-by-default` would be wrong because a decision is externally consequential or destructive. That protects the system against turning valuable preferences into brittle universal laws.

### Success criteria

Within the first month of operation:

- At least 20 canonical cases represent the highest-value recurring Leo work.
- Every material behavioral change names the expected benefit and the cases it could regress.
- At least one seemingly sensible change is revised or rejected because the evals expose a downside.
- James can look at a short changelog and understand why Leo's behavior changed.

### Non-goals and guardrails

- Do not build an elaborate automated benchmark platform before there is a validated manual corpus.
- Do not use generic benchmark questions; they will not measure Leo's differentiated value.
- Do not optimize toward prose similarity with old outputs. Measure the underlying decision quality.
- Do not allow a model judge to replace James's judgment about usefulness, voice, or trust.

---

## 2. Build a context compiler and freshness system

### Problem

Leo has accumulated a powerful but large memory substrate: extensive work and self context, 170+ session logs, ~70 behavioral instincts, a large knowledge base, project artifacts, organization records, and tool-specific configuration.

The main risk is no longer “Leo does not know enough.” It is that Leo:

- retrieves an old fact and treats it as current;
- inherits a stale recommendation because it was repeated across handoffs;
- misses a superseding decision buried in a newer log;
- loads too much history and gives an over-weighted or slow answer;
- sees a detail without its source, confidence, or time horizon;
- makes conflicting documents appear equally authoritative.

The recent need to refresh `system/leo-overview.md` is an example of the benign version: a useful document became stale because it described an earlier architecture and old operating assumptions. The cost becomes much higher in live stakeholder, reorg, and project decisions.

### Target behavior

For any high-stakes context claim, Leo should be able to state:

> “This is the current operating view, sourced from X on date Y. It supersedes Z. The remaining uncertainty is Q.”

For a task, Leo should load a small **context packet** rather than indiscriminately reading a folder or carrying an ever-larger base prompt.

`AGENTS.md` should remain the router and contract, not become the repository's complete encyclopedia.

### Minimal design

Introduce compact, explicitly maintained operational briefs for the most active domains. Each brief should be one to three pages, not a reorganization of the underlying records.

Initial suggested briefs:

| Brief | Purpose | Canonical inputs |
|---|---|---|
| Current P13N Retrieval operating state | Current org shape, ownership, transitions, immediate open decisions | `team_members_scope.md`, reorg records, latest relevant session logs |
| Dylan working model | Relationship operating context, active asks, trust signals, known uncertainty | Dylan archive, stakeholders file, recent 1:1 records |
| Reflex evaluation state | Architecture, canonical dataset names, open decisions, owners, next evidence needed | Reflex critique, glossary, lockbox protocol, latest eval handoff |
| Career/charter state | Current Director-track thesis, keystones, advocates, real next moves | `self/goals.md`, career artifacts, current session evidence |
| Leo operating state | Current portable architecture, integrations, known gaps, active maintenance work | `AGENTS.md`, `CLAUDE.md`, workflows, system overview, relevant logs |

Each brief should contain:

```markdown
Status: current / needs-confirmation / historical snapshot
Last verified: YYYY-MM-DD
Authority: named file(s) and decision owner(s)

## Current facts
## Ratified decisions
## Open decisions and uncertainties
## Superseded beliefs (with links)
## Next evidence or event that will update this view
```

The existing detailed records remain the system of record. The brief is a retrieval and decision interface, not a replacement database.

### Freshness and provenance rules

1. **Every short brief points to its primary sources.** It never gains authority merely by being concise.
2. **Every material claim has a date or state marker.** “Current,” “proposed,” “TBD,” and “historical” are part of the fact.
3. **Supersession is explicit.** When an organization decision changes, the old claim is not silently left to be rediscovered by search.
4. **Uncertainty travels.** A `TBD`, “needs confirmation,” or provisional statement cannot become a settled fact when moved into a brief.
5. **Context loading follows the task.** Meeting prep needs a stakeholder brief plus current task material; technical critique needs the project brief plus sources; it does not need a global dump.
6. **Briefs are refreshed after triggering events, not on a blind schedule.** Reorgs, a substantive 1:1, goal changes, and project design decisions should trigger an update. Routine chat should not.

### A future compiler, after manual validation

Once several briefs are genuinely useful, build a small compiler/checker rather than a fully autonomous summarizer.

The first useful automation would:

- scan a brief for links to source documents;
- compare source modification dates with the brief's `Last verified` date;
- flag a brief as potentially stale when newer named sources exist;
- report unresolved `TBD` / `⟨confirm⟩` markers;
- surface direct contradictions in explicitly named current facts;
- produce a review queue, not silently overwrite human-maintained context.

Do **not** start by asking an LLM to rewrite all context automatically. That trades visible staleness for invisible hallucinated synthesis.

### Success criteria

- The five highest-stakes operating domains have compact, source-linked briefs.
- Important task openings load a relevant brief instead of multiple long historical files by default.
- Stale claims get caught as a routine review signal before they affect advice.
- When James asks “what changed?” Leo can provide a dated, sourced answer in under a minute.
- The amount of context loaded per task decreases without loss of decision quality.

### Non-goals and guardrails

- Do not flatten rich relationship or coaching history into a sterile database. The detailed archive remains necessary.
- Do not invent a new top-level source of truth; briefs are interfaces, not competing records.
- Do not automatically delete or rewrite historical records just because a newer state exists.
- Do not treat recency alone as authority; a recent speculation is not stronger than a ratified decision.

---

## 3. Create an external-expert intake workflow, starting with Ethan Evans

### Problem

Some external specialist experiences are genuinely better than Leo's current equivalent. The Ethan Evans Custom GPT is the immediate example: it appears to provide a sharper framework corpus and/or a stronger decision procedure than the current local NotebookLM consultation.

Leo should not pretend that every external specialist can be cloned with a few source files and an instruction prompt. Nor should useful consultations remain isolated in ChatGPT, unable to benefit from James's actual organizational context or become durable insight.

The objective is not to reverse-engineer a Custom GPT's hidden instructions or scrape its private knowledge. It is to make Leo excellent at turning legitimate, user-provided external advice into a contextualized operating move.

### Target behavior

James should be able to consult a specialist in ChatGPT, bring the result to Leo, and receive:

1. a compact extraction of the framework and recommendation;
2. a clear separation between the expert's claim and Leo's inference;
3. a pressure test against James's actual goals, stakeholder state, and constraints;
4. a concrete next move or artifact; and
5. durable filing only when the learning is broadly reusable.

The relationship should be:

```text
External specialist: framework depth / outside perspective
Leo: James-specific context / continuity / implementation / provenance
James: final judgment and source selection
```

### Minimal workflow: `import-consultation`

Create a portable workflow (and, where useful, a Claude/Codex-native skill) that takes a pasted transcript, summary, or uploaded artifact from a trusted external expert.

Required output format:

```markdown
## Source
- Expert/system:
- Date:
- Original question:
- Material supplied by James:

## What the expert is actually claiming
- Framework or principle:
- Reasoning chain:
- Recommended move:
- Assumptions / conditions:

## Leo's contextualization
- Evidence in James's current context that supports or weakens it:
- What the expert could not know about this situation:
- Robust move across plausible stakeholder states:

## Action
- Immediate next step:
- Suggested language / artifact (if warranted):
- What, if anything, should be filed durably:

## Provenance
- Link or source reference to the original consultation
- Explicit labels for direct expert claim versus Leo inference
```

The default should be **chat synthesis, not automatic filing**. File only an enduring framework, a changed decision, or stakeholder-relevant information—not every specialist conversation.

### Ethan Evans behavior-distillation campaign

The next step is not an API integration. A Custom GPT is not directly callable as an API sub-agent, and we should not attempt to extract hidden prompts or private knowledge.

Instead, evaluate its observable public behavior.

1. Create a set of 12–20 real Director-track scenarios from James's world: sponsor utility, scope ambiguity, promotion, managing up, resource allocation, organizational conflict, frontier-lab optionality, and executive communication.
2. Ask the Ethan GPT each scenario and preserve the answers James is legitimately able to access.
3. Run Leo's current Ethan NotebookLM workflow on the same prompts.
4. Compare the results on:
   - framework selection;
   - diagnostic questions;
   - quality of pushback;
   - specificity of the recommended move;
   - brevity and voice;
   - use of evidence versus generic career advice;
   - fit with James's actual context.
5. Identify whether the gap is primarily:
   - **source coverage** — missing Ethan material;
   - **retrieval** — the material exists but is not surfaced;
   - **decision procedure** — the source is present but Leo does not apply it in the same sequence;
   - **model / tool behavior** — ChatGPT's configured experience has a materially different interaction pattern.
6. Distill only the repeatable, legitimate behavior into Leo: framework-routing rules, diagnostic sequences, and output standards. Do not copy long outputs or claim access to hidden materials.

This is a useful first use case for Fix #1: the external Ethan GPT can act as one reference signal in a human-owned behavioral evaluation, while James remains the authority on which answer actually helps.

### Why this is better than trying to clone the GPT

An external specialist starts fresh. Leo can add value by connecting a framework to the actual organization, career strategy, prior stated preferences, and already-filed stakeholder evidence. A perfect clone would still be missing much of that context; a good intake and contextualization loop makes the two systems complementary.

It also keeps tool boundaries honest:

- ChatGPT Custom GPTs are used in ChatGPT; they are not treated as callable Codex APIs.
- External sources are credited rather than laundered into “Leo knowledge.”
- Sensitive internal context stays in Leo unless James explicitly chooses to share it with the outside specialist.
- A specialist's generic advice does not silently override a ratified plan or current stakeholder facts.

### Success criteria

- One consultation can be imported and contextualized in less than ten minutes.
- The Ethan comparison set identifies at least three concrete behavioral gaps—not vague impressions that it is “better.”
- At least one improved Leo workflow closes a measured gap on that set.
- External consultations produce clearer James-specific moves without creating a flood of permanent notes.

### Non-goals and guardrails

- Do not scrape, reverse-engineer, or prompt-inject a third-party Custom GPT.
- Do not upload Pinterest-sensitive materials to an external tool without explicit judgment about the data boundary.
- Do not call a distilled approximation “Ethan Evans” as if it is the original product; name it as a Leo workflow informed by Ethan's public frameworks.
- Do not make the external specialist a source of truth over James's real context and judgment.

---

## Recommended sequencing

### Phase 1 — Establish the quality bar

Start with the Leo evaluation corpus. This is a small, manual project, not a platform build.

- Select 20 canonical cases from real prior interactions.
- Write expected moves and failure modes.
- Add a lightweight scoring sheet.
- Use it on the next material workflow or instinct change.

**Exit criterion:** the corpus catches at least one non-obvious regression or produces a change that James agrees is materially better.

### Phase 2 — Stabilize the most expensive context

Create the first two operational briefs: P13N Retrieval operating state and Reflex evaluation state. They are current, active, and particularly exposed to stale-context failures.

**Exit criterion:** a relevant task can begin from the brief plus primary artifacts, and the brief makes uncertainty/supersession easier to see than the raw corpus does.

### Phase 3 — Pilot the Ethan intake

Create the import format, collect the first behavior-distillation set, and compare it with Leo's current NotebookLM-backed answer.

**Exit criterion:** identify the top three gaps and improve one of them in a portable Leo workflow.

### Phase 4 — Automate only proven friction

After the manual processes have demonstrated value:

- add context freshness checks;
- formalize eval-run records;
- make the external-expert intake a reusable skill;
- consider a small dashboard only if it saves real review time.

No autonomous context rewriting, broad multi-agent overhaul, or API build should precede these validated workflows.

---

## Decision rule

When choosing future Leo work, ask:

> Does this improve Leo's ability to produce trustworthy, context-aware decisions for James—or does it merely add another capability to an already complex system?

The three proposals above pass that test because they improve the substrate beneath every future capability: measurement, truth maintenance, and learning from stronger outside systems.
