# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-28T01:48:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 3 · markets on board: 4712 · contracts joined: 765 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 690, 'OK': 34, 'NO_EDGE': 41}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 130, 'game_early_goal': 3, 'first_goal': 110, 'game_winner': 6, 'player_goals': 193, 'game_overtime': 3, 'player_points': 173, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ VGK | 2026-10-28T02:00:00Z | T-10m | 0.572 | 0.428 | 0.163 | 6.68 | 3.57 | 3.11 | 242 (25/217) | CONFIRMED/CONFIRMED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-10m | 0.653 | 0.347 | 0.160 | 6.92 | 3.97 | 2.95 | 251 (25/226) | CONFIRMED/CONFIRMED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-30m | 0.463 | 0.537 | 0.171 | 6.74 | 3.25 | 3.50 | 272 (25/247) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT27BUFSJ-SJ | game_winner | 0.463 | 0.415 | 0.425 | 42 | 59 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.203 | 0.250 | 0.240 | 26 | 76 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-9 | game_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.322 | 0.365 | 0.356 | 37 | 64 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT27VANANA-9 | game_total | 0.271 | 0.235 | 0.242 | 24 | 77 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT27VANANA-10 | game_total | 0.144 | 0.115 | 0.120 | 12 | 89 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT3 | team_total | 0.603 | 0.560 | 0.569 | 57 | 45 | yes | +0.016 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-8 | game_total | 0.329 | 0.295 | 0.302 | 30 | 71 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3 | team_total | 0.682 | 0.720 | 0.713 | 73 | 29 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT6 | team_total | 0.098 | 0.075 | 0.079 | 8 | 93 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-5 | game_total | 0.830 | 0.855 | 0.850 | 86 | 15 | no | +0.011 | OK |
| KXNHLGAME-26OCT27OTTVGK-OTT | game_winner | 0.428 | 0.395 | 0.402 | 40 | 61 | yes | +0.011 | OK |
| KXNHLGAME-26OCT27OTTVGK-VGK | game_winner | 0.572 | 0.605 | 0.598 | 61 | 40 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT5 | team_total | 0.212 | 0.185 | 0.190 | 19 | 82 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT27VANANA-8 | game_total | 0.366 | 0.335 | 0.341 | 34 | 67 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN6 | team_total | 0.085 | 0.060 | 0.064 | 7 | 95 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-SJ2 | game_spread | 0.262 | 0.235 | 0.240 | 24 | 77 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-6 | game_total | 0.635 | 0.605 | 0.611 | 61 | 40 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT2 | team_total | 0.810 | 0.785 | 0.790 | 79 | 22 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN5 | team_total | 0.188 | 0.160 | 0.165 | 17 | 85 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT27VANANA-7 | game_total | 0.565 | 0.535 | 0.541 | 54 | 47 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-4 | game_total | 0.897 | 0.915 | 0.912 | 92 | 9 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT27VANANA-6 | game_total | 0.673 | 0.645 | 0.651 | 65 | 36 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-10 | game_total | 0.124 | 0.100 | 0.104 | 11 | 91 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF5 | team_total | 0.279 | 0.315 | 0.308 | 33 | 70 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-7 | game_total | 0.524 | 0.495 | 0.501 | 50 | 51 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT27OTTVGK-VGK3 | game_spread | 0.231 | 0.255 | 0.250 | 26 | 75 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT27VANANA-4 | game_total | 0.909 | 0.925 | 0.922 | 93 | 8 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ6 | team_total | 0.112 | 0.095 | 0.098 | 10 | 91 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT27OTTVGK-OTT2 | game_spread | 0.236 | 0.215 | 0.219 | 22 | 79 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2 | team_total | 0.861 | 0.880 | 0.876 | 89 | 13 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT27VANANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT27VANANA-ANA3 | game_spread | 0.305 | 0.325 | 0.321 | 33 | 68 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-6 | game_total | 0.645 | 0.665 | 0.661 | 67 | 34 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA2 | team_total | 0.906 | 0.920 | 0.917 | 93 | 9 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT27VANANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT4 | team_total | 0.384 | 0.365 | 0.369 | 37 | 64 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT27BUFSJ-SJ3 | game_spread | 0.156 | 0.145 | 0.147 | 15 | 86 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT27VANANA-VAN3 | game_spread | 0.102 | 0.095 | 0.096 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT27OTTVGK-VGK2 | game_spread | 0.358 | 0.375 | 0.372 | 38 | 63 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT27VANANA-5 | game_total | 0.845 | 0.855 | 0.853 | 86 | 15 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-5 | game_total | 0.824 | 0.835 | 0.833 | 84 | 17 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-7 | game_total | 0.537 | 0.555 | 0.551 | 56 | 45 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK2 | team_total | 0.868 | 0.885 | 0.882 | 90 | 13 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN3 | team_total | 0.562 | 0.540 | 0.544 | 55 | 47 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-3 | game_total | 0.974 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ4 | team_total | 0.420 | 0.405 | 0.408 | 41 | 60 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ5 | team_total | 0.234 | 0.220 | 0.223 | 23 | 79 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT27VANANA-ANA2 | game_spread | 0.441 | 0.455 | 0.452 | 46 | 55 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF6 | team_total | 0.140 | 0.150 | 0.148 | 16 | 86 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT27VANANA-VAN2 | game_spread | 0.182 | 0.170 | 0.172 | 18 | 84 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT27VANANA-ANA | game_winner | 0.653 | 0.665 | 0.663 | 67 | 34 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT27VANANA-VAN | game_winner | 0.347 | 0.335 | 0.337 | 34 | 67 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT27OTTVGK-4 | game_total | 0.892 | 0.895 | 0.894 | 90 | 11 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-10 | game_total | 0.129 | 0.125 | 0.126 | 13 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-3 | game_total | 0.977 | 0.980 | 0.979 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK5 | team_total | 0.294 | 0.285 | 0.287 | 29 | 72 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN2 | team_total | 0.781 | 0.775 | 0.776 | 78 | 23 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK6 | team_total | 0.147 | 0.140 | 0.141 | 15 | 87 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT27OTTVGK-OTT3 | game_spread | 0.136 | 0.135 | 0.135 | 14 | 87 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK4 | team_total | 0.494 | 0.485 | 0.487 | 49 | 52 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ3 | team_total | 0.633 | 0.620 | 0.623 | 63 | 39 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN4 | team_total | 0.352 | 0.345 | 0.346 | 35 | 66 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK3 | team_total | 0.698 | 0.695 | 0.696 | 70 | 31 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA6 | team_total | 0.203 | 0.195 | 0.197 | 21 | 82 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ2 | team_total | 0.828 | 0.830 | 0.830 | 84 | 18 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA3 | team_total | 0.766 | 0.770 | 0.769 | 78 | 24 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-9 | game_total | 0.248 | 0.250 | 0.250 | 26 | 76 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA4 | team_total | 0.576 | 0.575 | 0.575 | 58 | 43 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-8 | game_total | 0.341 | 0.340 | 0.340 | 35 | 67 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27VANANA-ANA5 | team_total | 0.371 | 0.370 | 0.370 | 38 | 64 |  | -0.025 | NO_EDGE |
| KXNHL1P-26OCT27OTTVGK-OTT | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT27OTTVGK-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT27OTTVGK-VGK | period_winner |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT27OTTVGK-OTT2 | period_spread |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT27OTTVGK-VGK2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ VGK | 0.572 | 0.581 | 0.163 | 0.213 | 6.68 | 6.30 | 1.004/1.040 | KXNHLTOTAL-26OCT27OTTVGK-6 -0.062 |
| VAN @ ANA | 0.653 | 0.602 | 0.160 | 0.204 | 6.92 | 6.80 | 1.016/1.034 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.051 |
| BUF @ SJS | 0.463 | 0.524 | 0.171 | 0.214 | 6.74 | 6.52 | 1.039/0.999 | KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 -0.069 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Mitch Marner: 1+ assists NO @ 46c · p 0.6106 (adj 0.5095) · $16.06 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0848 (adj 0.0774) · $3.35 · thesis VGK:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 58c · p 0.7115 (adj 0.6228) · $18.32 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1607 (adj 0.1518) · $4.2 · thesis OTT:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 17c · p 0.2618 (adj 0.2376) · $15.87 · thesis ANA:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2367 (adj 0.2238) · $6.93 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2116 (adj 0.2) · $5.66 · thesis VAN:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 13c · p 0.1652 (adj 0.1552) · $4.55 · thesis ANA:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1747 (adj 0.1623) · $6.53 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 61c · p 0.6756 (adj 0.658) · $20.0 · thesis BUF:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 22c · p 0.2695 (adj 0.2559) · $8.16 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 63c · p 0.7344 (adj 0.6633) · $15.18 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ VGK** · priced 185/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.26, exp saves 22.87 (sd 6.3), pull risk 0.054
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.79, exp saves 22.82 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Johansson: 28+ saves | 0.227 | 0.395 | 40/61 | +0.146 |  |
| Mitch Marner: 1+ assists | 0.389 | 0.545 | 55/46 | +0.133 | STANDARD |
| Jake Sanderson: 1+ points | 0.370 | 0.510 | 52/50 | +0.113 | STANDARD |
| Jake Sanderson: 1+ assists | 0.288 | 0.425 | 43/58 | +0.114 | STANDARD |
| Mitch Marner: 1+ points | 0.538 | 0.655 | 66/35 | +0.096 | STANDARD |
| Jack Eichel: 2+ points | 0.249 | 0.365 | 37/64 | +0.095 | STANDARD |

**VAN @ ANA** · priced 180/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 23.87, exp saves 20.87 (sd 6.01), pull risk 0.064
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 31.6, exp saves 26.65 (sd 7.6), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Washe: 1+ points | 0.427 | 0.295 | 30/71 | +0.112 | STANDARD |
| Tim Washe: 1+ assists | 0.312 | 0.205 | 21/80 | +0.091 | STANDARD |
| A.J. Greer: 1+ points | 0.429 | 0.330 | 34/68 | +0.074 | STANDARD |
| A.J. Greer: 1+ goals | 0.262 | 0.165 | 17/84 | +0.082 | STANDARD |
| Arshdeep Bains: 1+ points | 0.265 | 0.175 | 22/87 | +0.033 | STANDARD |
| Tom Willander: 1+ points | 0.324 | 0.245 | 26/77 | +0.051 | STANDARD |

**BUF @ SJS** · priced 218/221 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.51, exp saves 24.68 (sd 6.72), pull risk 0.063
- BUF net: Colten Ellis (PROBABLE) exp shots 27.09, exp saves 23.35 (sd 6.5), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.298 | 0.125 | 17/92 | +0.118 | STANDARD |
| Ivar Stenberg: 1+ points | 0.407 | 0.575 | 58/43 | +0.145 | STANDARD |
| Zack Ostapchuk: 1+ points | 0.236 | 0.090 | 16/98 | +0.067 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.447 | 0.580 | 59/43 | +0.106 | STANDARD |
| Barclay Goodrow: 1+ points | 0.230 | 0.100 | 18/98 | +0.039 | STANDARD |
| Peyton Krebs: 1+ assists | 0.221 | 0.105 | 19/98 | +0.020 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
