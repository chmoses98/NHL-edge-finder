# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T22:18:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2978 · contracts joined: 451 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 401, 'OK': 17, 'NO_EDGE': 33}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 62, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 129, 'game_overtime': 2, 'player_points': 83, 'goalie_saves': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ FLA | 2026-10-30T23:00:00Z | T-30m | 0.626 | 0.374 | 0.167 | 6.13 | 3.47 | 2.66 | 222 (25/197) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-90m | 0.474 | 0.526 | 0.173 | 6.46 | 3.16 | 3.30 | 229 (25/204) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.472 | 0.540 | 0.526 | 55 | 47 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.400 | 0.455 | 0.444 | 46 | 55 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.687 | 0.735 | 0.726 | 74 | 27 | no | +0.029 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.626 | 0.675 | 0.665 | 68 | 33 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.268 | 0.320 | 0.309 | 33 | 69 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.860 | 0.900 | 0.893 | 91 | 11 | no | +0.023 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.961 | 0.985 | 0.982 | 99 | 2 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.184 | 0.155 | 0.160 | 16 | 85 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.767 | 0.795 | 0.790 | 80 | 21 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.132 | 0.155 | 0.150 | 16 | 85 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.104 | 0.085 | 0.089 | 9 | 92 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.548 | 0.575 | 0.570 | 58 | 43 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.438 | 0.465 | 0.460 | 47 | 54 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.649 | 0.625 | 0.630 | 63 | 38 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.217 | 0.235 | 0.231 | 24 | 77 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.294 | 0.275 | 0.279 | 28 | 73 |  | -0.000 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.474 | 0.495 | 0.491 | 50 | 51 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.526 | 0.505 | 0.509 | 51 | 50 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.162 | 0.175 | 0.172 | 18 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.248 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.396 | 0.425 | 0.419 | 44 | 59 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.805 | 0.815 | 0.813 | 82 | 19 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.879 | 0.885 | 0.884 | 89 | 12 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.079 | 0.075 | 0.076 | 8 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.500 | 0.485 | 0.488 | 49 | 52 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.286 | 0.270 | 0.273 | 28 | 74 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.098 | 0.095 | 0.096 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.189 | 0.200 | 0.198 | 21 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.054 | 0.045 | 0.047 | 6 | 97 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.820 | 0.825 | 0.824 | 83 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.116 | 0.105 | 0.107 | 12 | 91 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.137 | 0.125 | 0.127 | 14 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.210 | 0.200 | 0.202 | 21 | 81 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.615 | 0.630 | 0.627 | 64 | 38 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.172 | 0.180 | 0.178 | 19 | 83 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.605 | 0.595 | 0.597 | 60 | 41 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.435 | 0.425 | 0.427 | 43 | 58 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.240 | 0.230 | 0.232 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.270 | 0.275 | 0.274 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.310 | 0.305 | 0.306 | 31 | 70 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.737 | 0.735 | 0.735 | 74 | 27 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.491 | 0.495 | 0.494 | 50 | 51 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.098 | 0.095 | 0.096 | 11 | 92 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.837 | 0.835 | 0.835 | 85 | 18 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT30WPGFLA-FLA | period_winner |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30WPGFLA-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30WPGFLA-WPG | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30WPGFLA-FLA2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30WPGFLA-WPG2 | period_spread |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT30WPGFLA-1 | period_total |  | 0.840 |  | 85 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT30WPGFLA-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT30WPGFLA-3 | period_total |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT30WPGFLA-FLA | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT30WPGFLA-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT30WPGFLA-WPG | period_winner |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT30WPGFLA-FLA2 | period_spread |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT30WPGFLA-WPG2 | period_spread |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT30WPGFLA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT30WPGFLA-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT30WPGFLA-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT30WPGFLA-FLA | period_winner |  | 0.475 |  | 49 | 54 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT30WPGFLA-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT30WPGFLA-WPG | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT30WPGFLA-FLA2 | period_spread |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT30WPGFLA-WPG2 | period_spread |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT30WPGFLA-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT30WPGFLA-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT30WPGFLA-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30WPGFLA-FLAAEKBLAD5-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30WPGFLA-FLAAEKBLAD5-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30WPGFLA-FLAALUNDELL15-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30WPGFLA-FLABTKACHUK8-1 | player_assists |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30WPGFLA-FLABTKACHUK8-2 | player_assists |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT30WPGFLA-FLACVERHAEGHE23-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ FLA | 0.626 | 0.590 | 0.167 | 0.213 | 6.13 | 6.16 | 0.992/0.998 | KXNHLGAME-26OCT30WPGFLA-FLA -0.036 |
| SEA @ CGY | 0.474 | 0.467 | 0.173 | 0.217 | 6.46 | 6.35 | 1.006/1.006 | KXNHLTOTAL-26OCT30SEACGY-6 -0.028 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Brady Tkachuk: 1+ goals NO @ 60c · p 0.6794 (adj 0.6583) · $16.39 · thesis FLA:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 64c · p 0.698 (adj 0.6823) · $13.61 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 68c · p 0.7578 (adj 0.7164) · $11.61 · thesis GAME:TIGHT
- Akira Schmid: 23+ saves YES @ 38c · p 0.4839 (adj 0.4131) · $6.31 · thesis FLA:NET_HIGH_VOLUME
- Berkly Catton: 1+ goals YES @ 18c · p 0.221 (adj 0.2082) · $5.17 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 13c · p 0.1568 (adj 0.1488) · $2.98 · thesis SEA:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2219 (adj 0.2127) · $3.43 · thesis CGY:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 14c · p 0.1718 (adj 0.1588) · $2.75 · thesis SEA:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ FLA** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 25.38, exp saves 22.34 (sd 6.1), pull risk 0.048
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.78 (sd 6.7), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.327 | 0.455 | 46/55 | +0.106 | STANDARD |
| Sam Reinhart: 1+ points | 0.530 | 0.645 | 65/36 | +0.093 | STANDARD |
| Akira Schmid: 23+ saves | 0.484 | 0.375 | 38/63 | +0.087 |  |
| Brady Tkachuk: 1+ points | 0.558 | 0.665 | 67/34 | +0.086 | STANDARD |
| Elias Salomonsson: 1+ points | 0.230 | 0.335 | 34/67 | +0.084 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.481 | 0.585 | 59/42 | +0.082 | STANDARD |

**SEA @ CGY** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.63, exp saves 23.8 (sd 6.59), pull risk 0.065
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.77 (sd 6.82), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 27+ saves | 0.331 | 0.395 | 41/62 | +0.032 |  |
| Brandon Montour: 1+ assists | 0.377 | 0.320 | 33/69 | +0.031 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.172 | 0.120 | 14/90 | +0.023 | STANDARD |
| Berkly Catton: 1+ goals | 0.221 | 0.170 | 18/84 | +0.031 | STANDARD |
| Berkly Catton: 1+ points | 0.440 | 0.390 | 40/62 | +0.023 | STANDARD |
| Joel Farabee: 1+ points | 0.513 | 0.560 | 57/45 | +0.020 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
