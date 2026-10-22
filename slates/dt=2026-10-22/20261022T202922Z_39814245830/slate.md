# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T20:29:22Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4862 · contracts joined: 2914 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2614, 'NO_EDGE': 123, 'OK': 177}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 467, 'game_early_goal': 12, 'first_goal': 435, 'game_winner': 24, 'player_goals': 752, 'game_overtime': 12, 'player_points': 629, 'goalie_saves': 19, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-90m | 0.585 | 0.415 | 0.170 | 6.45 | 3.50 | 2.96 | 227 (25/202) | CONFIRMED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-90m | 0.440 | 0.560 | 0.177 | 6.38 | 3.00 | 3.38 | 236 (25/211) | CONFIRMED/CONFIRMED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-90m | 0.558 | 0.442 | 0.167 | 6.61 | 3.50 | 3.11 | 265 (25/240) | PROBABLE/CONFIRMED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-90m | 0.589 | 0.411 | 0.164 | 6.40 | 3.49 | 2.91 | 227 (25/202) | CONFIRMED/CONFIRMED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-90m | 0.527 | 0.473 | 0.173 | 6.71 | 3.45 | 3.27 | 281 (25/256) | CONFIRMED/PROBABLE |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-3h | 0.577 | 0.423 | 0.186 | 5.81 | 3.13 | 2.67 | 208 (25/183) | CONFIRMED/PROBABLE |
| VGK @ STL | 2026-10-23T00:00:00Z | T-3h | 0.570 | 0.430 | 0.171 | 6.34 | 3.39 | 2.95 | 263 (25/238) | CONFIRMED/PROBABLE |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-3h | 0.593 | 0.407 | 0.187 | 5.47 | 3.01 | 2.45 | 258 (25/233) | CONFIRMED/CONFIRMED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-3h | 0.471 | 0.529 | 0.181 | 5.74 | 2.77 | 2.97 | 230 (25/205) | CONFIRMED/PROBABLE |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-3h | 0.532 | 0.468 | 0.176 | 6.55 | 3.37 | 3.17 | 236 (25/211) | CONFIRMED/PROBABLE |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-3h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 232 (25/207) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-3h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 251 (25/226) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.357 | 0.505 | 0.475 | 51 | 50 | no | +0.126 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.304 | 0.435 | 0.407 | 44 | 57 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.579 | 0.710 | 0.686 | 72 | 30 | no | +0.106 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.471 | 0.345 | 0.369 | 35 | 66 | yes | +0.105 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.529 | 0.655 | 0.631 | 66 | 35 | no | +0.105 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.430 | 0.545 | 0.522 | 55 | 46 | no | +0.093 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.570 | 0.455 | 0.478 | 46 | 55 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.183 | 0.295 | 0.270 | 30 | 71 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.181 | 0.295 | 0.269 | 31 | 72 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.349 | 0.255 | 0.272 | 26 | 75 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.791 | 0.875 | 0.861 | 88 | 13 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.671 | 0.755 | 0.739 | 76 | 25 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.452 | 0.360 | 0.378 | 37 | 65 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.133 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.482 | 0.565 | 0.548 | 57 | 44 | no | +0.061 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.423 | 0.505 | 0.489 | 51 | 50 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.577 | 0.495 | 0.511 | 50 | 51 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.666 | 0.580 | 0.598 | 59 | 43 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.474 | 0.555 | 0.539 | 56 | 45 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.237 | 0.315 | 0.298 | 32 | 69 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.259 | 0.180 | 0.194 | 19 | 83 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.247 | 0.175 | 0.188 | 18 | 83 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.411 | 0.335 | 0.350 | 34 | 67 | yes | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.589 | 0.665 | 0.650 | 67 | 34 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.369 | 0.445 | 0.430 | 45 | 56 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.222 | 0.155 | 0.167 | 16 | 85 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.113 | 0.175 | 0.161 | 18 | 83 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.567 | 0.640 | 0.626 | 65 | 37 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.367 | 0.435 | 0.421 | 44 | 57 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.507 | 0.580 | 0.566 | 59 | 43 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.289 | 0.355 | 0.341 | 36 | 65 | no | +0.045 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.535 | 0.522 | 54 | 47 | no | +0.045 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.713 | 0.775 | 0.763 | 78 | 23 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.395 | 0.381 | 40 | 61 | no | +0.044 | OK |
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
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.777 | 0.825 | 0.816 | 83 | 18 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.137 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ2 | team_total | 0.862 | 0.910 | 0.902 | 92 | 10 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22MINCGY-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22ANANJ-6 | game_total | 0.593 | 0.645 | 0.635 | 65 | 36 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.137 | 0.095 | 0.102 | 10 | 91 | yes | +0.031 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.593 | 0.645 | 0.635 | 65 | 36 | no | +0.031 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.407 | 0.355 | 0.365 | 36 | 65 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.665 | 0.720 | 0.709 | 73 | 29 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.510 | 0.498 | 52 | 50 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT22MINCGY-8 | game_total | 0.198 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.354 | 0.410 | 0.398 | 42 | 60 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.354 | 0.405 | 0.395 | 41 | 60 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.188 | 0.250 | 0.237 | 27 | 77 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR3 | team_total | 0.616 | 0.670 | 0.660 | 68 | 34 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.436 | 0.485 | 0.475 | 49 | 52 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.847 | 0.800 | 0.810 | 81 | 21 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.328 | 0.380 | 0.369 | 39 | 63 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.477 | 0.525 | 0.515 | 53 | 48 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-9 | game_total | 0.215 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-8 | game_total | 0.298 | 0.255 | 0.263 | 26 | 75 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22ANANJ-5 | game_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 44 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1919 (adj 0.1752) · $2.61 · thesis BOS:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 5c · p 0.077 (adj 0.0703) · $1.43 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 11c · p 0.1509 (adj 0.1382) · $1.95 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3146 (adj 0.2972) · $2.55 · thesis NSH:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.138 (adj 0.1248) · $1.66 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 11c · p 0.1356 (adj 0.128) · $1.05 · thesis TOR:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 26c · p 0.3215 (adj 0.2858) · $1.57 · thesis NYR:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 67c · p 0.7075 (adj 0.6956) · $3.2 · thesis NYR:SUPPRESSED
- Dmitry Orlov: 1+ goals NO @ 91c · p 0.9413 (adj 0.9322) · $6.52 · thesis SJS:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 56c · p 0.7139 (adj 0.6041) · $5.9 · thesis OTT:SUPPRESSED
- Ridly Greig: 1+ goals YES @ 16c · p 0.197 (adj 0.1865) · $1.68 · thesis OTT:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 70c · p 0.7767 (adj 0.7283) · $3.84 · thesis SJS:SUPPRESSED
- Alex Killorn: 1+ goals YES @ 17c · p 0.2217 (adj 0.2075) · $2.88 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 22c · p 0.3075 (adj 0.2588) · $2.77 · thesis ANA:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.67 (adj 0.6538) · $6.04 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 72c · p 0.7612 (adj 0.7496) · $4.72 · thesis NJD:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1897 (adj 0.171) · $3.13 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1495 (adj 0.1334) · $2.37 · thesis PIT:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.7084 (adj 0.6875) · $7.17 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 10c · p 0.1411 (adj 0.1283) · $2.13 · thesis FLA:WINS_BY_2PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2473 (adj 0.2367) · $1.68 · thesis NYI:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 23c · p 0.2698 (adj 0.2573) · $1.56 · thesis STL:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 73c · p 0.7692 (adj 0.7581) · $5.09 · thesis VGK:SUPPRESSED
- Tomas Hertl: 1+ goals NO @ 71c · p 0.7496 (adj 0.7385) · $4.72 · thesis VGK:SUPPRESSED
- Jake Neighbours: 1+ assists YES @ 24c · p 0.3023 (adj 0.2636) · $1.05 · thesis STL:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 3c · p 0.0544 (adj 0.0483) · $1.28 · thesis WPG:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 86c · p 0.8976 (adj 0.8857) · $7.17 · thesis DAL:SUPPRESSED
- Gabriel Vilardi: 1+ goals YES @ 22c · p 0.2655 (adj 0.2516) · $2.2 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 27c · p 0.3042 (adj 0.2944) · $1.25 · thesis WPG:OFFENSE_4PLUS
- Ben Jones: 1+ goals NO @ 86c · p 0.9142 (adj 0.8994) · $7.17 · thesis CGY:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2239 (adj 0.2079) · $2.92 · thesis CGY:OFFENSE_4PLUS
- Morgan Frost: 1+ goals YES @ 23c · p 0.2758 (adj 0.2606) · $2.1 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 51c · p 0.62 (adj 0.5453) · $3.44 · thesis MIN:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.111 (adj 0.0983) · $1.95 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1854 (adj 0.1678) · $2.76 · thesis EDM:OFFENSE_4PLUS
- Shayne Gostisbehere: 1+ assists NO @ 54c · p 0.6338 (adj 0.5844) · $5.96 · thesis CAR:SUPPRESSED
- Shane Wright: 1+ goals YES @ 14c · p 0.2009 (adj 0.1844) · $3.44 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1404 (adj 0.129) · $2.02 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.7021 (adj 0.6853) · $7.17 · thesis UTA:SUPPRESSED
- Mackie Samoskevich: 1+ goals YES @ 17c · p 0.215 (adj 0.2025) · $2.35 · thesis SEA:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 10c · p 0.1771 (adj 0.1553) · $4.09 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2699 (adj 0.2462) · $4.54 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1648 (adj 0.1511) · $2.12 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7198 (adj 0.7048) · $5.82 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 169/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (CONFIRMED) exp shots 27.6, exp saves 23.97 (sd 6.59), pull risk 0.062
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.21 (sd 6.77), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.389 | 0.515 | 52/49 | +0.103 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.445 | 45/56 | +0.088 | STANDARD |
| Marat Khusnutdinov: 1+ assists | 0.249 | 0.140 | 19/91 | +0.048 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.326 | 0.220 | 25/81 | +0.063 | STANDARD |
| Hampus Lindholm: 1+ points | 0.380 | 0.275 | 30/75 | +0.065 | STANDARD |
| Charlie McAvoy: 1+ points | 0.476 | 0.570 | 58/44 | +0.067 | STANDARD |

**NYR @ TOR** · priced 180/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.12 (sd 6.56), pull risk 0.063
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.92, exp saves 23.17 (sd 6.49), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colton Sissons: 1+ points | 0.332 | 0.145 | 28/99 | +0.038 | STANDARD |
| Tye Kartye: 1+ assists | 0.266 | 0.135 | 26/99 | -0.008 | STANDARD |
| Colton Sissons: 1+ assists | 0.227 | 0.115 | 22/99 | -0.005 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.463 | 0.545 | 56/47 | +0.050 | STANDARD |
| Dylan Garand: 26+ saves | 0.345 | 0.420 | 47/63 | +0.009 |  |
| Pavel Dorofeyev: 1+ assists | 0.240 | 0.315 | 33/70 | +0.045 | STANDARD |

**SJS @ OTT** · priced 213/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROBABLE) exp shots 24.89, exp saves 21.66 (sd 6.08), pull risk 0.055
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.6, exp saves 24.41 (sd 6.73), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.424 | 0.620 | 63/39 | +0.169 | STANDARD |
| Jordan Spence: 1+ assists | 0.311 | 0.125 | 24/99 | +0.059 | STANDARD |
| Tyler Kleven: 1+ assists | 0.257 | 0.080 | 15/99 | +0.098 | STANDARD |
| Tyler Kleven: 1+ points | 0.302 | 0.130 | 19/93 | +0.101 | STANDARD |
| Jake Sanderson: 1+ assists | 0.286 | 0.455 | 47/56 | +0.137 | STANDARD |
| Nick Cousins: 1+ points | 0.301 | 0.140 | 21/93 | +0.080 | STANDARD |

**ANA @ NJD** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (CONFIRMED) exp shots 27.82, exp saves 24.22 (sd 6.56), pull risk 0.06
- ANA net: Ville Husso (CONFIRMED) exp shots 29.59, exp saves 25.34 (sd 6.93), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.197 | 0.400 | 42/62 | +0.166 | STANDARD |
| Luke Evangelista: 1+ points | 0.375 | 0.530 | 54/48 | +0.127 | STANDARD |
| Ville Husso: 28+ saves | 0.366 | 0.510 | 53/51 | +0.106 |  |
| Jack Hughes: 1+ assists | 0.413 | 0.550 | 57/47 | +0.100 | STANDARD |
| Jack Hughes: 2+ points | 0.239 | 0.370 | 38/64 | +0.105 | STANDARD |
| Alex Killorn: 1+ points | 0.462 | 0.340 | 36/68 | +0.086 | STANDARD |

**FLA @ PIT** · priced 229/230 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.42, exp saves 23.02 (sd 6.33), pull risk 0.056
- FLA net: Cooper Black (PROBABLE) exp shots 27.3, exp saves 23.17 (sd 6.63), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Dewar: 1+ points | 0.384 | 0.155 | 24/93 | +0.131 | STANDARD |
| Kaedan Korczak: 1+ points | 0.284 | 0.105 | 20/99 | +0.073 | STANDARD |
| Connor Dewar: 1+ assists | 0.245 | 0.090 | 17/99 | +0.065 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.240 | 0.090 | 17/99 | +0.060 | STANDARD |
| Declan Carlile: 1+ points | 0.260 | 0.110 | 20/98 | +0.049 | STANDARD |
| Dmitry Kulikov: 1+ points | 0.220 | 0.095 | 18/99 | +0.030 | STANDARD |

**LAK @ NYI** · priced 154/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.26 (sd 6.35), pull risk 0.05
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.51), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jean-Gabriel Pageau: 1+ assists | 0.250 | 0.120 | 23/99 | +0.008 | STANDARD |
| Trevor Moore: 1+ assists | 0.275 | 0.165 | 23/90 | +0.033 | STANDARD |
| Victor Eklund: 1+ assists | 0.192 | 0.115 | 22/99 | -0.040 | STANDARD |
| Jean-Gabriel Pageau: 1+ points | 0.382 | 0.310 | 34/72 | +0.026 | STANDARD |
| Erik Haula: 1+ assists | 0.199 | 0.130 | 25/99 | -0.064 | STANDARD |
| Artemi Panarin: 1+ assists | 0.381 | 0.445 | 46/57 | +0.032 | STANDARD |

**VGK @ STL** · priced 207/212 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.81 (sd 6.62), pull risk 0.059
- VGK net: Adin Hill (PROBABLE) exp shots 25.57, exp saves 22.1 (sd 6.17), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pius Suter: 1+ points | 0.339 | 0.140 | 27/99 | +0.056 | STANDARD |
| Brayden McNabb: 1+ assists | 0.258 | 0.125 | 24/99 | +0.005 | STANDARD |
| Jack Eichel: 1+ assists | 0.428 | 0.555 | 57/46 | +0.094 | STANDARD |
| Jeremy Lauzon: 1+ points | 0.224 | 0.100 | 19/99 | +0.023 | STANDARD |
| Mitch Marner: 1+ assists | 0.401 | 0.525 | 54/49 | +0.091 | STANDARD |
| Justin Barron: 1+ points | 0.218 | 0.095 | 18/99 | +0.027 | STANDARD |

**WPG @ DAL** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.58 (sd 5.98), pull risk 0.047
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.81, exp saves 22.93 (sd 6.47), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.283 | 0.105 | 20/99 | +0.072 | STANDARD |
| Jamie Benn: 1+ points | 0.389 | 0.215 | 37/94 | +0.003 | STANDARD |
| Adam Lowry: 1+ points | 0.286 | 0.140 | 27/99 | +0.002 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.244 | 0.100 | 19/99 | +0.044 | STANDARD |
| Arttu Hyry: 1+ points | 0.285 | 0.145 | 28/99 | -0.009 | STANDARD |
| Dylan Samberg: 1+ assists | 0.231 | 0.100 | 19/99 | +0.030 | STANDARD |

**MIN @ CGY** · priced 166/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.26, exp saves 26.09 (sd 6.99), pull risk 0.062
- MIN net: Jesper Wallstedt (PROBABLE) exp shots 28.91, exp saves 25.19 (sd 6.66), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.234 | 0.355 | 37/66 | +0.090 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.380 | 0.495 | 50/51 | +0.093 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.274 | 0.385 | 40/63 | +0.079 | STANDARD |
| Quinn Hughes: 1+ assists | 0.540 | 0.645 | 67/38 | +0.064 | STANDARD |
| Max Shabanov: 1+ points | 0.357 | 0.445 | 47/58 | +0.046 | STANDARD |
| Quinn Hughes: 2+ assists | 0.178 | 0.265 | 29/76 | +0.050 | STANDARD |

**CAR @ EDM** · priced 172/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.06 (sd 7.0), pull risk 0.064
- CAR net: Brandon Bussi (PROBABLE) exp shots 25.41, exp saves 21.63 (sd 6.33), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Carrier: 1+ assists | 0.271 | 0.115 | 22/99 | +0.039 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.281 | 0.125 | 24/99 | +0.028 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.350 | 0.210 | 25/83 | +0.087 | STANDARD |
| William Carrier: 1+ points | 0.395 | 0.260 | 33/81 | +0.049 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.290 | 31/73 | +0.097 | STANDARD |
| Sebastian Aho: 2+ points | 0.209 | 0.325 | 33/68 | +0.096 | STANDARD |

**UTA @ SEA** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 1+ points | 0.590 | 0.725 | 73/28 | +0.116 | STANDARD |
| Anders Lee: 1+ points | 0.387 | 0.260 | 42/90 | -0.050 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.565 | 57/44 | +0.100 | STANDARD |
| Clayton Keller: 2+ points | 0.224 | 0.345 | 36/67 | +0.091 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.256 | 0.145 | 27/98 | -0.028 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.209 | 0.310 | 33/71 | +0.067 | STANDARD |

**DET @ VAN** · priced 172/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.411 | 0.180 | 33/97 | +0.066 | STANDARD |
| Drew O'Connor: 1+ points | 0.381 | 0.165 | 30/97 | +0.066 | STANDARD |
| Linus Karlsson: 1+ assists | 0.325 | 0.140 | 27/99 | +0.041 | STANDARD |
| Linus Karlsson: 1+ points | 0.503 | 0.330 | 40/74 | +0.086 | STANDARD |
| Max Sasson: 1+ points | 0.321 | 0.150 | 21/91 | +0.099 | STANDARD |
| Tom Willander: 1+ assists | 0.283 | 0.130 | 25/99 | +0.020 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
