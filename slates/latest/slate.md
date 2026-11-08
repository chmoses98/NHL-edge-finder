# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-08T02:38:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 1 · markets on board: 3614 · contracts joined: 225 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 200, 'OK': 16, 'NO_EDGE': 9}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 34, 'game_early_goal': 1, 'first_goal': 35, 'game_winner': 2, 'player_goals': 59, 'game_overtime': 1, 'player_points': 45, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ EDM | 2026-11-08T03:00:00Z | T-10m | 0.742 | 0.258 | 0.137 | 7.26 | 4.50 | 2.76 | 225 (25/200) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.423 | 0.365 | 0.376 | 37 | 64 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.154 | 0.110 | 0.118 | 12 | 90 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.522 | 0.470 | 0.480 | 48 | 54 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.066 | 0.035 | 0.040 | 4 | 97 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07VANEDM-9 | game_total | 0.316 | 0.270 | 0.279 | 28 | 74 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.305 | 0.260 | 0.269 | 27 | 75 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV07VANEDM-10 | game_total | 0.179 | 0.145 | 0.151 | 15 | 86 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV07VANEDM-7 | game_total | 0.614 | 0.575 | 0.583 | 58 | 43 | yes | +0.017 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.742 | 0.775 | 0.769 | 78 | 23 | no | +0.016 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM6 | team_total | 0.297 | 0.265 | 0.271 | 27 | 74 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.410 | 0.445 | 0.438 | 45 | 56 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN2 | team_total | 0.751 | 0.725 | 0.730 | 73 | 28 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV07VANEDM-6 | game_total | 0.720 | 0.690 | 0.696 | 70 | 32 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV07VANEDM-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV07VANEDM-VAN3 | game_spread | 0.065 | 0.055 | 0.057 | 6 | 95 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM2 | team_total | 0.937 | 0.945 | 0.943 | 95 | 6 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-4 | game_total | 0.927 | 0.935 | 0.933 | 94 | 7 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM3 | team_total | 0.834 | 0.850 | 0.847 | 86 | 16 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV07VANEDM-VAN2 | game_spread | 0.122 | 0.110 | 0.112 | 12 | 90 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM5 | team_total | 0.482 | 0.465 | 0.468 | 47 | 54 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-5 | game_total | 0.872 | 0.865 | 0.867 | 87 | 14 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-3 | game_total | 0.983 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV07VANEDM-EDM2 | game_spread | 0.550 | 0.565 | 0.562 | 57 | 44 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM4 | team_total | 0.677 | 0.680 | 0.679 | 69 | 33 |  | -0.022 | NO_EDGE |
| KXNHL1P-26NOV07VANEDM-EDM | period_winner |  | 0.505 |  | 51 | 50 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07VANEDM-TIE | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07VANEDM-VAN | period_winner |  | 0.215 |  | 22 | 79 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07VANEDM-EDM2 | period_spread |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07VANEDM-VAN2 | period_spread |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV07VANEDM-1 | period_total |  | 0.885 |  | 89 | 12 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV07VANEDM-2 | period_total |  | 0.645 |  | 65 | 36 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV07VANEDM-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV07VANEDM-EDM | period_winner |  | 0.515 |  | 53 | 50 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV07VANEDM-TIE | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV07VANEDM-VAN | period_winner |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV07VANEDM-EDM2 | period_spread |  | 0.235 |  | 26 | 79 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV07VANEDM-VAN2 | period_spread |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV07VANEDM-1 | period_total |  | 0.930 |  | 96 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV07VANEDM-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV07VANEDM-3 | period_total |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV07VANEDM-EDM | period_winner |  | 0.540 |  | 56 | 48 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV07VANEDM-TIE | period_winner |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV07VANEDM-VAN | period_winner |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV07VANEDM-EDM2 | period_spread |  | 0.290 |  | 32 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV07VANEDM-VAN2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV07VANEDM-1 | period_total |  | 0.930 |  | 97 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV07VANEDM-2 | period_total |  | 0.725 |  | 76 | 31 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV07VANEDM-3 | period_total |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-1 | player_assists |  | 0.735 |  | 76 | 29 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2 | player_assists |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-3 | player_assists |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-4 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMURPHY5-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMEBOUCHARD2-1 | player_assists |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMEBOUCHARD2-2 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMEBOUCHARD2-3 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMJDICKINSON16-1 | player_assists |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMKKAPANEN42-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMKKAPANEN42-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-1 | player_assists |  | 0.635 |  | 65 | 38 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-3 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRNUGENTHOPKINS93-1 | player_assists |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRNUGENTHOPKINS93-2 | player_assists |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRSHEA6-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRSHEA6-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANBBOESER6-1 | player_assists |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANBBOESER6-2 | player_assists |  | 0.090 |  | 9 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANEPETTERSSON40-1 | player_assists |  | 0.405 |  | 43 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANEPETTERSSON40-2 | player_assists |  |  |  | 13 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANFHRONEK17-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANFHRONEK17-2 | player_assists |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANJDEBRUSK74-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANJDEBRUSK74-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANJLEKKERIMKI88-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ EDM | 0.742 | 0.671 | 0.137 | 0.188 | 7.26 | 7.00 | 0.994/1.034 | KXNHLTEAMTOTAL-26NOV07VANEDM-EDM5 -0.083 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3479 (adj 0.3272) · $15.5 · thesis EDM:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2216 (adj 0.2049) · $8.55 · thesis VAN:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 11c · p 0.154 (adj 0.1417) · $6.78 · thesis EDM:OFFENSE_4PLUS
- Edmonton wins by over 2.5 goals NO @ 56c · p 0.6495 (adj 0.6022) · $19.18 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.3 (sd 5.98), pull risk 0.053
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 30.14, exp saves 25.05 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.265 | 0.425 | 43/58 | +0.138 | STANDARD |
| Connor McDavid: 2+ points | 0.512 | 0.635 | 64/37 | +0.102 | STANDARD |
| Connor McDavid: 3+ points | 0.253 | 0.370 | 39/65 | +0.081 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.411 | 0.300 | 31/71 | +0.086 | STANDARD |
| Leon Draisaitl: 2+ points | 0.436 | 0.545 | 56/47 | +0.076 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.187 | 0.295 | 30/71 | +0.089 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
