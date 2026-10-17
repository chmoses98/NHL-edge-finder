# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T18:11:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 13 · markets on board: 4803 · contracts joined: 2816 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2491, 'OK': 245, 'NO_EDGE': 80}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 370, 'game_early_goal': 13, 'first_goal': 477, 'game_winner': 26, 'player_goals': 814, 'game_overtime': 13, 'player_points': 482, 'goalie_saves': 10, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ WPG | 2026-10-17T19:30:00Z | T-60m | 0.431 | 0.569 | 0.173 | 6.03 | 2.79 | 3.24 | 224 (25/199) | PROBABLE/PROJECTED |
| VAN @ TBL | 2026-10-17T20:00:00Z | T-90m | 0.691 | 0.309 | 0.152 | 6.26 | 3.75 | 2.50 | 203 (25/178) | PROJECTED/PROJECTED |
| SEA @ FLA | 2026-10-17T22:00:00Z | T-3h | 0.517 | 0.483 | 0.175 | 6.58 | 3.35 | 3.23 | 215 (25/190) | CONFIRMED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-3h | 0.470 | 0.530 | 0.173 | 6.33 | 3.07 | 3.26 | 234 (25/209) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-3h | 0.517 | 0.483 | 0.178 | 6.19 | 3.15 | 3.04 | 217 (25/192) | CONFIRMED/PROBABLE |
| SJS @ DET | 2026-10-17T23:00:00Z | T-3h | 0.550 | 0.450 | 0.179 | 5.95 | 3.14 | 2.81 | 221 (25/196) | CONFIRMED/CONFIRMED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-3h | 0.489 | 0.511 | 0.183 | 5.58 | 2.76 | 2.82 | 226 (25/201) | CONFIRMED/CONFIRMED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-3h | 0.531 | 0.469 | 0.177 | 5.82 | 3.00 | 2.82 | 217 (25/192) | PROBABLE/CONFIRMED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-3h | 0.464 | 0.536 | 0.188 | 5.60 | 2.70 | 2.90 | 206 (25/181) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-3h | 0.538 | 0.462 | 0.170 | 6.88 | 3.56 | 3.32 | 216 (25/191) | PROBABLE/CONFIRMED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-6h | 0.511 | 0.489 | 0.187 | 5.60 | 2.83 | 2.77 | 204 (25/179) | PROBABLE/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-6h | 0.560 | 0.440 | 0.169 | 6.72 | 3.56 | 3.16 | 219 (25/194) | PROBABLE/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-6h | 0.615 | 0.385 | 0.163 | 6.77 | 3.78 | 2.99 | 214 (25/189) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.341 | 0.495 | 0.463 | 50 | 51 | no | +0.131 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.561 | 0.710 | 0.682 | 72 | 30 | no | +0.125 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB3 | game_spread | 0.328 | 0.465 | 0.436 | 47 | 54 | no | +0.115 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.464 | 0.335 | 0.359 | 34 | 67 | yes | +0.108 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.536 | 0.665 | 0.641 | 67 | 34 | no | +0.108 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.297 | 0.425 | 0.398 | 43 | 58 | no | +0.106 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.172 | 0.295 | 0.267 | 30 | 71 | no | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.416 | 0.290 | 0.314 | 30 | 72 | yes | +0.102 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.517 | 0.635 | 0.612 | 64 | 37 | no | +0.096 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.483 | 0.365 | 0.388 | 37 | 64 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.172 | 0.295 | 0.267 | 31 | 72 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.779 | 0.890 | 0.873 | 90 | 12 | no | +0.093 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.629 | 0.510 | 0.534 | 52 | 50 | yes | +0.092 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB2 | game_spread | 0.473 | 0.585 | 0.563 | 59 | 42 | no | +0.090 | OK |
| KXNHLTOTAL-26OCT17STLNSH-7 | game_total | 0.557 | 0.445 | 0.467 | 45 | 56 | yes | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB4 | team_total | 0.536 | 0.650 | 0.628 | 66 | 36 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.233 | 0.130 | 0.147 | 14 | 88 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.309 | 0.415 | 0.393 | 42 | 59 | no | +0.084 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.355 | 0.250 | 0.269 | 26 | 76 | yes | +0.081 | OK |
| KXNHLTOTAL-26OCT17STLNSH-6 | game_total | 0.666 | 0.565 | 0.586 | 57 | 44 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.276 | 0.185 | 0.201 | 19 | 82 | yes | +0.075 | OK |
| KXNHLTOTAL-26OCT17STLNSH-9 | game_total | 0.264 | 0.175 | 0.191 | 18 | 83 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.194 | 0.285 | 0.265 | 29 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.292 | 0.200 | 0.217 | 21 | 81 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.322 | 0.420 | 0.400 | 43 | 59 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB5 | team_total | 0.333 | 0.430 | 0.410 | 44 | 58 | no | +0.070 | OK |
| KXNHLGAME-26OCT17VANTB-TB | game_winner | 0.691 | 0.775 | 0.760 | 78 | 23 | no | +0.067 | OK |
| KXNHLGAME-26OCT17VANTB-VAN | game_winner | 0.309 | 0.225 | 0.240 | 23 | 78 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.483 | 0.390 | 0.408 | 40 | 62 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.246 | 0.160 | 0.175 | 17 | 85 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB6 | team_total | 0.172 | 0.255 | 0.236 | 26 | 75 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.693 | 0.780 | 0.764 | 79 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.691 | 0.600 | 0.619 | 61 | 41 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4 | team_total | 0.419 | 0.510 | 0.492 | 52 | 50 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.350 | 0.440 | 0.421 | 45 | 57 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.460 | 0.550 | 0.532 | 56 | 46 | no | +0.063 | OK |
| KXNHLGAME-26OCT17OTTPHI-PHI | game_winner | 0.489 | 0.405 | 0.422 | 41 | 60 | yes | +0.062 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.530 | 0.445 | 0.462 | 45 | 56 | yes | +0.062 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR3 | game_spread | 0.215 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2 | team_total | 0.823 | 0.745 | 0.762 | 75 | 26 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET4 | team_total | 0.395 | 0.475 | 0.459 | 48 | 53 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.690 | 0.765 | 0.751 | 77 | 24 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR2 | game_spread | 0.346 | 0.425 | 0.409 | 43 | 58 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB3 | team_total | 0.732 | 0.815 | 0.800 | 83 | 20 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.326 | 0.410 | 0.393 | 42 | 60 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.547 | 0.630 | 0.614 | 64 | 38 | no | +0.057 | OK |
| KXNHLGAME-26OCT17CARWPG-CAR | game_winner | 0.569 | 0.645 | 0.630 | 65 | 36 | no | +0.055 | OK |
| KXNHLGAME-26OCT17CARWPG-WPG | game_winner | 0.431 | 0.355 | 0.370 | 36 | 65 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.725 | 0.795 | 0.782 | 80 | 21 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.389 | 0.465 | 0.450 | 47 | 54 | no | +0.054 | OK |
| KXNHLGAME-26OCT17OTTPHI-OTT | game_winner | 0.511 | 0.585 | 0.570 | 59 | 42 | no | +0.052 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.501 | 0.575 | 0.560 | 58 | 43 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.461 | 0.535 | 0.520 | 54 | 47 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR3 | team_total | 0.634 | 0.710 | 0.696 | 72 | 30 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.545 | 0.620 | 0.605 | 63 | 39 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.793 | 0.860 | 0.848 | 87 | 15 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.741 | 0.805 | 0.793 | 81 | 20 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17VANTB-5 | game_total | 0.773 | 0.835 | 0.824 | 84 | 17 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.152 | 0.215 | 0.201 | 22 | 79 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT2 | game_spread | 0.278 | 0.345 | 0.331 | 35 | 66 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH2 | team_total | 0.866 | 0.805 | 0.819 | 81 | 20 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA6 | team_total | 0.109 | 0.050 | 0.059 | 6 | 96 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT17SEAFLA-7 | game_total | 0.512 | 0.445 | 0.458 | 45 | 56 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET3 | team_total | 0.609 | 0.675 | 0.662 | 68 | 33 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6 | team_total | 0.150 | 0.085 | 0.096 | 10 | 93 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.409 | 0.480 | 0.466 | 49 | 53 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR5 | team_total | 0.232 | 0.300 | 0.286 | 31 | 71 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT2 | team_total | 0.766 | 0.830 | 0.819 | 84 | 18 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17STLNSH-5 | game_total | 0.844 | 0.785 | 0.798 | 79 | 22 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.351 | 0.420 | 0.406 | 43 | 59 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17SJDET-6 | game_total | 0.521 | 0.585 | 0.572 | 59 | 42 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17STLNSH-10 | game_total | 0.138 | 0.075 | 0.085 | 9 | 94 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.071 | 0.130 | 0.116 | 14 | 88 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17SEAFLA-8 | game_total | 0.315 | 0.255 | 0.266 | 26 | 75 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA3 | game_spread | 0.168 | 0.115 | 0.124 | 12 | 89 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT17BOSLA-4 | game_total | 0.790 | 0.850 | 0.839 | 86 | 16 | no | +0.040 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ WPG | 0.431 | 0.460 | 0.173 | 0.218 | 6.03 | 6.34 | 0.994/0.997 | KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3 +0.063 |
| VAN @ TBL | 0.691 | 0.624 | 0.152 | 0.216 | 6.26 | 6.27 | 0.974/1.026 | KXNHLSPREAD-26OCT17VANTB-TB2 -0.077 |
| SEA @ FLA | 0.517 | 0.516 | 0.175 | 0.218 | 6.58 | 6.31 | 1.015/1.005 | KXNHLTOTAL-26OCT17SEAFLA-6 -0.044 |
| NYI @ TOR | 0.470 | 0.507 | 0.173 | 0.218 | 6.33 | 6.31 | 0.988/0.952 | KXNHLSPREAD-26OCT17NYITOR-NYI2 -0.038 |
| BUF @ MTL | 0.517 | 0.519 | 0.178 | 0.222 | 6.19 | 6.44 | 0.983/1.000 | KXNHLTOTAL-26OCT17BUFMTL-7 +0.051 |
| SJS @ DET | 0.550 | 0.519 | 0.179 | 0.219 | 5.95 | 6.21 | 0.994/1.021 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ3 +0.055 |
| OTT @ PHI | 0.489 | 0.476 | 0.183 | 0.231 | 5.58 | 5.69 | 0.994/0.968 | KXNHLTOTAL-26OCT17OTTPHI-5 +0.024 |
| NYR @ CBJ | 0.531 | 0.559 | 0.177 | 0.219 | 5.82 | 6.06 | 0.955/0.988 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ3 +0.051 |
| DAL @ CHI | 0.464 | 0.467 | 0.188 | 0.221 | 5.60 | 6.16 | 0.988/0.994 | KXNHLTOTAL-26OCT17DALCHI-7 +0.098 |
| STL @ NSH | 0.538 | 0.506 | 0.170 | 0.222 | 6.88 | 6.48 | 1.002/1.032 | KXNHLTOTAL-26OCT17STLNSH-6 -0.062 |
| BOS @ LAK | 0.511 | 0.540 | 0.187 | 0.222 | 5.60 | 6.05 | 0.988/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.560 | 0.528 | 0.169 | 0.214 | 6.72 | 6.89 | 0.991/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.047 |
| PIT @ VGK | 0.615 | 0.628 | 0.163 | 0.203 | 6.77 | 6.50 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-8 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Sebastian Aho: 1+ assists NO @ 45c · p 0.6297 (adj 0.4966) · $4.82 · thesis CAR:SUPPRESSED
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7767 (adj 0.7638) · $6.36 · thesis CAR:SUPPRESSED
- Kyle Connor: 1+ goals YES @ 37c · p 0.4116 (adj 0.4) · $2.05 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 31c · p 0.3516 (adj 0.3375) · $1.67 · thesis WPG:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.6072 (adj 0.4823) · $2.71 · thesis GAME:TIGHT
- Tampa Bay wins by over 2.5 goals NO @ 54c · p 0.7256 (adj 0.6017) · $5.64 · thesis GAME:TIGHT
- Nikita Kucherov: 1+ goals NO @ 58c · p 0.6467 (adj 0.6275) · $5.02 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals NO @ 60c · p 0.6647 (adj 0.646) · $5.26 · thesis TBL:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1478 (adj 0.1333) · $2.19 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7086 (adj 0.6902) · $4.6 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6937 (adj 0.6765) · $4.36 · thesis FLA:SUPPRESSED
- Matthew Tkachuk: 1+ goals NO @ 66c · p 0.7042 (adj 0.6894) · $2.21 · thesis FLA:SUPPRESSED
- Gavin McKenna: 1+ assists NO @ 70c · p 0.7684 (adj 0.7292) · $5.2 · thesis TOR:SUPPRESSED
- Owen Power: 1+ goals NO @ 86c · p 0.9039 (adj 0.8917) · $7.45 · thesis BUF:SUPPRESSED
- Zach Benson: 1+ goals YES @ 23c · p 0.2763 (adj 0.2635) · $2.51 · thesis BUF:OFFENSE_4PLUS
- Ryan McLeod: 1+ goals YES @ 15c · p 0.183 (adj 0.1723) · $1.42 · thesis BUF:OFFENSE_4PLUS
- Chris Kreider: 1+ goals NO @ 73c · p 0.7669 (adj 0.7564) · $4.73 · thesis MTL:SUPPRESSED
- Nate Danielson: 1+ goals NO @ 84c · p 0.884 (adj 0.8718) · $7.45 · thesis DET:SUPPRESSED
- Luca Cagnoni: 1+ assists NO @ 69c · p 0.7613 (adj 0.7231) · $6.42 · thesis SJS:SUPPRESSED
- Detroit over 3.5 goals scored NO @ 53c · p 0.599 (adj 0.562) · $2.49 · thesis DET:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2013 (adj 0.191) · $1.25 · thesis SJS:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 73c · p 0.851 (adj 0.7658) · $5.64 · thesis OTT:SUPPRESSED
- Tim Stutzle: 1+ assists NO @ 50c · p 0.626 (adj 0.5409) · $3.1 · thesis OTT:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8224 (adj 0.8093) · $6.25 · thesis PHI:SUPPRESSED
- Carter Yakemchuk: 1+ assists NO @ 71c · p 0.7802 (adj 0.7351) · $2.43 · thesis OTT:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.791 (adj 0.748) · $3.66 · thesis NYR:SUPPRESSED
- Will Cuylle: 1+ goals NO @ 78c · p 0.8126 (adj 0.8032) · $3.49 · thesis NYR:SUPPRESSED
- J.T. Miller: 1+ assists NO @ 59c · p 0.6558 (adj 0.6204) · $1.89 · thesis NYR:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 69c · p 0.7277 (adj 0.7158) · $2.13 · thesis NYR:SUPPRESSED
- Frank Nazar: 1+ goals YES @ 19c · p 0.2415 (adj 0.2274) · $2.88 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1484 (adj 0.1351) · $1.71 · thesis CHI:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 20c · p 0.2475 (adj 0.2319) · $2.23 · thesis CHI:OFFENSE_4PLUS
- Cole Smith: 1+ goals YES @ 7c · p 0.0953 (adj 0.0877) · $1.2 · thesis CHI:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 5c · p 0.0706 (adj 0.0654) · $1.09 · thesis NSH:OFFENSE_4PLUS
- Matthew Poitras: 1+ goals YES @ 10c · p 0.1311 (adj 0.1208) · $1.4 · thesis BOS:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 51c · p 0.6225 (adj 0.5396) · $2.51 · thesis LAK:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 14c · p 0.1807 (adj 0.1693) · $2.16 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1098 (adj 0.1011) · $1.52 · thesis EDM:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 20c · p 0.2454 (adj 0.2316) · $2.29 · thesis UTA:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 31c · p 0.358 (adj 0.3435) · $2.53 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 67c · p 0.7341 (adj 0.7156) · $7.45 · thesis VGK:SUPPRESSED
- Bryan Rust: 1+ goals YES @ 24c · p 0.2838 (adj 0.2691) · $1.99 · thesis PIT:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 64c · p 0.6808 (adj 0.6694) · $3.73 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ WPG** · priced 171/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.7, exp saves 25.52 (sd 6.9), pull risk 0.066
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.96, exp saves 20.7 (sd 5.96), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.370 | 0.575 | 60/45 | +0.162 | STANDARD |
| Sean Walker: 1+ points | 0.381 | 0.215 | 39/96 | -0.026 | STANDARD |
| K'Andre Miller: 1+ points | 0.373 | 0.220 | 40/96 | -0.044 | STANDARD |
| Sebastian Aho: 1+ points | 0.549 | 0.655 | 67/36 | +0.075 | STANDARD |
| Adam Lowry: 1+ assists | 0.204 | 0.105 | 20/99 | -0.007 | STANDARD |
| Alex Iafallo: 1+ points | 0.377 | 0.280 | 29/73 | +0.072 | STANDARD |

**VAN @ TBL** · priced 145/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROJECTED) exp shots 23.47, exp saves 20.67 (sd 5.82), pull risk 0.046
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.69, exp saves 26.08 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.415 | 0.610 | 63/41 | +0.158 | STANDARD |
| John Carlson: 1+ assists | 0.332 | 0.525 | 54/49 | +0.161 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.505 | 52/51 | +0.152 | STANDARD |
| Nikita Kucherov: 3+ points | 0.109 | 0.260 | 28/76 | +0.118 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.497 | 0.640 | 65/37 | +0.116 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.230 | 26/80 | +0.094 | STANDARD |

**SEA @ FLA** · priced 160/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 25.35, exp saves 22.01 (sd 6.12), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.19 (sd 6.88), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kaapo Kakko: 1+ points | 0.470 | 0.355 | 37/66 | +0.084 | STANDARD |
| Brady Tkachuk: 1+ points | 0.512 | 0.625 | 64/39 | +0.081 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.293 | 0.405 | 43/62 | +0.070 | STANDARD |
| Sam Reinhart: 1+ assists | 0.311 | 0.420 | 44/60 | +0.072 | STANDARD |
| Brady Tkachuk: 2+ points | 0.160 | 0.265 | 30/77 | +0.058 | STANDARD |
| Sam Reinhart: 1+ points | 0.513 | 0.615 | 63/40 | +0.070 | STANDARD |

**NYI @ TOR** · priced 180/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.61, exp saves 26.56 (sd 7.07), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.0, exp saves 22.41 (sd 6.3), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ assists | 0.232 | 0.310 | 32/70 | +0.054 | PRIOR_HEAVY |
| Adam Pelech: 1+ points | 0.290 | 0.215 | 23/80 | +0.048 | STANDARD |
| Gavin McKenna: 1+ points | 0.373 | 0.445 | 45/56 | +0.050 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.329 | 0.400 | 41/61 | +0.044 | STANDARD |
| Sergei Bobrovsky: 26+ saves | 0.558 | 0.490 | 51/53 | +0.030 |  |
| Darren Raddysh: 1+ assists | 0.373 | 0.440 | 46/58 | +0.030 | STANDARD |

**BUF @ MTL** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.31, exp saves 24.62 (sd 6.73), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.14, exp saves 22.47 (sd 6.39), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.628 | 0.450 | 52/62 | +0.091 |  |
| Ukko-Pekka Luukkonen: 26+ saves | 0.308 | 0.425 | 45/60 | +0.075 |  |
| Zach Benson: 1+ points | 0.562 | 0.460 | 47/55 | +0.074 | STANDARD |
| Nick Suzuki: 1+ assists | 0.461 | 0.560 | 57/45 | +0.071 | STANDARD |
| Nick Suzuki: 2+ points | 0.266 | 0.345 | 36/67 | +0.048 | STANDARD |
| Chris Kreider: 1+ points | 0.411 | 0.485 | 50/53 | +0.042 | STANDARD |

**SJS @ DET** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.93, exp saves 22.5 (sd 6.24), pull risk 0.057
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 29.07, exp saves 25.14 (sd 6.77), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.319 | 0.440 | 45/57 | +0.094 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.191 | 0.305 | 32/71 | +0.085 | PRIOR_HEAVY |
| Nate Danielson: 1+ points | 0.254 | 0.335 | 34/67 | +0.061 | STANDARD |
| Luca Cagnoni: 1+ assists | 0.239 | 0.315 | 32/69 | +0.056 | STANDARD |
| Luca Cagnoni: 1+ points | 0.285 | 0.360 | 37/65 | +0.049 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.290 | 0.365 | 39/66 | +0.034 | STANDARD |

**OTT @ PHI** · priced 170/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.39, exp saves 23.79 (sd 6.48), pull risk 0.052
- OTT net: Linus Ullmark (CONFIRMED) exp shots 24.0, exp saves 21.01 (sd 5.93), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ assists | 0.149 | 0.280 | 29/73 | +0.107 | STANDARD |
| Tim Stutzle: 1+ assists | 0.374 | 0.505 | 51/50 | +0.108 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.269 | 0.375 | 38/63 | +0.084 | STANDARD |
| Tim Stutzle: 2+ points | 0.195 | 0.295 | 33/74 | +0.052 | STANDARD |
| Tim Stutzle: 1+ points | 0.555 | 0.655 | 67/36 | +0.069 | STANDARD |
| Andre Burakovsky: 1+ points | 0.261 | 0.355 | 36/65 | +0.073 | STANDARD |

**NYR @ CBJ** · priced 160/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 24.38, exp saves 21.36 (sd 5.9), pull risk 0.047
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.58, exp saves 24.54 (sd 6.73), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Fox: 1+ assists | 0.417 | 0.510 | 52/50 | +0.065 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.209 | 0.295 | 31/72 | +0.057 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.425 | 0.510 | 52/50 | +0.057 | STANDARD |
| J.T. Miller: 1+ assists | 0.344 | 0.415 | 42/59 | +0.049 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.245 | 0.315 | 34/71 | +0.031 | STANDARD |
| Adam Fox: 1+ points | 0.478 | 0.545 | 56/47 | +0.035 | STANDARD |

**DAL @ CHI** · priced 150/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.33, exp saves 23.58 (sd 6.43), pull risk 0.064
- DAL net: Jake Oettinger (CONFIRMED) exp shots 23.84, exp saves 20.66 (sd 5.88), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jason Robertson: 2+ points | 0.269 | 0.360 | 38/66 | +0.055 | STANDARD |
| Mikko Rantanen: 2+ points | 0.259 | 0.350 | 37/67 | +0.055 | STANDARD |
| Connor Bedard: 1+ assists | 0.345 | 0.435 | 46/59 | +0.048 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.533 | 0.450 | 47/57 | +0.046 | STANDARD |
| Jason Robertson: 1+ assists | 0.394 | 0.475 | 48/53 | +0.058 | STANDARD |
| Spencer Knight: 26+ saves | 0.372 | 0.450 | 49/59 | +0.021 |  |

**STL @ NSH** · priced 161/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.32, exp saves 23.59 (sd 6.57), pull risk 0.067
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.33, exp saves 23.54 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Neighbours: 1+ assists | 0.308 | 0.230 | 26/80 | +0.035 | STANDARD |
| Jake Neighbours: 1+ points | 0.456 | 0.385 | 40/63 | +0.039 | STANDARD |
| Mason McTavish: 1+ assists | 0.254 | 0.320 | 34/70 | +0.031 | STANDARD |
| Robert Thomas: 1+ assists | 0.414 | 0.480 | 50/54 | +0.028 | STANDARD |
| Adam Jiricek: 1+ assists | 0.234 | 0.290 | 31/73 | +0.022 | PRIOR_HEAVY |
| Adam Jiricek: 1+ points | 0.296 | 0.350 | 36/66 | +0.028 | PRIOR_HEAVY |

**BOS @ LAK** · priced 145/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROBABLE) exp shots 25.88, exp saves 22.58 (sd 6.18), pull risk 0.052
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.56 (sd 6.91), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.378 | 0.505 | 52/51 | +0.095 | STANDARD |
| Fraser Minten: 1+ points | 0.436 | 0.345 | 36/67 | +0.060 | STANDARD |
| Artemi Panarin: 1+ points | 0.570 | 0.660 | 67/35 | +0.064 | STANDARD |
| JJ Peterka: 1+ assists | 0.217 | 0.300 | 32/72 | +0.049 | STANDARD |
| Fraser Minten: 1+ assists | 0.291 | 0.215 | 23/80 | +0.049 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.310 | 0.235 | 27/80 | +0.026 | STANDARD |

**EDM @ UTA** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 27.03, exp saves 23.36 (sd 6.59), pull risk 0.068
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.229 | 0.355 | 37/66 | +0.095 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.450 | 0.565 | 58/45 | +0.083 | STANDARD |
| Leon Draisaitl: 2+ points | 0.286 | 0.400 | 42/62 | +0.077 | STANDARD |
| Mattias Ekholm: 1+ points | 0.432 | 0.320 | 34/70 | +0.076 | STANDARD |
| Connor McDavid: 2+ points | 0.380 | 0.475 | 49/54 | +0.062 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.363 | 0.270 | 28/74 | +0.069 | STANDARD |

**PIT @ VGK** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.53, exp saves 23.36 (sd 6.36), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.280 | 0.425 | 44/59 | +0.113 | STANDARD |
| Jack Eichel: 1+ assists | 0.481 | 0.615 | 63/40 | +0.103 | STANDARD |
| Mitch Marner: 2+ points | 0.230 | 0.350 | 37/67 | +0.085 | STANDARD |
| Jack Eichel: 2+ assists | 0.136 | 0.250 | 28/78 | +0.072 | STANDARD |
| Trevor Connelly: 1+ points | 0.390 | 0.495 | 51/52 | +0.072 | PRIOR_HEAVY |
| Evgeni Malkin: 1+ assists | 0.284 | 0.385 | 40/63 | +0.069 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
