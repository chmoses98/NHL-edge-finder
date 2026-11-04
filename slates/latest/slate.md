# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-04T19:40:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2875 · contracts joined: 938 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 838, 'OK': 57, 'NO_EDGE': 43}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 157, 'game_early_goal': 4, 'first_goal': 135, 'game_winner': 8, 'player_goals': 233, 'game_overtime': 4, 'player_points': 202, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-3h | 0.610 | 0.390 | 0.167 | 6.82 | 3.77 | 3.04 | 244 (25/219) | PROBABLE/CONFIRMED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-3h | 0.600 | 0.401 | 0.175 | 6.24 | 3.44 | 2.80 | 222 (25/197) | CONFIRMED/PROBABLE |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-6h | 0.591 | 0.409 | 0.170 | 6.36 | 3.49 | 2.87 | 247 (25/222) | PROBABLE/CONFIRMED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-6h | 0.587 | 0.413 | 0.169 | 6.48 | 3.51 | 2.96 | 225 (25/200) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.401 | 0.295 | 0.315 | 30 | 71 | yes | +0.086 | OK |
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.600 | 0.705 | 0.685 | 71 | 30 | no | +0.086 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.373 | 0.475 | 0.454 | 48 | 53 | no | +0.080 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.241 | 0.335 | 0.315 | 34 | 67 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.533 | 0.440 | 0.459 | 45 | 57 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4 | team_total | 0.319 | 0.245 | 0.259 | 25 | 76 | yes | +0.056 | OK |
| KXNHLGAME-26NOV04OTTBUF-BUF | game_winner | 0.610 | 0.535 | 0.550 | 54 | 47 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 | team_total | 0.460 | 0.535 | 0.520 | 54 | 47 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT2 | game_spread | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF2 | game_spread | 0.396 | 0.325 | 0.339 | 33 | 68 | yes | +0.050 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI2 | game_spread | 0.204 | 0.145 | 0.156 | 15 | 86 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF4 | team_total | 0.531 | 0.465 | 0.478 | 47 | 54 | yes | +0.043 | OK |
| KXNHLGAME-26NOV04OTTBUF-OTT | game_winner | 0.390 | 0.455 | 0.442 | 46 | 55 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5 | team_total | 0.157 | 0.105 | 0.114 | 11 | 90 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2 | team_total | 0.758 | 0.705 | 0.716 | 71 | 30 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA3 | team_total | 0.676 | 0.730 | 0.720 | 74 | 28 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA5 | team_total | 0.266 | 0.320 | 0.309 | 33 | 69 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF3 | team_total | 0.734 | 0.685 | 0.695 | 69 | 32 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.496 | 0.445 | 0.455 | 45 | 56 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.855 | 0.900 | 0.892 | 91 | 11 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.113 | 0.075 | 0.082 | 8 | 93 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.176 | 0.135 | 0.142 | 14 | 87 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.330 | 0.285 | 0.294 | 29 | 72 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.116 | 0.155 | 0.146 | 16 | 85 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.257 | 0.215 | 0.223 | 22 | 79 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.066 | 0.025 | 0.030 | 4 | 99 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.300 | 0.265 | 0.272 | 27 | 74 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.143 | 0.115 | 0.120 | 12 | 89 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.216 | 0.185 | 0.191 | 19 | 82 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.369 | 0.405 | 0.398 | 41 | 60 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.480 | 0.445 | 0.452 | 45 | 56 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.285 | 0.250 | 0.257 | 26 | 76 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.688 | 0.655 | 0.662 | 66 | 35 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.097 | 0.075 | 0.079 | 8 | 93 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF2 | team_total | 0.889 | 0.865 | 0.870 | 87 | 14 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-7 | game_total | 0.548 | 0.515 | 0.522 | 52 | 49 | yes | +0.010 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.413 | 0.445 | 0.439 | 45 | 56 | no | +0.010 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.587 | 0.555 | 0.561 | 56 | 45 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.198 | 0.225 | 0.219 | 23 | 78 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.283 | 0.255 | 0.260 | 26 | 75 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-10 | game_total | 0.136 | 0.115 | 0.119 | 12 | 89 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.606 | 0.575 | 0.581 | 58 | 43 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.133 | 0.160 | 0.154 | 17 | 85 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.104 | 0.080 | 0.084 | 9 | 93 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-6 | game_total | 0.654 | 0.625 | 0.631 | 63 | 38 | yes | +0.008 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.363 | 0.335 | 0.341 | 34 | 67 | yes | +0.007 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.220 | 0.245 | 0.240 | 25 | 76 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.587 | 0.620 | 0.613 | 63 | 39 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-8 | game_total | 0.352 | 0.320 | 0.326 | 33 | 69 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-9 | game_total | 0.257 | 0.235 | 0.239 | 24 | 77 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-4 | game_total | 0.900 | 0.915 | 0.912 | 92 | 9 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.128 | 0.145 | 0.141 | 15 | 86 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.266 | 0.245 | 0.249 | 25 | 76 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT6 | team_total | 0.091 | 0.105 | 0.102 | 11 | 90 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.203 | 0.180 | 0.184 | 19 | 83 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.967 | 0.980 | 0.978 | 99 | 3 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-3 | game_total | 0.969 | 0.980 | 0.978 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.114 | 0.125 | 0.123 | 13 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.801 | 0.825 | 0.820 | 84 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.188 | 0.170 | 0.174 | 18 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA4 | team_total | 0.475 | 0.495 | 0.491 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.454 | 0.435 | 0.439 | 44 | 57 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.071 | 0.065 | 0.066 | 7 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.081 | 0.075 | 0.076 | 8 | 93 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY5 | team_total | 0.186 | 0.175 | 0.177 | 18 | 83 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.133 | 0.125 | 0.127 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.867 | 0.880 | 0.878 | 89 | 13 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.242 | 0.255 | 0.252 | 26 | 75 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-7 | game_total | 0.472 | 0.455 | 0.458 | 46 | 55 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.236 | 0.220 | 0.223 | 23 | 79 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.088 | 0.075 | 0.078 | 9 | 94 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-LA | game_winner | 0.591 | 0.605 | 0.602 | 61 | 40 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-SJ | game_winner | 0.409 | 0.395 | 0.398 | 40 | 61 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.172 | 0.165 | 0.166 | 17 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-5 | game_total | 0.803 | 0.795 | 0.797 | 80 | 21 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.610 | 0.537 | 0.167 | 0.215 | 6.82 | 6.59 | 0.999/1.072 | KXNHLSPREAD-26NOV04OTTBUF-BUF2 -0.077 |
| CHI @ FLA | 0.600 | 0.615 | 0.175 | 0.210 | 6.24 | 6.39 | 1.015/0.996 | KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 +0.033 |
| SJS @ LAK | 0.591 | 0.583 | 0.170 | 0.216 | 6.36 | 6.13 | 0.994/1.040 | KXNHLTOTAL-26NOV04SJLA-6 -0.041 |
| CGY @ SEA | 0.587 | 0.598 | 0.169 | 0.207 | 6.48 | 6.43 | 1.002/0.998 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Claude Giroux: 1+ goals YES @ 15c · p 0.203 (adj 0.1885) · $8.21 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.203 (adj 0.1885) · $5.3 · thesis OTT:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 15c · p 0.1828 (adj 0.1734) · $4.12 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.1839 (adj 0.1729) · $3.98 · thesis OTT:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 61c · p 0.7015 (adj 0.6774) · $20.0 · thesis FLA:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 11c · p 0.1576 (adj 0.1432) · $6.66 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2699 (adj 0.2537) · $9.69 · thesis CHI:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1266 (adj 0.1149) · $4.76 · thesis FLA:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 11c · p 0.1522 (adj 0.1391) · $5.55 · thesis LAK:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8498 (adj 0.8361) · $19.15 · thesis SJS:SUPPRESSED
- Trevor Moore: 1+ assists YES @ 28c · p 0.365 (adj 0.32) · $8.08 · thesis LAK:OFFENSE_4PLUS
- Macklin Celebrini: 1+ assists NO @ 47c · p 0.6117 (adj 0.5131) · $10.85 · thesis SJS:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1598 (adj 0.1436) · $9.0 · thesis SEA:OFFENSE_4PLUS
- Zach Whitecloud: 1+ goals YES @ 2c · p 0.0421 (adj 0.0391) · $3.9 · thesis CGY:OFFENSE_4PLUS
- Jani Nyman: 1+ goals YES @ 11c · p 0.1568 (adj 0.1426) · $6.54 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.2308 (adj 0.2156) · $7.26 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 192/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.17, exp saves 23.53 (sd 6.58), pull risk 0.064
- OTT net: Samuel Ersson (CONFIRMED) exp shots 27.44, exp saves 23.49 (sd 6.59), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ridly Greig: 1+ points | 0.416 | 0.340 | 37/69 | +0.030 | STANDARD |
| Tim Stutzle: 1+ points | 0.629 | 0.705 | 71/30 | +0.056 | STANDARD |
| Tage Thompson: 1+ assists | 0.365 | 0.440 | 46/58 | +0.038 | STANDARD |
| Tage Thompson: 2+ points | 0.236 | 0.305 | 32/71 | +0.039 | STANDARD |
| Jake Sanderson: 1+ assists | 0.397 | 0.465 | 48/55 | +0.035 | STANDARD |
| Ridly Greig: 1+ assists | 0.267 | 0.200 | 24/84 | +0.014 | STANDARD |

**CHI @ FLA** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 23.85, exp saves 20.91 (sd 5.81), pull risk 0.054
- CHI net: Spencer Knight (PROBABLE) exp shots 29.57, exp saves 25.16 (sd 7.0), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 2+ points | 0.189 | 0.315 | 32/69 | +0.106 | STANDARD |
| Sam Reinhart: 1+ assists | 0.343 | 0.460 | 47/55 | +0.090 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.361 | 0.470 | 48/54 | +0.081 | STANDARD |
| Sam Reinhart: 1+ points | 0.536 | 0.640 | 66/38 | +0.067 | STANDARD |
| Brady Tkachuk: 2+ points | 0.212 | 0.310 | 32/70 | +0.073 | STANDARD |
| Sam Reinhart: 1+ goals | 0.298 | 0.395 | 40/61 | +0.075 | STANDARD |

**SJS @ LAK** · priced 179/196 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.34, exp saves 23.03 (sd 6.21), pull risk 0.048
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 29.28, exp saves 25.09 (sd 6.78), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikey Anderson: 1+ points | 0.333 | 0.140 | 27/99 | +0.049 | STANDARD |
| Artemi Panarin: 1+ assists | 0.413 | 0.575 | 58/43 | +0.139 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.388 | 0.540 | 55/47 | +0.124 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.264 | 0.135 | 21/94 | +0.043 | STANDARD |
| Macklin Celebrini: 2+ points | 0.233 | 0.360 | 38/66 | +0.091 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.086 | 0.205 | 24/83 | +0.074 | STANDARD |

**CGY @ SEA** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.65, exp saves 25.21 (sd 6.7), pull risk 0.05
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.22, exp saves 23.96 (sd 6.72), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.286 | 0.200 | 24/84 | +0.033 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.429 | 0.345 | 39/70 | +0.022 | STANDARD |
| Ben Meyers: 1+ goals | 0.160 | 0.095 | 10/91 | +0.053 | STANDARD |
| Joey Daccord: 25+ saves | 0.542 | 0.480 | 53/57 | -0.006 |  |
| Berkly Catton: 1+ goals | 0.231 | 0.170 | 18/84 | +0.040 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.204 | 0.145 | 16/87 | +0.034 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
