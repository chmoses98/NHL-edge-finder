# NHL slate 2026-10-09 — RESEARCH_ONLY

generated 2026-10-09T22:22:07Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3433 · contracts joined: 956 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 856, 'OK': 48, 'NO_EDGE': 52}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 146, 'game_early_goal': 4, 'first_goal': 144, 'game_winner': 8, 'player_goals': 254, 'game_overtime': 4, 'player_points': 202, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 2026-10-09T23:00:00Z | T-30m | 0.546 | 0.454 | 0.177 | 5.87 | 3.08 | 2.79 | 222 (25/197) | CONFIRMED/PROJECTED |
| NYR @ WSH | 2026-10-09T23:00:00Z | T-30m | 0.544 | 0.456 | 0.183 | 5.83 | 3.06 | 2.77 | 248 (25/223) | CONFIRMED/CONFIRMED |
| PIT @ CBJ | 2026-10-09T23:00:00Z | T-30m | 0.495 | 0.505 | 0.170 | 6.87 | 3.42 | 3.46 | 236 (25/211) | CONFIRMED/CONFIRMED |
| ANA @ WPG | 2026-10-10T00:00:00Z | T-90m | 0.547 | 0.453 | 0.172 | 6.18 | 3.24 | 2.94 | 250 (25/225) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT09PITCBJ-8 | game_total | 0.359 | 0.305 | 0.315 | 31 | 70 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT09SEADET-6 | game_total | 0.503 | 0.555 | 0.545 | 56 | 45 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET4 | team_total | 0.386 | 0.440 | 0.429 | 45 | 57 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-9 | game_total | 0.268 | 0.225 | 0.233 | 23 | 78 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-10 | game_total | 0.142 | 0.105 | 0.112 | 11 | 90 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET5 | team_total | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT09SEADET-5 | game_total | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT09SEADET-7 | game_total | 0.389 | 0.435 | 0.426 | 44 | 57 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-6 | game_total | 0.553 | 0.595 | 0.587 | 60 | 41 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-5 | game_total | 0.770 | 0.805 | 0.798 | 81 | 20 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-7 | game_total | 0.444 | 0.485 | 0.477 | 49 | 52 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-4 | game_total | 0.855 | 0.885 | 0.879 | 89 | 12 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT6 | team_total | 0.134 | 0.105 | 0.110 | 11 | 90 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT09SEADET-9 | game_total | 0.143 | 0.175 | 0.168 | 18 | 83 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT3 | team_total | 0.672 | 0.635 | 0.642 | 64 | 37 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT09SEADET-DET3 | game_spread | 0.192 | 0.225 | 0.218 | 23 | 78 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT09SEADET-8 | game_total | 0.213 | 0.245 | 0.238 | 25 | 76 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH2 | team_total | 0.806 | 0.835 | 0.829 | 84 | 17 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT09SEADET-4 | game_total | 0.828 | 0.855 | 0.850 | 86 | 15 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-5 | game_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET2 | team_total | 0.808 | 0.840 | 0.834 | 85 | 17 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 | team_total | 0.352 | 0.385 | 0.378 | 39 | 62 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET3 | team_total | 0.602 | 0.635 | 0.629 | 64 | 37 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT5 | team_total | 0.273 | 0.240 | 0.246 | 25 | 77 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT2 | game_spread | 0.303 | 0.275 | 0.281 | 28 | 73 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET6 | team_total | 0.085 | 0.105 | 0.101 | 11 | 90 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-6 | game_total | 0.665 | 0.635 | 0.641 | 64 | 37 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT09NYRWSH-WSH3 | game_spread | 0.190 | 0.215 | 0.210 | 22 | 79 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH4 | team_total | 0.375 | 0.405 | 0.399 | 41 | 60 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA3 | game_spread | 0.143 | 0.165 | 0.160 | 17 | 84 | no | +0.008 | OK |
| KXNHLGAME-26OCT09SEADET-SEA | game_winner | 0.454 | 0.425 | 0.431 | 43 | 58 | yes | +0.007 | OK |
| KXNHLGAME-26OCT09SEADET-DET | game_winner | 0.546 | 0.575 | 0.569 | 58 | 43 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-3 | game_total | 0.951 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 | team_total | 0.463 | 0.430 | 0.437 | 44 | 58 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-3 | game_total | 0.963 | 0.975 | 0.973 | 98 | 3 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA2 | team_total | 0.784 | 0.805 | 0.801 | 81 | 20 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ6 | team_total | 0.132 | 0.115 | 0.118 | 12 | 89 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT09SEADET-3 | game_total | 0.953 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH3 | team_total | 0.601 | 0.625 | 0.620 | 63 | 38 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT09SEADET-DET2 | game_spread | 0.322 | 0.350 | 0.344 | 36 | 66 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 | team_total | 0.571 | 0.595 | 0.590 | 60 | 41 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA5 | team_total | 0.178 | 0.205 | 0.199 | 22 | 81 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-4 | game_total | 0.819 | 0.835 | 0.832 | 84 | 17 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-3 | game_total | 0.978 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH5 | team_total | 0.197 | 0.220 | 0.215 | 23 | 79 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 | team_total | 0.314 | 0.335 | 0.331 | 34 | 67 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ3 | game_spread | 0.179 | 0.195 | 0.192 | 20 | 81 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ4 | team_total | 0.457 | 0.435 | 0.439 | 44 | 57 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG2 | game_spread | 0.325 | 0.305 | 0.309 | 31 | 70 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-WSH2 | game_spread | 0.315 | 0.335 | 0.331 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-WPG | game_winner | 0.547 | 0.525 | 0.529 | 53 | 48 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-ANA | game_winner | 0.453 | 0.475 | 0.471 | 48 | 53 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-ANA2 | game_spread | 0.247 | 0.265 | 0.261 | 27 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-8 | game_total | 0.257 | 0.275 | 0.271 | 28 | 73 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-10 | game_total | 0.084 | 0.075 | 0.077 | 8 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA2 | team_total | 0.759 | 0.780 | 0.776 | 79 | 23 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT09NYRWSH-NYR | game_winner | 0.456 | 0.435 | 0.439 | 44 | 57 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT09NYRWSH-WSH | game_winner | 0.544 | 0.565 | 0.561 | 57 | 44 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT09PITCBJ-CBJ | game_winner | 0.495 | 0.515 | 0.511 | 52 | 49 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26OCT09PITCBJ-PIT | game_winner | 0.505 | 0.485 | 0.489 | 49 | 52 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-6 | game_total | 0.496 | 0.515 | 0.511 | 52 | 49 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-SEA3 | game_spread | 0.135 | 0.145 | 0.143 | 15 | 86 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR6 | team_total | 0.060 | 0.055 | 0.056 | 6 | 95 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ2 | game_spread | 0.291 | 0.305 | 0.302 | 31 | 70 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT09PITCBJ-PIT3 | game_spread | 0.184 | 0.175 | 0.177 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT2 | team_total | 0.852 | 0.835 | 0.839 | 85 | 18 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-7 | game_total | 0.390 | 0.405 | 0.402 | 41 | 60 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ5 | team_total | 0.266 | 0.255 | 0.257 | 26 | 75 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-10 | game_total | 0.064 | 0.070 | 0.069 | 8 | 94 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-WPG2 | team_total | 0.829 | 0.840 | 0.838 | 85 | 17 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR5 | team_total | 0.150 | 0.145 | 0.146 | 15 | 86 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-4 | game_total | 0.903 | 0.905 | 0.905 | 91 | 10 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-8 | game_total | 0.208 | 0.215 | 0.214 | 22 | 79 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR3 | game_spread | 0.132 | 0.135 | 0.134 | 14 | 87 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH6 | team_total | 0.085 | 0.085 | 0.085 | 9 | 92 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-WPG6 | team_total | 0.104 | 0.105 | 0.105 | 11 | 90 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-9 | game_total | 0.142 | 0.150 | 0.148 | 16 | 86 |  | -0.011 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 0.546 | 0.532 | 0.177 | 0.216 | 5.87 | 6.21 | 0.994/1.015 | KXNHLTOTAL-26OCT09SEADET-7 +0.065 |
| NYR @ WSH | 0.544 | 0.542 | 0.183 | 0.217 | 5.83 | 6.14 | 0.937/0.934 | KXNHLTOTAL-26OCT09NYRWSH-7 +0.055 |
| PIT @ CBJ | 0.495 | 0.525 | 0.170 | 0.214 | 6.87 | 6.55 | 1.007/1.012 | KXNHLTOTAL-26OCT09PITCBJ-8 -0.056 |
| ANA @ WPG | 0.547 | 0.519 | 0.172 | 0.218 | 6.18 | 6.41 | 0.994/1.024 | KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 +0.048 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Winterton: 1+ goals YES @ 10c · p 0.1369 (adj 0.1264) · $4.99 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 9c · p 0.1204 (adj 0.1115) · $3.96 · thesis SEA:OFFENSE_4PLUS
- Carter Mazur: 1+ goals YES @ 8c · p 0.1061 (adj 0.0983) · $3.13 · thesis DET:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ assists NO @ 80c · p 0.8712 (adj 0.8256) · $19.23 · thesis SEA:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2417 (adj 0.22) · $14.25 · thesis WSH:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 22c · p 0.3045 (adj 0.2597) · $7.8 · thesis NYR:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 14c · p 0.1678 (adj 0.1596) · $3.12 · thesis WSH:OFFENSE_4PLUS
- Jordan Kyrou: 1+ assists NO @ 74c · p 0.8385 (adj 0.7647) · $19.23 · thesis WSH:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 10c · p 0.1415 (adj 0.1299) · $5.72 · thesis CBJ:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 11c · p 0.1465 (adj 0.1361) · $5.05 · thesis PIT:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2026 (adj 0.1907) · $5.68 · thesis CBJ:OFFENSE_4PLUS
- Evgeni Malkin: 1+ assists NO @ 59c · p 0.6781 (adj 0.6316) · $16.14 · thesis PIT:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 15c · p 0.2343 (adj 0.212) · $13.52 · thesis ANA:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 87c · p 0.926 (adj 0.9108) · $19.23 · thesis WPG:SUPPRESSED
- Judd Caulfield: 1+ goals YES @ 7c · p 0.1091 (adj 0.0968) · $4.92 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 8c · p 0.1129 (adj 0.1022) · $4.01 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ DET** · priced 162/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.67, exp saves 22.4 (sd 6.23), pull risk 0.056
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.51, exp saves 25.31 (sd 6.85), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Emmitt Finnie: 1+ points | 0.471 | 0.350 | 36/66 | +0.094 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.335 | 0.230 | 25/79 | +0.072 | STANDARD |
| Andrew Copp: 1+ points | 0.476 | 0.380 | 39/63 | +0.070 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.129 | 0.220 | 24/80 | +0.060 | STANDARD |
| Mackie Samoskevich: 1+ points | 0.305 | 0.395 | 41/62 | +0.058 | STANDARD |
| Andrew Copp: 1+ assists | 0.343 | 0.260 | 27/75 | +0.059 | STANDARD |

**NYR @ WSH** · priced 191/197 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 25.25, exp saves 22.05 (sd 6.08), pull risk 0.052
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 27.39, exp saves 23.53 (sd 6.53), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.305 | 0.130 | 23/97 | +0.062 | STANDARD |
| Martin Fehervary: 1+ assists | 0.261 | 0.120 | 22/98 | +0.029 | STANDARD |
| Tye Kartye: 1+ assists | 0.225 | 0.105 | 19/98 | +0.024 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.162 | 0.275 | 29/74 | +0.085 | STANDARD |
| Ryan Leonard: 1+ assists | 0.323 | 0.215 | 24/81 | +0.070 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.222 | 0.115 | 20/97 | +0.011 | STANDARD |

**PIT @ CBJ** · priced 180/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.49, exp saves 23.79 (sd 6.53), pull risk 0.062
- PIT net: Sergei Murashov (CONFIRMED) exp shots 27.56, exp saves 23.63 (sd 6.61), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Knies: 1+ assists | 0.280 | 0.400 | 41/61 | +0.094 | STANDARD |
| Matthew Knies: 1+ points | 0.496 | 0.615 | 63/40 | +0.087 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.203 | 0.305 | 31/70 | +0.083 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.338 | 0.240 | 26/78 | +0.065 | STANDARD |
| Sergei Murashov: 25+ saves | 0.440 | 0.535 | 55/48 | +0.063 |  |
| Evgeni Malkin: 1+ assists | 0.322 | 0.415 | 42/59 | +0.071 | STANDARD |

**ANA @ WPG** · priced 193/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.53, exp saves 25.56 (sd 6.89), pull risk 0.062
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.65, exp saves 23.05 (sd 6.41), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan DeMelo: 1+ assists | 0.256 | 0.120 | 22/98 | +0.024 | STANDARD |
| Alex Iafallo: 1+ points | 0.411 | 0.275 | 30/75 | +0.096 | STANDARD |
| Isak Rosen: 1+ assists | 0.202 | 0.085 | 16/99 | +0.032 | STANDARD |
| Neal Pionk: 1+ assists | 0.339 | 0.440 | 45/57 | +0.074 | STANDARD |
| Alex Iafallo: 1+ assists | 0.274 | 0.175 | 18/83 | +0.083 | STANDARD |
| Neal Pionk: 1+ points | 0.386 | 0.480 | 49/53 | +0.067 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
