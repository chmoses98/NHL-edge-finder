# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-08T02:12:36Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 1 · markets on board: 3644 · contracts joined: 225 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 200, 'OK': 17, 'NO_EDGE': 8}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 34, 'game_early_goal': 1, 'first_goal': 35, 'game_winner': 2, 'player_goals': 59, 'game_overtime': 1, 'player_points': 45, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ EDM | 2026-11-08T03:00:00Z | T-30m | 0.734 | 0.266 | 0.139 | 7.19 | 4.43 | 2.76 | 225 (25/200) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.519 | 0.465 | 0.476 | 47 | 54 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.153 | 0.115 | 0.122 | 12 | 89 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.405 | 0.365 | 0.373 | 37 | 64 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07VANEDM-10 | game_total | 0.172 | 0.145 | 0.150 | 15 | 86 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.065 | 0.040 | 0.044 | 5 | 97 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV07VANEDM-6 | game_total | 0.713 | 0.685 | 0.691 | 69 | 32 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN2 | team_total | 0.752 | 0.725 | 0.731 | 73 | 28 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV07VANEDM-9 | game_total | 0.302 | 0.270 | 0.276 | 28 | 74 | yes | +0.007 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM2 | game_spread | 0.539 | 0.565 | 0.560 | 57 | 44 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV07VANEDM-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV07VANEDM-VAN3 | game_spread | 0.067 | 0.055 | 0.057 | 6 | 95 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV07VANEDM-VAN2 | game_spread | 0.129 | 0.110 | 0.114 | 12 | 90 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM2 | team_total | 0.935 | 0.945 | 0.943 | 95 | 6 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM6 | team_total | 0.283 | 0.265 | 0.269 | 27 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-4 | game_total | 0.928 | 0.935 | 0.934 | 94 | 7 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-3 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-7 | game_total | 0.601 | 0.585 | 0.588 | 59 | 42 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-5 | game_total | 0.871 | 0.865 | 0.866 | 87 | 14 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM4 | team_total | 0.663 | 0.685 | 0.681 | 70 | 33 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM3 | team_total | 0.829 | 0.845 | 0.842 | 86 | 17 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM5 | team_total | 0.465 | 0.470 | 0.469 | 48 | 54 |  | -0.022 | NO_EDGE |
| KXNHL1P-26NOV07VANEDM-EDM | period_winner |  | 0.505 |  | 51 | 50 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07VANEDM-TIE | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07VANEDM-VAN | period_winner |  | 0.215 |  | 22 | 79 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07VANEDM-EDM2 | period_spread |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07VANEDM-VAN2 | period_spread |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV07VANEDM-1 | period_total |  | 0.885 |  | 89 | 12 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV07VANEDM-2 | period_total |  | 0.645 |  | 65 | 36 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV07VANEDM-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV07VANEDM-EDM | period_winner |  | 0.515 |  | 53 | 50 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV07VANEDM-TIE | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV07VANEDM-VAN | period_winner |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV07VANEDM-EDM2 | period_spread |  | 0.235 |  | 26 | 79 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV07VANEDM-VAN2 | period_spread |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV07VANEDM-1 | period_total |  | 0.925 |  | 96 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV07VANEDM-2 | period_total |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV07VANEDM-3 | period_total |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV07VANEDM-EDM | period_winner |  | 0.540 |  | 56 | 48 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV07VANEDM-TIE | period_winner |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV07VANEDM-VAN | period_winner |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV07VANEDM-EDM2 | period_spread |  | 0.290 |  | 32 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV07VANEDM-VAN2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV07VANEDM-1 | period_total |  | 0.930 |  | 97 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV07VANEDM-2 | period_total |  | 0.725 |  | 76 | 31 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV07VANEDM-3 | period_total |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-1 | player_assists |  | 0.735 |  | 77 | 30 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2 | player_assists |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-3 | player_assists |  | 0.175 |  | 20 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-4 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMCMURPHY5-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMEBOUCHARD2-1 | player_assists |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMEBOUCHARD2-2 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMEBOUCHARD2-3 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMJDICKINSON16-1 | player_assists |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMKKAPANEN42-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMKKAPANEN42-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-1 | player_assists |  | 0.645 |  | 65 | 36 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-3 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRNUGENTHOPKINS93-1 | player_assists |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRNUGENTHOPKINS93-2 | player_assists |  | 0.125 |  | 15 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRSHEA6-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMRSHEA6-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANBBOESER6-1 | player_assists |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANBBOESER6-2 | player_assists |  | 0.090 |  | 9 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANEPETTERSSON40-1 | player_assists |  | 0.405 |  | 43 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANEPETTERSSON40-2 | player_assists |  |  |  | 11 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANFHRONEK17-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANFHRONEK17-2 | player_assists |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANJDEBRUSK74-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANJDEBRUSK74-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV07VANEDM-VANJLEKKERIMKI88-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ EDM | 0.734 | 0.670 | 0.139 | 0.190 | 7.19 | 6.99 | 0.994/1.030 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3483 (adj 0.3262) · $15.42 · thesis EDM:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2205 (adj 0.2041) · $9.31 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 10c · p 0.1436 (adj 0.1302) · $5.78 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 58c · p 0.7356 (adj 0.628) · $19.49 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.32 (sd 5.93), pull risk 0.052
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.14, exp saves 25.04 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.264 | 0.430 | 44/58 | +0.139 | STANDARD |
| Connor McDavid: 2+ points | 0.513 | 0.645 | 66/37 | +0.100 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.416 | 0.300 | 31/71 | +0.091 | STANDARD |
| Leon Draisaitl: 2+ points | 0.433 | 0.545 | 56/47 | +0.080 | STANDARD |
| Connor McDavid: 3+ points | 0.254 | 0.365 | 38/65 | +0.080 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.187 | 0.295 | 30/71 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
