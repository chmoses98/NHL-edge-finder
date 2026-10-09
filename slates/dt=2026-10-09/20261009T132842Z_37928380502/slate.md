# NHL slate 2026-10-09 — RESEARCH_ONLY

generated 2026-10-09T13:28:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3237 · contracts joined: 845 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 745, 'NO_EDGE': 71, 'OK': 29}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 108, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 250, 'game_overtime': 4, 'player_points': 141, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 2026-10-09T23:00:00Z | T-6h | 0.576 | 0.424 | 0.177 | 6.05 | 3.27 | 2.79 | 208 (25/183) | CONFIRMED/PROJECTED |
| NYR @ WSH | 2026-10-09T23:00:00Z | T-6h | 0.542 | 0.458 | 0.179 | 6.04 | 3.16 | 2.88 | 216 (25/191) | PROJECTED/PROJECTED |
| PIT @ CBJ | 2026-10-09T23:00:00Z | T-6h | 0.568 | 0.432 | 0.169 | 6.46 | 3.44 | 3.02 | 214 (25/189) | PROJECTED/PROJECTED |
| ANA @ WPG | 2026-10-10T00:00:00Z | T-6h | 0.542 | 0.458 | 0.176 | 6.22 | 3.24 | 2.98 | 207 (25/182) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT09PITCBJ-CBJ2 | game_spread | 0.347 | 0.305 | 0.313 | 31 | 70 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT2 | game_spread | 0.235 | 0.275 | 0.267 | 28 | 73 | no | +0.021 | OK |
| KXNHLGAME-26OCT09PITCBJ-CBJ | game_winner | 0.568 | 0.525 | 0.534 | 53 | 48 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 | team_total | 0.365 | 0.405 | 0.397 | 41 | 60 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT09SEADET-5 | game_total | 0.751 | 0.785 | 0.779 | 79 | 22 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-5 | game_total | 0.776 | 0.805 | 0.800 | 81 | 20 | no | +0.012 | OK |
| KXNHLGAME-26OCT09PITCBJ-PIT | game_winner | 0.432 | 0.465 | 0.458 | 47 | 54 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT09SEADET-SEA3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT09SEADET-4 | game_total | 0.842 | 0.865 | 0.861 | 87 | 14 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ3 | team_total | 0.674 | 0.645 | 0.651 | 65 | 36 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT2 | team_total | 0.793 | 0.820 | 0.815 | 83 | 19 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-4 | game_total | 0.856 | 0.875 | 0.871 | 88 | 13 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT09NYRWSH-WSH3 | game_spread | 0.194 | 0.215 | 0.211 | 22 | 79 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ4 | team_total | 0.462 | 0.430 | 0.436 | 44 | 58 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA3 | game_spread | 0.146 | 0.165 | 0.161 | 17 | 84 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA5 | team_total | 0.184 | 0.210 | 0.205 | 22 | 80 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-3 | game_total | 0.964 | 0.975 | 0.973 | 98 | 3 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-7 | game_total | 0.449 | 0.475 | 0.470 | 48 | 53 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ6 | team_total | 0.131 | 0.110 | 0.114 | 12 | 90 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ2 | team_total | 0.853 | 0.835 | 0.839 | 84 | 17 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 | team_total | 0.360 | 0.395 | 0.388 | 41 | 62 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA2 | game_spread | 0.254 | 0.275 | 0.271 | 28 | 73 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT3 | team_total | 0.581 | 0.615 | 0.608 | 63 | 40 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR4 | team_total | 0.337 | 0.315 | 0.319 | 32 | 69 | yes | +0.002 | OK |
| KXNHLGAME-26OCT09NYRWSH-NYR | game_winner | 0.458 | 0.435 | 0.440 | 44 | 57 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT09SEADET-7 | game_total | 0.422 | 0.445 | 0.440 | 45 | 56 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT09SEADET-DET3 | game_spread | 0.217 | 0.235 | 0.231 | 24 | 77 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-6 | game_total | 0.563 | 0.585 | 0.581 | 59 | 42 | no | +0.000 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ3 | game_spread | 0.222 | 0.205 | 0.208 | 21 | 80 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA2 | team_total | 0.758 | 0.780 | 0.776 | 79 | 23 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-5 | game_total | 0.800 | 0.815 | 0.812 | 82 | 19 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 | team_total | 0.316 | 0.335 | 0.331 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR5 | team_total | 0.168 | 0.155 | 0.158 | 16 | 85 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-3 | game_total | 0.959 | 0.970 | 0.968 | 98 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-7 | game_total | 0.425 | 0.405 | 0.409 | 41 | 60 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-SEA2 | game_spread | 0.220 | 0.235 | 0.232 | 24 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT5 | team_total | 0.191 | 0.210 | 0.206 | 22 | 80 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-10 | game_total | 0.087 | 0.095 | 0.093 | 10 | 91 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA2 | team_total | 0.792 | 0.815 | 0.811 | 83 | 20 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR3 | team_total | 0.554 | 0.530 | 0.535 | 54 | 48 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-6 | game_total | 0.536 | 0.555 | 0.551 | 56 | 45 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA5 | team_total | 0.154 | 0.165 | 0.163 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-4 | game_total | 0.877 | 0.885 | 0.883 | 89 | 12 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 | team_total | 0.578 | 0.600 | 0.596 | 61 | 41 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ5 | team_total | 0.269 | 0.245 | 0.250 | 26 | 77 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR6 | team_total | 0.070 | 0.060 | 0.062 | 7 | 95 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-WPG | game_winner | 0.542 | 0.525 | 0.528 | 53 | 48 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA6 | team_total | 0.081 | 0.095 | 0.092 | 11 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-8 | game_total | 0.263 | 0.275 | 0.272 | 28 | 73 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-9 | game_total | 0.163 | 0.150 | 0.153 | 16 | 86 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-9 | game_total | 0.167 | 0.175 | 0.173 | 18 | 83 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG2 | game_spread | 0.317 | 0.305 | 0.307 | 31 | 70 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH2 | team_total | 0.818 | 0.830 | 0.828 | 84 | 18 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG3 | game_spread | 0.197 | 0.205 | 0.203 | 21 | 80 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET6 | team_total | 0.108 | 0.100 | 0.102 | 11 | 91 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-4 | game_total | 0.840 | 0.845 | 0.844 | 85 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR2 | team_total | 0.783 | 0.770 | 0.773 | 78 | 24 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET2 | team_total | 0.829 | 0.845 | 0.842 | 86 | 17 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT09NYRWSH-WSH | game_winner | 0.542 | 0.555 | 0.552 | 56 | 45 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR2 | game_spread | 0.243 | 0.235 | 0.237 | 24 | 77 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-10 | game_total | 0.075 | 0.075 | 0.075 | 8 | 93 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-9 | game_total | 0.211 | 0.200 | 0.202 | 21 | 81 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-8 | game_total | 0.294 | 0.285 | 0.287 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-10 | game_total | 0.106 | 0.095 | 0.097 | 11 | 92 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-6 | game_total | 0.536 | 0.525 | 0.527 | 53 | 48 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA3 | team_total | 0.534 | 0.545 | 0.543 | 55 | 46 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-10 | game_total | 0.073 | 0.070 | 0.071 | 8 | 94 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR3 | game_spread | 0.137 | 0.135 | 0.135 | 14 | 87 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT6 | team_total | 0.088 | 0.095 | 0.093 | 11 | 92 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-9 | game_total | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-WSH2 | game_spread | 0.318 | 0.325 | 0.324 | 33 | 68 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET4 | team_total | 0.426 | 0.440 | 0.437 | 45 | 57 |  | -0.014 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 0.576 | 0.530 | 0.177 | 0.223 | 6.05 | 6.19 | 0.994/1.005 | KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 +0.050 |
| NYR @ WSH | 0.542 | 0.539 | 0.179 | 0.220 | 6.04 | 6.28 | 0.960/0.957 | KXNHLTOTAL-26OCT09NYRWSH-7 +0.039 |
| PIT @ CBJ | 0.568 | 0.554 | 0.169 | 0.220 | 6.46 | 6.50 | 0.964/1.033 | KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 +0.018 |
| ANA @ WPG | 0.542 | 0.517 | 0.176 | 0.216 | 6.22 | 6.40 | 0.988/1.024 | KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 +0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 19c · p 0.248 (adj 0.2298) · $8.81 · thesis WSH:OFFENSE_4PLUS
- Alex Tuch: 1+ assists NO @ 69c · p 0.7702 (adj 0.7251) · $20.0 · thesis WSH:SUPPRESSED
- Boone Jenner: 1+ goals YES @ 14c · p 0.1689 (adj 0.1592) · $3.14 · thesis WSH:OFFENSE_4PLUS
- Valeri Nichushkin: 1+ assists NO @ 71c · p 0.7933 (adj 0.7467) · $18.26 · thesis CBJ:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 11c · p 0.1443 (adj 0.132) · $4.11 · thesis CBJ:OFFENSE_4PLUS
- Matthew Knies: 1+ assists NO @ 65c · p 0.7242 (adj 0.6821) · $11.74 · thesis CBJ:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2085 (adj 0.1926) · $3.87 · thesis CBJ:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 88c · p 0.9276 (adj 0.912) · $20.0 · thesis WPG:SUPPRESSED
- Morgan Barron: 1+ goals YES @ 13c · p 0.1576 (adj 0.1482) · $2.93 · thesis WPG:OFFENSE_4PLUS
- Cutter Gauthier: 1+ goals NO @ 60c · p 0.6434 (adj 0.63) · $8.76 · thesis ANA:SUPPRESSED
- Neal Pionk: 1+ assists NO @ 57c · p 0.6779 (adj 0.598) · $7.82 · thesis WPG:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ DET** · priced 150/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.67, exp saves 22.38 (sd 6.24), pull risk 0.058
- SEA net: Joey Daccord (PROJECTED) exp shots 29.51, exp saves 25.45 (sd 6.84), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex DeBrincat: 2+ points | 0.294 | 0.175 | 32/97 | -0.041 | STANDARD |
| Lucas Raymond: 2+ points | 0.268 | 0.155 | 28/97 | -0.026 | STANDARD |
| Emmitt Finnie: 1+ points | 0.461 | 0.350 | 37/67 | +0.074 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.325 | 0.215 | 24/81 | +0.072 | STANDARD |
| Matty Beniers: 1+ goals | 0.229 | 0.120 | 22/98 | -0.003 | STANDARD |
| Andrew Copp: 1+ points | 0.479 | 0.375 | 39/64 | +0.072 | STANDARD |

**NYR @ WSH** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.25, exp saves 22.05 (sd 6.14), pull risk 0.053
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.39, exp saves 23.51 (sd 6.58), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Will Cuylle: 1+ points | 0.384 | 0.195 | 37/98 | -0.003 | STANDARD |
| Gabe Perreault: 1+ assists | 0.312 | 0.135 | 25/98 | +0.049 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.163 | 0.280 | 30/74 | +0.084 | STANDARD |
| Will Cuylle: 1+ assists | 0.234 | 0.120 | 23/99 | -0.009 | STANDARD |
| Alexis Lafreniere: 2+ points | 0.199 | 0.095 | 17/98 | +0.020 | STANDARD |
| Mika Zibanejad: 2+ points | 0.217 | 0.125 | 22/97 | -0.015 | STANDARD |

**PIT @ CBJ** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.49, exp saves 23.83 (sd 6.56), pull risk 0.063
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.56, exp saves 23.47 (sd 6.63), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Werenski: 2+ points | 0.283 | 0.170 | 30/96 | -0.032 | STANDARD |
| Charlie Coyle: 2+ points | 0.202 | 0.100 | 18/98 | +0.011 | STANDARD |
| Sean Monahan: 1+ goals | 0.243 | 0.145 | 22/93 | +0.011 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.207 | 0.300 | 31/71 | +0.069 | STANDARD |
| Sidney Crosby: 1+ assists | 0.395 | 0.480 | 49/53 | +0.058 | STANDARD |
| Matthew Knies: 1+ assists | 0.276 | 0.360 | 37/65 | +0.058 | STANDARD |

**ANA @ WPG** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 29.53, exp saves 25.59 (sd 6.93), pull risk 0.066
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.65, exp saves 23.04 (sd 6.33), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Connor: 1+ points | 0.676 | 0.395 | 71/92 | -0.048 | STANDARD |
| Neal Pionk: 1+ points | 0.372 | 0.520 | 54/50 | +0.110 | STANDARD |
| Mark Scheifele: 2+ points | 0.319 | 0.180 | 34/98 | -0.037 | STANDARD |
| Neal Pionk: 1+ assists | 0.322 | 0.445 | 46/57 | +0.091 | STANDARD |
| A.J. Greer: 1+ goals | 0.222 | 0.100 | 18/98 | +0.032 | STANDARD |
| Gabriel Vilardi: 2+ points | 0.231 | 0.115 | 21/98 | +0.009 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
