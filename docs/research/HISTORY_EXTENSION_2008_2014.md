# History extension: MoneyPuck + official results, seasons 2008–2014

> RESEARCH_ONLY. Data only; no model, price, stake, cap or contract is touched. Pulled by the existing `history-pull` workflow (run 39891401718, 2026-10-23) from a network-capable runner; `data/history/MANIFEST.json` carries the sha256 of every file. Existing seasons (2015–2025) are byte-for-byte unchanged.

Why: every earlier historical study (V1/V2 walk-forwards, the opponent-adjusted study and its tuned-V1 control) was scored on 2018–2025, and 2015–2017 serves as training history. To test a *procedure* (for example "retune V1's shrinkage constants from the two prior seasons and recalibrate") on seasons that no analysis has ever scored, seasons earlier than the history on disk are needed. 2008–2014 gives training history for 2010 onward and, with 2015–2017, up to eight never-scored seasons (2010–2017).

## Data-quality check (done before any model touched these seasons; coverage and completeness only)

| season | official final regular-season games | games with MoneyPuck rows for both teams | coverage | xG non-null | score-and-venue-adjusted xG non-null | scores non-null | games with an unresolved team abbreviation |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2008 | 1230 | 1227 | 0.998 | 1.0 | 1.0 | 1.0 | 13.3% |
| 2009 | 1230 | 1229 | 0.999 | 1.0 | 1.0 | 1.0 | 13.3% |
| 2010 | 1230 | 1230 | 1.000 | 1.0 | 1.0 | 1.0 | 13.3% |
| 2011 | 1230 | 1230 | 1.000 | 1.0 | 1.0 | 1.0 | 6.7% |
| 2012 | 720 (lockout) | 720 | 1.000 | 1.0 | 1.0 | 1.0 | 6.7% |
| 2013 | 1230 | 1230 | 1.000 | 1.0 | 1.0 | 1.0 | 6.7% |
| 2014 | 1230 | 1230 | 1.000 | 1.0 | 1.0 | 1.0 | 0.0% |

"Unresolved" = the official list gives a team id that the repository's abbreviation map does not know (the defunct/renamed Atlanta Thrashers and the Phoenix/Arizona franchise in some years). The evaluation frameworks drop those games for **every** arm alike (`walk_forward.evaluation_games`); MoneyPuck rows for those clubs still feed the ratings of their opponents. The loss is independent of any forecaster, but it is a fixed 13.3% / 6.7% of games in the early seasons and is stated wherever those seasons are scored.

## Isolation

* Production shadows and the frozen V1/V2 walk-forwards read `data.history.pinned_seasons` (seasons ≥ 2022, PR #61), so adding older seasons cannot change their inputs.
* The `OA_RIDGE_V1` live shadow (`workflows/shadow_oa.py`) now also reads only the pinned recent seasons: `fit_oa` uses at most three seasons back, so older history could only slow the production `simulate` job (≈ +1 s per extra 7 seasons).
