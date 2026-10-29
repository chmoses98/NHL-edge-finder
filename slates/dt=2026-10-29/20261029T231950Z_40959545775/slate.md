# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T23:19:50Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 8 · markets on board: 4659 · contracts joined: 1825 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1625, 'CANNOT_TRUST_INPUTS': 200}
families: {'period_winner': 72, 'period_spread': 48, 'period_total': 72, 'player_assists': 256, 'game_early_goal': 8, 'first_goal': 291, 'game_winner': 16, 'player_goals': 506, 'game_overtime': 8, 'player_points': 349, 'goalie_saves': 15, 'game_spread': 32, 'team_total': 80, 'game_total': 72}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ DET | 2026-10-29T23:30:00Z | T-10m | 0.597 | 0.403 | 0.183 | 5.64 | 3.12 | 2.52 | 235 (25/210) | CONFIRMED/PROBABLE |
| BOS @ STL | 2026-10-30T00:00:00Z | T-30m | 0.491 | 0.509 | 0.182 | 5.80 | 2.88 | 2.92 | 238 (25/213) | CONFIRMED/CONFIRMED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-30m | 0.539 | 0.461 | 0.170 | 6.70 | 3.47 | 3.22 | 223 (25/198) | CONFIRMED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-30m | 0.599 | 0.401 | 0.179 | 5.75 | 3.17 | 2.58 | 214 (25/189) | CONFIRMED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-30m | 0.597 | 0.403 | 0.179 | 5.66 | 3.12 | 2.54 | 231 (25/206) | CONFIRMED/CONFIRMED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-90m | 0.499 | 0.501 | 0.169 | 6.44 | 3.21 | 3.22 | 237 (25/212) | PROJECTED/PROBABLE |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-90m | 0.517 | 0.483 | 0.178 | 6.13 | 3.12 | 3.01 | 227 (25/202) | CONFIRMED/CONFIRMED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-90m | 0.591 | 0.409 | 0.160 | 7.13 | 3.87 | 3.25 | 220 (25/195) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.499 | 0.425 | 0.440 | 43 | 58 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.501 | 0.575 | 0.560 | 58 | 43 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.413 | 0.490 | 0.474 | 50 | 52 |  | +0.050 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.698 | 0.765 | 0.753 | 77 | 24 |  | +0.049 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-5 | game_total | 0.699 | 0.765 | 0.753 | 77 | 24 |  | +0.049 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.628 | 0.700 | 0.686 | 71 | 31 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.711 | 0.775 | 0.763 | 78 | 23 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.220 | 0.285 | 0.271 | 29 | 72 |  | +0.046 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.289 | 0.355 | 0.341 | 36 | 65 |  | +0.045 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.398 | 0.335 | 0.347 | 34 | 67 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.801 | 0.855 | 0.845 | 86 | 15 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.392 | 0.460 | 0.446 | 47 | 55 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-6 | game_total | 0.492 | 0.555 | 0.543 | 56 | 45 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.483 | 0.545 | 0.533 | 55 | 46 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.484 | 0.545 | 0.533 | 55 | 46 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.405 | 0.470 | 0.457 | 48 | 54 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.355 | 0.415 | 0.403 | 42 | 59 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.465 | 0.525 | 0.513 | 53 | 48 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.115 | 0.123 | 12 | 89 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-6 | game_total | 0.467 | 0.525 | 0.513 | 53 | 48 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.231 | 0.295 | 0.281 | 31 | 72 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-5 | game_total | 0.723 | 0.775 | 0.765 | 78 | 23 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.470 | 0.525 | 0.514 | 53 | 48 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.623 | 0.675 | 0.665 | 68 | 33 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.371 | 0.425 | 0.414 | 43 | 58 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-4 | game_total | 0.800 | 0.850 | 0.841 | 86 | 16 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN3 | team_total | 0.614 | 0.675 | 0.663 | 69 | 34 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.355 | 0.405 | 0.395 | 41 | 60 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.240 | 0.250 | 25 | 77 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.597 | 0.645 | 0.636 | 65 | 36 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.597 | 0.650 | 0.640 | 66 | 36 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.594 | 0.545 | 0.555 | 55 | 46 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN2 | team_total | 0.815 | 0.855 | 0.848 | 86 | 15 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-7 | game_total | 0.358 | 0.405 | 0.395 | 41 | 60 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29MTLDAL-DAL3 | game_spread | 0.221 | 0.265 | 0.256 | 27 | 74 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BOSSTL-STL4 | team_total | 0.338 | 0.385 | 0.375 | 39 | 62 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.298 | 0.250 | 0.259 | 26 | 76 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.870 | 0.862 | 88 | 14 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.700 | 0.655 | 0.664 | 66 | 35 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.185 | 0.230 | 0.220 | 24 | 78 |  | +0.023 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN5 | team_total | 0.204 | 0.260 | 0.248 | 28 | 76 |  | +0.023 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.243 | 0.205 | 0.212 | 21 | 80 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-7 | game_total | 0.382 | 0.425 | 0.416 | 43 | 58 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL5 | team_total | 0.216 | 0.265 | 0.255 | 28 | 75 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29CHIDET-CHI2 | game_spread | 0.197 | 0.235 | 0.227 | 24 | 77 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-8 | game_total | 0.188 | 0.225 | 0.217 | 23 | 78 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-9 | game_total | 0.122 | 0.155 | 0.148 | 16 | 85 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL2 | team_total | 0.822 | 0.855 | 0.849 | 86 | 15 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.266 | 0.305 | 0.297 | 31 | 70 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WSHNSH-8 | game_total | 0.334 | 0.295 | 0.303 | 30 | 71 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH5 | team_total | 0.282 | 0.240 | 0.248 | 25 | 77 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI2 | team_total | 0.708 | 0.750 | 0.742 | 76 | 26 |  | +0.018 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH3 | team_total | 0.674 | 0.635 | 0.643 | 64 | 37 |  | +0.018 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29WSHNSH-WSH3 | game_spread | 0.161 | 0.195 | 0.188 | 20 | 81 |  | +0.018 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-8 | game_total | 0.200 | 0.240 | 0.232 | 25 | 77 |  | +0.017 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.239 | 0.205 | 0.211 | 21 | 80 |  | +0.017 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.403 | 0.365 | 0.373 | 37 | 64 |  | +0.017 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI4 | team_total | 0.259 | 0.300 | 0.292 | 31 | 71 |  | +0.016 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.106 | 0.145 | 0.136 | 16 | 87 |  | +0.016 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-LA2 | game_spread | 0.299 | 0.260 | 0.268 | 27 | 75 |  | +0.015 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA3 | team_total | 0.611 | 0.575 | 0.582 | 58 | 43 |  | +0.014 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET4 | team_total | 0.389 | 0.430 | 0.422 | 44 | 58 |  | +0.014 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-9 | game_total | 0.137 | 0.165 | 0.159 | 17 | 84 |  | +0.014 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.471 | 0.430 | 0.438 | 44 | 58 |  | +0.014 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA2 | team_total | 0.815 | 0.780 | 0.787 | 79 | 23 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-8 | game_total | 0.291 | 0.325 | 0.318 | 33 | 68 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BOSSTL-STL3 | team_total | 0.560 | 0.600 | 0.592 | 61 | 41 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29WSHNSH-WSH2 | game_spread | 0.263 | 0.295 | 0.288 | 30 | 71 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH6 | team_total | 0.140 | 0.105 | 0.111 | 12 | 91 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN3 | team_total | 0.629 | 0.595 | 0.602 | 60 | 41 |  | +0.013 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WSHNSH-7 | game_total | 0.529 | 0.495 | 0.502 | 50 | 51 |  | +0.012 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29WSHNSH-NSH | game_winner | 0.539 | 0.505 | 0.512 | 51 | 50 |  | +0.012 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29WSHNSH-WSH | game_winner | 0.461 | 0.495 | 0.488 | 50 | 51 |  | +0.012 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-4 | game_total | 0.819 | 0.850 | 0.844 | 86 | 16 |  | +0.012 | CANNOT_TRUST_INPUTS |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ DET | 0.597 | 0.605 | 0.183 | 0.215 | 5.64 | 6.07 | 0.995/0.996 | KXNHLTOTAL-26OCT29CHIDET-7 +0.073 |
| BOS @ STL | 0.491 | 0.528 | 0.182 | 0.215 | 5.80 | 6.29 | 0.977/0.956 | KXNHLTOTAL-26OCT29BOSSTL-7 +0.088 |
| WSH @ NSH | 0.539 | 0.536 | 0.170 | 0.216 | 6.70 | 6.43 | 1.005/0.993 | KXNHLTOTAL-26OCT29WSHNSH-6 -0.047 |
| MTL @ DAL | 0.599 | 0.562 | 0.179 | 0.218 | 5.75 | 6.10 | 0.995/0.943 | KXNHLTEAMTOTAL-26OCT29MTLDAL-MTL3 +0.072 |
| NYI @ MIN | 0.597 | 0.560 | 0.179 | 0.215 | 5.66 | 6.10 | 0.991/0.948 | KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3 +0.080 |
| BUF @ ANA | 0.499 | 0.562 | 0.169 | 0.211 | 6.44 | 6.67 | 1.036/1.000 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.073 |
| OTT @ LAK | 0.517 | 0.529 | 0.178 | 0.224 | 6.13 | 6.01 | 0.996/1.040 | KXNHLTOTAL-26OCT29OTTLA-6 -0.027 |
| VAN @ SJS | 0.591 | 0.558 | 0.160 | 0.212 | 7.13 | 6.61 | 1.040/1.034 | KXNHLTOTAL-26OCT29VANSJ-8 -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ DET** · priced 165/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 24.08, exp saves 21.14 (sd 5.78), pull risk 0.043
- CHI net: Spencer Knight (PROBABLE) exp shots 30.26, exp saves 25.92 (sd 7.0), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.285 | 0.435 | 44/57 | +0.128 | STANDARD |
| Patrick Kane: 1+ points | 0.443 | 0.550 | 56/46 | +0.080 | STANDARD |
| Connor Bedard: 1+ assists | 0.338 | 0.445 | 46/57 | +0.075 | STANDARD |
| Connor Bedard: 1+ points | 0.516 | 0.610 | 63/41 | +0.057 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.402 | 0.315 | 32/69 | +0.067 | STANDARD |
| Lucas Raymond: 1+ assists | 0.390 | 0.475 | 48/53 | +0.063 | STANDARD |

**BOS @ STL** · priced 182/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.11, exp saves 22.63 (sd 6.26), pull risk 0.06
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.06, exp saves 24.16 (sd 6.7), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 1+ assists | 0.452 | 0.550 | 56/46 | +0.070 | STANDARD |
| Hampus Lindholm: 1+ points | 0.334 | 0.240 | 26/78 | +0.060 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.372 | 0.465 | 47/54 | +0.071 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.283 | 0.200 | 23/83 | +0.041 | STANDARD |
| David Pastrnak: 2+ points | 0.260 | 0.340 | 35/67 | +0.055 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.297 | 0.220 | 24/80 | +0.044 | STANDARD |

**WSH @ NSH** · priced 165/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.24, exp saves 24.51 (sd 6.67), pull risk 0.06
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.84 (sd 6.74), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.314 | 0.230 | 25/79 | +0.051 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.193 | 0.265 | 27/74 | +0.054 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.270 | 0.340 | 35/67 | +0.045 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.223 | 0.165 | 17/84 | +0.044 | STANDARD |
| Jordan Kyrou: 1+ points | 0.458 | 0.515 | 52/49 | +0.035 | STANDARD |
| Tom Wilson: 1+ assists | 0.335 | 0.280 | 29/73 | +0.031 | STANDARD |

**MTL @ DAL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.03, exp saves 20.94 (sd 5.96), pull risk 0.053
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.09 (sd 6.57), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.242 | 0.330 | 34/68 | +0.063 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.565 | 57/44 | +0.061 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.448 | 0.530 | 54/48 | +0.055 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.259 | 0.180 | 20/84 | +0.048 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.365 | 0.430 | 44/58 | +0.038 | STANDARD |
| Cole Caufield: 1+ assists | 0.321 | 0.385 | 39/62 | +0.043 | STANDARD |

**NYI @ MIN** · priced 175/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.41, exp saves 23.84 (sd 6.47), pull risk 0.053
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.87, exp saves 24.88 (sd 6.82), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.288 | 0.385 | 39/62 | +0.076 | STANDARD |
| Matt Boldy: 2+ points | 0.244 | 0.335 | 34/67 | +0.071 | STANDARD |
| Jesper Wallstedt: 22+ saves | 0.641 | 0.555 | 59/48 | +0.035 |  |
| Matt Boldy: 1+ assists | 0.410 | 0.495 | 50/51 | +0.062 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.646 | 0.730 | 74/28 | +0.060 | STANDARD |
| Max Shabanov: 1+ points | 0.377 | 0.460 | 47/55 | +0.056 | STANDARD |

**BUF @ ANA** · priced 176/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.5), pull risk 0.06
- BUF net: Colten Ellis (PROBABLE) exp shots 28.64, exp saves 24.47 (sd 6.89), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ points | 0.296 | 0.130 | 24/98 | +0.043 | STANDARD |
| Noah Warren: 1+ assists | 0.260 | 0.115 | 21/98 | +0.039 | STANDARD |
| A.J. Greer: 1+ goals | 0.262 | 0.135 | 15/88 | +0.103 | STANDARD |
| Lukas Dostal: 27+ saves | 0.334 | 0.460 | 50/58 | +0.069 |  |
| Alex Killorn: 1+ points | 0.454 | 0.350 | 37/67 | +0.068 | STANDARD |
| Jackson LaCombe: 2+ assists | 0.207 | 0.120 | 16/92 | +0.038 | STANDARD |

**OTT @ LAK** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.33, exp saves 23.88 (sd 6.44), pull risk 0.051
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.32, exp saves 22.76 (sd 6.28), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.308 | 0.435 | 44/57 | +0.105 | STANDARD |
| Jake Sanderson: 1+ points | 0.388 | 0.505 | 52/51 | +0.085 | STANDARD |
| Thomas Chabot: 1+ points | 0.285 | 0.375 | 39/64 | +0.059 | STANDARD |
| Thomas Chabot: 1+ assists | 0.210 | 0.290 | 31/73 | +0.047 | STANDARD |
| Jake Sanderson: 2+ points | 0.086 | 0.165 | 19/86 | +0.046 | STANDARD |
| Tim Stutzle: 1+ points | 0.557 | 0.635 | 64/37 | +0.056 | STANDARD |

**VAN @ SJS** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.3 (sd 6.23), pull risk 0.06
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.42, exp saves 25.06 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.425 | 0.575 | 58/43 | +0.128 | STANDARD |
| Macklin Celebrini: 2+ points | 0.333 | 0.460 | 47/55 | +0.099 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.472 | 0.595 | 60/41 | +0.101 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.284 | 0.400 | 41/61 | +0.089 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.134 | 0.245 | 25/76 | +0.094 | STANDARD |
| Ivar Stenberg: 2+ points | 0.107 | 0.210 | 23/81 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
