# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-04T01:39:39Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 1 · markets on board: 4005 · contracts joined: 221 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 196, 'OK': 18, 'NO_EDGE': 7}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 30, 'game_early_goal': 1, 'first_goal': 35, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 39, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ VAN | 2026-11-04T02:00:00Z | T-10m | 0.420 | 0.580 | 0.164 | 7.25 | 3.36 | 3.89 | 221 (25/196) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN4 | team_total | 0.440 | 0.375 | 0.388 | 38 | 63 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN3 | team_total | 0.649 | 0.580 | 0.594 | 59 | 43 | yes | +0.042 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.418 | 0.355 | 0.367 | 36 | 65 | yes | +0.042 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.176 | 0.125 | 0.134 | 13 | 88 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN5 | team_total | 0.258 | 0.195 | 0.207 | 21 | 82 | yes | +0.037 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-9 | game_total | 0.319 | 0.265 | 0.275 | 27 | 74 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN6 | team_total | 0.126 | 0.080 | 0.088 | 9 | 93 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV03ANAVAN-ANA3 | game_spread | 0.251 | 0.295 | 0.286 | 30 | 71 | no | +0.024 | OK |
| KXNHLGAME-26NOV03ANAVAN-ANA | game_winner | 0.580 | 0.630 | 0.620 | 64 | 38 | no | +0.024 | OK |
| KXNHLGAME-26NOV03ANAVAN-VAN | game_winner | 0.420 | 0.375 | 0.384 | 38 | 63 | yes | +0.024 | OK |
| KXNHLSPREAD-26NOV03ANAVAN-VAN2 | game_spread | 0.238 | 0.205 | 0.211 | 21 | 80 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN2 | team_total | 0.837 | 0.800 | 0.808 | 81 | 21 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-6 | game_total | 0.711 | 0.675 | 0.682 | 68 | 33 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-7 | game_total | 0.612 | 0.575 | 0.583 | 58 | 43 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV03ANAVAN-ANA2 | game_spread | 0.374 | 0.405 | 0.399 | 41 | 60 | no | +0.009 | OK |
| KXNHLSPREAD-26NOV03ANAVAN-VAN3 | game_spread | 0.146 | 0.125 | 0.129 | 13 | 88 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-2 | game_total | 0.994 | 0.980 | 0.984 | 99 | 3 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-4 | game_total | 0.926 | 0.915 | 0.917 | 92 | 9 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA2 | team_total | 0.894 | 0.905 | 0.903 | 91 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4 | team_total | 0.558 | 0.575 | 0.572 | 58 | 43 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV03ANAVAN-3 | game_total | 0.983 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV03ANAVAN-5 | game_total | 0.870 | 0.865 | 0.866 | 87 | 14 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA3 | team_total | 0.749 | 0.760 | 0.758 | 77 | 25 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA6 | team_total | 0.199 | 0.195 | 0.196 | 21 | 82 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA5 | team_total | 0.357 | 0.360 | 0.359 | 37 | 65 |  | -0.023 | NO_EDGE |
| KXNHL1P-26NOV03ANAVAN-ANA | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV03ANAVAN-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV03ANAVAN-VAN | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV03ANAVAN-ANA2 | period_spread |  | 0.165 |  | 17 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV03ANAVAN-VAN2 | period_spread |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV03ANAVAN-1 | period_total |  | 0.870 |  | 88 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV03ANAVAN-2 | period_total |  | 0.635 |  | 64 | 37 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV03ANAVAN-3 | period_total |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV03ANAVAN-ANA | period_winner |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV03ANAVAN-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV03ANAVAN-VAN | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV03ANAVAN-ANA2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV03ANAVAN-VAN2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV03ANAVAN-1 | period_total |  | 0.915 |  | 94 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV03ANAVAN-2 | period_total |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV03ANAVAN-3 | period_total |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV03ANAVAN-ANA | period_winner |  | 0.450 |  | 46 | 56 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV03ANAVAN-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV03ANAVAN-VAN | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV03ANAVAN-ANA2 | period_spread |  | 0.230 |  | 24 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV03ANAVAN-VAN2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV03ANAVAN-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV03ANAVAN-2 | period_total |  | 0.710 |  | 73 | 31 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV03ANAVAN-3 | period_total |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAAKILLORN17-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANABSENNECKE45-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANABSENNECKE45-2 | player_assists |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANACGAUTHIER61-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANACGAUTHIER61-2 | player_assists |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANADHELLESON14-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAJCAULFIELD28-1 | player_assists |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAJLACOMBE2-1 | player_assists |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAJLACOMBE2-2 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAJLACOMBE2-3 | player_assists |  | 0.045 |  | 5 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANALCARLSSON91-1 | player_assists |  | 0.535 |  | 54 | 47 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANALCARLSSON91-2 | player_assists |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANALCARLSSON91-3 | player_assists |  | 0.045 |  | 5 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAMGRANLUND64-1 | player_assists |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANAMGRANLUND64-2 | player_assists |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANATLUNEAU67-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-ANATLUNEAU67-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANBBOESER6-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANBBOESER6-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANFHRONEK17-1 | player_assists |  | 0.490 |  | 50 | 52 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANFHRONEK17-2 | player_assists |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANJDEBRUSK74-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANJDEBRUSK74-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANJLEKKERIMKI88-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANJLEKKERIMKI88-2 | player_assists |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANLOHGREN92-1 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANMROSSI23-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANMROSSI23-2 | player_assists |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANZBUIUM8-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV03ANAVAN-VANZBUIUM8-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLF10G-26NOV03ANAVAN-Y | game_early_goal |  | 0.630 |  | 64 | 38 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ VAN | 0.420 | 0.430 | 0.164 | 0.207 | 7.25 | 6.76 | 1.027/0.968 | KXNHLTOTAL-26NOV03ANAVAN-8 -0.081 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Linus Karlsson: 1+ goals YES @ 18c · p 0.2375 (adj 0.2219) · $8.94 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 19c · p 0.2412 (adj 0.2271) · $7.72 · thesis VAN:OFFENSE_4PLUS
- Tom Willander: 1+ goals YES @ 4c · p 0.0612 (adj 0.0546) · $2.68 · thesis VAN:OFFENSE_4PLUS
- Cutter Gauthier: 1+ goals NO @ 57c · p 0.6269 (adj 0.6102) · $13.67 · thesis ANA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ VAN** · priced 162/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.41, exp saves 25.96 (sd 7.26), pull risk 0.083
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 24.99, exp saves 21.71 (sd 6.12), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 2+ points | 0.241 | 0.345 | 35/66 | +0.083 | STANDARD |
| Leo Carlsson: 1+ assists | 0.432 | 0.535 | 54/47 | +0.081 | STANDARD |
| Liam Ohgren: 1+ points | 0.417 | 0.335 | 34/67 | +0.061 | STANDARD |
| Leo Carlsson: 1+ points | 0.610 | 0.685 | 69/32 | +0.055 | STANDARD |
| Cutter Gauthier: 2+ points | 0.233 | 0.305 | 31/70 | +0.052 | STANDARD |
| Leo Carlsson: 2+ assists | 0.110 | 0.180 | 20/84 | +0.041 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
