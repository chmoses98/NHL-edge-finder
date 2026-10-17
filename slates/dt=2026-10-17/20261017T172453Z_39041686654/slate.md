# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T17:24:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 13 · markets on board: 4822 · contracts joined: 2799 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2474, 'OK': 244, 'NO_EDGE': 81}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 362, 'game_early_goal': 13, 'first_goal': 478, 'game_winner': 26, 'player_goals': 816, 'game_overtime': 13, 'player_points': 473, 'goalie_saves': 7, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ WPG | 2026-10-17T19:30:00Z | T-90m | 0.431 | 0.569 | 0.173 | 6.03 | 2.79 | 3.24 | 214 (25/189) | PROBABLE/PROJECTED |
| VAN @ TBL | 2026-10-17T20:00:00Z | T-90m | 0.691 | 0.309 | 0.152 | 6.26 | 3.75 | 2.50 | 203 (25/178) | PROJECTED/PROJECTED |
| SEA @ FLA | 2026-10-17T22:00:00Z | T-3h | 0.517 | 0.483 | 0.175 | 6.58 | 3.35 | 3.23 | 215 (25/190) | CONFIRMED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-3h | 0.470 | 0.530 | 0.173 | 6.33 | 3.07 | 3.26 | 229 (25/204) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-3h | 0.517 | 0.483 | 0.178 | 6.19 | 3.15 | 3.04 | 217 (25/192) | CONFIRMED/PROBABLE |
| SJS @ DET | 2026-10-17T23:00:00Z | T-3h | 0.550 | 0.450 | 0.182 | 5.96 | 3.15 | 2.82 | 221 (25/196) | CONFIRMED/PROJECTED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-3h | 0.489 | 0.511 | 0.183 | 5.58 | 2.76 | 2.82 | 228 (25/203) | CONFIRMED/CONFIRMED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-3h | 0.531 | 0.469 | 0.177 | 5.82 | 3.00 | 2.82 | 216 (25/191) | PROBABLE/CONFIRMED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-3h | 0.464 | 0.536 | 0.188 | 5.60 | 2.70 | 2.90 | 205 (25/180) | CONFIRMED/CONFIRMED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-6h | 0.538 | 0.462 | 0.170 | 6.88 | 3.56 | 3.32 | 214 (25/189) | PROBABLE/CONFIRMED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-6h | 0.507 | 0.493 | 0.189 | 5.62 | 2.83 | 2.78 | 204 (25/179) | PROJECTED/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-6h | 0.557 | 0.443 | 0.169 | 6.73 | 3.56 | 3.17 | 219 (25/194) | PROJECTED/CONFIRMED |
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
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.416 | 0.295 | 0.318 | 30 | 71 | yes | +0.102 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.517 | 0.635 | 0.612 | 64 | 37 | no | +0.096 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.483 | 0.365 | 0.388 | 37 | 64 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.172 | 0.295 | 0.267 | 31 | 72 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.779 | 0.890 | 0.873 | 90 | 12 | no | +0.093 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.629 | 0.515 | 0.538 | 52 | 49 | yes | +0.092 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB2 | game_spread | 0.473 | 0.585 | 0.563 | 59 | 42 | no | +0.090 | OK |
| KXNHLTOTAL-26OCT17STLNSH-7 | game_total | 0.557 | 0.445 | 0.467 | 45 | 56 | yes | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB4 | team_total | 0.536 | 0.650 | 0.628 | 66 | 36 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.233 | 0.135 | 0.151 | 14 | 87 | yes | +0.084 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.355 | 0.250 | 0.269 | 26 | 76 | yes | +0.081 | OK |
| KXNHLTOTAL-26OCT17STLNSH-6 | game_total | 0.666 | 0.565 | 0.586 | 57 | 44 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.276 | 0.185 | 0.201 | 19 | 82 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.309 | 0.405 | 0.385 | 41 | 60 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT17STLNSH-9 | game_total | 0.264 | 0.175 | 0.191 | 18 | 83 | yes | +0.073 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.460 | 0.555 | 0.536 | 56 | 45 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.194 | 0.285 | 0.265 | 29 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.292 | 0.200 | 0.217 | 21 | 81 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.322 | 0.420 | 0.400 | 43 | 59 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.323 | 0.415 | 0.396 | 42 | 59 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB5 | team_total | 0.333 | 0.435 | 0.414 | 45 | 58 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2 | team_total | 0.823 | 0.735 | 0.755 | 74 | 27 | yes | +0.070 | OK |
| KXNHLGAME-26OCT17VANTB-TB | game_winner | 0.691 | 0.775 | 0.760 | 78 | 23 | no | +0.067 | OK |
| KXNHLGAME-26OCT17VANTB-VAN | game_winner | 0.309 | 0.225 | 0.240 | 23 | 78 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.483 | 0.390 | 0.408 | 40 | 62 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.246 | 0.160 | 0.175 | 17 | 85 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB6 | team_total | 0.172 | 0.260 | 0.240 | 27 | 75 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.693 | 0.780 | 0.764 | 79 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4 | team_total | 0.419 | 0.505 | 0.488 | 51 | 50 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.350 | 0.435 | 0.417 | 44 | 57 | no | +0.063 | OK |
| KXNHLGAME-26OCT17OTTPHI-PHI | game_winner | 0.489 | 0.405 | 0.422 | 41 | 60 | yes | +0.062 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR3 | game_spread | 0.215 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET4 | team_total | 0.393 | 0.475 | 0.458 | 48 | 53 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR2 | game_spread | 0.346 | 0.425 | 0.409 | 43 | 58 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB3 | team_total | 0.732 | 0.815 | 0.800 | 83 | 20 | no | +0.057 | OK |
| KXNHLGAME-26OCT17CARWPG-CAR | game_winner | 0.569 | 0.645 | 0.630 | 65 | 36 | no | +0.055 | OK |
| KXNHLGAME-26OCT17CARWPG-WPG | game_winner | 0.431 | 0.355 | 0.370 | 36 | 65 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.549 | 0.630 | 0.614 | 64 | 38 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.691 | 0.605 | 0.623 | 62 | 41 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.725 | 0.795 | 0.782 | 80 | 21 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.389 | 0.465 | 0.450 | 47 | 54 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.459 | 0.535 | 0.520 | 54 | 47 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLGAME-26OCT17OTTPHI-OTT | game_winner | 0.511 | 0.585 | 0.570 | 59 | 42 | no | +0.052 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.530 | 0.455 | 0.470 | 46 | 55 | yes | +0.052 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.501 | 0.575 | 0.560 | 58 | 43 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR3 | team_total | 0.634 | 0.710 | 0.696 | 72 | 30 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.545 | 0.620 | 0.605 | 63 | 39 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.793 | 0.860 | 0.848 | 87 | 15 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17VANTB-5 | game_total | 0.773 | 0.835 | 0.824 | 84 | 17 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.152 | 0.215 | 0.201 | 22 | 79 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT2 | game_spread | 0.278 | 0.345 | 0.331 | 35 | 66 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.743 | 0.810 | 0.798 | 82 | 20 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT17SJDET-6 | game_total | 0.517 | 0.585 | 0.572 | 59 | 42 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH2 | team_total | 0.866 | 0.805 | 0.819 | 81 | 20 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA6 | team_total | 0.109 | 0.050 | 0.059 | 6 | 96 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT17SEAFLA-7 | game_total | 0.512 | 0.445 | 0.458 | 45 | 56 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6 | team_total | 0.150 | 0.085 | 0.096 | 10 | 93 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR5 | team_total | 0.232 | 0.300 | 0.286 | 31 | 71 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT2 | team_total | 0.766 | 0.830 | 0.819 | 84 | 18 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17STLNSH-5 | game_total | 0.844 | 0.785 | 0.798 | 79 | 22 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.410 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17STLNSH-10 | game_total | 0.138 | 0.075 | 0.085 | 9 | 94 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.071 | 0.135 | 0.119 | 15 | 88 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA3 | game_spread | 0.168 | 0.115 | 0.124 | 12 | 89 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.352 | 0.420 | 0.406 | 43 | 59 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET3 | team_total | 0.614 | 0.675 | 0.663 | 68 | 33 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.178 | 0.240 | 0.226 | 25 | 77 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-8 | game_total | 0.207 | 0.265 | 0.253 | 27 | 74 | no | +0.040 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CAR @ WPG | 0.431 | 0.460 | 0.173 | 0.218 | 6.03 | 6.34 | 0.994/0.997 | KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3 +0.063 |
| VAN @ TBL | 0.691 | 0.624 | 0.152 | 0.216 | 6.26 | 6.27 | 0.974/1.026 | KXNHLSPREAD-26OCT17VANTB-TB2 -0.077 |
| SEA @ FLA | 0.517 | 0.516 | 0.175 | 0.218 | 6.58 | 6.31 | 1.015/1.005 | KXNHLTOTAL-26OCT17SEAFLA-6 -0.044 |
| NYI @ TOR | 0.470 | 0.507 | 0.173 | 0.218 | 6.33 | 6.31 | 0.988/0.952 | KXNHLSPREAD-26OCT17NYITOR-NYI2 -0.038 |
| BUF @ MTL | 0.517 | 0.519 | 0.178 | 0.222 | 6.19 | 6.44 | 0.983/1.000 | KXNHLTOTAL-26OCT17BUFMTL-7 +0.051 |
| SJS @ DET | 0.550 | 0.520 | 0.182 | 0.221 | 5.96 | 6.22 | 0.994/1.027 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ4 +0.052 |
| OTT @ PHI | 0.489 | 0.476 | 0.183 | 0.231 | 5.58 | 5.69 | 0.994/0.968 | KXNHLTOTAL-26OCT17OTTPHI-5 +0.024 |
| NYR @ CBJ | 0.531 | 0.559 | 0.177 | 0.219 | 5.82 | 6.06 | 0.955/0.988 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ3 +0.051 |
| DAL @ CHI | 0.464 | 0.467 | 0.188 | 0.221 | 5.60 | 6.16 | 0.988/0.994 | KXNHLTOTAL-26OCT17DALCHI-7 +0.098 |
| STL @ NSH | 0.538 | 0.506 | 0.170 | 0.222 | 6.88 | 6.48 | 1.002/1.032 | KXNHLTOTAL-26OCT17STLNSH-6 -0.062 |
| BOS @ LAK | 0.507 | 0.542 | 0.189 | 0.222 | 5.62 | 6.05 | 0.989/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.557 | 0.522 | 0.169 | 0.210 | 6.73 | 6.89 | 0.993/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.046 |
| PIT @ VGK | 0.615 | 0.628 | 0.163 | 0.203 | 6.77 | 6.50 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-8 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7767 (adj 0.7638) · $7.22 · thesis CAR:SUPPRESSED
- Kyle Connor: 1+ goals YES @ 37c · p 0.4116 (adj 0.4) · $1.99 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 31c · p 0.3516 (adj 0.3375) · $1.6 · thesis WPG:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.71 (adj 0.6963) · $3.08 · thesis CAR:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.6072 (adj 0.4823) · $2.88 · thesis GAME:TIGHT
- Tampa Bay wins by over 2.5 goals NO @ 54c · p 0.7256 (adj 0.6017) · $4.97 · thesis GAME:TIGHT
- John Carlson: 1+ goals NO @ 82c · p 0.8782 (adj 0.8599) · $6.15 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 58c · p 0.6467 (adj 0.6275) · $4.09 · thesis TBL:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1478 (adj 0.1346) · $2.55 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1554 (adj 0.1416) · $2.24 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7086 (adj 0.6902) · $7.24 · thesis FLA:SUPPRESSED
- Mackie Samoskevich: 1+ goals YES @ 19c · p 0.2334 (adj 0.2213) · $2.21 · thesis SEA:OFFENSE_4PLUS
- Gavin McKenna: 1+ assists NO @ 70c · p 0.7684 (adj 0.7292) · $5.05 · thesis TOR:SUPPRESSED
- Owen Power: 1+ goals NO @ 87c · p 0.9039 (adj 0.8929) · $7.24 · thesis BUF:SUPPRESSED
- Ryan McLeod: 1+ goals YES @ 15c · p 0.183 (adj 0.1723) · $1.37 · thesis BUF:OFFENSE_4PLUS
- Chris Kreider: 1+ goals NO @ 73c · p 0.7669 (adj 0.7564) · $4.61 · thesis MTL:SUPPRESSED
- Zach Benson: 1+ goals YES @ 24c · p 0.2763 (adj 0.2647) · $1.42 · thesis BUF:OFFENSE_4PLUS
- Nate Danielson: 1+ goals NO @ 84c · p 0.8822 (adj 0.8704) · $7.24 · thesis DET:SUPPRESSED
- Luca Cagnoni: 1+ goals NO @ 91c · p 0.9392 (adj 0.9294) · $7.24 · thesis DIFFUSE
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2038 (adj 0.1929) · $1.36 · thesis SJS:OFFENSE_4PLUS
- Detroit over 3.5 goals scored NO @ 53c · p 0.5918 (adj 0.5584) · $1.68 · thesis DET:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8224 (adj 0.8093) · $6.21 · thesis PHI:SUPPRESSED
- Andre Burakovsky: 1+ assists NO @ 74c · p 0.851 (adj 0.7691) · $5.45 · thesis OTT:SUPPRESSED
- Tim Stutzle: 1+ assists NO @ 50c · p 0.626 (adj 0.5343) · $2.22 · thesis OTT:SUPPRESSED
- Carter Yakemchuk: 1+ assists NO @ 71c · p 0.7802 (adj 0.7376) · $3.19 · thesis OTT:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.791 (adj 0.748) · $5.34 · thesis NYR:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 69c · p 0.7277 (adj 0.7158) · $3.41 · thesis NYR:SUPPRESSED
- Frank Nazar: 1+ goals YES @ 19c · p 0.2415 (adj 0.2274) · $2.8 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1484 (adj 0.1351) · $1.66 · thesis CHI:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 20c · p 0.2475 (adj 0.2319) · $2.17 · thesis CHI:OFFENSE_4PLUS
- Cole Smith: 1+ goals YES @ 7c · p 0.0953 (adj 0.0877) · $1.16 · thesis CHI:OFFENSE_4PLUS
- Dylan Peterson: 1+ goals YES @ 7c · p 0.1015 (adj 0.0924) · $1.57 · thesis STL:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 5c · p 0.0706 (adj 0.0654) · $1.06 · thesis NSH:OFFENSE_4PLUS
- Matthew Poitras: 1+ goals YES @ 10c · p 0.1269 (adj 0.1177) · $1.1 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.7878 (adj 0.7389) · $5.58 · thesis BOS:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 15c · p 0.209 (adj 0.193) · $3.15 · thesis EDM:OFFENSE_4PLUS
- Mathieu Joseph: 1+ goals YES @ 7c · p 0.1034 (adj 0.0938) · $1.54 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 29c · p 0.3555 (adj 0.3366) · $3.74 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ assists YES @ 32c · p 0.4535 (adj 0.357) · $2.43 · thesis EDM:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0865 (adj 0.0761) · $1.02 · thesis VGK:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 24c · p 0.2838 (adj 0.2703) · $2.08 · thesis PIT:OFFENSE_4PLUS
- Trevor Connelly: 1+ goals NO @ 75c · p 0.7907 (adj 0.7768) · $5.5 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 69c · p 0.7341 (adj 0.7181) · $4.18 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CAR @ WPG** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.7, exp saves 25.52 (sd 6.9), pull risk 0.066
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.96, exp saves 20.7 (sd 5.96), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nino Niederreiter: 2+ points | 0.028 | 0.500 | 97/97 | -0.000 | STANDARD |
| Viggo Bjorck: 2+ points | 0.039 | 0.505 | 97/96 | -0.001 | PRIOR_HEAVY |
| Alex Iafallo: 2+ points | 0.081 | 0.500 | 96/96 | -0.043 | STANDARD |
| Nino Niederreiter: 1+ points | 0.231 | 0.500 | 96/96 | -0.193 | STANDARD |
| Viggo Bjorck: 1+ points | 0.265 | 0.500 | 96/96 | -0.228 | PRIOR_HEAVY |
| Alex Iafallo: 1+ points | 0.377 | 0.165 | 31/98 | +0.052 | STANDARD |

**VAN @ TBL** · priced 145/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROJECTED) exp shots 23.47, exp saves 20.67 (sd 5.82), pull risk 0.046
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.69, exp saves 26.08 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.415 | 0.615 | 63/40 | +0.168 | STANDARD |
| John Carlson: 1+ assists | 0.332 | 0.520 | 54/50 | +0.151 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.505 | 52/51 | +0.152 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.497 | 0.645 | 66/37 | +0.116 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.235 | 25/78 | +0.113 | STANDARD |
| Nikita Kucherov: 3+ points | 0.109 | 0.240 | 26/78 | +0.099 | STANDARD |

**SEA @ FLA** · priced 160/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 25.35, exp saves 22.01 (sd 6.12), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.19 (sd 6.88), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ assists | 0.293 | 0.415 | 43/60 | +0.090 | STANDARD |
| Kaapo Kakko: 1+ points | 0.470 | 0.360 | 37/65 | +0.084 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.344 | 0.235 | 26/79 | +0.071 | STANDARD |
| Sam Reinhart: 1+ assists | 0.311 | 0.420 | 44/60 | +0.072 | STANDARD |
| Brady Tkachuk: 1+ points | 0.512 | 0.620 | 64/40 | +0.071 | STANDARD |
| Sam Reinhart: 1+ points | 0.513 | 0.615 | 63/40 | +0.070 | STANDARD |

**NYI @ TOR** · priced 172/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.61, exp saves 26.56 (sd 7.07), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.0, exp saves 22.41 (sd 6.3), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ assists | 0.232 | 0.310 | 32/70 | +0.054 | PRIOR_HEAVY |
| Sergei Bobrovsky: 26+ saves | 0.558 | 0.480 | 50/54 | +0.040 |  |
| Gavin McKenna: 1+ points | 0.373 | 0.445 | 45/56 | +0.050 | PRIOR_HEAVY |
| Darren Raddysh: 1+ assists | 0.373 | 0.440 | 45/57 | +0.040 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.329 | 0.395 | 41/62 | +0.034 | STANDARD |
| Darren Raddysh: 2+ points | 0.133 | 0.195 | 20/81 | +0.046 | STANDARD |

**BUF @ MTL** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.31, exp saves 24.62 (sd 6.73), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.14, exp saves 22.47 (sd 6.39), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.628 | 0.440 | 52/64 | +0.091 |  |
| Ukko-Pekka Luukkonen: 26+ saves | 0.308 | 0.485 | 50/53 | +0.144 |  |
| Nick Suzuki: 1+ assists | 0.461 | 0.560 | 58/46 | +0.061 | STANDARD |
| Zach Benson: 1+ points | 0.562 | 0.470 | 48/54 | +0.064 | STANDARD |
| Chris Kreider: 1+ assists | 0.231 | 0.310 | 33/71 | +0.045 | STANDARD |
| Nick Suzuki: 2+ points | 0.266 | 0.345 | 36/67 | +0.048 | STANDARD |

**SJS @ DET** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.93, exp saves 22.5 (sd 6.3), pull risk 0.057
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 29.07, exp saves 25.1 (sd 6.74), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.318 | 0.440 | 45/57 | +0.095 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.190 | 0.305 | 32/71 | +0.086 | PRIOR_HEAVY |
| Nate Danielson: 1+ points | 0.248 | 0.335 | 34/67 | +0.067 | STANDARD |
| Luca Cagnoni: 1+ points | 0.287 | 0.370 | 38/64 | +0.057 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.291 | 0.370 | 39/65 | +0.043 | STANDARD |
| Luca Cagnoni: 1+ assists | 0.239 | 0.310 | 32/70 | +0.046 | STANDARD |

**OTT @ PHI** · priced 172/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.39, exp saves 23.79 (sd 6.48), pull risk 0.052
- OTT net: Linus Ullmark (CONFIRMED) exp shots 24.0, exp saves 21.01 (sd 5.93), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.374 | 0.515 | 53/50 | +0.108 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.149 | 0.275 | 29/74 | +0.098 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.269 | 0.380 | 39/63 | +0.084 | STANDARD |
| Tim Stutzle: 2+ points | 0.195 | 0.300 | 33/73 | +0.061 | STANDARD |
| Andre Burakovsky: 1+ points | 0.261 | 0.365 | 37/64 | +0.083 | STANDARD |
| Tim Stutzle: 1+ points | 0.555 | 0.655 | 67/36 | +0.069 | STANDARD |

**NYR @ CBJ** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 24.38, exp saves 21.36 (sd 5.9), pull risk 0.047
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.58, exp saves 24.54 (sd 6.73), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Fox: 1+ assists | 0.417 | 0.510 | 52/50 | +0.065 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.209 | 0.295 | 31/72 | +0.057 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.425 | 0.510 | 53/51 | +0.047 | STANDARD |
| J.T. Miller: 1+ assists | 0.344 | 0.425 | 44/59 | +0.049 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.245 | 0.315 | 34/71 | +0.031 | STANDARD |
| Adam Fox: 1+ points | 0.478 | 0.545 | 56/47 | +0.035 | STANDARD |

**DAL @ CHI** · priced 149/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.33, exp saves 23.58 (sd 6.43), pull risk 0.064
- DAL net: Jake Oettinger (CONFIRMED) exp shots 23.84, exp saves 20.66 (sd 5.88), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 26+ saves | 0.372 | 0.475 | 49/54 | +0.070 |  |
| Jason Robertson: 2+ points | 0.269 | 0.365 | 39/66 | +0.055 | STANDARD |
| Mikko Rantanen: 2+ points | 0.259 | 0.350 | 37/67 | +0.055 | STANDARD |
| Connor Bedard: 1+ assists | 0.345 | 0.435 | 45/58 | +0.058 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.533 | 0.445 | 46/57 | +0.056 | STANDARD |
| Mikko Rantanen: 2+ assists | 0.124 | 0.205 | 22/81 | +0.055 | STANDARD |

**STL @ NSH** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.32, exp saves 23.59 (sd 6.57), pull risk 0.067
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.33, exp saves 23.54 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Neighbours: 1+ assists | 0.308 | 0.230 | 25/79 | +0.045 | STANDARD |
| Mason McTavish: 1+ assists | 0.254 | 0.330 | 35/69 | +0.041 | STANDARD |
| Adam Jiricek: 1+ points | 0.296 | 0.370 | 38/64 | +0.047 | PRIOR_HEAVY |
| Jake Neighbours: 1+ points | 0.456 | 0.390 | 41/63 | +0.029 | STANDARD |
| Robert Thomas: 1+ assists | 0.414 | 0.475 | 49/54 | +0.028 | STANDARD |
| Adam Jiricek: 1+ assists | 0.234 | 0.290 | 30/72 | +0.031 | PRIOR_HEAVY |

**BOS @ LAK** · priced 145/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.88, exp saves 22.55 (sd 6.28), pull risk 0.054
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.61 (sd 6.83), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.384 | 0.505 | 52/51 | +0.089 | STANDARD |
| Fraser Minten: 1+ assists | 0.297 | 0.195 | 22/83 | +0.065 | STANDARD |
| JJ Peterka: 1+ assists | 0.212 | 0.310 | 33/71 | +0.063 | STANDARD |
| Fraser Minten: 1+ points | 0.440 | 0.345 | 36/67 | +0.063 | STANDARD |
| Artemi Panarin: 2+ points | 0.212 | 0.295 | 33/74 | +0.035 | STANDARD |
| Artemi Panarin: 1+ points | 0.578 | 0.660 | 67/35 | +0.056 | STANDARD |

**EDM @ UTA** · priced 155/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.03, exp saves 23.36 (sd 6.56), pull risk 0.07
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vasily Podkolzin: 1+ points | 0.645 | 0.475 | 48/53 | +0.147 | STANDARD |
| Mattias Ekholm: 1+ points | 0.469 | 0.320 | 34/70 | +0.114 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.454 | 0.305 | 32/71 | +0.118 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.283 | 0.150 | 17/87 | +0.103 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.226 | 0.355 | 37/66 | +0.098 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.393 | 0.270 | 28/74 | +0.099 | STANDARD |

**PIT @ VGK** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.53, exp saves 23.36 (sd 6.36), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.280 | 0.415 | 43/60 | +0.103 | STANDARD |
| Jack Eichel: 1+ assists | 0.481 | 0.610 | 63/41 | +0.092 | STANDARD |
| Mitch Marner: 2+ points | 0.230 | 0.350 | 37/67 | +0.085 | STANDARD |
| Jack Eichel: 2+ assists | 0.136 | 0.250 | 28/78 | +0.072 | STANDARD |
| Trevor Connelly: 1+ points | 0.390 | 0.495 | 51/52 | +0.072 | PRIOR_HEAVY |
| Jack Eichel: 3+ points | 0.088 | 0.185 | 20/83 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
