# NHL slate 2026-10-09 — RESEARCH_ONLY

generated 2026-10-09T15:28:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3237 · contracts joined: 845 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 745, 'NO_EDGE': 67, 'OK': 33}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 108, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 250, 'game_overtime': 4, 'player_points': 141, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 2026-10-09T23:00:00Z | T-6h | 0.576 | 0.424 | 0.177 | 6.05 | 3.27 | 2.79 | 208 (25/183) | CONFIRMED/PROJECTED |
| NYR @ WSH | 2026-10-09T23:00:00Z | T-6h | 0.565 | 0.435 | 0.182 | 5.93 | 3.17 | 2.77 | 216 (25/191) | CONFIRMED/PROJECTED |
| PIT @ CBJ | 2026-10-09T23:00:00Z | T-6h | 0.494 | 0.506 | 0.166 | 6.89 | 3.43 | 3.46 | 214 (25/189) | CONFIRMED/PROJECTED |
| ANA @ WPG | 2026-10-10T00:00:00Z | T-6h | 0.542 | 0.458 | 0.176 | 6.22 | 3.24 | 2.98 | 207 (25/182) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT09PITCBJ-8 | game_total | 0.358 | 0.285 | 0.299 | 29 | 72 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-9 | game_total | 0.267 | 0.210 | 0.221 | 22 | 80 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-6 | game_total | 0.665 | 0.615 | 0.625 | 62 | 39 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 | team_total | 0.465 | 0.415 | 0.425 | 42 | 59 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT3 | team_total | 0.671 | 0.625 | 0.634 | 63 | 38 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-10 | game_total | 0.141 | 0.100 | 0.107 | 11 | 91 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT5 | team_total | 0.276 | 0.230 | 0.239 | 24 | 78 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT6 | team_total | 0.136 | 0.100 | 0.106 | 11 | 91 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-7 | game_total | 0.555 | 0.510 | 0.519 | 52 | 50 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT09SEADET-5 | game_total | 0.751 | 0.785 | 0.779 | 79 | 22 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-5 | game_total | 0.776 | 0.805 | 0.800 | 81 | 20 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT09SEADET-SEA3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT09SEADET-4 | game_total | 0.842 | 0.865 | 0.861 | 87 | 14 | no | +0.009 | OK |
| KXNHLGAME-26OCT09PITCBJ-CBJ | game_winner | 0.494 | 0.525 | 0.519 | 53 | 48 | no | +0.009 | OK |
| KXNHLGAME-26OCT09PITCBJ-PIT | game_winner | 0.506 | 0.475 | 0.481 | 48 | 53 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA2 | team_total | 0.792 | 0.820 | 0.815 | 83 | 19 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT2 | game_spread | 0.301 | 0.275 | 0.280 | 28 | 73 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-4 | game_total | 0.856 | 0.875 | 0.871 | 88 | 13 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT09NYRWSH-WSH3 | game_spread | 0.202 | 0.225 | 0.220 | 23 | 78 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-5 | game_total | 0.845 | 0.825 | 0.829 | 83 | 18 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA3 | game_spread | 0.146 | 0.165 | 0.161 | 17 | 84 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA5 | team_total | 0.184 | 0.210 | 0.205 | 22 | 80 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-3 | game_total | 0.964 | 0.975 | 0.973 | 98 | 3 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT2 | team_total | 0.853 | 0.830 | 0.835 | 84 | 18 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-7 | game_total | 0.449 | 0.475 | 0.470 | 48 | 53 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ4 | team_total | 0.461 | 0.435 | 0.440 | 44 | 57 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 | team_total | 0.360 | 0.385 | 0.380 | 39 | 62 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-3 | game_total | 0.954 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA2 | game_spread | 0.254 | 0.275 | 0.271 | 28 | 73 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ3 | game_spread | 0.187 | 0.205 | 0.201 | 21 | 80 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-2 | game_total | 0.993 | 0.985 | 0.987 | 99 | 2 | yes | +0.002 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ2 | game_spread | 0.293 | 0.315 | 0.311 | 32 | 69 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-6 | game_total | 0.563 | 0.585 | 0.581 | 59 | 42 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA2 | team_total | 0.758 | 0.780 | 0.776 | 79 | 23 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-4 | game_total | 0.906 | 0.895 | 0.897 | 90 | 11 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-3 | game_total | 0.981 | 0.975 | 0.976 | 98 | 3 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR3 | game_spread | 0.123 | 0.135 | 0.132 | 14 | 87 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-4 | game_total | 0.832 | 0.845 | 0.842 | 85 | 16 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT09PITCBJ-PIT3 | game_spread | 0.189 | 0.175 | 0.178 | 18 | 83 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-SEA2 | game_spread | 0.220 | 0.235 | 0.232 | 24 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-10 | game_total | 0.087 | 0.095 | 0.093 | 10 | 91 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-5 | game_total | 0.740 | 0.755 | 0.752 | 76 | 25 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-6 | game_total | 0.536 | 0.555 | 0.551 | 56 | 45 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ6 | team_total | 0.134 | 0.120 | 0.123 | 13 | 89 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA5 | team_total | 0.154 | 0.165 | 0.163 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 | team_total | 0.578 | 0.600 | 0.596 | 61 | 41 |  | -0.004 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-WPG | game_winner | 0.542 | 0.525 | 0.528 | 53 | 48 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ5 | team_total | 0.268 | 0.250 | 0.253 | 26 | 76 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA6 | team_total | 0.081 | 0.090 | 0.088 | 10 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-8 | game_total | 0.263 | 0.275 | 0.272 | 28 | 73 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-9 | game_total | 0.167 | 0.175 | 0.173 | 18 | 83 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-WSH2 | game_spread | 0.331 | 0.345 | 0.342 | 35 | 66 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG3 | game_spread | 0.197 | 0.205 | 0.203 | 21 | 80 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET6 | team_total | 0.108 | 0.100 | 0.102 | 11 | 91 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET2 | team_total | 0.829 | 0.845 | 0.842 | 86 | 17 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-DET3 | game_spread | 0.217 | 0.225 | 0.223 | 23 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-7 | game_total | 0.422 | 0.435 | 0.432 | 44 | 57 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH4 | team_total | 0.403 | 0.415 | 0.413 | 42 | 59 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-10 | game_total | 0.075 | 0.075 | 0.075 | 8 | 93 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-10 | game_total | 0.066 | 0.070 | 0.069 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH2 | team_total | 0.820 | 0.830 | 0.828 | 84 | 18 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR2 | game_spread | 0.228 | 0.235 | 0.234 | 24 | 77 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 | team_total | 0.316 | 0.330 | 0.327 | 34 | 68 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ3 | team_total | 0.665 | 0.650 | 0.653 | 66 | 36 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ2 | team_total | 0.848 | 0.840 | 0.842 | 85 | 17 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA3 | team_total | 0.534 | 0.550 | 0.547 | 56 | 46 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26OCT09NYRWSH-WSH | game_winner | 0.565 | 0.575 | 0.573 | 58 | 43 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-9 | game_total | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR4 | team_total | 0.308 | 0.315 | 0.314 | 32 | 69 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR6 | team_total | 0.061 | 0.060 | 0.060 | 7 | 95 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-6 | game_total | 0.516 | 0.525 | 0.523 | 53 | 48 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET5 | team_total | 0.239 | 0.235 | 0.236 | 24 | 77 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-8 | game_total | 0.242 | 0.245 | 0.244 | 25 | 76 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-8 | game_total | 0.223 | 0.230 | 0.229 | 24 | 78 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET3 | team_total | 0.639 | 0.645 | 0.644 | 65 | 36 |  | -0.015 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 0.576 | 0.530 | 0.177 | 0.223 | 6.05 | 6.19 | 0.994/1.005 | KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 +0.050 |
| NYR @ WSH | 0.565 | 0.548 | 0.182 | 0.216 | 5.93 | 6.20 | 0.937/0.957 | KXNHLTOTAL-26OCT09NYRWSH-7 +0.049 |
| PIT @ CBJ | 0.494 | 0.535 | 0.166 | 0.217 | 6.89 | 6.61 | 1.007/1.033 | KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 -0.058 |
| ANA @ WPG | 0.542 | 0.517 | 0.176 | 0.216 | 6.22 | 6.40 | 0.988/1.024 | KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 +0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Winterton: 1+ goals YES @ 10c · p 0.1406 (adj 0.1255) · $4.69 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 9c · p 0.1203 (adj 0.1077) · $2.94 · thesis SEA:OFFENSE_4PLUS
- Michael Rasmussen: 1+ goals YES @ 11c · p 0.1444 (adj 0.1295) · $3.24 · thesis DET:OFFENSE_4PLUS
- Kaapo Kakko: 1+ assists YES @ 29c · p 0.3489 (adj 0.3145) · $2.89 · thesis SEA:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2514 (adj 0.2298) · $14.07 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 13c · p 0.1733 (adj 0.16) · $6.12 · thesis WSH:OFFENSE_4PLUS
- Alex Tuch: 1+ assists NO @ 69c · p 0.7761 (adj 0.728) · $20.0 · thesis WSH:SUPPRESSED
- J.T. Miller: 1+ assists NO @ 60c · p 0.6598 (adj 0.6274) · $5.92 · thesis NYR:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 10c · p 0.1409 (adj 0.1282) · $5.64 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2069 (adj 0.1939) · $7.02 · thesis CBJ:OFFENSE_4PLUS
- Valeri Nichushkin: 1+ assists NO @ 70c · p 0.7878 (adj 0.7414) · $17.13 · thesis CBJ:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 64c · p 0.7208 (adj 0.6754) · $12.87 · thesis CBJ:SUPPRESSED
- Neal Pionk: 1+ goals NO @ 88c · p 0.9276 (adj 0.912) · $17.79 · thesis WPG:SUPPRESSED
- Judd Caulfield: 1+ goals YES @ 7c · p 0.1045 (adj 0.0921) · $4.16 · thesis ANA:OFFENSE_4PLUS
- Morgan Barron: 1+ goals YES @ 12c · p 0.1576 (adj 0.1469) · $5.44 · thesis WPG:OFFENSE_4PLUS
- Neal Pionk: 1+ assists NO @ 56c · p 0.6779 (adj 0.598) · $12.21 · thesis WPG:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ DET** · priced 150/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.67, exp saves 22.38 (sd 6.24), pull risk 0.058
- SEA net: Joey Daccord (PROJECTED) exp shots 29.51, exp saves 25.45 (sd 6.84), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Emmitt Finnie: 1+ points | 0.461 | 0.355 | 37/66 | +0.074 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.325 | 0.225 | 25/80 | +0.062 | STANDARD |
| Andrew Copp: 1+ points | 0.479 | 0.380 | 39/63 | +0.072 | STANDARD |
| Andrew Copp: 1+ assists | 0.341 | 0.260 | 28/76 | +0.046 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.140 | 0.220 | 24/80 | +0.049 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.299 | 0.375 | 39/64 | +0.044 | STANDARD |

**NYR @ WSH** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 25.25, exp saves 22.04 (sd 6.12), pull risk 0.054
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.39, exp saves 23.49 (sd 6.57), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gabe Perreault: 1+ assists | 0.294 | 0.140 | 25/97 | +0.031 | STANDARD |
| Will Cuylle: 1+ assists | 0.226 | 0.115 | 22/99 | -0.007 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.174 | 0.275 | 29/74 | +0.072 | STANDARD |
| Alex Tuch: 1+ assists | 0.224 | 0.320 | 33/69 | +0.071 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.251 | 0.165 | 17/84 | +0.072 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.206 | 0.280 | 29/73 | +0.050 | STANDARD |

**PIT @ CBJ** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.49, exp saves 23.75 (sd 6.57), pull risk 0.064
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.56, exp saves 23.55 (sd 6.6), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 2+ points | 0.200 | 0.105 | 17/96 | +0.020 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.212 | 0.305 | 31/70 | +0.073 | STANDARD |
| Matthew Knies: 1+ assists | 0.279 | 0.370 | 38/64 | +0.065 | STANDARD |
| Sidney Crosby: 1+ assists | 0.400 | 0.480 | 49/53 | +0.053 | STANDARD |
| Matthew Knies: 1+ points | 0.492 | 0.570 | 58/44 | +0.050 | STANDARD |
| Sidney Crosby: 1+ points | 0.566 | 0.635 | 64/37 | +0.047 | STANDARD |

**ANA @ WPG** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 29.53, exp saves 25.59 (sd 6.93), pull risk 0.066
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.65, exp saves 23.04 (sd 6.33), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Neal Pionk: 1+ assists | 0.322 | 0.445 | 45/56 | +0.101 | STANDARD |
| Neal Pionk: 1+ points | 0.372 | 0.495 | 50/51 | +0.100 | STANDARD |
| A.J. Greer: 1+ goals | 0.222 | 0.105 | 17/96 | +0.043 | STANDARD |
| Gabriel Vilardi: 2+ points | 0.231 | 0.140 | 21/93 | +0.009 | STANDARD |
| Alex Iafallo: 1+ goals | 0.193 | 0.110 | 17/95 | +0.013 | STANDARD |
| Cole Perfetti: 1+ assists | 0.432 | 0.360 | 37/65 | +0.046 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
