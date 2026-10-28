## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-28T00:39:32Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 40372 across 64 games. Settled: 14051 (void/DNP 539, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 918 (27) | 0.434 | -0.017 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 957 (27) | 0.416 | -0.020 | 0.228 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 918 (27) | 0.283 | -0.006 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 957 (27) | 0.276 | -0.006 | 0.144 | 82% | — |
| points | PLAYER_SIM_V1 (incumbent) | 918 (27) | 0.548 | -0.022 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 957 (27) | 0.531 | -0.027 | 0.309 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 47 (27) | 4.877 | -1.435 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 52 (27) | 4.814 | -1.019 | 3.523 | 87% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 918 (27) | 1.011 | -0.100 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 957 (27) | 1.007 | -0.005 | 0.686 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 54 (27) | 1.506 | -0.129 | 1.051 | 78% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 918 (27) | 1.810 | -0.417 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 957 (27) | 1.715 | +0.031 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 52 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 54 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 918 (27) | -0.0123 [-0.0195, -0.0044] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 918 (27) | -0.0008 [-0.0019, +0.0003] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 650 (27) | +0.0005 [-0.0049, +0.0054] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 650 (27) | +0.0002 [-0.0071, +0.0070] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 47 (27) | -0.0147 [-0.0311, +0.0016] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 918 (27) | -0.0893 [-0.1523, -0.0274] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 68 projected goalie-games, named goalie started 76.5% (mean published P(start) 0.9074).
- participation CONFIRMED_ACTIVE: n=36, started 100.0%
- participation LIKELY_ACTIVE: n=32, started 50.0%

**Skater lineup check**: 995 projected skaters, 96.2% dressed.
- participation CONFIRMED_ACTIVE: n=199, dressed 99.0%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=779, dressed 97.0%
- participation UNCERTAIN: n=13, dressed 30.8%

**Availability capture**: mean coverage 1.0, newest capture age 12.4 min (median over recent runs), runs summarised: 12.
