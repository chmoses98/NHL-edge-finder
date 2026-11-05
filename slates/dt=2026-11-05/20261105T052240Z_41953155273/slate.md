# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T05:22:40Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 2607 · contracts joined: 561 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 286, 'OK': 119, 'NO_EDGE': 156}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'game_early_goal': 11, 'game_winner': 22, 'game_overtime': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-12h | 0.522 | 0.478 | 0.175 | 6.31 | 3.22 | 3.09 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-12h | 0.533 | 0.467 | 0.178 | 6.20 | 3.19 | 3.01 | 51 (25/26) | PROJECTED/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-12h | 0.688 | 0.312 | 0.162 | 6.03 | 3.62 | 2.40 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-12h | 0.560 | 0.440 | 0.182 | 5.95 | 3.17 | 2.78 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-12h | 0.421 | 0.579 | 0.179 | 5.83 | 2.67 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-12h | 0.620 | 0.380 | 0.175 | 6.01 | 3.36 | 2.64 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-12h | 0.462 | 0.538 | 0.168 | 6.47 | 3.10 | 3.37 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-12h | 0.458 | 0.542 | 0.177 | 5.98 | 2.85 | 3.13 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-12h | 0.607 | 0.393 | 0.168 | 6.50 | 3.59 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-12h | 0.621 | 0.379 | 0.158 | 7.11 | 3.96 | 3.15 | 51 (25/26) | PROJECTED/PROJECTED |
| NSH @ COL | 2026-11-06T02:30:00Z | T-12h | 0.653 | 0.347 | 0.158 | 6.61 | 3.80 | 2.81 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.315 | 0.445 | 0.418 | 45 | 56 | no | +0.107 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.459 | 0.585 | 0.560 | 59 | 42 | no | +0.104 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.298 | 0.420 | 0.394 | 43 | 59 | no | +0.095 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.503 | 0.630 | 0.605 | 65 | 39 | no | +0.091 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.533 | 0.435 | 0.454 | 44 | 57 | yes | +0.076 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.467 | 0.565 | 0.546 | 57 | 44 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.714 | 0.815 | 0.797 | 83 | 20 | no | +0.075 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.312 | 0.225 | 0.241 | 23 | 78 | yes | +0.070 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.688 | 0.775 | 0.759 | 78 | 23 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.151 | 0.235 | 0.216 | 24 | 77 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.260 | 0.345 | 0.327 | 35 | 66 | no | +0.065 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.151 | 0.230 | 0.212 | 24 | 78 | no | +0.057 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.308 | 0.230 | 0.244 | 24 | 78 | yes | +0.055 | OK |
| KXNHLGAME-26NOV05STLNJ-NJ | game_winner | 0.560 | 0.635 | 0.620 | 64 | 37 | no | +0.053 | OK |
| KXNHLGAME-26NOV05STLNJ-STL | game_winner | 0.440 | 0.365 | 0.380 | 37 | 64 | yes | +0.053 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.534 | 0.610 | 0.595 | 62 | 40 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.420 | 0.485 | 0.472 | 49 | 52 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.629 | 0.550 | 0.566 | 57 | 47 | yes | +0.042 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ2 | game_spread | 0.332 | 0.395 | 0.382 | 40 | 61 | no | +0.041 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ3 | game_spread | 0.205 | 0.270 | 0.256 | 28 | 74 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV05CHITB-8 | game_total | 0.236 | 0.300 | 0.286 | 31 | 71 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.405 | 0.330 | 0.345 | 35 | 69 | yes | +0.039 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.386 | 0.445 | 0.433 | 45 | 56 | no | +0.037 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.607 | 0.665 | 0.654 | 67 | 34 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET5 | team_total | 0.226 | 0.160 | 0.172 | 18 | 86 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.881 | 0.930 | 0.922 | 94 | 8 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.252 | 0.305 | 0.294 | 31 | 70 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.623 | 0.680 | 0.669 | 69 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.382 | 0.445 | 0.432 | 46 | 57 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.402 | 0.470 | 0.456 | 49 | 55 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET3 | game_spread | 0.187 | 0.145 | 0.153 | 15 | 86 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.028 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.393 | 0.345 | 0.354 | 35 | 66 | yes | +0.027 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL2 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.163 | 0.210 | 0.200 | 22 | 80 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET6 | team_total | 0.101 | 0.060 | 0.067 | 7 | 95 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.753 | 0.795 | 0.787 | 80 | 21 | no | +0.026 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.579 | 0.625 | 0.616 | 63 | 38 | no | +0.025 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.421 | 0.375 | 0.384 | 38 | 63 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN6 | team_total | 0.078 | 0.045 | 0.050 | 5 | 96 | yes | +0.025 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.522 | 0.475 | 0.484 | 48 | 53 | yes | +0.024 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.478 | 0.525 | 0.516 | 53 | 48 | no | +0.024 | OK |
| KXNHLSPREAD-26NOV05CHITB-CHI2 | game_spread | 0.141 | 0.100 | 0.107 | 11 | 91 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.213 | 0.260 | 0.250 | 27 | 75 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.581 | 0.645 | 0.632 | 67 | 38 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV05CARNYI-5 | game_total | 0.725 | 0.765 | 0.757 | 77 | 24 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ2 | team_total | 0.818 | 0.855 | 0.848 | 86 | 15 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA5 | team_total | 0.205 | 0.255 | 0.244 | 27 | 76 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.273 | 0.315 | 0.306 | 32 | 69 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET2 | team_total | 0.824 | 0.775 | 0.785 | 79 | 24 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.215 | 0.260 | 0.250 | 27 | 75 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA3 | team_total | 0.602 | 0.655 | 0.645 | 67 | 36 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA2 | team_total | 0.810 | 0.850 | 0.843 | 86 | 16 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.216 | 0.265 | 0.255 | 28 | 75 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV05CHITB-4 | game_total | 0.842 | 0.885 | 0.877 | 90 | 13 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3 | team_total | 0.556 | 0.510 | 0.519 | 52 | 50 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.104 | 0.135 | 0.128 | 14 | 87 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4 | team_total | 0.343 | 0.295 | 0.304 | 31 | 72 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV05STLNJ-6 | game_total | 0.515 | 0.555 | 0.547 | 56 | 45 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-CHI5 | team_total | 0.102 | 0.075 | 0.080 | 8 | 93 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV05CARNYI-7 | game_total | 0.387 | 0.425 | 0.417 | 43 | 58 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV05CHITB-9 | game_total | 0.163 | 0.200 | 0.192 | 21 | 81 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.348 | 0.385 | 0.377 | 39 | 62 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.369 | 0.425 | 0.414 | 45 | 60 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA6 | team_total | 0.090 | 0.120 | 0.113 | 13 | 89 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.621 | 0.665 | 0.656 | 68 | 35 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV05CHITB-10 | game_total | 0.071 | 0.100 | 0.094 | 11 | 91 | no | +0.013 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.620 | 0.585 | 0.592 | 59 | 42 | yes | +0.013 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.380 | 0.415 | 0.408 | 42 | 59 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ6 | team_total | 0.100 | 0.125 | 0.120 | 13 | 88 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV05CARNYI-6 | game_total | 0.500 | 0.535 | 0.528 | 54 | 47 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.400 | 0.450 | 0.440 | 47 | 57 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.327 | 0.295 | 0.301 | 30 | 71 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-9 | game_total | 0.295 | 0.265 | 0.271 | 27 | 74 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV05CARNYI-4 | game_total | 0.820 | 0.850 | 0.844 | 86 | 16 | no | +0.011 | OK |
| KXNHLGAME-26NOV05BOSPIT-BOS | game_winner | 0.538 | 0.505 | 0.512 | 51 | 50 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV05CARNYI-9 | game_total | 0.141 | 0.165 | 0.160 | 17 | 84 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.150 | 0.180 | 0.174 | 19 | 83 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.256 | 0.285 | 0.279 | 29 | 72 | no | +0.010 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.522 | 0.507 | 0.175 | 0.214 | 6.31 | 6.61 | 0.976/0.993 | KXNHLTOTAL-26NOV05UTAMTL-7 +0.056 |
| VGK @ DET | 0.533 | 0.453 | 0.178 | 0.222 | 6.20 | 6.29 | 1.015/1.004 | KXNHLGAME-26NOV05VGKDET-DET -0.080 |
| CHI @ TBL | 0.688 | 0.686 | 0.162 | 0.196 | 6.03 | 6.31 | 0.958/1.004 | KXNHLTOTAL-26NOV05CHITB-7 +0.049 |
| STL @ NJD | 0.560 | 0.559 | 0.182 | 0.216 | 5.95 | 6.20 | 0.960/0.993 | KXNHLTOTAL-26NOV05STLNJ-7 +0.047 |
| CAR @ NYI | 0.421 | 0.485 | 0.179 | 0.224 | 5.83 | 6.38 | 0.957/0.997 | KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 +0.107 |
| PHI @ NYR | 0.620 | 0.542 | 0.175 | 0.219 | 6.01 | 5.98 | 0.987/0.992 | KXNHLGAME-26NOV05PHINYR-NYR -0.078 |
| BOS @ PIT | 0.462 | 0.521 | 0.168 | 0.216 | 6.47 | 6.70 | 1.033/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.073 |
| DAL @ CBJ | 0.458 | 0.525 | 0.177 | 0.223 | 5.98 | 6.14 | 0.990/0.987 | KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3 +0.070 |
| VAN @ WPG | 0.607 | 0.543 | 0.168 | 0.217 | 6.50 | 6.32 | 1.002/1.021 | KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4 -0.065 |
| ANA @ EDM | 0.621 | 0.573 | 0.158 | 0.203 | 7.11 | 7.19 | 1.010/0.986 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4 +0.049 |
| NSH @ COL | 0.653 | 0.661 | 0.158 | 0.198 | 6.61 | 6.65 | 0.977/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 13 recommended · full analysis in card.md / packet.json `thesis_card`

- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.5406 (adj 0.459) · $5.11 · thesis GAME:TIGHT
- Tampa Bay over 4.5 goals scored NO @ 59c · p 0.6726 (adj 0.6263) · $9.18 · thesis TBL:SUPPRESSED
- Chicago over 3.5 goals scored YES @ 21c · p 0.2683 (adj 0.2316) · $1.74 · thesis CHI:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 61c · p 0.6737 (adj 0.6393) · $6.72 · thesis STL:WINS
- St. Louis wins by over 1.5 goals YES @ 19c · p 0.2372 (adj 0.2111) · $2.01 · thesis STL:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 62c · p 0.7043 (adj 0.6597) · $11.79 · thesis NYI:WINS
- New York I wins by over 1.5 goals YES @ 21c · p 0.2745 (adj 0.2398) · $3.22 · thesis NYI:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 75c · p 0.8172 (adj 0.7786) · $2.47 · thesis NYI:WINS
- New York I over 1.5 goals scored YES @ 76c · p 0.822 (adj 0.7835) · $1.32 · thesis NYI:WINS
- Columbus wins by over 1.5 goals YES @ 25c · p 0.3018 (adj 0.2734) · $3.27 · thesis CBJ:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 17c · p 0.2472 (adj 0.2061) · $4.47 · thesis VAN:WINS_BY_2PLUS
- Winnipeg wins by over 2.5 goals NO @ 70c · p 0.7928 (adj 0.7439) · $20.0 · thesis VAN:WINS
- Vancouver over 5.5 goals scored YES @ 5c · p 0.0847 (adj 0.0648) · $1.11 · thesis GAME:HIGH_EVENT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.98, exp saves 25.0 (sd 6.83), pull risk 0.07
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.81, exp saves 22.22 (sd 6.36), pull risk 0.071

**VGK @ DET** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DET net: Daniil Tarasov (PROJECTED) exp shots 26.45, exp saves 22.7 (sd 6.34), pull risk 0.071
- VGK net: Adin Hill (PROJECTED) exp shots 27.41, exp saves 23.73 (sd 6.55), pull risk 0.058

**CHI @ TBL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.1, exp saves 20.61 (sd 5.75), pull risk 0.04
- CHI net: Spencer Knight (PROJECTED) exp shots 30.41, exp saves 25.44 (sd 7.28), pull risk 0.096

**STL @ NJD** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 24.87, exp saves 21.57 (sd 6.03), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 30.21, exp saves 25.94 (sd 7.07), pull risk 0.07

**CAR @ NYI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYI net: Ilya Sorokin (PROJECTED) exp shots 29.43, exp saves 25.34 (sd 6.81), pull risk 0.064
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.49, exp saves 21.14 (sd 6.08), pull risk 0.063

**PHI @ NYR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYR net: Dylan Garand (PROJECTED) exp shots 25.8, exp saves 22.54 (sd 6.2), pull risk 0.048
- PHI net: Joseph Woll (PROJECTED) exp shots 26.19, exp saves 22.62 (sd 6.28), pull risk 0.063

**BOS @ PIT** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.87, exp saves 22.25 (sd 6.41), pull risk 0.069
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.02 (sd 6.88), pull risk 0.077

**DAL @ CBJ** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CBJ net: Cam Talbot (PROJECTED) exp shots 25.44, exp saves 22.1 (sd 6.15), pull risk 0.055
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.62, exp saves 22.09 (sd 6.28), pull risk 0.068

**VAN @ WPG** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- WPG net: Stuart Skinner (PROJECTED) exp shots 24.76, exp saves 21.45 (sd 6.08), pull risk 0.064
- VAN net: Kevin Lankinen (PROJECTED) exp shots 29.31, exp saves 25.02 (sd 6.78), pull risk 0.07

**ANA @ EDM** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.9, exp saves 24.1 (sd 6.78), pull risk 0.078
- ANA net: Laurent Brossoit (PROJECTED) exp shots 27.83, exp saves 23.54 (sd 6.94), pull risk 0.1

**NSH @ COL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.73, exp saves 22.69 (sd 6.15), pull risk 0.047
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.34 (sd 7.59), pull risk 0.093

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
