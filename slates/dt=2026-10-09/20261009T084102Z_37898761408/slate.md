# NHL slate 2026-10-09 — RESEARCH_ONLY

generated 2026-10-09T08:41:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2602 · contracts joined: 204 (unjoined to any game: 1575)
gates: {'UNSUPPORTED': 104, 'NO_EDGE': 73, 'OK': 27}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'game_early_goal': 4, 'game_winner': 8, 'game_overtime': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 2026-10-09T23:00:00Z | T-12h | 0.574 | 0.426 | 0.176 | 6.07 | 3.27 | 2.80 | 51 (25/26) | CONFIRMED/PROJECTED |
| NYR @ WSH | 2026-10-09T23:00:00Z | T-12h | 0.545 | 0.455 | 0.173 | 6.06 | 3.17 | 2.90 | 51 (25/26) | PROJECTED/PROJECTED |
| PIT @ CBJ | 2026-10-09T23:00:00Z | T-12h | 0.569 | 0.431 | 0.170 | 6.48 | 3.46 | 3.03 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ WPG | 2026-10-10T00:00:00Z | T-12h | 0.542 | 0.458 | 0.173 | 6.24 | 3.25 | 2.99 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT09PITCBJ-CBJ2 | game_spread | 0.351 | 0.305 | 0.314 | 31 | 70 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLGAME-26OCT09PITCBJ-CBJ | game_winner | 0.569 | 0.525 | 0.534 | 53 | 48 | yes | +0.022 | OK |
| KXNHLGAME-26OCT09PITCBJ-PIT | game_winner | 0.431 | 0.475 | 0.466 | 48 | 53 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-PIT2 | game_spread | 0.237 | 0.275 | 0.267 | 28 | 73 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-5 | game_total | 0.773 | 0.805 | 0.799 | 81 | 20 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT09PITCBJ-CBJ3 | game_spread | 0.224 | 0.195 | 0.201 | 20 | 81 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ3 | team_total | 0.675 | 0.635 | 0.643 | 65 | 38 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT09SEADET-4 | game_total | 0.843 | 0.865 | 0.861 | 87 | 14 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT09SEADET-SEA3 | game_spread | 0.123 | 0.145 | 0.140 | 15 | 86 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA2 | team_total | 0.760 | 0.785 | 0.780 | 79 | 22 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ6 | team_total | 0.134 | 0.110 | 0.115 | 12 | 90 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA2 | team_total | 0.792 | 0.820 | 0.815 | 83 | 19 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT4 | team_total | 0.366 | 0.405 | 0.397 | 42 | 61 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT09NYRWSH-WSH3 | game_spread | 0.192 | 0.215 | 0.210 | 22 | 79 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA3 | game_spread | 0.146 | 0.165 | 0.161 | 17 | 84 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT09SEADET-5 | game_total | 0.754 | 0.780 | 0.775 | 79 | 23 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 | team_total | 0.360 | 0.395 | 0.388 | 41 | 62 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ2 | team_total | 0.853 | 0.835 | 0.839 | 84 | 17 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT2 | team_total | 0.796 | 0.820 | 0.815 | 83 | 19 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT09ANAWPG-ANA2 | game_spread | 0.254 | 0.275 | 0.271 | 28 | 73 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-4 | game_total | 0.860 | 0.880 | 0.876 | 89 | 13 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT5 | team_total | 0.196 | 0.220 | 0.215 | 23 | 79 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT3 | team_total | 0.581 | 0.615 | 0.608 | 63 | 40 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-6 | game_total | 0.562 | 0.585 | 0.580 | 59 | 42 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT09ANAWPG-7 | game_total | 0.452 | 0.475 | 0.470 | 48 | 53 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA5 | team_total | 0.188 | 0.210 | 0.206 | 22 | 80 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT09PITCBJ-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR5 | team_total | 0.168 | 0.155 | 0.158 | 16 | 85 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ5 | team_total | 0.272 | 0.245 | 0.250 | 26 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-CBJ4 | team_total | 0.466 | 0.435 | 0.441 | 45 | 58 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-4 | game_total | 0.875 | 0.885 | 0.883 | 89 | 12 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-5 | game_total | 0.802 | 0.815 | 0.812 | 82 | 19 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT09ANAWPG-WPG2 | game_spread | 0.322 | 0.305 | 0.308 | 31 | 70 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA4 | team_total | 0.318 | 0.340 | 0.336 | 35 | 67 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-8 | game_total | 0.300 | 0.280 | 0.284 | 29 | 73 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-10 | game_total | 0.089 | 0.100 | 0.098 | 11 | 91 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-7 | game_total | 0.427 | 0.450 | 0.445 | 46 | 56 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-ANA | game_winner | 0.458 | 0.475 | 0.472 | 48 | 53 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT09ANAWPG-WPG | game_winner | 0.542 | 0.525 | 0.528 | 53 | 48 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-9 | game_total | 0.216 | 0.205 | 0.207 | 21 | 80 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-6 | game_total | 0.538 | 0.555 | 0.552 | 56 | 45 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR2 | game_spread | 0.247 | 0.235 | 0.237 | 24 | 77 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA5 | team_total | 0.157 | 0.170 | 0.167 | 18 | 84 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-NYR3 | game_spread | 0.138 | 0.145 | 0.144 | 15 | 86 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR4 | team_total | 0.339 | 0.320 | 0.324 | 33 | 69 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-5 | game_total | 0.754 | 0.765 | 0.763 | 77 | 24 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-9 | game_total | 0.167 | 0.180 | 0.177 | 19 | 83 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-SEA2 | game_spread | 0.225 | 0.235 | 0.233 | 24 | 77 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-2 | game_total | 0.984 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-3 | game_total | 0.965 | 0.965 | 0.965 | 97 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET6 | team_total | 0.109 | 0.105 | 0.106 | 11 | 90 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-NYR3 | team_total | 0.559 | 0.540 | 0.544 | 55 | 47 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09NYRWSH-WSH2 | team_total | 0.819 | 0.825 | 0.824 | 83 | 18 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-10 | game_total | 0.108 | 0.100 | 0.102 | 11 | 91 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT09PITCBJ-6 | game_total | 0.608 | 0.595 | 0.598 | 60 | 41 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT09SEADET-DET3 | game_spread | 0.217 | 0.225 | 0.223 | 23 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA3 | team_total | 0.583 | 0.605 | 0.601 | 62 | 41 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-DET2 | team_total | 0.830 | 0.840 | 0.838 | 85 | 17 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-8 | game_total | 0.242 | 0.235 | 0.236 | 24 | 77 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-10 | game_total | 0.074 | 0.070 | 0.071 | 8 | 94 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-7 | game_total | 0.426 | 0.415 | 0.417 | 42 | 59 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT09NYRWSH-WSH | game_winner | 0.545 | 0.555 | 0.553 | 56 | 45 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26OCT09NYRWSH-NYR | game_winner | 0.455 | 0.445 | 0.447 | 45 | 56 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT09NYRWSH-WSH2 | game_spread | 0.323 | 0.315 | 0.317 | 32 | 69 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-9 | game_total | 0.167 | 0.160 | 0.161 | 17 | 85 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-10 | game_total | 0.078 | 0.080 | 0.080 | 9 | 93 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-WPG5 | team_total | 0.231 | 0.240 | 0.238 | 25 | 77 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT09ANAWPG-8 | game_total | 0.270 | 0.275 | 0.274 | 28 | 73 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT09NYRWSH-4 | game_total | 0.846 | 0.845 | 0.845 | 85 | 16 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT6 | team_total | 0.088 | 0.095 | 0.094 | 11 | 92 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT09SEADET-8 | game_total | 0.242 | 0.250 | 0.248 | 26 | 76 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09ANAWPG-WPG6 | team_total | 0.108 | 0.110 | 0.110 | 12 | 90 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT09SEADET-SEA3 | team_total | 0.537 | 0.555 | 0.551 | 57 | 46 |  | -0.015 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ DET | 0.574 | 0.530 | 0.176 | 0.219 | 6.07 | 6.20 | 0.994/1.005 | KXNHLTEAMTOTAL-26OCT09SEADET-SEA3 +0.048 |
| NYR @ WSH | 0.545 | 0.536 | 0.173 | 0.217 | 6.06 | 6.27 | 0.960/0.957 | KXNHLTOTAL-26OCT09NYRWSH-7 +0.040 |
| PIT @ CBJ | 0.569 | 0.552 | 0.170 | 0.219 | 6.48 | 6.50 | 0.964/1.033 | KXNHLTEAMTOTAL-26OCT09PITCBJ-PIT3 +0.025 |
| ANA @ WPG | 0.542 | 0.518 | 0.173 | 0.213 | 6.24 | 6.40 | 0.988/1.024 | KXNHLTEAMTOTAL-26OCT09ANAWPG-ANA4 +0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.67, exp saves 22.41 (sd 6.18), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.51, exp saves 25.41 (sd 6.84), pull risk 0.063

**NYR @ WSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.25, exp saves 22.0 (sd 6.17), pull risk 0.057
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.39, exp saves 23.52 (sd 6.58), pull risk 0.068

**PIT @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 27.49, exp saves 23.84 (sd 6.51), pull risk 0.061
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.56, exp saves 23.54 (sd 6.63), pull risk 0.075

**ANA @ WPG** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 29.53, exp saves 25.57 (sd 6.93), pull risk 0.064
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.65, exp saves 23.02 (sd 6.42), pull risk 0.067

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
