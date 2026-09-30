# NHL slate 2026-09-30 — RESEARCH_ONLY

generated 2026-09-30T15:43:05Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2602 · contracts joined: 533 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 458, 'NO_EDGE': 35, 'OK': 40}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 76, 'game_early_goal': 3, 'first_goal': 103, 'game_winner': 6, 'player_goals': 103, 'game_overtime': 3, 'player_points': 98, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 2026-09-30T23:30:00Z | T-6h | 0.576 | 0.424 | 0.178 | 6.12 | 3.30 | 2.82 | 177 (25/152) | CONFIRMED/PROJECTED |
| NYI @ TOR | 2026-09-30T23:30:00Z | T-6h | 0.435 | 0.565 | 0.178 | 6.17 | 2.88 | 3.29 | 176 (25/151) | PROJECTED/PROBABLE |
| LAK @ COL | 2026-10-01T02:00:00Z | T-6h | 0.645 | 0.355 | 0.172 | 5.80 | 3.35 | 2.45 | 180 (25/155) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP30NYITOR-NYI | game_winner | 0.565 | 0.455 | 0.477 | 46 | 55 | yes | +0.087 | OK |
| KXNHLGAME-26SEP30NYITOR-TOR | game_winner | 0.435 | 0.545 | 0.523 | 55 | 46 | no | +0.087 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI2 | game_spread | 0.342 | 0.255 | 0.271 | 26 | 75 | yes | +0.068 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR2 | game_spread | 0.229 | 0.315 | 0.296 | 32 | 69 | no | +0.066 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR3 | game_spread | 0.128 | 0.210 | 0.191 | 22 | 80 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4 | team_total | 0.334 | 0.425 | 0.406 | 44 | 59 | no | +0.059 | OK |
| KXNHLTOTAL-26SEP30LACOL-6 | game_total | 0.496 | 0.575 | 0.559 | 58 | 43 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR3 | team_total | 0.553 | 0.635 | 0.619 | 65 | 38 | no | +0.050 | OK |
| KXNHLTOTAL-26SEP30LACOL-7 | game_total | 0.384 | 0.455 | 0.441 | 46 | 55 | no | +0.048 | OK |
| KXNHLTOTAL-26SEP30LACOL-5 | game_total | 0.722 | 0.790 | 0.777 | 80 | 22 | no | +0.046 | OK |
| KXNHLTOTAL-26SEP30LACOL-8 | game_total | 0.202 | 0.265 | 0.251 | 27 | 74 | no | +0.045 | OK |
| KXNHLTOTAL-26SEP30LACOL-4 | game_total | 0.819 | 0.875 | 0.865 | 88 | 13 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 | team_total | 0.432 | 0.365 | 0.378 | 38 | 65 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR2 | team_total | 0.775 | 0.835 | 0.824 | 85 | 18 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA3 | team_total | 0.449 | 0.510 | 0.498 | 52 | 50 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI3 | team_total | 0.650 | 0.595 | 0.606 | 60 | 41 | yes | +0.034 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI3 | game_spread | 0.213 | 0.165 | 0.174 | 17 | 84 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL4 | team_total | 0.441 | 0.500 | 0.488 | 51 | 51 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5 | team_total | 0.172 | 0.225 | 0.214 | 24 | 79 | no | +0.026 | OK |
| KXNHLTOTAL-26SEP30LACOL-9 | game_total | 0.134 | 0.175 | 0.166 | 18 | 83 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA4 | team_total | 0.243 | 0.295 | 0.284 | 31 | 72 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA5 | team_total | 0.102 | 0.145 | 0.135 | 16 | 87 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA2 | team_total | 0.697 | 0.745 | 0.736 | 76 | 27 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI2 | team_total | 0.839 | 0.795 | 0.804 | 81 | 22 | yes | +0.018 | OK |
| KXNHLTOTAL-26SEP30LACOL-10 | game_total | 0.058 | 0.085 | 0.079 | 9 | 92 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL2 | team_total | 0.846 | 0.880 | 0.874 | 89 | 13 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL5 | team_total | 0.250 | 0.295 | 0.286 | 31 | 72 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI5 | team_total | 0.237 | 0.190 | 0.199 | 21 | 83 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR6 | team_total | 0.071 | 0.105 | 0.097 | 12 | 91 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL3 | team_total | 0.662 | 0.700 | 0.693 | 71 | 31 | no | +0.013 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT3 | game_spread | 0.120 | 0.145 | 0.140 | 15 | 86 | no | +0.011 | OK |
| KXNHLSPREAD-26SEP30LACOL-LA3 | game_spread | 0.085 | 0.105 | 0.101 | 11 | 90 | no | +0.009 | OK |
| KXNHLTOTAL-26SEP30LACOL-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL6 | team_total | 0.115 | 0.145 | 0.139 | 16 | 87 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI6 | team_total | 0.110 | 0.085 | 0.090 | 10 | 93 | yes | +0.004 | OK |
| KXNHLTOTAL-26SEP30PITPHI-5 | game_total | 0.764 | 0.785 | 0.781 | 79 | 22 | no | +0.004 | OK |
| KXNHLTOTAL-26SEP30PITPHI-4 | game_total | 0.849 | 0.870 | 0.866 | 88 | 14 | no | +0.002 | OK |
| KXNHLTOTAL-26SEP30LACOL-2 | game_total | 0.978 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP30NYITOR-4 | game_total | 0.851 | 0.870 | 0.866 | 88 | 14 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP30NYITOR-5 | game_total | 0.768 | 0.785 | 0.782 | 79 | 22 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA6 | team_total | 0.038 | 0.055 | 0.051 | 7 | 96 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL3 | game_spread | 0.267 | 0.285 | 0.281 | 29 | 72 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-9 | game_total | 0.178 | 0.165 | 0.168 | 17 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-6 | game_total | 0.545 | 0.565 | 0.561 | 57 | 44 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PIT2 | game_spread | 0.222 | 0.235 | 0.232 | 24 | 77 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI2 | game_spread | 0.349 | 0.335 | 0.338 | 34 | 67 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 | team_total | 0.322 | 0.345 | 0.340 | 36 | 67 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA2 | game_spread | 0.168 | 0.175 | 0.174 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 | team_total | 0.541 | 0.565 | 0.560 | 58 | 45 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-8 | game_total | 0.255 | 0.245 | 0.247 | 25 | 76 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT6 | team_total | 0.065 | 0.075 | 0.073 | 9 | 94 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT2 | team_total | 0.768 | 0.785 | 0.782 | 80 | 23 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-7 | game_total | 0.433 | 0.445 | 0.443 | 45 | 56 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT5 | team_total | 0.161 | 0.175 | 0.172 | 19 | 84 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PHI | game_winner | 0.576 | 0.565 | 0.567 | 57 | 44 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PIT | game_winner | 0.424 | 0.435 | 0.433 | 44 | 57 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-LA | game_winner | 0.355 | 0.365 | 0.363 | 37 | 64 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI3 | game_spread | 0.220 | 0.215 | 0.216 | 22 | 79 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-9 | game_total | 0.173 | 0.175 | 0.175 | 18 | 83 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-10 | game_total | 0.083 | 0.075 | 0.077 | 9 | 94 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-6 | game_total | 0.556 | 0.565 | 0.563 | 57 | 44 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-10 | game_total | 0.081 | 0.080 | 0.080 | 9 | 93 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL2 | game_spread | 0.410 | 0.405 | 0.406 | 41 | 60 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI2 | team_total | 0.841 | 0.835 | 0.836 | 85 | 18 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI6 | team_total | 0.113 | 0.115 | 0.115 | 13 | 90 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-8 | game_total | 0.248 | 0.250 | 0.250 | 26 | 76 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-COL | game_winner | 0.645 | 0.645 | 0.645 | 65 | 36 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-7 | game_total | 0.444 | 0.445 | 0.445 | 45 | 56 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI5 | team_total | 0.240 | 0.250 | 0.248 | 27 | 77 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI3 | team_total | 0.649 | 0.655 | 0.654 | 67 | 36 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI4 | team_total | 0.431 | 0.435 | 0.434 | 45 | 58 |  | -0.028 | NO_EDGE |
| KXNHL1P-26SEP30PITPHI-PHI | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PIT | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-TIE | period_winner |  | 0.335 |  | 36 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PHI2 | period_spread |  | 0.105 |  | 13 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 0.576 | 0.543 | 0.178 | 0.218 | 6.12 | 6.24 | 0.994/1.033 | KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 +0.038 |
| NYI @ TOR | 0.435 | 0.480 | 0.178 | 0.226 | 6.17 | 6.02 | 0.965/0.951 | KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 -0.051 |
| LAK @ COL | 0.645 | 0.589 | 0.172 | 0.220 | 5.80 | 5.94 | 0.973/0.992 | KXNHLTEAMTOTAL-26SEP30LACOL-LA3 +0.063 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ PHI** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.45, exp saves 23.13 (sd 6.32), pull risk 0.054
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.68, exp saves 22.06 (sd 6.27), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Christian Dvorak: 1+ points | 0.471 | 0.340 | 35/67 | +0.105 | STANDARD |
| Sidney Crosby: 1+ assists | 0.374 | 0.485 | 50/53 | +0.079 | STANDARD |
| Christian Dvorak: 1+ assists | 0.320 | 0.220 | 24/80 | +0.067 | STANDARD |
| Porter Martone: 1+ points | 0.449 | 0.540 | 55/47 | +0.064 | STANDARD |
| Porter Martone: 1+ goals | 0.224 | 0.305 | 32/71 | +0.052 | STANDARD |
| Sidney Crosby: 1+ points | 0.561 | 0.635 | 65/38 | +0.042 | STANDARD |

**NYI @ TOR** · priced 125/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.12, exp saves 26.87 (sd 7.06), pull risk 0.058
- NYI net: Ilya Sorokin (PROBABLE) exp shots 25.96, exp saves 22.61 (sd 6.31), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ assists | 0.276 | 0.395 | 42/63 | +0.077 | STANDARD |
| Darren Raddysh: 1+ assists | 0.288 | 0.400 | 42/62 | +0.075 | STANDARD |
| Matias Maccelli: 1+ assists | 0.188 | 0.295 | 31/72 | +0.078 | STANDARD |
| Darren Raddysh: 1+ points | 0.388 | 0.490 | 50/52 | +0.074 | STANDARD |
| Kirill Marchenko: 1+ points | 0.463 | 0.560 | 58/46 | +0.059 | STANDARD |
| Auston Matthews: 1+ assists | 0.310 | 0.405 | 42/61 | +0.063 | STANDARD |

**LAK @ COL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Scott Wedgewood (PROJECTED) exp shots 25.97, exp saves 22.81 (sd 6.12), pull risk 0.044
- LAK net: Darcy Kuemper (PROJECTED) exp shots 31.35, exp saves 26.9 (sd 7.15), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.405 | 0.580 | 60/44 | +0.138 | STANDARD |
| Cale Makar: 1+ points | 0.506 | 0.675 | 69/34 | +0.138 | STANDARD |
| Cale Makar: 2+ points | 0.154 | 0.315 | 33/70 | +0.132 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.308 | 0.460 | 47/55 | +0.124 | STANDARD |
| Cale Makar: 2+ assists | 0.093 | 0.220 | 24/80 | +0.096 | STANDARD |
| Artemi Panarin: 1+ assists | 0.334 | 0.460 | 48/56 | +0.089 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
