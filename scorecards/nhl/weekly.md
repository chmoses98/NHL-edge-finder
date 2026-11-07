## NHL projection scorecard (weekly) — last 28 days

Generated 2026-11-07T15:10:54Z. Research only; nothing here is a betting signal.

Archived pregame forecasts: 87029 across 142 games. Settled: 30739 (void/DNP 1274, stat corrections 0).

| Stat | Model | n (games) | MAE | Bias | CRPS | 80% range caught | vs incumbent (CRPS) |
|---|---|---|---|---|---|---|---|
| assists | PLAYER_SIM_V1 (incumbent) | 2952 (88) | 0.428 | -0.008 | — | — |  |
| assists | pf-nhl-F_stack (challenger) | 3097 (88) | 0.409 | -0.014 | 0.222 | 80% | — |
| goals | PLAYER_SIM_V1 (incumbent) | 2952 (88) | 0.285 | -0.002 | — | — |  |
| goals | pf-nhl-F_stack (challenger) | 3097 (88) | 0.277 | -0.003 | 0.144 | 80% | — |
| points | PLAYER_SIM_V1 (incumbent) | 2952 (88) | 0.551 | -0.010 | — | — |  |
| points | pf-nhl-F_stack (challenger) | 3097 (88) | 0.533 | -0.017 | 0.308 | 80% | — |
| saves | PLAYER_SIM_V1 (incumbent) | 146 (85) | 5.028 | -0.450 | — | — |  |
| saves | pf-nhl-F_stack (challenger) | 172 (88) | 4.935 | -0.124 | 3.600 | 84% | — |
| shots | PLAYER_SIM_V1 (incumbent) | 2952 (88) | 1.006 | -0.070 | — | — |  |
| shots | pf-nhl-F_stack (challenger) | 3097 (88) | 1.004 | +0.038 | 0.673 | 80% | — |
| team_goals | pf-nhl-F_stack (challenger) | 176 (88) | 1.363 | -0.051 | 0.929 | 81% | — |
| toi_minutes | PLAYER_SIM_V1 (incumbent) | 2952 (88) | 1.871 | -0.393 | — | — |  |
| toi_minutes | pf-nhl-E_lightgbm (challenger) | 3097 (88) | 1.761 | +0.055 | — | — | — |

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
| shots | CRPS (incumbent as Poisson) | 2949 (88) | -0.0078 [-0.0113, -0.0042] | **better** | SHADOW VALIDATION |
| goals | rung RPS | 2949 (88) | -0.0009 [-0.0016, -0.0003] | **better** | SHADOW VALIDATION |
| assists | rung RPS | 1969 (88) | -0.0031 [-0.0056, -0.0004] | **better** | SHADOW VALIDATION |
| points | rung RPS | 1968 (88) | -0.0034 [-0.0066, -0.0002] | **better** | SHADOW VALIDATION |
| saves | rung RPS | 146 (85) | -0.0058 [-0.0147, +0.0022] | **not yet distinguishable** | NEEDS IMPROVEMENT |
| team_goals | n/a | 0 (0) | — | **no incumbent** | SHADOW VALIDATION |
| toi_minutes | absolute error | 2949 (88) | -0.1098 [-0.1501, -0.0690] | **better** | SHADOW VALIDATION |

**Goalie starter check**: 226 projected goalie-games, named goalie started 76.1% (mean published P(start) 0.9128).
- participation CONFIRMED_ACTIVE: n=128, started 100.0%
- participation LIKELY_ACTIVE: n=98, started 44.9%

**Skater lineup check**: 3252 projected skaters, 95.2% dressed.
- participation CONFIRMED_ACTIVE: n=387, dressed 96.9%
- participation CONFIRMED_OUT: n=6, dressed 33.3%
- participation LIKELY_ACTIVE: n=2812, dressed 96.0%
- participation UNCERTAIN: n=47, dressed 42.5%

**Availability capture**: mean coverage 1.0, newest capture age 12.5 min (median over recent runs), runs summarised: 12.
