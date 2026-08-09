# Long-Term Retirement Plan — When Work Becomes Optional

*Written 2026-07-13. Model: `self/finance/retirement_model.py` (run with `python3`). All figures in real (2026) dollars. Re-run annually or on any major input change.*

> **Data caveat:** the fact base came from the mac copy of the pf repo (net worth snapshot **2026-02-14**, since deleted from this machine). James's most accurate figures live on the PC. First re-run should refresh the constants at the top of the model from the PC numbers; dates below carry roughly ±6 months of staleness risk on top of the modeled ranges.

## The Answer

**Work becomes optional between 2032 and 2034, when James is 45 to 47.** Full certainty (the paranoid line) arrives one to two years later, 2033 to 2035. This holds across comp scenarios from the $2M/yr family floor to the likely growth path, and across 3% to 7% real return assumptions. The bear-market worst case pushes work-optional to 2035 (age 48).

Two lines, two meanings:

| Line | Definition | Investable target | Likely date |
|---|---|---|---|
| **Work-optional** | 3.5% SWR covers burn + healthcare + withdrawal taxes; college fully carved out; ARMs paid off at reset | **~$15.9M** | **2032–2034 (J45–47)** |
| **Full-certainty** | Same at 3.0% SWR — survives a 1966-style sequence | **~$18.1M** | **2033–2035 (J46–48)** |

Current position: **$7.23M investable** (post Lee Place sale), plus $4.25M real estate equity as backstop, on family savings of roughly $700K to $1.4M per year. You are a little under halfway to the line, but the compounding back half is faster than the front half was.

## The Kid Clock (why "life is short" is the right frame)

- **Evelyn leaves for college fall 2035** — she turns 18 in May 2035. That is **9 more summers**.
- **Ethan leaves fall 2039** — 13 more summers.
- The work-optional date (2032–2034) lands **1 to 3 years before Evelyn leaves**. On the likely path you get FI with roughly two years of the full four-person household left, and five to seven years of Ethan.

This is the plan's central tension: the money line and the kid line cross at nearly the same moment. Working "just two more years" past the line spends the scarcest asset you have. The plan's job is to make that trade visible each year, not to make it for you.

## Scenario Table

Model output (see script for assumptions):

| Comp scenario | Returns (real) | Work-optional | Full-certainty |
|---|---|---|---|
| Worst case ($2M flat) | 3% bear | 2035 (J48) | 2037 (J50) |
| Worst case ($2M flat) | 5% base | 2034 (J47) | 2035 (J48) |
| Likely (→ ~$3.15M) | 3% bear | 2033 (J46) | 2034 (J47) |
| **Likely (→ ~$3.15M)** | **5% base** | **2032 (J45)** | **2033 (J46)** |
| Likely (→ ~$3.15M) | 7% bull | 2032 (J45) | 2033 (J46) |

Reference point: at a 4% SWR (the standard FIRE line, aggressive for a 45-year horizon) the target is ~$14.3M, reached 2031–2033. The 3.5%/3.0% lines above are deliberately conservative because you asked for certainty.

Coast option (James stops earning, Fan keeps working, base returns): stopping in 2031 at age 44 delays work-optional only to 2033. **The last two working years buy almost nothing; Fan's income covering burn means the portfolio compounds untouched.** This is the "life is short" escape hatch: past roughly $14M, James's marginal year of work moves the date by months, not years.

## Fact Base (as modeled)

- James 39 (12/1986), Fan 36 (12/1989), Evelyn 9, Ethan 5. Mountain View.
- Investable $7.23M: taxable $5.55M (Schwab $2.29M, eTrade $1.57M, Shareworks $0.18M, Coinbase $0.15M, cash $1.21M, Lee proceeds ~$0.69M) + retirement $1.14M. Excludes 529s ($62K) and real estate.
- Burn $455K/yr ex income tax (2025 actuals), including ~$105K mortgage P&I, $78K property tax, $40K private school.
- Comp: family floor $2M/yr (James's stated worst case). Likely path: James $1.23M → ~$2M on L18 by 2029; Fan $800K growing ~6%/yr to ~$1.15M. Effective tax 42%.
- College: $480K per kid in today's dollars (4yr private), 529s nearly unfunded → ~$900K liability carried in the targets.
- ARMs: Whisman $1.36M @2.5% + Gatetree $0.74M @2.375%, both originated 10/2021. Model assumes 7/1 (reset Oct 2028) to ~6.5%, and assumes payoff-at-reset since that beats carrying (guaranteed 6.5% return vs 5% expected).
- Retirement healthcare $36K/yr pre-65; withdrawal tax gross-up 17%.

## Levers, In Order of Impact

1. **Comp trajectory (yours).** The L18/Director outcome moves the date about two years versus the floor scenario. The Director run and this plan point the same direction until roughly 2032; there is no conflict between the two dreams and this plan for the next 6 years.
2. **ARM decision (near-term, dated).** Confirm reset structure this month. If they are 5/1s, the reset is **October 2026** and the payoff-vs-carry analysis needs to run now; $2.1M of the cash/bond position covers it and cuts burn by ~$105K/yr.
3. **Burn discipline.** Every $35K/yr of permanent burn is ~$1M of target at 3.5%. The $447K limit in the strategy doc is the right control; the model breaks if burn drifts to $550K.
4. **529 catch-up.** Superfund both 529s (5-year gift-tax averaging, ~$180K per parent per kid available) from the Lee proceeds and cash pile. Pre-funding college removes ~$900K from the target and de-risks the single largest dated liability.
5. **Concentration and cash drag.** ~$1.2M sits in cash/CD beyond the $100K tax reserve, and the Schwab book is single-name tech heavy. The plan's SWR math assumes a diversified portfolio; the $25K/month VTI/VOO auto-invest is the mechanism, and the tax-loss harvesting on Fan's TEAM position funds the cleanup.
6. **Real estate simplification.** $4.25M equity across three properties earning (approximately) nothing after costs. Each property sold and redeployed at 5% real moves the date forward meaningfully; Lee was the template. Not modeled as required, listed as acceleration.

## Decision Points and Tripwires

- **Now (July 2026):** confirm ARM reset dates from loan docs; superfund 529s; keep auto-invest running.
- **Oct 2026 or Oct 2028 (reset):** execute payoff from cash/taxable unless rates have collapsed below ~4%.
- **Each January:** re-run `retirement_model.py` with the new snapshot. The output to watch is the gap between investable and the $15.9M line.
- **At ~$14M (projected 2030–2031, James ~44):** this is the real decision year. Marginal-year value collapses; coast becomes nearly free. Decide then whether years 2031+ at Pinterest (or a lab) are chosen for the work itself. Put this review on the calendar when the portfolio crosses $13M.
- **At $15.9M:** work is optional. Everything after is by choice, priced in Ethan-summers (Evelyn will be nearly gone).
- **At $18.1M:** even the paranoid version relaxes. Past this line, continued accumulation has no life justification the model can see.

## Open Items (affect the date by ±1 year)

1. **ARM structure** — 5/1 vs 7/1. Determines whether the payoff decision is 3 months or 27 months away. *(Highest urgency.)*
2. **Net rental cash flow** on Gatetree and Lexington — modeled as neutral; actuals would refine burn.
3. **College assumption** — $480K/kid private is the expensive case; in-state public halves it and pulls the work-optional date in ~8 months.
4. **Fan's plans** — the model assumes she works to the family line. If she wants her own earlier date, the coast scenarios invert and the targets stand but arrive ~2 years later.

## How This Sits With the Two Dreams

The 2026-07-11 session framed frontier-lab-later and Director-here as an optionality portfolio sharing 90% of next moves. This plan adds the third axis and finds the same answer: **for the next ~5 years, maximum-trajectory work is also the fastest path to the money line, so nothing forks yet.** The fork arrives around 2030–2031 at ~$14M, when marginal work-years stop buying meaningful time and start costing Ethan-summers. That is the date to circle, and it is also roughly when the Director outcome resolves and when a lab move would be trust-routed through delivered work. All three clocks converge on the same two-year window. Plan accordingly, decide then.

---

## 2026-08-08 snapshot — SUPERSEDES the 2026-07-13 numbers above (post-Lee-sale, corrected costs)

From James's PC-side workbook compute (pasted 8/8):

- **Net worth $12,291,705** (+$1.13M / +10.1% YoY; +32% over two years). Mix: cash $1.90M (13%) · investments $6.40M (45%) · real estate $6.06M (42%, down from 53% — Lee sold) · debt −$2.07M (−22% YoY).
- **Accessible-today liquidity: $6.12M after-tax** (after ~$796k tax on $2.3M embedded gains, 11.5% haircut), before touching retirement accounts or property.
- **Income:** household TC $2,350,660 (James $1.50M · Fan $854k incl. one-time $70k retention). **Spend:** $455k measured 2025 → ~$407k run-rate with Lee carrying costs gone, vs the $447k limit — first real headroom.
- **Retirement machine: ~70% funded.** Fuel $8.24M vs ~$11.8M target ($304k/yr mortgage-free @3.5% SWR, both surviving mortgages paid at finish). **Central crossing ~Jan 2029, at 42** (corrected — the earlier Apr-2030 carried dead Lee costs); band ≈ mid-2027 (at 41) to ~2032 (at 45) — even pessimistic paths land before 46. Gap closing at ~$1.6–1.7M/yr.
- **Levers ranked:** recurring burn is king (−$25k/yr ≈ a $500k raise) · one-offs are noise (~0.7 days per $3k trip — take the vacations) · marginal income weak (~1.5 months per $100k/yr) · markets ±2 years. Job menu priced: Pinterest promo ≈ 8 months · Meta at the $3M ask ≈ 18-month sprint · lab offers count only if equity sells on schedule.
- **Watch list:** (1) Oct 1 ARM reset — $2.07M repricing toward ~6.5% worst case; caps unknown (Range); paydown-vs-deploy analysis queued, $671k wire ready. (2) Taxes — $37k federal top-up Sep 15; ~$230–240k total tax cash earmarked through next April. (3) Grant dependency — ~63% of household income is PINS/TEAM equity (untradeable); a grant freeze = 2029 → 2032. (4) Education fork — both-kids-private pushes retirement ~1.5–2 years; decision arrives fall 2027 with the finish line visible.
