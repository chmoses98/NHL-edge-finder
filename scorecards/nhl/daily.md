## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-26T00:52:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 32212 across 50 games. Settled: 12293 (void/DNP 481, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1116 (33) | 0.424 | -0.003 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1166 (33) | 0.408 | -0.004 | 0.219 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1116 (33) | 0.279 | +0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1166 (33) | 0.275 | +0.002 | 0.141 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1116 (33) | 0.541 | -0.001 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1166 (33) | 0.527 | -0.002 | 0.302 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 61 (33) | 4.959 | -1.410 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 64 (33) | 4.702 | -1.398 | 3.382 | 86% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1116 (33) | 1.002 | -0.110 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1166 (33) | 0.999 | +0.002 | 0.677 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 66 (33) | 1.347 | +0.011 | 0.927 | 83% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1116 (33) | 1.884 | -0.443 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1166 (33) | 1.756 | +0.019 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 1116 (33) | -0.0114 [-0.0180, -0.0052] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1116 (33) | -0.0004 [-0.0015, +0.0007] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 785 (33) | -0.0002 [-0.0055, +0.0047] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 783 (33) | +0.0001 [-0.0064, +0.0064] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 61 (33) | -0.0101 [-0.0255, +0.0020] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1116 (33) | -0.1274 [-0.1857, -0.0710] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 87 projected goalie-games, named goalie started 73.6% (mean published P(start) 0.9258).
- participation CONFIRMED_ACTIVE: n=53, started 100.0%
- participation LIKELY_ACTIVE: n=34, started 32.4%

**Skater lineup check**: 1223 projected skaters, 95.3% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=1004, dressed 96.0%
- participation UNCERTAIN: n=16, dressed 31.2%

**Availability capture**: mean coverage 1.0, newest capture age 13.4 min (median over recent runs), runs summarised: 12.
