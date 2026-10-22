# SIFT NHL model-improvement research

> RESEARCH ONLY. Start with **EXECUTIVE_REPORT.md**; resume from **PROGRESS.md**. Companion to (and stacked on) `docs/research/nhl-market-audit/` (PR #52), which is not modified.

| requested report | file |
|---|---|
| 1 Independent PR #52 review | PR52_INDEPENDENT_REVIEW.md |
| 2 Historical data-quality assessment | DATA_QUALITY_AND_LINEAGE.md |
| 3 Comprehensive prediction-error audit | PREDICTION_ERROR_AUDIT.md (`data/live_game_attribution.csv`, `data/wf_scan.json`) |
| 4 NHL matchup-feature analysis | MATCHUP_AND_SCRIPT_STUDY.md §1 |
| 5 Game-script calibration | MATCHUP_AND_SCRIPT_STUDY.md §2 |
| 6 Goalie and scoring-distribution study | PREDICTION_ERROR_AUDIT.md (questions 5–9), RESULTS_TABLES.md (M-DIST-1, M-GOALIE-1, M-PLAYER-1) |
| 7 Existing-model failure analysis | PREDICTION_ERROR_AUDIT.md §"Why are our models less accurate than the market?" |
| 8 Challenger model comparison | CHALLENGER_MODEL_COMPARISON.md |
| 9 Historical market-family comparison | MARKET_FAMILIES_AND_EXPRESSION.md §1 (builds on the reproduced prior study) |
| 10 Information-event opportunity assessment | INFORMATION_EVENT_ASSESSMENT.md |
| 11 Actual routed wager audit | ACTUAL_WAGER_AUDIT.md §1–3 |
| 12 October 20 case study | ACTUAL_WAGER_AUDIT.md §4 |
| 13 Market-expression research | MARKET_FAMILIES_AND_EXPRESSION.md §2–5 |
| Prospective ledger isolation and sealed storage | LEDGER_ISOLATION_REVIEW.md (finding), SEALED_LEDGER_DESIGN.md (design, threat model, security review), SEALED_LEDGER_UNATTENDED.md (unattended architecture, permissions analysis, exceptions, one-time setup), SEALED_LEDGER_KEY_SETUP.md (key custody, recovery), SEALED_LEDGER_OWNER_CHECKLIST.md (macOS checklist), DEPENDENCY_AND_ACTION_PINNING.md (pinned actions, hash-locked dependencies, update procedure) |
| 14 Statistical validation and robustness | CHALLENGER_MODEL_COMPARISON.md (protocol, multiplicity, robustness), PROSPECTIVE_PROTOCOL.md |
| 15 Final recommendations | EXECUTIVE_REPORT.md |

Branch history: COMMIT_MAP.md maps pre-rebuild to rebuilt commits (the registry's `code_commit` fields hold pre-rebuild SHAs).

Machine-readable results: `data/*.json|csv`. Every table in the narrative can be regenerated: `RESULTS_TABLES.md` (`python -m nhl_edge.model_research.render_tables --repo .`). The append-only, hash-chained experiment registry is `experiment_registry.jsonl` (`python -c "from nhl_edge.model_research import registry; print(registry.verify(...))"`).

## Reproduce

```
python -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]" scipy statsmodels
# read-only copies of the archive and ledger (see ../nhl-market-audit/PROGRESS.md), then:
python -m nhl_edge.market_audit.pipeline --archive ../rdata/data-archive --accounting ../rdata/accounting-data --history data/history --repo . --work ../rdata/work --out ../rdata/out
python -m nhl_edge.model_research.build_tables --archive ../rdata/data-archive --out ../rdata/model_research
R=docs/research/nhl-model-improvement; W=../rdata/work; M=../rdata/model_research
python -m nhl_edge.model_research.exp_cal     --repo . --out $R/data                       # M-DIST-1, M-CAL-1/2 (registry entries appended once)
python -m nhl_edge.model_research.exp_scan    --repo . --out $R/data   # M-SCAN-1
python -m nhl_edge.model_research.exp_goalie  --live $M/live_t60.parquet --repo . --out $R/data
python -m nhl_edge.model_research.exp_market  --repo . --derived $W --out $R/data           # M-MKT-1
python -m nhl_edge.model_research.exp_live    --repo . --live $M/live_t60.parquet --derived $W --out $R/data   # M-LIVE-1 (one look)
python -m nhl_edge.model_research.exp_info    --archive ../rdata/data-archive --derived $W --repo . --out $R/data [--record]
python -m nhl_edge.model_research.exp_scripts --archive ../rdata/data-archive --repo . --out $R/data
python -m nhl_edge.model_research.exp_players --archive ../rdata/data-archive --derived $W --out $R/data [--record]
python -m nhl_edge.model_research.render_tables --repo .
python -m pytest -q
```
Runners record a RESULT in the registry exactly once per id/revision (and refuse a RESULT without a PREREG); re-running them regenerates the `data/` files without adding entries. **Do not re-run `exp_live` expecting a new look: M-LIVE-1 is a single look.**

## Safety

Nothing in `src/nhl_edge/market_audit` or `src/nhl_edge/model_research` is imported by a production path; the only workflow files added are two manual-dispatch workflows (`market_audit.yml` from PR #52, `model_research_daily.yml`; schedules commented out, `publish=false` by default).
