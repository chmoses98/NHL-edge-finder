# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-04T14:37:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2455 · contracts joined: 518 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 418, 'OK': 50, 'NO_EDGE': 50}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 54, 'game_early_goal': 4, 'first_goal': 71, 'game_winner': 8, 'player_goals': 121, 'game_overtime': 4, 'player_points': 68, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-6h | 0.589 | 0.411 | 0.171 | 6.71 | 3.65 | 3.06 | 206 (25/181) | PROJECTED/PROJECTED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-6h | 0.612 | 0.388 | 0.172 | 6.21 | 3.46 | 2.75 | 210 (25/185) | PROJECTED/PROJECTED |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-12h | 0.594 | 0.406 | 0.171 | 6.28 | 3.43 | 2.85 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-12h | 0.589 | 0.411 | 0.169 | 6.45 | 3.51 | 2.94 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.388 | 0.295 | 0.313 | 30 | 71 | yes | +0.074 | OK |
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.612 | 0.705 | 0.687 | 71 | 30 | no | +0.074 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.386 | 0.475 | 0.457 | 48 | 53 | no | +0.067 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.248 | 0.335 | 0.316 | 34 | 67 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.522 | 0.450 | 0.464 | 46 | 56 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4 | team_total | 0.307 | 0.245 | 0.257 | 25 | 76 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 | team_total | 0.469 | 0.535 | 0.522 | 54 | 47 | no | +0.044 | OK |
| KXNHLGAME-26NOV04OTTBUF-BUF | game_winner | 0.589 | 0.525 | 0.538 | 53 | 48 | yes | +0.041 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI2 | game_spread | 0.194 | 0.145 | 0.154 | 15 | 86 | yes | +0.035 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT2 | game_spread | 0.221 | 0.275 | 0.264 | 28 | 73 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5 | team_total | 0.149 | 0.105 | 0.113 | 11 | 90 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF2 | game_spread | 0.373 | 0.325 | 0.334 | 33 | 68 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA3 | team_total | 0.680 | 0.730 | 0.720 | 74 | 28 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2 | team_total | 0.750 | 0.705 | 0.714 | 71 | 30 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.858 | 0.895 | 0.888 | 90 | 11 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA5 | team_total | 0.271 | 0.320 | 0.310 | 33 | 69 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.490 | 0.445 | 0.454 | 45 | 56 | yes | +0.023 | OK |
| KXNHLGAME-26NOV04OTTBUF-OTT | game_winner | 0.411 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.063 | 0.025 | 0.030 | 4 | 99 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF4 | team_total | 0.505 | 0.465 | 0.473 | 47 | 54 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.299 | 0.255 | 0.263 | 27 | 76 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.142 | 0.115 | 0.120 | 12 | 89 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.246 | 0.215 | 0.221 | 22 | 79 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.215 | 0.180 | 0.187 | 19 | 83 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.479 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.108 | 0.085 | 0.089 | 9 | 92 | yes | +0.012 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.129 | 0.160 | 0.153 | 17 | 85 | no | +0.012 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.411 | 0.445 | 0.438 | 45 | 56 | no | +0.012 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.589 | 0.555 | 0.562 | 56 | 45 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.160 | 0.135 | 0.140 | 14 | 87 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.284 | 0.250 | 0.257 | 26 | 76 | yes | +0.011 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.374 | 0.410 | 0.403 | 42 | 60 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.801 | 0.830 | 0.824 | 84 | 18 | no | +0.009 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.124 | 0.145 | 0.140 | 15 | 86 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.134 | 0.155 | 0.151 | 16 | 85 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-4 | game_total | 0.897 | 0.915 | 0.912 | 92 | 9 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF3 | team_total | 0.711 | 0.685 | 0.690 | 69 | 32 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-8 | game_total | 0.329 | 0.305 | 0.310 | 31 | 70 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.204 | 0.230 | 0.225 | 24 | 78 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.233 | 0.255 | 0.251 | 26 | 75 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.965 | 0.980 | 0.978 | 99 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.859 | 0.875 | 0.872 | 88 | 13 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.599 | 0.575 | 0.580 | 58 | 43 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT6 | team_total | 0.091 | 0.105 | 0.102 | 11 | 90 | no | +0.002 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.368 | 0.345 | 0.350 | 35 | 66 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.592 | 0.620 | 0.614 | 63 | 39 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.687 | 0.660 | 0.665 | 67 | 35 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.306 | 0.285 | 0.289 | 29 | 72 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.261 | 0.245 | 0.248 | 25 | 76 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.104 | 0.085 | 0.089 | 10 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.271 | 0.255 | 0.258 | 26 | 75 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-10 | game_total | 0.124 | 0.115 | 0.117 | 12 | 89 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.093 | 0.075 | 0.078 | 9 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-5 | game_total | 0.798 | 0.785 | 0.788 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.238 | 0.225 | 0.228 | 23 | 78 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.069 | 0.065 | 0.066 | 7 | 94 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-3 | game_total | 0.964 | 0.970 | 0.969 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ2 | team_total | 0.765 | 0.775 | 0.773 | 78 | 23 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.183 | 0.170 | 0.173 | 18 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.449 | 0.435 | 0.438 | 44 | 57 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-7 | game_total | 0.459 | 0.445 | 0.448 | 45 | 56 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.121 | 0.125 | 0.124 | 13 | 88 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.860 | 0.850 | 0.852 | 86 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.192 | 0.180 | 0.182 | 19 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.129 | 0.125 | 0.126 | 13 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.086 | 0.075 | 0.077 | 9 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF2 | team_total | 0.878 | 0.870 | 0.872 | 88 | 14 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.170 | 0.165 | 0.166 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-3 | game_total | 0.969 | 0.975 | 0.974 | 99 | 4 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-9 | game_total | 0.240 | 0.235 | 0.236 | 24 | 77 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-5 | game_total | 0.780 | 0.790 | 0.788 | 80 | 22 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-3 | game_total | 0.978 | 0.975 | 0.976 | 99 | 4 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.854 | 0.855 | 0.855 | 86 | 15 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-5 | game_total | 0.771 | 0.775 | 0.774 | 78 | 23 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.589 | 0.524 | 0.171 | 0.213 | 6.71 | 6.53 | 0.998/1.051 | KXNHLGAME-26NOV04OTTBUF-OTT +0.065 |
| CHI @ FLA | 0.612 | 0.619 | 0.172 | 0.209 | 6.21 | 6.40 | 1.008/1.004 | KXNHLTOTAL-26NOV04CHIFLA-7 +0.038 |
| SJS @ LAK | 0.594 | 0.580 | 0.171 | 0.218 | 6.28 | 6.11 | 0.993/1.034 | KXNHLTOTAL-26NOV04SJLA-6 -0.033 |
| CGY @ SEA | 0.589 | 0.595 | 0.169 | 0.211 | 6.45 | 6.44 | 1.006/0.998 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Ridly Greig: 1+ goals YES @ 16c · p 0.207 (adj 0.1915) · $6.53 · thesis OTT:OFFENSE_4PLUS
- Artem Zub: 1+ goals YES @ 4c · p 0.0604 (adj 0.0528) · $2.22 · thesis OTT:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 17c · p 0.2027 (adj 0.1908) · $3.39 · thesis OTT:OFFENSE_4PLUS
- Thomas Chabot: 1+ assists NO @ 67c · p 0.7365 (adj 0.6983) · $13.81 · thesis OTT:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 20c · p 0.2834 (adj 0.2588) · $13.78 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1603 (adj 0.1452) · $7.01 · thesis CHI:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 61c · p 0.6891 (adj 0.6668) · $20.0 · thesis FLA:SUPPRESSED
- Wyatt Kaiser: 1+ goals YES @ 4c · p 0.0629 (adj 0.0572) · $3.28 · thesis CHI:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 154/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 27.17, exp saves 23.48 (sd 6.57), pull risk 0.066
- OTT net: Samuel Ersson (PROJECTED) exp shots 27.44, exp saves 23.5 (sd 6.63), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Benson: 2+ points | 0.241 | 0.155 | 23/92 | -0.002 | STANDARD |
| Thomas Chabot: 1+ assists | 0.264 | 0.340 | 35/67 | +0.051 | STANDARD |
| Thomas Chabot: 1+ points | 0.350 | 0.420 | 43/59 | +0.043 | STANDARD |
| Jake Sanderson: 1+ assists | 0.399 | 0.465 | 48/55 | +0.034 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.463 | 0.525 | 54/49 | +0.030 | STANDARD |
| Tage Thompson: 1+ assists | 0.363 | 0.425 | 44/59 | +0.030 | STANDARD |

**CHI @ FLA** · priced 156/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 23.85, exp saves 20.95 (sd 5.77), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 29.57, exp saves 25.09 (sd 7.1), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.351 | 0.470 | 49/55 | +0.081 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.363 | 0.475 | 49/54 | +0.079 | STANDARD |
| Sam Reinhart: 2+ points | 0.195 | 0.295 | 32/73 | +0.061 | STANDARD |
| Tyler Bertuzzi: 1+ goals | 0.283 | 0.185 | 20/83 | +0.072 | STANDARD |
| Brady Tkachuk: 1+ points | 0.576 | 0.670 | 68/34 | +0.069 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.514 | 0.425 | 44/59 | +0.057 | STANDARD |

**SJS @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.34, exp saves 23.04 (sd 6.17), pull risk 0.046
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.28, exp saves 25.13 (sd 6.83), pull risk 0.067

**CGY @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 28.65, exp saves 25.17 (sd 6.72), pull risk 0.052
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.22, exp saves 24.02 (sd 6.66), pull risk 0.077

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
