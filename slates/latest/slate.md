# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T17:45:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4059 · contracts joined: 2367 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2092, 'OK': 171, 'NO_EDGE': 104}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 309, 'game_early_goal': 11, 'first_goal': 392, 'game_winner': 22, 'player_goals': 679, 'game_overtime': 11, 'player_points': 412, 'goalie_saves': 14, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-6h | 0.481 | 0.519 | 0.167 | 7.09 | 3.48 | 3.61 | 237 (25/212) | CONFIRMED/PROBABLE |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-6h | 0.654 | 0.346 | 0.171 | 5.87 | 3.42 | 2.45 | 200 (25/175) | CONFIRMED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-6h | 0.641 | 0.359 | 0.172 | 6.03 | 3.45 | 2.57 | 216 (25/191) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-6h | 0.506 | 0.494 | 0.179 | 6.01 | 3.01 | 2.99 | 203 (25/178) | CONFIRMED/CONFIRMED |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-6h | 0.439 | 0.561 | 0.186 | 5.69 | 2.66 | 3.02 | 214 (25/189) | CONFIRMED/CONFIRMED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-6h | 0.539 | 0.461 | 0.167 | 6.81 | 3.53 | 3.27 | 216 (25/191) | CONFIRMED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-6h | 0.559 | 0.441 | 0.185 | 5.67 | 3.02 | 2.66 | 222 (25/197) | CONFIRMED/CONFIRMED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-6h | 0.362 | 0.638 | 0.167 | 6.16 | 2.64 | 3.52 | 213 (25/188) | CONFIRMED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-6h | 0.535 | 0.465 | 0.171 | 6.44 | 3.34 | 3.10 | 218 (25/193) | CONFIRMED/CONFIRMED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-6h | 0.370 | 0.630 | 0.167 | 6.31 | 2.74 | 3.56 | 220 (25/195) | CONFIRMED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-6h | 0.411 | 0.589 | 0.158 | 7.18 | 3.28 | 3.89 | 208 (25/183) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.362 | 0.475 | 0.452 | 48 | 53 | no | +0.091 | OK |
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.638 | 0.525 | 0.548 | 53 | 48 | yes | +0.091 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.367 | 0.465 | 0.445 | 47 | 54 | no | +0.076 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.180 | 0.275 | 0.254 | 28 | 73 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.492 | 0.590 | 0.571 | 60 | 42 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-COL2 | game_spread | 0.413 | 0.325 | 0.342 | 33 | 68 | yes | +0.068 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.267 | 0.355 | 0.336 | 36 | 65 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.466 | 0.560 | 0.541 | 57 | 45 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.408 | 0.495 | 0.477 | 50 | 51 | no | +0.065 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.195 | 0.275 | 0.257 | 28 | 73 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.283 | 0.370 | 0.352 | 38 | 64 | no | +0.061 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN2 | game_spread | 0.323 | 0.405 | 0.388 | 41 | 60 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.264 | 0.345 | 0.328 | 35 | 66 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.503 | 0.585 | 0.569 | 59 | 42 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.731 | 0.805 | 0.791 | 81 | 20 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.286 | 0.365 | 0.348 | 37 | 64 | no | +0.058 | OK |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.359 | 0.285 | 0.299 | 29 | 72 | yes | +0.054 | OK |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.641 | 0.715 | 0.701 | 72 | 29 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.097 | 0.165 | 0.149 | 17 | 84 | no | +0.054 | OK |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.469 | 0.545 | 0.530 | 55 | 46 | no | +0.053 | OK |
| KXNHLTOTAL-26NOV03MINPHI-6 | game_total | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.053 | OK |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.439 | 0.365 | 0.379 | 37 | 64 | yes | +0.052 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-COL3 | game_spread | 0.272 | 0.205 | 0.217 | 21 | 80 | yes | +0.050 | OK |
| KXNHLTOTAL-26NOV03MINPHI-5 | game_total | 0.708 | 0.775 | 0.763 | 78 | 23 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN3 | team_total | 0.597 | 0.670 | 0.656 | 68 | 34 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG4 | team_total | 0.240 | 0.305 | 0.291 | 31 | 70 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV03MINPHI-7 | game_total | 0.358 | 0.425 | 0.411 | 43 | 58 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.222 | 0.285 | 0.272 | 29 | 72 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.683 | 0.750 | 0.737 | 76 | 26 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 | team_total | 0.600 | 0.535 | 0.548 | 54 | 47 | yes | +0.043 | OK |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.561 | 0.625 | 0.613 | 63 | 38 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN5 | team_total | 0.185 | 0.255 | 0.240 | 27 | 76 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 | team_total | 0.451 | 0.520 | 0.506 | 53 | 49 | no | +0.042 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.119 | 0.175 | 0.162 | 18 | 83 | no | +0.041 | OK |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.441 | 0.505 | 0.492 | 51 | 50 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.386 | 0.325 | 0.337 | 33 | 68 | yes | +0.040 | OK |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.535 | 0.595 | 0.583 | 60 | 41 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.741 | 0.800 | 0.789 | 81 | 21 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.133 | 0.195 | 0.181 | 21 | 82 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL3 | team_total | 0.691 | 0.635 | 0.647 | 64 | 37 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.401 | 0.345 | 0.356 | 35 | 66 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6 | team_total | 0.141 | 0.095 | 0.103 | 10 | 91 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.861 | 0.910 | 0.902 | 92 | 10 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV03DALWSH-5 | game_total | 0.704 | 0.755 | 0.745 | 76 | 25 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.171 | 0.125 | 0.133 | 13 | 88 | yes | +0.033 | OK |
| KXNHLTOTAL-26NOV03DALWSH-7 | game_total | 0.360 | 0.415 | 0.404 | 42 | 59 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV03MINPHI-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR4 | team_total | 0.468 | 0.410 | 0.422 | 42 | 60 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV03MINPHI-8 | game_total | 0.186 | 0.235 | 0.225 | 24 | 77 | no | +0.031 | OK |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.559 | 0.505 | 0.516 | 51 | 50 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-9 | game_total | 0.305 | 0.255 | 0.264 | 26 | 75 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.130 | 0.180 | 0.169 | 19 | 83 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV03DALWSH-4 | game_total | 0.800 | 0.850 | 0.841 | 86 | 16 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV03EDMNJ-7 | game_total | 0.487 | 0.435 | 0.445 | 44 | 57 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL5 | team_total | 0.131 | 0.185 | 0.173 | 20 | 83 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.209 | 0.155 | 0.165 | 17 | 86 | yes | +0.029 | OK |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.465 | 0.415 | 0.425 | 42 | 59 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV03WPGMTL-6 | game_total | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.028 | OK |
| KXNHLGAME-26NOV03WPGMTL-MTL | game_winner | 0.654 | 0.605 | 0.615 | 61 | 40 | yes | +0.028 | OK |
| KXNHLGAME-26NOV03WPGMTL-WPG | game_winner | 0.346 | 0.395 | 0.385 | 40 | 61 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV03WPGMTL-WPG2 | game_spread | 0.163 | 0.205 | 0.196 | 21 | 80 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV03MINPHI-9 | game_total | 0.125 | 0.165 | 0.156 | 17 | 84 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.202 | 0.245 | 0.236 | 25 | 76 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.390 | 0.345 | 0.354 | 35 | 66 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.297 | 0.250 | 0.259 | 26 | 76 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03VGKPIT-8 | game_total | 0.349 | 0.305 | 0.313 | 31 | 70 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.439 | 0.485 | 0.476 | 49 | 52 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL4 | team_total | 0.481 | 0.430 | 0.440 | 44 | 58 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-7 | game_total | 0.601 | 0.555 | 0.564 | 56 | 45 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV03EDMNJ-8 | game_total | 0.297 | 0.250 | 0.259 | 26 | 76 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV03UTATOR-10 | game_total | 0.160 | 0.120 | 0.127 | 13 | 89 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL6 | team_total | 0.139 | 0.100 | 0.107 | 11 | 91 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV03UTATOR-7 | game_total | 0.589 | 0.545 | 0.554 | 55 | 46 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG2 | team_total | 0.695 | 0.745 | 0.735 | 76 | 27 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV03WPGMTL-7 | game_total | 0.392 | 0.435 | 0.426 | 44 | 57 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6 | team_total | 0.096 | 0.060 | 0.066 | 7 | 95 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ2 | game_spread | 0.323 | 0.365 | 0.356 | 37 | 64 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV03DALWSH-8 | game_total | 0.187 | 0.225 | 0.217 | 23 | 78 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR3 | team_total | 0.676 | 0.630 | 0.639 | 64 | 38 | yes | +0.020 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 0.481 | 0.500 | 0.167 | 0.213 | 7.09 | 6.78 | 0.989/0.999 | KXNHLTOTAL-26NOV03UTATOR-8 -0.052 |
| WPG @ MTL | 0.654 | 0.584 | 0.171 | 0.213 | 5.87 | 6.29 | 0.983/1.002 | KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 +0.102 |
| DET @ TBL | 0.641 | 0.644 | 0.172 | 0.208 | 6.03 | 6.23 | 0.958/1.004 | KXNHLTOTAL-26NOV03DETTB-7 +0.038 |
| STL @ NYR | 0.506 | 0.517 | 0.179 | 0.222 | 6.01 | 6.25 | 0.988/0.977 | KXNHLTOTAL-26NOV03STLNYR-7 +0.041 |
| MIN @ PHI | 0.439 | 0.518 | 0.186 | 0.223 | 5.69 | 6.00 | 0.995/0.991 | KXNHLTEAMTOTAL-26NOV03MINPHI-PHI3 +0.095 |
| VGK @ PIT | 0.539 | 0.522 | 0.167 | 0.215 | 6.81 | 6.55 | 1.042/1.004 | KXNHLTOTAL-26NOV03VGKPIT-6 -0.047 |
| DAL @ WSH | 0.559 | 0.550 | 0.185 | 0.222 | 5.67 | 6.13 | 0.939/0.995 | KXNHLTOTAL-26NOV03DALWSH-7 +0.078 |
| COL @ CBJ | 0.362 | 0.463 | 0.167 | 0.220 | 6.16 | 6.40 | 1.008/0.971 | KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 +0.110 |
| EDM @ NJD | 0.535 | 0.510 | 0.171 | 0.212 | 6.44 | 6.62 | 0.950/1.023 | KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 +0.042 |
| CAR @ NSH | 0.370 | 0.455 | 0.167 | 0.214 | 6.31 | 6.56 | 1.005/0.998 | KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4 +0.095 |
| ANA @ VAN | 0.411 | 0.453 | 0.158 | 0.211 | 7.18 | 6.91 | 1.027/1.017 | KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4 -0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 11c · p 0.1768 (adj 0.1564) · $4.89 · thesis TOR:WINS_BY_2PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2195 (adj 0.2071) · $2.52 · thesis UTA:OFFENSE_4PLUS
- Kevin Stenlund: 1+ goals YES @ 8c · p 0.1086 (adj 0.0965) · $1.36 · thesis UTA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 65c · p 0.6909 (adj 0.6794) · $4.74 · thesis UTA:SUPPRESSED
- Dylan Samberg: 1+ goals YES @ 4c · p 0.0658 (adj 0.0568) · $1.46 · thesis WPG:OFFENSE_4PLUS
- Cole Perfetti: 1+ assists YES @ 30c · p 0.3737 (adj 0.3294) · $1.51 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 27c · p 0.306 (adj 0.2958) · $1.34 · thesis WPG:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9217 (adj 0.91) · $10.07 · thesis TBL:SUPPRESSED
- Emmitt Finnie: 1+ assists YES @ 26c · p 0.3293 (adj 0.2922) · $2.7 · thesis DET:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 65c · p 0.7157 (adj 0.6804) · $5.06 · thesis GAME:TIGHT
- Ilya Mikheyev: 1+ goals YES @ 15c · p 0.1826 (adj 0.1695) · $1.69 · thesis TBL:OFFENSE_4PLUS
- Alexis Lafreniere: 1+ goals YES @ 29c · p 0.3366 (adj 0.3237) · $3.42 · thesis NYR:OFFENSE_4PLUS
- Tye Kartye: 1+ goals YES @ 16c · p 0.1924 (adj 0.1805) · $1.58 · thesis NYR:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 29c · p 0.3279 (adj 0.3172) · $2.31 · thesis STL:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2189 (adj 0.2029) · $4.31 · thesis PHI:OFFENSE_4PLUS
- Philadelphia wins by over 1.5 goals YES @ 20c · p 0.2884 (adj 0.2417) · $2.6 · thesis PHI:WINS_BY_2PLUS
- Matt Boldy: 1+ goals NO @ 63c · p 0.6902 (adj 0.6726) · $8.0 · thesis MIN:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 52c · p 0.6432 (adj 0.5599) · $4.75 · thesis MIN:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.164 (adj 0.1542) · $2.25 · thesis PIT:OFFENSE_4PLUS
- Justin Brazeau: 1+ goals YES @ 15c · p 0.1841 (adj 0.1693) · $1.44 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2378 (adj 0.2171) · $6.58 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 15c · p 0.2121 (adj 0.1953) · $4.99 · thesis WSH:OFFENSE_4PLUS
- Martin Fehervary: 1+ goals YES @ 3c · p 0.0494 (adj 0.0433) · $1.25 · thesis DIFFUSE
- Miro Heiskanen: 1+ goals NO @ 87c · p 0.9029 (adj 0.8934) · $10.07 · thesis DAL:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1841 (adj 0.1743) · $2.19 · thesis CBJ:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 15c · p 0.1831 (adj 0.1736) · $2.11 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 9c · p 0.1192 (adj 0.1069) · $1.43 · thesis CBJ:OFFENSE_4PLUS
- Cole Sillinger: 1+ goals YES @ 13c · p 0.1626 (adj 0.1507) · $1.66 · thesis CBJ:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 7c · p 0.1296 (adj 0.1122) · $4.19 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 11c · p 0.1535 (adj 0.1401) · $2.98 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 22c · p 0.275 (adj 0.26) · $4.85 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 36c · p 0.4668 (adj 0.3909) · $4.54 · thesis EDM:SUPPRESSED
- Jack Drury: 1+ goals YES @ 9c · p 0.1321 (adj 0.1203) · $3.05 · thesis NSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ assists NO @ 50c · p 0.6415 (adj 0.5463) · $7.84 · thesis CAR:SUPPRESSED
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1713 (adj 0.156) · $2.35 · thesis NSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7171 (adj 0.7028) · $7.1 · thesis CAR:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2486 (adj 0.2302) · $5.76 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1593 (adj 0.147) · $2.62 · thesis VAN:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 12c · p 0.1566 (adj 0.1462) · $2.63 · thesis ANA:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 20c · p 0.245 (adj 0.2313) · $3.05 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ TOR** · priced 180/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.46 (sd 7.24), pull risk 0.077
- UTA net: Sebastian Cossa (PROBABLE) exp shots 26.79, exp saves 23.1 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.443 | 0.325 | 34/69 | +0.087 | STANDARD |
| Sebastian Cossa: 23+ saves | 0.534 | 0.430 | 50/64 | +0.017 |  |
| Morgan Rielly: 1+ assists | 0.340 | 0.255 | 27/76 | +0.056 | STANDARD |
| Teddy Blueger: 1+ goals | 0.177 | 0.095 | 11/92 | +0.060 | STANDARD |
| Auston Matthews: 1+ assists | 0.408 | 0.490 | 50/52 | +0.054 | STANDARD |
| Sergei Bobrovsky: 29+ saves | 0.380 | 0.460 | 48/56 | +0.043 |  |

**WPG @ MTL** · priced 143/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.0, exp saves 23.62 (sd 6.23), pull risk 0.049
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.07, exp saves 22.98 (sd 6.51), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Perfetti: 1+ assists | 0.374 | 0.285 | 30/73 | +0.059 | STANDARD |
| Cole Perfetti: 1+ points | 0.540 | 0.455 | 48/57 | +0.043 | STANDARD |
| Jake Evans: 1+ points | 0.377 | 0.310 | 33/71 | +0.032 | STANDARD |
| Juraj Slafkovský: 1+ assists | 0.386 | 0.450 | 47/57 | +0.027 | STANDARD |
| Cole Caufield: 1+ assists | 0.367 | 0.425 | 43/58 | +0.036 | STANDARD |
| Adam Lowry: 1+ goals | 0.131 | 0.080 | 11/95 | +0.014 | STANDARD |

**DET @ TBL** · priced 154/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.08 (sd 6.22), pull risk 0.044
- DET net: John Gibson (PROJECTED) exp shots 27.95, exp saves 23.68 (sd 6.8), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.524 | 0.650 | 66/36 | +0.100 | STANDARD |
| Nikita Kucherov: 2+ points | 0.338 | 0.460 | 47/55 | +0.095 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.169 | 0.285 | 30/73 | +0.088 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.329 | 0.255 | 26/75 | +0.056 | STANDARD |
| Lucas Raymond: 1+ assists | 0.332 | 0.405 | 42/61 | +0.042 | STANDARD |
| Emmitt Finnie: 1+ points | 0.482 | 0.425 | 43/58 | +0.035 | STANDARD |

**STL @ NYR** · priced 151/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.61, exp saves 23.04 (sd 6.32), pull risk 0.055
- STL net: Joel Hofer (CONFIRMED) exp shots 26.51, exp saves 22.95 (sd 6.34), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 23+ saves | 0.530 | 0.470 | 49/55 | +0.023 |  |
| Pavel Dorofeyev: 1+ assists | 0.273 | 0.330 | 35/69 | +0.022 | STANDARD |
| Tye Kartye: 1+ points | 0.416 | 0.360 | 38/66 | +0.020 | STANDARD |
| Philip Broberg: 1+ points | 0.486 | 0.430 | 44/58 | +0.028 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.492 | 0.545 | 56/47 | +0.020 | STANDARD |
| Alexis Lafreniere: 1+ goals | 0.337 | 0.285 | 29/72 | +0.032 | STANDARD |

**MIN @ PHI** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.47, exp saves 24.7 (sd 6.68), pull risk 0.058
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 25.89, exp saves 22.45 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.245 | 0.405 | 42/61 | +0.128 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.389 | 0.530 | 54/48 | +0.113 | STANDARD |
| Matt Boldy: 1+ assists | 0.374 | 0.505 | 52/51 | +0.099 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.357 | 0.485 | 49/52 | +0.106 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.601 | 0.725 | 75/30 | +0.084 | STANDARD |
| Matt Boldy: 2+ points | 0.211 | 0.320 | 33/69 | +0.084 | STANDARD |

**VGK @ PIT** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.98, exp saves 23.37 (sd 6.5), pull risk 0.066
- VGK net: Adin Hill (PROJECTED) exp shots 27.28, exp saves 23.52 (sd 6.54), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 27+ saves | 0.299 | 0.420 | 43/59 | +0.094 |  |
| Mitch Marner: 1+ assists | 0.422 | 0.515 | 53/50 | +0.060 | STANDARD |
| Mitch Marner: 1+ points | 0.557 | 0.650 | 66/36 | +0.066 | STANDARD |
| Jack Eichel: 1+ assists | 0.439 | 0.525 | 54/49 | +0.054 | STANDARD |
| Jack Eichel: 2+ points | 0.241 | 0.325 | 34/69 | +0.054 | STANDARD |
| Mitch Marner: 2+ points | 0.199 | 0.275 | 30/75 | +0.037 | STANDARD |

**DAL @ WSH** · priced 167/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 26.25, exp saves 22.86 (sd 6.28), pull risk 0.053
- DAL net: Jake Oettinger (CONFIRMED) exp shots 25.46, exp saves 21.82 (sd 6.17), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.447 | 0.555 | 57/46 | +0.075 | STANDARD |
| Aliaksei Protas: 1+ points | 0.443 | 0.350 | 37/67 | +0.056 | STANDARD |
| Mikko Rantanen: 2+ points | 0.202 | 0.290 | 31/73 | +0.055 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.238 | 0.155 | 16/85 | +0.068 | STANDARD |
| Miro Heiskanen: 2+ points | 0.123 | 0.205 | 22/81 | +0.056 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.389 | 0.470 | 48/54 | +0.054 | STANDARD |

**COL @ CBJ** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 29.48, exp saves 25.52 (sd 6.84), pull risk 0.064
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.34 (sd 6.32), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Scott Wedgewood: 26+ saves | 0.356 | 0.455 | 48/57 | +0.057 |  |
| Zach Werenski: 1+ assists | 0.484 | 0.550 | 57/47 | +0.029 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.301 | 0.365 | 38/65 | +0.033 | STANDARD |
| Matthew Knies: 1+ assists | 0.298 | 0.360 | 37/65 | +0.036 | STANDARD |
| Cale Makar: 2+ points | 0.184 | 0.240 | 25/77 | +0.034 | STANDARD |
| Damon Severson: 1+ goals | 0.119 | 0.070 | 9/95 | +0.023 | STANDARD |

**EDM @ NJD** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.46, exp saves 22.85 (sd 6.47), pull risk 0.067
- EDM net: Tristan Jarry (CONFIRMED) exp shots 29.41, exp saves 25.29 (sd 6.96), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.370 | 0.495 | 50/51 | +0.102 | STANDARD |
| Connor McDavid: 2+ assists | 0.168 | 0.290 | 31/73 | +0.088 | STANDARD |
| Connor McDavid: 1+ assists | 0.533 | 0.650 | 66/36 | +0.091 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.515 | 52/49 | +0.080 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.519 | 0.420 | 43/59 | +0.072 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.312 | 0.220 | 24/80 | +0.060 | STANDARD |

**CAR @ NSH** · priced 165/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 31.84, exp saves 27.15 (sd 7.47), pull risk 0.082
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.29 (sd 6.07), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Sebastian Aho: 2+ points | 0.179 | 0.290 | 31/73 | +0.077 | STANDARD |
| Sebastian Aho: 1+ points | 0.543 | 0.645 | 66/37 | +0.070 | STANDARD |
| Sebastian Aho: 2+ assists | 0.071 | 0.155 | 18/87 | +0.051 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.347 | 0.425 | 44/59 | +0.046 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.387 | 0.460 | 48/56 | +0.036 | STANDARD |

**ANA @ VAN** · priced 146/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.41, exp saves 26.03 (sd 7.2), pull risk 0.081
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.99, exp saves 21.59 (sd 6.16), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ assists | 0.414 | 0.515 | 53/50 | +0.069 | STANDARD |
| Leo Carlsson: 2+ points | 0.230 | 0.305 | 31/70 | +0.056 | STANDARD |
| Marco Rossi: 1+ goals | 0.249 | 0.175 | 18/83 | +0.058 | STANDARD |
| Leo Carlsson: 2+ assists | 0.104 | 0.175 | 19/84 | +0.047 | STANDARD |
| Marco Rossi: 1+ points | 0.480 | 0.415 | 43/60 | +0.033 | STANDARD |
| Mikael Granlund: 1+ assists | 0.388 | 0.450 | 46/56 | +0.035 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
