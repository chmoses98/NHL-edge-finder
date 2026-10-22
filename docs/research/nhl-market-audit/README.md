# NHL SIFT historical market audit

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

Start with **EXECUTIVE_REPORT.md**. Resume work from **PROGRESS.md**. Reproduce everything with `python -m nhl_edge.market_audit.pipeline` (see HISTORICAL_RECONSTRUCTION.md).

| document | phase |
|---|---|
| EXECUTIVE_REPORT.md | summary, answers A-J |
| DATA_INVENTORY.md, CAPTURE_COVERAGE.md, DATA_QUALITY_AUDIT.md, HISTORICAL_RECONSTRUCTION.md | A - inventory, coverage, quality, lineage |
| MARKET_TAXONOMY.md, OUTCOME_MAPPING_REPORT.md | B - taxonomy and the deterministic outcome engine |
| MARKET_EFFICIENCY_STUDY.md | C - calibration, bands, lines, friction, power |
| MATCHUP_FACTOR_STUDY.md | D - factors beyond the market |
| PREDICTION_ENGINE_COMPARISON.md, OCT20_CASE_STUDY.md | E - model audit; routed-wager case study |
| CANDIDATE_SIGNAL_REGISTRY.md | F - pre-registered hypotheses, every result |
| EXPRESSION_ENGINE_SPEC.md | G - shadow market-expression engine |
| WALK_FORWARD_VALIDATION.md, STRATEGY_ROBUSTNESS.md | H - replay, controls, fees / slippage / liquidity |
| RISK_MANAGEMENT_FRAMEWORK.md | I |
| AUTOMATION_AND_MONITORING_PLAN.md, IMPLEMENTATION_ROADMAP.md | J and next steps |
| `data/*.json`, `data/wager_audit.csv`, `data/lineage.json` | machine-readable results |
