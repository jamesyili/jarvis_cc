# EvalResult v2 — straw schema + significance-aware dominance gate

**James Li · 2026-08-12 · straw proposal for Janvi's review thread (target: `evolve/infra/schemas/eval_result.py`)**
**Grounded in TDD §3.2/§3.3.5 as written 8/4 (source: `sources/janvi_evolve_tdd_2026-08-04.pdf`).**

The TDD's contract design is right: rubric lives in the values, EvalResult is the sole coupling point, contract_version asserted at startup. v2 adds the fields that make scores *trustworthy over time* — uncertainty, judge provenance, and fixture provenance — plus one default flip. Everything is additive except the flip; minor version bump except where noted.

## 1. MetricScore changes

```python
class MetricScore(BaseModel):
    name: str
    value: float                          # aggregate over trials (mean unless noted)
    trial_values: list[float] | None = None   # NEW — per-trial raw scores, len == n_trials
    scale_min: float = 0.0
    scale_max: float = 1.0
    direction: Direction = "maximize"
    weight: float = 0.0
    is_pareto_axis: bool = False          # CHANGED — was True; axes are now opt-in
    rationale: str | None = None
```

**Why `trial_values`:** K trials produce a distribution; passing only the scalar mean forces the Pareto gate to compare noisy point estimates — with small K it selects on noise. Trial-level scores also let Evolve compute Pass@K / Pass^K itself instead of each adapter pre-aggregating differently.

**Why the default flip (breaking — major bump):** with `is_pareto_axis=True` by default, any diagnostic metric a stage adds silently becomes a gate axis. At 4+ axes, "no worse everywhere" approaches unsatisfiable and runs burn the invocation budget producing nothing. Axes should be a deliberate declaration in `targets/<t>.yaml`, not a side effect of logging a number. (Pairs with epsilon-dominance or tiered gates as a later refinement — not needed for v2.)

## 2. EvalResult changes

```python
class EvalResult(BaseModel):
    contract_version: str                 # existing — bump to 2.0
    scores: dict[str, MetricScore]        # existing, unchanged shape
    feedback: str                         # existing — the reflective gradient
    n_trials: int                         # existing per TDD §3.3.5

    # NEW — judge provenance
    judge_version: str                    # bumps on ANY judge prompt/model/rubric change
    judge_model: str | None = None        # convenience; version is the contract

    # NEW — world provenance
    fixture_snapshot_id: str              # which frozen world produced this result
    fixture_created_at: datetime          # feeds a staleness gate (refuse/warn past max age)

    # NEW — case provenance
    case_id: str
    case_source: Literal["rotation", "calibration", "lockbox", "synthetic"]
```

**Why `judge_version`:** the judge is itself being GEPA-optimized (Chao Stage 1) while Evolve uses it as fitness. Unversioned, a score delta across generations is unattributable — improved playbook or drifted judge? Rules the field enables (enforced in the runner, not the schema): search and landing re-run pin the same version; cross-generation fitness comparisons only within a version; judge upgrade ⇒ re-baseline.

**Why `fixture_snapshot_id` + age:** an edit that dominates on stale fixtures can regress live. Snapshot ID makes "same world" checkable; created_at makes staleness a gate instead of a hope.

**Why `case_source`:** the contamination policy becomes enforceable — the runner refuses `lockbox` cases in any GEPA loop, and the Feedback Curator filters `calibration`/`lockbox` out of pattern extraction. One enum, three protections.

## 3. The significance-aware dominance gate

Replaces raw mean comparison in Pareto select (TDD §3.3.6.5). Candidate survives iff **not significantly worse on any declared axis, and significantly better on at least one** — paired bootstrap over shared cases:

```python
def dominates(parent: list[EvalResult], candidate: list[EvalResult],
              axes: list[str], alpha: float = 0.05, B: int = 10_000) -> GateVerdict:
    """Paired bootstrap over cases (pairing removes case-difficulty variance).
    For each axis: per-case delta = mean(candidate trials) - mean(parent trials),
    resample cases with replacement B times -> CI on the mean delta.
      - any axis with CI entirely < 0  -> reject (significantly worse)
      - no axis with CI entirely > 0   -> reject (no significant win; don't land noise)
      - else                           -> accept
    Verdict carries per-axis deltas + CIs so the proposal record shows *why*.
    """
```

~a day of work including tests; pure function of v2 fields (needs `trial_values` — this is why §1 matters). Sits in `evolve/infra/gates/` and is also what makes the "Held-out regression catch" success criterion (TDD §5) statistically meaningful rather than anecdotal.

## 4. Migration

v1 adapters keep working behind a shim (`trial_values=None` ⇒ gate falls back to means with a loud `UNPOWERED_COMPARISON` warning in the proposal record). The only true break is the `is_pareto_axis` default — a one-line explicit `true` in each existing target YAML, grep-able, done in minutes.

---

*Relation to the other two artifacts: `judge_version` + `case_source` are the schema half of the lockbox protocol (`lockbox_protocol_2026-08-12.md`); the seam message (`seam_message_drafts_2026-08-12.md`) references this doc as the "concrete proposals for the contract seam."*
