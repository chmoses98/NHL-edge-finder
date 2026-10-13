# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T04:08:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 16 · markets on board: 2696 · contracts joined: 816 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 416, 'NO_EDGE': 167, 'OK': 233}
families: {'period_winner': 144, 'period_spread': 96, 'period_total': 144, 'game_early_goal': 16, 'game_winner': 32, 'game_overtime': 16, 'game_spread': 64, 'team_total': 160, 'game_total': 144}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 2026-10-13T22:00:00Z | T-12h | 0.516 | 0.484 | 0.188 | 5.73 | 2.91 | 2.82 | 51 (25/26) | PROJECTED/CONFIRMED |
| FLA @ CBJ | 2026-10-13T22:15:00Z | T-12h | 0.597 | 0.403 | 0.180 | 5.87 | 3.23 | 2.64 | 51 (25/26) | PROJECTED/PROJECTED |
| BUF @ MTL | 2026-10-13T22:30:00Z | T-12h | 0.506 | 0.494 | 0.172 | 6.11 | 3.08 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |
| WSH @ CAR | 2026-10-13T22:45:00Z | T-12h | 0.591 | 0.409 | 0.171 | 6.13 | 3.36 | 2.77 | 51 (25/26) | PROJECTED/PROJECTED |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-12h | 0.462 | 0.538 | 0.178 | 5.99 | 2.88 | 3.11 | 51 (25/26) | PROJECTED/PROJECTED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-12h | 0.516 | 0.484 | 0.181 | 5.82 | 2.96 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ OTT | 2026-10-13T23:30:00Z | T-12h | 0.576 | 0.424 | 0.169 | 6.48 | 3.48 | 3.00 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-12h | 0.642 | 0.358 | 0.164 | 6.34 | 3.63 | 2.72 | 51 (25/26) | PROJECTED/PROJECTED |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-12h | 0.477 | 0.523 | 0.175 | 6.29 | 3.07 | 3.22 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-12h | 0.508 | 0.492 | 0.178 | 6.16 | 3.12 | 3.04 | 51 (25/26) | PROJECTED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-12h | 0.489 | 0.511 | 0.187 | 5.97 | 2.96 | 3.01 | 51 (25/26) | PROJECTED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-12h | 0.490 | 0.510 | 0.175 | 6.51 | 3.23 | 3.28 | 51 (25/26) | PROJECTED/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-12h | 0.664 | 0.336 | 0.152 | 6.76 | 3.94 | 2.83 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-12h | 0.602 | 0.398 | 0.173 | 6.04 | 3.34 | 2.70 | 51 (25/26) | PROJECTED/PROJECTED |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-12h | 0.441 | 0.559 | 0.176 | 6.20 | 2.91 | 3.29 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-12h | 0.445 | 0.555 | 0.176 | 6.21 | 2.93 | 3.28 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT13TBNYR-NYR | game_winner | 0.516 | 0.395 | 0.419 | 40 | 61 | yes | +0.100 | OK |
| KXNHLGAME-26OCT13TBNYR-TB | game_winner | 0.484 | 0.595 | 0.573 | 60 | 41 | no | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB3 | team_total | 0.556 | 0.665 | 0.644 | 67 | 34 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB4 | team_total | 0.336 | 0.450 | 0.426 | 46 | 56 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB2 | game_spread | 0.268 | 0.375 | 0.352 | 38 | 63 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB3 | game_spread | 0.152 | 0.245 | 0.224 | 25 | 76 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 | team_total | 0.381 | 0.475 | 0.456 | 48 | 53 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB5 | team_total | 0.166 | 0.260 | 0.239 | 27 | 75 | no | +0.071 | OK |
| KXNHLGAME-26OCT13BUFMTL-BUF | game_winner | 0.494 | 0.405 | 0.422 | 41 | 60 | yes | +0.067 | OK |
| KXNHLGAME-26OCT13BUFMTL-MTL | game_winner | 0.506 | 0.595 | 0.578 | 60 | 41 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL3 | team_total | 0.601 | 0.690 | 0.673 | 70 | 32 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA3 | team_total | 0.492 | 0.580 | 0.563 | 59 | 43 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA4 | team_total | 0.284 | 0.375 | 0.356 | 39 | 64 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.567 | 0.480 | 0.498 | 49 | 53 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.774 | 0.855 | 0.841 | 87 | 16 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.288 | 0.210 | 0.224 | 22 | 80 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.452 | 0.375 | 0.390 | 38 | 63 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT13NJDET-6 | game_total | 0.479 | 0.555 | 0.540 | 56 | 45 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT13NJDET-5 | game_total | 0.714 | 0.785 | 0.772 | 79 | 22 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL3 | game_spread | 0.174 | 0.245 | 0.229 | 25 | 76 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL5 | team_total | 0.203 | 0.280 | 0.263 | 29 | 73 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT13NJDET-7 | game_total | 0.370 | 0.445 | 0.430 | 45 | 56 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-MTL2 | game_spread | 0.294 | 0.365 | 0.350 | 37 | 64 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT13STLOTT-6 | game_total | 0.605 | 0.535 | 0.549 | 54 | 47 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA2 | team_total | 0.730 | 0.805 | 0.791 | 82 | 21 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT13STLOTT-7 | game_total | 0.495 | 0.425 | 0.439 | 43 | 58 | yes | +0.048 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.336 | 0.405 | 0.391 | 41 | 60 | no | +0.048 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.664 | 0.595 | 0.609 | 60 | 41 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT13STLOTT-8 | game_total | 0.300 | 0.235 | 0.247 | 24 | 77 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13CGYANA-ANA3 | game_spread | 0.238 | 0.305 | 0.291 | 31 | 70 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-OTT3 | team_total | 0.683 | 0.605 | 0.621 | 62 | 41 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT13FLACBJ-FLA3 | game_spread | 0.105 | 0.165 | 0.151 | 17 | 84 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.760 | 0.690 | 0.705 | 70 | 32 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.317 | 0.250 | 0.263 | 26 | 76 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-OTT4 | team_total | 0.470 | 0.390 | 0.406 | 41 | 63 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT13NJDET-4 | game_total | 0.811 | 0.865 | 0.855 | 87 | 14 | no | +0.041 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.523 | 0.585 | 0.573 | 59 | 42 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA4 | team_total | 0.443 | 0.505 | 0.492 | 51 | 50 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ3 | team_total | 0.544 | 0.615 | 0.601 | 63 | 40 | no | +0.040 | OK |
| KXNHLGAME-26OCT13FLACBJ-CBJ | game_winner | 0.597 | 0.535 | 0.547 | 54 | 47 | yes | +0.039 | OK |
| KXNHLGAME-26OCT13FLACBJ-FLA | game_winner | 0.403 | 0.465 | 0.453 | 47 | 54 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.141 | 0.195 | 0.183 | 20 | 81 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.363 | 0.290 | 0.304 | 31 | 73 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT2 | game_spread | 0.353 | 0.295 | 0.306 | 30 | 71 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.170 | 0.225 | 0.213 | 23 | 78 | no | +0.038 | OK |
| KXNHLGAME-26OCT13BOSSJ-BOS | game_winner | 0.555 | 0.495 | 0.507 | 50 | 51 | yes | +0.038 | OK |
| KXNHLGAME-26OCT13BOSSJ-SJ | game_winner | 0.445 | 0.505 | 0.493 | 51 | 50 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT13FLACBJ-FLA5 | team_total | 0.132 | 0.190 | 0.177 | 20 | 82 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.143 | 0.195 | 0.184 | 20 | 81 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.815 | 0.865 | 0.856 | 87 | 14 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.722 | 0.780 | 0.769 | 79 | 23 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT13FLACBJ-FLA2 | game_spread | 0.201 | 0.255 | 0.243 | 26 | 75 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13STLOTT-9 | game_total | 0.215 | 0.165 | 0.174 | 17 | 84 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.240 | 0.295 | 0.283 | 30 | 71 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT13TBNYR-7 | game_total | 0.388 | 0.445 | 0.433 | 45 | 56 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT13BUFMTL-BUF2 | game_spread | 0.277 | 0.220 | 0.231 | 23 | 79 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL2 | team_total | 0.807 | 0.860 | 0.851 | 87 | 15 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.253 | 0.305 | 0.294 | 31 | 70 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA6 | team_total | 0.202 | 0.145 | 0.155 | 16 | 87 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT13TBNYR-6 | game_total | 0.500 | 0.555 | 0.544 | 56 | 45 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-OTT5 | team_total | 0.274 | 0.210 | 0.222 | 23 | 81 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.336 | 0.285 | 0.295 | 29 | 72 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.412 | 0.465 | 0.454 | 47 | 54 | no | +0.031 | OK |
| KXNHLGAME-26OCT13SEAPHI-PHI | game_winner | 0.462 | 0.515 | 0.504 | 52 | 49 | no | +0.031 | OK |
| KXNHLGAME-26OCT13SEAPHI-SEA | game_winner | 0.538 | 0.485 | 0.496 | 49 | 52 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13NJDET-NJ4 | team_total | 0.323 | 0.385 | 0.372 | 40 | 63 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT13NJDET-8 | game_total | 0.197 | 0.250 | 0.239 | 26 | 76 | no | +0.030 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.477 | 0.425 | 0.435 | 43 | 58 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.553 | 0.610 | 0.599 | 62 | 40 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-OTT6 | team_total | 0.136 | 0.090 | 0.098 | 10 | 92 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.092 | 0.135 | 0.125 | 14 | 87 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-7 | game_total | 0.433 | 0.485 | 0.475 | 49 | 52 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-SEA2 | game_spread | 0.313 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA5 | team_total | 0.246 | 0.300 | 0.289 | 31 | 71 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT13CGYANA-ANA2 | game_spread | 0.374 | 0.425 | 0.415 | 43 | 58 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT13BUFMTL-5 | game_total | 0.760 | 0.805 | 0.797 | 81 | 20 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT3 | game_spread | 0.189 | 0.235 | 0.225 | 24 | 77 | no | +0.029 | OK |
| KXNHLGAME-26OCT13STLOTT-STL | game_winner | 0.424 | 0.475 | 0.465 | 48 | 53 | no | +0.028 | OK |
| KXNHLGAME-26OCT13STLOTT-OTT | game_winner | 0.576 | 0.525 | 0.535 | 53 | 48 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB6 | team_total | 0.066 | 0.115 | 0.103 | 13 | 90 | no | +0.028 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ DET | 0.516 | 0.511 | 0.188 | 0.229 | 5.73 | 5.84 | 1.003/0.984 | KXNHLTOTAL-26OCT13NJDET-5 +0.021 |
| FLA @ CBJ | 0.597 | 0.597 | 0.180 | 0.219 | 5.87 | 5.99 | 0.964/0.998 | KXNHLTOTAL-26OCT13FLACBJ-7 +0.024 |
| BUF @ MTL | 0.506 | 0.535 | 0.172 | 0.215 | 6.11 | 6.24 | 0.976/0.997 | KXNHLTEAMTOTAL-26OCT13BUFMTL-MTL4 +0.039 |
| WSH @ CAR | 0.591 | 0.582 | 0.171 | 0.213 | 6.13 | 6.36 | 0.997/0.961 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.046 |
| SEA @ PHI | 0.462 | 0.528 | 0.178 | 0.228 | 5.99 | 5.89 | 0.992/1.005 | KXNHLGAME-26OCT13SEAPHI-PHI +0.067 |
| TBL @ NYR | 0.516 | 0.520 | 0.181 | 0.221 | 5.82 | 5.98 | 0.983/0.958 | KXNHLTOTAL-26OCT13TBNYR-5 +0.033 |
| STL @ OTT | 0.576 | 0.572 | 0.169 | 0.216 | 6.48 | 6.14 | 0.998/1.016 | KXNHLTOTAL-26OCT13STLOTT-6 -0.057 |
| VAN @ NYI | 0.642 | 0.583 | 0.164 | 0.221 | 6.34 | 6.24 | 0.956/1.021 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.066 |
| PIT @ CHI | 0.477 | 0.448 | 0.175 | 0.217 | 6.29 | 6.48 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 +0.048 |
| MIN @ WPG | 0.508 | 0.497 | 0.178 | 0.218 | 6.16 | 6.22 | 0.988/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN3 +0.022 |
| COL @ DAL | 0.489 | 0.475 | 0.187 | 0.213 | 5.97 | 6.17 | 0.986/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.040 |
| VGK @ NSH | 0.490 | 0.469 | 0.175 | 0.219 | 6.51 | 6.23 | 1.000/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.048 |
| TOR @ UTA | 0.664 | 0.609 | 0.152 | 0.209 | 6.76 | 6.46 | 0.992/0.979 | KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 -0.070 |
| CGY @ ANA | 0.602 | 0.614 | 0.173 | 0.216 | 6.04 | 6.38 | 1.035/0.986 | KXNHLTOTAL-26OCT13CGYANA-7 +0.062 |
| EDM @ LAK | 0.441 | 0.479 | 0.176 | 0.220 | 6.20 | 6.23 | 0.993/0.994 | KXNHLGAME-26OCT13EDMLA-LA +0.039 |
| BOS @ SJS | 0.445 | 0.517 | 0.176 | 0.212 | 6.21 | 6.40 | 1.034/0.968 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 +0.072 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 3.5 goals scored NO @ 14c · p 0.1834 (adj 0.1592) · $2.27 · thesis GAME:LOW_EVENT
- Florida wins by over 2.5 goals NO @ 84c · p 0.8861 (adj 0.8605) · $20.0 · thesis CBJ:WINS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8336 (adj 0.7943) · $17.97 · thesis NYR:WINS
- Tampa Bay over 4.5 goals scored NO @ 75c · p 0.8239 (adj 0.7819) · $9.87 · thesis NYR:WINS
- New York R wins by over 1.5 goals YES @ 22c · p 0.2905 (adj 0.2502) · $3.1 · thesis NYR:WINS_BY_2PLUS
- New York I wins by over 2.5 goals NO @ 69c · p 0.7568 (adj 0.7209) · $11.99 · thesis GAME:TIGHT
- New York I wins by over 1.5 goals NO @ 57c · p 0.6447 (adj 0.6024) · $2.58 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ DET** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 28.74, exp saves 25.03 (sd 6.65), pull risk 0.049
- NJD net: Jake Allen (CONFIRMED) exp shots 27.87, exp saves 24.15 (sd 6.53), pull risk 0.052

**FLA @ CBJ** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.31, exp saves 23.12 (sd 6.2), pull risk 0.044
- FLA net: Akira Schmid (PROJECTED) exp shots 28.0, exp saves 23.93 (sd 6.66), pull risk 0.07

**BUF @ MTL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.81, exp saves 25.1 (sd 6.7), pull risk 0.056
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.48, exp saves 21.88 (sd 6.25), pull risk 0.066

**WSH @ CAR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.49, exp saves 20.51 (sd 5.74), pull risk 0.051
- WSH net: Logan Thompson (PROJECTED) exp shots 31.11, exp saves 26.51 (sd 7.27), pull risk 0.081

**SEA @ PHI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- PHI net: Joseph Woll (PROJECTED) exp shots 26.23, exp saves 22.8 (sd 6.28), pull risk 0.049
- SEA net: Joey Daccord (PROJECTED) exp shots 26.94, exp saves 23.33 (sd 6.31), pull risk 0.053

**TBL @ NYR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYR net: Dylan Garand (PROJECTED) exp shots 27.72, exp saves 24.03 (sd 6.5), pull risk 0.057
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.07, exp saves 20.88 (sd 5.94), pull risk 0.058

**STL @ OTT** · priced 0/0 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.35, exp saves 21.35 (sd 5.92), pull risk 0.047
- STL net: Jordan Binnington (PROJECTED) exp shots 28.14, exp saves 24.05 (sd 6.72), pull risk 0.073

**VAN @ NYI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYI net: Ilya Sorokin (PROJECTED) exp shots 24.73, exp saves 21.75 (sd 5.9), pull risk 0.051
- VAN net: Kevin Lankinen (PROJECTED) exp shots 29.68, exp saves 25.36 (sd 6.94), pull risk 0.069

**PIT @ CHI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CHI net: Spencer Knight (PROJECTED) exp shots 29.01, exp saves 24.86 (sd 6.88), pull risk 0.075
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.04, exp saves 21.72 (sd 6.15), pull risk 0.061

**MIN @ WPG** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 28.08, exp saves 24.39 (sd 6.72), pull risk 0.061
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.36 (sd 6.51), pull risk 0.056

**COL @ DAL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DAL net: Jake Oettinger (PROJECTED) exp shots 28.74, exp saves 24.91 (sd 6.74), pull risk 0.06
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.09 (sd 6.09), pull risk 0.054

**VGK @ NSH** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 29.36, exp saves 25.46 (sd 6.87), pull risk 0.065
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.74 (sd 6.3), pull risk 0.056

**TOR @ UTA** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.03, exp saves 21.91 (sd 6.05), pull risk 0.053
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.85, exp saves 26.95 (sd 7.46), pull risk 0.085

**CGY @ ANA** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- ANA net: Ville Husso (PROJECTED) exp shots 26.29, exp saves 23.12 (sd 6.26), pull risk 0.048
- CGY net: Devin Cooley (PROJECTED) exp shots 31.79, exp saves 26.85 (sd 7.39), pull risk 0.086

**EDM @ LAK** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.16, exp saves 24.33 (sd 6.65), pull risk 0.063
- EDM net: Devon Levi (PROJECTED) exp shots 27.62, exp saves 23.98 (sd 6.5), pull risk 0.053

**BOS @ SJS** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 26.63, exp saves 23.01 (sd 6.42), pull risk 0.067
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.58, exp saves 23.81 (sd 6.57), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
