# Goalie change-log capture — proposal (not wired, not enabled)

**RESEARCH_ONLY / DRAFT.** Adds `nhl_edge.data.goalie_watch`: a pure diff of Daily Faceoff goalie observations into an append-only *event* log
(`FIRST_SEEN`, `STATUS_CHANGE`, `GOALIE_CHANGE`, `CONFIRMED`, each with `first_seen_utc`, the source's own `source_reported_at_utc` when supplied, and `latency_min`),
plus a fail-soft `watch_once` that reuses the existing `fetch_dailyfaceoff`. **No workflow, job, model, stake, cap or existing capture is changed.**

Why: the independent research (`docs/research/nhl-model-improvement/INFORMATION_EVENT_ASSESSMENT.md` on branch `claude/nhl-model-improvement-f6kn0k`) found our goalie capture lags the
source's own report by a median 27.6 min (26% within 15 min), which makes any news-timing study or strategy impossible. A change log at 1–3 minute resolution around the pregame window
fixes the measurement at near-zero cost.

Cost design (decision needed): call `watch_once` from inside the existing capture-worker cycle during 10:00 ET → puck drop (one ~100 KB GET per poll) rather than adding a cron workflow
(a separate 5-minute workflow would cost roughly 3,000+ Actions minutes a month).

Next step if approved: wire the conditional poll into the capture worker behind a feature flag, run ≥ 4 weeks in shadow, evaluate latency and repricing at ≤ 5-minute resolution.
