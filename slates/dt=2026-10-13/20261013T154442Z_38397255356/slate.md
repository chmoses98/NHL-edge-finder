# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T15:44:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 16 · markets on board: 5362 · contracts joined: 3482 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 3082, 'OK': 220, 'NO_EDGE': 180}
families: {'period_winner': 144, 'period_spread': 96, 'period_total': 144, 'player_assists': 463, 'game_early_goal': 16, 'first_goal': 582, 'game_winner': 32, 'player_goals': 999, 'game_overtime': 16, 'player_points': 614, 'goalie_saves': 8, 'game_spread': 64, 'team_total': 160, 'game_total': 144}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 2026-10-13T22:00:00Z | T-6h | 0.558 | 0.442 | 0.188 | 5.64 | 2.99 | 2.65 | 217 (25/192) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-10-13T22:15:00Z | T-6h | 0.572 | 0.428 | 0.176 | 6.22 | 3.34 | 2.88 | 211 (25/186) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-13T22:30:00Z | T-6h | 0.546 | 0.454 | 0.180 | 6.06 | 3.17 | 2.89 | 210 (25/185) | CONFIRMED/PROJECTED |
| WSH @ CAR | 2026-10-13T22:45:00Z | T-6h | 0.594 | 0.406 | 0.166 | 6.12 | 3.35 | 2.77 | 244 (25/219) | PROBABLE/PROJECTED |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-6h | 0.461 | 0.539 | 0.181 | 5.69 | 2.73 | 2.96 | 226 (25/201) | PROBABLE/PROJECTED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-6h | 0.523 | 0.477 | 0.179 | 5.75 | 2.95 | 2.80 | 230 (25/205) | CONFIRMED/PROJECTED |
| STL @ OTT | 2026-10-13T23:30:00Z | T-6h | 0.451 | 0.549 | 0.180 | 6.14 | 2.92 | 3.22 | 225 (25/200) | PROJECTED/PROJECTED |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-6h | 0.652 | 0.348 | 0.163 | 6.24 | 3.61 | 2.62 | 220 (25/195) | CONFIRMED/PROJECTED |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-6h | 0.454 | 0.546 | 0.179 | 6.15 | 2.93 | 3.22 | 219 (25/194) | PROJECTED/PROJECTED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-6h | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 199 (25/174) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-6h | 0.493 | 0.507 | 0.186 | 5.96 | 2.95 | 3.01 | 208 (25/183) | PROJECTED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-6h | 0.532 | 0.468 | 0.169 | 6.47 | 3.34 | 3.13 | 214 (25/189) | PROJECTED/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-6h | 0.664 | 0.336 | 0.158 | 6.76 | 3.93 | 2.83 | 217 (25/192) | PROJECTED/PROJECTED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-6h | 0.603 | 0.397 | 0.175 | 6.03 | 3.34 | 2.70 | 209 (25/184) | PROJECTED/PROJECTED |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-6h | 0.440 | 0.560 | 0.175 | 6.20 | 2.91 | 3.29 | 215 (25/190) | PROJECTED/PROJECTED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-6h | 0.444 | 0.556 | 0.176 | 6.20 | 2.93 | 3.27 | 218 (25/193) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT13TBNYR-NYR | game_winner | 0.523 | 0.395 | 0.420 | 40 | 61 | yes | +0.106 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB3 | team_total | 0.540 | 0.665 | 0.641 | 67 | 34 | no | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB4 | team_total | 0.320 | 0.445 | 0.419 | 45 | 56 | no | +0.103 | OK |
| KXNHLGAME-26OCT13TBNYR-TB | game_winner | 0.477 | 0.595 | 0.572 | 60 | 41 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB2 | game_spread | 0.258 | 0.365 | 0.342 | 37 | 64 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB3 | game_spread | 0.142 | 0.245 | 0.221 | 25 | 76 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB5 | team_total | 0.155 | 0.255 | 0.232 | 26 | 75 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ3 | team_total | 0.499 | 0.595 | 0.576 | 60 | 41 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ4 | team_total | 0.290 | 0.385 | 0.365 | 39 | 62 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.294 | 0.205 | 0.221 | 21 | 80 | yes | +0.072 | OK |
| KXNHLTOTAL-26OCT13NJDET-7 | game_total | 0.356 | 0.445 | 0.427 | 45 | 56 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.765 | 0.850 | 0.835 | 86 | 16 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ5 | team_total | 0.134 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT13NJDET-6 | game_total | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 | team_total | 0.301 | 0.390 | 0.371 | 40 | 62 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.522 | 0.610 | 0.593 | 62 | 40 | no | +0.061 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.664 | 0.585 | 0.601 | 59 | 42 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.712 | 0.785 | 0.772 | 79 | 22 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.452 | 0.375 | 0.390 | 38 | 63 | yes | +0.055 | OK |
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.532 | 0.455 | 0.470 | 46 | 55 | yes | +0.055 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.468 | 0.545 | 0.530 | 55 | 46 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-5 | game_total | 0.704 | 0.775 | 0.762 | 78 | 23 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT13NJDET-5 | game_total | 0.705 | 0.780 | 0.766 | 79 | 23 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ2 | team_total | 0.737 | 0.810 | 0.797 | 82 | 20 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-6 | game_total | 0.471 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 | team_total | 0.401 | 0.475 | 0.460 | 48 | 53 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13NJDET-4 | game_total | 0.801 | 0.865 | 0.854 | 87 | 14 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.412 | 0.485 | 0.470 | 49 | 52 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-7 | game_total | 0.362 | 0.435 | 0.420 | 44 | 57 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT13TBNYR-7 | game_total | 0.373 | 0.445 | 0.430 | 45 | 56 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-4 | game_total | 0.802 | 0.865 | 0.854 | 87 | 14 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI2 | team_total | 0.751 | 0.820 | 0.808 | 83 | 19 | no | +0.048 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.336 | 0.405 | 0.391 | 41 | 60 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.321 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT13TBNYR-6 | game_total | 0.486 | 0.555 | 0.541 | 56 | 45 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.564 | 0.495 | 0.509 | 50 | 51 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT13NJDET-8 | game_total | 0.182 | 0.245 | 0.231 | 25 | 76 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.155 | 0.215 | 0.202 | 22 | 79 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.136 | 0.195 | 0.182 | 20 | 81 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT13STLOTT-STL2 | game_spread | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL3 | team_total | 0.622 | 0.690 | 0.677 | 70 | 32 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI5 | team_total | 0.147 | 0.210 | 0.196 | 22 | 80 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.810 | 0.865 | 0.855 | 87 | 14 | no | +0.042 | OK |
| KXNHLGAME-26OCT13STLOTT-OTT | game_winner | 0.451 | 0.515 | 0.502 | 52 | 49 | no | +0.041 | OK |
| KXNHLGAME-26OCT13STLOTT-STL | game_winner | 0.549 | 0.485 | 0.498 | 49 | 52 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.647 | 0.585 | 0.598 | 59 | 42 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ2 | game_spread | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-6 | game_total | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL5 | team_total | 0.220 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.760 | 0.700 | 0.713 | 71 | 31 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.361 | 0.300 | 0.312 | 31 | 71 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-7 | game_total | 0.427 | 0.485 | 0.473 | 49 | 52 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR3 | game_spread | 0.173 | 0.125 | 0.134 | 13 | 88 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-5 | game_total | 0.753 | 0.810 | 0.800 | 82 | 20 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.766 | 0.815 | 0.806 | 82 | 19 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.203 | 0.155 | 0.164 | 16 | 85 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.439 | 0.495 | 0.484 | 50 | 51 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB6 | team_total | 0.061 | 0.110 | 0.098 | 12 | 90 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.632 | 0.690 | 0.679 | 70 | 32 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.400 | 0.388 | 41 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.167 | 0.215 | 0.205 | 22 | 79 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLGAME-26OCT13SEAPHI-PHI | game_winner | 0.461 | 0.515 | 0.504 | 52 | 49 | no | +0.032 | OK |
| KXNHLGAME-26OCT13SEAPHI-SEA | game_winner | 0.539 | 0.485 | 0.496 | 49 | 52 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL2 | team_total | 0.820 | 0.870 | 0.861 | 88 | 14 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT3 | game_spread | 0.139 | 0.185 | 0.175 | 19 | 82 | no | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-DET | game_winner | 0.558 | 0.505 | 0.516 | 51 | 50 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-NJ | game_winner | 0.442 | 0.495 | 0.484 | 50 | 51 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT13CGYANA-ANA3 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT13NJDET-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL5 | team_total | 0.231 | 0.185 | 0.194 | 19 | 82 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT13TBNYR-8 | game_total | 0.198 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.246 | 0.300 | 0.289 | 31 | 71 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.266 | 0.315 | 0.305 | 32 | 69 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.227 | 0.280 | 0.269 | 29 | 73 | no | +0.029 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 0.558 | 0.545 | 0.188 | 0.224 | 5.64 | 5.77 | 0.994/0.984 | KXNHLTOTAL-26OCT13NJDET-7 +0.027 |
| FLA @ CBJ | 0.572 | 0.609 | 0.176 | 0.214 | 6.22 | 6.07 | 1.008/0.995 | KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3 -0.040 |
| BUF @ MTL | 0.546 | 0.553 | 0.180 | 0.216 | 6.06 | 6.27 | 0.983/0.997 | KXNHLTOTAL-26OCT13BUFMTL-7 +0.039 |
| WSH @ CAR | 0.594 | 0.587 | 0.166 | 0.210 | 6.12 | 6.38 | 1.000/0.961 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.045 |
| SEA @ PHI | 0.461 | 0.531 | 0.181 | 0.221 | 5.69 | 5.93 | 0.994/1.015 | KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 +0.083 |
| TBL @ NYR | 0.523 | 0.522 | 0.179 | 0.226 | 5.75 | 6.01 | 0.988/0.958 | KXNHLTOTAL-26OCT13TBNYR-7 +0.047 |
| STL @ OTT | 0.451 | 0.519 | 0.180 | 0.223 | 6.14 | 6.16 | 1.041/0.993 | KXNHLGAME-26OCT13STLOTT-OTT +0.068 |
| VAN @ NYI | 0.652 | 0.589 | 0.163 | 0.214 | 6.24 | 6.25 | 0.947/1.026 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.069 |
| PIT @ CHI | 0.454 | 0.445 | 0.179 | 0.221 | 6.15 | 6.48 | 1.003/1.021 | KXNHLTOTAL-26OCT13PITCHI-7 +0.059 |
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.493 | 0.475 | 0.186 | 0.221 | 5.96 | 6.19 | 0.986/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.044 |
| VGK @ NSH | 0.532 | 0.504 | 0.169 | 0.218 | 6.47 | 6.19 | 1.000/1.004 | KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 -0.052 |
| TOR @ UTA | 0.664 | 0.607 | 0.158 | 0.212 | 6.76 | 6.47 | 0.992/0.979 | KXNHLSPREAD-26OCT13TORUTA-UTA2 -0.070 |
| CGY @ ANA | 0.603 | 0.620 | 0.175 | 0.208 | 6.03 | 6.37 | 1.024/0.986 | KXNHLTOTAL-26OCT13CGYANA-7 +0.061 |
| EDM @ LAK | 0.440 | 0.478 | 0.175 | 0.216 | 6.20 | 6.23 | 0.993/0.994 | KXNHLGAME-26OCT13EDMLA-LA +0.038 |
| BOS @ SJS | 0.444 | 0.518 | 0.176 | 0.215 | 6.20 | 6.42 | 1.034/0.968 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 +0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 47 recommended · full analysis in card.md / packet.json `thesis_card`

- Timo Meier: 1+ goals NO @ 74c · p 0.7905 (adj 0.7766) · $3.76 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 65c · p 0.7042 (adj 0.6894) · $3.1 · thesis NJD:SUPPRESSED
- Viktor Arvidsson: 1+ assists NO @ 62c · p 0.7298 (adj 0.6519) · $2.62 · thesis DET:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7554 (adj 0.7365) · $4.57 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 84c · p 0.8943 (adj 0.8646) · $4.57 · thesis CBJ:WINS
- Sean Monahan: 1+ goals YES @ 19c · p 0.2294 (adj 0.217) · $1.01 · thesis CBJ:OFFENSE_4PLUS
- Owen Power: 1+ goals NO @ 88c · p 0.9206 (adj 0.9054) · $4.57 · thesis BUF:SUPPRESSED
- Chris Kreider: 1+ assists NO @ 69c · p 0.7531 (adj 0.719) · $3.48 · thesis MTL:SUPPRESSED
- Ethen Frank: 1+ goals YES @ 9c · p 0.129 (adj 0.1155) · $1.14 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 27c · p 0.3458 (adj 0.3054) · $1.61 · thesis WSH:OFFENSE_4PLUS
- Jordan Kyrou: 1+ assists NO @ 74c · p 0.7997 (adj 0.7673) · $4.57 · thesis WSH:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 9c · p 0.1267 (adj 0.115) · $1.06 · thesis SEA:OFFENSE_4PLUS
- Bobby McMann: 1+ goals NO @ 72c · p 0.7745 (adj 0.7584) · $3.43 · thesis SEA:SUPPRESSED
- Jared McCann: 1+ goals NO @ 73c · p 0.7823 (adj 0.7667) · $3.43 · thesis SEA:SUPPRESSED
- Kaapo Kakko: 1+ assists YES @ 25c · p 0.3156 (adj 0.2803) · $1.31 · thesis SEA:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 55c · p 0.7075 (adj 0.6019) · $4.24 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8387 (adj 0.7969) · $4.57 · thesis NYR:WINS
- Adam Jiricek: 2+ assists NO @ 94c · p 0.9744 (adj 0.9547) · $3.83 · thesis STL:SUPPRESSED
- Adam Jiricek: 1+ assists NO @ 67c · p 0.7796 (adj 0.7051) · $3.02 · thesis STL:SUPPRESSED
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.8304 (adj 0.7424) · $4.09 · thesis OTT:SUPPRESSED
- Aatu Raty: 1+ goals YES @ 10c · p 0.1382 (adj 0.1249) · $1.08 · thesis VAN:WINS_BY_2PLUS
- Paul Cotter: 1+ goals NO @ 83c · p 0.8701 (adj 0.8588) · $4.57 · thesis VAN:SUPPRESSED
- Kyle Palmieri: 1+ goals NO @ 70c · p 0.7496 (adj 0.7347) · $4.17 · thesis NYI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 14c · p 0.2162 (adj 0.1934) · $2.78 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 52c · p 0.7014 (adj 0.5802) · $4.57 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 29c · p 0.3476 (adj 0.3307) · $2.46 · thesis CHI:OFFENSE_4PLUS
- Cole Smith: 1+ goals YES @ 10c · p 0.1367 (adj 0.1238) · $1.02 · thesis CHI:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 86c · p 0.9322 (adj 0.9117) · $4.57 · thesis WPG:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 59c · p 0.6464 (adj 0.631) · $4.22 · thesis MIN:SUPPRESSED
- Ryan Hartman: 1+ assists YES @ 23c · p 0.3052 (adj 0.2601) · $1.54 · thesis MIN:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 57c · p 0.6478 (adj 0.6271) · $3.85 · thesis COL:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 20c · p 0.2469 (adj 0.2339) · $1.57 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 81c · p 0.8433 (adj 0.8325) · $3.0 · thesis COL:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 71c · p 0.7586 (adj 0.7452) · $2.81 · thesis VGK:SUPPRESSED
- Jack Eichel: 1+ goals NO @ 68c · p 0.7303 (adj 0.7165) · $2.54 · thesis VGK:SUPPRESSED
- Dylan Guenther: 1+ goals NO @ 61c · p 0.6687 (adj 0.6528) · $3.83 · thesis UTA:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 63c · p 0.7172 (adj 0.6711) · $3.2 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ assists NO @ 57c · p 0.6485 (adj 0.6067) · $1.91 · thesis TOR:SUPPRESSED
- Darren Raddysh: 1+ assists NO @ 58c · p 0.6858 (adj 0.6138) · $1.74 · thesis TOR:SUPPRESSED
- Alex Killorn: 1+ assists YES @ 30c · p 0.3663 (adj 0.3306) · $1.06 · thesis ANA:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 25c · p 0.3357 (adj 0.2878) · $1.79 · thesis EDM:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6135 (adj 0.5202) · $2.65 · thesis LAK:SUPPRESSED
- Mattias Ekholm: 1+ assists YES @ 28c · p 0.3509 (adj 0.313) · $1.46 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.5675 (adj 0.4456) · $2.21 · thesis EDM:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 55c · p 0.7075 (adj 0.5954) · $4.25 · thesis BOS:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.8082 (adj 0.7281) · $4.57 · thesis SJS:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.215 (adj 0.1975) · $1.3 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ DET** · priced 147/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 28.74, exp saves 25.15 (sd 6.61), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 27.87, exp saves 24.0 (sd 6.63), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.361 | 0.500 | 51/51 | +0.112 | STANDARD |
| Jack Hughes: 2+ points | 0.192 | 0.325 | 34/69 | +0.103 | STANDARD |
| Luke Evangelista: 1+ points | 0.347 | 0.470 | 48/54 | +0.095 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.270 | 0.390 | 40/62 | +0.093 | STANDARD |
| Anthony Mantha: 1+ assists | 0.167 | 0.285 | 29/72 | +0.099 | STANDARD |
| Anthony Mantha: 1+ points | 0.325 | 0.440 | 45/57 | +0.088 | STANDARD |

**FLA @ CBJ** · priced 155/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 26.31, exp saves 23.15 (sd 6.15), pull risk 0.041
- FLA net: Akira Schmid (PROBABLE) exp shots 28.0, exp saves 23.89 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ points | 0.420 | 0.560 | 57/45 | +0.113 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.241 | 0.370 | 38/64 | +0.103 | STANDARD |
| Sam Reinhart: 1+ points | 0.448 | 0.575 | 58/43 | +0.105 | STANDARD |
| Sam Reinhart: 1+ assists | 0.270 | 0.390 | 40/62 | +0.094 | STANDARD |
| Charlie Coyle: 1+ points | 0.552 | 0.455 | 47/56 | +0.065 | STANDARD |
| Sam Reinhart: 2+ points | 0.124 | 0.220 | 24/80 | +0.065 | STANDARD |

**BUF @ MTL** · priced 154/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.81, exp saves 25.11 (sd 6.84), pull risk 0.058
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.48, exp saves 21.86 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ points | 0.435 | 0.510 | 52/50 | +0.047 | STANDARD |
| Nick Suzuki: 1+ assists | 0.502 | 0.575 | 58/43 | +0.051 | STANDARD |
| Chris Kreider: 1+ assists | 0.247 | 0.315 | 32/69 | +0.048 | STANDARD |
| Chris Kreider: 2+ points | 0.109 | 0.170 | 19/85 | +0.032 | STANDARD |
| Owen Power: 1+ goals | 0.079 | 0.140 | 16/88 | +0.033 | STANDARD |
| Josh Norris: 1+ points | 0.434 | 0.375 | 39/64 | +0.028 | STANDARD |

**WSH @ CAR** · priced 182/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.49, exp saves 20.49 (sd 5.76), pull risk 0.052
- WSH net: Logan Thompson (PROJECTED) exp shots 31.11, exp saves 26.54 (sd 7.29), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.346 | 0.465 | 48/55 | +0.086 | STANDARD |
| Sebastian Aho: 1+ points | 0.544 | 0.635 | 64/37 | +0.070 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.316 | 0.225 | 25/80 | +0.053 | STANDARD |
| Taylor Hall: 1+ goals | 0.245 | 0.155 | 22/91 | +0.013 | STANDARD |
| Sebastian Aho: 2+ points | 0.188 | 0.270 | 30/76 | +0.039 | STANDARD |
| Ryan Leonard: 1+ assists | 0.346 | 0.265 | 27/74 | +0.062 | STANDARD |

**SEA @ PHI** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROBABLE) exp shots 26.23, exp saves 22.8 (sd 6.23), pull risk 0.049
- SEA net: Philipp Grubauer (PROJECTED) exp shots 26.94, exp saves 23.29 (sd 6.3), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dan Vladar: 24+ saves | 0.442 | 0.290 | 56/98 | -0.135 |  |
| Mackie Samoskevich: 1+ points | 0.308 | 0.420 | 44/60 | +0.075 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.142 | 0.250 | 27/77 | +0.075 | STANDARD |
| Sean Couturier: 1+ goals | 0.199 | 0.105 | 18/97 | +0.009 | STANDARD |
| David Jiricek: 1+ points | 0.250 | 0.340 | 35/67 | +0.064 | STANDARD |
| Jared McCann: 1+ points | 0.442 | 0.525 | 54/49 | +0.051 | STANDARD |

**TBL @ NYR** · priced 173/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 27.72, exp saves 24.04 (sd 6.52), pull risk 0.058
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.07, exp saves 20.82 (sd 5.9), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gabe Perreault: 1+ assists | 0.307 | 0.115 | 21/98 | +0.085 | STANDARD |
| John Carlson: 1+ points | 0.371 | 0.540 | 55/47 | +0.141 | STANDARD |
| John Carlson: 1+ assists | 0.292 | 0.455 | 46/55 | +0.140 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.461 | 0.605 | 61/40 | +0.123 | STANDARD |
| Dylan Garand: 26+ saves | 0.401 | 0.270 | 52/98 | -0.136 |  |
| Nikita Kucherov: 2+ points | 0.276 | 0.405 | 41/60 | +0.107 | STANDARD |

**STL @ OTT** · priced 166/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.35, exp saves 21.19 (sd 5.94), pull risk 0.057
- STL net: Joel Hofer (PROJECTED) exp shots 28.14, exp saves 24.27 (sd 6.69), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ points | 0.302 | 0.445 | 46/57 | +0.111 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.170 | 0.305 | 32/71 | +0.106 | STANDARD |
| Adam Jiricek: 1+ points | 0.280 | 0.400 | 41/61 | +0.093 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.220 | 0.335 | 34/67 | +0.094 | PRIOR_HEAVY |
| Jordan Spence: 1+ points | 0.387 | 0.275 | 28/73 | +0.093 | STANDARD |
| Jordan Spence: 1+ assists | 0.329 | 0.225 | 24/79 | +0.076 | STANDARD |

**VAN @ NYI** · priced 162/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.75 (sd 5.99), pull risk 0.051
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.68, exp saves 25.35 (sd 6.92), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ilya Sorokin: 21+ saves | 0.579 | 0.300 | 53/93 | +0.032 |  |
| Victor Eklund: 1+ assists | 0.207 | 0.340 | 35/67 | +0.107 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ points | 0.427 | 0.555 | 57/46 | +0.095 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.236 | 0.350 | 36/66 | +0.088 | STANDARD |
| Victor Eklund: 1+ points | 0.366 | 0.475 | 49/54 | +0.077 | PRIOR_HEAVY |
| Bo Horvat: 1+ points | 0.559 | 0.660 | 67/35 | +0.075 | STANDARD |

**PIT @ CHI** · priced 156/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.01, exp saves 24.82 (sd 6.95), pull risk 0.076
- PIT net: Sergei Murashov (PROJECTED) exp shots 25.04, exp saves 21.75 (sd 6.14), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.299 | 0.485 | 49/52 | +0.164 | STANDARD |
| Patrick Kane: 1+ points | 0.495 | 0.630 | 64/38 | +0.109 | STANDARD |
| Anton Frondell: 1+ points | 0.566 | 0.440 | 45/57 | +0.098 | STANDARD |
| Anton Frondell: 1+ assists | 0.385 | 0.260 | 27/75 | +0.101 | STANDARD |
| Patrick Kane: 2+ points | 0.156 | 0.260 | 28/76 | +0.071 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.593 | 0.490 | 50/52 | +0.076 | STANDARD |

**MIN @ WPG** · priced 145/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Stuart Skinner: 26+ saves | 0.432 | 0.270 | 52/98 | -0.105 |  |
| Neal Pionk: 1+ points | 0.383 | 0.490 | 50/52 | +0.080 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.243 | 0.345 | 36/67 | +0.072 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.599 | 0.695 | 71/32 | +0.066 | STANDARD |
| Gabriel Vilardi: 2+ points | 0.203 | 0.110 | 18/96 | +0.012 | STANDARD |
| Ryan Hartman: 1+ assists | 0.305 | 0.215 | 23/80 | +0.063 | STANDARD |

**COL @ DAL** · priced 156/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 28.74, exp saves 24.86 (sd 6.77), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.0 (sd 6.13), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.283 | 0.400 | 42/62 | +0.080 | STANDARD |
| Cale Makar: 1+ points | 0.502 | 0.615 | 63/40 | +0.081 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.276 | 0.385 | 40/63 | +0.078 | STANDARD |
| Cale Makar: 2+ points | 0.155 | 0.255 | 28/77 | +0.062 | STANDARD |
| Mikko Rantanen: 1+ points | 0.569 | 0.665 | 68/35 | +0.065 | STANDARD |
| Miro Heiskanen: 1+ points | 0.461 | 0.550 | 57/47 | +0.052 | STANDARD |

**VGK @ NSH** · priced 160/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 29.36, exp saves 25.64 (sd 6.78), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.61 (sd 6.32), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.216 | 0.350 | 36/66 | +0.108 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 1+ points | 0.579 | 0.695 | 70/31 | +0.096 | STANDARD |
| Roman Josi: 1+ assists | 0.438 | 0.535 | 54/47 | +0.074 | STANDARD |
| Jack Eichel: 2+ assists | 0.108 | 0.200 | 22/82 | +0.062 | STANDARD |
| Mark Stone: 1+ goals | 0.297 | 0.210 | 33/91 | -0.048 | STANDARD |

**TOR @ UTA** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.03, exp saves 21.92 (sd 6.05), pull risk 0.052
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.85, exp saves 26.92 (sd 7.47), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.510 | 52/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.218 | 0.320 | 33/69 | +0.077 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.283 | 0.375 | 38/63 | +0.071 | STANDARD |
| Auston Matthews: 1+ assists | 0.351 | 0.435 | 44/57 | +0.061 | STANDARD |
| Clayton Keller: 1+ assists | 0.477 | 0.555 | 56/45 | +0.056 | STANDARD |

**CGY @ ANA** · priced 155/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.29, exp saves 23.16 (sd 6.24), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 31.79, exp saves 26.81 (sd 7.5), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.258 | 0.135 | 17/90 | +0.078 | STANDARD |
| Aydar Suniev: 1+ goals | 0.193 | 0.110 | 18/96 | +0.002 | PRIOR_HEAVY |
| Alex Killorn: 1+ assists | 0.366 | 0.295 | 30/71 | +0.052 | STANDARD |
| A.J. Greer: 1+ assists | 0.148 | 0.210 | 23/81 | +0.031 | STANDARD |
| Tim Washe: 1+ goals | 0.150 | 0.095 | 12/93 | +0.023 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.278 | 0.225 | 25/80 | +0.014 | STANDARD |

**EDM @ LAK** · priced 161/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.16, exp saves 24.36 (sd 6.7), pull risk 0.062
- EDM net: Devon Levi (PROJECTED) exp shots 27.62, exp saves 23.96 (sd 6.59), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.432 | 0.595 | 60/41 | +0.141 | STANDARD |
| Leon Draisaitl: 2+ points | 0.288 | 0.440 | 45/57 | +0.124 | STANDARD |
| Connor McDavid: 1+ assists | 0.491 | 0.635 | 64/37 | +0.122 | STANDARD |
| Artemi Panarin: 1+ assists | 0.387 | 0.530 | 54/48 | +0.116 | STANDARD |
| Connor McDavid: 2+ points | 0.349 | 0.485 | 50/53 | +0.104 | STANDARD |
| Trevor Moore: 1+ assists | 0.326 | 0.195 | 23/84 | +0.083 | STANDARD |

**BOS @ SJS** · priced 162/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 26.63, exp saves 22.97 (sd 6.47), pull risk 0.07
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.58, exp saves 23.81 (sd 6.56), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.292 | 0.465 | 48/55 | +0.140 | STANDARD |
| Charlie McAvoy: 1+ points | 0.385 | 0.555 | 57/46 | +0.138 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.336 | 0.205 | 24/83 | +0.083 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.192 | 0.315 | 32/69 | +0.103 | PRIOR_HEAVY |
| Luca Cagnoni: 1+ points | 0.312 | 0.425 | 44/59 | +0.081 | STANDARD |
| Tyler Toffoli: 1+ points | 0.474 | 0.365 | 38/65 | +0.077 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
