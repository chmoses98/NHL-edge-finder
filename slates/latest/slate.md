# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T13:49:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4244 · contracts joined: 2348 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2048, 'OK': 158, 'NO_EDGE': 142}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 325, 'game_early_goal': 12, 'first_goal': 361, 'game_winner': 24, 'player_goals': 623, 'game_overtime': 12, 'player_points': 426, 'game_spread': 48, 'team_total': 120, 'game_total': 108, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 2026-10-24T17:00:00Z | T-3h | 0.500 | 0.500 | 0.177 | 5.94 | 2.97 | 2.98 | 213 (25/188) | PROJECTED/PROJECTED |
| LAK @ NJD | 2026-10-24T19:30:00Z | T-3h | 0.614 | 0.386 | 0.176 | 5.87 | 3.29 | 2.58 | 227 (25/202) | PROJECTED/PROJECTED |
| SJS @ BOS | 2026-10-24T23:00:00Z | T-6h | 0.660 | 0.340 | 0.159 | 6.52 | 3.80 | 2.72 | 241 (25/216) | PROJECTED/PROJECTED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-6h | 0.465 | 0.535 | 0.181 | 6.21 | 3.00 | 3.21 | 226 (25/201) | PROJECTED/PROJECTED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-6h | 0.571 | 0.429 | 0.171 | 6.68 | 3.58 | 3.10 | 210 (25/185) | PROJECTED/PROJECTED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-6h | 0.503 | 0.497 | 0.171 | 6.59 | 3.31 | 3.28 | 234 (25/209) | PROJECTED/PROJECTED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-6h | 0.482 | 0.518 | 0.179 | 6.00 | 2.94 | 3.07 | 220 (25/195) | PROJECTED/PROJECTED |
| CAR @ STL | 2026-10-24T23:00:00Z | T-6h | 0.503 | 0.497 | 0.180 | 6.21 | 3.10 | 3.10 | 216 (25/191) | PROJECTED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-6h | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 234 (25/209) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-6h | 0.553 | 0.447 | 0.175 | 6.07 | 3.20 | 2.87 | 225 (25/200) | PROJECTED/PROJECTED |
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
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.536 | 0.630 | 0.612 | 64 | 38 | no | +0.068 | OK |
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
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.387 | 0.465 | 0.449 | 47 | 54 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.601 | 0.680 | 0.665 | 69 | 33 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.284 | 0.215 | 0.228 | 22 | 79 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.185 | 0.265 | 0.247 | 28 | 75 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.481 | 0.555 | 0.540 | 56 | 45 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.406 | 0.480 | 0.465 | 49 | 53 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY2 | game_spread | 0.288 | 0.225 | 0.237 | 23 | 78 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.222 | 0.295 | 0.279 | 31 | 72 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.242 | 0.315 | 0.299 | 33 | 70 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.714 | 0.780 | 0.768 | 79 | 23 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.371 | 0.440 | 0.426 | 45 | 57 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.843 | 0.895 | 0.886 | 90 | 11 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.313 | 0.255 | 0.266 | 26 | 75 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.257 | 0.315 | 0.303 | 32 | 69 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.627 | 0.690 | 0.678 | 70 | 32 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.807 | 0.855 | 0.846 | 86 | 15 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.061 | 0.110 | 0.098 | 12 | 90 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB3 | team_total | 0.553 | 0.605 | 0.595 | 61 | 40 | no | +0.031 | OK |
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
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR3 | team_total | 0.631 | 0.580 | 0.590 | 59 | 43 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 | team_total | 0.379 | 0.430 | 0.420 | 44 | 58 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-5 | game_total | 0.745 | 0.785 | 0.777 | 79 | 22 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6 | team_total | 0.081 | 0.120 | 0.111 | 13 | 89 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT24TOREDM-9 | game_total | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.170 | 0.135 | 0.141 | 14 | 87 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY3 | game_spread | 0.170 | 0.135 | 0.141 | 14 | 87 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR3 | game_spread | 0.190 | 0.155 | 0.162 | 16 | 85 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.130 | 0.170 | 0.161 | 18 | 84 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA6 | team_total | 0.102 | 0.140 | 0.131 | 15 | 87 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR4 | team_total | 0.407 | 0.365 | 0.373 | 37 | 64 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI2 | team_total | 0.789 | 0.825 | 0.818 | 83 | 18 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT24TOREDM-8 | game_total | 0.416 | 0.375 | 0.383 | 38 | 63 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL3 | team_total | 0.607 | 0.560 | 0.569 | 57 | 45 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.178 | 0.140 | 0.147 | 15 | 87 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.335 | 0.380 | 0.371 | 39 | 63 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5 | team_total | 0.209 | 0.165 | 0.173 | 18 | 85 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.209 | 0.260 | 0.249 | 28 | 76 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.178 | 0.145 | 0.151 | 15 | 86 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.240 | 0.205 | 0.212 | 21 | 80 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL4 | team_total | 0.384 | 0.345 | 0.353 | 35 | 66 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT24TOREDM-EDM5 | team_total | 0.405 | 0.365 | 0.373 | 37 | 64 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR6 | team_total | 0.102 | 0.070 | 0.076 | 8 | 94 | yes | +0.017 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 30 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 12c · p 0.1951 (adj 0.1751) · $7.03 · thesis ANA:OFFENSE_4PLUS
- Denver Barkey: 1+ goals YES @ 14c · p 0.1845 (adj 0.1721) · $3.75 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 19c · p 0.2373 (adj 0.2217) · $3.75 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 14c · p 0.1838 (adj 0.1653) · $2.63 · thesis PHI:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 3c · p 0.0583 (adj 0.05) · $1.81 · thesis LAK:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 66c · p 0.8179 (adj 0.712) · $10.22 · thesis LAK:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 63c · p 0.7006 (adj 0.6792) · $10.22 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 75c · p 0.786 (adj 0.7758) · $6.81 · thesis NJD:SUPPRESSED
- Pavel Zacha: 1+ goals YES @ 27c · p 0.32 (adj 0.3063) · $4.44 · thesis BOS:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 11c · p 0.1413 (adj 0.1322) · $2.38 · thesis BOS:OFFENSE_4PLUS
- Macklin Celebrini: 1+ goals YES @ 35c · p 0.3934 (adj 0.3813) · $3.41 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 19c · p 0.223 (adj 0.2135) · $2.18 · thesis SJS:OFFENSE_4PLUS
- Gabe Perreault: 1+ goals YES @ 21c · p 0.257 (adj 0.2428) · $3.78 · thesis NYR:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1103 (adj 0.0952) · $1.39 · thesis OTT:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 63c · p 0.6931 (adj 0.6748) · $11.63 · thesis BUF:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 26c · p 0.3865 (adj 0.2945) · $3.67 · thesis WSH:OFFENSE_4PLUS
- Jack Eichel: 1+ assists NO @ 42c · p 0.5677 (adj 0.4494) · $2.85 · thesis VGK:SUPPRESSED
- Mark Stone: 1+ assists NO @ 56c · p 0.62 (adj 0.5875) · $3.05 · thesis VGK:SUPPRESSED
- St. Louis wins by over 1.5 goals YES @ 22c · p 0.3056 (adj 0.2603) · $3.29 · thesis STL:WINS_BY_2PLUS
- Robert Thomas: 1+ goals YES @ 23c · p 0.2898 (adj 0.2661) · $3.34 · thesis STL:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 76c · p 0.83 (adj 0.7925) · $8.07 · thesis STL:WINS
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7274 (adj 0.7118) · $5.76 · thesis CAR:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 63c · p 0.7022 (adj 0.6611) · $6.1 · thesis TOR:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 38c · p 0.4855 (adj 0.4104) · $3.27 · thesis EDM:SUPPRESSED
- Auston Matthews: 1+ assists NO @ 57c · p 0.6419 (adj 0.601) · $4.64 · thesis TOR:SUPPRESSED
- Anthony Cirelli: 1+ goals YES @ 17c · p 0.2156 (adj 0.193) · $2.12 · thesis TBL:OFFENSE_4PLUS
- Detroit wins by over 2.5 goals NO @ 77c · p 0.8321 (adj 0.7985) · $10.75 · thesis CGY:WINS
- Detroit wins by over 1.5 goals NO @ 66c · p 0.7273 (adj 0.6911) · $1.46 · thesis CGY:WINS
- Seattle wins by over 1.5 goals YES @ 22c · p 0.3055 (adj 0.2602) · $3.71 · thesis SEA:WINS_BY_2PLUS
- Minnesota wins by over 2.5 goals NO @ 76c · p 0.8421 (adj 0.7985) · $11.63 · thesis SEA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ PHI** · priced 158/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 28.6, exp saves 24.89 (sd 6.7), pull risk 0.052
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.01, exp saves 21.54 (sd 6.12), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tristan Luneau: 1+ points | 0.321 | 0.200 | 37/97 | -0.066 | STANDARD |
| Travis Sanheim: 1+ points | 0.444 | 0.340 | 36/68 | +0.068 | STANDARD |
| Travis Sanheim: 1+ assists | 0.363 | 0.265 | 28/75 | +0.069 | STANDARD |
| Tristan Luneau: 1+ assists | 0.260 | 0.165 | 31/98 | -0.065 | STANDARD |
| Denver Barkey: 1+ points | 0.469 | 0.375 | 40/65 | +0.053 | STANDARD |
| Denver Barkey: 1+ assists | 0.349 | 0.260 | 28/76 | +0.055 | STANDARD |

**LAK @ NJD** · priced 171/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.53, exp saves 23.16 (sd 6.22), pull risk 0.045
- LAK net: Darcy Kuemper (PROJECTED) exp shots 30.31, exp saves 26.11 (sd 7.0), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.210 | 0.400 | 42/62 | +0.154 | STANDARD |
| Connor Brown: 1+ points | 0.384 | 0.220 | 41/97 | -0.043 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.182 | 0.345 | 35/66 | +0.142 | STANDARD |
| Luke Evangelista: 1+ points | 0.371 | 0.525 | 55/50 | +0.112 | STANDARD |
| Jack Hughes: 2+ points | 0.215 | 0.340 | 36/68 | +0.089 | STANDARD |
| Jack Hughes: 1+ assists | 0.400 | 0.515 | 53/50 | +0.082 | STANDARD |

**SJS @ BOS** · priced 186/190 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.44, exp saves 23.96 (sd 6.5), pull risk 0.056
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.84, exp saves 23.59 (sd 6.67), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.412 | 0.515 | 52/49 | +0.080 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.310 | 0.210 | 24/82 | +0.057 | STANDARD |
| David Pastrnak: 1+ points | 0.693 | 0.595 | 73/54 | -0.051 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.418 | 0.515 | 53/50 | +0.064 | STANDARD |
| Michael Misa: 1+ goals | 0.199 | 0.110 | 16/94 | +0.029 | STANDARD |
| Tyler Toffoli: 1+ points | 0.464 | 0.380 | 40/64 | +0.047 | STANDARD |

**NYR @ OTT** · priced 171/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 23.91, exp saves 20.8 (sd 5.96), pull risk 0.059
- NYR net: Dylan Garand (PROJECTED) exp shots 29.38, exp saves 25.34 (sd 6.83), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.299 | 0.430 | 45/59 | +0.094 | STANDARD |
| Alexis Lafreniere: 2+ points | 0.232 | 0.120 | 22/98 | +0.000 | STANDARD |
| Jake Sanderson: 1+ points | 0.384 | 0.495 | 52/53 | +0.069 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.398 | 0.295 | 32/73 | +0.063 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.342 | 0.240 | 26/78 | +0.068 | STANDARD |
| Warren Foegele: 1+ goals | 0.193 | 0.100 | 18/98 | +0.003 | STANDARD |

**NSH @ PIT** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.07, exp saves 22.77 (sd 6.32), pull risk 0.057
- NSH net: Juuse Saros (PROJECTED) exp shots 29.45, exp saves 24.96 (sd 7.03), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kris Letang: 1+ points | 0.384 | 0.220 | 42/98 | -0.053 | STANDARD |
| Ville Koivunen: 1+ points | 0.403 | 0.245 | 47/98 | -0.084 | STANDARD |
| Kris Letang: 1+ assists | 0.334 | 0.180 | 34/98 | -0.022 | STANDARD |
| Rickard Rakell: 2+ points | 0.246 | 0.130 | 24/98 | -0.007 | STANDARD |
| Ville Koivunen: 1+ assists | 0.290 | 0.175 | 33/98 | -0.056 | STANDARD |
| Connor Dewar: 1+ goals | 0.180 | 0.080 | 14/98 | +0.032 | STANDARD |

**BUF @ WSH** · priced 169/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (PROJECTED) exp shots 28.16, exp saves 24.46 (sd 6.68), pull risk 0.058
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.97, exp saves 23.1 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.269 | 0.115 | 19/96 | +0.068 | STANDARD |
| Ryan Leonard: 1+ assists | 0.387 | 0.245 | 26/77 | +0.113 | STANDARD |
| Dylan Strome: 2+ points | 0.238 | 0.115 | 21/98 | +0.016 | STANDARD |
| Ryan Leonard: 1+ points | 0.537 | 0.425 | 44/59 | +0.080 | STANDARD |
| Boone Jenner: 1+ goals | 0.217 | 0.105 | 17/96 | +0.037 | STANDARD |
| Ryan Leonard: 2+ points | 0.182 | 0.075 | 13/98 | +0.044 | STANDARD |

**VGK @ CBJ** · priced 160/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.34, exp saves 23.69 (sd 6.39), pull risk 0.056
- VGK net: Carter Hart (PROJECTED) exp shots 27.42, exp saves 23.78 (sd 6.35), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Damon Severson: 1+ points | 0.412 | 0.195 | 37/98 | +0.026 | STANDARD |
| Damon Severson: 1+ assists | 0.338 | 0.165 | 31/98 | +0.013 | STANDARD |
| Jack Eichel: 1+ assists | 0.432 | 0.590 | 60/42 | +0.131 | STANDARD |
| Jack Eichel: 2+ points | 0.231 | 0.370 | 39/65 | +0.103 | STANDARD |
| Zach Werenski: 1+ assists | 0.464 | 0.565 | 58/45 | +0.069 | STANDARD |
| Charlie Coyle: 1+ goals | 0.251 | 0.160 | 22/90 | +0.019 | STANDARD |

**CAR @ STL** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 30.19, exp saves 26.11 (sd 7.16), pull risk 0.067
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.39 (sd 5.89), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cam Fowler: 1+ points | 0.338 | 0.195 | 37/98 | -0.049 | STANDARD |
| Cam Fowler: 1+ assists | 0.302 | 0.170 | 32/98 | -0.033 | STANDARD |
| Sebastian Aho: 1+ assists | 0.375 | 0.485 | 49/52 | +0.088 | STANDARD |
| Jimmy Snuggerud: 2+ points | 0.228 | 0.120 | 22/98 | -0.004 | STANDARD |
| Seth Jarvis: 1+ assists | 0.210 | 0.315 | 34/71 | +0.065 | STANDARD |
| Robert Thomas: 1+ goals | 0.290 | 0.195 | 23/84 | +0.047 | STANDARD |

**TOR @ EDM** · priced 175/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kasperi Kapanen: 1+ points | 0.446 | 0.230 | 44/98 | -0.011 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.338 | 0.140 | 27/99 | +0.055 | STANDARD |
| Evan Bouchard: 1+ points | 0.713 | 0.530 | 71/65 | -0.011 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.514 | 0.630 | 64/38 | +0.089 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.415 | 43/60 | +0.081 | STANDARD |
| Ryan Nugent-Hopkins: 1+ points | 0.470 | 0.575 | 60/45 | +0.062 | STANDARD |

**TBL @ UTA** · priced 166/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.29 (sd 6.31), pull risk 0.051
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.6, exp saves 22.8 (sd 6.42), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.639 | 0.510 | 74/72 | -0.114 | STANDARD |
| Clayton Keller: 1+ points | 0.600 | 0.475 | 72/77 | -0.134 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.217 | 0.340 | 36/68 | +0.088 | STANDARD |
| Anthony Cirelli: 1+ goals | 0.216 | 0.125 | 17/92 | +0.036 | STANDARD |
| Brayden Point: 2+ points | 0.204 | 0.115 | 21/98 | -0.018 | STANDARD |
| Brandon Hagel: 2+ points | 0.239 | 0.150 | 28/98 | -0.055 | STANDARD |

**DET @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 29.78, exp saves 25.84 (sd 6.79), pull risk 0.055
- DET net: Michal Postava (PROJECTED) exp shots 27.65, exp saves 23.91 (sd 6.64), pull risk 0.057

**MIN @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.27 (sd 6.92), pull risk 0.059
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.36, exp saves 23.53 (sd 6.49), pull risk 0.067

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
