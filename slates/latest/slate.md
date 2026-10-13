# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T21:47:56Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 16 · markets on board: 5676 · contracts joined: 3796 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 3396, 'OK': 229, 'NO_EDGE': 171}
families: {'period_winner': 144, 'period_spread': 96, 'period_total': 144, 'player_assists': 589, 'game_early_goal': 16, 'first_goal': 580, 'game_winner': 32, 'player_goals': 998, 'game_overtime': 16, 'player_points': 783, 'goalie_saves': 30, 'game_spread': 64, 'team_total': 160, 'game_total': 144}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 2026-10-13T22:00:00Z | T-10m | 0.558 | 0.442 | 0.188 | 5.64 | 2.99 | 2.65 | 234 (25/209) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-10-13T22:15:00Z | T-10m | 0.577 | 0.423 | 0.173 | 6.23 | 3.35 | 2.88 | 221 (25/196) | CONFIRMED/CONFIRMED |
| BUF @ MTL | 2026-10-13T22:30:00Z | T-30m | 0.546 | 0.454 | 0.180 | 6.06 | 3.17 | 2.89 | 263 (25/238) | CONFIRMED/PROJECTED |
| WSH @ CAR | 2026-10-13T22:45:00Z | T-30m | 0.577 | 0.423 | 0.175 | 5.99 | 3.22 | 2.76 | 242 (25/217) | PROBABLE/CONFIRMED |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-60m | 0.465 | 0.535 | 0.189 | 5.67 | 2.73 | 2.94 | 258 (25/233) | CONFIRMED/PROJECTED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-60m | 0.514 | 0.486 | 0.186 | 5.72 | 2.91 | 2.81 | 252 (25/227) | CONFIRMED/PROBABLE |
| STL @ OTT | 2026-10-13T23:30:00Z | T-90m | 0.429 | 0.571 | 0.175 | 6.21 | 2.88 | 3.33 | 242 (25/217) | CONFIRMED/PROBABLE |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-90m | 0.661 | 0.339 | 0.160 | 6.30 | 3.68 | 2.62 | 222 (25/197) | CONFIRMED/PROBABLE |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-90m | 0.463 | 0.537 | 0.180 | 6.13 | 2.94 | 3.19 | 227 (25/202) | CONFIRMED/CONFIRMED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-90m | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 213 (25/188) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-90m | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 214 (25/189) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-90m | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 239 (25/214) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-3h | 0.674 | 0.326 | 0.152 | 6.79 | 3.98 | 2.81 | 225 (25/200) | PROBABLE/CONFIRMED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-3h | 0.645 | 0.355 | 0.171 | 6.36 | 3.64 | 2.72 | 250 (25/225) | CONFIRMED/PROBABLE |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-3h | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 217 (25/192) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-3h | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB4 | team_total | 0.324 | 0.455 | 0.428 | 46 | 55 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB3 | team_total | 0.541 | 0.670 | 0.646 | 68 | 34 | no | +0.103 | OK |
| KXNHLGAME-26OCT13TBNYR-NYR | game_winner | 0.514 | 0.405 | 0.426 | 41 | 60 | yes | +0.087 | OK |
| KXNHLGAME-26OCT13TBNYR-TB | game_winner | 0.486 | 0.595 | 0.574 | 60 | 41 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB2 | game_spread | 0.262 | 0.365 | 0.343 | 37 | 64 | no | +0.082 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB3 | game_spread | 0.147 | 0.245 | 0.222 | 25 | 76 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB5 | team_total | 0.157 | 0.255 | 0.233 | 26 | 75 | no | +0.080 | OK |
| KXNHLTOTAL-26OCT13NJDET-7 | game_total | 0.356 | 0.455 | 0.435 | 46 | 55 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ3 | team_total | 0.499 | 0.595 | 0.576 | 60 | 41 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT13NJDET-6 | game_total | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ4 | team_total | 0.290 | 0.375 | 0.357 | 38 | 63 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.767 | 0.850 | 0.836 | 86 | 16 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT13NJDET-5 | game_total | 0.705 | 0.785 | 0.770 | 79 | 22 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 | team_total | 0.401 | 0.485 | 0.468 | 49 | 52 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.403 | 0.485 | 0.468 | 49 | 52 | no | +0.059 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.326 | 0.405 | 0.389 | 41 | 60 | no | +0.057 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.674 | 0.595 | 0.611 | 60 | 41 | yes | +0.057 | OK |
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.533 | 0.455 | 0.471 | 46 | 55 | yes | +0.056 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ5 | team_total | 0.134 | 0.205 | 0.189 | 21 | 80 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-6 | game_total | 0.478 | 0.555 | 0.540 | 56 | 45 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-7 | game_total | 0.368 | 0.445 | 0.429 | 45 | 56 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13NJDET-8 | game_total | 0.182 | 0.255 | 0.239 | 26 | 75 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.461 | 0.385 | 0.400 | 39 | 62 | yes | +0.055 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.286 | 0.215 | 0.228 | 22 | 79 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ2 | team_total | 0.737 | 0.810 | 0.797 | 82 | 20 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 | team_total | 0.302 | 0.375 | 0.360 | 38 | 63 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT13NJDET-4 | game_total | 0.801 | 0.865 | 0.854 | 87 | 14 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-5 | game_total | 0.698 | 0.765 | 0.752 | 77 | 24 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.804 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-6 | game_total | 0.466 | 0.535 | 0.521 | 54 | 47 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-5 | game_total | 0.753 | 0.815 | 0.804 | 82 | 19 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-7 | game_total | 0.427 | 0.495 | 0.481 | 50 | 51 | no | +0.046 | OK |
| KXNHLGAME-26OCT13STLOTT-OTT | game_winner | 0.429 | 0.495 | 0.482 | 50 | 51 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-4 | game_total | 0.798 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL3 | team_total | 0.622 | 0.685 | 0.673 | 69 | 32 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.585 | 0.598 | 59 | 42 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.523 | 0.585 | 0.573 | 59 | 42 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT13NJDET-9 | game_total | 0.121 | 0.175 | 0.163 | 18 | 83 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.626 | 0.690 | 0.678 | 70 | 32 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT2 | game_spread | 0.227 | 0.285 | 0.273 | 29 | 72 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.577 | 0.510 | 0.523 | 52 | 50 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA6 | team_total | 0.208 | 0.150 | 0.160 | 16 | 86 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL5 | team_total | 0.250 | 0.195 | 0.205 | 20 | 81 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ2 | game_spread | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-6 | game_total | 0.536 | 0.595 | 0.583 | 60 | 41 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI5 | team_total | 0.143 | 0.195 | 0.183 | 20 | 81 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT13WSHCAR-CAR4 | team_total | 0.416 | 0.475 | 0.463 | 48 | 53 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.436 | 0.495 | 0.483 | 50 | 51 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.763 | 0.815 | 0.805 | 82 | 19 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.371 | 0.305 | 0.318 | 32 | 71 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL5 | team_total | 0.220 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.463 | 0.405 | 0.416 | 41 | 60 | yes | +0.036 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.537 | 0.595 | 0.584 | 60 | 41 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.221 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.134 | 0.185 | 0.174 | 19 | 82 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-5 | game_total | 0.743 | 0.795 | 0.785 | 80 | 21 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL6 | team_total | 0.119 | 0.070 | 0.078 | 8 | 94 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT13PITCHI-6 | game_total | 0.549 | 0.605 | 0.594 | 61 | 40 | no | +0.034 | OK |
| KXNHLGAME-26OCT13STLOTT-STL | game_winner | 0.571 | 0.515 | 0.526 | 52 | 49 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-7 | game_total | 0.359 | 0.415 | 0.404 | 42 | 59 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL3 | team_total | 0.649 | 0.595 | 0.606 | 60 | 41 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT13TBNYR-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13STLOTT-STL2 | game_spread | 0.347 | 0.295 | 0.305 | 30 | 71 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-4 | game_total | 0.830 | 0.875 | 0.867 | 88 | 13 | no | +0.032 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 0.558 | 0.545 | 0.188 | 0.224 | 5.64 | 5.77 | 0.994/0.984 | KXNHLTOTAL-26OCT13NJDET-7 +0.027 |
| FLA @ CBJ | 0.577 | 0.606 | 0.173 | 0.213 | 6.23 | 6.07 | 1.008/0.991 | KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3 -0.039 |
| BUF @ MTL | 0.546 | 0.553 | 0.180 | 0.216 | 6.06 | 6.27 | 0.983/0.997 | KXNHLTOTAL-26OCT13BUFMTL-7 +0.039 |
| WSH @ CAR | 0.577 | 0.574 | 0.175 | 0.216 | 5.99 | 6.31 | 1.000/0.938 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.055 |
| SEA @ PHI | 0.465 | 0.534 | 0.189 | 0.223 | 5.67 | 5.93 | 0.994/1.015 | KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 +0.080 |
| TBL @ NYR | 0.514 | 0.519 | 0.186 | 0.221 | 5.72 | 6.00 | 0.988/0.957 | KXNHLTOTAL-26OCT13TBNYR-7 +0.052 |
| STL @ OTT | 0.429 | 0.499 | 0.175 | 0.224 | 6.21 | 6.21 | 1.071/0.984 | KXNHLSPREAD-26OCT13STLOTT-STL2 -0.074 |
| VAN @ NYI | 0.661 | 0.593 | 0.160 | 0.210 | 6.30 | 6.26 | 0.947/1.030 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.076 |
| PIT @ CHI | 0.463 | 0.446 | 0.180 | 0.212 | 6.13 | 6.40 | 0.988/1.012 | KXNHLTOTAL-26OCT13PITCHI-7 +0.055 |
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.496 | 0.474 | 0.178 | 0.221 | 5.91 | 6.20 | 0.994/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.059 |
| VGK @ NSH | 0.533 | 0.507 | 0.171 | 0.217 | 6.49 | 6.20 | 1.002/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.054 |
| TOR @ UTA | 0.674 | 0.597 | 0.152 | 0.209 | 6.79 | 6.40 | 0.991/0.956 | KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 -0.092 |
| CGY @ ANA | 0.645 | 0.631 | 0.171 | 0.210 | 6.36 | 6.41 | 1.016/1.002 | KXNHLTEAMTOTAL-26OCT13CGYANA-CGY2 +0.018 |
| EDM @ LAK | 0.440 | 0.480 | 0.173 | 0.218 | 6.27 | 6.25 | 0.995/0.994 | KXNHLSPREAD-26OCT13EDMLA-EDM2 -0.043 |
| BOS @ SJS | 0.413 | 0.507 | 0.175 | 0.216 | 6.17 | 6.40 | 1.039/0.956 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 +0.094 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 53 recommended · full analysis in card.md / packet.json `thesis_card`

- Nico Hischier: 1+ goals NO @ 70c · p 0.76 (adj 0.7438) · $4.42 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 51c · p 0.6401 (adj 0.5523) · $2.53 · thesis NJD:SUPPRESSED
- Andrew Copp: 1+ goals YES @ 16c · p 0.1978 (adj 0.1871) · $1.14 · thesis DET:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.2107 (adj 0.1943) · $2.23 · thesis CBJ:WINS_BY_2PLUS
- Danton Heinen: 1+ goals YES @ 10c · p 0.1371 (adj 0.1266) · $1.21 · thesis CBJ:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 70c · p 0.7598 (adj 0.7436) · $4.63 · thesis FLA:SUPPRESSED
- Sandis Vilmanis: 1+ goals YES @ 9c · p 0.1235 (adj 0.1139) · $1.1 · thesis FLA:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 15c · p 0.1958 (adj 0.1831) · $1.03 · thesis BUF:OFFENSE_4PLUS
- Chris Kreider: 1+ goals NO @ 72c · p 0.7676 (adj 0.7544) · $4.63 · thesis MTL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2225 (adj 0.2081) · $1.83 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 14c · p 0.1769 (adj 0.1664) · $1.08 · thesis WSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ assists NO @ 54c · p 0.6661 (adj 0.5776) · $2.78 · thesis CAR:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.143 (adj 0.131) · $1.4 · thesis SEA:OFFENSE_4PLUS
- Jared McCann: 1+ goals NO @ 72c · p 0.7849 (adj 0.7674) · $4.44 · thesis SEA:SUPPRESSED
- Porter Martone: 1+ goals NO @ 75c · p 0.8046 (adj 0.7897) · $4.44 · thesis PHI:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 16c · p 0.2018 (adj 0.1901) · $1.3 · thesis PHI:WINS_BY_2PLUS
- Gabe Perreault: 1+ assists YES @ 22c · p 0.3103 (adj 0.2626) · $1.8 · thesis NYR:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8409 (adj 0.7979) · $4.63 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 71c · p 0.7668 (adj 0.7359) · $3.79 · thesis NYR:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $1.59 · thesis OTT:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1483 (adj 0.1375) · $1.19 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.838 (adj 0.7516) · $4.39 · thesis OTT:SUPPRESSED
- Adam Jiricek: 1+ assists NO @ 69c · p 0.7788 (adj 0.7294) · $4.39 · thesis STL:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1852 (adj 0.1701) · $1.97 · thesis VAN:OFFENSE_4PLUS
- Kyle Palmieri: 1+ goals NO @ 70c · p 0.7465 (adj 0.7336) · $3.74 · thesis NYI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 12c · p 0.1902 (adj 0.1714) · $2.65 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 53c · p 0.7216 (adj 0.5906) · $4.63 · thesis CHI:SUPPRESSED
- Anton Frondell: 1+ assists YES @ 27c · p 0.3517 (adj 0.3084) · $1.78 · thesis CHI:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1645 (adj 0.1546) · $1.13 · thesis PIT:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 87c · p 0.9322 (adj 0.9154) · $4.63 · thesis WPG:SUPPRESSED
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1353 (adj 0.1252) · $1.13 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 23c · p 0.3052 (adj 0.2601) · $1.46 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 60c · p 0.6464 (adj 0.6335) · $3.2 · thesis MIN:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 9c · p 0.1355 (adj 0.1229) · $1.55 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 20c · p 0.256 (adj 0.2408) · $2.06 · thesis COL:OFFENSE_4PLUS
- Nathan MacKinnon: 2+ goals NO @ 89c · p 0.922 (adj 0.9128) · $4.63 · thesis COL:SUPPRESSED
- Miro Heiskanen: 1+ assists NO @ 53c · p 0.6085 (adj 0.5668) · $2.54 · thesis DAL:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 71c · p 0.7616 (adj 0.7475) · $4.63 · thesis VGK:SUPPRESSED
- Brady Skjei: 1+ assists YES @ 23c · p 0.308 (adj 0.2615) · $1.29 · thesis NSH:OFFENSE_4PLUS
- Darren Raddysh: 2+ assists NO @ 89c · p 0.9442 (adj 0.9146) · $4.07 · thesis TOR:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 70c · p 0.7882 (adj 0.7391) · $4.07 · thesis UTA:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 24c · p 0.3101 (adj 0.2701) · $1.02 · thesis TOR:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6552) · $2.41 · thesis UTA:SUPPRESSED
- Tim Washe: 1+ goals YES @ 10c · p 0.149 (adj 0.1355) · $1.74 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1395 (adj 0.1271) · $1.24 · thesis ANA:OFFENSE_4PLUS
- Nikita Nesterenko: 1+ assists NO @ 74c · p 0.8073 (adj 0.7687) · $4.63 · thesis ANA:SUPPRESSED
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9098 (adj 0.8624) · $4.55 · thesis LAK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6128 (adj 0.5232) · $2.4 · thesis LAK:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 32c · p 0.4006 (adj 0.3578) · $1.88 · thesis EDM:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $1.46 · thesis BOS:OFFENSE_4PLUS
- Matthew Poitras: 1+ goals YES @ 9c · p 0.1244 (adj 0.1145) · $1.07 · thesis BOS:OFFENSE_4PLUS
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.148 (adj 0.1372) · $1.24 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ goals NO @ 74c · p 0.7912 (adj 0.7772) · $4.63 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ DET** · priced 154/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 28.74, exp saves 25.15 (sd 6.61), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 27.87, exp saves 24.0 (sd 6.63), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.360 | 0.495 | 50/51 | +0.113 | STANDARD |
| Jack Hughes: 2+ points | 0.189 | 0.320 | 33/69 | +0.106 | STANDARD |
| Anthony Mantha: 1+ points | 0.317 | 0.445 | 45/56 | +0.106 | STANDARD |
| Nico Hischier: 1+ points | 0.454 | 0.575 | 58/43 | +0.099 | STANDARD |
| Albert Johansson: 1+ assists | 0.194 | 0.075 | 13/98 | +0.056 | STANDARD |
| Jack Hughes: 1+ points | 0.549 | 0.665 | 67/34 | +0.096 | STANDARD |

**FLA @ CBJ** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 26.31, exp saves 23.08 (sd 6.23), pull risk 0.046
- FLA net: Akira Schmid (CONFIRMED) exp shots 28.0, exp saves 23.91 (sd 6.64), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ points | 0.420 | 0.560 | 57/45 | +0.113 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.236 | 0.370 | 38/64 | +0.108 | STANDARD |
| Sam Reinhart: 1+ points | 0.444 | 0.570 | 58/44 | +0.099 | STANDARD |
| Sam Reinhart: 1+ assists | 0.260 | 0.380 | 39/63 | +0.093 | STANDARD |
| Charlie Coyle: 1+ points | 0.563 | 0.460 | 47/55 | +0.076 | STANDARD |
| Brady Tkachuk: 2+ points | 0.103 | 0.205 | 22/81 | +0.076 | STANDARD |

**BUF @ MTL** · priced 207/212 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.81, exp saves 25.17 (sd 6.76), pull risk 0.055
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.48, exp saves 21.86 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.655 | 0.480 | 50/54 | +0.137 |  |
| Mattias Samuelsson: 1+ assists | 0.258 | 0.150 | 27/97 | -0.025 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.247 | 0.145 | 27/98 | -0.037 | STANDARD |
| Alexandre Carrier: 1+ assists | 0.220 | 0.125 | 22/97 | -0.012 | STANDARD |
| Chris Kreider: 1+ points | 0.415 | 0.505 | 51/50 | +0.067 | STANDARD |
| Nick Suzuki: 1+ assists | 0.497 | 0.575 | 58/43 | +0.056 | STANDARD |

**WSH @ CAR** · priced 181/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.49, exp saves 20.51 (sd 5.8), pull risk 0.051
- WSH net: Logan Thompson (CONFIRMED) exp shots 31.11, exp saves 26.58 (sd 7.28), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.334 | 0.470 | 48/54 | +0.109 | STANDARD |
| Sebastian Aho: 1+ points | 0.527 | 0.635 | 64/37 | +0.087 | STANDARD |
| Pyotr Kochetkov: 23+ saves | 0.353 | 0.455 | 46/55 | +0.079 |  |
| Sebastian Aho: 2+ points | 0.179 | 0.275 | 29/74 | +0.067 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.317 | 0.235 | 24/77 | +0.064 | STANDARD |
| Ryan Leonard: 1+ assists | 0.346 | 0.270 | 28/74 | +0.052 | STANDARD |

**SEA @ PHI** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.23, exp saves 22.79 (sd 6.27), pull risk 0.05
- SEA net: Philipp Grubauer (PROJECTED) exp shots 26.94, exp saves 23.31 (sd 6.32), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.203 | 0.510 | 96/94 | -0.147 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.297 | 0.510 | 96/94 | -0.241 | STANDARD |
| Adam Larsson: 1+ assists | 0.249 | 0.115 | 20/97 | +0.038 | STANDARD |
| David Jiricek: 1+ points | 0.245 | 0.355 | 36/65 | +0.089 | STANDARD |
| Jared McCann: 1+ points | 0.444 | 0.545 | 55/46 | +0.079 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.139 | 0.240 | 25/77 | +0.078 | STANDARD |

**TBL @ NYR** · priced 195/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 27.72, exp saves 24.07 (sd 6.49), pull risk 0.056
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.07, exp saves 20.83 (sd 5.92), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.377 | 0.555 | 57/46 | +0.146 | STANDARD |
| John Carlson: 1+ assists | 0.296 | 0.455 | 46/55 | +0.137 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.471 | 0.620 | 63/39 | +0.122 | STANDARD |
| Andrei Vasilevskiy: 24+ saves | 0.311 | 0.455 | 48/57 | +0.101 |  |
| Nikita Kucherov: 2+ points | 0.276 | 0.410 | 42/60 | +0.107 | STANDARD |
| John Carlson: 2+ points | 0.078 | 0.190 | 20/82 | +0.092 | STANDARD |

**STL @ OTT** · priced 185/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 24.35, exp saves 21.12 (sd 5.93), pull risk 0.059
- STL net: Joel Hofer (PROBABLE) exp shots 28.14, exp saves 24.3 (sd 6.76), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ points | 0.404 | 0.265 | 27/74 | +0.120 | STANDARD |
| Michael Amadio: 1+ assists | 0.267 | 0.130 | 24/98 | +0.014 | STANDARD |
| Andre Burakovsky: 1+ points | 0.294 | 0.430 | 44/58 | +0.109 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.162 | 0.295 | 30/71 | +0.114 | STANDARD |
| Jordan Spence: 1+ assists | 0.342 | 0.225 | 24/79 | +0.089 | STANDARD |
| Joel Hofer: 27+ saves | 0.364 | 0.250 | 44/94 | -0.093 |  |

**VAN @ NYI** · priced 158/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.73 (sd 6.02), pull risk 0.051
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.68, exp saves 25.33 (sd 6.96), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ assists | 0.215 | 0.340 | 35/67 | +0.100 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ points | 0.430 | 0.535 | 55/48 | +0.073 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.241 | 0.345 | 35/66 | +0.083 | STANDARD |
| Victor Eklund: 1+ points | 0.377 | 0.475 | 48/53 | +0.075 | PRIOR_HEAVY |
| Bo Horvat: 1+ points | 0.559 | 0.650 | 66/36 | +0.064 | STANDARD |
| Ilya Sorokin: 21+ saves | 0.580 | 0.495 | 50/51 | +0.062 |  |

**PIT @ CHI** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 29.01, exp saves 24.77 (sd 6.88), pull risk 0.08
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.04, exp saves 21.77 (sd 6.08), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.278 | 0.480 | 49/53 | +0.174 | STANDARD |
| Alex Vlasic: 1+ assists | 0.282 | 0.100 | 18/98 | +0.092 | STANDARD |
| Patrick Kane: 1+ points | 0.460 | 0.630 | 64/38 | +0.143 | STANDARD |
| Samuel Girard: 1+ assists | 0.296 | 0.140 | 26/98 | +0.022 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.259 | 0.105 | 19/98 | +0.058 | STANDARD |
| Sam Rinzel: 1+ assists | 0.252 | 0.105 | 19/98 | +0.051 | STANDARD |

**MIN @ WPG** · priced 159/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 27+ saves | 0.361 | 0.465 | 47/54 | +0.082 |  |
| Kirill Kaprizov: 2+ points | 0.243 | 0.340 | 35/67 | +0.072 | STANDARD |
| Ryan Hartman: 1+ assists | 0.305 | 0.215 | 23/80 | +0.063 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.599 | 0.685 | 69/32 | +0.066 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.388 | 0.470 | 48/54 | +0.054 | STANDARD |
| Neal Pionk: 2+ points | 0.086 | 0.160 | 17/85 | +0.055 | STANDARD |

**COL @ DAL** · priced 154/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.286 | 0.400 | 41/61 | +0.088 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.409 | 0.505 | 51/50 | +0.073 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.286 | 0.380 | 39/63 | +0.068 | STANDARD |
| Mikko Rantanen: 2+ points | 0.202 | 0.295 | 31/72 | +0.064 | STANDARD |
| Devon Toews: 1+ points | 0.403 | 0.495 | 50/51 | +0.069 | STANDARD |
| Miro Heiskanen: 1+ points | 0.450 | 0.540 | 55/47 | +0.063 | STANDARD |

**VGK @ NSH** · priced 187/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Hanifin: 1+ assists | 0.260 | 0.100 | 18/98 | +0.070 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 2+ points | 0.216 | 0.340 | 35/67 | +0.099 | STANDARD |
| Nicolas Hague: 1+ assists | 0.193 | 0.070 | 12/98 | +0.066 | STANDARD |
| Nick Perbix: 1+ assists | 0.195 | 0.080 | 14/98 | +0.047 | STANDARD |
| Jack Eichel: 1+ points | 0.583 | 0.695 | 70/31 | +0.092 | STANDARD |

**TOR @ UTA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 25.03, exp saves 21.92 (sd 6.07), pull risk 0.052
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.85, exp saves 26.98 (sd 7.41), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.319 | 0.425 | 43/58 | +0.084 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.510 | 52/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.212 | 0.310 | 32/70 | +0.074 | STANDARD |
| Easton Cowan: 1+ points | 0.421 | 0.340 | 35/67 | +0.055 | STANDARD |
| John Tavares: 1+ assists | 0.294 | 0.375 | 39/64 | +0.050 | STANDARD |
| Easton Cowan: 1+ assists | 0.310 | 0.230 | 24/78 | +0.057 | STANDARD |

**CGY @ ANA** · priced 191/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 26.29, exp saves 23.15 (sd 6.3), pull risk 0.047
- CGY net: Dustin Wolf (PROBABLE) exp shots 31.79, exp saves 26.75 (sd 7.4), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ assists | 0.294 | 0.100 | 18/98 | +0.104 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.237 | 0.075 | 13/98 | +0.100 | STANDARD |
| Noah Warren: 1+ points | 0.341 | 0.190 | 20/82 | +0.130 | PRIOR_HEAVY |
| Tim Washe: 1+ assists | 0.256 | 0.115 | 21/98 | +0.034 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.223 | 0.085 | 15/98 | +0.064 | STANDARD |
| Kevin Bahl: 1+ points | 0.277 | 0.155 | 17/86 | +0.097 | STANDARD |

**EDM @ LAK** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 28.16, exp saves 24.3 (sd 6.72), pull risk 0.065
- EDM net: Devon Levi (CONFIRMED) exp shots 27.62, exp saves 23.94 (sd 6.59), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.435 | 0.595 | 60/41 | +0.138 | STANDARD |
| Connor McDavid: 1+ assists | 0.481 | 0.635 | 64/37 | +0.132 | STANDARD |
| Leon Draisaitl: 2+ points | 0.290 | 0.435 | 44/57 | +0.123 | STANDARD |
| Connor McDavid: 2+ points | 0.337 | 0.480 | 49/53 | +0.115 | STANDARD |
| Artemi Panarin: 1+ assists | 0.387 | 0.525 | 53/48 | +0.115 | STANDARD |
| Connor McDavid: 2+ assists | 0.139 | 0.270 | 28/74 | +0.107 | STANDARD |

**BOS @ SJS** · priced 219/226 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.44), pull risk 0.069
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.58, exp saves 23.85 (sd 6.47), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.396 | 0.560 | 57/45 | +0.137 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.297 | 0.450 | 46/56 | +0.126 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.555 | 56/45 | +0.113 | STANDARD |
| Sam Dickinson: 1+ assists | 0.215 | 0.080 | 14/98 | +0.066 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.230 | 0.100 | 18/98 | +0.040 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.183 | 0.310 | 32/70 | +0.103 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
