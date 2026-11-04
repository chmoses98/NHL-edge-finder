# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-04T21:20:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2906 · contracts joined: 943 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 843, 'OK': 57, 'NO_EDGE': 43}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 157, 'game_early_goal': 4, 'first_goal': 136, 'game_winner': 8, 'player_goals': 236, 'game_overtime': 4, 'player_points': 202, 'goalie_saves': 8, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-3h | 0.610 | 0.390 | 0.167 | 6.82 | 3.77 | 3.04 | 247 (25/222) | PROBABLE/CONFIRMED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-3h | 0.600 | 0.401 | 0.175 | 6.24 | 3.44 | 2.80 | 222 (25/197) | CONFIRMED/PROBABLE |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-3h | 0.591 | 0.409 | 0.170 | 6.36 | 3.49 | 2.87 | 248 (25/223) | PROBABLE/CONFIRMED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-3h | 0.591 | 0.409 | 0.168 | 6.51 | 3.55 | 2.96 | 226 (25/201) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.401 | 0.295 | 0.315 | 30 | 71 | yes | +0.086 | OK |
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.600 | 0.705 | 0.685 | 71 | 30 | no | +0.086 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.373 | 0.475 | 0.454 | 48 | 53 | no | +0.080 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.241 | 0.335 | 0.315 | 34 | 67 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.533 | 0.450 | 0.467 | 46 | 56 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4 | team_total | 0.319 | 0.245 | 0.259 | 25 | 76 | yes | +0.056 | OK |
| KXNHLGAME-26NOV04OTTBUF-BUF | game_winner | 0.610 | 0.535 | 0.550 | 54 | 47 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 | team_total | 0.460 | 0.535 | 0.520 | 54 | 47 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT2 | game_spread | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF2 | game_spread | 0.396 | 0.325 | 0.339 | 33 | 68 | yes | +0.050 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI2 | game_spread | 0.204 | 0.145 | 0.156 | 15 | 86 | yes | +0.046 | OK |
| KXNHLGAME-26NOV04OTTBUF-OTT | game_winner | 0.390 | 0.455 | 0.442 | 46 | 55 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2 | team_total | 0.758 | 0.705 | 0.716 | 71 | 30 | yes | +0.034 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.499 | 0.445 | 0.456 | 45 | 56 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5 | team_total | 0.157 | 0.110 | 0.118 | 12 | 90 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA5 | team_total | 0.266 | 0.320 | 0.309 | 33 | 69 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF3 | team_total | 0.734 | 0.685 | 0.695 | 69 | 32 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.855 | 0.900 | 0.892 | 91 | 11 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.113 | 0.075 | 0.082 | 8 | 93 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.176 | 0.135 | 0.142 | 14 | 87 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.330 | 0.285 | 0.294 | 29 | 72 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.116 | 0.155 | 0.146 | 16 | 85 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF4 | team_total | 0.531 | 0.480 | 0.490 | 49 | 53 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.307 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.294 | 0.250 | 0.258 | 26 | 76 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA3 | team_total | 0.676 | 0.725 | 0.716 | 74 | 29 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.694 | 0.655 | 0.663 | 66 | 35 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.485 | 0.445 | 0.453 | 45 | 56 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.373 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.257 | 0.220 | 0.227 | 23 | 79 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.369 | 0.405 | 0.398 | 41 | 60 | no | +0.014 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.409 | 0.445 | 0.438 | 45 | 56 | no | +0.014 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.591 | 0.555 | 0.562 | 56 | 45 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.066 | 0.030 | 0.035 | 5 | 99 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.610 | 0.575 | 0.582 | 58 | 43 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.108 | 0.080 | 0.085 | 9 | 93 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.097 | 0.075 | 0.079 | 8 | 93 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.223 | 0.190 | 0.196 | 20 | 82 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.149 | 0.120 | 0.125 | 13 | 89 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.198 | 0.225 | 0.219 | 23 | 78 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.283 | 0.255 | 0.260 | 26 | 75 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-10 | game_total | 0.136 | 0.115 | 0.119 | 12 | 89 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.133 | 0.165 | 0.158 | 18 | 85 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.587 | 0.620 | 0.613 | 63 | 39 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-8 | game_total | 0.352 | 0.320 | 0.326 | 33 | 69 | yes | +0.007 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.126 | 0.150 | 0.145 | 16 | 86 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-9 | game_total | 0.257 | 0.230 | 0.235 | 24 | 78 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-4 | game_total | 0.900 | 0.915 | 0.912 | 92 | 9 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.266 | 0.245 | 0.249 | 25 | 76 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT6 | team_total | 0.091 | 0.110 | 0.106 | 12 | 90 | no | +0.002 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.244 | 0.220 | 0.225 | 23 | 79 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.203 | 0.180 | 0.184 | 19 | 83 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF2 | team_total | 0.889 | 0.870 | 0.874 | 88 | 14 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.967 | 0.980 | 0.978 | 99 | 3 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-7 | game_total | 0.548 | 0.525 | 0.530 | 53 | 48 | yes | +0.000 | OK |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.114 | 0.125 | 0.123 | 13 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.801 | 0.825 | 0.820 | 84 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-6 | game_total | 0.654 | 0.630 | 0.635 | 64 | 38 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.188 | 0.170 | 0.174 | 18 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-3 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.454 | 0.435 | 0.439 | 44 | 57 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.864 | 0.845 | 0.849 | 86 | 17 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.867 | 0.880 | 0.878 | 89 | 13 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.242 | 0.255 | 0.252 | 26 | 75 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-5 | game_total | 0.806 | 0.795 | 0.797 | 80 | 21 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-7 | game_total | 0.472 | 0.455 | 0.458 | 46 | 55 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-4 | game_total | 0.859 | 0.865 | 0.864 | 87 | 14 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.088 | 0.075 | 0.078 | 9 | 94 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-LA | game_winner | 0.591 | 0.605 | 0.602 | 61 | 40 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-SJ | game_winner | 0.409 | 0.395 | 0.398 | 40 | 61 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.172 | 0.165 | 0.166 | 17 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-3 | game_total | 0.966 | 0.970 | 0.969 | 98 | 4 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-4 | game_total | 0.878 | 0.870 | 0.872 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-5 | game_total | 0.789 | 0.795 | 0.794 | 80 | 21 |  | -0.011 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.610 | 0.537 | 0.167 | 0.215 | 6.82 | 6.59 | 0.999/1.072 | KXNHLSPREAD-26NOV04OTTBUF-BUF2 -0.077 |
| CHI @ FLA | 0.600 | 0.615 | 0.175 | 0.210 | 6.24 | 6.39 | 1.015/0.996 | KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 +0.033 |
| SJS @ LAK | 0.591 | 0.583 | 0.170 | 0.216 | 6.36 | 6.13 | 0.994/1.040 | KXNHLTOTAL-26NOV04SJLA-6 -0.041 |
| CGY @ SEA | 0.591 | 0.600 | 0.168 | 0.212 | 6.51 | 6.45 | 1.002/1.006 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.017 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 13 recommended · full analysis in card.md / packet.json `thesis_card`

- Zach Benson: 1+ goals YES @ 26c · p 0.3049 (adj 0.2924) · $6.38 · thesis BUF:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.1839 (adj 0.1729) · $3.95 · thesis OTT:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 17c · p 0.203 (adj 0.191) · $3.36 · thesis OTT:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 60c · p 0.6746 (adj 0.6547) · $20.0 · thesis FLA:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 11c · p 0.1576 (adj 0.1419) · $6.35 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2699 (adj 0.2537) · $9.87 · thesis CHI:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1266 (adj 0.1124) · $4.08 · thesis FLA:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8522 (adj 0.8379) · $20.0 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 47c · p 0.6101 (adj 0.5093) · $9.69 · thesis SJS:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 42c · p 0.554 (adj 0.4498) · $5.64 · thesis LAK:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1696 (adj 0.1497) · $10.33 · thesis SEA:OFFENSE_4PLUS
- Jani Nyman: 1+ goals YES @ 11c · p 0.1615 (adj 0.1461) · $7.31 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.2288 (adj 0.2153) · $7.22 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 192/196 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.17, exp saves 23.53 (sd 6.58), pull risk 0.064
- OTT net: Samuel Ersson (CONFIRMED) exp shots 27.44, exp saves 23.49 (sd 6.59), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ridly Greig: 1+ points | 0.416 | 0.340 | 36/68 | +0.040 | STANDARD |
| Tim Stutzle: 1+ points | 0.629 | 0.705 | 71/30 | +0.056 | STANDARD |
| Tage Thompson: 1+ assists | 0.365 | 0.440 | 46/58 | +0.038 | STANDARD |
| Jake Sanderson: 1+ points | 0.477 | 0.550 | 56/46 | +0.046 | STANDARD |
| Jake Sanderson: 1+ assists | 0.397 | 0.470 | 48/54 | +0.045 | STANDARD |
| Michael Amadio: 1+ points | 0.377 | 0.305 | 34/73 | +0.021 | STANDARD |

**CHI @ FLA** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 23.85, exp saves 20.91 (sd 5.81), pull risk 0.054
- CHI net: Spencer Knight (PROBABLE) exp shots 29.57, exp saves 25.16 (sd 7.0), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 2+ points | 0.189 | 0.320 | 33/69 | +0.106 | STANDARD |
| Sam Reinhart: 1+ assists | 0.343 | 0.460 | 47/55 | +0.090 | STANDARD |
| Sam Reinhart: 1+ points | 0.536 | 0.650 | 67/37 | +0.077 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.361 | 0.465 | 48/55 | +0.071 | STANDARD |
| Sam Reinhart: 1+ goals | 0.298 | 0.400 | 41/61 | +0.075 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.494 | 0.400 | 42/62 | +0.057 | STANDARD |

**SJS @ LAK** · priced 195/197 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.34, exp saves 23.08 (sd 6.18), pull risk 0.045
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 29.28, exp saves 25.09 (sd 6.78), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.390 | 0.545 | 56/47 | +0.123 | STANDARD |
| Artemi Panarin: 1+ assists | 0.446 | 0.585 | 59/42 | +0.117 | STANDARD |
| Macklin Celebrini: 2+ points | 0.227 | 0.360 | 37/65 | +0.107 | STANDARD |
| Artemi Panarin: 2+ points | 0.258 | 0.375 | 40/65 | +0.076 | STANDARD |
| Ivar Stenberg: 1+ points | 0.342 | 0.450 | 47/57 | +0.071 | STANDARD |
| Artemi Panarin: 1+ points | 0.626 | 0.725 | 74/29 | +0.069 | STANDARD |

**CGY @ SEA** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.65, exp saves 25.21 (sd 6.68), pull risk 0.049
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.22, exp saves 23.9 (sd 6.7), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.296 | 0.205 | 23/82 | +0.053 | STANDARD |
| Joey Daccord: 25+ saves | 0.538 | 0.450 | 47/57 | +0.050 |  |
| Freddy Gaudreau: 1+ points | 0.430 | 0.345 | 38/69 | +0.034 | STANDARD |
| Ben Meyers: 1+ goals | 0.170 | 0.090 | 10/92 | +0.063 | STANDARD |
| Jani Nyman: 1+ goals | 0.162 | 0.100 | 11/91 | +0.045 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.341 | 0.285 | 29/72 | +0.036 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
