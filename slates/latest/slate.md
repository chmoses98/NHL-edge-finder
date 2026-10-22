# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T12:11:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 3847 · contracts joined: 1948 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1648, 'NO_EDGE': 122, 'OK': 178}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 236, 'game_early_goal': 12, 'first_goal': 291, 'game_winner': 24, 'player_goals': 497, 'game_overtime': 12, 'player_points': 312, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-6h | 0.616 | 0.384 | 0.170 | 6.24 | 3.50 | 2.74 | 218 (25/193) | PROJECTED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-6h | 0.460 | 0.540 | 0.171 | 6.42 | 3.09 | 3.34 | 220 (25/195) | PROJECTED/PROJECTED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-6h | 0.558 | 0.442 | 0.172 | 6.45 | 3.42 | 3.04 | 217 (25/192) | PROJECTED/PROJECTED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-6h | 0.584 | 0.416 | 0.172 | 6.32 | 3.42 | 2.90 | 222 (25/197) | PROJECTED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-6h | 0.545 | 0.455 | 0.169 | 6.61 | 3.44 | 3.16 | 232 (25/207) | PROJECTED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-6h | 0.562 | 0.438 | 0.188 | 5.51 | 2.94 | 2.57 | 205 (25/180) | PROJECTED/PROJECTED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-6h | 0.550 | 0.450 | 0.174 | 6.36 | 3.34 | 3.02 | 225 (25/200) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-6h | 0.592 | 0.408 | 0.180 | 5.55 | 3.05 | 2.50 | 205 (25/180) | PROJECTED/PROJECTED |
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
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.595 | 0.700 | 0.680 | 71 | 31 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.186 | 0.290 | 0.267 | 30 | 72 | no | +0.080 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.550 | 0.455 | 0.474 | 46 | 55 | yes | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.377 | 0.470 | 0.451 | 48 | 54 | no | +0.066 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.450 | 0.535 | 0.518 | 54 | 47 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.285 | 0.265 | 30 | 73 | no | +0.060 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.332 | 0.255 | 0.269 | 26 | 75 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.228 | 0.305 | 0.289 | 31 | 70 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.682 | 0.755 | 0.741 | 76 | 25 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.602 | 0.685 | 0.669 | 70 | 33 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.252 | 0.185 | 0.197 | 19 | 82 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.170 | 0.183 | 18 | 84 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.437 | 0.360 | 0.375 | 37 | 65 | yes | +0.051 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.416 | 0.345 | 0.359 | 35 | 66 | yes | +0.050 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.584 | 0.655 | 0.641 | 66 | 35 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.580 | 0.596 | 59 | 43 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.210 | 0.195 | 22 | 80 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.193 | 0.265 | 0.249 | 28 | 75 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.865 | 0.855 | 87 | 14 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.339 | 0.405 | 0.392 | 41 | 60 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.043 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.481 | 0.550 | 0.536 | 56 | 46 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.525 | 0.512 | 53 | 48 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.355 | 0.415 | 0.403 | 42 | 59 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.267 | 0.330 | 0.317 | 34 | 68 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.679 | 0.735 | 0.724 | 74 | 27 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4 | team_total | 0.398 | 0.460 | 0.447 | 47 | 55 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.390 | 0.377 | 40 | 62 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.116 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.725 | 0.780 | 0.770 | 79 | 23 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3 | team_total | 0.611 | 0.670 | 0.659 | 68 | 34 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.370 | 0.430 | 0.418 | 44 | 58 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.592 | 0.645 | 0.635 | 65 | 36 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.408 | 0.355 | 0.365 | 36 | 65 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.674 | 0.735 | 0.723 | 75 | 28 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.583 | 0.640 | 0.629 | 65 | 37 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.555 | 0.544 | 56 | 45 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.266 | 0.325 | 0.313 | 34 | 69 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3 | team_total | 0.535 | 0.480 | 0.491 | 49 | 53 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK2 | team_total | 0.793 | 0.835 | 0.827 | 84 | 17 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.172 | 0.215 | 0.206 | 22 | 79 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-9 | game_total | 0.116 | 0.155 | 0.146 | 16 | 85 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.435 | 0.426 | 44 | 57 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.119 | 0.080 | 0.087 | 9 | 93 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.335 | 0.346 | 35 | 68 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT22FLAPIT-7 | game_total | 0.510 | 0.560 | 0.550 | 57 | 45 | no | +0.023 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22LANYI-7 | game_total | 0.331 | 0.380 | 0.370 | 39 | 63 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.118 | 0.165 | 0.155 | 18 | 85 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2 | team_total | 0.820 | 0.855 | 0.849 | 86 | 15 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.083 | 0.120 | 0.111 | 13 | 89 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.495 | 0.486 | 50 | 51 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.665 | 0.710 | 0.701 | 72 | 30 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.380 | 0.370 | 39 | 63 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.841 | 0.800 | 0.809 | 81 | 21 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4 | team_total | 0.314 | 0.275 | 0.283 | 28 | 73 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.150 | 0.185 | 0.177 | 19 | 82 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT22LANYI-6 | game_total | 0.443 | 0.485 | 0.477 | 49 | 52 | no | +0.020 | OK |

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

- Full Game: Over 7.5 goals scored YES @ 24c · p 0.298 (adj 0.2665) · $3.05 · thesis GAME:HIGH_EVENT
- Pavel Zacha: 1+ assists NO @ 55c · p 0.6662 (adj 0.5809) · $6.55 · thesis BOS:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 50c · p 0.6233 (adj 0.5302) · $5.61 · thesis BOS:SUPPRESSED
- Full Game: Over 5.5 goals scored YES @ 55c · p 0.6105 (adj 0.5777) · $3.04 · thesis BOS:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 55c · p 0.7163 (adj 0.5985) · $12.79 · thesis OTT:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2102 (adj 0.1864) · $7.48 · thesis ANA:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 70c · p 0.7914 (adj 0.7432) · $12.49 · thesis ANA:WINS
- Jack Hughes: 1+ goals NO @ 63c · p 0.6772 (adj 0.6642) · $5.86 · thesis NJD:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 71c · p 0.7916 (adj 0.7483) · $12.49 · thesis PIT:WINS
- Florida wins by over 2.5 goals NO @ 82c · p 0.8809 (adj 0.8455) · $1.83 · thesis PIT:WINS
- Florida over 4.5 goals scored NO @ 75c · p 0.815 (adj 0.7775) · $2.85 · thesis PIT:WINS
- Connor Dewar: 1+ goals YES @ 15c · p 0.1929 (adj 0.1697) · $1.31 · thesis PIT:WINS_BY_2PLUS
- Mats Zuccarello: 1+ assists NO @ 65c · p 0.836 (adj 0.6956) · $12.79 · thesis LAK:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7756 (adj 0.7403) · $8.18 · thesis GAME:TIGHT
- Dallas wins by over 1.5 goals NO @ 59c · p 0.6596 (adj 0.6223) · $1.88 · thesis GAME:TIGHT
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6804 (adj 0.6327) · $3.75 · thesis CGY:WINS
- Carolina wins by over 1.5 goals NO @ 69c · p 0.7639 (adj 0.7245) · $7.14 · thesis EDM:WINS
- Edmonton wins by over 1.5 goals YES @ 28c · p 0.3474 (adj 0.3112) · $2.16 · thesis EDM:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 80c · p 0.8552 (adj 0.8251) · $3.89 · thesis EDM:WINS
- Utah wins by over 2.5 goals NO @ 73c · p 0.8173 (adj 0.7712) · $12.79 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 21c · p 0.2807 (adj 0.2429) · $2.87 · thesis SEA:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 22c · p 0.3098 (adj 0.2624) · $3.22 · thesis VAN:WINS_BY_2PLUS
- Detroit wins by over 2.5 goals NO @ 74c · p 0.8499 (adj 0.7752) · $8.36 · thesis VAN:WINS
- Detroit over 5.5 goals scored NO @ 87c · p 0.9196 (adj 0.8898) · $6.87 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.6, exp saves 24.07 (sd 6.54), pull risk 0.056
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.23 (sd 6.73), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.377 | 0.520 | 54/50 | +0.106 | STANDARD |
| Filip Forsberg: 1+ goals | 0.331 | 0.195 | 31/92 | +0.006 | STANDARD |
| Filip Forsberg: 2+ points | 0.260 | 0.125 | 22/97 | +0.028 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.465 | 48/55 | +0.099 | STANDARD |
| Steven Stamkos: 1+ goals | 0.340 | 0.220 | 34/90 | -0.016 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.231 | 0.120 | 21/97 | +0.009 | STANDARD |

**NYR @ TOR** · priced 164/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 27.8, exp saves 24.16 (sd 6.63), pull risk 0.06
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.16 (sd 6.5), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Nylander: 2+ points | 0.271 | 0.165 | 30/97 | -0.044 | STANDARD |
| J.T. Miller: 1+ goals | 0.264 | 0.160 | 27/95 | -0.020 | STANDARD |
| William Nylander: 1+ goals | 0.350 | 0.260 | 33/81 | +0.005 | STANDARD |
| Kirill Marchenko: 1+ goals | 0.299 | 0.210 | 34/92 | -0.057 | STANDARD |
| Auston Matthews: 2+ points | 0.276 | 0.190 | 34/96 | -0.080 | STANDARD |
| Gabe Perreault: 1+ assists | 0.314 | 0.230 | 26/80 | +0.040 | STANDARD |

**SJS @ OTT** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.66 (sd 6.14), pull risk 0.057
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.36 (sd 6.71), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.284 | 0.465 | 48/55 | +0.149 | STANDARD |
| Jake Sanderson: 1+ points | 0.376 | 0.545 | 56/47 | +0.137 | STANDARD |
| Ivar Stenberg: 1+ points | 0.357 | 0.485 | 50/53 | +0.096 | STANDARD |
| Tim Stutzle: 1+ assists | 0.417 | 0.545 | 57/48 | +0.086 | STANDARD |
| Tim Stutzle: 1+ goals | 0.327 | 0.210 | 33/91 | -0.018 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.222 | 0.330 | 35/69 | +0.073 | STANDARD |

**ANA @ NJD** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 27.82, exp saves 24.19 (sd 6.63), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.35 (sd 7.01), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.198 | 0.385 | 41/64 | +0.146 | STANDARD |
| Luke Evangelista: 1+ points | 0.377 | 0.530 | 55/49 | +0.116 | STANDARD |
| Jack Hughes: 1+ assists | 0.411 | 0.535 | 55/48 | +0.091 | STANDARD |
| Jesper Bratt: 1+ assists | 0.392 | 0.505 | 52/51 | +0.080 | STANDARD |
| Jack Hughes: 2+ points | 0.233 | 0.345 | 36/67 | +0.082 | STANDARD |
| Leo Carlsson: 1+ goals | 0.295 | 0.185 | 27/90 | +0.011 | STANDARD |

**FLA @ PIT** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.42, exp saves 23.08 (sd 6.34), pull risk 0.055
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.16 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ goals | 0.376 | 0.195 | 34/95 | +0.020 | STANDARD |
| Sidney Crosby: 1+ goals | 0.366 | 0.225 | 36/91 | -0.010 | STANDARD |
| Rickard Rakell: 2+ points | 0.261 | 0.140 | 25/97 | -0.003 | STANDARD |
| Sam Reinhart: 1+ points | 0.486 | 0.595 | 62/43 | +0.066 | STANDARD |
| Sam Reinhart: 1+ assists | 0.295 | 0.400 | 42/62 | +0.069 | STANDARD |
| Evgeni Malkin: 1+ goals | 0.294 | 0.190 | 31/93 | -0.030 | STANDARD |

**LAK @ NYI** · priced 151/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.76, exp saves 23.35 (sd 6.23), pull risk 0.044
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.67, exp saves 23.92 (sd 6.57), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.164 | 0.380 | 41/65 | +0.170 | STANDARD |
| Mats Zuccarello: 1+ points | 0.337 | 0.505 | 53/52 | +0.125 | STANDARD |
| Bo Horvat: 1+ goals | 0.355 | 0.200 | 37/97 | -0.031 | STANDARD |
| Adrian Kempe: 1+ goals | 0.339 | 0.195 | 36/97 | -0.038 | STANDARD |
| Artemi Panarin: 1+ goals | 0.307 | 0.185 | 34/97 | -0.049 | STANDARD |
| Alex Laferriere: 1+ goals | 0.271 | 0.155 | 28/97 | -0.023 | STANDARD |

**VGK @ STL** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.79 (sd 6.58), pull risk 0.063
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.09 (sd 6.21), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jimmy Snuggerud: 1+ goals | 0.317 | 0.170 | 32/98 | -0.018 | STANDARD |
| Jack Eichel: 1+ assists | 0.436 | 0.570 | 60/46 | +0.086 | STANDARD |
| Robert Thomas: 1+ goals | 0.270 | 0.140 | 26/98 | -0.004 | STANDARD |
| Mark Stone: 1+ goals | 0.318 | 0.190 | 36/98 | -0.058 | STANDARD |
| Dylan Holloway: 1+ goals | 0.281 | 0.165 | 31/98 | -0.044 | STANDARD |
| Jack Eichel: 2+ points | 0.232 | 0.345 | 37/68 | +0.073 | STANDARD |

**WPG @ DAL** · priced 153/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.55 (sd 5.96), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.93 (sd 6.41), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 3+ points | 0.030 | 0.495 | 97/98 | -0.011 | STANDARD |
| Wyatt Johnston: 3+ points | 0.047 | 0.495 | 97/98 | -0.028 | STANDARD |
| Mikko Rantanen: 3+ points | 0.067 | 0.495 | 97/98 | -0.048 | STANDARD |
| Tyler Seguin: 2+ points | 0.090 | 0.500 | 99/99 | -0.081 | STANDARD |
| Roope Hintz: 3+ points | 0.041 | 0.440 | 86/98 | -0.023 | STANDARD |
| Mark Scheifele: 3+ points | 0.071 | 0.460 | 90/98 | -0.052 | STANDARD |

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
