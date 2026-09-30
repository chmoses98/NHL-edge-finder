# NHL slate 2026-09-30 — RESEARCH_ONLY

generated 2026-09-30T14:43:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2562 · contracts joined: 533 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 458, 'NO_EDGE': 38, 'OK': 37}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 76, 'game_early_goal': 3, 'first_goal': 103, 'game_winner': 6, 'player_goals': 103, 'game_overtime': 3, 'player_points': 98, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 2026-09-30T23:30:00Z | T-6h | 0.569 | 0.431 | 0.175 | 6.17 | 3.30 | 2.87 | 177 (25/152) | PROJECTED/PROJECTED |
| NYI @ TOR | 2026-09-30T23:30:00Z | T-6h | 0.435 | 0.565 | 0.178 | 6.17 | 2.88 | 3.29 | 176 (25/151) | PROJECTED/PROBABLE |
| LAK @ COL | 2026-10-01T02:00:00Z | T-6h | 0.645 | 0.355 | 0.172 | 5.80 | 3.35 | 2.45 | 180 (25/155) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP30NYITOR-NYI | game_winner | 0.565 | 0.455 | 0.477 | 46 | 55 | yes | +0.087 | OK |
| KXNHLGAME-26SEP30NYITOR-TOR | game_winner | 0.435 | 0.535 | 0.515 | 54 | 47 | no | +0.077 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI2 | game_spread | 0.342 | 0.255 | 0.271 | 26 | 75 | yes | +0.068 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR2 | game_spread | 0.229 | 0.315 | 0.296 | 32 | 69 | no | +0.066 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR3 | game_spread | 0.128 | 0.205 | 0.187 | 21 | 80 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4 | team_total | 0.334 | 0.425 | 0.406 | 44 | 59 | no | +0.059 | OK |
| KXNHLTOTAL-26SEP30LACOL-6 | game_total | 0.496 | 0.580 | 0.563 | 59 | 43 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR3 | team_total | 0.553 | 0.635 | 0.619 | 65 | 38 | no | +0.050 | OK |
| KXNHLTOTAL-26SEP30LACOL-7 | game_total | 0.384 | 0.455 | 0.441 | 46 | 55 | no | +0.048 | OK |
| KXNHLTOTAL-26SEP30LACOL-5 | game_total | 0.722 | 0.790 | 0.777 | 80 | 22 | no | +0.046 | OK |
| KXNHLTOTAL-26SEP30LACOL-8 | game_total | 0.202 | 0.265 | 0.251 | 27 | 74 | no | +0.045 | OK |
| KXNHLTOTAL-26SEP30LACOL-4 | game_total | 0.819 | 0.875 | 0.865 | 88 | 13 | no | +0.044 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI3 | game_spread | 0.213 | 0.155 | 0.165 | 16 | 85 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 | team_total | 0.432 | 0.365 | 0.378 | 38 | 65 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR2 | team_total | 0.775 | 0.835 | 0.824 | 85 | 18 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA3 | team_total | 0.449 | 0.515 | 0.502 | 53 | 50 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI3 | team_total | 0.650 | 0.585 | 0.598 | 60 | 43 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL4 | team_total | 0.441 | 0.500 | 0.488 | 51 | 51 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5 | team_total | 0.172 | 0.225 | 0.214 | 24 | 79 | no | +0.026 | OK |
| KXNHLTOTAL-26SEP30LACOL-9 | game_total | 0.134 | 0.175 | 0.166 | 18 | 83 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA4 | team_total | 0.243 | 0.300 | 0.288 | 32 | 72 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA5 | team_total | 0.102 | 0.145 | 0.135 | 16 | 87 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA2 | team_total | 0.697 | 0.745 | 0.736 | 76 | 27 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI2 | team_total | 0.839 | 0.795 | 0.804 | 81 | 22 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL2 | team_total | 0.846 | 0.880 | 0.874 | 89 | 13 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL5 | team_total | 0.250 | 0.295 | 0.286 | 31 | 72 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI5 | team_total | 0.237 | 0.190 | 0.199 | 21 | 83 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR6 | team_total | 0.071 | 0.105 | 0.097 | 12 | 91 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL3 | team_total | 0.662 | 0.700 | 0.693 | 71 | 31 | no | +0.013 | OK |
| KXNHLSPREAD-26SEP30LACOL-LA3 | game_spread | 0.085 | 0.105 | 0.101 | 11 | 90 | no | +0.009 | OK |
| KXNHLTOTAL-26SEP30LACOL-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTOTAL-26SEP30LACOL-10 | game_total | 0.058 | 0.085 | 0.079 | 10 | 93 | no | +0.007 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT3 | game_spread | 0.127 | 0.145 | 0.141 | 15 | 86 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI6 | team_total | 0.110 | 0.085 | 0.090 | 10 | 93 | yes | +0.004 | OK |
| KXNHLTOTAL-26SEP30PITPHI-4 | game_total | 0.850 | 0.870 | 0.866 | 88 | 14 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP30LACOL-2 | game_total | 0.978 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP30NYITOR-4 | game_total | 0.851 | 0.870 | 0.866 | 88 | 14 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA6 | team_total | 0.038 | 0.055 | 0.051 | 7 | 96 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL3 | game_spread | 0.267 | 0.285 | 0.281 | 29 | 72 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-9 | game_total | 0.178 | 0.165 | 0.168 | 17 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL6 | team_total | 0.115 | 0.140 | 0.135 | 16 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA2 | game_spread | 0.168 | 0.175 | 0.174 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-8 | game_total | 0.255 | 0.245 | 0.247 | 25 | 76 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-5 | game_total | 0.768 | 0.780 | 0.778 | 79 | 23 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PIT2 | game_spread | 0.228 | 0.235 | 0.234 | 24 | 77 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-LA | game_winner | 0.355 | 0.365 | 0.363 | 37 | 64 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-5 | game_total | 0.770 | 0.775 | 0.774 | 78 | 23 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-9 | game_total | 0.178 | 0.175 | 0.176 | 18 | 83 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-10 | game_total | 0.083 | 0.075 | 0.077 | 9 | 94 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-10 | game_total | 0.082 | 0.080 | 0.080 | 9 | 93 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-6 | game_total | 0.556 | 0.565 | 0.563 | 57 | 44 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI2 | game_spread | 0.342 | 0.335 | 0.336 | 34 | 67 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT5 | team_total | 0.166 | 0.175 | 0.173 | 19 | 84 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT6 | team_total | 0.071 | 0.075 | 0.074 | 9 | 94 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-6 | game_total | 0.558 | 0.565 | 0.564 | 57 | 44 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI3 | game_spread | 0.215 | 0.215 | 0.215 | 22 | 79 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL2 | game_spread | 0.410 | 0.405 | 0.406 | 41 | 60 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT2 | team_total | 0.775 | 0.785 | 0.783 | 80 | 23 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI2 | team_total | 0.842 | 0.835 | 0.836 | 85 | 18 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-8 | game_total | 0.256 | 0.250 | 0.251 | 26 | 76 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PIT | game_winner | 0.431 | 0.435 | 0.434 | 44 | 57 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PHI | game_winner | 0.569 | 0.565 | 0.566 | 57 | 44 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-7 | game_total | 0.443 | 0.445 | 0.445 | 45 | 56 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 | team_total | 0.553 | 0.565 | 0.563 | 58 | 45 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 | team_total | 0.335 | 0.345 | 0.343 | 36 | 67 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-COL | game_winner | 0.645 | 0.645 | 0.645 | 65 | 36 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI6 | team_total | 0.115 | 0.115 | 0.115 | 13 | 90 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-7 | game_total | 0.444 | 0.445 | 0.445 | 45 | 56 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI5 | team_total | 0.241 | 0.250 | 0.248 | 27 | 77 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI3 | team_total | 0.648 | 0.655 | 0.654 | 67 | 36 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI4 | team_total | 0.430 | 0.435 | 0.434 | 45 | 58 |  | -0.027 | NO_EDGE |
| KXNHL1P-26SEP30PITPHI-TIE | period_winner |  | 0.335 |  | 36 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PIT | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PHI | period_winner |  | 0.340 |  | 36 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PHI2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 0.569 | 0.541 | 0.175 | 0.216 | 6.17 | 6.24 | 0.993/1.033 | KXNHLGAME-26SEP30PITPHI-PIT +0.027 |
| NYI @ TOR | 0.435 | 0.480 | 0.178 | 0.226 | 6.17 | 6.02 | 0.965/0.951 | KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 -0.051 |
| LAK @ COL | 0.645 | 0.589 | 0.172 | 0.220 | 5.80 | 5.94 | 0.973/0.992 | KXNHLTEAMTOTAL-26SEP30LACOL-LA3 +0.063 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ PHI** · priced 126/126 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 26.45, exp saves 23.12 (sd 6.25), pull risk 0.053
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.68, exp saves 22.07 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sidney Crosby: 1+ assists | 0.376 | 0.500 | 52/52 | +0.087 | STANDARD |
| Christian Dvorak: 1+ points | 0.474 | 0.355 | 37/66 | +0.088 | STANDARD |
| Christian Dvorak: 1+ assists | 0.323 | 0.220 | 24/80 | +0.070 | STANDARD |
| Porter Martone: 1+ points | 0.452 | 0.540 | 55/47 | +0.061 | STANDARD |
| Porter Martone: 1+ goals | 0.227 | 0.305 | 32/71 | +0.049 | STANDARD |
| Sidney Crosby: 2+ points | 0.203 | 0.275 | 29/74 | +0.044 | STANDARD |

**NYI @ TOR** · priced 125/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.12, exp saves 26.87 (sd 7.06), pull risk 0.058
- NYI net: Ilya Sorokin (PROBABLE) exp shots 25.96, exp saves 22.61 (sd 6.31), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ assists | 0.276 | 0.395 | 42/63 | +0.077 | STANDARD |
| Matias Maccelli: 1+ assists | 0.188 | 0.300 | 32/72 | +0.078 | STANDARD |
| Darren Raddysh: 1+ assists | 0.288 | 0.400 | 42/62 | +0.075 | STANDARD |
| Darren Raddysh: 1+ points | 0.388 | 0.495 | 51/52 | +0.074 | STANDARD |
| Kirill Marchenko: 1+ points | 0.463 | 0.560 | 58/46 | +0.059 | STANDARD |
| Auston Matthews: 1+ assists | 0.310 | 0.405 | 42/61 | +0.063 | STANDARD |

**LAK @ COL** · priced 127/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Scott Wedgewood (PROJECTED) exp shots 25.97, exp saves 22.81 (sd 6.12), pull risk 0.044
- LAK net: Darcy Kuemper (PROJECTED) exp shots 31.35, exp saves 26.9 (sd 7.15), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.405 | 0.580 | 60/44 | +0.138 | STANDARD |
| Cale Makar: 1+ points | 0.506 | 0.665 | 68/35 | +0.128 | STANDARD |
| Cale Makar: 2+ points | 0.154 | 0.310 | 33/71 | +0.122 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.308 | 0.450 | 47/57 | +0.105 | STANDARD |
| Cale Makar: 2+ assists | 0.093 | 0.220 | 24/80 | +0.096 | STANDARD |
| Artemi Panarin: 1+ assists | 0.334 | 0.460 | 48/56 | +0.089 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
