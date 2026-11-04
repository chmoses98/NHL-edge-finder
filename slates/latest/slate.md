# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-04T06:22:31Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2141 · contracts joined: 204 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 104, 'OK': 39, 'NO_EDGE': 61}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'game_early_goal': 4, 'game_winner': 8, 'game_overtime': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-12h | 0.583 | 0.417 | 0.167 | 6.64 | 3.59 | 3.06 | 51 (25/26) | PROJECTED/PROJECTED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-12h | 0.614 | 0.386 | 0.170 | 6.20 | 3.46 | 2.74 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-12h | 0.594 | 0.406 | 0.168 | 6.27 | 3.43 | 2.84 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-12h | 0.610 | 0.390 | 0.168 | 6.31 | 3.51 | 2.80 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.614 | 0.705 | 0.688 | 71 | 30 | no | +0.072 | OK |
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.386 | 0.305 | 0.321 | 31 | 70 | yes | +0.061 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.387 | 0.470 | 0.453 | 48 | 54 | no | +0.055 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4 | team_total | 0.306 | 0.245 | 0.256 | 25 | 76 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI2 | game_spread | 0.197 | 0.145 | 0.154 | 15 | 86 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5 | team_total | 0.149 | 0.105 | 0.113 | 11 | 90 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.518 | 0.465 | 0.475 | 47 | 54 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.061 | 0.025 | 0.030 | 3 | 98 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY2 | team_total | 0.761 | 0.805 | 0.797 | 81 | 20 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA3 | team_total | 0.680 | 0.730 | 0.720 | 74 | 28 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA5 | team_total | 0.269 | 0.315 | 0.305 | 32 | 69 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 | team_total | 0.467 | 0.525 | 0.513 | 54 | 49 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.387 | 0.345 | 0.353 | 35 | 66 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.111 | 0.145 | 0.137 | 15 | 86 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.199 | 0.235 | 0.228 | 24 | 77 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.858 | 0.890 | 0.884 | 90 | 12 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.141 | 0.115 | 0.120 | 12 | 89 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.109 | 0.085 | 0.089 | 9 | 92 | yes | +0.013 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.390 | 0.430 | 0.422 | 44 | 58 | no | +0.013 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.610 | 0.570 | 0.578 | 58 | 44 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT2 | game_spread | 0.224 | 0.255 | 0.249 | 26 | 75 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.254 | 0.225 | 0.231 | 23 | 78 | yes | +0.012 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF2 | game_spread | 0.367 | 0.335 | 0.341 | 34 | 67 | yes | +0.011 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.130 | 0.155 | 0.150 | 16 | 85 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.282 | 0.250 | 0.256 | 26 | 76 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.801 | 0.830 | 0.824 | 84 | 18 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.067 | 0.085 | 0.081 | 9 | 92 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.133 | 0.155 | 0.150 | 16 | 85 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.201 | 0.225 | 0.220 | 23 | 78 | no | +0.007 | OK |
| KXNHLGAME-26NOV04OTTBUF-OTT | game_winner | 0.417 | 0.445 | 0.439 | 45 | 56 | no | +0.006 | OK |
| KXNHLGAME-26NOV04OTTBUF-BUF | game_winner | 0.583 | 0.555 | 0.561 | 56 | 45 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2 | team_total | 0.750 | 0.725 | 0.730 | 73 | 28 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.153 | 0.135 | 0.139 | 14 | 87 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-4 | game_total | 0.890 | 0.910 | 0.906 | 92 | 10 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.689 | 0.655 | 0.662 | 67 | 36 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY3 | team_total | 0.530 | 0.565 | 0.558 | 58 | 45 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT6 | team_total | 0.091 | 0.105 | 0.102 | 11 | 90 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.469 | 0.445 | 0.450 | 45 | 56 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY5 | team_total | 0.161 | 0.185 | 0.180 | 20 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.476 | 0.450 | 0.455 | 46 | 56 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.374 | 0.400 | 0.395 | 41 | 61 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.280 | 0.260 | 0.264 | 27 | 75 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-3 | game_total | 0.972 | 0.980 | 0.979 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.238 | 0.220 | 0.224 | 23 | 79 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.196 | 0.180 | 0.183 | 19 | 83 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.070 | 0.065 | 0.066 | 7 | 94 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY4 | team_total | 0.320 | 0.345 | 0.340 | 36 | 67 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.184 | 0.170 | 0.173 | 18 | 84 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ2 | team_total | 0.764 | 0.780 | 0.777 | 79 | 23 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.861 | 0.850 | 0.852 | 86 | 16 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-3 | game_total | 0.964 | 0.975 | 0.973 | 99 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.591 | 0.615 | 0.610 | 63 | 40 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-3 | game_total | 0.965 | 0.975 | 0.973 | 99 | 4 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.578 | 0.565 | 0.568 | 57 | 44 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-5 | game_total | 0.821 | 0.815 | 0.816 | 82 | 19 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.086 | 0.085 | 0.085 | 9 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.967 | 0.975 | 0.974 | 99 | 4 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.851 | 0.855 | 0.854 | 86 | 15 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.862 | 0.870 | 0.868 | 88 | 14 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.169 | 0.160 | 0.162 | 17 | 85 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.294 | 0.285 | 0.287 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.127 | 0.125 | 0.125 | 13 | 88 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.262 | 0.250 | 0.252 | 26 | 76 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-4 | game_total | 0.853 | 0.860 | 0.859 | 87 | 15 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-5 | game_total | 0.780 | 0.785 | 0.784 | 79 | 22 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.125 | 0.130 | 0.129 | 14 | 88 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.084 | 0.070 | 0.073 | 9 | 95 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.094 | 0.090 | 0.091 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.445 | 0.435 | 0.437 | 44 | 57 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.240 | 0.250 | 0.248 | 26 | 76 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-LA | game_winner | 0.594 | 0.585 | 0.587 | 59 | 42 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-SJ | game_winner | 0.406 | 0.415 | 0.413 | 42 | 59 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-6 | game_total | 0.627 | 0.635 | 0.633 | 64 | 37 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ2 | game_spread | 0.219 | 0.215 | 0.216 | 22 | 79 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.583 | 0.527 | 0.167 | 0.214 | 6.64 | 6.47 | 0.998/1.034 | KXNHLSPREAD-26NOV04OTTBUF-BUF2 -0.062 |
| CHI @ FLA | 0.614 | 0.623 | 0.170 | 0.212 | 6.20 | 6.39 | 1.008/1.004 | KXNHLTOTAL-26NOV04CHIFLA-7 +0.040 |
| SJS @ LAK | 0.594 | 0.582 | 0.168 | 0.218 | 6.27 | 6.09 | 0.993/1.034 | KXNHLTOTAL-26NOV04SJLA-6 -0.035 |
| CGY @ SEA | 0.610 | 0.591 | 0.168 | 0.212 | 6.31 | 6.45 | 1.016/0.998 | KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY3 +0.036 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 2 recommended · full analysis in card.md / packet.json `thesis_card`

- Chicago over 4.5 goals scored YES @ 11c · p 0.1585 (adj 0.1318) · $2.39 · thesis CHI:OFFENSE_4PLUS
- Chicago over 3.5 goals scored YES @ 25c · p 0.3179 (adj 0.2814) · $3.17 · thesis CHI:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 27.17, exp saves 23.48 (sd 6.58), pull risk 0.065
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.44, exp saves 23.57 (sd 6.59), pull risk 0.071

**CHI @ FLA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 23.85, exp saves 20.94 (sd 5.84), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 29.57, exp saves 25.08 (sd 7.02), pull risk 0.086

**SJS @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.34, exp saves 23.06 (sd 6.19), pull risk 0.046
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 29.28, exp saves 25.11 (sd 6.87), pull risk 0.069

**CGY @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.65, exp saves 25.17 (sd 6.77), pull risk 0.052
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.22, exp saves 23.96 (sd 6.76), pull risk 0.083

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
