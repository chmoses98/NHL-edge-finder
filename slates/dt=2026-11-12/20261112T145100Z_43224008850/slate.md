# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-12T14:51:00Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3837 · contracts joined: 2164 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 1889, 'OK': 143, 'NO_EDGE': 132}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 274, 'game_early_goal': 11, 'first_goal': 360, 'game_winner': 22, 'player_goals': 619, 'game_overtime': 11, 'player_points': 350, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 2026-11-12T17:00:00Z | T-90m | 0.392 | 0.608 | 0.168 | 6.54 | 2.90 | 3.63 | 210 (25/185) | PROBABLE/PROBABLE |
| MTL @ BOS | 2026-11-13T00:00:00Z | T-6h | 0.566 | 0.434 | 0.177 | 6.02 | 3.21 | 2.81 | 214 (25/189) | PROJECTED/CONFIRMED |
| MIN @ TOR | 2026-11-13T00:00:00Z | T-6h | 0.437 | 0.563 | 0.171 | 6.40 | 2.99 | 3.41 | 204 (25/179) | PROJECTED/PROJECTED |
| COL @ OTT | 2026-11-13T00:00:00Z | T-6h | 0.460 | 0.540 | 0.172 | 6.36 | 3.05 | 3.31 | 214 (25/189) | PROJECTED/PROJECTED |
| WSH @ NJD | 2026-11-13T00:00:00Z | T-6h | 0.557 | 0.443 | 0.175 | 6.17 | 3.27 | 2.91 | 218 (25/193) | PROJECTED/PROJECTED |
| TBL @ CBJ | 2026-11-13T00:00:00Z | T-6h | 0.421 | 0.579 | 0.174 | 6.15 | 2.81 | 3.34 | 212 (25/187) | PROJECTED/PROJECTED |
| DET @ FLA | 2026-11-13T00:30:00Z | T-6h | 0.563 | 0.437 | 0.177 | 6.16 | 3.26 | 2.90 | 219 (25/194) | PROJECTED/PROJECTED |
| BUF @ CHI | 2026-11-13T01:00:00Z | T-6h | 0.476 | 0.524 | 0.175 | 6.06 | 2.95 | 3.11 | 209 (25/184) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-6h | 0.593 | 0.407 | 0.176 | 5.80 | 3.19 | 2.61 | 204 (25/179) | PROJECTED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-6h | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 209 (25/184) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-12h | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV12CARSEA-CAR2 | game_spread | 0.391 | 0.525 | 0.498 | 53 | 48 | no | +0.112 | OK |
| KXNHLSPREAD-26NOV12CARSEA-CAR3 | game_spread | 0.258 | 0.390 | 0.362 | 40 | 62 | no | +0.105 | OK |
| KXNHLGAME-26NOV12CARSEA-SEA | game_winner | 0.392 | 0.275 | 0.297 | 28 | 73 | yes | +0.097 | OK |
| KXNHLGAME-26NOV12CARSEA-CAR | game_winner | 0.608 | 0.725 | 0.703 | 73 | 28 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA3 | team_total | 0.559 | 0.460 | 0.480 | 47 | 55 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR4 | team_total | 0.506 | 0.600 | 0.582 | 61 | 41 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5 | team_total | 0.308 | 0.395 | 0.377 | 40 | 61 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.389 | 0.480 | 0.462 | 49 | 53 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA4 | team_total | 0.343 | 0.255 | 0.271 | 27 | 76 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5 | team_total | 0.172 | 0.100 | 0.112 | 11 | 91 | yes | +0.056 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.427 | 0.505 | 0.489 | 51 | 50 | no | +0.055 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.545 | 0.530 | 55 | 46 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA2 | game_spread | 0.201 | 0.130 | 0.142 | 14 | 88 | yes | +0.053 | OK |
| KXNHLTOTAL-26NOV12NYILA-5 | game_total | 0.695 | 0.770 | 0.756 | 78 | 24 | no | +0.052 | OK |
| KXNHLGAME-26NOV12TBCBJ-TB | game_winner | 0.579 | 0.505 | 0.520 | 51 | 50 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ4 | team_total | 0.323 | 0.395 | 0.380 | 40 | 61 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR3 | team_total | 0.707 | 0.780 | 0.767 | 79 | 23 | no | +0.050 | OK |
| KXNHLGAME-26NOV12BUFCHI-BUF | game_winner | 0.524 | 0.595 | 0.581 | 60 | 41 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5 | team_total | 0.208 | 0.280 | 0.264 | 29 | 73 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF3 | team_total | 0.607 | 0.685 | 0.670 | 70 | 33 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2 | team_total | 0.781 | 0.710 | 0.725 | 72 | 30 | yes | +0.047 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA3 | game_spread | 0.201 | 0.265 | 0.251 | 27 | 74 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-6 | game_total | 0.539 | 0.605 | 0.592 | 61 | 40 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 | team_total | 0.540 | 0.610 | 0.596 | 62 | 40 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF3 | game_spread | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.043 | OK |
| KXNHLGAME-26NOV12TBCBJ-CBJ | game_winner | 0.421 | 0.485 | 0.472 | 49 | 52 | no | +0.042 | OK |
| KXNHLGAME-26NOV12MINTOR-MIN | game_winner | 0.563 | 0.625 | 0.613 | 63 | 38 | no | +0.041 | OK |
| KXNHLGAME-26NOV12MINTOR-TOR | game_winner | 0.437 | 0.375 | 0.387 | 38 | 63 | yes | +0.041 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.476 | 0.415 | 0.427 | 42 | 59 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ2 | team_total | 0.760 | 0.820 | 0.809 | 83 | 19 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.813 | 0.865 | 0.856 | 87 | 14 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.305 | 0.370 | 0.357 | 38 | 64 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ2 | game_spread | 0.218 | 0.275 | 0.263 | 28 | 73 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.845 | 0.836 | 85 | 16 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.751 | 0.810 | 0.799 | 82 | 20 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ5 | team_total | 0.162 | 0.220 | 0.207 | 23 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-TB2 | game_spread | 0.361 | 0.305 | 0.316 | 31 | 70 | yes | +0.036 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.838 | 0.885 | 0.877 | 89 | 12 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA2 | game_spread | 0.330 | 0.385 | 0.374 | 39 | 62 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.560 | 0.548 | 57 | 45 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR2 | team_total | 0.873 | 0.920 | 0.912 | 93 | 9 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-6 | game_total | 0.532 | 0.585 | 0.575 | 59 | 42 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.795 | 0.784 | 81 | 22 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA6 | team_total | 0.073 | 0.030 | 0.036 | 4 | 98 | yes | +0.031 | OK |
| KXNHLGAME-26NOV12DETFLA-FLA | game_winner | 0.563 | 0.615 | 0.605 | 62 | 39 | no | +0.030 | OK |
| KXNHLGAME-26NOV12DETFLA-DET | game_winner | 0.437 | 0.385 | 0.395 | 39 | 62 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-CHI2 | game_spread | 0.262 | 0.215 | 0.224 | 22 | 79 | yes | +0.030 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-7 | game_total | 0.443 | 0.495 | 0.484 | 50 | 51 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL4 | team_total | 0.325 | 0.375 | 0.365 | 38 | 63 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN3 | game_spread | 0.218 | 0.265 | 0.255 | 27 | 74 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA3 | game_spread | 0.113 | 0.070 | 0.077 | 8 | 94 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ3 | game_spread | 0.123 | 0.165 | 0.156 | 17 | 84 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-6 | game_total | 0.555 | 0.605 | 0.595 | 61 | 40 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN2 | game_spread | 0.346 | 0.395 | 0.385 | 40 | 61 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-5 | game_total | 0.762 | 0.810 | 0.801 | 82 | 20 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL2 | team_total | 0.763 | 0.815 | 0.805 | 83 | 20 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-4 | game_total | 0.848 | 0.885 | 0.878 | 89 | 12 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV12MINTOR-TOR2 | game_spread | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.243 | 0.285 | 0.276 | 29 | 72 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET5 | team_total | 0.171 | 0.135 | 0.142 | 14 | 87 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV12DETFLA-DET2 | game_spread | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL3 | team_total | 0.541 | 0.590 | 0.580 | 60 | 42 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.492 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.092 | 0.125 | 0.118 | 13 | 88 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-9 | game_total | 0.169 | 0.210 | 0.201 | 22 | 80 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-5 | game_total | 0.750 | 0.790 | 0.782 | 80 | 22 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL2 | team_total | 0.824 | 0.855 | 0.849 | 86 | 15 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL4 | team_total | 0.406 | 0.450 | 0.441 | 46 | 56 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI3 | game_spread | 0.126 | 0.155 | 0.149 | 16 | 85 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-5 | game_total | 0.722 | 0.755 | 0.749 | 76 | 25 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET4 | team_total | 0.340 | 0.300 | 0.308 | 31 | 71 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL5 | team_total | 0.156 | 0.195 | 0.187 | 21 | 82 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-4 | game_total | 0.838 | 0.870 | 0.864 | 88 | 14 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4 | team_total | 0.359 | 0.325 | 0.332 | 33 | 68 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI5 | team_total | 0.138 | 0.175 | 0.167 | 19 | 84 | no | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 0.392 | 0.415 | 0.168 | 0.210 | 6.54 | 6.69 | 1.019/0.987 | KXNHLTEAMTOTAL-26NOV12CARSEA-SEA3 +0.039 |
| MTL @ BOS | 0.566 | 0.588 | 0.177 | 0.212 | 6.02 | 6.67 | 0.969/0.983 | KXNHLTOTAL-26NOV12MTLBOS-7 +0.112 |
| MIN @ TOR | 0.437 | 0.498 | 0.171 | 0.215 | 6.40 | 6.48 | 0.965/0.995 | KXNHLGAME-26NOV12MINTOR-MIN -0.060 |
| COL @ OTT | 0.460 | 0.493 | 0.172 | 0.221 | 6.36 | 6.46 | 0.999/0.977 | KXNHLTEAMTOTAL-26NOV12COLOTT-OTT3 +0.039 |
| WSH @ NJD | 0.557 | 0.556 | 0.175 | 0.216 | 6.17 | 6.31 | 0.959/0.961 | KXNHLTOTAL-26NOV12WSHNJ-7 +0.032 |
| TBL @ CBJ | 0.421 | 0.501 | 0.174 | 0.224 | 6.15 | 6.20 | 0.990/0.974 | KXNHLSPREAD-26NOV12TBCBJ-TB2 -0.084 |
| DET @ FLA | 0.563 | 0.565 | 0.177 | 0.217 | 6.16 | 6.29 | 1.008/1.015 | KXNHLTOTAL-26NOV12DETFLA-7 +0.032 |
| BUF @ CHI | 0.476 | 0.488 | 0.175 | 0.214 | 6.06 | 6.24 | 0.990/0.998 | KXNHLTOTAL-26NOV12BUFCHI-5 +0.031 |
| WPG @ DAL | 0.593 | 0.585 | 0.176 | 0.213 | 5.80 | 6.11 | 0.987/1.001 | KXNHLTOTAL-26NOV12WPGDAL-7 +0.052 |
| STL @ UTA | 0.511 | 0.532 | 0.172 | 0.220 | 6.17 | 6.40 | 0.993/0.993 | KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4 +0.044 |
| NYI @ LAK | 0.554 | 0.551 | 0.185 | 0.221 | 5.66 | 5.99 | 0.990/0.956 | KXNHLTOTAL-26NOV12NYILA-5 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Winterton: 1+ goals YES @ 9c · p 0.1378 (adj 0.1234) · $5.07 · thesis SEA:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 64c · p 0.7208 (adj 0.6981) · $15.54 · thesis CAR:SUPPRESSED
- Berkly Catton: 1+ goals YES @ 16c · p 0.2218 (adj 0.2026) · $6.7 · thesis SEA:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 48c · p 0.6342 (adj 0.5307) · $7.6 · thesis SEA:WINS
- William Borgen: 1+ goals YES @ 6c · p 0.0899 (adj 0.0787) · $2.55 · thesis BOS:WINS_BY_2PLUS
- Fraser Minten: 1+ goals YES @ 19c · p 0.2261 (adj 0.2146) · $3.05 · thesis BOS:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 52c · p 0.6387 (adj 0.5518) · $5.96 · thesis MTL:SUPPRESSED
- Boston over 3.5 goals scored YES @ 44c · p 0.5018 (adj 0.4684) · $1.03 · thesis BOS:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 55c · p 0.625 (adj 0.6038) · $14.52 · thesis MIN:SUPPRESSED
- Minnesota wins by over 2.5 goals NO @ 74c · p 0.8256 (adj 0.7803) · $15.54 · thesis TOR:WINS
- Yakov Trenin: 1+ goals YES @ 11c · p 0.1411 (adj 0.1296) · $2.88 · thesis MIN:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 20c · p 0.241 (adj 0.227) · $3.15 · thesis TOR:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2243 (adj 0.2095) · $6.58 · thesis WSH:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 13c · p 0.1723 (adj 0.1542) · $3.19 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 59c · p 0.6427 (adj 0.6283) · $10.27 · thesis NJD:SUPPRESSED
- Connor Brown: 1+ goals YES @ 19c · p 0.2302 (adj 0.2164) · $3.64 · thesis NJD:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2123 (adj 0.198) · $4.04 · thesis CBJ:WINS_BY_2PLUS
- Sam Bennett: 1+ goals YES @ 27c · p 0.3135 (adj 0.3001) · $3.94 · thesis FLA:OFFENSE_4PLUS
- Aaron Ekblad: 1+ assists YES @ 27c · p 0.3323 (adj 0.2986) · $3.36 · thesis FLA:OFFENSE_4PLUS
- Chicago wins by over 1.5 goals YES @ 22c · p 0.2755 (adj 0.2453) · $2.01 · thesis CHI:WINS_BY_2PLUS
- Buffalo wins by over 1.5 goals NO @ 64c · p 0.7093 (adj 0.6697) · $2.03 · thesis CHI:WINS
- Buffalo over 3.5 goals scored NO @ 53c · p 0.6025 (adj 0.5613) · $2.17 · thesis BUF:SUPPRESSED
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.8178 (adj 0.7839) · $4.55 · thesis CHI:WINS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.1923 (adj 0.1792) · $4.4 · thesis DAL:WINS_BY_2PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2462 (adj 0.2259) · $7.86 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 14c · p 0.1824 (adj 0.1668) · $3.83 · thesis UTA:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.162 (adj 0.1515) · $2.84 · thesis STL:OFFENSE_4PLUS
- MacKenzie Weegar: 1+ assists YES @ 30c · p 0.3669 (adj 0.326) · $1.69 · thesis UTA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ SEA** · priced 158/159 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- SEA net: Philipp Grubauer (PROBABLE) exp shots 31.95, exp saves 27.12 (sd 7.56), pull risk 0.086
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.45, exp saves 20.48 (sd 5.88), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.366 | 0.510 | 52/50 | +0.117 | STANDARD |
| Sebastian Aho: 2+ points | 0.189 | 0.320 | 33/69 | +0.106 | STANDARD |
| Sebastian Aho: 1+ points | 0.542 | 0.655 | 67/36 | +0.082 | STANDARD |
| Taylor Hall: 1+ assists | 0.210 | 0.315 | 33/70 | +0.076 | STANDARD |
| Nikolaj Ehlers: 2+ points | 0.158 | 0.255 | 28/77 | +0.059 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.364 | 0.460 | 48/56 | +0.058 | STANDARD |

**MTL @ BOS** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.96, exp saves 23.55 (sd 6.56), pull risk 0.059
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.11, exp saves 23.83 (sd 6.83), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.361 | 0.495 | 51/52 | +0.101 | STANDARD |
| Fraser Minten: 1+ points | 0.457 | 0.370 | 40/66 | +0.040 | STANDARD |
| Fraser Minten: 2+ points | 0.136 | 0.055 | 10/99 | +0.030 | STANDARD |
| Fraser Minten: 1+ assists | 0.305 | 0.230 | 24/78 | +0.052 | STANDARD |
| Nick Suzuki: 1+ points | 0.551 | 0.625 | 65/40 | +0.033 | STANDARD |
| Nick Suzuki: 2+ assists | 0.078 | 0.150 | 17/87 | +0.044 | STANDARD |

**MIN @ TOR** · priced 148/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.08, exp saves 26.87 (sd 7.13), pull risk 0.065
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.87, exp saves 23.93 (sd 6.65), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ points | 0.539 | 0.400 | 42/62 | +0.102 | STANDARD |
| Easton Cowan: 2+ points | 0.192 | 0.065 | 12/99 | +0.065 | STANDARD |
| Easton Cowan: 1+ assists | 0.399 | 0.280 | 29/73 | +0.095 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.275 | 0.385 | 41/64 | +0.069 | STANDARD |
| Teddy Blueger: 1+ goals | 0.177 | 0.075 | 10/95 | +0.071 | STANDARD |
| Matt Boldy: 1+ assists | 0.401 | 0.495 | 51/52 | +0.062 | STANDARD |

**COL @ OTT** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 28.4, exp saves 24.59 (sd 6.79), pull risk 0.066
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 27.05, exp saves 23.42 (sd 6.46), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 1+ assists | 0.449 | 0.540 | 56/48 | +0.054 | STANDARD |
| Jordan Spence: 1+ points | 0.338 | 0.265 | 29/76 | +0.033 | STANDARD |
| Jake Sanderson: 1+ points | 0.461 | 0.530 | 55/49 | +0.032 | STANDARD |
| Ridly Greig: 1+ goals | 0.202 | 0.135 | 17/90 | +0.022 | STANDARD |
| Jake Sanderson: 1+ assists | 0.380 | 0.445 | 46/57 | +0.033 | STANDARD |
| Martin Necas: 1+ assists | 0.426 | 0.490 | 51/53 | +0.027 | STANDARD |

**WSH @ NJD** · priced 161/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 25.32, exp saves 22.03 (sd 6.08), pull risk 0.058
- WSH net: Logan Thompson (PROJECTED) exp shots 30.42, exp saves 26.06 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brett Pesce: 1+ points | 0.364 | 0.265 | 28/75 | +0.069 | STANDARD |
| Jack Hughes: 2+ points | 0.274 | 0.360 | 38/66 | +0.050 | STANDARD |
| Brett Pesce: 1+ assists | 0.314 | 0.240 | 25/77 | +0.051 | STANDARD |
| Jack Hughes: 1+ assists | 0.447 | 0.520 | 53/49 | +0.046 | STANDARD |
| Cody Glass: 1+ goals | 0.172 | 0.100 | 13/93 | +0.034 | STANDARD |
| Luke Evangelista: 1+ assists | 0.268 | 0.340 | 35/67 | +0.047 | STANDARD |

**TBL @ CBJ** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROJECTED) exp shots 27.7, exp saves 24.01 (sd 6.61), pull risk 0.061
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.39, exp saves 22.82 (sd 6.32), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.445 | 0.580 | 60/44 | +0.098 | STANDARD |
| Nikita Kucherov: 2+ points | 0.268 | 0.385 | 41/64 | +0.076 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.116 | 0.225 | 25/80 | +0.073 | STANDARD |
| Brandon Hagel: 2+ points | 0.215 | 0.140 | 24/96 | -0.037 | STANDARD |
| Nikita Kucherov: 1+ points | 0.638 | 0.565 | 76/63 | -0.135 | STANDARD |
| Damon Severson: 1+ points | 0.375 | 0.305 | 33/72 | +0.030 | STANDARD |

**DET @ FLA** · priced 159/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.02, exp saves 23.54 (sd 6.42), pull risk 0.054
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.83, exp saves 23.78 (sd 6.67), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex DeBrincat: 2+ points | 0.236 | 0.130 | 22/96 | +0.004 | STANDARD |
| Carter Verhaeghe: 2+ points | 0.239 | 0.140 | 24/96 | -0.014 | STANDARD |
| Aaron Ekblad: 1+ points | 0.393 | 0.305 | 33/72 | +0.048 | STANDARD |
| Gustav Forsling: 1+ points | 0.363 | 0.290 | 32/74 | +0.028 | STANDARD |
| Emmitt Finnie: 2+ points | 0.157 | 0.085 | 16/99 | -0.013 | STANDARD |
| Aaron Ekblad: 1+ assists | 0.332 | 0.265 | 27/74 | +0.049 | STANDARD |

**BUF @ CHI** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.67, exp saves 25.65 (sd 6.91), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 25.13, exp saves 21.73 (sd 6.09), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ assists | 0.423 | 0.525 | 54/49 | +0.070 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.519 | 0.620 | 64/40 | +0.064 | STANDARD |
| Tage Thompson: 2+ points | 0.210 | 0.290 | 32/74 | +0.037 | STANDARD |
| Tage Thompson: 1+ points | 0.570 | 0.645 | 67/38 | +0.034 | STANDARD |
| Tage Thompson: 1+ assists | 0.343 | 0.415 | 43/60 | +0.040 | STANDARD |
| Tyler Bertuzzi: 2+ points | 0.175 | 0.105 | 18/97 | -0.016 | STANDARD |

**WPG @ DAL** · priced 150/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.73 (sd 5.96), pull risk 0.045
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.72, exp saves 22.82 (sd 6.39), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.251 | 0.395 | 42/63 | +0.102 | STANDARD |
| Josh Morrissey: 1+ points | 0.326 | 0.440 | 46/58 | +0.077 | STANDARD |
| Roope Hintz: 2+ points | 0.209 | 0.135 | 23/96 | -0.034 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.443 | 0.515 | 53/50 | +0.039 | STANDARD |
| Mikko Rantanen: 2+ points | 0.246 | 0.310 | 34/72 | +0.020 | STANDARD |
| Cole Perfetti: 1+ assists | 0.359 | 0.295 | 31/72 | +0.034 | STANDARD |

**STL @ UTA** · priced 151/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.26), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.65, exp saves 24.64 (sd 6.73), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| MacKenzie Weegar: 1+ assists | 0.367 | 0.285 | 30/73 | +0.052 | STANDARD |
| Lawson Crouse: 1+ goals | 0.246 | 0.165 | 18/85 | +0.056 | STANDARD |
| Barrett Hayton: 1+ points | 0.477 | 0.400 | 43/63 | +0.030 | STANDARD |
| Robert Thomas: 1+ assists | 0.431 | 0.505 | 52/51 | +0.042 | STANDARD |
| Barrett Hayton: 1+ assists | 0.333 | 0.260 | 27/75 | +0.050 | STANDARD |
| Clayton Keller: 1+ assists | 0.478 | 0.550 | 57/47 | +0.034 | STANDARD |

**NYI @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.98, exp saves 23.62 (sd 6.37), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.46, exp saves 24.61 (sd 6.69), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
