## NHL projection scorecard (season) — season to date

Generated 2026-11-08T09:33:51Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 91305 across 148 games. Settled: 31785 (void/DNP 1296, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3052 (91) | 0.427 | -0.007 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3203 (91) | 0.408 | -0.013 | 0.221 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3052 (91) | 0.284 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3203 (91) | 0.277 | -0.002 | 0.144 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3052 (91) | 0.549 | -0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3203 (91) | 0.531 | -0.016 | 0.306 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 150 (88) | 5.051 | -0.373 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 178 (91) | 4.930 | -0.102 | 3.607 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3052 (91) | 1.005 | -0.072 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3203 (91) | 1.002 | +0.035 | 0.672 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 182 (91) | 1.339 | -0.046 | 0.917 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3052 (91) | 1.874 | -0.389 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3203 (91) | 1.767 | +0.056 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 3049 (91) | -0.0076 [-0.0112, -0.0040] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3049 (91) | -0.0008 [-0.0015, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2023 (91) | -0.0031 [-0.0058, -0.0004] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2022 (91) | -0.0034 [-0.0069, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 150 (88) | -0.0058 [-0.0147, +0.0033] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3049 (91) | -0.1058 [-0.1474, -0.0695] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 234 projected goalie-games, named goalie started 76.1% (mean published P(start) 0.9122).
- participation CONFIRMED_ACTIVE: n=132, started 100.0%
- participation LIKELY_ACTIVE: n=102, started 45.1%

**Skater lineup check**: 3360 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2918, dressed 96.1%
- participation UNCERTAIN: n=49, dressed 42.9%

**Availability capture**: mean coverage 1.0, newest capture age 4.4 min (median over recent runs), runs summarised: 12.
