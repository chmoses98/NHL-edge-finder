# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T22:02:05Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4881 · contracts joined: 2933 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2633, 'NO_EDGE': 120, 'OK': 180}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 471, 'game_early_goal': 12, 'first_goal': 440, 'game_winner': 24, 'player_goals': 755, 'game_overtime': 12, 'player_points': 636, 'goalie_saves': 19, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-30m | 0.585 | 0.415 | 0.170 | 6.45 | 3.50 | 2.96 | 233 (25/208) | CONFIRMED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-30m | 0.440 | 0.560 | 0.177 | 6.38 | 3.00 | 3.38 | 236 (25/211) | CONFIRMED/CONFIRMED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-30m | 0.550 | 0.450 | 0.165 | 6.65 | 3.49 | 3.16 | 265 (25/240) | CONFIRMED/CONFIRMED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-30m | 0.589 | 0.411 | 0.164 | 6.40 | 3.49 | 2.91 | 227 (25/202) | CONFIRMED/CONFIRMED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-30m | 0.527 | 0.473 | 0.173 | 6.71 | 3.45 | 3.27 | 285 (25/260) | CONFIRMED/CONFIRMED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-60m | 0.577 | 0.423 | 0.186 | 5.81 | 3.13 | 2.67 | 208 (25/183) | CONFIRMED/PROBABLE |
| VGK @ STL | 2026-10-23T00:00:00Z | T-90m | 0.570 | 0.430 | 0.171 | 6.34 | 3.39 | 2.95 | 266 (25/241) | CONFIRMED/PROBABLE |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-90m | 0.593 | 0.407 | 0.187 | 5.47 | 3.01 | 2.45 | 258 (25/233) | CONFIRMED/CONFIRMED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-90m | 0.463 | 0.537 | 0.188 | 5.73 | 2.75 | 2.98 | 235 (25/210) | CONFIRMED/CONFIRMED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-90m | 0.532 | 0.468 | 0.176 | 6.55 | 3.37 | 3.17 | 236 (25/211) | CONFIRMED/PROBABLE |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-3h | 0.491 | 0.509 | 0.174 | 6.27 | 3.10 | 3.17 | 232 (25/207) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-3h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 252 (25/227) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.358 | 0.505 | 0.475 | 51 | 50 | no | +0.124 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.578 | 0.715 | 0.690 | 72 | 29 | no | +0.117 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.537 | 0.655 | 0.632 | 66 | 35 | no | +0.097 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.463 | 0.345 | 0.368 | 35 | 66 | yes | +0.097 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.179 | 0.300 | 0.273 | 31 | 71 | no | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.396 | 0.520 | 0.495 | 53 | 49 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.308 | 0.425 | 0.400 | 43 | 58 | no | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.491 | 0.375 | 0.398 | 38 | 63 | yes | +0.095 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.509 | 0.625 | 0.602 | 63 | 38 | no | +0.095 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.430 | 0.545 | 0.522 | 55 | 46 | no | +0.093 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.570 | 0.455 | 0.478 | 46 | 55 | yes | +0.093 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.182 | 0.295 | 0.269 | 31 | 72 | no | +0.084 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.292 | 0.395 | 0.373 | 40 | 61 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.178 | 0.275 | 0.253 | 28 | 73 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.619 | 0.720 | 0.701 | 73 | 29 | no | +0.077 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.349 | 0.250 | 0.268 | 26 | 76 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.671 | 0.755 | 0.739 | 76 | 25 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.452 | 0.360 | 0.378 | 37 | 65 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.133 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.480 | 0.565 | 0.548 | 57 | 44 | no | +0.062 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.423 | 0.505 | 0.489 | 51 | 50 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.577 | 0.495 | 0.511 | 50 | 51 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.666 | 0.580 | 0.598 | 59 | 43 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.474 | 0.555 | 0.539 | 56 | 45 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA5 | team_total | 0.217 | 0.305 | 0.286 | 32 | 71 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.237 | 0.315 | 0.298 | 32 | 69 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.795 | 0.870 | 0.857 | 88 | 14 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.278 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.367 | 0.445 | 0.429 | 45 | 56 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.367 | 0.445 | 0.429 | 45 | 56 | no | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.411 | 0.335 | 0.350 | 34 | 67 | yes | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.589 | 0.665 | 0.650 | 67 | 34 | no | +0.056 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.545 | 0.530 | 55 | 46 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.245 | 0.175 | 0.188 | 18 | 83 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.222 | 0.155 | 0.167 | 16 | 85 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.592 | 0.665 | 0.651 | 67 | 34 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA2 | team_total | 0.821 | 0.885 | 0.874 | 89 | 12 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.215 | 0.285 | 0.270 | 29 | 72 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.113 | 0.175 | 0.161 | 18 | 83 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.259 | 0.185 | 0.198 | 20 | 83 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.567 | 0.640 | 0.626 | 65 | 37 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.507 | 0.580 | 0.566 | 59 | 43 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.289 | 0.355 | 0.341 | 36 | 65 | no | +0.045 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.713 | 0.775 | 0.763 | 78 | 23 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.156 | 0.215 | 0.202 | 22 | 79 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.686 | 0.750 | 0.738 | 76 | 26 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI3 | team_total | 0.617 | 0.555 | 0.568 | 56 | 45 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR3 | team_total | 0.616 | 0.675 | 0.664 | 68 | 33 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.076 | 0.135 | 0.121 | 15 | 88 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.477 | 0.535 | 0.523 | 54 | 47 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT22LANYI-NYI2 | game_spread | 0.340 | 0.285 | 0.296 | 29 | 72 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.135 | 0.195 | 0.182 | 21 | 82 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.262 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-4 | game_total | 0.808 | 0.860 | 0.851 | 87 | 15 | no | +0.033 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.777 | 0.830 | 0.820 | 84 | 18 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.746 | 0.795 | 0.786 | 80 | 21 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.137 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22MINCGY-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22UTASEA-5 | game_total | 0.778 | 0.825 | 0.816 | 83 | 18 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ2 | team_total | 0.862 | 0.910 | 0.902 | 92 | 10 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA6 | team_total | 0.100 | 0.155 | 0.142 | 17 | 86 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT22ANANJ-6 | game_total | 0.593 | 0.645 | 0.635 | 65 | 36 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR4 | team_total | 0.402 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.137 | 0.095 | 0.102 | 10 | 91 | yes | +0.031 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.593 | 0.645 | 0.635 | 65 | 36 | no | +0.031 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.407 | 0.355 | 0.365 | 36 | 65 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.314 | 0.260 | 0.270 | 27 | 75 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT22SJOTT-8 | game_total | 0.324 | 0.275 | 0.284 | 28 | 73 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.607 | 0.550 | 0.562 | 56 | 46 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.354 | 0.415 | 0.402 | 43 | 60 | no | +0.030 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.585 | 0.571 | 0.170 | 0.208 | 6.45 | 6.59 | 0.999/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH4 +0.029 |
| NYR @ TOR | 0.440 | 0.509 | 0.177 | 0.218 | 6.38 | 6.34 | 0.988/0.988 | KXNHLGAME-26OCT22NYRTOR-TOR +0.068 |
| SJS @ OTT | 0.550 | 0.556 | 0.165 | 0.212 | 6.65 | 6.38 | 1.071/1.039 | KXNHLTOTAL-26OCT22SJOTT-6 -0.047 |
| ANA @ NJD | 0.589 | 0.541 | 0.164 | 0.213 | 6.40 | 6.45 | 0.996/1.043 | KXNHLSPREAD-26OCT22ANANJ-NJ2 -0.049 |
| FLA @ PIT | 0.527 | 0.585 | 0.173 | 0.212 | 6.71 | 6.58 | 1.042/1.000 | KXNHLGAME-26OCT22FLAPIT-FLA -0.058 |
| LAK @ NYI | 0.577 | 0.534 | 0.186 | 0.226 | 5.81 | 5.96 | 0.978/0.994 | KXNHLTEAMTOTAL-26OCT22LANYI-LA4 +0.049 |
| VGK @ STL | 0.570 | 0.504 | 0.171 | 0.219 | 6.34 | 6.28 | 0.977/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.066 |
| WPG @ DAL | 0.593 | 0.580 | 0.187 | 0.216 | 5.47 | 6.01 | 0.994/1.003 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.092 |
| MIN @ CGY | 0.463 | 0.452 | 0.188 | 0.219 | 5.73 | 6.07 | 0.978/0.991 | KXNHLTOTAL-26OCT22MINCGY-7 +0.067 |
| CAR @ EDM | 0.532 | 0.565 | 0.176 | 0.210 | 6.55 | 6.74 | 0.994/0.987 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.046 |
| UTA @ SEA | 0.491 | 0.498 | 0.174 | 0.215 | 6.27 | 6.52 | 1.015/0.992 | KXNHLTOTAL-26OCT22UTASEA-7 +0.043 |
| DET @ VAN | 0.450 | 0.531 | 0.176 | 0.215 | 6.37 | 6.28 | 1.021/1.003 | KXNHLGAME-26OCT22DETVAN-DET -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 46 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1919 (adj 0.1752) · $2.53 · thesis BOS:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 5c · p 0.077 (adj 0.0703) · $1.39 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 11c · p 0.1509 (adj 0.1382) · $1.89 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3146 (adj 0.2997) · $2.78 · thesis NSH:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.138 (adj 0.1248) · $1.61 · thesis TOR:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1094 (adj 0.1008) · $1.37 · thesis NYR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 11c · p 0.1356 (adj 0.128) · $1.04 · thesis TOR:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 26c · p 0.3215 (adj 0.2858) · $1.42 · thesis NYR:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.2012 (adj 0.1896) · $2.13 · thesis OTT:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 56c · p 0.7065 (adj 0.6015) · $5.95 · thesis OTT:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 39c · p 0.5665 (adj 0.4304) · $3.08 · thesis SJS:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.7687 (adj 0.7244) · $5.97 · thesis SJS:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2109 (adj 0.1882) · $4.17 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 17c · p 0.2217 (adj 0.2075) · $2.51 · thesis ANA:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.67 (adj 0.6525) · $5.6 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 72c · p 0.7612 (adj 0.7496) · $4.84 · thesis NJD:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1935 (adj 0.1739) · $3.18 · thesis PIT:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.718 (adj 0.6935) · $6.96 · thesis FLA:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1487 (adj 0.1328) · $2.27 · thesis PIT:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 10c · p 0.1388 (adj 0.1266) · $1.88 · thesis FLA:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2473 (adj 0.2367) · $1.64 · thesis NYI:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 55c · p 0.6188 (adj 0.5819) · $3.01 · thesis LAK:SUPPRESSED
- Trevor Connelly: 1+ goals NO @ 78c · p 0.8186 (adj 0.8077) · $6.02 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 73c · p 0.7692 (adj 0.7581) · $4.42 · thesis VGK:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 23c · p 0.2698 (adj 0.2549) · $1.35 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3162 (adj 0.3059) · $1.38 · thesis STL:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 86c · p 0.8976 (adj 0.8857) · $5.78 · thesis DAL:SUPPRESSED
- Gabriel Vilardi: 1+ goals YES @ 22c · p 0.2655 (adj 0.2529) · $2.27 · thesis WPG:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 66c · p 0.7111 (adj 0.6971) · $4.66 · thesis DAL:SUPPRESSED
- Mark Scheifele: 1+ goals YES @ 27c · p 0.3042 (adj 0.2944) · $1.27 · thesis WPG:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 16c · p 0.2214 (adj 0.2048) · $3.04 · thesis CGY:OFFENSE_4PLUS
- Kirill Kaprizov: 2+ goals NO @ 87c · p 0.9142 (adj 0.8994) · $6.32 · thesis MIN:SUPPRESSED
- Minnesota over 3.5 goals scored NO @ 50c · p 0.5896 (adj 0.5423) · $3.73 · thesis MIN:SUPPRESSED
- Jesper Wallstedt: 23+ saves YES @ 57c · p 0.6543 (adj 0.6072) · $4.31 · thesis MIN:NET_HIGH_VOLUME
- Alex Formenton: 1+ goals YES @ 12c · p 0.1854 (adj 0.1666) · $3.35 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.111 (adj 0.0983) · $1.82 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 24c · p 0.2899 (adj 0.2762) · $2.4 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 79c · p 0.8562 (adj 0.8206) · $5.99 · thesis EDM:WINS
- Shane Wright: 1+ goals YES @ 14c · p 0.2053 (adj 0.1877) · $3.6 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1362 (adj 0.1259) · $1.66 · thesis SEA:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ goals YES @ 17c · p 0.2181 (adj 0.2023) · $2.26 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1508 (adj 0.1418) · $1.35 · thesis SEA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2701 (adj 0.2463) · $4.21 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2593 (adj 0.2407) · $3.73 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 12c · p 0.1767 (adj 0.1575) · $2.5 · thesis VAN:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7198 (adj 0.7048) · $5.38 · thesis DET:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 175/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (CONFIRMED) exp shots 27.6, exp saves 23.97 (sd 6.59), pull risk 0.062
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.21 (sd 6.77), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| James Hagens: 1+ points | 0.362 | 0.220 | 38/94 | -0.034 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.389 | 0.515 | 52/49 | +0.103 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.445 | 45/56 | +0.088 | STANDARD |
| Marat Khusnutdinov: 1+ assists | 0.249 | 0.140 | 19/91 | +0.048 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.326 | 0.220 | 25/81 | +0.063 | STANDARD |
| Hampus Lindholm: 1+ points | 0.380 | 0.275 | 30/75 | +0.065 | STANDARD |

**NYR @ TOR** · priced 180/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.12 (sd 6.56), pull risk 0.063
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.92, exp saves 23.17 (sd 6.49), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colton Sissons: 1+ points | 0.332 | 0.140 | 27/99 | +0.048 | STANDARD |
| Tye Kartye: 1+ assists | 0.266 | 0.135 | 26/99 | -0.008 | STANDARD |
| Colton Sissons: 1+ assists | 0.227 | 0.115 | 22/99 | -0.005 | STANDARD |
| Dylan Garand: 26+ saves | 0.345 | 0.455 | 47/56 | +0.078 |  |
| Pavel Dorofeyev: 1+ assists | 0.240 | 0.320 | 34/70 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.463 | 0.540 | 56/48 | +0.040 | STANDARD |

**SJS @ OTT** · priced 213/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 24.89, exp saves 21.62 (sd 6.12), pull risk 0.061
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.6, exp saves 24.4 (sd 6.77), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tyler Kleven: 1+ points | 0.300 | 0.100 | 19/99 | +0.099 | STANDARD |
| Jordan Spence: 1+ assists | 0.307 | 0.120 | 23/99 | +0.065 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.433 | 0.615 | 62/39 | +0.160 | STANDARD |
| Nick Cousins: 1+ points | 0.295 | 0.115 | 22/99 | +0.063 | STANDARD |
| Tyler Kleven: 1+ assists | 0.256 | 0.080 | 15/99 | +0.097 | STANDARD |
| Jake Sanderson: 1+ assists | 0.293 | 0.455 | 47/56 | +0.129 | STANDARD |

**ANA @ NJD** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (CONFIRMED) exp shots 27.82, exp saves 24.22 (sd 6.56), pull risk 0.06
- ANA net: Ville Husso (CONFIRMED) exp shots 29.59, exp saves 25.34 (sd 6.93), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.197 | 0.395 | 42/63 | +0.156 | STANDARD |
| Luke Evangelista: 1+ points | 0.375 | 0.535 | 54/47 | +0.137 | STANDARD |
| Ville Husso: 28+ saves | 0.366 | 0.505 | 53/52 | +0.096 |  |
| Jack Hughes: 1+ assists | 0.413 | 0.550 | 56/46 | +0.110 | STANDARD |
| Jack Hughes: 2+ points | 0.239 | 0.375 | 39/64 | +0.105 | STANDARD |
| Alex Killorn: 1+ points | 0.462 | 0.345 | 35/66 | +0.096 | STANDARD |

**FLA @ PIT** · priced 223/234 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.42, exp saves 23.07 (sd 6.31), pull risk 0.053
- FLA net: Cooper Black (CONFIRMED) exp shots 27.3, exp saves 23.17 (sd 6.63), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Dewar: 1+ points | 0.390 | 0.120 | 23/99 | +0.148 | STANDARD |
| Kaedan Korczak: 1+ points | 0.290 | 0.105 | 20/99 | +0.078 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.248 | 0.090 | 17/99 | +0.068 | STANDARD |
| Declan Carlile: 1+ points | 0.271 | 0.115 | 20/97 | +0.060 | STANDARD |
| Connor Dewar: 1+ assists | 0.246 | 0.090 | 17/99 | +0.066 | STANDARD |
| Niko Mikkola: 1+ points | 0.254 | 0.115 | 22/99 | +0.022 | STANDARD |

**LAK @ NYI** · priced 154/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.26 (sd 6.35), pull risk 0.05
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.51), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ points | 0.343 | 0.205 | 35/94 | -0.023 | STANDARD |
| Jean-Gabriel Pageau: 1+ assists | 0.250 | 0.120 | 23/99 | +0.008 | STANDARD |
| Trevor Moore: 1+ assists | 0.275 | 0.165 | 23/90 | +0.033 | STANDARD |
| Jean-Gabriel Pageau: 1+ points | 0.382 | 0.295 | 34/75 | +0.026 | STANDARD |
| Artemi Panarin: 1+ assists | 0.381 | 0.455 | 46/55 | +0.051 | STANDARD |
| Erik Haula: 1+ assists | 0.199 | 0.130 | 25/99 | -0.064 | STANDARD |

**VGK @ STL** · priced 210/215 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.81 (sd 6.62), pull risk 0.059
- VGK net: Adin Hill (PROBABLE) exp shots 25.57, exp saves 22.1 (sd 6.17), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pius Suter: 1+ points | 0.339 | 0.155 | 30/99 | +0.025 | STANDARD |
| Brayden McNabb: 1+ points | 0.311 | 0.145 | 27/98 | +0.027 | STANDARD |
| Mitch Marner: 1+ assists | 0.401 | 0.535 | 55/48 | +0.101 | STANDARD |
| Brayden McNabb: 1+ assists | 0.258 | 0.125 | 24/99 | +0.005 | STANDARD |
| Jack Eichel: 1+ assists | 0.428 | 0.560 | 57/45 | +0.104 | STANDARD |
| Dalibor Dvorsky: 1+ points | 0.282 | 0.155 | 29/98 | -0.023 | STANDARD |

**WPG @ DAL** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.58 (sd 5.98), pull risk 0.047
- WPG net: Stuart Skinner (CONFIRMED) exp shots 26.81, exp saves 22.93 (sd 6.47), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.283 | 0.105 | 20/99 | +0.072 | STANDARD |
| Adam Lowry: 1+ points | 0.286 | 0.140 | 27/99 | +0.002 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.244 | 0.100 | 19/99 | +0.044 | STANDARD |
| Dylan Samberg: 1+ assists | 0.231 | 0.100 | 19/99 | +0.030 | STANDARD |
| Jamie Benn: 1+ assists | 0.265 | 0.135 | 26/99 | -0.009 | STANDARD |
| Arttu Hyry: 1+ points | 0.285 | 0.165 | 28/95 | -0.009 | STANDARD |

**MIN @ CGY** · priced 170/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.26, exp saves 26.04 (sd 7.05), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.91, exp saves 25.15 (sd 6.68), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.233 | 0.355 | 37/66 | +0.091 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.285 | 0.165 | 23/90 | +0.042 | STANDARD |
| Quinn Hughes: 1+ assists | 0.531 | 0.645 | 65/36 | +0.093 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.381 | 0.495 | 50/51 | +0.092 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.274 | 0.385 | 40/63 | +0.080 | STANDARD |
| Quinn Hughes: 1+ points | 0.597 | 0.700 | 71/31 | +0.078 | STANDARD |

**CAR @ EDM** · priced 172/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.06 (sd 7.0), pull risk 0.064
- CAR net: Brandon Bussi (PROBABLE) exp shots 25.41, exp saves 21.63 (sd 6.33), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Carrier: 1+ points | 0.395 | 0.195 | 33/94 | +0.049 | STANDARD |
| William Carrier: 1+ assists | 0.271 | 0.115 | 22/99 | +0.039 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.281 | 0.125 | 24/99 | +0.028 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.290 | 31/73 | +0.097 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.350 | 0.225 | 25/80 | +0.087 | STANDARD |
| Sebastian Aho: 1+ assists | 0.381 | 0.505 | 51/50 | +0.101 | STANDARD |

**UTA @ SEA** · priced 180/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 29.05, exp saves 25.09 (sd 6.72), pull risk 0.064
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anders Lee: 1+ points | 0.385 | 0.250 | 43/93 | -0.062 | STANDARD |
| Clayton Keller: 1+ points | 0.593 | 0.725 | 73/28 | +0.113 | STANDARD |
| Clayton Keller: 2+ points | 0.230 | 0.360 | 37/65 | +0.104 | STANDARD |
| Kailer Yamamoto: 1+ assists | 0.264 | 0.145 | 27/98 | -0.020 | STANDARD |
| Clayton Keller: 1+ assists | 0.447 | 0.565 | 57/44 | +0.096 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.211 | 0.315 | 33/70 | +0.075 | STANDARD |

**DET @ VAN** · priced 172/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.411 | 0.175 | 33/98 | +0.066 | STANDARD |
| Max Sasson: 1+ points | 0.321 | 0.110 | 21/99 | +0.099 | STANDARD |
| Linus Karlsson: 1+ assists | 0.325 | 0.140 | 27/99 | +0.041 | STANDARD |
| Paul Cotter: 1+ points | 0.372 | 0.195 | 33/94 | +0.027 | STANDARD |
| Linus Karlsson: 1+ points | 0.503 | 0.345 | 40/71 | +0.086 | STANDARD |
| Tom Willander: 1+ assists | 0.283 | 0.130 | 25/99 | +0.020 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
