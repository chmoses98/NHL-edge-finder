# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T21:05:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 10 · markets on board: 4501 · contracts joined: 2418 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2168, 'NO_EDGE': 91, 'OK': 159}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 382, 'game_early_goal': 10, 'first_goal': 369, 'game_winner': 20, 'player_goals': 629, 'game_overtime': 10, 'player_points': 512, 'goalie_saves': 16, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ BOS | 2026-10-24T23:00:00Z | T-90m | 0.649 | 0.350 | 0.167 | 6.18 | 3.56 | 2.61 | 260 (25/235) | CONFIRMED/CONFIRMED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-90m | 0.468 | 0.532 | 0.176 | 6.09 | 2.94 | 3.14 | 232 (25/207) | CONFIRMED/CONFIRMED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-90m | 0.571 | 0.429 | 0.169 | 6.74 | 3.61 | 3.13 | 232 (25/207) | PROBABLE/CONFIRMED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-90m | 0.490 | 0.510 | 0.176 | 6.61 | 3.28 | 3.33 | 262 (25/237) | CONFIRMED/CONFIRMED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-90m | 0.411 | 0.589 | 0.172 | 6.46 | 2.96 | 3.50 | 244 (25/219) | CONFIRMED/PROBABLE |
| CAR @ STL | 2026-10-24T23:00:00Z | T-90m | 0.512 | 0.488 | 0.184 | 6.15 | 3.11 | 3.04 | 227 (25/202) | CONFIRMED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-90m | 0.649 | 0.351 | 0.150 | 7.29 | 4.16 | 3.13 | 261 (25/236) | CONFIRMED/CONFIRMED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-3h | 0.554 | 0.446 | 0.176 | 6.08 | 3.21 | 2.87 | 235 (25/210) | PROBABLE/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-3h | 0.517 | 0.483 | 0.189 | 5.54 | 2.82 | 2.72 | 234 (25/209) | CONFIRMED/CONFIRMED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-3h | 0.469 | 0.531 | 0.174 | 6.26 | 3.04 | 3.22 | 231 (25/206) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.296 | 0.425 | 0.398 | 43 | 58 | no | +0.107 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.447 | 0.555 | 0.534 | 56 | 45 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.520 | 0.630 | 0.609 | 64 | 38 | no | +0.084 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.686 | 0.785 | 0.767 | 79 | 22 | no | +0.082 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.488 | 0.585 | 0.566 | 59 | 42 | no | +0.075 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.512 | 0.415 | 0.434 | 42 | 59 | yes | +0.075 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.531 | 0.625 | 0.607 | 63 | 38 | no | +0.073 | OK |
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.469 | 0.375 | 0.393 | 38 | 63 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.341 | 0.435 | 0.416 | 44 | 57 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.139 | 0.230 | 0.209 | 24 | 78 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.161 | 0.245 | 0.226 | 25 | 76 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.428 | 0.515 | 0.498 | 52 | 49 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.542 | 0.630 | 0.613 | 64 | 38 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.139 | 0.215 | 0.198 | 22 | 79 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.752 | 0.835 | 0.820 | 85 | 18 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.277 | 0.360 | 0.342 | 37 | 65 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.786 | 0.855 | 0.843 | 86 | 15 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.589 | 0.670 | 0.654 | 68 | 34 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.173 | 0.245 | 0.229 | 25 | 76 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.757 | 0.830 | 0.817 | 84 | 18 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.311 | 0.385 | 0.370 | 39 | 62 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.294 | 0.225 | 0.238 | 23 | 78 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.190 | 0.260 | 0.245 | 27 | 75 | no | +0.047 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.468 | 0.535 | 0.522 | 54 | 47 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.223 | 0.290 | 0.276 | 30 | 72 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.264 | 0.205 | 0.216 | 21 | 80 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.243 | 0.310 | 0.296 | 32 | 70 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.842 | 0.895 | 0.886 | 90 | 11 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.412 | 0.480 | 0.466 | 49 | 53 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.800 | 0.860 | 0.849 | 87 | 15 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.167 | 0.225 | 0.212 | 23 | 78 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.372 | 0.435 | 0.422 | 44 | 57 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.198 | 0.260 | 0.247 | 27 | 75 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.312 | 0.255 | 0.266 | 26 | 75 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.150 | 0.205 | 0.193 | 21 | 80 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.114 | 0.170 | 0.157 | 18 | 84 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.785 | 0.835 | 0.826 | 84 | 17 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.570 | 0.630 | 0.618 | 64 | 38 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.590 | 0.530 | 0.542 | 54 | 48 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.411 | 0.465 | 0.454 | 47 | 54 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL4 | team_total | 0.386 | 0.330 | 0.341 | 34 | 68 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT24SJBOS-7 | game_total | 0.442 | 0.495 | 0.484 | 50 | 51 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.054 | 0.100 | 0.089 | 11 | 91 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT5 | team_total | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.375 | 0.315 | 0.327 | 33 | 70 | yes | +0.030 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.354 | 0.410 | 0.399 | 42 | 60 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR3 | team_total | 0.616 | 0.565 | 0.575 | 57 | 44 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT24SJBOS-5 | game_total | 0.770 | 0.820 | 0.811 | 83 | 19 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT3 | team_total | 0.704 | 0.650 | 0.661 | 66 | 36 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT24TOREDM-EDM2 | game_spread | 0.445 | 0.395 | 0.405 | 40 | 61 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.176 | 0.135 | 0.142 | 14 | 87 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT5 | team_total | 0.301 | 0.250 | 0.260 | 26 | 76 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT24NSHPIT-PIT2 | game_spread | 0.362 | 0.315 | 0.324 | 32 | 69 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.186 | 0.145 | 0.152 | 15 | 86 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-8 | game_total | 0.300 | 0.250 | 0.260 | 26 | 76 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.248 | 0.200 | 0.209 | 21 | 81 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-9 | game_total | 0.217 | 0.175 | 0.183 | 18 | 83 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT24SJBOS-6 | game_total | 0.557 | 0.605 | 0.596 | 61 | 40 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT24NSHPIT-PIT4 | team_total | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA2 | team_total | 0.826 | 0.865 | 0.858 | 87 | 14 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.629 | 0.680 | 0.670 | 69 | 33 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.202 | 0.245 | 0.236 | 25 | 76 | no | +0.025 | OK |
| KXNHLGAME-26OCT24NSHPIT-PIT | game_winner | 0.571 | 0.525 | 0.534 | 53 | 48 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.337 | 0.295 | 0.303 | 30 | 71 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK3 | team_total | 0.688 | 0.640 | 0.650 | 65 | 37 | yes | +0.023 | OK |
| KXNHLGAME-26OCT24TOREDM-EDM | game_winner | 0.649 | 0.605 | 0.614 | 61 | 40 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.829 | 0.865 | 0.858 | 87 | 14 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24SJBOS-BOS4 | team_total | 0.490 | 0.535 | 0.526 | 54 | 47 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT24DETCGY-10 | game_total | 0.044 | 0.080 | 0.071 | 9 | 93 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT24NSHPIT-NSH2 | game_spread | 0.235 | 0.275 | 0.267 | 28 | 73 | no | +0.021 | OK |
| KXNHLGAME-26OCT24VGKCBJ-CBJ | game_winner | 0.411 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLGAME-26OCT24VGKCBJ-VGK | game_winner | 0.589 | 0.545 | 0.554 | 55 | 46 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5 | team_total | 0.201 | 0.155 | 0.163 | 17 | 86 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.226 | 0.270 | 0.261 | 28 | 74 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA6 | team_total | 0.102 | 0.140 | 0.131 | 15 | 87 | no | +0.020 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ BOS | 0.649 | 0.603 | 0.167 | 0.215 | 6.18 | 6.50 | 0.955/1.021 | KXNHLTEAMTOTAL-26OCT24SJBOS-SJ3 +0.076 |
| NYR @ OTT | 0.468 | 0.544 | 0.176 | 0.219 | 6.09 | 6.21 | 1.039/0.988 | KXNHLGAME-26OCT24NYROTT-NYR -0.076 |
| NSH @ PIT | 0.571 | 0.582 | 0.169 | 0.208 | 6.74 | 6.60 | 1.038/1.004 | KXNHLTOTAL-26OCT24NSHPIT-8 -0.025 |
| BUF @ WSH | 0.490 | 0.536 | 0.176 | 0.215 | 6.61 | 6.51 | 1.015/1.002 | KXNHLGAME-26OCT24BUFWSH-BUF -0.046 |
| VGK @ CBJ | 0.411 | 0.469 | 0.172 | 0.223 | 6.46 | 6.14 | 1.007/1.003 | KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 -0.078 |
| CAR @ STL | 0.512 | 0.525 | 0.184 | 0.219 | 6.15 | 6.46 | 0.976/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.055 |
| TOR @ EDM | 0.649 | 0.635 | 0.150 | 0.201 | 7.29 | 6.89 | 1.022/0.955 | KXNHLTOTAL-26OCT24TOREDM-8 -0.067 |
| TBL @ UTA | 0.554 | 0.577 | 0.176 | 0.216 | 6.08 | 6.34 | 0.990/0.973 | KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 +0.051 |
| DET @ CGY | 0.517 | 0.498 | 0.189 | 0.226 | 5.54 | 5.99 | 0.978/0.994 | KXNHLTOTAL-26OCT24DETCGY-7 +0.079 |
| MIN @ SEA | 0.469 | 0.522 | 0.174 | 0.216 | 6.26 | 6.29 | 1.001/0.991 | KXNHLGAME-26OCT24MINSEA-SEA +0.052 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Tanner Jeannot: 1+ goals YES @ 9c · p 0.116 (adj 0.1082) · $1.59 · thesis BOS:OFFENSE_4PLUS
- James Hagens: 1+ goals NO @ 78c · p 0.8149 (adj 0.8049) · $7.91 · thesis BOS:SUPPRESSED
- David Pastrnak: 1+ goals NO @ 60c · p 0.6415 (adj 0.6299) · $4.23 · thesis BOS:SUPPRESSED
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1196 (adj 0.106) · $2.32 · thesis NYR:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 57c · p 0.7129 (adj 0.6168) · $9.96 · thesis OTT:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 25c · p 0.3384 (adj 0.2892) · $3.6 · thesis NYR:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1084 (adj 0.0963) · $1.46 · thesis OTT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 34c · p 0.4125 (adj 0.3931) · $6.95 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 15c · p 0.2047 (adj 0.186) · $3.59 · thesis PIT:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 75c · p 0.8707 (adj 0.789) · $9.96 · thesis NSH:SUPPRESSED
- Sidney Crosby: 1+ goals YES @ 34c · p 0.3788 (adj 0.3666) · $1.91 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2405 (adj 0.2216) · $5.83 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 25c · p 0.3655 (adj 0.2872) · $3.31 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ assists NO @ 52c · p 0.608 (adj 0.5615) · $6.37 · thesis BUF:SUPPRESSED
- Jordan Kyrou: 1+ assists NO @ 65c · p 0.7247 (adj 0.6824) · $7.54 · thesis WSH:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2599 (adj 0.2487) · $2.63 · thesis CBJ:OFFENSE_4PLUS
- Cam Talbot: 27+ saves NO @ 54c · p 0.6849 (adj 0.5687) · $3.64 · thesis CBJ:NET_LOW_VOLUME
- Robert Thomas: 1+ goals YES @ 22c · p 0.2825 (adj 0.2606) · $4.31 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1666 (adj 0.155) · $2.24 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3311 (adj 0.3158) · $3.57 · thesis STL:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7287 (adj 0.7153) · $8.45 · thesis CAR:SUPPRESSED
- Leon Draisaitl: 2+ assists NO @ 75c · p 0.8367 (adj 0.7883) · $9.96 · thesis EDM:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1494 (adj 0.1358) · $2.43 · thesis TOR:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.1987 (adj 0.1878) · $2.61 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3143 (adj 0.302) · $3.77 · thesis EDM:OFFENSE_4PLUS
- Anthony Cirelli: 1+ goals YES @ 18c · p 0.2232 (adj 0.2112) · $3.02 · thesis TBL:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1528 (adj 0.1396) · $1.57 · thesis UTA:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 11c · p 0.1492 (adj 0.1344) · $2.24 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $1.86 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2296 (adj 0.2172) · $2.43 · thesis CGY:OFFENSE_4PLUS
- Lucas Raymond: 1+ goals NO @ 72c · p 0.7583 (adj 0.7475) · $6.15 · thesis DET:SUPPRESSED
- Berkly Catton: 1+ goals YES @ 16c · p 0.2173 (adj 0.1992) · $4.14 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1657 (adj 0.1518) · $3.11 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1453 (adj 0.1277) · $2.55 · thesis SEA:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 17c · p 0.2139 (adj 0.1992) · $2.8 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ BOS** · priced 208/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.44, exp saves 24.01 (sd 6.53), pull risk 0.055
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.84, exp saves 23.62 (sd 6.72), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.270 | 0.115 | 22/99 | +0.038 | STANDARD |
| Matthew Poitras: 1+ points | 0.307 | 0.165 | 31/98 | -0.018 | STANDARD |
| Michael Kesselring: 1+ points | 0.240 | 0.115 | 21/98 | +0.018 | STANDARD |
| Sam Dickinson: 1+ assists | 0.221 | 0.105 | 20/99 | +0.010 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.409 | 0.525 | 54/49 | +0.083 | STANDARD |
| Michael Kesselring: 1+ assists | 0.195 | 0.090 | 17/99 | +0.015 | STANDARD |

**NYR @ OTT** · priced 175/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Jonas Johansson (CONFIRMED) exp shots 23.91, exp saves 20.9 (sd 5.92), pull risk 0.054
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.38, exp saves 25.27 (sd 6.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.287 | 0.435 | 44/57 | +0.126 | STANDARD |
| Jake Sanderson: 1+ points | 0.372 | 0.515 | 53/50 | +0.111 | STANDARD |
| Artem Zub: 1+ assists | 0.255 | 0.130 | 24/98 | +0.003 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.338 | 0.240 | 25/77 | +0.075 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.392 | 0.295 | 31/72 | +0.067 | STANDARD |
| Tim Stutzle: 1+ assists | 0.396 | 0.490 | 50/52 | +0.066 | STANDARD |

**NSH @ PIT** · priced 172/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 26.07, exp saves 22.79 (sd 6.24), pull risk 0.059
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.45, exp saves 24.98 (sd 6.96), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ assists | 0.293 | 0.120 | 22/98 | +0.061 | STANDARD |
| Rickard Rakell: 2+ points | 0.277 | 0.145 | 22/93 | +0.045 | STANDARD |
| Adam Wilsby: 1+ points | 0.343 | 0.215 | 27/84 | +0.059 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.129 | 0.255 | 26/75 | +0.108 | STANDARD |
| Thomas Novak: 2+ points | 0.197 | 0.100 | 19/99 | -0.004 | STANDARD |
| Rickard Rakell: 1+ points | 0.652 | 0.570 | 59/45 | +0.045 | STANDARD |

**BUF @ WSH** · priced 204/211 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.16, exp saves 24.43 (sd 6.67), pull risk 0.06
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 26.97, exp saves 23.14 (sd 6.53), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Timothy Liljegren: 1+ points | 0.230 | 0.095 | 18/99 | +0.040 | STANDARD |
| Anthony Beauvillier: 1+ assists | 0.212 | 0.085 | 16/99 | +0.043 | STANDARD |
| Ryan Leonard: 1+ assists | 0.365 | 0.245 | 25/76 | +0.102 | STANDARD |
| Timothy Liljegren: 1+ assists | 0.192 | 0.080 | 15/99 | +0.033 | STANDARD |
| Anthony Beauvillier: 1+ points | 0.331 | 0.220 | 26/82 | +0.058 | STANDARD |
| Beck Malenstyn: 1+ points | 0.195 | 0.090 | 17/99 | +0.015 | STANDARD |

**VGK @ CBJ** · priced 180/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.34, exp saves 23.55 (sd 6.41), pull risk 0.066
- VGK net: Carter Hart (PROBABLE) exp shots 27.42, exp saves 23.74 (sd 6.42), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cam Talbot: 27+ saves | 0.315 | 0.470 | 48/54 | +0.128 |  |
| Jack Eichel: 2+ points | 0.246 | 0.375 | 39/64 | +0.097 | STANDARD |
| Jack Eichel: 1+ assists | 0.450 | 0.570 | 59/45 | +0.083 | STANDARD |
| Brayden McNabb: 1+ assists | 0.276 | 0.160 | 29/97 | -0.028 | STANDARD |
| Jack Eichel: 2+ assists | 0.122 | 0.220 | 23/79 | +0.077 | STANDARD |
| Zach Werenski: 1+ assists | 0.460 | 0.555 | 57/46 | +0.063 | STANDARD |

**CAR @ STL** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 30.19, exp saves 26.11 (sd 7.15), pull risk 0.065
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.37 (sd 5.89), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.362 | 0.485 | 49/52 | +0.100 | STANDARD |
| Jalen Chatfield: 1+ assists | 0.222 | 0.115 | 21/98 | -0.000 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.347 | 0.450 | 47/57 | +0.065 | STANDARD |
| Seth Jarvis: 1+ assists | 0.207 | 0.310 | 34/72 | +0.058 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.419 | 0.520 | 53/49 | +0.074 | STANDARD |
| Philip Broberg: 1+ points | 0.482 | 0.385 | 41/64 | +0.055 | STANDARD |

**TOR @ EDM** · priced 202/210 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.28 (sd 6.43), pull risk 0.058
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 32.17, exp saves 27.04 (sd 7.6), pull risk 0.102

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Michaels: 1+ points | 0.275 | 0.125 | 23/98 | +0.033 | STANDARD |
| Troy Stecher: 1+ assists | 0.216 | 0.080 | 15/99 | +0.057 | STANDARD |
| Jake McCabe: 1+ assists | 0.246 | 0.115 | 21/98 | +0.025 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.338 | 0.210 | 23/81 | +0.096 | STANDARD |
| Leon Draisaitl: 2+ points | 0.368 | 0.490 | 51/53 | +0.084 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.304 | 0.425 | 44/59 | +0.089 | STANDARD |

**TBL @ UTA** · priced 174/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 26.79, exp saves 23.31 (sd 6.33), pull risk 0.051
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.6, exp saves 22.78 (sd 6.44), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.222 | 0.340 | 36/68 | +0.083 | STANDARD |
| Brayden Point: 2+ points | 0.205 | 0.115 | 21/98 | -0.016 | STANDARD |
| Jake Guentzel: 2+ points | 0.235 | 0.145 | 26/97 | -0.039 | STANDARD |
| Clayton Keller: 2+ points | 0.239 | 0.325 | 34/69 | +0.056 | STANDARD |
| Clayton Keller: 1+ assists | 0.460 | 0.545 | 56/47 | +0.053 | STANDARD |
| Lawson Crouse: 1+ points | 0.420 | 0.335 | 36/69 | +0.044 | STANDARD |

**DET @ CGY** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 29.78, exp saves 25.85 (sd 6.81), pull risk 0.053
- DET net: John Gibson (CONFIRMED) exp shots 27.65, exp saves 23.91 (sd 6.55), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ points | 0.269 | 0.145 | 22/93 | +0.037 | STANDARD |
| Aydar Suniev: 1+ assists | 0.237 | 0.130 | 24/98 | -0.015 | STANDARD |
| Ben Jones: 1+ points | 0.199 | 0.305 | 33/72 | +0.066 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.281 | 0.375 | 39/64 | +0.063 | STANDARD |
| Dylan Larkin: 1+ assists | 0.326 | 0.405 | 43/62 | +0.038 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.235 | 0.160 | 18/86 | +0.044 | STANDARD |

**MIN @ SEA** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 30.26, exp saves 26.22 (sd 7.0), pull risk 0.06
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.36, exp saves 23.54 (sd 6.46), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kaapo Kakko: 1+ points | 0.498 | 0.270 | 45/91 | +0.031 | STANDARD |
| Ryker Evans: 1+ points | 0.323 | 0.145 | 27/98 | +0.039 | STANDARD |
| Adam Larsson: 1+ assists | 0.281 | 0.110 | 20/98 | +0.070 | STANDARD |
| Ryker Evans: 1+ assists | 0.274 | 0.120 | 22/98 | +0.042 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.255 | 0.390 | 40/62 | +0.108 | STANDARD |
| Adam Larsson: 1+ points | 0.334 | 0.210 | 24/82 | +0.081 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
