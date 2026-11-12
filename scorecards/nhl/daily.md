## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-12T00:50:11Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 102541 across 164 games. Settled: 33883 (void/DNP 1361, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 299 (9) | 0.399 | +0.048 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 320 (9) | 0.374 | +0.037 | 0.185 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 299 (9) | 0.264 | +0.037 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 320 (9) | 0.262 | +0.021 | 0.128 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 299 (9) | 0.486 | +0.085 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 320 (9) | 0.471 | +0.057 | 0.252 | 84% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 13 (9) | 4.883 | +0.969 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 18 (9) | 5.179 | -0.527 | 3.727 | 78% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 299 (9) | 1.001 | -0.019 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 320 (9) | 1.027 | +0.030 | 0.692 | 79% | — |
| team_goals | pf-nhl-F_stack (challenger) | 18 (9) | 1.036 | +0.319 | 0.734 | 100% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 299 (9) | 1.693 | -0.057 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 320 (9) | 1.699 | +0.257 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 18 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 18 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 299 (9) | +0.0003 [-0.0122, +0.0142] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 299 (9) | +0.0001 [-0.0015, +0.0019] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 165 (9) | +0.0017 [-0.0030, +0.0061] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 166 (9) | -0.0003 [-0.0075, +0.0071] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 13 (9) | -0.0058 [-0.0134, +0.0030] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 299 (9) | +0.0155 [-0.0484, +0.0799] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 25 projected goalie-games, named goalie started 72.0% (mean published P(start) 0.906).
- participation CONFIRMED_ACTIVE: n=14, started 100.0%
- participation LIKELY_ACTIVE: n=11, started 36.4%

**Skater lineup check**: 332 projected skaters, 96.4% dressed.
- participation CONFIRMED_ACTIVE: n=19, dressed 94.7%
- participation LIKELY_ACTIVE: n=304, dressed 97.4%
- participation UNCERTAIN: n=9, dressed 66.7%

**Availability capture**: mean coverage 1.0, newest capture age 16.6 min (median over recent runs), runs summarised: 12.
