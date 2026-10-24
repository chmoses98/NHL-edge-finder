# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T20:35:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 10 · markets on board: 4544 · contracts joined: 2424 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2174, 'NO_EDGE': 87, 'OK': 163}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 384, 'game_early_goal': 10, 'first_goal': 369, 'game_winner': 20, 'player_goals': 629, 'game_overtime': 10, 'player_points': 516, 'goalie_saves': 16, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ BOS | 2026-10-24T23:00:00Z | T-90m | 0.651 | 0.349 | 0.163 | 6.17 | 3.56 | 2.61 | 260 (25/235) | CONFIRMED/CONFIRMED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-90m | 0.471 | 0.529 | 0.179 | 6.09 | 2.95 | 3.14 | 238 (25/213) | CONFIRMED/CONFIRMED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-90m | 0.572 | 0.428 | 0.168 | 6.74 | 3.61 | 3.13 | 232 (25/207) | PROBABLE/CONFIRMED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-90m | 0.496 | 0.504 | 0.176 | 6.61 | 3.28 | 3.33 | 262 (25/237) | CONFIRMED/CONFIRMED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-90m | 0.416 | 0.584 | 0.168 | 6.46 | 2.96 | 3.50 | 244 (25/219) | CONFIRMED/PROBABLE |
| CAR @ STL | 2026-10-24T23:00:00Z | T-90m | 0.510 | 0.490 | 0.178 | 6.14 | 3.10 | 3.04 | 227 (25/202) | CONFIRMED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-90m | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 261 (25/236) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-3h | 0.554 | 0.446 | 0.176 | 6.08 | 3.21 | 2.87 | 235 (25/210) | PROBABLE/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-3h | 0.517 | 0.483 | 0.189 | 5.54 | 2.82 | 2.72 | 234 (25/209) | CONFIRMED/CONFIRMED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-3h | 0.471 | 0.529 | 0.175 | 6.26 | 3.04 | 3.23 | 231 (25/206) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.295 | 0.420 | 0.394 | 43 | 59 | no | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.520 | 0.640 | 0.617 | 65 | 37 | no | +0.094 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.447 | 0.555 | 0.533 | 56 | 45 | no | +0.086 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.686 | 0.785 | 0.767 | 79 | 22 | no | +0.082 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.490 | 0.585 | 0.566 | 59 | 42 | no | +0.073 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.510 | 0.415 | 0.434 | 42 | 59 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.341 | 0.435 | 0.416 | 44 | 57 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.139 | 0.230 | 0.209 | 24 | 78 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.752 | 0.840 | 0.825 | 85 | 17 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.162 | 0.245 | 0.226 | 25 | 76 | no | +0.066 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.529 | 0.615 | 0.598 | 62 | 39 | no | +0.064 | OK |
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.471 | 0.380 | 0.398 | 39 | 63 | yes | +0.064 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.429 | 0.515 | 0.498 | 52 | 49 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.757 | 0.835 | 0.821 | 84 | 17 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.273 | 0.360 | 0.342 | 37 | 65 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.543 | 0.630 | 0.613 | 64 | 38 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.139 | 0.215 | 0.198 | 22 | 79 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.786 | 0.855 | 0.843 | 86 | 15 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.589 | 0.670 | 0.654 | 68 | 34 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.173 | 0.245 | 0.229 | 25 | 76 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.799 | 0.865 | 0.854 | 87 | 14 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.312 | 0.385 | 0.370 | 39 | 62 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.293 | 0.220 | 0.233 | 23 | 79 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.373 | 0.450 | 0.434 | 46 | 56 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.189 | 0.255 | 0.241 | 26 | 75 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.242 | 0.310 | 0.296 | 32 | 70 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.224 | 0.290 | 0.276 | 30 | 72 | no | +0.042 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.041 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.842 | 0.895 | 0.886 | 90 | 11 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.148 | 0.205 | 0.192 | 21 | 80 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.167 | 0.225 | 0.212 | 23 | 78 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.197 | 0.260 | 0.246 | 27 | 75 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.413 | 0.480 | 0.466 | 49 | 53 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.261 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.336 | 0.395 | 0.383 | 40 | 61 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.311 | 0.255 | 0.266 | 26 | 75 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.628 | 0.685 | 0.674 | 69 | 32 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.114 | 0.170 | 0.157 | 18 | 84 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.260 | 0.315 | 0.303 | 32 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.591 | 0.535 | 0.546 | 54 | 47 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.410 | 0.465 | 0.454 | 47 | 54 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.571 | 0.630 | 0.618 | 64 | 38 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.353 | 0.410 | 0.398 | 42 | 60 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.634 | 0.690 | 0.679 | 70 | 32 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.054 | 0.100 | 0.089 | 11 | 91 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT4 | team_total | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.375 | 0.325 | 0.335 | 33 | 68 | yes | +0.030 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-7 | game_total | 0.443 | 0.495 | 0.485 | 50 | 51 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR3 | team_total | 0.616 | 0.565 | 0.575 | 57 | 44 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.250 | 0.200 | 0.209 | 21 | 81 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-5 | game_total | 0.771 | 0.820 | 0.811 | 83 | 19 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5 | team_total | 0.197 | 0.150 | 0.159 | 16 | 86 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB2 | team_total | 0.771 | 0.815 | 0.807 | 82 | 19 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT24NSHPIT-PIT2 | game_spread | 0.363 | 0.315 | 0.324 | 32 | 69 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT6 | team_total | 0.155 | 0.110 | 0.118 | 12 | 90 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT5 | team_total | 0.301 | 0.255 | 0.264 | 26 | 75 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT5 | team_total | 0.181 | 0.230 | 0.220 | 24 | 78 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-8 | game_total | 0.299 | 0.255 | 0.263 | 26 | 75 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT24SJBOS-6 | game_total | 0.558 | 0.605 | 0.596 | 61 | 40 | no | +0.025 | OK |
| KXNHLGAME-26OCT24NSHPIT-PIT | game_winner | 0.572 | 0.525 | 0.534 | 53 | 48 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL5 | team_total | 0.204 | 0.160 | 0.168 | 17 | 85 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.173 | 0.135 | 0.142 | 14 | 87 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK3 | team_total | 0.690 | 0.645 | 0.654 | 65 | 36 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.785 | 0.830 | 0.822 | 84 | 18 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA2 | team_total | 0.828 | 0.865 | 0.858 | 87 | 14 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.204 | 0.245 | 0.236 | 25 | 76 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-9 | game_total | 0.214 | 0.175 | 0.182 | 18 | 83 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT24SJBOS-8 | game_total | 0.253 | 0.295 | 0.286 | 30 | 71 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-SJ2 | team_total | 0.724 | 0.770 | 0.761 | 78 | 24 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.337 | 0.295 | 0.303 | 30 | 71 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT3 | team_total | 0.707 | 0.660 | 0.670 | 67 | 35 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR3 | game_spread | 0.191 | 0.155 | 0.162 | 16 | 85 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24TOREDM-EDM2 | game_spread | 0.438 | 0.395 | 0.404 | 40 | 61 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT24DETCGY-10 | game_total | 0.044 | 0.080 | 0.071 | 9 | 93 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA6 | team_total | 0.101 | 0.140 | 0.131 | 15 | 87 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TOREDM-EDM6 | team_total | 0.232 | 0.195 | 0.202 | 20 | 81 | yes | +0.021 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ BOS | 0.651 | 0.603 | 0.163 | 0.215 | 6.17 | 6.50 | 0.955/1.021 | KXNHLTEAMTOTAL-26OCT24SJBOS-SJ3 +0.079 |
| NYR @ OTT | 0.471 | 0.544 | 0.179 | 0.219 | 6.09 | 6.21 | 1.039/0.988 | KXNHLGAME-26OCT24NYROTT-NYR -0.073 |
| NSH @ PIT | 0.572 | 0.582 | 0.168 | 0.208 | 6.74 | 6.60 | 1.038/1.004 | KXNHLTOTAL-26OCT24NSHPIT-8 -0.025 |
| BUF @ WSH | 0.496 | 0.536 | 0.176 | 0.215 | 6.61 | 6.51 | 1.015/1.002 | KXNHLGAME-26OCT24BUFWSH-BUF -0.040 |
| VGK @ CBJ | 0.416 | 0.469 | 0.168 | 0.223 | 6.46 | 6.14 | 1.007/1.003 | KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 -0.079 |
| CAR @ STL | 0.510 | 0.525 | 0.178 | 0.219 | 6.14 | 6.46 | 0.976/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.058 |
| TOR @ EDM | 0.637 | 0.641 | 0.151 | 0.201 | 7.24 | 6.92 | 1.022/0.965 | KXNHLTOTAL-26OCT24TOREDM-8 -0.054 |
| TBL @ UTA | 0.554 | 0.577 | 0.176 | 0.216 | 6.08 | 6.34 | 0.990/0.973 | KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 +0.051 |
| DET @ CGY | 0.517 | 0.498 | 0.189 | 0.226 | 5.54 | 5.99 | 0.978/0.994 | KXNHLTOTAL-26OCT24DETCGY-7 +0.080 |
| MIN @ SEA | 0.471 | 0.522 | 0.175 | 0.216 | 6.26 | 6.29 | 1.001/0.991 | KXNHLGAME-26OCT24MINSEA-SEA +0.051 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Tanner Jeannot: 1+ goals YES @ 9c · p 0.116 (adj 0.1082) · $1.49 · thesis BOS:OFFENSE_4PLUS
- James Hagens: 1+ goals NO @ 78c · p 0.8149 (adj 0.8049) · $7.44 · thesis BOS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 21c · p 0.2424 (adj 0.2331) · $1.68 · thesis SJS:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 60c · p 0.6415 (adj 0.6299) · $3.96 · thesis BOS:SUPPRESSED
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1196 (adj 0.1072) · $2.34 · thesis NYR:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 57c · p 0.7129 (adj 0.6168) · $9.34 · thesis OTT:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 25c · p 0.3384 (adj 0.2892) · $3.35 · thesis NYR:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1084 (adj 0.0975) · $1.53 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 15c · p 0.2047 (adj 0.1885) · $3.72 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 34c · p 0.4125 (adj 0.3931) · $6.51 · thesis PIT:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 75c · p 0.8707 (adj 0.789) · $9.34 · thesis NSH:SUPPRESSED
- Sidney Crosby: 1+ goals YES @ 34c · p 0.3788 (adj 0.3679) · $2.01 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2405 (adj 0.2216) · $5.47 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 25c · p 0.3655 (adj 0.2872) · $3.1 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ assists NO @ 52c · p 0.608 (adj 0.5615) · $5.98 · thesis BUF:SUPPRESSED
- Jordan Kyrou: 1+ assists NO @ 65c · p 0.7247 (adj 0.6824) · $7.07 · thesis WSH:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2599 (adj 0.2487) · $2.69 · thesis CBJ:OFFENSE_4PLUS
- Adam Fantilli: 1+ assists NO @ 62c · p 0.6935 (adj 0.6518) · $5.87 · thesis CBJ:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 22c · p 0.2825 (adj 0.2644) · $4.61 · thesis STL:OFFENSE_4PLUS
- Justin Barron: 1+ goals YES @ 5c · p 0.0736 (adj 0.0652) · $1.3 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3311 (adj 0.3171) · $3.62 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1666 (adj 0.155) · $2.09 · thesis STL:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1514 (adj 0.1361) · $2.27 · thesis TOR:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 81c · p 0.8547 (adj 0.8423) · $9.34 · thesis TOR:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 37c · p 0.4855 (adj 0.4072) · $4.64 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3125 (adj 0.3006) · $3.39 · thesis EDM:OFFENSE_4PLUS
- Anthony Cirelli: 1+ goals YES @ 18c · p 0.2232 (adj 0.2112) · $2.81 · thesis TBL:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1528 (adj 0.1408) · $1.68 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.7782 (adj 0.7014) · $7.15 · thesis UTA:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 11c · p 0.1492 (adj 0.1344) · $2.1 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.74 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2296 (adj 0.2172) · $2.28 · thesis CGY:OFFENSE_4PLUS
- Lucas Raymond: 1+ goals NO @ 72c · p 0.7583 (adj 0.7475) · $5.76 · thesis DET:SUPPRESSED
- Berkly Catton: 1+ goals YES @ 16c · p 0.2173 (adj 0.1992) · $3.88 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1657 (adj 0.153) · $3.09 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1453 (adj 0.129) · $2.56 · thesis SEA:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 17c · p 0.2139 (adj 0.2004) · $2.8 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ BOS** · priced 208/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.44, exp saves 24.01 (sd 6.53), pull risk 0.055
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.84, exp saves 23.62 (sd 6.72), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.270 | 0.115 | 22/99 | +0.038 | STANDARD |
| Michael Kesselring: 1+ points | 0.240 | 0.115 | 21/98 | +0.018 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.409 | 0.530 | 54/48 | +0.093 | STANDARD |
| Sam Dickinson: 1+ assists | 0.221 | 0.105 | 20/99 | +0.010 | STANDARD |
| Michael Kesselring: 1+ assists | 0.195 | 0.090 | 17/99 | +0.015 | STANDARD |
| Adam Gaudette: 1+ points | 0.255 | 0.160 | 31/99 | -0.070 | STANDARD |

**NYR @ OTT** · priced 181/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Jonas Johansson (CONFIRMED) exp shots 23.91, exp saves 20.9 (sd 5.92), pull risk 0.054
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.38, exp saves 25.27 (sd 6.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.287 | 0.435 | 44/57 | +0.126 | STANDARD |
| Jake Sanderson: 1+ points | 0.372 | 0.515 | 53/50 | +0.111 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.338 | 0.240 | 25/77 | +0.075 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.392 | 0.295 | 31/72 | +0.067 | STANDARD |
| Jake Sanderson: 2+ points | 0.081 | 0.175 | 19/84 | +0.070 | STANDARD |
| Tim Stutzle: 2+ points | 0.226 | 0.315 | 33/70 | +0.060 | STANDARD |

**NSH @ PIT** · priced 172/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 26.07, exp saves 22.79 (sd 6.24), pull risk 0.059
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.45, exp saves 24.98 (sd 6.96), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ assists | 0.293 | 0.120 | 22/98 | +0.061 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.129 | 0.255 | 26/75 | +0.108 | STANDARD |
| Adam Wilsby: 1+ points | 0.343 | 0.230 | 27/81 | +0.059 | STANDARD |
| Thomas Novak: 2+ points | 0.197 | 0.105 | 19/98 | -0.004 | STANDARD |
| Rickard Rakell: 1+ points | 0.652 | 0.570 | 59/45 | +0.045 | STANDARD |
| Mavrik Bourque: 1+ points | 0.307 | 0.385 | 39/62 | +0.057 | STANDARD |

**BUF @ WSH** · priced 204/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.16, exp saves 24.43 (sd 6.67), pull risk 0.06
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 26.97, exp saves 23.14 (sd 6.53), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Sourdif: 1+ points | 0.317 | 0.170 | 30/96 | +0.002 | STANDARD |
| Timothy Liljegren: 1+ points | 0.230 | 0.095 | 18/99 | +0.040 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.212 | 0.085 | 16/99 | +0.043 | STANDARD |
| Ryan Leonard: 1+ assists | 0.365 | 0.245 | 25/76 | +0.102 | STANDARD |
| Timothy Liljegren: 1+ assists | 0.192 | 0.080 | 15/99 | +0.033 | STANDARD |
| Beck Malenstyn: 1+ points | 0.195 | 0.095 | 17/98 | +0.015 | STANDARD |

**VGK @ CBJ** · priced 180/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.34, exp saves 23.55 (sd 6.41), pull risk 0.066
- VGK net: Carter Hart (PROBABLE) exp shots 27.42, exp saves 23.74 (sd 6.42), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cam Talbot: 27+ saves | 0.315 | 0.465 | 48/55 | +0.118 |  |
| Jack Eichel: 2+ points | 0.246 | 0.375 | 39/64 | +0.097 | STANDARD |
| Jack Eichel: 1+ assists | 0.450 | 0.575 | 59/44 | +0.093 | STANDARD |
| Brayden McNabb: 1+ assists | 0.276 | 0.160 | 29/97 | -0.028 | STANDARD |
| Mathieu Olivier: 1+ assists | 0.202 | 0.095 | 18/99 | +0.012 | STANDARD |
| Zach Werenski: 1+ assists | 0.460 | 0.560 | 57/45 | +0.073 | STANDARD |

**CAR @ STL** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 30.19, exp saves 26.11 (sd 7.15), pull risk 0.065
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.37 (sd 5.89), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.362 | 0.485 | 49/52 | +0.100 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.347 | 0.455 | 47/56 | +0.075 | STANDARD |
| Seth Jarvis: 1+ assists | 0.207 | 0.315 | 34/71 | +0.068 | STANDARD |
| Jalen Chatfield: 1+ assists | 0.222 | 0.115 | 21/98 | -0.000 | STANDARD |
| Seth Jarvis: 1+ points | 0.404 | 0.505 | 53/52 | +0.059 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.419 | 0.520 | 53/49 | +0.074 | STANDARD |

**TOR @ EDM** · priced 202/210 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Formenton: 1+ points | 0.355 | 0.170 | 28/94 | +0.061 | STANDARD |
| Owen Michaels: 1+ points | 0.280 | 0.120 | 22/98 | +0.048 | STANDARD |
| Mathieu Joseph: 1+ points | 0.284 | 0.130 | 24/98 | +0.031 | STANDARD |
| Troy Stecher: 1+ assists | 0.213 | 0.080 | 15/99 | +0.054 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.430 | 45/59 | +0.091 | STANDARD |
| Leon Draisaitl: 2+ points | 0.372 | 0.495 | 51/52 | +0.091 | STANDARD |

**TBL @ UTA** · priced 174/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 26.79, exp saves 23.31 (sd 6.33), pull risk 0.051
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.6, exp saves 22.78 (sd 6.44), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.222 | 0.340 | 35/67 | +0.093 | STANDARD |
| Clayton Keller: 2+ points | 0.239 | 0.340 | 36/68 | +0.066 | STANDARD |
| Clayton Keller: 1+ assists | 0.460 | 0.555 | 56/45 | +0.073 | STANDARD |
| Nikita Kucherov: 2+ points | 0.283 | 0.365 | 38/65 | +0.051 | STANDARD |
| Lawson Crouse: 1+ assists | 0.256 | 0.175 | 20/85 | +0.044 | STANDARD |
| Brayden Point: 2+ points | 0.205 | 0.125 | 22/97 | -0.027 | STANDARD |

**DET @ CGY** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 29.78, exp saves 25.85 (sd 6.81), pull risk 0.053
- DET net: John Gibson (CONFIRMED) exp shots 27.65, exp saves 23.91 (sd 6.55), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Gibson: 24+ saves | 0.523 | 0.285 | 52/95 | -0.014 |  |
| Ben Jones: 1+ points | 0.199 | 0.320 | 36/72 | +0.066 | STANDARD |
| Aydar Suniev: 1+ assists | 0.237 | 0.130 | 24/98 | -0.015 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.281 | 0.375 | 39/64 | +0.063 | STANDARD |
| Dylan Larkin: 1+ assists | 0.326 | 0.410 | 43/61 | +0.047 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.235 | 0.155 | 18/87 | +0.044 | STANDARD |

**MIN @ SEA** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 30.26, exp saves 26.22 (sd 7.0), pull risk 0.06
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.36, exp saves 23.54 (sd 6.46), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kaapo Kakko: 1+ points | 0.498 | 0.250 | 42/92 | +0.061 | STANDARD |
| Adam Larsson: 1+ assists | 0.281 | 0.110 | 20/98 | +0.070 | STANDARD |
| Ryker Evans: 1+ assists | 0.274 | 0.120 | 22/98 | +0.042 | STANDARD |
| Ryker Evans: 1+ points | 0.323 | 0.175 | 27/92 | +0.039 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.255 | 0.390 | 40/62 | +0.108 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.364 | 0.240 | 28/80 | +0.070 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
