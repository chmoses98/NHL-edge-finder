# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T20:05:16Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 10 · markets on board: 4554 · contracts joined: 2418 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2168, 'NO_EDGE': 83, 'OK': 167}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 382, 'game_early_goal': 10, 'first_goal': 369, 'game_winner': 20, 'player_goals': 629, 'game_overtime': 10, 'player_points': 512, 'goalie_saves': 16, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ BOS | 2026-10-24T23:00:00Z | T-90m | 0.651 | 0.349 | 0.163 | 6.17 | 3.56 | 2.61 | 260 (25/235) | CONFIRMED/CONFIRMED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-90m | 0.471 | 0.529 | 0.179 | 6.09 | 2.95 | 3.14 | 232 (25/207) | CONFIRMED/CONFIRMED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-90m | 0.572 | 0.428 | 0.168 | 6.74 | 3.61 | 3.13 | 232 (25/207) | PROBABLE/CONFIRMED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-90m | 0.496 | 0.504 | 0.176 | 6.61 | 3.28 | 3.33 | 262 (25/237) | CONFIRMED/CONFIRMED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-90m | 0.416 | 0.584 | 0.168 | 6.46 | 2.96 | 3.50 | 244 (25/219) | CONFIRMED/PROBABLE |
| CAR @ STL | 2026-10-24T23:00:00Z | T-90m | 0.510 | 0.490 | 0.178 | 6.14 | 3.10 | 3.04 | 227 (25/202) | CONFIRMED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-90m | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 261 (25/236) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-3h | 0.554 | 0.446 | 0.176 | 6.08 | 3.21 | 2.87 | 235 (25/210) | PROBABLE/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-3h | 0.517 | 0.483 | 0.189 | 5.54 | 2.82 | 2.72 | 234 (25/209) | CONFIRMED/CONFIRMED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-3h | 0.505 | 0.495 | 0.184 | 6.05 | 3.05 | 3.00 | 231 (25/206) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.495 | 0.615 | 0.592 | 62 | 39 | no | +0.098 | OK |
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.505 | 0.380 | 0.404 | 39 | 63 | yes | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.295 | 0.420 | 0.394 | 43 | 59 | no | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.520 | 0.640 | 0.617 | 65 | 37 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.271 | 0.385 | 0.361 | 39 | 62 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.365 | 0.480 | 0.456 | 49 | 53 | no | +0.087 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.447 | 0.555 | 0.533 | 56 | 45 | no | +0.086 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.686 | 0.785 | 0.767 | 79 | 22 | no | +0.082 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.158 | 0.260 | 0.237 | 27 | 75 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.586 | 0.690 | 0.670 | 70 | 32 | no | +0.078 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.429 | 0.525 | 0.506 | 53 | 48 | no | +0.074 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.490 | 0.585 | 0.566 | 59 | 42 | no | +0.073 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.510 | 0.415 | 0.434 | 42 | 59 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.341 | 0.435 | 0.416 | 44 | 57 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.139 | 0.230 | 0.209 | 24 | 78 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.752 | 0.840 | 0.825 | 85 | 17 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.162 | 0.245 | 0.226 | 25 | 76 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.757 | 0.835 | 0.821 | 84 | 17 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.273 | 0.355 | 0.338 | 36 | 65 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.139 | 0.215 | 0.198 | 22 | 79 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.189 | 0.270 | 0.252 | 28 | 74 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.279 | 0.205 | 0.219 | 21 | 80 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.786 | 0.855 | 0.843 | 86 | 15 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.589 | 0.670 | 0.654 | 68 | 34 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.173 | 0.245 | 0.229 | 25 | 76 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.799 | 0.865 | 0.854 | 87 | 14 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.293 | 0.220 | 0.233 | 23 | 79 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.373 | 0.450 | 0.434 | 46 | 56 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.242 | 0.310 | 0.296 | 32 | 70 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.798 | 0.855 | 0.845 | 86 | 15 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.224 | 0.290 | 0.276 | 30 | 72 | no | +0.042 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.041 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.842 | 0.895 | 0.886 | 90 | 11 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.148 | 0.205 | 0.192 | 21 | 80 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.167 | 0.225 | 0.212 | 23 | 78 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.353 | 0.415 | 0.402 | 42 | 59 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.597 | 0.535 | 0.548 | 54 | 47 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.197 | 0.260 | 0.246 | 27 | 75 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.336 | 0.395 | 0.383 | 40 | 61 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.311 | 0.255 | 0.266 | 26 | 75 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.628 | 0.685 | 0.674 | 69 | 32 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.114 | 0.170 | 0.157 | 18 | 84 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.260 | 0.315 | 0.303 | 32 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.785 | 0.835 | 0.826 | 84 | 17 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.410 | 0.465 | 0.454 | 47 | 54 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.571 | 0.630 | 0.618 | 64 | 38 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.054 | 0.095 | 0.085 | 10 | 91 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.168 | 0.125 | 0.133 | 13 | 88 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT4 | team_total | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.030 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-7 | game_total | 0.443 | 0.495 | 0.485 | 50 | 51 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.250 | 0.200 | 0.209 | 21 | 81 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-5 | game_total | 0.771 | 0.820 | 0.811 | 83 | 19 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB2 | team_total | 0.771 | 0.815 | 0.807 | 82 | 19 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT24MINSEA-5 | game_total | 0.750 | 0.795 | 0.787 | 80 | 21 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT6 | team_total | 0.155 | 0.110 | 0.118 | 12 | 90 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT5 | team_total | 0.301 | 0.255 | 0.264 | 26 | 75 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT5 | team_total | 0.181 | 0.230 | 0.220 | 24 | 78 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-8 | game_total | 0.299 | 0.250 | 0.259 | 26 | 76 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT24SJBOS-6 | game_total | 0.558 | 0.605 | 0.596 | 61 | 40 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL5 | team_total | 0.204 | 0.160 | 0.168 | 17 | 85 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.173 | 0.135 | 0.142 | 14 | 87 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK3 | team_total | 0.690 | 0.645 | 0.654 | 65 | 36 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA2 | team_total | 0.828 | 0.865 | 0.858 | 87 | 14 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.204 | 0.245 | 0.236 | 25 | 76 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-9 | game_total | 0.214 | 0.175 | 0.182 | 18 | 83 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT24SJBOS-8 | game_total | 0.253 | 0.295 | 0.286 | 30 | 71 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-SJ2 | team_total | 0.724 | 0.770 | 0.761 | 78 | 24 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.337 | 0.295 | 0.303 | 30 | 71 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-10 | game_total | 0.128 | 0.095 | 0.101 | 10 | 91 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT3 | team_total | 0.707 | 0.660 | 0.670 | 67 | 35 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR3 | game_spread | 0.191 | 0.155 | 0.162 | 16 | 85 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6 | team_total | 0.082 | 0.120 | 0.111 | 13 | 89 | no | +0.021 | OK |
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
| MIN @ SEA | 0.505 | 0.513 | 0.184 | 0.217 | 6.05 | 6.32 | 1.015/0.991 | KXNHLTOTAL-26OCT24MINSEA-5 +0.048 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 36 recommended · full analysis in card.md / packet.json `thesis_card`

- Macklin Celebrini: 2+ assists NO @ 83c · p 0.9056 (adj 0.8628) · $9.26 · thesis SJS:SUPPRESSED
- Tanner Jeannot: 1+ goals YES @ 9c · p 0.116 (adj 0.1082) · $1.49 · thesis BOS:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 60c · p 0.6415 (adj 0.6299) · $3.96 · thesis BOS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 21c · p 0.2424 (adj 0.2318) · $1.64 · thesis SJS:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1196 (adj 0.1072) · $2.47 · thesis NYR:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 58c · p 0.7129 (adj 0.62) · $7.89 · thesis OTT:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 8c · p 0.1084 (adj 0.0975) · $1.49 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 14c · p 0.1697 (adj 0.1598) · $1.6 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 15c · p 0.2047 (adj 0.1885) · $3.69 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 34c · p 0.4125 (adj 0.3931) · $6.45 · thesis PIT:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 76c · p 0.8707 (adj 0.7922) · $9.26 · thesis NSH:SUPPRESSED
- Sidney Crosby: 1+ goals YES @ 34c · p 0.3788 (adj 0.3666) · $1.77 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2405 (adj 0.2216) · $5.32 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 25c · p 0.3655 (adj 0.2872) · $2.97 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ assists NO @ 52c · p 0.608 (adj 0.5615) · $5.95 · thesis BUF:SUPPRESSED
- Rasmus Dahlin: 1+ goals NO @ 80c · p 0.8339 (adj 0.8242) · $7.93 · thesis BUF:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2599 (adj 0.2487) · $2.66 · thesis CBJ:OFFENSE_4PLUS
- Adam Fantilli: 1+ assists NO @ 62c · p 0.6935 (adj 0.6518) · $5.82 · thesis CBJ:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 22c · p 0.2825 (adj 0.2656) · $4.77 · thesis STL:OFFENSE_4PLUS
- Justin Barron: 1+ goals YES @ 5c · p 0.0736 (adj 0.0652) · $1.29 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3311 (adj 0.3171) · $3.58 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1666 (adj 0.155) · $2.07 · thesis STL:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1514 (adj 0.1373) · $2.41 · thesis TOR:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 81c · p 0.8547 (adj 0.8423) · $9.26 · thesis TOR:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 37c · p 0.4855 (adj 0.4072) · $4.59 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3125 (adj 0.3006) · $3.36 · thesis EDM:OFFENSE_4PLUS
- Anthony Cirelli: 1+ goals YES @ 18c · p 0.2232 (adj 0.2112) · $2.81 · thesis TBL:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1528 (adj 0.1408) · $1.62 · thesis UTA:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 11c · p 0.1492 (adj 0.1344) · $2.08 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.74 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2296 (adj 0.2172) · $2.28 · thesis CGY:OFFENSE_4PLUS
- Justin Faulk: 1+ goals NO @ 89c · p 0.9152 (adj 0.9077) · $9.26 · thesis DET:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.145 (adj 0.1312) · $2.78 · thesis SEA:OFFENSE_4PLUS
- Minnesota wins by over 2.5 goals NO @ 75c · p 0.8391 (adj 0.7895) · $9.26 · thesis SEA:WINS
- Mackie Samoskevich: 1+ goals YES @ 19c · p 0.2375 (adj 0.2244) · $3.06 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1602 (adj 0.1464) · $2.15 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ BOS** · priced 208/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.44, exp saves 24.01 (sd 6.53), pull risk 0.055
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.84, exp saves 23.62 (sd 6.72), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.270 | 0.115 | 22/99 | +0.038 | STANDARD |
| Michael Kesselring: 1+ points | 0.240 | 0.110 | 20/98 | +0.029 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.409 | 0.530 | 54/48 | +0.093 | STANDARD |
| Sam Dickinson: 1+ assists | 0.221 | 0.105 | 20/99 | +0.010 | STANDARD |
| Mason Lohrei: 1+ points | 0.266 | 0.160 | 30/98 | -0.049 | STANDARD |
| Michael Kesselring: 1+ assists | 0.195 | 0.090 | 17/99 | +0.015 | STANDARD |

**NYR @ OTT** · priced 175/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Jonas Johansson (CONFIRMED) exp shots 23.91, exp saves 20.9 (sd 5.92), pull risk 0.054
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.38, exp saves 25.27 (sd 6.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artem Zub: 1+ points | 0.293 | 0.145 | 27/98 | +0.009 | STANDARD |
| Jake Sanderson: 1+ assists | 0.287 | 0.430 | 44/58 | +0.116 | STANDARD |
| Jake Sanderson: 1+ points | 0.372 | 0.510 | 53/51 | +0.101 | STANDARD |
| Artem Zub: 1+ assists | 0.255 | 0.125 | 24/99 | +0.003 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.338 | 0.230 | 25/79 | +0.075 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.392 | 0.290 | 31/73 | +0.067 | STANDARD |

**NSH @ PIT** · priced 172/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 26.07, exp saves 22.79 (sd 6.24), pull risk 0.059
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.45, exp saves 24.98 (sd 6.96), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ points | 0.343 | 0.150 | 27/97 | +0.059 | STANDARD |
| Adam Wilsby: 1+ assists | 0.293 | 0.115 | 22/99 | +0.061 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.129 | 0.250 | 26/76 | +0.098 | STANDARD |
| Thomas Novak: 2+ points | 0.197 | 0.105 | 19/98 | -0.004 | STANDARD |
| Rickard Rakell: 1+ points | 0.652 | 0.570 | 59/45 | +0.045 | STANDARD |
| Rickard Rakell: 1+ goals | 0.412 | 0.335 | 34/67 | +0.057 | STANDARD |

**BUF @ WSH** · priced 204/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.16, exp saves 24.43 (sd 6.67), pull risk 0.06
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 26.97, exp saves 23.14 (sd 6.53), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Peyton Krebs: 1+ points | 0.321 | 0.165 | 31/98 | -0.004 | STANDARD |
| Timothy Liljegren: 1+ points | 0.230 | 0.095 | 18/99 | +0.040 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.212 | 0.085 | 16/99 | +0.043 | STANDARD |
| Ukko-Pekka Luukkonen: 27+ saves | 0.293 | 0.420 | 54/70 | -0.008 |  |
| Ryan Leonard: 1+ assists | 0.365 | 0.245 | 25/76 | +0.102 | STANDARD |
| Timothy Liljegren: 1+ assists | 0.192 | 0.080 | 15/99 | +0.033 | STANDARD |

**VGK @ CBJ** · priced 180/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.34, exp saves 23.55 (sd 6.41), pull risk 0.066
- VGK net: Carter Hart (PROBABLE) exp shots 27.42, exp saves 23.74 (sd 6.42), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cam Talbot: 27+ saves | 0.315 | 0.460 | 47/55 | +0.118 |  |
| Jack Eichel: 2+ points | 0.246 | 0.375 | 39/64 | +0.097 | STANDARD |
| Jack Eichel: 1+ assists | 0.450 | 0.575 | 59/44 | +0.093 | STANDARD |
| Brayden McNabb: 1+ assists | 0.276 | 0.155 | 29/98 | -0.028 | STANDARD |
| Mathieu Olivier: 1+ assists | 0.202 | 0.095 | 18/99 | +0.012 | STANDARD |
| Zach Werenski: 1+ assists | 0.460 | 0.560 | 57/45 | +0.073 | STANDARD |

**CAR @ STL** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 30.19, exp saves 26.11 (sd 7.15), pull risk 0.065
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.37 (sd 5.89), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Hofer: 27+ saves | 0.474 | 0.350 | 53/83 | -0.073 |  |
| Sebastian Aho: 1+ assists | 0.362 | 0.485 | 49/52 | +0.100 | STANDARD |
| Jalen Chatfield: 1+ assists | 0.222 | 0.110 | 21/99 | -0.000 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.347 | 0.455 | 47/56 | +0.075 | STANDARD |
| Seth Jarvis: 1+ assists | 0.207 | 0.315 | 34/71 | +0.068 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.419 | 0.520 | 53/49 | +0.074 | STANDARD |

**TOR @ EDM** · priced 202/210 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Michaels: 1+ points | 0.280 | 0.135 | 24/97 | +0.027 | STANDARD |
| Troy Stecher: 1+ assists | 0.213 | 0.080 | 15/99 | +0.054 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.430 | 45/59 | +0.091 | STANDARD |
| Jake McCabe: 1+ assists | 0.238 | 0.115 | 21/98 | +0.016 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.514 | 0.635 | 64/37 | +0.099 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.338 | 0.220 | 23/79 | +0.096 | STANDARD |

**TBL @ UTA** · priced 174/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 26.79, exp saves 23.31 (sd 6.33), pull risk 0.051
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.6, exp saves 22.78 (sd 6.44), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.649 | 0.525 | 71/66 | -0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.222 | 0.335 | 35/68 | +0.083 | STANDARD |
| Clayton Keller: 2+ points | 0.239 | 0.340 | 36/68 | +0.066 | STANDARD |
| Clayton Keller: 1+ assists | 0.460 | 0.555 | 56/45 | +0.073 | STANDARD |
| Brayden Point: 2+ points | 0.205 | 0.115 | 21/98 | -0.016 | STANDARD |
| Lawson Crouse: 1+ points | 0.420 | 0.330 | 36/70 | +0.044 | STANDARD |

**DET @ CGY** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 29.78, exp saves 25.85 (sd 6.81), pull risk 0.053
- DET net: John Gibson (CONFIRMED) exp shots 27.65, exp saves 23.91 (sd 6.55), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ben Jones: 1+ points | 0.199 | 0.320 | 36/72 | +0.066 | STANDARD |
| John Gibson: 24+ saves | 0.523 | 0.405 | 51/70 | -0.004 |  |
| Aydar Suniev: 1+ assists | 0.237 | 0.125 | 24/99 | -0.015 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.281 | 0.370 | 39/65 | +0.054 | STANDARD |
| Dylan Larkin: 1+ assists | 0.326 | 0.405 | 43/62 | +0.038 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.235 | 0.160 | 18/86 | +0.044 | STANDARD |

**MIN @ SEA** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.26 (sd 6.98), pull risk 0.059
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.36, exp saves 23.55 (sd 6.5), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kaapo Kakko: 1+ points | 0.503 | 0.225 | 43/98 | +0.056 | STANDARD |
| Ryker Evans: 1+ points | 0.318 | 0.145 | 27/98 | +0.034 | STANDARD |
| Adam Larsson: 1+ assists | 0.278 | 0.105 | 20/99 | +0.066 | STANDARD |
| Ryker Evans: 1+ assists | 0.268 | 0.115 | 22/99 | +0.036 | STANDARD |
| Adam Larsson: 1+ points | 0.332 | 0.205 | 24/83 | +0.079 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.264 | 0.380 | 39/63 | +0.090 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
