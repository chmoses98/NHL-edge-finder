# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T18:39:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4350 · contracts joined: 2461 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2186, 'OK': 172, 'NO_EDGE': 103}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 335, 'game_early_goal': 11, 'first_goal': 402, 'game_winner': 22, 'player_goals': 700, 'game_overtime': 11, 'player_points': 451, 'goalie_saves': 12, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-3h | 0.646 | 0.354 | 0.172 | 5.62 | 3.25 | 2.37 | 218 (25/193) | CONFIRMED/CONFIRMED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-3h | 0.468 | 0.532 | 0.170 | 6.70 | 3.25 | 3.45 | 218 (25/193) | CONFIRMED/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-3h | 0.656 | 0.344 | 0.172 | 5.84 | 3.40 | 2.44 | 225 (25/200) | PROBABLE/CONFIRMED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-3h | 0.597 | 0.403 | 0.183 | 5.64 | 3.12 | 2.52 | 234 (25/209) | CONFIRMED/PROBABLE |
| BOS @ STL | 2026-10-30T00:00:00Z | T-3h | 0.491 | 0.509 | 0.182 | 5.80 | 2.88 | 2.92 | 227 (25/202) | CONFIRMED/CONFIRMED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-3h | 0.539 | 0.461 | 0.170 | 6.70 | 3.47 | 3.22 | 225 (25/200) | CONFIRMED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-3h | 0.599 | 0.401 | 0.179 | 5.75 | 3.17 | 2.58 | 213 (25/188) | CONFIRMED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-3h | 0.583 | 0.417 | 0.181 | 5.72 | 3.12 | 2.61 | 230 (25/205) | PROJECTED/CONFIRMED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-6h | 0.504 | 0.496 | 0.172 | 6.45 | 3.23 | 3.23 | 233 (25/208) | PROJECTED/PROJECTED |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-6h | 0.510 | 0.490 | 0.180 | 6.04 | 3.05 | 2.99 | 219 (25/194) | PROJECTED/PROJECTED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-6h | 0.574 | 0.426 | 0.158 | 7.00 | 3.75 | 3.26 | 219 (25/194) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.461 | 0.565 | 0.544 | 57 | 44 | no | +0.082 | OK |
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.349 | 0.445 | 0.425 | 45 | 56 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.693 | 0.775 | 0.760 | 78 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.419 | 0.510 | 0.492 | 52 | 50 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.390 | 0.475 | 0.458 | 48 | 53 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.414 | 0.500 | 0.483 | 51 | 51 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.227 | 0.310 | 0.292 | 32 | 70 | no | +0.058 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.504 | 0.425 | 0.441 | 43 | 58 | yes | +0.057 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.496 | 0.575 | 0.559 | 58 | 43 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.626 | 0.700 | 0.686 | 71 | 31 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.287 | 0.355 | 0.341 | 36 | 65 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.836 | 0.895 | 0.885 | 90 | 11 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.650 | 0.720 | 0.707 | 73 | 29 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.230 | 0.300 | 0.285 | 31 | 71 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.674 | 0.740 | 0.727 | 75 | 27 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.799 | 0.860 | 0.849 | 87 | 15 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.214 | 0.280 | 0.266 | 29 | 73 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.274 | 0.335 | 0.322 | 34 | 67 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.801 | 0.860 | 0.849 | 87 | 15 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-6 | game_total | 0.492 | 0.555 | 0.543 | 56 | 45 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.256 | 0.320 | 0.307 | 33 | 69 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.698 | 0.760 | 0.748 | 77 | 25 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.454 | 0.515 | 0.503 | 52 | 49 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.355 | 0.415 | 0.403 | 42 | 59 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.405 | 0.470 | 0.457 | 48 | 54 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.465 | 0.530 | 0.517 | 54 | 48 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.486 | 0.545 | 0.533 | 55 | 46 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.347 | 0.405 | 0.393 | 41 | 60 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.711 | 0.770 | 0.759 | 78 | 24 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.875 | 0.866 | 88 | 13 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.471 | 0.415 | 0.426 | 42 | 59 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-5 | game_total | 0.704 | 0.755 | 0.745 | 76 | 25 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.470 | 0.525 | 0.514 | 53 | 48 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.809 | 0.860 | 0.851 | 87 | 15 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN5 | team_total | 0.205 | 0.260 | 0.248 | 27 | 75 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.421 | 0.475 | 0.464 | 48 | 53 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-7 | game_total | 0.382 | 0.435 | 0.424 | 44 | 57 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-6 | game_total | 0.482 | 0.535 | 0.524 | 54 | 47 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN3 | team_total | 0.613 | 0.670 | 0.659 | 68 | 34 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-5 | game_total | 0.727 | 0.780 | 0.770 | 79 | 23 | no | +0.031 | OK |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.583 | 0.635 | 0.625 | 64 | 37 | no | +0.031 | OK |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.417 | 0.365 | 0.375 | 37 | 64 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.101 | 0.150 | 0.139 | 16 | 86 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-6 | game_total | 0.503 | 0.555 | 0.545 | 56 | 45 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.256 | 0.310 | 0.299 | 32 | 70 | no | +0.030 | OK |
| KXNHLGAME-26OCT29CBJCAR-CAR | game_winner | 0.656 | 0.705 | 0.696 | 71 | 30 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH5 | team_total | 0.282 | 0.230 | 0.240 | 24 | 78 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.484 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.855 | 0.895 | 0.888 | 90 | 11 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN2 | team_total | 0.813 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-4 | game_total | 0.803 | 0.850 | 0.841 | 86 | 16 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.237 | 0.185 | 0.195 | 20 | 83 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-7 | game_total | 0.368 | 0.415 | 0.405 | 42 | 59 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.107 | 0.145 | 0.137 | 15 | 86 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-7 | game_total | 0.389 | 0.435 | 0.426 | 44 | 57 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-5 | game_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.151 | 0.115 | 0.122 | 12 | 89 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29BOSSTL-STL3 | team_total | 0.560 | 0.605 | 0.596 | 61 | 40 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH6 | team_total | 0.140 | 0.100 | 0.107 | 11 | 91 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.185 | 0.225 | 0.216 | 23 | 78 | no | +0.023 | OK |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.510 | 0.465 | 0.474 | 47 | 54 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.602 | 0.645 | 0.637 | 65 | 36 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.244 | 0.285 | 0.276 | 29 | 72 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-4 | game_total | 0.819 | 0.860 | 0.853 | 87 | 15 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.623 | 0.670 | 0.661 | 68 | 34 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.377 | 0.335 | 0.343 | 34 | 67 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT29CHIDET-CHI2 | game_spread | 0.197 | 0.235 | 0.227 | 24 | 77 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.121 | 0.165 | 0.155 | 18 | 85 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT29BUFANA-4 | game_total | 0.874 | 0.905 | 0.899 | 91 | 10 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT29CHIDET-9 | game_total | 0.122 | 0.160 | 0.152 | 17 | 85 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-8 | game_total | 0.334 | 0.295 | 0.303 | 30 | 71 | yes | +0.019 | OK |
| KXNHLGAME-26OCT29CBJCAR-CBJ | game_winner | 0.344 | 0.305 | 0.313 | 31 | 70 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-NYI2 | game_spread | 0.209 | 0.175 | 0.181 | 18 | 83 | yes | +0.018 | OK |

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
| VAN @ SJS | 0.574 | 0.556 | 0.158 | 0.210 | 7.00 | 6.59 | 1.040/1.026 | KXNHLTOTAL-26OCT29VANSJ-6 -0.065 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 36 recommended · full analysis in card.md / packet.json `thesis_card`

- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9286 (adj 0.9177) · $9.39 · thesis TBL:SUPPRESSED
- Adam Lowry: 1+ goals YES @ 9c · p 0.1182 (adj 0.1099) · $1.68 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 25c · p 0.29 (adj 0.2787) · $2.39 · thesis WPG:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 11c · p 0.1392 (adj 0.1281) · $1.36 · thesis WPG:OFFENSE_4PLUS
- Nick Robertson: 1+ goals YES @ 16c · p 0.2509 (adj 0.2269) · $6.18 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1542 (adj 0.1356) · $3.7 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 32c · p 0.3812 (adj 0.3646) · $4.21 · thesis PIT:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 19c · p 0.2244 (adj 0.2133) · $1.94 · thesis UTA:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1848 (adj 0.1699) · $3.91 · thesis CBJ:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 14c · p 0.1843 (adj 0.1707) · $2.73 · thesis CBJ:OFFENSE_4PLUS
- Seth Jarvis: 1+ goals NO @ 70c · p 0.7512 (adj 0.7371) · $7.8 · thesis CAR:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7219 (adj 0.7052) · $6.29 · thesis CAR:SUPPRESSED
- Emmitt Finnie: 1+ assists YES @ 32c · p 0.4022 (adj 0.3586) · $3.73 · thesis DET:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 58c · p 0.7147 (adj 0.6206) · $8.12 · thesis CHI:SUPPRESSED
- Anton Frondell: 1+ goals YES @ 16c · p 0.1976 (adj 0.1832) · $2.02 · thesis CHI:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 41c · p 0.4508 (adj 0.4394) · $1.44 · thesis DET:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1787 (adj 0.1665) · $2.37 · thesis BOS:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2825 (adj 0.2706) · $2.71 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 29c · p 0.3305 (adj 0.3191) · $2.44 · thesis STL:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2234 (adj 0.2088) · $3.9 · thesis WSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 29c · p 0.3314 (adj 0.3198) · $2.55 · thesis NSH:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2539 (adj 0.2304) · $5.26 · thesis NYI:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 53c · p 0.6166 (adj 0.5937) · $9.39 · thesis MIN:SUPPRESSED
- Olli Maatta: 1+ goals YES @ 4c · p 0.0628 (adj 0.0546) · $1.26 · thesis MIN:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.1534 (adj 0.1413) · $1.63 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1632 (adj 0.1462) · $4.45 · thesis ANA:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.8528 (adj 0.8039) · $9.39 · thesis ANA:WINS
- Tage Thompson: 1+ goals NO @ 63c · p 0.6953 (adj 0.6765) · $8.95 · thesis BUF:SUPPRESSED
- Scott Laughton: 1+ goals YES @ 11c · p 0.1604 (adj 0.1415) · $2.8 · thesis LAK:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0768 (adj 0.0676) · $1.46 · thesis LAK:OFFENSE_4PLUS
- Drake Batherson: 1+ goals NO @ 70c · p 0.7474 (adj 0.733) · $6.86 · thesis OTT:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 58c · p 0.7002 (adj 0.6123) · $3.8 · thesis OTT:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 71c · p 0.8089 (adj 0.7414) · $8.79 · thesis SJS:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2272 (adj 0.2142) · $1.87 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 13c · p 0.1575 (adj 0.1481) · $1.33 · thesis VAN:OFFENSE_4PLUS
- Tyler Toffoli: 1+ assists YES @ 28c · p 0.3361 (adj 0.3055) · $1.89 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 160/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 24.76, exp saves 21.92 (sd 5.98), pull risk 0.039
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.88, exp saves 24.51 (sd 6.81), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.502 | 0.605 | 62/41 | +0.071 | STANDARD |
| John Carlson: 1+ points | 0.386 | 0.470 | 49/55 | +0.046 | STANDARD |
| John Carlson: 1+ assists | 0.305 | 0.385 | 40/63 | +0.049 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.159 | 0.235 | 26/79 | +0.039 | STANDARD |
| Nikita Kucherov: 2+ points | 0.330 | 0.400 | 42/62 | +0.034 | STANDARD |
| Anthony Cirelli: 1+ points | 0.476 | 0.425 | 44/59 | +0.019 | STANDARD |

**UTA @ PIT** · priced 149/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 27.0, exp saves 23.28 (sd 6.55), pull risk 0.075
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.13, exp saves 23.31 (sd 6.54), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ points | 0.681 | 0.540 | 56/48 | +0.104 | STANDARD |
| Rickard Rakell: 1+ goals | 0.435 | 0.305 | 32/71 | +0.100 | STANDARD |
| Rickard Rakell: 2+ points | 0.313 | 0.185 | 20/83 | +0.102 | STANDARD |
| Connor Dewar: 1+ goals | 0.223 | 0.105 | 11/90 | +0.106 | STANDARD |
| Thomas Novak: 1+ points | 0.594 | 0.490 | 51/53 | +0.066 | STANDARD |
| Ville Koivunen: 1+ points | 0.483 | 0.385 | 40/63 | +0.067 | STANDARD |

**CBJ @ CAR** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.87, exp saves 20.86 (sd 5.9), pull risk 0.051
- CBJ net: Jet Greaves (CONFIRMED) exp shots 30.96, exp saves 26.54 (sd 7.13), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.362 | 0.470 | 48/54 | +0.081 | STANDARD |
| Sebastian Aho: 1+ points | 0.539 | 0.645 | 65/36 | +0.085 | STANDARD |
| Seth Jarvis: 1+ assists | 0.245 | 0.350 | 36/66 | +0.079 | STANDARD |
| Charlie Coyle: 1+ goals | 0.258 | 0.155 | 17/86 | +0.078 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.417 | 0.515 | 53/50 | +0.066 | STANDARD |
| Charlie Coyle: 1+ points | 0.510 | 0.420 | 43/59 | +0.063 | STANDARD |

**CHI @ DET** · priced 164/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 24.08, exp saves 21.14 (sd 5.78), pull risk 0.043
- CHI net: Spencer Knight (PROBABLE) exp shots 30.26, exp saves 25.92 (sd 7.0), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.285 | 0.430 | 44/58 | +0.118 | STANDARD |
| Patrick Kane: 1+ points | 0.443 | 0.550 | 56/46 | +0.080 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.228 | 0.125 | 23/98 | -0.014 | STANDARD |
| Connor Bedard: 1+ assists | 0.338 | 0.440 | 46/58 | +0.065 | STANDARD |
| Emmitt Finnie: 2+ points | 0.213 | 0.115 | 15/92 | +0.054 | STANDARD |
| Connor Bedard: 1+ points | 0.516 | 0.605 | 62/41 | +0.057 | STANDARD |

**BOS @ STL** · priced 171/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.11, exp saves 22.63 (sd 6.26), pull risk 0.06
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.06, exp saves 24.16 (sd 6.7), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 1+ assists | 0.452 | 0.540 | 55/47 | +0.060 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.372 | 0.455 | 47/56 | +0.051 | STANDARD |
| David Pastrnak: 2+ points | 0.260 | 0.340 | 35/67 | +0.055 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.297 | 0.220 | 23/79 | +0.055 | STANDARD |
| Jonatan Berggren: 1+ points | 0.405 | 0.340 | 37/69 | +0.018 | STANDARD |
| Jimmy Snuggerud: 1+ points | 0.579 | 0.520 | 54/50 | +0.022 | STANDARD |

**WSH @ NSH** · priced 167/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.24, exp saves 24.51 (sd 6.67), pull risk 0.06
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.84 (sd 6.74), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.314 | 0.235 | 26/79 | +0.040 | STANDARD |
| Tom Wilson: 1+ assists | 0.335 | 0.265 | 29/76 | +0.031 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.270 | 0.335 | 35/68 | +0.035 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.193 | 0.255 | 27/76 | +0.034 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.223 | 0.165 | 17/84 | +0.044 | STANDARD |
| Steven Stamkos: 1+ assists | 0.416 | 0.360 | 38/66 | +0.020 | STANDARD |

**MTL @ DAL** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.03, exp saves 20.94 (sd 5.96), pull risk 0.053
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.09 (sd 6.57), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.482 | 0.555 | 58/47 | +0.031 | STANDARD |
| Cole Caufield: 1+ assists | 0.321 | 0.390 | 40/62 | +0.043 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.259 | 0.190 | 21/83 | +0.037 | STANDARD |
| Mikko Rantanen: 2+ points | 0.242 | 0.310 | 33/71 | +0.034 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.365 | 0.430 | 45/59 | +0.028 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.426 | 0.490 | 51/53 | +0.027 | STANDARD |

**NYI @ MIN** · priced 174/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.41, exp saves 23.88 (sd 6.46), pull risk 0.051
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.87, exp saves 24.95 (sd 6.75), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Yakov Trenin: 1+ points | 0.315 | 0.125 | 23/98 | +0.073 | STANDARD |
| Logan Stanley: 1+ points | 0.268 | 0.120 | 22/98 | +0.036 | STANDARD |
| Ryan Hartman: 1+ assists | 0.244 | 0.115 | 21/98 | +0.022 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.281 | 0.390 | 40/62 | +0.082 | STANDARD |
| Anthony Duclair: 1+ assists | 0.228 | 0.120 | 22/98 | -0.004 | STANDARD |
| Logan Stanley: 1+ assists | 0.222 | 0.115 | 21/98 | +0.000 | STANDARD |

**BUF @ ANA** · priced 181/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.65), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 28.64, exp saves 24.45 (sd 6.9), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ points | 0.295 | 0.130 | 24/98 | +0.042 | STANDARD |
| Noah Warren: 1+ assists | 0.260 | 0.105 | 19/98 | +0.059 | STANDARD |
| A.J. Greer: 1+ goals | 0.258 | 0.140 | 15/87 | +0.099 | STANDARD |
| Tage Thompson: 1+ points | 0.527 | 0.625 | 63/38 | +0.076 | STANDARD |
| Tage Thompson: 2+ points | 0.179 | 0.275 | 29/74 | +0.068 | STANDARD |
| Alex Killorn: 1+ points | 0.451 | 0.360 | 38/66 | +0.055 | STANDARD |

**OTT @ LAK** · priced 163/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.33, exp saves 23.89 (sd 6.42), pull risk 0.048
- OTT net: Jonas Johansson (PROJECTED) exp shots 26.32, exp saves 22.72 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.300 | 0.435 | 45/58 | +0.103 | STANDARD |
| Jake Sanderson: 1+ points | 0.376 | 0.495 | 52/53 | +0.076 | STANDARD |
| Tim Stutzle: 1+ assists | 0.364 | 0.450 | 46/56 | +0.059 | STANDARD |
| Alex Laferriere: 2+ points | 0.220 | 0.135 | 18/91 | +0.030 | STANDARD |
| Jake Sanderson: 2+ points | 0.077 | 0.160 | 19/87 | +0.045 | STANDARD |
| Trevor Moore: 1+ assists | 0.310 | 0.230 | 25/79 | +0.047 | STANDARD |

**VAN @ SJS** · priced 161/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.23 (sd 6.28), pull risk 0.063
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.42, exp saves 25.08 (sd 7.0), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.418 | 0.560 | 58/46 | +0.104 | STANDARD |
| Macklin Celebrini: 2+ points | 0.327 | 0.460 | 47/55 | +0.105 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.281 | 0.410 | 43/61 | +0.093 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.465 | 0.585 | 59/42 | +0.098 | STANDARD |
| Ivar Stenberg: 1+ goals | 0.191 | 0.295 | 30/71 | +0.084 | STANDARD |
| Ivar Stenberg: 2+ points | 0.103 | 0.200 | 24/84 | +0.047 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
