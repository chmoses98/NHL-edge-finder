# NHL slate 2026-11-14 — RESEARCH_ONLY

generated 2026-11-14T17:59:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4717 · contracts joined: 3061 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 2711, 'OK': 194, 'NO_EDGE': 156}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 406, 'game_early_goal': 14, 'first_goal': 501, 'game_winner': 28, 'player_goals': 864, 'game_overtime': 14, 'player_points': 557, 'goalie_saves': 19, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CAR | 2026-11-14T18:00:00Z | T-<10m | 0.695 | 0.305 | 0.153 | 6.47 | 3.88 | 2.58 | 219 (25/194) | CONFIRMED/CONFIRMED |
| WPG @ CHI | 2026-11-14T20:30:00Z | T-90m | 0.455 | 0.545 | 0.180 | 5.98 | 2.85 | 3.12 | 223 (25/198) | PROJECTED/PROJECTED |
| MIN @ BOS | 2026-11-15T00:00:00Z | T-6h | 0.525 | 0.475 | 0.181 | 5.85 | 3.01 | 2.84 | 221 (25/196) | CONFIRMED/CONFIRMED |
| EDM @ TOR | 2026-11-15T00:00:00Z | T-6h | 0.414 | 0.586 | 0.164 | 6.88 | 3.15 | 3.73 | 227 (25/202) | CONFIRMED/PROJECTED |
| COL @ MTL | 2026-11-15T00:00:00Z | T-6h | 0.451 | 0.549 | 0.168 | 6.50 | 3.11 | 3.40 | 204 (25/179) | CONFIRMED/CONFIRMED |
| DET @ TBL | 2026-11-15T00:00:00Z | T-6h | 0.661 | 0.339 | 0.167 | 6.08 | 3.55 | 2.53 | 195 (25/170) | PROBABLE/PROBABLE |
| OTT @ PIT | 2026-11-15T00:00:00Z | T-6h | 0.500 | 0.500 | 0.175 | 6.60 | 3.30 | 3.30 | 229 (25/204) | CONFIRMED/CONFIRMED |
| NJD @ WSH | 2026-11-15T00:00:00Z | T-6h | 0.450 | 0.550 | 0.171 | 6.56 | 3.11 | 3.45 | 232 (25/207) | CONFIRMED/CONFIRMED |
| PHI @ CBJ | 2026-11-15T00:00:00Z | T-6h | 0.585 | 0.415 | 0.185 | 5.64 | 3.07 | 2.57 | 215 (25/190) | CONFIRMED/CONFIRMED |
| FLA @ STL | 2026-11-15T00:00:00Z | T-6h | 0.589 | 0.411 | 0.178 | 6.18 | 3.37 | 2.81 | 221 (25/196) | CONFIRMED/CONFIRMED |
| BUF @ DAL | 2026-11-15T01:00:00Z | T-6h | 0.548 | 0.452 | 0.179 | 5.87 | 3.08 | 2.79 | 227 (25/202) | CONFIRMED/PROBABLE |
| SJS @ UTA | 2026-11-15T02:00:00Z | T-6h | 0.665 | 0.335 | 0.166 | 6.45 | 3.77 | 2.68 | 206 (25/181) | PROBABLE/PROJECTED |
| NYI @ ANA | 2026-11-15T03:00:00Z | T-6h | 0.554 | 0.446 | 0.170 | 6.54 | 3.45 | 3.10 | 228 (25/203) | PROJECTED/PROJECTED |
| CGY @ LAK | 2026-11-15T03:00:00Z | T-6h | 0.562 | 0.438 | 0.184 | 5.53 | 2.95 | 2.58 | 214 (25/189) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV14COLMTL-MTL | game_winner | 0.451 | 0.565 | 0.542 | 57 | 44 | no | +0.092 | OK |
| KXNHLGAME-26NOV14COLMTL-COL | game_winner | 0.549 | 0.435 | 0.458 | 44 | 57 | yes | +0.092 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA4 | team_total | 0.354 | 0.465 | 0.442 | 47 | 54 | no | +0.089 | OK |
| KXNHLSPREAD-26NOV14SEACAR-CAR3 | game_spread | 0.335 | 0.445 | 0.422 | 45 | 56 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG4 | team_total | 0.389 | 0.495 | 0.473 | 50 | 51 | no | +0.084 | OK |
| KXNHLSPREAD-26NOV14SEACAR-CAR2 | game_spread | 0.481 | 0.585 | 0.564 | 59 | 42 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA3 | team_total | 0.576 | 0.670 | 0.652 | 68 | 34 | no | +0.068 | OK |
| KXNHLTOTAL-26NOV14CGYLA-6 | game_total | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.064 | OK |
| KXNHLGAME-26NOV14SEACAR-CAR | game_winner | 0.695 | 0.775 | 0.760 | 78 | 23 | no | +0.063 | OK |
| KXNHLGAME-26NOV14SEACAR-SEA | game_winner | 0.305 | 0.225 | 0.240 | 23 | 78 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3 | team_total | 0.477 | 0.395 | 0.411 | 40 | 61 | yes | +0.060 | OK |
| KXNHLTOTAL-26NOV14CGYLA-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN3 | team_total | 0.547 | 0.630 | 0.614 | 64 | 38 | no | +0.056 | OK |
| KXNHLTOTAL-26NOV14CGYLA-7 | game_total | 0.338 | 0.415 | 0.399 | 42 | 59 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN4 | team_total | 0.329 | 0.410 | 0.393 | 42 | 60 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA3 | game_spread | 0.193 | 0.265 | 0.249 | 27 | 74 | no | +0.054 | OK |
| KXNHLGAME-26NOV14FLASTL-FLA | game_winner | 0.411 | 0.485 | 0.470 | 49 | 52 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4 | team_total | 0.271 | 0.200 | 0.213 | 21 | 81 | yes | +0.049 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-5 | game_total | 0.729 | 0.795 | 0.783 | 80 | 21 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-6 | game_total | 0.504 | 0.575 | 0.561 | 58 | 43 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV14WPGCHI-WPG2 | game_spread | 0.315 | 0.385 | 0.370 | 39 | 62 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV14COLMTL-MTL3 | game_spread | 0.150 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL4 | team_total | 0.455 | 0.380 | 0.395 | 39 | 63 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA3 | team_total | 0.536 | 0.610 | 0.596 | 62 | 40 | no | +0.047 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-7 | game_total | 0.396 | 0.465 | 0.451 | 47 | 54 | no | +0.046 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-7 | game_total | 0.408 | 0.475 | 0.461 | 48 | 53 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV14COLMTL-COL2 | game_spread | 0.328 | 0.265 | 0.277 | 27 | 74 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG3 | team_total | 0.610 | 0.680 | 0.667 | 69 | 33 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV14MINBOS-MIN3 | game_spread | 0.145 | 0.205 | 0.192 | 21 | 80 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV14FLASTL-FLA2 | game_spread | 0.212 | 0.275 | 0.262 | 28 | 73 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA4 | team_total | 0.321 | 0.390 | 0.376 | 40 | 62 | no | +0.043 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-6 | game_total | 0.520 | 0.585 | 0.572 | 59 | 42 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR4 | team_total | 0.561 | 0.625 | 0.612 | 63 | 38 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA5 | team_total | 0.176 | 0.250 | 0.234 | 27 | 77 | no | +0.042 | OK |
| KXNHLGAME-26NOV14CGYLA-CGY | game_winner | 0.438 | 0.375 | 0.387 | 38 | 63 | yes | +0.041 | OK |
| KXNHLGAME-26NOV14CGYLA-LA | game_winner | 0.562 | 0.625 | 0.613 | 63 | 38 | no | +0.041 | OK |
| KXNHLGAME-26NOV14FLASTL-STL | game_winner | 0.589 | 0.525 | 0.538 | 53 | 48 | yes | +0.041 | OK |
| KXNHLSPREAD-26NOV14COLMTL-MTL2 | game_spread | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA2 | team_total | 0.716 | 0.655 | 0.668 | 66 | 35 | yes | +0.041 | OK |
| KXNHLSPREAD-26NOV14FLASTL-FLA3 | game_spread | 0.119 | 0.180 | 0.166 | 19 | 83 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-5 | game_total | 0.696 | 0.755 | 0.744 | 76 | 25 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV14MINBOS-MIN2 | game_spread | 0.255 | 0.315 | 0.302 | 32 | 69 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA2 | game_spread | 0.325 | 0.385 | 0.373 | 39 | 62 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV14CGYLA-4 | game_total | 0.782 | 0.840 | 0.829 | 85 | 17 | no | +0.038 | OK |
| KXNHLGAME-26NOV14MINBOS-BOS | game_winner | 0.525 | 0.465 | 0.477 | 47 | 54 | yes | +0.038 | OK |
| KXNHLGAME-26NOV14MINBOS-MIN | game_winner | 0.475 | 0.535 | 0.523 | 54 | 47 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL6 | team_total | 0.122 | 0.070 | 0.078 | 8 | 94 | yes | +0.037 | OK |
| KXNHLSPREAD-26NOV14COLMTL-COL3 | game_spread | 0.206 | 0.155 | 0.164 | 16 | 85 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA2 | team_total | 0.794 | 0.850 | 0.840 | 86 | 16 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-6 | game_total | 0.466 | 0.525 | 0.513 | 53 | 48 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV14FLASTL-STL2 | game_spread | 0.361 | 0.305 | 0.316 | 31 | 70 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV14OTTPIT-PIT3 | team_total | 0.643 | 0.580 | 0.593 | 59 | 43 | yes | +0.036 | OK |
| KXNHLSPREAD-26NOV14WPGCHI-WPG3 | game_spread | 0.192 | 0.250 | 0.237 | 26 | 76 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL5 | team_total | 0.257 | 0.195 | 0.206 | 21 | 82 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV14MINBOS-7 | game_total | 0.389 | 0.445 | 0.434 | 45 | 56 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN5 | team_total | 0.164 | 0.220 | 0.208 | 23 | 79 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA5 | team_total | 0.130 | 0.075 | 0.084 | 9 | 94 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL3 | team_total | 0.661 | 0.600 | 0.612 | 61 | 41 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14BUFDAL-DAL4 | team_total | 0.380 | 0.440 | 0.428 | 45 | 57 | no | +0.033 | OK |
| KXNHLGAME-26NOV14OTTPIT-OTT | game_winner | 0.500 | 0.555 | 0.544 | 56 | 45 | no | +0.033 | OK |
| KXNHLGAME-26NOV14OTTPIT-PIT | game_winner | 0.500 | 0.445 | 0.456 | 45 | 56 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL5 | team_total | 0.254 | 0.185 | 0.198 | 21 | 84 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV14OTTPIT-PIT5 | team_total | 0.243 | 0.185 | 0.196 | 20 | 83 | yes | +0.032 | OK |
| KXNHLTOTAL-26NOV14MINBOS-5 | game_total | 0.726 | 0.775 | 0.766 | 78 | 23 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN2 | team_total | 0.768 | 0.825 | 0.815 | 84 | 19 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-4 | game_total | 0.821 | 0.870 | 0.861 | 88 | 14 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI4 | team_total | 0.264 | 0.325 | 0.312 | 34 | 69 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL4 | team_total | 0.447 | 0.390 | 0.401 | 40 | 62 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV14MINBOS-BOS2 | game_spread | 0.304 | 0.255 | 0.264 | 26 | 75 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL3 | team_total | 0.667 | 0.610 | 0.622 | 62 | 40 | yes | +0.030 | OK |
| KXNHLTOTAL-26NOV14OTTPIT-8 | game_total | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA5 | team_total | 0.159 | 0.210 | 0.199 | 22 | 80 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV14MINBOS-6 | game_total | 0.504 | 0.560 | 0.549 | 57 | 45 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-7 | game_total | 0.355 | 0.410 | 0.399 | 42 | 60 | no | +0.029 | OK |
| KXNHLGAME-26NOV14WPGCHI-WPG | game_winner | 0.545 | 0.595 | 0.585 | 60 | 41 | no | +0.028 | OK |
| KXNHLGAME-26NOV14WPGCHI-CHI | game_winner | 0.455 | 0.405 | 0.415 | 41 | 60 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL2 | team_total | 0.849 | 0.800 | 0.811 | 81 | 21 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI2 | team_total | 0.719 | 0.775 | 0.765 | 79 | 24 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR5 | team_total | 0.355 | 0.410 | 0.399 | 42 | 60 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV14OTTPIT-7 | game_total | 0.515 | 0.465 | 0.475 | 47 | 54 | yes | +0.028 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CAR | 0.695 | 0.578 | 0.153 | 0.210 | 6.47 | 6.65 | 1.002/0.998 | KXNHLSPREAD-26NOV14SEACAR-CAR2 -0.126 |
| WPG @ CHI | 0.455 | 0.472 | 0.180 | 0.221 | 5.98 | 6.25 | 0.990/1.001 | KXNHLTOTAL-26NOV14WPGCHI-7 +0.053 |
| MIN @ BOS | 0.525 | 0.545 | 0.181 | 0.222 | 5.85 | 6.46 | 0.955/0.991 | KXNHLTOTAL-26NOV14MINBOS-7 +0.112 |
| EDM @ TOR | 0.414 | 0.442 | 0.164 | 0.210 | 6.88 | 6.82 | 0.955/0.994 | KXNHLSPREAD-26NOV14EDMTOR-EDM2 -0.031 |
| COL @ MTL | 0.451 | 0.465 | 0.168 | 0.214 | 6.50 | 6.63 | 0.942/0.978 | KXNHLTEAMTOTAL-26NOV14COLMTL-MTL4 +0.027 |
| DET @ TBL | 0.661 | 0.654 | 0.167 | 0.205 | 6.08 | 6.33 | 0.951/1.019 | KXNHLTOTAL-26NOV14DETTB-7 +0.043 |
| OTT @ PIT | 0.500 | 0.485 | 0.175 | 0.217 | 6.60 | 6.32 | 1.012/0.968 | KXNHLTOTAL-26NOV14OTTPIT-6 -0.047 |
| NJD @ WSH | 0.450 | 0.490 | 0.171 | 0.216 | 6.56 | 6.41 | 1.015/0.949 | KXNHLSPREAD-26NOV14NJWSH-NJ2 -0.047 |
| PHI @ CBJ | 0.585 | 0.554 | 0.185 | 0.230 | 5.64 | 5.69 | 0.946/0.990 | KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI3 +0.032 |
| FLA @ STL | 0.589 | 0.572 | 0.178 | 0.217 | 6.18 | 6.31 | 0.976/1.014 | KXNHLTEAMTOTAL-26NOV14FLASTL-FLA3 +0.030 |
| BUF @ DAL | 0.548 | 0.551 | 0.179 | 0.222 | 5.87 | 6.17 | 0.994/0.985 | KXNHLTOTAL-26NOV14BUFDAL-5 +0.052 |
| SJS @ UTA | 0.665 | 0.613 | 0.166 | 0.203 | 6.45 | 6.36 | 0.990/1.034 | KXNHLSPREAD-26NOV14SJUTA-UTA2 -0.057 |
| NYI @ ANA | 0.554 | 0.575 | 0.170 | 0.208 | 6.54 | 6.83 | 1.030/0.956 | KXNHLTOTAL-26NOV14NYIANA-7 +0.046 |
| CGY @ LAK | 0.562 | 0.591 | 0.184 | 0.221 | 5.53 | 5.99 | 0.989/0.986 | KXNHLTOTAL-26NOV14CGYLA-7 +0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 49 recommended · full analysis in card.md / packet.json `thesis_card`

- Berkly Catton: 1+ goals YES @ 14c · p 0.22 (adj 0.1975) · $3.54 · thesis SEA:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 42c · p 0.6348 (adj 0.4919) · $5.85 · thesis SEA:WINS
- Nikolaj Ehlers: 1+ goals NO @ 71c · p 0.784 (adj 0.7643) · $6.13 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2631 (adj 0.2486) · $2.78 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 60c · p 0.7333 (adj 0.6402) · $6.21 · thesis CHI:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 12c · p 0.1502 (adj 0.1414) · $1.34 · thesis CHI:OFFENSE_4PLUS
- Winnipeg over 3.5 goals scored NO @ 51c · p 0.5855 (adj 0.5453) · $2.97 · thesis WPG:SUPPRESSED
- William Borgen: 1+ goals YES @ 5c · p 0.0856 (adj 0.073) · $1.28 · thesis BOS:WINS_BY_2PLUS
- Kirill Kaprizov: 1+ goals NO @ 59c · p 0.655 (adj 0.635) · $5.42 · thesis MIN:SUPPRESSED
- Michael Eyssimont: 1+ goals YES @ 12c · p 0.1531 (adj 0.1436) · $1.32 · thesis BOS:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1657 (adj 0.1493) · $2.56 · thesis TOR:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 10c · p 0.1426 (adj 0.1295) · $1.9 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 31c · p 0.4033 (adj 0.3542) · $3.33 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 27c · p 0.3469 (adj 0.3034) · $2.26 · thesis EDM:OFFENSE_4PLUS
- Martin Necas: 1+ goals YES @ 31c · p 0.3907 (adj 0.3693) · $3.57 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 31c · p 0.3888 (adj 0.3679) · $3.5 · thesis COL:OFFENSE_4PLUS
- Brock Nelson: 1+ goals YES @ 19c · p 0.2543 (adj 0.2345) · $2.24 · thesis COL:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 50c · p 0.6154 (adj 0.5339) · $2.59 · thesis MTL:SUPPRESSED
- Conor Geekie: 1+ goals NO @ 82c · p 0.8728 (adj 0.8583) · $5.36 · thesis TBL:SUPPRESSED
- Jake Guentzel: 2+ goals YES @ 8c · p 0.1144 (adj 0.1046) · $1.27 · thesis TBL:OFFENSE_4PLUS
- Jake Guentzel: 1+ goals YES @ 38c · p 0.4445 (adj 0.4259) · $3.43 · thesis TBL:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 37c · p 0.4632 (adj 0.4141) · $3.96 · thesis TBL:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1521 (adj 0.1416) · $1.15 · thesis PIT:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 56c · p 0.6353 (adj 0.5927) · $2.95 · thesis OTT:SUPPRESSED
- Pierre-Luc Dubois: 1+ goals YES @ 18c · p 0.2302 (adj 0.2139) · $1.94 · thesis WSH:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1512 (adj 0.1359) · $1.52 · thesis NJD:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 24c · p 0.3207 (adj 0.2753) · $1.72 · thesis WSH:OFFENSE_4PLUS
- Luca Del Bel Belluz: 1+ goals NO @ 86c · p 0.9154 (adj 0.9003) · $6.12 · thesis CBJ:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 15c · p 0.1954 (adj 0.1828) · $2.33 · thesis PHI:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2128 (adj 0.1983) · $1.61 · thesis CBJ:WINS_BY_2PLUS
- Travis Konecny: 1+ assists NO @ 67c · p 0.7463 (adj 0.7006) · $5.47 · thesis PHI:SUPPRESSED
- Pius Suter: 1+ goals YES @ 13c · p 0.1651 (adj 0.1551) · $1.44 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3514 (adj 0.3373) · $2.46 · thesis STL:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 25c · p 0.2971 (adj 0.2841) · $2.07 · thesis STL:OFFENSE_4PLUS
- Dylan Holloway: 1+ goals YES @ 26c · p 0.2976 (adj 0.2869) · $1.42 · thesis STL:OFFENSE_4PLUS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.196 (adj 0.182) · $1.97 · thesis DAL:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 28c · p 0.3225 (adj 0.3094) · $1.57 · thesis DAL:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 22c · p 0.2581 (adj 0.2461) · $1.42 · thesis BUF:OFFENSE_4PLUS
- Daniil But: 1+ goals NO @ 80c · p 0.8578 (adj 0.8421) · $6.21 · thesis UTA:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 67c · p 0.7546 (adj 0.7048) · $5.29 · thesis SJS:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 59c · p 0.6649 (adj 0.62) · $2.51 · thesis UTA:SUPPRESSED
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0984 (adj 0.0876) · $1.74 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1491 (adj 0.1356) · $2.4 · thesis ANA:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 11c · p 0.156 (adj 0.1432) · $2.18 · thesis ANA:OFFENSE_4PLUS
- Troy Terry: 1+ assists NO @ 67c · p 0.8391 (adj 0.7162) · $6.21 · thesis ANA:SUPPRESSED
- Kevin Fiala: 1+ assists NO @ 61c · p 0.8191 (adj 0.6734) · $3.55 · thesis LAK:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0776 (adj 0.0707) · $1.09 · thesis LAK:WINS_BY_2PLUS
- Mats Zuccarello: 1+ assists NO @ 68c · p 0.8134 (adj 0.7202) · $3.55 · thesis LAK:SUPPRESSED
- Artemi Panarin: 1+ goals NO @ 65c · p 0.7014 (adj 0.6861) · $2.2 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ CAR** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 22.35, exp saves 19.41 (sd 5.66), pull risk 0.06
- SEA net: Joey Daccord (CONFIRMED) exp shots 32.91, exp saves 28.23 (sd 7.6), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.184 | 0.395 | 40/61 | +0.189 | STANDARD |
| Sebastian Aho: 1+ points | 0.548 | 0.735 | 75/28 | +0.158 | STANDARD |
| Sebastian Aho: 1+ assists | 0.369 | 0.525 | 54/49 | +0.124 | STANDARD |
| Sebastian Aho: 1+ goals | 0.281 | 0.435 | 44/57 | +0.132 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.442 | 0.570 | 58/44 | +0.100 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.371 | 0.495 | 51/52 | +0.091 | STANDARD |

**WPG @ CHI** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.2, exp saves 24.26 (sd 6.68), pull risk 0.063
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.42, exp saves 22.0 (sd 6.15), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.267 | 0.410 | 42/60 | +0.117 | STANDARD |
| Josh Morrissey: 1+ points | 0.404 | 0.545 | 55/46 | +0.119 | STANDARD |
| Josh Morrissey: 1+ assists | 0.325 | 0.465 | 47/54 | +0.118 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.540 | 55/47 | +0.081 | STANDARD |
| Josh Morrissey: 2+ points | 0.093 | 0.190 | 20/82 | +0.077 | STANDARD |
| Kyle Connor: 2+ points | 0.278 | 0.370 | 38/64 | +0.066 | STANDARD |

**MIN @ BOS** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.01, exp saves 25.27 (sd 6.85), pull risk 0.056
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.53, exp saves 23.65 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Hampus Lindholm: 1+ points | 0.392 | 0.145 | 26/97 | +0.118 | STANDARD |
| Jesper Wallstedt: 23+ saves | 0.568 | 0.405 | 55/74 | +0.001 |  |
| Hampus Lindholm: 1+ assists | 0.339 | 0.185 | 23/86 | +0.096 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.247 | 0.355 | 37/66 | +0.077 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.610 | 0.705 | 71/30 | +0.075 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.407 | 0.500 | 51/51 | +0.065 | STANDARD |

**EDM @ TOR** · priced 174/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 29.92, exp saves 25.62 (sd 7.2), pull risk 0.087
- EDM net: Devon Levi (PROJECTED) exp shots 27.37, exp saves 23.77 (sd 6.56), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.471 | 0.595 | 61/42 | +0.092 | STANDARD |
| Connor McDavid: 2+ assists | 0.222 | 0.345 | 35/66 | +0.102 | STANDARD |
| Connor McDavid: 2+ points | 0.429 | 0.545 | 55/46 | +0.094 | STANDARD |
| Leon Draisaitl: 2+ points | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Connor McDavid: 1+ assists | 0.597 | 0.695 | 70/31 | +0.078 | STANDARD |
| John Tavares: 1+ assists | 0.274 | 0.370 | 38/64 | +0.070 | STANDARD |

**COL @ MTL** · priced 147/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.75, exp saves 26.28 (sd 7.16), pull risk 0.08
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.08, exp saves 22.45 (sd 6.29), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.385 | 0.510 | 52/50 | +0.098 | STANDARD |
| Jakub Dobes: 28+ saves | 0.429 | 0.305 | 32/71 | +0.093 |  |
| Gabriel Landeskog: 1+ points | 0.494 | 0.395 | 41/62 | +0.067 | STANDARD |
| Gabriel Landeskog: 1+ assists | 0.323 | 0.225 | 25/80 | +0.060 | STANDARD |
| Martin Necas: 1+ goals | 0.391 | 0.305 | 31/70 | +0.066 | STANDARD |
| Artturi Lehkonen: 1+ goals | 0.389 | 0.305 | 31/70 | +0.064 | STANDARD |

**DET @ TBL** · priced 136/144 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.0, exp saves 22.96 (sd 6.3), pull risk 0.044
- DET net: Daniil Tarasov (PROBABLE) exp shots 28.29, exp saves 23.89 (sd 6.79), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 23+ saves | 0.524 | 0.370 | 52/78 | -0.014 |  |
| Nikita Kucherov: 1+ assists | 0.537 | 0.635 | 64/37 | +0.077 | STANDARD |
| Nikita Kucherov: 2+ points | 0.378 | 0.465 | 47/54 | +0.064 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.188 | 0.270 | 29/75 | +0.049 | STANDARD |
| Jake Guentzel: 1+ goals | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |
| Charle-Edouard D'Astous: 1+ assists | 0.468 | 0.400 | 42/62 | +0.031 | STANDARD |

**OTT @ PIT** · priced 171/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.72, exp saves 23.01 (sd 6.47), pull risk 0.068
- OTT net: Linus Ullmark (CONFIRMED) exp shots 26.84, exp saves 23.29 (sd 6.46), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.432 | 0.520 | 53/49 | +0.060 | STANDARD |
| Jake Sanderson: 1+ assists | 0.365 | 0.450 | 46/56 | +0.058 | STANDARD |
| Jordan Spence: 1+ points | 0.361 | 0.285 | 30/73 | +0.047 | STANDARD |
| Jake Sanderson: 1+ points | 0.444 | 0.520 | 54/50 | +0.038 | STANDARD |
| Egor Chinakhov: 1+ points | 0.415 | 0.340 | 37/69 | +0.029 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.273 | 0.200 | 22/82 | +0.041 | STANDARD |

**NJD @ WSH** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 29.47, exp saves 25.55 (sd 6.83), pull risk 0.064
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.15, exp saves 22.66 (sd 6.38), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.244 | 0.140 | 16/88 | +0.075 | STANDARD |
| Aliaksei Protas: 1+ points | 0.466 | 0.370 | 38/64 | +0.069 | STANDARD |
| Ryan Leonard: 1+ assists | 0.321 | 0.230 | 24/78 | +0.068 | STANDARD |
| Jack Hughes: 2+ points | 0.276 | 0.355 | 37/66 | +0.049 | STANDARD |
| Ryan Leonard: 1+ points | 0.469 | 0.395 | 41/62 | +0.042 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.313 | 0.385 | 40/63 | +0.041 | STANDARD |

**PHI @ CBJ** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.08, exp saves 21.91 (sd 5.92), pull risk 0.039
- PHI net: Joseph Woll (CONFIRMED) exp shots 27.6, exp saves 23.86 (sd 6.53), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kent Johnson: 1+ points | 0.466 | 0.565 | 58/45 | +0.066 | STANDARD |
| Travis Konecny: 1+ points | 0.393 | 0.485 | 49/52 | +0.069 | STANDARD |
| Travis Konecny: 1+ assists | 0.254 | 0.345 | 36/67 | +0.061 | STANDARD |
| Joseph Woll: 25+ saves | 0.453 | 0.365 | 51/78 | -0.075 |  |
| Trevor Zegras: 1+ points | 0.444 | 0.525 | 54/49 | +0.049 | STANDARD |
| Trevor Zegras: 1+ assists | 0.305 | 0.385 | 40/63 | +0.049 | STANDARD |

**FLA @ STL** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.91, exp saves 24.38 (sd 6.5), pull risk 0.053
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 26.59, exp saves 22.82 (sd 6.44), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Tkachuk: 1+ assists | 0.435 | 0.520 | 54/50 | +0.047 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.221 | 0.305 | 32/71 | +0.055 | STANDARD |
| Brady Tkachuk: 1+ points | 0.509 | 0.585 | 60/43 | +0.044 | STANDARD |
| Brady Tkachuk: 2+ points | 0.165 | 0.235 | 24/77 | +0.052 | STANDARD |
| Jake Neighbours: 1+ assists | 0.340 | 0.270 | 29/75 | +0.035 | STANDARD |
| Sam Reinhart: 1+ points | 0.519 | 0.585 | 60/43 | +0.034 | STANDARD |

**BUF @ DAL** · priced 171/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 25.87, exp saves 22.59 (sd 6.2), pull risk 0.053
- BUF net: Alex Lyon (PROBABLE) exp shots 26.69, exp saves 22.97 (sd 6.28), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.227 | 0.325 | 34/69 | +0.068 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.435 | 0.525 | 54/49 | +0.058 | STANDARD |
| Mikko Rantanen: 2+ assists | 0.113 | 0.175 | 22/87 | +0.009 | STANDARD |
| Arttu Hyry: 1+ goals | 0.196 | 0.140 | 15/87 | +0.037 | STANDARD |
| Thomas Harley: 1+ assists | 0.506 | 0.450 | 47/57 | +0.018 | STANDARD |
| Noah Ostlund: 1+ points | 0.412 | 0.465 | 48/55 | +0.021 | STANDARD |

**SJS @ UTA** · priced 150/155 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 26.08, exp saves 22.89 (sd 6.27), pull risk 0.05
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.55, exp saves 25.18 (sd 6.92), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.399 | 0.500 | 52/52 | +0.063 | STANDARD |
| Vincent Trocheck: 1+ points | 0.504 | 0.605 | 63/42 | +0.059 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.245 | 0.345 | 36/67 | +0.069 | STANDARD |
| Alexander Wennberg: 1+ assists | 0.219 | 0.315 | 34/71 | +0.057 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.335 | 0.425 | 44/59 | +0.058 | STANDARD |
| Alexander Wennberg: 1+ points | 0.335 | 0.425 | 45/60 | +0.048 | STANDARD |

**NYI @ ANA** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.3, exp saves 22.87 (sd 6.32), pull risk 0.064
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.92, exp saves 24.55 (sd 6.98), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Troy Terry: 1+ assists | 0.161 | 0.350 | 37/67 | +0.154 | STANDARD |
| Tristan Luneau: 1+ points | 0.405 | 0.320 | 35/71 | +0.039 | STANDARD |
| Judd Caulfield: 1+ points | 0.403 | 0.320 | 33/69 | +0.057 | STANDARD |
| Tristan Luneau: 1+ assists | 0.340 | 0.260 | 28/76 | +0.046 | STANDARD |
| Matias Maccelli: 1+ assists | 0.216 | 0.295 | 31/72 | +0.050 | STANDARD |
| Emil Heineman: 1+ points | 0.449 | 0.370 | 39/65 | +0.042 | STANDARD |

**CGY @ LAK** · priced 160/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.67, exp saves 23.41 (sd 6.34), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 29.98, exp saves 25.68 (sd 6.96), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Fiala: 1+ assists | 0.181 | 0.405 | 42/61 | +0.192 | STANDARD |
| Kevin Fiala: 1+ points | 0.393 | 0.570 | 59/45 | +0.139 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.187 | 0.330 | 34/68 | +0.118 | STANDARD |
| Artemi Panarin: 2+ points | 0.228 | 0.330 | 34/68 | +0.077 | STANDARD |
| Alex Laferriere: 2+ points | 0.203 | 0.115 | 19/96 | +0.002 | STANDARD |
| Mats Zuccarello: 1+ points | 0.340 | 0.425 | 45/60 | +0.044 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
