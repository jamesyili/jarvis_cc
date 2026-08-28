---
id: flag-unreadable-screenshot-text
trigger: When reading a screenshot (calendar week view, Slack thread, table) where labels are truncated, wrapped into single letters, or overlapped — and the answer depends on what those labels say
behavior: Say which items you could not read before asserting anything about them. Reason from the readable ones and the shape (density, overlaps, protected blocks), and mark per-slot claims as uncertain ("the 11 AM stack — can't read the names"). Never name a meeting from a two-letter fragment as if it were legible. If the ask is precise (which meetings to cut), offer the readable subset confidently and list the unreadable slots as "you'd have to tell me."
confidence: 0.3
evidence_count: 1
created: 2026-08-28
last_updated: 2026-08-28
status: active
---

## Evidence

### 2026-08-28
> "No you can't read the entire meeting names. That's why you can be confused about certain time slots. It's fine. I think your points are mainly maybe on point."
Context: Leo read three phone calendar screenshots (a day view + two week views with dozens of one-to-three-letter truncated boxes) and produced a per-meeting hand-off list, naming several standing syncs from fragments. The structural read (density, triple-booking, ~5 protected hours) landed; the per-slot names were partly guesses and James said so.
Signal: correction
