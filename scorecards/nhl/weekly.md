## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-07T21:05:01Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 89158 across 142 games. Settled: 31084 (void/DNP 1285, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2985 (89) | 0.428 | -0.007 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3132 (89) | 0.409 | -0.013 | 0.221 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2985 (89) | 0.285 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3132 (89) | 0.277 | -0.003 | 0.144 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2985 (89) | 0.551 | -0.009 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3132 (89) | 0.533 | -0.016 | 0.307 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 147 (86) | 5.016 | -0.469 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 174 (89) | 4.920 | -0.164 | 3.587 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2985 (89) | 1.006 | -0.070 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3132 (89) | 1.003 | +0.037 | 0.672 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 178 (89) | 1.353 | -0.053 | 0.924 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2985 (89) | 1.882 | -0.386 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3132 (89) | 1.775 | +0.060 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2982 (89) | -0.0078 [-0.0118, -0.0042] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2982 (89) | -0.0008 [-0.0015, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1988 (89) | -0.0031 [-0.0056, -0.0004] | **better** | SHADOW VALIDATION |
| points | rung RPS | 1987 (89) | -0.0035 [-0.0068, -0.0001] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 147 (86) | -0.0060 [-0.0151, +0.0023] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2982 (89) | -0.1078 [-0.1473, -0.0652] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 229 projected goalie-games, named goalie started 76.0% (mean published P(start) 0.913).
- participation CONFIRMED_ACTIVE: n=130, started 100.0%
- participation LIKELY_ACTIVE: n=99, started 44.4%

**Skater lineup check**: 3288 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2847, dressed 96.1%
- participation UNCERTAIN: n=48, dressed 41.7%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
