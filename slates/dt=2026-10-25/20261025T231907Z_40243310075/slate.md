# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T23:19:07Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 2 · markets on board: 2830 · contracts joined: 465 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 415, 'OK': 40, 'NO_EDGE': 10}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 69, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 125, 'game_overtime': 2, 'player_points': 93, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ NSH | 2026-10-26T00:00:00Z | T-30m | 0.373 | 0.627 | 0.168 | 6.00 | 2.60 | 3.40 | 237 (25/212) | PROBABLE/PROBABLE |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-90m | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.454 | 0.575 | 0.551 | 58 | 43 | no | +0.099 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.257 | 0.360 | 0.338 | 37 | 65 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.673 | 0.770 | 0.752 | 78 | 24 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.417 | 0.320 | 0.339 | 33 | 69 | yes | +0.072 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.552 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.448 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.627 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 16 | 85 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.533 | 0.615 | 0.599 | 62 | 39 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.750 | 0.830 | 0.816 | 84 | 18 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.256 | 0.335 | 0.318 | 34 | 67 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.416 | 0.495 | 0.479 | 50 | 51 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.223 | 0.300 | 0.283 | 31 | 71 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.837 | 0.895 | 0.885 | 90 | 11 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.231 | 0.295 | 0.281 | 30 | 71 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.119 | 0.175 | 0.162 | 18 | 83 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.855 | 0.905 | 0.896 | 91 | 10 | no | +0.039 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.038 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.351 | 0.295 | 0.306 | 30 | 71 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.770 | 0.781 | 78 | 24 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.095 | 0.102 | 10 | 91 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.210 | 0.219 | 22 | 80 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.065 | 0.072 | 8 | 95 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.115 | 0.121 | 12 | 89 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.735 | 0.728 | 74 | 27 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.867 | 0.895 | 0.890 | 90 | 11 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.071 | 0.100 | 0.093 | 11 | 91 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.625 | 0.631 | 63 | 38 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5 | team_total | 0.298 | 0.330 | 0.323 | 34 | 68 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH2 | team_total | 0.724 | 0.745 | 0.741 | 75 | 26 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT25MINVAN-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT25COLNSH-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-5 | game_total | 0.837 | 0.825 | 0.828 | 83 | 18 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH3 | team_total | 0.486 | 0.510 | 0.505 | 52 | 50 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-4 | game_total | 0.902 | 0.890 | 0.893 | 90 | 12 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH5 | team_total | 0.129 | 0.135 | 0.134 | 14 | 87 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH4 | team_total | 0.273 | 0.285 | 0.283 | 29 | 72 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-3 | game_total | 0.978 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT25COLNSH-NSH3 | game_spread | 0.095 | 0.095 | 0.095 | 10 | 91 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH6 | team_total | 0.051 | 0.050 | 0.050 | 6 | 96 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN6 | team_total | 0.152 | 0.155 | 0.154 | 17 | 86 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT25COLNSH-COL | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT25COLNSH-NSH | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT25COLNSH-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT25COLNSH-COL2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT25COLNSH-NSH2 | period_spread |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT25COLNSH-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT25COLNSH-2 | period_total |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT25COLNSH-3 | period_total |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT25COLNSH-COL | period_winner |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT25COLNSH-NSH | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT25COLNSH-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT25COLNSH-COL2 | period_spread |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT25COLNSH-NSH2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT25COLNSH-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT25COLNSH-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT25COLNSH-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT25COLNSH-COL | period_winner |  | 0.490 |  | 50 | 52 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT25COLNSH-NSH | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT25COLNSH-TIE | period_winner |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT25COLNSH-COL2 | period_spread |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT25COLNSH-NSH2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT25COLNSH-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT25COLNSH-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT25COLNSH-3 | period_total |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25COLNSH-COLALEHKONEN62-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25COLNSH-COLALEHKONEN62-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25COLNSH-COLBNELSON11-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25COLNSH-COLBNELSON11-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25COLNSH-COLCMAKAR8-1 | player_assists |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25COLNSH-COLCMAKAR8-2 | player_assists |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ NSH | 0.373 | 0.394 | 0.168 | 0.214 | 6.00 | 6.46 | 0.991/0.972 | KXNHLTOTAL-26OCT25COLNSH-7 +0.079 |
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Cale Makar: 1+ goals NO @ 77c · p 0.8146 (adj 0.8022) · $20.0 · thesis COL:SUPPRESSED
- Mavrik Bourque: 1+ assists NO @ 77c · p 0.8662 (adj 0.8004) · $20.0 · thesis NSH:SUPPRESSED
- Adam Edstrom: 1+ goals YES @ 11c · p 0.1346 (adj 0.1272) · $2.82 · thesis NSH:WINS_BY_2PLUS
- Colorado over 3.5 goals scored NO @ 43c · p 0.4964 (adj 0.4607) · $4.37 · thesis COL:SUPPRESSED
- Kirill Kaprizov: 2+ goals NO @ 85c · p 0.9148 (adj 0.8973) · $15.0 · thesis MIN:SUPPRESSED
- Matt Boldy: 1+ goals NO @ 58c · p 0.6593 (adj 0.6382) · $15.0 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 58c · p 0.7313 (adj 0.6297) · $15.39 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**COL @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROBABLE) exp shots 32.01, exp saves 27.18 (sd 7.46), pull risk 0.085
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.47, exp saves 23.19 (sd 6.3), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| Cale Makar: 2+ points | 0.193 | 0.295 | 31/72 | +0.073 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.134 | 0.235 | 24/77 | +0.084 | STANDARD |
| Scott Wedgewood: 22+ saves | 0.608 | 0.510 | 52/50 | +0.070 |  |
| Cale Makar: 1+ assists | 0.459 | 0.555 | 56/45 | +0.073 | STANDARD |
| Cale Makar: 1+ points | 0.562 | 0.655 | 66/35 | +0.072 | STANDARD |

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.268 | 0.420 | 44/60 | +0.115 | STANDARD |
| Liam Ohgren: 1+ assists | 0.264 | 0.115 | 21/98 | +0.042 | STANDARD |
| Matt Boldy: 2+ points | 0.241 | 0.380 | 39/63 | +0.113 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.628 | 0.765 | 78/25 | +0.109 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.650 | 66/36 | +0.105 | STANDARD |
| Quinn Hughes: 2+ points | 0.221 | 0.350 | 36/66 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
