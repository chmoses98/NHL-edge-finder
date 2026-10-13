# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T19:16:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 16 · markets on board: 5537 · contracts joined: 3657 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 3257, 'OK': 227, 'NO_EDGE': 173}
families: {'period_winner': 144, 'period_spread': 96, 'period_total': 144, 'player_assists': 529, 'game_early_goal': 16, 'first_goal': 581, 'game_winner': 32, 'player_goals': 996, 'game_overtime': 16, 'player_points': 707, 'goalie_saves': 28, 'game_spread': 64, 'team_total': 160, 'game_total': 144}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 2026-10-13T22:00:00Z | T-90m | 0.558 | 0.442 | 0.188 | 5.64 | 2.99 | 2.65 | 233 (25/208) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-10-13T22:15:00Z | T-90m | 0.572 | 0.428 | 0.176 | 6.22 | 3.34 | 2.88 | 215 (25/190) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-13T22:30:00Z | T-3h | 0.546 | 0.454 | 0.180 | 6.06 | 3.17 | 2.89 | 263 (25/238) | CONFIRMED/PROJECTED |
| WSH @ CAR | 2026-10-13T22:45:00Z | T-3h | 0.577 | 0.423 | 0.175 | 5.99 | 3.22 | 2.76 | 245 (25/220) | PROBABLE/CONFIRMED |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-3h | 0.465 | 0.535 | 0.189 | 5.67 | 2.73 | 2.94 | 258 (25/233) | CONFIRMED/PROJECTED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-3h | 0.514 | 0.486 | 0.186 | 5.72 | 2.91 | 2.81 | 239 (25/214) | CONFIRMED/PROBABLE |
| STL @ OTT | 2026-10-13T23:30:00Z | T-3h | 0.448 | 0.552 | 0.179 | 6.11 | 2.88 | 3.22 | 234 (25/209) | PROJECTED/PROBABLE |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-3h | 0.661 | 0.339 | 0.160 | 6.30 | 3.68 | 2.62 | 222 (25/197) | CONFIRMED/PROBABLE |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-3h | 0.459 | 0.541 | 0.178 | 6.15 | 2.94 | 3.21 | 209 (25/184) | PROBABLE/CONFIRMED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-3h | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 207 (25/182) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-3h | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 214 (25/189) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-3h | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 216 (25/191) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-3h | 0.674 | 0.326 | 0.152 | 6.79 | 3.98 | 2.81 | 225 (25/200) | PROBABLE/CONFIRMED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-6h | 0.645 | 0.355 | 0.171 | 6.36 | 3.64 | 2.72 | 211 (25/186) | CONFIRMED/PROBABLE |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-6h | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 216 (25/191) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-6h | 0.429 | 0.571 | 0.173 | 6.28 | 2.93 | 3.36 | 250 (25/225) | CONFIRMED/PROJECTED |

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
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ3 | team_total | 0.499 | 0.595 | 0.576 | 60 | 41 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT13NJDET-6 | game_total | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ4 | team_total | 0.290 | 0.375 | 0.357 | 38 | 63 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.286 | 0.205 | 0.220 | 21 | 80 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.767 | 0.850 | 0.836 | 86 | 16 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT13NJDET-5 | game_total | 0.705 | 0.785 | 0.770 | 79 | 22 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 | team_total | 0.302 | 0.385 | 0.368 | 39 | 62 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-5 | game_total | 0.698 | 0.775 | 0.761 | 78 | 23 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.523 | 0.605 | 0.589 | 61 | 40 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
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
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.408 | 0.485 | 0.469 | 49 | 52 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-7 | game_total | 0.359 | 0.435 | 0.420 | 44 | 57 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ2 | team_total | 0.737 | 0.810 | 0.797 | 82 | 20 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 | team_total | 0.401 | 0.475 | 0.460 | 48 | 53 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13NJDET-4 | game_total | 0.801 | 0.865 | 0.854 | 87 | 14 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.625 | 0.695 | 0.682 | 70 | 31 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.804 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI5 | team_total | 0.143 | 0.205 | 0.191 | 21 | 80 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-7 | game_total | 0.427 | 0.495 | 0.481 | 50 | 51 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI2 | team_total | 0.756 | 0.815 | 0.804 | 82 | 19 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-4 | game_total | 0.798 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL3 | team_total | 0.622 | 0.685 | 0.673 | 69 | 32 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT13NJDET-9 | game_total | 0.121 | 0.175 | 0.163 | 18 | 83 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.577 | 0.510 | 0.523 | 52 | 50 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ2 | game_spread | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-6 | game_total | 0.536 | 0.595 | 0.583 | 60 | 41 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.763 | 0.815 | 0.805 | 82 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.371 | 0.305 | 0.318 | 32 | 71 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL5 | team_total | 0.220 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT2 | team_total | 0.826 | 0.875 | 0.866 | 88 | 13 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-5 | game_total | 0.753 | 0.810 | 0.800 | 82 | 20 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-8 | game_total | 0.192 | 0.245 | 0.234 | 25 | 76 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-5 | game_total | 0.743 | 0.795 | 0.785 | 80 | 21 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-6 | game_total | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT3 | game_spread | 0.137 | 0.185 | 0.174 | 19 | 82 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.590 | 0.602 | 60 | 42 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT13TBNYR-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-4 | game_total | 0.830 | 0.875 | 0.867 | 88 | 13 | no | +0.032 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.459 | 0.405 | 0.416 | 41 | 60 | yes | +0.032 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.541 | 0.595 | 0.584 | 60 | 41 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.766 | 0.715 | 0.726 | 72 | 29 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.225 | 0.280 | 0.268 | 29 | 73 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB6 | team_total | 0.063 | 0.115 | 0.102 | 13 | 90 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.127 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR3 | game_spread | 0.169 | 0.125 | 0.133 | 13 | 88 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-DET | game_winner | 0.558 | 0.505 | 0.516 | 51 | 50 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-NJ | game_winner | 0.442 | 0.495 | 0.484 | 50 | 51 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT3 | game_spread | 0.197 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.199 | 0.155 | 0.163 | 16 | 85 | yes | +0.030 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 0.558 | 0.545 | 0.188 | 0.224 | 5.64 | 5.77 | 0.994/0.984 | KXNHLTOTAL-26OCT13NJDET-7 +0.027 |
| FLA @ CBJ | 0.572 | 0.609 | 0.176 | 0.214 | 6.22 | 6.07 | 1.008/0.995 | KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3 -0.040 |
| BUF @ MTL | 0.546 | 0.553 | 0.180 | 0.216 | 6.06 | 6.27 | 0.983/0.997 | KXNHLTOTAL-26OCT13BUFMTL-7 +0.039 |
| WSH @ CAR | 0.577 | 0.574 | 0.175 | 0.216 | 5.99 | 6.31 | 1.000/0.938 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.055 |
| SEA @ PHI | 0.465 | 0.534 | 0.189 | 0.223 | 5.67 | 5.93 | 0.994/1.015 | KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 +0.080 |
| TBL @ NYR | 0.514 | 0.519 | 0.186 | 0.221 | 5.72 | 6.00 | 0.988/0.957 | KXNHLTOTAL-26OCT13TBNYR-7 +0.052 |
| STL @ OTT | 0.448 | 0.513 | 0.179 | 0.226 | 6.11 | 6.14 | 1.041/0.984 | KXNHLSPREAD-26OCT13STLOTT-STL2 -0.072 |
| VAN @ NYI | 0.661 | 0.593 | 0.160 | 0.210 | 6.30 | 6.26 | 0.947/1.030 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.076 |
| PIT @ CHI | 0.459 | 0.445 | 0.178 | 0.212 | 6.15 | 6.41 | 0.995/1.012 | KXNHLTOTAL-26OCT13PITCHI-7 +0.047 |
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.496 | 0.474 | 0.178 | 0.221 | 5.91 | 6.20 | 0.994/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.059 |
| VGK @ NSH | 0.533 | 0.507 | 0.171 | 0.217 | 6.49 | 6.20 | 1.002/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.054 |
| TOR @ UTA | 0.674 | 0.597 | 0.152 | 0.209 | 6.79 | 6.40 | 0.991/0.956 | KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 -0.092 |
| CGY @ ANA | 0.645 | 0.631 | 0.171 | 0.210 | 6.36 | 6.41 | 1.016/1.002 | KXNHLTEAMTOTAL-26OCT13CGYANA-CGY2 +0.018 |
| EDM @ LAK | 0.440 | 0.480 | 0.173 | 0.218 | 6.27 | 6.25 | 0.995/0.994 | KXNHLSPREAD-26OCT13EDMLA-EDM2 -0.043 |
| BOS @ SJS | 0.429 | 0.515 | 0.173 | 0.216 | 6.28 | 6.45 | 1.039/0.968 | KXNHLGAME-26OCT13BOSSJ-BOS -0.086 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 56 recommended · full analysis in card.md / packet.json `thesis_card`

- Nico Hischier: 1+ goals NO @ 70c · p 0.7617 (adj 0.745) · $3.58 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 74c · p 0.7905 (adj 0.7766) · $3.58 · thesis NJD:SUPPRESSED
- Dylan Larkin: 1+ assists NO @ 59c · p 0.659 (adj 0.622) · $1.92 · thesis DET:SUPPRESSED
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7089 (adj 0.6979) · $1.94 · thesis DET:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7554 (adj 0.7378) · $4.78 · thesis FLA:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2093 (adj 0.1945) · $1.64 · thesis CBJ:OFFENSE_4PLUS
- Danton Heinen: 1+ goals YES @ 10c · p 0.1343 (adj 0.1245) · $1.1 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2726 (adj 0.2595) · $1.21 · thesis CBJ:OFFENSE_4PLUS
- Owen Power: 1+ goals NO @ 88c · p 0.9178 (adj 0.9058) · $4.78 · thesis BUF:SUPPRESSED
- Chris Kreider: 1+ goals NO @ 72c · p 0.7676 (adj 0.7544) · $4.75 · thesis MTL:SUPPRESSED
- Zach Benson: 1+ goals YES @ 21c · p 0.2495 (adj 0.2359) · $1.06 · thesis BUF:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2225 (adj 0.2081) · $1.88 · thesis WSH:OFFENSE_4PLUS
- Ethen Frank: 1+ goals YES @ 9c · p 0.1245 (adj 0.1146) · $1.12 · thesis WSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ assists NO @ 53c · p 0.6661 (adj 0.5744) · $3.74 · thesis CAR:SUPPRESSED
- Boone Jenner: 1+ goals YES @ 14c · p 0.1769 (adj 0.1664) · $1.18 · thesis WSH:OFFENSE_4PLUS
- Bobby McMann: 1+ goals NO @ 71c · p 0.7802 (adj 0.7614) · $4.78 · thesis SEA:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.143 (adj 0.131) · $1.51 · thesis SEA:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 16c · p 0.2018 (adj 0.1889) · $1.33 · thesis PHI:WINS_BY_2PLUS
- Porter Martone: 1+ goals NO @ 77c · p 0.8046 (adj 0.7947) · $3.46 · thesis PHI:SUPPRESSED
- New York R wins by over 1.5 goals YES @ 21c · p 0.2901 (adj 0.2476) · $1.1 · thesis NYR:WINS_BY_2PLUS
- Vladislav Gavrikov: 1+ assists YES @ 23c · p 0.3172 (adj 0.2686) · $1.67 · thesis NYR:OFFENSE_4PLUS
- Tampa Bay over 4.5 goals scored NO @ 75c · p 0.8236 (adj 0.7843) · $4.42 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 63c · p 0.6756 (adj 0.6629) · $1.65 · thesis TBL:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1764 (adj 0.1636) · $1.75 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.8417 (adj 0.7528) · $4.16 · thesis OTT:SUPPRESSED
- Tim Stutzle: 1+ assists NO @ 51c · p 0.6049 (adj 0.555) · $3.01 · thesis OTT:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 24c · p 0.279 (adj 0.268) · $1.2 · thesis STL:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1852 (adj 0.1701) · $2.06 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 10c · p 0.1338 (adj 0.1241) · $1.1 · thesis VAN:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 61c · p 0.6629 (adj 0.6484) · $3.46 · thesis NYI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 12c · p 0.1908 (adj 0.1719) · $2.73 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 52c · p 0.7125 (adj 0.5841) · $4.78 · thesis CHI:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1672 (adj 0.1554) · $1.12 · thesis PIT:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 86c · p 0.9322 (adj 0.9129) · $4.78 · thesis WPG:SUPPRESSED
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1353 (adj 0.1252) · $1.16 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 59c · p 0.6464 (adj 0.631) · $4.4 · thesis MIN:SUPPRESSED
- Ryan Hartman: 1+ assists YES @ 23c · p 0.3052 (adj 0.2601) · $1.6 · thesis MIN:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 9c · p 0.1355 (adj 0.1229) · $1.58 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 20c · p 0.256 (adj 0.2408) · $2.1 · thesis COL:OFFENSE_4PLUS
- Parker Kelly: 1+ goals YES @ 9c · p 0.1267 (adj 0.1163) · $1.25 · thesis COL:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 68c · p 0.7257 (adj 0.713) · $3.68 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 72c · p 0.7616 (adj 0.7487) · $3.44 · thesis VGK:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 70c · p 0.7882 (adj 0.7391) · $3.99 · thesis UTA:SUPPRESSED
- Dylan Guenther: 1+ goals NO @ 61c · p 0.6686 (adj 0.6527) · $3.17 · thesis UTA:SUPPRESSED
- John Tavares: 1+ assists NO @ 63c · p 0.7058 (adj 0.6629) · $2.84 · thesis TOR:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 24c · p 0.3101 (adj 0.2675) · $1.05 · thesis TOR:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1395 (adj 0.1246) · $1.7 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.149 (adj 0.1367) · $1.25 · thesis ANA:OFFENSE_4PLUS
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9098 (adj 0.8624) · $4.69 · thesis LAK:SUPPRESSED
- Andre Lee: 1+ goals YES @ 8c · p 0.1107 (adj 0.1018) · $1.02 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6128 (adj 0.5232) · $2.48 · thesis LAK:SUPPRESSED
- Mattias Ekholm: 1+ assists YES @ 28c · p 0.3533 (adj 0.3142) · $1.66 · thesis EDM:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2132 (adj 0.1961) · $2.16 · thesis SJS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 55c · p 0.7103 (adj 0.6029) · $4.26 · thesis BOS:SUPPRESSED
- Collin Graf: 1+ goals YES @ 14c · p 0.1819 (adj 0.1702) · $1.25 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.8162 (adj 0.7309) · $4.26 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ DET** · priced 162/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 28.74, exp saves 25.15 (sd 6.61), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 27.87, exp saves 24.0 (sd 6.63), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.361 | 0.505 | 51/50 | +0.122 | STANDARD |
| Jack Hughes: 2+ points | 0.192 | 0.325 | 33/68 | +0.113 | STANDARD |
| Jake Allen: 28+ saves | 0.287 | 0.415 | 43/60 | +0.096 |  |
| Luke Evangelista: 1+ assists | 0.202 | 0.330 | 34/68 | +0.102 | STANDARD |
| Albert Johansson: 1+ assists | 0.194 | 0.070 | 12/98 | +0.067 | STANDARD |
| Luke Evangelista: 1+ points | 0.347 | 0.470 | 48/54 | +0.095 | STANDARD |

**FLA @ CBJ** · priced 159/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 26.31, exp saves 23.15 (sd 6.15), pull risk 0.041
- FLA net: Akira Schmid (PROBABLE) exp shots 28.0, exp saves 23.89 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Akira Schmid: 24+ saves | 0.526 | 0.300 | 53/93 | -0.021 |  |
| Brady Tkachuk: 1+ points | 0.420 | 0.565 | 58/45 | +0.113 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.241 | 0.370 | 38/64 | +0.103 | STANDARD |
| Sam Reinhart: 1+ points | 0.448 | 0.575 | 58/43 | +0.105 | STANDARD |
| Sam Reinhart: 1+ assists | 0.270 | 0.395 | 40/61 | +0.104 | STANDARD |
| Sam Reinhart: 2+ points | 0.124 | 0.220 | 23/79 | +0.075 | STANDARD |

**BUF @ MTL** · priced 207/212 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.81, exp saves 25.17 (sd 6.76), pull risk 0.055
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.48, exp saves 21.86 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.655 | 0.455 | 47/56 | +0.167 |  |
| Mattias Samuelsson: 1+ assists | 0.256 | 0.145 | 26/97 | -0.017 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.247 | 0.145 | 27/98 | -0.037 | STANDARD |
| Chris Kreider: 1+ points | 0.415 | 0.515 | 53/50 | +0.067 | STANDARD |
| Alexandre Carrier: 1+ assists | 0.220 | 0.125 | 22/97 | -0.012 | STANDARD |
| Jake Evans: 1+ assists | 0.185 | 0.100 | 18/98 | -0.005 | STANDARD |

**WSH @ CAR** · priced 181/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.49, exp saves 20.51 (sd 5.8), pull risk 0.051
- WSH net: Logan Thompson (CONFIRMED) exp shots 31.11, exp saves 26.58 (sd 7.28), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.334 | 0.475 | 48/53 | +0.119 | STANDARD |
| Sebastian Aho: 1+ points | 0.527 | 0.635 | 64/37 | +0.087 | STANDARD |
| Sebastian Aho: 2+ points | 0.179 | 0.270 | 28/74 | +0.067 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.317 | 0.235 | 24/77 | +0.064 | STANDARD |
| Ryan Leonard: 1+ assists | 0.346 | 0.270 | 28/74 | +0.052 | STANDARD |
| Alex Ovechkin: 1+ points | 0.497 | 0.430 | 44/58 | +0.039 | STANDARD |

**SEA @ PHI** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.23, exp saves 22.79 (sd 6.27), pull risk 0.05
- SEA net: Philipp Grubauer (PROJECTED) exp shots 26.94, exp saves 23.31 (sd 6.32), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.203 | 0.490 | 96/98 | -0.184 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.297 | 0.490 | 97/99 | -0.287 | STANDARD |
| Adam Larsson: 1+ assists | 0.249 | 0.110 | 20/98 | +0.038 | STANDARD |
| David Jiricek: 1+ points | 0.245 | 0.370 | 38/64 | +0.099 | STANDARD |
| Ben Meyers: 1+ points | 0.242 | 0.125 | 24/99 | -0.011 | STANDARD |
| Nick Seeler: 1+ assists | 0.200 | 0.095 | 17/98 | +0.020 | STANDARD |

**TBL @ NYR** · priced 182/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 27.72, exp saves 24.07 (sd 6.49), pull risk 0.056
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.07, exp saves 20.83 (sd 5.92), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.377 | 0.550 | 56/46 | +0.146 | STANDARD |
| John Carlson: 1+ assists | 0.296 | 0.460 | 47/55 | +0.137 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.471 | 0.615 | 62/39 | +0.122 | STANDARD |
| Nikita Kucherov: 2+ points | 0.276 | 0.410 | 42/60 | +0.107 | STANDARD |
| John Carlson: 2+ points | 0.078 | 0.195 | 20/81 | +0.101 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.367 | 0.265 | 27/74 | +0.083 | STANDARD |

**STL @ OTT** · priced 177/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.35, exp saves 21.19 (sd 5.86), pull risk 0.053
- STL net: Joel Hofer (PROBABLE) exp shots 28.14, exp saves 24.24 (sd 6.64), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Samuel Ersson: 20+ saves | 0.611 | 0.445 | 55/66 | +0.043 |  |
| Andre Burakovsky: 1+ points | 0.291 | 0.430 | 44/58 | +0.112 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.158 | 0.295 | 30/71 | +0.117 | STANDARD |
| Jordan Spence: 1+ points | 0.396 | 0.275 | 28/73 | +0.102 | STANDARD |
| Jordan Spence: 1+ assists | 0.336 | 0.220 | 24/80 | +0.083 | STANDARD |
| Adam Jiricek: 1+ points | 0.276 | 0.390 | 40/62 | +0.088 | PRIOR_HEAVY |

**VAN @ NYI** · priced 158/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.73 (sd 6.02), pull risk 0.051
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.68, exp saves 25.33 (sd 6.96), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ assists | 0.215 | 0.340 | 35/67 | +0.100 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ assists | 0.241 | 0.350 | 36/66 | +0.083 | STANDARD |
| Kyle Palmieri: 1+ points | 0.430 | 0.535 | 55/48 | +0.073 | STANDARD |
| Victor Eklund: 1+ points | 0.377 | 0.480 | 49/53 | +0.075 | PRIOR_HEAVY |
| Bo Horvat: 1+ points | 0.559 | 0.660 | 67/35 | +0.075 | STANDARD |
| Bo Horvat: 1+ assists | 0.337 | 0.430 | 44/58 | +0.066 | STANDARD |

**PIT @ CHI** · priced 155/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 29.01, exp saves 24.86 (sd 6.92), pull risk 0.073
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.04, exp saves 21.76 (sd 6.12), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.287 | 0.485 | 49/52 | +0.175 | STANDARD |
| Patrick Kane: 1+ points | 0.471 | 0.635 | 65/38 | +0.133 | STANDARD |
| Patrick Kane: 2+ points | 0.136 | 0.265 | 28/75 | +0.101 | STANDARD |
| Evgeni Malkin: 1+ assists | 0.353 | 0.460 | 47/55 | +0.079 | STANDARD |
| Patrick Kane: 2+ assists | 0.047 | 0.140 | 15/87 | +0.075 | STANDARD |
| Evgeni Malkin: 1+ points | 0.512 | 0.605 | 62/41 | +0.061 | STANDARD |

**MIN @ WPG** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.243 | 0.340 | 35/67 | +0.072 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.599 | 0.695 | 70/31 | +0.076 | STANDARD |
| Ryan Hartman: 1+ assists | 0.305 | 0.215 | 23/80 | +0.063 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.388 | 0.475 | 49/54 | +0.054 | STANDARD |
| Calvin Pickard: 27+ saves | 0.361 | 0.280 | 51/95 | -0.166 |  |
| Neal Pionk: 1+ points | 0.384 | 0.465 | 48/55 | +0.049 | STANDARD |

**COL @ DAL** · priced 154/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.286 | 0.390 | 40/62 | +0.078 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.409 | 0.505 | 51/50 | +0.073 | STANDARD |
| Devon Toews: 1+ points | 0.403 | 0.495 | 50/51 | +0.069 | STANDARD |
| Artturi Lehkonen: 1+ points | 0.466 | 0.375 | 38/63 | +0.070 | STANDARD |
| Miro Heiskanen: 1+ points | 0.450 | 0.540 | 55/47 | +0.063 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.286 | 0.375 | 38/63 | +0.068 | STANDARD |

**VGK @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.216 | 0.350 | 36/66 | +0.108 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 1+ points | 0.583 | 0.695 | 70/31 | +0.092 | STANDARD |
| Adin Hill: 25+ saves | 0.374 | 0.270 | 47/93 | -0.114 |  |
| Roman Josi: 1+ assists | 0.435 | 0.525 | 53/48 | +0.067 | STANDARD |
| Jack Eichel: 2+ assists | 0.107 | 0.195 | 21/82 | +0.063 | STANDARD |

**TOR @ UTA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 25.03, exp saves 21.92 (sd 6.07), pull risk 0.052
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.85, exp saves 26.98 (sd 7.41), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.319 | 0.430 | 44/58 | +0.084 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.510 | 52/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.212 | 0.310 | 32/70 | +0.074 | STANDARD |
| Easton Cowan: 1+ points | 0.421 | 0.325 | 34/69 | +0.066 | STANDARD |
| Clayton Keller: 1+ assists | 0.464 | 0.555 | 56/45 | +0.068 | STANDARD |
| John Tavares: 1+ assists | 0.294 | 0.380 | 39/63 | +0.059 | STANDARD |

**CGY @ ANA** · priced 154/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 26.29, exp saves 23.15 (sd 6.3), pull risk 0.047
- CGY net: Dustin Wolf (PROBABLE) exp shots 31.79, exp saves 26.75 (sd 7.4), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.272 | 0.145 | 16/87 | +0.103 | STANDARD |
| Alex Killorn: 1+ points | 0.557 | 0.445 | 45/56 | +0.090 | STANDARD |
| Alex Killorn: 1+ assists | 0.399 | 0.295 | 30/71 | +0.084 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.565 | 0.485 | 49/52 | +0.058 | STANDARD |
| Alex Killorn: 2+ points | 0.199 | 0.125 | 14/89 | +0.051 | STANDARD |
| A.J. Greer: 1+ assists | 0.135 | 0.200 | 22/82 | +0.035 | STANDARD |

**EDM @ LAK** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 28.16, exp saves 24.3 (sd 6.72), pull risk 0.065
- EDM net: Devon Levi (CONFIRMED) exp shots 27.62, exp saves 23.94 (sd 6.59), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.435 | 0.595 | 60/41 | +0.138 | STANDARD |
| Connor McDavid: 1+ assists | 0.481 | 0.635 | 64/37 | +0.132 | STANDARD |
| Connor McDavid: 2+ points | 0.337 | 0.485 | 50/53 | +0.115 | STANDARD |
| Leon Draisaitl: 2+ points | 0.290 | 0.435 | 44/57 | +0.123 | STANDARD |
| Artemi Panarin: 1+ assists | 0.387 | 0.525 | 53/48 | +0.115 | STANDARD |
| Trevor Moore: 1+ assists | 0.325 | 0.190 | 22/84 | +0.093 | STANDARD |

**BOS @ SJS** · priced 192/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 26.63, exp saves 23.01 (sd 6.51), pull risk 0.069
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.58, exp saves 23.84 (sd 6.51), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.384 | 0.555 | 56/45 | +0.149 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.290 | 0.455 | 46/55 | +0.143 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.184 | 0.315 | 32/69 | +0.111 | PRIOR_HEAVY |
| Nikita Zadorov: 1+ assists | 0.233 | 0.105 | 19/98 | +0.033 | STANDARD |
| Ivar Stenberg: 1+ points | 0.325 | 0.440 | 45/57 | +0.088 | PRIOR_HEAVY |
| Tyler Toffoli: 1+ assists | 0.328 | 0.220 | 23/79 | +0.086 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
