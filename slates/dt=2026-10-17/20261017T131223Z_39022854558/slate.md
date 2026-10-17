# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T13:12:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4410 · contracts joined: 2623 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2273, 'OK': 242, 'NO_EDGE': 108}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 317, 'game_early_goal': 14, 'first_goal': 434, 'game_winner': 28, 'player_goals': 743, 'game_overtime': 14, 'player_points': 415, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 2026-10-17T17:00:00Z | T-3h | 0.562 | 0.438 | 0.182 | 6.10 | 3.24 | 2.86 | 221 (25/196) | PROJECTED/PROJECTED |
| CAR @ WPG | 2026-10-17T19:30:00Z | T-6h | 0.431 | 0.569 | 0.173 | 6.03 | 2.79 | 3.24 | 201 (25/176) | PROBABLE/PROJECTED |
| VAN @ TBL | 2026-10-17T20:00:00Z | T-6h | 0.696 | 0.304 | 0.153 | 6.24 | 3.76 | 2.49 | 200 (25/175) | PROJECTED/PROJECTED |
| SEA @ FLA | 2026-10-17T22:00:00Z | T-6h | 0.537 | 0.463 | 0.173 | 6.45 | 3.35 | 3.10 | 214 (25/189) | PROJECTED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-6h | 0.483 | 0.517 | 0.170 | 6.37 | 3.13 | 3.25 | 221 (25/196) | PROJECTED/PROJECTED |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-6h | 0.509 | 0.491 | 0.176 | 6.27 | 3.16 | 3.11 | 214 (25/189) | PROJECTED/PROJECTED |
| SJS @ DET | 2026-10-17T23:00:00Z | T-6h | 0.540 | 0.460 | 0.180 | 6.02 | 3.14 | 2.87 | 217 (25/192) | PROJECTED/PROJECTED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-6h | 0.476 | 0.523 | 0.186 | 5.60 | 2.74 | 2.87 | 201 (25/176) | PROJECTED/PROJECTED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-6h | 0.534 | 0.466 | 0.177 | 5.89 | 3.05 | 2.85 | 210 (25/185) | PROJECTED/PROJECTED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-6h | 0.466 | 0.534 | 0.183 | 5.67 | 2.74 | 2.93 | 204 (25/179) | PROJECTED/PROJECTED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-6h | 0.554 | 0.446 | 0.171 | 6.53 | 3.43 | 3.09 | 214 (25/189) | PROJECTED/PROJECTED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-6h | 0.507 | 0.493 | 0.189 | 5.62 | 2.83 | 2.78 | 204 (25/179) | PROJECTED/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-12h | 0.557 | 0.443 | 0.169 | 6.73 | 3.56 | 3.17 | 51 (25/26) | PROJECTED/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-12h | 0.615 | 0.385 | 0.163 | 6.77 | 3.78 | 2.99 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT17VANTB-TB3 | game_spread | 0.330 | 0.465 | 0.437 | 47 | 54 | no | +0.112 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.569 | 0.695 | 0.671 | 70 | 31 | no | +0.106 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.350 | 0.480 | 0.453 | 49 | 53 | no | +0.103 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.300 | 0.415 | 0.391 | 42 | 59 | no | +0.093 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.466 | 0.355 | 0.376 | 36 | 65 | yes | +0.090 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.534 | 0.645 | 0.624 | 65 | 36 | no | +0.090 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB2 | game_spread | 0.473 | 0.585 | 0.563 | 59 | 42 | no | +0.090 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.177 | 0.285 | 0.261 | 29 | 72 | no | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB4 | team_total | 0.536 | 0.640 | 0.620 | 65 | 37 | no | +0.078 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.537 | 0.635 | 0.616 | 64 | 37 | no | +0.076 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.463 | 0.365 | 0.384 | 37 | 64 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.174 | 0.275 | 0.252 | 29 | 74 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB5 | team_total | 0.331 | 0.430 | 0.410 | 44 | 58 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.323 | 0.420 | 0.400 | 43 | 59 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.784 | 0.870 | 0.856 | 88 | 14 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.388 | 0.300 | 0.317 | 31 | 71 | yes | +0.063 | OK |
| KXNHLGAME-26OCT17VANTB-TB | game_winner | 0.696 | 0.775 | 0.760 | 78 | 23 | no | +0.062 | OK |
| KXNHLGAME-26OCT17VANTB-VAN | game_winner | 0.304 | 0.225 | 0.240 | 23 | 78 | yes | +0.062 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.204 | 0.285 | 0.267 | 29 | 72 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.324 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.605 | 0.520 | 0.537 | 53 | 49 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB6 | team_total | 0.170 | 0.255 | 0.236 | 27 | 76 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.258 | 0.185 | 0.198 | 19 | 82 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.701 | 0.775 | 0.761 | 78 | 23 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.549 | 0.630 | 0.614 | 64 | 38 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.358 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB3 | team_total | 0.735 | 0.810 | 0.796 | 82 | 20 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.459 | 0.535 | 0.520 | 54 | 47 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.332 | 0.405 | 0.390 | 41 | 60 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.352 | 0.425 | 0.410 | 43 | 58 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.251 | 0.180 | 0.193 | 19 | 83 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.208 | 0.145 | 0.156 | 15 | 86 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.555 | 0.625 | 0.611 | 63 | 38 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.731 | 0.800 | 0.787 | 81 | 21 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6 | team_total | 0.132 | 0.075 | 0.084 | 8 | 93 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.271 | 0.335 | 0.321 | 34 | 67 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 | team_total | 0.399 | 0.470 | 0.456 | 48 | 54 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4 | team_total | 0.419 | 0.495 | 0.480 | 51 | 52 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.399 | 0.465 | 0.452 | 47 | 54 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.669 | 0.600 | 0.614 | 61 | 41 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK3 | game_spread | 0.272 | 0.335 | 0.322 | 34 | 67 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.166 | 0.225 | 0.212 | 23 | 78 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.799 | 0.855 | 0.845 | 86 | 15 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR3 | game_spread | 0.215 | 0.275 | 0.262 | 28 | 73 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.458 | 0.390 | 0.403 | 40 | 62 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.512 | 0.580 | 0.567 | 59 | 43 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR3 | team_total | 0.634 | 0.695 | 0.683 | 70 | 31 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.187 | 0.245 | 0.232 | 25 | 76 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK2 | game_spread | 0.403 | 0.465 | 0.452 | 47 | 54 | no | +0.040 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.517 | 0.455 | 0.467 | 46 | 55 | yes | +0.040 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.483 | 0.545 | 0.533 | 55 | 46 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.073 | 0.125 | 0.113 | 13 | 88 | no | +0.039 | OK |
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.385 | 0.325 | 0.337 | 33 | 68 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.302 | 0.245 | 0.256 | 25 | 76 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA3 | game_spread | 0.160 | 0.215 | 0.203 | 22 | 79 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA5 | team_total | 0.160 | 0.220 | 0.207 | 23 | 79 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.160 | 0.220 | 0.207 | 23 | 79 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT2 | game_spread | 0.286 | 0.345 | 0.333 | 35 | 66 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 | team_total | 0.545 | 0.610 | 0.597 | 62 | 40 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR2 | game_spread | 0.346 | 0.405 | 0.393 | 41 | 60 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.751 | 0.805 | 0.795 | 81 | 20 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.300 | 0.245 | 0.255 | 25 | 76 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-8 | game_total | 0.219 | 0.275 | 0.263 | 28 | 73 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA2 | team_total | 0.773 | 0.830 | 0.820 | 84 | 18 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-VAN4 | team_total | 0.248 | 0.195 | 0.205 | 20 | 81 | yes | +0.037 | OK |
| KXNHLGAME-26OCT17STLNSH-NSH | game_winner | 0.554 | 0.495 | 0.507 | 50 | 51 | yes | +0.037 | OK |
| KXNHLGAME-26OCT17STLNSH-STL | game_winner | 0.446 | 0.505 | 0.493 | 51 | 50 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT17BOSLA-4 | game_total | 0.794 | 0.845 | 0.836 | 85 | 16 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL3 | team_total | 0.619 | 0.680 | 0.668 | 69 | 33 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT17VANTB-VAN2 | game_spread | 0.142 | 0.095 | 0.103 | 10 | 91 | yes | +0.035 | OK |
| KXNHLGAME-26OCT17CARWPG-CAR | game_winner | 0.569 | 0.625 | 0.614 | 63 | 38 | no | +0.035 | OK |
| KXNHLGAME-26OCT17CARWPG-WPG | game_winner | 0.431 | 0.375 | 0.386 | 38 | 63 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-VAN3 | team_total | 0.451 | 0.395 | 0.406 | 40 | 61 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.418 | 0.475 | 0.464 | 48 | 53 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT17SJDET-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-VAN2 | team_total | 0.700 | 0.645 | 0.656 | 65 | 36 | yes | +0.034 | OK |
| KXNHLGAME-26OCT17BUFMTL-BUF | game_winner | 0.491 | 0.435 | 0.446 | 44 | 57 | yes | +0.034 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 0.562 | 0.547 | 0.182 | 0.218 | 6.10 | 6.19 | 0.961/0.987 | KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 +0.031 |
| CAR @ WPG | 0.431 | 0.460 | 0.173 | 0.218 | 6.03 | 6.34 | 0.994/0.997 | KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3 +0.063 |
| VAN @ TBL | 0.696 | 0.631 | 0.153 | 0.209 | 6.24 | 6.22 | 0.958/1.026 | KXNHLSPREAD-26OCT17VANTB-TB2 -0.070 |
| SEA @ FLA | 0.537 | 0.524 | 0.173 | 0.221 | 6.45 | 6.27 | 0.998/1.005 | KXNHLTOTAL-26OCT17SEAFLA-6 -0.038 |
| NYI @ TOR | 0.483 | 0.517 | 0.170 | 0.220 | 6.37 | 6.28 | 0.965/0.956 | KXNHLGAME-26OCT17NYITOR-NYI -0.034 |
| BUF @ MTL | 0.509 | 0.523 | 0.176 | 0.216 | 6.27 | 6.42 | 0.976/0.998 | KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 +0.032 |
| SJS @ DET | 0.540 | 0.515 | 0.180 | 0.215 | 6.02 | 6.27 | 1.015/1.027 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ4 +0.052 |
| OTT @ PHI | 0.476 | 0.491 | 0.186 | 0.228 | 5.60 | 5.74 | 0.993/0.998 | KXNHLTEAMTOTAL-26OCT17OTTPHI-PHI3 +0.033 |
| NYR @ CBJ | 0.534 | 0.558 | 0.177 | 0.220 | 5.89 | 6.10 | 0.964/0.992 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ3 +0.041 |
| DAL @ CHI | 0.466 | 0.457 | 0.183 | 0.222 | 5.67 | 6.19 | 1.003/0.986 | KXNHLTOTAL-26OCT17DALCHI-7 +0.098 |
| STL @ NSH | 0.554 | 0.506 | 0.171 | 0.220 | 6.53 | 6.42 | 0.994/1.016 | KXNHLSPREAD-26OCT17STLNSH-NSH2 -0.049 |
| BOS @ LAK | 0.507 | 0.542 | 0.189 | 0.222 | 5.62 | 6.05 | 0.989/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.557 | 0.522 | 0.169 | 0.210 | 6.73 | 6.89 | 0.993/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.046 |
| PIT @ VGK | 0.615 | 0.628 | 0.163 | 0.203 | 6.77 | 6.50 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-8 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 32 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2429 (adj 0.2272) · $5.11 · thesis WSH:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 66c · p 0.7055 (adj 0.6916) · $5.21 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 75c · p 0.7884 (adj 0.7775) · $5.86 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 53c · p 0.6515 (adj 0.5628) · $3.33 · thesis NJD:SUPPRESSED
- Mike Reilly: 1+ goals YES @ 4c · p 0.0568 (adj 0.0551) · $1.56 · thesis CAR:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 73c · p 0.8095 (adj 0.7672) · $9.6 · thesis WPG:WINS
- Cole Koepke: 1+ goals YES @ 9c · p 0.1157 (adj 0.1093) · $1.54 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 31c · p 0.3516 (adj 0.3412) · $2.26 · thesis WPG:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 15c · p 0.209 (adj 0.1942) · $4.14 · thesis VAN:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 54c · p 0.7285 (adj 0.6027) · $9.6 · thesis GAME:TIGHT
- Linus Karlsson: 1+ goals YES @ 15c · p 0.1931 (adj 0.1823) · $2.76 · thesis VAN:OFFENSE_4PLUS
- Jake Guentzel: 1+ goals NO @ 60c · p 0.6626 (adj 0.6444) · $6.92 · thesis TBL:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7135 (adj 0.6926) · $9.6 · thesis FLA:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1413 (adj 0.1285) · $2.51 · thesis SEA:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 72c · p 0.8018 (adj 0.7584) · $7.85 · thesis SEA:WINS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1543 (adj 0.1345) · $1.9 · thesis SEA:OFFENSE_4PLUS
- Easton Cowan: 1+ assists YES @ 26c · p 0.3275 (adj 0.2863) · $1.96 · thesis TOR:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2406 (adj 0.2317) · $1.52 · thesis NYI:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 23c · p 0.2852 (adj 0.2689) · $4.03 · thesis BUF:OFFENSE_4PLUS
- Zach Benson: 1+ assists YES @ 34c · p 0.4122 (adj 0.3686) · $1.86 · thesis BUF:OFFENSE_4PLUS
- Jack Quinn: 1+ goals YES @ 27c · p 0.3057 (adj 0.2955) · $1.55 · thesis BUF:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.814 (adj 0.7237) · $9.6 · thesis SJS:SUPPRESSED
- Collin Graf: 1+ goals YES @ 13c · p 0.1716 (adj 0.1499) · $1.57 · thesis SJS:OFFENSE_4PLUS
- Tim Stutzle: 1+ assists NO @ 50c · p 0.6238 (adj 0.5368) · $4.01 · thesis OTT:SUPPRESSED
- Dylan Cozens: 1+ assists NO @ 67c · p 0.7336 (adj 0.6993) · $4.11 · thesis OTT:SUPPRESSED
- Andre Burakovsky: 1+ assists NO @ 75c · p 0.849 (adj 0.7749) · $6.28 · thesis OTT:SUPPRESSED
- Ottawa wins by over 2.5 goals NO @ 78c · p 0.8304 (adj 0.8027) · $3.97 · thesis PHI:WINS
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.7861 (adj 0.748) · $6.98 · thesis NYR:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 72c · p 0.8074 (adj 0.7612) · $9.6 · thesis CHI:WINS
- Chicago over 2.5 goals scored YES @ 50c · p 0.579 (adj 0.5345) · $2.0 · thesis CHI:OFFENSE_4PLUS
- Matthew Wood: 1+ goals YES @ 17c · p 0.2137 (adj 0.194) · $1.91 · thesis NSH:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.8261 (adj 0.7409) · $9.29 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ WSH** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 29.7, exp saves 25.94 (sd 6.9), pull risk 0.05
- NJD net: Jake Allen (PROJECTED) exp shots 26.3, exp saves 22.7 (sd 6.39), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.348 | 0.485 | 50/53 | +0.104 | STANDARD |
| Jack Hughes: 1+ points | 0.541 | 0.645 | 66/37 | +0.073 | STANDARD |
| Jesper Bratt: 1+ assists | 0.354 | 0.445 | 46/57 | +0.059 | STANDARD |
| Ryan Leonard: 1+ assists | 0.375 | 0.285 | 30/73 | +0.060 | STANDARD |
| Nico Hischier: 1+ assists | 0.284 | 0.370 | 38/64 | +0.060 | STANDARD |
| Nico Hischier: 1+ points | 0.466 | 0.550 | 56/46 | +0.057 | STANDARD |

**CAR @ WPG** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.7, exp saves 25.52 (sd 6.9), pull risk 0.066
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.96, exp saves 20.7 (sd 5.96), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.370 | 0.470 | 49/55 | +0.062 | STANDARD |
| Sebastian Aho: 1+ points | 0.549 | 0.645 | 66/37 | +0.065 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.440 | 0.505 | 53/52 | +0.022 | STANDARD |
| Kyle Connor: 2+ points | 0.304 | 0.240 | 29/81 | -0.000 | STANDARD |
| Gabriel Vilardi: 1+ points | 0.542 | 0.480 | 50/54 | +0.024 | STANDARD |
| Sebastian Aho: 2+ points | 0.195 | 0.255 | 31/80 | -0.006 | STANDARD |

**VAN @ TBL** · priced 142/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.47, exp saves 20.71 (sd 5.84), pull risk 0.044
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.69, exp saves 26.07 (sd 7.19), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.684 | 0.465 | 84/91 | -0.165 | STANDARD |
| John Carlson: 1+ points | 0.413 | 0.605 | 62/41 | +0.160 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.510 | 53/51 | +0.152 | STANDARD |
| John Carlson: 1+ assists | 0.332 | 0.520 | 54/50 | +0.150 | STANDARD |
| Brandon Hagel: 1+ points | 0.669 | 0.485 | 71/74 | -0.055 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.509 | 0.655 | 68/37 | +0.105 | STANDARD |

**SEA @ FLA** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 25.35, exp saves 21.99 (sd 6.17), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.21 (sd 6.89), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Tkachuk: 1+ points | 0.627 | 0.475 | 70/75 | -0.088 | STANDARD |
| Brady Tkachuk: 1+ points | 0.511 | 0.630 | 65/39 | +0.082 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.300 | 0.415 | 43/60 | +0.083 | STANDARD |
| Sam Reinhart: 1+ points | 0.506 | 0.620 | 64/40 | +0.078 | STANDARD |
| Sam Reinhart: 1+ assists | 0.307 | 0.420 | 43/59 | +0.086 | STANDARD |
| Kaapo Kakko: 1+ points | 0.464 | 0.360 | 38/66 | +0.068 | STANDARD |

**NYI @ TOR** · priced 164/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.61, exp saves 26.57 (sd 7.05), pull risk 0.06
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.0, exp saves 22.37 (sd 6.32), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ goals | 0.304 | 0.180 | 34/98 | -0.052 | STANDARD |
| Easton Cowan: 1+ goals | 0.190 | 0.105 | 19/98 | -0.011 | STANDARD |
| Easton Cowan: 1+ assists | 0.328 | 0.245 | 26/77 | +0.054 | STANDARD |
| Matias Maccelli: 1+ goals | 0.205 | 0.125 | 18/93 | +0.015 | STANDARD |
| Calum Ritchie: 1+ goals | 0.174 | 0.100 | 18/98 | -0.017 | STANDARD |
| Victor Eklund: 1+ goals | 0.175 | 0.105 | 19/98 | -0.026 | PRIOR_HEAVY |

**BUF @ MTL** · priced 154/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.31, exp saves 24.61 (sd 6.71), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.14, exp saves 22.52 (sd 6.23), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ points | 0.641 | 0.370 | 72/98 | -0.093 | STANDARD |
| Cole Caufield: 1+ goals | 0.387 | 0.255 | 43/92 | -0.060 | STANDARD |
| Josh Doan: 1+ goals | 0.255 | 0.130 | 24/98 | +0.002 | STANDARD |
| Zach Benson: 1+ points | 0.580 | 0.465 | 48/55 | +0.083 | STANDARD |
| Juraj Slafkovský: 1+ goals | 0.283 | 0.175 | 33/98 | -0.062 | STANDARD |
| Ryan McLeod: 1+ goals | 0.182 | 0.090 | 16/98 | +0.013 | STANDARD |

**SJS @ DET** · priced 159/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROJECTED) exp shots 25.93, exp saves 22.46 (sd 6.29), pull risk 0.061
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 29.07, exp saves 25.12 (sd 6.83), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ assists | 0.186 | 0.325 | 34/69 | +0.109 | PRIOR_HEAVY |
| Viktor Arvidsson: 1+ goals | 0.298 | 0.165 | 31/98 | -0.027 | STANDARD |
| Dylan Larkin: 1+ goals | 0.316 | 0.185 | 35/98 | -0.050 | STANDARD |
| Ivar Stenberg: 1+ points | 0.320 | 0.450 | 47/57 | +0.092 | PRIOR_HEAVY |
| Mason Marchment: 1+ goals | 0.236 | 0.120 | 22/98 | +0.004 | STANDARD |
| Kiefer Sherwood: 1+ goals | 0.205 | 0.100 | 18/98 | +0.015 | STANDARD |

**OTT @ PHI** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 27.39, exp saves 23.81 (sd 6.43), pull risk 0.053
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.0, exp saves 20.94 (sd 5.93), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.376 | 0.510 | 52/50 | +0.106 | STANDARD |
| Owen Tippett: 1+ goals | 0.244 | 0.120 | 22/98 | +0.012 | STANDARD |
| Tim Stutzle: 1+ goals | 0.288 | 0.165 | 31/98 | -0.037 | STANDARD |
| Tyson Foerster: 1+ goals | 0.247 | 0.125 | 23/98 | +0.005 | STANDARD |
| Andre Burakovsky: 1+ points | 0.258 | 0.375 | 39/64 | +0.086 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.151 | 0.265 | 28/75 | +0.086 | STANDARD |

**NYR @ CBJ** · priced 153/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 24.38, exp saves 21.32 (sd 5.97), pull risk 0.052
- NYR net: Dylan Garand (PROJECTED) exp shots 28.58, exp saves 24.51 (sd 6.8), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mika Zibanejad: 1+ goals | 0.279 | 0.145 | 27/98 | -0.004 | STANDARD |
| Matthew Knies: 1+ goals | 0.284 | 0.165 | 31/98 | -0.041 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.203 | 0.095 | 17/98 | +0.024 | STANDARD |
| Sean Monahan: 1+ goals | 0.229 | 0.125 | 23/98 | -0.013 | STANDARD |
| Valeri Nichushkin: 1+ goals | 0.231 | 0.130 | 24/98 | -0.021 | STANDARD |
| J.T. Miller: 1+ assists | 0.350 | 0.430 | 45/59 | +0.043 | STANDARD |

**DAL @ CHI** · priced 148/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.33, exp saves 23.53 (sd 6.47), pull risk 0.064
- DAL net: Jake Oettinger (PROJECTED) exp shots 23.84, exp saves 20.7 (sd 5.9), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jason Robertson: 1+ points | 0.642 | 0.490 | 71/73 | -0.082 | STANDARD |
| Mikko Rantanen: 1+ points | 0.626 | 0.495 | 72/73 | -0.108 | STANDARD |
| Tyler Bertuzzi: 1+ goals | 0.303 | 0.175 | 25/90 | +0.040 | STANDARD |
| Anton Frondell: 1+ goals | 0.246 | 0.120 | 17/93 | +0.066 | STANDARD |
| Frank Nazar: 1+ goals | 0.228 | 0.105 | 19/98 | +0.027 | STANDARD |
| Connor Bedard: 1+ assists | 0.347 | 0.440 | 46/58 | +0.056 | STANDARD |

**STL @ NSH** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 27.32, exp saves 23.57 (sd 6.56), pull risk 0.069
- STL net: Jordan Binnington (PROJECTED) exp shots 27.33, exp saves 23.53 (sd 6.6), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan O'Reilly: 1+ goals | 0.308 | 0.145 | 27/98 | +0.025 | STANDARD |
| Jimmy Snuggerud: 1+ goals | 0.328 | 0.170 | 32/98 | -0.007 | STANDARD |
| Filip Forsberg: 1+ goals | 0.342 | 0.190 | 34/96 | -0.014 | STANDARD |
| Connor McMichael: 1+ goals | 0.229 | 0.125 | 23/98 | -0.013 | STANDARD |
| Jake Neighbours: 1+ goals | 0.216 | 0.115 | 21/98 | -0.006 | STANDARD |
| Pius Suter: 1+ goals | 0.184 | 0.100 | 18/98 | -0.007 | STANDARD |

**BOS @ LAK** · priced 152/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.88, exp saves 22.55 (sd 6.28), pull risk 0.054
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.61 (sd 6.83), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ assists | 0.174 | 0.305 | 32/71 | +0.102 | STANDARD |
| Adrian Kempe: 1+ goals | 0.324 | 0.200 | 38/98 | -0.072 | STANDARD |
| Pavel Zacha: 1+ goals | 0.264 | 0.140 | 26/98 | -0.010 | STANDARD |
| Artemi Panarin: 1+ goals | 0.313 | 0.190 | 36/98 | -0.063 | STANDARD |
| Artemi Panarin: 1+ assists | 0.384 | 0.500 | 52/52 | +0.079 | STANDARD |
| Quinton Byfield: 1+ goals | 0.278 | 0.165 | 31/98 | -0.047 | STANDARD |

**EDM @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.03, exp saves 23.36 (sd 6.56), pull risk 0.07
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.085

**PIT @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.53, exp saves 23.36 (sd 6.36), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.79), pull risk 0.09

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
