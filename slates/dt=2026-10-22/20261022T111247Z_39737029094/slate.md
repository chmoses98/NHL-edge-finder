# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T11:12:47Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 3360 · contracts joined: 1461 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1161, 'NO_EDGE': 140, 'OK': 160}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 147, 'game_early_goal': 12, 'first_goal': 184, 'game_winner': 24, 'player_goals': 318, 'game_overtime': 12, 'player_points': 200, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-6h | 0.616 | 0.384 | 0.170 | 6.24 | 3.50 | 2.74 | 218 (25/193) | PROJECTED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-6h | 0.460 | 0.540 | 0.171 | 6.42 | 3.09 | 3.34 | 215 (25/190) | PROJECTED/PROJECTED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-6h | 0.558 | 0.442 | 0.172 | 6.45 | 3.42 | 3.04 | 217 (25/192) | PROJECTED/PROJECTED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-6h | 0.584 | 0.416 | 0.172 | 6.32 | 3.42 | 2.90 | 222 (25/197) | PROJECTED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-6h | 0.545 | 0.455 | 0.169 | 6.61 | 3.44 | 3.16 | 232 (25/207) | PROJECTED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-12h | 0.562 | 0.438 | 0.188 | 5.51 | 2.94 | 2.57 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-12h | 0.550 | 0.450 | 0.174 | 6.36 | 3.34 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-12h | 0.592 | 0.408 | 0.180 | 5.55 | 3.05 | 2.50 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-12h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-12h | 0.529 | 0.471 | 0.170 | 6.54 | 3.37 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-12h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-12h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.377 | 0.490 | 0.467 | 50 | 52 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.186 | 0.290 | 0.267 | 30 | 72 | no | +0.080 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.550 | 0.455 | 0.474 | 46 | 55 | yes | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.377 | 0.475 | 0.455 | 49 | 54 | no | +0.066 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.450 | 0.535 | 0.518 | 54 | 47 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.595 | 0.680 | 0.664 | 69 | 33 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.332 | 0.255 | 0.269 | 26 | 75 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.228 | 0.305 | 0.289 | 31 | 70 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.682 | 0.755 | 0.741 | 76 | 25 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.215 | 0.199 | 22 | 79 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.602 | 0.685 | 0.669 | 70 | 33 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.170 | 0.183 | 18 | 84 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.437 | 0.355 | 0.371 | 37 | 66 | yes | +0.051 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.416 | 0.345 | 0.359 | 35 | 66 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.245 | 0.315 | 0.300 | 32 | 69 | no | +0.050 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.385 | 0.399 | 39 | 62 | yes | +0.049 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.615 | 0.601 | 62 | 39 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.193 | 0.270 | 0.253 | 29 | 75 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.339 | 0.405 | 0.392 | 41 | 60 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.525 | 0.512 | 53 | 48 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.252 | 0.180 | 0.193 | 20 | 84 | yes | +0.041 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.584 | 0.650 | 0.637 | 66 | 36 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.265 | 0.253 | 27 | 74 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.580 | 0.596 | 60 | 44 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.355 | 0.415 | 0.403 | 42 | 59 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.267 | 0.335 | 0.321 | 35 | 68 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.679 | 0.735 | 0.724 | 74 | 27 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.385 | 0.374 | 39 | 62 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.116 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.860 | 0.851 | 87 | 15 | no | +0.034 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.605 | 0.594 | 61 | 40 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.370 | 0.435 | 0.422 | 45 | 58 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.471 | 0.525 | 0.514 | 53 | 48 | no | +0.032 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.529 | 0.475 | 0.486 | 48 | 53 | yes | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.592 | 0.645 | 0.635 | 65 | 36 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.408 | 0.355 | 0.365 | 36 | 65 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.674 | 0.735 | 0.723 | 75 | 28 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.481 | 0.545 | 0.532 | 56 | 47 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4 | team_total | 0.314 | 0.260 | 0.270 | 27 | 75 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.266 | 0.325 | 0.313 | 34 | 69 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3 | team_total | 0.535 | 0.480 | 0.491 | 49 | 53 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.134 | 0.090 | 0.098 | 10 | 92 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.172 | 0.215 | 0.206 | 22 | 79 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-9 | game_total | 0.116 | 0.155 | 0.146 | 16 | 85 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.340 | 0.350 | 35 | 67 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT22FLAPIT-7 | game_total | 0.510 | 0.555 | 0.546 | 56 | 45 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22LANYI-7 | game_total | 0.331 | 0.380 | 0.370 | 39 | 63 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.118 | 0.165 | 0.155 | 18 | 85 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3 | team_total | 0.611 | 0.655 | 0.646 | 66 | 35 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.495 | 0.484 | 51 | 52 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.583 | 0.635 | 0.625 | 65 | 38 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.083 | 0.125 | 0.115 | 14 | 89 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.545 | 0.536 | 55 | 46 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.841 | 0.795 | 0.805 | 81 | 22 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.210 | 0.218 | 22 | 80 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.150 | 0.185 | 0.177 | 19 | 82 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT22LANYI-6 | game_total | 0.443 | 0.485 | 0.477 | 49 | 52 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT22FLAPIT-6 | game_total | 0.625 | 0.670 | 0.661 | 68 | 34 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY2 | team_total | 0.763 | 0.715 | 0.725 | 73 | 30 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT22FLAPIT-FLA2 | game_spread | 0.256 | 0.295 | 0.287 | 30 | 71 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.606 | 0.555 | 0.565 | 57 | 46 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA5 | team_total | 0.219 | 0.260 | 0.251 | 27 | 75 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT22ANANJ-ANA2 | game_spread | 0.219 | 0.185 | 0.191 | 19 | 82 | yes | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.616 | 0.589 | 0.170 | 0.212 | 6.24 | 6.52 | 0.968/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH3 +0.056 |
| NYR @ TOR | 0.460 | 0.511 | 0.171 | 0.217 | 6.42 | 6.32 | 0.978/0.992 | KXNHLSPREAD-26OCT22NYRTOR-NYR2 -0.052 |
| SJS @ OTT | 0.558 | 0.567 | 0.172 | 0.214 | 6.45 | 6.29 | 1.041/1.034 | KXNHLTOTAL-26OCT22SJOTT-6 -0.027 |
| ANA @ NJD | 0.584 | 0.534 | 0.172 | 0.215 | 6.32 | 6.40 | 0.992/1.024 | KXNHLGAME-26OCT22ANANJ-ANA +0.049 |
| FLA @ PIT | 0.545 | 0.594 | 0.169 | 0.212 | 6.61 | 6.53 | 1.021/1.001 | KXNHLGAME-26OCT22FLAPIT-FLA -0.049 |
| LAK @ NYI | 0.562 | 0.545 | 0.188 | 0.224 | 5.51 | 5.89 | 0.956/0.989 | KXNHLTOTAL-26OCT22LANYI-7 +0.068 |
| VGK @ STL | 0.550 | 0.494 | 0.174 | 0.222 | 6.36 | 6.33 | 0.993/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.056 |
| WPG @ DAL | 0.592 | 0.575 | 0.180 | 0.214 | 5.55 | 5.95 | 0.986/0.988 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.072 |
| MIN @ CGY | 0.457 | 0.449 | 0.186 | 0.221 | 5.85 | 6.11 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.052 |
| CAR @ EDM | 0.529 | 0.567 | 0.170 | 0.215 | 6.54 | 6.74 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.052 |
| UTA @ SEA | 0.456 | 0.499 | 0.170 | 0.215 | 6.51 | 6.50 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-UTA -0.044 |
| DET @ VAN | 0.450 | 0.532 | 0.176 | 0.218 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 24 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 7.5 goals scored YES @ 24c · p 0.298 (adj 0.2665) · $3.31 · thesis GAME:HIGH_EVENT
- Full Game: Over 5.5 goals scored YES @ 55c · p 0.6105 (adj 0.5777) · $1.97 · thesis BOS:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 70c · p 0.7914 (adj 0.7432) · $17.8 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 19c · p 0.2501 (adj 0.2175) · $1.32 · thesis ANA:WINS_BY_2PLUS
- New Jersey over 3.5 goals scored NO @ 48c · p 0.5606 (adj 0.5178) · $1.33 · thesis NJD:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 12c · p 0.1549 (adj 0.1462) · $4.0 · thesis PIT:WINS_BY_2PLUS
- Florida wins by over 1.5 goals NO @ 71c · p 0.7916 (adj 0.7483) · $16.24 · thesis PIT:WINS
- Connor Dewar: 1+ goals YES @ 16c · p 0.1929 (adj 0.1847) · $3.09 · thesis PIT:WINS_BY_2PLUS
- Florida wins by over 2.5 goals NO @ 82c · p 0.8809 (adj 0.8455) · $3.04 · thesis PIT:WINS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7756 (adj 0.7403) · $11.38 · thesis GAME:TIGHT
- Dallas wins by over 1.5 goals NO @ 59c · p 0.6596 (adj 0.6223) · $2.61 · thesis GAME:TIGHT
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6804 (adj 0.6327) · $11.23 · thesis CGY:WINS
- Minnesota wins by over 2.5 goals NO @ 72c · p 0.7946 (adj 0.7523) · $2.94 · thesis CGY:WINS
- Calgary over 3.5 goals scored YES @ 27c · p 0.3445 (adj 0.3023) · $2.53 · thesis CGY:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 69c · p 0.7639 (adj 0.7245) · $9.94 · thesis EDM:WINS
- Edmonton wins by over 1.5 goals YES @ 28c · p 0.3474 (adj 0.3112) · $3.01 · thesis EDM:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 80c · p 0.8552 (adj 0.8251) · $5.42 · thesis EDM:WINS
- Utah wins by over 2.5 goals NO @ 74c · p 0.8173 (adj 0.7762) · $17.37 · thesis SEA:WINS
- Utah wins by over 1.5 goals NO @ 62c · p 0.7049 (adj 0.66) · $4.43 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 22c · p 0.2807 (adj 0.2454) · $1.31 · thesis SEA:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 22c · p 0.3098 (adj 0.2624) · $4.15 · thesis VAN:WINS_BY_2PLUS
- Vancouver wins by over 2.5 goals YES @ 13c · p 0.1966 (adj 0.1608) · $1.86 · thesis VAN:WINS_BY_2PLUS
- Detroit wins by over 1.5 goals NO @ 62c · p 0.7514 (adj 0.6627) · $4.87 · thesis VAN:WINS
- Detroit wins by over 2.5 goals NO @ 74c · p 0.8499 (adj 0.7752) · $13.89 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.6, exp saves 24.07 (sd 6.54), pull risk 0.056
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.23 (sd 6.73), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan O'Reilly: 3+ points | 0.062 | 0.495 | 98/99 | -0.053 | STANDARD |
| Steven Stamkos: 3+ points | 0.065 | 0.495 | 98/99 | -0.055 | STANDARD |
| Filip Forsberg: 3+ points | 0.077 | 0.495 | 98/99 | -0.068 | STANDARD |
| Steven Stamkos: 2+ assists | 0.088 | 0.495 | 98/99 | -0.078 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.231 | 0.495 | 98/99 | -0.221 | STANDARD |
| David Pastrnak: 1+ points | 0.673 | 0.410 | 81/99 | -0.148 | STANDARD |

**NYR @ TOR** · priced 159/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 27.8, exp saves 24.16 (sd 6.63), pull risk 0.06
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.16 (sd 6.5), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Nylander: 3+ points | 0.087 | 0.495 | 98/99 | -0.078 | STANDARD |
| Alexis Lafreniere: 1+ points | 0.587 | 0.340 | 67/99 | -0.099 | STANDARD |
| Gabe Perreault: 1+ points | 0.465 | 0.235 | 46/99 | -0.012 | STANDARD |
| William Nylander: 2+ points | 0.271 | 0.495 | 98/99 | -0.262 | STANDARD |
| Jack Roslovic: 1+ points | 0.483 | 0.260 | 51/99 | -0.044 | STANDARD |
| Easton Cowan: 1+ points | 0.487 | 0.270 | 53/99 | -0.060 | STANDARD |

**SJS @ OTT** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.66 (sd 6.14), pull risk 0.057
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.36 (sd 6.71), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 3+ points | 0.010 | 0.495 | 98/99 | -0.001 | STANDARD |
| Tim Stutzle: 3+ assists | 0.019 | 0.495 | 98/99 | -0.009 | STANDARD |
| Ivar Stenberg: 2+ assists | 0.025 | 0.495 | 98/99 | -0.016 | STANDARD |
| Mason Marchment: 2+ assists | 0.030 | 0.495 | 98/99 | -0.021 | STANDARD |
| Carter Yakemchuk: 2+ assists | 0.031 | 0.495 | 98/99 | -0.022 | STANDARD |
| Jacob Trouba: 2+ assists | 0.034 | 0.495 | 98/99 | -0.025 | STANDARD |

**ANA @ NJD** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 27.82, exp saves 24.19 (sd 6.63), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.35 (sd 7.01), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 3+ points | 0.011 | 0.500 | 99/99 | -0.002 | STANDARD |
| Cody Glass: 2+ goals | 0.014 | 0.495 | 98/99 | -0.005 | STANDARD |
| Evan Rodrigues: 2+ assists | 0.021 | 0.495 | 98/99 | -0.011 | STANDARD |
| Luke Evangelista: 2+ assists | 0.022 | 0.495 | 98/99 | -0.012 | STANDARD |
| Luke Hughes: 3+ points | 0.023 | 0.495 | 98/99 | -0.014 | STANDARD |
| Jack Hughes: 3+ assists | 0.019 | 0.490 | 97/99 | -0.010 | STANDARD |

**FLA @ PIT** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.42, exp saves 23.08 (sd 6.34), pull risk 0.055
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.16 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kris Letang: 2+ goals | 0.003 | 0.495 | 98/99 | +0.007 | STANDARD |
| Thomas Novak: 3+ goals | 0.003 | 0.495 | 98/99 | +0.006 | STANDARD |
| Garnet Hathaway: 2+ goals | 0.004 | 0.495 | 98/99 | +0.006 | STANDARD |
| Anton Lundell: 2+ assists | 0.025 | 0.495 | 98/99 | -0.016 | STANDARD |
| Sam Reinhart: 3+ points | 0.032 | 0.495 | 98/99 | -0.023 | STANDARD |
| Brady Tkachuk: 3+ points | 0.038 | 0.495 | 98/99 | -0.029 | STANDARD |

**LAK @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.76, exp saves 23.35 (sd 6.23), pull risk 0.044
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.67, exp saves 23.92 (sd 6.57), pull risk 0.06

**VGK @ STL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.79 (sd 6.58), pull risk 0.063
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.09 (sd 6.21), pull risk 0.056

**WPG @ DAL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.55 (sd 5.96), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.93 (sd 6.41), pull risk 0.063

**MIN @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.04 (sd 7.01), pull risk 0.067
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.13 (sd 6.71), pull risk 0.053

**CAR @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.08 (sd 6.92), pull risk 0.06
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.63 (sd 6.28), pull risk 0.081

**UTA @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

**DET @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
