# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T17:59:05Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 11 · markets on board: 4550 · contracts joined: 2481 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2206, 'NO_EDGE': 113, 'OK': 162}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 350, 'game_early_goal': 11, 'first_goal': 403, 'game_winner': 22, 'player_goals': 690, 'game_overtime': 11, 'player_points': 464, 'game_spread': 44, 'team_total': 110, 'game_total': 99, 'goalie_saves': 13}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NJD | 2026-10-24T19:30:00Z | T-90m | 0.617 | 0.383 | 0.180 | 5.88 | 3.30 | 2.58 | 214 (25/189) | CONFIRMED/PROJECTED |
| SJS @ BOS | 2026-10-24T23:00:00Z | T-3h | 0.651 | 0.349 | 0.163 | 6.17 | 3.56 | 2.61 | 243 (25/218) | CONFIRMED/CONFIRMED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-3h | 0.471 | 0.529 | 0.179 | 6.09 | 2.95 | 3.14 | 230 (25/205) | CONFIRMED/CONFIRMED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-3h | 0.572 | 0.428 | 0.168 | 6.74 | 3.61 | 3.13 | 212 (25/187) | PROBABLE/CONFIRMED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-3h | 0.496 | 0.504 | 0.176 | 6.61 | 3.28 | 3.33 | 236 (25/211) | CONFIRMED/CONFIRMED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-3h | 0.416 | 0.584 | 0.168 | 6.46 | 2.96 | 3.50 | 227 (25/202) | CONFIRMED/PROBABLE |
| CAR @ STL | 2026-10-24T23:00:00Z | T-3h | 0.510 | 0.490 | 0.178 | 6.14 | 3.10 | 3.04 | 217 (25/192) | CONFIRMED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-3h | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 234 (25/209) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-6h | 0.559 | 0.441 | 0.176 | 6.08 | 3.21 | 2.87 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-6h | 0.517 | 0.483 | 0.189 | 5.54 | 2.82 | 2.72 | 230 (25/205) | CONFIRMED/CONFIRMED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-6h | 0.518 | 0.482 | 0.182 | 6.11 | 3.11 | 3.00 | 213 (25/188) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.295 | 0.425 | 0.398 | 44 | 59 | no | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.520 | 0.640 | 0.617 | 65 | 37 | no | +0.094 | OK |
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.518 | 0.405 | 0.427 | 41 | 60 | yes | +0.091 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.447 | 0.555 | 0.533 | 56 | 45 | no | +0.086 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.686 | 0.785 | 0.767 | 79 | 22 | no | +0.082 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.482 | 0.585 | 0.565 | 59 | 42 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.268 | 0.365 | 0.344 | 37 | 64 | no | +0.076 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.429 | 0.525 | 0.506 | 53 | 48 | no | +0.073 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.490 | 0.585 | 0.566 | 59 | 42 | no | +0.073 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.510 | 0.415 | 0.434 | 42 | 59 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.341 | 0.435 | 0.416 | 44 | 57 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.156 | 0.250 | 0.229 | 26 | 76 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.363 | 0.460 | 0.440 | 47 | 55 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.139 | 0.235 | 0.213 | 25 | 78 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.751 | 0.835 | 0.820 | 84 | 17 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.162 | 0.245 | 0.226 | 25 | 76 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.297 | 0.215 | 0.230 | 22 | 79 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.541 | 0.630 | 0.613 | 64 | 38 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.185 | 0.270 | 0.251 | 28 | 74 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.273 | 0.355 | 0.338 | 36 | 65 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.139 | 0.215 | 0.198 | 22 | 79 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.752 | 0.840 | 0.825 | 86 | 18 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.587 | 0.675 | 0.658 | 69 | 34 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.786 | 0.860 | 0.847 | 87 | 15 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.173 | 0.245 | 0.229 | 25 | 76 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.799 | 0.865 | 0.854 | 87 | 14 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.293 | 0.220 | 0.233 | 23 | 79 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.589 | 0.665 | 0.650 | 68 | 35 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.224 | 0.295 | 0.280 | 31 | 72 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.841 | 0.900 | 0.890 | 91 | 11 | no | +0.042 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.148 | 0.205 | 0.192 | 21 | 80 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.353 | 0.415 | 0.402 | 42 | 59 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.245 | 0.310 | 0.296 | 32 | 70 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.335 | 0.395 | 0.383 | 40 | 61 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.170 | 0.225 | 0.213 | 23 | 78 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.311 | 0.255 | 0.266 | 26 | 75 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.392 | 0.330 | 0.342 | 34 | 68 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.114 | 0.170 | 0.157 | 18 | 84 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-8 | game_total | 0.299 | 0.245 | 0.255 | 25 | 76 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.260 | 0.315 | 0.303 | 32 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.785 | 0.835 | 0.826 | 84 | 17 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.337 | 0.285 | 0.295 | 29 | 72 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.571 | 0.630 | 0.618 | 64 | 38 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.410 | 0.465 | 0.454 | 47 | 54 | no | +0.032 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.471 | 0.525 | 0.514 | 53 | 48 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-BOS4 | team_total | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.373 | 0.430 | 0.418 | 44 | 58 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.197 | 0.255 | 0.243 | 27 | 76 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT4 | team_total | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.607 | 0.550 | 0.562 | 56 | 46 | yes | +0.030 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-7 | game_total | 0.443 | 0.495 | 0.485 | 50 | 51 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.178 | 0.135 | 0.143 | 14 | 87 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.250 | 0.200 | 0.209 | 21 | 81 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-5 | game_total | 0.771 | 0.820 | 0.811 | 83 | 19 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT6 | team_total | 0.155 | 0.105 | 0.114 | 12 | 91 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.200 | 0.245 | 0.236 | 25 | 76 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-7 | game_total | 0.534 | 0.485 | 0.495 | 49 | 52 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-7 | game_total | 0.492 | 0.445 | 0.454 | 45 | 56 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.173 | 0.135 | 0.142 | 14 | 87 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK3 | team_total | 0.690 | 0.640 | 0.650 | 65 | 37 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA2 | team_total | 0.827 | 0.865 | 0.858 | 87 | 14 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-9 | game_total | 0.214 | 0.175 | 0.182 | 18 | 83 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-SJ2 | team_total | 0.724 | 0.770 | 0.761 | 78 | 24 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6 | team_total | 0.081 | 0.125 | 0.115 | 14 | 89 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT24TOREDM-9 | game_total | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-10 | game_total | 0.128 | 0.095 | 0.101 | 10 | 91 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT3 | team_total | 0.707 | 0.660 | 0.670 | 67 | 35 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT24LANJ-5 | game_total | 0.736 | 0.775 | 0.768 | 78 | 23 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT24DETCGY-10 | game_total | 0.044 | 0.080 | 0.071 | 9 | 93 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.054 | 0.095 | 0.085 | 11 | 92 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TOREDM-EDM6 | team_total | 0.232 | 0.190 | 0.198 | 20 | 82 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24BUFWSH-WSH3 | game_spread | 0.169 | 0.205 | 0.197 | 21 | 80 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-SJ4 | team_total | 0.276 | 0.320 | 0.311 | 33 | 69 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.178 | 0.145 | 0.151 | 15 | 86 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK6 | team_total | 0.136 | 0.095 | 0.102 | 11 | 92 | yes | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NJD | 0.617 | 0.548 | 0.180 | 0.225 | 5.88 | 5.82 | 0.983/0.992 | KXNHLGAME-26OCT24LANJ-LA +0.068 |
| SJS @ BOS | 0.651 | 0.603 | 0.163 | 0.215 | 6.17 | 6.50 | 0.955/1.021 | KXNHLTEAMTOTAL-26OCT24SJBOS-SJ3 +0.079 |
| NYR @ OTT | 0.471 | 0.544 | 0.179 | 0.219 | 6.09 | 6.21 | 1.039/0.988 | KXNHLGAME-26OCT24NYROTT-NYR -0.073 |
| NSH @ PIT | 0.572 | 0.582 | 0.168 | 0.208 | 6.74 | 6.60 | 1.038/1.004 | KXNHLTOTAL-26OCT24NSHPIT-8 -0.025 |
| BUF @ WSH | 0.496 | 0.536 | 0.176 | 0.215 | 6.61 | 6.51 | 1.015/1.002 | KXNHLGAME-26OCT24BUFWSH-BUF -0.040 |
| VGK @ CBJ | 0.416 | 0.469 | 0.168 | 0.223 | 6.46 | 6.14 | 1.007/1.003 | KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 -0.079 |
| CAR @ STL | 0.510 | 0.525 | 0.178 | 0.219 | 6.14 | 6.46 | 0.976/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.058 |
| TOR @ EDM | 0.637 | 0.641 | 0.151 | 0.201 | 7.24 | 6.92 | 1.022/0.965 | KXNHLTOTAL-26OCT24TOREDM-8 -0.054 |
| TBL @ UTA | 0.559 | 0.572 | 0.176 | 0.215 | 6.08 | 6.35 | 0.992/0.973 | KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 +0.049 |
| DET @ CGY | 0.517 | 0.498 | 0.189 | 0.226 | 5.54 | 5.99 | 0.978/0.994 | KXNHLTOTAL-26OCT24DETCGY-7 +0.080 |
| MIN @ SEA | 0.518 | 0.514 | 0.182 | 0.223 | 6.11 | 6.34 | 1.015/0.995 | KXNHLTOTAL-26OCT24MINSEA-7 +0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Jack Hughes: 1+ goals NO @ 62c · p 0.6962 (adj 0.6759) · $6.36 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 73c · p 0.7895 (adj 0.7734) · $6.36 · thesis NJD:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2766 (adj 0.2637) · $2.27 · thesis LAK:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 73c · p 0.7963 (adj 0.7607) · $3.81 · thesis LAK:WINS
- Tanner Jeannot: 1+ goals YES @ 9c · p 0.116 (adj 0.1082) · $1.38 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 67c · p 0.7377 (adj 0.6988) · $4.41 · thesis BOS:SUPPRESSED
- David Pastrnak: 1+ goals NO @ 60c · p 0.6415 (adj 0.6299) · $3.04 · thesis BOS:SUPPRESSED
- Taylor Raddysh: 1+ goals YES @ 7c · p 0.1196 (adj 0.1035) · $2.77 · thesis NYR:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1084 (adj 0.0963) · $1.21 · thesis OTT:OFFENSE_4PLUS
- Tim Stutzle: 1+ goals NO @ 65c · p 0.6964 (adj 0.6835) · $5.07 · thesis OTT:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 59c · p 0.7129 (adj 0.6233) · $4.57 · thesis OTT:SUPPRESSED
- Rickard Rakell: 1+ goals YES @ 34c · p 0.4125 (adj 0.3931) · $5.91 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 15c · p 0.2047 (adj 0.1873) · $3.21 · thesis PIT:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 76c · p 0.8707 (adj 0.7922) · $8.48 · thesis NSH:SUPPRESSED
- Sidney Crosby: 1+ goals YES @ 34c · p 0.3788 (adj 0.3666) · $1.62 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2405 (adj 0.2179) · $4.45 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ assists NO @ 52c · p 0.608 (adj 0.5615) · $5.46 · thesis BUF:SUPPRESSED
- Boone Jenner: 1+ goals YES @ 16c · p 0.1971 (adj 0.1828) · $1.55 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ goals NO @ 80c · p 0.8339 (adj 0.8242) · $7.25 · thesis BUF:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2599 (adj 0.2487) · $2.22 · thesis CBJ:OFFENSE_4PLUS
- Trevor Connelly: 1+ goals NO @ 77c · p 0.8028 (adj 0.7933) · $5.49 · thesis VGK:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 21c · p 0.2825 (adj 0.2606) · $4.96 · thesis STL:OFFENSE_4PLUS
- Justin Barron: 1+ goals YES @ 5c · p 0.0736 (adj 0.064) · $1.03 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1666 (adj 0.1537) · $1.78 · thesis STL:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7287 (adj 0.714) · $6.88 · thesis CAR:SUPPRESSED
- Gavin McKenna: 1+ goals NO @ 81c · p 0.8547 (adj 0.8423) · $8.48 · thesis TOR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1514 (adj 0.1348) · $1.94 · thesis TOR:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3125 (adj 0.3006) · $2.22 · thesis EDM:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 24c · p 0.3383 (adj 0.2679) · $1.75 · thesis EDM:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1492 (adj 0.1269) · $2.06 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.6 · thesis CGY:OFFENSE_4PLUS
- Justin Faulk: 1+ goals NO @ 89c · p 0.9152 (adj 0.9077) · $8.48 · thesis DET:SUPPRESSED
- Viktor Arvidsson: 1+ assists NO @ 64c · p 0.7195 (adj 0.6698) · $4.23 · thesis DET:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6248 (adj 0.6024) · $8.48 · thesis MIN:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1455 (adj 0.1304) · $2.57 · thesis SEA:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ goals YES @ 18c · p 0.2391 (adj 0.2206) · $3.62 · thesis SEA:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 16c · p 0.212 (adj 0.1953) · $3.03 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NJD** · priced 156/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 26.53, exp saves 23.14 (sd 6.28), pull risk 0.045
- LAK net: Darcy Kuemper (PROJECTED) exp shots 30.31, exp saves 26.06 (sd 7.05), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.210 | 0.405 | 42/61 | +0.164 | STANDARD |
| Luke Evangelista: 1+ points | 0.371 | 0.535 | 54/47 | +0.142 | STANDARD |
| Jack Hughes: 2+ points | 0.214 | 0.335 | 35/68 | +0.091 | STANDARD |
| Jack Hughes: 1+ assists | 0.395 | 0.515 | 53/50 | +0.087 | STANDARD |
| Jack Hughes: 1+ points | 0.579 | 0.690 | 70/32 | +0.086 | STANDARD |
| Luke Evangelista: 2+ points | 0.082 | 0.185 | 20/83 | +0.078 | STANDARD |

**SJS @ BOS** · priced 191/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.44, exp saves 24.01 (sd 6.53), pull risk 0.055
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.84, exp saves 23.62 (sd 6.72), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.409 | 0.515 | 53/50 | +0.073 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.420 | 0.505 | 52/51 | +0.052 | STANDARD |
| David Pastrnak: 2+ points | 0.327 | 0.405 | 42/61 | +0.047 | STANDARD |
| JJ Peterka: 1+ assists | 0.262 | 0.340 | 35/67 | +0.052 | STANDARD |
| Tyler Toffoli: 1+ points | 0.439 | 0.365 | 38/65 | +0.043 | STANDARD |
| Mason Marchment: 1+ goals | 0.242 | 0.170 | 21/87 | +0.021 | STANDARD |

**NYR @ OTT** · priced 173/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Jonas Johansson (CONFIRMED) exp shots 23.91, exp saves 20.9 (sd 5.92), pull risk 0.054
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.38, exp saves 25.27 (sd 6.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Johansson: 22+ saves | 0.447 | 0.270 | 47/93 | -0.040 |  |
| Jake Sanderson: 1+ points | 0.372 | 0.510 | 53/51 | +0.101 | STANDARD |
| Jake Sanderson: 1+ assists | 0.287 | 0.425 | 44/59 | +0.106 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.338 | 0.230 | 25/79 | +0.075 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.392 | 0.290 | 31/73 | +0.067 | STANDARD |
| Jordan Spence: 1+ points | 0.345 | 0.250 | 26/76 | +0.071 | STANDARD |

**NSH @ PIT** · priced 152/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 26.07, exp saves 22.79 (sd 6.24), pull risk 0.059
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.45, exp saves 24.98 (sd 6.96), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.129 | 0.250 | 26/76 | +0.098 | STANDARD |
| Thomas Novak: 2+ points | 0.197 | 0.105 | 19/98 | -0.004 | STANDARD |
| Rickard Rakell: 1+ points | 0.652 | 0.570 | 59/45 | +0.045 | STANDARD |
| Mavrik Bourque: 1+ points | 0.307 | 0.385 | 39/62 | +0.057 | STANDARD |
| Rickard Rakell: 1+ goals | 0.412 | 0.335 | 34/67 | +0.057 | STANDARD |
| Connor Dewar: 1+ goals | 0.205 | 0.135 | 15/88 | +0.046 | STANDARD |

**BUF @ WSH** · priced 181/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.16, exp saves 24.43 (sd 6.67), pull risk 0.06
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 26.97, exp saves 23.14 (sd 6.53), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 27+ saves | 0.293 | 0.635 | 88/61 | +0.080 |  |
| Ryan Leonard: 1+ assists | 0.365 | 0.235 | 25/78 | +0.102 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.392 | 0.485 | 49/52 | +0.071 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.240 | 0.150 | 17/87 | +0.061 | STANDARD |
| Aliaksei Protas: 1+ points | 0.451 | 0.370 | 38/64 | +0.055 | STANDARD |
| Ryan Leonard: 1+ points | 0.506 | 0.425 | 43/58 | +0.059 | STANDARD |

**VGK @ CBJ** · priced 163/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.34, exp saves 23.55 (sd 6.41), pull risk 0.066
- VGK net: Carter Hart (PROBABLE) exp shots 27.42, exp saves 23.74 (sd 6.42), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cam Talbot: 27+ saves | 0.315 | 0.445 | 46/57 | +0.098 |  |
| Jack Eichel: 1+ assists | 0.450 | 0.575 | 59/44 | +0.093 | STANDARD |
| Jack Eichel: 2+ points | 0.246 | 0.370 | 39/65 | +0.088 | STANDARD |
| Zach Werenski: 1+ assists | 0.460 | 0.555 | 57/46 | +0.063 | STANDARD |
| Jack Eichel: 2+ assists | 0.122 | 0.215 | 24/81 | +0.057 | STANDARD |
| Adam Fantilli: 1+ assists | 0.306 | 0.385 | 40/63 | +0.047 | STANDARD |

**CAR @ STL** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 30.19, exp saves 26.11 (sd 7.15), pull risk 0.065
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.37 (sd 5.89), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.362 | 0.485 | 49/52 | +0.100 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.347 | 0.445 | 45/56 | +0.075 | STANDARD |
| Seth Jarvis: 1+ assists | 0.207 | 0.305 | 33/72 | +0.058 | STANDARD |
| Philip Broberg: 1+ points | 0.482 | 0.385 | 41/64 | +0.055 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.419 | 0.515 | 53/50 | +0.064 | STANDARD |
| Seth Jarvis: 1+ points | 0.404 | 0.495 | 52/53 | +0.049 | STANDARD |

**TOR @ EDM** · priced 175/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.420 | 44/60 | +0.081 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.514 | 0.625 | 64/39 | +0.079 | STANDARD |
| Leon Draisaitl: 2+ points | 0.372 | 0.480 | 50/54 | +0.071 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.338 | 0.230 | 24/78 | +0.086 | STANDARD |
| Gavin McKenna: 1+ points | 0.350 | 0.455 | 47/56 | +0.073 | STANDARD |
| Ryan Nugent-Hopkins: 1+ points | 0.470 | 0.575 | 60/45 | +0.062 | STANDARD |

**TBL @ UTA** · priced 164/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.3 (sd 6.37), pull risk 0.052
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.6, exp saves 22.78 (sd 6.46), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.220 | 0.335 | 36/69 | +0.075 | STANDARD |
| Lawson Crouse: 1+ goals | 0.227 | 0.115 | 19/96 | +0.026 | STANDARD |
| Clayton Keller: 2+ points | 0.245 | 0.340 | 36/68 | +0.060 | STANDARD |
| Clayton Keller: 1+ assists | 0.449 | 0.540 | 56/48 | +0.053 | STANDARD |
| Brayden Point: 2+ points | 0.207 | 0.120 | 21/97 | -0.015 | STANDARD |
| Jack McBain: 1+ goals | 0.154 | 0.070 | 12/98 | +0.027 | STANDARD |

**DET @ CGY** · priced 172/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 29.78, exp saves 25.85 (sd 6.81), pull risk 0.053
- DET net: John Gibson (CONFIRMED) exp shots 27.65, exp saves 23.91 (sd 6.55), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ points | 0.269 | 0.135 | 22/95 | +0.037 | STANDARD |
| Kevin Bahl: 1+ points | 0.297 | 0.170 | 26/92 | +0.024 | STANDARD |
| Ben Jones: 1+ points | 0.199 | 0.325 | 37/72 | +0.066 | STANDARD |
| Aydar Suniev: 1+ goals | 0.230 | 0.105 | 19/98 | +0.029 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.281 | 0.380 | 40/64 | +0.063 | STANDARD |
| Jonathan Castagna: 1+ goals | 0.149 | 0.060 | 10/98 | +0.043 | PRIOR_HEAVY |

**MIN @ SEA** · priced 154/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.27 (sd 6.92), pull risk 0.059
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.36, exp saves 23.53 (sd 6.49), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.259 | 0.380 | 39/63 | +0.094 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.375 | 0.465 | 47/54 | +0.067 | STANDARD |
| Matt Boldy: 2+ points | 0.243 | 0.330 | 35/69 | +0.052 | STANDARD |
| Quinn Hughes: 2+ points | 0.234 | 0.320 | 36/72 | +0.031 | STANDARD |
| Matt Boldy: 1+ assists | 0.397 | 0.480 | 49/53 | +0.055 | STANDARD |
| Quinn Hughes: 1+ assists | 0.543 | 0.625 | 65/40 | +0.040 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
