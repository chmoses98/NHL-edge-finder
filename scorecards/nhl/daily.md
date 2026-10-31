## NHL projection scorecard (daily) — last 7 days

Generated 2026-10-31T13:16:25Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 56826 across 92 games. Settled: 20719 (void/DNP 812, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 1145 (34) | 0.429 | -0.006 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 1204 (34) | 0.411 | -0.017 | 0.223 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 1145 (34) | 0.287 | -0.008 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 1204 (34) | 0.276 | -0.007 | 0.144 | 81% | — |
| points | PLAYER_SIM_V1 (incumbent) | 1145 (34) | 0.547 | -0.014 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 1204 (34) | 0.527 | -0.025 | 0.305 | 82% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 53 (33) | 4.819 | +0.089 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 65 (34) | 4.720 | +0.276 | 3.412 | 88% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 1145 (34) | 1.002 | -0.044 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 1204 (34) | 0.999 | +0.053 | 0.665 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 68 (34) | 1.419 | -0.125 | 0.968 | 85% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 1145 (34) | 1.841 | -0.384 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 1204 (34) | 1.760 | +0.049 | — | — | — |

**Drift checks**

- assists: **OK** — within expectations
- goals: **OK** — within expectations
- points: **OK** — within expectations
- saves: **INSUFFICIENT** — 65 settled forecasts (< 100)
- shots: **OK** — within expectations
- team_goals: **INSUFFICIENT** — 68 settled forecasts (< 100)
- toi_minutes: **OK** — within expectations

### Live promotion status (challenger vs PLAYER_SIM_V1 incumbent, identical settled player-games)

A family is **better** only if the game-clustered 95% CI of the paired loss difference is below 0 with at least 1,000 settled player-games; otherwise it is **not yet distinguishable**. Research only.

| Family | Loss | Paired n (games) | Challenger - incumbent [95% CI] | promotion_status | Readiness (frozen study) |
|---|---|---|---|---|---|
| shots | CRPS (incumbent as Poisson) | 1145 (34) | -0.0100 [-0.0145, -0.0048] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 1145 (34) | -0.0017 [-0.0027, -0.0007] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 747 (34) | -0.0030 [-0.0068, +0.0008] | **not yet distinguishable** | SHADOW VALIDATION |
| points | rung RPS | 747 (34) | -0.0045 [-0.0087, -0.0004] | **not yet distinguishable** | SHADOW VALIDATION |
| saves | rung RPS | 53 (33) | -0.0148 [-0.0300, +0.0026] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 1145 (34) | -0.0856 [-0.1667, -0.0099] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 80 projected goalie-games, named goalie started 81.2% (mean published P(start) 0.9107).
- participation CONFIRMED_ACTIVE: n=45, started 100.0%
- participation LIKELY_ACTIVE: n=35, started 57.1%

**Skater lineup check**: 1259 projected skaters, 95.6% dressed.
- participation CONFIRMED_ACTIVE: n=114, dressed 93.9%
- participation CONFIRMED_OUT: n=1, dressed 100.0%
- participation LIKELY_ACTIVE: n=1123, dressed 96.5%
- participation UNCERTAIN: n=21, dressed 57.1%

**Availability capture**: mean coverage 1.0, newest capture age 15.4 min (median over recent runs), runs summarised: 12.
