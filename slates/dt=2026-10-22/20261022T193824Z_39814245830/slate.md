# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T19:38:24Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4868 · contracts joined: 2920 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2620, 'NO_EDGE': 120, 'OK': 180}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 469, 'game_early_goal': 12, 'first_goal': 436, 'game_winner': 24, 'player_goals': 753, 'game_overtime': 12, 'player_points': 631, 'goalie_saves': 19, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-3h | 0.585 | 0.415 | 0.170 | 6.45 | 3.50 | 2.96 | 227 (25/202) | CONFIRMED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-3h | 0.440 | 0.560 | 0.177 | 6.38 | 3.00 | 3.38 | 236 (25/211) | CONFIRMED/CONFIRMED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-3h | 0.558 | 0.442 | 0.167 | 6.61 | 3.50 | 3.11 | 265 (25/240) | PROBABLE/CONFIRMED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-3h | 0.589 | 0.411 | 0.164 | 6.40 | 3.49 | 2.91 | 227 (25/202) | CONFIRMED/CONFIRMED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-3h | 0.527 | 0.473 | 0.173 | 6.71 | 3.45 | 3.27 | 281 (25/256) | CONFIRMED/PROBABLE |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-3h | 0.577 | 0.423 | 0.186 | 5.81 | 3.13 | 2.67 | 208 (25/183) | CONFIRMED/PROBABLE |
| VGK @ STL | 2026-10-23T00:00:00Z | T-3h | 0.570 | 0.430 | 0.171 | 6.34 | 3.39 | 2.95 | 263 (25/238) | CONFIRMED/PROBABLE |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-3h | 0.593 | 0.407 | 0.187 | 5.47 | 3.01 | 2.45 | 258 (25/233) | CONFIRMED/CONFIRMED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-3h | 0.471 | 0.529 | 0.181 | 5.74 | 2.77 | 2.97 | 230 (25/205) | CONFIRMED/PROBABLE |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-3h | 0.532 | 0.468 | 0.176 | 6.55 | 3.37 | 3.17 | 242 (25/217) | CONFIRMED/PROBABLE |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-6h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 232 (25/207) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-6h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 251 (25/226) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.357 | 0.500 | 0.471 | 51 | 51 | no | +0.116 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.579 | 0.705 | 0.682 | 71 | 30 | no | +0.106 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.471 | 0.345 | 0.369 | 35 | 66 | yes | +0.105 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.529 | 0.655 | 0.631 | 66 | 35 | no | +0.105 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.304 | 0.425 | 0.400 | 43 | 58 | no | +0.099 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.430 | 0.545 | 0.522 | 55 | 46 | no | +0.093 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.570 | 0.455 | 0.478 | 46 | 55 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.183 | 0.295 | 0.270 | 30 | 71 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.181 | 0.290 | 0.265 | 30 | 72 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.349 | 0.255 | 0.272 | 26 | 75 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.671 | 0.755 | 0.739 | 76 | 25 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.452 | 0.360 | 0.378 | 37 | 65 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.133 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.482 | 0.565 | 0.548 | 57 | 44 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.791 | 0.870 | 0.857 | 88 | 14 | no | +0.061 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.423 | 0.505 | 0.489 | 51 | 50 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.577 | 0.495 | 0.511 | 50 | 51 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.666 | 0.580 | 0.598 | 59 | 43 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.259 | 0.185 | 0.198 | 19 | 82 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.247 | 0.175 | 0.188 | 18 | 83 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.411 | 0.335 | 0.350 | 34 | 67 | yes | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.589 | 0.665 | 0.650 | 67 | 34 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.369 | 0.445 | 0.430 | 45 | 56 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.222 | 0.155 | 0.167 | 16 | 85 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.237 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.474 | 0.545 | 0.531 | 55 | 46 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.113 | 0.175 | 0.161 | 18 | 83 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.567 | 0.640 | 0.626 | 65 | 37 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.367 | 0.435 | 0.421 | 44 | 57 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.507 | 0.575 | 0.562 | 58 | 43 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.289 | 0.355 | 0.341 | 36 | 65 | no | +0.045 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.535 | 0.522 | 54 | 47 | no | +0.045 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.713 | 0.775 | 0.763 | 78 | 23 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.395 | 0.381 | 40 | 61 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.777 | 0.835 | 0.824 | 84 | 17 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.592 | 0.660 | 0.647 | 67 | 35 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.215 | 0.280 | 0.266 | 29 | 73 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.686 | 0.750 | 0.738 | 76 | 26 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI3 | team_total | 0.617 | 0.555 | 0.568 | 56 | 45 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.803 | 0.860 | 0.850 | 87 | 15 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK2 | team_total | 0.783 | 0.840 | 0.830 | 85 | 17 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT22LANYI-NYI2 | game_spread | 0.340 | 0.285 | 0.296 | 29 | 72 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.135 | 0.190 | 0.178 | 20 | 82 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.078 | 0.130 | 0.118 | 14 | 88 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.156 | 0.210 | 0.198 | 22 | 80 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.137 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22MINCGY-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22ANANJ-6 | game_total | 0.593 | 0.645 | 0.635 | 65 | 36 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.137 | 0.095 | 0.102 | 10 | 91 | yes | +0.031 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.593 | 0.645 | 0.635 | 65 | 36 | no | +0.031 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.407 | 0.355 | 0.365 | 36 | 65 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.515 | 0.502 | 53 | 50 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT22MINCGY-8 | game_total | 0.198 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.188 | 0.255 | 0.240 | 28 | 77 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.436 | 0.485 | 0.475 | 49 | 52 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.847 | 0.800 | 0.810 | 81 | 21 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.328 | 0.380 | 0.369 | 39 | 63 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.477 | 0.525 | 0.515 | 53 | 48 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.163 | 0.205 | 0.196 | 21 | 80 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-9 | game_total | 0.215 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-8 | game_total | 0.298 | 0.255 | 0.263 | 26 | 75 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22ANANJ-5 | game_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.262 | 0.305 | 0.296 | 31 | 70 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT22SJOTT-8 | game_total | 0.318 | 0.275 | 0.283 | 28 | 73 | yes | +0.024 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.585 | 0.571 | 0.170 | 0.208 | 6.45 | 6.59 | 0.999/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH4 +0.029 |
| NYR @ TOR | 0.440 | 0.509 | 0.177 | 0.218 | 6.38 | 6.34 | 0.988/0.988 | KXNHLGAME-26OCT22NYRTOR-TOR +0.068 |
| SJS @ OTT | 0.558 | 0.558 | 0.167 | 0.214 | 6.61 | 6.36 | 1.061/1.039 | KXNHLTOTAL-26OCT22SJOTT-6 -0.046 |
| ANA @ NJD | 0.589 | 0.541 | 0.164 | 0.213 | 6.40 | 6.45 | 0.996/1.043 | KXNHLSPREAD-26OCT22ANANJ-NJ2 -0.049 |
| FLA @ PIT | 0.527 | 0.584 | 0.173 | 0.213 | 6.71 | 6.59 | 1.042/1.001 | KXNHLGAME-26OCT22FLAPIT-FLA -0.057 |
| LAK @ NYI | 0.577 | 0.534 | 0.186 | 0.226 | 5.81 | 5.96 | 0.978/0.994 | KXNHLTEAMTOTAL-26OCT22LANYI-LA4 +0.049 |
| VGK @ STL | 0.570 | 0.504 | 0.171 | 0.219 | 6.34 | 6.28 | 0.977/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.066 |
| WPG @ DAL | 0.593 | 0.580 | 0.187 | 0.216 | 5.47 | 6.01 | 0.994/1.003 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.092 |
| MIN @ CGY | 0.471 | 0.451 | 0.181 | 0.216 | 5.74 | 6.07 | 0.978/0.993 | KXNHLTOTAL-26OCT22MINCGY-7 +0.061 |
| CAR @ EDM | 0.532 | 0.565 | 0.176 | 0.210 | 6.55 | 6.74 | 0.994/0.987 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.046 |
| UTA @ SEA | 0.456 | 0.499 | 0.170 | 0.215 | 6.51 | 6.50 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-UTA -0.044 |
| DET @ VAN | 0.450 | 0.532 | 0.176 | 0.218 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 45 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1919 (adj 0.1752) · $2.66 · thesis BOS:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 11c · p 0.1509 (adj 0.1382) · $2.0 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3146 (adj 0.2972) · $2.67 · thesis NSH:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.6592 (adj 0.6457) · $4.47 · thesis BOS:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.138 (adj 0.1248) · $1.72 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 11c · p 0.1356 (adj 0.128) · $1.09 · thesis TOR:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 26c · p 0.3215 (adj 0.2858) · $1.62 · thesis NYR:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 67c · p 0.7075 (adj 0.6956) · $3.32 · thesis NYR:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 56c · p 0.7139 (adj 0.6041) · $7.27 · thesis OTT:SUPPRESSED
- Ridly Greig: 1+ goals YES @ 16c · p 0.197 (adj 0.1865) · $2.02 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.1773 (adj 0.1692) · $1.18 · thesis OTT:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 70c · p 0.7641 (adj 0.727) · $4.54 · thesis SJS:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2109 (adj 0.1869) · $4.53 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 17c · p 0.2217 (adj 0.2075) · $2.81 · thesis ANA:OFFENSE_4PLUS
- Jackson LaCombe: 1+ goals YES @ 10c · p 0.1408 (adj 0.1269) · $1.87 · thesis ANA:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.67 (adj 0.6538) · $6.88 · thesis NJD:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1897 (adj 0.171) · $3.23 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1495 (adj 0.1334) · $2.46 · thesis PIT:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.7084 (adj 0.6875) · $7.42 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 10c · p 0.1411 (adj 0.1283) · $2.2 · thesis FLA:WINS_BY_2PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2473 (adj 0.2367) · $1.74 · thesis NYI:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 55c · p 0.6188 (adj 0.5794) · $2.67 · thesis LAK:SUPPRESSED
- Trevor Connelly: 1+ goals NO @ 78c · p 0.8186 (adj 0.8077) · $6.38 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 73c · p 0.7692 (adj 0.7581) · $4.75 · thesis VGK:SUPPRESSED
- Jake Neighbours: 1+ assists YES @ 24c · p 0.3023 (adj 0.2636) · $1.13 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3162 (adj 0.3046) · $1.21 · thesis STL:OFFENSE_4PLUS
- Gabriel Vilardi: 1+ goals YES @ 21c · p 0.2655 (adj 0.2466) · $2.68 · thesis WPG:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 86c · p 0.8976 (adj 0.8857) · $7.42 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 71c · p 0.77 (adj 0.7375) · $2.72 · thesis GAME:TIGHT
- Mark Scheifele: 1+ goals YES @ 27c · p 0.3042 (adj 0.2944) · $1.15 · thesis WPG:OFFENSE_4PLUS
- Ben Jones: 1+ goals NO @ 86c · p 0.9142 (adj 0.8994) · $7.42 · thesis CGY:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2239 (adj 0.2079) · $3.01 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 51c · p 0.62 (adj 0.5453) · $3.6 · thesis MIN:SUPPRESSED
- Morgan Frost: 1+ goals YES @ 24c · p 0.2758 (adj 0.2643) · $1.44 · thesis CGY:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1854 (adj 0.1691) · $3.0 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.111 (adj 0.0983) · $2.01 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 24c · p 0.2899 (adj 0.2737) · $2.44 · thesis EDM:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 15c · p 0.2009 (adj 0.1869) · $2.85 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1404 (adj 0.129) · $2.08 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.7021 (adj 0.6853) · $7.42 · thesis UTA:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1544 (adj 0.1446) · $1.7 · thesis SEA:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 11c · p 0.1771 (adj 0.1566) · $3.65 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1648 (adj 0.1511) · $2.28 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7198 (adj 0.7048) · $6.01 · thesis DET:SUPPRESSED
- Jake DeBrusk: 1+ goals YES @ 28c · p 0.3247 (adj 0.3123) · $2.35 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 169/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (CONFIRMED) exp shots 27.6, exp saves 23.97 (sd 6.59), pull risk 0.062
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.21 (sd 6.77), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Hampus Lindholm: 1+ assists | 0.326 | 0.130 | 25/99 | +0.063 | STANDARD |
| Hampus Lindholm: 1+ points | 0.380 | 0.225 | 30/85 | +0.065 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.450 | 46/56 | +0.088 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.389 | 0.505 | 52/51 | +0.083 | STANDARD |
| Frederic Brunet: 1+ points | 0.279 | 0.165 | 31/98 | -0.046 | PRIOR_HEAVY |
| Marat Khusnutdinov: 1+ assists | 0.249 | 0.140 | 19/91 | +0.048 | STANDARD |

**NYR @ TOR** · priced 180/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.12 (sd 6.56), pull risk 0.063
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.92, exp saves 23.17 (sd 6.49), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tye Kartye: 1+ assists | 0.266 | 0.135 | 26/99 | -0.008 | STANDARD |
| Colton Sissons: 1+ assists | 0.227 | 0.115 | 22/99 | -0.005 | STANDARD |
| Colton Sissons: 1+ points | 0.332 | 0.225 | 28/83 | +0.038 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.463 | 0.545 | 56/47 | +0.050 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.240 | 0.315 | 33/70 | +0.045 | STANDARD |
| Nick Paul: 1+ assists | 0.248 | 0.175 | 24/89 | -0.005 | STANDARD |

**SJS @ OTT** · priced 213/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROBABLE) exp shots 24.89, exp saves 21.66 (sd 6.08), pull risk 0.055
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.6, exp saves 24.41 (sd 6.73), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tyler Kleven: 1+ points | 0.302 | 0.105 | 20/99 | +0.091 | STANDARD |
| Nick Cousins: 1+ points | 0.301 | 0.110 | 21/99 | +0.080 | STANDARD |
| Jordan Spence: 1+ assists | 0.311 | 0.125 | 24/99 | +0.059 | STANDARD |
| Tyler Kleven: 1+ assists | 0.257 | 0.080 | 15/99 | +0.098 | STANDARD |
| Jake Sanderson: 1+ assists | 0.286 | 0.455 | 47/56 | +0.137 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.424 | 0.590 | 60/42 | +0.138 | STANDARD |

**ANA @ NJD** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (CONFIRMED) exp shots 27.82, exp saves 24.22 (sd 6.56), pull risk 0.06
- ANA net: Ville Husso (CONFIRMED) exp shots 29.59, exp saves 25.34 (sd 6.93), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.197 | 0.395 | 42/63 | +0.156 | STANDARD |
| Luke Evangelista: 1+ points | 0.375 | 0.530 | 54/48 | +0.127 | STANDARD |
| Ville Husso: 28+ saves | 0.366 | 0.515 | 54/51 | +0.106 |  |
| Jack Hughes: 1+ assists | 0.413 | 0.550 | 57/47 | +0.100 | STANDARD |
| Jack Hughes: 2+ points | 0.239 | 0.370 | 38/64 | +0.105 | STANDARD |
| Alex Killorn: 1+ points | 0.462 | 0.335 | 35/68 | +0.096 | STANDARD |

**FLA @ PIT** · priced 229/230 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.42, exp saves 23.02 (sd 6.33), pull risk 0.056
- FLA net: Cooper Black (PROBABLE) exp shots 27.3, exp saves 23.17 (sd 6.63), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Dewar: 1+ points | 0.384 | 0.190 | 24/86 | +0.131 | STANDARD |
| Kaedan Korczak: 1+ points | 0.284 | 0.105 | 20/99 | +0.073 | STANDARD |
| Connor Dewar: 1+ assists | 0.245 | 0.090 | 17/99 | +0.065 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.240 | 0.090 | 17/99 | +0.060 | STANDARD |
| Declan Carlile: 1+ points | 0.260 | 0.110 | 20/98 | +0.049 | STANDARD |
| Niko Mikkola: 1+ points | 0.252 | 0.115 | 22/99 | +0.020 | STANDARD |

**LAK @ NYI** · priced 154/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.26 (sd 6.35), pull risk 0.05
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.51), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ points | 0.343 | 0.185 | 35/98 | -0.023 | STANDARD |
| Jean-Gabriel Pageau: 1+ assists | 0.250 | 0.125 | 24/99 | -0.003 | STANDARD |
| Trevor Moore: 1+ assists | 0.275 | 0.165 | 23/90 | +0.033 | STANDARD |
| Jean-Gabriel Pageau: 1+ points | 0.382 | 0.275 | 34/79 | +0.026 | STANDARD |
| Erik Haula: 1+ points | 0.330 | 0.250 | 37/87 | -0.057 | STANDARD |
| Artemi Panarin: 1+ assists | 0.381 | 0.460 | 47/55 | +0.051 | STANDARD |

**VGK @ STL** · priced 207/212 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.81 (sd 6.62), pull risk 0.059
- VGK net: Adin Hill (PROBABLE) exp shots 25.57, exp saves 22.1 (sd 6.17), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ assists | 0.288 | 0.130 | 25/99 | +0.025 | STANDARD |
| Rasmus Andersson: 1+ assists | 0.290 | 0.140 | 27/99 | +0.006 | STANDARD |
| Pius Suter: 1+ points | 0.339 | 0.190 | 30/92 | +0.025 | STANDARD |
| Mitch Marner: 1+ assists | 0.401 | 0.535 | 54/47 | +0.111 | STANDARD |
| Brayden McNabb: 1+ assists | 0.258 | 0.125 | 24/99 | +0.005 | STANDARD |
| Noah Hanifin: 2+ points | 0.045 | 0.175 | 34/99 | -0.036 | STANDARD |

**WPG @ DAL** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.58 (sd 5.98), pull risk 0.047
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.81, exp saves 22.93 (sd 6.47), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.283 | 0.105 | 20/99 | +0.072 | STANDARD |
| Adam Lowry: 1+ points | 0.286 | 0.140 | 27/99 | +0.002 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.244 | 0.100 | 19/99 | +0.044 | STANDARD |
| Arttu Hyry: 1+ points | 0.285 | 0.145 | 28/99 | -0.009 | STANDARD |
| Dylan Samberg: 1+ assists | 0.231 | 0.100 | 19/99 | +0.030 | STANDARD |
| Dylan DeMelo: 1+ points | 0.238 | 0.110 | 19/97 | +0.037 | STANDARD |

**MIN @ CGY** · priced 166/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.26, exp saves 26.09 (sd 6.99), pull risk 0.062
- MIN net: Jesper Wallstedt (PROBABLE) exp shots 28.91, exp saves 25.19 (sd 6.66), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.234 | 0.355 | 37/66 | +0.090 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.380 | 0.495 | 50/51 | +0.093 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.274 | 0.385 | 40/63 | +0.079 | STANDARD |
| Jesper Wallstedt: 23+ saves | 0.660 | 0.555 | 57/46 | +0.073 |  |
| Quinn Hughes: 1+ assists | 0.540 | 0.645 | 65/36 | +0.084 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.281 | 0.185 | 24/87 | +0.028 | STANDARD |

**CAR @ EDM** · priced 178/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.06 (sd 7.0), pull risk 0.064
- CAR net: Brandon Bussi (PROBABLE) exp shots 25.41, exp saves 21.63 (sd 6.33), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Carrier: 1+ points | 0.395 | 0.170 | 33/99 | +0.049 | STANDARD |
| Jordan Martinook: 1+ points | 0.343 | 0.165 | 30/97 | +0.028 | STANDARD |
| William Carrier: 1+ assists | 0.271 | 0.115 | 22/99 | +0.039 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.281 | 0.125 | 24/99 | +0.028 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.290 | 31/73 | +0.097 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.350 | 0.225 | 26/81 | +0.077 | STANDARD |

**UTA @ SEA** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 1+ points | 0.590 | 0.725 | 74/29 | +0.106 | STANDARD |
| Clayton Keller: 2+ points | 0.224 | 0.350 | 37/67 | +0.091 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.565 | 57/44 | +0.100 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.256 | 0.145 | 27/98 | -0.028 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.209 | 0.310 | 33/71 | +0.067 | STANDARD |
| Vincent Trocheck: 1+ points | 0.354 | 0.445 | 47/58 | +0.049 | STANDARD |

**DET @ VAN** · priced 172/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.411 | 0.175 | 33/98 | +0.066 | STANDARD |
| Max Sasson: 1+ points | 0.321 | 0.105 | 20/99 | +0.109 | STANDARD |
| Linus Karlsson: 1+ assists | 0.325 | 0.140 | 27/99 | +0.041 | STANDARD |
| Linus Karlsson: 1+ points | 0.503 | 0.330 | 40/74 | +0.086 | STANDARD |
| Tom Willander: 1+ assists | 0.283 | 0.130 | 25/99 | +0.020 | STANDARD |
| Ben Chiarot: 1+ assists | 0.248 | 0.095 | 18/99 | +0.057 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
