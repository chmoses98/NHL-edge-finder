# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T15:56:43Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4281 · contracts joined: 2392 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2117, 'NO_EDGE': 122, 'OK': 153}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 318, 'game_early_goal': 11, 'first_goal': 395, 'game_winner': 22, 'player_goals': 690, 'game_overtime': 11, 'player_points': 424, 'goalie_saves': 4, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-6h | 0.669 | 0.331 | 0.169 | 5.66 | 3.35 | 2.31 | 213 (25/188) | CONFIRMED/PROJECTED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-6h | 0.457 | 0.543 | 0.168 | 6.67 | 3.20 | 3.47 | 225 (25/200) | PROBABLE/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-6h | 0.640 | 0.360 | 0.172 | 6.00 | 3.44 | 2.56 | 218 (25/193) | PROBABLE/PROJECTED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-6h | 0.631 | 0.369 | 0.170 | 5.78 | 3.28 | 2.50 | 222 (25/197) | PROJECTED/PROJECTED |
| BOS @ STL | 2026-10-30T00:00:00Z | T-6h | 0.507 | 0.493 | 0.177 | 6.03 | 3.04 | 2.99 | 223 (25/198) | PROJECTED/PROJECTED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-6h | 0.531 | 0.469 | 0.164 | 6.70 | 3.47 | 3.23 | 223 (25/198) | PROJECTED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-6h | 0.564 | 0.436 | 0.180 | 5.75 | 3.05 | 2.70 | 212 (25/187) | PROJECTED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-6h | 0.590 | 0.410 | 0.176 | 5.93 | 3.25 | 2.68 | 205 (25/180) | PROJECTED/PROJECTED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-6h | 0.511 | 0.489 | 0.175 | 6.52 | 3.28 | 3.24 | 225 (25/200) | PROJECTED/PROJECTED |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-6h | 0.513 | 0.486 | 0.177 | 6.04 | 3.07 | 2.98 | 212 (25/187) | PROJECTED/PROJECTED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-6h | 0.585 | 0.415 | 0.159 | 7.11 | 3.84 | 3.27 | 214 (25/189) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.470 | 0.575 | 0.554 | 58 | 43 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.355 | 0.455 | 0.434 | 46 | 55 | no | +0.077 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.511 | 0.425 | 0.442 | 43 | 58 | yes | +0.063 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.489 | 0.575 | 0.558 | 58 | 43 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.414 | 0.500 | 0.483 | 51 | 51 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.700 | 0.775 | 0.761 | 78 | 23 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.172 | 0.245 | 0.229 | 25 | 76 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.378 | 0.460 | 0.443 | 47 | 55 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.408 | 0.485 | 0.469 | 49 | 52 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.243 | 0.320 | 0.304 | 33 | 69 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.263 | 0.335 | 0.320 | 34 | 67 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.462 | 0.540 | 0.524 | 55 | 47 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.443 | 0.520 | 0.505 | 53 | 49 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.284 | 0.355 | 0.340 | 36 | 65 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.266 | 0.335 | 0.321 | 34 | 67 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.598 | 0.670 | 0.656 | 68 | 34 | no | +0.046 | OK |
| KXNHLGAME-26OCT29CBJCAR-CAR | game_winner | 0.640 | 0.705 | 0.692 | 71 | 30 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.807 | 0.865 | 0.855 | 87 | 14 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.631 | 0.705 | 0.691 | 72 | 31 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.232 | 0.300 | 0.286 | 31 | 71 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL5 | team_total | 0.196 | 0.260 | 0.246 | 27 | 75 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.462 | 0.525 | 0.512 | 53 | 48 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT29MTLDAL-DAL3 | game_spread | 0.197 | 0.260 | 0.246 | 27 | 75 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT29VANSJ-8 | game_total | 0.395 | 0.335 | 0.347 | 34 | 67 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.189 | 0.255 | 0.241 | 27 | 76 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT29CHIDET-CHI2 | game_spread | 0.179 | 0.235 | 0.223 | 24 | 77 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.668 | 0.730 | 0.718 | 74 | 28 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.485 | 0.545 | 0.533 | 55 | 46 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.806 | 0.860 | 0.850 | 87 | 15 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.712 | 0.770 | 0.759 | 78 | 24 | no | +0.035 | OK |
| KXNHLGAME-26OCT29CBJCAR-CBJ | game_winner | 0.360 | 0.305 | 0.316 | 31 | 70 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI4 | team_total | 0.251 | 0.310 | 0.298 | 32 | 70 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL2 | team_total | 0.807 | 0.855 | 0.846 | 86 | 15 | no | +0.034 | OK |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.590 | 0.645 | 0.634 | 65 | 36 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.470 | 0.415 | 0.426 | 42 | 59 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.851 | 0.895 | 0.887 | 90 | 11 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.294 | 0.245 | 0.254 | 25 | 76 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.716 | 0.765 | 0.756 | 77 | 24 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT29VANSJ-7 | game_total | 0.588 | 0.535 | 0.546 | 54 | 47 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-WPG3 | team_total | 0.413 | 0.465 | 0.455 | 47 | 54 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.373 | 0.425 | 0.415 | 43 | 58 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.227 | 0.280 | 0.269 | 29 | 73 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.123 | 0.170 | 0.160 | 18 | 84 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.678 | 0.740 | 0.728 | 76 | 28 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-7 | game_total | 0.525 | 0.475 | 0.485 | 48 | 53 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.248 | 0.200 | 0.209 | 21 | 81 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN4 | team_total | 0.422 | 0.370 | 0.380 | 38 | 64 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.279 | 0.330 | 0.319 | 34 | 68 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT29MTLDAL-DAL2 | game_spread | 0.328 | 0.375 | 0.365 | 38 | 63 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.816 | 0.860 | 0.852 | 87 | 15 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT29VANSJ-10 | game_total | 0.163 | 0.120 | 0.128 | 13 | 89 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT29VANSJ-9 | game_total | 0.299 | 0.250 | 0.259 | 26 | 76 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.379 | 0.425 | 0.416 | 43 | 58 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.155 | 0.195 | 0.186 | 20 | 81 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI2 | team_total | 0.703 | 0.755 | 0.745 | 77 | 26 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.859 | 0.895 | 0.889 | 90 | 11 | no | +0.024 | OK |
| KXNHLGAME-26OCT29CHIDET-CHI | game_winner | 0.369 | 0.415 | 0.406 | 42 | 59 | no | +0.024 | OK |
| KXNHLGAME-26OCT29CHIDET-DET | game_winner | 0.631 | 0.585 | 0.594 | 59 | 42 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH5 | team_total | 0.277 | 0.230 | 0.239 | 24 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.120 | 0.075 | 0.082 | 9 | 94 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.828 | 0.870 | 0.862 | 88 | 14 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.127 | 0.170 | 0.161 | 18 | 84 | no | +0.023 | OK |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.410 | 0.365 | 0.374 | 37 | 64 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.109 | 0.150 | 0.141 | 16 | 86 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.361 | 0.405 | 0.396 | 41 | 60 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.253 | 0.295 | 0.286 | 30 | 71 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.491 | 0.535 | 0.526 | 54 | 47 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.421 | 0.465 | 0.456 | 47 | 54 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT29VANSJ-6 | game_total | 0.696 | 0.650 | 0.659 | 66 | 36 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT29CHIDET-CHI3 | game_spread | 0.093 | 0.125 | 0.118 | 13 | 88 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.241 | 0.190 | 0.200 | 21 | 83 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT29WSHNSH-WSH3 | game_spread | 0.160 | 0.195 | 0.188 | 20 | 81 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL6 | team_total | 0.084 | 0.120 | 0.112 | 13 | 89 | no | +0.019 | OK |
| KXNHLGAME-26OCT29MTLDAL-MTL | game_winner | 0.436 | 0.395 | 0.403 | 40 | 61 | yes | +0.019 | OK |
| KXNHLGAME-26OCT29MTLDAL-DAL | game_winner | 0.564 | 0.605 | 0.597 | 61 | 40 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.113 | 0.150 | 0.142 | 16 | 86 | no | +0.019 | OK |
| KXNHLGAME-26OCT29VANSJ-VAN | game_winner | 0.415 | 0.375 | 0.383 | 38 | 63 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT29CHIDET-DET2 | game_spread | 0.394 | 0.355 | 0.363 | 36 | 65 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.200 | 0.235 | 0.228 | 24 | 77 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.268 | 0.305 | 0.297 | 31 | 70 | no | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 0.669 | 0.627 | 0.169 | 0.211 | 5.66 | 5.96 | 0.947/1.002 | KXNHLTEAMTOTAL-26OCT29WPGTB-WPG3 +0.071 |
| UTA @ PIT | 0.457 | 0.512 | 0.168 | 0.214 | 6.67 | 6.71 | 1.038/0.993 | KXNHLGAME-26OCT29UTAPIT-PIT +0.055 |
| CBJ @ CAR | 0.640 | 0.579 | 0.172 | 0.216 | 6.00 | 6.22 | 1.000/0.965 | KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3 +0.080 |
| CHI @ DET | 0.631 | 0.615 | 0.170 | 0.214 | 5.78 | 6.16 | 1.003/1.026 | KXNHLTOTAL-26OCT29CHIDET-7 +0.064 |
| BOS @ STL | 0.507 | 0.523 | 0.177 | 0.213 | 6.03 | 6.37 | 0.993/0.969 | KXNHLTOTAL-26OCT29BOSSTL-7 +0.057 |
| WSH @ NSH | 0.531 | 0.545 | 0.164 | 0.218 | 6.70 | 6.41 | 1.001/0.993 | KXNHLTOTAL-26OCT29WSHNSH-6 -0.051 |
| MTL @ DAL | 0.564 | 0.560 | 0.180 | 0.218 | 5.75 | 6.09 | 0.987/0.943 | KXNHLTOTAL-26OCT29MTLDAL-7 +0.060 |
| NYI @ MIN | 0.590 | 0.566 | 0.176 | 0.218 | 5.93 | 6.13 | 0.996/0.957 | KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3 +0.050 |
| BUF @ ANA | 0.511 | 0.558 | 0.175 | 0.210 | 6.52 | 6.66 | 1.036/0.998 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.053 |
| OTT @ LAK | 0.513 | 0.528 | 0.177 | 0.224 | 6.04 | 5.99 | 0.993/1.034 | KXNHLTOTAL-26OCT29OTTLA-6 -0.020 |
| VAN @ SJS | 0.585 | 0.556 | 0.159 | 0.216 | 7.11 | 6.58 | 1.035/1.026 | KXNHLTOTAL-26OCT29VANSJ-8 -0.087 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Elias Salomonsson: 1+ goals NO @ 92c · p 0.9542 (adj 0.9444) · $8.33 · thesis WPG:SUPPRESSED
- Jake Guentzel: 2+ goals YES @ 7c · p 0.0994 (adj 0.0896) · $1.84 · thesis TBL:OFFENSE_4PLUS
- Anthony Cirelli: 1+ goals YES @ 23c · p 0.2745 (adj 0.2559) · $2.4 · thesis TBL:OFFENSE_4PLUS
- Tampa Bay over 4.5 goals scored NO @ 69c · p 0.7527 (adj 0.7164) · $8.33 · thesis TBL:SUPPRESSED
- Declan Carlile: 1+ goals YES @ 6c · p 0.0986 (adj 0.0877) · $2.28 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 2+ goals YES @ 7c · p 0.1138 (adj 0.0966) · $1.8 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 32c · p 0.3845 (adj 0.3671) · $4.77 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 32c · p 0.4432 (adj 0.3599) · $1.93 · thesis PIT:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 17c · p 0.2539 (adj 0.2317) · $5.85 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1904 (adj 0.1741) · $3.83 · thesis CBJ:OFFENSE_4PLUS
- Carolina wins by over 1.5 goals NO @ 52c · p 0.6493 (adj 0.562) · $1.35 · thesis GAME:TIGHT
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7201 (adj 0.7038) · $5.85 · thesis CAR:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 57c · p 0.7117 (adj 0.6131) · $7.17 · thesis CHI:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 58c · p 0.6544 (adj 0.6072) · $1.98 · thesis CHI:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 54c · p 0.6308 (adj 0.5829) · $6.48 · thesis BOS:SUPPRESSED
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1769 (adj 0.1652) · $2.11 · thesis BOS:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2835 (adj 0.2714) · $2.5 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 29c · p 0.3295 (adj 0.3184) · $1.99 · thesis STL:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2327 (adj 0.2158) · $4.25 · thesis WSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 29c · p 0.334 (adj 0.318) · $2.08 · thesis NSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 25c · p 0.3216 (adj 0.2733) · $1.03 · thesis WSH:OFFENSE_4PLUS
- Cole Caufield: 1+ assists NO @ 61c · p 0.6813 (adj 0.6381) · $3.41 · thesis MTL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2438 (adj 0.2216) · $3.67 · thesis NYI:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 53c · p 0.6058 (adj 0.5856) · $8.36 · thesis MIN:SUPPRESSED
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.1593 (adj 0.1445) · $1.86 · thesis NYI:OFFENSE_4PLUS
- Anthony Duclair: 1+ goals YES @ 13c · p 0.159 (adj 0.1492) · $1.36 · thesis NYI:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.1632 (adj 0.1474) · $2.95 · thesis ANA:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.8528 (adj 0.8039) · $8.36 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 25c · p 0.3447 (adj 0.2949) · $2.44 · thesis ANA:WINS_BY_2PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2242 (adj 0.2107) · $1.95 · thesis ANA:OFFENSE_4PLUS
- Tim Stutzle: 1+ assists NO @ 55c · p 0.6352 (adj 0.5901) · $5.12 · thesis OTT:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 58c · p 0.7025 (adj 0.6131) · $3.62 · thesis OTT:SUPPRESSED
- Tim Stutzle: 1+ goals NO @ 68c · p 0.7188 (adj 0.7078) · $3.8 · thesis OTT:SUPPRESSED
- Erik Gustafsson: 1+ assists NO @ 63c · p 0.6988 (adj 0.6594) · $4.02 · thesis LAK:SUPPRESSED
- Dmitry Orlov: 1+ goals NO @ 90c · p 0.9322 (adj 0.9204) · $7.34 · thesis DIFFUSE
- Ivar Stenberg: 1+ goals NO @ 70c · p 0.806 (adj 0.7339) · $6.67 · thesis SJS:SUPPRESSED
- San Jose wins by over 2.5 goals NO @ 71c · p 0.7731 (adj 0.739) · $3.6 · thesis VAN:WINS
- Ivar Stenberg: 1+ assists NO @ 60c · p 0.7199 (adj 0.6322) · $3.3 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 150/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 24.76, exp saves 21.9 (sd 5.94), pull risk 0.038
- WPG net: Stuart Skinner (PROJECTED) exp shots 28.88, exp saves 24.54 (sd 6.86), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.496 | 0.605 | 62/41 | +0.077 | STANDARD |
| Jake Guentzel: 2+ points | 0.309 | 0.225 | 29/84 | +0.004 | STANDARD |
| Anthony Cirelli: 1+ goals | 0.275 | 0.200 | 23/83 | +0.032 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.155 | 0.225 | 28/83 | +0.005 | STANDARD |
| Brayden Point: 2+ points | 0.278 | 0.215 | 26/83 | +0.005 | STANDARD |
| Ilya Mikheyev: 1+ goals | 0.207 | 0.150 | 18/88 | +0.016 | STANDARD |

**UTA @ PIT** · priced 151/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROBABLE) exp shots 27.0, exp saves 23.31 (sd 6.55), pull risk 0.072
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.13, exp saves 23.28 (sd 6.55), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 2+ points | 0.310 | 0.160 | 21/89 | +0.089 | STANDARD |
| Rickard Rakell: 1+ points | 0.680 | 0.550 | 57/47 | +0.093 | STANDARD |
| Rickard Rakell: 1+ goals | 0.443 | 0.315 | 32/69 | +0.108 | STANDARD |
| Connor Dewar: 1+ goals | 0.213 | 0.105 | 12/91 | +0.086 | STANDARD |
| Nick Robertson: 1+ goals | 0.252 | 0.145 | 16/87 | +0.082 | STANDARD |
| Thomas Novak: 1+ assists | 0.424 | 0.330 | 35/69 | +0.058 | STANDARD |

**CBJ @ CAR** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.87, exp saves 20.84 (sd 5.92), pull risk 0.054
- CBJ net: Jet Greaves (PROJECTED) exp shots 30.96, exp saves 26.51 (sd 7.2), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pyotr Kochetkov: 21+ saves | 0.517 | 0.245 | 37/88 | +0.131 |  |
| Sebastian Aho: 2+ points | 0.182 | 0.285 | 31/74 | +0.065 | STANDARD |
| Sebastian Aho: 1+ assists | 0.369 | 0.470 | 49/55 | +0.064 | STANDARD |
| Sebastian Aho: 1+ points | 0.545 | 0.645 | 65/36 | +0.079 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.356 | 0.445 | 46/57 | +0.057 | STANDARD |
| Charlie Coyle: 1+ goals | 0.254 | 0.165 | 17/84 | +0.074 | STANDARD |

**CHI @ DET** · priced 162/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 24.08, exp saves 21.14 (sd 5.89), pull risk 0.047
- CHI net: Arvid Soderblom (PROJECTED) exp shots 30.26, exp saves 25.87 (sd 7.05), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.288 | 0.440 | 45/57 | +0.125 | STANDARD |
| Patrick Kane: 1+ points | 0.446 | 0.560 | 58/46 | +0.077 | STANDARD |
| Connor Bedard: 1+ assists | 0.346 | 0.440 | 46/58 | +0.057 | STANDARD |
| Connor Bedard: 1+ points | 0.519 | 0.605 | 62/41 | +0.054 | STANDARD |
| Roman Kantserov: 1+ points | 0.400 | 0.480 | 50/54 | +0.043 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.357 | 0.290 | 31/73 | +0.032 | STANDARD |

**BOS @ STL** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.11, exp saves 22.65 (sd 6.27), pull risk 0.06
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.06, exp saves 24.16 (sd 6.67), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.369 | 0.465 | 47/54 | +0.073 | STANDARD |
| David Pastrnak: 2+ points | 0.256 | 0.345 | 35/66 | +0.069 | STANDARD |
| David Pastrnak: 1+ assists | 0.452 | 0.540 | 55/47 | +0.061 | STANDARD |
| Charlie McAvoy: 1+ points | 0.445 | 0.520 | 54/50 | +0.038 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.296 | 0.225 | 25/80 | +0.033 | STANDARD |
| David Pastrnak: 2+ assists | 0.119 | 0.180 | 20/84 | +0.032 | STANDARD |

**WSH @ NSH** · priced 165/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 28.24, exp saves 24.49 (sd 6.62), pull risk 0.056
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.85 (sd 6.68), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.322 | 0.225 | 25/80 | +0.058 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.271 | 0.340 | 35/67 | +0.044 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.233 | 0.165 | 17/84 | +0.053 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.334 | 0.270 | 29/75 | +0.030 | STANDARD |
| Aliaksei Protas: 1+ points | 0.425 | 0.365 | 38/65 | +0.029 | STANDARD |
| Ryan Leonard: 1+ points | 0.454 | 0.395 | 40/61 | +0.037 | STANDARD |

**MTL @ DAL** · priced 157/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.03, exp saves 20.99 (sd 5.89), pull risk 0.049
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.02 (sd 6.55), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Caufield: 1+ assists | 0.319 | 0.405 | 42/61 | +0.055 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.530 | 54/48 | +0.050 | STANDARD |
| Thomas Harley: 1+ assists | 0.429 | 0.355 | 37/66 | +0.043 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.262 | 0.190 | 21/83 | +0.040 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.370 | 0.440 | 45/57 | +0.043 | STANDARD |
| Mikko Rantanen: 2+ points | 0.248 | 0.315 | 33/70 | +0.038 | STANDARD |

**NYI @ MIN** · priced 151/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.41, exp saves 23.85 (sd 6.48), pull risk 0.052
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.87, exp saves 24.9 (sd 6.84), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matt Boldy: 1+ assists | 0.407 | 0.510 | 52/50 | +0.076 | STANDARD |
| Emil Heineman: 1+ points | 0.397 | 0.295 | 32/73 | +0.062 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.276 | 0.375 | 40/65 | +0.058 | STANDARD |
| Emil Heineman: 1+ assists | 0.262 | 0.165 | 18/85 | +0.071 | STANDARD |
| Matt Boldy: 2+ points | 0.242 | 0.335 | 34/67 | +0.072 | STANDARD |
| Brayden Schenn: 1+ goals | 0.244 | 0.155 | 18/87 | +0.053 | STANDARD |

**BUF @ ANA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.65), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 28.64, exp saves 24.45 (sd 6.9), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.258 | 0.145 | 16/87 | +0.088 | STANDARD |
| Tage Thompson: 1+ points | 0.527 | 0.630 | 64/38 | +0.076 | STANDARD |
| Tage Thompson: 2+ points | 0.179 | 0.275 | 29/74 | +0.068 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.511 | 0.605 | 61/40 | +0.073 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.162 | 0.250 | 27/77 | +0.056 | STANDARD |
| Alex Killorn: 1+ points | 0.451 | 0.365 | 38/65 | +0.055 | STANDARD |

**OTT @ LAK** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.33, exp saves 23.9 (sd 6.42), pull risk 0.048
- OTT net: Jonas Johansson (PROJECTED) exp shots 26.32, exp saves 22.72 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.297 | 0.435 | 45/58 | +0.105 | STANDARD |
| Jake Sanderson: 1+ points | 0.377 | 0.510 | 52/50 | +0.105 | STANDARD |
| Tim Stutzle: 1+ points | 0.544 | 0.640 | 65/37 | +0.070 | STANDARD |
| Tim Stutzle: 1+ assists | 0.365 | 0.455 | 46/55 | +0.068 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.301 | 0.380 | 39/63 | +0.052 | STANDARD |
| Erik Gustafsson: 1+ points | 0.352 | 0.425 | 43/58 | +0.051 | STANDARD |

**VAN @ SJS** · priced 156/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 25.57, exp saves 22.26 (sd 6.27), pull risk 0.063
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.42, exp saves 25.09 (sd 7.01), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.417 | 0.580 | 59/43 | +0.136 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.280 | 0.415 | 43/60 | +0.103 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.464 | 0.585 | 59/42 | +0.099 | STANDARD |
| Ivar Stenberg: 2+ points | 0.109 | 0.230 | 24/78 | +0.099 | STANDARD |
| Ivar Stenberg: 1+ goals | 0.194 | 0.305 | 31/70 | +0.091 | STANDARD |
| Linus Karlsson: 1+ points | 0.453 | 0.350 | 38/68 | +0.057 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
