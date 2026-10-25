## NHL projection scorecard (weekly) — last 28 days

Generated 2026-10-25T01:11:52Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 28698 across 45 games. Settled: 9452 (void/DNP 393, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 909 (27) | 0.417 | +0.006 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 950 (27) | 0.402 | +0.005 | 0.214 | 83% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 909 (27) | 0.272 | +0.010 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 950 (27) | 0.269 | +0.010 | 0.136 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 909 (27) | 0.539 | +0.016 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 950 (27) | 0.526 | +0.014 | 0.298 | 83% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 51 (27) | 5.358 | -1.559 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 52 (27) | 5.239 | -1.468 | 3.736 | 79% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 909 (27) | 1.002 | -0.119 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 950 (27) | 0.992 | +0.009 | 0.673 | 81% | — |
| team_goals | pf-nhl-F_stack (challenger) | 54 (27) | 1.284 | +0.151 | 0.871 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 909 (27) | 1.871 | -0.430 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 950 (27) | 1.739 | +0.018 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 908 (27) | -0.0115 [-0.0188, -0.0040] | **not yet distinguishable** | SHADOW VALIDATION |
| goals | rung RPS | 908 (27) | +0.0001 [-0.0012, +0.0014] | **not yet distinguishable** | SHADOW VALIDATION |
| assists | rung RPS | 633 (27) | +0.0013 [-0.0044, +0.0066] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 631 (27) | +0.0027 [-0.0050, +0.0099] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 51 (27) | -0.0072 [-0.0235, +0.0063] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 908 (27) | -0.1359 [-0.1959, -0.0750] | **not yet distinguishable** | SHADOW VALIDATION |

**Goalie starter check**: 75 projected goalie-games, named goalie started 69.3% (mean published P(start) 0.9232).
- participation CONFIRMED_ACTIVE: n=44, started 100.0%
- participation LIKELY_ACTIVE: n=31, started 25.8%

**Skater lineup check**: 1000 projected skaters, 95.0% dressed.
- participation CONFIRMED_ACTIVE: n=180, dressed 99.4%
- participation CONFIRMED_OUT: n=4, dressed 0.0%
- participation LIKELY_ACTIVE: n=804, dressed 95.5%
- participation UNCERTAIN: n=12, dressed 25.0%

**Availability capture**: mean coverage 1.0, newest capture age 7.9 min (median over recent runs), runs summarised: 12.
