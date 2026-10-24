# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T17:05:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 11 · markets on board: 4592 · contracts joined: 2480 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2205, 'NO_EDGE': 113, 'OK': 162}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 350, 'game_early_goal': 11, 'first_goal': 403, 'game_winner': 22, 'player_goals': 690, 'game_overtime': 11, 'player_points': 464, 'game_spread': 44, 'team_total': 110, 'game_total': 99, 'goalie_saves': 12}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NJD | 2026-10-24T19:30:00Z | T-90m | 0.614 | 0.386 | 0.176 | 5.87 | 3.29 | 2.58 | 214 (25/189) | PROJECTED/PROJECTED |
| SJS @ BOS | 2026-10-24T23:00:00Z | T-3h | 0.651 | 0.349 | 0.163 | 6.17 | 3.56 | 2.61 | 242 (25/217) | CONFIRMED/CONFIRMED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-3h | 0.471 | 0.529 | 0.179 | 6.09 | 2.95 | 3.14 | 230 (25/205) | CONFIRMED/CONFIRMED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-3h | 0.572 | 0.428 | 0.168 | 6.74 | 3.61 | 3.13 | 212 (25/187) | PROBABLE/CONFIRMED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-3h | 0.496 | 0.504 | 0.176 | 6.61 | 3.28 | 3.33 | 236 (25/211) | CONFIRMED/CONFIRMED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-3h | 0.416 | 0.584 | 0.168 | 6.46 | 2.96 | 3.50 | 227 (25/202) | CONFIRMED/PROBABLE |
| CAR @ STL | 2026-10-24T23:00:00Z | T-3h | 0.510 | 0.490 | 0.178 | 6.14 | 3.10 | 3.04 | 217 (25/192) | CONFIRMED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-3h | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 234 (25/209) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-6h | 0.559 | 0.441 | 0.176 | 6.08 | 3.21 | 2.87 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-6h | 0.536 | 0.464 | 0.185 | 5.64 | 2.93 | 2.71 | 230 (25/205) | CONFIRMED/PROJECTED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-6h | 0.518 | 0.482 | 0.182 | 6.11 | 3.11 | 3.00 | 213 (25/188) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.294 | 0.425 | 0.397 | 44 | 59 | no | +0.099 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.518 | 0.640 | 0.616 | 65 | 37 | no | +0.096 | OK |
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.518 | 0.405 | 0.427 | 41 | 60 | yes | +0.091 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.482 | 0.585 | 0.565 | 59 | 42 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.268 | 0.365 | 0.344 | 37 | 64 | no | +0.076 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.429 | 0.525 | 0.506 | 53 | 48 | no | +0.073 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.490 | 0.585 | 0.566 | 59 | 42 | no | +0.073 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.510 | 0.415 | 0.434 | 42 | 59 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.243 | 0.335 | 0.315 | 34 | 67 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.156 | 0.245 | 0.225 | 25 | 76 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.462 | 0.555 | 0.536 | 56 | 45 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.273 | 0.365 | 0.346 | 37 | 64 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.363 | 0.460 | 0.440 | 47 | 55 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.139 | 0.235 | 0.213 | 25 | 78 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.699 | 0.785 | 0.769 | 79 | 22 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.751 | 0.835 | 0.820 | 84 | 17 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.132 | 0.215 | 0.196 | 22 | 79 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.162 | 0.245 | 0.226 | 25 | 76 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.297 | 0.215 | 0.230 | 22 | 79 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.541 | 0.630 | 0.613 | 64 | 38 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.351 | 0.435 | 0.418 | 44 | 57 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.185 | 0.270 | 0.251 | 28 | 74 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.749 | 0.840 | 0.824 | 86 | 18 | no | +0.060 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.464 | 0.545 | 0.529 | 55 | 46 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.587 | 0.675 | 0.658 | 69 | 34 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.293 | 0.220 | 0.233 | 23 | 79 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.373 | 0.445 | 0.430 | 45 | 56 | no | +0.050 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.536 | 0.465 | 0.479 | 47 | 54 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.589 | 0.665 | 0.650 | 68 | 35 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.185 | 0.245 | 0.232 | 25 | 76 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.224 | 0.290 | 0.276 | 30 | 72 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.841 | 0.900 | 0.890 | 91 | 11 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.799 | 0.860 | 0.849 | 87 | 15 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.799 | 0.865 | 0.854 | 88 | 15 | no | +0.042 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.148 | 0.205 | 0.192 | 21 | 80 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY2 | game_spread | 0.304 | 0.245 | 0.256 | 25 | 76 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.353 | 0.415 | 0.402 | 42 | 59 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.245 | 0.310 | 0.296 | 32 | 70 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.335 | 0.395 | 0.383 | 40 | 61 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.170 | 0.225 | 0.213 | 23 | 78 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.311 | 0.255 | 0.266 | 26 | 75 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.392 | 0.330 | 0.342 | 34 | 68 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-8 | game_total | 0.299 | 0.245 | 0.255 | 25 | 76 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.260 | 0.315 | 0.303 | 32 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.785 | 0.835 | 0.826 | 84 | 17 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.337 | 0.285 | 0.295 | 29 | 72 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.571 | 0.630 | 0.618 | 64 | 38 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.410 | 0.465 | 0.454 | 47 | 54 | no | +0.032 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.471 | 0.525 | 0.514 | 53 | 48 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-BOS4 | team_total | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.197 | 0.255 | 0.243 | 27 | 76 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT4 | team_total | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.607 | 0.550 | 0.562 | 56 | 46 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT24SJBOS-7 | game_total | 0.443 | 0.495 | 0.485 | 50 | 51 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.178 | 0.135 | 0.143 | 14 | 87 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.250 | 0.200 | 0.209 | 21 | 81 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-5 | game_total | 0.771 | 0.820 | 0.811 | 83 | 19 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT6 | team_total | 0.155 | 0.105 | 0.114 | 12 | 91 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT24LANJ-5 | game_total | 0.730 | 0.775 | 0.766 | 78 | 23 | no | +0.027 | OK |
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
| KXNHLSPREAD-26OCT24BUFWSH-WSH3 | game_spread | 0.169 | 0.205 | 0.197 | 21 | 80 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.055 | 0.095 | 0.085 | 11 | 92 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-SJ4 | team_total | 0.276 | 0.320 | 0.311 | 33 | 69 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.178 | 0.145 | 0.151 | 15 | 86 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK6 | team_total | 0.136 | 0.095 | 0.102 | 11 | 92 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5 | team_total | 0.209 | 0.165 | 0.173 | 18 | 85 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB2 | team_total | 0.770 | 0.815 | 0.807 | 83 | 20 | no | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NJD | 0.614 | 0.551 | 0.176 | 0.218 | 5.87 | 5.80 | 0.973/0.992 | KXNHLGAME-26OCT24LANJ-LA +0.064 |
| SJS @ BOS | 0.651 | 0.603 | 0.163 | 0.215 | 6.17 | 6.50 | 0.955/1.021 | KXNHLTEAMTOTAL-26OCT24SJBOS-SJ3 +0.079 |
| NYR @ OTT | 0.471 | 0.544 | 0.179 | 0.219 | 6.09 | 6.21 | 1.039/0.988 | KXNHLGAME-26OCT24NYROTT-NYR -0.073 |
| NSH @ PIT | 0.572 | 0.582 | 0.168 | 0.208 | 6.74 | 6.60 | 1.038/1.004 | KXNHLTOTAL-26OCT24NSHPIT-8 -0.025 |
| BUF @ WSH | 0.496 | 0.534 | 0.176 | 0.218 | 6.61 | 6.51 | 1.015/1.002 | KXNHLGAME-26OCT24BUFWSH-BUF -0.038 |
| VGK @ CBJ | 0.416 | 0.469 | 0.168 | 0.223 | 6.46 | 6.14 | 1.007/1.003 | KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 -0.079 |
| CAR @ STL | 0.510 | 0.525 | 0.178 | 0.219 | 6.14 | 6.46 | 0.976/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.058 |
| TOR @ EDM | 0.637 | 0.641 | 0.151 | 0.201 | 7.24 | 6.92 | 1.022/0.965 | KXNHLTOTAL-26OCT24TOREDM-8 -0.054 |
| TBL @ UTA | 0.559 | 0.572 | 0.176 | 0.215 | 6.08 | 6.35 | 0.992/0.973 | KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 +0.049 |
| DET @ CGY | 0.536 | 0.499 | 0.185 | 0.224 | 5.64 | 6.02 | 0.978/1.003 | KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 +0.071 |
| MIN @ SEA | 0.518 | 0.514 | 0.182 | 0.223 | 6.11 | 6.34 | 1.015/0.995 | KXNHLTOTAL-26OCT24MINSEA-7 +0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 39 recommended · full analysis in card.md / packet.json `thesis_card`

- Joel Edmundson: 1+ goals YES @ 3c · p 0.0583 (adj 0.0487) · $1.5 · thesis LAK:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 63c · p 0.7006 (adj 0.6804) · $6.8 · thesis NJD:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 62c · p 0.7903 (adj 0.6666) · $6.8 · thesis NJD:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2781 (adj 0.2648) · $3.2 · thesis LAK:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 27c · p 0.3166 (adj 0.3037) · $3.07 · thesis BOS:OFFENSE_4PLUS
- Tanner Jeannot: 1+ goals YES @ 9c · p 0.116 (adj 0.1082) · $1.44 · thesis BOS:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 11c · p 0.1382 (adj 0.1299) · $1.55 · thesis BOS:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 60c · p 0.6415 (adj 0.6299) · $3.72 · thesis BOS:SUPPRESSED
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1196 (adj 0.1047) · $2.11 · thesis NYR:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1084 (adj 0.0963) · $1.25 · thesis OTT:OFFENSE_4PLUS
- Gabe Perreault: 1+ goals YES @ 22c · p 0.2522 (adj 0.2429) · $1.57 · thesis NYR:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 34c · p 0.4301 (adj 0.4063) · $8.01 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 15c · p 0.2109 (adj 0.1869) · $3.07 · thesis PIT:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 77c · p 0.8751 (adj 0.797) · $8.8 · thesis NSH:SUPPRESSED
- Sidney Crosby: 1+ goals YES @ 34c · p 0.3856 (adj 0.3717) · $2.52 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2405 (adj 0.2191) · $4.88 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ assists NO @ 52c · p 0.608 (adj 0.5615) · $5.82 · thesis BUF:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 25c · p 0.3655 (adj 0.2807) · $2.05 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ goals NO @ 80c · p 0.8339 (adj 0.8242) · $7.78 · thesis BUF:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2599 (adj 0.2474) · $2.41 · thesis CBJ:OFFENSE_4PLUS
- Adam Fantilli: 1+ assists NO @ 62c · p 0.6935 (adj 0.6518) · $5.61 · thesis CBJ:SUPPRESSED
- Trevor Connelly: 1+ goals NO @ 77c · p 0.8028 (adj 0.7933) · $5.77 · thesis VGK:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 22c · p 0.2825 (adj 0.2644) · $4.2 · thesis STL:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 76c · p 0.8342 (adj 0.7946) · $8.97 · thesis STL:WINS
- Justin Barron: 1+ goals YES @ 5c · p 0.0736 (adj 0.064) · $1.03 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1666 (adj 0.1537) · $1.71 · thesis STL:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1514 (adj 0.1361) · $2.27 · thesis TOR:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 26c · p 0.3383 (adj 0.2916) · $2.44 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3125 (adj 0.3006) · $2.39 · thesis EDM:OFFENSE_4PLUS
- Auston Matthews: 1+ assists NO @ 57c · p 0.6419 (adj 0.601) · $4.02 · thesis TOR:SUPPRESSED
- Erik Cernak: 1+ goals YES @ 3c · p 0.0461 (adj 0.0421) · $1.05 · thesis TBL:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1528 (adj 0.1296) · $2.44 · thesis CGY:OFFENSE_4PLUS
- Justin Faulk: 1+ goals NO @ 89c · p 0.9187 (adj 0.9103) · $9.07 · thesis DET:SUPPRESSED
- Brennan Othmann: 1+ goals YES @ 10c · p 0.1256 (adj 0.1179) · $1.3 · thesis CGY:OFFENSE_4PLUS
- Detroit wins by over 1.5 goals NO @ 67c · p 0.7302 (adj 0.6976) · $2.46 · thesis CGY:WINS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6248 (adj 0.6024) · $9.07 · thesis MIN:SUPPRESSED
- Shane Wright: 1+ goals YES @ 15c · p 0.1965 (adj 0.1799) · $2.66 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 15c · p 0.1944 (adj 0.1795) · $2.5 · thesis SEA:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ goals YES @ 18c · p 0.2258 (adj 0.2106) · $2.68 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NJD** · priced 158/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.53, exp saves 23.16 (sd 6.22), pull risk 0.045
- LAK net: Darcy Kuemper (PROJECTED) exp shots 30.31, exp saves 26.11 (sd 7.0), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.210 | 0.400 | 42/62 | +0.154 | STANDARD |
| Luke Evangelista: 1+ points | 0.371 | 0.535 | 55/48 | +0.132 | STANDARD |
| Jack Hughes: 2+ points | 0.215 | 0.340 | 35/67 | +0.099 | STANDARD |
| Jack Hughes: 1+ assists | 0.400 | 0.520 | 54/50 | +0.082 | STANDARD |
| Luke Evangelista: 2+ points | 0.079 | 0.180 | 20/84 | +0.072 | STANDARD |
| Alex Laferriere: 2+ points | 0.183 | 0.090 | 16/98 | +0.013 | STANDARD |

**SJS @ BOS** · priced 190/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.44, exp saves 24.01 (sd 6.53), pull risk 0.055
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.84, exp saves 23.62 (sd 6.72), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jeremy Swayman: 24+ saves | 0.526 | 0.400 | 50/70 | +0.009 |  |
| Macklin Celebrini: 1+ assists | 0.409 | 0.515 | 53/50 | +0.073 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.420 | 0.500 | 51/51 | +0.052 | STANDARD |
| David Pastrnak: 2+ points | 0.327 | 0.405 | 42/61 | +0.047 | STANDARD |
| JJ Peterka: 1+ assists | 0.262 | 0.340 | 35/67 | +0.052 | STANDARD |
| Mason Marchment: 1+ goals | 0.242 | 0.165 | 21/88 | +0.021 | STANDARD |

**NYR @ OTT** · priced 173/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Jonas Johansson (CONFIRMED) exp shots 23.91, exp saves 20.9 (sd 5.92), pull risk 0.054
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.38, exp saves 25.27 (sd 6.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.372 | 0.505 | 53/52 | +0.091 | STANDARD |
| Jake Sanderson: 1+ assists | 0.287 | 0.420 | 44/60 | +0.096 | STANDARD |
| Jonas Johansson: 22+ saves | 0.447 | 0.315 | 45/82 | -0.020 |  |
| Vladislav Gavrikov: 1+ assists | 0.338 | 0.230 | 25/79 | +0.075 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.392 | 0.290 | 31/73 | +0.067 | STANDARD |
| Jordan Spence: 1+ points | 0.345 | 0.250 | 26/76 | +0.071 | STANDARD |

**NSH @ PIT** · priced 152/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 26.07, exp saves 22.79 (sd 6.25), pull risk 0.059
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.45, exp saves 24.98 (sd 6.96), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 23+ saves | 0.515 | 0.285 | 50/93 | -0.002 |  |
| Mavrik Bourque: 1+ assists | 0.125 | 0.245 | 26/77 | +0.093 | STANDARD |
| Thomas Novak: 2+ points | 0.214 | 0.105 | 19/98 | +0.013 | STANDARD |
| Connor Dewar: 1+ goals | 0.211 | 0.115 | 15/92 | +0.052 | STANDARD |
| Rickard Rakell: 1+ goals | 0.430 | 0.335 | 34/67 | +0.074 | STANDARD |
| Rickard Rakell: 1+ points | 0.659 | 0.565 | 59/46 | +0.052 | STANDARD |

**BUF @ WSH** · priced 181/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.16, exp saves 24.43 (sd 6.67), pull risk 0.06
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 26.97, exp saves 23.14 (sd 6.53), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 27+ saves | 0.293 | 0.430 | 50/64 | +0.050 |  |
| Ryan Leonard: 1+ assists | 0.365 | 0.235 | 25/78 | +0.102 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.392 | 0.485 | 49/52 | +0.071 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.240 | 0.155 | 17/86 | +0.061 | STANDARD |
| Aliaksei Protas: 1+ points | 0.451 | 0.370 | 38/64 | +0.055 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.275 | 0.355 | 37/66 | +0.049 | STANDARD |

**VGK @ CBJ** · priced 163/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.34, exp saves 23.55 (sd 6.41), pull risk 0.066
- VGK net: Carter Hart (PROBABLE) exp shots 27.42, exp saves 23.74 (sd 6.42), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.450 | 0.580 | 59/43 | +0.103 | STANDARD |
| Cam Talbot: 27+ saves | 0.315 | 0.435 | 46/59 | +0.078 |  |
| Jack Eichel: 2+ points | 0.246 | 0.365 | 38/65 | +0.088 | STANDARD |
| Carter Hart: 24+ saves | 0.509 | 0.410 | 51/69 | -0.018 |  |
| Zach Werenski: 1+ assists | 0.460 | 0.555 | 57/46 | +0.063 | STANDARD |
| Adam Fantilli: 1+ assists | 0.306 | 0.390 | 40/62 | +0.057 | STANDARD |

**CAR @ STL** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 30.19, exp saves 26.11 (sd 7.15), pull risk 0.065
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.37 (sd 5.89), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.362 | 0.485 | 49/52 | +0.100 | STANDARD |
| Seth Jarvis: 1+ assists | 0.207 | 0.305 | 33/72 | +0.058 | STANDARD |
| Philip Broberg: 1+ points | 0.482 | 0.385 | 41/64 | +0.055 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.419 | 0.515 | 53/50 | +0.064 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.347 | 0.440 | 45/57 | +0.065 | STANDARD |
| Seth Jarvis: 1+ points | 0.404 | 0.495 | 52/53 | +0.049 | STANDARD |

**TOR @ EDM** · priced 175/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.420 | 44/60 | +0.081 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.514 | 0.625 | 64/39 | +0.079 | STANDARD |
| Leon Draisaitl: 2+ points | 0.372 | 0.480 | 50/54 | +0.071 | STANDARD |
| Gavin McKenna: 1+ points | 0.350 | 0.455 | 47/56 | +0.073 | STANDARD |
| Connor McDavid: 2+ points | 0.471 | 0.575 | 59/44 | +0.072 | STANDARD |
| Connor McDavid: 2+ assists | 0.259 | 0.360 | 38/66 | +0.065 | STANDARD |

**TBL @ UTA** · priced 164/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.3 (sd 6.37), pull risk 0.052
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.6, exp saves 22.78 (sd 6.46), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.220 | 0.335 | 36/69 | +0.075 | STANDARD |
| Lawson Crouse: 1+ goals | 0.227 | 0.120 | 20/96 | +0.016 | STANDARD |
| Clayton Keller: 1+ assists | 0.449 | 0.540 | 56/48 | +0.053 | STANDARD |
| Clayton Keller: 2+ points | 0.245 | 0.335 | 36/69 | +0.050 | STANDARD |
| Jack McBain: 1+ goals | 0.154 | 0.070 | 12/98 | +0.027 | STANDARD |
| Ilya Mikheyev: 1+ goals | 0.162 | 0.080 | 14/98 | +0.013 | STANDARD |

**DET @ CGY** · priced 172/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 29.78, exp saves 25.87 (sd 6.82), pull risk 0.053
- DET net: Michal Postava (PROJECTED) exp shots 27.65, exp saves 23.9 (sd 6.55), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Bahl: 1+ points | 0.301 | 0.145 | 26/97 | +0.028 | STANDARD |
| Zach Whitecloud: 1+ points | 0.277 | 0.135 | 22/95 | +0.045 | STANDARD |
| Aydar Suniev: 1+ goals | 0.234 | 0.100 | 18/98 | +0.044 | STANDARD |
| Ben Jones: 1+ points | 0.200 | 0.325 | 37/72 | +0.066 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.278 | 0.375 | 40/65 | +0.056 | STANDARD |
| Jonathan Castagna: 1+ goals | 0.153 | 0.060 | 10/98 | +0.046 | PRIOR_HEAVY |

**MIN @ SEA** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.27 (sd 6.92), pull risk 0.059
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.36, exp saves 23.53 (sd 6.49), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.259 | 0.380 | 39/63 | +0.094 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.625 | 0.720 | 74/30 | +0.061 | STANDARD |
| Quinn Hughes: 1+ assists | 0.543 | 0.635 | 65/38 | +0.060 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.375 | 0.465 | 47/54 | +0.067 | STANDARD |
| Matt Boldy: 2+ points | 0.243 | 0.330 | 35/69 | +0.052 | STANDARD |
| Quinn Hughes: 2+ points | 0.234 | 0.320 | 36/72 | +0.031 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
