# NHL slate 2026-09-30 — RESEARCH_ONLY

generated 2026-09-30T23:23:43Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2607 · contracts joined: 538 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 463, 'NO_EDGE': 38, 'OK': 37}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 76, 'game_early_goal': 3, 'first_goal': 103, 'game_winner': 6, 'player_goals': 103, 'game_overtime': 3, 'player_points': 98, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 2026-09-30T23:30:00Z | T-<10m | 0.585 | 0.415 | 0.173 | 6.18 | 3.36 | 2.82 | 179 (25/154) | CONFIRMED/CONFIRMED |
| NYI @ TOR | 2026-09-30T23:30:00Z | T-<10m | 0.415 | 0.585 | 0.173 | 6.17 | 2.83 | 3.35 | 178 (25/153) | CONFIRMED/CONFIRMED |
| LAK @ COL | 2026-10-01T02:00:00Z | T-90m | 0.629 | 0.371 | 0.173 | 5.94 | 3.37 | 2.57 | 181 (25/156) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP30NYITOR-NYI | game_winner | 0.585 | 0.435 | 0.465 | 44 | 57 | yes | +0.128 | OK |
| KXNHLGAME-26SEP30NYITOR-TOR | game_winner | 0.415 | 0.565 | 0.535 | 57 | 44 | no | +0.128 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR2 | game_spread | 0.218 | 0.335 | 0.309 | 34 | 67 | no | +0.096 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI2 | game_spread | 0.359 | 0.245 | 0.266 | 25 | 76 | yes | +0.095 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR3 | team_total | 0.540 | 0.640 | 0.621 | 65 | 37 | no | +0.074 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR3 | game_spread | 0.127 | 0.215 | 0.194 | 22 | 79 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4 | team_total | 0.326 | 0.415 | 0.397 | 42 | 59 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI3 | team_total | 0.662 | 0.575 | 0.593 | 58 | 43 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 | team_total | 0.441 | 0.350 | 0.368 | 36 | 66 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI5 | team_total | 0.249 | 0.170 | 0.184 | 18 | 84 | yes | +0.059 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI3 | game_spread | 0.226 | 0.155 | 0.168 | 16 | 85 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5 | team_total | 0.165 | 0.235 | 0.219 | 24 | 77 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL4 | team_total | 0.444 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR2 | team_total | 0.764 | 0.830 | 0.818 | 84 | 18 | no | +0.045 | OK |
| KXNHLTOTAL-26SEP30LACOL-6 | game_total | 0.519 | 0.585 | 0.572 | 59 | 42 | no | +0.044 | OK |
| KXNHLTOTAL-26SEP30LACOL-5 | game_total | 0.738 | 0.795 | 0.784 | 80 | 21 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI2 | team_total | 0.844 | 0.785 | 0.798 | 80 | 23 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI6 | team_total | 0.117 | 0.070 | 0.078 | 8 | 94 | yes | +0.032 | OK |
| KXNHLTOTAL-26SEP30LACOL-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26SEP30LACOL-7 | game_total | 0.404 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL3 | team_total | 0.668 | 0.715 | 0.706 | 72 | 29 | no | +0.028 | OK |
| KXNHLTOTAL-26SEP30LACOL-8 | game_total | 0.221 | 0.265 | 0.256 | 27 | 74 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL5 | team_total | 0.252 | 0.300 | 0.290 | 31 | 71 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR6 | team_total | 0.066 | 0.100 | 0.092 | 11 | 91 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL2 | team_total | 0.849 | 0.875 | 0.870 | 88 | 13 | no | +0.013 | OK |
| KXNHLSPREAD-26SEP30LACOL-COL3 | game_spread | 0.255 | 0.285 | 0.279 | 29 | 72 | no | +0.011 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26SEP30LACOL-9 | game_total | 0.151 | 0.180 | 0.174 | 19 | 83 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA4 | team_total | 0.268 | 0.300 | 0.293 | 31 | 71 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA2 | team_total | 0.721 | 0.750 | 0.744 | 76 | 26 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA3 | team_total | 0.478 | 0.505 | 0.500 | 51 | 50 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL6 | team_total | 0.118 | 0.140 | 0.135 | 15 | 87 | no | +0.004 | OK |
| KXNHLTOTAL-26SEP30PITPHI-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 | team_total | 0.539 | 0.565 | 0.560 | 57 | 44 | no | +0.003 | OK |
| KXNHLTOTAL-26SEP30LACOL-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA5 | team_total | 0.121 | 0.145 | 0.140 | 16 | 87 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 | team_total | 0.323 | 0.350 | 0.345 | 36 | 66 | no | +0.001 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT2 | game_spread | 0.218 | 0.235 | 0.232 | 24 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI2 | team_total | 0.849 | 0.835 | 0.838 | 84 | 17 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA3 | game_spread | 0.095 | 0.110 | 0.107 | 12 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT5 | team_total | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-10 | game_total | 0.067 | 0.080 | 0.077 | 9 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-10 | game_total | 0.083 | 0.075 | 0.077 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-6 | game_total | 0.556 | 0.575 | 0.571 | 58 | 43 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-4 | game_total | 0.855 | 0.865 | 0.863 | 87 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-5 | game_total | 0.771 | 0.785 | 0.782 | 79 | 22 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL2 | game_spread | 0.397 | 0.415 | 0.411 | 42 | 59 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-COL | game_winner | 0.629 | 0.645 | 0.642 | 65 | 36 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-LA | game_winner | 0.371 | 0.355 | 0.358 | 36 | 65 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-4 | game_total | 0.857 | 0.865 | 0.863 | 87 | 14 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT2 | team_total | 0.764 | 0.780 | 0.777 | 79 | 23 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-3 | game_total | 0.964 | 0.965 | 0.965 | 97 | 4 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI2 | game_spread | 0.359 | 0.345 | 0.348 | 35 | 66 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI6 | team_total | 0.120 | 0.110 | 0.112 | 12 | 90 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA6 | team_total | 0.045 | 0.055 | 0.053 | 7 | 96 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA2 | game_spread | 0.181 | 0.175 | 0.176 | 18 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-8 | game_total | 0.253 | 0.245 | 0.247 | 25 | 76 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-5 | game_total | 0.768 | 0.775 | 0.774 | 78 | 23 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT6 | team_total | 0.067 | 0.070 | 0.069 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-6 | game_total | 0.553 | 0.565 | 0.563 | 57 | 44 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-7 | game_total | 0.444 | 0.455 | 0.453 | 46 | 55 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PHI | game_winner | 0.585 | 0.575 | 0.577 | 58 | 43 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PIT | game_winner | 0.415 | 0.425 | 0.423 | 43 | 58 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-10 | game_total | 0.082 | 0.080 | 0.080 | 9 | 93 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI3 | game_spread | 0.228 | 0.225 | 0.226 | 23 | 78 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-9 | game_total | 0.176 | 0.170 | 0.171 | 18 | 84 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI4 | team_total | 0.443 | 0.435 | 0.437 | 44 | 57 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-8 | game_total | 0.256 | 0.255 | 0.255 | 26 | 75 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-9 | game_total | 0.178 | 0.180 | 0.180 | 19 | 83 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI5 | team_total | 0.253 | 0.250 | 0.251 | 26 | 76 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-7 | game_total | 0.445 | 0.445 | 0.445 | 45 | 56 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI3 | team_total | 0.660 | 0.660 | 0.660 | 67 | 35 |  | -0.026 | NO_EDGE |
| KXNHL1P-26SEP30PITPHI-PHI | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PIT | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PHI2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PIT2 | period_spread |  | 0.075 |  | 10 | 95 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 0.585 | 0.544 | 0.173 | 0.221 | 6.18 | 6.26 | 0.994/1.042 | KXNHLSPREAD-26SEP30PITPHI-PHI2 -0.041 |
| NYI @ TOR | 0.415 | 0.480 | 0.173 | 0.230 | 6.17 | 5.99 | 0.955/0.947 | KXNHLSPREAD-26SEP30NYITOR-NYI2 -0.066 |
| LAK @ COL | 0.629 | 0.592 | 0.173 | 0.218 | 5.94 | 5.96 | 0.978/0.994 | KXNHLSPREAD-26SEP30LACOL-COL2 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ PHI** · priced 128/128 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.45, exp saves 23.14 (sd 6.3), pull risk 0.054
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.68, exp saves 22.08 (sd 6.21), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sidney Crosby: 1+ assists | 0.377 | 0.475 | 49/54 | +0.066 | STANDARD |
| Arturs Silovs: 26+ saves | 0.280 | 0.365 | 41/68 | +0.025 |  |
| Porter Martone: 1+ points | 0.451 | 0.535 | 55/48 | +0.051 | STANDARD |
| Porter Martone: 2+ points | 0.118 | 0.200 | 21/81 | +0.061 | STANDARD |
| Porter Martone: 1+ goals | 0.224 | 0.305 | 31/70 | +0.061 | STANDARD |
| Christian Dvorak: 1+ points | 0.482 | 0.405 | 42/61 | +0.045 | STANDARD |

**NYI @ TOR** · priced 125/127 player contracts · lineups LINES_PROJECTED/LINES_CONFIRMED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.12, exp saves 26.88 (sd 7.02), pull risk 0.058
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 25.96, exp saves 22.61 (sd 6.26), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ilya Sorokin: 25+ saves | 0.373 | 0.525 | 54/49 | +0.119 |  |
| Kirill Marchenko: 1+ assists | 0.271 | 0.395 | 42/63 | +0.083 | STANDARD |
| Darren Raddysh: 1+ assists | 0.285 | 0.400 | 41/61 | +0.089 | STANDARD |
| Matias Maccelli: 1+ assists | 0.209 | 0.315 | 32/69 | +0.086 | FULL |
| Darren Raddysh: 1+ points | 0.387 | 0.490 | 50/52 | +0.076 | STANDARD |
| Auston Matthews: 1+ assists | 0.306 | 0.405 | 41/60 | +0.077 | STANDARD |

**LAK @ COL** · priced 126/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.97, exp saves 22.8 (sd 6.08), pull risk 0.042
- LAK net: Darcy Kuemper (PROBABLE) exp shots 31.35, exp saves 26.84 (sd 7.11), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.408 | 0.585 | 60/43 | +0.145 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.306 | 0.480 | 49/53 | +0.146 | STANDARD |
| Cale Makar: 2+ points | 0.157 | 0.305 | 32/71 | +0.119 | STANDARD |
| Cale Makar: 1+ points | 0.509 | 0.655 | 67/36 | +0.115 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.208 | 0.340 | 35/67 | +0.106 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.489 | 0.605 | 61/40 | +0.094 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
