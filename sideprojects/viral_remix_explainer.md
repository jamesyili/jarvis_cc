# Viral Remix — Codebase Explainer

**Date:** 2026-04-18
**Context:** Plain-English walkthrough of every architectural and tooling decision made in the Step 1 scaffold of `viral_pivot` (the viral-remix pipeline). Written for a reader without strong backend background.

**Related docs:**
- `viral_pivot/docs/codebase-sequencing.md` — the build sequencing plan
- `viral_pivot/docs/gaps.md` — adversarial review findings
- `viral_pivot/docs/decisions/0001-initial-architecture.md` — the 11 decisions (D1–D11) distilled as ADR

---

## 1. How the folders are organized

**`src/viral_remix/` instead of a flat layout.** Python projects historically dumped code next to tests and config. The "src layout" puts all importable code in `src/` so tests can't accidentally pick up local files — they have to go through the real install path, same as a production user would. Catches a class of "works on my machine" bugs.

**Subsystems as folders (scrapers, extraction, annotation, db, retrieval, generation, stitch, publish).** One folder per pipeline stage, matching the blueprint. Anyone asking "where does YouTube scraping live?" can guess in one try.

**`core/` is the shared spine.** `models.py` (data shapes), `guardrails.py` (the rules every video must follow), `costs.py` (spend tracking), `selection.py` (picking clips). Everything else imports from `core/`. One source of truth.

**`_bridge/` is a waiting room.** When we copy a file from the Rekko codebase that still has `from rekko_server` imports in it, it lands in `_bridge/` first. CI flags it. We clean it up in the next PR. Prevents "I'll fix the imports later" rot.

**`docs/` holds everything written, not just user guides.** Planning docs, architecture decisions (ADRs), session logs, competitor research — all in one tree so nothing gets lost across scattered folders.

**`data/` is gitignored.** Video files are big (GB scale). Git doesn't handle them well. The `.gitkeep` trick keeps the empty directory in git but nothing inside it.

## 2. Python 3.12

Python 3.11 and 3.12 added major speed improvements and better error messages. Anything older (3.10, 3.9) means slower runs and weaker type syntax. Pinned via `.python-version` so everyone's machine uses the same version — prevents "works on my 3.11 breaks on my 3.12" surprises.

## 3. `uv` as the package manager

Python's classic package tool (`pip`) has two problems: (a) no lock file by default, so you can install the same `requirements.txt` twice and get different versions; (b) it's slow.

`uv` is a new Rust-written replacement. It's 10–100× faster and it always locks. `uv.lock` records the exact version of every dependency, down to transitive ones. Committed to git — anyone cloning gets identical packages.

**"Extras" are optional dependency groups.** The `pyproject.toml` defines groups like `pipeline` (LLM SDKs), `scraping` (YouTube + yt-dlp), `extract` (video processing), `db` (Postgres stuff), `tts`, `ui`, `dev`. You install what you need: `uv sync --all-extras` for local dev, just `uv sync` if you're running a narrow slice. Keeps the "just use this code" install light.

## 4. Pydantic v2 for everything that holds data

Pydantic is a library that makes Python classes validate themselves. Instead of `{"name": "foo", "age": 30}` being a loose dict that could have typos, you declare a `class Person(BaseModel): name: str; age: int`. If someone tries to create one with `age="thirty"`, it errors loudly.

I use it for every data shape — the `Clip` model, the `ClipAnnotation`, the `VideoScript`, etc. Benefits:
- Schema is code, not documentation that drifts
- Automatic JSON serialization + deserialization (critical for API calls + file writes)
- Editor autocomplete knows every field
- Prevents bad data from sneaking between pipeline stages

`pydantic-ai` builds on this for LLM calls — you tell it "the answer should be a `ClipAnnotation`" and it'll retry the model until it gets one that parses.

## 5. Ruff (linter + formatter) and Mypy (type checker)

**Ruff** catches stylistic and correctness issues — unused imports, mismatched quotes, obviously wrong code patterns. It also formats code so nobody argues about spacing. It replaces 5+ older tools with one fast one.

**Mypy in strict mode** checks that types match. If `commentary_ratio()` takes two lists of floats and you pass it a string, mypy fails *before* the code runs. Strict mode is aggressive — every function needs type hints; no `Any` escape hatch without an explicit opt-in.

These are "cheap insurance" — they run in a second and catch a meaningful chunk of bugs that would otherwise surface in production.

## 6. Pytest + test tiers

**Pytest** is the standard Python test runner. `asyncio_mode = "auto"` means async tests (which we need because we talk to LLMs, HTTP APIs, and databases) don't need special decorators.

**Three test tiers:**
- **Default** (`uv run pytest`) — runs instantly with fake APIs mocked out. No network, no secrets needed. This is what CI runs on every PR.
- **Live** (`uv run pytest -m live`) — actually calls OpenAI, Gemini, ElevenLabs. Costs money. Only runs on demand.
- **Slow** (`uv run pytest -m slow`) — full integration tests that spin up Postgres or render a Remotion video. Nightly only.

Why three tiers? If every PR ran real API calls, CI would cost $ and take 20 minutes. If CI only ran mocked tests, real API breakage wouldn't be caught until too late. Three tiers = fast feedback by default, safety net on demand.

## 7. Logfire for observability

When the pipeline runs — scraping, annotating 1000 clips, rendering a video — you want a trace of what happened: which calls succeeded, which retried, which failed, how long each step took, how much it cost. `logfire` is Pydantic's observability tool. One line to set up; instruments `httpx` (HTTP calls) and `pydantic-ai` (LLM calls) automatically. Production issues become diagnosable instead of mysterious.

## 8. Storage choices

**Postgres + pgvector (not SQLite).** Postgres is the industrial-strength relational database. `pgvector` is a plugin that teaches Postgres about vectors (the 1536-number arrays that represent a clip's meaning). We can query "find the 10 clips most similar to this query" in SQL. At our MVP scale (~10K clips) SQLite + its vector plugin would also work, but Postgres scales further and has more ops tooling. Rekko used SQLite; we're not porting that because our schema is different anyway.

**OpenAI embeddings, not a local model.** An "embedding" is a math trick that turns text into a point in high-dimensional space, where similar meanings sit close together. OpenAI's `text-embedding-3-small` is $0.02 per million tokens — effectively free at our scale — and produces higher-quality vectors than the free local model Rekko uses. At larger scale I'd reconsider, but right now the quality win is free.

**JSONL for the cost ledger, not a database.** `data/costs/ledger.jsonl` is just one JSON object per line, appended as things happen. For a cost log — append-only, low-volume, read occasionally — a file is simpler than a database table. If the ledger gets huge we can move it to Postgres without changing the interface.

**Local filesystem for raw videos + clips, not S3.** At MVP scale (~20GB) that's cheaper and faster than cloud storage. If we get to 100K clips (Phase 2) we switch to S3. Design decision: don't solve Phase 2 problems with Phase 1 work.

## 9. Key architectural modules (the "why these exist")

**`core/guardrails.py` — one implementation of the rules.** Every video must have commentary-to-clip ratio ≥ 2.0 (ideally 2.2 with safety margin). Every clip must be 3–5 seconds. The script generator checks the ratio, the renderer re-checks it, the QC step checks it again. If each step had its own check, they'd drift apart over time (someone tweaks one but forgets the others). Having one module everyone imports prevents drift.

**`core/costs.py` — tag every paid call with a `run_id`.** When we render one video, it hits several APIs (VLM, embeddings, TTS, maybe Remotion cloud later). The `run_id` is the video's unique identifier. Every API call records `(run_id, step, $)`. Then we can ask "what did video #42 cost total? What step was most expensive?" without reverse-engineering logs. `budget guard` raises an exception if a batch runs past its ceiling — prevents a bug from burning $100 while we're not watching.

**`core/selection.py` — fail loud, never quiet.** When the retrieval system returns top-10 clips for a script beat, we have to pick one. Easy to write "pick the first one" and move on. But if all 10 are bad matches, we'd publish a video with wrong clips and not notice until it's live. The design choice: if no clip above a similarity threshold survives the filters (not already used, not recently used), raise `NoMatchError`. The operator sees the failure and decides — regenerate the script, widen the search, or abort. **Silent degradation is the #1 way quality-sensitive pipelines rot.**

**`core/models.py` — `RenderProps` is beat-shaped, not section-shaped.** Rekko's Remotion composition hard-codes 5 sections (hook, context, evidence, reveal, CTA) because it's a prediction-market explainer format. Our videos have a variable number of beats determined by the script. So `RenderProps` has `beats: list[BeatRenderProps]` — a list that can be any length. This is why Step 9 can't be a straight port from Rekko.

## 10. Workflow mechanisms

**Port-hygiene script (`scripts/port-hygiene.sh`).** When we copy code from the Rekko codebase, leftover imports and domain terms (`kalshi`, `polymarket`, `market_key`) can sneak in. A grep in CI fails the build if any forbidden string lands in `src/`. Cheap mechanical enforcement of a rule that humans would otherwise forget.

**ADRs (`docs/decisions/0001-*.md`).** "Architecture Decision Records" are short markdown files capturing *why* a non-obvious choice was made. Someone joining the project six months later can read them instead of asking "why Postgres and not SQLite?" They're append-only — if a decision gets overturned, you write a new ADR that supersedes the old one, not edit the old one. The git-blame of decisions.

**Session logs (`docs/session-logs/YYYY-MM-DD.md`).** One file per working day: what got done, what was decided, what's next. Bridges the gap between commit messages (too granular) and a full roadmap (too coarse). Matters more than it sounds — your own memory of "what did I do last Tuesday?" decays fast.

**Branch-per-step (`step-N-slug`).** Every sequencing step gets its own git branch. PRs to `main`. CI gates the merge. Squash-merge produces a clean commit history where each commit = one step done. Easier to rollback, easier to bisect regressions. `main` is always green.

## 11. Settings design

**`pydantic-settings` reads config from environment variables.** Instead of hard-coding API keys or model names, they come from `.env` (local) or GitHub Actions secrets (CI) or env vars (prod). Changing the embedding model from `text-embedding-3-small` to `text-embedding-3-large` is `VIRAL_REMIX_EMBEDDING_MODEL=text-embedding-3-large` — no code change.

**`SecretStr` for keys.** If an API key accidentally gets logged or printed, `SecretStr` prints `**********` instead of the actual key. Tiny safety net that's saved a lot of people from leaking credentials into error reports.

**`get_settings()` is a function, not a global.** In tests, we need to override the settings (fake API keys, test database URL). A function is easy to patch; a module-level global is hard to swap without breaking imports. Small detail, but pays off the first time you write a test.

---

## Candidates to defer if over-built feels real

Things I'd keep as-is but could live without at MVP:

- **Logfire** — can start with `print` statements; wire up when debugging gets painful.
- **Mypy strict** — mypy loose is fine at MVP scale; strict pays off when the team grows.
- **ADRs + session logs** — overhead until you've made your first "wait, why did we do it this way?" decision.

Everything else I'd defend as "cheaper now than later."

---

## 12. Testing — the three-tier pyramid

Added after Steps 1-3 landed. Three tiers separated by pytest markers; each catches bugs the tier above can't see.

```
Tier          Runs              Catches                                 Cost
────────────  ────────────────  ──────────────────────────────────────  ──────
default       mocked units      logic bugs, type errors, bad imports    free
  ↓
slow          real tools        wrong ffmpeg flags, PySceneDetect       disk + time
                                 drift, Whisper load failures
  ↓
live          real API calls    YouTube shape changes, yt-dlp           quota/$
                                 breakage, auth/quota issues
```

**Why tiers at all?** If every PR ran real API calls + real ffmpeg, CI would cost money and take 20 minutes. If CI only ran mocked tests, real-world breakage (YouTube changing their API) wouldn't surface until you tried to actually ingest. Tiers let you pick your trade-off per context: fast during dev, thorough before merge, live in nightly.

### What each tier catches

- **Default** (131 tests, <1s): pure logic. Mocks stand in for every external dep. Runs on every PR.
- **Slow** (16 tests, ~30s first run): real `ffmpeg`, real `PySceneDetect`, real `faster-whisper`. The mocked tests pass happily even if your `ffmpeg` command-line has a typo — the mock doesn't care. Slow tests find those.
- **Live** (2 tests, ~10s): real YouTube Data API, real `yt-dlp`. Catches quarterly-ish upstream breakages that nothing else can.

### Synthetic video fixtures (the neat trick)

The slow tests need real video files to feed real ffmpeg. Instead of committing binary `.mp4` fixtures to git (slow clones, merge conflicts, no reproducibility), we generate them on session start with `ffmpeg`'s built-in `lavfi` filter:

- **`synthetic_mp4`** — 5 seconds of test pattern + 1kHz tone. For "does ffmpeg work?" tests.
- **`synthetic_mp4_with_cuts`** — 9 seconds, four solid-color segments (red → blue → green → yellow) glued together. The sharp color changes are more detectable than any real shot cut, so this is what we use to validate `PySceneDetect`.
- **`synthetic_silent_mp4`** — 3 silent seconds. For the Whisper-on-silence edge case.

If `ffmpeg` isn't installed, all slow tests **skip** cleanly — never fail mysteriously.

### `scripts/dev-smoke.sh` — the eyeball-level check

Tests say "the assertion passed." The smoke script says "here are the actual files it produced; go look at them."

```bash
scripts/dev-smoke.sh 2    # ingest 2 YT Shorts, segment them into clips
# → data/raw/{today}/*.mp4
# → data/clips/{id}/*.mp4 + data/keyframes/{id}/*.jpg
# → data/raw/manifest.jsonl, data/clips/manifest.jsonl
```

This is the bridge between "tests pass" and "the pipeline works." Useful for the class of bugs where the code is technically correct but the *output* is bad (e.g., keyframes are black, clips have glitchy audio, scene detection fires on every frame).

### Decision tree for what to run when

| Situation | Command |
|---|---|
| Writing code, want fast feedback | `uv run pytest` |
| Before merging a PR that touches ffmpeg/PySceneDetect/Whisper | `uv run pytest -m slow` |
| Before merging a PR that touches scraper/publish code | `uv run pytest -m live` (needs `.env`) |
| Nightly CI / pre-release sanity check | `uv run pytest -m "live or slow"` |
| "Did we break anything real?" | `scripts/dev-smoke.sh 2` |

---

## 13. Why the pipeline has three "manifests"

Each pipeline stage writes its output to a JSONL file called a manifest. You end up with:

- `data/raw/manifest.jsonl` — one line per ingested YouTube Short (Step 2)
- `data/clips/manifest.jsonl` — one line per extracted 3-5s clip (Step 3)
- (future) `data/annotations/manifest.jsonl` — one line per VLM-annotated clip (Step 4)

**Why three files, not one DB?** A few reasons:

1. **Filesystem is simpler than Postgres.** At MVP scale (~1K clips), a flat file is easier to debug, back up, and grep through than a database table.
2. **Stage-at-a-time dedupe.** Each stage's manifest lets it answer "did I already process this?" on startup without loading the entire DB.
3. **Postgres ingests these later (Step 5).** The manifests stay as the source of truth on the filesystem; the DB is an index built from them. If the DB gets corrupted, replay from manifests.

The three manifest classes (`Manifest`, `ClipManifest`, `AnnotationManifest`) are nearly identical in shape. At some point we'll DRY them into a generic `JsonlManifest[T]` — I held off because premature abstraction hurts more than three near-duplicates until a fourth shows up.

---

## 14. Step 4 — VLM annotation (what each clip "means")

**What a VLM is.** A Vision-Language Model reads both images and text and produces text. Gemini Flash, GPT-4o, Claude Opus — all VLMs. We send it 3 keyframes + an audio transcript and ask "what's in this clip?" It gives us back a structured answer: scene description, named celebrities, emotion, setting, objects, brands, and a one-line "semantic caption" that we'll later search over.

### `VlmAnnotation` vs `ClipAnnotation` — the "who owns what" split

When we ask the VLM to describe a clip, we only want it describing what it *saw*. We don't want it deciding:
- its own `annotator_model` field ("I am gemini-2.0-flash")
- the `prompt_version` we used to ask it
- when we did the asking (`annotated_at`)
- what `clip_id` we're tracking this under

These are facts the *pipeline* owns. If we let the VLM fill them in, it might hallucinate its own model name, drift prompt version over time, or leak secrets into outputs.

Fix: two classes. `VlmAnnotation` is the narrow shape the VLM fills in. Our code then wraps that into the full `ClipAnnotation` with the system-owned fields attached by us. The boundary is tight and the VLM can't accidentally trample identity fields.

This is a general pattern: **when letting an LLM produce structured output, carve the schema down to just the model's job.** Everything else gets attached by the caller.

### `pydantic-ai` structured output

`pydantic-ai` wraps model calls with typed output. Instead of getting back raw JSON we have to parse:

```python
agent = Agent("google-gla:gemini-2.0-flash-exp", output_type=VlmAnnotation)
result = await agent.run([keyframe1, keyframe2, keyframe3, prompt_text])
vlm: VlmAnnotation = result.output   # parsed, validated, typed
```

If the model returns malformed JSON, `pydantic-ai` retries automatically. If after retries it still can't produce a valid `VlmAnnotation`, we get a clean exception — not a silent bad row.

### The budget guard — teeth, not trim

The annotator is the pipeline's first place where calls cost real money. Gemini Flash is cheap (~$0.0002 per clip), but a bug loop or prompt injection could burn through quota in minutes.

Two defenses:
1. `core/costs.CostLedger.guard(run_id, ceiling)` — raises `BudgetExceeded` if accumulated spend on this run has crossed a ceiling. Checked *before* each call, not after.
2. `asyncio.Event` propagates the halt signal — once one task hits the ceiling, every other in-flight task sees the event and short-circuits. No new calls dispatch.

**Caveat:** tasks already dispatched finish. If concurrency is 10 and the ceiling trips, you might see up to ~10 extra calls complete before the halt. That's acceptable slop for a guardrail — we trade exact-stop for simpler code. For an accountant-level budget cap, we'd need a queue-based pattern that checks the ledger between each dispatch.

### Concurrency via `asyncio.Semaphore`

Gemini Flash has rate limits (~60 RPM on free tier). Running 100 annotations serially at ~1s each takes 100 seconds; running all 100 in parallel slams the rate limit. A semaphore caps in-flight calls at N (default 10):

```python
sem = asyncio.Semaphore(10)
async def one(clip):
    async with sem:  # wait for a free slot
        await annotate_clip(clip)

await asyncio.gather(*[one(c) for c in clips])  # 100 tasks, 10 run at a time
```

This is a standard pattern. The semaphore is "the bouncer at the rate-limit club."

### Prompt versioning

Every annotation row has a `prompt_version` column (`v1` right now). When the prompt in `prompts/annotate_clip.md` changes materially, we bump the version. Step 5's ingest notices rows with old versions and can re-annotate only those — no need to wipe the whole table.

This is cheap to set up and saves a lot of pain when you realize the prompt was subtly wrong and need to regenerate annotations. **Prompts are config, and config changes benefit from version tracking, same as code.**

---

## 15. Step 5 — Postgres + pgvector + embeddings

Where the pipeline grows a real database. Up to now everything lived in JSONL files. Those are fine until you need to answer queries like "find the 10 clips most similar to 'Taylor Swift red carpet.'" For that you need vectors, an index, and a DB.

### SQLAlchemy ORM (alongside Pydantic — not instead of)

Pydantic models describe data in *motion* — what enters and leaves the system. SQLAlchemy ORM models describe data at *rest* — how it sits in Postgres tables. They're related but separate concerns.

Example: our Pydantic `Clip` has `keyframe_paths: list[Path]`. Postgres doesn't have a `Path` type; it has `TEXT[]` (text array). So the ORM class stores them as strings and has helpers to convert at the boundary:

```python
class ClipORM(Base):
    keyframe_paths: Mapped[list[str]] = mapped_column(ARRAY(Text))
    
    @classmethod
    def from_pydantic(cls, clip: Clip) -> ClipORM:
        return cls(keyframe_paths=[str(p) for p in clip.keyframe_paths], ...)
    
    def to_pydantic(self) -> Clip:
        return Clip(keyframe_paths=[Path(s) for s in self.keyframe_paths], ...)
```

The payoff: the rest of the codebase never sees ORM objects or SQL. Services work with Pydantic models. The conversion is a thin layer at the DB edge.

### Alembic migrations

When you change the schema (add a column, drop a table), you need a way to apply that change to every environment — dev, CI, production — without losing data. Alembic is Python's standard migration tool. Each change is a Python file in `alembic/versions/` that defines `upgrade()` and `downgrade()`. Running `alembic upgrade head` applies all pending migrations in order.

Our initial migration (`0001_initial.py`) creates four tables, enables the `pgvector` extension, and builds the cosine-similarity index. Future changes — adding a column, tightening a constraint — get their own revision file.

This pays off when you deploy to multiple environments or want to roll back a schema change. For a solo local project it's mild overhead; for anything that ever sees a production-like deploy it's essential.

### pgvector and cosine similarity

`pgvector` is a Postgres extension that adds a `VECTOR(N)` column type and distance operators. Our `embeddings` table stores one 1536-dimensional vector per clip. To find similar clips:

```sql
SELECT clip_id FROM embeddings
ORDER BY vector <=> '[0.1, 0.2, ...]'   -- <=> is cosine distance
LIMIT 10;
```

Without an index this is a full scan — fine for 1K rows, slow at 100K. So we build an `ivfflat` index: Postgres clusters similar vectors together ahead of time, then a query only needs to search the relevant cluster(s). `lists=100` means 100 clusters — a standard starting point for <100K rows. At larger scale we rebuild with more lists.

`ivfflat` is approximate — it might miss a vector that's close but sits in a different cluster. For MVP retrieval that's fine. If we ever need exact results, there's a more expensive `hnsw` index available.

### The two-phase ingest

Ingesting the three manifests and then computing embeddings is **not** one transaction. Here's why:

1. Transaction 1: upsert source_videos → clips → annotations. Commit.
2. Query: "which annotations don't have an embedding under the current model?" This query only sees rows that are *committed*. If step 1 and the query were in the same transaction, the query would see the new annotations as "not yet embedded" — which is true but trivially so. Two transactions is also the natural unit for *retry*: if the OpenAI call fails mid-batch, step 1's data is safe.
3. Call OpenAI to embed the gap.
4. Transaction 2: insert the new embedding rows. Commit.

**The separation is about dependency, not style.** Step 2's query needs committed data from step 1 to be meaningful.

### Re-embedding detection (parallel to prompt versioning)

Every `embeddings` row carries an `embedding_model` column. When we switch to a different embedding model — say, OpenAI bumps from `-3-small` to `-4-small` — the ingest query looks for clips that lack an embedding *under the new model name*, not lacking an embedding at all. It will find every clip (none have the new model yet) and re-embed them.

Meanwhile, the old rows sit there untouched so we can roll back if the new model turns out to be worse. Eventually we prune old-model rows once we're confident in the new one.

Same pattern, different column, as prompt versioning on annotations. The recipe: **version the thing that produces the output, and let the ingest decide what to refresh.**

### testcontainers — real Postgres in CI

Unit tests mock the database. But mocked SQL is a theory, not a fact. Our `slow` tier spins up an actual Postgres container (with pgvector already installed, via `pgvector/pgvector:pg16`) in Docker, runs the migration, does a real ingest, runs a real cosine query. The container starts in ~3 seconds and is torn down at the end of the test session.

This catches:
- Schema bugs the ORM definition would pass but real Postgres rejects.
- pgvector extension/indexing mistakes.
- FK cascade surprises when you delete a parent row.
- Query shape issues — does our cosine ordering actually rank correctly?

First run pulls the ~200MB image. Subsequent runs use the cache.

### Filesystem-first, DB-second (the recovery story)

The JSONL manifests in `data/` are the **source of truth**. Postgres is a rebuildable index built from them. If Postgres gets corrupted or dropped:

```bash
docker compose up -d postgres
uv run alembic upgrade head    # fresh schema
uv run python -m viral_remix.db ingest    # drains manifests, re-embeds
```

Everything is recovered except the ~$ for re-embeddings. That's why `scripts/db-backup.sh` exists — `pg_dump` before any risky migration preserves the embeddings so we don't pay OpenAI twice.

The inverse is NOT true: if the manifests get corrupted, Postgres can't recover them (we don't snapshot the source MP4 files into the DB). So `data/` is the thing to back up; Postgres is convenience.

---

## 16. Patterns that recur across steps

Worth noting because they'll keep showing up:

1. **Run-id tagging for cost + tracing.** Every expensive operation takes a `run_id` argument. Cost ledger, logfire spans, future retry policies — all partitioned by run_id. Lets you ask "what did video #42 cost?" instead of reverse-engineering logs.

2. **Isolated subprocess/API calls for mock-ability.** Every ffmpeg/openai/youtube call goes through a tiny wrapper function (`_run_vlm_agent`, `_embed_batch_via_openai`, etc.). Tests monkey-patch the wrapper, not the underlying library. Keeps tests fast, deterministic, and offline.

3. **Manifest dedupe + idempotent re-run.** Every stage can be run twice and produces no duplicate work. This is important when something crashes mid-batch — you don't have to figure out "what got processed." Just re-run and dedupe handles it.

4. **Versioning the producer.** `prompt_version` on annotations, `embedding_model` on embeddings. Whenever an output depends on a config parameter, that parameter gets stored on the output row. Change the config → next ingest detects stale rows → regenerates only those.

5. **Pydantic at the edges, specialized internals in between.** Models are Pydantic. Persistence is SQLAlchemy. LLM calls use pydantic-ai. The seam between "my domain type" and "library I happen to use" is narrow and crossed once, cleanly.
