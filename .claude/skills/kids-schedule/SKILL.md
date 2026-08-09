---
name: kids-schedule
description: Show Ethan + Evelyn's extracurricular schedule — weekly grid, start dates, what's started vs. upcoming, and open slots still unbooked (speech & debate, robotics, ping-pong). Use when James asks "what's the kids' schedule", "when does X start", or types /kids-schedule.
user_invocable: true
---

# Kids Schedule

You are Leo showing James the kids' extracurricular schedule. This is a read-and-render dashboard — scannable in 30 seconds, phone-friendly (James often asks from remote-control).

## Source of truth

**`self/fall_2026_extracurriculars.md`** — the living timetable file. Read it fresh every time; never answer from memory or hardcode schedule data in this skill. If the file and this skill's examples ever disagree, the file wins.

Companions (read only if the question goes deeper):
- `self/evelyn_prep/speech_debate_options_2026-07.md` — the two speech options in detail
- `self/evelyn_prep/contacts_fall_2026.md` — provider contacts
- `backlog.md` Personal section — decision deadlines (e.g. Evelyn's speech pick)

## Process

1. Read `self/fall_2026_extracurriculars.md`. Check today's date.
2. Render three blocks, in this order:

**① Weekly grid** — reproduce the day-by-day table (Mon–Sun, one column per kid). Compact; this is the thing James most often wants at a glance.

**② Start dates** — the activity list with dates, made date-aware:
- Already running → mark ✅ started
- Starting within the next 7 days → mark ⏳ with the weekday ("this Tuesday")
- Further out → plain date
- During the stagger window (first ~2 weeks of the season), show the start-date sequence explicitly so nothing gets missed.

**③ Not booked yet** — every open slot from the file's "Not yet scheduled" section. **Lead with Evelyn's speech & debate**: it's a pending decision (Able2Shine Sat 9:30 vs. GSA Sun 8:30), and the backlog carries a deadline — surface the deadline and days remaining. Then the rest (robotics, ping-pong, improv, post-soccer Saturday). One line each.

3. Close with any logistics flags from the file that bite **this week** (Saturday chaining, two-devices-at-7pm, etc.). Skip flags that aren't near-term.

## Rules

- **Display, don't manage.** No nagging, no "you still haven't booked X" pressure framing — state open slots neutrally with their dates. Family time is demand-led and joy-first (see `self/family.md` usage notes); the schedule is a container, not a scoreboard.
- If James states a schedule change or a booking mid-conversation ("we signed Evelyn up for GSA"), update `self/fall_2026_extracurriculars.md` in the same turn — move the item from "Not yet scheduled" into the grid + details table, adjust the logistics flags, and confirm in one line.
- Unresolved placeholders in the file (⟨…⟩ markers) are open questions — carry them through visibly, don't invent answers.
- Keep total output short. This is a fridge-door timetable, not a report.
