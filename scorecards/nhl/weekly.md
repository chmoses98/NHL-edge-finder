## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-05T00:44:21Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 72723 across 116 games. Settled: 30037 (void/DNP 1229, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2885 (86) | 0.428 | -0.009 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3026 (86) | 0.410 | -0.015 | 0.222 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2885 (86) | 0.285 | -0.003 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3026 (86) | 0.278 | -0.003 | 0.145 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2885 (86) | 0.551 | -0.012 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3026 (86) | 0.533 | -0.019 | 0.308 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 142 (83) | 5.106 | -0.464 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 168 (86) | 5.001 | -0.129 | 3.641 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2885 (86) | 1.007 | -0.072 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3026 (86) | 1.005 | +0.037 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 172 (86) | 1.364 | -0.061 | 0.931 | 80% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2885 (86) | 1.869 | -0.393 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3026 (86) | 1.757 | +0.062 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2882 (86) | -0.0075 [-0.0113, -0.0039] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2882 (86) | -0.0008 [-0.0014, -0.0001] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1923 (86) | -0.0030 [-0.0057, -0.0005] | **better** | SHADOW VALIDATION |
| points | rung RPS | 1922 (86) | -0.0033 [-0.0067, -0.0001] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 142 (83) | -0.0053 [-0.0144, +0.0046] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2882 (86) | -0.1110 [-0.1500, -0.0709] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 222 projected goalie-games, named goalie started 75.7% (mean published P(start) 0.9125).
- participation CONFIRMED_ACTIVE: n=126, started 100.0%
- participation LIKELY_ACTIVE: n=96, started 43.8%

**Skater lineup check**: 3176 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2737, dressed 96.0%
- participation UNCERTAIN: n=46, dressed 43.5%

**Availability capture**: mean coverage 1.0, newest capture age 4.5 min (median over recent runs), runs summarised: 12.
