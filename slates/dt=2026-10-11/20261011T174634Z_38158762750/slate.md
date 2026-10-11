# NHL slate 2026-10-11 — RESEARCH_ONLY

generated 2026-10-11T17:46:34Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2725 · contracts joined: 705 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 630, 'OK': 39, 'NO_EDGE': 36}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 107, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 147, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'goalie_saves': 4}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ WSH | 2026-10-11T21:00:00Z | T-3h | 0.588 | 0.412 | 0.179 | 6.04 | 3.29 | 2.74 | 258 (25/233) | PROJECTED/PROJECTED |
| VAN @ NYR | 2026-10-11T22:00:00Z | T-3h | 0.698 | 0.302 | 0.152 | 6.43 | 3.87 | 2.56 | 207 (25/182) | CONFIRMED/PROBABLE |
| CAR @ PHI | 2026-10-11T23:00:00Z | T-3h | 0.378 | 0.622 | 0.178 | 5.82 | 2.54 | 3.27 | 240 (25/215) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT11SEAWSH-WSH3 | game_spread | 0.224 | 0.305 | 0.287 | 31 | 70 | no | +0.062 | OK |
| KXNHLGAME-26OCT11SEAWSH-SEA | game_winner | 0.412 | 0.335 | 0.350 | 34 | 67 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH4 | team_total | 0.432 | 0.505 | 0.490 | 51 | 50 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH3 | team_total | 0.646 | 0.715 | 0.702 | 72 | 29 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH5 | team_total | 0.238 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT11SEAWSH-WSH2 | game_spread | 0.357 | 0.425 | 0.411 | 43 | 58 | no | +0.046 | OK |
| KXNHLGAME-26OCT11SEAWSH-WSH | game_winner | 0.588 | 0.655 | 0.642 | 66 | 35 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH2 | team_total | 0.839 | 0.890 | 0.881 | 90 | 12 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT11CARPHI-CAR3 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-7 | game_total | 0.421 | 0.475 | 0.464 | 48 | 53 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-4 | game_total | 0.841 | 0.885 | 0.877 | 89 | 12 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-6 | game_total | 0.533 | 0.585 | 0.575 | 59 | 42 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH6 | team_total | 0.112 | 0.160 | 0.149 | 17 | 85 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-5 | game_total | 0.755 | 0.795 | 0.787 | 80 | 21 | no | +0.023 | OK |
| KXNHLGAME-26OCT11CARPHI-CAR | game_winner | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLGAME-26OCT11CARPHI-PHI | game_winner | 0.378 | 0.335 | 0.343 | 34 | 67 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-8 | game_total | 0.235 | 0.275 | 0.267 | 28 | 73 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT11SEAWSH-SEA2 | game_spread | 0.211 | 0.175 | 0.182 | 18 | 83 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-9 | game_total | 0.162 | 0.200 | 0.192 | 21 | 81 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4 | team_total | 0.427 | 0.465 | 0.457 | 47 | 54 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT11CARPHI-5 | game_total | 0.726 | 0.760 | 0.753 | 77 | 25 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11CARPHI-4 | game_total | 0.820 | 0.845 | 0.840 | 85 | 16 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11VANNYR-8 | game_total | 0.294 | 0.260 | 0.267 | 27 | 75 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT11CARPHI-6 | game_total | 0.493 | 0.525 | 0.519 | 53 | 48 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT11CARPHI-CAR2 | game_spread | 0.384 | 0.415 | 0.409 | 42 | 59 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT11SEAWSH-SEA3 | game_spread | 0.115 | 0.095 | 0.099 | 10 | 91 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT11VANNYR-9 | game_total | 0.207 | 0.180 | 0.185 | 19 | 83 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT11VANNYR-10 | game_total | 0.102 | 0.080 | 0.084 | 9 | 93 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT11VANNYR-7 | game_total | 0.483 | 0.455 | 0.461 | 46 | 55 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR5 | team_total | 0.231 | 0.255 | 0.250 | 26 | 75 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5 | team_total | 0.122 | 0.100 | 0.104 | 11 | 91 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3 | team_total | 0.473 | 0.445 | 0.451 | 45 | 56 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT11VANNYR-6 | game_total | 0.601 | 0.575 | 0.580 | 58 | 43 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT11CARPHI-7 | game_total | 0.379 | 0.410 | 0.404 | 42 | 60 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN4 | team_total | 0.265 | 0.240 | 0.245 | 25 | 77 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-10 | game_total | 0.073 | 0.090 | 0.086 | 10 | 92 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2 | team_total | 0.716 | 0.695 | 0.699 | 70 | 31 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR2 | team_total | 0.841 | 0.860 | 0.856 | 87 | 15 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT11VANNYR-NYR3 | game_spread | 0.334 | 0.355 | 0.351 | 36 | 65 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-5 | game_total | 0.800 | 0.785 | 0.788 | 79 | 22 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT11VANNYR-NYR | game_winner | 0.698 | 0.715 | 0.712 | 72 | 29 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT11VANNYR-VAN | game_winner | 0.302 | 0.285 | 0.288 | 29 | 72 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR6 | team_total | 0.105 | 0.125 | 0.121 | 14 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-3 | game_total | 0.969 | 0.960 | 0.962 | 97 | 5 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-10 | game_total | 0.060 | 0.070 | 0.068 | 8 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT11SEAWSH-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-PHI3 | game_spread | 0.098 | 0.105 | 0.104 | 11 | 90 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-3 | game_total | 0.951 | 0.960 | 0.958 | 97 | 5 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6 | team_total | 0.049 | 0.040 | 0.042 | 5 | 97 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-PHI2 | game_spread | 0.185 | 0.170 | 0.173 | 18 | 84 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR5 | team_total | 0.350 | 0.335 | 0.338 | 34 | 67 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT11VANNYR-VAN2 | game_spread | 0.138 | 0.145 | 0.143 | 15 | 86 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI5 | team_total | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA6 | team_total | 0.057 | 0.050 | 0.051 | 6 | 96 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR3 | team_total | 0.652 | 0.670 | 0.666 | 68 | 34 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI6 | team_total | 0.046 | 0.040 | 0.041 | 5 | 97 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA5 | team_total | 0.150 | 0.140 | 0.142 | 15 | 87 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT11VANNYR-4 | game_total | 0.877 | 0.870 | 0.872 | 88 | 14 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-9 | game_total | 0.142 | 0.150 | 0.148 | 16 | 86 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT11VANNYR-NYR2 | game_spread | 0.482 | 0.495 | 0.492 | 50 | 51 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA4 | team_total | 0.305 | 0.290 | 0.293 | 30 | 72 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-8 | game_total | 0.209 | 0.220 | 0.218 | 23 | 79 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-2 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA2 | team_total | 0.752 | 0.740 | 0.742 | 75 | 27 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA3 | team_total | 0.523 | 0.510 | 0.513 | 52 | 50 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR6 | team_total | 0.187 | 0.175 | 0.177 | 19 | 84 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR2 | team_total | 0.901 | 0.900 | 0.900 | 91 | 11 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT11VANNYR-VAN3 | game_spread | 0.071 | 0.075 | 0.074 | 9 | 94 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR3 | team_total | 0.754 | 0.755 | 0.755 | 76 | 25 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI2 | team_total | 0.713 | 0.715 | 0.715 | 72 | 29 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3 | team_total | 0.469 | 0.475 | 0.474 | 48 | 53 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR4 | team_total | 0.559 | 0.555 | 0.556 | 56 | 45 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4 | team_total | 0.263 | 0.260 | 0.261 | 27 | 75 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT11SEAWSH-SEA | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11SEAWSH-TIE | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11SEAWSH-WSH | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11SEAWSH-SEA2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11SEAWSH-WSH2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ WSH | 0.588 | 0.564 | 0.179 | 0.211 | 6.04 | 6.28 | 0.961/1.015 | KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA3 +0.048 |
| VAN @ NYR | 0.698 | 0.614 | 0.152 | 0.207 | 6.43 | 6.22 | 0.988/1.026 | KXNHLSPREAD-26OCT11VANNYR-NYR2 -0.094 |
| CAR @ PHI | 0.378 | 0.478 | 0.178 | 0.227 | 5.82 | 5.88 | 0.992/0.997 | KXNHLGAME-26OCT11CARPHI-CAR -0.100 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Shane Wright: 1+ goals YES @ 14c · p 0.1917 (adj 0.1775) · $7.39 · thesis SEA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 20c · p 0.2475 (adj 0.2344) · $8.3 · thesis WSH:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1357 (adj 0.123) · $3.83 · thesis SEA:OFFENSE_4PLUS
- Washington wins by over 2.5 goals NO @ 70c · p 0.7741 (adj 0.7346) · $19.36 · thesis GAME:TIGHT
- Drew O'Connor: 1+ goals YES @ 13c · p 0.182 (adj 0.1678) · $7.64 · thesis VAN:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 60c · p 0.6749 (adj 0.6537) · $20.0 · thesis NYR:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 19c · p 0.2393 (adj 0.2257) · $7.07 · thesis VAN:OFFENSE_4PLUS
- New York R wins by over 2.5 goals NO @ 65c · p 0.7432 (adj 0.6941) · $14.25 · thesis GAME:TIGHT
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7507 (adj 0.7318) · $15.0 · thesis CAR:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 14c · p 0.1852 (adj 0.1714) · $6.19 · thesis PHI:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 75c · p 0.8066 (adj 0.7899) · $15.0 · thesis CAR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ WSH** · priced 200/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 26.2, exp saves 22.93 (sd 6.31), pull risk 0.051
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.6, exp saves 24.41 (sd 6.73), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ points | 0.298 | 0.125 | 24/99 | +0.045 | STANDARD |
| Ryan Winterton: 1+ points | 0.287 | 0.130 | 24/98 | +0.034 | STANDARD |
| Adam Larsson: 1+ assists | 0.249 | 0.095 | 17/98 | +0.069 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.170 | 0.290 | 30/72 | +0.096 | STANDARD |
| Jordan Kyrou: 1+ points | 0.335 | 0.455 | 47/56 | +0.087 | STANDARD |
| Ben Meyers: 1+ points | 0.243 | 0.125 | 23/98 | +0.000 | STANDARD |

**VAN @ NYR** · priced 148/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 25.36, exp saves 22.27 (sd 6.14), pull risk 0.05
- VAN net: Kevin Lankinen (PROBABLE) exp shots 27.14, exp saves 23.19 (sd 6.53), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 21+ saves | 0.611 | 0.490 | 50/52 | +0.093 |  |
| Pavel Dorofeyev: 1+ points | 0.496 | 0.600 | 62/42 | +0.067 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.247 | 0.345 | 36/67 | +0.068 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.139 | 0.235 | 25/78 | +0.069 | STANDARD |
| J.T. Miller: 1+ assists | 0.379 | 0.475 | 48/53 | +0.073 | STANDARD |
| Adam Fox: 1+ assists | 0.482 | 0.570 | 58/44 | +0.061 | STANDARD |

**CAR @ PHI** · priced 189/189 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 30.15, exp saves 26.02 (sd 6.92), pull risk 0.055
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.75, exp saves 19.77 (sd 5.63), pull risk 0.049

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pyotr Kochetkov: 20+ saves | 0.512 | 0.310 | 55/93 | -0.055 |  |
| Sebastian Aho: 1+ assists | 0.297 | 0.470 | 49/55 | +0.136 | STANDARD |
| Sebastian Aho: 1+ points | 0.470 | 0.630 | 64/38 | +0.133 | STANDARD |
| Sebastian Aho: 2+ points | 0.141 | 0.265 | 28/75 | +0.096 | STANDARD |
| Jordan Martinook: 1+ assists | 0.205 | 0.110 | 20/98 | -0.006 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.474 | 0.565 | 58/45 | +0.059 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
