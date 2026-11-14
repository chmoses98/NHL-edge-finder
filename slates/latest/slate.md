# NHL slate 2026-11-14 — RESEARCH_ONLY

generated 2026-11-14T16:35:01Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4633 · contracts joined: 2977 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 2627, 'OK': 190, 'NO_EDGE': 160}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 379, 'game_early_goal': 14, 'first_goal': 500, 'game_winner': 28, 'player_goals': 858, 'game_overtime': 14, 'player_points': 519, 'goalie_saves': 7, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CAR | 2026-11-14T18:00:00Z | T-60m | 0.692 | 0.308 | 0.155 | 6.47 | 3.87 | 2.60 | 218 (25/193) | PROBABLE/PROBABLE |
| WPG @ CHI | 2026-11-14T20:30:00Z | T-3h | 0.455 | 0.545 | 0.180 | 5.98 | 2.85 | 3.12 | 215 (25/190) | PROJECTED/PROJECTED |
| MIN @ BOS | 2026-11-15T00:00:00Z | T-6h | 0.541 | 0.459 | 0.179 | 5.95 | 3.11 | 2.84 | 211 (25/186) | CONFIRMED/PROJECTED |
| EDM @ TOR | 2026-11-15T00:00:00Z | T-6h | 0.414 | 0.586 | 0.164 | 6.88 | 3.15 | 3.73 | 226 (25/201) | CONFIRMED/PROJECTED |
| COL @ MTL | 2026-11-15T00:00:00Z | T-6h | 0.460 | 0.540 | 0.169 | 6.54 | 3.14 | 3.40 | 196 (25/171) | CONFIRMED/PROJECTED |
| DET @ TBL | 2026-11-15T00:00:00Z | T-6h | 0.661 | 0.339 | 0.167 | 6.08 | 3.55 | 2.53 | 192 (25/167) | PROBABLE/PROBABLE |
| OTT @ PIT | 2026-11-15T00:00:00Z | T-6h | 0.500 | 0.500 | 0.175 | 6.60 | 3.30 | 3.30 | 221 (25/196) | CONFIRMED/CONFIRMED |
| NJD @ WSH | 2026-11-15T00:00:00Z | T-6h | 0.450 | 0.550 | 0.171 | 6.56 | 3.11 | 3.45 | 228 (25/203) | CONFIRMED/CONFIRMED |
| PHI @ CBJ | 2026-11-15T00:00:00Z | T-6h | 0.584 | 0.416 | 0.183 | 5.62 | 3.06 | 2.56 | 201 (25/176) | CONFIRMED/PROJECTED |
| FLA @ STL | 2026-11-15T00:00:00Z | T-6h | 0.482 | 0.518 | 0.165 | 6.70 | 3.30 | 3.40 | 214 (25/189) | PROJECTED/PROJECTED |
| BUF @ DAL | 2026-11-15T01:00:00Z | T-6h | 0.547 | 0.453 | 0.184 | 5.93 | 3.11 | 2.82 | 214 (25/189) | PROJECTED/PROJECTED |
| SJS @ UTA | 2026-11-15T02:00:00Z | T-6h | 0.670 | 0.330 | 0.157 | 6.43 | 3.76 | 2.67 | 206 (25/181) | PROJECTED/PROJECTED |
| NYI @ ANA | 2026-11-15T03:00:00Z | T-6h | 0.554 | 0.446 | 0.170 | 6.54 | 3.45 | 3.10 | 225 (25/200) | PROJECTED/PROJECTED |
| CGY @ LAK | 2026-11-15T03:00:00Z | T-6h | 0.562 | 0.438 | 0.184 | 5.53 | 2.95 | 2.58 | 210 (25/185) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV14SEACAR-CAR3 | game_spread | 0.329 | 0.455 | 0.429 | 46 | 55 | no | +0.104 | OK |
| KXNHLSPREAD-26NOV14SEACAR-CAR2 | game_spread | 0.474 | 0.585 | 0.563 | 59 | 42 | no | +0.089 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA4 | team_total | 0.354 | 0.465 | 0.442 | 47 | 54 | no | +0.089 | OK |
| KXNHLTOTAL-26NOV14FLASTL-8 | game_total | 0.331 | 0.230 | 0.248 | 24 | 78 | yes | +0.079 | OK |
| KXNHLTOTAL-26NOV14FLASTL-9 | game_total | 0.243 | 0.155 | 0.170 | 16 | 85 | yes | +0.073 | OK |
| KXNHLGAME-26NOV14SEACAR-CAR | game_winner | 0.692 | 0.775 | 0.760 | 78 | 23 | no | +0.066 | OK |
| KXNHLGAME-26NOV14SEACAR-SEA | game_winner | 0.308 | 0.225 | 0.240 | 23 | 78 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG4 | team_total | 0.389 | 0.475 | 0.457 | 48 | 53 | no | +0.064 | OK |
| KXNHLGAME-26NOV14COLMTL-MTL | game_winner | 0.460 | 0.545 | 0.528 | 55 | 46 | no | +0.063 | OK |
| KXNHLTOTAL-26NOV14FLASTL-7 | game_total | 0.529 | 0.440 | 0.458 | 45 | 57 | yes | +0.062 | OK |
| KXNHLTOTAL-26NOV14FLASTL-6 | game_total | 0.636 | 0.555 | 0.572 | 56 | 45 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA3 | team_total | 0.576 | 0.660 | 0.644 | 67 | 35 | no | +0.058 | OK |
| KXNHLTOTAL-26NOV14CGYLA-5 | game_total | 0.680 | 0.760 | 0.745 | 77 | 25 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3 | team_total | 0.483 | 0.400 | 0.416 | 41 | 61 | yes | +0.056 | OK |
| KXNHLTOTAL-26NOV14CGYLA-7 | game_total | 0.338 | 0.415 | 0.399 | 42 | 59 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4 | team_total | 0.276 | 0.200 | 0.214 | 21 | 81 | yes | +0.055 | OK |
| KXNHLTOTAL-26NOV14CGYLA-6 | game_total | 0.448 | 0.525 | 0.510 | 53 | 48 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA3 | game_spread | 0.193 | 0.265 | 0.249 | 27 | 74 | no | +0.054 | OK |
| KXNHLGAME-26NOV14COLMTL-COL | game_winner | 0.540 | 0.465 | 0.480 | 47 | 54 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA2 | team_total | 0.794 | 0.855 | 0.844 | 86 | 15 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR4 | team_total | 0.558 | 0.625 | 0.612 | 63 | 38 | no | +0.046 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-7 | game_total | 0.408 | 0.475 | 0.461 | 48 | 53 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG3 | team_total | 0.610 | 0.680 | 0.667 | 69 | 33 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA2 | team_total | 0.719 | 0.650 | 0.665 | 66 | 36 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV14COLMTL-COL2 | game_spread | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN4 | team_total | 0.330 | 0.395 | 0.382 | 40 | 61 | no | +0.043 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-6 | game_total | 0.520 | 0.585 | 0.572 | 59 | 42 | no | +0.043 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-5 | game_total | 0.694 | 0.755 | 0.744 | 76 | 25 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-6 | game_total | 0.460 | 0.525 | 0.512 | 53 | 48 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA5 | team_total | 0.176 | 0.245 | 0.230 | 26 | 77 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-7 | game_total | 0.351 | 0.415 | 0.402 | 42 | 59 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV14FLASTL-10 | game_total | 0.127 | 0.070 | 0.079 | 8 | 94 | yes | +0.041 | OK |
| KXNHLGAME-26NOV14CGYLA-CGY | game_winner | 0.438 | 0.375 | 0.387 | 38 | 63 | yes | +0.041 | OK |
| KXNHLGAME-26NOV14CGYLA-LA | game_winner | 0.562 | 0.625 | 0.613 | 63 | 38 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR5 | team_total | 0.352 | 0.415 | 0.402 | 42 | 59 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL4 | team_total | 0.457 | 0.390 | 0.403 | 40 | 62 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI4 | team_total | 0.265 | 0.330 | 0.316 | 34 | 68 | no | +0.040 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-6 | game_total | 0.513 | 0.575 | 0.563 | 58 | 43 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV14WPGCHI-WPG2 | game_spread | 0.315 | 0.375 | 0.363 | 38 | 63 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA2 | game_spread | 0.325 | 0.385 | 0.373 | 39 | 62 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV14CGYLA-4 | game_total | 0.782 | 0.840 | 0.829 | 85 | 17 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA5 | team_total | 0.134 | 0.085 | 0.093 | 9 | 92 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN3 | team_total | 0.545 | 0.610 | 0.597 | 62 | 40 | no | +0.038 | OK |
| KXNHLSPREAD-26NOV14COLMTL-MTL2 | game_spread | 0.258 | 0.315 | 0.303 | 32 | 69 | no | +0.037 | OK |
| KXNHLSPREAD-26NOV14MINBOS-BOS2 | game_spread | 0.320 | 0.265 | 0.276 | 27 | 74 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG5 | team_total | 0.210 | 0.270 | 0.257 | 28 | 74 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL6 | team_total | 0.121 | 0.070 | 0.078 | 8 | 94 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI3 | team_total | 0.477 | 0.535 | 0.523 | 54 | 47 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV14WPGCHI-WPG3 | game_spread | 0.192 | 0.250 | 0.237 | 26 | 76 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV14CGYLA-8 | game_total | 0.173 | 0.225 | 0.214 | 23 | 78 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL5 | team_total | 0.246 | 0.185 | 0.196 | 20 | 83 | yes | +0.035 | OK |
| KXNHLSPREAD-26NOV14COLMTL-MTL3 | game_spread | 0.154 | 0.205 | 0.194 | 21 | 80 | no | +0.035 | OK |
| KXNHLGAME-26NOV14MINBOS-BOS | game_winner | 0.541 | 0.485 | 0.496 | 49 | 52 | yes | +0.034 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-5 | game_total | 0.735 | 0.790 | 0.780 | 80 | 22 | no | +0.033 | OK |
| KXNHLGAME-26NOV14OTTPIT-OTT | game_winner | 0.500 | 0.555 | 0.544 | 56 | 45 | no | +0.033 | OK |
| KXNHLGAME-26NOV14OTTPIT-PIT | game_winner | 0.500 | 0.445 | 0.456 | 45 | 56 | yes | +0.033 | OK |
| KXNHLTOTAL-26NOV14FLASTL-5 | game_total | 0.824 | 0.775 | 0.786 | 78 | 23 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL3 | team_total | 0.668 | 0.615 | 0.626 | 62 | 39 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA6 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL3 | team_total | 0.638 | 0.585 | 0.596 | 59 | 42 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL4 | team_total | 0.427 | 0.370 | 0.381 | 38 | 64 | yes | +0.031 | OK |
| KXNHLSPREAD-26NOV14MINBOS-MIN2 | game_spread | 0.245 | 0.300 | 0.288 | 31 | 71 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV14OTTPIT-8 | game_total | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV14MINBOS-MIN3 | game_spread | 0.140 | 0.190 | 0.179 | 20 | 82 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN2 | team_total | 0.770 | 0.820 | 0.811 | 83 | 19 | no | +0.029 | OK |
| KXNHLGAME-26NOV14WPGCHI-WPG | game_winner | 0.545 | 0.595 | 0.585 | 60 | 41 | no | +0.028 | OK |
| KXNHLGAME-26NOV14WPGCHI-CHI | game_winner | 0.455 | 0.405 | 0.415 | 41 | 60 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV14SEACAR-SEA2 | game_spread | 0.145 | 0.105 | 0.112 | 11 | 90 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG2 | team_total | 0.814 | 0.860 | 0.852 | 87 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-7 | game_total | 0.405 | 0.460 | 0.449 | 47 | 55 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA4 | team_total | 0.454 | 0.405 | 0.415 | 41 | 60 | yes | +0.027 | OK |
| KXNHLGAME-26NOV14NYIANA-ANA | game_winner | 0.554 | 0.505 | 0.515 | 51 | 50 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL5 | team_total | 0.258 | 0.205 | 0.215 | 22 | 81 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV14CGYLA-9 | game_total | 0.115 | 0.160 | 0.150 | 17 | 85 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14OTTPIT-PIT3 | team_total | 0.643 | 0.590 | 0.601 | 60 | 42 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-4 | game_total | 0.794 | 0.835 | 0.827 | 84 | 17 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV14NJWSH-9 | game_total | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR3 | team_total | 0.753 | 0.805 | 0.795 | 82 | 21 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14NYIANA-NYI2 | team_total | 0.805 | 0.850 | 0.842 | 86 | 16 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-4 | game_total | 0.826 | 0.865 | 0.858 | 87 | 14 | no | +0.025 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CAR | 0.692 | 0.578 | 0.155 | 0.209 | 6.47 | 6.66 | 1.000/1.001 | KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3 +0.115 |
| WPG @ CHI | 0.455 | 0.472 | 0.180 | 0.221 | 5.98 | 6.25 | 0.990/1.001 | KXNHLTOTAL-26NOV14WPGCHI-7 +0.053 |
| MIN @ BOS | 0.541 | 0.549 | 0.179 | 0.211 | 5.95 | 6.46 | 0.955/0.995 | KXNHLTOTAL-26NOV14MINBOS-7 +0.089 |
| EDM @ TOR | 0.414 | 0.442 | 0.164 | 0.210 | 6.88 | 6.82 | 0.955/0.994 | KXNHLSPREAD-26NOV14EDMTOR-EDM2 -0.031 |
| COL @ MTL | 0.460 | 0.468 | 0.169 | 0.218 | 6.54 | 6.63 | 0.942/0.976 | KXNHLTEAMTOTAL-26NOV14COLMTL-MTL4 +0.022 |
| DET @ TBL | 0.661 | 0.654 | 0.167 | 0.205 | 6.08 | 6.33 | 0.951/1.019 | KXNHLTOTAL-26NOV14DETTB-7 +0.043 |
| OTT @ PIT | 0.500 | 0.485 | 0.175 | 0.217 | 6.60 | 6.32 | 1.012/0.968 | KXNHLTOTAL-26NOV14OTTPIT-6 -0.047 |
| NJD @ WSH | 0.450 | 0.490 | 0.171 | 0.216 | 6.56 | 6.41 | 1.015/0.949 | KXNHLSPREAD-26NOV14NJWSH-NJ2 -0.047 |
| PHI @ CBJ | 0.584 | 0.551 | 0.183 | 0.226 | 5.62 | 5.68 | 0.946/0.991 | KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI3 +0.034 |
| FLA @ STL | 0.482 | 0.551 | 0.165 | 0.221 | 6.70 | 6.39 | 1.016/1.008 | KXNHLTEAMTOTAL-26NOV14FLASTL-FLA4 -0.082 |
| BUF @ DAL | 0.547 | 0.555 | 0.184 | 0.219 | 5.93 | 6.16 | 0.986/0.988 | KXNHLTOTAL-26NOV14BUFDAL-5 +0.040 |
| SJS @ UTA | 0.670 | 0.611 | 0.157 | 0.212 | 6.43 | 6.37 | 0.992/1.034 | KXNHLSPREAD-26NOV14SJUTA-UTA2 -0.060 |
| NYI @ ANA | 0.554 | 0.575 | 0.170 | 0.208 | 6.54 | 6.83 | 1.030/0.956 | KXNHLTOTAL-26NOV14NYIANA-7 +0.046 |
| CGY @ LAK | 0.562 | 0.591 | 0.184 | 0.221 | 5.53 | 5.99 | 0.989/0.986 | KXNHLTOTAL-26NOV14CGYLA-7 +0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 50 recommended · full analysis in card.md / packet.json `thesis_card`

- Carolina wins by over 1.5 goals NO @ 42c · p 0.6393 (adj 0.4935) · $3.99 · thesis SEA:WINS
- Carolina wins by over 2.5 goals NO @ 55c · p 0.7589 (adj 0.6199) · $5.88 · thesis SEA:WINS
- Nikolaj Ehlers: 1+ goals NO @ 71c · p 0.7786 (adj 0.7602) · $6.14 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2631 (adj 0.2486) · $2.96 · thesis CHI:OFFENSE_4PLUS
- Mario Ferraro: 1+ goals YES @ 5c · p 0.0739 (adj 0.0667) · $1.05 · thesis WPG:WINS_BY_2PLUS
- Patrick Kane: 1+ assists NO @ 60c · p 0.7333 (adj 0.6402) · $6.58 · thesis CHI:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 12c · p 0.1502 (adj 0.1414) · $1.43 · thesis CHI:OFFENSE_4PLUS
- Danila Yurov: 1+ goals YES @ 16c · p 0.2171 (adj 0.2016) · $2.96 · thesis MIN:OFFENSE_4PLUS
- William Borgen: 1+ goals YES @ 5c · p 0.0835 (adj 0.0714) · $1.3 · thesis BOS:WINS_BY_2PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1401 (adj 0.1288) · $1.89 · thesis MIN:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 9c · p 0.1225 (adj 0.1131) · $1.43 · thesis BOS:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1657 (adj 0.1493) · $2.71 · thesis TOR:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 10c · p 0.1426 (adj 0.1295) · $2.01 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 31c · p 0.4033 (adj 0.3542) · $3.55 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 27c · p 0.3469 (adj 0.3059) · $2.67 · thesis EDM:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 32c · p 0.3864 (adj 0.3686) · $3.98 · thesis COL:OFFENSE_4PLUS
- Martin Necas: 1+ goals YES @ 32c · p 0.3852 (adj 0.3676) · $3.92 · thesis COL:OFFENSE_4PLUS
- Logan O'Connor: 1+ goals YES @ 9c · p 0.1202 (adj 0.1101) · $1.19 · thesis COL:OFFENSE_4PLUS
- Oliver Kapanen: 1+ goals YES @ 15c · p 0.1829 (adj 0.1734) · $1.37 · thesis MTL:OFFENSE_4PLUS
- Conor Geekie: 1+ goals NO @ 82c · p 0.8728 (adj 0.8583) · $5.81 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals YES @ 38c · p 0.4445 (adj 0.4271) · $4.76 · thesis TBL:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 37c · p 0.4632 (adj 0.4141) · $4.06 · thesis TBL:SUPPRESSED
- Alex DeBrincat: 1+ goals YES @ 31c · p 0.3462 (adj 0.3359) · $1.24 · thesis DET:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 18c · p 0.2237 (adj 0.2103) · $1.98 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1521 (adj 0.1416) · $1.25 · thesis PIT:OFFENSE_4PLUS
- Justin Brazeau: 1+ goals YES @ 13c · p 0.1598 (adj 0.1511) · $1.2 · thesis PIT:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 10c · p 0.1512 (adj 0.1321) · $2.06 · thesis NJD:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 19c · p 0.2302 (adj 0.2189) · $1.8 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 15c · p 0.1884 (adj 0.1738) · $1.3 · thesis WSH:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 15c · p 0.1991 (adj 0.1843) · $2.28 · thesis PHI:OFFENSE_4PLUS
- Kent Johnson: 1+ goals NO @ 72c · p 0.7705 (adj 0.7566) · $6.58 · thesis CBJ:SUPPRESSED
- Matvei Michkov: 1+ goals NO @ 73c · p 0.7754 (adj 0.7628) · $6.33 · thesis PHI:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2045 (adj 0.1934) · $1.26 · thesis CBJ:WINS_BY_2PLUS
- Pius Suter: 1+ goals YES @ 12c · p 0.1692 (adj 0.1532) · $2.16 · thesis STL:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 25c · p 0.2939 (adj 0.2817) · $1.95 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3448 (adj 0.3311) · $1.9 · thesis STL:OFFENSE_4PLUS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.1986 (adj 0.1852) · $2.42 · thesis DAL:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 13c · p 0.1642 (adj 0.1544) · $1.51 · thesis BUF:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 28c · p 0.3184 (adj 0.3075) · $1.54 · thesis DAL:OFFENSE_4PLUS
- Daniil But: 1+ goals NO @ 79c · p 0.8558 (adj 0.8381) · $6.58 · thesis UTA:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 67c · p 0.7511 (adj 0.703) · $5.01 · thesis SJS:SUPPRESSED
- Clayton Keller: 1+ assists NO @ 40c · p 0.4722 (adj 0.4311) · $1.82 · thesis UTA:SUPPRESSED
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0984 (adj 0.0876) · $1.85 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1491 (adj 0.1331) · $2.29 · thesis ANA:OFFENSE_4PLUS
- Troy Terry: 1+ assists NO @ 67c · p 0.8391 (adj 0.7162) · $6.58 · thesis ANA:SUPPRESSED
- Sam Colangelo: 1+ goals YES @ 12c · p 0.156 (adj 0.1445) · $1.58 · thesis ANA:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0776 (adj 0.0682) · $1.49 · thesis LAK:WINS_BY_2PLUS
- Kevin Fiala: 1+ assists NO @ 61c · p 0.8191 (adj 0.6767) · $3.76 · thesis LAK:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 68c · p 0.8134 (adj 0.7202) · $3.76 · thesis LAK:SUPPRESSED
- Artemi Panarin: 1+ goals NO @ 65c · p 0.7014 (adj 0.6861) · $2.35 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ CAR** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.35, exp saves 19.42 (sd 5.66), pull risk 0.062
- SEA net: Joey Daccord (PROBABLE) exp shots 32.91, exp saves 28.19 (sd 7.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.184 | 0.395 | 41/62 | +0.180 | STANDARD |
| Sebastian Aho: 1+ points | 0.541 | 0.725 | 74/29 | +0.154 | STANDARD |
| Sebastian Aho: 1+ assists | 0.358 | 0.530 | 54/48 | +0.144 | STANDARD |
| Sebastian Aho: 1+ goals | 0.280 | 0.425 | 43/58 | +0.123 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.370 | 0.500 | 51/51 | +0.102 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.441 | 0.570 | 58/44 | +0.102 | STANDARD |

**WPG @ CHI** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.2, exp saves 24.26 (sd 6.68), pull risk 0.063
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.42, exp saves 22.0 (sd 6.15), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.267 | 0.410 | 42/60 | +0.117 | STANDARD |
| Josh Morrissey: 1+ points | 0.404 | 0.545 | 56/47 | +0.108 | STANDARD |
| Josh Morrissey: 1+ assists | 0.325 | 0.460 | 47/55 | +0.108 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.535 | 55/48 | +0.071 | STANDARD |
| Josh Morrissey: 2+ points | 0.093 | 0.190 | 20/82 | +0.077 | STANDARD |
| Kyle Connor: 2+ points | 0.278 | 0.370 | 38/64 | +0.066 | STANDARD |

**MIN @ BOS** · priced 149/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.01, exp saves 25.22 (sd 6.92), pull risk 0.061
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.53, exp saves 23.63 (sd 6.63), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 1+ assists | 0.395 | 0.500 | 51/51 | +0.078 | STANDARD |
| Matt Boldy: 1+ assists | 0.368 | 0.460 | 47/55 | +0.065 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.273 | 0.355 | 37/66 | +0.052 | STANDARD |
| Blake Coleman: 1+ points | 0.436 | 0.355 | 37/66 | +0.050 | STANDARD |
| Blake Coleman: 1+ assists | 0.255 | 0.185 | 19/82 | +0.054 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.634 | 0.700 | 71/31 | +0.041 | STANDARD |

**EDM @ TOR** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 29.92, exp saves 25.62 (sd 7.2), pull risk 0.087
- EDM net: Devon Levi (PROJECTED) exp shots 27.37, exp saves 23.77 (sd 6.56), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.429 | 0.555 | 56/45 | +0.104 | STANDARD |
| Connor McDavid: 2+ assists | 0.222 | 0.345 | 35/66 | +0.102 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.471 | 0.590 | 60/42 | +0.092 | STANDARD |
| Leon Draisaitl: 2+ points | 0.345 | 0.455 | 46/55 | +0.088 | STANDARD |
| Connor McDavid: 1+ assists | 0.597 | 0.695 | 70/31 | +0.078 | STANDARD |
| John Tavares: 1+ assists | 0.274 | 0.370 | 38/64 | +0.070 | STANDARD |

**COL @ MTL** · priced 139/145 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.75, exp saves 26.34 (sd 7.2), pull risk 0.076
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.08, exp saves 22.5 (sd 6.33), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.393 | 0.500 | 51/51 | +0.079 | STANDARD |
| Gabriel Landeskog: 1+ points | 0.490 | 0.390 | 42/64 | +0.053 | STANDARD |
| Brock Nelson: 1+ points | 0.514 | 0.435 | 46/59 | +0.036 | STANDARD |
| Gabriel Landeskog: 2+ points | 0.143 | 0.065 | 11/98 | +0.027 | STANDARD |
| Artturi Lehkonen: 1+ points | 0.589 | 0.515 | 52/49 | +0.051 | STANDARD |
| Nick Suzuki: 2+ points | 0.217 | 0.290 | 32/74 | +0.029 | STANDARD |

**DET @ TBL** · priced 133/141 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.0, exp saves 22.96 (sd 6.3), pull risk 0.044
- DET net: Daniil Tarasov (PROBABLE) exp shots 28.29, exp saves 23.89 (sd 6.79), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.537 | 0.635 | 64/37 | +0.077 | STANDARD |
| Nikita Kucherov: 2+ points | 0.378 | 0.465 | 47/54 | +0.064 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.188 | 0.270 | 29/75 | +0.049 | STANDARD |
| Charle-Edouard D'Astous: 1+ assists | 0.468 | 0.390 | 40/62 | +0.051 | STANDARD |
| Jake Guentzel: 1+ goals | 0.445 | 0.375 | 38/63 | +0.048 | STANDARD |
| Charle-Edouard D'Astous: 1+ points | 0.529 | 0.470 | 48/54 | +0.031 | STANDARD |

**OTT @ PIT** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.72, exp saves 23.01 (sd 6.47), pull risk 0.068
- OTT net: Linus Ullmark (CONFIRMED) exp shots 26.84, exp saves 23.29 (sd 6.46), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.374 | 0.450 | 46/56 | +0.049 | STANDARD |
| Tim Stutzle: 1+ assists | 0.434 | 0.510 | 53/51 | +0.038 | STANDARD |
| Jordan Spence: 1+ points | 0.353 | 0.280 | 29/73 | +0.049 | STANDARD |
| Jake Sanderson: 1+ points | 0.453 | 0.525 | 54/49 | +0.039 | STANDARD |
| Sidney Crosby: 1+ assists | 0.364 | 0.435 | 45/58 | +0.038 | STANDARD |
| Ben Kindel: 1+ points | 0.419 | 0.485 | 50/53 | +0.034 | STANDARD |

**NJD @ WSH** · priced 169/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 29.47, exp saves 25.55 (sd 6.83), pull risk 0.064
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.15, exp saves 22.66 (sd 6.38), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.244 | 0.140 | 16/88 | +0.075 | STANDARD |
| Aliaksei Protas: 1+ points | 0.466 | 0.370 | 38/64 | +0.069 | STANDARD |
| Ryan Leonard: 1+ assists | 0.321 | 0.230 | 24/78 | +0.068 | STANDARD |
| Cody Glass: 1+ goals | 0.151 | 0.075 | 10/95 | +0.045 | STANDARD |
| Ryan Leonard: 1+ points | 0.469 | 0.395 | 40/61 | +0.052 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.313 | 0.385 | 39/62 | +0.051 | STANDARD |

**PHI @ CBJ** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 25.08, exp saves 21.9 (sd 5.92), pull risk 0.043
- PHI net: Joseph Woll (PROJECTED) exp shots 27.6, exp saves 23.89 (sd 6.58), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.253 | 0.345 | 36/67 | +0.062 | STANDARD |
| Travis Konecny: 1+ points | 0.396 | 0.485 | 49/52 | +0.066 | STANDARD |
| Kent Johnson: 1+ points | 0.473 | 0.560 | 57/45 | +0.060 | STANDARD |
| Porter Martone: 1+ points | 0.351 | 0.430 | 44/58 | +0.052 | STANDARD |
| Matthew Knies: 1+ points | 0.455 | 0.530 | 54/48 | +0.047 | STANDARD |
| Trevor Zegras: 1+ points | 0.451 | 0.525 | 54/49 | +0.042 | STANDARD |

**FLA @ STL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (PROJECTED) exp shots 27.91, exp saves 24.27 (sd 6.59), pull risk 0.058
- FLA net: Jacob Markstrom (PROJECTED) exp shots 26.59, exp saves 22.89 (sd 6.46), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Tkachuk: 1+ assists | 0.442 | 0.510 | 52/50 | +0.041 | STANDARD |
| Brady Tkachuk: 2+ points | 0.167 | 0.235 | 24/77 | +0.051 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.229 | 0.295 | 30/71 | +0.046 | STANDARD |
| Pius Suter: 1+ goals | 0.169 | 0.105 | 12/91 | +0.042 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.604 | 0.545 | 55/46 | +0.037 | STANDARD |
| Brady Tkachuk: 1+ points | 0.526 | 0.585 | 60/43 | +0.027 | STANDARD |

**BUF @ DAL** · priced 158/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.87, exp saves 22.64 (sd 6.23), pull risk 0.052
- BUF net: Alex Lyon (PROJECTED) exp shots 26.69, exp saves 22.94 (sd 6.39), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.229 | 0.325 | 34/69 | +0.066 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.443 | 0.530 | 54/48 | +0.059 | STANDARD |
| Mikko Rantanen: 2+ assists | 0.110 | 0.180 | 20/84 | +0.041 | STANDARD |
| Noah Ostlund: 1+ points | 0.409 | 0.470 | 48/54 | +0.034 | STANDARD |
| Mikko Rantanen: 1+ points | 0.601 | 0.660 | 70/38 | +0.002 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.489 | 0.545 | 56/47 | +0.023 | STANDARD |

**SJS @ UTA** · priced 150/155 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.08, exp saves 22.87 (sd 6.2), pull risk 0.05
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.55, exp saves 25.17 (sd 6.95), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 2+ points | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Ivar Stenberg: 1+ points | 0.400 | 0.510 | 52/50 | +0.083 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.333 | 0.440 | 46/58 | +0.070 | STANDARD |
| Alexander Wennberg: 1+ assists | 0.214 | 0.315 | 34/71 | +0.062 | STANDARD |
| Vincent Trocheck: 1+ points | 0.500 | 0.600 | 62/42 | +0.063 | STANDARD |
| Macklin Celebrini: 2+ points | 0.256 | 0.355 | 36/65 | +0.078 | STANDARD |

**NYI @ ANA** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.3, exp saves 22.87 (sd 6.32), pull risk 0.064
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.92, exp saves 24.55 (sd 6.98), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Troy Terry: 1+ assists | 0.161 | 0.350 | 37/67 | +0.154 | STANDARD |
| Tristan Luneau: 1+ points | 0.405 | 0.315 | 35/72 | +0.039 | STANDARD |
| Judd Caulfield: 1+ points | 0.403 | 0.315 | 33/70 | +0.057 | STANDARD |
| Tristan Luneau: 1+ assists | 0.340 | 0.260 | 28/76 | +0.046 | STANDARD |
| Matias Maccelli: 1+ assists | 0.216 | 0.295 | 31/72 | +0.050 | STANDARD |
| Emil Heineman: 1+ points | 0.449 | 0.370 | 39/65 | +0.042 | STANDARD |

**CGY @ LAK** · priced 156/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.67, exp saves 23.41 (sd 6.34), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 29.98, exp saves 25.68 (sd 6.96), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Fiala: 1+ assists | 0.181 | 0.400 | 41/61 | +0.192 | STANDARD |
| Kevin Fiala: 1+ points | 0.393 | 0.575 | 60/45 | +0.139 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.187 | 0.330 | 34/68 | +0.118 | STANDARD |
| Artemi Panarin: 2+ points | 0.228 | 0.320 | 33/69 | +0.067 | STANDARD |
| Mats Zuccarello: 1+ points | 0.340 | 0.425 | 45/60 | +0.044 | STANDARD |
| Artemi Panarin: 1+ assists | 0.422 | 0.495 | 51/52 | +0.040 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
