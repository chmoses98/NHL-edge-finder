# NHL slate 2026-10-20 — RESEARCH_ONLY

generated 2026-10-20T15:48:10Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4278 · contracts joined: 2381 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2106, 'OK': 182, 'NO_EDGE': 93}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 332, 'game_early_goal': 11, 'first_goal': 377, 'game_winner': 22, 'player_goals': 685, 'game_overtime': 11, 'player_points': 418, 'game_spread': 44, 'team_total': 110, 'game_total': 99, 'goalie_saves': 8}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 2026-10-20T23:00:00Z | T-6h | 0.605 | 0.395 | 0.177 | 6.17 | 3.42 | 2.75 | 209 (25/184) | CONFIRMED/PROBABLE |
| COL @ NJD | 2026-10-20T23:00:00Z | T-6h | 0.456 | 0.544 | 0.180 | 5.79 | 2.77 | 3.02 | 239 (25/214) | CONFIRMED/CONFIRMED |
| ANA @ NYI | 2026-10-20T23:00:00Z | T-6h | 0.616 | 0.384 | 0.172 | 5.98 | 3.35 | 2.63 | 201 (25/176) | CONFIRMED/CONFIRMED |
| LAK @ WSH | 2026-10-20T23:00:00Z | T-6h | 0.620 | 0.380 | 0.185 | 5.60 | 3.15 | 2.44 | 225 (25/200) | CONFIRMED/PROJECTED |
| TOR @ CBJ | 2026-10-20T23:00:00Z | T-6h | 0.648 | 0.352 | 0.160 | 6.19 | 3.58 | 2.62 | 211 (25/186) | CONFIRMED/CONFIRMED |
| WPG @ STL | 2026-10-21T00:00:00Z | T-6h | 0.601 | 0.399 | 0.183 | 5.96 | 3.30 | 2.67 | 222 (25/197) | PROJECTED/PROJECTED |
| BOS @ DAL | 2026-10-21T00:00:00Z | T-6h | 0.512 | 0.488 | 0.182 | 5.69 | 2.89 | 2.80 | 213 (25/188) | PROJECTED/PROJECTED |
| MIN @ EDM | 2026-10-21T01:00:00Z | T-6h | 0.568 | 0.432 | 0.171 | 6.42 | 3.42 | 3.00 | 229 (25/204) | PROJECTED/PROJECTED |
| DET @ SEA | 2026-10-21T01:40:00Z | T-6h | 0.581 | 0.419 | 0.176 | 6.02 | 3.26 | 2.77 | 209 (25/184) | PROJECTED/CONFIRMED |
| CAR @ VAN | 2026-10-21T02:00:00Z | T-6h | 0.349 | 0.651 | 0.162 | 6.44 | 2.72 | 3.72 | 211 (25/186) | PROJECTED/PROJECTED |
| TBL @ VGK | 2026-10-21T02:30:00Z | T-6h | 0.552 | 0.448 | 0.182 | 5.95 | 3.13 | 2.82 | 212 (25/187) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT20COLNJ-7 | game_total | 0.378 | 0.485 | 0.463 | 49 | 52 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ4 | team_total | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT20COLNJ-5 | game_total | 0.718 | 0.815 | 0.798 | 82 | 19 | no | +0.081 | OK |
| KXNHLTOTAL-26OCT20COLNJ-6 | game_total | 0.493 | 0.595 | 0.575 | 60 | 41 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET3 | team_total | 0.523 | 0.630 | 0.609 | 64 | 38 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 | team_total | 0.526 | 0.630 | 0.610 | 64 | 38 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL4 | team_total | 0.337 | 0.435 | 0.415 | 44 | 57 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET4 | team_total | 0.312 | 0.415 | 0.393 | 43 | 60 | no | +0.072 | OK |
| KXNHLGAME-26OCT20BOSDAL-BOS | game_winner | 0.488 | 0.395 | 0.413 | 40 | 61 | yes | +0.071 | OK |
| KXNHLGAME-26OCT20BOSDAL-DAL | game_winner | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL3 | game_spread | 0.166 | 0.255 | 0.235 | 26 | 75 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR2 | game_spread | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT20SJMTL-7 | game_total | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL3 | team_total | 0.557 | 0.650 | 0.632 | 66 | 36 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3 | team_total | 0.487 | 0.580 | 0.562 | 59 | 43 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL4 | team_total | 0.457 | 0.550 | 0.532 | 56 | 46 | no | +0.065 | OK |
| KXNHLGAME-26OCT20CARVAN-CAR | game_winner | 0.651 | 0.735 | 0.719 | 74 | 27 | no | +0.065 | OK |
| KXNHLGAME-26OCT20DETSEA-DET | game_winner | 0.419 | 0.505 | 0.488 | 51 | 50 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT20SJMTL-6 | game_total | 0.553 | 0.635 | 0.619 | 64 | 37 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5 | team_total | 0.266 | 0.355 | 0.336 | 37 | 66 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT20LAWSH-5 | game_total | 0.690 | 0.765 | 0.751 | 77 | 24 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 | team_total | 0.446 | 0.525 | 0.509 | 53 | 48 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT20CARVAN-CAR3 | game_spread | 0.297 | 0.380 | 0.363 | 39 | 63 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ5 | team_total | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET5 | team_total | 0.152 | 0.230 | 0.212 | 24 | 78 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-DAL2 | game_spread | 0.288 | 0.370 | 0.353 | 38 | 64 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR4 | team_total | 0.278 | 0.360 | 0.343 | 37 | 65 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT20DETSEA-7 | game_total | 0.417 | 0.495 | 0.479 | 50 | 51 | no | +0.055 | OK |
| KXNHLGAME-26OCT20CARVAN-VAN | game_winner | 0.349 | 0.275 | 0.289 | 28 | 73 | yes | +0.055 | OK |
| KXNHLGAME-26OCT20DETSEA-SEA | game_winner | 0.581 | 0.505 | 0.520 | 51 | 50 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT20COLNJ-8 | game_total | 0.203 | 0.275 | 0.259 | 28 | 73 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR2 | team_total | 0.726 | 0.800 | 0.786 | 81 | 21 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL2 | team_total | 0.778 | 0.845 | 0.833 | 85 | 16 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL3 | team_total | 0.674 | 0.750 | 0.736 | 76 | 26 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20DETSEA-DET2 | team_total | 0.758 | 0.830 | 0.817 | 84 | 18 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB4 | team_total | 0.322 | 0.405 | 0.388 | 42 | 61 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT20SJMTL-5 | game_total | 0.769 | 0.835 | 0.823 | 84 | 17 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL3 | game_spread | 0.245 | 0.315 | 0.300 | 32 | 69 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT20COLNJ-NJ2 | team_total | 0.760 | 0.830 | 0.817 | 84 | 18 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT20LAWSH-7 | game_total | 0.344 | 0.415 | 0.401 | 42 | 59 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT20COLNJ-4 | game_total | 0.814 | 0.880 | 0.869 | 89 | 13 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT20BOSDAL-DAL5 | team_total | 0.170 | 0.240 | 0.225 | 25 | 77 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT20DETSEA-DET3 | game_spread | 0.123 | 0.185 | 0.171 | 19 | 82 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT20LAWSH-6 | game_total | 0.456 | 0.530 | 0.515 | 54 | 48 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB2 | team_total | 0.763 | 0.825 | 0.814 | 83 | 18 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ3 | game_spread | 0.135 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA2 | team_total | 0.692 | 0.755 | 0.743 | 76 | 25 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB3 | team_total | 0.539 | 0.610 | 0.596 | 62 | 40 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT20DETSEA-6 | game_total | 0.530 | 0.595 | 0.582 | 60 | 41 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT20SJMTL-MTL2 | game_spread | 0.381 | 0.445 | 0.432 | 45 | 56 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT20SJMTL-4 | game_total | 0.852 | 0.905 | 0.896 | 91 | 10 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT20COLNJ-NJ2 | game_spread | 0.244 | 0.305 | 0.292 | 31 | 70 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20SJMTL-8 | game_total | 0.254 | 0.320 | 0.306 | 33 | 69 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT20TBVGK-5 | game_total | 0.739 | 0.800 | 0.789 | 81 | 21 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT20TBVGK-TB2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR2 | game_spread | 0.171 | 0.225 | 0.213 | 23 | 78 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT20LAWSH-4 | game_total | 0.794 | 0.850 | 0.840 | 86 | 16 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT20DETSEA-5 | game_total | 0.752 | 0.810 | 0.799 | 82 | 20 | no | +0.036 | OK |
| KXNHLGAME-26OCT20COLNJ-COL | game_winner | 0.544 | 0.485 | 0.497 | 49 | 52 | yes | +0.036 | OK |
| KXNHLGAME-26OCT20COLNJ-NJ | game_winner | 0.456 | 0.515 | 0.503 | 52 | 49 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT20LAWSH-LA4 | team_total | 0.240 | 0.300 | 0.287 | 31 | 71 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT20DETSEA-SEA2 | game_spread | 0.350 | 0.295 | 0.306 | 30 | 71 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT20TBVGK-7 | game_total | 0.408 | 0.465 | 0.453 | 47 | 54 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT20BOSDAL-5 | game_total | 0.702 | 0.755 | 0.745 | 76 | 25 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3 | team_total | 0.512 | 0.455 | 0.466 | 46 | 55 | yes | +0.035 | OK |
| KXNHLGAME-26OCT20TBVGK-VGK | game_winner | 0.552 | 0.495 | 0.506 | 50 | 51 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-CBJ2 | game_spread | 0.429 | 0.375 | 0.386 | 38 | 63 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT20TORCBJ-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20COLNJ-9 | game_total | 0.138 | 0.190 | 0.178 | 20 | 82 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL6 | team_total | 0.128 | 0.180 | 0.168 | 19 | 83 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT20SJMTL-MTL2 | team_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT20TBVGK-6 | game_total | 0.521 | 0.575 | 0.564 | 58 | 43 | no | +0.031 | OK |
| KXNHLGAME-26OCT20TORCBJ-CBJ | game_winner | 0.648 | 0.595 | 0.606 | 60 | 41 | yes | +0.031 | OK |
| KXNHLGAME-26OCT20TORCBJ-TOR | game_winner | 0.352 | 0.405 | 0.394 | 41 | 60 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2 | team_total | 0.885 | 0.925 | 0.918 | 93 | 8 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT20BOSDAL-BOS2 | game_spread | 0.262 | 0.215 | 0.224 | 22 | 79 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT20SJMTL-9 | game_total | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT20TBVGK-TB5 | team_total | 0.159 | 0.210 | 0.199 | 22 | 80 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5 | team_total | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ MTL | 0.605 | 0.610 | 0.177 | 0.206 | 6.17 | 6.25 | 0.943/1.024 | KXNHLTOTAL-26OCT20SJMTL-7 +0.016 |
| COL @ NJD | 0.456 | 0.483 | 0.180 | 0.219 | 5.79 | 6.15 | 0.984/0.971 | KXNHLTEAMTOTAL-26OCT20COLNJ-NJ3 +0.066 |
| ANA @ NYI | 0.616 | 0.578 | 0.172 | 0.215 | 5.98 | 6.36 | 0.947/1.016 | KXNHLTOTAL-26OCT20ANANYI-7 +0.074 |
| LAK @ WSH | 0.620 | 0.575 | 0.185 | 0.222 | 5.60 | 5.88 | 0.938/0.989 | KXNHLTEAMTOTAL-26OCT20LAWSH-LA3 +0.065 |
| TOR @ CBJ | 0.648 | 0.620 | 0.160 | 0.217 | 6.19 | 5.99 | 0.946/0.956 | KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ5 -0.049 |
| WPG @ STL | 0.601 | 0.582 | 0.183 | 0.221 | 5.96 | 6.22 | 0.993/0.988 | KXNHLTOTAL-26OCT20WPGSTL-7 +0.046 |
| BOS @ DAL | 0.512 | 0.537 | 0.182 | 0.219 | 5.69 | 6.22 | 0.986/0.968 | KXNHLTOTAL-26OCT20BOSDAL-7 +0.091 |
| MIN @ EDM | 0.568 | 0.595 | 0.171 | 0.206 | 6.42 | 6.68 | 0.994/0.995 | KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4 +0.054 |
| DET @ SEA | 0.581 | 0.575 | 0.176 | 0.210 | 6.02 | 6.24 | 1.015/1.024 | KXNHLTOTAL-26OCT20DETSEA-7 +0.041 |
| CAR @ VAN | 0.349 | 0.442 | 0.162 | 0.216 | 6.44 | 6.50 | 1.026/0.997 | KXNHLSPREAD-26OCT20CARVAN-CAR2 -0.097 |
| TBL @ VGK | 0.552 | 0.581 | 0.182 | 0.213 | 5.95 | 6.11 | 1.003/0.958 | KXNHLTEAMTOTAL-26OCT20TBVGK-VGK4 +0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Mason Marchment: 1+ goals YES @ 18c · p 0.2285 (adj 0.2151) · $2.9 · thesis SJS:OFFENSE_4PLUS
- Cole Caufield: 1+ goals NO @ 54c · p 0.6047 (adj 0.5873) · $5.34 · thesis MTL:SUPPRESSED
- Zachary Bolduc: 1+ goals NO @ 76c · p 0.8044 (adj 0.7895) · $6.03 · thesis MTL:SUPPRESSED
- Full Game: Over 5.5 goals scored NO @ 37c · p 0.4345 (adj 0.3997) · $1.54 · thesis GAME:LOW_EVENT
- Fedor Svechkov: 1+ goals YES @ 8c · p 0.1156 (adj 0.1042) · $1.83 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ assists NO @ 44c · p 0.6011 (adj 0.4899) · $6.26 · thesis COL:SUPPRESSED
- Parker Kelly: 1+ goals YES @ 9c · p 0.1252 (adj 0.1152) · $1.93 · thesis COL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 65c · p 0.7039 (adj 0.6892) · $6.77 · thesis NJD:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 12c · p 0.2121 (adj 0.1878) · $5.67 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.129 (adj 0.1192) · $1.32 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 11c · p 0.1365 (adj 0.1286) · $1.16 · thesis ANA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2379 (adj 0.2209) · $3.3 · thesis WSH:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 4c · p 0.062 (adj 0.0553) · $1.14 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 53c · p 0.6428 (adj 0.5597) · $3.14 · thesis LAK:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 31c · p 0.3723 (adj 0.3362) · $1.28 · thesis WSH:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8464 (adj 0.8336) · $7.58 · thesis TOR:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 19c · p 0.2327 (adj 0.2195) · $2.34 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4777 (adj 0.4364) · $2.97 · thesis GAME:LOW_EVENT
- Toronto over 3.5 goals scored NO @ 65c · p 0.7242 (adj 0.6821) · $1.3 · thesis TOR:SUPPRESSED
- Morgan Barron: 1+ goals YES @ 6c · p 0.1242 (adj 0.1069) · $3.48 · thesis WPG:OFFENSE_4PLUS
- Dalibor Dvorsky: 1+ goals NO @ 82c · p 0.8565 (adj 0.8461) · $7.58 · thesis STL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 25c · p 0.2935 (adj 0.2801) · $2.12 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 15c · p 0.1832 (adj 0.1724) · $1.39 · thesis STL:OFFENSE_4PLUS
- Morgan Geekie: 1+ goals YES @ 25c · p 0.299 (adj 0.2855) · $2.49 · thesis BOS:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7298 (adj 0.7148) · $5.89 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8096 (adj 0.7773) · $3.32 · thesis BOS:WINS
- Alex Formenton: 1+ goals YES @ 14c · p 0.1915 (adj 0.1761) · $2.96 · thesis EDM:OFFENSE_4PLUS
- Quinn Hughes: 1+ assists NO @ 39c · p 0.4831 (adj 0.434) · $4.3 · thesis MIN:SUPPRESSED
- Zach Hyman: 1+ goals YES @ 32c · p 0.3697 (adj 0.3548) · $3.34 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 68c · p 0.7811 (adj 0.7121) · $7.58 · thesis EDM:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1648 (adj 0.1523) · $2.37 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1526 (adj 0.1407) · $2.24 · thesis SEA:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 18c · p 0.2226 (adj 0.2107) · $2.05 · thesis SEA:OFFENSE_4PLUS
- Detroit wins by over 1.5 goals NO @ 71c · p 0.7832 (adj 0.7441) · $4.46 · thesis SEA:WINS
- Drew O'Connor: 1+ goals YES @ 12c · p 0.1732 (adj 0.1562) · $2.39 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 48c · p 0.6564 (adj 0.5385) · $5.42 · thesis VAN:WINS
- Vancouver over 1.5 goals scored YES @ 71c · p 0.799 (adj 0.752) · $4.85 · thesis VAN:WINS
- Sebastian Aho: 1+ goals NO @ 63c · p 0.6848 (adj 0.6673) · $4.51 · thesis CAR:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 71c · p 0.7917 (adj 0.7484) · $7.05 · thesis VGK:WINS
- Brett Howden: 1+ goals YES @ 19c · p 0.2358 (adj 0.2206) · $1.92 · thesis VGK:OFFENSE_4PLUS
- Nikita Kucherov: 1+ goals NO @ 64c · p 0.6842 (adj 0.6706) · $2.77 · thesis TBL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ MTL** · priced 148/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 27.0, exp saves 23.53 (sd 6.48), pull risk 0.053
- SJS net: Alex Nedeljkovic (PROBABLE) exp shots 27.29, exp saves 23.18 (sd 6.64), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.480 | 0.595 | 61/42 | +0.083 | STANDARD |
| Nick Suzuki: 2+ points | 0.278 | 0.385 | 40/63 | +0.076 | STANDARD |
| Nick Suzuki: 1+ points | 0.649 | 0.735 | 75/28 | +0.057 | STANDARD |
| Ivar Stenberg: 1+ points | 0.342 | 0.420 | 43/59 | +0.051 | PRIOR_HEAVY |
| Chris Kreider: 1+ points | 0.393 | 0.470 | 49/55 | +0.040 | STANDARD |
| Cole Caufield: 1+ goals | 0.395 | 0.465 | 47/54 | +0.047 | STANDARD |

**COL @ NJD** · priced 182/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 29.27, exp saves 25.27 (sd 6.74), pull risk 0.061
- COL net: Scott Wedgewood (CONFIRMED) exp shots 28.54, exp saves 24.76 (sd 6.74), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.399 | 0.570 | 58/44 | +0.144 | STANDARD |
| Luke Evangelista: 1+ assists | 0.155 | 0.320 | 34/70 | +0.130 | STANDARD |
| Jack Hughes: 1+ assists | 0.389 | 0.535 | 54/47 | +0.124 | STANDARD |
| Scott Wedgewood: 28+ saves | 0.330 | 0.475 | 50/55 | +0.103 |  |
| Cale Makar: 1+ points | 0.496 | 0.640 | 65/37 | +0.118 | STANDARD |
| Cale Makar: 2+ points | 0.147 | 0.290 | 30/72 | +0.119 | STANDARD |

**ANA @ NYI** · priced 147/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.2, exp saves 24.63 (sd 6.66), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.37, exp saves 23.37 (sd 6.6), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lukas Dostal: 27+ saves | 0.310 | 0.430 | 48/62 | +0.054 |  |
| Ilya Sorokin: 23+ saves | 0.624 | 0.510 | 53/51 | +0.076 |  |
| A.J. Greer: 1+ goals | 0.212 | 0.115 | 12/89 | +0.085 | STANDARD |
| Beckett Sennecke: 2+ points | 0.200 | 0.145 | 20/91 | -0.011 | STANDARD |
| Victor Eklund: 1+ points | 0.357 | 0.410 | 43/61 | +0.017 | PRIOR_HEAVY |
| Jackson LaCombe: 1+ points | 0.548 | 0.495 | 50/51 | +0.031 | STANDARD |

**LAK @ WSH** · priced 164/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.19, exp saves 24.65 (sd 6.55), pull risk 0.045
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.88, exp saves 23.01 (sd 6.32), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.357 | 0.485 | 50/53 | +0.095 | STANDARD |
| Matt Roy: 1+ assists | 0.153 | 0.245 | 27/78 | +0.055 | STANDARD |
| Artemi Panarin: 1+ points | 0.536 | 0.620 | 64/40 | +0.048 | STANDARD |
| Alex Laferriere: 1+ points | 0.510 | 0.430 | 45/59 | +0.042 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.266 | 0.345 | 36/67 | +0.049 | STANDARD |
| Ryan Leonard: 1+ assists | 0.372 | 0.300 | 31/71 | +0.047 | STANDARD |

**TOR @ CBJ** · priced 146/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.9, exp saves 22.95 (sd 6.05), pull risk 0.037
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.4, exp saves 26.78 (sd 7.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.339 | 0.455 | 46/55 | +0.094 | STANDARD |
| Auston Matthews: 1+ points | 0.554 | 0.650 | 66/36 | +0.070 | STANDARD |
| Kirill Marchenko: 1+ points | 0.454 | 0.545 | 55/46 | +0.069 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.272 | 0.360 | 37/65 | +0.062 | STANDARD |
| Gavin McKenna: 1+ points | 0.337 | 0.425 | 44/59 | +0.056 | STANDARD |
| Jet Greaves: 25+ saves | 0.385 | 0.470 | 49/55 | +0.048 |  |

**WPG @ STL** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.09, exp saves 22.87 (sd 6.23), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.62, exp saves 22.62 (sd 6.49), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Philip Broberg: 1+ points | 0.465 | 0.365 | 38/65 | +0.068 | STANDARD |
| Philip Broberg: 1+ assists | 0.405 | 0.315 | 33/70 | +0.059 | STANDARD |
| Pavel Buchnevich: 1+ assists | 0.251 | 0.330 | 35/69 | +0.044 | STANDARD |
| Mason McTavish: 1+ assists | 0.269 | 0.340 | 36/68 | +0.036 | STANDARD |
| Morgan Barron: 1+ goals | 0.124 | 0.055 | 6/95 | +0.060 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.597 | 0.535 | 55/48 | +0.030 | STANDARD |

**BOS @ DAL** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.49, exp saves 21.27 (sd 5.98), pull risk 0.057
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.85, exp saves 24.06 (sd 6.49), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.231 | 0.325 | 34/69 | +0.064 | STANDARD |
| Miro Heiskanen: 1+ points | 0.467 | 0.550 | 56/46 | +0.055 | STANDARD |
| Roope Hintz: 2+ points | 0.163 | 0.245 | 26/77 | +0.055 | STANDARD |
| Tyler Seguin: 1+ assists | 0.204 | 0.285 | 30/73 | +0.052 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.447 | 0.525 | 54/49 | +0.045 | STANDARD |
| Morgan Geekie: 1+ points | 0.541 | 0.465 | 48/55 | +0.044 | STANDARD |

**MIN @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.88, exp saves 24.28 (sd 6.69), pull risk 0.064
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.26, exp saves 24.81 (sd 7.09), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kasperi Kapanen: 1+ assists | 0.312 | 0.190 | 22/84 | +0.080 | STANDARD |
| Connor McDavid: 1+ assists | 0.587 | 0.695 | 71/32 | +0.078 | STANDARD |
| Connor McDavid: 2+ assists | 0.219 | 0.325 | 33/68 | +0.086 | STANDARD |
| Leon Draisaitl: 2+ points | 0.332 | 0.435 | 45/58 | +0.071 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.487 | 0.590 | 60/42 | +0.076 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.420 | 0.320 | 33/69 | +0.074 | STANDARD |

**DET @ SEA** · priced 149/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.42, exp saves 25.69 (sd 6.74), pull risk 0.05
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.75, exp saves 22.84 (sd 6.46), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Moritz Seider: 1+ points | 0.454 | 0.590 | 60/42 | +0.109 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.354 | 0.235 | 27/80 | +0.070 | STANDARD |
| Moritz Seider: 2+ points | 0.130 | 0.245 | 27/78 | +0.078 | STANDARD |
| Moritz Seider: 1+ assists | 0.396 | 0.500 | 52/52 | +0.066 | STANDARD |
| Kaapo Kakko: 1+ points | 0.490 | 0.390 | 41/63 | +0.063 | STANDARD |
| Daniil Tarasov: 26+ saves | 0.330 | 0.410 | 50/68 | -0.025 |  |

**CAR @ VAN** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 32.33, exp saves 27.7 (sd 7.44), pull risk 0.074
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.8, exp saves 19.88 (sd 5.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.219 | 0.340 | 35/67 | +0.095 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.504 | 0.605 | 62/41 | +0.069 | STANDARD |
| Filip Chytil: 1+ goals | 0.245 | 0.145 | 17/88 | +0.066 | STANDARD |
| Sebastian Aho: 1+ assists | 0.396 | 0.495 | 51/52 | +0.066 | STANDARD |
| Linus Karlsson: 1+ goals | 0.232 | 0.145 | 18/89 | +0.042 | STANDARD |
| Brock Boeser: 1+ assists | 0.347 | 0.260 | 28/76 | +0.053 | STANDARD |

**TBL @ VGK** · priced 158/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.99, exp saves 23.65 (sd 6.38), pull risk 0.049
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.35, exp saves 22.53 (sd 6.4), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.270 | 0.400 | 42/62 | +0.094 | STANDARD |
| John Carlson: 1+ points | 0.335 | 0.465 | 48/55 | +0.098 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.443 | 0.570 | 58/44 | +0.100 | STANDARD |
| Nikita Kucherov: 2+ points | 0.251 | 0.370 | 38/64 | +0.093 | STANDARD |
| Shea Theodore: 1+ assists | 0.344 | 0.260 | 28/76 | +0.049 | STANDARD |
| Jack Eichel: 2+ points | 0.243 | 0.325 | 34/69 | +0.052 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
