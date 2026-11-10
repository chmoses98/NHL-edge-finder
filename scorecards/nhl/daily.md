## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-10T00:56:21Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 95729 across 151 games. Settled: 32495 (void/DNP 1324, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 610 (18) | 0.420 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 635 (18) | 0.403 | -0.008 | 0.215 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 610 (18) | 0.284 | +0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 635 (18) | 0.279 | +0.002 | 0.144 | 82% | — |
| points | PLAYER_SIM_V1 (incumbent) | 610 (18) | 0.549 | +0.004 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 635 (18) | 0.532 | -0.007 | 0.302 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 29 (18) | 5.684 | +0.590 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 36 (18) | 5.734 | +0.133 | 4.319 | 75% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 610 (18) | 1.012 | -0.080 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 635 (18) | 1.015 | +0.004 | 0.677 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 36 (18) | 1.169 | +0.029 | 0.824 | 86% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 610 (18) | 1.899 | -0.279 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 635 (18) | 1.822 | +0.114 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 36 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 36 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 608 (18) | -0.0061 [-0.0129, +0.0000] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 608 (18) | -0.0004 [-0.0022, +0.0012] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 385 (18) | -0.0026 [-0.0063, +0.0016] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 387 (18) | -0.0027 [-0.0071, +0.0016] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 29 (18) | +0.0054 [-0.0093, +0.0227] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 608 (18) | -0.0636 [-0.1248, +0.0086] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 45 projected goalie-games, named goalie started 80.0% (mean published P(start) 0.9072).
- participation CONFIRMED_ACTIVE: n=25, started 100.0%
- participation LIKELY_ACTIVE: n=20, started 55.0%

**Skater lineup check**: 662 projected skaters, 95.9% dressed.
- participation CONFIRMED_ACTIVE: n=38, dressed 94.7%
- participation LIKELY_ACTIVE: n=615, dressed 96.9%
- participation UNCERTAIN: n=9, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
