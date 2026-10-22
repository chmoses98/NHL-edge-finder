# NHL slate 2026-10-22 — RESEARCH_ONLY

generated 2026-10-22T14:57:16Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 12 · markets on board: 4505 · contracts joined: 2606 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2306, 'NO_EDGE': 129, 'OK': 171}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 353, 'game_early_goal': 12, 'first_goal': 431, 'game_winner': 24, 'player_goals': 749, 'game_overtime': 12, 'player_points': 461, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 2026-10-22T23:00:00Z | T-6h | 0.586 | 0.414 | 0.167 | 6.46 | 3.50 | 2.96 | 219 (25/194) | PROBABLE/PROJECTED |
| NYR @ TOR | 2026-10-22T23:00:00Z | T-6h | 0.456 | 0.544 | 0.174 | 6.46 | 3.09 | 3.37 | 220 (25/195) | CONFIRMED/PROJECTED |
| SJS @ OTT | 2026-10-22T23:00:00Z | T-6h | 0.558 | 0.442 | 0.172 | 6.45 | 3.42 | 3.04 | 217 (25/192) | PROJECTED/PROJECTED |
| ANA @ NJD | 2026-10-22T23:00:00Z | T-6h | 0.584 | 0.416 | 0.172 | 6.32 | 3.42 | 2.90 | 222 (25/197) | PROJECTED/PROJECTED |
| FLA @ PIT | 2026-10-22T23:00:00Z | T-6h | 0.545 | 0.455 | 0.169 | 6.61 | 3.44 | 3.16 | 232 (25/207) | PROJECTED/PROJECTED |
| LAK @ NYI | 2026-10-22T23:30:00Z | T-6h | 0.551 | 0.449 | 0.184 | 5.61 | 2.94 | 2.67 | 205 (25/180) | CONFIRMED/PROJECTED |
| VGK @ STL | 2026-10-23T00:00:00Z | T-6h | 0.550 | 0.450 | 0.174 | 6.36 | 3.34 | 3.02 | 225 (25/200) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-10-23T00:00:00Z | T-6h | 0.592 | 0.408 | 0.180 | 5.55 | 3.05 | 2.50 | 205 (25/180) | PROJECTED/PROJECTED |
| MIN @ CGY | 2026-10-23T01:00:00Z | T-6h | 0.457 | 0.543 | 0.186 | 5.85 | 2.79 | 3.06 | 218 (25/193) | PROJECTED/PROJECTED |
| CAR @ EDM | 2026-10-23T01:00:00Z | T-6h | 0.529 | 0.471 | 0.170 | 6.54 | 3.37 | 3.17 | 218 (25/193) | PROJECTED/PROJECTED |
| UTA @ SEA | 2026-10-23T02:00:00Z | T-6h | 0.456 | 0.544 | 0.170 | 6.51 | 3.11 | 3.40 | 225 (25/200) | PROJECTED/PROJECTED |
| DET @ VAN | 2026-10-23T02:00:00Z | T-6h | 0.450 | 0.550 | 0.176 | 6.37 | 3.02 | 3.35 | 200 (25/175) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4 | team_total | 0.377 | 0.485 | 0.463 | 49 | 52 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN2 | game_spread | 0.310 | 0.415 | 0.393 | 42 | 59 | no | +0.083 | OK |
| KXNHLGAME-26OCT22MINCGY-CGY | game_winner | 0.457 | 0.355 | 0.375 | 36 | 65 | yes | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN3 | team_total | 0.595 | 0.700 | 0.680 | 71 | 31 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT22MINCGY-MIN3 | game_spread | 0.186 | 0.290 | 0.267 | 30 | 72 | no | +0.080 | OK |
| KXNHLGAME-26OCT22VGKSTL-STL | game_winner | 0.550 | 0.455 | 0.474 | 46 | 55 | yes | +0.073 | OK |
| KXNHLGAME-26OCT22VGKSTL-VGK | game_winner | 0.450 | 0.545 | 0.526 | 55 | 46 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ3 | game_spread | 0.228 | 0.315 | 0.296 | 32 | 69 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL3 | game_spread | 0.214 | 0.295 | 0.277 | 30 | 71 | no | +0.062 | OK |
| KXNHLGAME-26OCT22MINCGY-MIN | game_winner | 0.543 | 0.625 | 0.609 | 63 | 38 | no | +0.061 | OK |
| KXNHLGAME-26OCT22ANANJ-ANA | game_winner | 0.416 | 0.335 | 0.351 | 34 | 67 | yes | +0.061 | OK |
| KXNHLGAME-26OCT22ANANJ-NJ | game_winner | 0.584 | 0.665 | 0.649 | 67 | 34 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK2 | game_spread | 0.245 | 0.325 | 0.308 | 33 | 68 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN5 | team_total | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLGAME-26OCT22UTASEA-SEA | game_winner | 0.456 | 0.375 | 0.391 | 38 | 63 | yes | +0.059 | OK |
| KXNHLGAME-26OCT22UTASEA-UTA | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL2 | game_spread | 0.332 | 0.255 | 0.269 | 26 | 75 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-5 | game_total | 0.682 | 0.755 | 0.741 | 76 | 25 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT22ANANJ-NJ2 | game_spread | 0.361 | 0.435 | 0.420 | 44 | 57 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL5 | team_total | 0.252 | 0.180 | 0.193 | 19 | 83 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT22MINCGY-CGY2 | game_spread | 0.241 | 0.170 | 0.183 | 18 | 84 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4 | team_total | 0.462 | 0.540 | 0.524 | 55 | 47 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL4 | team_total | 0.437 | 0.360 | 0.375 | 37 | 65 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA3 | game_spread | 0.207 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL3 | team_total | 0.655 | 0.580 | 0.596 | 59 | 43 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA4 | team_total | 0.286 | 0.355 | 0.341 | 36 | 65 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL4 | team_total | 0.377 | 0.450 | 0.435 | 46 | 56 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-VGK3 | game_spread | 0.144 | 0.205 | 0.191 | 21 | 80 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT22UTASEA-UTA2 | game_spread | 0.329 | 0.395 | 0.381 | 40 | 61 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL5 | team_total | 0.193 | 0.265 | 0.249 | 28 | 75 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN2 | team_total | 0.807 | 0.870 | 0.859 | 88 | 14 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA3 | team_total | 0.509 | 0.575 | 0.562 | 58 | 43 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ3 | team_total | 0.674 | 0.740 | 0.728 | 75 | 27 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL3 | team_total | 0.602 | 0.670 | 0.657 | 68 | 34 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-CAR | game_winner | 0.471 | 0.535 | 0.522 | 54 | 47 | no | +0.042 | OK |
| KXNHLGAME-26OCT22CAREDM-EDM | game_winner | 0.529 | 0.465 | 0.478 | 47 | 54 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ5 | team_total | 0.266 | 0.330 | 0.317 | 34 | 68 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET3 | game_spread | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-7 | game_total | 0.491 | 0.435 | 0.446 | 44 | 57 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT22MINCGY-7 | game_total | 0.389 | 0.445 | 0.434 | 45 | 56 | no | +0.034 | OK |
| KXNHLGAME-26OCT22LANYI-LA | game_winner | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.034 | OK |
| KXNHLGAME-26OCT22LANYI-NYI | game_winner | 0.551 | 0.495 | 0.506 | 50 | 51 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT22ANANJ-NJ6 | team_total | 0.127 | 0.175 | 0.164 | 18 | 83 | no | +0.034 | OK |
| KXNHLGAME-26OCT22DETVAN-VAN | game_winner | 0.450 | 0.395 | 0.406 | 40 | 61 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-6 | game_total | 0.450 | 0.505 | 0.494 | 51 | 50 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-8 | game_total | 0.295 | 0.245 | 0.255 | 25 | 76 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA3 | game_spread | 0.128 | 0.175 | 0.165 | 18 | 83 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-DAL | game_winner | 0.592 | 0.645 | 0.635 | 65 | 36 | no | +0.032 | OK |
| KXNHLGAME-26OCT22WPGDAL-WPG | game_winner | 0.408 | 0.355 | 0.365 | 36 | 65 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-4 | game_total | 0.789 | 0.835 | 0.826 | 84 | 17 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR2 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK3 | team_total | 0.583 | 0.640 | 0.629 | 65 | 37 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT22CAREDM-CAR3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22LANYI-5 | game_total | 0.696 | 0.745 | 0.736 | 75 | 26 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT22MINCGY-6 | game_total | 0.502 | 0.560 | 0.548 | 57 | 45 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA4 | team_total | 0.452 | 0.505 | 0.494 | 51 | 50 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT22UTASEA-SEA2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT22DETVAN-DET2 | game_spread | 0.333 | 0.385 | 0.374 | 39 | 62 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3 | team_total | 0.606 | 0.555 | 0.565 | 56 | 45 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT22VGKSTL-STL3 | game_spread | 0.208 | 0.160 | 0.169 | 17 | 85 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT22WPGDAL-DAL2 | game_spread | 0.355 | 0.405 | 0.395 | 41 | 60 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY3 | team_total | 0.535 | 0.485 | 0.495 | 49 | 52 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT22WPGDAL-DAL2 | team_total | 0.804 | 0.855 | 0.846 | 87 | 16 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-MIN6 | team_total | 0.087 | 0.130 | 0.120 | 14 | 88 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT22LANYI-7 | game_total | 0.348 | 0.395 | 0.386 | 40 | 61 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT22ANANJ-5 | game_total | 0.785 | 0.825 | 0.818 | 83 | 18 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT22WPGDAL-7 | game_total | 0.339 | 0.390 | 0.380 | 40 | 62 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4 | team_total | 0.389 | 0.340 | 0.350 | 35 | 67 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22LANYI-LA2 | team_total | 0.745 | 0.785 | 0.777 | 79 | 22 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-VGK4 | team_total | 0.370 | 0.415 | 0.406 | 42 | 59 | no | +0.023 | OK |
| KXNHLGAME-26OCT22DETVAN-DET | game_winner | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT22CAREDM-EDM2 | game_spread | 0.316 | 0.275 | 0.283 | 28 | 73 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT22ANANJ-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22DETVAN-DET4 | team_total | 0.441 | 0.490 | 0.480 | 50 | 52 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT22NSHBOS-6 | game_total | 0.598 | 0.555 | 0.564 | 56 | 45 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT22UTASEA-UTA3 | team_total | 0.665 | 0.710 | 0.701 | 72 | 30 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22VGKSTL-STL2 | team_total | 0.841 | 0.800 | 0.809 | 81 | 21 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT22NYRTOR-TOR3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT22LANYI-LA2 | game_spread | 0.236 | 0.280 | 0.271 | 29 | 73 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT22MINCGY-CGY2 | team_total | 0.763 | 0.725 | 0.733 | 73 | 28 | yes | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ BOS | 0.586 | 0.575 | 0.167 | 0.211 | 6.46 | 6.58 | 0.993/1.000 | KXNHLTOTAL-26OCT22NSHBOS-7 +0.026 |
| NYR @ TOR | 0.456 | 0.506 | 0.174 | 0.219 | 6.46 | 6.35 | 0.988/0.992 | KXNHLSPREAD-26OCT22NYRTOR-NYR2 -0.051 |
| SJS @ OTT | 0.558 | 0.567 | 0.172 | 0.214 | 6.45 | 6.29 | 1.041/1.034 | KXNHLTOTAL-26OCT22SJOTT-6 -0.027 |
| ANA @ NJD | 0.584 | 0.534 | 0.172 | 0.215 | 6.32 | 6.40 | 0.992/1.024 | KXNHLGAME-26OCT22ANANJ-ANA +0.049 |
| FLA @ PIT | 0.545 | 0.594 | 0.169 | 0.212 | 6.61 | 6.53 | 1.021/1.001 | KXNHLGAME-26OCT22FLAPIT-FLA -0.049 |
| LAK @ NYI | 0.551 | 0.531 | 0.184 | 0.224 | 5.61 | 5.94 | 0.978/0.989 | KXNHLTOTAL-26OCT22LANYI-7 +0.063 |
| VGK @ STL | 0.550 | 0.494 | 0.174 | 0.222 | 6.36 | 6.33 | 0.993/1.004 | KXNHLSPREAD-26OCT22VGKSTL-STL2 -0.056 |
| WPG @ DAL | 0.592 | 0.575 | 0.180 | 0.214 | 5.55 | 5.95 | 0.986/0.988 | KXNHLTOTAL-26OCT22WPGDAL-7 +0.072 |
| MIN @ CGY | 0.457 | 0.449 | 0.186 | 0.221 | 5.85 | 6.11 | 0.986/0.995 | KXNHLTOTAL-26OCT22MINCGY-7 +0.052 |
| CAR @ EDM | 0.529 | 0.567 | 0.170 | 0.215 | 6.54 | 6.74 | 0.994/0.989 | KXNHLTEAMTOTAL-26OCT22CAREDM-EDM4 +0.052 |
| UTA @ SEA | 0.456 | 0.499 | 0.170 | 0.215 | 6.51 | 6.50 | 1.005/0.992 | KXNHLGAME-26OCT22UTASEA-UTA -0.044 |
| DET @ VAN | 0.450 | 0.532 | 0.176 | 0.218 | 6.37 | 6.28 | 1.021/1.003 | KXNHLSPREAD-26OCT22DETVAN-DET2 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Edstrom: 1+ goals YES @ 11c · p 0.1476 (adj 0.132) · $1.72 · thesis NSH:WINS_BY_2PLUS
- Casey Mittelstadt: 1+ goals YES @ 15c · p 0.1938 (adj 0.1754) · $2.04 · thesis BOS:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 6c · p 0.079 (adj 0.0742) · $1.17 · thesis NSH:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 62c · p 0.659 (adj 0.6468) · $3.21 · thesis BOS:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 69c · p 0.7594 (adj 0.7172) · $5.18 · thesis NYR:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 14c · p 0.183 (adj 0.171) · $2.96 · thesis OTT:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 56c · p 0.716 (adj 0.6048) · $8.87 · thesis OTT:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 69c · p 0.7914 (adj 0.7222) · $5.47 · thesis ANA:WINS
- Jack Hughes: 1+ goals NO @ 63c · p 0.6772 (adj 0.6629) · $4.78 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 73c · p 0.7709 (adj 0.7582) · $5.7 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6986 (adj 0.6789) · $9.09 · thesis FLA:SUPPRESSED
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1495 (adj 0.1271) · $2.12 · thesis PIT:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 82c · p 0.8809 (adj 0.8479) · $9.09 · thesis PIT:WINS
- Connor Dewar: 1+ goals YES @ 15c · p 0.192 (adj 0.1703) · $1.12 · thesis PIT:WINS_BY_2PLUS
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.8273 (adj 0.6926) · $9.09 · thesis LAK:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2483 (adj 0.2375) · $2.21 · thesis NYI:OFFENSE_4PLUS
- Mark Stone: 1+ assists NO @ 53c · p 0.6244 (adj 0.5747) · $7.01 · thesis VGK:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3174 (adj 0.3068) · $1.96 · thesis STL:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 3c · p 0.0507 (adj 0.0443) · $1.17 · thesis WPG:OFFENSE_4PLUS
- Gabriel Vilardi: 1+ goals YES @ 21c · p 0.2645 (adj 0.2471) · $3.27 · thesis WPG:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 71c · p 0.7756 (adj 0.7403) · $4.29 · thesis GAME:TIGHT
- Kirill Kaprizov: 1+ goals NO @ 53c · p 0.6127 (adj 0.5883) · $8.72 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 59c · p 0.6804 (adj 0.6327) · $3.86 · thesis CGY:WINS
- Quinn Hughes: 1+ assists NO @ 36c · p 0.4494 (adj 0.3997) · $2.3 · thesis MIN:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 17c · p 0.2061 (adj 0.1933) · $1.57 · thesis CGY:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1194 (adj 0.1021) · $1.67 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 69c · p 0.7639 (adj 0.7245) · $5.06 · thesis EDM:WINS
- Zach Hyman: 1+ goals YES @ 31c · p 0.3615 (adj 0.3424) · $2.4 · thesis EDM:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 80c · p 0.8552 (adj 0.8251) · $2.26 · thesis EDM:WINS
- Shane Wright: 1+ goals YES @ 14c · p 0.2009 (adj 0.1782) · $2.63 · thesis SEA:OFFENSE_4PLUS
- Utah wins by over 2.5 goals NO @ 73c · p 0.8173 (adj 0.7712) · $7.69 · thesis SEA:WINS
- Utah wins by over 1.5 goals NO @ 61c · p 0.7049 (adj 0.6549) · $2.23 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 21c · p 0.2807 (adj 0.2429) · $1.08 · thesis SEA:WINS_BY_2PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2699 (adj 0.2462) · $5.69 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 12c · p 0.1771 (adj 0.1528) · $2.73 · thesis VAN:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1648 (adj 0.1511) · $2.65 · thesis VAN:OFFENSE_4PLUS
- Detroit wins by over 1.5 goals NO @ 62c · p 0.7514 (adj 0.6627) · $4.22 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ BOS** · priced 163/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Michael DiPietro (PROBABLE) exp shots 27.6, exp saves 23.97 (sd 6.6), pull risk 0.061
- NSH net: Juuse Saros (PROJECTED) exp shots 28.42, exp saves 24.26 (sd 6.75), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.381 | 0.525 | 54/49 | +0.112 | STANDARD |
| Pavel Zacha: 1+ assists | 0.346 | 0.465 | 48/55 | +0.087 | STANDARD |
| Charlie McAvoy: 1+ points | 0.471 | 0.570 | 59/45 | +0.062 | STANDARD |
| David Pastrnak: 2+ points | 0.300 | 0.390 | 40/62 | +0.064 | STANDARD |
| David Pastrnak: 1+ assists | 0.491 | 0.580 | 60/44 | +0.051 | STANDARD |
| Matthew Wood: 1+ goals | 0.201 | 0.125 | 16/91 | +0.031 | STANDARD |

**NYR @ TOR** · priced 166/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 27.8, exp saves 24.1 (sd 6.59), pull risk 0.064
- NYR net: Dylan Garand (PROJECTED) exp shots 26.92, exp saves 23.14 (sd 6.54), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ assists | 0.241 | 0.325 | 34/69 | +0.054 | STANDARD |
| Gabe Perreault: 1+ assists | 0.316 | 0.235 | 26/79 | +0.043 | STANDARD |
| Gavin McKenna: 1+ points | 0.385 | 0.465 | 48/55 | +0.048 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.468 | 0.540 | 56/48 | +0.035 | STANDARD |
| Auston Matthews: 1+ assists | 0.397 | 0.465 | 48/55 | +0.035 | STANDARD |
| Gabe Perreault: 1+ points | 0.467 | 0.400 | 41/61 | +0.040 | STANDARD |

**SJS @ OTT** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 24.89, exp saves 21.66 (sd 6.14), pull risk 0.057
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.6, exp saves 24.36 (sd 6.71), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.284 | 0.455 | 47/56 | +0.139 | STANDARD |
| Jake Sanderson: 1+ points | 0.376 | 0.535 | 55/48 | +0.126 | STANDARD |
| Tim Stutzle: 1+ assists | 0.417 | 0.540 | 56/48 | +0.085 | STANDARD |
| Ivar Stenberg: 1+ points | 0.357 | 0.470 | 49/55 | +0.076 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.222 | 0.325 | 34/69 | +0.073 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.415 | 0.505 | 52/51 | +0.057 | STANDARD |

**ANA @ NJD** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROJECTED) exp shots 27.82, exp saves 24.19 (sd 6.63), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 29.59, exp saves 25.35 (sd 7.01), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ points | 0.599 | 0.385 | 72/95 | -0.135 | STANDARD |
| Luke Evangelista: 1+ assists | 0.198 | 0.385 | 41/64 | +0.146 | STANDARD |
| Luke Evangelista: 1+ points | 0.377 | 0.530 | 55/49 | +0.116 | STANDARD |
| Jack Hughes: 1+ assists | 0.411 | 0.550 | 56/46 | +0.111 | STANDARD |
| Jack Hughes: 2+ points | 0.233 | 0.360 | 38/66 | +0.091 | STANDARD |
| Luke Hughes: 1+ points | 0.455 | 0.565 | 58/45 | +0.078 | STANDARD |

**FLA @ PIT** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.42, exp saves 23.08 (sd 6.34), pull risk 0.055
- FLA net: Cooper Black (PROJECTED) exp shots 27.3, exp saves 23.16 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.291 | 0.405 | 42/61 | +0.082 | STANDARD |
| Sam Reinhart: 1+ points | 0.483 | 0.580 | 60/44 | +0.059 | STANDARD |
| Blake Lizotte: 1+ goals | 0.149 | 0.060 | 10/98 | +0.043 | STANDARD |
| Connor Dewar: 1+ goals | 0.192 | 0.105 | 15/94 | +0.033 | STANDARD |
| Rickard Rakell: 2+ points | 0.246 | 0.160 | 23/91 | +0.003 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.313 | 0.395 | 41/62 | +0.050 | STANDARD |

**LAK @ NYI** · priced 151/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 26.76, exp saves 23.29 (sd 6.31), pull risk 0.049
- LAK net: Anton Forsberg (PROJECTED) exp shots 27.67, exp saves 23.97 (sd 6.55), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.173 | 0.380 | 40/64 | +0.171 | STANDARD |
| Mats Zuccarello: 1+ points | 0.344 | 0.505 | 52/51 | +0.128 | STANDARD |
| Mats Zuccarello: 1+ goals | 0.207 | 0.120 | 22/98 | -0.025 | STANDARD |
| Trevor Moore: 1+ assists | 0.279 | 0.200 | 23/83 | +0.037 | STANDARD |
| Artemi Panarin: 1+ assists | 0.383 | 0.450 | 46/56 | +0.040 | STANDARD |
| Mats Zuccarello: 2+ points | 0.065 | 0.130 | 19/93 | +0.000 | STANDARD |

**VGK @ STL** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.55, exp saves 23.79 (sd 6.58), pull risk 0.063
- VGK net: Adin Hill (PROJECTED) exp shots 25.57, exp saves 22.09 (sd 6.21), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.436 | 0.560 | 57/45 | +0.096 | STANDARD |
| Mitch Marner: 1+ assists | 0.410 | 0.520 | 53/49 | +0.082 | STANDARD |
| Jack Eichel: 2+ points | 0.232 | 0.340 | 36/68 | +0.073 | STANDARD |
| Mark Stone: 1+ assists | 0.376 | 0.475 | 48/53 | +0.077 | STANDARD |
| Mitch Marner: 1+ points | 0.544 | 0.640 | 65/37 | +0.070 | STANDARD |
| Trevor Connelly: 1+ points | 0.367 | 0.440 | 45/57 | +0.046 | STANDARD |

**WPG @ DAL** · priced 153/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.62, exp saves 21.55 (sd 5.96), pull risk 0.046
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.81, exp saves 22.93 (sd 6.41), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.241 | 0.325 | 34/69 | +0.054 | STANDARD |
| Tyler Seguin: 1+ assists | 0.215 | 0.295 | 32/73 | +0.041 | STANDARD |
| Cole Perfetti: 1+ points | 0.527 | 0.450 | 47/57 | +0.040 | STANDARD |
| Miro Heiskanen: 1+ points | 0.488 | 0.565 | 59/46 | +0.035 | STANDARD |
| Cole Perfetti: 1+ assists | 0.369 | 0.295 | 31/72 | +0.044 | STANDARD |
| Gabriel Vilardi: 1+ goals | 0.265 | 0.195 | 21/82 | +0.043 | STANDARD |

**MIN @ CGY** · priced 166/167 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 30.26, exp saves 26.04 (sd 7.01), pull risk 0.067
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.91, exp saves 25.13 (sd 6.71), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Quinn Hughes: 2+ points | 0.242 | 0.350 | 37/67 | +0.072 | STANDARD |
| Quinn Hughes: 1+ assists | 0.551 | 0.650 | 66/36 | +0.073 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.387 | 0.485 | 50/53 | +0.065 | STANDARD |
| Joel Eriksson Ek: 1+ goals | 0.305 | 0.215 | 31/88 | -0.020 | STANDARD |
| Morgan Frost: 1+ goals | 0.264 | 0.180 | 24/88 | +0.011 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.284 | 0.360 | 38/66 | +0.040 | STANDARD |

**CAR @ EDM** · priced 156/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 29.98, exp saves 26.08 (sd 6.92), pull risk 0.06
- CAR net: Brandon Bussi (PROJECTED) exp shots 25.41, exp saves 21.63 (sd 6.28), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ points | 0.440 | 0.305 | 33/72 | +0.095 | STANDARD |
| Sebastian Aho: 1+ assists | 0.384 | 0.510 | 52/50 | +0.099 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.366 | 0.240 | 27/79 | +0.082 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.471 | 0.590 | 60/42 | +0.092 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.225 | 0.130 | 20/94 | +0.014 | STANDARD |
| Alex Formenton: 1+ goals | 0.183 | 0.090 | 14/96 | +0.035 | STANDARD |

**UTA @ SEA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 29.05, exp saves 25.15 (sd 6.79), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.82, exp saves 22.3 (sd 6.27), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Clayton Keller: 1+ points | 0.590 | 0.720 | 74/30 | +0.095 | STANDARD |
| Clayton Keller: 2+ points | 0.224 | 0.345 | 36/67 | +0.091 | STANDARD |
| Clayton Keller: 1+ assists | 0.443 | 0.560 | 58/46 | +0.080 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.209 | 0.320 | 34/70 | +0.077 | STANDARD |
| Vincent Trocheck: 1+ points | 0.354 | 0.465 | 48/55 | +0.078 | STANDARD |
| Nick Schmaltz: 1+ goals | 0.304 | 0.205 | 33/92 | -0.042 | STANDARD |

**DET @ VAN** · priced 126/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.0, exp saves 26.16 (sd 6.93), pull risk 0.055
- DET net: John Gibson (PROJECTED) exp shots 25.34, exp saves 21.75 (sd 6.11), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex DeBrincat: 1+ goals | 0.409 | 0.235 | 40/93 | -0.008 | STANDARD |
| Jake DeBrusk: 1+ goals | 0.325 | 0.165 | 29/96 | +0.020 | STANDARD |
| Linus Karlsson: 1+ goals | 0.259 | 0.140 | 20/92 | +0.048 | STANDARD |
| Alex DeBrincat: 2+ points | 0.293 | 0.175 | 33/98 | -0.053 | STANDARD |
| Viktor Arvidsson: 1+ goals | 0.283 | 0.170 | 30/96 | -0.031 | STANDARD |
| Brock Boeser: 1+ goals | 0.271 | 0.160 | 28/96 | -0.023 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
