# NHL slate 2026-11-04 — RESEARCH_ONLY

generated 2026-11-05T00:12:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2929 · contracts joined: 953 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 853, 'OK': 54, 'NO_EDGE': 46}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 162, 'game_early_goal': 4, 'first_goal': 136, 'game_winner': 8, 'player_goals': 236, 'game_overtime': 4, 'player_points': 207, 'goalie_saves': 8, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 2026-11-05T00:30:00Z | T-10m | 0.607 | 0.393 | 0.166 | 6.81 | 3.77 | 3.04 | 257 (25/232) | CONFIRMED/CONFIRMED |
| CHI @ FLA | 2026-11-05T00:30:00Z | T-10m | 0.599 | 0.401 | 0.169 | 6.22 | 3.42 | 2.79 | 222 (25/197) | CONFIRMED/CONFIRMED |
| SJS @ LAK | 2026-11-05T03:00:00Z | T-90m | 0.591 | 0.409 | 0.170 | 6.36 | 3.49 | 2.87 | 248 (25/223) | PROBABLE/CONFIRMED |
| CGY @ SEA | 2026-11-05T03:00:00Z | T-90m | 0.591 | 0.409 | 0.168 | 6.51 | 3.55 | 2.96 | 226 (25/201) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV04CHIFLA-CHI | game_winner | 0.401 | 0.295 | 0.315 | 30 | 71 | yes | +0.087 | OK |
| KXNHLGAME-26NOV04CHIFLA-FLA | game_winner | 0.599 | 0.705 | 0.685 | 71 | 30 | no | +0.087 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA2 | game_spread | 0.377 | 0.475 | 0.455 | 48 | 53 | no | +0.076 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-FLA3 | game_spread | 0.243 | 0.335 | 0.315 | 34 | 67 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 | team_total | 0.457 | 0.545 | 0.527 | 55 | 46 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4 | team_total | 0.319 | 0.245 | 0.259 | 25 | 76 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI2 | team_total | 0.758 | 0.685 | 0.701 | 69 | 32 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI3 | team_total | 0.530 | 0.450 | 0.466 | 46 | 56 | yes | +0.052 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF2 | game_spread | 0.397 | 0.325 | 0.339 | 33 | 68 | yes | +0.051 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI2 | game_spread | 0.209 | 0.145 | 0.156 | 15 | 86 | yes | +0.050 | OK |
| KXNHLGAME-26NOV04OTTBUF-BUF | game_winner | 0.607 | 0.535 | 0.550 | 54 | 47 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI5 | team_total | 0.160 | 0.100 | 0.110 | 11 | 91 | yes | +0.043 | OK |
| KXNHLGAME-26NOV04OTTBUF-OTT | game_winner | 0.393 | 0.455 | 0.442 | 46 | 55 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT2 | game_spread | 0.208 | 0.265 | 0.253 | 27 | 74 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF5 | team_total | 0.332 | 0.270 | 0.282 | 28 | 74 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA3 | team_total | 0.672 | 0.730 | 0.719 | 74 | 28 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA5 | team_total | 0.263 | 0.320 | 0.308 | 33 | 69 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA2 | team_total | 0.852 | 0.900 | 0.892 | 91 | 11 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV04CHIFLA-CHI3 | game_spread | 0.115 | 0.075 | 0.082 | 8 | 93 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF6 | team_total | 0.177 | 0.130 | 0.138 | 14 | 88 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-BUF3 | game_spread | 0.269 | 0.225 | 0.233 | 23 | 78 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF3 | team_total | 0.731 | 0.685 | 0.694 | 69 | 32 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI6 | team_total | 0.067 | 0.030 | 0.035 | 4 | 98 | yes | +0.024 | OK |
| KXNHLGAME-26NOV04CGYSEA-CGY | game_winner | 0.409 | 0.455 | 0.446 | 46 | 55 | no | +0.024 | OK |
| KXNHLGAME-26NOV04CGYSEA-SEA | game_winner | 0.591 | 0.545 | 0.554 | 55 | 46 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-10 | game_total | 0.108 | 0.075 | 0.081 | 8 | 93 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-8 | game_total | 0.307 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF4 | team_total | 0.530 | 0.480 | 0.490 | 49 | 53 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV04OTTBUF-OTT3 | game_spread | 0.119 | 0.160 | 0.151 | 17 | 85 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA6 | team_total | 0.149 | 0.115 | 0.121 | 12 | 89 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA5 | team_total | 0.294 | 0.255 | 0.262 | 26 | 75 | yes | +0.020 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA2 | game_spread | 0.373 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT3 | team_total | 0.586 | 0.625 | 0.617 | 63 | 38 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY3 | game_spread | 0.126 | 0.155 | 0.149 | 16 | 85 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT4 | team_total | 0.371 | 0.405 | 0.398 | 41 | 60 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-7 | game_total | 0.499 | 0.465 | 0.472 | 47 | 54 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV04SJLA-10 | game_total | 0.097 | 0.075 | 0.079 | 8 | 93 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-9 | game_total | 0.223 | 0.190 | 0.196 | 20 | 82 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT2 | team_total | 0.799 | 0.835 | 0.828 | 85 | 18 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV04SJLA-8 | game_total | 0.283 | 0.255 | 0.260 | 26 | 75 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-9 | game_total | 0.252 | 0.225 | 0.230 | 23 | 78 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-CGY2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA4 | team_total | 0.485 | 0.455 | 0.461 | 46 | 55 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-9 | game_total | 0.186 | 0.165 | 0.169 | 17 | 84 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-10 | game_total | 0.131 | 0.115 | 0.118 | 12 | 89 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA6 | team_total | 0.128 | 0.150 | 0.145 | 16 | 86 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV04CGYSEA-6 | game_total | 0.610 | 0.585 | 0.590 | 59 | 42 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-10 | game_total | 0.087 | 0.075 | 0.077 | 8 | 93 | yes | +0.002 | OK |
| KXNHLSPREAD-26NOV04CGYSEA-SEA3 | game_spread | 0.244 | 0.225 | 0.229 | 23 | 78 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04SJLA-9 | game_total | 0.203 | 0.185 | 0.188 | 19 | 82 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-BUF2 | team_total | 0.889 | 0.870 | 0.874 | 88 | 14 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV04CHIFLA-8 | game_total | 0.264 | 0.245 | 0.249 | 25 | 76 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV04SJLA-3 | game_total | 0.967 | 0.980 | 0.978 | 99 | 3 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV04OTTBUF-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA3 | team_total | 0.694 | 0.675 | 0.679 | 68 | 33 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-SJ3 | game_spread | 0.114 | 0.125 | 0.123 | 13 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04OTTBUF-OTT5 | team_total | 0.200 | 0.225 | 0.220 | 24 | 79 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-4 | game_total | 0.854 | 0.865 | 0.863 | 87 | 14 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-3 | game_total | 0.979 | 0.970 | 0.972 | 98 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ6 | team_total | 0.071 | 0.065 | 0.066 | 7 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-CGY6 | team_total | 0.082 | 0.075 | 0.076 | 8 | 93 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-3 | game_total | 0.962 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04CGYSEA-SEA2 | team_total | 0.864 | 0.855 | 0.857 | 86 | 15 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA6 | team_total | 0.133 | 0.125 | 0.127 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-4 | game_total | 0.867 | 0.880 | 0.878 | 89 | 13 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA3 | game_spread | 0.242 | 0.255 | 0.252 | 26 | 75 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV04SJLA-7 | game_total | 0.472 | 0.455 | 0.458 | 46 | 55 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26NOV04SJLA-LA2 | game_spread | 0.371 | 0.385 | 0.382 | 39 | 62 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-LA | game_winner | 0.591 | 0.605 | 0.602 | 61 | 40 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV04SJLA-SJ | game_winner | 0.409 | 0.395 | 0.398 | 40 | 61 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-SJ5 | team_total | 0.172 | 0.165 | 0.166 | 17 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-5 | game_total | 0.839 | 0.845 | 0.844 | 85 | 16 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV04CHIFLA-7 | game_total | 0.449 | 0.435 | 0.438 | 44 | 57 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV04SJLA-LA2 | team_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04CGYSEA-4 | game_total | 0.878 | 0.875 | 0.876 | 88 | 13 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-8 | game_total | 0.346 | 0.330 | 0.333 | 34 | 68 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV04OTTBUF-6 | game_total | 0.655 | 0.645 | 0.647 | 65 | 36 |  | -0.010 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ BUF | 0.607 | 0.535 | 0.166 | 0.214 | 6.81 | 6.59 | 1.000/1.072 | KXNHLSPREAD-26NOV04OTTBUF-BUF2 -0.080 |
| CHI @ FLA | 0.599 | 0.612 | 0.169 | 0.213 | 6.22 | 6.37 | 1.015/0.988 | KXNHLTEAMTOTAL-26NOV04CHIFLA-FLA4 +0.035 |
| SJS @ LAK | 0.591 | 0.583 | 0.170 | 0.216 | 6.36 | 6.13 | 0.994/1.040 | KXNHLTOTAL-26NOV04SJLA-6 -0.041 |
| CGY @ SEA | 0.591 | 0.600 | 0.168 | 0.212 | 6.51 | 6.45 | 1.002/1.006 | KXNHLSPREAD-26NOV04CGYSEA-SEA3 +0.017 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Owen Power: 1+ goals NO @ 88c · p 0.9101 (adj 0.9013) · $19.36 · thesis BUF:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 15c · p 0.1827 (adj 0.1733) · $3.99 · thesis OTT:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 26c · p 0.3028 (adj 0.2908) · $5.88 · thesis BUF:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 17c · p 0.2064 (adj 0.1948) · $4.21 · thesis OTT:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 59c · p 0.6755 (adj 0.6529) · $19.31 · thesis FLA:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 10c · p 0.1461 (adj 0.1333) · $6.87 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.267 (adj 0.2515) · $9.76 · thesis CHI:OFFENSE_4PLUS
- Connor Bedard: 1+ assists NO @ 53c · p 0.6259 (adj 0.5603) · $12.46 · thesis CHI:SUPPRESSED
- Macklin Celebrini: 2+ assists NO @ 82c · p 0.9121 (adj 0.8636) · $14.52 · thesis SJS:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8522 (adj 0.8379) · $14.52 · thesis SJS:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2027 (adj 0.1933) · $3.58 · thesis SJS:OFFENSE_4PLUS
- Yaroslav Askarov: 28+ saves NO @ 57c · p 0.6463 (adj 0.6032) · $8.73 · thesis SJS:NET_LOW_VOLUME
- Ben Meyers: 1+ goals YES @ 11c · p 0.1696 (adj 0.1535) · $8.85 · thesis SEA:OFFENSE_4PLUS
- Jani Nyman: 1+ goals YES @ 11c · p 0.1615 (adj 0.1461) · $7.11 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.2288 (adj 0.2153) · $6.97 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 17c · p 0.2052 (adj 0.1939) · $3.88 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ BUF** · priced 202/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (CONFIRMED) exp shots 27.17, exp saves 23.52 (sd 6.51), pull risk 0.064
- OTT net: Samuel Ersson (CONFIRMED) exp shots 27.44, exp saves 23.49 (sd 6.64), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Beck Malenstyn: 1+ points | 0.233 | 0.095 | 18/99 | +0.042 | STANDARD |
| Ridly Greig: 1+ points | 0.416 | 0.320 | 35/71 | +0.051 | STANDARD |
| Beck Malenstyn: 1+ assists | 0.159 | 0.070 | 13/99 | +0.021 | STANDARD |
| Tim Stutzle: 1+ points | 0.627 | 0.715 | 72/29 | +0.069 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.431 | 0.350 | 37/67 | +0.045 | STANDARD |
| Sam Carrick: 1+ points | 0.186 | 0.105 | 20/99 | -0.025 | STANDARD |

**CHI @ FLA** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 23.85, exp saves 20.94 (sd 5.82), pull risk 0.051
- CHI net: Spencer Knight (CONFIRMED) exp shots 29.57, exp saves 25.22 (sd 7.01), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 2+ points | 0.187 | 0.315 | 32/69 | +0.108 | STANDARD |
| Sam Reinhart: 1+ assists | 0.343 | 0.465 | 47/54 | +0.100 | STANDARD |
| Brady Tkachuk: 1+ points | 0.564 | 0.680 | 69/33 | +0.091 | STANDARD |
| Brady Tkachuk: 2+ points | 0.209 | 0.320 | 33/69 | +0.086 | STANDARD |
| Sam Reinhart: 1+ points | 0.537 | 0.640 | 66/38 | +0.067 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.358 | 0.460 | 47/55 | +0.075 | STANDARD |

**SJS @ LAK** · priced 195/197 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.34, exp saves 23.08 (sd 6.18), pull risk 0.045
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 29.28, exp saves 25.09 (sd 6.78), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.390 | 0.550 | 57/47 | +0.123 | STANDARD |
| Artemi Panarin: 1+ assists | 0.446 | 0.600 | 61/41 | +0.127 | STANDARD |
| Macklin Celebrini: 2+ points | 0.227 | 0.355 | 37/66 | +0.097 | STANDARD |
| Artemi Panarin: 2+ points | 0.258 | 0.385 | 40/63 | +0.095 | STANDARD |
| Ivar Stenberg: 1+ points | 0.342 | 0.455 | 47/56 | +0.081 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.088 | 0.185 | 19/82 | +0.082 | STANDARD |

**CGY @ SEA** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.65, exp saves 25.21 (sd 6.68), pull risk 0.049
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.22, exp saves 23.9 (sd 6.7), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.296 | 0.205 | 22/81 | +0.064 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.430 | 0.340 | 37/69 | +0.044 | STANDARD |
| Ben Meyers: 1+ goals | 0.170 | 0.105 | 11/90 | +0.053 | STANDARD |
| Jani Nyman: 1+ goals | 0.162 | 0.100 | 11/91 | +0.045 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.341 | 0.285 | 29/72 | +0.036 | STANDARD |
| Berkly Catton: 1+ goals | 0.229 | 0.175 | 18/83 | +0.038 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
