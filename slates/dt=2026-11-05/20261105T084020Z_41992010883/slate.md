# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T08:40:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 2213 · contracts joined: 561 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 286, 'OK': 105, 'NO_EDGE': 170}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'game_early_goal': 11, 'game_winner': 22, 'game_overtime': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-12h | 0.523 | 0.477 | 0.171 | 6.30 | 3.22 | 3.08 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-12h | 0.533 | 0.467 | 0.178 | 6.20 | 3.19 | 3.01 | 51 (25/26) | PROJECTED/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-12h | 0.693 | 0.307 | 0.157 | 6.04 | 3.64 | 2.40 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-12h | 0.560 | 0.440 | 0.182 | 5.95 | 3.17 | 2.78 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-12h | 0.421 | 0.579 | 0.179 | 5.83 | 2.67 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-12h | 0.617 | 0.384 | 0.169 | 6.00 | 3.36 | 2.64 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-12h | 0.464 | 0.536 | 0.170 | 6.47 | 3.10 | 3.37 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-12h | 0.454 | 0.546 | 0.182 | 5.99 | 2.85 | 3.14 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-12h | 0.609 | 0.391 | 0.164 | 6.49 | 3.59 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-12h | 0.622 | 0.378 | 0.161 | 7.11 | 3.96 | 3.15 | 51 (25/26) | PROJECTED/PROJECTED |
| NSH @ COL | 2026-11-06T02:30:00Z | T-12h | 0.651 | 0.349 | 0.160 | 6.62 | 3.80 | 2.81 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.315 | 0.445 | 0.418 | 45 | 56 | no | +0.108 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.467 | 0.585 | 0.562 | 59 | 42 | no | +0.096 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.509 | 0.640 | 0.615 | 66 | 38 | no | +0.095 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.301 | 0.425 | 0.399 | 44 | 59 | no | +0.092 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.467 | 0.575 | 0.554 | 58 | 43 | no | +0.086 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.533 | 0.435 | 0.455 | 44 | 57 | yes | +0.076 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.307 | 0.215 | 0.232 | 22 | 79 | yes | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.151 | 0.245 | 0.224 | 26 | 77 | no | +0.066 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.693 | 0.775 | 0.760 | 78 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.717 | 0.810 | 0.793 | 83 | 21 | no | +0.062 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.308 | 0.230 | 0.244 | 24 | 78 | yes | +0.055 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.260 | 0.340 | 0.323 | 35 | 67 | no | +0.055 | OK |
| KXNHLGAME-26NOV05STLNJ-NJ | game_winner | 0.560 | 0.635 | 0.620 | 64 | 37 | no | +0.053 | OK |
| KXNHLGAME-26NOV05STLNJ-STL | game_winner | 0.440 | 0.365 | 0.380 | 37 | 64 | yes | +0.053 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.151 | 0.225 | 0.208 | 24 | 79 | no | +0.047 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.537 | 0.615 | 0.600 | 63 | 40 | no | +0.046 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.418 | 0.485 | 0.471 | 49 | 52 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ3 | game_spread | 0.205 | 0.270 | 0.256 | 28 | 74 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.405 | 0.330 | 0.345 | 35 | 69 | yes | +0.039 | OK |
| KXNHLTOTAL-26NOV05CHITB-8 | game_total | 0.237 | 0.300 | 0.287 | 31 | 71 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.753 | 0.805 | 0.795 | 81 | 20 | no | +0.036 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.609 | 0.665 | 0.654 | 67 | 34 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.252 | 0.310 | 0.298 | 32 | 70 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.390 | 0.445 | 0.434 | 45 | 56 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.623 | 0.685 | 0.673 | 70 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.629 | 0.555 | 0.570 | 58 | 47 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ2 | game_spread | 0.332 | 0.390 | 0.378 | 40 | 62 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.402 | 0.470 | 0.456 | 49 | 55 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.383 | 0.450 | 0.436 | 47 | 57 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.207 | 0.165 | 0.173 | 17 | 84 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV05CHITB-9 | game_total | 0.162 | 0.205 | 0.196 | 21 | 80 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL2 | game_spread | 0.227 | 0.180 | 0.189 | 19 | 83 | yes | +0.026 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.523 | 0.475 | 0.485 | 48 | 53 | yes | +0.026 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.477 | 0.525 | 0.515 | 53 | 48 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4 | team_total | 0.340 | 0.290 | 0.300 | 30 | 72 | yes | +0.026 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.391 | 0.345 | 0.354 | 35 | 66 | yes | +0.025 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.579 | 0.625 | 0.616 | 63 | 38 | no | +0.025 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.421 | 0.375 | 0.384 | 38 | 63 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA5 | team_total | 0.202 | 0.255 | 0.244 | 27 | 76 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET5 | team_total | 0.225 | 0.165 | 0.176 | 19 | 86 | yes | +0.025 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.271 | 0.315 | 0.306 | 32 | 69 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA3 | team_total | 0.600 | 0.660 | 0.648 | 68 | 36 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.881 | 0.925 | 0.918 | 94 | 9 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.581 | 0.640 | 0.628 | 66 | 38 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ2 | team_total | 0.818 | 0.855 | 0.848 | 86 | 15 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.400 | 0.460 | 0.448 | 48 | 56 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET2 | team_total | 0.824 | 0.770 | 0.782 | 79 | 25 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.215 | 0.260 | 0.250 | 27 | 75 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV05CHITB-CHI2 | game_spread | 0.139 | 0.100 | 0.107 | 11 | 91 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.305 | 0.265 | 0.273 | 27 | 74 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.216 | 0.270 | 0.259 | 29 | 75 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV05CHITB-10 | game_total | 0.075 | 0.110 | 0.102 | 12 | 90 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV05CHITB-4 | game_total | 0.843 | 0.885 | 0.878 | 90 | 13 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET3 | game_spread | 0.187 | 0.150 | 0.157 | 16 | 86 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.162 | 0.200 | 0.192 | 21 | 81 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV05CARNYI-7 | game_total | 0.387 | 0.425 | 0.417 | 43 | 58 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.348 | 0.385 | 0.377 | 39 | 62 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET6 | team_total | 0.101 | 0.065 | 0.071 | 8 | 95 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV05NSHCOL-9 | game_total | 0.236 | 0.200 | 0.207 | 21 | 81 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.213 | 0.255 | 0.246 | 27 | 76 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-9 | game_total | 0.298 | 0.265 | 0.271 | 27 | 74 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.369 | 0.425 | 0.414 | 45 | 60 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.328 | 0.295 | 0.301 | 30 | 71 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.621 | 0.665 | 0.656 | 68 | 35 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA2 | team_total | 0.807 | 0.845 | 0.838 | 86 | 17 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV05CARNYI-6 | game_total | 0.500 | 0.540 | 0.532 | 55 | 47 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV05CARNYI-5 | game_total | 0.725 | 0.760 | 0.753 | 77 | 25 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN3 | game_spread | 0.118 | 0.095 | 0.099 | 10 | 91 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV05CARNYI-4 | game_total | 0.820 | 0.850 | 0.844 | 86 | 16 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV05NSHCOL-8 | game_total | 0.325 | 0.295 | 0.301 | 30 | 71 | yes | +0.010 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.617 | 0.585 | 0.591 | 59 | 42 | yes | +0.010 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.384 | 0.415 | 0.409 | 42 | 59 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.151 | 0.180 | 0.174 | 19 | 83 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV05UTAMTL-7 | game_total | 0.464 | 0.495 | 0.489 | 50 | 51 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV05NSHCOL-7 | game_total | 0.516 | 0.485 | 0.491 | 49 | 52 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV05CARNYI-8 | game_total | 0.209 | 0.240 | 0.234 | 25 | 77 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR6 | team_total | 0.095 | 0.120 | 0.115 | 13 | 89 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV05STLNJ-6 | game_total | 0.515 | 0.550 | 0.543 | 56 | 46 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.823 | 0.855 | 0.849 | 87 | 16 | no | +0.007 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.523 | 0.507 | 0.171 | 0.214 | 6.30 | 6.61 | 0.976/0.993 | KXNHLTOTAL-26NOV05UTAMTL-7 +0.057 |
| VGK @ DET | 0.533 | 0.453 | 0.178 | 0.222 | 6.20 | 6.29 | 1.015/1.004 | KXNHLGAME-26NOV05VGKDET-DET -0.080 |
| CHI @ TBL | 0.693 | 0.686 | 0.157 | 0.196 | 6.04 | 6.31 | 0.958/1.004 | KXNHLTOTAL-26NOV05CHITB-7 +0.051 |
| STL @ NJD | 0.560 | 0.559 | 0.182 | 0.216 | 5.95 | 6.20 | 0.960/0.993 | KXNHLTOTAL-26NOV05STLNJ-7 +0.047 |
| CAR @ NYI | 0.421 | 0.485 | 0.179 | 0.224 | 5.83 | 6.38 | 0.957/0.997 | KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 +0.107 |
| PHI @ NYR | 0.617 | 0.542 | 0.169 | 0.219 | 6.00 | 5.98 | 0.987/0.992 | KXNHLGAME-26NOV05PHINYR-NYR -0.075 |
| BOS @ PIT | 0.464 | 0.521 | 0.170 | 0.216 | 6.47 | 6.70 | 1.033/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.071 |
| DAL @ CBJ | 0.454 | 0.525 | 0.182 | 0.223 | 5.99 | 6.14 | 0.990/0.987 | KXNHLGAME-26NOV05DALCBJ-DAL -0.072 |
| VAN @ WPG | 0.609 | 0.543 | 0.164 | 0.217 | 6.49 | 6.32 | 1.002/1.021 | KXNHLGAME-26NOV05VANWPG-VAN +0.066 |
| ANA @ EDM | 0.622 | 0.573 | 0.161 | 0.203 | 7.11 | 7.19 | 1.010/0.986 | KXNHLGAME-26NOV05ANAEDM-ANA +0.049 |
| NSH @ COL | 0.651 | 0.661 | 0.160 | 0.198 | 6.62 | 6.65 | 0.977/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.024 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.5406 (adj 0.459) · $5.91 · thesis GAME:TIGHT
- Tampa Bay wins by over 2.5 goals NO @ 56c · p 0.674 (adj 0.5967) · $3.27 · thesis GAME:TIGHT
- Tampa Bay over 4.5 goals scored NO @ 59c · p 0.6726 (adj 0.6238) · $3.08 · thesis TBL:SUPPRESSED
- Tampa Bay over 5.5 goals scored NO @ 77c · p 0.8338 (adj 0.7944) · $4.77 · thesis CHI:WINS
- Carolina wins by over 1.5 goals NO @ 62c · p 0.7043 (adj 0.6597) · $12.07 · thesis NYI:WINS
- New York I over 4.5 goals scored YES @ 15c · p 0.2149 (adj 0.1749) · $2.41 · thesis NYI:OFFENSE_4PLUS
- New York I wins by over 1.5 goals YES @ 21c · p 0.2745 (adj 0.2373) · $1.02 · thesis NYI:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 75c · p 0.8172 (adj 0.7786) · $2.43 · thesis NYI:WINS
- Vancouver wins by over 1.5 goals YES @ 17c · p 0.2472 (adj 0.2061) · $5.86 · thesis VAN:WINS_BY_2PLUS
- Winnipeg wins by over 1.5 goals NO @ 56c · p 0.678 (adj 0.598) · $6.62 · thesis VAN:WINS
- Winnipeg over 4.5 goals scored NO @ 69c · p 0.7599 (adj 0.7175) · $1.03 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.98, exp saves 25.0 (sd 6.83), pull risk 0.07
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.81, exp saves 22.22 (sd 6.36), pull risk 0.071

**VGK @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROJECTED) exp shots 26.45, exp saves 22.7 (sd 6.34), pull risk 0.071
- VGK net: Adin Hill (PROJECTED) exp shots 27.41, exp saves 23.73 (sd 6.55), pull risk 0.058

**CHI @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.1, exp saves 20.61 (sd 5.75), pull risk 0.04
- CHI net: Spencer Knight (PROJECTED) exp shots 30.41, exp saves 25.44 (sd 7.28), pull risk 0.096

**STL @ NJD** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 24.87, exp saves 21.57 (sd 6.03), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 30.21, exp saves 25.94 (sd 7.07), pull risk 0.07

**CAR @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 29.43, exp saves 25.34 (sd 6.81), pull risk 0.064
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.49, exp saves 21.14 (sd 6.08), pull risk 0.063

**PHI @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 25.8, exp saves 22.54 (sd 6.2), pull risk 0.048
- PHI net: Joseph Woll (PROJECTED) exp shots 26.19, exp saves 22.62 (sd 6.28), pull risk 0.063

**BOS @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.87, exp saves 22.25 (sd 6.41), pull risk 0.069
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.02 (sd 6.88), pull risk 0.077

**DAL @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROJECTED) exp shots 25.44, exp saves 22.1 (sd 6.15), pull risk 0.055
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.62, exp saves 22.09 (sd 6.28), pull risk 0.068

**VAN @ WPG** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 24.76, exp saves 21.45 (sd 6.07), pull risk 0.064
- VAN net: Kevin Lankinen (PROJECTED) exp shots 29.31, exp saves 25.02 (sd 6.78), pull risk 0.07

**ANA @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.9, exp saves 24.1 (sd 6.78), pull risk 0.078
- ANA net: Laurent Brossoit (PROJECTED) exp shots 27.83, exp saves 23.54 (sd 6.94), pull risk 0.1

**NSH @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.73, exp saves 22.69 (sd 6.15), pull risk 0.047
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.34 (sd 7.59), pull risk 0.093

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
