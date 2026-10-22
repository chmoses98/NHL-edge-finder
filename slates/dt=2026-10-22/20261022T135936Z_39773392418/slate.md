# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T13:59:36Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4181 · contracts joined: 2282 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1982, 'NO_EDGE': 126, 'OK': 174}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 295, 'game_early_goal': 12, 'first_goal': 365, 'game_winner': 24, 'player_goals': 622, 'game_overtime': 12, 'player_points': 388, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

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
| MIN @ CGY | 2026-10-23T01:00:00Z | T-6h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 218 (25/193) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-6h | 0.529 | 0.471 | 0.170 | 6.54 | 3.37 | 3.17 | 218 (25/193) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-12h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-12h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.186 | 0.295 | 0.270 | 30 | 71 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.377 | 0.485 | 0.463 | 49 | 52 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.595 | 0.700 | 0.680 | 71 | 31 | no | +0.080 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.550 | 0.455 | 0.474 | 46 | 55 | yes | +0.073 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.450 | 0.535 | 0.518 | 54 | 47 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.332 | 0.255 | 0.269 | 26 | 75 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.228 | 0.305 | 0.289 | 31 | 70 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.377 | 0.460 | 0.443 | 47 | 55 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.682 | 0.755 | 0.741 | 76 | 25 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.602 | 0.680 | 0.665 | 69 | 33 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.170 | 0.183 | 18 | 84 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.437 | 0.360 | 0.375 | 37 | 65 | yes | +0.051 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.416 | 0.345 | 0.359 | 35 | 66 | yes | +0.050 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.584 | 0.655 | 0.641 | 66 | 35 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.580 | 0.596 | 59 | 43 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.210 | 0.195 | 22 | 80 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.193 | 0.265 | 0.249 | 28 | 75 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.865 | 0.855 | 87 | 14 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.339 | 0.405 | 0.392 | 41 | 60 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.425 | 0.412 | 43 | 58 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.481 | 0.550 | 0.536 | 56 | 46 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.525 | 0.512 | 53 | 48 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.252 | 0.185 | 0.197 | 20 | 83 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.267 | 0.330 | 0.317 | 34 | 68 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.679 | 0.735 | 0.724 | 74 | 27 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.390 | 0.377 | 40 | 62 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.116 | 0.165 | 0.154 | 17 | 84 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.450 | 0.438 | 46 | 56 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22FLAPIT-7 | game_total | 0.510 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.725 | 0.780 | 0.770 | 79 | 23 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3 | team_total | 0.611 | 0.670 | 0.659 | 68 | 34 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.370 | 0.430 | 0.418 | 44 | 58 | no | +0.033 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.592 | 0.645 | 0.635 | 65 | 36 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.408 | 0.355 | 0.365 | 36 | 65 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.674 | 0.735 | 0.723 | 75 | 28 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.789 | 0.835 | 0.826 | 84 | 17 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.583 | 0.640 | 0.629 | 65 | 37 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.555 | 0.544 | 56 | 45 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT22FLAPIT-6 | game_total | 0.625 | 0.675 | 0.665 | 68 | 33 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.266 | 0.325 | 0.313 | 34 | 69 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.355 | 0.405 | 0.395 | 41 | 60 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.087 | 0.135 | 0.124 | 15 | 88 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4 | team_total | 0.398 | 0.450 | 0.439 | 46 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.127 | 0.170 | 0.160 | 18 | 84 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.340 | 0.350 | 35 | 67 | yes | +0.023 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22LANYI-7 | game_total | 0.331 | 0.380 | 0.370 | 39 | 63 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA5 | team_total | 0.118 | 0.165 | 0.155 | 18 | 85 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT22FLAPIT-5 | game_total | 0.819 | 0.855 | 0.848 | 86 | 15 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.490 | 0.480 | 50 | 52 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL6 | team_total | 0.083 | 0.125 | 0.115 | 14 | 89 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.500 | 0.490 | 51 | 51 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.665 | 0.710 | 0.701 | 72 | 30 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.380 | 0.370 | 39 | 63 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.841 | 0.800 | 0.809 | 81 | 21 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.150 | 0.185 | 0.177 | 19 | 82 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT22LANYI-6 | game_total | 0.443 | 0.485 | 0.477 | 49 | 52 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY2 | team_total | 0.763 | 0.725 | 0.733 | 73 | 28 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT22FLAPIT-FLA2 | game_spread | 0.256 | 0.295 | 0.287 | 30 | 71 | no | +0.019 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 34 recommended · full analysis in card.md / packet.json `thesis_card`

- David Pastrnak: 1+ goals NO @ 61c · p 0.6598 (adj 0.6461) · $5.79 · thesis BOS:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 49c · p 0.6233 (adj 0.5269) · $4.78 · thesis BOS:SUPPRESSED
- Matthew Wood: 1+ goals YES @ 16c · p 0.2026 (adj 0.1832) · $1.46 · thesis NSH:OFFENSE_4PLUS
- Full Game: Over 7.5 goals scored YES @ 24c · p 0.298 (adj 0.2665) · $2.48 · thesis GAME:HIGH_EVENT
- Pavel Dorofeyev: 1+ assists NO @ 69c · p 0.7627 (adj 0.7188) · $5.67 · thesis NYR:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 56c · p 0.716 (adj 0.6016) · $7.46 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 15c · p 0.183 (adj 0.1723) · $1.77 · thesis OTT:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 70c · p 0.7914 (adj 0.7432) · $8.73 · thesis ANA:WINS
- Jack Hughes: 1+ goals NO @ 63c · p 0.6772 (adj 0.6642) · $4.52 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 73c · p 0.7709 (adj 0.7582) · $4.92 · thesis NJD:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1549 (adj 0.1312) · $2.39 · thesis PIT:WINS_BY_2PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.7014 (adj 0.6823) · $8.73 · thesis FLA:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 71c · p 0.7916 (adj 0.7483) · $6.62 · thesis PIT:WINS
- Andrei Kuzmenko: 1+ goals YES @ 16c · p 0.2072 (adj 0.1866) · $1.87 · thesis PIT:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 65c · p 0.836 (adj 0.6988) · $8.73 · thesis LAK:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 4c · p 0.0647 (adj 0.056) · $1.36 · thesis LAK:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2461 (adj 0.2358) · $1.99 · thesis NYI:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 56c · p 0.6302 (adj 0.5901) · $3.58 · thesis LAK:SUPPRESSED
- Trevor Connelly: 1+ assists NO @ 72c · p 0.7823 (adj 0.7461) · $5.45 · thesis VGK:SUPPRESSED
- Dylan Samberg: 1+ goals YES @ 3c · p 0.0507 (adj 0.0443) · $1.14 · thesis WPG:OFFENSE_4PLUS
- Gabriel Vilardi: 1+ goals YES @ 21c · p 0.2645 (adj 0.2484) · $3.41 · thesis WPG:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7756 (adj 0.7403) · $4.71 · thesis GAME:TIGHT
- Jonathan Castagna: 1+ goals YES @ 8c · p 0.134 (adj 0.113) · $2.58 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6127 (adj 0.5895) · $6.37 · thesis MIN:SUPPRESSED
- Minnesota wins by over 2.5 goals NO @ 71c · p 0.7946 (adj 0.7498) · $6.98 · thesis CGY:WINS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1194 (adj 0.1021) · $1.61 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 69c · p 0.7639 (adj 0.7245) · $4.87 · thesis EDM:WINS
- Zach Hyman: 1+ goals YES @ 31c · p 0.3615 (adj 0.3424) · $2.31 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 80c · p 0.8552 (adj 0.8251) · $2.17 · thesis EDM:WINS
- Utah wins by over 2.5 goals NO @ 73c · p 0.8173 (adj 0.7712) · $8.73 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 21c · p 0.2807 (adj 0.2429) · $1.96 · thesis SEA:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 22c · p 0.3098 (adj 0.2624) · $2.2 · thesis VAN:WINS_BY_2PLUS
- Detroit wins by over 2.5 goals NO @ 74c · p 0.8499 (adj 0.7752) · $5.7 · thesis VAN:WINS
- Detroit over 5.5 goals scored NO @ 87c · p 0.9196 (adj 0.8898) · $4.69 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 27.6, exp saves 24.07 (sd 6.54), pull risk 0.056
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.23 (sd 6.73), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.377 | 0.525 | 54/49 | +0.116 | STANDARD |
| Marat Khusnutdinov: 1+ assists | 0.244 | 0.105 | 20/99 | +0.033 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.465 | 48/55 | +0.099 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.301 | 0.195 | 26/87 | +0.027 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.231 | 0.125 | 22/97 | -0.001 | STANDARD |
| Charlie McAvoy: 1+ points | 0.468 | 0.570 | 59/45 | +0.064 | STANDARD |

**NYR @ TOR** · priced 164/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 27.8, exp saves 24.16 (sd 6.63), pull risk 0.06
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.16 (sd 6.5), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gabe Perreault: 1+ assists | 0.314 | 0.140 | 26/98 | +0.040 | STANDARD |
| William Nylander: 2+ points | 0.271 | 0.165 | 30/97 | -0.044 | STANDARD |
| Auston Matthews: 2+ points | 0.276 | 0.185 | 34/97 | -0.080 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.237 | 0.325 | 34/69 | +0.058 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.461 | 0.540 | 56/48 | +0.042 | STANDARD |
| Alexis Lafreniere: 2+ points | 0.217 | 0.140 | 25/97 | -0.046 | STANDARD |

**SJS @ OTT** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.66 (sd 6.14), pull risk 0.057
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.36 (sd 6.71), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.284 | 0.460 | 48/56 | +0.139 | STANDARD |
| Jake Sanderson: 1+ points | 0.376 | 0.540 | 55/47 | +0.136 | STANDARD |
| Tim Stutzle: 1+ assists | 0.417 | 0.540 | 56/48 | +0.085 | STANDARD |
| Ivar Stenberg: 1+ points | 0.357 | 0.470 | 49/55 | +0.076 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.222 | 0.330 | 35/69 | +0.073 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.415 | 0.505 | 52/51 | +0.057 | STANDARD |

**ANA @ NJD** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 27.82, exp saves 24.19 (sd 6.63), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.35 (sd 7.01), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.198 | 0.380 | 41/65 | +0.136 | STANDARD |
| Luke Evangelista: 1+ points | 0.377 | 0.535 | 56/49 | +0.116 | STANDARD |
| Dawson Mercer: 1+ assists | 0.275 | 0.125 | 24/99 | +0.023 | STANDARD |
| Jack Hughes: 1+ assists | 0.411 | 0.545 | 56/47 | +0.101 | STANDARD |
| A.J. Greer: 1+ goals | 0.210 | 0.095 | 13/94 | +0.072 | STANDARD |
| Jack Hughes: 2+ points | 0.233 | 0.345 | 36/67 | +0.082 | STANDARD |

**FLA @ PIT** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.42, exp saves 23.08 (sd 6.34), pull risk 0.055
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.16 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Thomas Novak: 1+ assists | 0.393 | 0.175 | 34/99 | +0.037 | STANDARD |
| Rickard Rakell: 2+ points | 0.261 | 0.130 | 24/98 | +0.008 | STANDARD |
| Rickard Rakell: 1+ goals | 0.376 | 0.255 | 34/83 | +0.020 | STANDARD |
| Sam Reinhart: 1+ assists | 0.293 | 0.405 | 42/61 | +0.081 | STANDARD |
| Erik Karlsson: 2+ points | 0.234 | 0.130 | 23/97 | -0.008 | STANDARD |
| Connor Dewar: 1+ goals | 0.193 | 0.090 | 14/96 | +0.044 | STANDARD |

**LAK @ NYI** · priced 151/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.76, exp saves 23.35 (sd 6.23), pull risk 0.044
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.67, exp saves 23.92 (sd 6.57), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.164 | 0.375 | 40/65 | +0.170 | STANDARD |
| Mats Zuccarello: 1+ points | 0.337 | 0.500 | 52/52 | +0.125 | STANDARD |
| Trevor Moore: 1+ assists | 0.274 | 0.120 | 23/99 | +0.031 | STANDARD |
| Logan Stanley: 1+ assists | 0.237 | 0.130 | 24/98 | -0.016 | STANDARD |
| Artemi Panarin: 1+ goals | 0.307 | 0.210 | 32/90 | -0.029 | STANDARD |
| Artemi Panarin: 1+ assists | 0.370 | 0.450 | 46/56 | +0.053 | STANDARD |

**VGK @ STL** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.79 (sd 6.58), pull risk 0.063
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.09 (sd 6.21), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.436 | 0.555 | 57/46 | +0.086 | STANDARD |
| Mitch Marner: 1+ assists | 0.410 | 0.525 | 53/48 | +0.092 | STANDARD |
| Jack Eichel: 2+ points | 0.232 | 0.340 | 36/68 | +0.073 | STANDARD |
| Mitch Marner: 1+ points | 0.544 | 0.640 | 65/37 | +0.070 | STANDARD |
| Brett Howden: 1+ assists | 0.221 | 0.130 | 25/99 | -0.043 | STANDARD |
| Mark Stone: 1+ assists | 0.376 | 0.460 | 48/56 | +0.047 | STANDARD |

**WPG @ DAL** · priced 153/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.55 (sd 5.96), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.93 (sd 6.41), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jason Robertson: 1+ points | 0.649 | 0.475 | 70/75 | -0.066 | STANDARD |
| Mark Scheifele: 2+ points | 0.245 | 0.145 | 26/97 | -0.028 | STANDARD |
| Mikko Rantanen: 2+ points | 0.241 | 0.325 | 34/69 | +0.054 | STANDARD |
| Miro Heiskanen: 1+ points | 0.488 | 0.570 | 59/45 | +0.045 | STANDARD |
| Cole Perfetti: 2+ points | 0.174 | 0.095 | 16/97 | +0.004 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.432 | 0.505 | 51/50 | +0.051 | STANDARD |

**MIN @ CGY** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.04 (sd 7.01), pull risk 0.067
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.13 (sd 6.71), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matt Coronato: 1+ assists | 0.351 | 0.185 | 35/98 | -0.015 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.272 | 0.125 | 24/99 | +0.019 | STANDARD |
| Zayne Parekh: 1+ assists | 0.291 | 0.155 | 26/95 | +0.018 | STANDARD |
| Morgan Frost: 1+ goals | 0.270 | 0.135 | 24/97 | +0.017 | STANDARD |
| Danila Yurov: 1+ assists | 0.235 | 0.105 | 20/99 | +0.024 | STANDARD |
| Joel Eriksson Ek: 1+ goals | 0.305 | 0.175 | 32/97 | -0.030 | STANDARD |

**CAR @ EDM** · priced 156/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.08 (sd 6.92), pull risk 0.06
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.63 (sd 6.28), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.384 | 0.515 | 53/50 | +0.099 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.366 | 0.235 | 27/80 | +0.082 | STANDARD |
| Mattias Ekholm: 1+ points | 0.440 | 0.310 | 33/71 | +0.095 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.471 | 0.595 | 61/42 | +0.092 | STANDARD |
| Logan Stankoven: 1+ goals | 0.306 | 0.185 | 27/90 | +0.022 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.225 | 0.110 | 20/98 | +0.014 | STANDARD |

**UTA @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

**DET @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
