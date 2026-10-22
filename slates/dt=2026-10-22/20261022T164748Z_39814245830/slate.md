# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T16:47:48Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4644 · contracts joined: 2745 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2445, 'NO_EDGE': 128, 'OK': 172}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 405, 'game_early_goal': 12, 'first_goal': 431, 'game_winner': 24, 'player_goals': 750, 'game_overtime': 12, 'player_points': 538, 'goalie_saves': 9, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-6h | 0.585 | 0.415 | 0.170 | 6.45 | 3.50 | 2.96 | 220 (25/195) | CONFIRMED/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-6h | 0.440 | 0.560 | 0.177 | 6.38 | 3.00 | 3.38 | 229 (25/204) | CONFIRMED/CONFIRMED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-6h | 0.570 | 0.430 | 0.167 | 6.53 | 3.50 | 3.04 | 234 (25/209) | PROJECTED/CONFIRMED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-6h | 0.574 | 0.426 | 0.177 | 6.35 | 3.42 | 2.93 | 230 (25/205) | CONFIRMED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-6h | 0.527 | 0.473 | 0.173 | 6.71 | 3.45 | 3.27 | 274 (25/249) | CONFIRMED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-6h | 0.577 | 0.423 | 0.186 | 5.81 | 3.13 | 2.67 | 207 (25/182) | CONFIRMED/PROBABLE |
| VGK @ STL | 2026-10-23T00:00:00Z | T-6h | 0.560 | 0.440 | 0.171 | 6.29 | 3.34 | 2.95 | 225 (25/200) | CONFIRMED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-6h | 0.592 | 0.408 | 0.180 | 5.55 | 3.05 | 2.50 | 256 (25/231) | PROJECTED/PROJECTED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-6h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 220 (25/195) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-6h | 0.529 | 0.471 | 0.170 | 6.54 | 3.37 | 3.17 | 221 (25/196) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-6h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-6h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 204 (25/179) | PROJECTED/PROJECTED |

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
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.574 | 0.665 | 0.648 | 67 | 34 | no | +0.070 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.426 | 0.335 | 0.352 | 34 | 67 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.341 | 0.255 | 0.271 | 26 | 75 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.238 | 0.325 | 0.306 | 33 | 68 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.229 | 0.315 | 0.296 | 32 | 69 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.460 | 0.545 | 0.528 | 55 | 46 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.423 | 0.505 | 0.489 | 51 | 50 | no | +0.059 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.577 | 0.495 | 0.511 | 50 | 51 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.265 | 0.350 | 0.332 | 36 | 66 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.356 | 0.435 | 0.419 | 44 | 57 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.682 | 0.755 | 0.741 | 76 | 25 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.875 | 0.863 | 88 | 13 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.674 | 0.745 | 0.732 | 75 | 26 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.136 | 0.210 | 0.193 | 22 | 80 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.170 | 0.183 | 18 | 84 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.656 | 0.580 | 0.596 | 59 | 43 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.113 | 0.175 | 0.161 | 18 | 83 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.377 | 0.450 | 0.435 | 46 | 56 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.507 | 0.575 | 0.562 | 58 | 43 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.289 | 0.355 | 0.341 | 36 | 65 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.395 | 0.381 | 40 | 61 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.455 | 0.442 | 46 | 55 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.127 | 0.195 | 0.179 | 21 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.602 | 0.670 | 0.657 | 68 | 34 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.439 | 0.365 | 0.379 | 38 | 65 | yes | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.215 | 0.280 | 0.266 | 29 | 73 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.565 | 0.553 | 57 | 44 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.251 | 0.185 | 0.197 | 20 | 83 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-NYI3 | team_total | 0.617 | 0.550 | 0.564 | 56 | 46 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.477 | 0.535 | 0.523 | 54 | 47 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT22ANANJ-6 | game_total | 0.588 | 0.645 | 0.634 | 65 | 36 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT22LANYI-NYI2 | game_spread | 0.340 | 0.285 | 0.296 | 29 | 72 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.193 | 0.260 | 0.245 | 28 | 76 | no | +0.035 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.137 | 0.185 | 0.175 | 19 | 82 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.572 | 0.625 | 0.615 | 63 | 38 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.592 | 0.645 | 0.635 | 65 | 36 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.408 | 0.355 | 0.365 | 36 | 65 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.789 | 0.835 | 0.826 | 84 | 17 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.505 | 0.494 | 51 | 50 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT22ANANJ-5 | game_total | 0.790 | 0.835 | 0.827 | 84 | 17 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.840 | 0.790 | 0.801 | 80 | 22 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.606 | 0.555 | 0.565 | 56 | 45 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ2 | team_total | 0.855 | 0.900 | 0.892 | 91 | 11 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.355 | 0.405 | 0.395 | 41 | 60 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK5 | team_total | 0.180 | 0.230 | 0.219 | 24 | 78 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.355 | 0.405 | 0.395 | 41 | 60 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK2 | team_total | 0.783 | 0.830 | 0.821 | 84 | 18 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22MINCGY-5 | game_total | 0.732 | 0.775 | 0.767 | 78 | 23 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.087 | 0.135 | 0.124 | 15 | 88 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-9 | game_total | 0.215 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-8 | game_total | 0.298 | 0.255 | 0.263 | 26 | 75 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.260 | 0.250 | 27 | 75 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22CAREDM-CAR4 | team_total | 0.398 | 0.450 | 0.440 | 46 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.340 | 0.350 | 35 | 67 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.450 | 0.495 | 0.486 | 50 | 51 | no | +0.023 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT22ANANJ-ANA2 | game_spread | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.023 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.585 | 0.571 | 0.170 | 0.208 | 6.45 | 6.59 | 0.999/1.000 | KXNHLTEAMTOTAL-26OCT22NSHBOS-NSH4 +0.029 |
| NYR @ TOR | 0.440 | 0.509 | 0.177 | 0.218 | 6.38 | 6.34 | 0.988/0.988 | KXNHLGAME-26OCT22NYRTOR-TOR +0.068 |
| SJS @ OTT | 0.570 | 0.569 | 0.167 | 0.215 | 6.53 | 6.32 | 1.041/1.039 | KXNHLTOTAL-26OCT22SJOTT-8 -0.039 |
| ANA @ NJD | 0.574 | 0.536 | 0.177 | 0.217 | 6.35 | 6.41 | 0.996/1.024 | KXNHLSPREAD-26OCT22ANANJ-NJ2 -0.042 |
| FLA @ PIT | 0.527 | 0.589 | 0.173 | 0.212 | 6.71 | 6.57 | 1.042/1.001 | KXNHLGAME-26OCT22FLAPIT-FLA -0.062 |
| LAK @ NYI | 0.577 | 0.534 | 0.186 | 0.226 | 5.81 | 5.96 | 0.978/0.994 | KXNHLTEAMTOTAL-26OCT22LANYI-LA4 +0.049 |
| VGK @ STL | 0.560 | 0.503 | 0.171 | 0.222 | 6.29 | 6.28 | 0.977/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.062 |
| WPG @ DAL | 0.592 | 0.575 | 0.180 | 0.214 | 5.55 | 5.95 | 0.986/0.988 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.072 |
| MIN @ CGY | 0.457 | 0.449 | 0.186 | 0.221 | 5.85 | 6.11 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.052 |
| CAR @ EDM | 0.529 | 0.567 | 0.170 | 0.215 | 6.54 | 6.74 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.052 |
| UTA @ SEA | 0.456 | 0.499 | 0.170 | 0.215 | 6.51 | 6.50 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-UTA -0.044 |
| DET @ VAN | 0.450 | 0.532 | 0.176 | 0.218 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.3146 (adj 0.2984) · $2.94 · thesis NSH:OFFENSE_4PLUS
- Matthew Wood: 1+ goals YES @ 16c · p 0.202 (adj 0.1903) · $2.13 · thesis NSH:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.6592 (adj 0.6444) · $4.21 · thesis BOS:SUPPRESSED
- Casey Mittelstadt: 1+ goals YES @ 15c · p 0.1919 (adj 0.1714) · $1.15 · thesis BOS:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.138 (adj 0.1223) · $1.43 · thesis TOR:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 25c · p 0.3215 (adj 0.2757) · $1.43 · thesis NYR:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 54c · p 0.71 (adj 0.5962) · $7.15 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 15c · p 0.1833 (adj 0.1737) · $1.58 · thesis OTT:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 67c · p 0.7757 (adj 0.7037) · $5.86 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 71c · p 0.7702 (adj 0.7351) · $3.33 · thesis SJS:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2099 (adj 0.1874) · $4.51 · thesis ANA:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 63c · p 0.7996 (adj 0.6764) · $6.18 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 62c · p 0.6752 (adj 0.6602) · $4.57 · thesis NJD:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 14c · p 0.1931 (adj 0.1736) · $2.3 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 11c · p 0.1518 (adj 0.1363) · $1.72 · thesis PIT:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6896 (adj 0.6722) · $5.19 · thesis FLA:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 67c · p 0.727 (adj 0.7103) · $5.57 · thesis FLA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.8327 (adj 0.6912) · $7.17 · thesis LAK:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2473 (adj 0.2367) · $1.71 · thesis NYI:OFFENSE_4PLUS
- Scott Laughton: 1+ goals YES @ 13c · p 0.1596 (adj 0.1497) · $1.24 · thesis LAK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 73c · p 0.7764 (adj 0.7635) · $7.11 · thesis VGK:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3221 (adj 0.3091) · $1.83 · thesis STL:OFFENSE_4PLUS
- Gabriel Vilardi: 1+ goals YES @ 21c · p 0.2645 (adj 0.2484) · $2.72 · thesis WPG:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7756 (adj 0.7403) · $3.33 · thesis GAME:TIGHT
- Mikko Rantanen: 1+ goals NO @ 67c · p 0.7171 (adj 0.7016) · $4.37 · thesis DAL:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 53c · p 0.6127 (adj 0.5908) · $7.17 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6804 (adj 0.6327) · $3.06 · thesis CGY:WINS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1348 (adj 0.1199) · $1.12 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2061 (adj 0.1946) · $1.36 · thesis CGY:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 25c · p 0.3098 (adj 0.2936) · $3.41 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1194 (adj 0.1033) · $1.46 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 15c · p 0.1832 (adj 0.1724) · $1.3 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 80c · p 0.8552 (adj 0.8251) · $4.35 · thesis EDM:WINS
- Shane Wright: 1+ goals YES @ 14c · p 0.2009 (adj 0.1844) · $3.23 · thesis SEA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 11c · p 0.1484 (adj 0.1376) · $2.19 · thesis UTA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.7021 (adj 0.6841) · $6.46 · thesis UTA:SUPPRESSED
- Utah wins by over 1.5 goals NO @ 61c · p 0.7049 (adj 0.6549) · $6.05 · thesis SEA:WINS
- Liam Ohgren: 1+ goals YES @ 11c · p 0.1771 (adj 0.1553) · $3.36 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2699 (adj 0.2474) · $4.8 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1648 (adj 0.1511) · $2.17 · thesis VAN:OFFENSE_4PLUS
- Detroit over 5.5 goals scored NO @ 87c · p 0.9196 (adj 0.8923) · $7.17 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 164/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (CONFIRMED) exp shots 27.6, exp saves 23.97 (sd 6.59), pull risk 0.062
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.21 (sd 6.77), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.389 | 0.510 | 52/50 | +0.093 | STANDARD |
| Marat Khusnutdinov: 1+ assists | 0.249 | 0.135 | 19/92 | +0.048 | STANDARD |
| Pavel Zacha: 1+ assists | 0.334 | 0.445 | 45/56 | +0.088 | STANDARD |
| Charlie McAvoy: 1+ points | 0.476 | 0.570 | 59/45 | +0.056 | STANDARD |
| Casey Mittelstadt: 1+ goals | 0.192 | 0.110 | 15/93 | +0.033 | STANDARD |
| David Pastrnak: 2+ points | 0.303 | 0.385 | 41/64 | +0.040 | STANDARD |

**NYR @ TOR** · priced 173/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.12 (sd 6.56), pull risk 0.063
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.92, exp saves 23.17 (sd 6.49), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gabe Perreault: 1+ assists | 0.322 | 0.230 | 25/79 | +0.058 | STANDARD |
| Gavin McKenna: 1+ points | 0.389 | 0.470 | 48/54 | +0.054 | STANDARD |
| Dylan Garand: 26+ saves | 0.345 | 0.425 | 49/64 | -0.001 |  |
| Pavel Dorofeyev: 1+ points | 0.463 | 0.540 | 56/48 | +0.040 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.240 | 0.315 | 33/70 | +0.045 | STANDARD |
| Nick Paul: 1+ assists | 0.248 | 0.175 | 24/89 | -0.005 | STANDARD |

**SJS @ OTT** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.66 (sd 6.13), pull risk 0.056
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.6, exp saves 24.37 (sd 6.73), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Michael Amadio: 1+ points | 0.391 | 0.180 | 35/99 | +0.025 | STANDARD |
| Jake Sanderson: 1+ assists | 0.290 | 0.465 | 47/54 | +0.153 | STANDARD |
| Nick Cousins: 1+ points | 0.297 | 0.130 | 25/99 | +0.034 | STANDARD |
| Jake Sanderson: 1+ points | 0.381 | 0.530 | 54/48 | +0.122 | STANDARD |
| Michael Amadio: 1+ assists | 0.259 | 0.125 | 24/99 | +0.006 | STANDARD |
| Nick Cousins: 1+ assists | 0.212 | 0.085 | 16/99 | +0.043 | STANDARD |

**ANA @ NJD** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (CONFIRMED) exp shots 27.82, exp saves 24.19 (sd 6.62), pull risk 0.06
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.37 (sd 6.97), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.200 | 0.390 | 41/63 | +0.153 | STANDARD |
| Luke Evangelista: 1+ points | 0.382 | 0.530 | 55/49 | +0.111 | STANDARD |
| Jack Hughes: 1+ assists | 0.411 | 0.550 | 57/47 | +0.102 | STANDARD |
| Jack Hughes: 2+ points | 0.237 | 0.370 | 38/64 | +0.106 | STANDARD |
| Jesper Bratt: 1+ assists | 0.392 | 0.500 | 51/51 | +0.081 | STANDARD |
| Luke Hughes: 1+ points | 0.454 | 0.555 | 56/45 | +0.079 | STANDARD |

**FLA @ PIT** · priced 215/223 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.42, exp saves 23.06 (sd 6.31), pull risk 0.056
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.15 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Dewar: 1+ points | 0.389 | 0.150 | 27/97 | +0.105 | STANDARD |
| Kaedan Korczak: 1+ points | 0.296 | 0.120 | 23/99 | +0.054 | STANDARD |
| Gustav Forsling: 1+ points | 0.347 | 0.180 | 29/93 | +0.042 | STANDARD |
| Gustav Forsling: 1+ assists | 0.289 | 0.130 | 25/99 | +0.026 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.253 | 0.095 | 18/99 | +0.063 | STANDARD |
| Connor Dewar: 1+ assists | 0.243 | 0.095 | 18/99 | +0.052 | STANDARD |

**LAK @ NYI** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.26 (sd 6.35), pull risk 0.05
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.51), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.167 | 0.385 | 41/64 | +0.177 | STANDARD |
| Darcy Kuemper: 24+ saves | 0.521 | 0.340 | 50/82 | +0.004 |  |
| Mats Zuccarello: 1+ points | 0.340 | 0.510 | 53/51 | +0.132 | STANDARD |
| Trevor Moore: 1+ assists | 0.286 | 0.165 | 23/90 | +0.044 | STANDARD |
| Trevor Moore: 1+ points | 0.437 | 0.365 | 39/66 | +0.030 | STANDARD |
| Artemi Panarin: 1+ assists | 0.388 | 0.460 | 47/55 | +0.044 | STANDARD |

**VGK @ STL** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.55, exp saves 23.81 (sd 6.5), pull risk 0.061
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.08 (sd 6.22), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.432 | 0.555 | 57/46 | +0.091 | STANDARD |
| Mitch Marner: 1+ assists | 0.411 | 0.525 | 54/49 | +0.082 | STANDARD |
| Jack Eichel: 2+ points | 0.232 | 0.335 | 35/68 | +0.073 | STANDARD |
| Mark Stone: 1+ assists | 0.380 | 0.480 | 49/53 | +0.073 | STANDARD |
| Mitch Marner: 1+ points | 0.543 | 0.640 | 65/37 | +0.070 | STANDARD |
| Trevor Connelly: 1+ points | 0.364 | 0.450 | 46/56 | +0.059 | STANDARD |

**WPG @ DAL** · priced 204/205 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.55 (sd 5.96), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.93 (sd 6.41), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Iafallo: 1+ points | 0.366 | 0.190 | 36/98 | -0.010 | STANDARD |
| Jamie Benn: 1+ points | 0.383 | 0.220 | 37/93 | -0.003 | STANDARD |
| Nils Lundkvist: 1+ points | 0.276 | 0.115 | 22/99 | +0.044 | STANDARD |
| Dylan Samberg: 1+ points | 0.270 | 0.120 | 23/99 | +0.027 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.238 | 0.100 | 19/99 | +0.037 | STANDARD |
| Adam Lowry: 1+ points | 0.290 | 0.155 | 30/99 | -0.024 | STANDARD |

**MIN @ CGY** · priced 168/169 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.04 (sd 7.01), pull risk 0.067
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.13 (sd 6.71), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.242 | 0.355 | 37/66 | +0.082 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.268 | 0.165 | 23/90 | +0.025 | STANDARD |
| Quinn Hughes: 1+ assists | 0.551 | 0.640 | 66/38 | +0.053 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.387 | 0.475 | 48/53 | +0.065 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.284 | 0.365 | 38/65 | +0.050 | STANDARD |
| Max Shabanov: 1+ points | 0.375 | 0.450 | 48/58 | +0.028 | STANDARD |

**CAR @ EDM** · priced 159/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.08 (sd 6.92), pull risk 0.06
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.63 (sd 6.28), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kasperi Kapanen: 1+ assists | 0.292 | 0.130 | 25/99 | +0.029 | STANDARD |
| Mattias Ekholm: 1+ points | 0.440 | 0.290 | 31/73 | +0.115 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.366 | 0.235 | 26/79 | +0.092 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.411 | 0.290 | 32/74 | +0.075 | STANDARD |
| Sebastian Aho: 1+ assists | 0.384 | 0.500 | 51/51 | +0.089 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.593 | 0.485 | 49/52 | +0.086 | STANDARD |

**UTA @ SEA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 1+ points | 0.590 | 0.715 | 72/29 | +0.106 | STANDARD |
| Clayton Keller: 2+ points | 0.224 | 0.345 | 36/67 | +0.091 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.555 | 57/46 | +0.080 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.209 | 0.320 | 34/70 | +0.077 | STANDARD |
| Logan Cooley: 1+ assists | 0.336 | 0.420 | 44/60 | +0.047 | STANDARD |
| Lawson Crouse: 1+ points | 0.419 | 0.340 | 40/72 | +0.002 | STANDARD |

**DET @ VAN** · priced 130/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ goals | 0.259 | 0.140 | 19/91 | +0.058 | STANDARD |
| Dylan Larkin: 1+ points | 0.531 | 0.635 | 66/39 | +0.063 | STANDARD |
| Dylan Larkin: 1+ assists | 0.348 | 0.440 | 46/58 | +0.055 | STANDARD |
| Filip Chytil: 1+ goals | 0.270 | 0.180 | 19/83 | +0.069 | STANDARD |
| Jake DeBrusk: 1+ points | 0.548 | 0.460 | 47/55 | +0.060 | STANDARD |
| Liam Ohgren: 1+ goals | 0.177 | 0.090 | 11/93 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
