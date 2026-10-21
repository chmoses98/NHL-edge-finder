# Historical pregame reconstruction: data quality, lineage and gaps

> RESEARCH ONLY. Code: `src/nhl_edge/model_research/{slates,live_dataset,wf_data}.py`. The archive and ledger are read-only inputs; derived tables are written outside the repository (small committed extracts are in `data/`).

## What can be reconstructed, for which games

| tier | games | what is point-in-time reconstructable | what is not |
|---|---|---|---|
| **LIVE** (2026-09-29..10-20) | 151 finals | everything below at **T-60** (the last production slate run ≤ cut; median slate age 26.8 min, max 50.8) | news timing between observations |
| **Walk-forward history** (2024, 2025 seasons) | 2,624 | the production V1 expected goals, seeds, rest/b2b, team ratings, V2 published ladders (every parameter fitted on earlier seasons only); outcomes | starter/injury/line news (the walk-forward uses a neutral goalie factor — a valid pregame arm, not an oracle); Kalshi quotes only for 2025-26 |
| **2025-26 Kalshi history** | 1,312 | hourly candle bid/ask at T-0/60/360/1440 for moneyline, total, puck line | depth, settlement for live, trades |
| **Prospective** | not read | by `daily.py` only, blinded | — |

## Per-game pregame record at the cut (`live_dataset.build_live_dataset`)

Provenance classes: **OBSERVED** (an archived value stamped by the archive), **MODEL-DERIVED** (a production output at a stamped time), **DERIVED** (computed from stamped inputs), **LABEL** (known only after the game; never an input).

| column group | class | source and rule |
|---|---|---|
| `game_id`, `start_time_utc`, teams | OBSERVED | latest schedule snapshot; `start_changed` flags postponements (none in the 151) |
| `cut_utc` = start − 60 min; `slate_run_id`, `slate_generated_at`, `slate_age_min` | DERIVED / OBSERVED | the last `slates/` run with `generated_at ≤ cut` (asserted); a game with none would be a counted gap (0 of 151) |
| `v1_lam_home/away`, `v1_seed`, `v1_n_sims`, `v1_p_*`, `v1_exp_*`, `v1_inputs_trusted` | MODEL-DERIVED | production `nhl-sim-1.1` / `DATA_ONLY_V1`; **the full predictive distribution regenerates bit-for-bit** from `lam` + `seed` (max \|Δ P(home win)\| = 0.0 over 151 games) |
| `v2_lam_*`, `v2_p_*` | MODEL-DERIVED | `nhl-sim-2.0` shadow arm in the same run (seed not regenerated here) |
| `{home,away}_goalie_*` | OBSERVED | goalie named by the slate at the cut and its status; CONFIRMED 100/83, PROBABLE 37/31, PROJECTED 14/37 (home/away) |
| `gobs_{home,away}_*` | OBSERVED | last Daily Faceoff observation ≤ cut; first confirmation's observed and **source-reported** times. Post-start `nhl_api_boxscore` observations are excluded from every pregame field |
| `sb_p_home`, `sb_n_providers`, `sb_overround` | OBSERVED | de-vigged median over six NHL-API partner books (American and decimal odds are mixed by provider and normalised; 147 of 151 games covered) |
| Kalshi mids | OBSERVED | the market-audit T-60 panel (`available_at = tick + 45 s ≤ cut`; a one-sided/inactive state at the cut is a missing quote, never an older one) |
| `actual_*_starter_id`, saves, shots against; `y_*`, `home_final`, `away_final` | LABEL | archived boxscore / results |

Not backfilled: no end-of-season statistic enters a pregame column (the slate packets record the snapshots they used); the final confirmed starter is **not** treated as known before its confirmation time.

## Data-quality findings (new in this work)

1. **The archived `starter` flag is unreliable.** `player_events/goalies.starter` is False for the goalies who played the whole game in 76 of 151 games. Goalie of record is the goalie with the most ice time (`n_goalies_used > 1` marks relief appearances: 16 team-games).
2. **Sportsbook odds are mixed-format.** DraftKings/FanDuel/Sportradar publish American odds, the others decimal; a naive parse yields negative probabilities. Normalised in `to_decimal_odds`; tests cover it.
3. **Source timestamps exist for goalie confirmations** (the prior audit declared them absent): 33% of goalie observation rows, all 223 pregame first confirmations. They are a floor on public availability, not proof of market learning.
4. **Script forecasts only exist from 2026-10-07** (99 of 151 games have a forecast at the cut and a postmortem).
5. **MoneyPuck team xG** for the 2026 games comes from a team-games snapshot that lags: 140 of 151 games have it (ex-post data; used only for decompositions).
6. **Player events**: 145 of 151 games have priced players with archived outcomes; 1.0% of priced player-games did not dress.
7. **Predictive distributions are stored as thresholds only** (prediction rows), but `lam + seed + n_sims` in the slate packet make the V1 distribution exactly reproducible; the V2 and PLAYER_SIM distributions were not regenerated.
8. **Review defects D1/D2** (coverage "usable quote" ordering inflating usable contracts by ~11.5%; quiet-market drop of 4.8% of T-60 rows) are corrected/optioned in code — see `PR52_INDEPENDENT_REVIEW.md`.
9. A pre-existing process finding: the market-audit pipeline evaluated the prospective tier on every run (now blinded).

## Gaps that block reliable historical analysis

* No timestamped lineup/injury/scratch timeline; no actual puck-drop time (only hourly schedule snapshots); no Kalshi settlement for live contracts; no trade tape; depth for 4 of 14 families; 15-minute board cadence; hourly capture of goalie status.
* Walk-forward history has no starter information, so goalie-uncertainty claims on 2024-25 cannot be tested; they are tested on LIVE only (n = 302 team-games).
* LIVE is the first three weeks of one season: early-season uncertainty cannot be separated from a general effect.

## Reproduce

```
python -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]" scipy statsmodels
git fetch --depth=1 origin data-archive accounting-data   # then `git archive` each into ../rdata/ (see market-audit PROGRESS.md)
python -m nhl_edge.market_audit.pipeline --archive ../rdata/data-archive --accounting ../rdata/accounting-data --history data/history --repo . --work ../rdata/work --out ../rdata/out
python - <<'PY'   # LIVE pregame table at T-60
from pathlib import Path
from nhl_edge.model_research.live_dataset import build_live_dataset
build_live_dataset(Path("../rdata/data-archive"), 60).to_parquet("../rdata/live_t60.parquet")
PY
```
