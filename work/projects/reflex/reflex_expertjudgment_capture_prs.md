# Reflex — ExpertJudgment Capture + Observability PRs (work-leo transfer pack)

**Owner:** James Li
**Context transfer for:** work-leo on work mac
**Created:** 2026-04-19 (Sunday)
**Scope committed:** 5 PRs — gas-it mode for Monday RLHF meeting prep
**Companion docs:**
- `reflex_feedback_curator_and_skeptic.md` — original design
- `reflex_feedback_curator_and_skeptic_prompts.md` — agent definition PR (already on work mac, ready to send today)
- `reflex_redesign.md` — target architecture (I-0: expert labeling must compound)
- `reflex_redesign_process.md` — deliberation log

---

## Why this matters (30-second version)

The Curator + Skeptic PR (landing today) defines the agent behavior. These 5 follow-up PRs build the **structured capture substrate + observability + velocity baseline + meeting prototype** so that James walks into Monday's RLHF meeting with a **working demonstration**, not a proposal:

- 60+ expert judgments already captured from cycles 1-66 (backfilled)
- Baseline velocity number computed from real card history ("current median idea-to-launch: N days")
- Dashboard showing judgment distribution + pattern provenance + verdict counts
- 10 fresh Skeptic verdicts on top Opportunity cards for structured discussion material

Meeting reframe: from *proposal-review* to *experience the system and tell us where you disagree*. That's architect-altitude positioning.

**Load-bearing invariant (I-0):** every expert-minute produces a structured, attributable, queryable, durable unit of knowledge that makes future cards better.

**I-1 (observability) enablers added:** cost ledger + cycle log + Skeptic verdict log so every agent run is inspectable from day 1 and regressions surface immediately.

---

## Dependency chain

```
PR #1 (state primitives, 6 schemas)
   ExpertJudgment, Disagreement, CostLedgerEntry, CycleLogEntry,
   SkepticVerdict, PatternProvenance + CLIs + tests
        │
        ├──▶ PR #2 (Curator + Skeptic emit structured records)
        │       Curator emits judgments + cost + cycle
        │       Skeptic emits verdicts + cost + cycle
        │         │
        │         ├──▶ PR #3 (backfill + provenance port)
        │         │      Curator runs over cycles 1-66 comment history
        │         │      quality_patterns.md entries → PatternProvenance seed
        │         │
        │         └──▶ PR #5 (pre-meeting Skeptic run — stretch)
        │                10 top Opportunity cards → verdict_log.jsonl
        │
        └──▶ PR #4 (velocity baseline + dashboard)
               Computes per-card cycle times from Asana metadata
               Dashboard CLI reads all JSONL logs → summary stats
```

PRs #1-3 land serially. PR #4 can run parallel to #3 (depends only on #1). PR #5 requires #1+#2 merged and Skeptic validated first.

**Timing target:** all 5 land by Monday AM before the RLHF meeting. Realistic in 36 hours of focused work-leo time if CI is fast.

---

## Prerequisites (expected state on work mac before starting)

- [x] Curator + Skeptic agent definition PR is merged (primary PR going today; assume merged before PR #1 below)
- [x] `services/reflex/detect/agents/feedback_curator.md` exists
- [x] `services/reflex/detect/agents/skeptic.md` exists
- [x] `services/reflex/detect/quality/proposed/.gitkeep` exists
- [x] `services/reflex/detect/CLAUDE.md` references the two new agents
- [x] Python env has `pydantic >= 2.0` available (it's already used in Reflex, verify)

If any prerequisite is missing, resolve before starting.

---

## PR #1 — State primitives (typed schemas + JSONL I/O)

### Goal
Land ALL pydantic data contracts for expert judgment + observability + verdict capture, plus the append-only JSONL writer utility. No behavioral change yet — purely infrastructure. Same pattern repeated across 6 schemas so review surface is low-cognitive-load.

### Scope
- **6 pydantic schemas:** `ExpertJudgment`, `Disagreement` (+ `ExpertPosition`), `CostLedgerEntry`, `CycleLogEntry`, `SkepticVerdict` (+ `SkepticCheck`), `PatternProvenance`
- **1 I/O utility:** `append_jsonl`, `read_jsonl`, `iter_jsonl`
- **6 CLI wrappers:** `append_judgment`, `append_disagreement`, `append_cost_ledger`, `append_cycle_log`, `append_skeptic_verdict`, `append_pattern_provenance` — each validates-then-appends
- **Empty state files:** one per schema
- **Unit tests:** roundtrip + validation + I/O for every schema

### Files to create

#### 1. `services/reflex/detect/infra/__init__.py`
Empty file (package marker).

#### 2. `services/reflex/detect/infra/schemas/__init__.py`
```python
from .expert_judgment import ExpertJudgment, JudgmentType, JudgmentConfidence, JudgmentSource
from .disagreement import Disagreement, ExpertPosition
from .cost_ledger import CostLedgerEntry
from .cycle_log import CycleLogEntry
from .skeptic_verdict import SkepticVerdict, SkepticCheck, SkepticCheckName, SkepticCheckOutcome, VerdictKind
from .pattern_provenance import PatternProvenance, ProvenanceSeedSource

__all__ = [
    # Expert judgment
    "ExpertJudgment",
    "JudgmentType",
    "JudgmentConfidence",
    "JudgmentSource",
    # Disagreement
    "Disagreement",
    "ExpertPosition",
    # Cost ledger
    "CostLedgerEntry",
    # Cycle log
    "CycleLogEntry",
    # Skeptic verdict
    "SkepticVerdict",
    "SkepticCheck",
    "SkepticCheckName",
    "SkepticCheckOutcome",
    "VerdictKind",
    # Pattern provenance
    "PatternProvenance",
    "ProvenanceSeedSource",
]
```

#### 3. `services/reflex/detect/infra/schemas/expert_judgment.py`

```python
"""ExpertJudgment — the load-bearing record for I-0 (expert labeling must compound).

Every interaction between an expert and a card produces one record. Stored in
state/expert_judgments.jsonl, append-only. See docs/architecture.md for context.
"""
from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

JudgmentType = Literal[
    "agree",       # expert agrees with card as-is
    "disagree",    # expert rejects a claim in the card
    "reframe",     # expert recasts the hypothesis (e.g., "this is a supply problem, not ranking")
    "extend",      # expert adds a new analytical angle
    "retire",      # expert argues the card should die
    "new_info",    # expert brings evidence not in the card
    "question",    # expert asks for clarification
    "approve",     # expert explicitly approves promotion/shipping
]

JudgmentConfidence = Literal["low", "medium", "high"]

JudgmentSource = Literal[
    "asana_comment",
    "slack_dm",
    "one_on_one",
    "meeting",
    "direct_input",
    "canary_override",
]


class ExpertJudgment(BaseModel):
    """One expert's structured judgment on one card (or specific claim within).

    Curator produces these by parsing expert comments and discussions.
    Verbatim rationale is preserved; summary is Curator compression.
    """

    timestamp: datetime
    expert: str = Field(
        ..., description="Canonical expert ID (see infra/experts.yaml). Not a display name."
    )
    expert_role: str | None = Field(
        default=None,
        description="e.g., 'pm_retentive_recs', 'em_hf_ranking_retrieval'. Optional but helpful for analysis.",
    )
    card_gid: str
    card_title: str = Field(
        ..., description="Denormalized card title at time of capture, for audit readability."
    )
    cycle_id: int | None = Field(
        default=None,
        description="Reflex cycle at capture. None for pre-cycle-logging backfills.",
    )
    judgment_type: JudgmentType
    claim_targeted: str | None = Field(
        default=None,
        description="Specific claim the judgment targets (not the whole card). e.g., 'per-state "
        "weights don't survive RL retraining'. Null = judgment is about the whole card.",
    )
    rationale_verbatim: str = Field(
        ..., min_length=1, description="Expert's own words, preserved exactly. Never edited."
    )
    rationale_summary: str = Field(
        ..., min_length=1, description="Curator's ≤2-sentence compression."
    )
    confidence: JudgmentConfidence | None = Field(
        default=None,
        description="Curator's estimate of expert's confidence, based on linguistic signals.",
    )
    cross_card_propagation: list[str] = Field(
        default_factory=list,
        description="Other card_gids this judgment should apply to. Curator suggests; human "
        "can extend. Empty list = applies only to card_gid.",
    )
    source: JudgmentSource
    source_ref: str = Field(
        ..., description="URL, comment gid, or other identifier that locates the original input."
    )
    curator_version: str = Field(
        ...,
        description="Curator prompt version that produced this record. Pin for reproducibility.",
    )
```

#### 4. `services/reflex/detect/infra/schemas/disagreement.py`

```python
"""Disagreement — when two or more experts render conflicting judgments.

Stored in state/disagreements.jsonl. This is signal, not noise — it's where deep
discussion is warranted. Curator detects; humans resolve.
"""
from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class ExpertPosition(BaseModel):
    """One expert's position in a disagreement."""

    expert: str
    judgment_type: str           # from ExpertJudgment.judgment_type
    position_summary: str = Field(..., min_length=1)
    judgment_ref: str = Field(
        ...,
        description="Foreign key into expert_judgments.jsonl. "
        "Format: '{timestamp.isoformat()}:{expert}' (stable natural key).",
    )


ResolutionState = Literal["open", "resolved_by_data", "resolved_by_seniority", "parked"]


class Disagreement(BaseModel):
    """Two or more experts hold conflicting positions on the same claim."""

    timestamp: datetime
    card_gid: str
    cycle_id: int | None = None
    claim_targeted: str = Field(
        ..., min_length=1, description="The specific claim the experts disagree on."
    )
    positions: list[ExpertPosition] = Field(..., min_length=2)
    detected_by: Literal["curator_auto", "explicit_tag"]
    resolution: ResolutionState = "open"
    resolution_cycle: int | None = None
    resolution_notes: str | None = None

    @model_validator(mode="after")
    def _positions_have_distinct_experts(self) -> "Disagreement":
        experts = [p.expert for p in self.positions]
        if len(set(experts)) < 2:
            raise ValueError("Disagreement requires at least 2 distinct experts")
        return self
```

#### 4a. `services/reflex/detect/infra/schemas/cost_ledger.py`

```python
"""CostLedgerEntry — one record per agent API call.

Stored in state/cost_ledger.jsonl. Enables cost-per-card, cost-per-playbook, cost-per-cycle
analysis. Critical for I-1 (observability) — detect/CLAUDE.md line 102 currently says
"Cost: Untracked." This schema closes that gap.
"""
from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

AgentName = Literal["pm", "ds", "skeptic", "curator", "backfill", "pinkerton_canary"]


class CostLedgerEntry(BaseModel):
    """One API call's cost. Appended per-call, not per-cycle."""

    timestamp: datetime
    cycle_id: int | None = None
    run_id: str = Field(
        ..., description="UUID grouping calls within one agent run. Same across multiple API "
        "calls in one cycle."
    )
    agent: AgentName
    model: str = Field(..., description="e.g. 'claude-sonnet-4-6', 'claude-opus-4-7'")
    operation: str = Field(
        ..., description="Semantic op type: 'playbook_execution', 'enrichment', 'verdict', "
        "'judgment_emission', 'backfill_curate'"
    )
    capability: str | None = Field(
        default=None,
        description="Which playbook/check was active, if applicable. "
        "e.g. 'market_cg_performance', 'vlm_verification'.",
    )
    input_tokens: int = Field(..., ge=0)
    output_tokens: int = Field(..., ge=0)
    cached_tokens: int = Field(default=0, ge=0)
    cost_usd: float = Field(..., ge=0.0)
```

#### 4b. `services/reflex/detect/infra/schemas/cycle_log.py`

```python
"""CycleLogEntry — one record per agent cycle completion.

Stored in state/cycle_log.jsonl. Structured summary of what an agent did this cycle.
Enables regression detection and compounding-speed measurement. Load-bearing for I-1.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

AgentName = Literal["pm", "ds", "skeptic", "curator"]


class CycleLogEntry(BaseModel):
    """Summary of one agent run. Written at run end, even on failure."""

    cycle_id: int | None = None
    timestamp: datetime
    agent: AgentName
    run_id: str = Field(..., description="UUID correlating with cost_ledger entries.")
    duration_s: float = Field(..., ge=0.0)
    inputs: dict[str, Any] = Field(
        default_factory=dict,
        description="What the agent read. Structure is agent-specific but must be serializable. "
        "e.g. for PM: {'rough_ideas_count': 2, 'board_hypothesis_count': 12}.",
    )
    outputs: dict[str, Any] = Field(
        default_factory=dict,
        description="What the agent produced. e.g. for PM: {'hypotheses_created': 4, "
        "'hypotheses_strengthened': 2}.",
    )
    capabilities_invoked: list[str] = Field(
        default_factory=list,
        description="Which named moves ran. e.g. ['market_cg_performance', 'relevance_gaps'].",
    )
    errors: list[str] = Field(
        default_factory=list, description="Structured error messages, one per failure."
    )
    validation_failures: list[str] = Field(
        default_factory=list,
        description="Boundary-check failures — schema validation errors when reading or writing "
        "typed artifacts.",
    )
```

#### 4c. `services/reflex/detect/infra/schemas/skeptic_verdict.py`

```python
"""SkepticVerdict — one record per Skeptic review of a card.

Stored in state/verdict_log.jsonl. Load-bearing for the Skeptic eval harness:
precision/recall computed from these records once `human_agreed` is backfilled by the
expert review step. Without this schema, Skeptic regressions are invisible.
"""
from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

SkepticCheckName = Literal[
    "pattern_check",
    "context_check",
    "evidence_check",
    "internal_consistency",
    "novelty",
]

SkepticCheckOutcome = Literal["PASS", "FAIL", "N/A"]

VerdictKind = Literal["PASS", "FAIL", "NEEDS_HUMAN"]


class SkepticCheck(BaseModel):
    """One of the 5 Skeptic checks."""

    name: SkepticCheckName
    outcome: SkepticCheckOutcome
    rationale: str = Field(..., min_length=1)
    patterns_cited: list[str] = Field(default_factory=list)


class SkepticVerdict(BaseModel):
    """One Skeptic review pass over one OpportunityCard."""

    timestamp: datetime
    cycle_id: int | None = None
    card_gid: str
    card_title: str
    verdict: VerdictKind
    checks: list[SkepticCheck]
    fail_reasons: list[str] = Field(
        default_factory=list,
        description="Specific, pattern-cited reasons when verdict is FAIL or NEEDS_HUMAN.",
    )
    revision_round: int = Field(default=0, ge=0, le=2)
    confidence: float = Field(..., ge=0.0, le=1.0)
    skeptic_version: str = Field(..., description="Skeptic prompt version that produced this.")
    # Backfilled fields — critical for the eval harness
    human_reviewed: bool | None = Field(
        default=None,
        description="True once a human expert reviewed the card post-verdict. Backfilled by "
        "Curator when it sees the human comment on the card.",
    )
    human_agreed: bool | None = Field(
        default=None,
        description="True if the human's ultimate decision aligned with Skeptic's verdict. "
        "Backfilled. This is the eval signal — precision/recall run over these.",
    )
```

#### 4d. `services/reflex/detect/infra/schemas/pattern_provenance.py`

```python
"""PatternProvenance — links each pattern in the system to its originating expert judgment(s).

Stored in state/pattern_provenance.jsonl. Seed population comes from porting existing
quality_patterns.md entries (each has 'Discovered: Cycle X' — we reconstruct what we can).
Future entries come from Curator aggregation over ExpertJudgment records.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

ProvenanceSeedSource = Literal["quality_patterns_md_port", "judgment_aggregation"]


class PatternProvenance(BaseModel):
    """Traces a pattern to the expert judgments that justified it."""

    pattern_id: str = Field(..., description="Stable slug, e.g. 'cg_source_decomposition'")
    pattern_title: str
    pattern_file: str = Field(
        ..., description="Path to the pattern's current file location."
    )
    created_cycle: int | None = Field(
        default=None, description="Cycle pattern was first documented. None if unknown."
    )
    source_judgments: list[str] = Field(
        default_factory=list,
        description="Natural keys into expert_judgments.jsonl "
        "(format: '{timestamp.isoformat()}:{expert}'). Empty for seed-ported patterns.",
    )
    contributors: list[str] = Field(
        default_factory=list,
        description="Canonical expert IDs whose judgments informed this pattern. Empty for seeds "
        "until provenance is reconstructed.",
    )
    consensus_score: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="1.0 = all judgments agree; 0.0 = maximal disagreement. Null until ≥2 "
        "judgments exist.",
    )
    last_reinforced_cycle: int | None = None
    seed_source: ProvenanceSeedSource | None = Field(
        default=None,
        description="'quality_patterns_md_port' for initial port; 'judgment_aggregation' for "
        "runtime-aggregated; null for unset.",
    )
```

#### 5. `services/reflex/detect/infra/log_append.py`

```python
"""Append-only JSONL I/O for typed state records."""
from __future__ import annotations

from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def append_jsonl(path: Path, entry: BaseModel) -> None:
    """Append one pydantic model as a JSON line to path.

    Creates the file and parent directories if missing. Each write is one open-append-close
    cycle so concurrent writers on POSIX filesystems don't interleave within a line.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(entry.model_dump_json())
        f.write("\n")


def read_jsonl(path: Path, model: type[T]) -> list[T]:
    """Read all records from path into a list of pydantic models.

    Returns [] if path does not exist. Skips blank lines. Raises on malformed lines
    (deliberate — malformed data in an audit log must fail loud).
    """
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [model.model_validate_json(line) for line in f if line.strip()]


def iter_jsonl(path: Path, model: type[T]):
    """Streaming version for large files."""
    if not path.exists():
        return
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield model.model_validate_json(line)
```

#### 6. `services/reflex/detect/state/.gitkeep`
Empty file — ensures the `state/` directory exists in the repo.

#### 7. `services/reflex/detect/state/expert_judgments.jsonl`
Empty file (checked in — the log itself is the durable record).

#### 8. `services/reflex/detect/state/disagreements.jsonl`
Empty file.

#### 8a. `services/reflex/detect/state/cost_ledger.jsonl`
Empty file.

#### 8b. `services/reflex/detect/state/cycle_log.jsonl`
Empty file.

#### 8c. `services/reflex/detect/state/verdict_log.jsonl`
Empty file.

#### 8d. `services/reflex/detect/state/pattern_provenance.jsonl`
Empty file.

#### 9. `services/reflex/detect/infra/experts.yaml`

```yaml
# Canonical expert ID mapping.
# Curator normalizes expert names to canonical_id when writing ExpertJudgment records.
# Extend when new experts join the review rotation.

experts:
  - canonical_id: james_li
    role: em_hf_cg
    asana_gids: ["REPLACE_WITH_JAMES_ASANA_USER_GID"]
    name_variants: ["James Li", "jamesli", "james.li@pinterest.com"]

  - canonical_id: andrew_y
    role: sr_director_product
    asana_gids: ["REPLACE_WITH_ANDREW_ASANA_USER_GID"]
    name_variants: ["Andrew Y", "Andrew Yaroshevsky", "ayaroshevsky"]

  - canonical_id: dylan_wang
    role: em_hf_ranking_retrieval
    asana_gids: ["REPLACE_WITH_DYLAN_ASANA_USER_GID"]
    name_variants: ["Dylan Wang"]

  - canonical_id: anna_k
    role: pm_retentive_recs
    asana_gids: ["REPLACE_WITH_ANNA_ASANA_USER_GID"]
    name_variants: ["Anna K", "Anna Kittyhawk"]  # update with real last name on work-leo

  - canonical_id: matt_chun
    role: pm_upp
    asana_gids: ["REPLACE_WITH_MATT_ASANA_USER_GID"]
    name_variants: ["Matt Chun", "Matthew Chun"]

  - canonical_id: tim_chu
    role: em_homefeed_infra
    asana_gids: ["REPLACE_WITH_TIM_ASANA_USER_GID"]
    name_variants: ["Tim Chu"]

  - canonical_id: dhruvil_badani
    role: em_homefeed_peer  # update to actual title on work-leo
    asana_gids: ["REPLACE_WITH_DHRUVIL_ASANA_USER_GID"]
    name_variants: ["Dhruvil Badani", "Dhruvil"]

  - canonical_id: rahul_goutam
    role: em_blending_hf
    asana_gids: ["REPLACE_WITH_RAHUL_ASANA_USER_GID"]
    name_variants: ["Rahul Goutam"]

# If a commenter doesn't match any entry, Curator emits expert: "unknown_{slug}"
# and logs a warning. Add them to this file when seen.
```

**Work-leo note:** replace `REPLACE_WITH_*_ASANA_USER_GID` placeholders with real Asana user GIDs. Fetch via `GET /users` from the workspace.

### Tests

Create `services/reflex/detect/tests/test_schemas.py`:

```python
"""Tests for infra/schemas — roundtrip, validation, JSONL I/O."""
from datetime import datetime
from pathlib import Path

import pytest
from pydantic import ValidationError

from reflex.detect.infra.log_append import append_jsonl, read_jsonl
from reflex.detect.infra.schemas import (
    Disagreement,
    ExpertJudgment,
    ExpertPosition,
)


def _sample_judgment() -> ExpertJudgment:
    return ExpertJudgment(
        timestamp=datetime(2026, 4, 19, 12, 0, 0),
        expert="james_li",
        expert_role="em_hf_cg",
        card_gid="1210abc",
        card_title="Per-state utility weights",
        cycle_id=67,
        judgment_type="disagree",
        claim_targeted="per-state weights don't survive RL retraining",
        rationale_verbatim="I don't think this works because RL utility supersedes static per-state weights.",
        rationale_summary="Static per-state weights superseded by learned per-user weights from RL.",
        confidence="high",
        cross_card_propagation=["1210def", "1210ghi"],
        source="asana_comment",
        source_ref="https://app.asana.com/0/1/2/stories/3",
        curator_version="v0.1.0",
    )


def test_expert_judgment_roundtrip():
    original = _sample_judgment()
    serialized = original.model_dump_json()
    recovered = ExpertJudgment.model_validate_json(serialized)
    assert original == recovered


def test_expert_judgment_rejects_empty_rationale():
    with pytest.raises(ValidationError):
        ExpertJudgment(
            timestamp=datetime.now(),
            expert="james_li",
            card_gid="x",
            card_title="x",
            judgment_type="agree",
            rationale_verbatim="",  # empty — should fail
            rationale_summary="x",
            source="asana_comment",
            source_ref="x",
            curator_version="v0.1.0",
        )


def test_disagreement_requires_at_least_two_distinct_experts():
    with pytest.raises(ValidationError):
        Disagreement(
            timestamp=datetime.now(),
            card_gid="x",
            claim_targeted="y",
            positions=[
                ExpertPosition(
                    expert="james_li",
                    judgment_type="disagree",
                    position_summary="a",
                    judgment_ref="x",
                ),
                ExpertPosition(
                    expert="james_li",  # same expert twice — should fail
                    judgment_type="agree",
                    position_summary="b",
                    judgment_ref="y",
                ),
            ],
            detected_by="curator_auto",
        )


def test_log_append_creates_file_and_writes_one_line(tmp_path: Path):
    log_path = tmp_path / "state" / "expert_judgments.jsonl"
    append_jsonl(log_path, _sample_judgment())
    assert log_path.exists()
    content = log_path.read_text()
    assert content.count("\n") == 1
    assert '"expert":"james_li"' in content


def test_read_jsonl_roundtrips_multiple_entries(tmp_path: Path):
    log_path = tmp_path / "expert_judgments.jsonl"
    j1 = _sample_judgment()
    j2 = _sample_judgment().model_copy(update={"judgment_type": "agree"})
    append_jsonl(log_path, j1)
    append_jsonl(log_path, j2)
    recovered = read_jsonl(log_path, ExpertJudgment)
    assert len(recovered) == 2
    assert recovered[0].judgment_type == "disagree"
    assert recovered[1].judgment_type == "agree"


def test_read_jsonl_missing_file_returns_empty():
    assert read_jsonl(Path("/tmp/does_not_exist_yzz.jsonl"), ExpertJudgment) == []


# Additional schemas — roundtrip + validation

def test_cost_ledger_roundtrip():
    from reflex.detect.infra.schemas import CostLedgerEntry
    entry = CostLedgerEntry(
        timestamp=datetime(2026, 4, 19, 12, 0, 0),
        cycle_id=67,
        run_id="run-abc-123",
        agent="curator",
        model="claude-sonnet-4-6",
        operation="judgment_emission",
        capability=None,
        input_tokens=8400,
        output_tokens=1200,
        cached_tokens=6200,
        cost_usd=0.0187,
    )
    assert CostLedgerEntry.model_validate_json(entry.model_dump_json()) == entry


def test_cost_ledger_rejects_negative_tokens():
    from reflex.detect.infra.schemas import CostLedgerEntry
    with pytest.raises(ValidationError):
        CostLedgerEntry(
            timestamp=datetime.now(),
            run_id="x",
            agent="curator",
            model="x",
            operation="x",
            input_tokens=-1,   # should fail
            output_tokens=1,
            cost_usd=0.0,
        )


def test_cycle_log_roundtrip():
    from reflex.detect.infra.schemas import CycleLogEntry
    entry = CycleLogEntry(
        cycle_id=67,
        timestamp=datetime(2026, 4, 19, 13, 0, 0),
        agent="pm",
        run_id="run-xyz-456",
        duration_s=1847.3,
        inputs={"rough_ideas_count": 2, "unresponded_comments": 3},
        outputs={"hypotheses_created": 4, "hypotheses_strengthened": 2},
        capabilities_invoked=["market_cg_performance", "relevance_gaps"],
        errors=[],
        validation_failures=[],
    )
    assert CycleLogEntry.model_validate_json(entry.model_dump_json()) == entry


def test_skeptic_verdict_roundtrip_and_confidence_bounds():
    from reflex.detect.infra.schemas import SkepticCheck, SkepticVerdict
    verdict = SkepticVerdict(
        timestamp=datetime(2026, 4, 19, 14, 0, 0),
        cycle_id=67,
        card_gid="1210abc",
        card_title="Per-state utility weights",
        verdict="FAIL",
        checks=[
            SkepticCheck(
                name="context_check",
                outcome="FAIL",
                rationale="Uses datestr column; should be date per Known Dead Ends.",
                patterns_cited=["known_dead_ends.datestr_vs_date"],
            ),
            SkepticCheck(
                name="pattern_check",
                outcome="PASS",
                rationale="Applies CG source decomposition.",
                patterns_cited=["cg_source_decomposition"],
            ),
        ],
        fail_reasons=["datestr column usage"],
        revision_round=0,
        confidence=0.92,
        skeptic_version="v0.1.0",
    )
    assert SkepticVerdict.model_validate_json(verdict.model_dump_json()) == verdict

    with pytest.raises(ValidationError):
        verdict.model_copy(update={"confidence": 1.1})


def test_pattern_provenance_seed_port_shape():
    from reflex.detect.infra.schemas import PatternProvenance
    prov = PatternProvenance(
        pattern_id="cg_source_decomposition",
        pattern_title="CG source decomposition",
        pattern_file="services/reflex/detect/quality_patterns.md",
        created_cycle=2,
        source_judgments=[],
        contributors=[],
        consensus_score=None,
        seed_source="quality_patterns_md_port",
    )
    assert PatternProvenance.model_validate_json(prov.model_dump_json()) == prov
```

### CLI wrappers (6 files, same pattern)

All 6 CLIs live under `services/reflex/detect/cli/` and follow the same shape: parse JSON, validate via pydantic, append to the matching JSONL file, fail loud on invalid input. Include in PR1 so later PRs are purely prompt/script changes.

#### `cli/__init__.py`
Empty.

#### `cli/append_judgment.py`
```python
"""CLI: validate and append an ExpertJudgment to state/expert_judgments.jsonl."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from reflex.detect.infra.log_append import append_jsonl
from reflex.detect.infra.schemas import ExpertJudgment

LOG_PATH = Path(__file__).resolve().parents[1] / "state" / "expert_judgments.jsonl"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Append a validated ExpertJudgment.")
    parser.add_argument("--json", required=True)
    parser.add_argument("--log-path", default=str(LOG_PATH))
    args = parser.parse_args(argv)

    try:
        payload = json.loads(args.json)
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2
    try:
        judgment = ExpertJudgment.model_validate(payload)
    except Exception as exc:
        print(f"ERROR: validation failed: {exc}", file=sys.stderr)
        return 3

    append_jsonl(Path(args.log_path), judgment)
    print(f"OK: appended judgment for expert={judgment.expert} card={judgment.card_gid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

#### `cli/append_disagreement.py`
Mirror of the above; imports `Disagreement`; writes to `state/disagreements.jsonl`.

#### `cli/append_cost_ledger.py`
Mirror; imports `CostLedgerEntry`; writes to `state/cost_ledger.jsonl`.

#### `cli/append_cycle_log.py`
Mirror; imports `CycleLogEntry`; writes to `state/cycle_log.jsonl`.

#### `cli/append_skeptic_verdict.py`
Mirror; imports `SkepticVerdict`; writes to `state/verdict_log.jsonl`.

#### `cli/append_pattern_provenance.py`
Mirror; imports `PatternProvenance`; writes to `state/pattern_provenance.jsonl`.

**Work-leo implementation hint:** all 6 CLIs are ~40 LOC variations on the `append_judgment` template. Consider DRYing via a tiny helper in `cli/_base.py` that takes `(model_class, log_path)` and returns a main function — trade-off is 1 shared file vs 6 independent ones. Either is fine; favor independence if review latency matters.

### CLI integration tests

Add `services/reflex/detect/tests/test_cli_wrappers.py` with one parametrized test across all 6 CLIs: given a valid payload → exit 0 + one line appended; given an invalid payload → non-zero exit + no partial write.

### PR description (PR #1)

```markdown
## Reflex — State primitives + observability schemas (PR 1 of 5)

**Context:** Follows the Curator + Skeptic agent definition PR. Foundation layer for I-0
(expert labeling must compound) and I-1 (observability — no silent failures) per redesign doc.

**Scope — no behavioral change:**
- 6 pydantic schemas: `ExpertJudgment`, `Disagreement`, `CostLedgerEntry`, `CycleLogEntry`,
  `SkepticVerdict`, `PatternProvenance`
- `log_append` / `read_jsonl` / `iter_jsonl` utilities (append-only JSONL I/O)
- 6 CLI wrappers under `cli/` — each validates-then-appends, fails loud on bad input
- Canonical expert ID map at `infra/experts.yaml`
- 6 empty state files in `state/` (checked in — logs are durable records)
- Unit tests for roundtrip, validation, I/O, and CLI boundary behavior

**What this enables (follow-up PRs):**
- PR #2: Curator emits judgment records; Skeptic emits verdict records; both log cost + cycle
- PR #3: Backfill script populates judgment seed corpus; port script populates provenance seed
- PR #4: Velocity baseline + dashboard (reads from JSONL logs)
- PR #5: Pre-meeting Skeptic run against top 10 cards → verdict_log seed

**Why expanded PR1:** All 6 schemas follow identical shape (pydantic model + CLI + test).
Folding them into one PR keeps downstream PRs focused on behavior not infrastructure.
Review surface grows linearly; cognitive load stays flat.

**Out-of-scope safety:**
- State files are checked in but grow only via PRs #2-5. This PR creates empty files only.
- No agent prompt changes in this PR — Curator and Skeptic still behave as they do in the
  agent definition PR until PR #2 lands.

Co-authored-by: James Li <jli@pinterest.com>
```

### Validation
1. `pytest services/reflex/detect/tests/test_schemas.py` passes
2. `python -c "from reflex.detect.infra.schemas import ExpertJudgment"` imports cleanly
3. Confirm Asana user GIDs in `experts.yaml` are real (fetch via `GET /users`)

---

## PR #2 — Curator + Skeptic emit structured records

### Goal
Extend BOTH the Curator and Skeptic agents to emit structured typed records as they run. Curator emits `ExpertJudgment` + `Disagreement` per comment processed. Skeptic emits `SkepticVerdict` per card reviewed. Both agents also emit `CostLedgerEntry` per API call and one `CycleLogEntry` at end of each run.

### Scope
- Updated `feedback_curator.md` prompt — primary output shifts to typed ExpertJudgment; cost + cycle logging added
- Updated `skeptic.md` prompt — verdict output becomes typed SkepticVerdict via CLI; cost + cycle logging added
- No new Python files — all CLIs live in PR1
- Integration tests: both agents produce valid typed records on sample inputs

### Files to modify

#### 1. Updated `services/reflex/detect/agents/feedback_curator.md`

Append a new section at the top of the prompt (before existing Curator logic):

```markdown
## PRIMARY OUTPUT: Structured ExpertJudgment records

Every expert comment you process produces **two outputs**:

1. **Primary: One `ExpertJudgment` record** — structured, typed, appended to `state/expert_judgments.jsonl` via the CLI.
2. **Secondary: Optional pattern proposal** — only when the judgment reveals a pattern that would improve future cards (existing behavior from original Curator prompt).

The primary output is mandatory. The secondary is discretionary.

### How to emit an ExpertJudgment

For each human comment you process, construct an ExpertJudgment JSON object with these fields:

| Field | How to fill |
|---|---|
| `timestamp` | ISO 8601 of the comment (Asana `created_at` field) |
| `expert` | Canonical ID from `infra/experts.yaml`. Normalize the commenter's name/gid to its canonical_id. If no match, use `unknown_{slugified_name}` and flag for `experts.yaml` update. |
| `expert_role` | From `experts.yaml`; null if unknown expert |
| `card_gid` | Asana card GID the comment is on |
| `card_title` | Current card title (denormalized for audit readability) |
| `cycle_id` | Current Reflex cycle id, or null for backfills |
| `judgment_type` | Classify the comment: `agree` \| `disagree` \| `reframe` \| `extend` \| `retire` \| `new_info` \| `question` \| `approve`. If ambiguous, pick the closest and note ambiguity in rationale_summary. |
| `claim_targeted` | The specific claim the expert is addressing. Null ONLY if the judgment is about the whole card (rare — most comments target a specific claim). |
| `rationale_verbatim` | Expert's exact words. DO NOT summarize, edit, or clean up. Preserve prose as-is. |
| `rationale_summary` | Your ≤2-sentence compression. Capture the *point*, not the surface. |
| `confidence` | `low` \| `medium` \| `high` \| null. Infer from linguistic signals: "I think maybe" → low; "strongly recommend" → high; ambiguous → null. |
| `cross_card_propagation` | GIDs of other cards this judgment should apply to. If the expert says "this is true for all per-state cards," list the relevant card gids. Default: empty list. |
| `source` | `asana_comment` for this phase |
| `source_ref` | Asana comment permalink: `https://app.asana.com/0/{project_gid}/{task_gid}/stories/{story_gid}` |
| `curator_version` | `v0.1.0` (update when this prompt changes) |

### How to append

Once the JSON is constructed, append via the CLI:

```bash
python -m reflex.detect.cli.append_judgment --json '<JSON STRING>'
```

The CLI validates the payload against the pydantic schema. If validation fails, FIX the JSON and retry. Do not silently drop the judgment.

### Disagreement detection (inline)

Before appending a new ExpertJudgment, check existing entries in `state/expert_judgments.jsonl` for the same `card_gid` AND same `claim_targeted`. If an existing judgment has a conflicting `judgment_type` (e.g., existing `agree` + new `disagree`; or `reframe` + `retire` on the same claim), emit a `Disagreement` record:

```bash
python -m reflex.detect.cli.append_disagreement --json '<DISAGREEMENT JSON>'
```

The Disagreement references both judgments via their natural keys (`{timestamp.isoformat()}:{expert}`).

### Idempotency

If a judgment for the same `source_ref` (comment gid) already exists in `state/expert_judgments.jsonl`, skip — do not duplicate. This makes the Curator safe to re-run on overlapping comment windows.
```

### Curator — also emit cost + cycle logs

Append this additional section to the Curator prompt:

```markdown
## OBSERVABILITY: Emit cost ledger and cycle log records

Every Curator run must be inspectable from the state layer. Two additional obligations:

### Per API call: emit `CostLedgerEntry`

At the end of each Asana comment processing cycle, emit one `CostLedgerEntry` record summarizing the API call that processed it:

```bash
python -m reflex.detect.cli.append_cost_ledger --json '{
  "timestamp": "...",
  "cycle_id": null,
  "run_id": "<same run_id for this Curator run>",
  "agent": "curator",
  "model": "claude-sonnet-4-6",
  "operation": "judgment_emission",
  "capability": null,
  "input_tokens": <count>,
  "output_tokens": <count>,
  "cached_tokens": <count>,
  "cost_usd": <computed>
}'
```

If token counts aren't available, fall back to estimates from prompt length; never skip.

### At run end: emit `CycleLogEntry`

One record summarizing the full run:

```bash
python -m reflex.detect.cli.append_cycle_log --json '{
  "cycle_id": null,
  "timestamp": "<end-of-run>",
  "agent": "curator",
  "run_id": "<run_id>",
  "duration_s": <total>,
  "inputs": {"comments_processed": <N>, "cards_touched": <N>},
  "outputs": {"judgments_emitted": <N>, "disagreements_detected": <N>, "unknown_experts_flagged": <N>},
  "capabilities_invoked": [],
  "errors": [],
  "validation_failures": []
}'
```

Emit the cycle log EVEN ON FAILURE. An errored run is still data.
```

Keep the rest of the existing Curator prompt (pattern proposals, conflict detection) intact. Pattern proposals are now framed as *aggregates* over judgments, not the primary output.

#### 2. Updated `services/reflex/detect/agents/skeptic.md`

Append to the Skeptic prompt a new section that shifts its output from free-form annotations to typed `SkepticVerdict` records, plus adds the same cost + cycle logging obligations.

```markdown
## PRIMARY OUTPUT: Structured SkepticVerdict records

Every card review produces **two outputs**:

1. **Primary:** One `SkepticVerdict` record appended to `state/verdict_log.jsonl` via CLI.
2. **Secondary:** Human-readable annotation on the Asana card (existing behavior).

The structured record is mandatory. It's the load-bearing input to the Skeptic eval harness
(future work) — without it, regressions in the Skeptic prompt will be invisible.

### How to emit a SkepticVerdict

After running the 5 checks on a card, construct the verdict JSON:

```json
{
  "timestamp": "<now>",
  "cycle_id": null,
  "card_gid": "<card gid>",
  "card_title": "<current title>",
  "verdict": "PASS" | "FAIL" | "NEEDS_HUMAN",
  "checks": [
    {
      "name": "pattern_check",
      "outcome": "PASS" | "FAIL" | "N/A",
      "rationale": "<specific reason>",
      "patterns_cited": ["<pattern slug>", ...]
    },
    ... 5 checks total, one per check name (pattern_check, context_check,
        evidence_check, internal_consistency, novelty)
  ],
  "fail_reasons": ["<specific, pattern-cited reason>", ...],
  "revision_round": 0 | 1 | 2,
  "confidence": <float 0.0-1.0>,
  "skeptic_version": "v0.1.0"
}
```

Append via CLI:

```bash
python -m reflex.detect.cli.append_skeptic_verdict --json '<JSON STRING>'
```

The CLI validates. If validation fails, fix the JSON and retry. Do not silently drop.

### Rules for structured verdict output

- **All 5 checks always appear.** If a check isn't applicable to this card, emit it with `outcome: "N/A"` and a one-line rationale. Never omit a check.
- **`patterns_cited` references slugs from quality_patterns.md or dead_ends.yaml.** Use stable identifiers, not prose.
- **`fail_reasons` is only populated for FAIL or NEEDS_HUMAN verdicts.** Empty list for PASS.
- **`confidence` is your honest estimate.** Low confidence → NEEDS_HUMAN, not FAIL.

## OBSERVABILITY: Emit cost + cycle logs

Same pattern as Curator. After each card review, append one `CostLedgerEntry` via
`append_cost_ledger` (agent: "skeptic", operation: "verdict"). At run end, append one
`CycleLogEntry` via `append_cycle_log` (agent: "skeptic"). Emit cycle log even on failure.
```

Keep the rest of the existing Skeptic prompt (5 checks, 2-revision cap, NEEDS_HUMAN handling) intact.

### Integration test

Create `services/reflex/detect/tests/test_curator_append.py`:

```python
"""Test that the Curator CLI wrappers validate and append correctly.
The Curator prompt itself is not unit-tested here (that's the integration test via backfill).
"""
import json
import subprocess
from pathlib import Path


def test_append_judgment_cli_valid_input(tmp_path: Path):
    log_path = tmp_path / "expert_judgments.jsonl"
    payload = {
        "timestamp": "2026-04-19T12:00:00Z",
        "expert": "james_li",
        "card_gid": "1210abc",
        "card_title": "Per-state utility weights",
        "judgment_type": "disagree",
        "claim_targeted": "per-state weights don't survive RL retraining",
        "rationale_verbatim": "I don't think this works because RL supersedes static per-state weights.",
        "rationale_summary": "Static per-state weights superseded by learned per-user weights.",
        "source": "asana_comment",
        "source_ref": "https://app.asana.com/0/x/y/stories/z",
        "curator_version": "v0.1.0",
    }
    result = subprocess.run(
        [
            "python", "-m", "reflex.detect.cli.append_judgment",
            "--json", json.dumps(payload),
            "--log-path", str(log_path),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert log_path.exists()
    lines = log_path.read_text().strip().splitlines()
    assert len(lines) == 1


def test_append_judgment_cli_rejects_invalid(tmp_path: Path):
    log_path = tmp_path / "expert_judgments.jsonl"
    payload = {"timestamp": "2026-04-19T12:00:00Z"}  # missing required fields
    result = subprocess.run(
        [
            "python", "-m", "reflex.detect.cli.append_judgment",
            "--json", json.dumps(payload),
            "--log-path", str(log_path),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "validation failed" in result.stderr
    assert not log_path.exists()  # no partial write on failure
```

### PR description (PR #2)

```markdown
## Reflex — Curator + Skeptic emit structured records (PR 2 of 5)

**Context:** Follows PR #1 (state primitives). Activates the capture substrate by routing
Curator's and Skeptic's outputs through the typed JSONL logs.

**Scope — agent prompt extensions only:**
- Curator emits one `ExpertJudgment` per processed comment as primary output (pattern proposals
  become secondary aggregates)
- Curator emits `Disagreement` records when it detects conflicting judgments on the same
  card/claim
- Skeptic emits one `SkepticVerdict` per card reviewed (all 5 checks always present; typed
  verdict + fail_reasons + confidence)
- Both agents emit `CostLedgerEntry` per API call and one `CycleLogEntry` at run end — even
  on failure

**Reliability guardrails:**
- All CLIs fail loud on validation errors; no silent partial writes
- Curator idempotent by source_ref (safe to re-run)
- Unknown experts produce `unknown_{slug}` IDs surfaced for `experts.yaml` updates
- Cycle log emitted on failure so regressions are visible

**Non-goals:**
- Backfill over historical comments (PR #3)
- Skeptic eval harness (needs accumulated human_agreed backfills)
- Pattern aggregation from judgments (later phase)

Co-authored-by: James Li <jli@pinterest.com>
```

### Validation
1. `pytest services/reflex/detect/tests/test_cli_wrappers.py` passes (from PR1)
2. Manual Curator: sample comment payload → one valid `ExpertJudgment` line in log
3. Manual Curator: two conflicting comments on same card/claim → one `Disagreement` record
4. Manual Skeptic: sample card → one valid `SkepticVerdict` with all 5 checks present
5. Both agents: verify `cycle_log.jsonl` gains one record per run (including forced-error runs)
6. Both agents: verify `cost_ledger.jsonl` gains per-API-call records with non-zero token counts

---

## PR #3 — Backfill script + PatternProvenance seed port

### Goal
Populate the two seed corpora before the RLHF meeting:

1. **`state/expert_judgments.jsonl`** — backfilled by running the Curator over historical Asana card comments (cycles 1-66).
2. **`state/pattern_provenance.jsonl`** — seeded by parsing existing `quality_patterns.md` entries and emitting one `PatternProvenance` record per pattern.

Both populate real data that demonstrates the system's value at the meeting.

### Scope
- `scripts/backfill_expert_judgments.py` — the Curator backfill
- `scripts/port_pattern_provenance.py` — one-time port of quality_patterns.md
- README with run protocol for both
- Dry-run mode + bounded mode for both

### Files to create

#### 1. `services/reflex/detect/scripts/__init__.py`
Empty.

#### 2. `services/reflex/detect/scripts/backfill_expert_judgments.py`

```python
"""Backfill ExpertJudgment records from Asana card comment history.

Iterates Hypotheses + Opportunities + Archived sections, pulls human comments on
each card, feeds each comment through the Curator, writes structured records to
state/expert_judgments.jsonl.

Idempotent: keyed on source_ref (Asana story GID). Re-runs skip already-processed comments.
Resumable: partial runs leave the log in a consistent state.

Usage:
    # Dry run against 5 cards (prints what would be processed, no writes):
    python -m reflex.detect.scripts.backfill_expert_judgments --dry-run --max-cards 5

    # Real run against all cards:
    python -m reflex.detect.scripts.backfill_expert_judgments

    # Bounded real run (useful for first-time validation):
    python -m reflex.detect.scripts.backfill_expert_judgments --max-cards 20
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import requests  # use whatever HTTP library Reflex conventionally uses

from reflex.detect.infra.log_append import iter_jsonl
from reflex.detect.infra.schemas import ExpertJudgment

LOG = logging.getLogger(__name__)

ASANA_BASE_URL = "https://app.asana.com/api/1.0"
JUDGMENT_LOG = Path(__file__).resolve().parents[1] / "state" / "expert_judgments.jsonl"

# Section GIDs from board_setup.md — replace with real values on work-leo:
SECTION_HYPOTHESES = os.environ.get("SECTION_HYPOTHESES_GID", "REPLACE_ME")
SECTION_OPPORTUNITIES = os.environ.get("SECTION_OPPORTUNITIES_GID", "REPLACE_ME")
SECTION_ARCHIVED = os.environ.get("SECTION_ARCHIVED_GID", "REPLACE_ME")

ASANA_TOKEN = os.environ["ASANA_TOKEN"]  # fail loud if not set

AGENT_PREFIXES = ("**PM Agent**", "**DS Agent**", "**Skeptic**", "**Curator**", "**Feedback Curator**")


def _auth_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {ASANA_TOKEN}"}


def list_tasks_in_section(section_gid: str) -> list[dict[str, Any]]:
    """Return all tasks in the given section. Paginates as needed."""
    # Implementation: GET /sections/{gid}/tasks with pagination
    ...


def list_comments_on_task(task_gid: str) -> list[dict[str, Any]]:
    """Return all comments (stories of type 'comment') on a task."""
    # Implementation: GET /tasks/{gid}/stories, filter type == 'comment'
    ...


def is_human_comment(comment: dict[str, Any]) -> bool:
    """Filter out agent-authored comments. Humans = doesn't start with agent prefixes."""
    text = comment.get("html_text", "") or comment.get("text", "")
    return not any(text.strip().startswith(prefix) for prefix in AGENT_PREFIXES)


def already_processed_refs() -> set[str]:
    """Return the set of source_refs already in expert_judgments.jsonl."""
    return {j.source_ref for j in iter_jsonl(JUDGMENT_LOG, ExpertJudgment)}


def invoke_curator_on_comment(
    comment: dict[str, Any],
    card: dict[str, Any],
    dry_run: bool,
) -> None:
    """Hand the comment to the Curator agent.

    The Curator prompt knows how to emit ExpertJudgment records via the CLI.
    This function just sets up the invocation context.

    Implementation note: on the work mac, invoke via Claude CLI / the existing
    Reflex agent runner. Pass the comment text + card metadata as the agent's input.
    """
    if dry_run:
        LOG.info(
            "DRY RUN: would process comment %s on card %s",
            comment["gid"],
            card["gid"],
        )
        return

    # Actual invocation — structure depends on Reflex's agent runner convention.
    # Pseudo-code:
    #     result = run_agent(
    #         "feedback_curator",
    #         input={
    #             "mode": "backfill",
    #             "card_gid": card["gid"],
    #             "card_title": card["name"],
    #             "comment_gid": comment["gid"],
    #             "comment_created_at": comment["created_at"],
    #             "comment_author": comment["created_by"],
    #             "comment_text": comment["html_text"],
    #             "cycle_id": None,  # backfill has no live cycle
    #         },
    #     )
    # The Curator prompt will invoke `append_judgment` CLI internally.
    raise NotImplementedError("Wire to work-leo's agent runner.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--max-cards", type=int, default=None,
        help="Cap the number of cards processed (useful for first-time validation).",
    )
    parser.add_argument(
        "--section",
        choices=["hypotheses", "opportunities", "archived", "all"],
        default="all",
    )
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    sections = {
        "hypotheses": SECTION_HYPOTHESES,
        "opportunities": SECTION_OPPORTUNITIES,
        "archived": SECTION_ARCHIVED,
    }
    if args.section != "all":
        sections = {args.section: sections[args.section]}

    processed_refs = already_processed_refs()
    LOG.info("Resuming — %d comments already in log", len(processed_refs))

    processed_count = 0
    skipped_count = 0
    errors: list[str] = []

    for section_name, section_gid in sections.items():
        LOG.info("Section: %s (%s)", section_name, section_gid)
        tasks = list_tasks_in_section(section_gid)
        if args.max_cards:
            tasks = tasks[: args.max_cards]
        for task in tasks:
            comments = list_comments_on_task(task["gid"])
            for comment in comments:
                if not is_human_comment(comment):
                    continue
                ref = f"https://app.asana.com/0/{task['gid']}/stories/{comment['gid']}"
                if ref in processed_refs:
                    skipped_count += 1
                    continue
                try:
                    invoke_curator_on_comment(comment, task, args.dry_run)
                    processed_count += 1
                    time.sleep(0.5)  # gentle rate limiting
                except Exception as exc:
                    errors.append(f"card={task['gid']} comment={comment['gid']}: {exc}")
                    LOG.exception("Curator failed on comment %s", comment["gid"])

    LOG.info(
        "Done. processed=%d skipped=%d errors=%d",
        processed_count, skipped_count, len(errors),
    )
    if errors:
        LOG.warning("Errors (first 10): %s", errors[:10])
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

**Work-leo implementation notes:**
- The `list_tasks_in_section` / `list_comments_on_task` stubs need real implementations. Reference `board_setup.md` for the Asana REST API patterns already in use. The existing PM/DS agents already know how to iterate sections and read stories — mirror those patterns.
- `invoke_curator_on_comment` must wire to whatever agent-runner convention Reflex uses (whether it's a direct Claude CLI call, a subprocess, or an in-process library call — use what the existing agents use).
- Replace `SECTION_*_GID` env var defaults with real GIDs from `board_setup.md`.

#### 2b. `services/reflex/detect/scripts/port_pattern_provenance.py`

```python
"""One-time port: parse existing quality_patterns.md → PatternProvenance seed records.

Every existing pattern has a "Discovered: Cycle X" (and sometimes attribution) tag.
This script extracts those, emits one PatternProvenance record per pattern, and writes
them to state/pattern_provenance.jsonl with seed_source='quality_patterns_md_port'.

Contributors list is populated when attribution is reconstructable (e.g., pattern notes
"Dylan Wang feedback" or "reviewer feedback (James Li)"); otherwise left empty.

Usage:
    python -m reflex.detect.scripts.port_pattern_provenance --dry-run
    python -m reflex.detect.scripts.port_pattern_provenance
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from reflex.detect.infra.log_append import append_jsonl
from reflex.detect.infra.schemas import PatternProvenance

LOG = logging.getLogger(__name__)

QUALITY_PATTERNS = Path(__file__).resolve().parents[1] / "quality_patterns.md"
PROVENANCE_LOG = Path(__file__).resolve().parents[1] / "state" / "pattern_provenance.jsonl"

# Markdown section regex — "### Pattern Title" followed by body until next ###
SECTION_PATTERN = re.compile(r"^### (.+?)$", re.MULTILINE)

# Discovered tag: "- **Discovered:** Cycle N ..."
DISCOVERED_PATTERN = re.compile(r"\*\*Discovered:\*\*\s*Cycle\s*(\d+)", re.IGNORECASE)

# Attribution patterns — order-sensitive; more specific first
ATTRIBUTION_PATTERNS = [
    (re.compile(r"Dylan Wang feedback", re.IGNORECASE), "dylan_wang"),
    (re.compile(r"Andrew Y(\.?|aroshevsky)? feedback", re.IGNORECASE), "andrew_y"),
    (re.compile(r"James Li\b", re.IGNORECASE), "james_li"),
    (re.compile(r"Anna K(\.?)? feedback", re.IGNORECASE), "anna_k"),
    (re.compile(r"reviewer feedback", re.IGNORECASE), None),  # generic — no attribution
]


def slugify(title: str) -> str:
    """Stable slug generator. 'CG source decomposition' → 'cg_source_decomposition'."""
    s = title.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s-]+", "_", s)
    return s


def parse_patterns(text: str) -> list[tuple[str, str]]:
    """Return list of (title, body) for each ### section in the Analytical Approaches + Presentation
    Patterns sections. Stops at 'Known Dead Ends' and later sections (those aren't patterns).
    """
    # Truncate at Known Dead Ends section — everything after isn't "patterns" for provenance
    end_markers = ["## Known Dead Ends", "## Task Quality Ranking", "## Cycle Learnings"]
    cutoff = len(text)
    for marker in end_markers:
        idx = text.find(marker)
        if idx != -1 and idx < cutoff:
            cutoff = idx
    body = text[:cutoff]

    positions = [(m.start(), m.group(1).strip()) for m in SECTION_PATTERN.finditer(body)]
    sections: list[tuple[str, str]] = []
    for i, (start, title) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(body)
        sections.append((title, body[start:end]))
    return sections


def extract_cycle(body: str) -> int | None:
    m = DISCOVERED_PATTERN.search(body)
    return int(m.group(1)) if m else None


def extract_contributors(body: str) -> list[str]:
    found: list[str] = []
    for pat, canonical in ATTRIBUTION_PATTERNS:
        if pat.search(body) and canonical and canonical not in found:
            found.append(canonical)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--log-path", default=str(PROVENANCE_LOG))
    parser.add_argument("--patterns-path", default=str(QUALITY_PATTERNS))
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    patterns_path = Path(args.patterns_path)
    if not patterns_path.exists():
        LOG.error("quality_patterns.md not found at %s", patterns_path)
        return 1

    text = patterns_path.read_text(encoding="utf-8")
    sections = parse_patterns(text)
    LOG.info("Found %d pattern sections", len(sections))

    emitted = 0
    for title, body in sections:
        record = PatternProvenance(
            pattern_id=slugify(title),
            pattern_title=title,
            pattern_file="services/reflex/detect/quality_patterns.md",
            created_cycle=extract_cycle(body),
            source_judgments=[],
            contributors=extract_contributors(body),
            consensus_score=None,
            last_reinforced_cycle=None,
            seed_source="quality_patterns_md_port",
        )
        if args.dry_run:
            LOG.info(
                "DRY RUN: would emit pattern_id=%s cycle=%s contributors=%s",
                record.pattern_id, record.created_cycle, record.contributors,
            )
        else:
            append_jsonl(Path(args.log_path), record)
        emitted += 1

    LOG.info("Done. %d records %s.", emitted, "would-emit" if args.dry_run else "emitted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

**Idempotency note:** this is a one-time port intended to run ONCE. If re-run, it will duplicate records. If you need to re-run, truncate `state/pattern_provenance.jsonl` first. A future enhancement could dedupe by `pattern_id`; for v1, explicit single-run is simpler.

#### 3. `services/reflex/detect/scripts/README.md`

```markdown
# Reflex Backfill Scripts

## `backfill_expert_judgments.py`

Populates `state/expert_judgments.jsonl` by running the Curator agent against every human comment on every card in Hypotheses + Opportunities + Archived sections.

### Environment

```bash
export ASANA_TOKEN=...                    # personal access token
export SECTION_HYPOTHESES_GID=...
export SECTION_OPPORTUNITIES_GID=...
export SECTION_ARCHIVED_GID=...
```

### Recommended run sequence

1. **Dry run against 3 cards** to validate wiring:
   ```bash
   python -m reflex.detect.scripts.backfill_expert_judgments --dry-run --max-cards 3 -v
   ```
2. **Real run against 5 cards** to spot-check Curator parsing:
   ```bash
   python -m reflex.detect.scripts.backfill_expert_judgments --max-cards 5
   # Then: open state/expert_judgments.jsonl, eyeball 5-10 records,
   # cross-reference against the original Asana comments.
   ```
3. **If parsing looks clean, full run:**
   ```bash
   python -m reflex.detect.scripts.backfill_expert_judgments
   ```
4. **Post-run summary:**
   ```bash
   python -c "
   from reflex.detect.infra.log_append import iter_jsonl
   from reflex.detect.infra.schemas import ExpertJudgment
   from collections import Counter
   from pathlib import Path
   log = Path('services/reflex/detect/state/expert_judgments.jsonl')
   judgments = list(iter_jsonl(log, ExpertJudgment))
   print(f'Total: {len(judgments)}')
   print('By expert:', Counter(j.expert for j in judgments))
   print('By type:', Counter(j.judgment_type for j in judgments))
   print('Unknown experts (update experts.yaml):',
         [j.expert for j in judgments if j.expert.startswith('unknown_')])
   "
   ```

### Spot-check protocol

After the bounded run (step 2), James manually checks 20 records:
- Does `judgment_type` match the comment's actual intent?
- Is `claim_targeted` specific (not just the whole card)?
- Is `rationale_verbatim` preserved exactly?
- Is `rationale_summary` a faithful compression?
- Are unknown experts correctly flagged for `experts.yaml` update?

Fix Curator prompt issues before the full run.

### Resumability

The script skips any comment whose Asana story gid is already in `expert_judgments.jsonl`. Safe to re-run after failure — it picks up where it left off. Safe to re-run post-meeting to capture new comments without duplicates.

## `port_pattern_provenance.py`

One-time port of existing `quality_patterns.md` entries to `PatternProvenance` seed records. Run once before the RLHF meeting to populate `state/pattern_provenance.jsonl`.

### Recommended run sequence

```bash
# Dry run first — see what would be emitted
python -m reflex.detect.scripts.port_pattern_provenance --dry-run

# If looks right, real run
python -m reflex.detect.scripts.port_pattern_provenance

# Verify:
wc -l services/reflex/detect/state/pattern_provenance.jsonl
# Expect ~30-40 records (one per Analytical Approach + Presentation Pattern)
```

### What to check after

- Every pattern with a "Discovered: Cycle X" tag got a non-null `created_cycle`
- Patterns referencing known experts (Dylan, Andrew, James, Anna) have those in `contributors`
- Patterns without attribution have empty `contributors` (expected for seed state)

### Do not re-run

This port is idempotent-by-intention-only. Re-running duplicates records. If edits are needed, truncate the log first:
```bash
> services/reflex/detect/state/pattern_provenance.jsonl
python -m reflex.detect.scripts.port_pattern_provenance
```
```

### PR description (PR #3)

```markdown
## Reflex — Seed corpora: judgments backfill + pattern provenance port (PR 3 of 5)

**Context:** Follows PR #2 (Curator + Skeptic emit structured records). Populates two seed
corpora from existing state so the RLHF meeting starts hot, not cold.

**Scope:**
- `scripts/backfill_expert_judgments.py` — runs Curator over all Hypotheses + Opportunities +
  Archived card comments from cycles 1-66. Idempotent, resumable, dry-run-capable.
- `scripts/port_pattern_provenance.py` — one-time port of existing `quality_patterns.md`
  entries to `PatternProvenance` seed records. Reconstructs cycle-of-origin and (where
  visible) contributor attribution.
- README with run protocols for both scripts.
- Summary stats dumped post-run (records by expert / type, unknowns flagged).

**What to expect:**
- ~50-100 `ExpertJudgment` records from cycles 1-66 comment history
- ~30-40 `PatternProvenance` records from current quality_patterns.md entries
- Unknown-expert IDs surface for `experts.yaml` updates
- Curator parsing quirks surfaced before the meeting generates live volume

**Reliability guardrails:**
- Backfill idempotent by source_ref (safe to re-run)
- Backfill gentle-rate-limited (0.5s between comments)
- Failures are per-comment; batch continues
- Port is intentional single-run (truncate + re-run if needed)

**Non-goals:**
- Automated pattern aggregation (later phase)
- Cross-card propagation resolution (Curator suggests; human acts)

Co-authored-by: James Li <jli@pinterest.com>
```

### Validation protocol (post-merge)

1. Dry run backfill against 3 cards (`--dry-run --max-cards 3`) — verify wiring
2. Bounded real backfill (`--max-cards 5`) — James spot-checks 10 records
3. Fix Curator bugs surfaced in spot check (likely 1-2 iterations)
4. Full backfill — 30-60 min depending on comment volume
5. Dry run provenance port — verify pattern count + attribution matches expectations
6. Real provenance port — one-shot
7. Summary stats dumped and reviewed
8. `experts.yaml` updated with any unknowns before the RLHF meeting

---

## PR #4 — Velocity baseline + dashboard CLI

### Goal
Compute the headline system-health number ("current median idea-to-launch: N days") from existing Asana card timestamps, and ship a dashboard CLI that reads all JSONL logs to print a single-pane summary. Gives James the numbers to show in the meeting.

### Scope
- `CycleTimeRecord` pydantic schema (scoped to velocity; only PR4 uses it)
- `scripts/compute_velocity_baseline.py` — reconstructs per-card stage timestamps from Asana metadata; writes baseline JSONL; prints summary
- `scripts/reflex_dashboard.py` — reads all state/ JSONL logs; prints consolidated stats
- Depends only on PR #1 being merged (can run parallel to PR #3)

### Files to create

#### 1. `services/reflex/detect/infra/schemas/cycle_time.py`

```python
"""CycleTimeRecord — per-card end-to-end timeline from idea to launch.

Stored in state/velocity/cycle_times.jsonl (baseline + live). Headline metric is the
median of `total_days` across completed cards. VelocityAgent (future) maintains this;
v1 seeds from Asana metadata via compute_velocity_baseline.py.
"""
from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

TerminalStage = Literal[
    "hypothesis",
    "opportunity",
    "skeptic_reviewed",
    "expert_approved",
    "canary_run",
    "implementation_pr",
    "experiment_running",
    "result_in",
    "learning_written",
]

TerminalReason = Literal[
    "killed_by_skeptic",
    "killed_by_expert",
    "killed_by_canary",
    "killed_in_ab_test",
    "shipped",
    "stuck_in_stage",
    "still_active",
]


class CycleTimeRecord(BaseModel):
    """End-to-end timeline for one card. Baseline records are reconstructed from Asana metadata."""

    card_gid: str
    card_title: str
    surface: list[str] = Field(default_factory=list)
    pillar: list[str] = Field(default_factory=list)
    stage_timestamps: dict[str, datetime] = Field(
        default_factory=dict,
        description="Keys match stage names: t0_hypothesis_created, t1_enriched_to_opportunity, "
        "t2_skeptic_verdict, t3_expert_approved, t4_offline_canary_start, "
        "t5_offline_canary_result, t6_implementation_pr_opened, t7_experiment_running, "
        "t8_result_in, t9_learning_written.",
    )
    terminal_stage: TerminalStage
    terminal_reason: TerminalReason | None = None
    total_days: float | None = Field(
        default=None, ge=0.0,
        description="t_terminal - t0 in days. Null if card still active.",
    )
    baseline: bool = Field(
        default=False,
        description="True if this record was reconstructed from Asana metadata "
        "(not observed in real time).",
    )
```

Add to `schemas/__init__.py`: `from .cycle_time import CycleTimeRecord, TerminalStage, TerminalReason`.

#### 2. `services/reflex/detect/scripts/compute_velocity_baseline.py`

```python
"""Reconstruct per-card cycle time baseline from Asana metadata.

For each card in Hypotheses + Opportunities + Archived sections, derive the stage
timestamps we can recover from Asana:

- t0_hypothesis_created: task.created_at
- t1_enriched_to_opportunity: section_changed story → Opportunities section
- t2_skeptic_verdict: NOT AVAILABLE pre-Skeptic (null for baseline)
- t3_expert_approved: Asana approval event or first non-agent comment with 'approve'/'lgtm'
  heuristic (best-effort; null if unclear)
- t4+: NOT AVAILABLE for baseline (Pinkerton canary + implementation agents are future)

For shipped cards, terminal_stage = 'shipped'. For archived, 'killed_by_expert' (default).
For still-active, terminal_stage matches current section; total_days = null.

Writes state/velocity/cycle_times_baseline.jsonl and prints summary.

Usage:
    python -m reflex.detect.scripts.compute_velocity_baseline --dry-run
    python -m reflex.detect.scripts.compute_velocity_baseline
"""
from __future__ import annotations

import argparse
import logging
import os
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from reflex.detect.infra.log_append import append_jsonl
from reflex.detect.infra.schemas import CycleTimeRecord

LOG = logging.getLogger(__name__)

BASELINE_LOG = (
    Path(__file__).resolve().parents[1] / "state" / "velocity" / "cycle_times_baseline.jsonl"
)

# Section GIDs — reuse env from backfill
SECTION_HYPOTHESES = os.environ.get("SECTION_HYPOTHESES_GID", "REPLACE_ME")
SECTION_OPPORTUNITIES = os.environ.get("SECTION_OPPORTUNITIES_GID", "REPLACE_ME")
SECTION_ARCHIVED = os.environ.get("SECTION_ARCHIVED_GID", "REPLACE_ME")

ASANA_TOKEN = os.environ["ASANA_TOKEN"]


def list_tasks_in_section(section_gid: str) -> list[dict[str, Any]]:
    """Reuse the helper from backfill script. Placeholder."""
    ...


def list_stories(task_gid: str) -> list[dict[str, Any]]:
    """Reuse. Returns all story events on the task."""
    ...


def first_section_move_to(stories: list[dict[str, Any]], target_section_gid: str) -> datetime | None:
    """Find the earliest story where the task was moved into target_section_gid."""
    for story in sorted(stories, key=lambda s: s["created_at"]):
        if (
            story.get("resource_subtype") == "section_changed"
            and story.get("new_section", {}).get("gid") == target_section_gid
        ):
            return datetime.fromisoformat(story["created_at"].replace("Z", "+00:00"))
    return None


def derive_record(task: dict[str, Any], current_section_gid: str) -> CycleTimeRecord:
    stories = list_stories(task["gid"])
    stamps: dict[str, datetime] = {}

    t0 = datetime.fromisoformat(task["created_at"].replace("Z", "+00:00"))
    stamps["t0_hypothesis_created"] = t0

    t1 = first_section_move_to(stories, SECTION_OPPORTUNITIES)
    if t1:
        stamps["t1_enriched_to_opportunity"] = t1

    # Determine terminal state
    if current_section_gid == SECTION_ARCHIVED:
        terminal_stage = "opportunity"
        terminal_reason = "killed_by_expert"
        terminal_time = datetime.fromisoformat(task["modified_at"].replace("Z", "+00:00"))
        total_days = (terminal_time - t0).total_seconds() / 86400
    elif current_section_gid == SECTION_OPPORTUNITIES:
        terminal_stage = "opportunity"
        terminal_reason = "still_active"
        total_days = None
    elif current_section_gid == SECTION_HYPOTHESES:
        terminal_stage = "hypothesis"
        terminal_reason = "still_active"
        total_days = None
    else:
        terminal_stage = "hypothesis"
        terminal_reason = "stuck_in_stage"
        total_days = None

    # Surface/pillar from tags — parse from task["tags"]
    surface = [t["name"] for t in task.get("tags", []) if t["name"].lower() in
               ("homefeed", "search", "related pins", "notifications", "landing pages")]
    pillar = [t["name"] for t in task.get("tags", []) if t["name"].startswith("pillar_")]

    return CycleTimeRecord(
        card_gid=task["gid"],
        card_title=task["name"],
        surface=surface,
        pillar=pillar,
        stage_timestamps=stamps,
        terminal_stage=terminal_stage,
        terminal_reason=terminal_reason,
        total_days=total_days,
        baseline=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--log-path", default=str(BASELINE_LOG))
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    all_records: list[CycleTimeRecord] = []

    for section_name, section_gid in (
        ("hypotheses", SECTION_HYPOTHESES),
        ("opportunities", SECTION_OPPORTUNITIES),
        ("archived", SECTION_ARCHIVED),
    ):
        LOG.info("Processing section: %s", section_name)
        for task in list_tasks_in_section(section_gid):
            record = derive_record(task, section_gid)
            all_records.append(record)
            if not args.dry_run:
                append_jsonl(Path(args.log_path), record)

    # Summary
    completed = [r for r in all_records if r.total_days is not None]
    if completed:
        durations = sorted(r.total_days for r in completed)
        median = statistics.median(durations)
        p75 = durations[int(0.75 * len(durations))]
        p95 = durations[int(0.95 * len(durations))]
        LOG.info(
            "BASELINE VELOCITY — completed=%d median=%.1fd p75=%.1fd p95=%.1fd",
            len(completed), median, p75, p95,
        )
    else:
        LOG.warning("No completed cards found — baseline velocity undefined yet.")

    LOG.info("Total records: %d (%d completed, %d active)",
             len(all_records), len(completed), len(all_records) - len(completed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

**Work-leo note:** this is a best-effort baseline. Many stage timestamps will be null (pre-Skeptic, pre-Pinkerton, pre-implementation-agents). The headline number is what's available: `t_terminal - t0` for completed cards. Expect median to be high (weeks-to-months) — that's the point. Improvement is the delta over time.

#### 3. `services/reflex/detect/scripts/reflex_dashboard.py`

```python
"""Consolidated stats over all state/ JSONL logs.

Prints a single pane James can screenshot or paste into Slack for the RLHF meeting.

Usage:
    python -m reflex.detect.scripts.reflex_dashboard
    python -m reflex.detect.scripts.reflex_dashboard --format json
"""
from __future__ import annotations

import argparse
import json
import logging
import statistics
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from reflex.detect.infra.log_append import iter_jsonl
from reflex.detect.infra.schemas import (
    CostLedgerEntry,
    CycleLogEntry,
    CycleTimeRecord,
    Disagreement,
    ExpertJudgment,
    PatternProvenance,
    SkepticVerdict,
)

STATE_DIR = Path(__file__).resolve().parents[1] / "state"


def _load_all():
    return {
        "judgments": list(iter_jsonl(STATE_DIR / "expert_judgments.jsonl", ExpertJudgment)),
        "disagreements": list(iter_jsonl(STATE_DIR / "disagreements.jsonl", Disagreement)),
        "verdicts": list(iter_jsonl(STATE_DIR / "verdict_log.jsonl", SkepticVerdict)),
        "costs": list(iter_jsonl(STATE_DIR / "cost_ledger.jsonl", CostLedgerEntry)),
        "cycles": list(iter_jsonl(STATE_DIR / "cycle_log.jsonl", CycleLogEntry)),
        "provenance": list(iter_jsonl(STATE_DIR / "pattern_provenance.jsonl", PatternProvenance)),
        "velocity_baseline": list(
            iter_jsonl(STATE_DIR / "velocity" / "cycle_times_baseline.jsonl", CycleTimeRecord)
        ),
    }


def build_report(data) -> dict[str, Any]:
    js = data["judgments"]
    vs = data["verdicts"]
    vb = data["velocity_baseline"]
    completed_vb = [r for r in vb if r.total_days is not None]

    return {
        "expert_labeling": {
            "total_judgments": len(js),
            "by_expert": dict(Counter(j.expert for j in js).most_common()),
            "by_type": dict(Counter(j.judgment_type for j in js).most_common()),
            "unknown_experts": sorted({j.expert for j in js if j.expert.startswith("unknown_")}),
            "cards_covered": len({j.card_gid for j in js}),
        },
        "disagreements": {
            "total": len(data["disagreements"]),
            "open": sum(1 for d in data["disagreements"] if d.resolution == "open"),
        },
        "skeptic": {
            "total_verdicts": len(vs),
            "by_verdict": dict(Counter(v.verdict for v in vs).most_common()),
            "avg_confidence": round(statistics.mean(v.confidence for v in vs), 3) if vs else None,
            "with_human_review": sum(1 for v in vs if v.human_reviewed),
            "human_agreement_rate": (
                round(
                    sum(1 for v in vs if v.human_agreed) /
                    max(1, sum(1 for v in vs if v.human_reviewed is not None)),
                    3,
                ) if any(v.human_reviewed is not None for v in vs) else None
            ),
        },
        "patterns": {
            "total": len(data["provenance"]),
            "with_contributors": sum(1 for p in data["provenance"] if p.contributors),
        },
        "cost": {
            "total_usd": round(sum(c.cost_usd for c in data["costs"]), 4),
            "by_agent": {
                a: round(sum(c.cost_usd for c in data["costs"] if c.agent == a), 4)
                for a in sorted({c.agent for c in data["costs"]})
            },
        },
        "cycles_completed": len(data["cycles"]),
        "velocity_baseline": (
            {
                "completed_cards": len(completed_vb),
                "median_days": round(statistics.median(r.total_days for r in completed_vb), 1),
                "p75_days": round(
                    sorted(r.total_days for r in completed_vb)[int(0.75 * len(completed_vb))], 1
                ),
                "p95_days": round(
                    sorted(r.total_days for r in completed_vb)[int(0.95 * len(completed_vb))], 1
                ),
            }
            if completed_vb
            else {"completed_cards": 0, "note": "No baseline data yet"}
        ),
    }


def format_text(report: dict[str, Any]) -> str:
    lines = ["=" * 60, "REFLEX DASHBOARD", "=" * 60]
    lines.append("")
    lines.append(f"Expert labeling — total judgments: {report['expert_labeling']['total_judgments']}")
    lines.append(f"  By expert: {report['expert_labeling']['by_expert']}")
    lines.append(f"  By type:   {report['expert_labeling']['by_type']}")
    lines.append(f"  Cards covered: {report['expert_labeling']['cards_covered']}")
    if report['expert_labeling']['unknown_experts']:
        lines.append(f"  ⚠  Unknown experts (update experts.yaml): "
                     f"{report['expert_labeling']['unknown_experts']}")
    lines.append("")
    lines.append(f"Disagreements: {report['disagreements']['total']} "
                 f"({report['disagreements']['open']} open)")
    lines.append("")
    lines.append(f"Skeptic — verdicts: {report['skeptic']['total_verdicts']}")
    lines.append(f"  Distribution: {report['skeptic']['by_verdict']}")
    lines.append(f"  Avg confidence: {report['skeptic']['avg_confidence']}")
    if report['skeptic']['human_agreement_rate'] is not None:
        lines.append(f"  Human agreement rate: {report['skeptic']['human_agreement_rate']}")
    lines.append("")
    lines.append(f"Patterns — total: {report['patterns']['total']} "
                 f"(with contributors: {report['patterns']['with_contributors']})")
    lines.append("")
    lines.append(f"Cost — total: ${report['cost']['total_usd']}")
    for agent, usd in report['cost']['by_agent'].items():
        lines.append(f"  {agent}: ${usd}")
    lines.append("")
    lines.append(f"Cycles completed: {report['cycles_completed']}")
    lines.append("")
    vb = report['velocity_baseline']
    if vb.get('completed_cards'):
        lines.append(f"BASELINE VELOCITY ({vb['completed_cards']} completed cards):")
        lines.append(f"  Median idea-to-launch: {vb['median_days']} days")
        lines.append(f"  P75: {vb['p75_days']} days")
        lines.append(f"  P95: {vb['p95_days']} days")
    else:
        lines.append("BASELINE VELOCITY: (no completed cards yet)")
    lines.append("=" * 60)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()

    data = _load_all()
    report = build_report(data)

    if args.format == "json":
        print(json.dumps(report, indent=2, default=str))
    else:
        print(format_text(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

#### 4. `services/reflex/detect/state/velocity/.gitkeep`
Ensures the velocity dir exists.

### Tests

Add `services/reflex/detect/tests/test_dashboard.py`:

```python
"""Smoke test: dashboard runs on empty logs without crashing."""
import subprocess


def test_dashboard_on_empty_state(tmp_path, monkeypatch):
    """Dashboard should print something meaningful even with no data."""
    # Point STATE_DIR at a temp empty dir — adjust implementation to allow env override.
    ...
```

(Work-leo: add a `--state-dir` override to the dashboard CLI for testability; include this test as the minimum safety.)

### PR description (PR #4)

```markdown
## Reflex — Velocity baseline + dashboard CLI (PR 4 of 5)

**Context:** Depends only on PR #1 (state schemas). Can land in parallel with PRs #2-3.
Produces the headline number for the RLHF meeting: "current baseline median idea-to-launch: N days."

**Scope:**
- `CycleTimeRecord` pydantic schema (velocity-specific; PR #1 schemas stay focused)
- `scripts/compute_velocity_baseline.py` — reconstructs per-card stage timestamps from Asana
  metadata (task.created_at, section_changed stories, modified_at). Writes
  `state/velocity/cycle_times_baseline.jsonl`.
- `scripts/reflex_dashboard.py` — reads all state/ JSONL logs; prints consolidated stats
  (judgments by expert/type, disagreements, Skeptic verdicts, cost totals, cycles, velocity).
  Supports text + JSON output formats.

**What this enables:**
- James walks into the RLHF meeting with a current baseline velocity number
- Dashboard CLI gives a single-pane-of-glass view for live status
- Foundation for future `VelocityAgent` that passively maintains cycle_times.jsonl

**Reliability guardrails:**
- Dashboard safe on empty logs (prints zeros/no-data notes, doesn't crash)
- Baseline computation is best-effort — missing stage timestamps are null, not invented
- Records flagged `baseline: True` to distinguish from live-captured records

**Non-goals:**
- Full VelocityAgent (future — reads from live agent runs, not just Asana backfill)
- Time-series trend analysis (v1 is single snapshot)

Co-authored-by: James Li <jli@pinterest.com>
```

### Validation

1. `python -m reflex.detect.scripts.reflex_dashboard` runs on empty state, prints sensible zeros
2. `python -m reflex.detect.scripts.compute_velocity_baseline --dry-run` runs, prints summary
3. Real run writes `state/velocity/cycle_times_baseline.jsonl` with expected card count
4. Dashboard after backfill + baseline shows populated stats

---

## PR #5 — Pre-meeting Skeptic run against top N cards (stretch)

### Goal
Generate 10 fresh `SkepticVerdict` records on top Opportunity cards so James walks into the RLHF meeting with structured discussion material. Each verdict is per-check, pattern-cited, and discrete — experts can disagree on specific checks rather than vague card-level opinions.

**Dependency:** requires PRs #1 + #2 merged AND Skeptic validated as stable on real cards. If Skeptic has any teething issues on Sunday evening, park this PR — don't burn meeting prep time debugging.

### Scope
- `scripts/run_skeptic_on_top_cards.py` — selects top N cards, invokes Skeptic on each, relies on Skeptic's PR #2 emission to write verdicts
- No new schemas (all from PR #1)

### Files to create

#### 1. `services/reflex/detect/scripts/run_skeptic_on_top_cards.py`

```python
"""Run Skeptic against the top N Opportunity cards for pre-meeting review.

Selection: by composite score (parsed from card html_notes per opportunity_card.md schema).
Top 10 by default. Each invocation writes one SkepticVerdict to state/verdict_log.jsonl
via the Skeptic's own CLI (from PR #2).

Intended as a one-shot pre-meeting seed run — NOT a production cron. For ongoing Skeptic
operation, Reflex's normal cycle runs the Skeptic.

Usage:
    python -m reflex.detect.scripts.run_skeptic_on_top_cards --dry-run --top 3
    python -m reflex.detect.scripts.run_skeptic_on_top_cards --top 10
"""
from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

LOG = logging.getLogger(__name__)

SECTION_OPPORTUNITIES = os.environ.get("SECTION_OPPORTUNITIES_GID", "REPLACE_ME")
ASANA_TOKEN = os.environ["ASANA_TOKEN"]

# Composite score line parser — matches existing DS Agent format:
# "Impact: X · Feasibility: X · Alignment: X · Composite: X.X"
COMPOSITE_PATTERN = re.compile(r"Composite:\s*([\d.]+)", re.IGNORECASE)


def list_tasks_in_section(section_gid: str) -> list[dict[str, Any]]:
    """Reuse helper."""
    ...


def fetch_task_full(task_gid: str) -> dict[str, Any]:
    """GET /tasks/{gid} — returns full task with html_notes."""
    ...


def parse_composite(html_notes: str) -> float:
    """Extract composite score from opportunity card body. 0.0 if missing."""
    m = COMPOSITE_PATTERN.search(html_notes or "")
    return float(m.group(1)) if m else 0.0


def invoke_skeptic_on_card(card: dict[str, Any], dry_run: bool) -> None:
    """Hand the card to the Skeptic agent.

    Skeptic's prompt (from PR #2) knows to emit SkepticVerdict via CLI.
    This function just sets up the invocation.
    """
    if dry_run:
        LOG.info("DRY RUN: would invoke Skeptic on %s (%s)", card["gid"], card["name"])
        return
    # Actual invocation — mirror however Reflex invokes agents today.
    # Pseudo-code:
    #     run_agent("skeptic", input={
    #         "mode": "pre_meeting_seed",
    #         "card_gid": card["gid"],
    #         "card_title": card["name"],
    #         "card_html_notes": card["html_notes"],
    #     })
    raise NotImplementedError("Wire to work-leo's agent runner.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--top", type=int, default=10, help="Number of top cards to review.")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    LOG.info("Listing tasks in Opportunities...")
    tasks = list_tasks_in_section(SECTION_OPPORTUNITIES)
    LOG.info("Fetching full bodies for scoring (%d cards)...", len(tasks))

    scored: list[tuple[float, dict[str, Any]]] = []
    for t in tasks:
        full = fetch_task_full(t["gid"])
        score = parse_composite(full.get("html_notes", ""))
        scored.append((score, full))

    scored.sort(key=lambda x: x[0], reverse=True)
    top_cards = [t for _, t in scored[: args.top]]
    LOG.info("Selected top %d cards (scores: %s)",
             len(top_cards), [round(s, 2) for s, _ in scored[: args.top]])

    for card in top_cards:
        try:
            invoke_skeptic_on_card(card, args.dry_run)
            time.sleep(1.0)
        except Exception as exc:
            LOG.exception("Skeptic failed on card %s: %s", card["gid"], exc)

    LOG.info("Done. Check state/verdict_log.jsonl for emitted verdicts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### Validation

1. Dry run with `--top 3` — verify wiring + card selection
2. Real run with `--top 3` — verify 3 SkepticVerdicts land in `state/verdict_log.jsonl`, all fields populated, all 5 checks present
3. If any verdict looks wrong or Skeptic crashes, **stop and park PR #5**. Report to James.
4. If first 3 look clean, proceed with `--top 10`
5. After completion: eyeball all 10 verdicts. James will discuss these with experts at the meeting.

### PR description (PR #5)

```markdown
## Reflex — Pre-meeting Skeptic seed run on top 10 Opportunity cards (PR 5 of 5, stretch)

**Context:** Depends on PRs #1 + #2 merged AND Skeptic validated as stable. One-shot
seed run that gives James 10 structured Skeptic verdicts to bring to the RLHF meeting.

**Scope:**
- `scripts/run_skeptic_on_top_cards.py` — selects top N Opportunity cards by composite
  score and invokes Skeptic on each
- No new schemas or CLIs — all from PR #1
- Intended as pre-meeting one-shot, not a production cron

**Meeting impact:**
- Experts can discuss specific Skeptic checks (pattern/context/evidence/consistency/novelty)
  rather than vague card-level opinions
- Structured disagreements auto-surface during discussion
- Skeptic's first real test run produces the first precision/recall signal

**Reliability guardrails:**
- Dry-run mode with `--top N` for incremental validation
- Stops on crash per card (doesn't halt batch)
- 1s pacing between cards

**If this PR is paused:** The meeting still benefits from PRs #1-4. The dashboard shows
judgment volume + baseline velocity — the headline framing remains intact.

Co-authored-by: James Li <jli@pinterest.com>
```

---

## Combined timing target

| PR | Purpose | Dep | Est. code | Est. review |
|---|---|---|---|---|
| PR #1 | State primitives (6 schemas + CLIs + tests) | — | 5h | 1h |
| PR #2 | Curator + Skeptic emit typed records | #1 | 3h | 1h |
| PR #3 | Backfill + provenance seed | #2 | 5h | 1h |
| PR #4 | Velocity baseline + dashboard | #1 | 4h | 1h |
| PR #5 | Pre-meeting Skeptic seed run | #1+#2 | 2h | 1h |
| **Total** | | | **19h** | **5h** |

36-hour window. Fits if work-leo runs mostly continuously and CI is fast. Critical path = #1 → #2 → #3; #4 runs parallel; #5 stretch.

## Risks + mitigations

| Risk | Mitigation |
|---|---|
| Review throughput — 5 PRs stacked | Stack as feature branches; reviewers see chain; PRs 1-4 are all in new directories (no existing code collision), so James can self-merge with cc-for-awareness if Andrew's review slips |
| PR #1 becomes the bottleneck for everything downstream | If needed, split PR #1a (ExpertJudgment + Disagreement + CLIs, critical path) and PR #1b (the other 4 schemas + CLIs, parallel). Downstream only needs 1a |
| Skeptic instability blocks PR #5 | Park PR #5 if first dry-run surfaces issues. Meeting still works with PRs 1-4 |
| Claude Code rate limit (7pm PT reset) on work-leo | Preserve intermediate outputs before backfill runs; checkpoint state after each PR merges |
| Asana API rate limits on backfill + baseline scripts | Both scripts have 0.5-1s pacing. Fall back to smaller --max-cards windows if 429s surface |
| CycleTimeRecord baseline is mostly null | Expected — that's the whole point. Even partial timestamps give a headline median for completed cards |

---

## Summary — what to paste into work-leo

Paste this entire file into a fresh work-leo session on the work mac. work-leo should:

1. Confirm the Curator/Skeptic agent-definition PR is merged (prerequisite)
2. Scaffold branches `reflex-pr1-state-primitives` through `reflex-pr5-skeptic-seed`
3. Implement PRs in dependency order:
   - PR #1 (alone on critical path, ~5h)
   - PR #2 + PR #4 in parallel once #1 merges (~3h + ~4h)
   - PR #3 once #2 merges (~5h)
   - PR #5 only after #2 merges AND Skeptic passes a dry run (~2h)
4. Run validation for each PR before opening (all tests green)
5. After all PRs land:
   - Run backfill (`--dry-run` → `--max-cards 5` → spot check → full)
   - Run provenance port (`--dry-run` → real)
   - Run velocity baseline
   - Run dashboard — screenshot the output
   - If PR #5 landed: run Skeptic seed against top 10 cards
6. Update `infra/experts.yaml` with unknowns surfaced
7. Report back: final dashboard output + total time spent + any parking decisions

**Report for the next Leo session (Monday morning):**
- Dashboard screenshot (text format is fine)
- PR merge sequence + any deviations
- Parsing quirks surfaced + how resolved
- Unknown experts added to `experts.yaml`
- Any `claim_targeted` recurrences across cards (cross-card propagation signal)
- Baseline velocity numbers (median, p75, p95)
- Skeptic verdict distribution from PR #5 (if landed)

These inform Monday's meeting prep and the next Leo design cycle.

---

## Post-meeting capture notes

After the RLHF meeting, the Curator can be re-run to capture comments experts leave on cards during/after the meeting. The system is idempotent by `source_ref`, so re-running is safe. This converts meeting-generated commentary into structured judgments automatically — assuming experts leave comments on Asana cards (not just verbal discussion).

For verbal-only discussion, a post-meeting practice: James (or designated scribe) writes structured notes as Asana comments, tagged with the expert who made each point. Curator picks these up in the next run.

Future enhancement: a `capture_meeting_notes.py` script that takes meeting-notes prose + attendance list and emits direct `ExpertJudgment` records with `source: "meeting"` — bypassing the Asana round-trip. v2 work.
