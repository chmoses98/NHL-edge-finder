# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-12T16:42:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4075 · contracts joined: 2402 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 2127, 'OK': 153, 'NO_EDGE': 122}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 329, 'game_early_goal': 11, 'first_goal': 392, 'game_winner': 22, 'player_goals': 679, 'game_overtime': 11, 'player_points': 437, 'goalie_saves': 4, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 2026-11-12T17:00:00Z | T-10m | 0.385 | 0.615 | 0.167 | 6.54 | 2.90 | 3.64 | 246 (25/221) | CONFIRMED/CONFIRMED |
| MTL @ BOS | 2026-11-13T00:00:00Z | T-6h | 0.583 | 0.417 | 0.179 | 5.91 | 3.21 | 2.70 | 215 (25/190) | CONFIRMED/CONFIRMED |
| MIN @ TOR | 2026-11-13T00:00:00Z | T-6h | 0.430 | 0.570 | 0.172 | 6.43 | 2.99 | 3.44 | 209 (25/184) | CONFIRMED/PROJECTED |
| COL @ OTT | 2026-11-13T00:00:00Z | T-6h | 0.457 | 0.543 | 0.175 | 6.40 | 3.06 | 3.34 | 232 (25/207) | CONFIRMED/PROJECTED |
| WSH @ NJD | 2026-11-13T00:00:00Z | T-6h | 0.557 | 0.443 | 0.175 | 6.17 | 3.27 | 2.91 | 216 (25/191) | PROJECTED/PROJECTED |
| TBL @ CBJ | 2026-11-13T00:00:00Z | T-6h | 0.457 | 0.543 | 0.179 | 5.88 | 2.81 | 3.07 | 213 (25/188) | CONFIRMED/PROJECTED |
| DET @ FLA | 2026-11-13T00:30:00Z | T-6h | 0.573 | 0.427 | 0.176 | 6.08 | 3.27 | 2.82 | 220 (25/195) | CONFIRMED/PROJECTED |
| BUF @ CHI | 2026-11-13T01:00:00Z | T-6h | 0.454 | 0.546 | 0.182 | 5.94 | 2.83 | 3.11 | 218 (25/193) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-6h | 0.600 | 0.400 | 0.184 | 5.77 | 3.19 | 2.57 | 207 (25/182) | CONFIRMED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-6h | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 221 (25/196) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-6h | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 205 (25/180) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV12CARSEA-CAR3 | game_spread | 0.259 | 0.385 | 0.358 | 39 | 62 | no | +0.105 | OK |
| KXNHLSPREAD-26NOV12CARSEA-CAR2 | game_spread | 0.390 | 0.505 | 0.482 | 51 | 50 | no | +0.092 | OK |
| KXNHLGAME-26NOV12CARSEA-CAR | game_winner | 0.615 | 0.725 | 0.705 | 73 | 28 | no | +0.091 | OK |
| KXNHLGAME-26NOV12CARSEA-SEA | game_winner | 0.385 | 0.275 | 0.295 | 28 | 73 | yes | +0.091 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-7 | game_total | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR4 | team_total | 0.507 | 0.610 | 0.590 | 62 | 40 | no | +0.077 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-6 | game_total | 0.507 | 0.605 | 0.586 | 61 | 40 | no | +0.076 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.407 | 0.505 | 0.485 | 51 | 50 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.390 | 0.490 | 0.470 | 50 | 52 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA3 | team_total | 0.556 | 0.465 | 0.483 | 47 | 54 | yes | +0.069 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-6 | game_total | 0.518 | 0.605 | 0.588 | 61 | 40 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5 | team_total | 0.308 | 0.395 | 0.377 | 40 | 61 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA4 | team_total | 0.339 | 0.255 | 0.271 | 26 | 75 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR3 | team_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ4 | team_total | 0.324 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-5 | game_total | 0.732 | 0.810 | 0.796 | 82 | 20 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2 | team_total | 0.781 | 0.705 | 0.721 | 71 | 30 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL4 | team_total | 0.298 | 0.375 | 0.359 | 38 | 63 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF3 | team_total | 0.609 | 0.690 | 0.675 | 70 | 32 | no | +0.056 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.735 | 0.805 | 0.792 | 81 | 20 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA2 | game_spread | 0.201 | 0.130 | 0.142 | 14 | 88 | yes | +0.053 | OK |
| KXNHLTOTAL-26NOV12NYILA-5 | game_total | 0.695 | 0.770 | 0.756 | 78 | 24 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL3 | team_total | 0.513 | 0.590 | 0.575 | 60 | 42 | no | +0.050 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-4 | game_total | 0.825 | 0.885 | 0.875 | 89 | 12 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL2 | team_total | 0.741 | 0.810 | 0.797 | 82 | 20 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5 | team_total | 0.209 | 0.280 | 0.265 | 29 | 73 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5 | team_total | 0.172 | 0.115 | 0.125 | 12 | 89 | yes | +0.044 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.829 | 0.885 | 0.875 | 89 | 12 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.430 | 0.415 | 44 | 58 | no | +0.044 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.535 | 0.522 | 54 | 47 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 | team_total | 0.541 | 0.610 | 0.597 | 62 | 40 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.224 | 0.285 | 0.272 | 29 | 72 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-8 | game_total | 0.216 | 0.280 | 0.266 | 29 | 73 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ5 | team_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.812 | 0.870 | 0.860 | 88 | 14 | no | +0.040 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.845 | 0.836 | 85 | 16 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ2 | team_total | 0.763 | 0.825 | 0.814 | 84 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-5 | game_total | 0.733 | 0.790 | 0.779 | 80 | 22 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-9 | game_total | 0.154 | 0.210 | 0.198 | 22 | 80 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF3 | game_spread | 0.193 | 0.250 | 0.238 | 26 | 76 | no | +0.034 | OK |
| KXNHLGAME-26NOV12MINTOR-TOR | game_winner | 0.430 | 0.375 | 0.386 | 38 | 63 | yes | +0.033 | OK |
| KXNHLGAME-26NOV12MINTOR-MIN | game_winner | 0.570 | 0.625 | 0.614 | 63 | 38 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA3 | game_spread | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-SEA6 | team_total | 0.074 | 0.035 | 0.041 | 4 | 97 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.560 | 0.548 | 57 | 45 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-6 | game_total | 0.511 | 0.565 | 0.554 | 57 | 44 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-9 | game_total | 0.148 | 0.200 | 0.189 | 21 | 81 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.790 | 0.780 | 80 | 22 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR2 | team_total | 0.875 | 0.920 | 0.912 | 93 | 9 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-7 | game_total | 0.404 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL5 | team_total | 0.141 | 0.190 | 0.179 | 20 | 82 | no | +0.028 | OK |
| KXNHLGAME-26NOV12BUFCHI-BUF | game_winner | 0.546 | 0.595 | 0.585 | 60 | 41 | no | +0.027 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.454 | 0.405 | 0.415 | 41 | 60 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-4 | game_total | 0.825 | 0.870 | 0.862 | 88 | 14 | no | +0.027 | OK |
| KXNHLGAME-26NOV12MTLBOS-BOS | game_winner | 0.583 | 0.535 | 0.545 | 54 | 47 | yes | +0.026 | OK |
| KXNHLGAME-26NOV12TBCBJ-TB | game_winner | 0.543 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLGAME-26NOV12COLOTT-COL | game_winner | 0.543 | 0.495 | 0.505 | 50 | 51 | yes | +0.025 | OK |
| KXNHLSPREAD-26NOV12CARSEA-SEA3 | game_spread | 0.110 | 0.075 | 0.081 | 8 | 93 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-8 | game_total | 0.221 | 0.265 | 0.256 | 27 | 74 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.319 | 0.365 | 0.356 | 37 | 64 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV12MTLBOS-MTL2 | game_spread | 0.213 | 0.255 | 0.246 | 26 | 75 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12MTLBOS-MTL3 | game_spread | 0.118 | 0.155 | 0.147 | 16 | 85 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN3 | game_spread | 0.224 | 0.270 | 0.260 | 28 | 74 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4 | team_total | 0.380 | 0.425 | 0.416 | 43 | 58 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12NYILA-9 | game_total | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV12MINTOR-TOR2 | game_spread | 0.233 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN2 | game_spread | 0.352 | 0.395 | 0.386 | 40 | 61 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.091 | 0.125 | 0.118 | 13 | 88 | no | +0.021 | OK |
| KXNHLGAME-26NOV12DETFLA-DET | game_winner | 0.427 | 0.385 | 0.393 | 39 | 62 | yes | +0.021 | OK |
| KXNHLGAME-26NOV12DETFLA-FLA | game_winner | 0.573 | 0.615 | 0.607 | 62 | 39 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-5 | game_total | 0.716 | 0.755 | 0.748 | 76 | 25 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-9 | game_total | 0.150 | 0.185 | 0.178 | 19 | 82 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-10 | game_total | 0.065 | 0.095 | 0.088 | 10 | 91 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ2 | game_spread | 0.246 | 0.285 | 0.277 | 29 | 72 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV12CARSEA-CAR6 | team_total | 0.160 | 0.200 | 0.191 | 21 | 81 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ SEA | 0.385 | 0.411 | 0.167 | 0.212 | 6.54 | 6.70 | 1.023/0.984 | KXNHLTEAMTOTAL-26NOV12CARSEA-SEA4 +0.040 |
| MTL @ BOS | 0.583 | 0.590 | 0.179 | 0.209 | 5.91 | 6.65 | 0.956/0.983 | KXNHLTOTAL-26NOV12MTLBOS-7 +0.122 |
| MIN @ TOR | 0.430 | 0.505 | 0.172 | 0.217 | 6.43 | 6.46 | 0.956/0.995 | KXNHLGAME-26NOV12MINTOR-MIN -0.075 |
| COL @ OTT | 0.457 | 0.505 | 0.175 | 0.216 | 6.40 | 6.39 | 0.968/0.977 | KXNHLSPREAD-26NOV12COLOTT-COL2 -0.049 |
| WSH @ NJD | 0.557 | 0.556 | 0.175 | 0.216 | 6.17 | 6.31 | 0.959/0.961 | KXNHLTOTAL-26NOV12WSHNJ-7 +0.032 |
| TBL @ CBJ | 0.457 | 0.523 | 0.179 | 0.223 | 5.88 | 6.09 | 0.947/0.974 | KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 +0.071 |
| DET @ FLA | 0.573 | 0.576 | 0.176 | 0.220 | 6.08 | 6.26 | 0.992/1.015 | KXNHLTOTAL-26NOV12DETFLA-7 +0.035 |
| BUF @ CHI | 0.454 | 0.484 | 0.182 | 0.220 | 5.94 | 6.22 | 0.990/0.989 | KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI3 +0.058 |
| WPG @ DAL | 0.600 | 0.586 | 0.184 | 0.209 | 5.77 | 6.12 | 0.994/1.001 | KXNHLTOTAL-26NOV12WPGDAL-7 +0.061 |
| STL @ UTA | 0.511 | 0.532 | 0.172 | 0.220 | 6.17 | 6.40 | 0.993/0.993 | KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4 +0.044 |
| NYI @ LAK | 0.554 | 0.551 | 0.185 | 0.221 | 5.66 | 5.99 | 0.990/0.956 | KXNHLTOTAL-26NOV12NYILA-5 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Jani Nyman: 1+ goals YES @ 9c · p 0.1504 (adj 0.1316) · $5.3 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 15c · p 0.2214 (adj 0.2011) · $7.04 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 13c · p 0.1907 (adj 0.1743) · $5.94 · thesis SEA:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 62c · p 0.7507 (adj 0.6625) · $5.26 · thesis SEA:WINS
- William Borgen: 1+ goals YES @ 6c · p 0.0884 (adj 0.0813) · $2.65 · thesis BOS:WINS_BY_2PLUS
- Fraser Minten: 1+ goals YES @ 18c · p 0.2253 (adj 0.2127) · $4.11 · thesis BOS:OFFENSE_4PLUS
- Hampus Lindholm: 1+ goals YES @ 6c · p 0.0811 (adj 0.0746) · $1.66 · thesis BOS:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6284 (adj 0.605) · $13.1 · thesis MIN:SUPPRESSED
- Easton Cowan: 1+ goals YES @ 18c · p 0.2428 (adj 0.2258) · $6.66 · thesis TOR:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.135 (adj 0.12) · $2.18 · thesis MIN:OFFENSE_4PLUS
- Jack Roslovic: 1+ goals YES @ 25c · p 0.2905 (adj 0.2791) · $3.39 · thesis TOR:OFFENSE_4PLUS
- Hayden Hodgson: 1+ goals YES @ 6c · p 0.0959 (adj 0.0832) · $2.84 · thesis OTT:OFFENSE_4PLUS
- Jordan Spence: 1+ goals YES @ 6c · p 0.0885 (adj 0.0789) · $2.31 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.2036 (adj 0.189) · $3.6 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 19c · p 0.2227 (adj 0.212) · $2.24 · thesis OTT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2243 (adj 0.2095) · $5.64 · thesis WSH:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 13c · p 0.169 (adj 0.1555) · $3.17 · thesis NJD:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 18c · p 0.2112 (adj 0.2009) · $2.13 · thesis WSH:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2133 (adj 0.1962) · $5.1 · thesis CBJ:WINS_BY_2PLUS
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2702 (adj 0.2576) · $3.59 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ assists YES @ 25c · p 0.3111 (adj 0.2781) · $2.53 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4629 (adj 0.4289) · $6.23 · thesis GAME:LOW_EVENT
- J.T. Compher: 1+ goals YES @ 13c · p 0.1605 (adj 0.1504) · $2.23 · thesis DET:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 24c · p 0.2868 (adj 0.2701) · $3.43 · thesis CHI:OFFENSE_4PLUS
- Buffalo over 3.5 goals scored NO @ 52c · p 0.5998 (adj 0.5549) · $4.97 · thesis BUF:SUPPRESSED
- Buffalo wins by over 1.5 goals NO @ 64c · p 0.7081 (adj 0.6715) · $2.39 · thesis CHI:WINS
- Arttu Hyry: 1+ goals YES @ 15c · p 0.1787 (adj 0.169) · $1.91 · thesis DAL:OFFENSE_4PLUS
- Cole Perfetti: 1+ assists YES @ 30c · p 0.3621 (adj 0.3261) · $2.62 · thesis WPG:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 19c · p 0.2462 (adj 0.2284) · $5.1 · thesis UTA:OFFENSE_4PLUS
- MacKenzie Weegar: 1+ assists YES @ 29c · p 0.3669 (adj 0.326) · $3.92 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 14c · p 0.1824 (adj 0.1643) · $2.65 · thesis UTA:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.162 (adj 0.1515) · $2.41 · thesis STL:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 66c · p 0.8509 (adj 0.7171) · $13.1 · thesis LAK:SUPPRESSED
- Andre Lee: 1+ goals YES @ 9c · p 0.1318 (adj 0.1164) · $3.41 · thesis LAK:OFFENSE_4PLUS
- Alex Laferriere: 1+ goals YES @ 27c · p 0.3125 (adj 0.2981) · $3.4 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ SEA** · priced 191/195 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 31.95, exp saves 27.07 (sd 7.65), pull risk 0.089
- CAR net: Brandon Bussi (CONFIRMED) exp shots 23.45, exp saves 20.42 (sd 5.82), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.364 | 0.525 | 53/48 | +0.138 | STANDARD |
| Sebastian Aho: 2+ points | 0.185 | 0.345 | 35/66 | +0.139 | STANDARD |
| Sebastian Aho: 1+ points | 0.544 | 0.670 | 69/35 | +0.090 | STANDARD |
| Berkly Catton: 1+ points | 0.446 | 0.330 | 35/69 | +0.080 | STANDARD |
| Sebastian Aho: 1+ goals | 0.281 | 0.395 | 40/61 | +0.093 | STANDARD |
| Taylor Hall: 1+ assists | 0.207 | 0.320 | 33/69 | +0.088 | STANDARD |

**MTL @ BOS** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 26.96, exp saves 23.58 (sd 6.49), pull risk 0.057
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.11, exp saves 23.81 (sd 6.8), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.352 | 0.495 | 51/52 | +0.111 | STANDARD |
| Fraser Minten: 1+ points | 0.464 | 0.370 | 39/65 | +0.057 | STANDARD |
| Nick Suzuki: 1+ points | 0.544 | 0.630 | 65/39 | +0.049 | STANDARD |
| Nick Suzuki: 2+ points | 0.186 | 0.270 | 30/76 | +0.041 | STANDARD |
| Fraser Minten: 1+ assists | 0.307 | 0.225 | 23/78 | +0.065 | STANDARD |
| Tanner Jeannot: 1+ goals | 0.114 | 0.045 | 8/99 | +0.029 | STANDARD |

**MIN @ TOR** · priced 152/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.08, exp saves 26.9 (sd 7.18), pull risk 0.063
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.87, exp saves 23.93 (sd 6.63), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ points | 0.546 | 0.400 | 41/61 | +0.119 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.263 | 0.395 | 41/62 | +0.100 | STANDARD |
| Easton Cowan: 1+ assists | 0.403 | 0.275 | 28/73 | +0.109 | STANDARD |
| Teddy Blueger: 1+ goals | 0.176 | 0.070 | 10/96 | +0.070 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.633 | 0.735 | 75/28 | +0.073 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.415 | 0.510 | 53/51 | +0.058 | STANDARD |

**COL @ OTT** · priced 174/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (CONFIRMED) exp shots 28.4, exp saves 24.61 (sd 6.7), pull risk 0.062
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 27.05, exp saves 23.47 (sd 6.36), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Martin Necas: 1+ assists | 0.412 | 0.505 | 52/51 | +0.060 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.444 | 0.360 | 39/67 | +0.037 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.287 | 0.210 | 24/82 | +0.034 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.298 | 0.375 | 39/64 | +0.046 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.464 | 0.540 | 56/48 | +0.039 | STANDARD |
| Jordan Spence: 1+ points | 0.344 | 0.270 | 29/75 | +0.039 | STANDARD |

**WSH @ NJD** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 25.32, exp saves 22.03 (sd 6.08), pull risk 0.058
- WSH net: Logan Thompson (PROJECTED) exp shots 30.42, exp saves 26.06 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brett Pesce: 1+ points | 0.360 | 0.265 | 29/76 | +0.055 | STANDARD |
| Arseny Gritsyuk: 1+ points | 0.496 | 0.415 | 43/60 | +0.049 | STANDARD |
| Brett Pesce: 1+ assists | 0.309 | 0.245 | 26/77 | +0.036 | STANDARD |
| Jack Hughes: 2+ points | 0.297 | 0.360 | 38/66 | +0.027 | STANDARD |
| Arseny Gritsyuk: 1+ assists | 0.326 | 0.265 | 28/75 | +0.032 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.224 | 0.165 | 17/84 | +0.044 | STANDARD |

**TBL @ CBJ** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 27.7, exp saves 24.15 (sd 6.58), pull risk 0.054
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.39, exp saves 22.76 (sd 6.33), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.433 | 0.585 | 60/43 | +0.120 | STANDARD |
| Nikita Kucherov: 2+ points | 0.257 | 0.390 | 41/63 | +0.097 | STANDARD |
| Nikita Kucherov: 1+ points | 0.622 | 0.725 | 75/30 | +0.063 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.111 | 0.210 | 25/83 | +0.049 | STANDARD |
| Yanni Gourde: 1+ points | 0.253 | 0.335 | 36/69 | +0.042 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.213 | 0.145 | 16/87 | +0.044 | STANDARD |

**DET @ FLA** · priced 160/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 27.02, exp saves 23.58 (sd 6.37), pull risk 0.052
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.83, exp saves 23.78 (sd 6.68), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aaron Ekblad: 1+ points | 0.392 | 0.310 | 33/71 | +0.046 | STANDARD |
| Aaron Ekblad: 1+ assists | 0.331 | 0.250 | 27/77 | +0.047 | STANDARD |
| Gustav Forsling: 1+ points | 0.360 | 0.290 | 32/74 | +0.025 | STANDARD |
| Gustav Forsling: 1+ assists | 0.309 | 0.240 | 26/78 | +0.036 | STANDARD |
| Lucas Raymond: 1+ assists | 0.351 | 0.420 | 44/60 | +0.032 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.480 | 0.540 | 56/48 | +0.022 | STANDARD |

**BUF @ CHI** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.67, exp saves 25.66 (sd 6.84), pull risk 0.063
- BUF net: Alex Lyon (PROJECTED) exp shots 25.13, exp saves 21.69 (sd 6.06), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ points | 0.518 | 0.630 | 65/39 | +0.076 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.422 | 0.530 | 55/49 | +0.071 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.169 | 0.260 | 28/76 | +0.059 | STANDARD |
| Tage Thompson: 1+ points | 0.564 | 0.655 | 67/36 | +0.060 | STANDARD |
| Tage Thompson: 2+ points | 0.209 | 0.295 | 32/73 | +0.047 | STANDARD |
| Ryan Donato: 1+ assists | 0.270 | 0.190 | 21/83 | +0.048 | STANDARD |

**WPG @ DAL** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.66 (sd 6.03), pull risk 0.048
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.72, exp saves 22.89 (sd 6.34), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.257 | 0.395 | 42/63 | +0.097 | STANDARD |
| Josh Morrissey: 1+ points | 0.337 | 0.450 | 46/56 | +0.086 | STANDARD |
| Mikko Rantanen: 2+ points | 0.243 | 0.325 | 34/69 | +0.052 | STANDARD |
| Josh Morrissey: 2+ points | 0.062 | 0.140 | 16/88 | +0.051 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.525 | 54/49 | +0.040 | STANDARD |
| Cole Perfetti: 1+ assists | 0.362 | 0.290 | 30/72 | +0.047 | STANDARD |

**STL @ UTA** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.26), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.65, exp saves 24.64 (sd 6.73), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.450 | 0.345 | 38/69 | +0.054 | STANDARD |
| Jack McBain: 1+ points | 0.387 | 0.285 | 31/74 | +0.062 | STANDARD |
| Clayton Keller: 1+ assists | 0.478 | 0.565 | 58/45 | +0.054 | STANDARD |
| MacKenzie Weegar: 1+ assists | 0.367 | 0.285 | 29/72 | +0.062 | STANDARD |
| Robert Thomas: 1+ assists | 0.431 | 0.510 | 53/51 | +0.042 | STANDARD |
| Clayton Keller: 2+ points | 0.270 | 0.345 | 36/67 | +0.044 | STANDARD |

**NYI @ LAK** · priced 143/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.98, exp saves 23.62 (sd 6.37), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.46, exp saves 24.61 (sd 6.69), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.149 | 0.355 | 37/66 | +0.175 | STANDARD |
| Mats Zuccarello: 1+ points | 0.313 | 0.465 | 49/56 | +0.110 | STANDARD |
| Alex Laferriere: 1+ points | 0.608 | 0.520 | 54/50 | +0.050 | STANDARD |
| Andre Lee: 1+ goals | 0.132 | 0.070 | 9/95 | +0.036 | STANDARD |
| Alex Laferriere: 1+ assists | 0.431 | 0.370 | 39/65 | +0.025 | STANDARD |
| Alex Laferriere: 2+ points | 0.244 | 0.185 | 21/84 | +0.023 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
