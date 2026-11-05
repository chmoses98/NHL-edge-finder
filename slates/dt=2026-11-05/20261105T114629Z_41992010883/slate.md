# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T11:46:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 2213 · contracts joined: 561 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 286, 'OK': 126, 'NO_EDGE': 149}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'game_early_goal': 11, 'game_winner': 22, 'game_overtime': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-12h | 0.522 | 0.478 | 0.175 | 6.31 | 3.22 | 3.09 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-12h | 0.531 | 0.469 | 0.178 | 6.21 | 3.19 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-12h | 0.719 | 0.281 | 0.152 | 6.07 | 3.74 | 2.33 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-12h | 0.560 | 0.440 | 0.182 | 5.95 | 3.17 | 2.78 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-12h | 0.420 | 0.580 | 0.179 | 5.83 | 2.67 | 3.16 | 51 (25/26) | PROJECTED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-12h | 0.617 | 0.384 | 0.169 | 6.00 | 3.36 | 2.64 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-12h | 0.464 | 0.536 | 0.170 | 6.47 | 3.10 | 3.37 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-12h | 0.458 | 0.542 | 0.177 | 5.98 | 2.85 | 3.13 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-12h | 0.606 | 0.394 | 0.169 | 6.50 | 3.59 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-12h | 0.622 | 0.378 | 0.161 | 7.11 | 3.96 | 3.15 | 51 (25/26) | PROJECTED/PROJECTED |
| NSH @ COL | 2026-11-06T02:30:00Z | T-12h | 0.652 | 0.348 | 0.160 | 6.61 | 3.80 | 2.81 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.342 | 0.455 | 0.432 | 46 | 55 | no | +0.091 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.469 | 0.575 | 0.554 | 58 | 43 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.322 | 0.430 | 0.407 | 44 | 58 | no | +0.081 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.495 | 0.595 | 0.575 | 60 | 41 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.528 | 0.630 | 0.610 | 64 | 38 | no | +0.075 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.531 | 0.435 | 0.454 | 44 | 57 | yes | +0.074 | OK |
| KXNHLGAME-26NOV05STLNJ-STL | game_winner | 0.440 | 0.355 | 0.371 | 36 | 65 | yes | +0.064 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.541 | 0.625 | 0.609 | 63 | 38 | no | +0.063 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.281 | 0.205 | 0.219 | 21 | 80 | yes | +0.060 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.057 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.260 | 0.335 | 0.319 | 34 | 67 | no | +0.054 | OK |
| KXNHLGAME-26NOV05STLNJ-NJ | game_winner | 0.560 | 0.635 | 0.620 | 64 | 37 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.306 | 0.230 | 0.244 | 24 | 78 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.737 | 0.815 | 0.801 | 83 | 20 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ2 | game_spread | 0.332 | 0.405 | 0.390 | 41 | 60 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.167 | 0.235 | 0.220 | 24 | 77 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.406 | 0.320 | 0.336 | 34 | 70 | yes | +0.050 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.426 | 0.495 | 0.481 | 50 | 51 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET5 | team_total | 0.224 | 0.155 | 0.167 | 17 | 86 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.400 | 0.470 | 0.456 | 48 | 54 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.629 | 0.555 | 0.570 | 57 | 46 | yes | +0.042 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ3 | game_spread | 0.205 | 0.270 | 0.256 | 28 | 74 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.402 | 0.475 | 0.460 | 49 | 54 | no | +0.040 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.719 | 0.775 | 0.764 | 78 | 23 | no | +0.039 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.754 | 0.810 | 0.800 | 82 | 20 | no | +0.035 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.522 | 0.465 | 0.476 | 47 | 54 | yes | +0.034 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.389 | 0.445 | 0.434 | 45 | 56 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.622 | 0.685 | 0.673 | 70 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.382 | 0.450 | 0.436 | 47 | 57 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.216 | 0.270 | 0.259 | 28 | 74 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV05CHITB-8 | game_total | 0.245 | 0.305 | 0.292 | 32 | 71 | no | +0.030 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.606 | 0.655 | 0.645 | 66 | 35 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET3 | game_spread | 0.187 | 0.145 | 0.153 | 15 | 86 | yes | +0.028 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.394 | 0.345 | 0.355 | 35 | 66 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.207 | 0.165 | 0.173 | 17 | 84 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV05CHITB-4 | game_total | 0.846 | 0.890 | 0.882 | 90 | 12 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL2 | game_spread | 0.227 | 0.180 | 0.189 | 19 | 83 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.163 | 0.205 | 0.196 | 21 | 80 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.369 | 0.430 | 0.417 | 45 | 59 | no | +0.025 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.478 | 0.525 | 0.516 | 53 | 48 | no | +0.024 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.213 | 0.260 | 0.250 | 27 | 75 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV05CHITB-9 | game_total | 0.165 | 0.205 | 0.196 | 21 | 80 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.891 | 0.930 | 0.923 | 94 | 8 | no | +0.024 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.420 | 0.375 | 0.384 | 38 | 63 | yes | +0.023 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.580 | 0.625 | 0.616 | 63 | 38 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.252 | 0.300 | 0.290 | 31 | 71 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 | team_total | 0.390 | 0.435 | 0.426 | 44 | 57 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET2 | team_total | 0.824 | 0.770 | 0.782 | 79 | 25 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ2 | team_total | 0.818 | 0.855 | 0.848 | 86 | 15 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA5 | team_total | 0.205 | 0.245 | 0.237 | 25 | 76 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV05CARNYI-6 | game_total | 0.500 | 0.545 | 0.536 | 55 | 46 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.798 | 0.845 | 0.836 | 86 | 17 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA2 | team_total | 0.810 | 0.850 | 0.843 | 86 | 16 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.180 | 0.140 | 0.147 | 15 | 87 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.151 | 0.185 | 0.178 | 19 | 82 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV05CARNYI-7 | game_total | 0.385 | 0.425 | 0.417 | 43 | 58 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4 | team_total | 0.342 | 0.295 | 0.304 | 31 | 72 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV05CHITB-10 | game_total | 0.077 | 0.105 | 0.099 | 11 | 90 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.348 | 0.385 | 0.377 | 39 | 62 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET6 | team_total | 0.101 | 0.065 | 0.071 | 8 | 95 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.152 | 0.120 | 0.126 | 13 | 89 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN6 | team_total | 0.078 | 0.055 | 0.059 | 6 | 95 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-9 | game_total | 0.297 | 0.265 | 0.271 | 27 | 74 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.328 | 0.295 | 0.301 | 30 | 71 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-NYR6 | team_total | 0.119 | 0.095 | 0.099 | 10 | 91 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.273 | 0.305 | 0.298 | 31 | 70 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.622 | 0.665 | 0.657 | 68 | 35 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV05CARNYI-5 | game_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA3 | team_total | 0.602 | 0.650 | 0.641 | 67 | 37 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV05CARNYI-4 | game_total | 0.820 | 0.850 | 0.844 | 86 | 16 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL6 | team_total | 0.064 | 0.045 | 0.048 | 5 | 96 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV05NSHCOL-9 | game_total | 0.232 | 0.200 | 0.206 | 21 | 81 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.583 | 0.635 | 0.625 | 66 | 39 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.256 | 0.285 | 0.279 | 29 | 72 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5 | team_total | 0.221 | 0.185 | 0.192 | 20 | 83 | yes | +0.010 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.617 | 0.585 | 0.591 | 59 | 42 | yes | +0.010 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.384 | 0.415 | 0.409 | 42 | 59 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL3 | game_spread | 0.189 | 0.165 | 0.170 | 17 | 84 | yes | +0.009 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.522 | 0.509 | 0.175 | 0.220 | 6.31 | 6.60 | 0.976/0.993 | KXNHLTOTAL-26NOV05UTAMTL-7 +0.054 |
| VGK @ DET | 0.531 | 0.452 | 0.178 | 0.213 | 6.21 | 6.28 | 1.015/1.004 | KXNHLGAME-26NOV05VGKDET-DET -0.079 |
| CHI @ TBL | 0.719 | 0.707 | 0.152 | 0.191 | 6.07 | 6.32 | 0.958/1.004 | KXNHLTOTAL-26NOV05CHITB-7 +0.047 |
| STL @ NJD | 0.560 | 0.558 | 0.182 | 0.217 | 5.95 | 6.19 | 0.960/0.993 | KXNHLTOTAL-26NOV05STLNJ-7 +0.048 |
| CAR @ NYI | 0.420 | 0.491 | 0.179 | 0.221 | 5.83 | 6.36 | 0.957/0.997 | KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 +0.111 |
| PHI @ NYR | 0.617 | 0.539 | 0.169 | 0.225 | 6.00 | 5.98 | 0.987/0.992 | KXNHLGAME-26NOV05PHINYR-NYR -0.078 |
| BOS @ PIT | 0.464 | 0.518 | 0.170 | 0.220 | 6.47 | 6.69 | 1.033/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.068 |
| DAL @ CBJ | 0.458 | 0.523 | 0.177 | 0.214 | 5.98 | 6.12 | 0.990/0.987 | KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ4 +0.069 |
| VAN @ WPG | 0.606 | 0.545 | 0.169 | 0.220 | 6.50 | 6.32 | 1.002/1.021 | KXNHLSPREAD-26NOV05VANWPG-WPG2 -0.067 |
| ANA @ EDM | 0.622 | 0.577 | 0.161 | 0.203 | 7.11 | 7.18 | 1.010/0.986 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4 +0.048 |
| NSH @ COL | 0.652 | 0.661 | 0.160 | 0.204 | 6.61 | 6.65 | 0.977/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.021 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 13 recommended · full analysis in card.md / packet.json `thesis_card`

- Tampa Bay over 4.5 goals scored NO @ 58c · p 0.6603 (adj 0.6152) · $9.58 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 41c · p 0.5097 (adj 0.4416) · $2.87 · thesis GAME:TIGHT
- St. Louis over 4.5 goals scored YES @ 13c · p 0.1801 (adj 0.1501) · $2.38 · thesis STL:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 60c · p 0.6671 (adj 0.631) · $7.21 · thesis STL:WINS
- New York I wins by over 1.5 goals YES @ 20c · p 0.2763 (adj 0.2356) · $1.86 · thesis NYI:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 62c · p 0.7144 (adj 0.6647) · $9.18 · thesis NYI:WINS
- New York I over 1.5 goals scored YES @ 75c · p 0.8201 (adj 0.7801) · $3.36 · thesis NYI:WINS
- Columbus over 5.5 goals scored YES @ 6c · p 0.0946 (adj 0.0748) · $2.07 · thesis GAME:HIGH_EVENT
- Columbus wins by over 1.5 goals YES @ 25c · p 0.3064 (adj 0.2732) · $1.33 · thesis CBJ:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 17c · p 0.2479 (adj 0.2065) · $5.81 · thesis VAN:WINS_BY_2PLUS
- Winnipeg wins by over 2.5 goals NO @ 71c · p 0.7907 (adj 0.7453) · $14.61 · thesis VAN:WINS
- Anaheim over 4.5 goals scored YES @ 20c · p 0.2629 (adj 0.224) · $3.0 · thesis ANA:OFFENSE_4PLUS
- Anaheim over 2.5 goals scored YES @ 59c · p 0.6547 (adj 0.6173) · $3.55 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.98, exp saves 25.04 (sd 6.8), pull risk 0.065
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.81, exp saves 22.22 (sd 6.29), pull risk 0.07

**VGK @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROJECTED) exp shots 26.45, exp saves 22.68 (sd 6.46), pull risk 0.07
- VGK net: Adin Hill (PROJECTED) exp shots 27.41, exp saves 23.75 (sd 6.5), pull risk 0.058

**CHI @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.1, exp saves 20.67 (sd 5.74), pull risk 0.04
- CHI net: Spencer Knight (PROJECTED) exp shots 30.41, exp saves 25.36 (sd 7.11), pull risk 0.099

**STL @ NJD** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 24.87, exp saves 21.56 (sd 6.06), pull risk 0.055
- STL net: Joel Hofer (PROJECTED) exp shots 30.21, exp saves 25.98 (sd 7.14), pull risk 0.067

**CAR @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 29.43, exp saves 25.31 (sd 6.88), pull risk 0.068
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.49, exp saves 21.13 (sd 6.03), pull risk 0.061

**PHI @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 25.8, exp saves 22.54 (sd 6.17), pull risk 0.05
- PHI net: Joseph Woll (PROJECTED) exp shots 26.19, exp saves 22.64 (sd 6.26), pull risk 0.059

**BOS @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.87, exp saves 22.2 (sd 6.33), pull risk 0.071
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.09 (sd 6.88), pull risk 0.071

**DAL @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROJECTED) exp shots 25.44, exp saves 22.13 (sd 6.13), pull risk 0.055
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.62, exp saves 22.08 (sd 6.26), pull risk 0.065

**VAN @ WPG** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 24.76, exp saves 21.5 (sd 6.08), pull risk 0.059
- VAN net: Kevin Lankinen (PROJECTED) exp shots 29.31, exp saves 25.06 (sd 6.86), pull risk 0.07

**ANA @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.9, exp saves 24.11 (sd 6.75), pull risk 0.078
- ANA net: Laurent Brossoit (PROJECTED) exp shots 27.83, exp saves 23.59 (sd 6.82), pull risk 0.097

**NSH @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.73, exp saves 22.66 (sd 6.18), pull risk 0.047
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.24 (sd 7.61), pull risk 0.096

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
