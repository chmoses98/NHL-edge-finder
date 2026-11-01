## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-01T15:11:21Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 61577 across 97 games. Settled: 23766 (void/DNP 1016, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2284 (68) | 0.424 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2393 (68) | 0.406 | -0.008 | 0.218 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2284 (68) | 0.282 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2393 (68) | 0.275 | -0.001 | 0.142 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2284 (68) | 0.545 | -0.003 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2393 (68) | 0.527 | -0.010 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 113 (65) | 5.024 | -0.761 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 132 (68) | 4.847 | -0.525 | 3.525 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2284 (68) | 1.008 | -0.085 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2393 (68) | 1.005 | +0.029 | 0.677 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 136 (68) | 1.345 | -0.020 | 0.914 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2284 (68) | 1.886 | -0.419 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2393 (68) | 1.777 | +0.033 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **OK** — within expectations
- shots: **OK** — within expectations
- team_goals: **OK** — within expectations
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 2283 (68) | -0.0096 [-0.0138, -0.0051] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2283 (68) | -0.0009 [-0.0017, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1532 (68) | -0.0023 [-0.0055, +0.0010] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1530 (68) | -0.0028 [-0.0070, +0.0014] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 113 (65) | -0.0092 [-0.0198, +0.0006] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2283 (68) | -0.1099 [-0.1569, -0.0579] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 178 projected goalie-games, named goalie started 74.2% (mean published P(start) 0.9111).
- participation CONFIRMED_ACTIVE: n=98, started 100.0%
- participation LIKELY_ACTIVE: n=80, started 42.5%

**Skater lineup check**: 2516 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=313, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2159, dressed 95.9%
- participation UNCERTAIN: n=38, dressed 44.7%

**Availability capture**: mean coverage 1.0, newest capture age 18.7 min (median over recent runs), runs summarised: 12.
