# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T12:05:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3596 · contracts joined: 1699 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1424, 'OK': 163, 'NO_EDGE': 112}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 209, 'game_early_goal': 11, 'first_goal': 237, 'game_winner': 22, 'player_goals': 431, 'game_overtime': 11, 'player_points': 261, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-6h | 0.607 | 0.394 | 0.172 | 6.16 | 3.42 | 2.74 | 209 (25/184) | PROJECTED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-6h | 0.462 | 0.538 | 0.179 | 5.98 | 2.88 | 3.11 | 223 (25/198) | PROJECTED/PROJECTED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-6h | 0.596 | 0.404 | 0.176 | 6.09 | 3.35 | 2.74 | 199 (25/174) | PROJECTED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-6h | 0.601 | 0.399 | 0.181 | 5.69 | 3.15 | 2.54 | 224 (25/199) | PROJECTED/PROJECTED |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-6h | 0.642 | 0.358 | 0.167 | 6.26 | 3.59 | 2.67 | 205 (25/180) | PROJECTED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-6h | 0.601 | 0.399 | 0.183 | 5.96 | 3.30 | 2.67 | 222 (25/197) | PROJECTED/PROJECTED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-6h | 0.512 | 0.488 | 0.182 | 5.69 | 2.89 | 2.80 | 213 (25/188) | PROJECTED/PROJECTED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-12h | 0.568 | 0.432 | 0.171 | 6.42 | 3.42 | 3.00 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-12h | 0.581 | 0.419 | 0.176 | 6.02 | 3.26 | 2.77 | 51 (25/26) | PROJECTED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-12h | 0.349 | 0.651 | 0.162 | 6.44 | 2.72 | 3.72 | 51 (25/26) | PROJECTED/PROJECTED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-12h | 0.526 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.557 | 0.655 | 0.636 | 66 | 35 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.337 | 0.440 | 0.419 | 45 | 57 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.312 | 0.410 | 0.389 | 42 | 60 | no | +0.072 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.488 | 0.395 | 0.413 | 40 | 61 | yes | +0.071 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.166 | 0.255 | 0.235 | 26 | 75 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.523 | 0.625 | 0.605 | 64 | 39 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.260 | 0.350 | 0.331 | 36 | 66 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.459 | 0.550 | 0.532 | 56 | 46 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.441 | 0.525 | 0.508 | 53 | 48 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.288 | 0.370 | 0.353 | 38 | 64 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.417 | 0.495 | 0.479 | 50 | 51 | no | +0.055 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.651 | 0.725 | 0.711 | 73 | 28 | no | +0.055 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.349 | 0.275 | 0.289 | 28 | 73 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.672 | 0.750 | 0.735 | 76 | 26 | no | +0.054 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.419 | 0.495 | 0.480 | 50 | 51 | no | +0.053 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.581 | 0.505 | 0.520 | 51 | 50 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.410 | 0.485 | 0.470 | 49 | 52 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.758 | 0.825 | 0.813 | 83 | 18 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.501 | 0.575 | 0.560 | 58 | 43 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.553 | 0.630 | 0.615 | 64 | 38 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.524 | 0.595 | 0.581 | 60 | 41 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.217 | 0.285 | 0.270 | 29 | 72 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.170 | 0.240 | 0.225 | 25 | 77 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.247 | 0.315 | 0.301 | 32 | 69 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.123 | 0.185 | 0.171 | 19 | 82 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.297 | 0.365 | 0.351 | 37 | 64 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.152 | 0.225 | 0.209 | 24 | 79 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR4 | team_total | 0.526 | 0.605 | 0.590 | 62 | 41 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.763 | 0.830 | 0.818 | 84 | 18 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.338 | 0.405 | 0.391 | 41 | 60 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.744 | 0.805 | 0.794 | 81 | 20 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.734 | 0.800 | 0.788 | 81 | 21 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR5 | team_total | 0.320 | 0.395 | 0.380 | 41 | 62 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.530 | 0.600 | 0.586 | 61 | 41 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT20LAWSH-5 | game_total | 0.705 | 0.765 | 0.754 | 77 | 24 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.778 | 0.840 | 0.829 | 85 | 17 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.262 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.384 | 0.445 | 0.433 | 45 | 56 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.555 | 0.620 | 0.607 | 63 | 39 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3 | team_total | 0.731 | 0.790 | 0.779 | 80 | 22 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.752 | 0.815 | 0.804 | 83 | 20 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN2 | game_spread | 0.173 | 0.125 | 0.134 | 13 | 88 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.702 | 0.755 | 0.745 | 76 | 25 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.292 | 0.350 | 0.338 | 36 | 66 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.895 | 0.887 | 90 | 11 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20DETSEA-8 | game_total | 0.235 | 0.285 | 0.275 | 29 | 72 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20LAWSH-4 | game_total | 0.800 | 0.845 | 0.837 | 85 | 16 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.226 | 0.275 | 0.265 | 28 | 73 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.130 | 0.180 | 0.169 | 19 | 83 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT20SJMTL-9 | game_total | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5 | team_total | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.169 | 0.225 | 0.213 | 24 | 79 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-CBJ2 | game_spread | 0.415 | 0.365 | 0.375 | 37 | 64 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2 | team_total | 0.744 | 0.695 | 0.705 | 70 | 31 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR3 | game_spread | 0.093 | 0.135 | 0.126 | 14 | 87 | no | +0.029 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.394 | 0.345 | 0.354 | 35 | 66 | yes | +0.028 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.607 | 0.655 | 0.646 | 66 | 35 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4 | team_total | 0.300 | 0.250 | 0.260 | 26 | 76 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.773 | 0.825 | 0.815 | 84 | 19 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT20LAWSH-7 | game_total | 0.367 | 0.415 | 0.405 | 42 | 59 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG3 | game_spread | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.350 | 0.305 | 0.314 | 31 | 70 | yes | +0.025 | OK |
| KXNHLGAME-26OCT20TORCBJ-CBJ | game_winner | 0.642 | 0.595 | 0.605 | 60 | 41 | yes | +0.025 | OK |
| KXNHLGAME-26OCT20TORCBJ-TOR | game_winner | 0.358 | 0.405 | 0.395 | 41 | 60 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT20LAWSH-9 | game_total | 0.126 | 0.165 | 0.156 | 17 | 84 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.512 | 0.460 | 0.470 | 47 | 55 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.839 | 0.880 | 0.873 | 89 | 13 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT20DETSEA-4 | game_total | 0.839 | 0.880 | 0.873 | 89 | 13 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT20LAWSH-6 | game_total | 0.479 | 0.525 | 0.516 | 53 | 48 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.175 | 0.220 | 0.210 | 23 | 79 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT20COLNJ-9 | game_total | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT20TORCBJ-5 | game_total | 0.778 | 0.815 | 0.808 | 82 | 19 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR5 | team_total | 0.139 | 0.175 | 0.167 | 18 | 83 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-4 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET6 | team_total | 0.063 | 0.095 | 0.088 | 10 | 91 | no | +0.021 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 0.607 | 0.590 | 0.172 | 0.214 | 6.16 | 6.34 | 0.976/1.024 | KXNHLTEAMTOTAL-26OCT20SJMTL-SJ4 +0.034 |
| COL @ NJD | 0.462 | 0.481 | 0.179 | 0.225 | 5.98 | 6.18 | 0.992/0.973 | KXNHLTOTAL-26OCT20COLNJ-7 +0.044 |
| ANA @ NYI | 0.596 | 0.570 | 0.176 | 0.215 | 6.09 | 6.38 | 0.956/1.016 | KXNHLTEAMTOTAL-26OCT20ANANYI-ANA4 +0.052 |
| LAK @ WSH | 0.601 | 0.571 | 0.181 | 0.227 | 5.69 | 5.94 | 0.961/0.989 | KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 +0.055 |
| TOR @ CBJ | 0.642 | 0.614 | 0.167 | 0.217 | 6.26 | 6.04 | 0.964/0.956 | KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ4 -0.046 |
| WPG @ STL | 0.601 | 0.582 | 0.183 | 0.221 | 5.96 | 6.22 | 0.993/0.988 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.046 |
| BOS @ DAL | 0.512 | 0.537 | 0.182 | 0.219 | 5.69 | 6.22 | 0.986/0.968 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.091 |
| MIN @ EDM | 0.568 | 0.595 | 0.171 | 0.206 | 6.42 | 6.68 | 0.994/0.995 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.054 |
| DET @ SEA | 0.581 | 0.575 | 0.176 | 0.210 | 6.02 | 6.24 | 1.015/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.041 |
| CAR @ VAN | 0.349 | 0.442 | 0.162 | 0.216 | 6.44 | 6.50 | 1.026/0.997 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.097 |
| TBL @ VGK | 0.526 | 0.585 | 0.181 | 0.221 | 6.10 | 6.12 | 1.004/0.958 | KXNHLGAME-26OCT20TBVGK-TB -0.059 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 26 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 17c · p 0.2343 (adj 0.2157) · $8.13 · thesis SJS:OFFENSE_4PLUS
- Montreal wins by over 1.5 goals NO @ 56c · p 0.6352 (adj 0.5951) · $5.59 · thesis GAME:TIGHT
- Montreal wins by over 2.5 goals NO @ 69c · p 0.752 (adj 0.7185) · $1.01 · thesis GAME:TIGHT
- Fedor Svechkov: 1+ goals YES @ 8c · p 0.1182 (adj 0.1061) · $4.39 · thesis COL:OFFENSE_4PLUS
- Gabriel Landeskog: 1+ goals YES @ 18c · p 0.2212 (adj 0.2097) · $5.08 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ assists NO @ 46c · p 0.6022 (adj 0.4968) · $9.52 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 65c · p 0.696 (adj 0.6807) · $9.53 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 12c · p 0.2071 (adj 0.1828) · $11.45 · thesis ANA:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0652 (adj 0.0564) · $2.5 · thesis LAK:OFFENSE_4PLUS
- Toronto wins 1st Period by over 1.5 goals YES @ 2c · p 0.0821 (adj 0.0385) · $1.46 · thesis TOR:SCORES_FIRST
- Toronto over 2.5 goals scored NO @ 43c · p 0.5047 (adj 0.4649) · $7.1 · thesis TOR:SUPPRESSED
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4725 (adj 0.4337) · $3.87 · thesis GAME:LOW_EVENT
- Darren Raddysh: 1+ assists NO @ 60c · p 0.6691 (adj 0.627) · $3.85 · thesis TOR:SUPPRESSED
- Boston over 4.5 goals scored YES @ 13c · p 0.1882 (adj 0.1566) · $2.12 · thesis BOS:OFFENSE_4PLUS
- Boston over 2.5 goals scored YES @ 51c · p 0.5954 (adj 0.5477) · $4.04 · thesis BOS:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8096 (adj 0.7773) · $7.6 · thesis BOS:WINS
- Edmonton over 3.5 goals scored YES @ 44c · p 0.512 (adj 0.471) · $5.25 · thesis EDM:OFFENSE_4PLUS
- Detroit wins by over 2.5 goals NO @ 82c · p 0.8748 (adj 0.8449) · $16.69 · thesis SEA:WINS
- Detroit wins by over 1.5 goals NO @ 72c · p 0.7832 (adj 0.7491) · $2.92 · thesis SEA:WINS
- Detroit over 3.5 goals scored NO @ 60c · p 0.6681 (adj 0.629) · $1.51 · thesis DET:SUPPRESSED
- Vancouver over 4.5 goals scored YES @ 11c · p 0.1995 (adj 0.1522) · $3.85 · thesis VAN:OFFENSE_4PLUS
- Vancouver wins by over 2.5 goals YES @ 7c · p 0.1383 (adj 0.1017) · $2.16 · thesis VAN:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 48c · p 0.6564 (adj 0.5385) · $11.08 · thesis VAN:WINS
- Tampa Bay wins by over 1.5 goals NO @ 73c · p 0.7927 (adj 0.7589) · $6.95 · thesis VGK:WINS
- Tampa Bay wins by over 2.5 goals NO @ 83c · p 0.8786 (adj 0.8518) · $8.49 · thesis VGK:WINS
- Tampa Bay over 3.5 goals scored NO @ 61c · p 0.6848 (adj 0.6399) · $2.86 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 148/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.0, exp saves 23.52 (sd 6.46), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.28 (sd 6.61), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ goals | 0.366 | 0.195 | 36/97 | -0.010 | STANDARD |
| Cole Caufield: 1+ goals | 0.398 | 0.245 | 46/97 | -0.079 | STANDARD |
| Nick Suzuki: 1+ points | 0.656 | 0.540 | 76/68 | -0.117 | STANDARD |
| Nick Suzuki: 1+ goals | 0.326 | 0.215 | 36/93 | -0.051 | STANDARD |
| Will Smith: 1+ goals | 0.289 | 0.180 | 28/92 | -0.005 | STANDARD |
| Nick Suzuki: 1+ assists | 0.487 | 0.595 | 62/43 | +0.066 | STANDARD |

**COL @ NJD** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 29.27, exp saves 25.3 (sd 6.78), pull risk 0.06
- COL net: Scott Wedgewood (PROJECTED) exp shots 28.54, exp saves 24.74 (sd 6.73), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.398 | 0.560 | 58/46 | +0.125 | STANDARD |
| Jack Hughes: 1+ assists | 0.382 | 0.540 | 57/49 | +0.111 | STANDARD |
| Cale Makar: 1+ points | 0.496 | 0.640 | 66/38 | +0.108 | STANDARD |
| Jack Hughes: 2+ points | 0.207 | 0.345 | 37/68 | +0.098 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.664 | 0.540 | 75/67 | -0.099 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.300 | 0.410 | 42/60 | +0.083 | STANDARD |

**ANA @ NYI** · priced 145/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.2, exp saves 24.6 (sd 6.61), pull risk 0.056
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.47), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ goals | 0.273 | 0.150 | 27/97 | -0.011 | STANDARD |
| Cutter Gauthier: 1+ goals | 0.302 | 0.190 | 33/95 | -0.044 | STANDARD |
| Beckett Sennecke: 1+ goals | 0.291 | 0.180 | 29/93 | -0.014 | STANDARD |
| A.J. Greer: 1+ goals | 0.207 | 0.110 | 12/90 | +0.080 | STANDARD |
| Jean-Gabriel Pageau: 1+ goals | 0.199 | 0.105 | 18/97 | +0.008 | STANDARD |
| Alex Killorn: 1+ goals | 0.203 | 0.110 | 19/97 | +0.002 | STANDARD |

**LAK @ WSH** · priced 158/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.19, exp saves 24.61 (sd 6.48), pull risk 0.044
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.88, exp saves 22.97 (sd 6.35), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.238 | 0.115 | 19/96 | +0.037 | STANDARD |
| Artemi Panarin: 1+ assists | 0.361 | 0.480 | 50/54 | +0.082 | STANDARD |
| Quinton Byfield: 1+ goals | 0.262 | 0.150 | 27/97 | -0.022 | STANDARD |
| Alex Ovechkin: 1+ goals | 0.284 | 0.175 | 32/97 | -0.051 | STANDARD |
| Boone Jenner: 1+ goals | 0.213 | 0.110 | 19/97 | +0.013 | STANDARD |
| Artemi Panarin: 1+ points | 0.544 | 0.635 | 65/38 | +0.059 | STANDARD |

**TOR @ CBJ** · priced 145/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 25.9, exp saves 22.9 (sd 6.19), pull risk 0.043
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.76 (sd 7.19), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.295 | 0.145 | 26/97 | +0.021 | STANDARD |
| Auston Matthews: 1+ goals | 0.328 | 0.195 | 36/97 | -0.048 | STANDARD |
| Auston Matthews: 1+ assists | 0.342 | 0.470 | 49/55 | +0.091 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.231 | 0.105 | 18/97 | +0.040 | STANDARD |
| William Nylander: 1+ goals | 0.302 | 0.190 | 31/93 | -0.023 | STANDARD |
| Auston Matthews: 1+ points | 0.554 | 0.655 | 67/36 | +0.070 | STANDARD |

**WPG @ STL** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.09, exp saves 22.87 (sd 6.23), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.62, exp saves 22.62 (sd 6.49), pull risk 0.072

**BOS @ DAL** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.27 (sd 5.98), pull risk 0.057
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.85, exp saves 24.06 (sd 6.49), pull risk 0.062

**MIN @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.28 (sd 6.69), pull risk 0.064
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.81 (sd 7.09), pull risk 0.087

**DET @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.42, exp saves 25.69 (sd 6.74), pull risk 0.05
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.84 (sd 6.46), pull risk 0.076

**CAR @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 32.33, exp saves 27.7 (sd 7.44), pull risk 0.074
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.8, exp saves 19.88 (sd 5.73), pull risk 0.059

**TBL @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.99, exp saves 23.58 (sd 6.42), pull risk 0.051
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.35, exp saves 22.55 (sd 6.37), pull risk 0.071

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
