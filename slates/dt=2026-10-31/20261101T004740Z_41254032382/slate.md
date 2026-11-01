# NHL slate 2026-10-31 — RESEARCH_ONLY

generated 2026-11-01T00:47:40Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 1 · markets on board: 2772 · contracts joined: 236 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 211, 'OK': 23, 'NO_EDGE': 2}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 34, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 66, 'game_overtime': 1, 'player_points': 47, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ COL | 2026-11-01T02:00:00Z | T-60m | 0.681 | 0.319 | 0.164 | 6.21 | 3.68 | 2.53 | 236 (25/211) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT31CGYCOL-COL3 | game_spread | 0.308 | 0.465 | 0.432 | 47 | 54 | no | +0.134 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-COL2 | game_spread | 0.454 | 0.605 | 0.575 | 61 | 40 | no | +0.129 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4 | team_total | 0.515 | 0.660 | 0.632 | 67 | 35 | no | +0.119 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL5 | team_total | 0.312 | 0.440 | 0.413 | 45 | 57 | no | +0.101 | OK |
| KXNHLGAME-26OCT31CGYCOL-CGY | game_winner | 0.319 | 0.215 | 0.234 | 22 | 79 | yes | +0.086 | OK |
| KXNHLGAME-26OCT31CGYCOL-COL | game_winner | 0.681 | 0.785 | 0.766 | 79 | 22 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3 | team_total | 0.729 | 0.830 | 0.813 | 84 | 18 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6 | team_total | 0.160 | 0.250 | 0.230 | 26 | 76 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-6 | game_total | 0.564 | 0.635 | 0.621 | 64 | 37 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4 | team_total | 0.260 | 0.195 | 0.207 | 20 | 81 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3 | team_total | 0.465 | 0.395 | 0.409 | 40 | 61 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-COL2 | team_total | 0.886 | 0.940 | 0.932 | 95 | 7 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2 | team_total | 0.703 | 0.645 | 0.657 | 65 | 36 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-5 | game_total | 0.773 | 0.830 | 0.820 | 84 | 18 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY2 | game_spread | 0.149 | 0.100 | 0.108 | 11 | 91 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-7 | game_total | 0.446 | 0.495 | 0.485 | 50 | 51 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-8 | game_total | 0.259 | 0.305 | 0.295 | 31 | 70 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-4 | game_total | 0.859 | 0.900 | 0.893 | 91 | 11 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5 | team_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT31CGYCOL-CGY3 | game_spread | 0.076 | 0.055 | 0.059 | 6 | 95 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-10 | game_total | 0.085 | 0.105 | 0.101 | 11 | 90 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-9 | game_total | 0.182 | 0.215 | 0.208 | 23 | 80 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY6 | team_total | 0.045 | 0.025 | 0.028 | 4 | 99 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT31CGYCOL-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT31CGYCOL-3 | game_total | 0.964 | 0.975 | 0.973 | 99 | 4 |  | -0.007 | NO_EDGE |
| KXNHL1P-26OCT31CGYCOL-CGY | period_winner |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT31CGYCOL-COL | period_winner |  | 0.490 |  | 50 | 52 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT31CGYCOL-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT31CGYCOL-CGY2 | period_spread |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT31CGYCOL-COL2 | period_spread |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT31CGYCOL-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT31CGYCOL-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT31CGYCOL-3 | period_total |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT31CGYCOL-CGY | period_winner |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT31CGYCOL-COL | period_winner |  | 0.525 |  | 54 | 49 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT31CGYCOL-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT31CGYCOL-CGY2 | period_spread |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT31CGYCOL-COL2 | period_spread |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT31CGYCOL-1 | period_total |  | 0.920 |  | 93 | 9 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT31CGYCOL-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT31CGYCOL-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT31CGYCOL-CGY | period_winner |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT31CGYCOL-COL | period_winner |  | 0.570 |  | 58 | 44 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT31CGYCOL-TIE | period_winner |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT31CGYCOL-CGY2 | period_spread |  | 0.045 |  | 5 | 96 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT31CGYCOL-COL2 | period_spread |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT31CGYCOL-1 | period_total |  | 0.900 |  | 93 | 13 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT31CGYCOL-2 | period_total |  | 0.685 |  | 70 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT31CGYCOL-3 | period_total |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYASUNIEV61-1 | player_assists |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYJFARABEE86-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYJFARABEE86-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYMCORONATO27-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYMCORONATO27-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYMFROST16-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYMGRIDIN92-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYSNEMEC71-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYYSHARANGOVICH17-1 | player_assists |  | 0.195 |  | 22 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-CGYZPAREKH19-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLALEHKONEN62-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLALEHKONEN62-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLBNELSON11-1 | player_assists |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLBNELSON11-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLCMAKAR8-1 | player_assists |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLCMAKAR8-2 | player_assists |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLCMAKAR8-3 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLDTOEWS7-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLDTOEWS7-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLGLANDESKOG92-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLGLANDESKOG92-2 | player_assists |  | 0.045 |  | 8 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLJSCHWARTZ71-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLMNECAS88-1 | player_assists |  | 0.560 |  | 57 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLMNECAS88-2 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLMNECAS88-3 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLNKADRI91-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLNKADRI91-2 | player_assists |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLNMACKINNON29-1 | player_assists |  | 0.645 |  | 66 | 37 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLNMACKINNON29-2 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLNMACKINNON29-3 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT31CGYCOL-COLNROY10-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ COL | 0.681 | 0.694 | 0.164 | 0.189 | 6.21 | 6.54 | 0.979/0.992 | KXNHLTOTAL-26OCT31CGYCOL-7 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Cale Makar: 1+ goals NO @ 73c · p 0.803 (adj 0.7835) · $19.23 · thesis COL:SUPPRESSED
- Noah Juulsen: 1+ goals NO @ 94c · p 0.9717 (adj 0.9613) · $19.23 · thesis DIFFUSE
- Aydar Suniev: 1+ goals YES @ 14c · p 0.1868 (adj 0.1739) · $5.65 · thesis CGY:OFFENSE_4PLUS
- Calgary over 3.5 goals scored YES @ 20c · p 0.2829 (adj 0.2389) · $5.89 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CGY @ COL** · priced 184/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.33, exp saves 23.3 (sd 6.25), pull risk 0.043
- CGY net: Arsenii Sergeev (CONFIRMED) exp shots 33.08, exp saves 27.7 (sd 7.76), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.209 | 0.350 | 36/66 | +0.116 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.399 | 0.525 | 53/48 | +0.104 | STANDARD |
| Cale Makar: 1+ assists | 0.474 | 0.595 | 60/41 | +0.099 | STANDARD |
| Cale Makar: 1+ points | 0.579 | 0.695 | 70/31 | +0.096 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.156 | 0.265 | 27/74 | +0.090 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.536 | 0.645 | 66/37 | +0.077 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
