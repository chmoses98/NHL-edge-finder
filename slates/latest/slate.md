# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-04T17:21:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2826 · contracts joined: 889 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 789, 'OK': 53, 'NO_EDGE': 47}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 135, 'game_early_goal': 4, 'first_goal': 139, 'game_winner': 8, 'player_goals': 238, 'game_overtime': 4, 'player_points': 171, 'goalie_saves': 2, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-6h | 0.588 | 0.412 | 0.163 | 6.69 | 3.65 | 3.04 | 214 (25/189) | PROBABLE/PROJECTED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-6h | 0.604 | 0.396 | 0.175 | 6.26 | 3.46 | 2.80 | 218 (25/193) | CONFIRMED/PROJECTED |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-6h | 0.594 | 0.406 | 0.171 | 6.28 | 3.43 | 2.85 | 231 (25/206) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-6h | 0.589 | 0.411 | 0.169 | 6.45 | 3.51 | 2.94 | 226 (25/201) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.396 | 0.295 | 0.314 | 30 | 71 | yes | +0.081 | OK |
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.604 | 0.705 | 0.686 | 71 | 30 | no | +0.081 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.379 | 0.475 | 0.455 | 48 | 53 | no | +0.074 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.247 | 0.335 | 0.316 | 34 | 67 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.532 | 0.445 | 0.462 | 45 | 56 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4 | team_total | 0.319 | 0.245 | 0.259 | 25 | 76 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 | team_total | 0.467 | 0.535 | 0.521 | 54 | 47 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5 | team_total | 0.161 | 0.105 | 0.115 | 11 | 90 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI2 | game_spread | 0.203 | 0.145 | 0.155 | 15 | 86 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT2 | game_spread | 0.219 | 0.275 | 0.263 | 28 | 73 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2 | team_total | 0.757 | 0.705 | 0.716 | 71 | 30 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF2 | game_spread | 0.377 | 0.325 | 0.335 | 33 | 68 | yes | +0.032 | OK |
| KXNHLGAME-26NOV04OTTBUF-BUF | game_winner | 0.588 | 0.535 | 0.546 | 54 | 47 | yes | +0.031 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.112 | 0.075 | 0.081 | 8 | 93 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA3 | team_total | 0.680 | 0.730 | 0.720 | 74 | 28 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.859 | 0.900 | 0.893 | 91 | 11 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.066 | 0.025 | 0.030 | 4 | 99 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA5 | team_total | 0.272 | 0.320 | 0.310 | 33 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.490 | 0.445 | 0.454 | 45 | 56 | yes | +0.023 | OK |
| KXNHLGAME-26NOV04OTTBUF-OTT | game_winner | 0.412 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.123 | 0.160 | 0.152 | 17 | 85 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF4 | team_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.247 | 0.215 | 0.221 | 22 | 79 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.299 | 0.260 | 0.267 | 27 | 75 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.142 | 0.115 | 0.120 | 12 | 89 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.215 | 0.180 | 0.187 | 19 | 83 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA4 | team_total | 0.460 | 0.495 | 0.488 | 50 | 51 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.368 | 0.335 | 0.341 | 34 | 67 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.479 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.411 | 0.445 | 0.438 | 45 | 56 | no | +0.012 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.589 | 0.555 | 0.562 | 56 | 45 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.687 | 0.655 | 0.661 | 66 | 35 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.284 | 0.250 | 0.257 | 26 | 76 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.159 | 0.135 | 0.140 | 14 | 87 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.373 | 0.410 | 0.402 | 42 | 60 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-4 | game_total | 0.894 | 0.915 | 0.911 | 92 | 9 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.104 | 0.080 | 0.084 | 9 | 93 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.124 | 0.145 | 0.140 | 15 | 86 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.134 | 0.160 | 0.154 | 17 | 85 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.093 | 0.075 | 0.078 | 8 | 93 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.201 | 0.225 | 0.220 | 23 | 78 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.270 | 0.245 | 0.250 | 25 | 76 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF3 | team_total | 0.710 | 0.685 | 0.690 | 69 | 32 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT6 | team_total | 0.089 | 0.105 | 0.102 | 11 | 90 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-8 | game_total | 0.329 | 0.305 | 0.310 | 31 | 70 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.233 | 0.255 | 0.251 | 26 | 75 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.965 | 0.980 | 0.978 | 99 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.859 | 0.875 | 0.872 | 88 | 13 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.599 | 0.575 | 0.580 | 58 | 43 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.306 | 0.285 | 0.289 | 29 | 72 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.459 | 0.435 | 0.440 | 44 | 57 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.798 | 0.825 | 0.820 | 84 | 19 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.990 | 0.980 | 0.983 | 99 | 3 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF2 | team_total | 0.878 | 0.865 | 0.868 | 87 | 14 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.189 | 0.170 | 0.174 | 18 | 84 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.586 | 0.610 | 0.605 | 62 | 40 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.271 | 0.255 | 0.258 | 26 | 75 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.854 | 0.875 | 0.871 | 89 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-5 | game_total | 0.798 | 0.785 | 0.788 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.238 | 0.225 | 0.228 | 23 | 78 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-10 | game_total | 0.123 | 0.110 | 0.112 | 12 | 90 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.069 | 0.065 | 0.066 | 7 | 94 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-6 | game_total | 0.571 | 0.555 | 0.558 | 56 | 45 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ2 | team_total | 0.765 | 0.775 | 0.773 | 78 | 23 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-3 | game_total | 0.965 | 0.970 | 0.969 | 98 | 4 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-7 | game_total | 0.459 | 0.445 | 0.448 | 45 | 56 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.121 | 0.125 | 0.124 | 13 | 88 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.860 | 0.850 | 0.852 | 86 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.192 | 0.180 | 0.182 | 19 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.129 | 0.125 | 0.126 | 13 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.086 | 0.075 | 0.077 | 9 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.170 | 0.165 | 0.166 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-6 | game_total | 0.636 | 0.625 | 0.627 | 63 | 38 |  | -0.010 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-LA | game_winner | 0.594 | 0.605 | 0.603 | 61 | 40 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-SJ | game_winner | 0.406 | 0.395 | 0.397 | 40 | 61 |  | -0.011 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.588 | 0.526 | 0.163 | 0.214 | 6.69 | 6.54 | 0.999/1.051 | KXNHLSPREAD-26NOV04OTTBUF-BUF2 -0.068 |
| CHI @ FLA | 0.604 | 0.616 | 0.175 | 0.209 | 6.26 | 6.41 | 1.015/1.004 | KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 +0.032 |
| SJS @ LAK | 0.594 | 0.580 | 0.171 | 0.218 | 6.28 | 6.11 | 0.993/1.034 | KXNHLTOTAL-26NOV04SJLA-6 -0.033 |
| CGY @ SEA | 0.589 | 0.595 | 0.169 | 0.211 | 6.45 | 6.44 | 1.006/0.998 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Ridly Greig: 1+ goals YES @ 15c · p 0.2068 (adj 0.1901) · $8.83 · thesis OTT:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 25c · p 0.2982 (adj 0.2837) · $6.9 · thesis BUF:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 16c · p 0.1993 (adj 0.1857) · $4.98 · thesis OTT:OFFENSE_4PLUS
- Thomas Chabot: 1+ assists NO @ 67c · p 0.7365 (adj 0.6983) · $14.17 · thesis OTT:SUPPRESSED
- Wyatt Kaiser: 1+ goals YES @ 3c · p 0.0634 (adj 0.0538) · $4.36 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 20c · p 0.2734 (adj 0.2525) · $12.1 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1592 (adj 0.1444) · $6.84 · thesis CHI:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1334 (adj 0.1188) · $5.65 · thesis FLA:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8556 (adj 0.8392) · $17.61 · thesis SJS:SUPPRESSED
- Macklin Celebrini: 1+ assists NO @ 46c · p 0.621 (adj 0.5098) · $12.39 · thesis SJS:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 6c · p 0.0906 (adj 0.0792) · $3.39 · thesis LAK:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 11c · p 0.1531 (adj 0.1361) · $4.82 · thesis LAK:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 9c · p 0.1606 (adj 0.1404) · $10.39 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.2317 (adj 0.215) · $6.92 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 17c · p 0.2066 (adj 0.195) · $4.42 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.17, exp saves 23.54 (sd 6.55), pull risk 0.061
- OTT net: Samuel Ersson (PROJECTED) exp shots 27.44, exp saves 23.47 (sd 6.6), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ assists | 0.387 | 0.465 | 48/55 | +0.046 | STANDARD |
| Thomas Chabot: 1+ assists | 0.264 | 0.340 | 35/67 | +0.051 | STANDARD |
| Tage Thompson: 2+ points | 0.229 | 0.305 | 32/71 | +0.047 | STANDARD |
| Tage Thompson: 1+ assists | 0.367 | 0.440 | 46/58 | +0.036 | STANDARD |
| Jake Sanderson: 1+ points | 0.468 | 0.535 | 55/48 | +0.035 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.427 | 0.360 | 39/67 | +0.020 | STANDARD |

**CHI @ FLA** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 23.85, exp saves 20.95 (sd 5.83), pull risk 0.051
- CHI net: Spencer Knight (PROJECTED) exp shots 29.57, exp saves 25.14 (sd 7.0), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.343 | 0.470 | 48/54 | +0.099 | STANDARD |
| Sam Reinhart: 2+ points | 0.193 | 0.315 | 32/69 | +0.102 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.368 | 0.470 | 49/55 | +0.065 | STANDARD |
| Sam Reinhart: 1+ points | 0.544 | 0.645 | 67/38 | +0.059 | STANDARD |
| Brady Tkachuk: 2+ points | 0.214 | 0.305 | 32/71 | +0.061 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.513 | 0.425 | 44/59 | +0.056 | STANDARD |

**SJS @ LAK** · priced 163/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.34, exp saves 23.04 (sd 6.17), pull risk 0.046
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.28, exp saves 25.13 (sd 6.83), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.410 | 0.585 | 60/43 | +0.143 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.379 | 0.550 | 56/46 | +0.144 | STANDARD |
| Macklin Celebrini: 2+ points | 0.226 | 0.350 | 37/67 | +0.089 | STANDARD |
| Ivar Stenberg: 1+ points | 0.348 | 0.465 | 48/55 | +0.085 | STANDARD |
| Artemi Panarin: 2+ points | 0.261 | 0.375 | 39/64 | +0.083 | STANDARD |
| Trevor Moore: 1+ assists | 0.365 | 0.265 | 28/75 | +0.071 | STANDARD |

**CGY @ SEA** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 28.65, exp saves 25.17 (sd 6.72), pull risk 0.052
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.22, exp saves 24.02 (sd 6.66), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 2+ points | 0.112 | 0.495 | 98/99 | -0.103 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.424 | 0.205 | 40/99 | +0.007 | STANDARD |
| Ben Meyers: 1+ goals | 0.161 | 0.080 | 9/93 | +0.065 | STANDARD |
| Berkly Catton: 1+ goals | 0.232 | 0.165 | 18/85 | +0.041 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.340 | 0.275 | 29/74 | +0.036 | STANDARD |
| Kaapo Kakko: 1+ points | 0.478 | 0.420 | 43/59 | +0.030 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
