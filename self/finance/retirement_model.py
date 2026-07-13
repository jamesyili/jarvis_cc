"""Retirement timing model — when does work become optional, and when is it certain.

All figures in REAL 2026 dollars. Portfolio returns are real (inflation-adjusted).
Fact base: Li Family Net Worth workbook, 2026-02-14 snapshot (from the since-deleted
mac pf repo) + James's 2026-07-13 inputs. Canonical/current numbers live on the PC —
refresh the constants below from there before each annual re-run.

Definitions:
  WORK-OPTIONAL — investable assets cover gross withdrawal need at 3.5% SWR,
                  with college fully carved out. Never *have* to work again.
  FULL-CERTAINTY — same at 3.0% SWR with mortgages paid off. The paranoid line.
"""

# ---------------------------------------------------------------- fact base
YEAR0 = 2026
JAMES_AGE0, FAN_AGE0 = 39, 36  # turning 40 / 37 in Dec 2026
EVELYN_COLLEGE = 2035          # b. May 2017 -> enters fall 2035
ETHAN_COLLEGE = 2039           # b. Sep 2020 -> enters fall 2039 (starts K late-birthday typical)

# Feb 2026 snapshot, adjusted for Lee Place sale (~Jul 2026):
#   value 1,272,800 - mortgage 740,517*  - ~6% selling cost => ~+455k liquid
#   *Lee mortgage is account 4751 ($506,515 @3.0%)? Sheet maps 4751->Lee. Use 506,515.
#   equity = 1,272,800 - 506,515 - 76,368 (6%) = 689,917 -> round 690k to liquid
LIQUID_TAXABLE = 2_291_150 + 1_572_659 + 176_270 + 147_522 \
               + 418_000 + 137_657 + 655_696 + 690_000    # schwab+etrade+shareworks+coinbase+cash+lee proceeds
RETIREMENT = 541_246 + 522_664 + 41_425 + 38_523           # 401ks + IRA
COLLEGE_529 = 62_056
INVESTABLE0 = LIQUID_TAXABLE + RETIREMENT                  # exclude 529 (earmarked) & real estate

# Real estate AFTER Lee sale (kept out of investable; equity listed as backstop)
RE_EQUITY = (2_772_000 - 1_358_944) + (1_668_600 - 506_515) + 1_672_900
# ^ Whisman(primary), Gatetree, Lexington(no mortgage per sheet)
ARM_PRINCIPAL = 1_358_944 + 506_515   # wait — 4157 Gatetree 740,517@2.375; 4751 Lee 506,515@3.0
ARM_PRINCIPAL = 1_358_944 + 740_517   # Whisman @2.5 + Gatetree @2.375 (Lee's gone at sale)

# ------------------------------------------------------------------- burn
BURN = 455_000            # 2025 actuals, ex income tax (incl. P&I, prop tax, school)
MORTGAGE_PI = 105_000     # est. P&I inside BURN: 1.522M@2.5%/30y ~66k + 827k@2.375%/30y ~39k
ARM_RESET_YEAR = 2028     # 7/1 ARM assumption (Oct 2028). If 5/1 -> 2026. FLAGGED OPEN.
ARM_RESET_RATE = 0.065    # conservative reset
ARM_RESET_EXTRA = 78_000  # extra annual interest at reset: 2.1M*(6.5%-2.45% blended) ~ 85k, capped by caps ~78k

PRIVATE_SCHOOL = 40_000   # falls out of burn when each kid leaves for college (replaced by college line)
COLLEGE_COST_PER_KID = 480_000   # 4yr private, today's dollars (120k/yr all-in)

RETIRE_HEALTHCARE = 36_000       # pre-65 family ACA + OOP
WD_TAX_GROSSUP = 1.17            # blended LTCG+CA on withdrawals w/ basis return

# ------------------------------------------------------------------- comp
def family_comp_worst(y):
    """James's floor: $2M/yr family, flat real."""
    return 2_000_000

def family_comp_likely(y):
    """James 1.23M -> L18 ~2M by 2029; Fan 0.8M -> ~1.15M by 2031; plateau ~3.2M real."""
    james = {2026:1_230_000, 2027:1_300_000, 2028:1_450_000, 2029:2_000_000}.get(y, 2_000_000 if y>=2029 else 1_230_000)
    fan   = min(800_000 * (1.06 ** (y - 2026)), 1_150_000)
    return james + fan

EFF_TAX = 0.42            # fed+CA+FICA effective on $2-3M W2 CA married

# ---------------------------------------------------------------- returns
REAL_RETURN = {"bear": 0.03, "base": 0.05, "bull": 0.07}

# ---------------------------------------------------------------- targets
def gross_need(burn):
    return (burn + RETIRE_HEALTHCARE) * WD_TAX_GROSSUP

def college_liability(y):
    """PV of remaining college costs not yet covered by 529, as of year y."""
    remaining = 0
    for start in (EVELYN_COLLEGE, ETHAN_COLLEGE):
        for k in range(4):
            if start + k >= y:
                remaining += COLLEGE_COST_PER_KID / 4
    return max(0, remaining - COLLEGE_529)

def target_work_optional(y, arm_reset_hit):
    # retiree picks the cheaper strategy: carry the mortgage vs pay it off
    burn_carry = BURN + (ARM_RESET_EXTRA if arm_reset_hit else 0)
    carry = gross_need(burn_carry) / 0.035
    payoff = gross_need(BURN - MORTGAGE_PI) / 0.035 + ARM_PRINCIPAL
    return min(carry, payoff) + college_liability(y)

def target_full_certainty(y):
    # 3.0% SWR, mortgages paid off from portfolio, college pre-funded
    burn = BURN - MORTGAGE_PI
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
        if working:
            after_tax = comp_fn(y) * (1 - EFF_TAX)
            burn = BURN + (ARM_RESET_EXTRA if arm_hit else 0)
            bal += max(0, after_tax - burn)
        else:
            burn = BURN + (ARM_RESET_EXTRA if arm_hit else 0)
            bal -= gross_need(burn)
            # college paid from portfolio in-years
            for start in (EVELYN_COLLEGE, ETHAN_COLLEGE):
                if start <= y < start + 4:
                    bal -= COLLEGE_COST_PER_KID / 4
    return rows

def simulate_coast(james_stops, ret, horizon=20):
    """James stops earning at `james_stops`; Fan keeps working and covers burn.
    Portfolio compounds untouched (Fan surplus ~0 after burn). Returns rows."""
    bal = INVESTABLE0
    rows = []
    for i in range(horizon + 1):
        y = YEAR0 + i
        arm_hit = y >= ARM_RESET_YEAR
        rows.append((y, JAMES_AGE0 + i, FAN_AGE0 + i, bal,
                     target_work_optional(y, arm_hit), target_full_certainty(y)))
        bal *= (1 + ret)
        if y < james_stops:
            bal += max(0, family_comp_likely(y) * (1 - EFF_TAX) - (BURN + (ARM_RESET_EXTRA if arm_hit else 0)))
        else:
            fan_net = min(800_000 * (1.06 ** (y - 2026)), 1_150_000) * (1 - 0.38)
            burn = BURN + (ARM_RESET_EXTRA if arm_hit else 0)
            bal += fan_net - burn   # can be slightly negative post-reset
    return rows

def first_cross(rows, idx):
    for r in rows:
        if r[3] >= r[idx]:
            return r
    return None

def fmt(x): return f"${x/1e6:,.2f}M"

if __name__ == "__main__":
    print(f"Investable now (post-Lee): {fmt(INVESTABLE0)}  |  RE equity backstop: {fmt(RE_EQUITY)}")
    print(f"Work-optional target 2026 (pre-reset): {fmt(target_work_optional(2026, False))}")
    print(f"Work-optional target 2029 (post-reset, college nearer): {fmt(target_work_optional(2029, True))}")
    print(f"Full-certainty target 2026: {fmt(target_full_certainty(2026))}")
    print()
    for comp_name, comp_fn in (("WORST ($2M flat)", family_comp_worst), ("LIKELY (grows to ~$3.15M)", family_comp_likely)):
        for ret_name, ret in REAL_RETURN.items():
            rows = simulate(comp_fn, ret)
            opt = first_cross(rows, 4)
            cert = first_cross(rows, 5)
            o = f"{opt[0]} (J{opt[1]}/F{opt[2]}, {fmt(opt[3])})" if opt else ">2046"
            c = f"{cert[0]} (J{cert[1]}/F{cert[2]}, {fmt(cert[3])})" if cert else ">2046"
            print(f"{comp_name:28s} {ret_name:5s}  work-optional: {o:38s} full-certainty: {c}")
    print()
    # detail table, likely/base
    print("LIKELY comp, base 5% real — year by year:")
    print(f"{'year':>5} {'J':>3} {'F':>3} {'investable':>12} {'opt target':>12} {'cert target':>12}")
    for r in simulate(family_comp_likely, 0.05, horizon=12):
        print(f"{r[0]:>5} {r[1]:>3} {r[2]:>3} {fmt(r[3]):>12} {fmt(r[4]):>12} {fmt(r[5]):>12}")
    print()
    # coast scenarios: James stops, Fan keeps working
    print("COAST — James stops earning in year X, Fan works on (base 5% real):")
    for stop in (2029, 2031, 2033):
        rows = simulate_coast(stop, 0.05)
        opt, cert = first_cross(rows, 4), first_cross(rows, 5)
        o = f"{opt[0]} (J{opt[1]})" if opt else ">2046"
        c = f"{cert[0]} (J{cert[1]})" if cert else ">2046"
        print(f"  James stops {stop} (age {stop-1987}):  work-optional {o},  full-certainty {c}")
    print()
    # aggressive 4% SWR reference line
    burn_payoff = BURN - MORTGAGE_PI
    t4 = gross_need(burn_payoff) / 0.04 + ARM_PRINCIPAL + college_liability(2026)
    print(f"Reference: 4% SWR (payoff strategy) target today = {fmt(t4)}")
