# The game — what James would most enjoy building and playing

Started 2026-09-07 (Labor Day, remote). A `/grill-me`: one question at a time, Leo's recommended answer attached, James's answer recorded as given. **Garden project by James's own rule** (goals.md §Motivation Architecture, 8/29): no roadmap, no deadline, no launch target; Leo doesn't score it. Rename this file when the game has a name.

## What was already on the table before the grill

- **Why build at all.** "Work is a big part of me because absorption is a big part of me" (9/7, provisional in goals.md §Absorption). What James loves is losing hours finishing something doable with a process he enjoys, then the next objective. Building with AI coding agents leaves him the part where his time disappears (loop design, systems, balance, the director) and hands off the plumbing (engine, input, rendering, save system, content scaffolding).
- **Leo's opening pick, before the power input:** a run-based roguelike where the game learns its player — Hades-shaped runs, a director that models how he plays and chooses the offer slate. The recsys slate problem with one user and instant ground truth; interest exploration as the design problem (a director that only offers what you'd pick makes a run you'd drop at hour twenty). Built in playable slices. Browser, one repo, boon table as JSON he tunes by hand until the director earns it.
- **Taste record, from his backlog (9/7).** Tens are demanding-but-doable with visible progression and an ending: Hades (90 h), Horizon Forbidden West, FFXVI, Tales of Arise, Return to Moria, Skul, Nex Machina. Nines: Ghost of Tsushima, Black Myth: Wukong. Run-based games with a persistent layer he loves (Hades, Skul, Returnal, Death Must Die, Balatro); run-based without one he drops (Risk of Rain ×2, Soulstone). Drops are open-ended or punishing (Elden Ring at 25 h, Sekiro, Cuphead) or process-dead (Diablo 4, twice). Thirty drops, most under five hours: he abandons freely. Modest-looking games are fine when the loop is good (Hades, Skul, Balatro, Moria).
- **Rest shape (6/13):** solo, quiet, self-directed, no audience. Single-player by default.

## New input that opened the grill (James, 9/7)

> "Power accumulation is also very important. This power fantasy is part of the gameplay and eventually working up to absolute control, almost like the god. That's also very important for me."

What it changes in Leo's read:
1. **Hades' persistent layer is too thin for this.** Accumulation has to be the spine, not the garnish.
2. **A director that scales challenge *against* the player is anti-power-fantasy** — rubber-banding kills the god feeling. If the learning system survives, its job changes: curate what's offered, pace the god moment, make the world react. Never neutralize the power.
3. **His finished list is embodied power** (Wukong, Clive, Kratos, Zagreus, one-vs-a-thousand in Dynasty Warriors) plus **creation** (Tears of the Kingdom 120 h, Return to Moria) — not spreadsheet power (no 4X, grand strategy, or factory game finished). "Absolute control" reads as the end of an arc that starts in a body.

## Decision tree (in dependency order)

1. Shape of the fantasy: embodied god / ruling god / the arc from one to the other
2. What "absolute control" feels like at the end: force, command, or rewriting the rules
3. Loop structure: runs that feed a persistent ascent, or one unbroken ascent
4. Does it end: ascension as the ending vs. endless
5. Control scheme: real-time action / movement-plus-auto with build choices / turn-based
6. The learning system's role: curation, world reaction, challenge, or none
7. Theme and setting
8. What James owns in the build vs. what agents own; the first playable slice
9. Build constraints: hours, stack, the garden rule

## The grill (running log)

### Q1 — Shape of the fantasy
**Leo's recommended answer:** the arc. Start as one weak body; end as the thing the world obeys. The smashing is the middle of the game, the ruling is the end. Reason: every finished game on his list is embodied, but "absolute control" is a ruler's word.
**James:** (pending)
