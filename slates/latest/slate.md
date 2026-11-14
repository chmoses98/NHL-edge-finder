# NHL slate 2026-11-14 — RESEARCH_ONLY

generated 2026-11-14T18:25:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 13 · markets on board: 4761 · contracts joined: 2873 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 2548, 'OK': 177, 'NO_EDGE': 148}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 388, 'game_early_goal': 13, 'first_goal': 468, 'game_winner': 26, 'player_goals': 805, 'game_overtime': 13, 'player_points': 531, 'goalie_saves': 18, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CHI | 2026-11-14T20:30:00Z | T-90m | 0.455 | 0.545 | 0.180 | 5.98 | 2.85 | 3.12 | 223 (25/198) | PROJECTED/PROJECTED |
| MIN @ BOS | 2026-11-15T00:00:00Z | T-3h | 0.525 | 0.475 | 0.181 | 5.85 | 3.01 | 2.84 | 221 (25/196) | CONFIRMED/CONFIRMED |
| EDM @ TOR | 2026-11-15T00:00:00Z | T-3h | 0.414 | 0.586 | 0.164 | 6.88 | 3.15 | 3.73 | 227 (25/202) | CONFIRMED/PROJECTED |
| COL @ MTL | 2026-11-15T00:00:00Z | T-3h | 0.451 | 0.549 | 0.168 | 6.50 | 3.11 | 3.40 | 214 (25/189) | CONFIRMED/CONFIRMED |
| DET @ TBL | 2026-11-15T00:00:00Z | T-3h | 0.661 | 0.339 | 0.167 | 6.08 | 3.55 | 2.53 | 212 (25/187) | PROBABLE/PROBABLE |
| OTT @ PIT | 2026-11-15T00:00:00Z | T-3h | 0.500 | 0.500 | 0.175 | 6.60 | 3.30 | 3.30 | 229 (25/204) | CONFIRMED/CONFIRMED |
| NJD @ WSH | 2026-11-15T00:00:00Z | T-3h | 0.450 | 0.550 | 0.171 | 6.56 | 3.11 | 3.45 | 232 (25/207) | CONFIRMED/CONFIRMED |
| PHI @ CBJ | 2026-11-15T00:00:00Z | T-3h | 0.585 | 0.415 | 0.185 | 5.64 | 3.07 | 2.57 | 215 (25/190) | CONFIRMED/CONFIRMED |
| FLA @ STL | 2026-11-15T00:00:00Z | T-3h | 0.589 | 0.411 | 0.178 | 6.18 | 3.37 | 2.81 | 221 (25/196) | CONFIRMED/CONFIRMED |
| BUF @ DAL | 2026-11-15T01:00:00Z | T-6h | 0.548 | 0.452 | 0.179 | 5.87 | 3.08 | 2.79 | 231 (25/206) | CONFIRMED/PROBABLE |
| SJS @ UTA | 2026-11-15T02:00:00Z | T-6h | 0.665 | 0.335 | 0.166 | 6.45 | 3.77 | 2.68 | 206 (25/181) | PROBABLE/PROJECTED |
| NYI @ ANA | 2026-11-15T03:00:00Z | T-6h | 0.554 | 0.446 | 0.170 | 6.54 | 3.45 | 3.10 | 228 (25/203) | PROJECTED/PROJECTED |
| CGY @ LAK | 2026-11-15T03:00:00Z | T-6h | 0.562 | 0.438 | 0.184 | 5.53 | 2.95 | 2.58 | 214 (25/189) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV14COLMTL-MTL | game_winner | 0.451 | 0.565 | 0.542 | 57 | 44 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA4 | team_total | 0.354 | 0.465 | 0.442 | 47 | 54 | no | +0.089 | OK |
| KXNHLGAME-26NOV14COLMTL-COL | game_winner | 0.549 | 0.445 | 0.466 | 45 | 56 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG4 | team_total | 0.389 | 0.485 | 0.465 | 49 | 52 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA3 | team_total | 0.576 | 0.670 | 0.652 | 68 | 34 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN3 | team_total | 0.547 | 0.635 | 0.618 | 64 | 37 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV14CGYLA-5 | game_total | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV14CGYLA-7 | game_total | 0.338 | 0.415 | 0.399 | 42 | 59 | no | +0.055 | OK |
| KXNHLTOTAL-26NOV14CGYLA-6 | game_total | 0.448 | 0.530 | 0.514 | 54 | 48 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN4 | team_total | 0.329 | 0.410 | 0.393 | 42 | 60 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV14CGYLA-LA3 | game_spread | 0.193 | 0.265 | 0.249 | 27 | 74 | no | +0.054 | OK |
| KXNHLGAME-26NOV14FLASTL-FLA | game_winner | 0.411 | 0.485 | 0.470 | 49 | 52 | no | +0.051 | OK |
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
| KXNHLTEAMTOTAL-26NOV14OTTPIT-PIT5 | team_total | 0.243 | 0.180 | 0.192 | 19 | 83 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV14CGYLA-LA5 | team_total | 0.176 | 0.250 | 0.234 | 27 | 77 | no | +0.042 | OK |
| KXNHLGAME-26NOV14CGYLA-CGY | game_winner | 0.438 | 0.375 | 0.387 | 38 | 63 | yes | +0.041 | OK |
| KXNHLGAME-26NOV14CGYLA-LA | game_winner | 0.562 | 0.625 | 0.613 | 63 | 38 | no | +0.041 | OK |
| KXNHLGAME-26NOV14FLASTL-STL | game_winner | 0.589 | 0.525 | 0.538 | 53 | 48 | yes | +0.041 | OK |
| KXNHLSPREAD-26NOV14COLMTL-MTL2 | game_spread | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
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
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL5 | team_total | 0.257 | 0.190 | 0.202 | 21 | 83 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV14MINBOS-7 | game_total | 0.389 | 0.445 | 0.434 | 45 | 56 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN5 | team_total | 0.164 | 0.220 | 0.208 | 23 | 79 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL3 | team_total | 0.661 | 0.600 | 0.612 | 61 | 41 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV14BUFDAL-DAL4 | team_total | 0.380 | 0.440 | 0.428 | 45 | 57 | no | +0.033 | OK |
| KXNHLGAME-26NOV14OTTPIT-OTT | game_winner | 0.500 | 0.555 | 0.544 | 56 | 45 | no | +0.033 | OK |
| KXNHLGAME-26NOV14OTTPIT-PIT | game_winner | 0.500 | 0.445 | 0.456 | 45 | 56 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL5 | team_total | 0.254 | 0.195 | 0.206 | 21 | 82 | yes | +0.032 | OK |
| KXNHLTOTAL-26NOV14MINBOS-5 | game_total | 0.726 | 0.775 | 0.766 | 78 | 23 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV14MINBOS-MIN2 | team_total | 0.768 | 0.825 | 0.815 | 84 | 19 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV14BUFDAL-4 | game_total | 0.821 | 0.870 | 0.861 | 88 | 14 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI4 | team_total | 0.264 | 0.325 | 0.312 | 34 | 69 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-STL4 | team_total | 0.447 | 0.390 | 0.401 | 40 | 62 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV14MINBOS-BOS2 | game_spread | 0.304 | 0.255 | 0.264 | 26 | 75 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL6 | team_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL3 | team_total | 0.667 | 0.610 | 0.622 | 62 | 40 | yes | +0.030 | OK |
| KXNHLTOTAL-26NOV14OTTPIT-8 | game_total | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV14FLASTL-FLA5 | team_total | 0.159 | 0.210 | 0.199 | 22 | 80 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV14FLASTL-STL3 | game_spread | 0.230 | 0.185 | 0.193 | 19 | 82 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV14MINBOS-6 | game_total | 0.504 | 0.560 | 0.549 | 57 | 45 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV14PHICBJ-7 | game_total | 0.355 | 0.410 | 0.399 | 42 | 60 | no | +0.029 | OK |
| KXNHLGAME-26NOV14WPGCHI-WPG | game_winner | 0.545 | 0.595 | 0.585 | 60 | 41 | no | +0.028 | OK |
| KXNHLGAME-26NOV14WPGCHI-CHI | game_winner | 0.455 | 0.405 | 0.415 | 41 | 60 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV14SJUTA-SJ2 | game_spread | 0.161 | 0.205 | 0.195 | 21 | 80 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-COL2 | team_total | 0.849 | 0.800 | 0.811 | 81 | 21 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14PHICBJ-PHI2 | team_total | 0.719 | 0.775 | 0.765 | 79 | 24 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV14OTTPIT-7 | game_total | 0.515 | 0.465 | 0.475 | 47 | 54 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14COLMTL-MTL4 | team_total | 0.385 | 0.435 | 0.425 | 44 | 57 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG2 | team_total | 0.814 | 0.860 | 0.852 | 87 | 15 | no | +0.028 | OK |
| KXNHLGAME-26NOV14NYIANA-NYI | game_winner | 0.446 | 0.495 | 0.485 | 50 | 51 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV14WPGCHI-WPG5 | team_total | 0.210 | 0.265 | 0.253 | 28 | 75 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV14NJWSH-9 | game_total | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV14CGYLA-8 | game_total | 0.173 | 0.220 | 0.210 | 23 | 79 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV14OTTPIT-OTT2 | game_spread | 0.289 | 0.335 | 0.326 | 34 | 67 | no | +0.025 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 47 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2631 (adj 0.2486) · $2.97 · thesis CHI:OFFENSE_4PLUS
- Josh Morrissey: 1+ assists NO @ 54c · p 0.6752 (adj 0.5841) · $5.32 · thesis WPG:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 60c · p 0.7333 (adj 0.6402) · $6.75 · thesis CHI:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 12c · p 0.1502 (adj 0.1414) · $1.48 · thesis CHI:OFFENSE_4PLUS
- William Borgen: 1+ goals YES @ 5c · p 0.0856 (adj 0.073) · $1.38 · thesis BOS:WINS_BY_2PLUS
- Kirill Kaprizov: 1+ goals NO @ 58c · p 0.655 (adj 0.6338) · $6.75 · thesis MIN:SUPPRESSED
- Michael Eyssimont: 1+ goals YES @ 12c · p 0.1531 (adj 0.1423) · $1.32 · thesis BOS:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1283 (adj 0.12) · $1.19 · thesis MIN:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1657 (adj 0.1493) · $2.78 · thesis TOR:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 10c · p 0.1426 (adj 0.1282) · $1.94 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 31c · p 0.4033 (adj 0.3542) · $3.62 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 27c · p 0.3469 (adj 0.3034) · $2.46 · thesis EDM:OFFENSE_4PLUS
- Martin Necas: 1+ goals YES @ 31c · p 0.3907 (adj 0.3693) · $5.38 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 32c · p 0.3888 (adj 0.3703) · $4.37 · thesis COL:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 50c · p 0.6154 (adj 0.5371) · $3.44 · thesis MTL:SUPPRESSED
- Jakub Dobes: 28+ saves YES @ 32c · p 0.4287 (adj 0.3515) · $2.35 · thesis MTL:NET_HIGH_VOLUME
- Conor Geekie: 1+ goals NO @ 82c · p 0.8728 (adj 0.8583) · $5.83 · thesis TBL:SUPPRESSED
- Jake Guentzel: 2+ goals YES @ 8c · p 0.1144 (adj 0.1046) · $1.38 · thesis TBL:OFFENSE_4PLUS
- Jake Guentzel: 1+ goals YES @ 38c · p 0.4445 (adj 0.4259) · $3.73 · thesis TBL:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 37c · p 0.4632 (adj 0.4141) · $4.3 · thesis TBL:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1521 (adj 0.1428) · $1.38 · thesis PIT:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 56c · p 0.6353 (adj 0.5927) · $3.07 · thesis OTT:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2444 (adj 0.2196) · $4.57 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 18c · p 0.2302 (adj 0.2139) · $2.25 · thesis WSH:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1512 (adj 0.1359) · $1.66 · thesis NJD:OFFENSE_4PLUS
- Lenni Hameenaho: 1+ goals YES @ 10c · p 0.1321 (adj 0.1203) · $1.22 · thesis NJD:OFFENSE_4PLUS
- Luca Del Bel Belluz: 1+ goals NO @ 86c · p 0.9154 (adj 0.9003) · $6.75 · thesis CBJ:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 15c · p 0.1954 (adj 0.1828) · $2.28 · thesis PHI:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2128 (adj 0.1983) · $1.81 · thesis CBJ:WINS_BY_2PLUS
- Travis Konecny: 1+ goals NO @ 78c · p 0.8115 (adj 0.8024) · $4.25 · thesis PHI:SUPPRESSED
- Pius Suter: 1+ goals YES @ 13c · p 0.1651 (adj 0.1551) · $1.56 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3514 (adj 0.3373) · $2.66 · thesis STL:OFFENSE_4PLUS
- Sam Bennett: 1+ goals YES @ 22c · p 0.2632 (adj 0.2511) · $2.01 · thesis FLA:OFFENSE_4PLUS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.196 (adj 0.1833) · $2.29 · thesis DAL:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 22c · p 0.2581 (adj 0.2473) · $1.67 · thesis BUF:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 28c · p 0.3225 (adj 0.3094) · $1.74 · thesis DAL:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 13c · p 0.1585 (adj 0.1489) · $1.05 · thesis BUF:OFFENSE_4PLUS
- Daniil But: 1+ goals NO @ 80c · p 0.8578 (adj 0.8421) · $6.75 · thesis UTA:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 67c · p 0.7546 (adj 0.7048) · $5.74 · thesis SJS:SUPPRESSED
- Jeff Malott: 1+ goals YES @ 10c · p 0.1491 (adj 0.1343) · $2.49 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0984 (adj 0.0863) · $1.77 · thesis ANA:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 11c · p 0.156 (adj 0.1432) · $2.38 · thesis ANA:OFFENSE_4PLUS
- Troy Terry: 1+ assists NO @ 67c · p 0.8391 (adj 0.7162) · $6.75 · thesis ANA:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0776 (adj 0.0645) · $1.28 · thesis LAK:WINS_BY_2PLUS
- Kevin Fiala: 1+ assists NO @ 61c · p 0.8191 (adj 0.6734) · $3.92 · thesis LAK:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 68c · p 0.8134 (adj 0.7202) · $3.92 · thesis LAK:SUPPRESSED
- Artemi Panarin: 1+ goals NO @ 65c · p 0.7014 (adj 0.6848) · $2.29 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ CHI** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.2, exp saves 24.26 (sd 6.68), pull risk 0.063
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.42, exp saves 22.0 (sd 6.15), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.267 | 0.410 | 42/60 | +0.117 | STANDARD |
| Josh Morrissey: 1+ points | 0.404 | 0.545 | 55/46 | +0.119 | STANDARD |
| Josh Morrissey: 1+ assists | 0.325 | 0.465 | 47/54 | +0.118 | STANDARD |
| Patrick Kane: 1+ points | 0.431 | 0.535 | 54/47 | +0.081 | STANDARD |
| Josh Morrissey: 2+ points | 0.093 | 0.190 | 20/82 | +0.077 | STANDARD |
| Kyle Connor: 2+ points | 0.278 | 0.370 | 38/64 | +0.066 | STANDARD |

**MIN @ BOS** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 29.01, exp saves 25.27 (sd 6.85), pull risk 0.056
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.53, exp saves 23.65 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Hampus Lindholm: 1+ points | 0.392 | 0.170 | 26/92 | +0.118 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.339 | 0.200 | 22/82 | +0.106 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.247 | 0.360 | 37/65 | +0.087 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.610 | 0.705 | 71/30 | +0.075 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.407 | 0.500 | 51/51 | +0.065 | STANDARD |
| Jonas Brodin: 1+ points | 0.301 | 0.210 | 24/82 | +0.048 | STANDARD |

**EDM @ TOR** · priced 174/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 29.92, exp saves 25.62 (sd 7.2), pull risk 0.087
- EDM net: Devon Levi (PROJECTED) exp shots 27.37, exp saves 23.77 (sd 6.56), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 1+ assists | 0.471 | 0.595 | 61/42 | +0.092 | STANDARD |
| Connor McDavid: 2+ assists | 0.222 | 0.345 | 35/66 | +0.102 | STANDARD |
| Connor McDavid: 2+ points | 0.429 | 0.545 | 55/46 | +0.094 | STANDARD |
| Leon Draisaitl: 2+ points | 0.345 | 0.460 | 47/55 | +0.088 | STANDARD |
| Connor McDavid: 1+ assists | 0.597 | 0.695 | 70/31 | +0.078 | STANDARD |
| John Tavares: 1+ assists | 0.274 | 0.370 | 38/64 | +0.070 | STANDARD |

**COL @ MTL** · priced 157/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.75, exp saves 26.28 (sd 7.16), pull risk 0.08
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.08, exp saves 22.45 (sd 6.29), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.385 | 0.505 | 51/50 | +0.098 | STANDARD |
| Jakub Dobes: 28+ saves | 0.429 | 0.310 | 32/70 | +0.093 |  |
| Mackenzie Blackwood: 24+ saves | 0.429 | 0.315 | 46/83 | -0.048 |  |
| Sam Malinski: 1+ assists | 0.391 | 0.280 | 30/74 | +0.076 | STANDARD |
| Sam Malinski: 1+ points | 0.450 | 0.345 | 38/69 | +0.053 | STANDARD |
| Gabriel Landeskog: 1+ assists | 0.323 | 0.220 | 24/80 | +0.070 | STANDARD |

**DET @ TBL** · priced 153/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.0, exp saves 22.96 (sd 6.3), pull risk 0.044
- DET net: Daniil Tarasov (PROBABLE) exp shots 28.29, exp saves 23.89 (sd 6.79), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.537 | 0.635 | 64/37 | +0.077 | STANDARD |
| Nikita Kucherov: 2+ points | 0.378 | 0.465 | 47/54 | +0.064 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.188 | 0.270 | 29/75 | +0.049 | STANDARD |
| Jake Guentzel: 1+ goals | 0.445 | 0.370 | 38/64 | +0.048 | STANDARD |
| Zemgus Girgensons: 1+ points | 0.346 | 0.275 | 30/75 | +0.031 | STANDARD |
| Charle-Edouard D'Astous: 1+ assists | 0.468 | 0.400 | 42/62 | +0.031 | STANDARD |

**OTT @ PIT** · priced 171/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (CONFIRMED) exp shots 26.72, exp saves 23.01 (sd 6.47), pull risk 0.068
- OTT net: Linus Ullmark (CONFIRMED) exp shots 26.84, exp saves 23.29 (sd 6.46), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.432 | 0.520 | 53/49 | +0.060 | STANDARD |
| Jake Sanderson: 1+ assists | 0.365 | 0.450 | 46/56 | +0.058 | STANDARD |
| Jake Sanderson: 1+ points | 0.444 | 0.520 | 53/49 | +0.048 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.273 | 0.200 | 22/82 | +0.041 | STANDARD |
| Jordan Spence: 1+ points | 0.361 | 0.290 | 30/72 | +0.047 | STANDARD |
| Sidney Crosby: 1+ assists | 0.364 | 0.435 | 45/58 | +0.038 | STANDARD |

**NJD @ WSH** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 29.47, exp saves 25.55 (sd 6.83), pull risk 0.064
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.15, exp saves 22.66 (sd 6.38), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.244 | 0.145 | 16/87 | +0.075 | STANDARD |
| Aliaksei Protas: 1+ points | 0.466 | 0.370 | 38/64 | +0.069 | STANDARD |
| Ryan Leonard: 1+ assists | 0.321 | 0.230 | 24/78 | +0.068 | STANDARD |
| Jack Hughes: 2+ points | 0.276 | 0.355 | 37/66 | +0.049 | STANDARD |
| Ryan Leonard: 1+ points | 0.469 | 0.390 | 41/63 | +0.042 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.313 | 0.380 | 40/64 | +0.031 | STANDARD |

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
| Gustav Forsling: 1+ assists | 0.262 | 0.135 | 24/97 | +0.009 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.435 | 0.520 | 54/50 | +0.047 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.221 | 0.300 | 31/71 | +0.055 | STANDARD |
| Dylan Holloway: 1+ points | 0.573 | 0.495 | 50/51 | +0.055 | STANDARD |
| Brady Tkachuk: 1+ points | 0.509 | 0.585 | 60/43 | +0.044 | STANDARD |
| Brady Tkachuk: 2+ points | 0.165 | 0.235 | 24/77 | +0.052 | STANDARD |

**BUF @ DAL** · priced 175/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 25.87, exp saves 22.59 (sd 6.2), pull risk 0.053
- BUF net: Alex Lyon (PROBABLE) exp shots 26.69, exp saves 22.97 (sd 6.28), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.227 | 0.325 | 34/69 | +0.068 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.435 | 0.530 | 54/48 | +0.068 | STANDARD |
| Alex Lyon: 25+ saves | 0.394 | 0.480 | 95/99 | -0.384 |  |
| Mikko Rantanen: 2+ assists | 0.113 | 0.185 | 21/84 | +0.037 | STANDARD |
| Tage Thompson: 1+ points | 0.544 | 0.605 | 62/41 | +0.029 | STANDARD |
| Thomas Harley: 2+ assists | 0.155 | 0.095 | 15/96 | -0.003 | STANDARD |

**SJS @ UTA** · priced 150/155 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 26.08, exp saves 22.89 (sd 6.27), pull risk 0.05
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.55, exp saves 25.18 (sd 6.92), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.399 | 0.505 | 52/51 | +0.073 | STANDARD |
| Vincent Trocheck: 1+ points | 0.504 | 0.610 | 63/41 | +0.069 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.245 | 0.345 | 36/67 | +0.069 | STANDARD |
| Alexander Wennberg: 1+ assists | 0.219 | 0.315 | 34/71 | +0.057 | STANDARD |
| Alexander Wennberg: 1+ points | 0.335 | 0.430 | 46/60 | +0.048 | STANDARD |
| Clayton Keller: 2+ points | 0.316 | 0.410 | 43/61 | +0.058 | STANDARD |

**NYI @ ANA** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 26.3, exp saves 22.87 (sd 6.32), pull risk 0.064
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.92, exp saves 24.55 (sd 6.98), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Troy Terry: 1+ assists | 0.161 | 0.350 | 37/67 | +0.154 | STANDARD |
| Tristan Luneau: 1+ points | 0.405 | 0.320 | 34/70 | +0.049 | STANDARD |
| Judd Caulfield: 1+ points | 0.403 | 0.320 | 33/69 | +0.057 | STANDARD |
| Matias Maccelli: 1+ assists | 0.216 | 0.295 | 31/72 | +0.050 | STANDARD |
| Drew Helleson: 1+ points | 0.303 | 0.225 | 25/80 | +0.040 | STANDARD |
| Tristan Luneau: 1+ assists | 0.340 | 0.265 | 28/75 | +0.046 | STANDARD |

**CGY @ LAK** · priced 160/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.67, exp saves 23.41 (sd 6.34), pull risk 0.044
- CGY net: Devin Cooley (PROJECTED) exp shots 29.98, exp saves 25.68 (sd 6.96), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Fiala: 1+ assists | 0.181 | 0.405 | 42/61 | +0.192 | STANDARD |
| Kevin Fiala: 1+ points | 0.393 | 0.570 | 59/45 | +0.139 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.187 | 0.330 | 34/68 | +0.118 | STANDARD |
| Artemi Panarin: 1+ points | 0.598 | 0.475 | 72/77 | -0.137 | STANDARD |
| Artemi Panarin: 2+ points | 0.228 | 0.330 | 34/68 | +0.077 | STANDARD |
| Mats Zuccarello: 1+ points | 0.340 | 0.430 | 45/59 | +0.053 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
