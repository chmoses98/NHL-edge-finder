# NHL slate 2026-10-09 — RESEARCH_ONLY

generated 2026-10-09T16:28:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3241 · contracts joined: 849 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 749, 'NO_EDGE': 54, 'OK': 46}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 108, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 250, 'game_overtime': 4, 'player_points': 141, 'goalie_saves': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 2026-10-09T23:00:00Z | T-6h | 0.576 | 0.424 | 0.177 | 6.05 | 3.27 | 2.79 | 209 (25/184) | CONFIRMED/PROJECTED |
| NYR @ WSH | 2026-10-09T23:00:00Z | T-6h | 0.544 | 0.456 | 0.183 | 5.83 | 3.06 | 2.77 | 218 (25/193) | CONFIRMED/CONFIRMED |
| PIT @ CBJ | 2026-10-09T23:00:00Z | T-6h | 0.493 | 0.507 | 0.165 | 6.85 | 3.39 | 3.46 | 215 (25/190) | CONFIRMED/PROBABLE |
| ANA @ WPG | 2026-10-10T00:00:00Z | T-6h | 0.547 | 0.453 | 0.172 | 6.18 | 3.24 | 2.94 | 207 (25/182) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT09PITCBJ-8 | game_total | 0.353 | 0.285 | 0.298 | 29 | 72 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT5 | team_total | 0.276 | 0.225 | 0.235 | 23 | 78 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT3 | team_total | 0.669 | 0.625 | 0.634 | 63 | 38 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-10 | game_total | 0.139 | 0.100 | 0.107 | 11 | 91 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-6 | game_total | 0.656 | 0.615 | 0.623 | 62 | 39 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-9 | game_total | 0.261 | 0.220 | 0.228 | 23 | 79 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-5 | game_total | 0.770 | 0.805 | 0.798 | 81 | 20 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT09NYRWSH-WSH3 | game_spread | 0.190 | 0.225 | 0.218 | 23 | 78 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH4 | team_total | 0.375 | 0.415 | 0.407 | 42 | 59 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT6 | team_total | 0.135 | 0.100 | 0.106 | 11 | 91 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT09SEADET-5 | game_total | 0.751 | 0.785 | 0.779 | 79 | 22 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 | team_total | 0.463 | 0.415 | 0.425 | 43 | 60 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-5 | game_total | 0.725 | 0.755 | 0.749 | 76 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 | team_total | 0.352 | 0.385 | 0.378 | 39 | 62 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-4 | game_total | 0.819 | 0.845 | 0.840 | 85 | 16 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-7 | game_total | 0.549 | 0.515 | 0.522 | 52 | 49 | yes | +0.012 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ3 | game_spread | 0.177 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA5 | team_total | 0.178 | 0.210 | 0.203 | 22 | 80 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT09SEADET-SEA3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.011 | OK |
| KXNHLGAME-26OCT09PITCBJ-CBJ | game_winner | 0.493 | 0.525 | 0.519 | 53 | 48 | no | +0.010 | OK |
| KXNHLGAME-26OCT09PITCBJ-PIT | game_winner | 0.507 | 0.475 | 0.481 | 48 | 53 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-6 | game_total | 0.553 | 0.585 | 0.579 | 59 | 42 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT09SEADET-4 | game_total | 0.842 | 0.865 | 0.861 | 87 | 14 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT09NYRWSH-WSH2 | game_spread | 0.315 | 0.345 | 0.339 | 35 | 66 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT2 | game_spread | 0.303 | 0.275 | 0.281 | 28 | 73 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT09SEADET-3 | game_total | 0.959 | 0.975 | 0.972 | 98 | 3 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA2 | game_spread | 0.247 | 0.275 | 0.269 | 28 | 73 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-7 | game_total | 0.444 | 0.475 | 0.469 | 48 | 53 | no | +0.009 | OK |
| KXNHLGAME-26OCT09NYRWSH-NYR | game_winner | 0.456 | 0.425 | 0.431 | 43 | 58 | yes | +0.008 | OK |
| KXNHLGAME-26OCT09NYRWSH-WSH | game_winner | 0.544 | 0.575 | 0.569 | 58 | 43 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA3 | game_spread | 0.143 | 0.165 | 0.160 | 17 | 84 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-4 | game_total | 0.855 | 0.875 | 0.871 | 88 | 13 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-6 | game_total | 0.496 | 0.525 | 0.519 | 53 | 48 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-3 | game_total | 0.951 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-3 | game_total | 0.963 | 0.975 | 0.973 | 98 | 3 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA2 | team_total | 0.784 | 0.815 | 0.809 | 83 | 20 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH2 | team_total | 0.806 | 0.830 | 0.825 | 84 | 18 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH3 | team_total | 0.601 | 0.625 | 0.620 | 63 | 38 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ2 | game_spread | 0.293 | 0.315 | 0.310 | 32 | 69 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT3 | game_spread | 0.193 | 0.175 | 0.178 | 18 | 83 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 | team_total | 0.571 | 0.600 | 0.594 | 61 | 41 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT2 | team_total | 0.851 | 0.830 | 0.834 | 84 | 18 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH5 | team_total | 0.197 | 0.220 | 0.215 | 23 | 79 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT09NYRWSH-8 | game_total | 0.208 | 0.225 | 0.221 | 23 | 78 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-10 | game_total | 0.084 | 0.095 | 0.093 | 10 | 91 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA2 | team_total | 0.758 | 0.775 | 0.772 | 78 | 23 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG2 | game_spread | 0.325 | 0.305 | 0.309 | 31 | 70 |  | -0.000 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-WPG | game_winner | 0.547 | 0.525 | 0.529 | 53 | 48 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-8 | game_total | 0.257 | 0.275 | 0.271 | 28 | 73 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-3 | game_total | 0.980 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-4 | game_total | 0.904 | 0.895 | 0.897 | 90 | 11 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-5 | game_total | 0.838 | 0.825 | 0.828 | 83 | 18 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-SEA2 | game_spread | 0.220 | 0.235 | 0.232 | 24 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ5 | team_total | 0.261 | 0.245 | 0.248 | 25 | 76 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-6 | game_total | 0.536 | 0.555 | 0.551 | 56 | 45 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA5 | team_total | 0.154 | 0.165 | 0.163 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-10 | game_total | 0.060 | 0.070 | 0.068 | 8 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA6 | team_total | 0.079 | 0.090 | 0.088 | 10 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-9 | game_total | 0.167 | 0.175 | 0.173 | 18 | 83 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-7 | game_total | 0.390 | 0.405 | 0.402 | 41 | 60 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ4 | team_total | 0.449 | 0.435 | 0.438 | 44 | 57 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ6 | team_total | 0.130 | 0.115 | 0.118 | 13 | 90 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET6 | team_total | 0.108 | 0.105 | 0.106 | 11 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-WPG2 | team_total | 0.829 | 0.835 | 0.834 | 84 | 17 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET2 | team_total | 0.829 | 0.845 | 0.842 | 86 | 17 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-DET3 | game_spread | 0.217 | 0.225 | 0.223 | 23 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-7 | game_total | 0.422 | 0.435 | 0.432 | 44 | 57 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR3 | game_spread | 0.132 | 0.135 | 0.134 | 14 | 87 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-10 | game_total | 0.075 | 0.080 | 0.079 | 9 | 93 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH6 | team_total | 0.085 | 0.095 | 0.093 | 11 | 92 |  | -0.010 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-ANA | game_winner | 0.453 | 0.465 | 0.463 | 47 | 54 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-9 | game_total | 0.142 | 0.150 | 0.148 | 16 | 86 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 | team_total | 0.316 | 0.330 | 0.327 | 34 | 68 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA3 | team_total | 0.534 | 0.550 | 0.547 | 56 | 46 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG3 | game_spread | 0.201 | 0.205 | 0.204 | 21 | 80 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 0.576 | 0.530 | 0.177 | 0.223 | 6.05 | 6.19 | 0.994/1.005 | KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 +0.050 |
| NYR @ WSH | 0.544 | 0.542 | 0.183 | 0.217 | 5.83 | 6.14 | 0.937/0.934 | KXNHLTOTAL-26OCT09NYRWSH-7 +0.055 |
| PIT @ CBJ | 0.493 | 0.527 | 0.165 | 0.215 | 6.85 | 6.57 | 1.007/1.016 | KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 -0.055 |
| ANA @ WPG | 0.547 | 0.519 | 0.172 | 0.218 | 6.18 | 6.41 | 0.994/1.024 | KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 +0.048 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Winterton: 1+ goals YES @ 10c · p 0.1406 (adj 0.128) · $5.45 · thesis SEA:OFFENSE_4PLUS
- Andrew Copp: 1+ goals YES @ 17c · p 0.2091 (adj 0.1981) · $5.33 · thesis DET:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 9c · p 0.1203 (adj 0.109) · $3.34 · thesis SEA:OFFENSE_4PLUS
- Michael Rasmussen: 1+ goals YES @ 11c · p 0.1444 (adj 0.1308) · $3.6 · thesis DET:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2417 (adj 0.2238) · $8.79 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 13c · p 0.1678 (adj 0.1571) · $4.73 · thesis WSH:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.8016 (adj 0.7583) · $18.24 · thesis NYR:SUPPRESSED
- Alex Tuch: 1+ assists NO @ 69c · p 0.7717 (adj 0.7258) · $18.24 · thesis WSH:SUPPRESSED
- Danton Heinen: 1+ goals YES @ 9c · p 0.1444 (adj 0.1295) · $8.33 · thesis CBJ:OFFENSE_4PLUS
- Valeri Nichushkin: 1+ assists NO @ 70c · p 0.7945 (adj 0.7448) · $20.0 · thesis CBJ:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 11c · p 0.1491 (adj 0.1381) · $5.76 · thesis PIT:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2061 (adj 0.1933) · $6.99 · thesis CBJ:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 85c · p 0.926 (adj 0.9058) · $20.0 · thesis WPG:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 16c · p 0.2343 (adj 0.212) · $11.52 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 7c · p 0.1091 (adj 0.0968) · $5.17 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 8c · p 0.1129 (adj 0.0997) · $3.5 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ DET** · priced 151/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.67, exp saves 22.38 (sd 6.24), pull risk 0.058
- SEA net: Joey Daccord (PROJECTED) exp shots 29.51, exp saves 25.45 (sd 6.84), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Emmitt Finnie: 1+ points | 0.461 | 0.355 | 37/66 | +0.074 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.325 | 0.225 | 25/80 | +0.062 | STANDARD |
| Andrew Copp: 1+ points | 0.479 | 0.385 | 40/63 | +0.062 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.140 | 0.230 | 25/79 | +0.058 | STANDARD |
| Andrew Copp: 1+ assists | 0.341 | 0.260 | 28/76 | +0.046 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.299 | 0.375 | 39/64 | +0.044 | STANDARD |

**NYR @ WSH** · priced 161/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 25.25, exp saves 22.05 (sd 6.08), pull risk 0.052
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 27.39, exp saves 23.53 (sd 6.53), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Logan Thompson: 22+ saves | 0.526 | 0.310 | 56/94 | -0.052 |  |
| Jordan Kyrou: 1+ assists | 0.162 | 0.275 | 29/74 | +0.085 | STANDARD |
| Alex Tuch: 1+ assists | 0.228 | 0.320 | 33/69 | +0.067 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.198 | 0.285 | 29/72 | +0.067 | STANDARD |
| Jordan Kyrou: 1+ points | 0.331 | 0.410 | 42/60 | +0.053 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.422 | 0.500 | 51/51 | +0.051 | STANDARD |

**PIT @ CBJ** · priced 162/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.49, exp saves 23.77 (sd 6.6), pull risk 0.064
- PIT net: Sergei Murashov (PROBABLE) exp shots 27.56, exp saves 23.54 (sd 6.58), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Knies: 1+ assists | 0.279 | 0.380 | 39/63 | +0.075 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.205 | 0.305 | 31/70 | +0.080 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.335 | 0.255 | 28/77 | +0.041 | STANDARD |
| Charlie Coyle: 2+ points | 0.195 | 0.115 | 17/94 | +0.015 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.480 | 49/53 | +0.050 | STANDARD |
| Sidney Crosby: 1+ assists | 0.410 | 0.485 | 49/52 | +0.052 | STANDARD |

**ANA @ WPG** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.53, exp saves 25.56 (sd 6.89), pull risk 0.062
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.65, exp saves 23.05 (sd 6.41), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Neal Pionk: 1+ points | 0.386 | 0.490 | 50/52 | +0.077 | STANDARD |
| Neal Pionk: 1+ assists | 0.339 | 0.440 | 45/57 | +0.074 | STANDARD |
| A.J. Greer: 1+ goals | 0.234 | 0.145 | 16/87 | +0.065 | STANDARD |
| Neal Pionk: 1+ goals | 0.074 | 0.155 | 16/85 | +0.067 | STANDARD |
| Alex Iafallo: 1+ goals | 0.190 | 0.120 | 17/93 | +0.010 | STANDARD |
| Jackson LaCombe: 2+ points | 0.209 | 0.140 | 21/93 | -0.012 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
