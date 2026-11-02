## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-02T20:21:06Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 64505 across 101 games. Settled: 25454 (void/DNP 1079, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2442 (73) | 0.428 | -0.005 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 2567 (73) | 0.409 | -0.011 | 0.221 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2442 (73) | 0.284 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 2567 (73) | 0.276 | -0.003 | 0.144 | 79% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2442 (73) | 0.550 | -0.008 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 2567 (73) | 0.531 | -0.014 | 0.306 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 121 (70) | 4.964 | -0.706 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 142 (73) | 4.874 | -0.362 | 3.531 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2442 (73) | 1.005 | -0.078 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 2567 (73) | 1.002 | +0.034 | 0.674 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 146 (73) | 1.388 | -0.049 | 0.944 | 79% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2442 (73) | 1.853 | -0.394 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 2567 (73) | 1.747 | +0.061 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2441 (73) | -0.0090 [-0.0131, -0.0047] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2441 (73) | -0.0010 [-0.0018, -0.0003] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1620 (73) | -0.0030 [-0.0062, +0.0002] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 1618 (73) | -0.0036 [-0.0077, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 121 (70) | -0.0089 [-0.0188, +0.0012] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2441 (73) | -0.1079 [-0.1567, -0.0633] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 191 projected goalie-games, named goalie started 74.4% (mean published P(start) 0.9112).
- participation CONFIRMED_ACTIVE: n=106, started 100.0%
- participation LIKELY_ACTIVE: n=85, started 42.4%

**Skater lineup check**: 2698 projected skaters, 95.1% dressed.
- participation CONFIRMED_ACTIVE: n=349, dressed 97.1%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2301, dressed 95.9%
- participation UNCERTAIN: n=42, dressed 45.2%

**Availability capture**: mean coverage 1.0, newest capture age 13.7 min (median over recent runs), runs summarised: 12.
