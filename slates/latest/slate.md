# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T17:30:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 16 · markets on board: 5440 · contracts joined: 3560 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 3160, 'OK': 221, 'NO_EDGE': 179}
families: {'period_winner': 144, 'period_spread': 96, 'period_total': 144, 'player_assists': 489, 'game_early_goal': 16, 'first_goal': 582, 'game_winner': 32, 'player_goals': 1000, 'game_overtime': 16, 'player_points': 652, 'goalie_saves': 21, 'game_spread': 64, 'team_total': 160, 'game_total': 144}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 2026-10-13T22:00:00Z | T-3h | 0.558 | 0.442 | 0.188 | 5.64 | 2.99 | 2.65 | 230 (25/205) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-10-13T22:15:00Z | T-3h | 0.572 | 0.428 | 0.176 | 6.22 | 3.34 | 2.88 | 212 (25/187) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-13T22:30:00Z | T-3h | 0.546 | 0.454 | 0.180 | 6.06 | 3.17 | 2.89 | 234 (25/209) | CONFIRMED/PROJECTED |
| WSH @ CAR | 2026-10-13T22:45:00Z | T-3h | 0.587 | 0.413 | 0.174 | 6.04 | 3.28 | 2.76 | 245 (25/220) | PROBABLE/PROBABLE |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-3h | 0.465 | 0.535 | 0.189 | 5.67 | 2.73 | 2.94 | 226 (25/201) | CONFIRMED/PROJECTED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-3h | 0.514 | 0.486 | 0.186 | 5.72 | 2.91 | 2.81 | 239 (25/214) | CONFIRMED/PROBABLE |
| STL @ OTT | 2026-10-13T23:30:00Z | T-3h | 0.448 | 0.552 | 0.179 | 6.11 | 2.88 | 3.22 | 236 (25/211) | PROJECTED/PROBABLE |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-6h | 0.661 | 0.339 | 0.160 | 6.30 | 3.68 | 2.62 | 222 (25/197) | CONFIRMED/PROBABLE |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-6h | 0.459 | 0.541 | 0.173 | 6.14 | 2.94 | 3.20 | 220 (25/195) | PROBABLE/PROBABLE |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-6h | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 207 (25/182) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-6h | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 214 (25/189) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-6h | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 216 (25/191) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-6h | 0.674 | 0.326 | 0.152 | 6.79 | 3.98 | 2.81 | 217 (25/192) | PROBABLE/CONFIRMED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-6h | 0.603 | 0.397 | 0.175 | 6.03 | 3.34 | 2.70 | 209 (25/184) | PROJECTED/PROJECTED |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-6h | 0.440 | 0.560 | 0.175 | 6.20 | 2.91 | 3.29 | 215 (25/190) | PROJECTED/PROJECTED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-6h | 0.444 | 0.556 | 0.176 | 6.20 | 2.93 | 3.27 | 218 (25/193) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB3 | team_total | 0.541 | 0.670 | 0.646 | 68 | 34 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB4 | team_total | 0.324 | 0.450 | 0.424 | 46 | 56 | no | +0.099 | OK |
| KXNHLGAME-26OCT13TBNYR-NYR | game_winner | 0.514 | 0.405 | 0.426 | 41 | 60 | yes | +0.087 | OK |
| KXNHLGAME-26OCT13TBNYR-TB | game_winner | 0.486 | 0.595 | 0.574 | 60 | 41 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB2 | game_spread | 0.262 | 0.365 | 0.343 | 37 | 64 | no | +0.082 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB3 | game_spread | 0.147 | 0.245 | 0.222 | 25 | 76 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB5 | team_total | 0.157 | 0.255 | 0.233 | 26 | 75 | no | +0.080 | OK |
| KXNHLTOTAL-26OCT13NJDET-7 | game_total | 0.356 | 0.455 | 0.435 | 46 | 55 | no | +0.077 | OK |
| KXNHLTOTAL-26OCT13NJDET-6 | game_total | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ3 | team_total | 0.499 | 0.590 | 0.572 | 60 | 42 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ4 | team_total | 0.290 | 0.375 | 0.357 | 38 | 63 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.286 | 0.205 | 0.220 | 21 | 80 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.767 | 0.850 | 0.836 | 86 | 16 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT13NJDET-5 | game_total | 0.705 | 0.785 | 0.770 | 79 | 22 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 | team_total | 0.302 | 0.385 | 0.368 | 39 | 62 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-5 | game_total | 0.698 | 0.775 | 0.761 | 78 | 23 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.523 | 0.605 | 0.589 | 61 | 40 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.403 | 0.485 | 0.468 | 49 | 52 | no | +0.060 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.326 | 0.405 | 0.389 | 41 | 60 | no | +0.057 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.674 | 0.595 | 0.611 | 60 | 41 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-6 | game_total | 0.466 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.533 | 0.455 | 0.471 | 46 | 55 | yes | +0.056 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ5 | team_total | 0.134 | 0.210 | 0.192 | 22 | 80 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-6 | game_total | 0.478 | 0.555 | 0.540 | 56 | 45 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-7 | game_total | 0.368 | 0.445 | 0.429 | 45 | 56 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13NJDET-8 | game_total | 0.182 | 0.255 | 0.239 | 26 | 75 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.461 | 0.385 | 0.400 | 39 | 62 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-4 | game_total | 0.798 | 0.865 | 0.853 | 87 | 14 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-7 | game_total | 0.359 | 0.435 | 0.420 | 44 | 57 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ2 | team_total | 0.737 | 0.810 | 0.797 | 82 | 20 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 | team_total | 0.401 | 0.475 | 0.460 | 48 | 53 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13NJDET-4 | game_total | 0.801 | 0.865 | 0.854 | 87 | 14 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.708 | 0.780 | 0.767 | 79 | 23 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.577 | 0.500 | 0.515 | 51 | 51 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.804 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.628 | 0.695 | 0.682 | 70 | 31 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI5 | team_total | 0.143 | 0.210 | 0.195 | 22 | 80 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.371 | 0.300 | 0.314 | 31 | 71 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-5 | game_total | 0.753 | 0.815 | 0.804 | 82 | 19 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI2 | team_total | 0.756 | 0.815 | 0.804 | 82 | 19 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL3 | team_total | 0.622 | 0.690 | 0.677 | 70 | 32 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.585 | 0.598 | 59 | 42 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT13NJDET-9 | game_total | 0.121 | 0.175 | 0.163 | 18 | 83 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ2 | game_spread | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-6 | game_total | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.763 | 0.815 | 0.805 | 82 | 19 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL5 | team_total | 0.220 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-7 | game_total | 0.427 | 0.485 | 0.473 | 49 | 52 | no | +0.036 | OK |
| KXNHLGAME-26OCT13STLOTT-OTT | game_winner | 0.448 | 0.505 | 0.493 | 51 | 50 | no | +0.035 | OK |
| KXNHLGAME-26OCT13STLOTT-STL | game_winner | 0.552 | 0.495 | 0.507 | 50 | 51 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.439 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT13PITCHI-6 | game_total | 0.550 | 0.605 | 0.594 | 61 | 40 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT3 | game_spread | 0.137 | 0.185 | 0.174 | 19 | 82 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT13TBNYR-8 | game_total | 0.195 | 0.250 | 0.238 | 26 | 76 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.459 | 0.405 | 0.416 | 41 | 60 | yes | +0.032 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.541 | 0.595 | 0.584 | 60 | 41 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.766 | 0.705 | 0.718 | 72 | 31 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL2 | team_total | 0.820 | 0.870 | 0.861 | 88 | 14 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB6 | team_total | 0.063 | 0.110 | 0.098 | 12 | 90 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.127 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR3 | game_spread | 0.169 | 0.125 | 0.133 | 13 | 88 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-DET | game_winner | 0.558 | 0.505 | 0.516 | 51 | 50 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-NJ | game_winner | 0.442 | 0.495 | 0.484 | 50 | 51 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT13CGYANA-ANA3 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.226 | 0.280 | 0.269 | 29 | 73 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.199 | 0.155 | 0.163 | 16 | 85 | yes | +0.030 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 0.558 | 0.545 | 0.188 | 0.224 | 5.64 | 5.77 | 0.994/0.984 | KXNHLTOTAL-26OCT13NJDET-7 +0.027 |
| FLA @ CBJ | 0.572 | 0.609 | 0.176 | 0.214 | 6.22 | 6.07 | 1.008/0.995 | KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3 -0.040 |
| BUF @ MTL | 0.546 | 0.553 | 0.180 | 0.216 | 6.06 | 6.27 | 0.983/0.997 | KXNHLTOTAL-26OCT13BUFMTL-7 +0.039 |
| WSH @ CAR | 0.587 | 0.577 | 0.174 | 0.215 | 6.04 | 6.34 | 1.000/0.949 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.049 |
| SEA @ PHI | 0.465 | 0.534 | 0.189 | 0.223 | 5.67 | 5.93 | 0.994/1.015 | KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 +0.080 |
| TBL @ NYR | 0.514 | 0.519 | 0.186 | 0.221 | 5.72 | 6.00 | 0.988/0.957 | KXNHLTOTAL-26OCT13TBNYR-7 +0.052 |
| STL @ OTT | 0.448 | 0.513 | 0.179 | 0.226 | 6.11 | 6.14 | 1.041/0.984 | KXNHLSPREAD-26OCT13STLOTT-STL2 -0.072 |
| VAN @ NYI | 0.661 | 0.593 | 0.160 | 0.210 | 6.30 | 6.26 | 0.947/1.030 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.076 |
| PIT @ CHI | 0.459 | 0.448 | 0.173 | 0.220 | 6.14 | 6.43 | 0.995/1.017 | KXNHLTOTAL-26OCT13PITCHI-7 +0.053 |
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.496 | 0.474 | 0.178 | 0.221 | 5.91 | 6.20 | 0.994/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.059 |
| VGK @ NSH | 0.533 | 0.507 | 0.171 | 0.217 | 6.49 | 6.20 | 1.002/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.054 |
| TOR @ UTA | 0.674 | 0.597 | 0.152 | 0.209 | 6.79 | 6.40 | 0.991/0.956 | KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 -0.092 |
| CGY @ ANA | 0.603 | 0.620 | 0.175 | 0.208 | 6.03 | 6.37 | 1.024/0.986 | KXNHLTOTAL-26OCT13CGYANA-7 +0.061 |
| EDM @ LAK | 0.440 | 0.478 | 0.175 | 0.216 | 6.20 | 6.23 | 0.993/0.994 | KXNHLGAME-26OCT13EDMLA-LA +0.038 |
| BOS @ SJS | 0.444 | 0.518 | 0.176 | 0.215 | 6.20 | 6.42 | 1.034/0.968 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 +0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 55 recommended · full analysis in card.md / packet.json `thesis_card`

- Timo Meier: 1+ goals NO @ 74c · p 0.7905 (adj 0.7766) · $3.39 · thesis NJD:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 71c · p 0.7617 (adj 0.7475) · $3.35 · thesis NJD:SUPPRESSED
- Viktor Arvidsson: 1+ assists NO @ 62c · p 0.7298 (adj 0.6519) · $2.12 · thesis DET:SUPPRESSED
- Dylan Larkin: 1+ assists NO @ 58c · p 0.659 (adj 0.6095) · $1.38 · thesis DET:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7554 (adj 0.7378) · $4.49 · thesis FLA:SUPPRESSED
- Sandis Vilmanis: 1+ goals YES @ 9c · p 0.1276 (adj 0.1169) · $1.27 · thesis FLA:OFFENSE_4PLUS
- Florida wins by over 1.5 goals NO @ 75c · p 0.8142 (adj 0.7796) · $3.67 · thesis CBJ:WINS
- Owen Power: 1+ goals NO @ 88c · p 0.9178 (adj 0.9058) · $3.9 · thesis BUF:SUPPRESSED
- Chris Kreider: 1+ goals NO @ 72c · p 0.7676 (adj 0.7544) · $3.65 · thesis MTL:SUPPRESSED
- Chris Kreider: 1+ assists NO @ 69c · p 0.761 (adj 0.723) · $3.09 · thesis MTL:SUPPRESSED
- Ethen Frank: 1+ goals YES @ 9c · p 0.1308 (adj 0.1193) · $1.34 · thesis WSH:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2239 (adj 0.2092) · $1.92 · thesis WSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ assists NO @ 53c · p 0.6591 (adj 0.5687) · $2.77 · thesis CAR:SUPPRESSED
- Bobby McMann: 1+ goals NO @ 71c · p 0.7802 (adj 0.7614) · $4.48 · thesis SEA:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.143 (adj 0.131) · $1.38 · thesis SEA:OFFENSE_4PLUS
- Porter Martone: 1+ goals NO @ 75c · p 0.8046 (adj 0.7897) · $4.48 · thesis PHI:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 23c · p 0.3172 (adj 0.2686) · $1.41 · thesis NYR:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8409 (adj 0.7979) · $3.9 · thesis NYR:WINS
- Tampa Bay over 4.5 goals scored NO @ 75c · p 0.8236 (adj 0.7843) · $2.71 · thesis TBL:SUPPRESSED
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.8417 (adj 0.7528) · $4.49 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 14c · p 0.1764 (adj 0.1648) · $1.0 · thesis OTT:OFFENSE_4PLUS
- Adam Jiricek: 1+ assists NO @ 67c · p 0.7804 (adj 0.7054) · $4.18 · thesis STL:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 14c · p 0.1852 (adj 0.1714) · $1.32 · thesis VAN:OFFENSE_4PLUS
- New York I wins by over 2.5 goals NO @ 69c · p 0.7595 (adj 0.7223) · $3.21 · thesis GAME:TIGHT
- Calum Ritchie: 1+ assists YES @ 26c · p 0.3268 (adj 0.2859) · $1.09 · thesis NYI:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 62c · p 0.6629 (adj 0.6497) · $1.67 · thesis NYI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 13c · p 0.217 (adj 0.1928) · $3.04 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 29c · p 0.3525 (adj 0.3356) · $2.64 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 53c · p 0.7033 (adj 0.5809) · $4.3 · thesis CHI:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1723 (adj 0.1592) · $1.25 · thesis PIT:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 86c · p 0.9322 (adj 0.9117) · $4.49 · thesis WPG:SUPPRESSED
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1353 (adj 0.1252) · $1.09 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 59c · p 0.6464 (adj 0.6298) · $3.96 · thesis MIN:SUPPRESSED
- Ryan Hartman: 1+ assists YES @ 23c · p 0.3052 (adj 0.2601) · $1.49 · thesis MIN:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 9c · p 0.1355 (adj 0.1216) · $1.42 · thesis COL:OFFENSE_4PLUS
- Parker Kelly: 1+ goals YES @ 9c · p 0.1267 (adj 0.1163) · $1.16 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 21c · p 0.256 (adj 0.242) · $1.38 · thesis COL:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 58c · p 0.6302 (adj 0.6164) · $2.7 · thesis COL:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 71c · p 0.7616 (adj 0.7462) · $3.29 · thesis VGK:SUPPRESSED
- Jack Eichel: 1+ goals NO @ 68c · p 0.7257 (adj 0.7118) · $2.22 · thesis VGK:SUPPRESSED
- Shea Theodore: 1+ assists YES @ 28c · p 0.3505 (adj 0.3103) · $1.47 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 53c · p 0.6003 (adj 0.5626) · $1.23 · thesis VGK:SUPPRESSED
- John Tavares: 1+ assists NO @ 63c · p 0.7058 (adj 0.6654) · $3.36 · thesis TOR:SUPPRESSED
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6552) · $2.76 · thesis UTA:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.7882 (adj 0.7211) · $3.43 · thesis UTA:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 24c · p 0.3101 (adj 0.2675) · $1.1 · thesis TOR:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1392 (adj 0.1219) · $1.39 · thesis ANA:OFFENSE_4PLUS
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9119 (adj 0.8635) · $4.06 · thesis LAK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6135 (adj 0.5235) · $2.07 · thesis LAK:SUPPRESSED
- Kasperi Kapanen: 1+ goals NO @ 79c · p 0.8293 (adj 0.8182) · $4.06 · thesis EDM:SUPPRESSED
- Kasperi Kapanen: 1+ assists YES @ 26c · p 0.3357 (adj 0.2903) · $1.03 · thesis EDM:OFFENSE_4PLUS
- Luca Cagnoni: 1+ assists NO @ 65c · p 0.7386 (adj 0.6918) · $4.49 · thesis SJS:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.1462 (adj 0.1346) · $1.07 · thesis BOS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.215 (adj 0.2) · $1.34 · thesis SJS:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 62c · p 0.6783 (adj 0.6612) · $3.88 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ DET** · priced 159/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 28.74, exp saves 25.15 (sd 6.61), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 27.87, exp saves 24.0 (sd 6.63), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Allen: 28+ saves | 0.287 | 0.460 | 48/56 | +0.135 |  |
| Jack Hughes: 2+ points | 0.192 | 0.330 | 34/68 | +0.113 | STANDARD |
| Jack Hughes: 1+ assists | 0.361 | 0.495 | 50/51 | +0.112 | STANDARD |
| Albert Johansson: 1+ assists | 0.194 | 0.070 | 12/98 | +0.067 | STANDARD |
| Luke Evangelista: 1+ points | 0.347 | 0.470 | 48/54 | +0.095 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.270 | 0.390 | 40/62 | +0.093 | STANDARD |

**FLA @ CBJ** · priced 156/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 26.31, exp saves 23.15 (sd 6.15), pull risk 0.041
- FLA net: Akira Schmid (PROBABLE) exp shots 28.0, exp saves 23.89 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Akira Schmid: 24+ saves | 0.526 | 0.275 | 53/98 | -0.021 |  |
| Brady Tkachuk: 1+ points | 0.420 | 0.560 | 57/45 | +0.113 | STANDARD |
| Cam Talbot: 25+ saves | 0.399 | 0.265 | 46/93 | -0.078 |  |
| Brady Tkachuk: 1+ assists | 0.241 | 0.375 | 39/64 | +0.103 | STANDARD |
| Sam Reinhart: 1+ points | 0.448 | 0.575 | 58/43 | +0.105 | STANDARD |
| Sam Reinhart: 1+ assists | 0.270 | 0.390 | 40/62 | +0.094 | STANDARD |

**BUF @ MTL** · priced 178/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.81, exp saves 25.17 (sd 6.76), pull risk 0.055
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.48, exp saves 21.86 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.655 | 0.415 | 49/66 | +0.147 |  |
| Peyton Krebs: 1+ points | 0.406 | 0.295 | 36/77 | +0.030 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.247 | 0.140 | 27/99 | -0.037 | STANDARD |
| Alexandre Carrier: 1+ assists | 0.220 | 0.120 | 22/98 | -0.012 | STANDARD |
| Peyton Krebs: 1+ assists | 0.300 | 0.200 | 27/87 | +0.016 | STANDARD |
| Chris Kreider: 1+ points | 0.415 | 0.510 | 52/50 | +0.067 | STANDARD |

**WSH @ CAR** · priced 181/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.49, exp saves 20.54 (sd 5.84), pull risk 0.051
- WSH net: Logan Thompson (PROBABLE) exp shots 31.11, exp saves 26.56 (sd 7.27), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.480 | 49/53 | +0.112 | STANDARD |
| Sebastian Aho: 2+ points | 0.178 | 0.275 | 29/74 | +0.068 | STANDARD |
| Sebastian Aho: 1+ points | 0.541 | 0.635 | 64/37 | +0.073 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.315 | 0.225 | 25/80 | +0.051 | STANDARD |
| Ryan Leonard: 1+ assists | 0.357 | 0.270 | 28/74 | +0.063 | STANDARD |
| Logan Thompson: 27+ saves | 0.505 | 0.420 | 51/67 | -0.022 |  |

**SEA @ PHI** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.23, exp saves 22.79 (sd 6.27), pull risk 0.05
- SEA net: Philipp Grubauer (PROJECTED) exp shots 26.94, exp saves 23.31 (sd 6.32), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dan Vladar: 24+ saves | 0.445 | 0.300 | 54/94 | -0.112 |  |
| Mackie Samoskevich: 1+ assists | 0.139 | 0.240 | 25/77 | +0.078 | STANDARD |
| Mackie Samoskevich: 1+ points | 0.308 | 0.405 | 41/60 | +0.075 | STANDARD |
| David Jiricek: 1+ points | 0.245 | 0.335 | 34/67 | +0.069 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.317 | 0.235 | 25/78 | +0.054 | STANDARD |
| Jared McCann: 1+ points | 0.444 | 0.525 | 54/49 | +0.049 | STANDARD |

**TBL @ NYR** · priced 182/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 27.72, exp saves 24.07 (sd 6.49), pull risk 0.056
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.07, exp saves 20.83 (sd 5.92), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.377 | 0.550 | 56/46 | +0.146 | STANDARD |
| John Carlson: 1+ assists | 0.296 | 0.460 | 47/55 | +0.137 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.471 | 0.605 | 61/40 | +0.112 | STANDARD |
| Nikita Kucherov: 2+ points | 0.276 | 0.405 | 41/60 | +0.107 | STANDARD |
| John Carlson: 2+ points | 0.078 | 0.195 | 21/82 | +0.092 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.367 | 0.265 | 27/74 | +0.083 | STANDARD |

**STL @ OTT** · priced 177/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.35, exp saves 21.19 (sd 5.86), pull risk 0.053
- STL net: Joel Hofer (PROBABLE) exp shots 28.14, exp saves 24.24 (sd 6.64), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ points | 0.291 | 0.445 | 46/57 | +0.122 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.158 | 0.295 | 30/71 | +0.117 | STANDARD |
| Adam Jiricek: 1+ points | 0.276 | 0.400 | 41/61 | +0.097 | PRIOR_HEAVY |
| Jordan Spence: 1+ points | 0.396 | 0.275 | 28/73 | +0.102 | STANDARD |
| Jordan Spence: 1+ assists | 0.336 | 0.220 | 24/80 | +0.083 | STANDARD |
| Adam Jiricek: 1+ assists | 0.220 | 0.335 | 34/67 | +0.095 | PRIOR_HEAVY |

**VAN @ NYI** · priced 158/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.73 (sd 6.02), pull risk 0.051
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.68, exp saves 25.33 (sd 6.96), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Emil Heineman: 1+ assists | 0.266 | 0.135 | 25/98 | +0.002 | STANDARD |
| Victor Eklund: 1+ assists | 0.215 | 0.340 | 35/67 | +0.100 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ points | 0.430 | 0.545 | 56/47 | +0.083 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.241 | 0.350 | 36/66 | +0.083 | STANDARD |
| Bo Horvat: 1+ points | 0.559 | 0.660 | 67/35 | +0.075 | STANDARD |
| Victor Eklund: 1+ points | 0.377 | 0.475 | 49/54 | +0.066 | PRIOR_HEAVY |

**PIT @ CHI** · priced 157/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 29.01, exp saves 24.82 (sd 6.96), pull risk 0.076
- PIT net: Sergei Murashov (PROBABLE) exp shots 25.04, exp saves 21.78 (sd 6.08), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.297 | 0.485 | 50/53 | +0.156 | STANDARD |
| Spencer Knight: 25+ saves | 0.515 | 0.335 | 54/87 | -0.042 |  |
| Patrick Kane: 1+ points | 0.496 | 0.630 | 64/38 | +0.107 | STANDARD |
| Patrick Kane: 2+ points | 0.142 | 0.275 | 30/75 | +0.095 | STANDARD |
| Anton Frondell: 1+ points | 0.569 | 0.440 | 45/57 | +0.101 | STANDARD |
| Anton Frondell: 1+ assists | 0.385 | 0.265 | 27/74 | +0.101 | STANDARD |

**MIN @ WPG** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.243 | 0.345 | 36/67 | +0.072 | STANDARD |
| Neal Pionk: 1+ points | 0.384 | 0.485 | 49/52 | +0.079 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.599 | 0.695 | 70/31 | +0.076 | STANDARD |
| Ryan Hartman: 1+ assists | 0.305 | 0.215 | 23/80 | +0.063 | STANDARD |
| Matt Boldy: 1+ points | 0.577 | 0.660 | 67/35 | +0.057 | STANDARD |
| Neal Pionk: 1+ goals | 0.068 | 0.150 | 16/86 | +0.064 | STANDARD |

**COL @ DAL** · priced 154/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Oettinger: 25+ saves | 0.517 | 0.370 | 51/77 | -0.011 |  |
| Roope Hintz: 1+ assists | 0.286 | 0.405 | 42/61 | +0.088 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.409 | 0.510 | 52/50 | +0.073 | STANDARD |
| Miro Heiskanen: 1+ points | 0.450 | 0.545 | 56/47 | +0.063 | STANDARD |
| Mikko Rantanen: 2+ points | 0.202 | 0.295 | 32/73 | +0.054 | STANDARD |
| Mikko Rantanen: 1+ points | 0.568 | 0.660 | 67/35 | +0.066 | STANDARD |

**VGK @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.216 | 0.350 | 36/66 | +0.108 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 1+ points | 0.583 | 0.705 | 72/31 | +0.092 | STANDARD |
| Adin Hill: 25+ saves | 0.374 | 0.255 | 50/99 | -0.144 |  |
| Roman Josi: 1+ assists | 0.435 | 0.535 | 54/47 | +0.077 | STANDARD |
| Mitch Marner: 1+ points | 0.539 | 0.625 | 63/38 | +0.065 | STANDARD |

**TOR @ UTA** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 25.03, exp saves 21.92 (sd 6.07), pull risk 0.052
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.85, exp saves 26.98 (sd 7.41), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.319 | 0.425 | 43/58 | +0.084 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.212 | 0.315 | 32/69 | +0.083 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.505 | 51/50 | +0.076 | STANDARD |
| Easton Cowan: 1+ points | 0.421 | 0.325 | 34/69 | +0.066 | STANDARD |
| Clayton Keller: 1+ assists | 0.464 | 0.555 | 56/45 | +0.068 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.283 | 0.370 | 38/64 | +0.060 | STANDARD |

**CGY @ ANA** · priced 152/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.29, exp saves 23.16 (sd 6.24), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 31.79, exp saves 26.81 (sd 7.5), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.271 | 0.155 | 17/86 | +0.091 | STANDARD |
| Alex Killorn: 1+ points | 0.555 | 0.440 | 45/57 | +0.087 | STANDARD |
| Alex Killorn: 1+ assists | 0.399 | 0.295 | 30/71 | +0.084 | STANDARD |
| Jeff Malott: 1+ goals | 0.139 | 0.070 | 9/95 | +0.043 | STANDARD |
| A.J. Greer: 1+ assists | 0.133 | 0.200 | 22/82 | +0.037 | STANDARD |
| Aydar Suniev: 1+ goals | 0.192 | 0.125 | 18/93 | +0.002 | PRIOR_HEAVY |

**EDM @ LAK** · priced 161/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.16, exp saves 24.36 (sd 6.7), pull risk 0.062
- EDM net: Devon Levi (PROJECTED) exp shots 27.62, exp saves 23.96 (sd 6.59), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.432 | 0.600 | 61/41 | +0.141 | STANDARD |
| Leon Draisaitl: 2+ points | 0.288 | 0.435 | 45/58 | +0.114 | STANDARD |
| Connor McDavid: 1+ assists | 0.491 | 0.635 | 64/37 | +0.122 | STANDARD |
| Artemi Panarin: 1+ assists | 0.387 | 0.525 | 53/48 | +0.116 | STANDARD |
| Connor McDavid: 2+ points | 0.349 | 0.480 | 49/53 | +0.104 | STANDARD |
| Trevor Moore: 1+ assists | 0.326 | 0.195 | 23/84 | +0.083 | STANDARD |

**BOS @ SJS** · priced 162/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 26.63, exp saves 22.97 (sd 6.47), pull risk 0.07
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.58, exp saves 23.81 (sd 6.56), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.385 | 0.550 | 56/46 | +0.138 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.292 | 0.455 | 46/55 | +0.140 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.192 | 0.315 | 32/69 | +0.103 | PRIOR_HEAVY |
| Luca Cagnoni: 1+ points | 0.312 | 0.425 | 44/59 | +0.081 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.336 | 0.225 | 24/79 | +0.083 | STANDARD |
| Charlie McAvoy: 2+ points | 0.086 | 0.195 | 21/82 | +0.084 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
