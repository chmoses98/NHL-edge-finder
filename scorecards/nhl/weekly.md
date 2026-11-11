## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-11T02:13:09Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 99614 across 158 games. Settled: 32495 (void/DNP 1324, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 3121 (93) | 0.426 | -0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3274 (93) | 0.407 | -0.011 | 0.219 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 3121 (93) | 0.283 | -0.000 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3274 (93) | 0.276 | -0.002 | 0.143 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 3121 (93) | 0.547 | -0.005 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3274 (93) | 0.529 | -0.013 | 0.304 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 152 (90) | 5.062 | -0.424 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 182 (93) | 5.000 | -0.252 | 3.654 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 3121 (93) | 1.006 | -0.077 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3274 (93) | 1.004 | +0.029 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 186 (93) | 1.341 | -0.031 | 0.917 | 82% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 3121 (93) | 1.871 | -0.376 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3274 (93) | 1.766 | +0.063 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 3118 (93) | -0.0080 [-0.0117, -0.0046] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 3118 (93) | -0.0008 [-0.0014, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 2059 (93) | -0.0030 [-0.0058, -0.0004] | **better** | SHADOW VALIDATION |
| points | rung RPS | 2059 (93) | -0.0034 [-0.0068, -0.0002] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 152 (90) | -0.0055 [-0.0143, +0.0030] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 3118 (93) | -0.1030 [-0.1436, -0.0650] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 241 projected goalie-games, named goalie started 75.5% (mean published P(start) 0.9104).
- participation CONFIRMED_ACTIVE: n=134, started 100.0%
- participation LIKELY_ACTIVE: n=107, started 44.9%

**Skater lineup check**: 3434 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2990, dressed 96.2%
- participation UNCERTAIN: n=51, dressed 43.1%

**Availability capture**: mean coverage 1.0, newest capture age 16.6 min (median over recent runs), runs summarised: 12.
