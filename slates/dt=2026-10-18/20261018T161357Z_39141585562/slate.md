# NHL slate 2026-10-18 — RESEARCH_ONLY

generated 2026-10-18T16:13:57Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2438 · contracts joined: 442 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 392, 'OK': 40, 'NO_EDGE': 10}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 59, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 120, 'game_overtime': 2, 'player_points': 86, 'goalie_saves': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ MIN | 2026-10-18T22:00:00Z | T-3h | 0.676 | 0.324 | 0.162 | 6.24 | 3.69 | 2.55 | 226 (25/201) | CONFIRMED/PROJECTED |
| CAR @ CGY | 2026-10-19T00:00:00Z | T-6h | 0.439 | 0.561 | 0.180 | 5.91 | 2.77 | 3.14 | 216 (25/191) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4 | team_total | 0.396 | 0.520 | 0.495 | 53 | 49 | no | +0.097 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CAR3 | game_spread | 0.204 | 0.315 | 0.290 | 32 | 69 | no | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5 | team_total | 0.211 | 0.320 | 0.296 | 33 | 69 | no | +0.084 | OK |
| KXNHLGAME-26OCT18CARCGY-CAR | game_winner | 0.561 | 0.665 | 0.645 | 67 | 34 | no | +0.083 | OK |
| KXNHLGAME-26OCT18CARCGY-CGY | game_winner | 0.439 | 0.335 | 0.355 | 34 | 67 | yes | +0.083 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CAR2 | game_spread | 0.330 | 0.435 | 0.413 | 44 | 57 | no | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR3 | team_total | 0.614 | 0.725 | 0.704 | 74 | 29 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR2 | team_total | 0.819 | 0.890 | 0.878 | 90 | 12 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CGY2 | game_spread | 0.230 | 0.165 | 0.177 | 17 | 84 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT18CARCGY-6 | game_total | 0.513 | 0.585 | 0.571 | 59 | 42 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT18CARCGY-5 | game_total | 0.736 | 0.795 | 0.784 | 80 | 21 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT18CARCGY-7 | game_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT18CARCGY-4 | game_total | 0.824 | 0.875 | 0.866 | 88 | 13 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3 | team_total | 0.525 | 0.465 | 0.477 | 47 | 54 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR6 | team_total | 0.097 | 0.145 | 0.134 | 15 | 86 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-MIN2 | game_spread | 0.456 | 0.405 | 0.415 | 41 | 60 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT18CARCGY-8 | game_total | 0.222 | 0.265 | 0.256 | 27 | 74 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-CBJ3 | game_spread | 0.079 | 0.115 | 0.107 | 12 | 89 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY2 | team_total | 0.758 | 0.715 | 0.724 | 72 | 29 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ2 | team_total | 0.713 | 0.755 | 0.747 | 76 | 25 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CGY3 | game_spread | 0.128 | 0.095 | 0.101 | 10 | 91 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ3 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.021 | OK |
| KXNHLGAME-26OCT18CBJMIN-MIN | game_winner | 0.676 | 0.630 | 0.639 | 64 | 38 | yes | +0.020 | OK |
| KXNHLGAME-26OCT18CBJMIN-CBJ | game_winner | 0.324 | 0.365 | 0.357 | 37 | 64 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ4 | team_total | 0.266 | 0.310 | 0.301 | 32 | 70 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT18CARCGY-9 | game_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-CBJ2 | game_spread | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY5 | team_total | 0.153 | 0.125 | 0.130 | 13 | 88 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY6 | team_total | 0.064 | 0.045 | 0.048 | 5 | 96 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ5 | team_total | 0.123 | 0.145 | 0.140 | 15 | 86 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT18CARCGY-10 | game_total | 0.067 | 0.090 | 0.085 | 10 | 92 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-MIN3 | game_spread | 0.311 | 0.285 | 0.290 | 29 | 72 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY4 | team_total | 0.311 | 0.280 | 0.286 | 29 | 73 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT18CARCGY-3 | game_total | 0.951 | 0.970 | 0.967 | 98 | 4 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-4 | game_total | 0.858 | 0.880 | 0.876 | 89 | 13 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-5 | game_total | 0.774 | 0.800 | 0.795 | 81 | 21 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN3 | team_total | 0.728 | 0.700 | 0.706 | 71 | 31 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN6 | team_total | 0.162 | 0.145 | 0.148 | 15 | 86 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN4 | team_total | 0.520 | 0.495 | 0.500 | 50 | 51 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ6 | team_total | 0.046 | 0.055 | 0.053 | 6 | 95 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT18CARCGY-2 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-7 | game_total | 0.456 | 0.475 | 0.471 | 48 | 53 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-3 | game_total | 0.962 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-2 | game_total | 0.984 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-6 | game_total | 0.570 | 0.590 | 0.586 | 60 | 42 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN2 | team_total | 0.880 | 0.875 | 0.876 | 88 | 13 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN5 | team_total | 0.317 | 0.300 | 0.303 | 31 | 71 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-9 | game_total | 0.187 | 0.195 | 0.193 | 20 | 81 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-8 | game_total | 0.268 | 0.275 | 0.274 | 28 | 73 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-10 | game_total | 0.087 | 0.090 | 0.089 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHL1P-26OCT18CBJMIN-CBJ | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CBJMIN-MIN | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CBJMIN-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CBJMIN-CBJ2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CBJMIN-MIN2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CBJMIN-1 | period_total |  | 0.815 |  | 82 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CBJMIN-2 | period_total |  | 0.540 |  | 55 | 47 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CBJMIN-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CBJMIN-CBJ | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CBJMIN-MIN | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CBJMIN-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT18CBJMIN-CBJ2 | period_spread |  | 0.050 |  | 9 | 99 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT18CBJMIN-MIN2 | period_spread |  | 0.190 |  | 23 | 85 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CBJMIN-1 | period_total |  | 0.895 |  | 92 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CBJMIN-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CBJMIN-3 | period_total |  | 0.340 |  | 36 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CBJMIN-CBJ | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CBJMIN-MIN | period_winner |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CBJMIN-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT18CBJMIN-CBJ2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT18CBJMIN-MIN2 | period_spread |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CBJMIN-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CBJMIN-2 | period_total |  | 0.665 |  | 68 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CBJMIN-3 | period_total |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CBJMIN-CBJAFANTILLI19-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CBJMIN-CBJAFANTILLI19-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CBJMIN-CBJCCOYLE3-1 | player_assists |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CBJMIN-CBJCCOYLE3-2 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CBJMIN-CBJCGARLAND83-1 | player_assists |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT18CBJMIN-CBJDMATEYCHUK5-1 | player_assists |  | 0.255 |  | 28 | 77 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ MIN | 0.676 | 0.604 | 0.162 | 0.219 | 6.24 | 6.17 | 0.991/0.990 | KXNHLSPREAD-26OCT18CBJMIN-MIN2 -0.088 |
| CAR @ CGY | 0.439 | 0.449 | 0.180 | 0.212 | 5.91 | 6.18 | 0.986/0.984 | KXNHLTOTAL-26OCT18CARCGY-7 +0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Mathieu Olivier: 1+ goals YES @ 13c · p 0.1768 (adj 0.1613) · $6.27 · thesis CBJ:OFFENSE_4PLUS
- Valeri Nichushkin: 1+ assists NO @ 72c · p 0.8105 (adj 0.7628) · $20.0 · thesis CBJ:SUPPRESSED
- Quinn Hughes: 1+ assists NO @ 33c · p 0.4318 (adj 0.3624) · $5.76 · thesis MIN:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7147 (adj 0.6985) · $15.2 · thesis CAR:SUPPRESSED
- Carolina over 3.5 goals scored NO @ 49c · p 0.5791 (adj 0.5295) · $7.32 · thesis CAR:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 18c · p 0.2185 (adj 0.2064) · $4.66 · thesis CGY:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 69c · p 0.7882 (adj 0.7211) · $5.49 · thesis CGY:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ MIN** · priced 172/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.71, exp saves 25.25 (sd 6.6), pull risk 0.044
- CBJ net: Cam Talbot (PROJECTED) exp shots 28.7, exp saves 24.35 (sd 6.84), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jesper Wallstedt: 24+ saves | 0.606 | 0.495 | 53/54 | +0.058 |  |
| Quinn Hughes: 1+ assists | 0.568 | 0.675 | 68/33 | +0.086 | STANDARD |
| Quinn Hughes: 2+ points | 0.264 | 0.370 | 39/65 | +0.070 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.190 | 0.285 | 29/72 | +0.076 | STANDARD |
| Quinn Hughes: 2+ assists | 0.201 | 0.295 | 32/73 | +0.055 | STANDARD |
| Quinn Hughes: 1+ points | 0.633 | 0.705 | 71/30 | +0.052 | STANDARD |

**CAR @ CGY** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 31.92, exp saves 27.31 (sd 7.36), pull risk 0.069
- CAR net: Brandon Bussi (CONFIRMED) exp shots 24.78, exp saves 21.65 (sd 6.08), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.351 | 0.520 | 53/49 | +0.142 | STANDARD |
| Sebastian Aho: 2+ points | 0.182 | 0.315 | 34/71 | +0.093 | STANDARD |
| Bradly Nadeau: 1+ assists | 0.133 | 0.260 | 28/76 | +0.094 | STANDARD |
| Sebastian Aho: 1+ points | 0.538 | 0.660 | 67/35 | +0.096 | STANDARD |
| Bradly Nadeau: 1+ points | 0.294 | 0.400 | 42/62 | +0.070 | STANDARD |
| Yegor Sharangovich: 1+ goals | 0.193 | 0.105 | 17/96 | +0.013 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
