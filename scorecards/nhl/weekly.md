## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-08T23:25:20Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 94042 across 148 games. Settled: 32130 (void/DNP 1322, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3085 (92) | 0.427 | -0.006 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3238 (92) | 0.407 | -0.012 | 0.220 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3085 (92) | 0.284 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3238 (92) | 0.276 | -0.002 | 0.144 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3085 (92) | 0.547 | -0.007 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3238 (92) | 0.529 | -0.015 | 0.305 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 151 (89) | 5.085 | -0.437 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 180 (92) | 5.012 | -0.238 | 3.666 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3085 (92) | 1.006 | -0.078 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3238 (92) | 1.004 | +0.028 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 184 (92) | 1.340 | -0.038 | 0.917 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3085 (92) | 1.875 | -0.382 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3238 (92) | 1.768 | +0.061 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 3082 (92) | -0.0079 [-0.0115, -0.0042] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3082 (92) | -0.0008 [-0.0015, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2039 (92) | -0.0031 [-0.0056, -0.0005] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2038 (92) | -0.0034 [-0.0065, +0.0001] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 151 (89) | -0.0057 [-0.0144, +0.0027] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3082 (92) | -0.1059 [-0.1424, -0.0658] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 237 projected goalie-games, named goalie started 75.9% (mean published P(start) 0.9123).
- participation CONFIRMED_ACTIVE: n=134, started 100.0%
- participation LIKELY_ACTIVE: n=103, started 44.7%

**Skater lineup check**: 3398 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2954, dressed 96.1%
- participation UNCERTAIN: n=51, dressed 43.1%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
