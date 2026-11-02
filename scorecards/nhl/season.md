## NHL projection scorecard (season) — season to date

Generated 2026-11-02T00:48:30Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 62456 across 97 games. Settled: 24768 (void/DNP 1063, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2378 (71) | 0.428 | -0.005 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2496 (71) | 0.409 | -0.012 | 0.221 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2378 (71) | 0.283 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2496 (71) | 0.275 | -0.002 | 0.143 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2378 (71) | 0.548 | -0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2496 (71) | 0.530 | -0.014 | 0.305 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 118 (68) | 4.989 | -0.684 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 138 (71) | 4.879 | -0.380 | 3.551 | 83% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2378 (71) | 1.006 | -0.080 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2496 (71) | 1.002 | +0.033 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 142 (71) | 1.383 | -0.045 | 0.941 | 80% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2378 (71) | 1.863 | -0.403 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2496 (71) | 1.756 | +0.051 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2377 (71) | -0.0094 [-0.0132, -0.0050] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2377 (71) | -0.0010 [-0.0018, -0.0002] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1586 (71) | -0.0027 [-0.0061, +0.0005] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1584 (71) | -0.0032 [-0.0074, +0.0010] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 118 (68) | -0.0098 [-0.0196, +0.0001] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2377 (71) | -0.1078 [-0.1583, -0.0577] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 186 projected goalie-games, named goalie started 74.2% (mean published P(start) 0.9102).
- participation CONFIRMED_ACTIVE: n=102, started 100.0%
- participation LIKELY_ACTIVE: n=84, started 42.9%

**Skater lineup check**: 2624 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=313, dressed 96.8%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2265, dressed 95.9%
- participation UNCERTAIN: n=40, dressed 47.5%

**Availability capture**: mean coverage 1.0, newest capture age 17.4 min (median over recent runs), runs summarised: 12.
