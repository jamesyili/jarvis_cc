# Feedback Curator & Skeptic — Deep Dive

Detailed walkthrough of the two *quality* agents in Reflex's Detect stage: what they
actually do, the data contracts they enforce, and how they interlock into a closed
learning loop. Grounded in the current prompts and schemas as of 2026-08-28.

Sources read for this doc:
- `detect/agents/skeptic.md`
- `detect/agents/feedback_curator.md`
- `detect/CLAUDE.md` (Detect stage overview)
- `detect/infra/schemas/skeptic_verdict.py`
- `detect/infra/schemas/expert_judgment.py`
- `detect/state/dead_ends.yaml`
- `detect/capabilities/analytical_checks/registry.yaml`

---

## The big picture: where these two sit

Detect is a Kanban pipeline on Asana: `Rough Ideas → Hypotheses → Opportunities → Build → Archive`.
Two agents *author* content — the **PM Agent** generates hypotheses, the **DS Agent** matures
them into opportunity cards. The **Skeptic** and the **Feedback Curator** are the two *quality*
agents. They don't author cards; they protect the system's judgment.

The clean way to hold them in your head:

- **Skeptic = the gate.** Per-card, synchronous, blocks bad cards from reaching a human. Its
  currency is *tags* and a *verdict log*.
- **Feedback Curator = the memory.** Post-hoc, asynchronous, harvests what humans said into
  durable institutional knowledge. Its currency is *structured state files* and an
  *expert-judgment log*.

They form a loop: **the Skeptic reads the patterns the Curator writes.** The Skeptic catches
"the system already knows this is wrong"; the Curator is what put that knowledge into the files
in the first place.

Two structural facts worth stating up front:

1. **These are author/judge separation made concrete.** The DS Agent writes cards; the Skeptic
   judges them. The load-bearing rule (`skeptic.md:268`) is that the Skeptic *never edits a card
   body*. The moment the judge starts fixing the author's work, they stop being independent and
   the gate becomes theater.
2. **Both agents are prompt-defined, not code-defined.** There is no `skeptic.py` running an LLM
   loop — the `.md` file *is* the agent. Claude Code executes the markdown. The only Python is
   validation (the Pydantic schemas + the `log_record.py` writer), which matches the repo-wide
   decision: "Claude Code IS the LLM; the Python layer is validation-only."

---

## Part 1 — The Skeptic Agent

### Its job in one sentence

Sit between the DS Agent's finished opportunity card and the expensive human expert, and
**red-team the card against everything the system already knows** (deprecated CGs, holdout
confusion, unverified pin claims, wrong table names, layer confusion, tried-and-failed
approaches) so humans only spend review cycles on genuinely novel work.

It is adversarial against **cards**, not against the DS Agent (`skeptic.md:9`).

### How it's triggered and what it manipulates

The mental model is subtle and the prompt hammers it (`skeptic.md:12–18, 186`): **the Skeptic
never moves cards between sections.** A card lives in the Opportunities section from the moment
DS promotes it. The Skeptic's entire output is expressed through **tags**:

```
DS promotes card → tagged  awaiting-skeptic
                              │
                    ┌─────────┴─────────┐
                Skeptic runs on every awaiting-skeptic card
                              │
        ┌─────────────────────┼─────────────────────┐
      PASS                  FAIL                NEEDS-HUMAN
   ready-to-build       skeptic-failed       skeptic-needs-human
   (Router dispatches)  (DS re-enriches)     (human adjudicates)
```

`ready-to-build` is the single signal the **Router** keys on. So the Skeptic is literally the
valve controlling what flows into the Build stage. A card it doesn't bless is invisible to the
Router. It also re-runs when a card is re-enriched after a prior FAIL (DS re-tags it
`awaiting-skeptic`).

### The six checks (its actual work)

Every card runs through all six (`skeptic.md:46–181`). The first five are hygiene; the sixth is
the whole point.

1. **Pattern Check** — does the card violate a named analytical check from
   `capabilities/analytical_checks/registry.yaml`? e.g. claims pin content *without VLM
   verification* (the prompt calls VLM "the single most important pattern").
2. **Context Check** — cross-reference every claim against known state. This is where the
   concrete table/column landmines live, e.g.:
   ```
   datestr        → should be date or dt
   num_closeups   → doesn't exist; use num_pin_clicks
   irrelevance_reason → doesn't exist; use individual boolean columns
   country        → lowercase in bi.core_daily_search_feedview_stats,
                    UPPERCASE in bi.core_daily_feedview_pin_stats
   ```
   Every one of those is a live entry in `dead_ends.yaml` (`wrong_column_names_common`,
   `num_closeups_column`, `irrelevance_reason_column`, `search_feedview_country_case` vs
   `feedview_pin_stats_country_case`).
3. **Evidence Check** — but *first classify the card type*, because evidence requirements differ:

   | Card Type | VLM missing | Charts missing |
   |-----------|-------------|----------------|
   | Content quality | **HIGH** | **HIGH** |
   | Architecture/measurement | MED | MED |
   | Experiment monitoring | MED | MED |
   | Synthesis/meta | N/A | MED |

   This table is the antidote to "flag inflation" — flagging "missing VLM" on a card that argues
   from codebase config is called out explicitly as a failure mode (`skeptic.md:404`). The card
   type is set by the card's *primary argument*, not its title.
4. **Internal Consistency** — e.g. "low-volume holdout CG" can't *also* claim large aggregate
   engagement (HIGH); composite score must be on `/5` not `/10` (a real past error — see the
   `composite_score_10_scale` dead end, where a 6.4/10 card was parsed as 6.4/5 and wrongly
   ranked #1 for multiple cycles).
5. **Novelty Check** — search the archive for prior art. Surfaced as a *context block, not a
   flag* — the human decides redundancy.
6. **Strategic Viability Check** — **the highest-value check.** The prompt is emphatic
   (`skeptic.md:143, 405, 411`): checks 1–5 ask "is this card well-formed?"; check 6 asks
   *"does the system's accumulated knowledge predict this will actually work?"* Sub-checks:
   - **6a. Dead-end collision** — structural (not just table/column) similarity to a Known Dead
     End. e.g. a static CG-budget reallocation card collides with the
     `shopping_cg_budget_reallocation` dead end (HR-7220 shipped; the RL model handles dynamic
     suppression).
   - **6b. Architectural-principle violation** — e.g. proposing ranking-layer per-state
     differentiation when the `ranking_vs_utility_architecture` check says per-state belongs in
     utility (attributed to Dylan Wang, Cycle 49/57).
   - **6c. Cycle-learnings contradiction.**
   - **6d. Curator-correction recurrence** — if the card repeats a claim the Curator already
     corrected (read from `quality/audit-logs/`), that's an automatic HIGH.
   - **6e. Feasibility reality check** — does the card assume team capacity/ownership that
     doesn't exist, or recommend a static change a learned policy already subsumes?

   The killer line: *"If your review has zero Check 6 findings, ask whether you read the Cycle
   Learnings."*

**Why Check 6 is where a prompt-defined agent earns its keep over a linter:** a regex could catch
`num_closeups`. Only accumulated judgment catches *"this static CG-budget reallocation is
HR-7220, which shipped — the RL model already handles dynamic suppression, so this was tried and
won't add anything."* That's institutional memory applied as veto.

The FAIL worked example (`skeptic.md:335–365`) shows the discipline: every HIGH flag ends with a
concrete **"To resolve:"** — because the Skeptic flags but the DS Agent fixes. A flag without a
resolution path would just bounce forever.

### The verdict log — why it's the interesting part

After *every* verdict — including PASS — the Skeptic appends a `SkepticVerdict` JSON line to
`state/verdict_log.jsonl`. This is the substrate for measuring the Skeptic's *own* precision and
recall. The schema (`skeptic_verdict.py`):

```python
SkepticCheckName = Literal[
    "pattern_check", "context_check", "evidence_check",
    "internal_consistency", "novelty",
]
SkepticCheckOutcome = Literal["PASS", "FAIL", "N/A"]
VerdictKind = Literal["PASS", "FAIL", "NEEDS_HUMAN"]

class SkepticCheck(BaseModel):
    name: SkepticCheckName
    outcome: SkepticCheckOutcome
    rationale: str = Field(..., min_length=1)
    patterns_cited: list[str] = Field(default_factory=list)

class SkepticVerdict(BaseModel):
    timestamp: datetime
    cycle_id: int | None = None
    card_gid: str
    card_title: str
    verdict: VerdictKind
    checks: list[SkepticCheck]
    fail_reasons: list[str] = Field(default_factory=list)
    revision_round: int = Field(default=0, ge=0, le=2)   # hard-caps the loop
    confidence: float = Field(..., ge=0.0, le=1.0)
    skeptic_version: str
    human_reviewed: bool | None = None                   # backfilled later
    human_agreed: bool | None = None                     # backfilled later
```

Three design decisions worth calling out:

- **`human_agreed` starts `null` and is backfilled** when a human reviews the card. That backfill
  is *the entire point* — it's how you later compute "of everything the Skeptic FAILed, how often
  did the human agree it deserved to fail?" (precision) and "how many good cards did it wrongly
  block?" (the false-negative story requires logging PASS verdicts too — hence "Do not skip
  logging on PASS," `skeptic.md:250`).
- **The validated writer refuses malformed records.** `skeptic.md:246` — a FAIL with no
  `fail_reasons`, a PASS containing a failed check, or duplicate check names all get rejected.
  That's not pedantry: any of those would silently corrupt the eval harness's ability to score the
  agent. The prompt documents *why* you must use `log_record.py` and not `echo` — a pretty-printed
  heredoc breaks every line-based JSONL reader, and `echo` makes the LLM the serializer with
  nothing checking the record (`skeptic.md:235–238`). Maps to the repo decision "Route agent
  state writes through validating writers."
- **`revision_round: int = Field(..., ge=0, le=2)`** — the 2-round cap is enforced *at the schema
  level*, not just in prose. After two FAILs, the card escalates to a human regardless
  (`skeptic.md:204`). This caps compute and prevents an infinite DS↔Skeptic loop.

### Its scope boundaries (what it deliberately won't do)

`skeptic.md:264–275` — it won't rewrite cards, won't move them, won't retire them, won't generate
new patterns (it *suggests* pattern gaps for the Curator via a `consider adding pattern` note),
and won't touch any structured state file. **Read-only against the knowledge base, write-only
against tags + its own verdict log.** That asymmetry is the whole safety model.

### Failure modes the prompt explicitly warns against

- **Over-blocking** — it's a gate, not a wall. If ambiguous → NEEDS-HUMAN, not FAIL.
- **Under-catching** — miss a pattern violation and expert trust erodes.
- **Flag inflation** — don't add LOW flags to feel thorough; a LOW flag costs DS revision time.
- **Checklist-only reviewing** — "the Skeptic that only checks 'VLM? Charts? Composite scale?' is
  a formatting validator, not an adversarial gate." Highest-value catches are strategic.
- **Style policing** — card claims and evidence only, never DS writing style.

---

## Part 2 — The Feedback Curator Agent

### Its job in one sentence

Be the **institutional-memory custodian** — take high-signal human feedback (Asana comments,
Skeptic overrides, off-board experiment learnings) and convert it into durable, structured
knowledge so an expert's insight is captured *once* and reused *forever*, instead of evaporating
into Asana prose.

### Two distinct modes

This is really two agents in one file (`feedback_curator.md:7–10`):

**Mode 1 — Board-Feedback (automatic).** Triggered by a new Asana comment, a human Skeptic
override, a scheduled audit, or direct invocation. It processes the *full human signal corpus* on
the board.

**Mode 2 — Intake Agent (manual, interactive, high-bar).** A human shows up with a Helium link, a
launch review, a spec, or a screenshot and says something like *"ingest this experiment into
Reflex"* (`feedback_curator.md:32–39` — deliberately fuzzy trigger matching, no magic string).
The Curator then *interviews* them.

### The memory layers it owns

```
capabilities/analytical_checks/ + registry.yaml   ← forward-looking detection lenses
state/dead_ends.yaml                                ← approaches/tables that fail
state/rotation.yaml
state/learning_records.jsonl                        ← Intake: one reusable claim each
state/reinforcement_events.jsonl                    ← Intake: "same claim, more evidence"
state/intake_runs.jsonl                             ← Intake: session-level audit
state/expert_judgments.jsonl                        ← every human comment, structured
quality_patterns.md                                 ← READ-ONLY archive
```

### Board-Feedback mode: the discipline of "read everything first"

The most important instruction is **Phase 0: Deep Comprehension** (`feedback_curator.md:95–109`),
and it runs on *every* trigger, not just scheduled audits. The rule: **before acting on any single
comment, read ALL human comments on ALL cards across ALL sections, plus all human-created cards,
plus all structured state.**

Why so heavy? The prompt's rationale (`feedback_curator.md:99`): *re-reading previously-processed
comments in the context of newer ones surfaces patterns invisible on first pass.* A single comment
processed in isolation loses the theme — "three different reviewers all flagged the same class of
issue" is only visible if you read all three together. The synthesis it writes is called *"the
Curator's most important output. Individual pattern proposals flow from it — not the other way
around"* (`feedback_curator.md:109`).

Then it classifies each correction (Phase 2) into a category that maps to a specific file:

| Category | Maps to |
|----------|---------|
| `holdout-architecture`, `signal-decay`, `architecture`, `scope-miscalibration`, `ranking-vs-utility` | `analytical_checks/` |
| `deprecated-system`, `data-accuracy` | `dead_ends.yaml` |
| `evidence-verification` | `quality_patterns.md` (Presentation) |

And decides the **relationship** to existing patterns (Phase 3, `feedback_curator.md:136–142`):
**Strengthen / Contradict / Narrow / Orthogonal.**

**The single most emphasized rule in the whole file:** *"Do not merge contradictions silently.
Merging contradictions silently is the critical failure mode"* (`feedback_curator.md:302`). When
new feedback contradicts an existing pattern, the Curator must emit a **Conflict Report** with
three options — (a) Merge, (b) Version, (c) Replace — recommend one, and *route it back to the
original reviewer* without acting. This is deliberate: silently reconciling two experts'
contradictory guidance would let the system quietly overwrite one human's judgment with another's.

Same posture on retirement: *"never silently retire a pattern... Silent retirement is a critical
failure mode"* (`feedback_curator.md:338`). The Curator can *strengthen* autonomously (low blast
radius) but *retiring or broadening* always needs a human. (This is exactly the lesson in the
work-leo CLAUDE.md — "removals need a second look; a capability with no entry point is worse than
a deleted one.")

Auto-apply vs proposal split (Phase 5):
- **Auto-apply** (decay fixes, path corrections, reaffirmations, duplicate removal): edit the
  structured file directly, update affected Asana cards' `html_notes`, post a "Feedback Curator —
  Auto-applied" comment, log before/after in the audit log.
- **Proposal-only** (conflict reports, ambiguous feedback, pattern retirements): write the
  proposal to `quality/proposed/{name}.md`, post an "Awaiting {reviewer}" comment, and do **not**
  touch `quality_patterns.md` or card content until a human confirms.

### Phase 5b: the structural capture layer (the real innovation)

This is the Curator's reason for existing. For **every human comment processed**, it appends an
`ExpertJudgment` record to `state/expert_judgments.jsonl`. The prompt's justification
(`feedback_curator.md:213–214`): *"This is the structural capture layer for I-0 (expert labeling
must compound). Without this, expert-minutes evaporate into Asana prose."*

The schema (`expert_judgment.py`):

```python
JudgmentType = Literal[
    "agree", "disagree", "reframe", "extend",
    "retire", "new_info", "question", "approve",
]
JudgmentConfidence = Literal["low", "medium", "high"]
JudgmentSource = Literal[
    "asana_comment",
    "asana_action",    # a card moved between sections — approval with NO words attached
    "slack_dm", "one_on_one", "meeting", "direct_input", "canary_override",
]

class ExpertJudgment(BaseModel):
    timestamp: datetime
    expert: str                    # canonical ID: james_li, dylan_wang, andrew_y...
    expert_role: str | None
    card_gid: str
    card_title: str                # denormalized at time of capture
    cycle_id: int | None
    judgment_type: JudgmentType
    claim_targeted: str | None     # the specific claim, or None = whole card
    rationale_verbatim: str        # the expert's EXACT words
    rationale_summary: str         # Curator's <=2-sentence compression
    confidence: JudgmentConfidence | None
    cross_card_propagation: list[str]   # OTHER cards this judgment also fixes
    source: JudgmentSource
    source_ref: str                # URL/identifier of the original input
    curator_version: str
```

Two fields carry the design intent:

- **`rationale_verbatim`** — the expert's own words, preserved exactly. The prompt
  (`feedback_curator.md:178`) insists: *"Preserve the reviewer's language. Don't paraphrase away
  the specific example."* And the schema encodes the *one* exception: it may be empty **only**
  when `source == "asana_action"` — i.e. the expert moved a card between sections, an approval
  carried by an action with no words attached (see the comment right in the `JudgmentSource`
  enum). Every other source must quote.
- **`cross_card_propagation`** — *"this is what enables one expert comment to improve multiple
  cards"* (`feedback_curator.md:260`). When Dylan says "per-state differentiation belongs in
  utility, not ranking," that judgment applies to *every* per-state card on the board, not just
  the one he commented on. The constraint: it must not list the card the judgment is already on
  (`feedback_curator.md:249`).

The canonical worked example (`feedback_curator.md:218–235`):

```json
{
  "timestamp": "2026-05-03T14:00:00Z",
  "expert": "dylan_wang",
  "expert_role": "em_hf_ranking_retrieval",
  "card_gid": "1214106032167096",
  "card_title": "Per-state ranking gap",
  "cycle_id": 57,
  "judgment_type": "reframe",
  "claim_targeted": "Per-state differentiation belongs in ranking model",
  "rationale_verbatim": "Ranking should produce unbiased predictions. Per-state belongs in utility, not ranking. RL replaces static per-state weights.",
  "rationale_summary": "Per-state differentiation belongs in utility layer, not ranking. RL utility is the architecturally correct solver.",
  "confidence": "high",
  "cross_card_propagation": ["1214106032167100", "1214106032167105"],
  "source": "asana_comment",
  "source_ref": "https://app.asana.com/0/1214052141167470/1214106032167096",
  "curator_version": "v1.0"
}
```

There's also a **self-assessment loop** (`feedback_curator.md:293–296`): at the start of each run
the Curator reads its own judgment log and asks — *which experts get overridden later? Is
`disagree` the dominant judgment type (a sign cards keep missing known context)? Are cross-card
propagations actually being acted on?*

Alongside every run it also logs a `CycleLogEntry` to `state/cycle_log.jsonl` (agent="curator")
with phase tracking. **Phase tracking is mandatory and strict** (`feedback_curator.md:279–291`):
every `phases_attempted` must resolve into `phases_completed` or `phases_failed`; the writer
rejects a dangling phase or one listed in both. A required phase you didn't run is a *failure*
(list it with reason `"skipped"`), not an omission — so it counts against the run instead of
shrinking the denominator.

### Intake Agent mode: the interview

Completely different shape — **mandatory, interactive, one question at a time**
(`feedback_curator.md:342`). Required posture (`feedback_curator.md:339–346`):

- *"Start with the artifacts. No primary artifact, no durable learning."*
- Ask **one question at a time.**
- *"Do not default to a lightweight summary. Push until the reusable learning and its limits are
  clear."*
- Self-contained: don't create Asana follow-up homework by default.

It retrieves existing learnings first (`external_prior_retrieval.py`) to decide whether the claim
is new, a reinforcement of an unchanged claim, a supersede, or a contradiction requiring human
resolution. It covers mandatory interview categories (what happened / evidence / what's reusable /
what Detect lacks / where it should go) plus explicit **counterfactual probing**
(`feedback_curator.md:383–387`): *"What would make this lesson false? Where should this NOT
generalize? Is this about the mechanism, the segment, or the review logic?"*

Candidate learnings are resolved **serially**; a learning record is always **one reusable claim**.
Reinforcement of an unchanged claim → a reinforcement event, not a duplicate record. A meaningful
change in confidence/scope/recommendation → a new record that supersedes the old.

Routing at the end is opinionated (`feedback_curator.md:412–445`). Defaults:

```
Future opportunity detection      → analytical_check   (preferred default)
Retrospective interpretation      → playbook_rule
Repeated false-positive path      → dead_end
Broad stance change, many tasks   → agent_prompt_rule
```

with a strong bias toward forward-looking `analytical_check` — *"Do not choose a playbook_rule
merely because the source artifact is a launch review."* The framing question it asks itself: *"is
this mainly about finding future opportunities, or evaluating past ones?"*

And crucially, **it's allowed to conclude nothing was learned** (`feedback_curator.md:455–463`):
close the run as `no_durable_learning`, write no record. That's a real feature — it prevents the
memory from bloating with low-signal "learnings" just because someone ran an intake session.

### The blast-radius safety model

(`feedback_curator.md:424–447`) — this is the Curator's core safety discipline:

- **Auto-apply (low blast radius):** create learning records, create reinforcement events, update
  intake runs, *strengthen* an existing analytical check, *strengthen* an existing dead end.
- **Same-session human approval (high blast radius):** create a *new* analytical check, create a
  *new* dead end, change playbook behavior, change agent-prompt behavior, resolve contradictions
  between active learnings.

*"No high-blast-radius proposal may remain unresolved when the intake run closes."* Every one must
end as approved-and-applied, approved-and-deferred, or explicitly-not-approved.

Persistence is separate from the interview (`feedback_curator.md:477–487`): only after the
learning is resolved does it ask *"want me to open a worktree/branch and PR these changes?"* —
never blending repo mutation into the interview. (Matches the git-workflow rule: Asana data ops
need no PR, but code/state changes go through a branch.)

---

## Part 3 — How they interlock (the loop that matters)

```
   DS Agent authors card
          │
          ▼
   ┌─────────────┐   reads patterns    ┌──────────────────┐
   │   SKEPTIC   │ ◄────────────────── │  analytical_checks│
   │  (the gate) │                     │  dead_ends.yaml   │
   └─────────────┘                     │  quality_patterns │
      │      │                         └──────────────────┘
      │      │ "consider adding                  ▲
      │      │  pattern" note                    │ writes
      │      ▼                                    │
      │  ┌──────────────────┐  human comments  ┌──────────────┐
      │  │  human expert    │ ───────────────► │   CURATOR    │
      │  │  (reviews PASS)  │                  │ (the memory) │
      │  └──────────────────┘                  └──────────────┘
      │      │ backfills human_agreed              │
      ▼      ▼                                     ▼
   verdict_log.jsonl                     expert_judgments.jsonl
   (Skeptic's own eval)                  (compounding expert labels)
```

- The Skeptic **consumes** the knowledge; the Curator **produces** it. Skeptic explicitly does
  *not* write to the state files (`skeptic.md:260`); Curator is the only writer.
- When the Skeptic hits a violation no existing pattern covers, it emits a `consider adding
  pattern` note — and the Curator picks that up (`skeptic.md:261`).
- When a human *overrides* the Skeptic (approves a card it FAILed), that override is signal the
  Curator reads (`skeptic.md:262`) — and the Skeptic logs it so its own precision can be
  recomputed.
- The Skeptic even *reads the Curator's audit logs* as a check input (`skeptic.md:32`, Check 6d):
  if a card repeats a claim the Curator already corrected, that's an automatic HIGH flag. So the
  Curator's corrections directly sharpen the Skeptic's future catches.

---

## Part 4 — End-to-end trace: one expert comment becoming a permanent gate

The best way to see the loop is to follow a single insight from a human's mouth to a future card's
FAIL. The prompts share a hero example, so this trace is real, not hypothetical.

### Hero trace A: "per-state belongs in utility, not ranking" (Dylan Wang, Cycle 49/57)

**Step 1 — Human comment.** On a card titled "Per-state ranking gap," Dylan Wang comments:
*"Ranking should produce unbiased predictions. Per-state belongs in utility, not ranking. RL
replaces static per-state weights."*

**Step 2 — Curator captures it structurally (Phase 5b).** The Curator writes the `ExpertJudgment`
shown above to `expert_judgments.jsonl`:
- `judgment_type: "reframe"` (per the mapping: "not X, actually Y" → reframe)
- `rationale_verbatim` preserves Dylan's exact words
- `cross_card_propagation: ["1214106032167100", "1214106032167105"]` — this reframe applies to
  *every other* per-state card on the board, not just the one Dylan commented on.

**Step 3 — Curator promotes it to a durable pattern (Phase 4).** Because this is about how Detect
should *discover future opportunities* (which layer to target), routing defaults to an
`analytical_check`, not a playbook rule. It becomes the check now visible in the registry:
```yaml
- id: ranking_vs_utility_architecture
  name: Ranking-vs-utility architecture principle
  verdict: mandatory
  mandatory_when: "always — specify which layer the proposed change targets"
  applies_to: [Homefeed, Search, Related Pins]
  discovered_cycle: 49
```
Note `verdict: mandatory` — this pattern must be applied to every applicable card, forever.

**Step 4 — Skeptic enforces it as a gate (Check 6b).** Cycles later, a *new* card proposes
ranking-layer per-state differentiation. The Skeptic's Check 6b fires:
> Proposing ranking-layer per-state differentiation when the "Ranking-vs-utility architecture
> principle" says per-state belongs in utility (Dylan Wang, Cycle 49/57) → **HIGH** flag citing
> the specific principle and cycle where it was learned.

**Step 5 — The verdict logs, closing the measurement loop.** The FAIL is written to
`verdict_log.jsonl` with `verdict: "FAIL"`, a `context_check`/`internal_consistency` outcome, and
a `fail_reason` citing the check. If a human later reviews and agrees, `human_agreed: true` gets
backfilled — feeding the Skeptic's own precision score.

**Net effect:** Dylan spent ~30 seconds on one comment. The system now (a) auto-improves every
per-state card via cross-card propagation, (b) permanently refuses any future card that re-targets
the wrong layer, and (c) can measure whether that refusal was correct. The expert-minute
compounded.

### Hero trace B: "how did you calculate that?" (wangchao, 2026-07-14) — visible in the YAML

This one has the full provenance baked into `dead_ends.yaml`, so you can see the capture with your
own eyes:

**Step 1 — Human comment.** On task `1216476265300236`, wangchao asks: *"how did you come up with
the estimation of 0.01-0.03% search SSv2 increase?"* The PM Agent admits it was a guess with no
constituent numbers.

**Step 2 — Curator captures it as a dead end** (this is a *repeated-false-positive path* →
`dead_end` per the routing defaults), and — critically — records *who confirmed it and when*, so
the Skeptic can cite a real expert, not a faceless rule:
```yaml
- id: de_topline_guess_without_constituent_numbers
  label: "Topline impact guess without constituent numbers"
  category: evidence_quality
  what_failed: "Including topline impact estimates (e.g., '+0.01-0.03% Search SSv2') in
    hypothesis cards without having the constituent numbers to calculate it..."
  why_it_fails: "Aspirational precision. The estimate reads as validated fact... when
    challenged ('how did you calculate that?'), the agent has to admit it was a guess."
  correct_alternative: "Use 'topline impact TBD by DS Agent'... provide the formula with
    placeholders... Do NOT estimate without the constituent numbers."
  discovered: "2026-07-14 (Cycle 68, task 1216476265300236)"
  discovered_by: expert_feedback
  confirmed_by:
    - expert: wangchao
      date: "2026-07-14"
      context: "Asked 'how did you come up with the estimation...' — PM Agent admitted it was
        a guess without grounding."
```

**Step 3 — Skeptic enforces it.** A future card that states a topline SSv2 lift with no traced SQL
/ constituent numbers now trips Check 2 (untraced evidence, MED) and/or Check 6a (dead-end
collision, HIGH), with the flag citing this exact dead-end id and wangchao's confirmation.

Other dead ends in the same file show the identical lifecycle — human/expert catch → captured with
provenance → enforced:
- `feature_processor_tab_rl_deprecated` — confirmed by Rahul Goutam (EM Blending/HF): "commented-
  out code in this file does not represent a live opportunity."
- `rl_config_effort_xs` — Rahul Goutam again: RL config changes are S-M effort, not XS, because
  they require retraining + offline eval + online experiment.
- `shopping_cg_budget_reallocation` — the structural dead end the Skeptic's own 6a worked example
  cites (HR-7220 shipped; RL handles dynamic suppression).

---

## Part 5 — Why this design (the eval angle)

For the eval work specifically, the thing to internalize is that **both agents are built to be
scored, and the scoring substrate is a first-class output, not an afterthought.**

- **The Skeptic is measurable because it logs every verdict, including PASS.** With
  `human_agreed` backfill you get precision (of FAILs, how many did humans uphold?) and, because
  PASS verdicts are logged too, false-negative rate (how many blessed cards did humans later
  reject?). The validated writer guarantees the log is scoreable — no FAIL-without-reasons, no
  PASS-with-a-failed-check, no duplicate check names.
- **The Curator is measurable because expert labels compound into a typed store.** The
  `expert_judgments.jsonl` log is exactly the labeled dataset you'd want for evaluating whether
  the system is learning from experts: judgment-type distribution (too much `disagree` = cards
  keep missing known context), per-expert override rates, and whether `cross_card_propagation`
  entries actually got acted on.
- **The two logs are complementary.** `verdict_log.jsonl` measures the *gate's* quality;
  `expert_judgments.jsonl` measures the *memory's* fidelity. Together they let you ask the real
  question: *is expert judgment entering the system once and being reused correctly forever?* —
  which is the whole self-healing thesis of Reflex made auditable.

That's the self-healing story from the vision doc made concrete: expert judgment enters once
(Curator captures it structurally), becomes a reusable pattern (analytical check or dead end), and
the gate (Skeptic) enforces it forever after — while both agents keep logs that let you measure
whether they're actually getting better.
