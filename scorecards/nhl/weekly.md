## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-07T23:07:23Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 89284 across 142 games. Settled: 31434 (void/DNP 1285, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3018 (90) | 0.427 | -0.006 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3168 (90) | 0.408 | -0.012 | 0.220 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3018 (90) | 0.284 | -0.001 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3168 (90) | 0.277 | -0.002 | 0.144 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3018 (90) | 0.550 | -0.007 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3168 (90) | 0.531 | -0.015 | 0.306 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 148 (87) | 4.996 | -0.479 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 176 (90) | 4.884 | -0.182 | 3.567 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3018 (90) | 1.006 | -0.072 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3168 (90) | 1.004 | +0.036 | 0.673 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 180 (90) | 1.349 | -0.041 | 0.922 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3018 (90) | 1.879 | -0.389 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3168 (90) | 1.773 | +0.057 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 3015 (90) | -0.0078 [-0.0113, -0.0042] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3015 (90) | -0.0008 [-0.0015, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2003 (90) | -0.0032 [-0.0060, -0.0006] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2002 (90) | -0.0036 [-0.0070, -0.0003] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 148 (87) | -0.0059 [-0.0147, +0.0025] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3015 (90) | -0.1054 [-0.1470, -0.0673] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 231 projected goalie-games, named goalie started 76.2% (mean published P(start) 0.9127).
- participation CONFIRMED_ACTIVE: n=131, started 100.0%
- participation LIKELY_ACTIVE: n=100, started 45.0%

**Skater lineup check**: 3324 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2882, dressed 96.1%
- participation UNCERTAIN: n=49, dressed 42.9%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
