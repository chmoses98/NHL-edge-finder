# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-05T01:39:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 2 · markets on board: 2888 · contracts joined: 474 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 424, 'OK': 20, 'NO_EDGE': 30}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 82, 'game_early_goal': 2, 'first_goal': 66, 'game_winner': 4, 'player_goals': 116, 'game_overtime': 2, 'player_points': 104, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ LAK | 2026-11-05T03:00:00Z | T-60m | 0.591 | 0.409 | 0.170 | 6.36 | 3.49 | 2.87 | 248 (25/223) | PROBABLE/CONFIRMED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-60m | 0.591 | 0.409 | 0.168 | 6.51 | 3.55 | 2.96 | 226 (25/201) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.409 | 0.455 | 0.446 | 46 | 55 | no | +0.024 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.591 | 0.545 | 0.554 | 55 | 46 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.108 | 0.075 | 0.081 | 8 | 93 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.149 | 0.110 | 0.117 | 12 | 90 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.294 | 0.255 | 0.262 | 26 | 75 | yes | +0.020 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.373 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.126 | 0.155 | 0.149 | 16 | 85 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.307 | 0.270 | 0.277 | 28 | 74 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.499 | 0.465 | 0.472 | 47 | 54 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.097 | 0.075 | 0.079 | 8 | 93 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.283 | 0.255 | 0.260 | 26 | 75 | yes | +0.010 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.485 | 0.455 | 0.461 | 46 | 55 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.610 | 0.585 | 0.590 | 59 | 42 | yes | +0.003 | OK |
| KXNHLGAME-26NOV04SJLA-LA | game_winner | 0.591 | 0.615 | 0.610 | 62 | 39 | no | +0.003 | OK |
| KXNHLGAME-26NOV04SJLA-SJ | game_winner | 0.409 | 0.385 | 0.390 | 39 | 62 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.244 | 0.225 | 0.229 | 23 | 78 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.203 | 0.185 | 0.188 | 19 | 82 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.967 | 0.980 | 0.978 | 99 | 3 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.223 | 0.200 | 0.204 | 21 | 81 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.694 | 0.675 | 0.679 | 68 | 33 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.114 | 0.125 | 0.123 | 13 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA4 | team_total | 0.475 | 0.495 | 0.491 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.071 | 0.060 | 0.062 | 7 | 95 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.082 | 0.070 | 0.072 | 8 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.864 | 0.850 | 0.853 | 86 | 16 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.133 | 0.120 | 0.123 | 13 | 89 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.867 | 0.880 | 0.878 | 89 | 13 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.242 | 0.255 | 0.252 | 26 | 75 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-7 | game_total | 0.472 | 0.455 | 0.458 | 46 | 55 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.172 | 0.160 | 0.162 | 17 | 85 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-5 | game_total | 0.789 | 0.795 | 0.794 | 80 | 21 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ4 | team_total | 0.335 | 0.325 | 0.327 | 33 | 68 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY4 | team_total | 0.355 | 0.370 | 0.367 | 38 | 64 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ2 | game_spread | 0.209 | 0.205 | 0.206 | 21 | 80 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-6 | game_total | 0.584 | 0.575 | 0.577 | 58 | 43 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-3 | game_total | 0.970 | 0.975 | 0.974 | 99 | 4 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY3 | team_total | 0.566 | 0.580 | 0.577 | 59 | 43 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY5 | team_total | 0.187 | 0.170 | 0.173 | 19 | 85 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY2 | team_total | 0.787 | 0.785 | 0.785 | 79 | 22 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-5 | game_total | 0.806 | 0.805 | 0.805 | 81 | 20 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA5 | team_total | 0.272 | 0.275 | 0.274 | 28 | 73 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-4 | game_total | 0.878 | 0.880 | 0.880 | 89 | 13 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ3 | team_total | 0.549 | 0.555 | 0.554 | 56 | 45 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA2 | game_spread | 0.371 | 0.375 | 0.374 | 38 | 63 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA3 | team_total | 0.687 | 0.690 | 0.689 | 70 | 32 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ2 | team_total | 0.768 | 0.765 | 0.766 | 78 | 25 |  | -0.024 | NO_EDGE |
| KXNHL1P-26NOV04SJLA-LA | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV04SJLA-SJ | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV04SJLA-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV04SJLA-LA2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV04SJLA-SJ2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV04SJLA-1 | period_total |  | 0.845 |  | 86 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV04SJLA-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV04SJLA-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV04SJLA-LA | period_winner |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV04SJLA-SJ | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV04SJLA-TIE | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV04SJLA-LA2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV04SJLA-SJ2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV04SJLA-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV04SJLA-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV04SJLA-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV04SJLA-LA | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV04SJLA-SJ | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV04SJLA-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV04SJLA-LA2 | period_spread |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV04SJLA-SJ2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV04SJLA-1 | period_total |  | 0.910 |  | 92 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV04SJLA-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV04SJLA-3 | period_total |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV04SJLA-LAAKEMPE9-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV04SJLA-LAAKEMPE9-2 | player_assists |  | 0.105 |  | 13 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV04SJLA-LAALAFERRIERE14-1 | player_assists |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV04SJLA-LAALAFERRIERE14-2 | player_assists |  | 0.095 |  | 12 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV04SJLA-LAALEE47-1 | player_assists |  | 0.170 |  | 20 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV04SJLA-LAAPANARIN10-1 | player_assists |  | 0.570 |  | 59 | 45 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SJS @ LAK | 0.591 | 0.583 | 0.170 | 0.216 | 6.36 | 6.13 | 0.994/1.040 | KXNHLTOTAL-26NOV04SJLA-6 -0.041 |
| CGY @ SEA | 0.591 | 0.600 | 0.168 | 0.212 | 6.51 | 6.45 | 1.002/1.006 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.017 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Macklin Celebrini: 1+ assists NO @ 45c · p 0.6101 (adj 0.5028) · $14.58 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 65c · p 0.7324 (adj 0.6862) · $15.42 · thesis SJS:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2027 (adj 0.1933) · $5.08 · thesis SJS:OFFENSE_4PLUS
- Yaroslav Askarov: 28+ saves NO @ 55c · p 0.6463 (adj 0.5805) · $7.43 · thesis SJS:NET_LOW_VOLUME
- Jani Nyman: 1+ goals YES @ 11c · p 0.1615 (adj 0.1461) · $7.38 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 12c · p 0.1696 (adj 0.156) · $7.43 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 17c · p 0.2052 (adj 0.1939) · $4.1 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SJS @ LAK** · priced 195/197 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.34, exp saves 23.08 (sd 6.18), pull risk 0.045
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 29.28, exp saves 25.09 (sd 6.78), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.390 | 0.555 | 56/45 | +0.143 | STANDARD |
| Macklin Celebrini: 2+ points | 0.227 | 0.365 | 38/65 | +0.107 | STANDARD |
| Artemi Panarin: 2+ points | 0.258 | 0.385 | 40/63 | +0.095 | STANDARD |
| Artemi Panarin: 1+ assists | 0.446 | 0.570 | 59/45 | +0.087 | STANDARD |
| Ivar Stenberg: 1+ points | 0.342 | 0.455 | 47/56 | +0.081 | STANDARD |
| Yaroslav Askarov: 28+ saves | 0.354 | 0.455 | 46/55 | +0.079 |  |

**CGY @ SEA** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.65, exp saves 25.21 (sd 6.68), pull risk 0.049
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.22, exp saves 23.9 (sd 6.7), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.296 | 0.210 | 22/80 | +0.064 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.430 | 0.345 | 36/67 | +0.054 | STANDARD |
| Jani Nyman: 1+ goals | 0.162 | 0.100 | 11/91 | +0.045 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.341 | 0.285 | 29/72 | +0.036 | STANDARD |
| Ben Meyers: 1+ goals | 0.170 | 0.115 | 12/89 | +0.042 | STANDARD |
| Brandon Montour: 1+ assists | 0.394 | 0.345 | 36/67 | +0.018 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
