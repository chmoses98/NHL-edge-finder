# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T16:34:43Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 16 · markets on board: 5402 · contracts joined: 3522 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 3122, 'OK': 218, 'NO_EDGE': 182}
families: {'period_winner': 144, 'period_spread': 96, 'period_total': 144, 'player_assists': 474, 'game_early_goal': 16, 'first_goal': 582, 'game_winner': 32, 'player_goals': 999, 'game_overtime': 16, 'player_points': 630, 'goalie_saves': 21, 'game_spread': 64, 'team_total': 160, 'game_total': 144}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 2026-10-13T22:00:00Z | T-3h | 0.558 | 0.442 | 0.188 | 5.64 | 2.99 | 2.65 | 225 (25/200) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-10-13T22:15:00Z | T-3h | 0.572 | 0.428 | 0.176 | 6.22 | 3.34 | 2.88 | 212 (25/187) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-13T22:30:00Z | T-3h | 0.546 | 0.454 | 0.180 | 6.06 | 3.17 | 2.89 | 211 (25/186) | CONFIRMED/PROJECTED |
| WSH @ CAR | 2026-10-13T22:45:00Z | T-6h | 0.594 | 0.406 | 0.166 | 6.12 | 3.35 | 2.77 | 245 (25/220) | PROBABLE/PROJECTED |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-6h | 0.465 | 0.535 | 0.189 | 5.67 | 2.73 | 2.94 | 226 (25/201) | CONFIRMED/PROJECTED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-6h | 0.514 | 0.486 | 0.186 | 5.72 | 2.91 | 2.81 | 234 (25/209) | CONFIRMED/PROBABLE |
| STL @ OTT | 2026-10-13T23:30:00Z | T-6h | 0.448 | 0.552 | 0.179 | 6.11 | 2.88 | 3.22 | 236 (25/211) | PROJECTED/PROBABLE |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-6h | 0.661 | 0.339 | 0.160 | 6.30 | 3.68 | 2.62 | 221 (25/196) | CONFIRMED/PROBABLE |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-6h | 0.459 | 0.541 | 0.177 | 6.14 | 2.94 | 3.21 | 220 (25/195) | PROBABLE/PROJECTED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-6h | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 207 (25/182) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-6h | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 210 (25/185) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-6h | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 216 (25/191) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-6h | 0.664 | 0.336 | 0.158 | 6.76 | 3.93 | 2.83 | 217 (25/192) | PROJECTED/PROJECTED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-6h | 0.603 | 0.397 | 0.175 | 6.03 | 3.34 | 2.70 | 209 (25/184) | PROJECTED/PROJECTED |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-6h | 0.440 | 0.560 | 0.175 | 6.20 | 2.91 | 3.29 | 215 (25/190) | PROJECTED/PROJECTED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-6h | 0.444 | 0.556 | 0.176 | 6.20 | 2.93 | 3.27 | 218 (25/193) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB3 | team_total | 0.541 | 0.665 | 0.641 | 67 | 34 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB4 | team_total | 0.324 | 0.445 | 0.420 | 45 | 56 | no | +0.099 | OK |
| KXNHLGAME-26OCT13TBNYR-NYR | game_winner | 0.514 | 0.405 | 0.426 | 41 | 60 | yes | +0.087 | OK |
| KXNHLGAME-26OCT13TBNYR-TB | game_winner | 0.486 | 0.595 | 0.574 | 60 | 41 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB2 | game_spread | 0.262 | 0.365 | 0.343 | 37 | 64 | no | +0.082 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB3 | game_spread | 0.147 | 0.245 | 0.222 | 25 | 76 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB5 | team_total | 0.157 | 0.255 | 0.233 | 26 | 75 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ3 | team_total | 0.499 | 0.595 | 0.576 | 60 | 41 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT13NJDET-7 | game_total | 0.356 | 0.445 | 0.427 | 45 | 56 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ5 | team_total | 0.134 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT13NJDET-6 | game_total | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ4 | team_total | 0.290 | 0.375 | 0.357 | 38 | 63 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.286 | 0.205 | 0.220 | 21 | 80 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.767 | 0.850 | 0.836 | 86 | 16 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT13NJDET-5 | game_total | 0.705 | 0.785 | 0.770 | 79 | 22 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 | team_total | 0.302 | 0.390 | 0.372 | 40 | 62 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-5 | game_total | 0.698 | 0.775 | 0.761 | 78 | 23 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.523 | 0.610 | 0.593 | 62 | 40 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-6 | game_total | 0.466 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.533 | 0.455 | 0.471 | 46 | 55 | yes | +0.056 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.407 | 0.485 | 0.469 | 49 | 52 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-6 | game_total | 0.478 | 0.555 | 0.540 | 56 | 45 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-7 | game_total | 0.368 | 0.445 | 0.429 | 45 | 56 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-4 | game_total | 0.798 | 0.865 | 0.853 | 87 | 14 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-7 | game_total | 0.359 | 0.435 | 0.420 | 44 | 57 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ2 | team_total | 0.737 | 0.810 | 0.797 | 82 | 20 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 | team_total | 0.401 | 0.475 | 0.460 | 48 | 53 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT13NJDET-4 | game_total | 0.801 | 0.865 | 0.854 | 87 | 14 | no | +0.051 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.336 | 0.405 | 0.391 | 41 | 60 | no | +0.048 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.664 | 0.595 | 0.609 | 60 | 41 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.804 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.564 | 0.495 | 0.509 | 50 | 51 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI5 | team_total | 0.143 | 0.210 | 0.195 | 22 | 80 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.629 | 0.695 | 0.682 | 70 | 31 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT13NJDET-8 | game_total | 0.182 | 0.245 | 0.231 | 25 | 76 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLGAME-26OCT13STLOTT-STL | game_winner | 0.552 | 0.485 | 0.499 | 49 | 52 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.452 | 0.385 | 0.398 | 39 | 62 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI2 | team_total | 0.756 | 0.820 | 0.808 | 83 | 19 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL3 | team_total | 0.622 | 0.690 | 0.677 | 70 | 32 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.585 | 0.598 | 59 | 42 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13NJDET-NJ2 | game_spread | 0.229 | 0.285 | 0.273 | 29 | 72 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-6 | game_total | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.763 | 0.815 | 0.805 | 82 | 19 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL5 | team_total | 0.220 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.760 | 0.700 | 0.713 | 71 | 31 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.361 | 0.300 | 0.312 | 31 | 71 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-7 | game_total | 0.427 | 0.485 | 0.473 | 49 | 52 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-5 | game_total | 0.753 | 0.810 | 0.800 | 82 | 20 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.437 | 0.495 | 0.483 | 50 | 51 | no | +0.035 | OK |
| KXNHLGAME-26OCT13STLOTT-OTT | game_winner | 0.448 | 0.505 | 0.493 | 51 | 50 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT13PITCHI-6 | game_total | 0.550 | 0.605 | 0.594 | 61 | 40 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.224 | 0.280 | 0.268 | 29 | 73 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT3 | game_spread | 0.137 | 0.185 | 0.174 | 19 | 82 | no | +0.033 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.459 | 0.405 | 0.416 | 41 | 60 | yes | +0.033 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.541 | 0.595 | 0.584 | 60 | 41 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT13TBNYR-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT13COLDAL-6 | game_total | 0.511 | 0.565 | 0.554 | 57 | 44 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.167 | 0.215 | 0.205 | 22 | 79 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL2 | team_total | 0.820 | 0.870 | 0.861 | 88 | 14 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB6 | team_total | 0.063 | 0.115 | 0.102 | 13 | 90 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.127 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR3 | game_spread | 0.169 | 0.125 | 0.133 | 13 | 88 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-DET | game_winner | 0.558 | 0.505 | 0.516 | 51 | 50 | yes | +0.031 | OK |
| KXNHLGAME-26OCT13NJDET-NJ | game_winner | 0.442 | 0.495 | 0.484 | 50 | 51 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT13CGYANA-ANA3 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.199 | 0.155 | 0.163 | 16 | 85 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT13NJDET-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 0.558 | 0.545 | 0.188 | 0.224 | 5.64 | 5.77 | 0.994/0.984 | KXNHLTOTAL-26OCT13NJDET-7 +0.027 |
| FLA @ CBJ | 0.572 | 0.609 | 0.176 | 0.214 | 6.22 | 6.07 | 1.008/0.995 | KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3 -0.040 |
| BUF @ MTL | 0.546 | 0.553 | 0.180 | 0.216 | 6.06 | 6.27 | 0.983/0.997 | KXNHLTOTAL-26OCT13BUFMTL-7 +0.039 |
| WSH @ CAR | 0.594 | 0.587 | 0.166 | 0.210 | 6.12 | 6.38 | 1.000/0.961 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.045 |
| SEA @ PHI | 0.465 | 0.534 | 0.189 | 0.223 | 5.67 | 5.93 | 0.994/1.015 | KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 +0.080 |
| TBL @ NYR | 0.514 | 0.514 | 0.186 | 0.223 | 5.72 | 5.98 | 0.988/0.952 | KXNHLTOTAL-26OCT13TBNYR-7 +0.053 |
| STL @ OTT | 0.448 | 0.513 | 0.179 | 0.226 | 6.11 | 6.14 | 1.041/0.984 | KXNHLSPREAD-26OCT13STLOTT-STL2 -0.072 |
| VAN @ NYI | 0.661 | 0.593 | 0.160 | 0.210 | 6.30 | 6.26 | 0.947/1.030 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.076 |
| PIT @ CHI | 0.459 | 0.449 | 0.177 | 0.223 | 6.14 | 6.45 | 0.995/1.021 | KXNHLTOTAL-26OCT13PITCHI-7 +0.058 |
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.496 | 0.474 | 0.178 | 0.221 | 5.91 | 6.20 | 0.994/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.059 |
| VGK @ NSH | 0.533 | 0.507 | 0.171 | 0.217 | 6.49 | 6.20 | 1.002/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.054 |
| TOR @ UTA | 0.664 | 0.607 | 0.158 | 0.212 | 6.76 | 6.47 | 0.992/0.979 | KXNHLSPREAD-26OCT13TORUTA-UTA2 -0.070 |
| CGY @ ANA | 0.603 | 0.620 | 0.175 | 0.208 | 6.03 | 6.37 | 1.024/0.986 | KXNHLTOTAL-26OCT13CGYANA-7 +0.061 |
| EDM @ LAK | 0.440 | 0.478 | 0.175 | 0.216 | 6.20 | 6.23 | 0.993/0.994 | KXNHLGAME-26OCT13EDMLA-LA +0.038 |
| BOS @ SJS | 0.444 | 0.518 | 0.176 | 0.215 | 6.20 | 6.42 | 1.034/0.968 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 +0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 53 recommended · full analysis in card.md / packet.json `thesis_card`

- Timo Meier: 1+ goals NO @ 74c · p 0.7905 (adj 0.7754) · $3.92 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 65c · p 0.7042 (adj 0.6894) · $3.26 · thesis NJD:SUPPRESSED
- Dylan Larkin: 1+ assists NO @ 58c · p 0.659 (adj 0.6095) · $1.79 · thesis DET:SUPPRESSED
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7089 (adj 0.6967) · $1.95 · thesis DET:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7554 (adj 0.7378) · $4.79 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 84c · p 0.8943 (adj 0.8646) · $4.79 · thesis CBJ:WINS
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2726 (adj 0.2595) · $1.14 · thesis CBJ:OFFENSE_4PLUS
- Owen Power: 1+ goals NO @ 88c · p 0.9206 (adj 0.908) · $4.79 · thesis BUF:SUPPRESSED
- Chris Kreider: 1+ assists NO @ 69c · p 0.7531 (adj 0.719) · $3.01 · thesis MTL:SUPPRESSED
- Nick Suzuki: 1+ assists NO @ 43c · p 0.4982 (adj 0.4616) · $1.48 · thesis MTL:SUPPRESSED
- Ethen Frank: 1+ goals YES @ 9c · p 0.129 (adj 0.1155) · $1.21 · thesis WSH:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2243 (adj 0.2045) · $1.77 · thesis WSH:OFFENSE_4PLUS
- Jordan Kyrou: 1+ assists NO @ 74c · p 0.7997 (adj 0.7673) · $4.79 · thesis WSH:SUPPRESSED
- Ryan Leonard: 1+ goals YES @ 18c · p 0.2139 (adj 0.2029) · $1.1 · thesis WSH:OFFENSE_4PLUS
- Bobby McMann: 1+ goals NO @ 71c · p 0.7802 (adj 0.7614) · $3.59 · thesis SEA:SUPPRESSED
- Jared McCann: 1+ goals NO @ 73c · p 0.7849 (adj 0.7674) · $3.59 · thesis SEA:SUPPRESSED
- Kaapo Kakko: 1+ assists YES @ 25c · p 0.3169 (adj 0.276) · $1.02 · thesis SEA:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 55c · p 0.7094 (adj 0.6025) · $4.65 · thesis TBL:SUPPRESSED
- New York R wins by over 1.5 goals YES @ 21c · p 0.291 (adj 0.248) · $1.02 · thesis NYR:WINS_BY_2PLUS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8376 (adj 0.7963) · $4.21 · thesis NYR:WINS
- Gabe Perreault: 1+ assists YES @ 21c · p 0.3134 (adj 0.2429) · $1.06 · thesis NYR:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.8417 (adj 0.7528) · $4.79 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 14c · p 0.1764 (adj 0.1648) · $1.12 · thesis OTT:OFFENSE_4PLUS
- Adam Jiricek: 1+ assists NO @ 67c · p 0.7804 (adj 0.7021) · $4.11 · thesis STL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 24c · p 0.279 (adj 0.2668) · $1.27 · thesis STL:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 14c · p 0.1848 (adj 0.1711) · $1.43 · thesis VAN:OFFENSE_4PLUS
- Calum Ritchie: 1+ goals NO @ 75c · p 0.7995 (adj 0.7859) · $4.19 · thesis NYI:SUPPRESSED
- Matias Maccelli: 1+ assists NO @ 65c · p 0.7333 (adj 0.6866) · $2.99 · thesis NYI:SUPPRESSED
- New York I wins by over 2.5 goals NO @ 69c · p 0.7595 (adj 0.7223) · $2.16 · thesis GAME:TIGHT
- Ryan Greene: 1+ goals YES @ 13c · p 0.2193 (adj 0.1945) · $3.28 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 53c · p 0.7069 (adj 0.5822) · $4.66 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 29c · p 0.3483 (adj 0.3325) · $2.51 · thesis CHI:OFFENSE_4PLUS
- Ryan Donato: 1+ goals YES @ 17c · p 0.2141 (adj 0.2006) · $1.39 · thesis CHI:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 86c · p 0.9322 (adj 0.9117) · $4.79 · thesis WPG:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 59c · p 0.6464 (adj 0.6298) · $4.22 · thesis MIN:SUPPRESSED
- Ryan Hartman: 1+ assists YES @ 23c · p 0.3052 (adj 0.2601) · $1.59 · thesis MIN:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 60c · p 0.6445 (adj 0.6296) · $2.04 · thesis COL:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 71c · p 0.7616 (adj 0.745) · $3.04 · thesis VGK:SUPPRESSED
- Jack Eichel: 1+ goals NO @ 68c · p 0.7257 (adj 0.7118) · $2.16 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ assists NO @ 53c · p 0.6003 (adj 0.5626) · $1.21 · thesis VGK:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.7818 (adj 0.7334) · $3.82 · thesis UTA:SUPPRESSED
- Dylan Guenther: 1+ goals NO @ 61c · p 0.6687 (adj 0.6528) · $3.02 · thesis UTA:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 63c · p 0.7172 (adj 0.6711) · $3.17 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ assists NO @ 57c · p 0.6485 (adj 0.6067) · $1.96 · thesis TOR:SUPPRESSED
- Alex Killorn: 1+ assists YES @ 30c · p 0.3663 (adj 0.3306) · $1.13 · thesis ANA:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 48c · p 0.6135 (adj 0.5235) · $3.17 · thesis LAK:SUPPRESSED
- Mattias Ekholm: 1+ assists YES @ 28c · p 0.3509 (adj 0.313) · $1.56 · thesis EDM:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 26c · p 0.3357 (adj 0.2903) · $1.34 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.5675 (adj 0.4456) · $2.24 · thesis EDM:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.1462 (adj 0.1359) · $1.24 · thesis BOS:OFFENSE_4PLUS
- Luca Cagnoni: 1+ assists NO @ 65c · p 0.7386 (adj 0.6918) · $4.79 · thesis SJS:SUPPRESSED
- David Pastrnak: 1+ goals NO @ 62c · p 0.6783 (adj 0.6612) · $4.1 · thesis BOS:SUPPRESSED
- Collin Graf: 1+ goals YES @ 14c · p 0.1772 (adj 0.1654) · $1.15 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ DET** · priced 151/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 28.74, exp saves 25.15 (sd 6.61), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 27.87, exp saves 24.0 (sd 6.63), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.361 | 0.500 | 51/51 | +0.112 | STANDARD |
| Jack Hughes: 2+ points | 0.192 | 0.330 | 34/68 | +0.113 | STANDARD |
| Jack Hughes: 1+ points | 0.548 | 0.675 | 68/33 | +0.107 | STANDARD |
| Luke Evangelista: 1+ points | 0.347 | 0.470 | 48/54 | +0.095 | STANDARD |
| Anthony Mantha: 1+ assists | 0.167 | 0.285 | 29/72 | +0.099 | STANDARD |
| Anthony Mantha: 1+ points | 0.325 | 0.440 | 45/57 | +0.088 | STANDARD |

**FLA @ CBJ** · priced 156/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 26.31, exp saves 23.15 (sd 6.15), pull risk 0.041
- FLA net: Akira Schmid (PROBABLE) exp shots 28.0, exp saves 23.89 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Akira Schmid: 24+ saves | 0.526 | 0.275 | 53/98 | -0.021 |  |
| Brady Tkachuk: 1+ points | 0.420 | 0.565 | 58/45 | +0.113 | STANDARD |
| Sam Reinhart: 1+ points | 0.448 | 0.585 | 60/43 | +0.105 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.241 | 0.370 | 38/64 | +0.103 | STANDARD |
| Sam Reinhart: 1+ assists | 0.270 | 0.390 | 40/62 | +0.094 | STANDARD |
| Charlie Coyle: 1+ points | 0.552 | 0.455 | 47/56 | +0.065 | STANDARD |

**BUF @ MTL** · priced 155/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.81, exp saves 25.11 (sd 6.84), pull risk 0.058
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.48, exp saves 21.86 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Norris: 1+ goals | 0.197 | 0.110 | 18/96 | +0.007 | STANDARD |
| Chris Kreider: 1+ points | 0.435 | 0.515 | 52/49 | +0.057 | STANDARD |
| Nick Suzuki: 1+ assists | 0.502 | 0.575 | 58/43 | +0.051 | STANDARD |
| Chris Kreider: 1+ assists | 0.247 | 0.315 | 32/69 | +0.048 | STANDARD |
| Ryan McLeod: 1+ goals | 0.158 | 0.090 | 14/96 | +0.010 | STANDARD |
| Chris Kreider: 2+ points | 0.109 | 0.175 | 19/84 | +0.041 | STANDARD |

**WSH @ CAR** · priced 183/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.49, exp saves 20.49 (sd 5.76), pull risk 0.052
- WSH net: Logan Thompson (PROJECTED) exp shots 31.11, exp saves 26.54 (sd 7.29), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.346 | 0.465 | 48/55 | +0.086 | STANDARD |
| Sebastian Aho: 2+ points | 0.188 | 0.285 | 31/74 | +0.058 | STANDARD |
| Sebastian Aho: 1+ points | 0.544 | 0.640 | 65/37 | +0.070 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.316 | 0.225 | 25/80 | +0.053 | STANDARD |
| Andrei Svechnikov: 1+ goals | 0.315 | 0.225 | 35/90 | -0.051 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.224 | 0.145 | 17/88 | +0.044 | STANDARD |

**SEA @ PHI** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.23, exp saves 22.79 (sd 6.27), pull risk 0.05
- SEA net: Philipp Grubauer (PROJECTED) exp shots 26.94, exp saves 23.31 (sd 6.32), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mackie Samoskevich: 1+ points | 0.308 | 0.415 | 43/60 | +0.075 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.139 | 0.240 | 25/77 | +0.078 | STANDARD |
| David Jiricek: 1+ points | 0.245 | 0.335 | 34/67 | +0.069 | STANDARD |
| Ryan Winterton: 1+ goals | 0.143 | 0.060 | 10/98 | +0.037 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.317 | 0.235 | 25/78 | +0.054 | STANDARD |
| Jared McCann: 1+ points | 0.444 | 0.525 | 54/49 | +0.049 | STANDARD |

**TBL @ NYR** · priced 177/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 27.72, exp saves 24.09 (sd 6.58), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.07, exp saves 20.81 (sd 5.88), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.374 | 0.540 | 55/47 | +0.139 | STANDARD |
| John Carlson: 1+ assists | 0.291 | 0.455 | 46/55 | +0.142 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.462 | 0.605 | 61/40 | +0.121 | STANDARD |
| Nikita Kucherov: 2+ points | 0.271 | 0.405 | 41/60 | +0.112 | STANDARD |
| John Carlson: 2+ points | 0.080 | 0.190 | 21/83 | +0.080 | STANDARD |
| Gabe Perreault: 1+ assists | 0.313 | 0.205 | 21/80 | +0.092 | STANDARD |

**STL @ OTT** · priced 177/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.35, exp saves 21.19 (sd 5.86), pull risk 0.053
- STL net: Joel Hofer (PROBABLE) exp shots 28.14, exp saves 24.24 (sd 6.64), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ points | 0.291 | 0.445 | 46/57 | +0.122 | STANDARD |
| Samuel Ersson: 20+ saves | 0.611 | 0.460 | 55/63 | +0.043 |  |
| Andre Burakovsky: 1+ assists | 0.158 | 0.295 | 30/71 | +0.117 | STANDARD |
| Adam Jiricek: 1+ points | 0.276 | 0.400 | 41/61 | +0.097 | PRIOR_HEAVY |
| Jordan Spence: 1+ points | 0.396 | 0.275 | 28/73 | +0.102 | STANDARD |
| Adam Jiricek: 1+ assists | 0.220 | 0.340 | 35/67 | +0.095 | PRIOR_HEAVY |

**VAN @ NYI** · priced 157/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.73 (sd 6.02), pull risk 0.051
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.68, exp saves 25.33 (sd 6.96), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ assists | 0.215 | 0.340 | 35/67 | +0.100 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ points | 0.430 | 0.550 | 57/47 | +0.083 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.241 | 0.350 | 36/66 | +0.083 | STANDARD |
| Bo Horvat: 1+ points | 0.559 | 0.660 | 67/35 | +0.075 | STANDARD |
| Victor Eklund: 1+ points | 0.377 | 0.475 | 49/54 | +0.066 | PRIOR_HEAVY |
| Matias Maccelli: 1+ assists | 0.267 | 0.360 | 37/65 | +0.067 | STANDARD |

**PIT @ CHI** · priced 157/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 29.01, exp saves 24.83 (sd 6.94), pull risk 0.076
- PIT net: Sergei Murashov (PROJECTED) exp shots 25.04, exp saves 21.72 (sd 6.14), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.293 | 0.485 | 50/53 | +0.159 | STANDARD |
| Patrick Kane: 1+ points | 0.496 | 0.630 | 64/38 | +0.107 | STANDARD |
| Anton Frondell: 1+ points | 0.566 | 0.440 | 45/57 | +0.099 | STANDARD |
| Patrick Kane: 2+ points | 0.148 | 0.265 | 29/76 | +0.079 | STANDARD |
| Anton Frondell: 1+ assists | 0.379 | 0.265 | 27/74 | +0.096 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.596 | 0.490 | 50/52 | +0.078 | STANDARD |

**MIN @ WPG** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Neal Pionk: 1+ points | 0.384 | 0.490 | 50/52 | +0.079 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.243 | 0.345 | 36/67 | +0.072 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.599 | 0.690 | 70/32 | +0.066 | STANDARD |
| Ryan Hartman: 1+ assists | 0.305 | 0.215 | 23/80 | +0.063 | STANDARD |
| Matt Boldy: 2+ points | 0.213 | 0.300 | 31/71 | +0.062 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.388 | 0.475 | 49/54 | +0.054 | STANDARD |

**COL @ DAL** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ points | 0.503 | 0.615 | 63/40 | +0.080 | STANDARD |
| Roope Hintz: 1+ assists | 0.286 | 0.395 | 41/62 | +0.078 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.276 | 0.380 | 39/63 | +0.078 | STANDARD |
| Miro Heiskanen: 1+ points | 0.450 | 0.545 | 56/47 | +0.063 | STANDARD |
| Cale Makar: 2+ points | 0.160 | 0.255 | 28/77 | +0.057 | STANDARD |
| Mikko Rantanen: 1+ points | 0.568 | 0.660 | 67/35 | +0.066 | STANDARD |

**VGK @ NSH** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.425 | 0.565 | 57/44 | +0.118 | STANDARD |
| Jack Eichel: 2+ points | 0.216 | 0.350 | 36/66 | +0.108 | STANDARD |
| Jack Eichel: 1+ points | 0.583 | 0.695 | 70/31 | +0.092 | STANDARD |
| Adin Hill: 25+ saves | 0.374 | 0.265 | 51/98 | -0.154 |  |
| Roman Josi: 1+ assists | 0.435 | 0.540 | 55/47 | +0.077 | STANDARD |
| Jack Eichel: 2+ assists | 0.107 | 0.195 | 22/83 | +0.053 | STANDARD |

**TOR @ UTA** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.03, exp saves 21.92 (sd 6.05), pull risk 0.052
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.85, exp saves 26.92 (sd 7.47), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.505 | 51/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.218 | 0.315 | 32/69 | +0.077 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.283 | 0.375 | 38/63 | +0.071 | STANDARD |
| Barrett Hayton: 1+ goals | 0.190 | 0.105 | 17/96 | +0.010 | STANDARD |
| Auston Matthews: 1+ assists | 0.351 | 0.435 | 44/57 | +0.061 | STANDARD |

**CGY @ ANA** · priced 155/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.29, exp saves 23.16 (sd 6.24), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 31.79, exp saves 26.81 (sd 7.5), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.258 | 0.090 | 16/98 | +0.088 | STANDARD |
| Jeff Malott: 1+ goals | 0.135 | 0.060 | 10/98 | +0.028 | STANDARD |
| Alex Killorn: 1+ assists | 0.366 | 0.295 | 30/71 | +0.052 | STANDARD |
| Tim Washe: 1+ goals | 0.150 | 0.085 | 12/95 | +0.023 | STANDARD |
| A.J. Greer: 1+ points | 0.368 | 0.310 | 32/70 | +0.033 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.278 | 0.220 | 24/80 | +0.025 | STANDARD |

**EDM @ LAK** · priced 161/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.16, exp saves 24.36 (sd 6.7), pull risk 0.062
- EDM net: Devon Levi (PROJECTED) exp shots 27.62, exp saves 23.96 (sd 6.59), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.432 | 0.595 | 60/41 | +0.141 | STANDARD |
| Leon Draisaitl: 2+ points | 0.288 | 0.440 | 45/57 | +0.124 | STANDARD |
| Connor McDavid: 1+ assists | 0.491 | 0.635 | 64/37 | +0.122 | STANDARD |
| Artemi Panarin: 1+ assists | 0.387 | 0.525 | 53/48 | +0.116 | STANDARD |
| Connor McDavid: 2+ points | 0.349 | 0.480 | 49/53 | +0.104 | STANDARD |
| Trevor Moore: 1+ assists | 0.326 | 0.195 | 23/84 | +0.083 | STANDARD |

**BOS @ SJS** · priced 162/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 26.63, exp saves 22.97 (sd 6.47), pull risk 0.07
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.58, exp saves 23.81 (sd 6.56), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.385 | 0.555 | 56/45 | +0.148 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.292 | 0.455 | 46/55 | +0.140 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.192 | 0.315 | 32/69 | +0.103 | PRIOR_HEAVY |
| Luca Cagnoni: 1+ points | 0.312 | 0.425 | 44/59 | +0.081 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.336 | 0.225 | 24/79 | +0.083 | STANDARD |
| Charlie McAvoy: 2+ points | 0.086 | 0.195 | 21/82 | +0.084 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
