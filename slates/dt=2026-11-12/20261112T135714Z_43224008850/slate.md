# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-12T13:57:14Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3679 · contracts joined: 2006 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 1731, 'OK': 139, 'NO_EDGE': 136}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 248, 'game_early_goal': 11, 'first_goal': 324, 'game_winner': 22, 'player_goals': 556, 'game_overtime': 11, 'player_points': 317, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 2026-11-12T17:00:00Z | T-3h | 0.392 | 0.608 | 0.168 | 6.54 | 2.90 | 3.63 | 210 (25/185) | PROBABLE/PROBABLE |
| MTL @ BOS | 2026-11-13T00:00:00Z | T-6h | 0.566 | 0.434 | 0.177 | 6.02 | 3.21 | 2.81 | 214 (25/189) | PROJECTED/CONFIRMED |
| MIN @ TOR | 2026-11-13T00:00:00Z | T-6h | 0.437 | 0.563 | 0.171 | 6.40 | 2.99 | 3.41 | 204 (25/179) | PROJECTED/PROJECTED |
| COL @ OTT | 2026-11-13T00:00:00Z | T-6h | 0.460 | 0.540 | 0.172 | 6.36 | 3.05 | 3.31 | 214 (25/189) | PROJECTED/PROJECTED |
| WSH @ NJD | 2026-11-13T00:00:00Z | T-6h | 0.557 | 0.443 | 0.175 | 6.17 | 3.27 | 2.91 | 218 (25/193) | PROJECTED/PROJECTED |
| TBL @ CBJ | 2026-11-13T00:00:00Z | T-6h | 0.421 | 0.579 | 0.174 | 6.15 | 2.81 | 3.34 | 212 (25/187) | PROJECTED/PROJECTED |
| DET @ FLA | 2026-11-13T00:30:00Z | T-6h | 0.563 | 0.437 | 0.177 | 6.16 | 3.26 | 2.90 | 219 (25/194) | PROJECTED/PROJECTED |
| BUF @ CHI | 2026-11-13T01:00:00Z | T-6h | 0.476 | 0.524 | 0.175 | 6.06 | 2.95 | 3.11 | 209 (25/184) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-6h | 0.593 | 0.407 | 0.176 | 5.80 | 3.19 | 2.61 | 204 (25/179) | PROJECTED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-12h | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 51 (25/26) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-12h | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV12CARSEA-CAR3 | game_spread | 0.258 | 0.385 | 0.358 | 39 | 62 | no | +0.105 | OK |
| KXNHLSPREAD-26NOV12CARSEA-CAR2 | game_spread | 0.391 | 0.515 | 0.490 | 52 | 49 | no | +0.102 | OK |
| KXNHLGAME-26NOV12CARSEA-SEA | game_winner | 0.392 | 0.275 | 0.297 | 28 | 73 | yes | +0.097 | OK |
| KXNHLGAME-26NOV12CARSEA-CAR | game_winner | 0.608 | 0.725 | 0.703 | 73 | 28 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA3 | team_total | 0.559 | 0.460 | 0.480 | 47 | 55 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR4 | team_total | 0.506 | 0.600 | 0.582 | 61 | 41 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.389 | 0.480 | 0.462 | 49 | 53 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA4 | team_total | 0.343 | 0.255 | 0.271 | 27 | 76 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5 | team_total | 0.172 | 0.100 | 0.112 | 11 | 91 | yes | +0.056 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.427 | 0.505 | 0.489 | 51 | 50 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5 | team_total | 0.308 | 0.390 | 0.373 | 40 | 62 | no | +0.055 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.545 | 0.530 | 55 | 46 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA2 | game_spread | 0.201 | 0.135 | 0.147 | 14 | 87 | yes | +0.053 | OK |
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
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR2 | team_total | 0.873 | 0.925 | 0.917 | 93 | 8 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ2 | team_total | 0.760 | 0.820 | 0.809 | 83 | 19 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.813 | 0.865 | 0.856 | 87 | 14 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.305 | 0.370 | 0.357 | 38 | 64 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ2 | game_spread | 0.218 | 0.275 | 0.263 | 28 | 73 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.845 | 0.836 | 85 | 16 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.751 | 0.810 | 0.799 | 82 | 20 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ5 | team_total | 0.162 | 0.220 | 0.207 | 23 | 79 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-TB2 | game_spread | 0.361 | 0.300 | 0.312 | 31 | 71 | yes | +0.036 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.838 | 0.885 | 0.877 | 89 | 12 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-6 | game_total | 0.532 | 0.585 | 0.575 | 59 | 42 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA6 | team_total | 0.073 | 0.030 | 0.036 | 4 | 98 | yes | +0.031 | OK |
| KXNHLGAME-26NOV12MINTOR-MIN | game_winner | 0.563 | 0.615 | 0.605 | 62 | 39 | no | +0.031 | OK |
| KXNHLGAME-26NOV12MINTOR-TOR | game_winner | 0.437 | 0.385 | 0.395 | 39 | 62 | yes | +0.031 | OK |
| KXNHLGAME-26NOV12DETFLA-FLA | game_winner | 0.563 | 0.615 | 0.605 | 62 | 39 | no | +0.030 | OK |
| KXNHLGAME-26NOV12DETFLA-DET | game_winner | 0.437 | 0.385 | 0.395 | 39 | 62 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-CHI2 | game_spread | 0.262 | 0.215 | 0.224 | 22 | 79 | yes | +0.030 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-7 | game_total | 0.443 | 0.495 | 0.484 | 50 | 51 | no | +0.030 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.476 | 0.425 | 0.435 | 43 | 58 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL4 | team_total | 0.325 | 0.375 | 0.365 | 38 | 63 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN3 | game_spread | 0.218 | 0.265 | 0.255 | 27 | 74 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.240 | 0.229 | 25 | 77 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA3 | game_spread | 0.113 | 0.070 | 0.077 | 8 | 94 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ3 | game_spread | 0.123 | 0.165 | 0.156 | 17 | 84 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-5 | game_total | 0.762 | 0.805 | 0.797 | 81 | 20 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL2 | team_total | 0.763 | 0.815 | 0.805 | 83 | 20 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA2 | game_spread | 0.330 | 0.380 | 0.370 | 39 | 63 | no | +0.024 | OK |
| KXNHLSPREAD-26NOV12MINTOR-TOR2 | game_spread | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.243 | 0.285 | 0.276 | 29 | 72 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET5 | team_total | 0.171 | 0.135 | 0.142 | 14 | 87 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV12DETFLA-DET2 | game_spread | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL3 | team_total | 0.541 | 0.590 | 0.580 | 60 | 42 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.555 | 0.544 | 57 | 46 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.492 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.092 | 0.125 | 0.118 | 13 | 88 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.790 | 0.780 | 81 | 23 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-5 | game_total | 0.750 | 0.795 | 0.786 | 81 | 22 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-6 | game_total | 0.555 | 0.600 | 0.591 | 61 | 41 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN2 | game_spread | 0.346 | 0.385 | 0.377 | 39 | 62 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL4 | team_total | 0.406 | 0.450 | 0.441 | 46 | 56 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI3 | game_spread | 0.126 | 0.155 | 0.149 | 16 | 85 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-5 | game_total | 0.722 | 0.755 | 0.749 | 76 | 25 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET4 | team_total | 0.340 | 0.300 | 0.308 | 31 | 71 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-4 | game_total | 0.848 | 0.880 | 0.874 | 89 | 13 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL5 | team_total | 0.156 | 0.195 | 0.187 | 21 | 82 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-4 | game_total | 0.838 | 0.870 | 0.864 | 88 | 14 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4 | team_total | 0.359 | 0.325 | 0.332 | 33 | 68 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI5 | team_total | 0.138 | 0.175 | 0.167 | 19 | 84 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV12MTLBOS-MTL3 | game_spread | 0.128 | 0.155 | 0.149 | 16 | 85 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-CHI3 | game_spread | 0.150 | 0.125 | 0.130 | 13 | 88 | yes | +0.012 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 22 recommended · full analysis in card.md / packet.json `thesis_card`

- Berkly Catton: 1+ goals YES @ 14c · p 0.2218 (adj 0.2001) · $10.76 · thesis SEA:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 64c · p 0.7208 (adj 0.6981) · $16.54 · thesis CAR:SUPPRESSED
- Carolina wins by over 1.5 goals NO @ 49c · p 0.6342 (adj 0.5372) · $3.37 · thesis SEA:WINS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7523 (adj 0.6631) · $6.46 · thesis SEA:WINS
- William Borgen: 1+ goals YES @ 6c · p 0.0899 (adj 0.0787) · $2.62 · thesis BOS:WINS_BY_2PLUS
- Fraser Minten: 1+ goals YES @ 19c · p 0.2261 (adj 0.2146) · $3.01 · thesis BOS:OFFENSE_4PLUS
- Boston over 4.5 goals scored YES @ 24c · p 0.3048 (adj 0.2674) · $2.11 · thesis BOS:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 52c · p 0.6387 (adj 0.5518) · $6.37 · thesis MTL:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 55c · p 0.625 (adj 0.6025) · $14.86 · thesis MIN:SUPPRESSED
- Minnesota wins by over 2.5 goals NO @ 74c · p 0.8256 (adj 0.7803) · $16.54 · thesis TOR:WINS
- Yakov Trenin: 1+ goals YES @ 11c · p 0.1411 (adj 0.1296) · $3.06 · thesis MIN:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 20c · p 0.241 (adj 0.227) · $3.35 · thesis TOR:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2243 (adj 0.207) · $6.37 · thesis WSH:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 13c · p 0.1723 (adj 0.158) · $4.4 · thesis NJD:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 10c · p 0.134 (adj 0.118) · $2.45 · thesis NJD:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 67c · p 0.7321 (adj 0.6961) · $7.97 · thesis NJD:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2123 (adj 0.198) · $4.23 · thesis CBJ:WINS_BY_2PLUS
- Yanni Gourde: 1+ goals NO @ 86c · p 0.8933 (adj 0.8812) · $16.54 · thesis TBL:SUPPRESSED
- John Carlson: 1+ assists NO @ 62c · p 0.6909 (adj 0.648) · $6.22 · thesis TBL:SUPPRESSED
- Sam Bennett: 1+ goals YES @ 27c · p 0.3135 (adj 0.3001) · $4.19 · thesis FLA:OFFENSE_4PLUS
- Aaron Ekblad: 1+ assists YES @ 27c · p 0.3323 (adj 0.2986) · $3.58 · thesis FLA:OFFENSE_4PLUS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.1923 (adj 0.1805) · $5.0 · thesis DAL:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ SEA** · priced 158/159 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- SEA net: Philipp Grubauer (PROBABLE) exp shots 31.97, exp saves 27.14 (sd 7.53), pull risk 0.086
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.46, exp saves 20.48 (sd 5.85), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.366 | 0.510 | 52/50 | +0.117 | STANDARD |
| Sebastian Aho: 2+ points | 0.189 | 0.320 | 33/69 | +0.106 | STANDARD |
| Sebastian Aho: 1+ points | 0.542 | 0.665 | 70/37 | +0.072 | STANDARD |
| Taylor Hall: 1+ assists | 0.210 | 0.320 | 34/70 | +0.076 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.335 | 0.435 | 45/58 | +0.068 | STANDARD |
| Nikolaj Ehlers: 2+ points | 0.158 | 0.255 | 28/77 | +0.059 | STANDARD |

**MTL @ BOS** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.98, exp saves 23.52 (sd 6.47), pull risk 0.059
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.12, exp saves 23.8 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.361 | 0.495 | 51/52 | +0.101 | STANDARD |
| Fraser Minten: 1+ points | 0.457 | 0.375 | 40/65 | +0.040 | STANDARD |
| Nick Suzuki: 1+ points | 0.551 | 0.630 | 65/39 | +0.043 | STANDARD |
| Fraser Minten: 2+ points | 0.136 | 0.060 | 10/98 | +0.030 | STANDARD |
| Fraser Minten: 1+ assists | 0.305 | 0.230 | 24/78 | +0.052 | STANDARD |
| Nick Suzuki: 2+ points | 0.196 | 0.270 | 31/77 | +0.022 | STANDARD |

**MIN @ TOR** · priced 148/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.09, exp saves 26.88 (sd 7.21), pull risk 0.066
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.89, exp saves 23.98 (sd 6.58), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ points | 0.539 | 0.405 | 42/61 | +0.102 | STANDARD |
| Easton Cowan: 2+ points | 0.192 | 0.070 | 12/98 | +0.065 | STANDARD |
| Easton Cowan: 1+ assists | 0.399 | 0.280 | 29/73 | +0.095 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.275 | 0.380 | 40/64 | +0.069 | STANDARD |
| Teddy Blueger: 1+ goals | 0.177 | 0.075 | 10/95 | +0.071 | STANDARD |
| Matt Boldy: 1+ assists | 0.401 | 0.495 | 51/52 | +0.062 | STANDARD |

**COL @ OTT** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 28.41, exp saves 24.57 (sd 6.82), pull risk 0.068
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 27.06, exp saves 23.45 (sd 6.46), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 1+ assists | 0.449 | 0.540 | 56/48 | +0.054 | STANDARD |
| Jake Sanderson: 1+ points | 0.461 | 0.530 | 55/49 | +0.032 | STANDARD |
| Martin Necas: 1+ assists | 0.426 | 0.495 | 51/52 | +0.037 | STANDARD |
| Jordan Spence: 1+ points | 0.338 | 0.270 | 29/75 | +0.033 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.127 | 0.195 | 21/82 | +0.042 | STANDARD |
| Tim Stutzle: 1+ assists | 0.419 | 0.485 | 50/53 | +0.033 | STANDARD |

**WSH @ NJD** · priced 161/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 25.33, exp saves 22.05 (sd 6.11), pull risk 0.057
- WSH net: Logan Thompson (PROJECTED) exp shots 30.43, exp saves 26.09 (sd 7.15), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brett Pesce: 1+ points | 0.364 | 0.265 | 28/75 | +0.069 | STANDARD |
| Jack Hughes: 2+ points | 0.274 | 0.360 | 38/66 | +0.050 | STANDARD |
| Brett Pesce: 1+ assists | 0.314 | 0.240 | 25/77 | +0.051 | STANDARD |
| Jack Hughes: 1+ assists | 0.447 | 0.520 | 53/49 | +0.046 | STANDARD |
| Luke Evangelista: 1+ assists | 0.268 | 0.340 | 35/67 | +0.047 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.224 | 0.155 | 17/86 | +0.044 | STANDARD |

**TBL @ CBJ** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROJECTED) exp shots 27.86, exp saves 24.17 (sd 6.66), pull risk 0.063
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.24, exp saves 22.68 (sd 6.27), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.444 | 0.590 | 60/42 | +0.119 | STANDARD |
| Nikita Kucherov: 2+ points | 0.262 | 0.385 | 41/64 | +0.082 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.114 | 0.230 | 26/80 | +0.075 | STANDARD |
| John Carlson: 1+ points | 0.390 | 0.485 | 50/53 | +0.063 | STANDARD |
| John Carlson: 1+ assists | 0.309 | 0.395 | 41/62 | +0.054 | STANDARD |
| Nikita Kucherov: 3+ points | 0.073 | 0.155 | 17/86 | +0.058 | STANDARD |

**DET @ FLA** · priced 159/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.04, exp saves 23.55 (sd 6.4), pull risk 0.052
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.84, exp saves 23.8 (sd 6.66), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex DeBrincat: 2+ points | 0.236 | 0.135 | 22/95 | +0.004 | STANDARD |
| Carter Verhaeghe: 2+ points | 0.239 | 0.145 | 24/95 | -0.014 | STANDARD |
| Sam Bennett: 2+ points | 0.191 | 0.100 | 18/98 | +0.000 | STANDARD |
| Aaron Ekblad: 1+ points | 0.393 | 0.320 | 33/69 | +0.048 | STANDARD |
| Gustav Forsling: 1+ points | 0.363 | 0.295 | 32/73 | +0.028 | STANDARD |
| Aaron Ekblad: 1+ assists | 0.332 | 0.265 | 27/74 | +0.049 | STANDARD |

**BUF @ CHI** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.6, exp saves 25.6 (sd 6.94), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 25.26, exp saves 21.83 (sd 6.13), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ assists | 0.428 | 0.520 | 54/50 | +0.055 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.524 | 0.615 | 64/41 | +0.049 | STANDARD |
| Tage Thompson: 2+ points | 0.208 | 0.285 | 32/75 | +0.029 | STANDARD |
| Tage Thompson: 1+ assists | 0.347 | 0.415 | 43/60 | +0.036 | STANDARD |
| Tage Thompson: 1+ points | 0.568 | 0.635 | 66/39 | +0.025 | STANDARD |
| Connor Bedard: 1+ assists | 0.429 | 0.495 | 51/52 | +0.033 | STANDARD |

**WPG @ DAL** · priced 150/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.63, exp saves 21.68 (sd 6.09), pull risk 0.05
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.73, exp saves 22.89 (sd 6.32), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.251 | 0.395 | 42/63 | +0.102 | STANDARD |
| Josh Morrissey: 1+ points | 0.326 | 0.445 | 47/58 | +0.077 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.443 | 0.515 | 53/50 | +0.039 | STANDARD |
| Mikko Rantanen: 1+ points | 0.607 | 0.675 | 70/35 | +0.027 | STANDARD |
| Mikko Rantanen: 2+ points | 0.246 | 0.310 | 33/71 | +0.030 | STANDARD |
| Cole Perfetti: 1+ assists | 0.359 | 0.295 | 31/72 | +0.034 | STANDARD |

**STL @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.63, exp saves 22.15 (sd 6.24), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.91, exp saves 24.86 (sd 6.75), pull risk 0.067

**NYI @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.99, exp saves 23.6 (sd 6.32), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.47, exp saves 24.61 (sd 6.68), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
