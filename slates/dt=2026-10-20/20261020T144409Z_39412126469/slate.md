# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T14:44:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4265 · contracts joined: 2368 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2093, 'OK': 169, 'NO_EDGE': 106}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 332, 'game_early_goal': 11, 'first_goal': 376, 'game_winner': 22, 'player_goals': 681, 'game_overtime': 11, 'player_points': 418, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-6h | 0.607 | 0.394 | 0.172 | 6.16 | 3.42 | 2.74 | 209 (25/184) | PROJECTED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-6h | 0.462 | 0.538 | 0.179 | 5.98 | 2.88 | 3.11 | 236 (25/211) | PROJECTED/PROJECTED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-6h | 0.596 | 0.404 | 0.176 | 6.09 | 3.35 | 2.74 | 199 (25/174) | PROJECTED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-6h | 0.601 | 0.399 | 0.181 | 5.69 | 3.15 | 2.54 | 224 (25/199) | PROJECTED/PROJECTED |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-6h | 0.642 | 0.358 | 0.167 | 6.26 | 3.59 | 2.67 | 205 (25/180) | PROJECTED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-6h | 0.601 | 0.399 | 0.183 | 5.96 | 3.30 | 2.67 | 222 (25/197) | PROJECTED/PROJECTED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-6h | 0.512 | 0.488 | 0.182 | 5.69 | 2.89 | 2.80 | 213 (25/188) | PROJECTED/PROJECTED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-6h | 0.568 | 0.432 | 0.171 | 6.42 | 3.42 | 3.00 | 229 (25/204) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-6h | 0.581 | 0.419 | 0.176 | 6.02 | 3.26 | 2.77 | 208 (25/183) | PROJECTED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-6h | 0.349 | 0.651 | 0.162 | 6.44 | 2.72 | 3.72 | 211 (25/186) | PROJECTED/PROJECTED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-6h | 0.552 | 0.448 | 0.182 | 5.95 | 3.13 | 2.82 | 212 (25/187) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.557 | 0.655 | 0.636 | 66 | 35 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.337 | 0.440 | 0.419 | 45 | 57 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.312 | 0.410 | 0.389 | 42 | 60 | no | +0.072 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.488 | 0.395 | 0.413 | 40 | 61 | yes | +0.071 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.166 | 0.255 | 0.235 | 26 | 75 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.523 | 0.620 | 0.601 | 63 | 39 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.297 | 0.385 | 0.367 | 39 | 62 | no | +0.066 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.651 | 0.735 | 0.719 | 74 | 27 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.260 | 0.350 | 0.331 | 36 | 66 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.459 | 0.550 | 0.532 | 56 | 46 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.441 | 0.525 | 0.508 | 53 | 48 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.322 | 0.410 | 0.392 | 42 | 60 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.553 | 0.635 | 0.619 | 64 | 37 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.763 | 0.835 | 0.822 | 84 | 17 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.288 | 0.365 | 0.349 | 37 | 64 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.417 | 0.495 | 0.479 | 50 | 51 | no | +0.055 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.349 | 0.275 | 0.289 | 28 | 73 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.672 | 0.750 | 0.735 | 76 | 26 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.539 | 0.620 | 0.604 | 63 | 39 | no | +0.054 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.419 | 0.495 | 0.480 | 50 | 51 | no | +0.053 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.581 | 0.505 | 0.520 | 51 | 50 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.778 | 0.845 | 0.833 | 85 | 16 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.410 | 0.485 | 0.470 | 49 | 52 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.758 | 0.830 | 0.817 | 84 | 18 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.501 | 0.580 | 0.564 | 59 | 43 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.170 | 0.240 | 0.225 | 25 | 77 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.247 | 0.315 | 0.301 | 32 | 69 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.123 | 0.185 | 0.171 | 19 | 82 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.152 | 0.220 | 0.205 | 23 | 79 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.763 | 0.830 | 0.818 | 84 | 18 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.338 | 0.405 | 0.391 | 41 | 60 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.744 | 0.805 | 0.794 | 81 | 20 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.734 | 0.800 | 0.788 | 81 | 21 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.530 | 0.595 | 0.582 | 60 | 41 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT20LAWSH-5 | game_total | 0.705 | 0.765 | 0.754 | 77 | 24 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.262 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.384 | 0.445 | 0.433 | 45 | 56 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.524 | 0.585 | 0.573 | 59 | 42 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.159 | 0.225 | 0.211 | 24 | 79 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.555 | 0.620 | 0.607 | 63 | 39 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.752 | 0.810 | 0.799 | 82 | 20 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.350 | 0.295 | 0.306 | 30 | 71 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.408 | 0.470 | 0.457 | 48 | 54 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.702 | 0.755 | 0.745 | 76 | 25 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.512 | 0.455 | 0.466 | 46 | 55 | yes | +0.035 | OK |
| KXNHLGAME-26OCT20TBVGK-VGK | game_winner | 0.552 | 0.495 | 0.506 | 50 | 51 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR5 | team_total | 0.320 | 0.380 | 0.368 | 39 | 63 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.292 | 0.350 | 0.338 | 36 | 66 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.521 | 0.580 | 0.568 | 59 | 43 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20LAWSH-4 | game_total | 0.800 | 0.850 | 0.841 | 86 | 16 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.226 | 0.275 | 0.265 | 28 | 73 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2 | team_total | 0.885 | 0.925 | 0.918 | 93 | 8 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.130 | 0.180 | 0.169 | 19 | 83 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT20SJMTL-9 | game_total | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5 | team_total | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.169 | 0.225 | 0.213 | 24 | 79 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-CBJ2 | game_spread | 0.415 | 0.365 | 0.375 | 37 | 64 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR3 | game_spread | 0.093 | 0.135 | 0.126 | 14 | 87 | no | +0.029 | OK |
| KXNHLGAME-26OCT20SJMTL-SJ | game_winner | 0.394 | 0.345 | 0.354 | 35 | 66 | yes | +0.028 | OK |
| KXNHLGAME-26OCT20SJMTL-MTL | game_winner | 0.607 | 0.655 | 0.646 | 66 | 35 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR3 | team_total | 0.731 | 0.780 | 0.771 | 79 | 23 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4 | team_total | 0.300 | 0.250 | 0.260 | 26 | 76 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR4 | team_total | 0.526 | 0.575 | 0.565 | 58 | 43 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.773 | 0.825 | 0.815 | 84 | 19 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT20LAWSH-7 | game_total | 0.367 | 0.420 | 0.409 | 43 | 59 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB3 | game_spread | 0.134 | 0.180 | 0.170 | 19 | 83 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20WPGSTL-WPG3 | game_spread | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.025 | OK |
| KXNHLGAME-26OCT20TORCBJ-CBJ | game_winner | 0.642 | 0.595 | 0.605 | 60 | 41 | yes | +0.025 | OK |
| KXNHLGAME-26OCT20TORCBJ-TOR | game_winner | 0.358 | 0.405 | 0.395 | 41 | 60 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT20CARVAN-VAN2 | game_spread | 0.173 | 0.130 | 0.138 | 14 | 88 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.712 | 0.755 | 0.747 | 76 | 25 | no | +0.025 | OK |

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
| TBL @ VGK | 0.552 | 0.581 | 0.182 | 0.213 | 5.95 | 6.11 | 1.003/0.958 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK4 +0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 18c · p 0.2343 (adj 0.2182) · $3.16 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 16c · p 0.1978 (adj 0.1871) · $1.92 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 1+ goals NO @ 55c · p 0.602 (adj 0.5877) · $4.78 · thesis MTL:SUPPRESSED
- Zachary Bolduc: 1+ goals NO @ 76c · p 0.8023 (adj 0.788) · $6.94 · thesis MTL:SUPPRESSED
- Fedor Svechkov: 1+ goals YES @ 8c · p 0.1194 (adj 0.1083) · $2.25 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ assists NO @ 44c · p 0.6063 (adj 0.495) · $7.21 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 64c · p 0.696 (adj 0.6795) · $6.73 · thesis NJD:SUPPRESSED
- Parker Kelly: 1+ goals YES @ 10c · p 0.128 (adj 0.1197) · $1.48 · thesis COL:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 12c · p 0.2071 (adj 0.1828) · $5.34 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 11c · p 0.1361 (adj 0.1283) · $1.11 · thesis ANA:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0652 (adj 0.0576) · $1.34 · thesis LAK:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 19c · p 0.2379 (adj 0.2222) · $2.45 · thesis WSH:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 53c · p 0.639 (adj 0.5584) · $3.09 · thesis LAK:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 19c · p 0.2306 (adj 0.218) · $2.29 · thesis CBJ:WINS_BY_2PLUS
- Jack Roslovic: 1+ goals NO @ 76c · p 0.8019 (adj 0.7902) · $6.5 · thesis TOR:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 25c · p 0.2949 (adj 0.2812) · $2.79 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4725 (adj 0.4337) · $3.49 · thesis GAME:LOW_EVENT
- Morgan Barron: 1+ goals YES @ 5c · p 0.1242 (adj 0.1044) · $3.93 · thesis WPG:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 81c · p 0.8565 (adj 0.8436) · $7.82 · thesis STL:SUPPRESSED
- Philip Broberg: 1+ assists YES @ 33c · p 0.4045 (adj 0.3648) · $2.98 · thesis STL:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 28c · p 0.3158 (adj 0.3044) · $1.26 · thesis WPG:OFFENSE_4PLUS
- Morgan Geekie: 1+ goals YES @ 24c · p 0.299 (adj 0.283) · $3.19 · thesis BOS:OFFENSE_4PLUS
- Boston over 2.5 goals scored YES @ 51c · p 0.5954 (adj 0.5502) · $1.97 · thesis BOS:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8096 (adj 0.7773) · $3.04 · thesis BOS:WINS
- Alex Formenton: 1+ goals YES @ 14c · p 0.1915 (adj 0.1749) · $2.85 · thesis EDM:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 31c · p 0.3697 (adj 0.3535) · $4.5 · thesis EDM:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 58c · p 0.6268 (adj 0.6139) · $4.17 · thesis MIN:SUPPRESSED
- Connor McDavid: 2+ assists NO @ 68c · p 0.7811 (adj 0.7056) · $6.43 · thesis EDM:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1648 (adj 0.1548) · $1.67 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 12c · p 0.1526 (adj 0.1432) · $1.53 · thesis SEA:OFFENSE_4PLUS
- Detroit wins by over 1.5 goals NO @ 71c · p 0.7832 (adj 0.7441) · $5.66 · thesis SEA:WINS
- Michael Rasmussen: 1+ goals NO @ 85c · p 0.8823 (adj 0.873) · $7.82 · thesis DET:SUPPRESSED
- Carolina wins by over 1.5 goals NO @ 48c · p 0.6564 (adj 0.5385) · $3.17 · thesis VAN:WINS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7748 (adj 0.6709) · $3.6 · thesis VAN:WINS
- Vancouver over 1.5 goals scored YES @ 71c · p 0.799 (adj 0.752) · $4.95 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.6848 (adj 0.6661) · $5.99 · thesis CAR:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 71c · p 0.7917 (adj 0.7484) · $7.55 · thesis VGK:WINS
- Tampa Bay over 3.5 goals scored NO @ 60c · p 0.6849 (adj 0.6374) · $2.0 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 148/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.0, exp saves 23.52 (sd 6.46), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.28 (sd 6.61), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.487 | 0.595 | 62/43 | +0.066 | STANDARD |
| Nick Suzuki: 2+ points | 0.286 | 0.380 | 40/64 | +0.057 | STANDARD |
| Ivar Stenberg: 1+ points | 0.343 | 0.425 | 44/59 | +0.050 | PRIOR_HEAVY |
| Chris Kreider: 1+ points | 0.401 | 0.475 | 50/55 | +0.032 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.208 | 0.275 | 29/74 | +0.039 | PRIOR_HEAVY |
| Mason Marchment: 1+ goals | 0.234 | 0.170 | 18/84 | +0.044 | STANDARD |

**COL @ NJD** · priced 182/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 29.27, exp saves 25.3 (sd 6.78), pull risk 0.06
- COL net: Scott Wedgewood (PROJECTED) exp shots 28.54, exp saves 24.74 (sd 6.73), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.162 | 0.335 | 36/69 | +0.133 | STANDARD |
| Cale Makar: 1+ assists | 0.394 | 0.565 | 57/44 | +0.149 | STANDARD |
| Jack Hughes: 1+ assists | 0.382 | 0.540 | 55/47 | +0.131 | STANDARD |
| Cale Makar: 1+ points | 0.491 | 0.645 | 66/37 | +0.122 | STANDARD |
| Luke Evangelista: 1+ points | 0.332 | 0.485 | 51/54 | +0.111 | STANDARD |
| Jack Hughes: 2+ points | 0.207 | 0.345 | 37/68 | +0.098 | STANDARD |

**ANA @ NYI** · priced 145/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.2, exp saves 24.6 (sd 6.61), pull risk 0.056
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.47), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.207 | 0.110 | 12/90 | +0.080 | STANDARD |
| Jean-Gabriel Pageau: 1+ goals | 0.199 | 0.130 | 17/91 | +0.019 | STANDARD |
| Tim Washe: 1+ goals | 0.125 | 0.070 | 10/96 | +0.019 | STANDARD |
| Ondrej Palat: 1+ goals | 0.168 | 0.115 | 15/92 | +0.009 | STANDARD |
| Victor Eklund: 1+ points | 0.362 | 0.415 | 44/61 | +0.011 | PRIOR_HEAVY |
| Brayden Schenn: 1+ assists | 0.326 | 0.375 | 38/63 | +0.027 | STANDARD |

**LAK @ WSH** · priced 158/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.19, exp saves 24.61 (sd 6.48), pull risk 0.044
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.88, exp saves 22.97 (sd 6.35), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.361 | 0.485 | 50/53 | +0.092 | STANDARD |
| Artemi Panarin: 1+ points | 0.544 | 0.630 | 65/39 | +0.049 | STANDARD |
| Alex Laferriere: 1+ points | 0.518 | 0.435 | 45/58 | +0.050 | STANDARD |
| Alex Laferriere: 1+ assists | 0.342 | 0.260 | 28/76 | +0.047 | STANDARD |
| Artemi Panarin: 2+ points | 0.189 | 0.270 | 29/75 | +0.048 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.275 | 0.350 | 37/67 | +0.039 | STANDARD |

**TOR @ CBJ** · priced 145/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 25.9, exp saves 22.9 (sd 6.19), pull risk 0.043
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.76 (sd 7.19), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.344 | 0.470 | 49/55 | +0.089 | STANDARD |
| Gavin McKenna: 1+ points | 0.333 | 0.435 | 45/58 | +0.070 | STANDARD |
| Auston Matthews: 1+ points | 0.556 | 0.655 | 67/36 | +0.068 | STANDARD |
| Auston Matthews: 2+ points | 0.197 | 0.285 | 32/75 | +0.040 | STANDARD |
| Darren Raddysh: 1+ assists | 0.329 | 0.415 | 43/60 | +0.054 | STANDARD |
| Kirill Marchenko: 1+ points | 0.464 | 0.545 | 56/47 | +0.048 | STANDARD |

**WPG @ STL** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.09, exp saves 22.87 (sd 6.23), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.62, exp saves 22.62 (sd 6.49), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Philip Broberg: 1+ points | 0.465 | 0.360 | 38/66 | +0.068 | STANDARD |
| Philip Broberg: 1+ assists | 0.405 | 0.325 | 33/68 | +0.059 | STANDARD |
| Pavel Buchnevich: 1+ assists | 0.251 | 0.330 | 35/69 | +0.044 | STANDARD |
| Morgan Barron: 1+ goals | 0.124 | 0.045 | 5/96 | +0.071 | STANDARD |
| Mason McTavish: 1+ assists | 0.269 | 0.345 | 36/67 | +0.045 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.597 | 0.535 | 55/48 | +0.030 | STANDARD |

**BOS @ DAL** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.27 (sd 5.98), pull risk 0.057
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.85, exp saves 24.06 (sd 6.49), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.231 | 0.325 | 34/69 | +0.064 | STANDARD |
| Roope Hintz: 1+ assists | 0.321 | 0.405 | 43/62 | +0.043 | STANDARD |
| Miro Heiskanen: 1+ points | 0.467 | 0.550 | 56/46 | +0.055 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.447 | 0.525 | 54/49 | +0.045 | STANDARD |
| Tyler Seguin: 1+ assists | 0.204 | 0.280 | 30/74 | +0.043 | STANDARD |
| David Pastrnak: 1+ assists | 0.437 | 0.510 | 53/51 | +0.036 | STANDARD |

**MIN @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.28 (sd 6.69), pull risk 0.064
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.81 (sd 7.09), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kasperi Kapanen: 1+ assists | 0.312 | 0.180 | 20/84 | +0.101 | STANDARD |
| Connor McDavid: 2+ assists | 0.219 | 0.335 | 35/68 | +0.086 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.487 | 0.600 | 61/41 | +0.086 | STANDARD |
| Leon Draisaitl: 1+ points | 0.700 | 0.590 | 77/59 | -0.082 | STANDARD |
| Leon Draisaitl: 2+ points | 0.332 | 0.440 | 46/58 | +0.071 | STANDARD |
| Connor McDavid: 2+ points | 0.425 | 0.530 | 54/48 | +0.078 | STANDARD |

**DET @ SEA** · priced 148/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.42, exp saves 25.69 (sd 6.74), pull risk 0.05
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.84 (sd 6.46), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Moritz Seider: 1+ points | 0.454 | 0.595 | 61/42 | +0.109 | STANDARD |
| Moritz Seider: 2+ points | 0.130 | 0.245 | 28/79 | +0.069 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.354 | 0.240 | 28/80 | +0.060 | STANDARD |
| Kaapo Kakko: 1+ goals | 0.212 | 0.110 | 19/97 | +0.011 | STANDARD |
| Berkly Catton: 1+ goals | 0.209 | 0.110 | 19/97 | +0.008 | STANDARD |
| Bobby McMann: 1+ goals | 0.271 | 0.175 | 32/97 | -0.065 | STANDARD |

**CAR @ VAN** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 32.33, exp saves 27.7 (sd 7.44), pull risk 0.074
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.8, exp saves 19.88 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Martinook: 1+ points | 0.367 | 0.200 | 36/96 | -0.009 | STANDARD |
| Filip Chytil: 1+ goals | 0.245 | 0.110 | 17/95 | +0.066 | STANDARD |
| Sebastian Aho: 2+ points | 0.219 | 0.340 | 36/68 | +0.085 | STANDARD |
| Linus Karlsson: 1+ goals | 0.232 | 0.115 | 19/96 | +0.031 | STANDARD |
| Brock Boeser: 1+ goals | 0.251 | 0.135 | 25/98 | -0.012 | STANDARD |
| Sebastian Aho: 1+ assists | 0.396 | 0.500 | 51/51 | +0.076 | STANDARD |

**TBL @ VGK** · priced 158/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.99, exp saves 23.65 (sd 6.38), pull risk 0.049
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.35, exp saves 22.53 (sd 6.4), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mark Stone: 1+ goals | 0.327 | 0.185 | 33/96 | -0.018 | STANDARD |
| John Carlson: 1+ points | 0.335 | 0.465 | 48/55 | +0.098 | STANDARD |
| Brett Howden: 1+ goals | 0.236 | 0.110 | 20/98 | +0.025 | STANDARD |
| John Carlson: 1+ assists | 0.270 | 0.395 | 42/63 | +0.084 | STANDARD |
| Tomas Hertl: 1+ goals | 0.270 | 0.145 | 27/98 | -0.014 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.443 | 0.565 | 59/46 | +0.080 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
