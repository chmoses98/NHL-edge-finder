## NHL projection scorecard (daily) — last 7 days

Generated 2026-11-01T20:04:34Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62040 across 97 games. Settled: 23766 (void/DNP 1016, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1101 (33) | 0.428 | -0.007 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1158 (33) | 0.409 | -0.019 | 0.222 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1101 (33) | 0.288 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1158 (33) | 0.277 | -0.008 | 0.145 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1101 (33) | 0.553 | -0.015 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1158 (33) | 0.533 | -0.028 | 0.309 | 81% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 48 (30) | 4.775 | +0.240 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.763 | +0.479 | 3.534 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1101 (33) | 1.014 | -0.050 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1158 (33) | 1.011 | +0.060 | 0.675 | 79% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.353 | -0.117 | 0.913 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1101 (33) | 1.902 | -0.380 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1158 (33) | 1.809 | +0.062 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 64 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 66 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1101 (33) | -0.0078 [-0.0137, -0.0017] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1101 (33) | -0.0015 [-0.0025, -0.0005] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 703 (33) | -0.0047 [-0.0089, -0.0010] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 703 (33) | -0.0068 [-0.0115, -0.0022] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 48 (30) | -0.0068 [-0.0225, +0.0100] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1101 (33) | -0.0940 [-0.1747, -0.0097] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 84 projected goalie-games, named goalie started 76.2% (mean published P(start) 0.8986).
- participation CONFIRMED_ACTIVE: n=42, started 100.0%
- participation LIKELY_ACTIVE: n=42, started 52.4%

**Skater lineup check**: 1221 projected skaters, 94.8% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.0%
- participation CONFIRMED_OUT: n=2, dressed 100.0%
- participation LIKELY_ACTIVE: n=1083, dressed 95.8%
- participation UNCERTAIN: n=22, dressed 54.5%

**Availability capture**: mean coverage 1.0, newest capture age 17.9 min (median over recent runs), runs summarised: 12.
