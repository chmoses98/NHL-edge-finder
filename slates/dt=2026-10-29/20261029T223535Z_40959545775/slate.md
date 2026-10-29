# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T22:35:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4649 · contracts joined: 2505 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2230, 'CANNOT_TRUST_INPUTS': 275}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 348, 'game_early_goal': 11, 'first_goal': 403, 'game_winner': 22, 'player_goals': 701, 'game_overtime': 11, 'player_points': 472, 'goalie_saves': 20, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-10m | 0.646 | 0.354 | 0.172 | 5.62 | 3.25 | 2.37 | 221 (25/196) | CONFIRMED/CONFIRMED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-10m | 0.468 | 0.532 | 0.170 | 6.70 | 3.25 | 3.45 | 231 (25/206) | CONFIRMED/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-10m | 0.656 | 0.344 | 0.172 | 5.84 | 3.40 | 2.44 | 228 (25/203) | PROBABLE/CONFIRMED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-30m | 0.597 | 0.403 | 0.183 | 5.64 | 3.12 | 2.52 | 235 (25/210) | CONFIRMED/PROBABLE |
| BOS @ STL | 2026-10-30T00:00:00Z | T-60m | 0.491 | 0.509 | 0.182 | 5.80 | 2.88 | 2.92 | 238 (25/213) | CONFIRMED/CONFIRMED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-60m | 0.539 | 0.461 | 0.170 | 6.70 | 3.47 | 3.22 | 223 (25/198) | CONFIRMED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-60m | 0.599 | 0.401 | 0.179 | 5.75 | 3.17 | 2.58 | 214 (25/189) | CONFIRMED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-60m | 0.597 | 0.403 | 0.179 | 5.66 | 3.12 | 2.54 | 231 (25/206) | CONFIRMED/CONFIRMED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-3h | 0.499 | 0.501 | 0.169 | 6.44 | 3.21 | 3.22 | 237 (25/212) | PROJECTED/PROBABLE |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-3h | 0.517 | 0.483 | 0.178 | 6.13 | 3.12 | 3.01 | 227 (25/202) | CONFIRMED/CONFIRMED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-3h | 0.591 | 0.409 | 0.160 | 7.13 | 3.87 | 3.25 | 220 (25/195) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.461 | 0.565 | 0.544 | 57 | 44 |  | +0.082 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.693 | 0.775 | 0.760 | 78 | 23 |  | +0.065 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.349 | 0.435 | 0.417 | 44 | 57 |  | +0.064 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.419 | 0.510 | 0.492 | 52 | 50 |  | +0.064 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.799 | 0.865 | 0.853 | 87 | 14 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.499 | 0.425 | 0.440 | 43 | 58 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.501 | 0.575 | 0.560 | 58 | 43 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.392 | 0.465 | 0.450 | 47 | 54 |  | +0.050 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.413 | 0.490 | 0.474 | 50 | 52 |  | +0.050 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.698 | 0.765 | 0.753 | 77 | 24 |  | +0.049 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.227 | 0.305 | 0.288 | 32 | 71 |  | +0.049 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.628 | 0.700 | 0.686 | 71 | 31 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.711 | 0.775 | 0.763 | 78 | 23 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.650 | 0.720 | 0.707 | 73 | 29 |  | +0.046 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.220 | 0.285 | 0.271 | 29 | 72 |  | +0.046 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.289 | 0.355 | 0.341 | 36 | 65 |  | +0.045 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.185 | 0.245 | 0.232 | 25 | 76 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.398 | 0.335 | 0.347 | 34 | 67 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CBJCAR-5 | game_total | 0.727 | 0.785 | 0.774 | 79 | 22 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.274 | 0.335 | 0.322 | 34 | 67 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.801 | 0.855 | 0.845 | 86 | 15 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-6 | game_total | 0.492 | 0.555 | 0.543 | 56 | 45 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.483 | 0.545 | 0.533 | 55 | 46 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.256 | 0.320 | 0.307 | 33 | 69 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.484 | 0.545 | 0.533 | 55 | 46 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-5 | game_total | 0.699 | 0.760 | 0.748 | 77 | 25 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.454 | 0.515 | 0.503 | 52 | 49 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.405 | 0.465 | 0.453 | 47 | 54 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.355 | 0.415 | 0.403 | 42 | 59 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.465 | 0.525 | 0.513 | 53 | 48 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.115 | 0.123 | 12 | 89 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-6 | game_total | 0.467 | 0.525 | 0.513 | 53 | 48 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.231 | 0.295 | 0.281 | 31 | 72 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29MTLDAL-DAL3 | game_spread | 0.221 | 0.275 | 0.264 | 28 | 73 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.875 | 0.866 | 88 | 13 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-5 | game_total | 0.723 | 0.775 | 0.765 | 78 | 23 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.700 | 0.645 | 0.656 | 65 | 36 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.470 | 0.525 | 0.514 | 53 | 48 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.674 | 0.725 | 0.715 | 73 | 28 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CBJCAR-4 | game_total | 0.819 | 0.865 | 0.857 | 87 | 14 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.623 | 0.675 | 0.665 | 68 | 33 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.371 | 0.425 | 0.414 | 43 | 58 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.421 | 0.475 | 0.464 | 48 | 53 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BOSSTL-7 | game_total | 0.382 | 0.435 | 0.424 | 44 | 57 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-4 | game_total | 0.800 | 0.850 | 0.841 | 86 | 16 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.101 | 0.145 | 0.135 | 15 | 86 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN3 | team_total | 0.614 | 0.675 | 0.663 | 69 | 34 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CBJCAR-6 | game_total | 0.503 | 0.555 | 0.545 | 56 | 45 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.256 | 0.310 | 0.299 | 32 | 70 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.483 | 0.535 | 0.525 | 54 | 47 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.855 | 0.895 | 0.888 | 90 | 11 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI2 | team_total | 0.708 | 0.755 | 0.746 | 76 | 25 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.355 | 0.405 | 0.395 | 41 | 60 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.597 | 0.645 | 0.636 | 65 | 36 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29WPGTB-TB2 | game_spread | 0.406 | 0.455 | 0.445 | 46 | 55 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.597 | 0.645 | 0.636 | 65 | 36 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.594 | 0.545 | 0.555 | 55 | 46 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.836 | 0.885 | 0.876 | 90 | 13 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-WPG3 | team_total | 0.427 | 0.480 | 0.469 | 49 | 53 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29NYIMIN-7 | game_total | 0.358 | 0.405 | 0.395 | 41 | 60 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29BOSSTL-STL4 | team_total | 0.338 | 0.385 | 0.375 | 39 | 62 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.298 | 0.250 | 0.259 | 26 | 76 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET4 | team_total | 0.389 | 0.435 | 0.426 | 44 | 57 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.471 | 0.425 | 0.434 | 43 | 58 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.185 | 0.230 | 0.220 | 24 | 78 |  | +0.023 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN5 | team_total | 0.204 | 0.260 | 0.248 | 28 | 76 |  | +0.023 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.243 | 0.205 | 0.212 | 21 | 80 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29WPGTB-WPG4 | team_total | 0.225 | 0.265 | 0.257 | 27 | 74 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL5 | team_total | 0.216 | 0.265 | 0.255 | 28 | 75 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26OCT29CHIDET-CHI2 | game_spread | 0.197 | 0.235 | 0.227 | 24 | 77 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.121 | 0.155 | 0.148 | 16 | 85 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.115 | 0.075 | 0.082 | 9 | 94 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26OCT29CHIDET-9 | game_total | 0.122 | 0.155 | 0.148 | 16 | 85 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL2 | team_total | 0.822 | 0.855 | 0.849 | 86 | 15 |  | +0.019 | CANNOT_TRUST_INPUTS |

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
| NYI @ MIN | 0.597 | 0.560 | 0.179 | 0.215 | 5.66 | 6.10 | 0.991/0.948 | KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3 +0.080 |
| BUF @ ANA | 0.499 | 0.562 | 0.169 | 0.211 | 6.44 | 6.67 | 1.036/1.000 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.073 |
| OTT @ LAK | 0.517 | 0.529 | 0.178 | 0.224 | 6.13 | 6.01 | 0.996/1.040 | KXNHLTOTAL-26OCT29OTTLA-6 -0.027 |
| VAN @ SJS | 0.591 | 0.558 | 0.160 | 0.212 | 7.13 | 6.61 | 1.040/1.034 | KXNHLTOTAL-26OCT29VANSJ-8 -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 24.76, exp saves 21.92 (sd 5.98), pull risk 0.039
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.88, exp saves 24.51 (sd 6.81), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.502 | 0.625 | 63/38 | +0.101 | STANDARD |
| Elias Salomonsson: 1+ points | 0.211 | 0.300 | 32/72 | +0.055 | STANDARD |
| John Carlson: 1+ points | 0.386 | 0.470 | 49/55 | +0.046 | STANDARD |
| Nikita Kucherov: 2+ points | 0.330 | 0.410 | 42/60 | +0.054 | STANDARD |
| Charle-Edouard D'Astous: 1+ points | 0.406 | 0.480 | 49/53 | +0.047 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.159 | 0.230 | 25/79 | +0.039 | STANDARD |

**UTA @ PIT** · priced 162/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 27.0, exp saves 23.28 (sd 6.55), pull risk 0.075
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.13, exp saves 23.31 (sd 6.54), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ points | 0.681 | 0.545 | 55/46 | +0.114 | STANDARD |
| Rickard Rakell: 1+ goals | 0.435 | 0.310 | 32/70 | +0.100 | STANDARD |
| Rickard Rakell: 2+ points | 0.313 | 0.190 | 20/82 | +0.102 | STANDARD |
| Kaedan Korczak: 1+ points | 0.317 | 0.205 | 28/87 | +0.023 | STANDARD |
| Nick Robertson: 1+ goals | 0.251 | 0.150 | 16/86 | +0.081 | STANDARD |
| Connor Dewar: 1+ goals | 0.223 | 0.125 | 13/88 | +0.085 | STANDARD |

**CBJ @ CAR** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.87, exp saves 20.86 (sd 5.9), pull risk 0.051
- CBJ net: Jet Greaves (CONFIRMED) exp shots 30.96, exp saves 26.54 (sd 7.13), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.539 | 0.655 | 66/35 | +0.095 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.351 | 0.455 | 46/55 | +0.082 | STANDARD |
| Sebastian Aho: 1+ assists | 0.362 | 0.465 | 47/54 | +0.081 | STANDARD |
| Seth Jarvis: 1+ assists | 0.245 | 0.345 | 35/66 | +0.079 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.417 | 0.515 | 52/49 | +0.076 | STANDARD |
| Sebastian Aho: 2+ points | 0.183 | 0.280 | 29/73 | +0.073 | STANDARD |

**CHI @ DET** · priced 165/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 24.08, exp saves 21.14 (sd 5.78), pull risk 0.043
- CHI net: Spencer Knight (PROBABLE) exp shots 30.26, exp saves 25.92 (sd 7.0), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.285 | 0.435 | 44/57 | +0.128 | STANDARD |
| Patrick Kane: 1+ points | 0.443 | 0.550 | 56/46 | +0.080 | STANDARD |
| Connor Bedard: 1+ assists | 0.338 | 0.445 | 46/57 | +0.075 | STANDARD |
| Connor Bedard: 1+ points | 0.516 | 0.610 | 62/40 | +0.067 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.402 | 0.315 | 32/69 | +0.067 | STANDARD |
| John Gibson: 22+ saves | 0.458 | 0.375 | 39/64 | +0.052 |  |

**BOS @ STL** · priced 182/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.11, exp saves 22.63 (sd 6.26), pull risk 0.06
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.06, exp saves 24.16 (sd 6.7), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Hampus Lindholm: 1+ points | 0.334 | 0.135 | 26/99 | +0.060 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.283 | 0.120 | 23/99 | +0.041 | STANDARD |
| Casey Mittelstadt: 1+ points | 0.391 | 0.240 | 35/87 | +0.025 | STANDARD |
| Marat Khusnutdinov: 1+ points | 0.317 | 0.170 | 31/97 | -0.008 | STANDARD |
| Casey Mittelstadt: 1+ assists | 0.259 | 0.135 | 25/98 | -0.004 | STANDARD |
| Mason Lohrei: 1+ assists | 0.226 | 0.125 | 24/99 | -0.027 | STANDARD |

**WSH @ NSH** · priced 165/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.24, exp saves 24.51 (sd 6.67), pull risk 0.06
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.84 (sd 6.74), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.314 | 0.230 | 26/80 | +0.040 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.193 | 0.265 | 27/74 | +0.054 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.270 | 0.340 | 35/67 | +0.045 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.223 | 0.165 | 17/84 | +0.044 | STANDARD |
| Tom Wilson: 1+ assists | 0.335 | 0.280 | 29/73 | +0.031 | STANDARD |
| Jordan Kyrou: 1+ points | 0.458 | 0.510 | 52/50 | +0.025 | STANDARD |

**MTL @ DAL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.03, exp saves 20.94 (sd 5.96), pull risk 0.053
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.09 (sd 6.57), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 2+ points | 0.242 | 0.325 | 34/69 | +0.053 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.565 | 57/44 | +0.061 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.448 | 0.530 | 54/48 | +0.055 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.259 | 0.185 | 21/84 | +0.037 | STANDARD |
| Mikko Rantanen: 1+ points | 0.609 | 0.680 | 69/33 | +0.045 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.365 | 0.430 | 44/58 | +0.038 | STANDARD |

**NYI @ MIN** · priced 175/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.41, exp saves 23.84 (sd 6.47), pull risk 0.053
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.87, exp saves 24.88 (sd 6.82), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jesper Wallstedt: 22+ saves | 0.641 | 0.480 | 57/61 | +0.054 |  |
| Ryan Hartman: 1+ assists | 0.245 | 0.110 | 20/98 | +0.034 | STANDARD |
| Yakov Trenin: 1+ points | 0.312 | 0.210 | 25/83 | +0.048 | STANDARD |
| Yakov Trenin: 1+ assists | 0.197 | 0.100 | 18/98 | +0.007 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.288 | 0.380 | 39/63 | +0.066 | STANDARD |
| Matt Boldy: 2+ points | 0.244 | 0.335 | 34/67 | +0.071 | STANDARD |

**BUF @ ANA** · priced 176/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.5), pull risk 0.06
- BUF net: Colten Ellis (PROBABLE) exp shots 28.64, exp saves 24.47 (sd 6.89), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ points | 0.296 | 0.130 | 24/98 | +0.043 | STANDARD |
| Noah Warren: 1+ assists | 0.260 | 0.115 | 21/98 | +0.039 | STANDARD |
| A.J. Greer: 1+ goals | 0.262 | 0.135 | 15/88 | +0.103 | STANDARD |
| Alex Killorn: 1+ points | 0.454 | 0.350 | 37/67 | +0.068 | STANDARD |
| Lukas Dostal: 27+ saves | 0.334 | 0.435 | 47/60 | +0.049 |  |
| Colten Ellis: 25+ saves | 0.497 | 0.405 | 46/65 | +0.019 |  |

**OTT @ LAK** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.33, exp saves 23.88 (sd 6.44), pull risk 0.051
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.32, exp saves 22.76 (sd 6.28), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.308 | 0.430 | 44/58 | +0.095 | STANDARD |
| Jake Sanderson: 1+ points | 0.388 | 0.500 | 52/52 | +0.075 | STANDARD |
| Thomas Chabot: 1+ points | 0.285 | 0.370 | 39/65 | +0.049 | STANDARD |
| Thomas Chabot: 1+ assists | 0.210 | 0.290 | 31/73 | +0.047 | STANDARD |
| Jake Sanderson: 2+ points | 0.086 | 0.165 | 19/86 | +0.046 | STANDARD |
| Trevor Moore: 1+ assists | 0.288 | 0.215 | 23/80 | +0.045 | STANDARD |

**VAN @ SJS** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.3 (sd 6.23), pull risk 0.06
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.42, exp saves 25.06 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.425 | 0.575 | 58/43 | +0.128 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.472 | 0.595 | 60/41 | +0.101 | STANDARD |
| Macklin Celebrini: 2+ points | 0.333 | 0.455 | 47/56 | +0.090 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.284 | 0.400 | 41/61 | +0.089 | STANDARD |
| Ivar Stenberg: 2+ points | 0.107 | 0.215 | 23/80 | +0.082 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.134 | 0.225 | 24/79 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
