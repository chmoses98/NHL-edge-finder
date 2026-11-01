## NHL projection scorecard (season) — season to date

Generated 2026-11-01T23:51:59Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62358 across 97 games. Settled: 24467 (void/DNP 1027, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2351 (70) | 0.426 | -0.002 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2464 (70) | 0.407 | -0.009 | 0.219 | 81% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2351 (70) | 0.282 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2464 (70) | 0.275 | -0.002 | 0.142 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2351 (70) | 0.546 | -0.004 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2464 (70) | 0.528 | -0.011 | 0.303 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 116 (67) | 4.972 | -0.798 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 136 (70) | 4.878 | -0.459 | 3.559 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2351 (70) | 1.009 | -0.083 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2464 (70) | 1.005 | +0.029 | 0.677 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 140 (70) | 1.380 | -0.025 | 0.937 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2351 (70) | 1.871 | -0.409 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2464 (70) | 1.763 | +0.042 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2350 (70) | -0.0097 [-0.0139, -0.0054] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2350 (70) | -0.0010 [-0.0018, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1569 (70) | -0.0027 [-0.0061, +0.0007] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1567 (70) | -0.0032 [-0.0074, +0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 116 (67) | -0.0091 [-0.0195, +0.0007] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2350 (70) | -0.1086 [-0.1598, -0.0614] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 183 projected goalie-games, named goalie started 74.3% (mean published P(start) 0.9111).
- participation CONFIRMED_ACTIVE: n=101, started 100.0%
- participation LIKELY_ACTIVE: n=82, started 42.7%

**Skater lineup check**: 2588 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=313, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2231, dressed 96.0%
- participation UNCERTAIN: n=38, dressed 44.7%

**Availability capture**: mean coverage 1.0, newest capture age 16.7 min (median over recent runs), runs summarised: 12.
