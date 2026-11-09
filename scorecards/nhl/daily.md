## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-09T21:18:40Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 94609 across 151 games. Settled: 32495 (void/DNP 1324, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 679 (20) | 0.419 | -0.001 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 707 (20) | 0.400 | -0.009 | 0.214 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 679 (20) | 0.281 | +0.007 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 707 (20) | 0.276 | +0.002 | 0.142 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 679 (20) | 0.536 | +0.006 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 707 (20) | 0.521 | -0.008 | 0.297 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 31 (20) | 5.444 | +0.678 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 40 (20) | 5.445 | +0.141 | 4.089 | 78% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 679 (20) | 1.009 | -0.073 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 707 (20) | 1.011 | +0.011 | 0.674 | 82% | — |
| team_goals | pf-nhl-F_stack (challenger) | 40 (20) | 1.169 | +0.036 | 0.816 | 95% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 679 (20) | 1.933 | -0.313 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 707 (20) | 1.837 | +0.072 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 40 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 40 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 677 (20) | -0.0043 [-0.0105, +0.0018] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 677 (20) | -0.0002 [-0.0017, +0.0014] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 439 (20) | -0.0031 [-0.0062, +0.0006] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 441 (20) | -0.0026 [-0.0069, +0.0016] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 31 (20) | +0.0077 [-0.0072, +0.0234] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 677 (20) | -0.0854 [-0.1502, -0.0134] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 50 projected goalie-games, named goalie started 80.0% (mean published P(start) 0.9073).
- participation CONFIRMED_ACTIVE: n=28, started 100.0%
- participation LIKELY_ACTIVE: n=22, started 54.5%

**Skater lineup check**: 736 projected skaters, 96.1% dressed.
- participation CONFIRMED_ACTIVE: n=38, dressed 94.7%
- participation LIKELY_ACTIVE: n=689, dressed 97.0%
- participation UNCERTAIN: n=9, dressed 33.3%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
