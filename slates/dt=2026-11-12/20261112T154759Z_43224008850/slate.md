# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-12T15:47:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4015 · contracts joined: 2342 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 2067, 'OK': 154, 'NO_EDGE': 121}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 306, 'game_early_goal': 11, 'first_goal': 395, 'game_winner': 22, 'player_goals': 681, 'game_overtime': 11, 'player_points': 399, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 2026-11-12T17:00:00Z | T-60m | 0.392 | 0.608 | 0.168 | 6.54 | 2.90 | 3.63 | 216 (25/191) | PROBABLE/PROBABLE |
| MTL @ BOS | 2026-11-13T00:00:00Z | T-6h | 0.566 | 0.434 | 0.177 | 6.02 | 3.21 | 2.81 | 214 (25/189) | PROJECTED/CONFIRMED |
| MIN @ TOR | 2026-11-13T00:00:00Z | T-6h | 0.437 | 0.563 | 0.171 | 6.40 | 2.99 | 3.41 | 204 (25/179) | PROJECTED/PROJECTED |
| COL @ OTT | 2026-11-13T00:00:00Z | T-6h | 0.427 | 0.573 | 0.168 | 6.57 | 3.05 | 3.51 | 226 (25/201) | PROJECTED/PROJECTED |
| WSH @ NJD | 2026-11-13T00:00:00Z | T-6h | 0.557 | 0.443 | 0.175 | 6.17 | 3.27 | 2.91 | 218 (25/193) | PROJECTED/PROJECTED |
| TBL @ CBJ | 2026-11-13T00:00:00Z | T-6h | 0.456 | 0.544 | 0.181 | 5.91 | 2.81 | 3.09 | 215 (25/190) | PROBABLE/PROJECTED |
| DET @ FLA | 2026-11-13T00:30:00Z | T-6h | 0.574 | 0.426 | 0.175 | 6.07 | 3.26 | 2.81 | 219 (25/194) | PROJECTED/PROJECTED |
| BUF @ CHI | 2026-11-13T01:00:00Z | T-6h | 0.476 | 0.524 | 0.175 | 6.06 | 2.95 | 3.11 | 209 (25/184) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-6h | 0.593 | 0.407 | 0.176 | 5.80 | 3.19 | 2.61 | 207 (25/182) | PROJECTED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-6h | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 209 (25/184) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-6h | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 205 (25/180) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV12CARSEA-CAR3 | game_spread | 0.258 | 0.395 | 0.365 | 40 | 61 | no | +0.115 | OK |
| KXNHLSPREAD-26NOV12CARSEA-CAR2 | game_spread | 0.391 | 0.515 | 0.490 | 52 | 49 | no | +0.102 | OK |
| KXNHLGAME-26NOV12CARSEA-SEA | game_winner | 0.392 | 0.275 | 0.297 | 28 | 73 | yes | +0.097 | OK |
| KXNHLGAME-26NOV12CARSEA-CAR | game_winner | 0.608 | 0.725 | 0.703 | 73 | 28 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR4 | team_total | 0.506 | 0.605 | 0.586 | 61 | 40 | no | +0.077 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-6 | game_total | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA3 | team_total | 0.559 | 0.460 | 0.480 | 47 | 55 | yes | +0.071 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-7 | game_total | 0.402 | 0.495 | 0.476 | 50 | 51 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA4 | team_total | 0.343 | 0.250 | 0.267 | 26 | 76 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5 | team_total | 0.308 | 0.395 | 0.377 | 40 | 61 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.389 | 0.480 | 0.462 | 49 | 53 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR3 | team_total | 0.707 | 0.785 | 0.771 | 79 | 22 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ4 | team_total | 0.323 | 0.410 | 0.392 | 42 | 60 | no | +0.060 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-5 | game_total | 0.733 | 0.810 | 0.796 | 82 | 20 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5 | team_total | 0.172 | 0.100 | 0.112 | 11 | 91 | yes | +0.056 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.427 | 0.505 | 0.489 | 51 | 50 | no | +0.055 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA2 | game_spread | 0.201 | 0.135 | 0.147 | 14 | 87 | yes | +0.053 | OK |
| KXNHLTOTAL-26NOV12NYILA-5 | game_total | 0.695 | 0.770 | 0.756 | 78 | 24 | no | +0.052 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-4 | game_total | 0.823 | 0.885 | 0.874 | 89 | 12 | no | +0.050 | OK |
| KXNHLGAME-26NOV12BUFCHI-BUF | game_winner | 0.524 | 0.595 | 0.581 | 60 | 41 | no | +0.049 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.476 | 0.405 | 0.419 | 41 | 60 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5 | team_total | 0.208 | 0.280 | 0.264 | 29 | 73 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF3 | team_total | 0.607 | 0.685 | 0.670 | 70 | 33 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2 | team_total | 0.781 | 0.710 | 0.725 | 72 | 30 | yes | +0.047 | OK |
| KXNHLGAME-26NOV12COLOTT-OTT | game_winner | 0.427 | 0.495 | 0.481 | 50 | 51 | no | +0.046 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-6 | game_total | 0.539 | 0.605 | 0.592 | 61 | 40 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.430 | 0.415 | 44 | 58 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.540 | 0.526 | 55 | 47 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF3 | game_spread | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV12COLOTT-COL2 | game_spread | 0.357 | 0.295 | 0.307 | 30 | 71 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 | team_total | 0.541 | 0.610 | 0.596 | 62 | 40 | no | +0.042 | OK |
| KXNHLGAME-26NOV12MINTOR-MIN | game_winner | 0.563 | 0.625 | 0.613 | 63 | 38 | no | +0.041 | OK |
| KXNHLGAME-26NOV12MINTOR-TOR | game_winner | 0.437 | 0.375 | 0.387 | 38 | 63 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ5 | team_total | 0.159 | 0.220 | 0.207 | 23 | 79 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.813 | 0.870 | 0.860 | 88 | 14 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.305 | 0.365 | 0.353 | 37 | 64 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.845 | 0.836 | 85 | 16 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.751 | 0.805 | 0.795 | 81 | 20 | no | +0.037 | OK |
| KXNHLGAME-26NOV12COLOTT-COL | game_winner | 0.573 | 0.515 | 0.527 | 52 | 49 | yes | +0.036 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-8 | game_total | 0.220 | 0.275 | 0.263 | 28 | 73 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV12COLOTT-COL6 | team_total | 0.142 | 0.095 | 0.103 | 10 | 91 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.838 | 0.885 | 0.877 | 89 | 12 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ2 | team_total | 0.765 | 0.825 | 0.814 | 84 | 19 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV12COLOTT-COL3 | team_total | 0.688 | 0.635 | 0.646 | 64 | 37 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.560 | 0.548 | 57 | 45 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR2 | team_total | 0.873 | 0.920 | 0.912 | 93 | 9 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.790 | 0.780 | 80 | 22 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA6 | team_total | 0.073 | 0.030 | 0.036 | 4 | 98 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12COLOTT-COL5 | team_total | 0.283 | 0.230 | 0.240 | 24 | 78 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-CHI2 | game_spread | 0.262 | 0.215 | 0.224 | 22 | 79 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA3 | game_spread | 0.217 | 0.265 | 0.255 | 27 | 74 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL4 | team_total | 0.325 | 0.375 | 0.365 | 38 | 63 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN3 | game_spread | 0.218 | 0.270 | 0.259 | 28 | 74 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-9 | game_total | 0.151 | 0.200 | 0.189 | 21 | 81 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA3 | game_spread | 0.113 | 0.070 | 0.077 | 8 | 94 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN2 | game_spread | 0.346 | 0.395 | 0.385 | 40 | 61 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ3 | game_spread | 0.134 | 0.175 | 0.166 | 18 | 83 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL2 | team_total | 0.763 | 0.810 | 0.801 | 82 | 20 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ2 | game_spread | 0.240 | 0.285 | 0.276 | 29 | 72 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV12MINTOR-TOR2 | game_spread | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.243 | 0.285 | 0.276 | 29 | 72 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12COLOTT-OTT3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL3 | team_total | 0.541 | 0.590 | 0.580 | 60 | 42 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12COLOTT-COL4 | team_total | 0.478 | 0.430 | 0.440 | 44 | 58 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.492 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-6 | game_total | 0.532 | 0.575 | 0.566 | 58 | 43 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.092 | 0.125 | 0.118 | 13 | 88 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4 | team_total | 0.383 | 0.425 | 0.417 | 43 | 58 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV12COLOTT-OTT2 | game_spread | 0.236 | 0.280 | 0.271 | 29 | 73 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-9 | game_total | 0.169 | 0.210 | 0.201 | 22 | 80 | no | +0.020 | OK |
| KXNHLGAME-26NOV12DETFLA-FLA | game_winner | 0.574 | 0.615 | 0.607 | 62 | 39 | no | +0.019 | OK |
| KXNHLGAME-26NOV12DETFLA-DET | game_winner | 0.426 | 0.385 | 0.393 | 39 | 62 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-10 | game_total | 0.066 | 0.100 | 0.092 | 11 | 91 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-5 | game_total | 0.750 | 0.790 | 0.782 | 80 | 22 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV12COLOTT-COL3 | game_spread | 0.229 | 0.195 | 0.201 | 20 | 81 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL4 | team_total | 0.406 | 0.445 | 0.437 | 45 | 56 | no | +0.017 | OK |
| KXNHLGAME-26NOV12TBCBJ-CBJ | game_winner | 0.456 | 0.495 | 0.487 | 50 | 51 | no | +0.016 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 0.392 | 0.415 | 0.168 | 0.210 | 6.54 | 6.69 | 1.019/0.987 | KXNHLTEAMTOTAL-26NOV12CARSEA-SEA3 +0.039 |
| MTL @ BOS | 0.566 | 0.588 | 0.177 | 0.212 | 6.02 | 6.67 | 0.969/0.983 | KXNHLTOTAL-26NOV12MTLBOS-7 +0.112 |
| MIN @ TOR | 0.437 | 0.498 | 0.171 | 0.215 | 6.40 | 6.48 | 0.965/0.995 | KXNHLGAME-26NOV12MINTOR-MIN -0.060 |
| COL @ OTT | 0.427 | 0.471 | 0.168 | 0.212 | 6.57 | 6.57 | 1.041/0.977 | KXNHLSPREAD-26NOV12COLOTT-COL2 -0.046 |
| WSH @ NJD | 0.557 | 0.556 | 0.175 | 0.216 | 6.17 | 6.31 | 0.959/0.961 | KXNHLTOTAL-26NOV12WSHNJ-7 +0.032 |
| TBL @ CBJ | 0.456 | 0.516 | 0.181 | 0.226 | 5.91 | 6.12 | 0.955/0.974 | KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 +0.069 |
| DET @ FLA | 0.574 | 0.572 | 0.175 | 0.215 | 6.07 | 6.26 | 0.998/1.015 | KXNHLTOTAL-26NOV12DETFLA-7 +0.037 |
| BUF @ CHI | 0.476 | 0.488 | 0.175 | 0.214 | 6.06 | 6.24 | 0.990/0.998 | KXNHLTOTAL-26NOV12BUFCHI-5 +0.031 |
| WPG @ DAL | 0.593 | 0.585 | 0.176 | 0.213 | 5.80 | 6.11 | 0.987/1.001 | KXNHLTOTAL-26NOV12WPGDAL-7 +0.052 |
| STL @ UTA | 0.511 | 0.532 | 0.172 | 0.220 | 6.17 | 6.40 | 0.993/0.993 | KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4 +0.044 |
| NYI @ LAK | 0.554 | 0.551 | 0.185 | 0.221 | 5.66 | 5.99 | 0.990/0.956 | KXNHLTOTAL-26NOV12NYILA-5 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Berkly Catton: 1+ goals YES @ 15c · p 0.2218 (adj 0.2026) · $5.07 · thesis SEA:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 61c · p 0.7523 (adj 0.6566) · $6.74 · thesis SEA:WINS
- Nikolaj Ehlers: 1+ goals NO @ 72c · p 0.7728 (adj 0.7584) · $9.0 · thesis CAR:SUPPRESSED
- William Borgen: 1+ goals YES @ 6c · p 0.0899 (adj 0.0824) · $2.0 · thesis BOS:WINS_BY_2PLUS
- Fraser Minten: 1+ goals YES @ 18c · p 0.2261 (adj 0.2133) · $3.05 · thesis BOS:OFFENSE_4PLUS
- Nick Suzuki: 2+ assists NO @ 86c · p 0.9223 (adj 0.8837) · $9.1 · thesis MTL:SUPPRESSED
- Michael Eyssimont: 1+ goals YES @ 14c · p 0.1673 (adj 0.1592) · $1.35 · thesis BOS:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1772 (adj 0.1542) · $4.99 · thesis TOR:WINS_BY_2PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.625 (adj 0.6013) · $9.1 · thesis MIN:SUPPRESSED
- Easton Cowan: 1+ goals YES @ 18c · p 0.241 (adj 0.2245) · $4.34 · thesis TOR:OFFENSE_4PLUS
- Dakota Joshua: 1+ goals YES @ 10c · p 0.1406 (adj 0.1292) · $2.57 · thesis TOR:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.2084 (adj 0.1913) · $2.78 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 19c · p 0.223 (adj 0.2122) · $1.58 · thesis OTT:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.169 (adj 0.1542) · $3.23 · thesis NJD:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2243 (adj 0.2095) · $3.91 · thesis WSH:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2129 (adj 0.1984) · $3.94 · thesis CBJ:OFFENSE_4PLUS
- Yanni Gourde: 1+ goals NO @ 86c · p 0.9022 (adj 0.8904) · $9.1 · thesis TBL:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2695 (adj 0.2584) · $2.67 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4608 (adj 0.4279) · $3.54 · thesis GAME:LOW_EVENT
- Sam Bennett: 1+ goals YES @ 27c · p 0.3152 (adj 0.3014) · $2.49 · thesis FLA:OFFENSE_4PLUS
- Aaron Ekblad: 1+ assists YES @ 27c · p 0.3375 (adj 0.2988) · $1.9 · thesis FLA:OFFENSE_4PLUS
- J.T. Compher: 1+ goals YES @ 13c · p 0.1565 (adj 0.1486) · $1.34 · thesis DET:OFFENSE_4PLUS
- Tage Thompson: 2+ goals NO @ 90c · p 0.9325 (adj 0.9219) · $8.18 · thesis BUF:SUPPRESSED
- Buffalo wins by over 1.5 goals NO @ 64c · p 0.7093 (adj 0.6722) · $3.21 · thesis CHI:WINS
- Buffalo over 3.5 goals scored NO @ 53c · p 0.6025 (adj 0.5613) · $1.11 · thesis BUF:SUPPRESSED
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.8178 (adj 0.7839) · $1.14 · thesis CHI:WINS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.1923 (adj 0.1805) · $2.74 · thesis DAL:WINS_BY_2PLUS
- Josh Morrissey: 1+ assists NO @ 61c · p 0.7488 (adj 0.6488) · $7.91 · thesis WPG:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 19c · p 0.2462 (adj 0.2296) · $3.92 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 14c · p 0.1824 (adj 0.1706) · $2.78 · thesis UTA:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.162 (adj 0.1515) · $1.63 · thesis STL:OFFENSE_4PLUS
- Daniil But: 1+ goals NO @ 81c · p 0.8462 (adj 0.8347) · $9.1 · thesis UTA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 66c · p 0.8509 (adj 0.7171) · $9.1 · thesis LAK:SUPPRESSED
- Andre Lee: 1+ goals YES @ 9c · p 0.1318 (adj 0.1151) · $2.21 · thesis LAK:OFFENSE_4PLUS
- Alex Laferriere: 1+ goals YES @ 27c · p 0.3125 (adj 0.2994) · $2.56 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ SEA** · priced 164/165 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- SEA net: Philipp Grubauer (PROBABLE) exp shots 31.95, exp saves 27.12 (sd 7.56), pull risk 0.086
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.45, exp saves 20.48 (sd 5.88), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.189 | 0.340 | 35/67 | +0.126 | STANDARD |
| Sebastian Aho: 1+ assists | 0.366 | 0.510 | 52/50 | +0.117 | STANDARD |
| Taylor Hall: 1+ assists | 0.210 | 0.325 | 34/69 | +0.085 | STANDARD |
| Sebastian Aho: 1+ points | 0.542 | 0.655 | 67/36 | +0.082 | STANDARD |
| Berkly Catton: 1+ points | 0.444 | 0.335 | 37/70 | +0.057 | STANDARD |
| Sebastian Aho: 1+ goals | 0.279 | 0.380 | 39/63 | +0.074 | STANDARD |

**MTL @ BOS** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.96, exp saves 23.55 (sd 6.56), pull risk 0.059
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.11, exp saves 23.83 (sd 6.83), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.361 | 0.495 | 51/52 | +0.101 | STANDARD |
| David Pastrnak: 1+ points | 0.692 | 0.575 | 73/58 | -0.052 | STANDARD |
| Nick Suzuki: 1+ points | 0.551 | 0.640 | 65/37 | +0.063 | STANDARD |
| Nick Suzuki: 2+ points | 0.196 | 0.285 | 31/74 | +0.051 | STANDARD |
| Fraser Minten: 1+ points | 0.457 | 0.370 | 39/65 | +0.050 | STANDARD |
| Nick Suzuki: 2+ assists | 0.078 | 0.155 | 17/86 | +0.054 | STANDARD |

**MIN @ TOR** · priced 148/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.08, exp saves 26.87 (sd 7.13), pull risk 0.065
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.87, exp saves 23.93 (sd 6.65), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ points | 0.539 | 0.400 | 41/61 | +0.112 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.275 | 0.400 | 41/61 | +0.099 | STANDARD |
| Easton Cowan: 1+ assists | 0.399 | 0.280 | 29/73 | +0.095 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.641 | 0.745 | 75/26 | +0.086 | STANDARD |
| Matt Boldy: 2+ points | 0.237 | 0.340 | 35/67 | +0.077 | STANDARD |
| Matt Boldy: 1+ assists | 0.401 | 0.500 | 51/51 | +0.072 | STANDARD |

**COL @ OTT** · priced 168/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 28.4, exp saves 24.47 (sd 6.75), pull risk 0.07
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 27.05, exp saves 23.54 (sd 6.53), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ points | 0.348 | 0.270 | 29/75 | +0.044 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.476 | 0.550 | 56/46 | +0.046 | STANDARD |
| Ridly Greig: 1+ goals | 0.208 | 0.140 | 16/88 | +0.039 | STANDARD |
| Jordan Spence: 1+ assists | 0.288 | 0.220 | 23/79 | +0.046 | STANDARD |
| Artturi Lehkonen: 1+ points | 0.527 | 0.465 | 47/54 | +0.039 | STANDARD |
| Jake Sanderson: 1+ assists | 0.390 | 0.450 | 46/56 | +0.033 | STANDARD |

**WSH @ NJD** · priced 159/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 25.32, exp saves 22.03 (sd 6.08), pull risk 0.058
- WSH net: Logan Thompson (PROJECTED) exp shots 30.42, exp saves 26.06 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brett Pesce: 1+ points | 0.360 | 0.270 | 29/75 | +0.055 | STANDARD |
| Brett Pesce: 1+ assists | 0.309 | 0.230 | 25/79 | +0.046 | STANDARD |
| Luke Evangelista: 1+ assists | 0.272 | 0.340 | 36/68 | +0.033 | STANDARD |
| Jack Hughes: 1+ assists | 0.458 | 0.525 | 54/49 | +0.034 | STANDARD |
| Jack Hughes: 2+ points | 0.297 | 0.360 | 38/66 | +0.027 | STANDARD |
| Arseny Gritsyuk: 1+ points | 0.496 | 0.435 | 45/58 | +0.029 | STANDARD |

**TBL @ CBJ** · priced 161/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 27.7, exp saves 24.15 (sd 6.54), pull risk 0.054
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.39, exp saves 22.8 (sd 6.27), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.437 | 0.600 | 61/41 | +0.136 | STANDARD |
| Nikita Kucherov: 2+ points | 0.263 | 0.395 | 41/62 | +0.101 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.111 | 0.230 | 25/79 | +0.087 | STANDARD |
| Yanni Gourde: 1+ points | 0.246 | 0.350 | 37/67 | +0.069 | STANDARD |
| Nikita Kucherov: 3+ points | 0.080 | 0.160 | 17/85 | +0.061 | STANDARD |
| Nikita Kucherov: 1+ points | 0.621 | 0.555 | 75/64 | -0.142 | STANDARD |

**DET @ FLA** · priced 159/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 27.02, exp saves 23.51 (sd 6.42), pull risk 0.053
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.83, exp saves 23.79 (sd 6.67), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aaron Ekblad: 1+ assists | 0.338 | 0.260 | 27/75 | +0.054 | STANDARD |
| Aaron Ekblad: 1+ points | 0.393 | 0.320 | 33/69 | +0.047 | STANDARD |
| Sam Bennett: 2+ points | 0.188 | 0.120 | 17/93 | +0.008 | STANDARD |
| Gustav Forsling: 1+ points | 0.358 | 0.295 | 32/73 | +0.023 | STANDARD |
| Sam Reinhart: 1+ assists | 0.339 | 0.400 | 41/61 | +0.035 | STANDARD |
| Lucas Raymond: 1+ assists | 0.358 | 0.415 | 42/59 | +0.035 | STANDARD |

**BUF @ CHI** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.67, exp saves 25.65 (sd 6.91), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 25.13, exp saves 21.73 (sd 6.09), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ assists | 0.423 | 0.535 | 55/48 | +0.080 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.519 | 0.630 | 64/38 | +0.084 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.172 | 0.265 | 28/75 | +0.065 | STANDARD |
| Tage Thompson: 1+ points | 0.570 | 0.660 | 67/35 | +0.065 | STANDARD |
| Connor Bedard: 1+ assists | 0.429 | 0.510 | 52/50 | +0.053 | STANDARD |
| Tage Thompson: 2+ points | 0.210 | 0.290 | 32/74 | +0.037 | STANDARD |

**WPG @ DAL** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.73 (sd 5.96), pull risk 0.045
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.72, exp saves 22.82 (sd 6.39), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.251 | 0.405 | 42/61 | +0.122 | STANDARD |
| Josh Morrissey: 1+ points | 0.326 | 0.450 | 46/56 | +0.097 | STANDARD |
| Josh Morrissey: 2+ points | 0.058 | 0.145 | 16/87 | +0.064 | STANDARD |
| Mikko Rantanen: 2+ points | 0.246 | 0.325 | 34/69 | +0.049 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.443 | 0.520 | 54/50 | +0.039 | STANDARD |
| Josh Morrissey: 2+ assists | 0.031 | 0.100 | 12/92 | +0.044 | STANDARD |

**STL @ UTA** · priced 151/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.26), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.65, exp saves 24.64 (sd 6.73), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 1+ assists | 0.478 | 0.570 | 58/44 | +0.065 | STANDARD |
| Clayton Keller: 2+ points | 0.270 | 0.355 | 37/66 | +0.054 | STANDARD |
| Robert Thomas: 1+ assists | 0.431 | 0.515 | 53/50 | +0.052 | STANDARD |
| MacKenzie Weegar: 1+ assists | 0.367 | 0.285 | 30/73 | +0.052 | STANDARD |
| Barrett Hayton: 1+ assists | 0.333 | 0.260 | 27/75 | +0.050 | STANDARD |
| MacKenzie Weegar: 1+ points | 0.422 | 0.350 | 37/67 | +0.035 | STANDARD |

**NYI @ LAK** · priced 143/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.98, exp saves 23.62 (sd 6.37), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.46, exp saves 24.61 (sd 6.69), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.149 | 0.355 | 37/66 | +0.175 | STANDARD |
| Mats Zuccarello: 1+ points | 0.313 | 0.470 | 49/55 | +0.120 | STANDARD |
| Alex Laferriere: 1+ points | 0.608 | 0.530 | 54/48 | +0.050 | STANDARD |
| Alex Laferriere: 2+ points | 0.244 | 0.170 | 20/86 | +0.033 | STANDARD |
| Alex Turcotte: 1+ goals | 0.140 | 0.070 | 12/98 | +0.013 | STANDARD |
| Artemi Panarin: 1+ assists | 0.452 | 0.520 | 53/49 | +0.041 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
