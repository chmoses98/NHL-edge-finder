# NHL slate 2026-10-29 — RESEARCH_ONLY

generated 2026-10-29T13:51:19Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3756 · contracts joined: 1867 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1592, 'OK': 142, 'NO_EDGE': 133}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 219, 'game_early_goal': 11, 'first_goal': 291, 'game_winner': 22, 'player_goals': 506, 'game_overtime': 11, 'player_points': 290, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 2026-10-29T23:00:00Z | T-6h | 0.643 | 0.357 | 0.174 | 5.75 | 3.31 | 2.43 | 202 (25/177) | PROJECTED/PROJECTED |
| UTA @ PIT | 2026-10-29T23:00:00Z | T-6h | 0.479 | 0.521 | 0.171 | 6.65 | 3.25 | 3.40 | 224 (25/199) | PROJECTED/PROJECTED |
| CBJ @ CAR | 2026-10-29T23:00:00Z | T-6h | 0.666 | 0.334 | 0.173 | 5.92 | 3.46 | 2.46 | 214 (25/189) | PROJECTED/PROJECTED |
| CHI @ DET | 2026-10-29T23:30:00Z | T-6h | 0.595 | 0.405 | 0.181 | 5.68 | 3.13 | 2.55 | 221 (25/196) | PROJECTED/PROJECTED |
| BOS @ STL | 2026-10-30T00:00:00Z | T-6h | 0.503 | 0.497 | 0.176 | 5.98 | 3.00 | 2.98 | 216 (25/191) | PROJECTED/PROJECTED |
| WSH @ NSH | 2026-10-30T00:00:00Z | T-6h | 0.483 | 0.517 | 0.169 | 6.28 | 3.08 | 3.20 | 220 (25/195) | PROJECTED/PROJECTED |
| MTL @ DAL | 2026-10-30T00:00:00Z | T-6h | 0.589 | 0.411 | 0.184 | 5.80 | 3.17 | 2.63 | 212 (25/187) | PROJECTED/CONFIRMED |
| NYI @ MIN | 2026-10-30T00:00:00Z | T-6h | 0.599 | 0.401 | 0.179 | 5.84 | 3.23 | 2.61 | 205 (25/180) | PROJECTED/PROJECTED |
| BUF @ ANA | 2026-10-30T02:00:00Z | T-12h | 0.504 | 0.496 | 0.171 | 6.46 | 3.25 | 3.21 | 51 (25/26) | PROJECTED/PROJECTED |
| OTT @ LAK | 2026-10-30T02:00:00Z | T-12h | 0.535 | 0.465 | 0.179 | 6.19 | 3.21 | 2.98 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ SJS | 2026-10-30T02:00:00Z | T-12h | 0.613 | 0.387 | 0.160 | 6.77 | 3.75 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT29CHIDET-5 | game_total | 0.703 | 0.785 | 0.770 | 79 | 22 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT29WPGTB-6 | game_total | 0.484 | 0.565 | 0.549 | 57 | 44 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET4 | team_total | 0.394 | 0.475 | 0.459 | 48 | 53 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB4 | team_total | 0.434 | 0.515 | 0.499 | 52 | 49 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT29CHIDET-6 | game_total | 0.475 | 0.560 | 0.543 | 57 | 45 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4 | team_total | 0.410 | 0.490 | 0.474 | 50 | 52 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT29CHIDET-7 | game_total | 0.364 | 0.440 | 0.424 | 45 | 57 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4 | team_total | 0.464 | 0.540 | 0.525 | 55 | 47 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5 | team_total | 0.267 | 0.335 | 0.321 | 34 | 67 | no | +0.048 | OK |
| KXNHLGAME-26OCT29BUFANA-ANA | game_winner | 0.504 | 0.435 | 0.449 | 44 | 57 | yes | +0.047 | OK |
| KXNHLGAME-26OCT29BUFANA-BUF | game_winner | 0.496 | 0.565 | 0.551 | 57 | 44 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB3 | team_total | 0.659 | 0.730 | 0.717 | 74 | 28 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT29CHIDET-4 | game_total | 0.806 | 0.865 | 0.855 | 87 | 14 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB5 | team_total | 0.240 | 0.315 | 0.299 | 33 | 70 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF3 | game_spread | 0.173 | 0.240 | 0.225 | 25 | 77 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB3 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT29WPGTB-7 | game_total | 0.370 | 0.440 | 0.426 | 45 | 57 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT29WPGTB-5 | game_total | 0.715 | 0.775 | 0.764 | 78 | 23 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET5 | team_total | 0.206 | 0.270 | 0.256 | 28 | 74 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB2 | team_total | 0.843 | 0.895 | 0.886 | 90 | 11 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5 | team_total | 0.227 | 0.295 | 0.280 | 31 | 72 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR3 | game_spread | 0.276 | 0.335 | 0.323 | 34 | 67 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-4 | game_total | 0.813 | 0.865 | 0.856 | 87 | 14 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3 | team_total | 0.628 | 0.695 | 0.682 | 71 | 32 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-5 | game_total | 0.721 | 0.775 | 0.765 | 78 | 23 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT29WPGTB-TB2 | game_spread | 0.406 | 0.465 | 0.453 | 47 | 54 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET3 | team_total | 0.620 | 0.685 | 0.672 | 70 | 33 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT29CHIDET-8 | game_total | 0.185 | 0.245 | 0.232 | 26 | 77 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT29CBJCAR-CAR2 | game_spread | 0.420 | 0.475 | 0.464 | 48 | 53 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT2 | game_spread | 0.254 | 0.305 | 0.294 | 31 | 70 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT29BUFANA-ANA2 | game_spread | 0.294 | 0.245 | 0.254 | 25 | 76 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-7 | game_total | 0.402 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR3 | team_total | 0.686 | 0.745 | 0.734 | 76 | 27 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29WPGTB-8 | game_total | 0.197 | 0.250 | 0.239 | 26 | 76 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET2 | team_total | 0.822 | 0.865 | 0.857 | 87 | 14 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-7 | game_total | 0.383 | 0.440 | 0.428 | 45 | 57 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT29BUFANA-BUF2 | game_spread | 0.285 | 0.335 | 0.325 | 34 | 67 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-6 | game_total | 0.514 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29WPGTB-9 | game_total | 0.131 | 0.175 | 0.165 | 18 | 83 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-6 | game_total | 0.495 | 0.545 | 0.535 | 55 | 46 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29WPGTB-4 | game_total | 0.813 | 0.860 | 0.852 | 87 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT29CHIDET-9 | game_total | 0.123 | 0.165 | 0.156 | 17 | 84 | no | +0.027 | OK |
| KXNHLGAME-26OCT29OTTLA-LA | game_winner | 0.535 | 0.485 | 0.495 | 49 | 52 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF6 | team_total | 0.105 | 0.150 | 0.140 | 16 | 86 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI2 | team_total | 0.711 | 0.760 | 0.751 | 77 | 25 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT29BUFANA-BUF2 | team_total | 0.826 | 0.875 | 0.866 | 89 | 14 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL4 | team_total | 0.407 | 0.460 | 0.449 | 47 | 55 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT29BUFANA-7 | game_total | 0.487 | 0.535 | 0.525 | 54 | 47 | no | +0.025 | OK |
| KXNHLGAME-26OCT29NYIMIN-MIN | game_winner | 0.599 | 0.645 | 0.636 | 65 | 36 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT29NYIMIN-MIN4 | team_total | 0.418 | 0.465 | 0.456 | 47 | 54 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT29CHIDET-DET3 | game_spread | 0.223 | 0.265 | 0.256 | 27 | 74 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT29WPGTB-TB6 | team_total | 0.108 | 0.150 | 0.141 | 16 | 86 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT29OTTLA-OTT3 | game_spread | 0.147 | 0.190 | 0.181 | 20 | 82 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN3 | game_spread | 0.234 | 0.280 | 0.270 | 29 | 73 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-4 | game_total | 0.829 | 0.870 | 0.863 | 88 | 14 | no | +0.022 | OK |
| KXNHLGAME-26OCT29WPGTB-TB | game_winner | 0.643 | 0.685 | 0.677 | 69 | 32 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR2 | team_total | 0.861 | 0.900 | 0.893 | 91 | 11 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT29BUFANA-6 | game_total | 0.602 | 0.650 | 0.641 | 66 | 36 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR6 | team_total | 0.129 | 0.170 | 0.161 | 18 | 84 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-8 | game_total | 0.206 | 0.250 | 0.241 | 26 | 76 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL3 | team_total | 0.624 | 0.670 | 0.661 | 68 | 34 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT29MTLDAL-9 | game_total | 0.140 | 0.175 | 0.167 | 18 | 83 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT29MTLDAL-DAL5 | team_total | 0.217 | 0.265 | 0.255 | 28 | 75 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29UTAPIT-5 | game_total | 0.822 | 0.855 | 0.849 | 86 | 15 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT29CBJCAR-8 | game_total | 0.218 | 0.260 | 0.251 | 27 | 75 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT29NYIMIN-MIN2 | game_spread | 0.365 | 0.405 | 0.397 | 41 | 60 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-CHI3 | team_total | 0.475 | 0.515 | 0.507 | 52 | 49 | no | +0.017 | OK |
| KXNHLGAME-26OCT29OTTLA-OTT | game_winner | 0.465 | 0.510 | 0.501 | 52 | 50 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT29OTTLA-LA2 | game_spread | 0.311 | 0.270 | 0.278 | 28 | 74 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT29UTAPIT-UTA4 | team_total | 0.456 | 0.495 | 0.487 | 50 | 51 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT29UTAPIT-UTA2 | team_total | 0.846 | 0.880 | 0.874 | 89 | 13 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT29UTAPIT-UTA3 | team_total | 0.669 | 0.710 | 0.702 | 72 | 30 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT29UTAPIT-6 | game_total | 0.629 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLGAME-26OCT29NYIMIN-NYI | game_winner | 0.401 | 0.365 | 0.372 | 37 | 64 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT29OTTLA-LA4 | team_total | 0.411 | 0.365 | 0.374 | 38 | 65 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT29WSHNSH-NSH2 | game_spread | 0.271 | 0.305 | 0.298 | 31 | 70 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT29BOSSTL-5 | game_total | 0.743 | 0.775 | 0.769 | 78 | 23 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT29CHIDET-DET6 | team_total | 0.089 | 0.120 | 0.113 | 13 | 89 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT29WSHNSH-6 | game_total | 0.570 | 0.605 | 0.598 | 61 | 40 | no | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ TBL | 0.643 | 0.624 | 0.174 | 0.216 | 5.75 | 5.99 | 0.958/1.002 | KXNHLTOTAL-26OCT29WPGTB-7 +0.048 |
| UTA @ PIT | 0.479 | 0.510 | 0.171 | 0.213 | 6.65 | 6.70 | 1.034/0.993 | KXNHLSPREAD-26OCT29UTAPIT-UTA2 -0.037 |
| CBJ @ CAR | 0.666 | 0.573 | 0.173 | 0.216 | 5.92 | 6.21 | 0.998/0.965 | KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3 +0.102 |
| CHI @ DET | 0.595 | 0.605 | 0.181 | 0.218 | 5.68 | 6.10 | 1.003/1.004 | KXNHLTOTAL-26OCT29CHIDET-7 +0.076 |
| BOS @ STL | 0.503 | 0.523 | 0.176 | 0.213 | 5.98 | 6.37 | 0.993/0.969 | KXNHLTOTAL-26OCT29BOSSTL-7 +0.069 |
| WSH @ NSH | 0.483 | 0.524 | 0.169 | 0.216 | 6.28 | 6.32 | 1.001/0.961 | KXNHLSPREAD-26OCT29WSHNSH-WSH2 -0.043 |
| MTL @ DAL | 0.589 | 0.560 | 0.184 | 0.218 | 5.80 | 6.09 | 0.987/0.943 | KXNHLTEAMTOTAL-26OCT29MTLDAL-MTL3 +0.057 |
| NYI @ MIN | 0.599 | 0.566 | 0.179 | 0.218 | 5.84 | 6.13 | 0.996/0.957 | KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3 +0.064 |
| BUF @ ANA | 0.504 | 0.564 | 0.171 | 0.219 | 6.46 | 6.63 | 1.025/0.998 | KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3 +0.063 |
| OTT @ LAK | 0.535 | 0.537 | 0.179 | 0.218 | 6.19 | 6.02 | 0.993/1.051 | KXNHLTOTAL-26OCT29OTTLA-8 -0.030 |
| VAN @ SJS | 0.613 | 0.558 | 0.160 | 0.209 | 6.77 | 6.56 | 1.027/1.026 | KXNHLTEAMTOTAL-26OCT29VANSJ-SJ4 -0.063 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9188 (adj 0.9091) · $11.11 · thesis TBL:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 11c · p 0.1383 (adj 0.1287) · $1.75 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 25c · p 0.2877 (adj 0.277) · $2.56 · thesis WPG:OFFENSE_4PLUS
- Anthony Cirelli: 1+ goals YES @ 24c · p 0.2799 (adj 0.2649) · $2.19 · thesis TBL:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1633 (adj 0.14) · $4.32 · thesis PIT:WINS_BY_2PLUS
- Declan Carlile: 1+ goals YES @ 6c · p 0.0968 (adj 0.0863) · $2.88 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ goals YES @ 32c · p 0.386 (adj 0.3683) · $6.71 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 32c · p 0.4342 (adj 0.3567) · $4.05 · thesis PIT:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 17c · p 0.2526 (adj 0.2307) · $6.23 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1835 (adj 0.1689) · $3.56 · thesis CBJ:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 72c · p 0.7725 (adj 0.7581) · $8.78 · thesis CAR:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7162 (adj 0.7009) · $7.89 · thesis CAR:SUPPRESSED
- Roman Kantserov: 1+ goals NO @ 75c · p 0.8023 (adj 0.788) · $9.0 · thesis CHI:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 58c · p 0.7077 (adj 0.6182) · $4.86 · thesis CHI:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 57c · p 0.648 (adj 0.604) · $2.8 · thesis CHI:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 24c · p 0.2835 (adj 0.2714) · $3.35 · thesis STL:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 64c · p 0.6808 (adj 0.6694) · $5.4 · thesis BOS:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2267 (adj 0.2088) · $6.09 · thesis WSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 29c · p 0.3313 (adj 0.3197) · $3.0 · thesis NSH:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 52c · p 0.6058 (adj 0.5831) · $11.11 · thesis MIN:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2438 (adj 0.2253) · $5.55 · thesis NYI:OFFENSE_4PLUS
- Olli Maatta: 1+ goals YES @ 4c · p 0.0636 (adj 0.0552) · $1.56 · thesis MIN:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.1593 (adj 0.147) · $2.85 · thesis NYI:OFFENSE_4PLUS
- Anaheim wins by over 1.5 goals YES @ 25c · p 0.3439 (adj 0.2944) · $2.39 · thesis ANA:WINS_BY_2PLUS
- Buffalo wins by over 2.5 goals NO @ 77c · p 0.8578 (adj 0.8089) · $9.38 · thesis ANA:WINS
- Buffalo wins by over 1.5 goals NO @ 67c · p 0.7627 (adj 0.7139) · $3.95 · thesis ANA:WINS
- Ottawa wins by over 1.5 goals NO @ 70c · p 0.762 (adj 0.7285) · $7.27 · thesis LAK:WINS
- San Jose wins by over 2.5 goals NO @ 71c · p 0.7745 (adj 0.7398) · $8.44 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ TBL** · priced 139/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.76, exp saves 21.86 (sd 6.01), pull risk 0.04
- WPG net: Stuart Skinner (PROJECTED) exp shots 28.88, exp saves 24.56 (sd 6.84), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.505 | 0.620 | 63/39 | +0.089 | STANDARD |
| Nikita Kucherov: 2+ points | 0.342 | 0.430 | 44/58 | +0.061 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.156 | 0.235 | 27/80 | +0.033 | STANDARD |
| Anthony Cirelli: 1+ goals | 0.280 | 0.220 | 24/80 | +0.027 | STANDARD |
| Nikita Kucherov: 1+ points | 0.703 | 0.760 | 77/25 | +0.034 | STANDARD |
| Gabriel Vilardi: 1+ goals | 0.251 | 0.195 | 22/83 | +0.019 | STANDARD |

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
| Vincent Trocheck: 1+ assists | 0.237 | 0.335 | 35/68 | +0.068 | STANDARD |

**CBJ @ CAR** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.87, exp saves 20.82 (sd 5.85), pull risk 0.056
- CBJ net: Jet Greaves (PROJECTED) exp shots 30.96, exp saves 26.53 (sd 7.27), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.363 | 0.480 | 49/53 | +0.089 | STANDARD |
| Sebastian Aho: 1+ points | 0.548 | 0.650 | 66/36 | +0.076 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.517 | 0.615 | 63/40 | +0.066 | STANDARD |
| Sebastian Aho: 2+ points | 0.180 | 0.275 | 32/77 | +0.037 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.363 | 0.455 | 46/55 | +0.069 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.433 | 0.525 | 53/48 | +0.069 | STANDARD |

**CHI @ DET** · priced 161/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 24.08, exp saves 21.12 (sd 5.86), pull risk 0.046
- CHI net: Spencer Knight (PROJECTED) exp shots 30.26, exp saves 25.92 (sd 7.11), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.292 | 0.430 | 44/58 | +0.111 | STANDARD |
| Patrick Kane: 1+ points | 0.457 | 0.555 | 57/46 | +0.065 | STANDARD |
| Connor Bedard: 1+ assists | 0.352 | 0.440 | 45/57 | +0.061 | STANDARD |
| Connor Bedard: 1+ points | 0.524 | 0.610 | 62/40 | +0.059 | STANDARD |
| Roman Kantserov: 1+ points | 0.402 | 0.485 | 50/53 | +0.051 | STANDARD |
| Dylan Larkin: 1+ assists | 0.352 | 0.425 | 44/59 | +0.041 | STANDARD |

**BOS @ STL** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.11, exp saves 22.65 (sd 6.27), pull risk 0.06
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.06, exp saves 24.16 (sd 6.67), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.369 | 0.470 | 48/54 | +0.073 | STANDARD |
| David Pastrnak: 2+ points | 0.256 | 0.345 | 35/66 | +0.069 | STANDARD |
| David Pastrnak: 1+ assists | 0.452 | 0.540 | 55/47 | +0.061 | STANDARD |
| Charlie McAvoy: 1+ points | 0.445 | 0.525 | 54/49 | +0.048 | STANDARD |
| Robert Thomas: 1+ assists | 0.432 | 0.495 | 50/51 | +0.040 | STANDARD |
| Jimmy Snuggerud: 2+ points | 0.226 | 0.170 | 22/88 | -0.006 | STANDARD |

**WSH @ NSH** · priced 162/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 28.24, exp saves 24.5 (sd 6.57), pull risk 0.059
- WSH net: Logan Thompson (PROJECTED) exp shots 27.82, exp saves 23.89 (sd 6.65), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Leonard: 1+ assists | 0.321 | 0.225 | 25/80 | +0.058 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.227 | 0.155 | 16/85 | +0.057 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.272 | 0.340 | 36/68 | +0.033 | STANDARD |
| Ryan Leonard: 1+ points | 0.455 | 0.390 | 41/63 | +0.028 | STANDARD |
| Aliaksei Protas: 1+ points | 0.416 | 0.355 | 37/66 | +0.029 | STANDARD |
| Tom Wilson: 1+ assists | 0.335 | 0.275 | 29/74 | +0.031 | STANDARD |

**MTL @ DAL** · priced 157/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.03, exp saves 20.99 (sd 5.89), pull risk 0.049
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.04, exp saves 24.02 (sd 6.55), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Caufield: 1+ assists | 0.319 | 0.410 | 43/61 | +0.055 | STANDARD |
| Mikko Rantanen: 2+ points | 0.248 | 0.325 | 33/68 | +0.057 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.530 | 54/48 | +0.050 | STANDARD |
| Thomas Harley: 1+ assists | 0.429 | 0.355 | 37/66 | +0.043 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.262 | 0.190 | 21/83 | +0.040 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.370 | 0.440 | 45/57 | +0.043 | STANDARD |

**NYI @ MIN** · priced 151/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.41, exp saves 23.85 (sd 6.48), pull risk 0.052
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.87, exp saves 24.9 (sd 6.84), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.276 | 0.380 | 39/63 | +0.078 | STANDARD |
| Matt Boldy: 1+ assists | 0.407 | 0.510 | 52/50 | +0.076 | STANDARD |
| Emil Heineman: 1+ points | 0.397 | 0.295 | 33/74 | +0.052 | STANDARD |
| Emil Heineman: 1+ assists | 0.262 | 0.160 | 18/86 | +0.071 | STANDARD |
| Matt Boldy: 2+ points | 0.242 | 0.340 | 35/67 | +0.072 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.394 | 0.485 | 49/52 | +0.068 | STANDARD |

**BUF @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.32, exp saves 23.84 (sd 6.65), pull risk 0.062
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 28.64, exp saves 24.45 (sd 6.85), pull risk 0.08

**OTT @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 27.33, exp saves 23.89 (sd 6.44), pull risk 0.049
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.32, exp saves 22.7 (sd 6.3), pull risk 0.063

**VAN @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 25.57, exp saves 22.29 (sd 6.24), pull risk 0.058
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.42, exp saves 25.12 (sd 6.86), pull risk 0.076

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
