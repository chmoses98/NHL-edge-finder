# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-03T01:30:39Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 1 · markets on board: 2813 · contracts joined: 235 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 210, 'NO_EDGE': 15, 'OK': 10}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 40, 'game_early_goal': 1, 'first_goal': 34, 'game_winner': 2, 'player_goals': 56, 'game_overtime': 1, 'player_points': 52, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ SJS | 2026-11-03T02:00:00Z | T-10m | 0.530 | 0.470 | 0.166 | 6.65 | 3.42 | 3.23 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.324 | 0.265 | 0.276 | 27 | 74 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.634 | 0.585 | 0.595 | 59 | 42 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.235 | 0.195 | 0.203 | 20 | 81 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.524 | 0.480 | 0.489 | 49 | 53 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.234 | 0.200 | 0.207 | 21 | 81 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.128 | 0.105 | 0.109 | 11 | 90 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.111 | 0.085 | 0.090 | 10 | 93 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ5 | team_total | 0.265 | 0.240 | 0.245 | 25 | 77 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ3 | team_total | 0.667 | 0.640 | 0.645 | 65 | 37 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.990 | 0.980 | 0.982 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-SJ3 | game_spread | 0.203 | 0.215 | 0.213 | 22 | 79 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ4 | team_total | 0.462 | 0.440 | 0.444 | 45 | 57 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY4 | team_total | 0.411 | 0.395 | 0.398 | 40 | 61 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-4 | game_total | 0.891 | 0.885 | 0.886 | 89 | 12 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-3 | game_total | 0.975 | 0.970 | 0.971 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-5 | game_total | 0.820 | 0.810 | 0.812 | 82 | 20 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY3 | team_total | 0.626 | 0.610 | 0.613 | 62 | 40 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY2 | game_spread | 0.271 | 0.265 | 0.266 | 27 | 74 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-SJ2 | game_spread | 0.322 | 0.315 | 0.316 | 32 | 69 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY2 | team_total | 0.825 | 0.815 | 0.817 | 83 | 20 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY3 | game_spread | 0.165 | 0.165 | 0.165 | 17 | 84 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ2 | team_total | 0.848 | 0.855 | 0.854 | 87 | 16 |  | -0.017 | NO_EDGE |
| KXNHLGAME-26NOV02CGYSJ-SJ | game_winner | 0.530 | 0.525 | 0.526 | 53 | 48 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26NOV02CGYSJ-CGY | game_winner | 0.470 | 0.475 | 0.474 | 48 | 53 |  | -0.018 | NO_EDGE |
| KXNHL1P-26NOV02CGYSJ-CGY | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV02CGYSJ-SJ | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV02CGYSJ-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV02CGYSJ-CGY2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV02CGYSJ-SJ2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV02CGYSJ-1 | period_total |  | 0.835 |  | 84 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV02CGYSJ-2 | period_total |  | 0.585 |  | 59 | 42 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV02CGYSJ-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV02CGYSJ-CGY | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV02CGYSJ-SJ | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV02CGYSJ-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV02CGYSJ-CGY2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV02CGYSJ-SJ2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV02CGYSJ-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV02CGYSJ-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV02CGYSJ-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV02CGYSJ-CGY | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV02CGYSJ-SJ | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV02CGYSJ-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV02CGYSJ-CGY2 | period_spread |  | 0.140 |  | 16 | 88 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV02CGYSJ-SJ2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV02CGYSJ-1 | period_total |  | 0.905 |  | 94 | 13 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV02CGYSJ-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV02CGYSJ-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYASUNIEV61-1 | player_assists |  | 0.215 |  | 22 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYJFARABEE86-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYJFARABEE86-2 | player_assists |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYKBAHL7-1 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMBACKLUND11-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMCORONATO27-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMCORONATO27-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMFROST16-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMFROST16-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMGRIDIN92-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMGRIDIN92-2 | player_assists |  | 0.065 |  | 9 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYMPOSPISIL76-1 | player_assists |  | 0.160 |  | 20 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYRSTROME22-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYRSTROME22-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYSNEMEC71-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYSNEMEC71-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYYSHARANGOVICH17-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYZPAREKH19-1 | player_assists |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYZPAREKH19-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-CGYZWHITECLOUD28-1 | player_assists |  | 0.185 |  | 19 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJCGRAF51-1 | player_assists |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJDNURSE25-1 | player_assists |  | 0.180 |  | 19 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJDORLOV9-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJDORLOV9-2 | player_assists |  | 0.065 |  | 9 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJISTENBERG41-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJISTENBERG41-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJJTROUBA65-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJJTROUBA65-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJKSHERWOOD44-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJMCELEBRINI71-1 | player_assists |  | 0.570 |  | 58 | 44 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV02CGYSJ-SJMCELEBRINI71-2 | player_assists |  | 0.175 |  | 22 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ SJS | 0.530 | 0.559 | 0.166 | 0.212 | 6.65 | 6.46 | 1.040/1.007 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 -0.040 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Ivar Stenberg: 1+ goals NO @ 76c · p 0.8203 (adj 0.804) · $20.0 · thesis SJS:SUPPRESSED
- Michael Misa: 1+ goals YES @ 18c · p 0.2175 (adj 0.2069) · $4.95 · thesis SJS:OFFENSE_4PLUS
- Michael Misa: 1+ assists YES @ 26c · p 0.3199 (adj 0.2874) · $4.51 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 25c · p 0.2843 (adj 0.2732) · $2.62 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CGY @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.38, exp saves 24.66 (sd 6.72), pull risk 0.057
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.99, exp saves 24.78 (sd 6.97), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ assists | 0.243 | 0.100 | 18/98 | +0.052 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.435 | 0.570 | 58/44 | +0.108 | STANDARD |
| Macklin Celebrini: 2+ points | 0.303 | 0.420 | 43/59 | +0.090 | STANDARD |
| Sam Dickinson: 1+ points | 0.296 | 0.185 | 21/84 | +0.074 | STANDARD |
| Dustin Wolf: 27+ saves | 0.396 | 0.495 | 55/56 | +0.027 |  |
| Macklin Celebrini: 3+ points | 0.100 | 0.195 | 20/81 | +0.079 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
