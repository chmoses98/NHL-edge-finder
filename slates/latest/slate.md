# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-28T02:13:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 1 · markets on board: 4482 · contracts joined: 272 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 247, 'OK': 12, 'NO_EDGE': 13}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 53, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 65, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ SJS | 2026-10-28T02:30:00Z | T-10m | 0.459 | 0.541 | 0.170 | 6.74 | 3.24 | 3.50 | 272 (25/247) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT27BUFSJ-SJ | game_winner | 0.459 | 0.415 | 0.424 | 42 | 59 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.207 | 0.250 | 0.241 | 26 | 76 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.329 | 0.365 | 0.358 | 37 | 64 | no | +0.015 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.541 | 0.575 | 0.568 | 58 | 43 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3 | team_total | 0.684 | 0.720 | 0.713 | 73 | 29 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-5 | game_total | 0.830 | 0.855 | 0.850 | 86 | 15 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-SJ2 | game_spread | 0.261 | 0.235 | 0.240 | 24 | 77 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-4 | game_total | 0.896 | 0.915 | 0.912 | 92 | 9 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF5 | team_total | 0.279 | 0.315 | 0.308 | 33 | 70 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ6 | team_total | 0.109 | 0.095 | 0.098 | 10 | 91 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF2 | team_total | 0.862 | 0.880 | 0.877 | 89 | 13 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT27BUFSJ-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-7 | game_total | 0.535 | 0.555 | 0.551 | 56 | 45 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT27BUFSJ-SJ3 | game_spread | 0.156 | 0.145 | 0.147 | 15 | 86 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-6 | game_total | 0.648 | 0.665 | 0.662 | 67 | 34 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ4 | team_total | 0.420 | 0.405 | 0.408 | 41 | 60 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF6 | team_total | 0.139 | 0.150 | 0.148 | 16 | 86 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-3 | game_total | 0.977 | 0.980 | 0.979 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ5 | team_total | 0.233 | 0.225 | 0.227 | 23 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-10 | game_total | 0.128 | 0.125 | 0.126 | 13 | 88 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-9 | game_total | 0.248 | 0.255 | 0.254 | 26 | 75 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ3 | team_total | 0.630 | 0.620 | 0.622 | 63 | 39 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-SJ2 | team_total | 0.828 | 0.830 | 0.830 | 84 | 18 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT27BUFSJ-8 | game_total | 0.338 | 0.340 | 0.340 | 35 | 67 |  | -0.023 | NO_EDGE |
| KXNHL1P-26OCT27BUFSJ-BUF | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT27BUFSJ-SJ | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT27BUFSJ-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT27BUFSJ-BUF2 | period_spread |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT27BUFSJ-SJ2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT27BUFSJ-1 | period_total |  | 0.865 |  | 87 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT27BUFSJ-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT27BUFSJ-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT27BUFSJ-BUF | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT27BUFSJ-SJ | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT27BUFSJ-TIE | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT27BUFSJ-BUF2 | period_spread |  | 0.155 |  | 18 | 87 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT27BUFSJ-SJ2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT27BUFSJ-1 | period_total |  | 0.920 |  | 95 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT27BUFSJ-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT27BUFSJ-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT27BUFSJ-BUF | period_winner |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT27BUFSJ-SJ | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT27BUFSJ-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT27BUFSJ-BUF2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT27BUFSJ-SJ2 | period_spread |  | 0.130 |  | 15 | 89 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT27BUFSJ-1 | period_total |  | 0.940 |  | 96 | 8 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT27BUFSJ-2 | period_total |  | 0.710 |  | 74 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT27BUFSJ-3 | period_total |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFBMALENSTYN29-1 | player_assists |  | 0.080 |  | 14 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFJDOAN91-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFJDOAN91-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFJNORRIS9-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFJQUINN22-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFJQUINN22-2 | player_assists |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFJZUCKER17-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFKHELENIUS94-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFLCREVIER46-1 | player_assists |  | 0.090 |  | 16 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFMSAMUELSSON23-1 | player_assists |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFNOSTLUND86-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFNOSTLUND86-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFOPOWER25-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFOPOWER25-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFOZELLWEGER8-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFPKREBS19-1 | player_assists |  | 0.105 |  | 19 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFRDAHLIN26-1 | player_assists |  | 0.525 |  | 53 | 48 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFRDAHLIN26-2 | player_assists |  | 0.180 |  | 19 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFRMCLEOD71-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFRMCLEOD71-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFTKOZAK48-1 | player_assists |  | 0.055 |  | 10 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFTTHOMPSON72-1 | player_assists |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFTTHOMPSON72-2 | player_assists |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFZBENSON6-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFZBENSON6-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-BUFZMETSA73-1 | player_assists |  | 0.095 |  | 17 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-SJAGAUDETTE81-1 | player_assists |  | 0.095 |  | 18 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-SJBGOODROW23-1 | player_assists |  | 0.075 |  | 13 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-SJCGRAF51-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-SJCGRAF51-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT27BUFSJ-SJDNURSE25-1 | player_assists |  | 0.225 |  | 23 | 78 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ SJS | 0.459 | 0.527 | 0.170 | 0.214 | 6.74 | 6.53 | 1.039/1.000 | KXNHLGAME-26OCT27BUFSJ-SJ +0.067 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Gaudette: 1+ goals YES @ 13c · p 0.1808 (adj 0.1668) · $7.84 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 61c · p 0.6765 (adj 0.6586) · $20.0 · thesis BUF:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 63c · p 0.7236 (adj 0.6743) · $20.0 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ SJS** · priced 218/221 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.51, exp saves 24.69 (sd 6.8), pull risk 0.065
- BUF net: Colten Ellis (CONFIRMED) exp shots 27.09, exp saves 23.3 (sd 6.59), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.408 | 0.575 | 58/43 | +0.145 | STANDARD |
| Zack Ostapchuk: 1+ points | 0.235 | 0.090 | 16/98 | +0.066 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.434 | 0.580 | 59/43 | +0.118 | STANDARD |
| Barclay Goodrow: 1+ points | 0.234 | 0.100 | 18/98 | +0.044 | STANDARD |
| Sam Dickinson: 1+ points | 0.299 | 0.170 | 18/84 | +0.109 | STANDARD |
| Macklin Celebrini: 2+ points | 0.302 | 0.425 | 44/59 | +0.091 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
