"""Retirement timing model — when does work become optional, and when is it certain.

All figures in REAL 2026 dollars. Portfolio returns are real (inflation-adjusted).
Fact base: 2026-08-08 PC workbook snapshot + James's 2026-08-17 session answers
(1339 sale proceeds, rental income, ARM refi plan, comp simplification, $450k
retirement burn). Refresh constants from the PC workbook before each annual re-run.

Definitions:
  WORK-OPTIONAL — investable assets cover gross withdrawal need at 3.5% SWR,
                  with college fully carved out. Never *have* to work again.
  FULL-CERTAINTY — same at 3.0% SWR with mortgages paid off. The paranoid line.
"""

# ---------------------------------------------------------------- fact base
YEAR0 = 2026
JAMES_AGE0, FAN_AGE0 = 39, 36  # turning 40 / 37 in Dec 2026
EVELYN_COLLEGE = 2035          # b. May 2017 -> enters fall 2035
ETHAN_COLLEGE = 2039           # b. Sep 2020 -> enters fall 2039

# 8/8 workbook "fuel" $8.24M + 1339 sale net ~$675k (James 8/17: "$650-700k after
# taxes and fees and paying off the mortgage"). Taxable/retirement/cash split not
# refreshed this pass — pull from PC workbook at next re-run.
INVESTABLE0 = 8_240_000 + 675_000
COLLEGE_529 = 65_000           # James 8/17; NO superfund planned (ratified) — college funds from portfolio

# Real estate: three remain (Whisman primary, Gatetree, Lexington) — James 8/17.
# Equity is backstop only, excluded from investable. Values unrefreshed since Feb.
RE_EQUITY = (2_772_000 - 1_358_944) + (1_668_600 - 740_517) + 1_672_900
RENTAL_NET = 30_000            # James 8/17: ~$30k/yr net rental income, continues in retirement
ARM_PRINCIPAL = 1_358_944 + 740_517   # Whisman @2.5% + Gatetree @2.375%
ARM_RESET_YEAR = 2028          # CONFIRMED Oct 2028 (James 8/17) — the 5/1-vs-7/1 open item is closed
ARM_RESET_RATE = 0.065         # conservative refi rate
ARM_RESET_EXTRA = 78_000       # extra annual interest if refi lands ~6.5%
# Plan at reset = REFINANCE, not payoff (James 8/17) — model still lets the
# retiree pick the cheaper carry-vs-payoff strategy for the target math.

# ------------------------------------------------------------------- burn
BURN = 475_000            # James 8/17: $450-500k/yr current, "lower now that we sold 1339" — central
MORTGAGE_PI = 105_000     # est. P&I inside burn at pre-reset rates
RETIRE_BURN = 450_000     # James 8/17: "most likely lower but let's just say $450k" (incl. P&I) — SOFT, revisit
PRIVATE_SCHOOL = 40_000
COLLEGE_COST_PER_KID = 480_000   # 4yr private, today's dollars — school fork still open (fall 2027)
RETIRE_HEALTHCARE = 36_000       # pre-65 family ACA + OOP
WD_TAX_GROSSUP = 1.17            # blended LTCG+CA on withdrawals w/ basis return

# ------------------------------------------------------------------- comp
def comp_current(y):
    """James 8/17: 'just use $2.1M/yr as the current' (household, current stock prices)."""
    return 2_100_000

def comp_director(y, promo_year=2028):
    """Director lands -> household $2.6M (James 8/17). Timing read 8/16: real chance
    Jul '27, very real Jan '28 -> model from 2028."""
    return 2_600_000 if y >= promo_year else 2_100_000

EFF_TAX = 0.42            # fed+CA+FICA effective on $2-3M W2 CA married

# Fan works to the family finish line — both stop together (James 8/17).
# The old one-earner "coast" scenarios were removed accordingly.

# --- career-path scenarios (8/17 session; household comp) -------------------
# Timing priors (Leo, 8/17, from James's own reads): Director by mid-2028 ~75%;
# Sr Director 2031±1 ~35-45% conditional on Director (needs org growth/altitude
# change, not just performance); VP at Pinterest ~10-15% (seat-dependent —
# likelier route is external, which converges with the lab path).
def comp_sr_director(y):
    """Director 2028 -> Sr Director ~2031 (James ~$2.6M + Fan ~$0.9M)."""
    return 3_500_000 if y >= 2031 else comp_director(y)

def comp_vp(y):
    """Sr Dir path -> VP ~2033 (James ~$4.5M). Priced despite low probability."""
    return 5_500_000 if y >= 2033 else comp_sr_director(y)

def comp_lab(y):
    """External AI-lab re-pricing from 2028 (~$4.5M household, equity risk).
    REJECTED as a now-move (James 8/17): Meta-era kid-time cost, not worth it
    at current wealth."""
    return 4_500_000 if y >= 2028 else 2_100_000

def comp_boredom_sprint(y):
    """James's stated realistic external option (8/17): ride Pinterest+Director,
    and IF recsys goes stale in 5-10 yrs, jump to a pre-breakout company for a
    ~3-year cash sprint, then forget about it."""
    return 4_500_000 if 2033 <= y <= 2035 else comp_director(y)

SCENARIOS = {
    "A Sr EM plateau ($2.1M)":   comp_current,
    "B Director '28 ($2.6M)":    comp_director,
    "C + Sr Dir '31 ($3.5M)":    comp_sr_director,
    "D + VP '33 ($5.5M)":        comp_vp,
    "E Lab move '28 ($4.5M)":    comp_lab,
    "F Dir + sprint '33-35":     comp_boredom_sprint,
}

# ---------------------------------------------------------------- returns
REAL_RETURN = {"bear": 0.03, "base": 0.05, "bull": 0.07}

# ---------------------------------------------------------------- targets
def gross_need(burn):
    return (burn + RETIRE_HEALTHCARE) * WD_TAX_GROSSUP

def college_liability(y):
    """Remaining college costs not yet covered by 529, as of year y."""
    remaining = 0
    for start in (EVELYN_COLLEGE, ETHAN_COLLEGE):
        for k in range(4):
            if start + k >= y:
                remaining += COLLEGE_COST_PER_KID / 4
    return max(0, remaining - COLLEGE_529)

def target_work_optional(y, arm_reset_hit):
    # retiree picks the cheaper strategy: carry the (refinanced) mortgage vs pay it off
    burn_carry = RETIRE_BURN - RENTAL_NET + (ARM_RESET_EXTRA if arm_reset_hit else 0)
    carry = gross_need(burn_carry) / 0.035
    payoff = gross_need(RETIRE_BURN - MORTGAGE_PI - RENTAL_NET) / 0.035 + ARM_PRINCIPAL
    return min(carry, payoff) + college_liability(y)

def target_full_certainty(y):
    # 3.0% SWR, mortgages paid off from portfolio, college pre-funded
    burn = RETIRE_BURN - MORTGAGE_PI - RENTAL_NET
    return gross_need(burn) / 0.030 + college_liability(y) + ARM_PRINCIPAL

# ---------------------------------------------------------------- simulate
def simulate(comp_fn, ret, horizon=20, stop_saving_at=None):
    """Year-by-year investable balance. Returns list of (year, ages, balance, targets)."""
    bal = INVESTABLE0
    rows = []
    for i in range(horizon + 1):
        y = YEAR0 + i
        arm_hit = y >= ARM_RESET_YEAR
        t_opt = target_work_optional(y, arm_hit)
        t_cert = target_full_certainty(y)
        rows.append((y, JAMES_AGE0 + i, FAN_AGE0 + i, bal, t_opt, t_cert))
        # grow then save (conservative ordering)
        bal *= (1 + ret)
        working = stop_saving_at is None or y < stop_saving_at
        burn = BURN - RENTAL_NET + (ARM_RESET_EXTRA if arm_hit else 0)
        if working:
            after_tax = comp_fn(y) * (1 - EFF_TAX)
            bal += max(0, after_tax - burn)
        else:
            bal -= gross_need(RETIRE_BURN - RENTAL_NET + (ARM_RESET_EXTRA if arm_hit else 0))
            for start in (EVELYN_COLLEGE, ETHAN_COLLEGE):
                if start <= y < start + 4:
                    bal -= COLLEGE_COST_PER_KID / 4
    return rows

def first_cross(rows, idx):
    for r in rows:
        if r[3] >= r[idx]:
            return r
    return None

def fmt(x): return f"${x/1e6:,.2f}M"

if __name__ == "__main__":
    print(f"Investable now (Aug 2026, post-1339): {fmt(INVESTABLE0)}  |  RE equity backstop: {fmt(RE_EQUITY)}")
    print(f"Work-optional target 2026: {fmt(target_work_optional(2026, False))}")
    print(f"Work-optional target 2029 (post-reset): {fmt(target_work_optional(2029, True))}")
    print(f"Full-certainty target 2026: {fmt(target_full_certainty(2026))}")
    print()
    for comp_name, comp_fn in (("CURRENT ($2.1M flat)", comp_current), ("DIRECTOR ($2.6M from 2028)", comp_director)):
        for ret_name, ret in REAL_RETURN.items():
            rows = simulate(comp_fn, ret)
            opt = first_cross(rows, 4)
            cert = first_cross(rows, 5)
            o = f"{opt[0]} (J{opt[1]}/F{opt[2]}, {fmt(opt[3])})" if opt else ">2046"
            c = f"{cert[0]} (J{cert[1]}/F{cert[2]}, {fmt(cert[3])})" if cert else ">2046"
            print(f"{comp_name:28s} {ret_name:5s}  work-optional: {o:38s} full-certainty: {c}")
    print()
    for comp_name, comp_fn in (("CURRENT $2.1M", comp_current), ("DIRECTOR $2.6M from 2028", comp_director)):
        print(f"{comp_name}, base 5% real — year by year:")
        print(f"{'year':>5} {'J':>3} {'F':>3} {'investable':>12} {'opt target':>12} {'cert target':>12}")
        for r in simulate(comp_fn, 0.05, horizon=10):
            print(f"{r[0]:>5} {r[1]:>3} {r[2]:>3} {fmt(r[3]):>12} {fmt(r[4]):>12} {fmt(r[5]):>12}")
        print()
    # aggressive 4% SWR reference line
    t4 = gross_need(RETIRE_BURN - MORTGAGE_PI - RENTAL_NET) / 0.04 + ARM_PRINCIPAL + college_liability(2026)
    print(f"Reference: 4% SWR (payoff strategy) target today = {fmt(t4)}")
    print()
    # career-path scenario table (base 5% real): NW at 45/50/55 + wealth-tier crossings
    print("CAREER SCENARIOS (base 5% real):")
    print(f"{'path':28s} {'opt':>5s} {'NW@45':>8s} {'NW@50':>8s} {'NW@55':>8s}   $20M / $30M / $50M")
    for name, fn in SCENARIOS.items():
        rows = simulate(fn, 0.05, horizon=20)
        byyear = {r[0]: r[3] for r in rows}
        opt = first_cross(rows, 4)
        cr = []
        for t in (20e6, 30e6, 50e6):
            hit = next((r for r in rows if r[3] >= t), None)
            cr.append(f"{hit[0]}(J{hit[1]})" if hit else ">2046")
        print(f"{name:28s} {opt[0]:>5d} {byyear[2032]/1e6:>7.1f}M {byyear[2037]/1e6:>7.1f}M {byyear[2042]/1e6:>7.1f}M   {' / '.join(cr)}")
