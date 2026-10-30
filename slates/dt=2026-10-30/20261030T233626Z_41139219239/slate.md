# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T23:36:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 1 · markets on board: 2942 · contracts joined: 229 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 204, 'OK': 14, 'NO_EDGE': 11}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 32, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 68, 'game_overtime': 1, 'player_points': 40, 'goalie_saves': 1, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CGY | 2026-10-31T00:00:00Z | T-10m | 0.444 | 0.556 | 0.175 | 6.26 | 2.96 | 3.30 | 229 (25/204) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.353 | 0.415 | 0.402 | 42 | 59 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.182 | 0.235 | 0.224 | 24 | 77 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.574 | 0.625 | 0.615 | 63 | 38 | no | +0.030 | OK |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.556 | 0.505 | 0.515 | 51 | 50 | yes | +0.029 | OK |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.444 | 0.495 | 0.485 | 50 | 51 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.136 | 0.175 | 0.167 | 18 | 83 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.238 | 0.275 | 0.267 | 28 | 73 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.782 | 0.815 | 0.809 | 82 | 19 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.458 | 0.495 | 0.488 | 50 | 51 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.863 | 0.885 | 0.881 | 89 | 12 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.792 | 0.825 | 0.819 | 84 | 19 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.330 | 0.305 | 0.310 | 31 | 70 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.571 | 0.595 | 0.590 | 60 | 41 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.968 | 0.980 | 0.978 | 99 | 3 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.075 | 0.090 | 0.087 | 10 | 92 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.114 | 0.100 | 0.103 | 11 | 91 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.184 | 0.200 | 0.197 | 21 | 81 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.203 | 0.195 | 0.196 | 20 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.265 | 0.275 | 0.273 | 28 | 73 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.086 | 0.090 | 0.089 | 10 | 92 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.651 | 0.640 | 0.642 | 65 | 37 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.237 | 0.230 | 0.231 | 24 | 78 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.839 | 0.840 | 0.840 | 85 | 17 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.431 | 0.430 | 0.430 | 44 | 58 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT30SEACGY-CGY | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30SEACGY-SEA | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30SEACGY-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30SEACGY-CGY2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30SEACGY-SEA2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT30SEACGY-1 | period_total |  | 0.840 |  | 85 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT30SEACGY-2 | period_total |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT30SEACGY-3 | period_total |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT30SEACGY-CGY | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT30SEACGY-SEA | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT30SEACGY-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT30SEACGY-CGY2 | period_spread |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT30SEACGY-SEA2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT30SEACGY-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT30SEACGY-2 | period_total |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT30SEACGY-3 | period_total |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT30SEACGY-CGY | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT30SEACGY-SEA | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT30SEACGY-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT30SEACGY-CGY2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT30SEACGY-SEA2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT30SEACGY-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT30SEACGY-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT30SEACGY-3 | period_total |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYJFARABEE86-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYJFARABEE86-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMBACKLUND11-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMCORONATO27-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMCORONATO27-2 | player_assists |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMFROST16-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMFROST16-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMGRIDIN92-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYMGRIDIN92-2 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYRSTROME22-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYSNEMEC71-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYSNEMEC71-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYYSHARANGOVICH17-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYZPAREKH19-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-CGYZPAREKH19-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEABCATTON27-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEABCATTON27-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEABMCMANN74-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEABMCMANN74-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEABMONTOUR62-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEABMONTOUR62-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEACSTEPHENSON9-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEACSTEPHENSON9-2 | player_assists |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAJEBERLE7-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAJEBERLE7-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAKKAKKO84-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAKKAKKO84-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAMBENIERS10-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAMBENIERS10-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAMSAMOSKEVICH11-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30SEACGY-SEAVDUNN29-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CGY | 0.444 | 0.473 | 0.175 | 0.220 | 6.26 | 6.40 | 1.006/1.023 | KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 +0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Freddy Gaudreau: 1+ goals YES @ 11c · p 0.1733 (adj 0.1525) · $8.63 · thesis SEA:WINS_BY_2PLUS
- Ben Meyers: 1+ goals YES @ 12c · p 0.1566 (adj 0.1462) · $4.84 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.2211 (adj 0.2096) · $5.42 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ CGY** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.63, exp saves 23.74 (sd 6.57), pull risk 0.07
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 29.7, exp saves 25.72 (sd 6.88), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.173 | 0.090 | 11/93 | +0.056 | STANDARD |
| Berkly Catton: 1+ goals | 0.221 | 0.175 | 18/83 | +0.031 | STANDARD |
| Brandon Montour: 1+ assists | 0.371 | 0.325 | 33/68 | +0.025 | STANDARD |
| Berkly Catton: 1+ points | 0.451 | 0.405 | 41/60 | +0.024 | STANDARD |
| Vince Dunn: 1+ assists | 0.361 | 0.405 | 41/60 | +0.023 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.263 | 0.220 | 24/80 | +0.010 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
