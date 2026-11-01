# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T21:24:49Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 2 · markets on board: 2552 · contracts joined: 440 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 390, 'OK': 29, 'NO_EDGE': 21}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 59, 'game_early_goal': 2, 'first_goal': 69, 'game_winner': 4, 'player_goals': 119, 'game_overtime': 2, 'player_points': 87, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ NYR | 2026-11-01T23:00:00Z | T-90m | 0.516 | 0.484 | 0.171 | 6.46 | 3.28 | 3.19 | 222 (25/197) | CONFIRMED/CONFIRMED |
| OTT @ ANA | 2026-11-02T01:00:00Z | T-3h | 0.562 | 0.438 | 0.167 | 6.83 | 3.62 | 3.22 | 218 (25/193) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.562 | 0.465 | 0.484 | 47 | 54 | yes | +0.075 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.438 | 0.535 | 0.516 | 54 | 47 | no | +0.075 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.347 | 0.275 | 0.289 | 28 | 73 | yes | +0.053 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.500 | 0.435 | 0.448 | 44 | 57 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.624 | 0.690 | 0.677 | 70 | 32 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.823 | 0.880 | 0.870 | 89 | 13 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.411 | 0.465 | 0.454 | 47 | 54 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.305 | 0.255 | 0.265 | 26 | 75 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.157 | 0.110 | 0.118 | 12 | 90 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.704 | 0.650 | 0.661 | 66 | 36 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.230 | 0.275 | 0.266 | 28 | 73 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-5 | game_total | 0.802 | 0.835 | 0.829 | 84 | 17 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR3 | game_spread | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.905 | 0.925 | 0.921 | 93 | 8 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR2 | team_total | 0.832 | 0.855 | 0.851 | 86 | 15 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR3 | team_total | 0.635 | 0.670 | 0.663 | 68 | 34 | no | +0.009 | OK |
| KXNHLGAME-26NOV01EDMNYR-EDM | game_winner | 0.484 | 0.455 | 0.461 | 46 | 55 | yes | +0.007 | OK |
| KXNHLGAME-26NOV01EDMNYR-NYR | game_winner | 0.516 | 0.545 | 0.539 | 55 | 46 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.006 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR2 | game_spread | 0.302 | 0.325 | 0.320 | 33 | 68 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT6 | team_total | 0.111 | 0.125 | 0.122 | 13 | 88 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-7 | game_total | 0.491 | 0.515 | 0.510 | 52 | 49 | no | +0.002 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-EDM2 | game_spread | 0.275 | 0.255 | 0.259 | 26 | 75 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.870 | 0.845 | 0.850 | 86 | 17 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-4 | game_total | 0.874 | 0.890 | 0.887 | 90 | 12 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.354 | 0.335 | 0.339 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-9 | game_total | 0.211 | 0.225 | 0.222 | 23 | 78 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM6 | team_total | 0.103 | 0.090 | 0.093 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-10 | game_total | 0.135 | 0.125 | 0.127 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR5 | team_total | 0.240 | 0.260 | 0.256 | 27 | 75 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-9 | game_total | 0.260 | 0.245 | 0.248 | 25 | 76 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-6 | game_total | 0.603 | 0.620 | 0.617 | 63 | 39 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-5 | game_total | 0.841 | 0.850 | 0.848 | 86 | 16 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM2 | team_total | 0.821 | 0.835 | 0.832 | 85 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-3 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR6 | team_total | 0.115 | 0.120 | 0.119 | 13 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-8 | game_total | 0.297 | 0.305 | 0.303 | 31 | 70 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV01EDMNYR-EDM3 | game_spread | 0.168 | 0.165 | 0.166 | 17 | 84 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM3 | team_total | 0.623 | 0.610 | 0.613 | 62 | 40 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-3 | game_total | 0.972 | 0.975 | 0.974 | 99 | 4 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-7 | game_total | 0.548 | 0.555 | 0.554 | 56 | 45 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM5 | team_total | 0.222 | 0.220 | 0.220 | 23 | 79 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-6 | game_total | 0.655 | 0.660 | 0.659 | 67 | 35 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM4 | team_total | 0.403 | 0.400 | 0.401 | 41 | 61 |  | -0.024 | NO_EDGE |
| KXNHL1P-26NOV01EDMNYR-EDM | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01EDMNYR-NYR | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01EDMNYR-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01EDMNYR-EDM2 | period_spread |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01EDMNYR-NYR2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01EDMNYR-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01EDMNYR-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01EDMNYR-3 | period_total |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01EDMNYR-EDM | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01EDMNYR-NYR | period_winner |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01EDMNYR-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01EDMNYR-EDM2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01EDMNYR-NYR2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01EDMNYR-1 | period_total |  | 0.910 |  | 92 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01EDMNYR-2 | period_total |  | 0.635 |  | 65 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01EDMNYR-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01EDMNYR-EDM | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01EDMNYR-NYR | period_winner |  | 0.400 |  | 42 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01EDMNYR-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01EDMNYR-EDM2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01EDMNYR-NYR2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01EDMNYR-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01EDMNYR-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01EDMNYR-3 | period_total |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1 | player_assists |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-3 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMEBOUCHARD2-1 | player_assists |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMEBOUCHARD2-2 | player_assists |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMEBOUCHARD2-3 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ NYR | 0.516 | 0.503 | 0.171 | 0.211 | 6.46 | 6.68 | 0.988/1.000 | KXNHLTOTAL-26NOV01EDMNYR-7 +0.039 |
| OTT @ ANA | 0.562 | 0.586 | 0.167 | 0.213 | 6.83 | 6.57 | 0.968/1.034 | KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Formenton: 1+ goals YES @ 11c · p 0.1674 (adj 0.1518) · $8.74 · thesis EDM:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 9c · p 0.1364 (adj 0.1235) · $7.03 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ assists YES @ 26c · p 0.3549 (adj 0.3049) · $9.76 · thesis EDM:OFFENSE_4PLUS
- Dylan Garand: 24+ saves YES @ 42c · p 0.5694 (adj 0.4658) · $14.38 · thesis NYR:NET_HIGH_VOLUME
- A.J. Greer: 1+ goals YES @ 16c · p 0.2467 (adj 0.2225) · $11.6 · thesis ANA:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8805 (adj 0.8327) · $15.0 · thesis ANA:WINS
- Ottawa over 4.5 goals scored NO @ 73c · p 0.8151 (adj 0.7701) · $15.0 · thesis ANA:WINS
- Fabian Zetterlund: 1+ goals YES @ 17c · p 0.1996 (adj 0.191) · $3.43 · thesis OTT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**EDM @ NYR** · priced 163/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.57, exp saves 24.68 (sd 6.89), pull risk 0.069
- EDM net: Matt Tomkins (CONFIRMED) exp shots 25.83, exp saves 22.18 (sd 6.28), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 24+ saves | 0.569 | 0.410 | 42/60 | +0.132 |  |
| Vladislav Gavrikov: 1+ assists | 0.375 | 0.250 | 26/76 | +0.102 | STANDARD |
| Connor McDavid: 2+ assists | 0.181 | 0.295 | 30/71 | +0.094 | STANDARD |
| Connor McDavid: 2+ points | 0.381 | 0.495 | 50/51 | +0.091 | STANDARD |
| Connor McDavid: 1+ assists | 0.542 | 0.655 | 66/35 | +0.092 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.427 | 0.320 | 33/69 | +0.082 | STANDARD |

**OTT @ ANA** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.52), pull risk 0.056
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.68, exp saves 23.48 (sd 6.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.247 | 0.150 | 16/86 | +0.077 | STANDARD |
| Jake Sanderson: 1+ points | 0.445 | 0.540 | 55/47 | +0.068 | STANDARD |
| Thomas Chabot: 1+ assists | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Jake Sanderson: 1+ assists | 0.361 | 0.455 | 47/56 | +0.062 | STANDARD |
| Jackson LaCombe: 1+ points | 0.643 | 0.555 | 57/46 | +0.056 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.580 | 0.495 | 50/51 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
