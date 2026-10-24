# NHL slate 2026-10-24 — RESEARCH_ONLY

generated 2026-10-24T11:12:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4031 · contracts joined: 2135 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1835, 'OK': 162, 'NO_EDGE': 138}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 276, 'game_early_goal': 12, 'first_goal': 326, 'game_winner': 24, 'player_goals': 559, 'game_overtime': 12, 'player_points': 362, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 2026-10-24T17:00:00Z | T-3h | 0.498 | 0.502 | 0.179 | 5.94 | 2.96 | 2.98 | 213 (25/188) | PROJECTED/PROJECTED |
| LAK @ NJD | 2026-10-24T19:30:00Z | T-6h | 0.611 | 0.389 | 0.174 | 5.86 | 3.28 | 2.58 | 224 (25/199) | PROJECTED/PROJECTED |
| SJS @ BOS | 2026-10-24T23:00:00Z | T-6h | 0.666 | 0.334 | 0.158 | 6.51 | 3.79 | 2.72 | 230 (25/205) | PROJECTED/PROJECTED |
| NYR @ OTT | 2026-10-24T23:00:00Z | T-6h | 0.464 | 0.536 | 0.179 | 6.20 | 2.99 | 3.20 | 223 (25/198) | PROJECTED/PROJECTED |
| NSH @ PIT | 2026-10-24T23:00:00Z | T-6h | 0.574 | 0.426 | 0.169 | 6.67 | 3.57 | 3.10 | 199 (25/174) | PROJECTED/PROJECTED |
| BUF @ WSH | 2026-10-24T23:00:00Z | T-6h | 0.505 | 0.495 | 0.173 | 6.58 | 3.31 | 3.28 | 234 (25/209) | PROJECTED/PROJECTED |
| VGK @ CBJ | 2026-10-24T23:00:00Z | T-6h | 0.476 | 0.524 | 0.184 | 6.01 | 2.94 | 3.07 | 217 (25/192) | PROJECTED/PROJECTED |
| CAR @ STL | 2026-10-24T23:00:00Z | T-6h | 0.501 | 0.499 | 0.177 | 6.19 | 3.10 | 3.09 | 212 (25/187) | PROJECTED/PROJECTED |
| TOR @ EDM | 2026-10-24T23:00:00Z | T-6h | 0.637 | 0.363 | 0.152 | 7.23 | 4.10 | 3.13 | 230 (25/205) | CONFIRMED/PROJECTED |
| TBL @ UTA | 2026-10-25T01:00:00Z | T-12h | 0.516 | 0.484 | 0.178 | 6.06 | 3.09 | 2.98 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ CGY | 2026-10-25T02:00:00Z | T-12h | 0.509 | 0.491 | 0.190 | 5.65 | 2.85 | 2.80 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ SEA | 2026-10-25T02:00:00Z | T-12h | 0.517 | 0.483 | 0.176 | 6.10 | 3.10 | 3.00 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT24MINSEA-SEA | game_winner | 0.517 | 0.405 | 0.427 | 41 | 60 | yes | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET4 | team_total | 0.318 | 0.435 | 0.410 | 45 | 58 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET3 | team_total | 0.541 | 0.655 | 0.633 | 67 | 36 | no | +0.083 | OK |
| KXNHLGAME-26OCT24MINSEA-MIN | game_winner | 0.483 | 0.585 | 0.565 | 59 | 42 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN4 | team_total | 0.360 | 0.455 | 0.436 | 46 | 55 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN2 | game_spread | 0.272 | 0.365 | 0.345 | 37 | 64 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET3 | game_spread | 0.147 | 0.235 | 0.215 | 24 | 77 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT24MINSEA-MIN3 | game_spread | 0.158 | 0.245 | 0.225 | 25 | 76 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT24TBUTA-7 | game_total | 0.425 | 0.515 | 0.497 | 52 | 49 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET5 | team_total | 0.150 | 0.245 | 0.223 | 26 | 77 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA4 | team_total | 0.386 | 0.480 | 0.461 | 49 | 53 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA2 | game_spread | 0.297 | 0.215 | 0.230 | 22 | 79 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR2 | game_spread | 0.279 | 0.365 | 0.347 | 37 | 64 | no | +0.065 | OK |
| KXNHLGAME-26OCT24CARSTL-CAR | game_winner | 0.499 | 0.585 | 0.568 | 59 | 42 | no | +0.064 | OK |
| KXNHLGAME-26OCT24CARSTL-STL | game_winner | 0.501 | 0.415 | 0.432 | 42 | 59 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA3 | team_total | 0.602 | 0.690 | 0.673 | 70 | 32 | no | +0.063 | OK |
| KXNHLGAME-26OCT24DETCGY-CGY | game_winner | 0.509 | 0.425 | 0.442 | 43 | 58 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN3 | team_total | 0.585 | 0.670 | 0.654 | 68 | 34 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT24TBUTA-6 | game_total | 0.535 | 0.615 | 0.599 | 62 | 39 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT24DETCGY-DET2 | game_spread | 0.266 | 0.350 | 0.332 | 36 | 66 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR4 | team_total | 0.384 | 0.465 | 0.449 | 47 | 54 | no | +0.058 | OK |
| KXNHLGAME-26OCT24NYROTT-OTT | game_winner | 0.464 | 0.545 | 0.529 | 55 | 46 | no | +0.058 | OK |
| KXNHLGAME-26OCT24NYROTT-NYR | game_winner | 0.536 | 0.455 | 0.471 | 46 | 55 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT24DETCGY-5 | game_total | 0.701 | 0.780 | 0.765 | 79 | 23 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT24CARSTL-CAR3 | game_spread | 0.171 | 0.245 | 0.229 | 25 | 76 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT24DETCGY-7 | game_total | 0.357 | 0.440 | 0.423 | 45 | 57 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET2 | team_total | 0.767 | 0.840 | 0.827 | 85 | 17 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR3 | team_total | 0.602 | 0.680 | 0.665 | 69 | 33 | no | +0.052 | OK |
| KXNHLGAME-26OCT24DETCGY-DET | game_winner | 0.491 | 0.565 | 0.550 | 57 | 44 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT24DETCGY-6 | game_total | 0.471 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5 | team_total | 0.189 | 0.265 | 0.248 | 28 | 75 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT24TBUTA-5 | game_total | 0.756 | 0.815 | 0.804 | 82 | 19 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA5 | team_total | 0.204 | 0.275 | 0.260 | 29 | 74 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN2 | team_total | 0.799 | 0.855 | 0.845 | 86 | 15 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL2 | game_spread | 0.284 | 0.220 | 0.232 | 23 | 79 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT3 | game_spread | 0.150 | 0.205 | 0.193 | 21 | 80 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR2 | game_spread | 0.312 | 0.255 | 0.266 | 26 | 75 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT24DETCGY-4 | game_total | 0.802 | 0.855 | 0.845 | 86 | 15 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA3 | game_spread | 0.180 | 0.235 | 0.223 | 24 | 77 | no | +0.037 | OK |
| KXNHLGAME-26OCT24TBUTA-TB | game_winner | 0.484 | 0.425 | 0.437 | 43 | 58 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT24DETCGY-CGY2 | game_spread | 0.279 | 0.225 | 0.235 | 23 | 78 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT24DETCGY-8 | game_total | 0.182 | 0.240 | 0.228 | 25 | 77 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT24NYROTT-OTT2 | game_spread | 0.260 | 0.315 | 0.304 | 32 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT24DETCGY-DET6 | team_total | 0.059 | 0.105 | 0.094 | 11 | 90 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA2 | team_total | 0.807 | 0.855 | 0.846 | 86 | 15 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR2 | team_total | 0.808 | 0.855 | 0.846 | 86 | 15 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR3 | team_total | 0.630 | 0.575 | 0.586 | 58 | 43 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT24LANJ-5 | game_total | 0.728 | 0.775 | 0.766 | 78 | 23 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT24TBUTA-8 | game_total | 0.238 | 0.295 | 0.283 | 31 | 72 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT24TBUTA-UTA2 | game_spread | 0.297 | 0.345 | 0.335 | 35 | 66 | no | +0.027 | OK |
| KXNHLGAME-26OCT24TBUTA-UTA | game_winner | 0.516 | 0.565 | 0.555 | 57 | 44 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT3 | team_total | 0.577 | 0.630 | 0.620 | 64 | 38 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT24DETCGY-9 | game_total | 0.124 | 0.170 | 0.160 | 18 | 84 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT24TBUTA-4 | game_total | 0.846 | 0.890 | 0.882 | 90 | 12 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-7 | game_total | 0.416 | 0.465 | 0.455 | 47 | 54 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK4 | team_total | 0.378 | 0.430 | 0.419 | 44 | 58 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT24VGKCBJ-VGK3 | team_total | 0.599 | 0.650 | 0.640 | 66 | 36 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24TBUTA-UTA6 | team_total | 0.089 | 0.135 | 0.124 | 15 | 88 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-8 | game_total | 0.328 | 0.285 | 0.293 | 29 | 72 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-MIN6 | team_total | 0.080 | 0.120 | 0.111 | 13 | 89 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT24MINSEA-SEA4 | team_total | 0.389 | 0.335 | 0.345 | 35 | 68 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT24NYROTT-NYR3 | game_spread | 0.192 | 0.155 | 0.162 | 16 | 85 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT24VGKCBJ-VGK3 | game_spread | 0.176 | 0.220 | 0.211 | 23 | 79 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT24CARSTL-STL3 | game_spread | 0.170 | 0.135 | 0.142 | 14 | 87 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT24TBUTA-9 | game_total | 0.167 | 0.205 | 0.197 | 21 | 80 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI3 | team_total | 0.572 | 0.620 | 0.610 | 63 | 39 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-NYR4 | team_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT24TOREDM-9 | game_total | 0.315 | 0.275 | 0.283 | 28 | 73 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT24LANJ-6 | game_total | 0.502 | 0.545 | 0.536 | 55 | 46 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-CAR5 | team_total | 0.207 | 0.260 | 0.249 | 28 | 76 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT24NSHPIT-7 | game_total | 0.527 | 0.485 | 0.493 | 49 | 52 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT24MINSEA-SEA3 | game_spread | 0.179 | 0.145 | 0.151 | 15 | 86 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT24NYROTT-OTT4 | team_total | 0.364 | 0.410 | 0.401 | 42 | 60 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT24TBUTA-10 | game_total | 0.074 | 0.110 | 0.102 | 12 | 90 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT24VGKCBJ-5 | game_total | 0.749 | 0.785 | 0.778 | 79 | 22 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT24VGKCBJ-VGK2 | game_spread | 0.296 | 0.335 | 0.327 | 34 | 67 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT24CARSTL-STL4 | team_total | 0.384 | 0.345 | 0.353 | 35 | 66 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT24TOREDM-10 | game_total | 0.177 | 0.140 | 0.147 | 15 | 87 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI4 | team_total | 0.356 | 0.395 | 0.387 | 40 | 61 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT24BUFWSH-WSH3 | game_spread | 0.181 | 0.215 | 0.208 | 22 | 79 | no | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ PHI | 0.498 | 0.525 | 0.179 | 0.222 | 5.94 | 6.14 | 0.991/1.024 | KXNHLTEAMTOTAL-26OCT24ANAPHI-PHI3 +0.048 |
| LAK @ NJD | 0.611 | 0.552 | 0.174 | 0.226 | 5.86 | 5.80 | 0.973/0.992 | KXNHLGAME-26OCT24LANJ-LA +0.060 |
| SJS @ BOS | 0.666 | 0.596 | 0.158 | 0.212 | 6.51 | 6.57 | 0.968/1.034 | KXNHLGAME-26OCT24SJBOS-BOS -0.070 |
| NYR @ OTT | 0.464 | 0.543 | 0.179 | 0.222 | 6.20 | 6.24 | 1.050/0.992 | KXNHLGAME-26OCT24NYROTT-OTT +0.079 |
| NSH @ PIT | 0.574 | 0.583 | 0.169 | 0.209 | 6.67 | 6.57 | 1.033/1.000 | KXNHLTOTAL-26OCT24NSHPIT-6 -0.018 |
| BUF @ WSH | 0.505 | 0.537 | 0.173 | 0.216 | 6.58 | 6.43 | 0.992/0.997 | KXNHLTEAMTOTAL-26OCT24BUFWSH-BUF3 -0.040 |
| VGK @ CBJ | 0.476 | 0.489 | 0.184 | 0.222 | 6.01 | 6.02 | 0.964/1.003 | KXNHLGAME-26OCT24VGKCBJ-CBJ +0.013 |
| CAR @ STL | 0.501 | 0.524 | 0.177 | 0.218 | 6.19 | 6.50 | 0.993/0.997 | KXNHLTOTAL-26OCT24CARSTL-7 +0.055 |
| TOR @ EDM | 0.637 | 0.641 | 0.152 | 0.202 | 7.23 | 6.92 | 1.022/0.965 | KXNHLTOTAL-26OCT24TOREDM-8 -0.049 |
| TBL @ UTA | 0.516 | 0.538 | 0.178 | 0.214 | 6.06 | 6.34 | 0.992/0.957 | KXNHLTOTAL-26OCT24TBUTA-7 +0.053 |
| DET @ CGY | 0.509 | 0.506 | 0.190 | 0.222 | 5.65 | 6.03 | 0.986/1.003 | KXNHLTOTAL-26OCT24DETCGY-7 +0.063 |
| MIN @ SEA | 0.517 | 0.516 | 0.176 | 0.216 | 6.10 | 6.33 | 1.015/0.995 | KXNHLTOTAL-26OCT24MINSEA-7 +0.036 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Christian Dvorak: 1+ goals YES @ 17c · p 0.2305 (adj 0.2079) · $7.69 · thesis PHI:OFFENSE_4PLUS
- Denver Barkey: 1+ goals YES @ 15c · p 0.1853 (adj 0.1752) · $4.58 · thesis PHI:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 11c · p 0.2046 (adj 0.1301) · $2.49 · thesis ANA:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 14c · p 0.1811 (adj 0.1608) · $3.18 · thesis PHI:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 62c · p 0.7941 (adj 0.6679) · $20.0 · thesis NJD:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 68c · p 0.8194 (adj 0.7093) · $15.55 · thesis LAK:SUPPRESSED
- New Jersey over 3.5 goals scored NO @ 55c · p 0.6155 (adj 0.5802) · $4.41 · thesis NJD:SUPPRESSED
- Carolina wins by over 1.5 goals NO @ 64c · p 0.7305 (adj 0.6827) · $10.77 · thesis STL:WINS
- St. Louis over 3.5 goals scored YES @ 35c · p 0.4359 (adj 0.3904) · $4.14 · thesis STL:OFFENSE_4PLUS
- St. Louis wins by over 1.5 goals YES @ 23c · p 0.307 (adj 0.2635) · $2.38 · thesis STL:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 76c · p 0.8303 (adj 0.7927) · $7.61 · thesis STL:WINS
- Detroit wins by over 2.5 goals NO @ 77c · p 0.8369 (adj 0.801) · $20.0 · thesis CGY:WINS
- Minnesota wins by over 2.5 goals NO @ 76c · p 0.8428 (adj 0.7989) · $20.0 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 22c · p 0.3017 (adj 0.2584) · $6.19 · thesis SEA:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ PHI** · priced 154/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 28.6, exp saves 24.88 (sd 6.69), pull risk 0.053
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.01, exp saves 21.61 (sd 6.12), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.205 | 0.090 | 11/93 | +0.088 | STANDARD |
| Travis Sanheim: 1+ points | 0.447 | 0.345 | 37/68 | +0.061 | STANDARD |
| Denver Barkey: 1+ points | 0.463 | 0.365 | 41/68 | +0.036 | STANDARD |
| Travis Sanheim: 1+ assists | 0.366 | 0.270 | 29/75 | +0.062 | STANDARD |
| Denver Barkey: 1+ assists | 0.343 | 0.250 | 30/80 | +0.028 | STANDARD |
| Christian Dvorak: 1+ goals | 0.231 | 0.140 | 17/89 | +0.051 | STANDARD |

**LAK @ NJD** · priced 168/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.53, exp saves 23.2 (sd 6.26), pull risk 0.043
- LAK net: Darcy Kuemper (PROJECTED) exp shots 30.31, exp saves 26.12 (sd 6.98), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.206 | 0.400 | 42/62 | +0.158 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.181 | 0.350 | 38/68 | +0.124 | STANDARD |
| Luke Evangelista: 1+ points | 0.366 | 0.530 | 56/50 | +0.116 | STANDARD |
| Mats Zuccarello: 1+ points | 0.335 | 0.455 | 49/58 | +0.068 | STANDARD |
| Jack Hughes: 2+ points | 0.220 | 0.335 | 36/69 | +0.075 | STANDARD |
| Jack Hughes: 1+ assists | 0.398 | 0.510 | 53/51 | +0.074 | STANDARD |

**SJS @ BOS** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.44, exp saves 23.98 (sd 6.54), pull risk 0.055
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.84, exp saves 23.61 (sd 6.67), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Lindholm: 3+ goals | 0.004 | 0.495 | 98/99 | +0.005 | STANDARD |
| Pavel Zacha: 3+ goals | 0.007 | 0.490 | 97/99 | +0.002 | STANDARD |
| Charlie McAvoy: 2+ goals | 0.013 | 0.495 | 98/99 | -0.003 | STANDARD |
| Macklin Celebrini: 3+ goals | 0.015 | 0.495 | 98/99 | -0.006 | STANDARD |
| Matthew Poitras: 2+ goals | 0.012 | 0.490 | 97/99 | -0.003 | STANDARD |
| Marat Khusnutdinov: 2+ goals | 0.013 | 0.490 | 97/99 | -0.003 | STANDARD |

**NYR @ OTT** · priced 168/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 23.91, exp saves 20.84 (sd 5.98), pull risk 0.055
- NYR net: Dylan Garand (PROJECTED) exp shots 29.38, exp saves 25.23 (sd 6.9), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Warren Foegele: 2+ goals | 0.020 | 0.490 | 97/99 | -0.011 | STANDARD |
| Fabian Zetterlund: 2+ assists | 0.034 | 0.495 | 97/98 | -0.015 | STANDARD |
| Will Cuylle: 2+ points | 0.071 | 0.495 | 97/98 | -0.052 | STANDARD |
| Vladislav Gavrikov: 2+ points | 0.090 | 0.495 | 97/98 | -0.071 | STANDARD |
| Alexis Lafreniere: 1+ points | 0.595 | 0.315 | 61/98 | -0.032 | STANDARD |
| Mika Zibanejad: 1+ points | 0.602 | 0.340 | 66/98 | -0.074 | STANDARD |

**NSH @ PIT** · priced 147/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.07, exp saves 22.77 (sd 6.3), pull risk 0.058
- NSH net: Juuse Saros (PROJECTED) exp shots 29.45, exp saves 24.93 (sd 7.05), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Evgeni Malkin: 3+ goals | 0.004 | 0.490 | 97/99 | +0.006 | STANDARD |
| Filip Forsberg: 3+ goals | 0.006 | 0.490 | 97/99 | +0.003 | STANDARD |
| Nils Hoglander: 2+ goals | 0.010 | 0.490 | 97/99 | -0.000 | STANDARD |
| Blake Lizotte: 2+ goals | 0.011 | 0.490 | 97/99 | -0.001 | STANDARD |
| Elmer Soderblom: 2+ goals | 0.012 | 0.490 | 97/99 | -0.002 | STANDARD |
| Adam Edstrom: 2+ goals | 0.012 | 0.490 | 97/99 | -0.003 | STANDARD |

**BUF @ WSH** · priced 169/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (PROJECTED) exp shots 28.16, exp saves 24.4 (sd 6.8), pull risk 0.064
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.97, exp saves 23.12 (sd 6.51), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Power: 2+ goals | 0.003 | 0.485 | 96/99 | +0.006 | STANDARD |
| Peyton Krebs: 2+ goals | 0.009 | 0.485 | 96/99 | +0.000 | STANDARD |
| Ryan McLeod: 2+ goals | 0.011 | 0.485 | 96/99 | -0.001 | STANDARD |
| Konsta Helenius: 2+ goals | 0.011 | 0.485 | 96/99 | -0.002 | STANDARD |
| Jason Zucker: 2+ assists | 0.023 | 0.495 | 97/98 | -0.004 | STANDARD |
| Anthony Beauvillier: 2+ goals | 0.017 | 0.485 | 96/99 | -0.007 | STANDARD |

**VGK @ CBJ** · priced 157/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.34, exp saves 23.69 (sd 6.39), pull risk 0.058
- VGK net: Carter Hart (PROJECTED) exp shots 27.42, exp saves 23.75 (sd 6.44), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 4+ points | 0.014 | 0.500 | 99/99 | -0.004 | STANDARD |
| Valeri Nichushkin: 2+ assists | 0.020 | 0.495 | 98/99 | -0.011 | STANDARD |
| William Karlsson: 2+ assists | 0.027 | 0.500 | 98/98 | -0.009 | STANDARD |
| Zach Werenski: 3+ assists | 0.027 | 0.480 | 95/99 | -0.017 | STANDARD |
| Tomas Hertl: 2+ assists | 0.045 | 0.495 | 98/99 | -0.036 | STANDARD |
| Zach Werenski: 3+ points | 0.054 | 0.500 | 98/98 | -0.036 | STANDARD |

**CAR @ STL** · priced 158/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 30.19, exp saves 26.07 (sd 7.13), pull risk 0.069
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.68, exp saves 20.43 (sd 5.83), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dalibor Dvorsky: 2+ goals | 0.006 | 0.490 | 97/99 | +0.003 | STANDARD |
| Shayne Gostisbehere: 2+ goals | 0.007 | 0.490 | 97/99 | +0.003 | STANDARD |
| Jonatan Berggren: 2+ goals | 0.011 | 0.490 | 97/99 | -0.002 | STANDARD |
| Eric Robinson: 2+ goals | 0.011 | 0.490 | 97/99 | -0.002 | STANDARD |
| Shayne Gostisbehere: 3+ points | 0.017 | 0.495 | 97/98 | +0.002 | STANDARD |
| Jordan Martinook: 2+ goals | 0.014 | 0.490 | 97/99 | -0.005 | STANDARD |

**TOR @ EDM** · priced 171/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.54, exp saves 23.32 (sd 6.41), pull risk 0.058
- TOR net: Anthony Stolarz (PROJECTED) exp shots 32.17, exp saves 26.97 (sd 7.61), pull risk 0.106

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 3+ goals | 0.017 | 0.500 | 98/98 | +0.002 | STANDARD |
| Connor McDavid: 5+ points | 0.021 | 0.500 | 99/99 | -0.012 | STANDARD |
| Kirill Marchenko: 3+ points | 0.032 | 0.500 | 99/99 | -0.022 | STANDARD |
| Ryan Nugent-Hopkins: 3+ points | 0.027 | 0.495 | 98/99 | -0.018 | STANDARD |
| Gavin McKenna: 2+ assists | 0.033 | 0.495 | 97/98 | -0.015 | STANDARD |
| Jake Walman: 2+ points | 0.043 | 0.500 | 99/99 | -0.034 | STANDARD |

**TBL @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.18 (sd 6.41), pull risk 0.054
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.6, exp saves 22.93 (sd 6.4), pull risk 0.067

**DET @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 29.78, exp saves 25.83 (sd 6.77), pull risk 0.056
- DET net: John Gibson (PROJECTED) exp shots 27.65, exp saves 23.9 (sd 6.51), pull risk 0.058

**MIN @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 30.26, exp saves 26.23 (sd 7.05), pull risk 0.06
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.36, exp saves 23.59 (sd 6.51), pull risk 0.063

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
