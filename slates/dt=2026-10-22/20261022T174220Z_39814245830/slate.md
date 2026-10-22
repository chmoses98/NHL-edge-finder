# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T17:42:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4711 · contracts joined: 2812 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2512, 'NO_EDGE': 125, 'OK': 175}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 431, 'game_early_goal': 12, 'first_goal': 432, 'game_winner': 24, 'player_goals': 751, 'game_overtime': 12, 'player_points': 570, 'goalie_saves': 16, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-3h | 0.585 | 0.415 | 0.170 | 6.45 | 3.50 | 2.96 | 220 (25/195) | CONFIRMED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-3h | 0.440 | 0.560 | 0.177 | 6.38 | 3.00 | 3.38 | 229 (25/204) | CONFIRMED/CONFIRMED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-3h | 0.558 | 0.442 | 0.167 | 6.61 | 3.50 | 3.11 | 265 (25/240) | PROBABLE/CONFIRMED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-3h | 0.589 | 0.411 | 0.164 | 6.40 | 3.49 | 2.91 | 230 (25/205) | CONFIRMED/CONFIRMED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-3h | 0.527 | 0.473 | 0.173 | 6.71 | 3.45 | 3.27 | 285 (25/260) | CONFIRMED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-3h | 0.577 | 0.423 | 0.186 | 5.81 | 3.13 | 2.67 | 207 (25/182) | CONFIRMED/PROBABLE |
| VGK @ STL | 2026-10-23T00:00:00Z | T-6h | 0.560 | 0.440 | 0.171 | 6.29 | 3.34 | 2.95 | 227 (25/202) | CONFIRMED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-6h | 0.600 | 0.400 | 0.180 | 5.48 | 3.03 | 2.45 | 258 (25/233) | CONFIRMED/PROBABLE |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-6h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 220 (25/195) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-6h | 0.532 | 0.468 | 0.172 | 6.54 | 3.37 | 3.17 | 224 (25/199) | CONFIRMED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-6h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-6h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 222 (25/197) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.377 | 0.490 | 0.467 | 50 | 52 | no | +0.086 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.560 | 0.455 | 0.476 | 46 | 55 | yes | +0.083 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.440 | 0.545 | 0.524 | 55 | 46 | no | +0.083 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.595 | 0.700 | 0.680 | 71 | 31 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.186 | 0.290 | 0.267 | 30 | 72 | no | +0.080 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.635 | 0.617 | 64 | 37 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.341 | 0.255 | 0.271 | 26 | 75 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.238 | 0.325 | 0.306 | 33 | 68 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.672 | 0.755 | 0.740 | 76 | 25 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.136 | 0.215 | 0.197 | 22 | 79 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.423 | 0.505 | 0.489 | 51 | 50 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.577 | 0.495 | 0.511 | 50 | 51 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.219 | 0.295 | 0.279 | 30 | 71 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.411 | 0.335 | 0.350 | 34 | 67 | yes | +0.056 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.589 | 0.665 | 0.650 | 67 | 34 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.875 | 0.863 | 88 | 13 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.439 | 0.360 | 0.375 | 37 | 65 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.175 | 0.187 | 18 | 83 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.251 | 0.185 | 0.197 | 19 | 82 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.656 | 0.580 | 0.596 | 59 | 43 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.374 | 0.450 | 0.434 | 46 | 56 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.237 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.474 | 0.545 | 0.531 | 55 | 46 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.113 | 0.175 | 0.161 | 18 | 83 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.598 | 0.670 | 0.656 | 68 | 34 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.507 | 0.575 | 0.562 | 58 | 43 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.289 | 0.355 | 0.341 | 36 | 65 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.395 | 0.381 | 40 | 61 | no | +0.044 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.468 | 0.535 | 0.522 | 54 | 47 | no | +0.044 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.572 | 0.635 | 0.623 | 64 | 37 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.215 | 0.280 | 0.266 | 29 | 73 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.686 | 0.745 | 0.734 | 75 | 26 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.565 | 0.553 | 57 | 44 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.780 | 0.835 | 0.825 | 84 | 17 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI3 | team_total | 0.617 | 0.550 | 0.564 | 56 | 46 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.190 | 0.260 | 0.245 | 28 | 76 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.477 | 0.535 | 0.523 | 54 | 47 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT22LANYI-NYI2 | game_spread | 0.340 | 0.285 | 0.296 | 29 | 72 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.135 | 0.190 | 0.178 | 20 | 82 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.445 | 0.434 | 45 | 56 | no | +0.034 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.137 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.157 | 0.210 | 0.199 | 22 | 80 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.505 | 0.494 | 51 | 50 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.265 | 0.315 | 0.305 | 32 | 69 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK5 | team_total | 0.180 | 0.230 | 0.219 | 24 | 78 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.355 | 0.405 | 0.395 | 41 | 60 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY3 | game_spread | 0.134 | 0.095 | 0.102 | 10 | 91 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.855 | 0.846 | 87 | 16 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK2 | team_total | 0.783 | 0.835 | 0.826 | 85 | 18 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.732 | 0.775 | 0.767 | 78 | 23 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.087 | 0.130 | 0.120 | 14 | 88 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-8 | game_total | 0.164 | 0.205 | 0.196 | 21 | 80 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-9 | game_total | 0.215 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-8 | game_total | 0.298 | 0.255 | 0.263 | 26 | 75 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22ANANJ-5 | game_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.359 | 0.405 | 0.396 | 41 | 60 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.330 | 0.380 | 0.370 | 39 | 63 | no | +0.024 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.600 | 0.645 | 0.636 | 65 | 36 | no | +0.024 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.400 | 0.355 | 0.364 | 36 | 65 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT22SJOTT-8 | game_total | 0.318 | 0.275 | 0.283 | 28 | 73 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL6 | team_total | 0.119 | 0.080 | 0.087 | 9 | 93 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.340 | 0.350 | 35 | 67 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-9 | game_total | 0.108 | 0.145 | 0.137 | 15 | 86 | no | +0.023 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.585 | 0.571 | 0.170 | 0.208 | 6.45 | 6.59 | 0.999/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH4 +0.029 |
| NYR @ TOR | 0.440 | 0.509 | 0.177 | 0.218 | 6.38 | 6.34 | 0.988/0.988 | KXNHLGAME-26OCT22NYRTOR-TOR +0.068 |
| SJS @ OTT | 0.558 | 0.558 | 0.167 | 0.214 | 6.61 | 6.36 | 1.061/1.039 | KXNHLTOTAL-26OCT22SJOTT-6 -0.046 |
| ANA @ NJD | 0.589 | 0.541 | 0.164 | 0.213 | 6.40 | 6.45 | 0.996/1.043 | KXNHLSPREAD-26OCT22ANANJ-NJ2 -0.049 |
| FLA @ PIT | 0.527 | 0.589 | 0.173 | 0.212 | 6.71 | 6.57 | 1.042/1.001 | KXNHLGAME-26OCT22FLAPIT-FLA -0.062 |
| LAK @ NYI | 0.577 | 0.534 | 0.186 | 0.226 | 5.81 | 5.96 | 0.978/0.994 | KXNHLTEAMTOTAL-26OCT22LANYI-LA4 +0.049 |
| VGK @ STL | 0.560 | 0.503 | 0.171 | 0.222 | 6.29 | 6.28 | 0.977/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.062 |
| WPG @ DAL | 0.600 | 0.576 | 0.180 | 0.220 | 5.48 | 6.00 | 0.994/0.996 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.090 |
| MIN @ CGY | 0.457 | 0.449 | 0.186 | 0.221 | 5.85 | 6.11 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.052 |
| CAR @ EDM | 0.532 | 0.564 | 0.172 | 0.210 | 6.54 | 6.75 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.051 |
| UTA @ SEA | 0.456 | 0.499 | 0.170 | 0.215 | 6.51 | 6.50 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-UTA -0.044 |
| DET @ VAN | 0.450 | 0.532 | 0.176 | 0.218 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3146 (adj 0.2984) · $2.94 · thesis NSH:OFFENSE_4PLUS
- Matthew Wood: 1+ goals YES @ 16c · p 0.202 (adj 0.1903) · $2.18 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 12c · p 0.1509 (adj 0.1407) · $1.2 · thesis NSH:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.6592 (adj 0.6444) · $4.33 · thesis BOS:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.138 (adj 0.1248) · $1.68 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 11c · p 0.1356 (adj 0.128) · $1.05 · thesis TOR:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 55c · p 0.7139 (adj 0.6009) · $7.32 · thesis OTT:SUPPRESSED
- Ridly Greig: 1+ goals YES @ 16c · p 0.197 (adj 0.1865) · $1.98 · thesis OTT:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 67c · p 0.7767 (adj 0.7041) · $5.78 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 43c · p 0.5755 (adj 0.4626) · $2.27 · thesis SJS:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.209 (adj 0.1867) · $4.59 · thesis ANA:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 62c · p 0.8028 (adj 0.6742) · $6.69 · thesis NJD:SUPPRESSED
- Sam Colangelo: 1+ goals YES @ 12c · p 0.1541 (adj 0.1443) · $1.63 · thesis ANA:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 62c · p 0.67 (adj 0.6562) · $4.3 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.7098 (adj 0.6886) · $7.32 · thesis FLA:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 14c · p 0.1931 (adj 0.1761) · $2.71 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 11c · p 0.1518 (adj 0.1376) · $1.91 · thesis PIT:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 10c · p 0.136 (adj 0.1245) · $1.77 · thesis FLA:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.8327 (adj 0.6912) · $7.32 · thesis LAK:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2473 (adj 0.2367) · $1.74 · thesis NYI:OFFENSE_4PLUS
- Scott Laughton: 1+ goals YES @ 13c · p 0.1596 (adj 0.1497) · $1.27 · thesis LAK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 73c · p 0.7764 (adj 0.7635) · $7.26 · thesis VGK:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3221 (adj 0.3103) · $2.03 · thesis STL:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 66c · p 0.7163 (adj 0.6997) · $6.49 · thesis DAL:SUPPRESSED
- Gabriel Vilardi: 1+ goals YES @ 22c · p 0.2611 (adj 0.2483) · $1.72 · thesis WPG:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7719 (adj 0.7385) · $2.45 · thesis GAME:TIGHT
- Mark Scheifele: 1+ goals YES @ 27c · p 0.307 (adj 0.2965) · $1.41 · thesis WPG:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 52c · p 0.6127 (adj 0.5883) · $7.32 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6804 (adj 0.6327) · $2.99 · thesis CGY:WINS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1348 (adj 0.1224) · $1.4 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2061 (adj 0.1946) · $1.39 · thesis CGY:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 7c · p 0.1164 (adj 0.1036) · $2.38 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1803 (adj 0.1652) · $2.51 · thesis EDM:OFFENSE_4PLUS
- Logan Stankoven: 1+ goals YES @ 26c · p 0.3151 (adj 0.3001) · $3.77 · thesis CAR:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 69c · p 0.7659 (adj 0.7255) · $6.38 · thesis EDM:WINS
- Shane Wright: 1+ goals YES @ 14c · p 0.2009 (adj 0.1844) · $3.54 · thesis SEA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.7021 (adj 0.6841) · $7.32 · thesis UTA:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1544 (adj 0.1446) · $1.71 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 16c · p 0.198 (adj 0.186) · $1.66 · thesis SEA:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 11c · p 0.1771 (adj 0.1566) · $3.48 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1648 (adj 0.1511) · $2.13 · thesis VAN:OFFENSE_4PLUS
- Detroit wins by over 2.5 goals NO @ 74c · p 0.8499 (adj 0.7752) · $6.6 · thesis VAN:WINS
- Jake DeBrusk: 1+ goals YES @ 28c · p 0.3247 (adj 0.3123) · $2.07 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 164/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (CONFIRMED) exp shots 27.6, exp saves 23.97 (sd 6.59), pull risk 0.062
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.21 (sd 6.77), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.389 | 0.505 | 52/51 | +0.083 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.445 | 45/56 | +0.088 | STANDARD |
| Marat Khusnutdinov: 1+ assists | 0.249 | 0.140 | 19/91 | +0.048 | STANDARD |
| Charlie McAvoy: 1+ points | 0.476 | 0.570 | 58/44 | +0.067 | STANDARD |
| Marat Khusnutdinov: 1+ points | 0.367 | 0.285 | 30/73 | +0.052 | STANDARD |
| David Pastrnak: 2+ points | 0.303 | 0.385 | 40/63 | +0.050 | STANDARD |

**NYR @ TOR** · priced 173/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.12 (sd 6.56), pull risk 0.063
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.92, exp saves 23.17 (sd 6.49), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ points | 0.463 | 0.545 | 56/47 | +0.050 | STANDARD |
| Gabe Perreault: 1+ assists | 0.322 | 0.240 | 26/78 | +0.048 | STANDARD |
| Dylan Garand: 26+ saves | 0.345 | 0.425 | 47/62 | +0.019 |  |
| Pavel Dorofeyev: 1+ assists | 0.240 | 0.315 | 33/70 | +0.045 | STANDARD |
| Nick Paul: 1+ assists | 0.248 | 0.175 | 24/89 | -0.005 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.127 | 0.195 | 21/82 | +0.043 | STANDARD |

**SJS @ OTT** · priced 213/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROBABLE) exp shots 24.89, exp saves 21.66 (sd 6.08), pull risk 0.055
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.6, exp saves 24.41 (sd 6.73), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ assists | 0.311 | 0.130 | 25/99 | +0.048 | STANDARD |
| Tyler Kleven: 1+ assists | 0.257 | 0.080 | 15/99 | +0.098 | STANDARD |
| Jake Sanderson: 1+ assists | 0.286 | 0.460 | 47/55 | +0.147 | STANDARD |
| Tyler Kleven: 1+ points | 0.302 | 0.140 | 21/93 | +0.080 | STANDARD |
| Nick Cousins: 1+ points | 0.301 | 0.140 | 21/93 | +0.080 | STANDARD |
| Sam Dickinson: 1+ points | 0.261 | 0.100 | 19/99 | +0.060 | STANDARD |

**ANA @ NJD** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (CONFIRMED) exp shots 27.82, exp saves 24.22 (sd 6.56), pull risk 0.06
- ANA net: Ville Husso (CONFIRMED) exp shots 29.59, exp saves 25.34 (sd 6.93), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.197 | 0.395 | 41/62 | +0.166 | STANDARD |
| Luke Evangelista: 1+ points | 0.375 | 0.535 | 55/48 | +0.127 | STANDARD |
| Jack Hughes: 1+ assists | 0.413 | 0.555 | 57/46 | +0.110 | STANDARD |
| Jack Hughes: 2+ points | 0.239 | 0.370 | 38/64 | +0.105 | STANDARD |
| Ville Husso: 28+ saves | 0.366 | 0.495 | 53/54 | +0.076 |  |
| Jesper Bratt: 1+ assists | 0.394 | 0.500 | 51/51 | +0.079 | STANDARD |

**FLA @ PIT** · priced 229/234 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.42, exp saves 23.06 (sd 6.31), pull risk 0.056
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.15 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cooper Black: 25+ saves | 0.416 | 0.670 | 97/63 | -0.062 |  |
| Connor Dewar: 1+ points | 0.389 | 0.140 | 25/97 | +0.126 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.253 | 0.095 | 18/99 | +0.063 | STANDARD |
| Connor Dewar: 1+ assists | 0.243 | 0.090 | 17/99 | +0.063 | STANDARD |
| Niko Mikkola: 1+ points | 0.258 | 0.115 | 22/99 | +0.026 | STANDARD |
| Kaedan Korczak: 1+ points | 0.296 | 0.160 | 22/90 | +0.064 | STANDARD |

**LAK @ NYI** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.26 (sd 6.35), pull risk 0.05
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.51), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.167 | 0.385 | 41/64 | +0.177 | STANDARD |
| Mats Zuccarello: 1+ points | 0.340 | 0.510 | 53/51 | +0.132 | STANDARD |
| Trevor Moore: 1+ assists | 0.286 | 0.165 | 23/90 | +0.044 | STANDARD |
| Trevor Moore: 1+ points | 0.437 | 0.365 | 39/66 | +0.030 | STANDARD |
| Artemi Panarin: 1+ assists | 0.388 | 0.460 | 47/55 | +0.044 | STANDARD |
| Mats Zuccarello: 2+ points | 0.069 | 0.135 | 19/92 | +0.006 | STANDARD |

**VGK @ STL** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.81 (sd 6.5), pull risk 0.061
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.08 (sd 6.22), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adin Hill: 23+ saves | 0.466 | 0.330 | 51/85 | -0.061 |  |
| Jack Eichel: 1+ assists | 0.432 | 0.555 | 57/46 | +0.091 | STANDARD |
| Mitch Marner: 1+ assists | 0.411 | 0.530 | 54/48 | +0.092 | STANDARD |
| Jack Eichel: 2+ points | 0.232 | 0.335 | 36/69 | +0.063 | STANDARD |
| Mark Stone: 1+ assists | 0.380 | 0.480 | 49/53 | +0.073 | STANDARD |
| Mitch Marner: 1+ points | 0.543 | 0.640 | 65/37 | +0.070 | STANDARD |

**WPG @ DAL** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.6 (sd 6.04), pull risk 0.043
- WPG net: Stuart Skinner (PROBABLE) exp shots 26.81, exp saves 22.9 (sd 6.51), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Lowry: 2+ points | 0.048 | 0.495 | 98/99 | -0.039 | STANDARD |
| Nils Lundkvist: 1+ points | 0.276 | 0.115 | 22/99 | +0.044 | STANDARD |
| Adam Lowry: 1+ points | 0.289 | 0.140 | 27/99 | +0.005 | STANDARD |
| Dylan Samberg: 1+ points | 0.262 | 0.125 | 22/97 | +0.029 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.236 | 0.100 | 19/99 | +0.035 | STANDARD |
| Jamie Benn: 1+ assists | 0.268 | 0.140 | 27/99 | -0.016 | STANDARD |

**MIN @ CGY** · priced 168/169 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.04 (sd 7.01), pull risk 0.067
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.13 (sd 6.71), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.242 | 0.350 | 36/66 | +0.082 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.268 | 0.165 | 23/90 | +0.025 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.284 | 0.385 | 40/63 | +0.069 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.387 | 0.485 | 49/52 | +0.075 | STANDARD |
| Quinn Hughes: 1+ assists | 0.551 | 0.645 | 66/37 | +0.063 | STANDARD |
| Quinn Hughes: 2+ assists | 0.184 | 0.270 | 29/75 | +0.053 | STANDARD |

**CAR @ EDM** · priced 160/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 29.98, exp saves 26.07 (sd 6.84), pull risk 0.062
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.69 (sd 6.22), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.425 | 0.295 | 31/72 | +0.100 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.354 | 0.230 | 26/80 | +0.080 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.459 | 0.580 | 59/43 | +0.094 | STANDARD |
| Sebastian Aho: 1+ assists | 0.385 | 0.500 | 51/51 | +0.088 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.383 | 0.280 | 30/74 | +0.068 | STANDARD |
| Sebastian Aho: 2+ points | 0.208 | 0.295 | 32/73 | +0.048 | STANDARD |

**UTA @ SEA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 2+ points | 0.224 | 0.355 | 38/67 | +0.091 | STANDARD |
| Clayton Keller: 1+ points | 0.590 | 0.720 | 73/29 | +0.106 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.555 | 57/46 | +0.080 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.209 | 0.310 | 33/71 | +0.067 | STANDARD |
| Vincent Trocheck: 1+ points | 0.354 | 0.450 | 48/58 | +0.049 | STANDARD |
| Logan Cooley: 1+ assists | 0.336 | 0.420 | 44/60 | +0.047 | STANDARD |

**DET @ VAN** · priced 148/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Michael Rasmussen: 2+ points | 0.051 | 0.490 | 96/98 | -0.033 | STANDARD |
| Sheldon Dries: 1+ points | 0.175 | 0.495 | 98/99 | -0.166 | STANDARD |
| Drew O'Connor: 1+ points | 0.381 | 0.215 | 41/98 | -0.046 | STANDARD |
| Ben Chiarot: 1+ assists | 0.259 | 0.115 | 22/99 | +0.027 | STANDARD |
| Ben Chiarot: 1+ points | 0.295 | 0.165 | 32/99 | -0.040 | STANDARD |
| Linus Karlsson: 1+ goals | 0.259 | 0.145 | 19/90 | +0.058 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
