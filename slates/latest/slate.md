# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T19:32:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4541 · contracts joined: 2495 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2220, 'OK': 172, 'NO_EDGE': 103}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 344, 'game_early_goal': 11, 'first_goal': 404, 'game_winner': 22, 'player_goals': 703, 'game_overtime': 11, 'player_points': 465, 'goalie_saves': 18, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-3h | 0.646 | 0.354 | 0.172 | 5.62 | 3.25 | 2.37 | 221 (25/196) | CONFIRMED/CONFIRMED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-3h | 0.468 | 0.532 | 0.170 | 6.70 | 3.25 | 3.45 | 231 (25/206) | CONFIRMED/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-3h | 0.656 | 0.344 | 0.172 | 5.84 | 3.40 | 2.44 | 228 (25/203) | PROBABLE/CONFIRMED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-3h | 0.597 | 0.403 | 0.183 | 5.64 | 3.12 | 2.52 | 235 (25/210) | CONFIRMED/PROBABLE |
| BOS @ STL | 2026-10-30T00:00:00Z | T-3h | 0.491 | 0.509 | 0.182 | 5.80 | 2.88 | 2.92 | 227 (25/202) | CONFIRMED/CONFIRMED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-3h | 0.539 | 0.461 | 0.170 | 6.70 | 3.47 | 3.22 | 223 (25/198) | CONFIRMED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-3h | 0.599 | 0.401 | 0.179 | 5.75 | 3.17 | 2.58 | 214 (25/189) | CONFIRMED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-3h | 0.583 | 0.417 | 0.181 | 5.72 | 3.12 | 2.61 | 230 (25/205) | PROJECTED/CONFIRMED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-6h | 0.499 | 0.501 | 0.169 | 6.44 | 3.21 | 3.22 | 239 (25/214) | PROJECTED/PROBABLE |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-6h | 0.517 | 0.483 | 0.178 | 6.13 | 3.12 | 3.01 | 227 (25/202) | CONFIRMED/CONFIRMED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-6h | 0.591 | 0.409 | 0.160 | 7.13 | 3.87 | 3.25 | 220 (25/195) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.461 | 0.565 | 0.544 | 57 | 44 | no | +0.082 | OK |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.693 | 0.785 | 0.768 | 79 | 22 | no | +0.075 | OK |
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.349 | 0.445 | 0.425 | 45 | 56 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.419 | 0.510 | 0.492 | 52 | 50 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.390 | 0.465 | 0.450 | 47 | 54 | no | +0.052 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.499 | 0.425 | 0.440 | 43 | 58 | yes | +0.052 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.501 | 0.575 | 0.560 | 58 | 43 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.413 | 0.495 | 0.478 | 51 | 52 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.227 | 0.305 | 0.288 | 32 | 71 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.836 | 0.895 | 0.885 | 90 | 11 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.650 | 0.720 | 0.707 | 73 | 29 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.289 | 0.355 | 0.341 | 36 | 65 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.398 | 0.335 | 0.347 | 34 | 67 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.799 | 0.860 | 0.849 | 87 | 15 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.214 | 0.280 | 0.266 | 29 | 73 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.274 | 0.335 | 0.322 | 34 | 67 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-6 | game_total | 0.492 | 0.555 | 0.543 | 56 | 45 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.483 | 0.545 | 0.533 | 55 | 46 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.256 | 0.320 | 0.307 | 33 | 69 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.698 | 0.760 | 0.748 | 77 | 25 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.454 | 0.515 | 0.503 | 52 | 49 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.355 | 0.415 | 0.403 | 42 | 59 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.465 | 0.525 | 0.513 | 53 | 48 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.628 | 0.695 | 0.682 | 71 | 32 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.347 | 0.405 | 0.393 | 41 | 60 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.711 | 0.770 | 0.759 | 78 | 24 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.231 | 0.295 | 0.281 | 31 | 72 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.875 | 0.866 | 88 | 13 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.471 | 0.415 | 0.426 | 42 | 59 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-5 | game_total | 0.704 | 0.760 | 0.749 | 77 | 25 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.809 | 0.860 | 0.851 | 87 | 15 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.674 | 0.730 | 0.719 | 74 | 28 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.421 | 0.475 | 0.464 | 48 | 53 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-7 | game_total | 0.382 | 0.435 | 0.424 | 44 | 57 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-6 | game_total | 0.482 | 0.535 | 0.524 | 54 | 47 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN3 | team_total | 0.613 | 0.680 | 0.667 | 70 | 34 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-5 | game_total | 0.727 | 0.780 | 0.770 | 79 | 23 | no | +0.031 | OK |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.583 | 0.635 | 0.625 | 64 | 37 | no | +0.031 | OK |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.417 | 0.365 | 0.375 | 37 | 64 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.101 | 0.150 | 0.139 | 16 | 86 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.801 | 0.850 | 0.841 | 86 | 16 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-6 | game_total | 0.503 | 0.555 | 0.545 | 56 | 45 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.256 | 0.310 | 0.299 | 32 | 70 | no | +0.030 | OK |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.517 | 0.465 | 0.475 | 47 | 54 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH5 | team_total | 0.282 | 0.230 | 0.240 | 24 | 78 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.484 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.855 | 0.895 | 0.888 | 90 | 11 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN2 | team_total | 0.813 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.405 | 0.465 | 0.453 | 48 | 55 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.239 | 0.185 | 0.195 | 20 | 83 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT29NYIMIN-4 | game_total | 0.803 | 0.845 | 0.837 | 85 | 16 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB2 | game_spread | 0.406 | 0.455 | 0.445 | 46 | 55 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.594 | 0.545 | 0.555 | 55 | 46 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.106 | 0.150 | 0.140 | 16 | 86 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.298 | 0.250 | 0.259 | 26 | 76 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-7 | game_total | 0.389 | 0.435 | 0.426 | 44 | 57 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-5 | game_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.700 | 0.650 | 0.660 | 66 | 36 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH6 | team_total | 0.140 | 0.100 | 0.107 | 11 | 91 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.185 | 0.230 | 0.220 | 24 | 78 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT29WSHNSH-WSH2 | game_spread | 0.263 | 0.305 | 0.296 | 31 | 70 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.470 | 0.520 | 0.510 | 53 | 49 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN5 | team_total | 0.205 | 0.255 | 0.245 | 27 | 76 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-4 | game_total | 0.819 | 0.860 | 0.853 | 87 | 15 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.623 | 0.670 | 0.661 | 68 | 34 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT29CHIDET-CHI2 | game_spread | 0.197 | 0.235 | 0.227 | 24 | 77 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.121 | 0.160 | 0.151 | 17 | 85 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.115 | 0.075 | 0.082 | 9 | 94 | yes | +0.020 | OK |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.483 | 0.525 | 0.517 | 53 | 48 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29CHIDET-9 | game_total | 0.122 | 0.155 | 0.148 | 16 | 85 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.266 | 0.305 | 0.297 | 31 | 70 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-8 | game_total | 0.334 | 0.295 | 0.303 | 30 | 71 | yes | +0.019 | OK |

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
| BUF @ ANA | 0.499 | 0.562 | 0.169 | 0.211 | 6.44 | 6.67 | 1.036/1.000 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.073 |
| OTT @ LAK | 0.517 | 0.529 | 0.178 | 0.224 | 6.13 | 6.01 | 0.996/1.040 | KXNHLTOTAL-26OCT29OTTLA-6 -0.027 |
| VAN @ SJS | 0.591 | 0.558 | 0.160 | 0.212 | 7.13 | 6.61 | 1.040/1.034 | KXNHLTOTAL-26OCT29VANSJ-8 -0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9286 (adj 0.9177) · $8.35 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 41c · p 0.4979 (adj 0.449) · $3.72 · thesis TBL:SUPPRESSED
- Adam Lowry: 1+ goals YES @ 9c · p 0.1182 (adj 0.1086) · $1.35 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 25c · p 0.29 (adj 0.2787) · $2.12 · thesis WPG:OFFENSE_4PLUS
- Nick Robertson: 1+ goals YES @ 16c · p 0.2509 (adj 0.2269) · $5.03 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 14c · p 0.2226 (adj 0.2007) · $4.37 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1542 (adj 0.1369) · $3.11 · thesis PIT:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 65c · p 0.6888 (adj 0.6778) · $3.61 · thesis UTA:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 17c · p 0.2577 (adj 0.2345) · $4.85 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1848 (adj 0.1699) · $2.66 · thesis CBJ:OFFENSE_4PLUS
- Seth Jarvis: 1+ goals NO @ 70c · p 0.7512 (adj 0.7371) · $6.09 · thesis CAR:SUPPRESSED
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7784 (adj 0.7651) · $6.43 · thesis CAR:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 58c · p 0.7147 (adj 0.6206) · $7.12 · thesis CHI:SUPPRESSED
- Andrew Copp: 1+ goals YES @ 18c · p 0.2159 (adj 0.2057) · $1.88 · thesis DET:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 16c · p 0.1976 (adj 0.1832) · $1.74 · thesis CHI:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 41c · p 0.4508 (adj 0.4394) · $2.23 · thesis DET:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1787 (adj 0.1665) · $2.11 · thesis BOS:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2825 (adj 0.2706) · $2.41 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 29c · p 0.3305 (adj 0.3191) · $2.17 · thesis STL:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2234 (adj 0.2088) · $3.83 · thesis WSH:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 5c · p 0.0758 (adj 0.0681) · $1.41 · thesis NSH:OFFENSE_4PLUS
- Washington wins by over 1.5 goals NO @ 70c · p 0.7577 (adj 0.7264) · $7.31 · thesis NSH:WINS
- Mavrik Bourque: 1+ assists NO @ 75c · p 0.8071 (adj 0.7735) · $6.5 · thesis NSH:SUPPRESSED
- Chris Kreider: 1+ goals YES @ 16c · p 0.1948 (adj 0.1836) · $1.7 · thesis MTL:OFFENSE_4PLUS
- Alexandre Texier: 1+ goals YES @ 11c · p 0.1382 (adj 0.1274) · $1.16 · thesis MTL:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2539 (adj 0.2304) · $4.71 · thesis NYI:OFFENSE_4PLUS
- Adam Pelech: 1+ goals YES @ 3c · p 0.0559 (adj 0.0482) · $1.41 · thesis NYI:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6142 (adj 0.5931) · $8.32 · thesis MIN:SUPPRESSED
- Anthony Duclair: 1+ goals YES @ 12c · p 0.1616 (adj 0.1487) · $2.33 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.1657 (adj 0.1468) · $3.14 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 12c · p 0.1598 (adj 0.1461) · $2.13 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2249 (adj 0.2087) · $2.35 · thesis ANA:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 63c · p 0.6828 (adj 0.6671) · $6.26 · thesis BUF:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0754 (adj 0.0665) · $1.21 · thesis LAK:OFFENSE_4PLUS
- Jonas Johansson: 25+ saves NO @ 53c · p 0.6184 (adj 0.5717) · $5.2 · thesis OTT:NET_LOW_VOLUME
- Drake Batherson: 1+ goals NO @ 69c · p 0.7331 (adj 0.7211) · $5.39 · thesis OTT:SUPPRESSED
- Scott Laughton: 1+ goals YES @ 12c · p 0.1499 (adj 0.1387) · $1.15 · thesis LAK:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2182 (adj 0.2049) · $1.78 · thesis VAN:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 71c · p 0.807 (adj 0.7407) · $7.67 · thesis SJS:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 19c · p 0.2265 (adj 0.2136) · $1.6 · thesis VAN:OFFENSE_4PLUS
- Tyler Toffoli: 1+ assists YES @ 28c · p 0.3424 (adj 0.3087) · $2.11 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 24.76, exp saves 21.92 (sd 5.98), pull risk 0.039
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.88, exp saves 24.51 (sd 6.81), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Salomonsson: 1+ points | 0.211 | 0.315 | 35/72 | +0.055 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.502 | 0.600 | 61/41 | +0.071 | STANDARD |
| Elias Salomonsson: 1+ assists | 0.175 | 0.270 | 30/76 | +0.053 | STANDARD |
| John Carlson: 1+ points | 0.386 | 0.470 | 49/55 | +0.046 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.159 | 0.235 | 25/78 | +0.049 | STANDARD |
| Nikita Kucherov: 2+ points | 0.330 | 0.405 | 42/61 | +0.044 | STANDARD |

**UTA @ PIT** · priced 162/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 27.0, exp saves 23.28 (sd 6.55), pull risk 0.075
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.13, exp saves 23.31 (sd 6.54), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ points | 0.681 | 0.540 | 56/48 | +0.104 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.271 | 0.130 | 25/99 | +0.008 | STANDARD |
| Rickard Rakell: 2+ points | 0.313 | 0.180 | 20/84 | +0.102 | STANDARD |
| Rickard Rakell: 1+ goals | 0.435 | 0.305 | 32/71 | +0.100 | STANDARD |
| Kaedan Korczak: 1+ points | 0.317 | 0.205 | 28/87 | +0.023 | STANDARD |
| Ville Koivunen: 1+ assists | 0.355 | 0.255 | 26/75 | +0.082 | STANDARD |

**CBJ @ CAR** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.87, exp saves 20.86 (sd 5.9), pull risk 0.051
- CBJ net: Jet Greaves (CONFIRMED) exp shots 30.96, exp saves 26.54 (sd 7.13), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.539 | 0.645 | 65/36 | +0.085 | STANDARD |
| Sebastian Aho: 1+ assists | 0.362 | 0.465 | 47/54 | +0.081 | STANDARD |
| Charlie Coyle: 1+ points | 0.510 | 0.415 | 42/59 | +0.073 | STANDARD |
| Seth Jarvis: 1+ assists | 0.245 | 0.340 | 35/67 | +0.070 | STANDARD |
| Charlie Coyle: 1+ goals | 0.258 | 0.165 | 17/84 | +0.078 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.417 | 0.505 | 51/50 | +0.066 | STANDARD |

**CHI @ DET** · priced 165/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 24.08, exp saves 21.14 (sd 5.78), pull risk 0.043
- CHI net: Spencer Knight (PROBABLE) exp shots 30.26, exp saves 25.92 (sd 7.0), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.285 | 0.430 | 44/58 | +0.118 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.228 | 0.120 | 22/98 | -0.004 | STANDARD |
| Connor Bedard: 1+ assists | 0.338 | 0.440 | 46/58 | +0.065 | STANDARD |
| Patrick Kane: 1+ points | 0.443 | 0.540 | 55/47 | +0.070 | STANDARD |
| Emmitt Finnie: 2+ points | 0.213 | 0.120 | 15/91 | +0.054 | STANDARD |
| Connor Bedard: 1+ points | 0.516 | 0.605 | 62/41 | +0.057 | STANDARD |

**BOS @ STL** · priced 171/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 26.11, exp saves 22.63 (sd 6.26), pull risk 0.06
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.06, exp saves 24.16 (sd 6.7), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 1+ assists | 0.452 | 0.540 | 55/47 | +0.060 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.297 | 0.210 | 23/81 | +0.055 | STANDARD |
| David Pastrnak: 2+ points | 0.260 | 0.345 | 36/67 | +0.055 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.372 | 0.455 | 47/56 | +0.051 | STANDARD |
| Jonatan Berggren: 1+ points | 0.405 | 0.340 | 37/69 | +0.018 | STANDARD |
| Robert Thomas: 1+ assists | 0.417 | 0.480 | 49/53 | +0.035 | STANDARD |

**WSH @ NSH** · priced 165/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.24, exp saves 24.51 (sd 6.67), pull risk 0.06
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.84 (sd 6.74), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.314 | 0.235 | 26/79 | +0.040 | STANDARD |
| Tom Wilson: 1+ assists | 0.335 | 0.265 | 29/76 | +0.031 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.270 | 0.340 | 35/67 | +0.045 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.193 | 0.260 | 27/75 | +0.044 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.266 | 0.205 | 23/82 | +0.023 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.223 | 0.165 | 17/84 | +0.044 | STANDARD |

**MTL @ DAL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.03, exp saves 20.94 (sd 5.96), pull risk 0.053
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.09 (sd 6.57), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.448 | 0.520 | 54/50 | +0.035 | STANDARD |
| Cole Caufield: 1+ assists | 0.321 | 0.390 | 40/62 | +0.043 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.550 | 57/47 | +0.031 | STANDARD |
| Mikko Rantanen: 2+ points | 0.242 | 0.310 | 33/71 | +0.034 | STANDARD |
| Zachary Bolduc: 1+ points | 0.384 | 0.320 | 35/71 | +0.018 | STANDARD |
| Thomas Harley: 1+ assists | 0.412 | 0.350 | 37/67 | +0.025 | STANDARD |

**NYI @ MIN** · priced 174/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.41, exp saves 23.88 (sd 6.46), pull risk 0.051
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.87, exp saves 24.95 (sd 6.75), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Yakov Trenin: 1+ points | 0.322 | 0.125 | 23/98 | +0.079 | STANDARD |
| Logan Stanley: 1+ points | 0.268 | 0.120 | 22/98 | +0.036 | STANDARD |
| Ryan Hartman: 1+ assists | 0.252 | 0.120 | 22/98 | +0.020 | STANDARD |
| Anthony Duclair: 1+ assists | 0.228 | 0.120 | 22/98 | -0.004 | STANDARD |
| Logan Stanley: 1+ assists | 0.222 | 0.115 | 21/98 | +0.000 | STANDARD |
| Yakov Trenin: 1+ assists | 0.205 | 0.100 | 18/98 | +0.014 | STANDARD |

**BUF @ ANA** · priced 178/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.5), pull risk 0.06
- BUF net: Colten Ellis (PROBABLE) exp shots 28.64, exp saves 24.47 (sd 6.89), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ points | 0.296 | 0.130 | 24/98 | +0.043 | STANDARD |
| Noah Warren: 1+ assists | 0.260 | 0.115 | 21/98 | +0.039 | STANDARD |
| A.J. Greer: 1+ goals | 0.262 | 0.130 | 15/89 | +0.103 | STANDARD |
| Alex Killorn: 1+ points | 0.454 | 0.345 | 36/67 | +0.078 | STANDARD |
| Jackson LaCombe: 1+ points | 0.647 | 0.540 | 56/48 | +0.069 | STANDARD |
| Tristan Luneau: 1+ points | 0.410 | 0.320 | 35/71 | +0.044 | STANDARD |

**OTT @ LAK** · priced 168/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.33, exp saves 23.88 (sd 6.44), pull risk 0.051
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.32, exp saves 22.76 (sd 6.28), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.308 | 0.435 | 45/58 | +0.095 | STANDARD |
| Jake Sanderson: 1+ points | 0.388 | 0.495 | 52/53 | +0.065 | STANDARD |
| Jonas Johansson: 25+ saves | 0.382 | 0.475 | 48/53 | +0.071 |  |
| Thomas Chabot: 1+ assists | 0.210 | 0.295 | 33/74 | +0.037 | STANDARD |
| Thomas Chabot: 1+ points | 0.285 | 0.370 | 41/67 | +0.029 | STANDARD |
| Jake Sanderson: 2+ points | 0.086 | 0.160 | 19/87 | +0.036 | STANDARD |

**VAN @ SJS** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 25.57, exp saves 22.3 (sd 6.23), pull risk 0.06
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.42, exp saves 25.06 (sd 6.94), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.425 | 0.560 | 58/46 | +0.098 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.472 | 0.600 | 61/41 | +0.101 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.284 | 0.405 | 42/61 | +0.089 | STANDARD |
| Macklin Celebrini: 2+ points | 0.333 | 0.450 | 46/56 | +0.090 | STANDARD |
| Ivar Stenberg: 2+ points | 0.107 | 0.210 | 24/82 | +0.063 | STANDARD |
| Ivar Stenberg: 1+ goals | 0.193 | 0.295 | 30/71 | +0.083 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
