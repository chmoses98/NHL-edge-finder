## NHL projection scorecard (weekly) — last 28 days

Generated 2026-10-24T21:32:45Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 28557 across 45 games. Settled: 9093 (void/DNP 382, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 874 (26) | 0.419 | +0.004 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 914 (26) | 0.404 | +0.003 | 0.216 | 83% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 874 (26) | 0.274 | +0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 914 (26) | 0.270 | +0.008 | 0.137 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 874 (26) | 0.541 | +0.013 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 914 (26) | 0.529 | +0.010 | 0.301 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 50 (26) | 5.243 | -1.813 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 51 (26) | 5.132 | -1.706 | 3.665 | 80% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 874 (26) | 1.000 | -0.145 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 914 (26) | 0.991 | -0.012 | 0.675 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 52 (26) | 1.298 | +0.121 | 0.877 | 87% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 874 (26) | 1.898 | -0.443 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 914 (26) | 1.761 | +0.011 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 51 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 52 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 873 (26) | -0.0118 [-0.0196, -0.0036] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 873 (26) | +0.0000 [-0.0013, +0.0015] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 614 (26) | +0.0018 [-0.0039, +0.0070] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 612 (26) | +0.0028 [-0.0054, +0.0097] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 50 (26) | -0.0065 [-0.0226, +0.0075] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 873 (26) | -0.1383 [-0.2045, -0.0737] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 73 projected goalie-games, named goalie started 69.9% (mean published P(start) 0.924).
- participation CONFIRMED_ACTIVE: n=43, started 100.0%
- participation LIKELY_ACTIVE: n=30, started 26.7%

**Skater lineup check**: 963 projected skaters, 94.9% dressed.
- participation CONFIRMED_ACTIVE: n=161, dressed 100.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=786, dressed 95.4%
- participation UNCERTAIN: n=12, dressed 25.0%

**Availability capture**: mean coverage 1.0, newest capture age 5.3 min (median over recent runs), runs summarised: 12.
