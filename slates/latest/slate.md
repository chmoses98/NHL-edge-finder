# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-04T18:20:48Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2846 · contracts joined: 909 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 809, 'OK': 58, 'NO_EDGE': 42}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 145, 'game_early_goal': 4, 'first_goal': 137, 'game_winner': 8, 'player_goals': 236, 'game_overtime': 4, 'player_points': 185, 'goalie_saves': 2, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-6h | 0.610 | 0.390 | 0.167 | 6.82 | 3.77 | 3.04 | 210 (25/185) | PROBABLE/CONFIRMED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-6h | 0.600 | 0.401 | 0.175 | 6.24 | 3.44 | 2.80 | 221 (25/196) | CONFIRMED/PROBABLE |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-6h | 0.594 | 0.406 | 0.171 | 6.28 | 3.43 | 2.85 | 252 (25/227) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-6h | 0.589 | 0.411 | 0.169 | 6.45 | 3.51 | 2.94 | 226 (25/201) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.401 | 0.295 | 0.315 | 30 | 71 | yes | +0.086 | OK |
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.600 | 0.705 | 0.685 | 71 | 30 | no | +0.086 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.373 | 0.475 | 0.454 | 48 | 53 | no | +0.080 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.241 | 0.335 | 0.315 | 34 | 67 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.533 | 0.445 | 0.463 | 45 | 56 | yes | +0.066 | OK |
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
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.855 | 0.905 | 0.896 | 92 | 11 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.113 | 0.075 | 0.082 | 8 | 93 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.176 | 0.135 | 0.142 | 14 | 87 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-8 | game_total | 0.352 | 0.305 | 0.314 | 31 | 70 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.330 | 0.285 | 0.294 | 29 | 72 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.116 | 0.155 | 0.146 | 16 | 85 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.066 | 0.025 | 0.030 | 4 | 99 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.490 | 0.445 | 0.454 | 45 | 56 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.284 | 0.245 | 0.253 | 25 | 76 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.299 | 0.260 | 0.267 | 27 | 75 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.142 | 0.115 | 0.120 | 12 | 89 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.257 | 0.220 | 0.227 | 23 | 79 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.369 | 0.405 | 0.398 | 41 | 60 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.215 | 0.180 | 0.187 | 19 | 83 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA4 | team_total | 0.460 | 0.495 | 0.488 | 50 | 51 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.368 | 0.335 | 0.341 | 34 | 67 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.479 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.411 | 0.445 | 0.438 | 45 | 56 | no | +0.012 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.589 | 0.555 | 0.562 | 56 | 45 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF2 | team_total | 0.889 | 0.865 | 0.870 | 87 | 14 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.687 | 0.655 | 0.661 | 66 | 35 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-7 | game_total | 0.548 | 0.515 | 0.522 | 52 | 49 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.198 | 0.225 | 0.219 | 23 | 78 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-10 | game_total | 0.136 | 0.115 | 0.119 | 12 | 89 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.104 | 0.080 | 0.084 | 9 | 93 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.133 | 0.160 | 0.154 | 17 | 85 | no | +0.008 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.124 | 0.145 | 0.140 | 15 | 86 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-6 | game_total | 0.654 | 0.625 | 0.631 | 63 | 38 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.093 | 0.075 | 0.078 | 8 | 93 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.587 | 0.615 | 0.609 | 62 | 39 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-9 | game_total | 0.257 | 0.235 | 0.239 | 24 | 77 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-4 | game_total | 0.900 | 0.915 | 0.912 | 92 | 9 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.233 | 0.255 | 0.251 | 26 | 75 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.965 | 0.980 | 0.978 | 99 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.859 | 0.880 | 0.876 | 89 | 13 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.266 | 0.245 | 0.249 | 25 | 76 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.599 | 0.575 | 0.580 | 58 | 43 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT6 | team_total | 0.091 | 0.105 | 0.102 | 11 | 90 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.801 | 0.825 | 0.820 | 84 | 19 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.188 | 0.170 | 0.174 | 18 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-5 | game_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.271 | 0.255 | 0.258 | 26 | 75 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.454 | 0.435 | 0.439 | 44 | 57 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-5 | game_total | 0.798 | 0.785 | 0.788 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.238 | 0.220 | 0.224 | 23 | 79 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.069 | 0.065 | 0.066 | 7 | 94 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ2 | team_total | 0.765 | 0.775 | 0.773 | 78 | 23 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.088 | 0.075 | 0.078 | 9 | 94 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY4 | team_total | 0.351 | 0.365 | 0.362 | 37 | 64 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.121 | 0.125 | 0.124 | 13 | 88 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.860 | 0.850 | 0.852 | 86 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-3 | game_total | 0.966 | 0.970 | 0.969 | 98 | 4 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.192 | 0.180 | 0.182 | 19 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.129 | 0.125 | 0.126 | 13 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.170 | 0.165 | 0.166 | 17 | 84 |  | -0.010 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.610 | 0.537 | 0.167 | 0.215 | 6.82 | 6.59 | 0.999/1.072 | KXNHLSPREAD-26NOV04OTTBUF-BUF2 -0.077 |
| CHI @ FLA | 0.600 | 0.615 | 0.175 | 0.210 | 6.24 | 6.39 | 1.015/0.996 | KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 +0.033 |
| SJS @ LAK | 0.594 | 0.580 | 0.171 | 0.218 | 6.28 | 6.11 | 0.993/1.034 | KXNHLTOTAL-26NOV04SJLA-6 -0.033 |
| CGY @ SEA | 0.589 | 0.595 | 0.169 | 0.211 | 6.45 | 6.44 | 1.006/0.998 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Zach Benson: 1+ goals YES @ 25c · p 0.3049 (adj 0.2874) · $7.94 · thesis BUF:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.1839 (adj 0.1729) · $3.9 · thesis OTT:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 17c · p 0.203 (adj 0.191) · $3.37 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 17c · p 0.203 (adj 0.191) · $3.16 · thesis OTT:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 62c · p 0.7015 (adj 0.6786) · $20.0 · thesis FLA:SUPPRESSED
- Oliver Moore: 1+ goals YES @ 11c · p 0.1576 (adj 0.1432) · $6.69 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2699 (adj 0.2537) · $9.71 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1473 (adj 0.1355) · $4.85 · thesis CHI:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 6c · p 0.0906 (adj 0.0829) · $4.45 · thesis LAK:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8556 (adj 0.8405) · $17.64 · thesis SJS:SUPPRESSED
- Andre Lee: 1+ goals YES @ 11c · p 0.1531 (adj 0.1398) · $5.88 · thesis LAK:OFFENSE_4PLUS
- Macklin Celebrini: 1+ assists NO @ 46c · p 0.621 (adj 0.5098) · $12.36 · thesis SJS:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 9c · p 0.1606 (adj 0.1417) · $10.82 · thesis SEA:OFFENSE_4PLUS
- Jake Middleton: 1+ goals YES @ 4c · p 0.0593 (adj 0.0532) · $2.4 · thesis CGY:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 19c · p 0.2317 (adj 0.2188) · $5.06 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 17c · p 0.2066 (adj 0.1937) · $4.06 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.17, exp saves 23.53 (sd 6.58), pull risk 0.064
- OTT net: Samuel Ersson (CONFIRMED) exp shots 27.44, exp saves 23.49 (sd 6.59), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ assists | 0.365 | 0.435 | 46/59 | +0.028 | STANDARD |
| Zach Benson: 1+ goals | 0.305 | 0.235 | 25/78 | +0.042 | STANDARD |
| Jake Sanderson: 1+ assists | 0.397 | 0.465 | 48/55 | +0.035 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.430 | 0.370 | 38/64 | +0.033 | STANDARD |
| Tage Thompson: 2+ points | 0.236 | 0.295 | 32/73 | +0.020 | STANDARD |
| Josh Doan: 1+ points | 0.424 | 0.365 | 37/64 | +0.037 | STANDARD |

**CHI @ FLA** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 23.85, exp saves 20.91 (sd 5.81), pull risk 0.054
- CHI net: Spencer Knight (PROBABLE) exp shots 29.57, exp saves 25.16 (sd 7.0), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 2+ points | 0.189 | 0.315 | 32/69 | +0.106 | STANDARD |
| Sam Reinhart: 1+ assists | 0.343 | 0.465 | 48/55 | +0.090 | STANDARD |
| Sam Reinhart: 1+ points | 0.536 | 0.645 | 67/38 | +0.067 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.361 | 0.465 | 48/55 | +0.071 | STANDARD |
| Brady Tkachuk: 2+ points | 0.212 | 0.310 | 32/70 | +0.073 | STANDARD |
| Sam Reinhart: 1+ goals | 0.298 | 0.390 | 40/62 | +0.065 | STANDARD |

**SJS @ LAK** · priced 184/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.34, exp saves 23.04 (sd 6.17), pull risk 0.046
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.28, exp saves 25.13 (sd 6.83), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.379 | 0.550 | 56/46 | +0.144 | STANDARD |
| Artemi Panarin: 1+ assists | 0.410 | 0.580 | 59/43 | +0.143 | STANDARD |
| Brian Dumoulin: 1+ points | 0.300 | 0.140 | 25/97 | +0.037 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.265 | 0.130 | 21/95 | +0.043 | STANDARD |
| Macklin Celebrini: 2+ points | 0.226 | 0.350 | 36/66 | +0.098 | STANDARD |
| Joel Edmundson: 1+ points | 0.323 | 0.210 | 26/84 | +0.049 | STANDARD |

**CGY @ SEA** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 28.65, exp saves 25.17 (sd 6.72), pull risk 0.052
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.22, exp saves 24.02 (sd 6.66), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ points | 0.424 | 0.205 | 40/99 | +0.007 | STANDARD |
| Ben Meyers: 1+ goals | 0.161 | 0.085 | 9/92 | +0.065 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.340 | 0.275 | 29/74 | +0.036 | STANDARD |
| Kaapo Kakko: 1+ points | 0.478 | 0.420 | 43/59 | +0.030 | STANDARD |
| Freddy Gaudreau: 2+ points | 0.112 | 0.170 | 33/99 | -0.103 | STANDARD |
| Berkly Catton: 1+ goals | 0.232 | 0.180 | 19/83 | +0.031 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
