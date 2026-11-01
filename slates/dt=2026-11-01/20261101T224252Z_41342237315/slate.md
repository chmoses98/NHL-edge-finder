# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T22:42:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 2 · markets on board: 2506 · contracts joined: 436 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 386, 'NO_EDGE': 21, 'OK': 29}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 59, 'game_early_goal': 2, 'first_goal': 67, 'game_winner': 4, 'player_goals': 117, 'game_overtime': 2, 'player_points': 87, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ NYR | 2026-11-01T23:00:00Z | T-10m | 0.516 | 0.484 | 0.171 | 6.46 | 3.28 | 3.19 | 218 (25/193) | CONFIRMED/CONFIRMED |
| OTT @ ANA | 2026-11-02T01:00:00Z | T-90m | 0.562 | 0.438 | 0.167 | 6.83 | 3.62 | 3.22 | 218 (25/193) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.562 | 0.465 | 0.484 | 47 | 54 | yes | +0.075 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.438 | 0.535 | 0.516 | 54 | 47 | no | +0.075 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.347 | 0.275 | 0.289 | 28 | 73 | yes | +0.053 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.500 | 0.435 | 0.448 | 44 | 57 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.305 | 0.245 | 0.256 | 25 | 76 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.823 | 0.880 | 0.870 | 89 | 13 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.411 | 0.465 | 0.454 | 47 | 54 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.624 | 0.680 | 0.669 | 69 | 33 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.157 | 0.110 | 0.118 | 12 | 90 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.704 | 0.650 | 0.661 | 66 | 36 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-5 | game_total | 0.802 | 0.840 | 0.833 | 85 | 17 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.230 | 0.270 | 0.262 | 28 | 74 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR3 | game_spread | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-4 | game_total | 0.874 | 0.895 | 0.891 | 90 | 11 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR2 | team_total | 0.832 | 0.855 | 0.851 | 86 | 15 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR3 | team_total | 0.635 | 0.665 | 0.659 | 67 | 34 | no | +0.009 | OK |
| KXNHLGAME-26NOV01EDMNYR-NYR | game_winner | 0.516 | 0.545 | 0.539 | 55 | 46 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR5 | team_total | 0.240 | 0.265 | 0.260 | 27 | 74 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.006 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR2 | game_spread | 0.302 | 0.325 | 0.320 | 33 | 68 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT6 | team_total | 0.111 | 0.125 | 0.122 | 13 | 88 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-7 | game_total | 0.491 | 0.515 | 0.510 | 52 | 49 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.870 | 0.850 | 0.854 | 86 | 16 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-5 | game_total | 0.841 | 0.855 | 0.852 | 86 | 15 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-6 | game_total | 0.603 | 0.625 | 0.621 | 63 | 38 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.905 | 0.915 | 0.913 | 92 | 9 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.354 | 0.335 | 0.339 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-9 | game_total | 0.211 | 0.225 | 0.222 | 23 | 78 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM6 | team_total | 0.103 | 0.090 | 0.093 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-10 | game_total | 0.135 | 0.125 | 0.127 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-9 | game_total | 0.260 | 0.245 | 0.248 | 25 | 76 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26NOV01EDMNYR-EDM | game_winner | 0.484 | 0.465 | 0.469 | 47 | 54 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-3 | game_total | 0.972 | 0.980 | 0.979 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM5 | team_total | 0.222 | 0.235 | 0.232 | 24 | 77 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV01EDMNYR-EDM2 | game_spread | 0.275 | 0.265 | 0.267 | 27 | 74 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-10 | game_total | 0.107 | 0.105 | 0.105 | 11 | 90 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM4 | team_total | 0.403 | 0.415 | 0.413 | 42 | 59 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM2 | team_total | 0.821 | 0.835 | 0.832 | 85 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-3 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-6 | game_total | 0.655 | 0.665 | 0.663 | 67 | 34 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR6 | team_total | 0.115 | 0.120 | 0.119 | 13 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-8 | game_total | 0.297 | 0.305 | 0.303 | 31 | 70 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV01EDMNYR-EDM3 | game_spread | 0.168 | 0.165 | 0.166 | 17 | 84 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-7 | game_total | 0.548 | 0.555 | 0.554 | 56 | 45 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM3 | team_total | 0.623 | 0.630 | 0.629 | 64 | 38 |  | -0.019 | NO_EDGE |
| KXNHL1P-26NOV01EDMNYR-EDM | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01EDMNYR-NYR | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV01EDMNYR-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01EDMNYR-EDM2 | period_spread |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV01EDMNYR-NYR2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01EDMNYR-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01EDMNYR-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV01EDMNYR-3 | period_total |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01EDMNYR-EDM | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01EDMNYR-NYR | period_winner |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV01EDMNYR-TIE | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01EDMNYR-EDM2 | period_spread |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV01EDMNYR-NYR2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01EDMNYR-1 | period_total |  | 0.910 |  | 92 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01EDMNYR-2 | period_total |  | 0.640 |  | 65 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV01EDMNYR-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01EDMNYR-EDM | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01EDMNYR-NYR | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV01EDMNYR-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01EDMNYR-EDM2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV01EDMNYR-NYR2 | period_spread |  | 0.165 |  | 17 | 84 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01EDMNYR-1 | period_total |  | 0.910 |  | 92 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01EDMNYR-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV01EDMNYR-3 | period_total |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1 | player_assists |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-3 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMEBOUCHARD2-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMEBOUCHARD2-2 | player_assists |  | 0.180 |  | 19 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV01EDMNYR-EDMEBOUCHARD2-3 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ NYR | 0.516 | 0.503 | 0.171 | 0.211 | 6.46 | 6.68 | 0.988/1.000 | KXNHLTOTAL-26NOV01EDMNYR-7 +0.039 |
| OTT @ ANA | 0.562 | 0.586 | 0.167 | 0.213 | 6.83 | 6.57 | 0.968/1.034 | KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Filip Hallander: 1+ goals YES @ 9c · p 0.1325 (adj 0.1194) · $5.63 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ assists YES @ 26c · p 0.3523 (adj 0.3036) · $8.96 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1723 (adj 0.1592) · $5.65 · thesis EDM:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3446 (adj 0.2998) · $8.28 · thesis NYR:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2467 (adj 0.2238) · $14.43 · thesis ANA:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8805 (adj 0.8327) · $18.13 · thesis ANA:WINS
- Ottawa over 4.5 goals scored NO @ 74c · p 0.8151 (adj 0.7726) · $11.87 · thesis ANA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**EDM @ NYR** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.57, exp saves 24.66 (sd 6.88), pull risk 0.069
- EDM net: Matt Tomkins (CONFIRMED) exp shots 25.83, exp saves 22.18 (sd 6.28), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 24+ saves | 0.567 | 0.435 | 46/59 | +0.089 |  |
| Connor McDavid: 1+ assists | 0.541 | 0.655 | 66/35 | +0.093 | STANDARD |
| Connor McDavid: 2+ assists | 0.179 | 0.285 | 29/72 | +0.087 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.352 | 0.255 | 26/75 | +0.079 | STANDARD |
| Connor McDavid: 2+ points | 0.381 | 0.475 | 48/53 | +0.072 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.345 | 0.255 | 26/75 | +0.071 | STANDARD |

**OTT @ ANA** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.52), pull risk 0.056
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.68, exp saves 23.48 (sd 6.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.445 | 0.545 | 55/46 | +0.078 | STANDARD |
| Jake Sanderson: 1+ assists | 0.361 | 0.455 | 46/55 | +0.072 | STANDARD |
| A.J. Greer: 1+ goals | 0.247 | 0.155 | 16/85 | +0.077 | STANDARD |
| Thomas Chabot: 1+ assists | 0.246 | 0.335 | 34/67 | +0.069 | STANDARD |
| Tim Stutzle: 2+ points | 0.236 | 0.325 | 33/68 | +0.069 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.580 | 0.495 | 50/51 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
