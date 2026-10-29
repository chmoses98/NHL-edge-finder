# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T17:49:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4356 · contracts joined: 2467 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2192, 'NO_EDGE': 111, 'OK': 164}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 337, 'game_early_goal': 11, 'first_goal': 403, 'game_winner': 22, 'player_goals': 702, 'game_overtime': 11, 'player_points': 453, 'goalie_saves': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-3h | 0.646 | 0.354 | 0.172 | 5.62 | 3.25 | 2.37 | 218 (25/193) | CONFIRMED/CONFIRMED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-3h | 0.468 | 0.532 | 0.170 | 6.70 | 3.25 | 3.45 | 227 (25/202) | CONFIRMED/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-3h | 0.656 | 0.344 | 0.172 | 5.84 | 3.40 | 2.44 | 225 (25/200) | PROBABLE/CONFIRMED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-3h | 0.597 | 0.403 | 0.183 | 5.64 | 3.12 | 2.52 | 234 (25/209) | CONFIRMED/PROBABLE |
| BOS @ STL | 2026-10-30T00:00:00Z | T-6h | 0.491 | 0.509 | 0.182 | 5.80 | 2.88 | 2.92 | 227 (25/202) | CONFIRMED/CONFIRMED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-6h | 0.539 | 0.461 | 0.170 | 6.70 | 3.47 | 3.22 | 225 (25/200) | CONFIRMED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-6h | 0.599 | 0.401 | 0.179 | 5.75 | 3.17 | 2.58 | 213 (25/188) | CONFIRMED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-6h | 0.583 | 0.417 | 0.181 | 5.72 | 3.12 | 2.61 | 230 (25/205) | PROJECTED/CONFIRMED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-6h | 0.504 | 0.496 | 0.172 | 6.45 | 3.23 | 3.23 | 233 (25/208) | PROJECTED/PROJECTED |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-6h | 0.510 | 0.490 | 0.180 | 6.04 | 3.05 | 2.99 | 217 (25/192) | PROJECTED/PROJECTED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-6h | 0.585 | 0.415 | 0.163 | 6.94 | 3.75 | 3.19 | 218 (25/193) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.349 | 0.455 | 0.433 | 46 | 55 | no | +0.084 | OK |
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.461 | 0.565 | 0.544 | 57 | 44 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.414 | 0.505 | 0.487 | 51 | 50 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.693 | 0.775 | 0.760 | 78 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.419 | 0.510 | 0.492 | 52 | 50 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.390 | 0.475 | 0.458 | 48 | 53 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.626 | 0.710 | 0.694 | 72 | 30 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.227 | 0.310 | 0.292 | 32 | 70 | no | +0.058 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.496 | 0.575 | 0.559 | 58 | 43 | no | +0.057 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.504 | 0.425 | 0.441 | 43 | 58 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.287 | 0.355 | 0.341 | 36 | 65 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.836 | 0.895 | 0.885 | 90 | 11 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.650 | 0.720 | 0.707 | 73 | 29 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.230 | 0.300 | 0.285 | 31 | 71 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.674 | 0.740 | 0.727 | 75 | 27 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.799 | 0.860 | 0.849 | 87 | 15 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.214 | 0.280 | 0.266 | 29 | 73 | no | +0.042 | OK |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.583 | 0.645 | 0.633 | 65 | 36 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.274 | 0.335 | 0.322 | 34 | 67 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.801 | 0.860 | 0.849 | 87 | 15 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-6 | game_total | 0.492 | 0.555 | 0.543 | 56 | 45 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.256 | 0.320 | 0.307 | 33 | 69 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.698 | 0.760 | 0.748 | 77 | 25 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.454 | 0.515 | 0.503 | 52 | 49 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.355 | 0.415 | 0.403 | 42 | 59 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.465 | 0.530 | 0.517 | 54 | 48 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.347 | 0.405 | 0.393 | 41 | 60 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.711 | 0.770 | 0.759 | 78 | 24 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.875 | 0.866 | 88 | 13 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.471 | 0.415 | 0.426 | 42 | 59 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-5 | game_total | 0.704 | 0.755 | 0.745 | 76 | 25 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.470 | 0.525 | 0.514 | 53 | 48 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.809 | 0.860 | 0.851 | 87 | 15 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-4 | game_total | 0.819 | 0.870 | 0.861 | 88 | 14 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN5 | team_total | 0.205 | 0.260 | 0.248 | 27 | 75 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.421 | 0.480 | 0.468 | 49 | 53 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-7 | game_total | 0.382 | 0.435 | 0.424 | 44 | 57 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-6 | game_total | 0.482 | 0.535 | 0.524 | 54 | 47 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN3 | team_total | 0.613 | 0.670 | 0.659 | 68 | 34 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-5 | game_total | 0.727 | 0.780 | 0.770 | 79 | 23 | no | +0.031 | OK |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.417 | 0.365 | 0.375 | 37 | 64 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.101 | 0.150 | 0.139 | 16 | 86 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-6 | game_total | 0.503 | 0.555 | 0.545 | 56 | 45 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.256 | 0.310 | 0.299 | 32 | 70 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH5 | team_total | 0.282 | 0.230 | 0.240 | 24 | 78 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.484 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.855 | 0.895 | 0.888 | 90 | 11 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN2 | team_total | 0.813 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.405 | 0.465 | 0.453 | 48 | 55 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-4 | game_total | 0.803 | 0.850 | 0.841 | 86 | 16 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.486 | 0.535 | 0.525 | 54 | 47 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-7 | game_total | 0.368 | 0.415 | 0.405 | 42 | 59 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.107 | 0.145 | 0.137 | 15 | 86 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-7 | game_total | 0.389 | 0.435 | 0.426 | 44 | 57 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-5 | game_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29BOSSTL-STL3 | team_total | 0.560 | 0.605 | 0.596 | 61 | 40 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH6 | team_total | 0.140 | 0.100 | 0.107 | 11 | 91 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.185 | 0.225 | 0.216 | 23 | 78 | no | +0.023 | OK |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.510 | 0.465 | 0.474 | 47 | 54 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.602 | 0.645 | 0.637 | 65 | 36 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.244 | 0.285 | 0.276 | 29 | 72 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.623 | 0.670 | 0.661 | 68 | 34 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT29CHIDET-CHI2 | game_spread | 0.197 | 0.235 | 0.227 | 24 | 77 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.121 | 0.155 | 0.148 | 16 | 85 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT29BUFANA-4 | game_total | 0.874 | 0.905 | 0.899 | 91 | 10 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT29CHIDET-9 | game_total | 0.122 | 0.160 | 0.152 | 17 | 85 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL2 | team_total | 0.822 | 0.855 | 0.849 | 86 | 15 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-8 | game_total | 0.334 | 0.295 | 0.303 | 30 | 71 | yes | +0.019 | OK |
| KXNHLGAME-26OCT29CBJCAR-CBJ | game_winner | 0.344 | 0.305 | 0.313 | 31 | 70 | yes | +0.019 | OK |
| KXNHLGAME-26OCT29CBJCAR-CAR | game_winner | 0.656 | 0.700 | 0.691 | 71 | 31 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.146 | 0.115 | 0.121 | 12 | 89 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-NYI2 | game_spread | 0.209 | 0.175 | 0.181 | 18 | 83 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI2 | team_total | 0.708 | 0.755 | 0.746 | 77 | 26 | no | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 0.646 | 0.628 | 0.172 | 0.216 | 5.62 | 5.97 | 0.947/1.004 | KXNHLTOTAL-26OCT29WPGTB-7 +0.062 |
| UTA @ PIT | 0.468 | 0.513 | 0.170 | 0.218 | 6.70 | 6.74 | 1.042/0.993 | KXNHLGAME-26OCT29UTAPIT-PIT +0.045 |
| CBJ @ CAR | 0.656 | 0.565 | 0.172 | 0.219 | 5.84 | 6.17 | 1.000/0.947 | KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3 +0.108 |
| CHI @ DET | 0.597 | 0.605 | 0.183 | 0.215 | 5.64 | 6.07 | 0.995/0.996 | KXNHLTOTAL-26OCT29CHIDET-7 +0.073 |
| BOS @ STL | 0.491 | 0.528 | 0.182 | 0.215 | 5.80 | 6.29 | 0.977/0.956 | KXNHLTOTAL-26OCT29BOSSTL-7 +0.088 |
| WSH @ NSH | 0.539 | 0.536 | 0.170 | 0.216 | 6.70 | 6.43 | 1.005/0.993 | KXNHLTOTAL-26OCT29WSHNSH-6 -0.047 |
| MTL @ DAL | 0.599 | 0.562 | 0.179 | 0.218 | 5.75 | 6.10 | 0.995/0.943 | KXNHLTEAMTOTAL-26OCT29MTLDAL-MTL3 +0.072 |
| NYI @ MIN | 0.583 | 0.560 | 0.181 | 0.214 | 5.72 | 6.11 | 0.996/0.948 | KXNHLTOTAL-26OCT29NYIMIN-7 +0.069 |
| BUF @ ANA | 0.504 | 0.558 | 0.172 | 0.210 | 6.45 | 6.66 | 1.036/0.998 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.068 |
| OTT @ LAK | 0.510 | 0.528 | 0.180 | 0.224 | 6.04 | 5.99 | 0.993/1.034 | KXNHLSPREAD-26OCT29OTTLA-OTT2 -0.024 |
| VAN @ SJS | 0.585 | 0.556 | 0.163 | 0.216 | 6.94 | 6.58 | 1.035/1.026 | KXNHLTOTAL-26OCT29VANSJ-8 -0.062 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9286 (adj 0.9164) · $9.43 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 41c · p 0.4979 (adj 0.449) · $3.74 · thesis TBL:SUPPRESSED
- Nick Robertson: 1+ goals YES @ 16c · p 0.2509 (adj 0.2269) · $6.12 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1542 (adj 0.1369) · $3.8 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 32c · p 0.3812 (adj 0.3646) · $4.22 · thesis PIT:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 65c · p 0.6921 (adj 0.6791) · $4.6 · thesis UTA:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 17c · p 0.2577 (adj 0.2345) · $7.01 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1848 (adj 0.1699) · $3.81 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.1146 (adj 0.1035) · $2.07 · thesis CBJ:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7784 (adj 0.7638) · $9.36 · thesis CAR:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 57c · p 0.7147 (adj 0.6141) · $9.43 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 22c · p 0.2633 (adj 0.2512) · $3.29 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1401 (adj 0.1276) · $1.59 · thesis CHI:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 41c · p 0.4508 (adj 0.4394) · $2.43 · thesis DET:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1787 (adj 0.1665) · $2.38 · thesis BOS:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2825 (adj 0.2706) · $2.72 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 29c · p 0.3305 (adj 0.3191) · $2.45 · thesis STL:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2234 (adj 0.21) · $2.76 · thesis WSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 14c · p 0.1711 (adj 0.1621) · $1.82 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 29c · p 0.3314 (adj 0.3173) · $2.12 · thesis NSH:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2461 (adj 0.2233) · $4.34 · thesis NYI:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6166 (adj 0.595) · $9.43 · thesis MIN:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 11c · p 0.1545 (adj 0.1409) · $2.87 · thesis NYI:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.162 (adj 0.1477) · $2.43 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1632 (adj 0.1462) · $4.11 · thesis ANA:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.8528 (adj 0.8039) · $9.1 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 25c · p 0.3447 (adj 0.2949) · $2.3 · thesis ANA:WINS_BY_2PLUS
- Tage Thompson: 1+ goals NO @ 63c · p 0.6953 (adj 0.6777) · $8.05 · thesis BUF:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0743 (adj 0.0657) · $1.3 · thesis LAK:WINS_BY_2PLUS
- Scott Laughton: 1+ goals YES @ 12c · p 0.1549 (adj 0.1412) · $1.6 · thesis LAK:OFFENSE_4PLUS
- Ottawa wins by over 1.5 goals NO @ 70c · p 0.7564 (adj 0.7257) · $3.15 · thesis LAK:WINS
- Ivar Stenberg: 1+ goals NO @ 71c · p 0.806 (adj 0.7404) · $7.95 · thesis SJS:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 19c · p 0.228 (adj 0.2147) · $1.99 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 13c · p 0.1599 (adj 0.1499) · $1.51 · thesis VAN:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 61c · p 0.7199 (adj 0.6387) · $4.03 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 160/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 24.76, exp saves 21.92 (sd 5.98), pull risk 0.039
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.88, exp saves 24.51 (sd 6.81), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.502 | 0.600 | 61/41 | +0.071 | STANDARD |
| John Carlson: 1+ points | 0.386 | 0.470 | 49/55 | +0.046 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.159 | 0.240 | 27/79 | +0.039 | STANDARD |
| John Carlson: 1+ assists | 0.305 | 0.380 | 40/64 | +0.039 | STANDARD |
| Nikita Kucherov: 2+ points | 0.330 | 0.405 | 42/61 | +0.044 | STANDARD |
| Nikita Kucherov: 3+ points | 0.111 | 0.160 | 18/86 | +0.021 | STANDARD |

**UTA @ PIT** · priced 151/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 27.0, exp saves 23.28 (sd 6.55), pull risk 0.075
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.13, exp saves 23.31 (sd 6.54), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ points | 0.681 | 0.545 | 57/48 | +0.094 | STANDARD |
| Rickard Rakell: 1+ goals | 0.435 | 0.300 | 32/72 | +0.100 | STANDARD |
| Rickard Rakell: 2+ points | 0.313 | 0.185 | 20/83 | +0.102 | STANDARD |
| Connor Dewar: 1+ goals | 0.223 | 0.105 | 11/90 | +0.106 | STANDARD |
| Ville Koivunen: 1+ points | 0.483 | 0.380 | 40/64 | +0.067 | STANDARD |
| Nick Robertson: 1+ goals | 0.251 | 0.155 | 16/85 | +0.081 | STANDARD |

**CBJ @ CAR** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.87, exp saves 20.86 (sd 5.9), pull risk 0.051
- CBJ net: Jet Greaves (CONFIRMED) exp shots 30.96, exp saves 26.54 (sd 7.13), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.362 | 0.475 | 49/54 | +0.081 | STANDARD |
| Jet Greaves: 27+ saves | 0.503 | 0.395 | 53/74 | -0.045 |  |
| Sebastian Aho: 1+ points | 0.539 | 0.645 | 65/36 | +0.085 | STANDARD |
| Seth Jarvis: 1+ assists | 0.245 | 0.345 | 36/67 | +0.070 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.417 | 0.515 | 53/50 | +0.066 | STANDARD |
| Charlie Coyle: 1+ goals | 0.258 | 0.165 | 17/84 | +0.078 | STANDARD |

**CHI @ DET** · priced 164/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 24.08, exp saves 21.14 (sd 5.78), pull risk 0.043
- CHI net: Spencer Knight (PROBABLE) exp shots 30.26, exp saves 25.92 (sd 7.0), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.285 | 0.440 | 45/57 | +0.128 | STANDARD |
| Ryan Donato: 1+ assists | 0.222 | 0.100 | 19/99 | +0.021 | STANDARD |
| Patrick Kane: 1+ points | 0.443 | 0.550 | 56/46 | +0.080 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.228 | 0.125 | 23/98 | -0.014 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.402 | 0.300 | 32/72 | +0.067 | STANDARD |
| Connor Bedard: 1+ assists | 0.338 | 0.440 | 46/58 | +0.065 | STANDARD |

**BOS @ STL** · priced 171/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.11, exp saves 22.63 (sd 6.26), pull risk 0.06
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.06, exp saves 24.16 (sd 6.7), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ assists | 0.297 | 0.210 | 23/81 | +0.055 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.372 | 0.455 | 47/56 | +0.051 | STANDARD |
| David Pastrnak: 1+ assists | 0.452 | 0.535 | 55/48 | +0.050 | STANDARD |
| David Pastrnak: 2+ points | 0.260 | 0.340 | 35/67 | +0.055 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.579 | 0.515 | 54/51 | +0.022 | STANDARD |
| Robert Thomas: 1+ assists | 0.417 | 0.480 | 50/54 | +0.025 | STANDARD |

**WSH @ NSH** · priced 167/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.24, exp saves 24.51 (sd 6.67), pull risk 0.06
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.84 (sd 6.74), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.314 | 0.230 | 26/80 | +0.040 | STANDARD |
| Tom Wilson: 1+ assists | 0.335 | 0.265 | 29/76 | +0.031 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.270 | 0.335 | 35/68 | +0.035 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.193 | 0.250 | 27/77 | +0.025 | STANDARD |
| Steven Stamkos: 1+ assists | 0.416 | 0.360 | 38/66 | +0.020 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.331 | 0.275 | 29/74 | +0.027 | STANDARD |

**MTL @ DAL** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.03, exp saves 20.94 (sd 5.96), pull risk 0.053
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.09 (sd 6.57), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.448 | 0.520 | 54/50 | +0.035 | STANDARD |
| Cole Caufield: 1+ assists | 0.321 | 0.390 | 40/62 | +0.043 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.259 | 0.190 | 21/83 | +0.037 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.550 | 58/48 | +0.021 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.365 | 0.430 | 45/59 | +0.028 | STANDARD |
| Mikko Rantanen: 2+ points | 0.242 | 0.305 | 32/71 | +0.034 | STANDARD |

**NYI @ MIN** · priced 173/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.41, exp saves 23.88 (sd 6.46), pull risk 0.051
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.87, exp saves 24.95 (sd 6.75), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Yakov Trenin: 1+ points | 0.315 | 0.140 | 27/99 | +0.031 | STANDARD |
| Jonas Brodin: 1+ assists | 0.281 | 0.120 | 23/99 | +0.039 | STANDARD |
| Logan Stanley: 1+ points | 0.280 | 0.125 | 24/99 | +0.027 | STANDARD |
| Ryan Hartman: 1+ assists | 0.244 | 0.120 | 23/99 | +0.002 | STANDARD |
| Jonas Brodin: 1+ points | 0.322 | 0.200 | 28/88 | +0.028 | STANDARD |
| Anthony Duclair: 1+ assists | 0.235 | 0.120 | 23/99 | -0.007 | STANDARD |

**BUF @ ANA** · priced 181/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.65), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 28.64, exp saves 24.45 (sd 6.9), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ points | 0.295 | 0.125 | 24/99 | +0.042 | STANDARD |
| Noah Warren: 1+ assists | 0.260 | 0.105 | 20/99 | +0.049 | STANDARD |
| A.J. Greer: 1+ goals | 0.258 | 0.145 | 16/87 | +0.088 | STANDARD |
| Tage Thompson: 1+ points | 0.527 | 0.625 | 63/38 | +0.076 | STANDARD |
| Tage Thompson: 2+ points | 0.179 | 0.270 | 29/75 | +0.058 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.412 | 0.500 | 51/51 | +0.060 | STANDARD |

**OTT @ LAK** · priced 162/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.33, exp saves 23.9 (sd 6.42), pull risk 0.048
- OTT net: Jonas Johansson (PROJECTED) exp shots 26.32, exp saves 22.72 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.297 | 0.430 | 45/59 | +0.096 | STANDARD |
| Jake Sanderson: 1+ points | 0.377 | 0.495 | 52/53 | +0.075 | STANDARD |
| Tim Stutzle: 1+ assists | 0.365 | 0.445 | 46/57 | +0.048 | STANDARD |
| Alex Laferriere: 1+ points | 0.572 | 0.500 | 53/53 | +0.024 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.301 | 0.370 | 39/65 | +0.033 | STANDARD |
| Trevor Moore: 1+ points | 0.448 | 0.380 | 41/65 | +0.021 | STANDARD |

**VAN @ SJS** · priced 160/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 25.57, exp saves 22.26 (sd 6.27), pull risk 0.063
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.42, exp saves 25.09 (sd 7.01), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.417 | 0.560 | 59/47 | +0.096 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.280 | 0.405 | 42/61 | +0.093 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.464 | 0.580 | 59/43 | +0.089 | STANDARD |
| Macklin Celebrini: 2+ points | 0.329 | 0.435 | 45/58 | +0.074 | STANDARD |
| Ivar Stenberg: 1+ goals | 0.194 | 0.295 | 30/71 | +0.082 | STANDARD |
| Linus Karlsson: 1+ points | 0.453 | 0.360 | 37/65 | +0.067 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
