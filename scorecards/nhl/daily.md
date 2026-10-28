## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-28T01:08:46Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 40422 across 64 games. Settled: 14051 (void/DNP 539, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 882 (26) | 0.436 | -0.015 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 921 (26) | 0.417 | -0.018 | 0.228 | 79% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 882 (26) | 0.283 | -0.005 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 921 (26) | 0.277 | -0.006 | 0.144 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 882 (26) | 0.551 | -0.021 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 921 (26) | 0.534 | -0.025 | 0.311 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 45 (26) | 4.964 | -1.368 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 50 (26) | 4.891 | -0.944 | 3.572 | 88% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 882 (26) | 1.006 | -0.096 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 921 (26) | 1.006 | -0.002 | 0.682 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 52 (26) | 1.551 | -0.123 | 1.074 | 73% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 882 (26) | 1.787 | -0.409 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 921 (26) | 1.704 | +0.047 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 50 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 52 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 882 (26) | -0.0116 [-0.0188, -0.0043] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 882 (26) | -0.0007 [-0.0018, +0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 627 (26) | +0.0005 [-0.0059, +0.0064] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 627 (26) | +0.0004 [-0.0073, +0.0080] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 45 (26) | -0.0164 [-0.0341, +0.0018] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 882 (26) | -0.0787 [-0.1443, -0.0168] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 66 projected goalie-games, named goalie started 75.8% (mean published P(start) 0.9077).
- participation CONFIRMED_ACTIVE: n=35, started 100.0%
- participation LIKELY_ACTIVE: n=31, started 48.4%

**Skater lineup check**: 958 projected skaters, 96.1% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=742, dressed 97.0%
- participation UNCERTAIN: n=13, dressed 30.8%

**Availability capture**: mean coverage 1.0, newest capture age 11.6 min (median over recent runs), runs summarised: 12.
