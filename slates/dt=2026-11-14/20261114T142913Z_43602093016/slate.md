# NHL slate 2026-11-14 — RESEARCH_ONLY

generated 2026-11-14T14:29:13Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4297 · contracts joined: 2641 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 2291, 'OK': 160, 'NO_EDGE': 190}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 319, 'game_early_goal': 14, 'first_goal': 432, 'game_winner': 28, 'player_goals': 737, 'game_overtime': 14, 'player_points': 439, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CAR | 2026-11-14T18:00:00Z | T-3h | 0.680 | 0.320 | 0.152 | 6.47 | 3.84 | 2.63 | 220 (25/195) | PROJECTED/PROJECTED |
| WPG @ CHI | 2026-11-14T20:30:00Z | T-6h | 0.455 | 0.545 | 0.180 | 5.98 | 2.85 | 3.12 | 217 (25/192) | PROJECTED/PROJECTED |
| MIN @ BOS | 2026-11-15T00:00:00Z | T-6h | 0.523 | 0.477 | 0.179 | 6.06 | 3.11 | 2.95 | 210 (25/185) | PROJECTED/PROJECTED |
| EDM @ TOR | 2026-11-15T00:00:00Z | T-6h | 0.414 | 0.586 | 0.164 | 6.89 | 3.15 | 3.74 | 225 (25/200) | PROJECTED/PROJECTED |
| COL @ MTL | 2026-11-15T00:00:00Z | T-6h | 0.488 | 0.512 | 0.175 | 6.36 | 3.14 | 3.21 | 198 (25/173) | PROJECTED/PROJECTED |
| DET @ TBL | 2026-11-15T00:00:00Z | T-6h | 0.652 | 0.348 | 0.170 | 6.11 | 3.55 | 2.56 | 192 (25/167) | PROJECTED/PROBABLE |
| OTT @ PIT | 2026-11-15T00:00:00Z | T-6h | 0.503 | 0.497 | 0.171 | 6.53 | 3.27 | 3.26 | 214 (25/189) | PROJECTED/PROJECTED |
| NJD @ WSH | 2026-11-15T00:00:00Z | T-6h | 0.505 | 0.495 | 0.172 | 6.19 | 3.11 | 3.08 | 228 (25/203) | PROJECTED/CONFIRMED |
| PHI @ CBJ | 2026-11-15T00:00:00Z | T-6h | 0.539 | 0.461 | 0.181 | 5.86 | 3.05 | 2.81 | 201 (25/176) | PROJECTED/PROJECTED |
| FLA @ STL | 2026-11-15T00:00:00Z | T-6h | 0.482 | 0.518 | 0.165 | 6.70 | 3.30 | 3.40 | 214 (25/189) | PROJECTED/PROJECTED |
| BUF @ DAL | 2026-11-15T01:00:00Z | T-6h | 0.547 | 0.453 | 0.184 | 5.93 | 3.11 | 2.82 | 214 (25/189) | PROJECTED/PROJECTED |
| SJS @ UTA | 2026-11-15T02:00:00Z | T-6h | 0.670 | 0.330 | 0.157 | 6.43 | 3.76 | 2.67 | 206 (25/181) | PROJECTED/PROJECTED |
| NYI @ ANA | 2026-11-15T03:00:00Z | T-12h | 0.554 | 0.446 | 0.170 | 6.54 | 3.45 | 3.10 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ LAK | 2026-11-15T03:00:00Z | T-12h | 0.562 | 0.438 | 0.184 | 5.53 | 2.95 | 2.58 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV14SEACAR-CAR3 | game_spread | 0.321 | 0.455 | 0.427 | 46 | 55 | no | +0.112 | OK |
| KXNHLSPREAD-26NOV14SEACAR-CAR2 | game_spread | 0.465 | 0.595 | 0.570 | 60 | 41 | no | +0.108 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA4 | team_total | 0.354 | 0.455 | 0.434 | 46 | 55 | no | +0.079 | OK |
| KXNHLTOTAL-26NOV14FLASTL-8 | game_total | 0.331 | 0.230 | 0.248 | 24 | 78 | yes | +0.079 | OK |
| KXNHLGAME-26NOV14SEACAR-CAR | game_winner | 0.680 | 0.775 | 0.758 | 78 | 23 | no | +0.077 | OK |
| KXNHLGAME-26NOV14SEACAR-SEA | game_winner | 0.320 | 0.225 | 0.242 | 23 | 78 | yes | +0.077 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3 | team_total | 0.491 | 0.395 | 0.414 | 40 | 61 | yes | +0.074 | OK |
| KXNHLTOTAL-26NOV14FLASTL-9 | game_total | 0.243 | 0.155 | 0.170 | 16 | 85 | yes | +0.073 | OK |
| KXNHLTOTAL-26NOV14CGYLA-6 | game_total | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG4 | team_total | 0.389 | 0.475 | 0.457 | 48 | 53 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV14FLASTL-7 | game_total | 0.529 | 0.440 | 0.458 | 45 | 57 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4 | team_total | 0.283 | 0.200 | 0.215 | 21 | 81 | yes | +0.061 | OK |
| KXNHLTOTAL-26NOV14FLASTL-6 | game_total | 0.636 | 0.555 | 0.572 | 56 | 45 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA3 | team_total | 0.576 | 0.660 | 0.644 | 67 | 35 | no | +0.058 | OK |
| KXNHLTOTAL-26NOV14CGYLA-5 | game_total | 0.680 | 0.760 | 0.745 | 77 | 25 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV14CGYLA-7 | game_total | 0.338 | 0.415 | 0.399 | 42 | 59 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR4 | team_total | 0.551 | 0.625 | 0.610 | 63 | 38 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA2 | team_total | 0.727 | 0.650 | 0.666 | 66 | 36 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA2 | team_total | 0.794 | 0.855 | 0.844 | 86 | 15 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG3 | team_total | 0.610 | 0.680 | 0.667 | 69 | 33 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA3 | game_spread | 0.193 | 0.255 | 0.242 | 26 | 75 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-6 | game_total | 0.520 | 0.585 | 0.572 | 59 | 42 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA5 | team_total | 0.176 | 0.250 | 0.234 | 27 | 77 | no | +0.042 | OK |
| KXNHLGAME-26NOV14CGYLA-CGY | game_winner | 0.438 | 0.375 | 0.387 | 38 | 63 | yes | +0.041 | OK |
| KXNHLGAME-26NOV14CGYLA-LA | game_winner | 0.562 | 0.625 | 0.613 | 63 | 38 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-6 | game_total | 0.513 | 0.580 | 0.567 | 59 | 43 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV14WPGCHI-WPG2 | game_spread | 0.315 | 0.375 | 0.363 | 38 | 63 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA5 | team_total | 0.135 | 0.085 | 0.093 | 9 | 92 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR5 | team_total | 0.345 | 0.410 | 0.397 | 42 | 60 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA2 | game_spread | 0.325 | 0.385 | 0.373 | 39 | 62 | no | +0.039 | OK |
| KXNHLGAME-26NOV14WPGCHI-WPG | game_winner | 0.545 | 0.605 | 0.593 | 61 | 40 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV14CGYLA-4 | game_total | 0.782 | 0.840 | 0.829 | 85 | 17 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL6 | team_total | 0.121 | 0.070 | 0.078 | 8 | 94 | yes | +0.036 | OK |
| KXNHLSPREAD-26NOV14WPGCHI-WPG3 | game_spread | 0.192 | 0.250 | 0.237 | 26 | 76 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV14SEACAR-SEA2 | game_spread | 0.152 | 0.105 | 0.113 | 11 | 90 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV14CGYLA-8 | game_total | 0.173 | 0.230 | 0.218 | 24 | 78 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL5 | team_total | 0.246 | 0.185 | 0.196 | 20 | 83 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-7 | game_total | 0.408 | 0.465 | 0.453 | 47 | 54 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV14FLASTL-5 | game_total | 0.824 | 0.770 | 0.782 | 78 | 24 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA6 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL3 | team_total | 0.638 | 0.585 | 0.596 | 59 | 42 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV14FLASTL-10 | game_total | 0.127 | 0.075 | 0.083 | 9 | 94 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL4 | team_total | 0.427 | 0.375 | 0.385 | 38 | 63 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR3 | team_total | 0.748 | 0.805 | 0.795 | 82 | 21 | no | +0.030 | OK |
| KXNHLGAME-26NOV14WPGCHI-CHI | game_winner | 0.455 | 0.405 | 0.415 | 41 | 60 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG2 | team_total | 0.814 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-7 | game_total | 0.405 | 0.460 | 0.449 | 47 | 55 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV14OTTPIT-PIT2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA4 | team_total | 0.454 | 0.405 | 0.415 | 41 | 60 | yes | +0.027 | OK |
| KXNHLGAME-26NOV14NYIANA-ANA | game_winner | 0.554 | 0.505 | 0.515 | 51 | 50 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG5 | team_total | 0.210 | 0.265 | 0.253 | 28 | 75 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV14SEACAR-SEA3 | game_spread | 0.080 | 0.045 | 0.051 | 5 | 96 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV14CGYLA-9 | game_total | 0.115 | 0.160 | 0.150 | 17 | 85 | no | +0.026 | OK |
| KXNHLGAME-26NOV14OTTPIT-OTT | game_winner | 0.497 | 0.545 | 0.535 | 55 | 46 | no | +0.026 | OK |
| KXNHLGAME-26NOV14OTTPIT-PIT | game_winner | 0.503 | 0.455 | 0.465 | 46 | 55 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV14COLMTL-MTL2 | game_spread | 0.279 | 0.325 | 0.316 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14NYIANA-NYI2 | team_total | 0.805 | 0.850 | 0.842 | 86 | 16 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV14NYIANA-ANA2 | game_spread | 0.340 | 0.295 | 0.304 | 30 | 71 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV14NYIANA-NYI3 | team_total | 0.599 | 0.650 | 0.640 | 66 | 36 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV14BUFDAL-DAL4 | team_total | 0.388 | 0.440 | 0.429 | 45 | 57 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV14WPGCHI-5 | game_total | 0.743 | 0.785 | 0.777 | 79 | 22 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV14MINBOS-MIN2 | game_spread | 0.261 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLGAME-26NOV14COLMTL-COL | game_winner | 0.512 | 0.465 | 0.474 | 47 | 54 | yes | +0.025 | OK |
| KXNHLGAME-26NOV14COLMTL-MTL | game_winner | 0.488 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV14FLASTL-4 | game_total | 0.892 | 0.850 | 0.859 | 86 | 16 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-SEA6 | team_total | 0.056 | 0.020 | 0.025 | 3 | 99 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV14OTTPIT-OTT3 | game_spread | 0.176 | 0.215 | 0.207 | 22 | 79 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA6 | team_total | 0.072 | 0.110 | 0.101 | 12 | 90 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-8 | game_total | 0.225 | 0.270 | 0.261 | 28 | 74 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV14SEACAR-CAR2 | team_total | 0.894 | 0.930 | 0.924 | 94 | 8 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV14MINBOS-MIN3 | game_spread | 0.149 | 0.190 | 0.181 | 20 | 82 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA5 | team_total | 0.262 | 0.220 | 0.228 | 23 | 79 | yes | +0.020 | OK |
| KXNHLSPREAD-26NOV14NYIANA-NYI2 | game_spread | 0.246 | 0.285 | 0.277 | 29 | 72 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV14OTTPIT-PIT3 | team_total | 0.635 | 0.595 | 0.603 | 60 | 41 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA3 | team_total | 0.664 | 0.625 | 0.633 | 63 | 38 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA2 | team_total | 0.848 | 0.815 | 0.822 | 82 | 19 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV14SJUTA-UTA5 | team_total | 0.333 | 0.290 | 0.298 | 30 | 72 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV14OTTPIT-PIT5 | team_total | 0.239 | 0.200 | 0.207 | 21 | 81 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV14CGYLA-CGY2 | game_spread | 0.218 | 0.185 | 0.191 | 19 | 82 | yes | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CAR | 0.680 | 0.581 | 0.152 | 0.203 | 6.47 | 6.65 | 0.997/1.005 | KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3 +0.102 |
| WPG @ CHI | 0.455 | 0.472 | 0.180 | 0.221 | 5.98 | 6.25 | 0.990/1.001 | KXNHLTOTAL-26NOV14WPGCHI-7 +0.053 |
| MIN @ BOS | 0.523 | 0.535 | 0.179 | 0.217 | 6.06 | 6.50 | 0.968/0.995 | KXNHLTOTAL-26NOV14MINBOS-7 +0.075 |
| EDM @ TOR | 0.414 | 0.434 | 0.164 | 0.209 | 6.89 | 6.90 | 0.979/0.994 | KXNHLSPREAD-26NOV14EDMTOR-EDM2 -0.022 |
| COL @ MTL | 0.488 | 0.450 | 0.175 | 0.215 | 6.36 | 6.72 | 0.976/0.976 | KXNHLTEAMTOTAL-26NOV14COLMTL-COL4 +0.074 |
| DET @ TBL | 0.652 | 0.647 | 0.170 | 0.203 | 6.11 | 6.33 | 0.957/1.019 | KXNHLTOTAL-26NOV14DETTB-7 +0.039 |
| OTT @ PIT | 0.503 | 0.491 | 0.171 | 0.218 | 6.53 | 6.44 | 1.021/0.998 | KXNHLTOTAL-26NOV14OTTPIT-8 -0.020 |
| NJD @ WSH | 0.505 | 0.512 | 0.172 | 0.214 | 6.19 | 6.27 | 0.960/0.949 | KXNHLTOTAL-26NOV14NJWSH-7 +0.024 |
| PHI @ CBJ | 0.539 | 0.532 | 0.181 | 0.225 | 5.86 | 5.78 | 0.989/0.991 | KXNHLTOTAL-26NOV14PHICBJ-6 -0.017 |
| FLA @ STL | 0.482 | 0.551 | 0.165 | 0.221 | 6.70 | 6.39 | 1.016/1.008 | KXNHLTEAMTOTAL-26NOV14FLASTL-FLA4 -0.082 |
| BUF @ DAL | 0.547 | 0.555 | 0.184 | 0.219 | 5.93 | 6.16 | 0.986/0.988 | KXNHLTOTAL-26NOV14BUFDAL-5 +0.040 |
| SJS @ UTA | 0.670 | 0.611 | 0.157 | 0.212 | 6.43 | 6.37 | 0.992/1.034 | KXNHLSPREAD-26NOV14SJUTA-UTA2 -0.060 |
| NYI @ ANA | 0.554 | 0.575 | 0.170 | 0.208 | 6.54 | 6.83 | 1.030/0.956 | KXNHLTOTAL-26NOV14NYIANA-7 +0.046 |
| CGY @ LAK | 0.562 | 0.591 | 0.184 | 0.221 | 5.53 | 5.99 | 0.989/0.986 | KXNHLTOTAL-26NOV14CGYLA-7 +0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Berkly Catton: 1+ goals YES @ 14c · p 0.2268 (adj 0.2026) · $6.61 · thesis SEA:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 41c · p 0.6403 (adj 0.4874) · $7.77 · thesis GAME:TIGHT
- Carolina wins by over 2.5 goals NO @ 55c · p 0.7539 (adj 0.6181) · $5.77 · thesis GAME:TIGHT
- Seattle over 2.5 goals scored YES @ 40c · p 0.5984 (adj 0.4662) · $2.81 · thesis SEA:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2631 (adj 0.2486) · $4.46 · thesis CHI:OFFENSE_4PLUS
- Winnipeg wins by over 1.5 goals NO @ 63c · p 0.6968 (adj 0.6609) · $4.35 · thesis CHI:WINS
- Josh Morrissey: 1+ assists NO @ 56c · p 0.6752 (adj 0.5906) · $3.76 · thesis WPG:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 62c · p 0.7333 (adj 0.6467) · $5.92 · thesis CHI:SUPPRESSED
- William Borgen: 1+ goals YES @ 5c · p 0.0882 (adj 0.0749) · $2.39 · thesis BOS:WINS_BY_2PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1459 (adj 0.1332) · $3.87 · thesis MIN:OFFENSE_4PLUS
- Danila Yurov: 1+ goals YES @ 16c · p 0.2064 (adj 0.1935) · $4.03 · thesis MIN:OFFENSE_4PLUS
- Boston wins by over 2.5 goals YES @ 16c · p 0.2119 (adj 0.1835) · $2.05 · thesis BOS:WINS_BY_2PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1611 (adj 0.1408) · $3.23 · thesis TOR:WINS_BY_2PLUS
- Connor McDavid: 2+ assists NO @ 66c · p 0.7732 (adj 0.6964) · $10.91 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 27c · p 0.3495 (adj 0.3023) · $3.7 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 11c · p 0.1455 (adj 0.1291) · $1.76 · thesis EDM:OFFENSE_4PLUS
- Martin Necas: 1+ goals YES @ 31c · p 0.3995 (adj 0.3759) · $7.86 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 32c · p 0.3908 (adj 0.3719) · $5.72 · thesis COL:OFFENSE_4PLUS
- Montreal wins by over 1.5 goals NO @ 68c · p 0.7489 (adj 0.712) · $1.15 · thesis COL:WINS
- Nazem Kadri: 1+ goals YES @ 27c · p 0.3035 (adj 0.2939) · $1.44 · thesis COL:OFFENSE_4PLUS
- Conor Geekie: 1+ goals NO @ 83c · p 0.8799 (adj 0.8649) · $8.99 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 2+ assists NO @ 75c · p 0.8244 (adj 0.7772) · $6.37 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 37c · p 0.4676 (adj 0.3977) · $1.01 · thesis TBL:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1611 (adj 0.1483) · $1.53 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2413 (adj 0.2185) · $4.23 · thesis WSH:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1454 (adj 0.1303) · $1.87 · thesis NJD:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 24c · p 0.3153 (adj 0.2676) · $2.03 · thesis WSH:OFFENSE_4PLUS
- Nico Hischier: 1+ goals NO @ 70c · p 0.7396 (adj 0.7272) · $6.09 · thesis NJD:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2176 (adj 0.2019) · $1.82 · thesis CBJ:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 67c · p 0.7423 (adj 0.6986) · $6.15 · thesis PHI:SUPPRESSED
- Pius Suter: 1+ goals YES @ 13c · p 0.1692 (adj 0.1581) · $2.91 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3448 (adj 0.3323) · $3.18 · thesis STL:OFFENSE_4PLUS
- Sam Bennett: 1+ goals YES @ 25c · p 0.2907 (adj 0.2768) · $2.3 · thesis FLA:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 13c · p 0.1642 (adj 0.1544) · $2.49 · thesis BUF:OFFENSE_4PLUS
- Arttu Hyry: 1+ goals YES @ 16c · p 0.1986 (adj 0.1865) · $2.68 · thesis DAL:OFFENSE_4PLUS
- Clayton Keller: 1+ assists NO @ 40c · p 0.4722 (adj 0.4286) · $2.7 · thesis UTA:SUPPRESSED
- Anaheim wins by over 1.5 goals YES @ 30c · p 0.3698 (adj 0.3324) · $3.33 · thesis ANA:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ CAR** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.36, exp saves 19.41 (sd 5.69), pull risk 0.06
- SEA net: Joey Daccord (PROJECTED) exp shots 32.92, exp saves 28.25 (sd 7.68), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.206 | 0.385 | 40/63 | +0.148 | STANDARD |
| Sebastian Aho: 1+ points | 0.574 | 0.725 | 74/29 | +0.122 | STANDARD |
| Sebastian Aho: 1+ assists | 0.384 | 0.530 | 55/49 | +0.109 | STANDARD |
| Kaapo Kakko: 1+ points | 0.471 | 0.340 | 35/67 | +0.105 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.337 | 0.225 | 24/79 | +0.084 | STANDARD |
| Sebastian Aho: 1+ goals | 0.306 | 0.415 | 42/59 | +0.087 | STANDARD |

**WPG @ CHI** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.21, exp saves 24.29 (sd 6.71), pull risk 0.063
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.43, exp saves 22.04 (sd 6.1), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.267 | 0.400 | 42/62 | +0.097 | STANDARD |
| Josh Morrissey: 1+ points | 0.404 | 0.535 | 54/47 | +0.108 | STANDARD |
| Josh Morrissey: 1+ assists | 0.325 | 0.455 | 47/56 | +0.098 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.525 | 55/50 | +0.051 | STANDARD |
| Kyle Connor: 1+ assists | 0.412 | 0.495 | 51/52 | +0.050 | STANDARD |
| Kyle Connor: 2+ points | 0.278 | 0.355 | 38/67 | +0.037 | STANDARD |

**MIN @ BOS** · priced 148/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.02, exp saves 25.24 (sd 6.84), pull risk 0.059
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.54, exp saves 23.65 (sd 6.63), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matt Boldy: 1+ assists | 0.361 | 0.460 | 48/56 | +0.061 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.397 | 0.490 | 51/53 | +0.056 | STANDARD |
| Blake Coleman: 1+ points | 0.435 | 0.350 | 37/67 | +0.048 | STANDARD |
| Blake Coleman: 1+ assists | 0.255 | 0.175 | 19/84 | +0.054 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.278 | 0.355 | 37/66 | +0.047 | STANDARD |
| Fraser Minten: 1+ assists | 0.280 | 0.210 | 23/81 | +0.037 | STANDARD |

**EDM @ TOR** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 29.93, exp saves 25.59 (sd 7.19), pull risk 0.091
- EDM net: Devon Levi (PROJECTED) exp shots 27.38, exp saves 23.8 (sd 6.59), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.426 | 0.560 | 57/45 | +0.106 | STANDARD |
| Connor McDavid: 1+ assists | 0.588 | 0.710 | 72/30 | +0.098 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.478 | 0.600 | 61/41 | +0.095 | STANDARD |
| Connor McDavid: 2+ assists | 0.227 | 0.345 | 35/66 | +0.097 | STANDARD |
| Leon Draisaitl: 2+ points | 0.344 | 0.455 | 46/55 | +0.088 | STANDARD |
| John Tavares: 1+ assists | 0.269 | 0.370 | 38/64 | +0.075 | STANDARD |

**COL @ MTL** · priced 140/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 30.76, exp saves 26.21 (sd 7.32), pull risk 0.081
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.09, exp saves 22.5 (sd 6.35), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.390 | 0.505 | 52/51 | +0.083 | STANDARD |
| Gabriel Landeskog: 1+ points | 0.505 | 0.390 | 42/64 | +0.068 | STANDARD |
| Martin Necas: 1+ goals | 0.400 | 0.305 | 31/70 | +0.075 | STANDARD |
| Gabriel Landeskog: 2+ points | 0.159 | 0.065 | 11/98 | +0.042 | STANDARD |
| Brock Nelson: 1+ points | 0.521 | 0.435 | 46/59 | +0.044 | STANDARD |
| Artturi Lehkonen: 1+ goals | 0.391 | 0.315 | 32/69 | +0.056 | STANDARD |

**DET @ TBL** · priced 133/141 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.01, exp saves 23.02 (sd 6.23), pull risk 0.044
- DET net: Daniil Tarasov (PROBABLE) exp shots 28.3, exp saves 23.89 (sd 6.7), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.532 | 0.640 | 65/37 | +0.081 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.176 | 0.270 | 29/75 | +0.061 | STANDARD |
| Nikita Kucherov: 2+ points | 0.376 | 0.465 | 47/54 | +0.067 | STANDARD |
| Charle-Edouard D'Astous: 1+ assists | 0.466 | 0.385 | 40/63 | +0.049 | STANDARD |
| Charle-Edouard D'Astous: 2+ assists | 0.125 | 0.060 | 11/99 | +0.008 | STANDARD |
| Conor Geekie: 1+ goals | 0.120 | 0.180 | 19/83 | +0.040 | STANDARD |

**OTT @ PIT** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.73, exp saves 23.08 (sd 6.45), pull risk 0.067
- OTT net: Linus Ullmark (PROJECTED) exp shots 26.85, exp saves 23.25 (sd 6.49), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.432 | 0.515 | 53/50 | +0.050 | STANDARD |
| Jordan Spence: 1+ points | 0.354 | 0.280 | 30/74 | +0.040 | STANDARD |
| Jordan Spence: 1+ assists | 0.295 | 0.225 | 25/80 | +0.032 | STANDARD |
| Jake Sanderson: 1+ assists | 0.380 | 0.450 | 47/57 | +0.033 | STANDARD |
| Ben Kindel: 1+ assists | 0.279 | 0.330 | 35/69 | +0.016 | STANDARD |
| Connor Dewar: 1+ goals | 0.161 | 0.110 | 13/91 | +0.023 | STANDARD |

**NJD @ WSH** · priced 169/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 29.48, exp saves 25.68 (sd 6.82), pull risk 0.055
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.16, exp saves 22.65 (sd 6.42), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.315 | 0.220 | 24/80 | +0.063 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.241 | 0.150 | 18/88 | +0.051 | STANDARD |
| Aliaksei Protas: 1+ points | 0.462 | 0.375 | 38/63 | +0.065 | STANDARD |
| Ryan Leonard: 1+ points | 0.467 | 0.385 | 41/64 | +0.040 | STANDARD |
| Luke Evangelista: 1+ assists | 0.257 | 0.330 | 34/68 | +0.048 | STANDARD |
| Jack Hughes: 1+ assists | 0.423 | 0.490 | 50/52 | +0.040 | STANDARD |

**PHI @ CBJ** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROJECTED) exp shots 25.08, exp saves 21.84 (sd 6.01), pull risk 0.046
- PHI net: Joseph Woll (PROJECTED) exp shots 27.61, exp saves 23.96 (sd 6.53), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ points | 0.400 | 0.490 | 50/52 | +0.063 | STANDARD |
| Travis Konecny: 1+ assists | 0.258 | 0.345 | 36/67 | +0.057 | STANDARD |
| Kent Johnson: 1+ points | 0.486 | 0.565 | 58/45 | +0.046 | STANDARD |
| Trevor Zegras: 1+ points | 0.455 | 0.530 | 54/48 | +0.048 | STANDARD |
| Trevor Zegras: 1+ assists | 0.306 | 0.380 | 40/64 | +0.038 | STANDARD |
| Matthew Knies: 1+ points | 0.462 | 0.525 | 54/49 | +0.030 | STANDARD |

**FLA @ STL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (PROJECTED) exp shots 27.92, exp saves 24.28 (sd 6.63), pull risk 0.062
- FLA net: Jacob Markstrom (PROJECTED) exp shots 26.6, exp saves 22.92 (sd 6.48), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ points | 0.525 | 0.595 | 61/42 | +0.037 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.231 | 0.300 | 31/71 | +0.045 | STANDARD |
| Dylan Holloway: 1+ points | 0.569 | 0.500 | 53/53 | +0.021 | STANDARD |
| Brady Tkachuk: 2+ points | 0.169 | 0.235 | 24/77 | +0.048 | STANDARD |
| Philip Broberg: 1+ assists | 0.440 | 0.375 | 39/64 | +0.034 | STANDARD |
| Jimmy Snuggerud: 2+ points | 0.242 | 0.180 | 22/86 | +0.010 | STANDARD |

**BUF @ DAL** · priced 158/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.88, exp saves 22.64 (sd 6.2), pull risk 0.052
- BUF net: Alex Lyon (PROJECTED) exp shots 26.7, exp saves 22.94 (sd 6.43), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.443 | 0.525 | 54/49 | +0.049 | STANDARD |
| Thomas Harley: 2+ points | 0.199 | 0.130 | 20/94 | -0.012 | STANDARD |
| Mikko Rantanen: 1+ points | 0.601 | 0.670 | 70/36 | +0.023 | STANDARD |
| Thomas Harley: 2+ assists | 0.156 | 0.090 | 14/96 | +0.008 | STANDARD |
| Noah Ostlund: 1+ points | 0.409 | 0.465 | 48/55 | +0.024 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.402 | 0.455 | 47/56 | +0.021 | STANDARD |

**SJS @ UTA** · priced 150/155 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.09, exp saves 22.91 (sd 6.18), pull risk 0.046
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.56, exp saves 25.21 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 2+ points | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Alexander Wennberg: 1+ assists | 0.214 | 0.320 | 35/71 | +0.062 | STANDARD |
| Macklin Celebrini: 2+ points | 0.256 | 0.355 | 36/65 | +0.078 | STANDARD |
| Alexander Wennberg: 1+ points | 0.334 | 0.430 | 46/60 | +0.049 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.333 | 0.425 | 45/60 | +0.050 | STANDARD |
| Clayton Keller: 1+ assists | 0.528 | 0.615 | 63/40 | +0.055 | STANDARD |

**NYI @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.31, exp saves 22.86 (sd 6.43), pull risk 0.067
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.93, exp saves 24.47 (sd 7.0), pull risk 0.095

**CGY @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.68, exp saves 23.43 (sd 6.34), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 29.99, exp saves 25.69 (sd 6.99), pull risk 0.069

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
