# Roadmap reset — 2026-10-22

> RESEARCH_ONLY. Decision by the owner on 2026-10-22: **stop the sealed-ledger activation path; replace manual witnessing and "wait for 150 prospective games" with automated historical research, walk-forward evaluation, nightly settlement and ongoing diagnostics.** Nothing is deleted. No wager, stake, cap, authority or SIFT contract changes.

## What is retired from the active roadmap

* Activating `sealed_ledger_daily` / `sealed_ledger_admin`; generating age/Ed25519 keys; creating a ledger repository, deploy key, environment or activation variable; the weekly owner witness routine; the macOS checklist.
* Waiting for a prospective sample (150 / 300 / 450 games) before researching improvements. Historical walk-forward evidence (many seasons, point-in-time, chronologically validated) is now the working basis for development; prospective data is a confirmation layer, not a gate on research.

## What stays, untouched, for reproducibility

* PR #58 and the sealed-ledger code, tests (`tests/test_sealed_*.py`), workflows and documents. Both workflows remain `workflow_dispatch`-only with their schedules commented out and no key in `recipients.txt`; they are **dormant, not removed** (removing harmless dormant infrastructure is explicitly not worth development time). The documents carry a "superseded" banner and are no longer on the roadmap.
* Every frozen protocol, registry entry (`experiment_registry.jsonl`, hash-chained), historical result and audit report.

## The untouched out-of-sample set (kept as a safeguard, not a blocker)

* **Prospective tier**: every regular-season game that starts after `2026-10-21T17:13:05Z` (`market_audit.PROSPECTIVE_FREEZE_UTC`). No development code reads it (enforced by the date filters in `market_audit` and `model_research`; the new `oa_*` research modules only read seasons through 2025).
* It is recorded automatically and append-only by the production pipeline itself: every pregame prediction is archived with `predicted_at_utc`, `data_cutoff_utc`, input snapshot ids and the market state, in `data-archive` (manifest with sha256 per file; git commit times are the public timestamp). No keys, witnesses or approvals are involved.
* It is evaluated by the automated nightly settlement/evaluation and by the promotion scorecard's live non-inferiority gate (`G10`), never used to select a model.

## What replaces it (automated, hands-off)

| need | mechanism | state |
|---|---|---|
| pregame snapshots, projections, versions | `capture_worker` (continuous), `projection-foundation` (player layer), predictions archived with version + timestamp | running |
| settlement + scoring vs outcomes and market | worker `settle` / `evaluate`; `projection-foundation` settle/score | running (evaluate was timing out — fixed in PR #59) |
| pregame readiness / stale / missing-data detection | `nhl slate-check` | PR #59 |
| historical walk-forward, leakage and feature-availability checks | `research/oa_walk_forward.py`, `oa_evaluate.py` (preregistered), existing `walk_forward*.py` | PR (OA) |
| challenger-to-champion decisions | `research/promotion.py` (predefined gates) + `PROMOTION_SCORECARD.md` | PR (OA) |
| weekly / monthly research summary, alerts on meaningful failures only | see `AUTOMATION.md` | this PR |

## Safety rails that do not change

Forecasting research and betting execution stay separate. No automatic wager placement; no stake or cap increase; no automatic activation of any previously rejected NHL bet; no goal-scorer betting recommendations; no promotion without the scorecard; no speculative EV from stale or unexecutable prices; PASS is always acceptable; a projection-research change never silently alters the live betting engine. `kalshi-bet-router` still has no NHL destination.
