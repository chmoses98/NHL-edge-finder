# Model-improvement research — progress ledger (resume here)

Branch `claude/nhl-model-improvement-f6kn0k` (stacked on the exact tip `1040fbb` of `research/nhl-market-audit-20261021` = draft PR #52; rebuilt 2026-10-21 so the diff excludes `main`'s PR #51 — see COMMIT_MAP.md; backup branch `backup/pr53-pre-rebuild-6d5c366`). RESEARCH_ONLY.
Work state at 2026-10-21: all planned analyses executed; reports written; PRs opened as **drafts**; nothing merged.

## Frozen / one-shot items (do NOT redo or edit)

* Prior audit registry `nhl-hypotheses-1.0` (git `627b5fa7`) and its committed results: untouched. v1.1 (`market_audit/hypotheses_v11.py`) is a separate reading.
* **M-LIVE-1 is a single look** (spent). Experiments are append-only in `experiment_registry.jsonl`; a changed idea is a new id; never edit a line (`registry.verify` detects it).
* **Prospective tier** = games starting after 2026-10-21T17:13:05Z. Not read by any development code; only `daily.py` ingests it (blinded until 150 games; `LOOK_150.json` written once).
* Archive snapshot used: `data-archive` HEAD `e2d403e` (tick data to 2026-10-21T20:10Z), `accounting-data` `70c507a`; development window = games through 2026-10-20 only.

## Status

| phase | state | where |
|---|---|---|
| 1 Review PR #52 (4 independent reviews + cold re-run) | done | PR52_INDEPENDENT_REVIEW.md |
| 2 Fixes: engine F1-F4/F6, blinded prospective + freeze filters, coverage D1, age-rule D2 option, PIT test D6, fingerprint D7, registry v1.1 | done | commits listed in COMMIT_MAP.md (pre-rebuild `2f8a591c`… = rebuilt `10ba26fb`…); tests `test_market_audit_engine_v11`, `_review_fixes`, `test_hypotheses_v11` |
| 3 Pregame reconstruction + lineage | done (LIVE tier) | DATA_QUALITY_AND_LINEAGE.md |
| 4 Error attribution (A–F), distributions, goalie, player, scripts | done | PREDICTION_ERROR_AUDIT.md, MATCHUP_AND_SCRIPT_STUDY.md |
| 5-6 Challengers vs market | done (all rejected / inconclusive) | CHALLENGER_MODEL_COMPARISON.md |
| 7 Market families, information events | done; capture proposal as separate draft PR | MARKET_FAMILIES_AND_EXPRESSION.md, INFORMATION_EVENT_ASSESSMENT.md |
| 8 Expression engine | existing shadow engine corrected, replay re-run | `data/shadow_summary_fixed_engine.json` |
| 9 Daily loop | done, manual dispatch, publish=false; sealed (encrypted) ledger implemented, NOT activated (needs owner keys + approval) | `daily.py`, `src/nhl_edge/sealed_ledger/`, `.github/workflows/model_research_daily.yml` |
| 10 Reports, PRs, handoff | done | EXECUTIVE_REPORT.md |

## Open items (none changes a headline)

PR #52 review items left open: D3/D4 doc corrections, D5 postponed-game join, D8 availability-lag upper bound, D9 freeze filter for thesis/wager/case steps, D10, scorecard silent-on-missing-input alarm (F8), ledger robustness (F9), existing workflow's job-wide write scope and force-push (F10), surviving mutants in the PIT tests (D6), fees.py rounding docstring (F6), power-table α/SD (F4, reported via `mde80` in v1.1 only), alpha-spending rule (now proposed in PROSPECTIVE_PROTOCOL.md).
Research not done: regenerating V2 / PLAYER_SIM distributions; per-game goalie-saves forecast evaluation (no shots-faced forecast exists); lineup/injury timing (no data).

## Next exact actions

1. Review + decide on the draft PRs (see EXECUTIVE_REPORT.md "Recommended next actions").
2. If approved: run `model_research_daily` for each completed slate date (publish=false first); first look at 150 post-freeze games (~Dec 2026 at the current slate size). Do not read `LOOK_150.json` before then.
3. If the goalie capture is approved: wire `goalie_watch` behind a flag in the capture worker, 4-week shadow.

## Verification record

Full suite 656 passed, 2 skipped, 0 failures (CI-equivalent `ruff check src tests scripts` clean). Pipeline cold re-run reproduced every committed non-prospective output identically (see review report). Registry chain verified (25 entries).
