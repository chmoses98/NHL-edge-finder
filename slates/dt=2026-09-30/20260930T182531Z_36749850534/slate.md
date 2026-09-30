# NHL slate 2026-09-30 — RESEARCH_ONLY

generated 2026-09-30T18:25:31Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2607 · contracts joined: 538 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 463, 'NO_EDGE': 38, 'OK': 37}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 76, 'game_early_goal': 3, 'first_goal': 103, 'game_winner': 6, 'player_goals': 103, 'game_overtime': 3, 'player_points': 98, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 2026-09-30T23:30:00Z | T-3h | 0.585 | 0.415 | 0.173 | 6.18 | 3.36 | 2.82 | 179 (25/154) | CONFIRMED/CONFIRMED |
| NYI @ TOR | 2026-09-30T23:30:00Z | T-3h | 0.426 | 0.574 | 0.175 | 6.22 | 2.88 | 3.34 | 178 (25/153) | CONFIRMED/PROBABLE |
| LAK @ COL | 2026-10-01T02:00:00Z | T-6h | 0.627 | 0.373 | 0.170 | 5.92 | 3.35 | 2.57 | 181 (25/156) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP30NYITOR-TOR | game_winner | 0.426 | 0.545 | 0.521 | 55 | 46 | no | +0.097 | OK |
| KXNHLGAME-26SEP30NYITOR-NYI | game_winner | 0.574 | 0.455 | 0.479 | 46 | 55 | yes | +0.097 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI2 | game_spread | 0.351 | 0.255 | 0.273 | 26 | 75 | yes | +0.078 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR2 | game_spread | 0.224 | 0.315 | 0.295 | 32 | 69 | no | +0.071 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR3 | game_spread | 0.128 | 0.210 | 0.191 | 22 | 80 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4 | team_total | 0.336 | 0.425 | 0.407 | 44 | 59 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR3 | team_total | 0.554 | 0.635 | 0.619 | 65 | 38 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI5 | team_total | 0.249 | 0.180 | 0.193 | 19 | 83 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 | team_total | 0.443 | 0.365 | 0.380 | 38 | 65 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI3 | team_total | 0.657 | 0.595 | 0.608 | 60 | 41 | yes | +0.040 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI3 | game_spread | 0.219 | 0.165 | 0.175 | 17 | 84 | yes | +0.039 | OK |
| KXNHLTOTAL-26SEP30LACOL-6 | game_total | 0.515 | 0.575 | 0.563 | 58 | 43 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5 | team_total | 0.171 | 0.230 | 0.217 | 24 | 78 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR2 | team_total | 0.774 | 0.835 | 0.824 | 85 | 18 | no | +0.035 | OK |
| KXNHLTOTAL-26SEP30LACOL-7 | game_total | 0.399 | 0.455 | 0.444 | 46 | 55 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL4 | team_total | 0.440 | 0.500 | 0.488 | 51 | 51 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI6 | team_total | 0.117 | 0.070 | 0.078 | 8 | 94 | yes | +0.032 | OK |
| KXNHLTOTAL-26SEP30LACOL-5 | game_total | 0.740 | 0.790 | 0.781 | 80 | 22 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI2 | team_total | 0.844 | 0.795 | 0.806 | 81 | 22 | yes | +0.023 | OK |
| KXNHLTOTAL-26SEP30LACOL-4 | game_total | 0.829 | 0.870 | 0.862 | 88 | 14 | no | +0.023 | OK |
| KXNHLTOTAL-26SEP30LACOL-8 | game_total | 0.220 | 0.255 | 0.248 | 26 | 75 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL2 | team_total | 0.846 | 0.880 | 0.874 | 89 | 13 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL5 | team_total | 0.250 | 0.295 | 0.286 | 31 | 72 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL3 | team_total | 0.660 | 0.700 | 0.692 | 71 | 31 | no | +0.015 | OK |
| KXNHLSPREAD-26SEP30LACOL-COL3 | game_spread | 0.251 | 0.285 | 0.278 | 29 | 72 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR6 | team_total | 0.071 | 0.095 | 0.090 | 10 | 91 | no | +0.014 | OK |
| KXNHLTOTAL-26SEP30LACOL-10 | game_total | 0.064 | 0.085 | 0.080 | 9 | 92 | no | +0.011 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26SEP30LACOL-9 | game_total | 0.150 | 0.175 | 0.170 | 18 | 83 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA2 | team_total | 0.720 | 0.750 | 0.744 | 76 | 26 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL6 | team_total | 0.117 | 0.140 | 0.135 | 15 | 87 | no | +0.006 | OK |
| KXNHLSPREAD-26SEP30LACOL-LA3 | game_spread | 0.098 | 0.115 | 0.111 | 12 | 89 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI6 | team_total | 0.120 | 0.105 | 0.108 | 11 | 90 | yes | +0.003 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PHI2 | game_spread | 0.359 | 0.335 | 0.340 | 34 | 67 | yes | +0.003 | OK |
| KXNHLTOTAL-26SEP30NYITOR-9 | game_total | 0.183 | 0.165 | 0.168 | 17 | 84 | yes | +0.003 | OK |
| KXNHLSPREAD-26SEP30LACOL-COL2 | game_spread | 0.390 | 0.415 | 0.410 | 42 | 59 | no | +0.003 | OK |
| KXNHLTOTAL-26SEP30PITPHI-3 | game_total | 0.965 | 0.955 | 0.957 | 96 | 5 | yes | +0.002 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT2 | game_spread | 0.218 | 0.235 | 0.232 | 24 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA5 | team_total | 0.123 | 0.140 | 0.136 | 15 | 87 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-COL | game_winner | 0.627 | 0.645 | 0.641 | 65 | 36 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-LA | game_winner | 0.373 | 0.355 | 0.359 | 36 | 65 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-10 | game_total | 0.082 | 0.075 | 0.076 | 8 | 93 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-5 | game_total | 0.771 | 0.785 | 0.782 | 79 | 22 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI3 | game_spread | 0.228 | 0.215 | 0.218 | 22 | 79 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA3 | team_total | 0.476 | 0.505 | 0.499 | 52 | 51 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-8 | game_total | 0.259 | 0.245 | 0.248 | 25 | 76 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA4 | team_total | 0.270 | 0.295 | 0.290 | 31 | 72 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-4 | game_total | 0.857 | 0.865 | 0.863 | 87 | 14 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA2 | game_spread | 0.185 | 0.175 | 0.177 | 18 | 83 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT2 | team_total | 0.764 | 0.785 | 0.781 | 80 | 23 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA6 | team_total | 0.044 | 0.050 | 0.049 | 6 | 96 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-8 | game_total | 0.256 | 0.245 | 0.247 | 25 | 76 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-3 | game_total | 0.955 | 0.955 | 0.955 | 96 | 5 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-4 | game_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 | team_total | 0.323 | 0.345 | 0.341 | 36 | 67 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-5 | game_total | 0.778 | 0.785 | 0.784 | 79 | 22 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI2 | team_total | 0.849 | 0.840 | 0.842 | 85 | 17 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-2 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT5 | team_total | 0.161 | 0.170 | 0.168 | 18 | 84 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT6 | team_total | 0.067 | 0.070 | 0.069 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-10 | game_total | 0.085 | 0.075 | 0.077 | 9 | 94 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-9 | game_total | 0.178 | 0.175 | 0.176 | 18 | 83 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PHI | game_winner | 0.585 | 0.575 | 0.577 | 58 | 43 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PIT | game_winner | 0.415 | 0.425 | 0.423 | 43 | 58 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-6 | game_total | 0.556 | 0.565 | 0.563 | 57 | 44 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-7 | game_total | 0.453 | 0.445 | 0.447 | 45 | 56 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 | team_total | 0.539 | 0.560 | 0.556 | 58 | 46 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-6 | game_total | 0.567 | 0.565 | 0.565 | 57 | 44 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI5 | team_total | 0.253 | 0.245 | 0.246 | 26 | 77 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-7 | game_total | 0.444 | 0.445 | 0.445 | 45 | 56 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI4 | team_total | 0.443 | 0.440 | 0.441 | 45 | 57 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI3 | team_total | 0.660 | 0.655 | 0.656 | 67 | 36 |  | -0.026 | NO_EDGE |
| KXNHL1P-26SEP30PITPHI-PHI | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PIT | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PHI2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PIT2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 0.585 | 0.544 | 0.173 | 0.221 | 6.18 | 6.26 | 0.994/1.042 | KXNHLSPREAD-26SEP30PITPHI-PHI2 -0.041 |
| NYI @ TOR | 0.426 | 0.485 | 0.175 | 0.225 | 6.22 | 6.00 | 0.955/0.951 | KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 -0.069 |
| LAK @ COL | 0.627 | 0.592 | 0.170 | 0.218 | 5.92 | 5.96 | 0.978/0.992 | KXNHLGAME-26SEP30LACOL-COL -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ PHI** · priced 128/128 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.45, exp saves 23.14 (sd 6.3), pull risk 0.054
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.68, exp saves 22.08 (sd 6.21), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dan Vladar: 24+ saves | 0.467 | 0.260 | 51/99 | -0.060 |  |
| Christian Dvorak: 1+ assists | 0.329 | 0.225 | 24/79 | +0.077 | STANDARD |
| Christian Dvorak: 1+ points | 0.482 | 0.380 | 39/63 | +0.075 | STANDARD |
| Sidney Crosby: 1+ assists | 0.380 | 0.475 | 49/54 | +0.062 | STANDARD |
| Porter Martone: 1+ points | 0.451 | 0.540 | 55/47 | +0.061 | STANDARD |
| Porter Martone: 1+ goals | 0.224 | 0.310 | 32/70 | +0.061 | STANDARD |

**NYI @ TOR** · priced 125/127 player contracts · lineups LINES_PROJECTED/LINES_CONFIRMED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.12, exp saves 26.84 (sd 7.18), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 25.96, exp saves 22.65 (sd 6.28), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Stolarz: 27+ saves | 0.518 | 0.255 | 50/99 | +0.000 |  |
| Kirill Marchenko: 1+ assists | 0.274 | 0.400 | 42/62 | +0.090 | STANDARD |
| Darren Raddysh: 1+ assists | 0.279 | 0.395 | 41/62 | +0.084 | STANDARD |
| Darren Raddysh: 1+ points | 0.380 | 0.490 | 50/52 | +0.083 | STANDARD |
| Kirill Marchenko: 1+ points | 0.461 | 0.565 | 58/45 | +0.071 | STANDARD |
| Auston Matthews: 1+ assists | 0.302 | 0.405 | 42/61 | +0.071 | STANDARD |

**LAK @ COL** · priced 128/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.97, exp saves 22.79 (sd 6.13), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 31.35, exp saves 26.84 (sd 7.13), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.390 | 0.580 | 60/44 | +0.153 | STANDARD |
| Cale Makar: 1+ points | 0.494 | 0.675 | 69/34 | +0.151 | STANDARD |
| Cale Makar: 2+ points | 0.155 | 0.320 | 34/70 | +0.131 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.307 | 0.455 | 46/55 | +0.126 | STANDARD |
| Mackenzie Blackwood: 25+ saves | 0.379 | 0.250 | 48/98 | -0.118 |  |
| Cale Makar: 2+ assists | 0.093 | 0.220 | 24/80 | +0.096 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
