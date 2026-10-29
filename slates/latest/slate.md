# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T14:45:05Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4266 · contracts joined: 2377 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2102, 'OK': 151, 'NO_EDGE': 124}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 314, 'game_early_goal': 11, 'first_goal': 395, 'game_winner': 22, 'player_goals': 690, 'game_overtime': 11, 'player_points': 417, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-6h | 0.643 | 0.357 | 0.174 | 5.75 | 3.31 | 2.43 | 212 (25/187) | PROJECTED/PROJECTED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-6h | 0.479 | 0.521 | 0.171 | 6.65 | 3.25 | 3.40 | 224 (25/199) | PROJECTED/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-6h | 0.666 | 0.334 | 0.173 | 5.92 | 3.46 | 2.46 | 217 (25/192) | PROJECTED/PROJECTED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-6h | 0.628 | 0.372 | 0.175 | 5.86 | 3.32 | 2.54 | 221 (25/196) | PROJECTED/PROJECTED |
| BOS @ STL | 2026-10-30T00:00:00Z | T-6h | 0.503 | 0.497 | 0.176 | 5.98 | 3.00 | 2.98 | 223 (25/198) | PROJECTED/PROJECTED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-6h | 0.544 | 0.456 | 0.165 | 6.67 | 3.48 | 3.20 | 223 (25/198) | PROJECTED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-6h | 0.589 | 0.411 | 0.184 | 5.80 | 3.17 | 2.63 | 212 (25/187) | PROJECTED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-6h | 0.599 | 0.401 | 0.179 | 5.84 | 3.23 | 2.61 | 205 (25/180) | PROJECTED/PROJECTED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-6h | 0.504 | 0.496 | 0.172 | 6.45 | 3.23 | 3.23 | 217 (25/192) | PROJECTED/PROJECTED |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-6h | 0.510 | 0.490 | 0.180 | 6.04 | 3.05 | 2.99 | 212 (25/187) | PROJECTED/PROJECTED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-6h | 0.585 | 0.415 | 0.163 | 6.94 | 3.75 | 3.19 | 211 (25/186) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.484 | 0.565 | 0.549 | 57 | 44 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.434 | 0.515 | 0.499 | 52 | 49 | no | +0.058 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.504 | 0.425 | 0.441 | 43 | 58 | yes | +0.057 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.496 | 0.575 | 0.559 | 58 | 43 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.240 | 0.320 | 0.303 | 33 | 69 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.370 | 0.445 | 0.430 | 45 | 56 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.176 | 0.245 | 0.230 | 25 | 76 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.626 | 0.700 | 0.686 | 71 | 31 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.414 | 0.490 | 0.475 | 50 | 52 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.464 | 0.540 | 0.525 | 55 | 47 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.267 | 0.335 | 0.321 | 34 | 67 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.659 | 0.730 | 0.717 | 74 | 28 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.230 | 0.300 | 0.285 | 31 | 71 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.715 | 0.775 | 0.764 | 78 | 23 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.728 | 0.785 | 0.774 | 79 | 22 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.843 | 0.895 | 0.886 | 90 | 11 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.276 | 0.335 | 0.323 | 34 | 67 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.813 | 0.865 | 0.856 | 87 | 14 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.287 | 0.345 | 0.333 | 35 | 66 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.721 | 0.775 | 0.765 | 78 | 23 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH4 | team_total | 0.470 | 0.415 | 0.426 | 42 | 59 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.420 | 0.475 | 0.464 | 48 | 53 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT29VANSJ-SJ3 | game_spread | 0.244 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN4 | team_total | 0.407 | 0.350 | 0.361 | 36 | 66 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-7 | game_total | 0.402 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.686 | 0.745 | 0.734 | 76 | 27 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.197 | 0.250 | 0.239 | 26 | 76 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.383 | 0.435 | 0.424 | 44 | 57 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH5 | team_total | 0.282 | 0.230 | 0.240 | 24 | 78 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.504 | 0.560 | 0.549 | 57 | 45 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-6 | game_total | 0.514 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.495 | 0.545 | 0.535 | 55 | 46 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.813 | 0.860 | 0.852 | 87 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.486 | 0.535 | 0.525 | 54 | 47 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.825 | 0.865 | 0.858 | 87 | 14 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB2 | game_spread | 0.406 | 0.455 | 0.445 | 46 | 55 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-7 | game_total | 0.524 | 0.475 | 0.485 | 48 | 53 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.407 | 0.460 | 0.449 | 47 | 55 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI2 | team_total | 0.711 | 0.760 | 0.751 | 77 | 25 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT29WSHNSH-WSH3 | game_spread | 0.154 | 0.200 | 0.190 | 21 | 81 | no | +0.025 | OK |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.599 | 0.645 | 0.636 | 65 | 36 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.827 | 0.870 | 0.862 | 88 | 14 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.388 | 0.435 | 0.425 | 44 | 57 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.107 | 0.150 | 0.140 | 16 | 86 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.418 | 0.465 | 0.456 | 47 | 54 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.108 | 0.150 | 0.141 | 16 | 86 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.234 | 0.280 | 0.270 | 29 | 73 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-4 | game_total | 0.829 | 0.870 | 0.863 | 88 | 14 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN3 | team_total | 0.619 | 0.570 | 0.580 | 58 | 44 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.602 | 0.645 | 0.637 | 65 | 36 | no | +0.022 | OK |
| KXNHLGAME-26OCT29WPGTB-TB | game_winner | 0.643 | 0.685 | 0.677 | 69 | 32 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.861 | 0.895 | 0.889 | 90 | 11 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.129 | 0.170 | 0.161 | 18 | 84 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH6 | team_total | 0.138 | 0.100 | 0.107 | 11 | 91 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.624 | 0.670 | 0.661 | 68 | 34 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT29WSHNSH-NSH3 | team_total | 0.677 | 0.630 | 0.640 | 64 | 38 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN6 | team_total | 0.106 | 0.070 | 0.076 | 8 | 94 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.131 | 0.170 | 0.162 | 18 | 84 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL5 | team_total | 0.217 | 0.265 | 0.255 | 28 | 75 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29UTAPIT-5 | game_total | 0.822 | 0.855 | 0.849 | 86 | 15 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-8 | game_total | 0.218 | 0.260 | 0.251 | 27 | 75 | no | +0.018 | OK |
| KXNHLGAME-26OCT29VANSJ-VAN | game_winner | 0.415 | 0.375 | 0.383 | 38 | 63 | yes | +0.018 | OK |
| KXNHLGAME-26OCT29VANSJ-SJ | game_winner | 0.585 | 0.625 | 0.617 | 63 | 38 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-9 | game_total | 0.240 | 0.200 | 0.208 | 21 | 81 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN3 | team_total | 0.637 | 0.675 | 0.667 | 68 | 33 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT29MTLDAL-DAL3 | game_spread | 0.219 | 0.260 | 0.251 | 27 | 75 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.365 | 0.405 | 0.397 | 41 | 60 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT29BUFANA-5 | game_total | 0.803 | 0.835 | 0.829 | 84 | 17 | no | +0.017 | OK |
| KXNHLGAME-26OCT29WSHNSH-NSH | game_winner | 0.544 | 0.505 | 0.513 | 51 | 50 | yes | +0.017 | OK |
| KXNHLGAME-26OCT29WSHNSH-WSH | game_winner | 0.456 | 0.495 | 0.487 | 50 | 51 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT29WSHNSH-WSH2 | game_spread | 0.259 | 0.300 | 0.291 | 31 | 71 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT29VANSJ-VAN5 | team_total | 0.228 | 0.185 | 0.193 | 20 | 83 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT29UTAPIT-UTA2 | team_total | 0.846 | 0.875 | 0.870 | 88 | 13 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT29UTAPIT-6 | game_total | 0.629 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.401 | 0.365 | 0.372 | 37 | 64 | yes | +0.015 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 0.643 | 0.624 | 0.174 | 0.216 | 5.75 | 5.99 | 0.958/1.002 | KXNHLTOTAL-26OCT29WPGTB-7 +0.048 |
| UTA @ PIT | 0.479 | 0.510 | 0.171 | 0.213 | 6.65 | 6.70 | 1.034/0.993 | KXNHLSPREAD-26OCT29UTAPIT-UTA2 -0.037 |
| CBJ @ CAR | 0.666 | 0.573 | 0.173 | 0.216 | 5.92 | 6.21 | 0.998/0.965 | KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3 +0.102 |
| CHI @ DET | 0.628 | 0.615 | 0.175 | 0.214 | 5.86 | 6.16 | 1.003/1.026 | KXNHLTOTAL-26OCT29CHIDET-7 +0.055 |
| BOS @ STL | 0.503 | 0.523 | 0.176 | 0.213 | 5.98 | 6.37 | 0.993/0.969 | KXNHLTOTAL-26OCT29BOSSTL-7 +0.069 |
| WSH @ NSH | 0.544 | 0.545 | 0.165 | 0.218 | 6.67 | 6.41 | 1.001/0.993 | KXNHLTOTAL-26OCT29WSHNSH-6 -0.043 |
| MTL @ DAL | 0.589 | 0.560 | 0.184 | 0.218 | 5.80 | 6.09 | 0.987/0.943 | KXNHLTEAMTOTAL-26OCT29MTLDAL-MTL3 +0.057 |
| NYI @ MIN | 0.599 | 0.566 | 0.179 | 0.218 | 5.84 | 6.13 | 0.996/0.957 | KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3 +0.064 |
| BUF @ ANA | 0.504 | 0.558 | 0.172 | 0.210 | 6.45 | 6.66 | 1.036/0.998 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4 +0.068 |
| OTT @ LAK | 0.510 | 0.528 | 0.180 | 0.224 | 6.04 | 5.99 | 0.993/1.034 | KXNHLSPREAD-26OCT29OTTLA-OTT2 -0.024 |
| VAN @ SJS | 0.585 | 0.556 | 0.163 | 0.216 | 6.94 | 6.58 | 1.035/1.026 | KXNHLTOTAL-26OCT29VANSJ-8 -0.062 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Ilya Mikheyev: 1+ goals YES @ 17c · p 0.2095 (adj 0.1971) · $2.08 · thesis TBL:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9188 (adj 0.9091) · $8.29 · thesis TBL:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 11c · p 0.1383 (adj 0.1287) · $1.31 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 25c · p 0.2877 (adj 0.277) · $1.92 · thesis WPG:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1633 (adj 0.1412) · $3.37 · thesis PIT:WINS_BY_2PLUS
- Declan Carlile: 1+ goals YES @ 6c · p 0.0968 (adj 0.0863) · $2.15 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 32c · p 0.386 (adj 0.3683) · $5.0 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 32c · p 0.4342 (adj 0.3567) · $3.01 · thesis PIT:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 17c · p 0.2526 (adj 0.2307) · $5.59 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1835 (adj 0.1689) · $3.19 · thesis CBJ:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7162 (adj 0.6996) · $7.36 · thesis CAR:SUPPRESSED
- Seth Jarvis: 1+ goals NO @ 70c · p 0.7412 (adj 0.7297) · $4.58 · thesis CAR:SUPPRESSED
- Roman Kantserov: 1+ goals NO @ 75c · p 0.8031 (adj 0.7886) · $5.73 · thesis CHI:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 57c · p 0.7117 (adj 0.6163) · $4.39 · thesis CHI:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 57c · p 0.6544 (adj 0.6072) · $2.31 · thesis CHI:SUPPRESSED
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1769 (adj 0.1652) · $1.95 · thesis BOS:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.2835 (adj 0.2714) · $2.52 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 29c · p 0.3295 (adj 0.3171) · $1.84 · thesis STL:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2327 (adj 0.2133) · $5.0 · thesis WSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 29c · p 0.334 (adj 0.3155) · $1.71 · thesis NSH:OFFENSE_4PLUS
- Cole Caufield: 1+ assists NO @ 60c · p 0.6813 (adj 0.6331) · $4.7 · thesis MTL:SUPPRESSED
- Thomas Harley: 1+ assists YES @ 36c · p 0.4292 (adj 0.3896) · $2.17 · thesis DAL:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 52c · p 0.6058 (adj 0.5831) · $8.29 · thesis MIN:SUPPRESSED
- Olli Maatta: 1+ goals YES @ 4c · p 0.0636 (adj 0.0552) · $1.16 · thesis MIN:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.1593 (adj 0.147) · $2.14 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 20c · p 0.2438 (adj 0.2278) · $2.05 · thesis NYI:OFFENSE_4PLUS
- Zach Metsa: 1+ goals NO @ 92c · p 0.9658 (adj 0.9506) · $8.29 · thesis DIFFUSE
- Tim Washe: 1+ goals YES @ 11c · p 0.1632 (adj 0.1474) · $3.0 · thesis ANA:OFFENSE_4PLUS
- Anaheim wins by over 1.5 goals YES @ 25c · p 0.3447 (adj 0.2949) · $3.02 · thesis ANA:WINS_BY_2PLUS
- Tage Thompson: 1+ goals NO @ 64c · p 0.6953 (adj 0.6802) · $6.03 · thesis BUF:SUPPRESSED
- Jake Sanderson: 1+ assists NO @ 57c · p 0.7025 (adj 0.6066) · $4.79 · thesis OTT:SUPPRESSED
- Tim Stutzle: 1+ assists NO @ 56c · p 0.6352 (adj 0.5901) · $2.41 · thesis OTT:SUPPRESSED
- Ottawa wins by over 1.5 goals NO @ 70c · p 0.7564 (adj 0.7257) · $3.33 · thesis LAK:WINS
- Erik Gustafsson: 1+ assists NO @ 63c · p 0.6988 (adj 0.6569) · $3.68 · thesis LAK:SUPPRESSED
- Dmitry Orlov: 1+ goals NO @ 89c · p 0.9322 (adj 0.9179) · $7.39 · thesis DIFFUSE
- Ivar Stenberg: 1+ assists NO @ 60c · p 0.7199 (adj 0.6355) · $4.17 · thesis SJS:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 70c · p 0.806 (adj 0.7306) · $5.57 · thesis SJS:SUPPRESSED
- San Jose wins by over 2.5 goals NO @ 71c · p 0.7731 (adj 0.739) · $3.58 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 149/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.76, exp saves 21.86 (sd 6.01), pull risk 0.04
- WPG net: Stuart Skinner (PROJECTED) exp shots 28.88, exp saves 24.56 (sd 6.84), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.505 | 0.615 | 63/40 | +0.078 | STANDARD |
| Nikita Kucherov: 2+ points | 0.342 | 0.420 | 43/59 | +0.051 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.156 | 0.230 | 26/80 | +0.033 | STANDARD |
| Brayden Point: 1+ goals | 0.357 | 0.295 | 33/74 | +0.011 | STANDARD |
| Anthony Cirelli: 1+ goals | 0.280 | 0.220 | 24/80 | +0.027 | STANDARD |
| Nikita Kucherov: 1+ points | 0.703 | 0.760 | 77/25 | +0.034 | STANDARD |

**UTA @ PIT** · priced 150/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.0, exp saves 23.33 (sd 6.54), pull risk 0.074
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.13, exp saves 23.28 (sd 6.58), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ points | 0.677 | 0.555 | 57/46 | +0.090 | STANDARD |
| Rickard Rakell: 1+ goals | 0.434 | 0.315 | 32/69 | +0.099 | STANDARD |
| Nick Robertson: 1+ goals | 0.253 | 0.140 | 15/87 | +0.094 | STANDARD |
| Connor Dewar: 1+ goals | 0.217 | 0.110 | 12/90 | +0.090 | STANDARD |
| Rickard Rakell: 2+ points | 0.309 | 0.205 | 23/82 | +0.066 | STANDARD |
| Blake Lizotte: 1+ goals | 0.163 | 0.075 | 10/95 | +0.057 | STANDARD |

**CBJ @ CAR** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.87, exp saves 20.82 (sd 5.85), pull risk 0.056
- CBJ net: Jet Greaves (PROJECTED) exp shots 30.96, exp saves 26.53 (sd 7.27), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.180 | 0.300 | 32/72 | +0.085 | STANDARD |
| Sebastian Aho: 1+ assists | 0.363 | 0.475 | 49/54 | +0.080 | STANDARD |
| Sebastian Aho: 1+ points | 0.548 | 0.645 | 66/37 | +0.066 | STANDARD |
| Seth Jarvis: 1+ assists | 0.262 | 0.355 | 37/66 | +0.063 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.363 | 0.455 | 46/55 | +0.069 | STANDARD |
| Charlie Coyle: 1+ goals | 0.253 | 0.165 | 17/84 | +0.073 | STANDARD |

**CHI @ DET** · priced 161/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 24.08, exp saves 21.14 (sd 5.89), pull risk 0.047
- CHI net: Arvid Soderblom (PROJECTED) exp shots 30.26, exp saves 25.87 (sd 7.05), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.288 | 0.435 | 44/57 | +0.125 | STANDARD |
| Patrick Kane: 1+ points | 0.446 | 0.555 | 57/46 | +0.077 | STANDARD |
| Connor Bedard: 1+ points | 0.519 | 0.615 | 63/40 | +0.065 | STANDARD |
| Connor Bedard: 1+ assists | 0.346 | 0.440 | 45/57 | +0.067 | STANDARD |
| Roman Kantserov: 1+ points | 0.400 | 0.490 | 50/52 | +0.063 | STANDARD |
| Dylan Larkin: 2+ points | 0.186 | 0.255 | 27/76 | +0.041 | STANDARD |

**BOS @ STL** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.11, exp saves 22.65 (sd 6.27), pull risk 0.06
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.06, exp saves 24.16 (sd 6.67), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ points | 0.408 | 0.205 | 38/97 | +0.011 | STANDARD |
| Cam Fowler: 1+ points | 0.354 | 0.190 | 35/97 | -0.012 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.369 | 0.470 | 48/54 | +0.073 | STANDARD |
| David Pastrnak: 2+ points | 0.256 | 0.340 | 35/67 | +0.059 | STANDARD |
| David Pastrnak: 1+ assists | 0.452 | 0.535 | 55/48 | +0.051 | STANDARD |
| Charlie McAvoy: 1+ points | 0.445 | 0.525 | 54/49 | +0.048 | STANDARD |

**WSH @ NSH** · priced 165/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 28.24, exp saves 24.49 (sd 6.62), pull risk 0.056
- WSH net: Charlie Lindgren (PROJECTED) exp shots 27.82, exp saves 23.85 (sd 6.68), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.322 | 0.225 | 25/80 | +0.058 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.233 | 0.155 | 16/85 | +0.063 | STANDARD |
| Aliaksei Protas: 1+ points | 0.425 | 0.350 | 37/67 | +0.039 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.271 | 0.345 | 36/67 | +0.044 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.334 | 0.260 | 29/77 | +0.030 | STANDARD |
| Ryan Leonard: 1+ points | 0.454 | 0.390 | 40/62 | +0.037 | STANDARD |

**MTL @ DAL** · priced 157/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.03, exp saves 20.99 (sd 5.89), pull risk 0.049
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.02 (sd 6.55), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Caufield: 1+ assists | 0.319 | 0.415 | 43/60 | +0.065 | STANDARD |
| Thomas Harley: 1+ assists | 0.429 | 0.350 | 36/66 | +0.053 | STANDARD |
| Mikko Rantanen: 2+ points | 0.248 | 0.325 | 33/68 | +0.057 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.530 | 54/48 | +0.050 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.262 | 0.190 | 21/83 | +0.040 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.370 | 0.440 | 45/57 | +0.043 | STANDARD |

**NYI @ MIN** · priced 151/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.41, exp saves 23.85 (sd 6.48), pull risk 0.052
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.87, exp saves 24.9 (sd 6.84), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.276 | 0.390 | 40/62 | +0.088 | STANDARD |
| Matt Boldy: 1+ assists | 0.407 | 0.510 | 52/50 | +0.076 | STANDARD |
| Emil Heineman: 1+ assists | 0.262 | 0.160 | 18/86 | +0.071 | STANDARD |
| Matt Boldy: 1+ points | 0.609 | 0.515 | 68/65 | -0.086 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.394 | 0.485 | 49/52 | +0.068 | STANDARD |
| Emil Heineman: 1+ points | 0.397 | 0.310 | 32/70 | +0.062 | STANDARD |

**BUF @ ANA** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Ville Husso (PROJECTED) exp shots 27.32, exp saves 23.86 (sd 6.65), pull risk 0.063
- BUF net: Colten Ellis (PROJECTED) exp shots 28.64, exp saves 24.45 (sd 6.9), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tristan Luneau: 1+ points | 0.409 | 0.200 | 37/97 | +0.022 | STANDARD |
| Noah Ostlund: 1+ points | 0.454 | 0.270 | 51/97 | -0.073 | STANDARD |
| A.J. Greer: 1+ goals | 0.258 | 0.145 | 16/87 | +0.088 | STANDARD |
| Tage Thompson: 1+ points | 0.527 | 0.620 | 64/40 | +0.056 | STANDARD |
| Judd Caulfield: 1+ goals | 0.203 | 0.115 | 18/95 | +0.013 | STANDARD |
| Tage Thompson: 2+ points | 0.179 | 0.265 | 28/75 | +0.058 | STANDARD |

**OTT @ LAK** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.33, exp saves 23.9 (sd 6.42), pull risk 0.048
- OTT net: Jonas Johansson (PROJECTED) exp shots 26.32, exp saves 22.72 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.297 | 0.445 | 46/57 | +0.115 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.363 | 0.220 | 41/97 | -0.064 | STANDARD |
| Jake Sanderson: 1+ points | 0.377 | 0.515 | 53/50 | +0.105 | STANDARD |
| Tim Stutzle: 1+ points | 0.544 | 0.645 | 66/37 | +0.070 | STANDARD |
| Jake Sanderson: 2+ points | 0.083 | 0.175 | 20/85 | +0.058 | STANDARD |
| Tim Stutzle: 1+ assists | 0.365 | 0.455 | 47/56 | +0.058 | STANDARD |

**VAN @ SJS** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 25.57, exp saves 22.26 (sd 6.27), pull risk 0.063
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.42, exp saves 25.09 (sd 7.01), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.417 | 0.575 | 60/45 | +0.116 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.280 | 0.410 | 42/60 | +0.103 | STANDARD |
| Macklin Celebrini: 2+ points | 0.329 | 0.450 | 47/57 | +0.084 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.464 | 0.585 | 59/42 | +0.099 | STANDARD |
| Ivar Stenberg: 1+ goals | 0.194 | 0.310 | 32/70 | +0.091 | STANDARD |
| Ivar Stenberg: 2+ points | 0.109 | 0.220 | 23/79 | +0.089 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
