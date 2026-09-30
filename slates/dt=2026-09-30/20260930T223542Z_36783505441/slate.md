# NHL slate 2026-09-30 — RESEARCH_ONLY

generated 2026-09-30T22:35:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2607 · contracts joined: 538 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 463, 'NO_EDGE': 40, 'OK': 35}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 76, 'game_early_goal': 3, 'first_goal': 103, 'game_winner': 6, 'player_goals': 103, 'game_overtime': 3, 'player_points': 98, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 2026-09-30T23:30:00Z | T-30m | 0.585 | 0.415 | 0.173 | 6.18 | 3.36 | 2.82 | 179 (25/154) | CONFIRMED/CONFIRMED |
| NYI @ TOR | 2026-09-30T23:30:00Z | T-30m | 0.426 | 0.574 | 0.175 | 6.22 | 2.88 | 3.34 | 178 (25/153) | CONFIRMED/PROBABLE |
| LAK @ COL | 2026-10-01T02:00:00Z | T-3h | 0.629 | 0.371 | 0.173 | 5.94 | 3.37 | 2.57 | 181 (25/156) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP30NYITOR-TOR | game_winner | 0.426 | 0.565 | 0.537 | 57 | 44 | no | +0.117 | OK |
| KXNHLGAME-26SEP30NYITOR-NYI | game_winner | 0.574 | 0.435 | 0.463 | 44 | 57 | yes | +0.117 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI2 | game_spread | 0.351 | 0.245 | 0.264 | 25 | 76 | yes | +0.088 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR2 | game_spread | 0.224 | 0.325 | 0.303 | 33 | 68 | no | +0.081 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR3 | game_spread | 0.128 | 0.205 | 0.187 | 21 | 80 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR3 | team_total | 0.554 | 0.635 | 0.619 | 64 | 37 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI3 | team_total | 0.657 | 0.575 | 0.592 | 58 | 43 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI5 | team_total | 0.249 | 0.175 | 0.188 | 18 | 83 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4 | team_total | 0.336 | 0.415 | 0.399 | 42 | 59 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 | team_total | 0.443 | 0.360 | 0.376 | 37 | 65 | yes | +0.056 | OK |
| KXNHLTOTAL-26SEP30LACOL-5 | game_total | 0.738 | 0.795 | 0.784 | 80 | 21 | no | +0.040 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI3 | game_spread | 0.219 | 0.165 | 0.175 | 17 | 84 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL4 | team_total | 0.444 | 0.505 | 0.493 | 51 | 50 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5 | team_total | 0.171 | 0.230 | 0.217 | 24 | 78 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR2 | team_total | 0.774 | 0.830 | 0.820 | 84 | 18 | no | +0.035 | OK |
| KXNHLTOTAL-26SEP30LACOL-6 | game_total | 0.519 | 0.575 | 0.564 | 58 | 43 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI2 | team_total | 0.844 | 0.785 | 0.798 | 80 | 23 | yes | +0.033 | OK |
| KXNHLTOTAL-26SEP30LACOL-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26SEP30LACOL-7 | game_total | 0.404 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL5 | team_total | 0.252 | 0.300 | 0.290 | 31 | 71 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI6 | team_total | 0.117 | 0.075 | 0.082 | 9 | 94 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL3 | team_total | 0.668 | 0.705 | 0.698 | 71 | 30 | no | +0.017 | OK |
| KXNHLTOTAL-26SEP30LACOL-8 | game_total | 0.221 | 0.255 | 0.248 | 26 | 75 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR6 | team_total | 0.071 | 0.100 | 0.093 | 11 | 91 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL2 | team_total | 0.849 | 0.875 | 0.870 | 88 | 13 | no | +0.013 | OK |
| KXNHLSPREAD-26SEP30LACOL-COL3 | game_spread | 0.255 | 0.285 | 0.279 | 29 | 72 | no | +0.011 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26SEP30LACOL-9 | game_total | 0.151 | 0.175 | 0.170 | 18 | 83 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA3 | team_total | 0.478 | 0.505 | 0.500 | 51 | 50 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL6 | team_total | 0.118 | 0.145 | 0.139 | 16 | 87 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT2 | team_total | 0.764 | 0.790 | 0.785 | 80 | 22 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI6 | team_total | 0.120 | 0.105 | 0.108 | 11 | 90 | yes | +0.003 | OK |
| KXNHLTOTAL-26SEP30LACOL-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA5 | team_total | 0.121 | 0.145 | 0.140 | 16 | 87 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 | team_total | 0.323 | 0.350 | 0.345 | 36 | 66 | no | +0.001 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT2 | game_spread | 0.218 | 0.235 | 0.232 | 24 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-10 | game_total | 0.085 | 0.070 | 0.073 | 8 | 94 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA3 | game_spread | 0.095 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT5 | team_total | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-10 | game_total | 0.067 | 0.075 | 0.073 | 8 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA4 | team_total | 0.268 | 0.295 | 0.289 | 31 | 72 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-6 | game_total | 0.556 | 0.575 | 0.571 | 58 | 43 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-10 | game_total | 0.082 | 0.075 | 0.076 | 8 | 93 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-5 | game_total | 0.771 | 0.785 | 0.782 | 79 | 22 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL2 | game_spread | 0.397 | 0.415 | 0.411 | 42 | 59 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-COL | game_winner | 0.629 | 0.645 | 0.642 | 65 | 36 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-LA | game_winner | 0.371 | 0.355 | 0.358 | 36 | 65 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-4 | game_total | 0.857 | 0.865 | 0.863 | 87 | 14 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA2 | team_total | 0.721 | 0.740 | 0.736 | 75 | 27 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 | team_total | 0.539 | 0.555 | 0.552 | 56 | 45 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI2 | game_spread | 0.359 | 0.345 | 0.348 | 35 | 66 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-3 | game_total | 0.965 | 0.965 | 0.965 | 97 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-9 | game_total | 0.183 | 0.170 | 0.172 | 18 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA6 | team_total | 0.045 | 0.055 | 0.053 | 7 | 96 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-4 | game_total | 0.860 | 0.865 | 0.864 | 87 | 14 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA2 | game_spread | 0.181 | 0.175 | 0.176 | 18 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI2 | team_total | 0.849 | 0.840 | 0.842 | 85 | 17 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT6 | team_total | 0.067 | 0.070 | 0.069 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-7 | game_total | 0.444 | 0.455 | 0.453 | 46 | 55 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-9 | game_total | 0.178 | 0.175 | 0.176 | 18 | 83 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PHI | game_winner | 0.585 | 0.575 | 0.577 | 58 | 43 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PIT | game_winner | 0.415 | 0.425 | 0.423 | 43 | 58 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-5 | game_total | 0.778 | 0.775 | 0.776 | 78 | 23 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI3 | game_spread | 0.228 | 0.225 | 0.226 | 23 | 78 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-8 | game_total | 0.259 | 0.255 | 0.256 | 26 | 75 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI4 | team_total | 0.443 | 0.435 | 0.437 | 44 | 57 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-7 | game_total | 0.453 | 0.445 | 0.447 | 45 | 56 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI3 | team_total | 0.660 | 0.650 | 0.652 | 66 | 36 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-8 | game_total | 0.256 | 0.255 | 0.255 | 26 | 75 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-6 | game_total | 0.567 | 0.565 | 0.565 | 57 | 44 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI5 | team_total | 0.253 | 0.250 | 0.251 | 26 | 76 |  | -0.021 | NO_EDGE |
| KXNHL1P-26SEP30PITPHI-PHI | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PIT | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PHI2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PIT2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 0.585 | 0.544 | 0.173 | 0.221 | 6.18 | 6.26 | 0.994/1.042 | KXNHLSPREAD-26SEP30PITPHI-PHI2 -0.041 |
| NYI @ TOR | 0.426 | 0.485 | 0.175 | 0.225 | 6.22 | 6.00 | 0.955/0.951 | KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 -0.069 |
| LAK @ COL | 0.629 | 0.592 | 0.173 | 0.218 | 5.94 | 5.96 | 0.978/0.994 | KXNHLSPREAD-26SEP30LACOL-COL2 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ PHI** · priced 128/128 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.45, exp saves 23.14 (sd 6.3), pull risk 0.054
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.68, exp saves 22.08 (sd 6.21), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dan Vladar: 24+ saves | 0.467 | 0.285 | 52/95 | -0.070 |  |
| Christian Dvorak: 1+ points | 0.482 | 0.395 | 41/62 | +0.055 | STANDARD |
| Sidney Crosby: 1+ assists | 0.380 | 0.465 | 48/55 | +0.052 | STANDARD |
| Porter Martone: 1+ goals | 0.224 | 0.305 | 31/70 | +0.061 | STANDARD |
| Porter Martone: 1+ points | 0.451 | 0.530 | 54/48 | +0.051 | STANDARD |
| Arturs Silovs: 26+ saves | 0.280 | 0.355 | 45/74 | -0.033 |  |

**NYI @ TOR** · priced 125/127 player contracts · lineups LINES_PROJECTED/LINES_CONFIRMED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.12, exp saves 26.84 (sd 7.18), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 25.96, exp saves 22.65 (sd 6.28), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ilya Sorokin: 25+ saves | 0.375 | 0.525 | 53/48 | +0.127 |  |
| Kirill Marchenko: 1+ assists | 0.274 | 0.400 | 42/62 | +0.090 | STANDARD |
| Darren Raddysh: 1+ assists | 0.279 | 0.395 | 41/62 | +0.084 | STANDARD |
| Darren Raddysh: 1+ points | 0.380 | 0.495 | 51/52 | +0.083 | STANDARD |
| Kirill Marchenko: 1+ points | 0.461 | 0.565 | 58/45 | +0.071 | STANDARD |
| Matias Maccelli: 1+ assists | 0.215 | 0.315 | 32/69 | +0.080 | FULL |

**LAK @ COL** · priced 126/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.97, exp saves 22.8 (sd 6.08), pull risk 0.042
- LAK net: Darcy Kuemper (PROBABLE) exp shots 31.35, exp saves 26.84 (sd 7.11), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.306 | 0.475 | 49/54 | +0.136 | STANDARD |
| Cale Makar: 1+ assists | 0.408 | 0.575 | 60/45 | +0.124 | STANDARD |
| Cale Makar: 2+ points | 0.157 | 0.305 | 32/71 | +0.119 | STANDARD |
| Cale Makar: 1+ points | 0.509 | 0.655 | 67/36 | +0.115 | STANDARD |
| Mats Zuccarello: 1+ assists | 0.208 | 0.340 | 35/67 | +0.106 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.489 | 0.605 | 61/40 | +0.094 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
