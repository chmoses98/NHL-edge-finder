# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T15:46:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4581 · contracts joined: 2685 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2385, 'NO_EDGE': 148, 'OK': 152}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 381, 'game_early_goal': 12, 'first_goal': 435, 'game_winner': 24, 'player_goals': 749, 'game_overtime': 12, 'player_points': 504, 'goalie_saves': 4, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 2026-10-24T17:00:00Z | T-60m | 0.496 | 0.504 | 0.184 | 5.96 | 2.96 | 3.00 | 214 (25/189) | CONFIRMED/PROJECTED |
| LAK @ NJD | 2026-10-24T19:30:00Z | T-3h | 0.614 | 0.386 | 0.176 | 5.87 | 3.29 | 2.58 | 214 (25/189) | PROJECTED/PROJECTED |
| SJS @ BOS | 2026-10-24T23:00:00Z | T-6h | 0.682 | 0.318 | 0.153 | 6.40 | 3.80 | 2.60 | 242 (25/217) | CONFIRMED/PROJECTED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-6h | 0.471 | 0.529 | 0.179 | 6.09 | 2.95 | 3.14 | 228 (25/203) | CONFIRMED/CONFIRMED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-6h | 0.568 | 0.432 | 0.170 | 6.71 | 3.58 | 3.13 | 210 (25/185) | PROBABLE/PROJECTED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-6h | 0.492 | 0.508 | 0.171 | 6.62 | 3.29 | 3.33 | 235 (25/210) | CONFIRMED/PROBABLE |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-6h | 0.416 | 0.584 | 0.168 | 6.46 | 2.96 | 3.50 | 225 (25/200) | CONFIRMED/PROBABLE |
| CAR @ STL | 2026-10-24T23:00:00Z | T-6h | 0.503 | 0.497 | 0.180 | 6.21 | 3.10 | 3.10 | 216 (25/191) | PROJECTED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-6h | 0.637 | 0.363 | 0.151 | 7.24 | 4.10 | 3.14 | 234 (25/209) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-6h | 0.559 | 0.441 | 0.176 | 6.08 | 3.21 | 2.87 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-6h | 0.520 | 0.480 | 0.188 | 5.73 | 2.92 | 2.80 | 229 (25/204) | PROJECTED/PROJECTED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-6h | 0.518 | 0.482 | 0.182 | 6.11 | 3.11 | 3.00 | 213 (25/188) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.540 | 0.655 | 0.633 | 66 | 35 | no | +0.094 | OK |
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.518 | 0.405 | 0.427 | 41 | 60 | yes | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.318 | 0.430 | 0.407 | 44 | 58 | no | +0.085 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.482 | 0.585 | 0.565 | 59 | 42 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.268 | 0.365 | 0.344 | 37 | 64 | no | +0.076 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.145 | 0.235 | 0.214 | 24 | 77 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.156 | 0.245 | 0.225 | 25 | 76 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.363 | 0.460 | 0.440 | 47 | 55 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.751 | 0.835 | 0.820 | 84 | 17 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.257 | 0.345 | 0.326 | 35 | 66 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.764 | 0.850 | 0.835 | 86 | 16 | no | +0.067 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.497 | 0.585 | 0.568 | 59 | 42 | no | +0.066 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.503 | 0.410 | 0.428 | 42 | 60 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.297 | 0.215 | 0.230 | 22 | 79 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.154 | 0.240 | 0.221 | 25 | 77 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.429 | 0.515 | 0.498 | 52 | 49 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.541 | 0.630 | 0.613 | 64 | 38 | no | +0.063 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.520 | 0.435 | 0.452 | 44 | 57 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.282 | 0.365 | 0.348 | 37 | 64 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.587 | 0.675 | 0.658 | 69 | 34 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.170 | 0.250 | 0.232 | 26 | 76 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.387 | 0.465 | 0.449 | 47 | 54 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.714 | 0.785 | 0.772 | 79 | 22 | no | +0.054 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.480 | 0.555 | 0.540 | 56 | 45 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.185 | 0.265 | 0.247 | 28 | 75 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.481 | 0.555 | 0.540 | 56 | 45 | no | +0.052 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.529 | 0.455 | 0.470 | 46 | 55 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY2 | game_spread | 0.288 | 0.225 | 0.237 | 23 | 78 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.601 | 0.675 | 0.661 | 69 | 34 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.224 | 0.295 | 0.280 | 31 | 72 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.841 | 0.900 | 0.890 | 91 | 11 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.284 | 0.220 | 0.232 | 23 | 79 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.148 | 0.205 | 0.192 | 21 | 80 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.245 | 0.310 | 0.296 | 32 | 70 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB4 | team_total | 0.335 | 0.395 | 0.383 | 40 | 61 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.170 | 0.225 | 0.213 | 23 | 78 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.311 | 0.255 | 0.266 | 26 | 75 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.392 | 0.330 | 0.342 | 34 | 68 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-8 | game_total | 0.299 | 0.245 | 0.255 | 25 | 76 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.260 | 0.315 | 0.303 | 32 | 69 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.193 | 0.245 | 0.234 | 25 | 76 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.807 | 0.860 | 0.850 | 87 | 15 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.571 | 0.630 | 0.618 | 64 | 38 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.410 | 0.465 | 0.454 | 47 | 54 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.809 | 0.865 | 0.855 | 88 | 15 | no | +0.032 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.471 | 0.525 | 0.514 | 53 | 48 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.353 | 0.410 | 0.398 | 42 | 60 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.334 | 0.285 | 0.295 | 29 | 72 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL3 | team_total | 0.607 | 0.550 | 0.562 | 56 | 46 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.178 | 0.135 | 0.143 | 14 | 87 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.209 | 0.265 | 0.253 | 28 | 75 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-7 | game_total | 0.532 | 0.485 | 0.494 | 49 | 52 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-7 | game_total | 0.492 | 0.445 | 0.454 | 45 | 56 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT2 | team_total | 0.785 | 0.830 | 0.822 | 84 | 18 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.061 | 0.105 | 0.094 | 12 | 91 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-9 | game_total | 0.214 | 0.175 | 0.182 | 18 | 83 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-9 | game_total | 0.244 | 0.205 | 0.212 | 21 | 80 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6 | team_total | 0.081 | 0.130 | 0.118 | 15 | 89 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.632 | 0.690 | 0.679 | 71 | 33 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT24TOREDM-9 | game_total | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR3 | game_spread | 0.191 | 0.155 | 0.162 | 16 | 85 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.170 | 0.135 | 0.141 | 14 | 87 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY3 | game_spread | 0.170 | 0.135 | 0.141 | 14 | 87 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.130 | 0.170 | 0.161 | 18 | 84 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-10 | game_total | 0.127 | 0.095 | 0.101 | 10 | 91 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA3 | team_total | 0.607 | 0.555 | 0.566 | 57 | 46 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT24ANAPHI-PHI3 | game_spread | 0.160 | 0.195 | 0.187 | 20 | 81 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT24TOREDM-8 | game_total | 0.416 | 0.375 | 0.383 | 38 | 63 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.178 | 0.140 | 0.147 | 15 | 87 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT24SJBOS-BOS2 | game_spread | 0.466 | 0.425 | 0.433 | 43 | 58 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA5 | team_total | 0.209 | 0.165 | 0.173 | 18 | 85 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-TB2 | team_total | 0.770 | 0.815 | 0.807 | 83 | 20 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.200 | 0.235 | 0.228 | 24 | 77 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT5 | team_total | 0.181 | 0.225 | 0.216 | 24 | 79 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT24LANJ-NJ3 | game_spread | 0.239 | 0.275 | 0.268 | 28 | 73 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT24LANJ-5 | game_total | 0.730 | 0.765 | 0.758 | 77 | 24 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT24LANJ-4 | game_total | 0.824 | 0.855 | 0.849 | 86 | 15 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT24MINSEA-5 | game_total | 0.762 | 0.795 | 0.789 | 80 | 21 | no | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 0.496 | 0.527 | 0.184 | 0.224 | 5.96 | 6.13 | 0.990/1.024 | KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI3 +0.050 |
| LAK @ NJD | 0.614 | 0.551 | 0.176 | 0.218 | 5.87 | 5.80 | 0.973/0.992 | KXNHLGAME-26OCT24LANJ-NJ -0.064 |
| SJS @ BOS | 0.682 | 0.607 | 0.153 | 0.209 | 6.40 | 6.54 | 0.955/1.034 | KXNHLTEAMTOTAL-26OCT24SJBOS-SJ3 +0.083 |
| NYR @ OTT | 0.471 | 0.544 | 0.179 | 0.219 | 6.09 | 6.21 | 1.039/0.988 | KXNHLGAME-26OCT24NYROTT-NYR -0.073 |
| NSH @ PIT | 0.568 | 0.581 | 0.170 | 0.206 | 6.71 | 6.58 | 1.038/1.000 | KXNHLTOTAL-26OCT24NSHPIT-6 -0.024 |
| BUF @ WSH | 0.492 | 0.535 | 0.171 | 0.212 | 6.62 | 6.49 | 1.015/1.000 | KXNHLGAME-26OCT24BUFWSH-WSH +0.044 |
| VGK @ CBJ | 0.416 | 0.469 | 0.168 | 0.223 | 6.46 | 6.14 | 1.007/1.003 | KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 -0.079 |
| CAR @ STL | 0.503 | 0.517 | 0.180 | 0.219 | 6.21 | 6.50 | 0.993/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.054 |
| TOR @ EDM | 0.637 | 0.641 | 0.151 | 0.201 | 7.24 | 6.92 | 1.022/0.965 | KXNHLTOTAL-26OCT24TOREDM-8 -0.054 |
| TBL @ UTA | 0.559 | 0.572 | 0.176 | 0.215 | 6.08 | 6.35 | 0.992/0.973 | KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 +0.049 |
| DET @ CGY | 0.520 | 0.504 | 0.188 | 0.224 | 5.73 | 6.04 | 0.986/1.003 | KXNHLTOTAL-26OCT24DETCGY-7 +0.058 |
| MIN @ SEA | 0.518 | 0.514 | 0.182 | 0.223 | 6.11 | 6.34 | 1.015/0.995 | KXNHLTOTAL-26OCT24MINSEA-7 +0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 12c · p 0.2037 (adj 0.1815) · $6.68 · thesis ANA:OFFENSE_4PLUS
- Denver Barkey: 1+ goals YES @ 14c · p 0.1866 (adj 0.1737) · $3.35 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 14c · p 0.1863 (adj 0.171) · $3.05 · thesis PHI:OFFENSE_4PLUS
- Noah Cates: 1+ goals YES @ 13c · p 0.1616 (adj 0.1512) · $1.73 · thesis PHI:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 3c · p 0.0583 (adj 0.0487) · $1.64 · thesis LAK:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 63c · p 0.7006 (adj 0.6804) · $7.7 · thesis NJD:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2781 (adj 0.2623) · $3.09 · thesis LAK:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 74c · p 0.786 (adj 0.772) · $7.02 · thesis NJD:SUPPRESSED
- Pavel Zacha: 1+ goals YES @ 28c · p 0.3269 (adj 0.3139) · $3.36 · thesis BOS:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1196 (adj 0.1022) · $1.94 · thesis NYR:OFFENSE_4PLUS
- Gabe Perreault: 1+ goals YES @ 22c · p 0.2522 (adj 0.2429) · $1.7 · thesis NYR:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 35c · p 0.4268 (adj 0.4051) · $7.06 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 33c · p 0.3892 (adj 0.3719) · $4.58 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 13c · p 0.1739 (adj 0.1492) · $1.29 · thesis PIT:OFFENSE_4PLUS
- Nick Robertson: 1+ goals YES @ 20c · p 0.2334 (adj 0.2238) · $1.79 · thesis PIT:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 26c · p 0.384 (adj 0.2936) · $2.84 · thesis WSH:OFFENSE_4PLUS
- Rasmus Dahlin: 1+ goals NO @ 80c · p 0.8366 (adj 0.8262) · $9.46 · thesis BUF:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 64c · p 0.6859 (adj 0.6719) · $5.27 · thesis BUF:SUPPRESSED
- Adam Fantilli: 1+ assists NO @ 61c · p 0.6935 (adj 0.6492) · $8.55 · thesis CBJ:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2599 (adj 0.2462) · $2.53 · thesis CBJ:OFFENSE_4PLUS
- Jack Eichel: 1+ assists NO @ 42c · p 0.5501 (adj 0.4488) · $2.62 · thesis VGK:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 23c · p 0.2898 (adj 0.2673) · $3.34 · thesis STL:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 64c · p 0.7273 (adj 0.6811) · $6.6 · thesis STL:WINS
- Pius Suter: 1+ goals YES @ 13c · p 0.1667 (adj 0.1525) · $1.63 · thesis STL:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7274 (adj 0.713) · $6.06 · thesis CAR:SUPPRESSED
- Connor McDavid: 2+ assists NO @ 66c · p 0.7406 (adj 0.6953) · $9.82 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3125 (adj 0.3006) · $3.44 · thesis EDM:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1514 (adj 0.1398) · $1.65 · thesis TOR:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 26c · p 0.3383 (adj 0.2892) · $2.35 · thesis EDM:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1468 (adj 0.1251) · $2.06 · thesis CGY:OFFENSE_4PLUS
- Detroit wins by over 2.5 goals NO @ 77c · p 0.8321 (adj 0.7985) · $8.33 · thesis CGY:WINS
- Kirill Kaprizov: 1+ goals NO @ 55c · p 0.6248 (adj 0.6048) · $9.67 · thesis MIN:SUPPRESSED
- Seattle wins by over 1.5 goals YES @ 22c · p 0.3055 (adj 0.2602) · $2.32 · thesis SEA:WINS_BY_2PLUS
- Berkly Catton: 1+ goals YES @ 15c · p 0.1944 (adj 0.1795) · $2.45 · thesis SEA:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 15c · p 0.1965 (adj 0.1786) · $2.4 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ PHI** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 28.6, exp saves 24.88 (sd 6.74), pull risk 0.054
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.01, exp saves 21.57 (sd 6.08), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Sanheim: 1+ assists | 0.362 | 0.260 | 27/75 | +0.078 | STANDARD |
| Travis Sanheim: 1+ points | 0.443 | 0.345 | 36/67 | +0.067 | STANDARD |
| Denver Barkey: 1+ points | 0.474 | 0.385 | 41/64 | +0.047 | STANDARD |
| A.J. Greer: 1+ goals | 0.204 | 0.115 | 12/89 | +0.076 | STANDARD |
| Denver Barkey: 1+ assists | 0.353 | 0.265 | 28/75 | +0.059 | STANDARD |
| Joseph Woll: 24+ saves | 0.582 | 0.500 | 51/51 | +0.054 |  |

**LAK @ NJD** · priced 158/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.53, exp saves 23.16 (sd 6.22), pull risk 0.045
- LAK net: Darcy Kuemper (PROJECTED) exp shots 30.31, exp saves 26.11 (sd 7.0), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.210 | 0.405 | 43/62 | +0.154 | STANDARD |
| Luke Evangelista: 1+ points | 0.371 | 0.540 | 56/48 | +0.132 | STANDARD |
| Jack Hughes: 2+ points | 0.215 | 0.345 | 36/67 | +0.099 | STANDARD |
| Jack Hughes: 1+ assists | 0.400 | 0.520 | 54/50 | +0.082 | STANDARD |
| Luke Evangelista: 2+ points | 0.079 | 0.185 | 21/84 | +0.072 | STANDARD |
| Alex Laferriere: 2+ points | 0.183 | 0.090 | 16/98 | +0.013 | STANDARD |

**SJS @ BOS** · priced 190/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.44, exp saves 24.01 (sd 6.55), pull risk 0.055
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.84, exp saves 23.56 (sd 6.73), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.398 | 0.515 | 53/50 | +0.084 | STANDARD |
| JJ Peterka: 1+ assists | 0.264 | 0.345 | 36/67 | +0.050 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.422 | 0.500 | 51/51 | +0.050 | STANDARD |
| David Pastrnak: 2+ points | 0.330 | 0.405 | 42/61 | +0.043 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.091 | 0.165 | 19/86 | +0.041 | STANDARD |
| Collin Graf: 1+ assists | 0.300 | 0.230 | 25/79 | +0.037 | STANDARD |

**NYR @ OTT** · priced 171/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Jonas Johansson (CONFIRMED) exp shots 23.91, exp saves 20.9 (sd 5.92), pull risk 0.054
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.38, exp saves 25.27 (sd 6.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.287 | 0.420 | 44/60 | +0.096 | STANDARD |
| Jake Sanderson: 1+ points | 0.372 | 0.495 | 52/53 | +0.081 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.338 | 0.225 | 25/80 | +0.075 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.392 | 0.290 | 31/73 | +0.067 | STANDARD |
| Alexis Lafreniere: 2+ points | 0.226 | 0.125 | 22/97 | -0.006 | STANDARD |
| Gabe Perreault: 1+ points | 0.483 | 0.395 | 43/64 | +0.035 | STANDARD |

**NSH @ PIT** · priced 150/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 26.07, exp saves 22.77 (sd 6.31), pull risk 0.057
- NSH net: Juuse Saros (PROJECTED) exp shots 29.45, exp saves 24.9 (sd 6.97), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 2+ points | 0.296 | 0.135 | 24/97 | +0.043 | STANDARD |
| Connor Dewar: 1+ goals | 0.210 | 0.075 | 13/98 | +0.072 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.125 | 0.245 | 27/78 | +0.083 | STANDARD |
| Erik Karlsson: 2+ points | 0.261 | 0.155 | 27/96 | -0.022 | STANDARD |
| Elmer Soderblom: 1+ goals | 0.178 | 0.075 | 13/98 | +0.040 | STANDARD |
| Hendrix Lapierre: 1+ goals | 0.187 | 0.085 | 15/98 | +0.028 | STANDARD |

**BUF @ WSH** · priced 170/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.16, exp saves 24.38 (sd 6.71), pull risk 0.064
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.97, exp saves 23.17 (sd 6.54), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.272 | 0.110 | 18/96 | +0.081 | STANDARD |
| Ryan Leonard: 1+ assists | 0.384 | 0.245 | 26/77 | +0.111 | STANDARD |
| Boone Jenner: 1+ goals | 0.219 | 0.100 | 16/96 | +0.050 | STANDARD |
| Dylan Strome: 2+ points | 0.240 | 0.125 | 22/97 | +0.008 | STANDARD |
| Jason Zucker: 1+ goals | 0.243 | 0.130 | 21/95 | +0.021 | STANDARD |
| Ryan Leonard: 2+ points | 0.182 | 0.075 | 13/98 | +0.045 | STANDARD |

**VGK @ CBJ** · priced 161/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.34, exp saves 23.55 (sd 6.41), pull risk 0.066
- VGK net: Carter Hart (PROBABLE) exp shots 27.42, exp saves 23.74 (sd 6.42), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.450 | 0.585 | 59/42 | +0.113 | STANDARD |
| Jack Eichel: 2+ points | 0.246 | 0.365 | 38/65 | +0.088 | STANDARD |
| Zach Werenski: 1+ assists | 0.460 | 0.555 | 57/46 | +0.063 | STANDARD |
| Adam Fantilli: 1+ assists | 0.306 | 0.395 | 40/61 | +0.067 | STANDARD |
| Damon Severson: 1+ points | 0.404 | 0.330 | 35/69 | +0.038 | STANDARD |
| Zach Werenski: 2+ points | 0.201 | 0.270 | 30/76 | +0.026 | STANDARD |

**CAR @ STL** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 30.19, exp saves 26.11 (sd 7.16), pull risk 0.067
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.39 (sd 5.89), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.375 | 0.485 | 49/52 | +0.088 | STANDARD |
| Seth Jarvis: 1+ assists | 0.210 | 0.310 | 33/71 | +0.065 | STANDARD |
| Philip Broberg: 1+ points | 0.477 | 0.385 | 41/64 | +0.050 | STANDARD |
| Robert Thomas: 1+ goals | 0.290 | 0.200 | 23/83 | +0.047 | STANDARD |
| Seth Jarvis: 1+ points | 0.407 | 0.495 | 52/53 | +0.045 | STANDARD |
| Sebastian Aho: 1+ points | 0.543 | 0.625 | 64/39 | +0.050 | STANDARD |

**TOR @ EDM** · priced 175/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.3 (sd 6.48), pull risk 0.059
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.98 (sd 7.69), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.514 | 0.625 | 64/39 | +0.079 | STANDARD |
| Leon Draisaitl: 2+ points | 0.372 | 0.480 | 50/54 | +0.071 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.302 | 0.410 | 43/61 | +0.071 | STANDARD |
| Gavin McKenna: 1+ points | 0.350 | 0.450 | 47/57 | +0.063 | STANDARD |
| Ryan Nugent-Hopkins: 1+ points | 0.470 | 0.570 | 59/45 | +0.062 | STANDARD |
| Connor McDavid: 2+ points | 0.471 | 0.570 | 59/45 | +0.061 | STANDARD |

**TBL @ UTA** · priced 164/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.3 (sd 6.37), pull risk 0.052
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.6, exp saves 22.78 (sd 6.46), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.220 | 0.340 | 36/68 | +0.085 | STANDARD |
| Lawson Crouse: 1+ goals | 0.227 | 0.120 | 20/96 | +0.016 | STANDARD |
| Brayden Point: 2+ points | 0.207 | 0.115 | 21/98 | -0.015 | STANDARD |
| Clayton Keller: 1+ assists | 0.449 | 0.535 | 55/48 | +0.053 | STANDARD |
| Jack McBain: 1+ goals | 0.154 | 0.070 | 12/98 | +0.027 | STANDARD |
| Ilya Mikheyev: 1+ goals | 0.162 | 0.080 | 14/98 | +0.013 | STANDARD |

**DET @ CGY** · priced 171/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 29.78, exp saves 25.84 (sd 6.79), pull risk 0.055
- DET net: Michal Postava (PROJECTED) exp shots 27.65, exp saves 23.91 (sd 6.64), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Bahl: 1+ points | 0.295 | 0.160 | 26/94 | +0.022 | STANDARD |
| Aydar Suniev: 1+ goals | 0.235 | 0.105 | 19/98 | +0.034 | STANDARD |
| Zach Whitecloud: 1+ points | 0.276 | 0.150 | 22/92 | +0.044 | STANDARD |
| Ben Jones: 1+ points | 0.203 | 0.325 | 37/72 | +0.063 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.278 | 0.380 | 40/64 | +0.066 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.243 | 0.150 | 18/88 | +0.053 | STANDARD |

**MIN @ SEA** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.27 (sd 6.92), pull risk 0.059
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.36, exp saves 23.53 (sd 6.49), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.259 | 0.380 | 40/64 | +0.084 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.625 | 0.725 | 74/29 | +0.071 | STANDARD |
| Quinn Hughes: 1+ assists | 0.543 | 0.635 | 65/38 | +0.060 | STANDARD |
| Matt Boldy: 1+ assists | 0.397 | 0.485 | 50/53 | +0.055 | STANDARD |
| Matt Boldy: 2+ points | 0.243 | 0.330 | 35/69 | +0.052 | STANDARD |
| Quinn Hughes: 2+ points | 0.234 | 0.320 | 36/72 | +0.031 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
