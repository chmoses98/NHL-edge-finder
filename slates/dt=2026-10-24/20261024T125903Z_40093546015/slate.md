# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T12:59:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4027 · contracts joined: 2131 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1831, 'OK': 154, 'NO_EDGE': 146}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 276, 'game_early_goal': 12, 'first_goal': 324, 'game_winner': 24, 'player_goals': 557, 'game_overtime': 12, 'player_points': 362, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 2026-10-24T17:00:00Z | T-3h | 0.500 | 0.500 | 0.177 | 5.94 | 2.97 | 2.98 | 209 (25/184) | PROJECTED/PROJECTED |
| LAK @ NJD | 2026-10-24T19:30:00Z | T-6h | 0.614 | 0.386 | 0.176 | 5.87 | 3.29 | 2.58 | 224 (25/199) | PROJECTED/PROJECTED |
| SJS @ BOS | 2026-10-24T23:00:00Z | T-6h | 0.660 | 0.340 | 0.159 | 6.52 | 3.80 | 2.72 | 230 (25/205) | PROJECTED/PROJECTED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-6h | 0.465 | 0.535 | 0.181 | 6.21 | 3.00 | 3.21 | 223 (25/198) | PROJECTED/PROJECTED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-6h | 0.571 | 0.429 | 0.171 | 6.68 | 3.58 | 3.10 | 199 (25/174) | PROJECTED/PROJECTED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-6h | 0.503 | 0.497 | 0.171 | 6.59 | 3.31 | 3.28 | 234 (25/209) | PROJECTED/PROJECTED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-6h | 0.482 | 0.518 | 0.179 | 6.00 | 2.94 | 3.07 | 217 (25/192) | PROJECTED/PROJECTED |
| CAR @ STL | 2026-10-24T23:00:00Z | T-6h | 0.503 | 0.497 | 0.180 | 6.21 | 3.10 | 3.10 | 212 (25/187) | PROJECTED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-6h | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 230 (25/205) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-12h | 0.553 | 0.447 | 0.175 | 6.07 | 3.20 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-12h | 0.520 | 0.480 | 0.188 | 5.73 | 2.92 | 2.80 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-12h | 0.518 | 0.482 | 0.182 | 6.11 | 3.11 | 3.00 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.518 | 0.405 | 0.427 | 41 | 60 | yes | +0.091 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.268 | 0.375 | 0.352 | 38 | 63 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.318 | 0.435 | 0.411 | 45 | 58 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.540 | 0.655 | 0.633 | 67 | 36 | no | +0.084 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.482 | 0.585 | 0.565 | 59 | 42 | no | +0.081 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.503 | 0.405 | 0.424 | 41 | 60 | yes | +0.076 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.520 | 0.425 | 0.444 | 43 | 58 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.145 | 0.235 | 0.214 | 24 | 77 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.156 | 0.245 | 0.225 | 25 | 76 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.363 | 0.465 | 0.444 | 48 | 55 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.536 | 0.625 | 0.608 | 63 | 38 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.753 | 0.835 | 0.820 | 84 | 17 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.257 | 0.345 | 0.326 | 35 | 66 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.764 | 0.845 | 0.831 | 85 | 16 | no | +0.067 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.497 | 0.585 | 0.568 | 59 | 42 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.427 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.297 | 0.215 | 0.230 | 22 | 79 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.154 | 0.245 | 0.224 | 26 | 77 | no | +0.064 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.480 | 0.565 | 0.548 | 57 | 44 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.282 | 0.365 | 0.348 | 37 | 64 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.587 | 0.675 | 0.658 | 69 | 34 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.170 | 0.245 | 0.228 | 25 | 76 | no | +0.058 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.535 | 0.455 | 0.471 | 46 | 55 | yes | +0.057 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.465 | 0.545 | 0.529 | 55 | 46 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.601 | 0.680 | 0.665 | 69 | 33 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.371 | 0.445 | 0.430 | 45 | 56 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.284 | 0.215 | 0.228 | 22 | 79 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.185 | 0.265 | 0.247 | 28 | 75 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.406 | 0.485 | 0.469 | 50 | 53 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.387 | 0.465 | 0.449 | 48 | 55 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY2 | game_spread | 0.288 | 0.225 | 0.237 | 23 | 78 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.222 | 0.295 | 0.279 | 31 | 72 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.242 | 0.310 | 0.296 | 32 | 70 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.714 | 0.780 | 0.768 | 79 | 23 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.481 | 0.550 | 0.536 | 56 | 46 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.843 | 0.895 | 0.886 | 90 | 11 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.313 | 0.255 | 0.266 | 26 | 75 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.257 | 0.315 | 0.303 | 32 | 69 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.627 | 0.690 | 0.678 | 70 | 32 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.807 | 0.855 | 0.846 | 86 | 15 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.061 | 0.110 | 0.098 | 12 | 90 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.168 | 0.220 | 0.209 | 23 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.607 | 0.550 | 0.562 | 56 | 46 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT24VGKCBJ-VGK3 | game_spread | 0.179 | 0.225 | 0.215 | 23 | 78 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.791 | 0.840 | 0.831 | 85 | 17 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.200 | 0.245 | 0.235 | 25 | 76 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT24LANJ-5 | game_total | 0.730 | 0.775 | 0.766 | 78 | 23 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.392 | 0.335 | 0.346 | 35 | 68 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK3 | team_total | 0.598 | 0.650 | 0.640 | 66 | 36 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.579 | 0.630 | 0.620 | 64 | 38 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.193 | 0.240 | 0.230 | 25 | 77 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.329 | 0.285 | 0.294 | 29 | 72 | yes | +0.025 | OK |
| KXNHLGAME-26OCT24VGKCBJ-CBJ | game_winner | 0.482 | 0.435 | 0.444 | 44 | 57 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR3 | team_total | 0.631 | 0.580 | 0.590 | 59 | 43 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 | team_total | 0.379 | 0.435 | 0.424 | 45 | 58 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-5 | game_total | 0.745 | 0.785 | 0.777 | 79 | 22 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6 | team_total | 0.081 | 0.120 | 0.111 | 13 | 89 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT24TOREDM-9 | game_total | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.170 | 0.135 | 0.141 | 14 | 87 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY3 | game_spread | 0.170 | 0.135 | 0.141 | 14 | 87 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR3 | game_spread | 0.190 | 0.155 | 0.162 | 16 | 85 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.130 | 0.170 | 0.161 | 18 | 84 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA6 | team_total | 0.102 | 0.140 | 0.131 | 15 | 87 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB3 | team_total | 0.553 | 0.605 | 0.595 | 62 | 41 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI2 | team_total | 0.789 | 0.825 | 0.818 | 83 | 18 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT24TOREDM-8 | game_total | 0.416 | 0.375 | 0.383 | 38 | 63 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL3 | team_total | 0.607 | 0.560 | 0.569 | 57 | 45 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.178 | 0.140 | 0.147 | 15 | 87 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.335 | 0.380 | 0.371 | 39 | 63 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5 | team_total | 0.209 | 0.165 | 0.173 | 18 | 85 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.209 | 0.260 | 0.249 | 28 | 76 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.178 | 0.145 | 0.151 | 15 | 86 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.240 | 0.205 | 0.212 | 21 | 80 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR6 | team_total | 0.102 | 0.070 | 0.076 | 8 | 94 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB2 | team_total | 0.772 | 0.810 | 0.803 | 82 | 20 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT24MINSEA-5 | game_total | 0.762 | 0.795 | 0.789 | 80 | 21 | no | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 0.500 | 0.528 | 0.177 | 0.218 | 5.94 | 6.14 | 0.991/1.024 | KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI3 +0.045 |
| LAK @ NJD | 0.614 | 0.551 | 0.176 | 0.218 | 5.87 | 5.80 | 0.973/0.992 | KXNHLGAME-26OCT24LANJ-LA +0.064 |
| SJS @ BOS | 0.660 | 0.603 | 0.159 | 0.213 | 6.52 | 6.57 | 0.968/1.034 | KXNHLSPREAD-26OCT24SJBOS-BOS2 -0.064 |
| NYR @ OTT | 0.465 | 0.540 | 0.181 | 0.221 | 6.21 | 6.25 | 1.050/0.992 | KXNHLGAME-26OCT24NYROTT-NYR -0.074 |
| NSH @ PIT | 0.571 | 0.583 | 0.171 | 0.207 | 6.68 | 6.58 | 1.033/1.000 | KXNHLTOTAL-26OCT24NSHPIT-6 -0.022 |
| BUF @ WSH | 0.503 | 0.542 | 0.171 | 0.213 | 6.59 | 6.44 | 0.992/0.997 | KXNHLTEAMTOTAL-26OCT24BUFWSH-BUF3 -0.039 |
| VGK @ CBJ | 0.482 | 0.489 | 0.179 | 0.224 | 6.00 | 6.02 | 0.964/1.003 | KXNHLTOTAL-26OCT24VGKCBJ-5 +0.014 |
| CAR @ STL | 0.503 | 0.517 | 0.180 | 0.219 | 6.21 | 6.50 | 0.993/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.054 |
| TOR @ EDM | 0.637 | 0.641 | 0.151 | 0.201 | 7.24 | 6.92 | 1.022/0.965 | KXNHLTOTAL-26OCT24TOREDM-8 -0.054 |
| TBL @ UTA | 0.553 | 0.569 | 0.175 | 0.213 | 6.07 | 6.30 | 0.992/0.957 | KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 +0.043 |
| DET @ CGY | 0.520 | 0.504 | 0.188 | 0.224 | 5.73 | 6.04 | 0.986/1.003 | KXNHLTOTAL-26OCT24DETCGY-7 +0.058 |
| MIN @ SEA | 0.518 | 0.514 | 0.182 | 0.223 | 6.11 | 6.34 | 1.015/0.995 | KXNHLTOTAL-26OCT24MINSEA-7 +0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 33 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 12c · p 0.1951 (adj 0.1738) · $6.11 · thesis ANA:OFFENSE_4PLUS
- Denver Barkey: 1+ goals YES @ 13c · p 0.1845 (adj 0.1696) · $4.37 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 14c · p 0.1838 (adj 0.1641) · $2.16 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 20c · p 0.2373 (adj 0.2255) · $2.45 · thesis PHI:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 63c · p 0.7006 (adj 0.6804) · $7.86 · thesis NJD:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 62c · p 0.7903 (adj 0.6666) · $7.86 · thesis NJD:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 67c · p 0.8179 (adj 0.712) · $7.86 · thesis LAK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 56c · p 0.6259 (adj 0.5904) · $2.61 · thesis LAK:SUPPRESSED
- Mark Kastelic: 1+ goals YES @ 11c · p 0.1413 (adj 0.1322) · $2.12 · thesis BOS:OFFENSE_4PLUS
- Tanner Jeannot: 1+ goals YES @ 8c · p 0.111 (adj 0.0958) · $1.28 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 66c · p 0.7348 (adj 0.6899) · $7.08 · thesis BOS:SUPPRESSED
- Pavel Zacha: 1+ goals YES @ 27c · p 0.32 (adj 0.2975) · $2.79 · thesis BOS:OFFENSE_4PLUS
- Gabe Perreault: 1+ goals YES @ 21c · p 0.257 (adj 0.2428) · $3.11 · thesis NYR:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3416 (adj 0.2933) · $2.88 · thesis NYR:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1103 (adj 0.0952) · $1.33 · thesis OTT:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 58c · p 0.7009 (adj 0.6126) · $5.84 · thesis OTT:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 63c · p 0.6931 (adj 0.6748) · $10.28 · thesis BUF:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 26c · p 0.3865 (adj 0.2945) · $3.31 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ assists NO @ 53c · p 0.6076 (adj 0.5638) · $3.69 · thesis BUF:SUPPRESSED
- Ivan Barbashev: 1+ goals YES @ 18c · p 0.2283 (adj 0.215) · $4.56 · thesis VGK:OFFENSE_4PLUS
- Jack Eichel: 1+ assists NO @ 42c · p 0.5677 (adj 0.4494) · $4.14 · thesis VGK:SUPPRESSED
- Mark Stone: 1+ assists NO @ 56c · p 0.62 (adj 0.5875) · $4.47 · thesis VGK:SUPPRESSED
- St. Louis wins by over 1.5 goals YES @ 22c · p 0.3056 (adj 0.2603) · $3.31 · thesis STL:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 76c · p 0.83 (adj 0.7925) · $7.86 · thesis STL:WINS
- St. Louis over 2.5 goals scored YES @ 57c · p 0.6551 (adj 0.6076) · $1.24 · thesis STL:OFFENSE_4PLUS
- Shayne Gostisbehere: 1+ assists NO @ 56c · p 0.6384 (adj 0.5892) · $1.89 · thesis CAR:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 63c · p 0.7022 (adj 0.6611) · $5.48 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ assists NO @ 57c · p 0.6419 (adj 0.601) · $4.17 · thesis TOR:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 38c · p 0.4855 (adj 0.4072) · $2.27 · thesis EDM:SUPPRESSED
- Detroit wins by over 2.5 goals NO @ 77c · p 0.8321 (adj 0.7985) · $9.69 · thesis CGY:WINS
- Detroit wins by over 1.5 goals NO @ 66c · p 0.7273 (adj 0.6911) · $1.31 · thesis CGY:WINS
- Seattle wins by over 1.5 goals YES @ 22c · p 0.3055 (adj 0.2602) · $3.35 · thesis SEA:WINS_BY_2PLUS
- Minnesota wins by over 2.5 goals NO @ 76c · p 0.8421 (adj 0.7985) · $10.47 · thesis SEA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ PHI** · priced 154/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 28.6, exp saves 24.89 (sd 6.7), pull risk 0.052
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.01, exp saves 21.54 (sd 6.12), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Sanheim: 1+ points | 0.444 | 0.345 | 37/68 | +0.058 | STANDARD |
| Denver Barkey: 1+ points | 0.469 | 0.375 | 41/66 | +0.043 | STANDARD |
| Travis Sanheim: 1+ assists | 0.363 | 0.270 | 29/75 | +0.059 | STANDARD |
| A.J. Greer: 1+ goals | 0.195 | 0.110 | 12/90 | +0.068 | STANDARD |
| Denver Barkey: 1+ assists | 0.349 | 0.265 | 29/76 | +0.045 | STANDARD |
| Noah Cates: 1+ goals | 0.164 | 0.080 | 14/98 | +0.016 | STANDARD |

**LAK @ NJD** · priced 168/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.53, exp saves 23.16 (sd 6.22), pull risk 0.045
- LAK net: Darcy Kuemper (PROJECTED) exp shots 30.31, exp saves 26.11 (sd 7.0), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.210 | 0.400 | 42/62 | +0.154 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.182 | 0.345 | 36/67 | +0.132 | STANDARD |
| Luke Evangelista: 1+ points | 0.371 | 0.525 | 55/50 | +0.112 | STANDARD |
| Mats Zuccarello: 1+ points | 0.332 | 0.455 | 49/58 | +0.071 | STANDARD |
| Jack Hughes: 2+ points | 0.215 | 0.335 | 35/68 | +0.089 | STANDARD |
| Jack Hughes: 1+ assists | 0.400 | 0.515 | 53/50 | +0.082 | STANDARD |

**SJS @ BOS** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.44, exp saves 23.96 (sd 6.5), pull risk 0.056
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.84, exp saves 23.59 (sd 6.67), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 1+ points | 0.693 | 0.530 | 74/68 | -0.060 | STANDARD |
| Jacob Trouba: 1+ assists | 0.283 | 0.145 | 27/98 | -0.001 | STANDARD |
| Michael Misa: 1+ goals | 0.199 | 0.095 | 17/98 | +0.019 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.412 | 0.515 | 52/49 | +0.080 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.418 | 0.520 | 53/49 | +0.074 | STANDARD |
| Pavel Zacha: 1+ goals | 0.320 | 0.230 | 27/81 | +0.036 | STANDARD |

**NYR @ OTT** · priced 168/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 23.91, exp saves 20.8 (sd 5.96), pull risk 0.059
- NYR net: Dylan Garand (PROJECTED) exp shots 29.38, exp saves 25.34 (sd 6.83), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.299 | 0.435 | 45/58 | +0.104 | STANDARD |
| Alexis Lafreniere: 2+ points | 0.232 | 0.120 | 22/98 | +0.000 | STANDARD |
| Jake Sanderson: 1+ points | 0.384 | 0.495 | 52/53 | +0.069 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.398 | 0.295 | 32/73 | +0.063 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.342 | 0.245 | 26/77 | +0.068 | STANDARD |
| Ridly Greig: 1+ goals | 0.206 | 0.110 | 18/96 | +0.016 | STANDARD |

**NSH @ PIT** · priced 147/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.07, exp saves 22.77 (sd 6.32), pull risk 0.057
- NSH net: Juuse Saros (PROJECTED) exp shots 29.45, exp saves 24.96 (sd 7.03), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 2+ points | 0.246 | 0.130 | 24/98 | -0.007 | STANDARD |
| Connor Dewar: 1+ goals | 0.180 | 0.080 | 14/98 | +0.032 | STANDARD |
| Matthew Wood: 1+ goals | 0.194 | 0.100 | 18/98 | +0.004 | STANDARD |
| Evgeni Malkin: 2+ points | 0.202 | 0.115 | 21/98 | -0.020 | STANDARD |
| Andrei Kuzmenko: 1+ goals | 0.190 | 0.110 | 20/98 | -0.021 | STANDARD |
| Erik Karlsson: 1+ goals | 0.175 | 0.095 | 17/98 | -0.005 | STANDARD |

**BUF @ WSH** · priced 169/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (PROJECTED) exp shots 28.16, exp saves 24.46 (sd 6.68), pull risk 0.058
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.97, exp saves 23.1 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Martin Fehervary: 1+ assists | 0.305 | 0.135 | 25/98 | +0.042 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.269 | 0.115 | 19/96 | +0.068 | STANDARD |
| Ryan Leonard: 1+ assists | 0.387 | 0.245 | 26/77 | +0.113 | STANDARD |
| Martin Fehervary: 1+ points | 0.344 | 0.210 | 30/88 | +0.030 | STANDARD |
| Dylan Strome: 2+ points | 0.238 | 0.115 | 21/98 | +0.016 | STANDARD |
| Ryan Leonard: 1+ points | 0.537 | 0.415 | 43/60 | +0.090 | STANDARD |

**VGK @ CBJ** · priced 157/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.34, exp saves 23.69 (sd 6.39), pull risk 0.056
- VGK net: Carter Hart (PROJECTED) exp shots 27.42, exp saves 23.78 (sd 6.35), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.432 | 0.590 | 60/42 | +0.131 | STANDARD |
| Jack Eichel: 2+ points | 0.231 | 0.360 | 39/67 | +0.083 | STANDARD |
| Charlie Coyle: 1+ goals | 0.251 | 0.130 | 22/96 | +0.019 | STANDARD |
| Zach Werenski: 1+ assists | 0.464 | 0.565 | 58/45 | +0.069 | STANDARD |
| Conor Garland: 1+ points | 0.350 | 0.255 | 37/86 | -0.036 | STANDARD |
| Charlie Coyle: 2+ points | 0.166 | 0.085 | 15/98 | +0.007 | STANDARD |

**CAR @ STL** · priced 158/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 30.19, exp saves 26.11 (sd 7.16), pull risk 0.067
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.39 (sd 5.89), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.543 | 0.330 | 63/97 | -0.103 | STANDARD |
| Jimmy Snuggerud: 1+ goals | 0.334 | 0.225 | 30/85 | +0.020 | STANDARD |
| Jimmy Snuggerud: 2+ points | 0.228 | 0.120 | 22/98 | -0.004 | STANDARD |
| Seth Jarvis: 1+ assists | 0.210 | 0.315 | 34/71 | +0.065 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.362 | 0.460 | 48/56 | +0.061 | STANDARD |
| Sebastian Aho: 1+ assists | 0.375 | 0.280 | 48/92 | -0.123 | STANDARD |

**TOR @ EDM** · priced 171/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Evan Bouchard: 1+ points | 0.713 | 0.560 | 71/59 | -0.011 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.228 | 0.105 | 19/98 | +0.027 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.514 | 0.635 | 65/38 | +0.089 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.420 | 44/60 | +0.081 | STANDARD |
| Connor Murphy: 1+ assists | 0.237 | 0.130 | 24/98 | -0.016 | STANDARD |
| Evan Bouchard: 2+ assists | 0.272 | 0.170 | 28/94 | -0.022 | STANDARD |

**TBL @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.29 (sd 6.31), pull risk 0.051
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.6, exp saves 22.8 (sd 6.42), pull risk 0.073

**DET @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 29.78, exp saves 25.84 (sd 6.79), pull risk 0.055
- DET net: Michal Postava (PROJECTED) exp shots 27.65, exp saves 23.91 (sd 6.64), pull risk 0.057

**MIN @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.27 (sd 6.92), pull risk 0.059
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.36, exp saves 23.53 (sd 6.49), pull risk 0.067

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
