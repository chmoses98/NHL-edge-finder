## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-11T01:41:12Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 99614 across 158 games. Settled: 32495 (void/DNP 1324, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 236 (7) | 0.399 | +0.056 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 248 (7) | 0.374 | +0.040 | 0.185 | 82% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 236 (7) | 0.267 | +0.028 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 248 (7) | 0.261 | +0.018 | 0.128 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 236 (7) | 0.500 | +0.084 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 248 (7) | 0.478 | +0.056 | 0.257 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 10 (7) | 4.431 | +0.141 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 14 (7) | 4.980 | -1.724 | 3.803 | 79% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 236 (7) | 0.995 | -0.136 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 248 (7) | 0.996 | -0.074 | 0.678 | 79% | — |
| team_goals | pf-nhl-F_stack (challenger) | 14 (7) | 1.059 | +0.346 | 0.746 | 86% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 236 (7) | 1.886 | -0.176 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 248 (7) | 1.879 | +0.079 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 14 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 14 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 236 (7) | -0.0135 [-0.0238, -0.0022] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 236 (7) | -0.0010 [-0.0033, +0.0019] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 136 (7) | -0.0042 [-0.0084, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 137 (7) | -0.0045 [-0.0130, +0.0039] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 10 (7) | -0.0080 [-0.0205, +0.0051] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 236 (7) | -0.0047 [-0.1351, +0.1091] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 19 projected goalie-games, named goalie started 73.7% (mean published P(start) 0.8865).
- participation CONFIRMED_ACTIVE: n=8, started 100.0%
- participation LIKELY_ACTIVE: n=11, started 54.5%

**Skater lineup check**: 258 projected skaters, 96.1% dressed.
- participation LIKELY_ACTIVE: n=253, dressed 97.2%
- participation UNCERTAIN: n=5, dressed 40.0%

**Availability capture**: mean coverage 1.0, newest capture age 15.6 min (median over recent runs), runs summarised: 12.
