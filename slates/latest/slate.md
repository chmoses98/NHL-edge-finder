# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T21:04:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2895 · contracts joined: 676 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 601, 'NO_EDGE': 58, 'OK': 17}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 95, 'game_early_goal': 3, 'first_goal': 108, 'game_winner': 6, 'player_goals': 190, 'game_overtime': 3, 'player_points': 128, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'goalie_saves': 2}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 2026-10-30T22:00:00Z | T-30m | 0.522 | 0.478 | 0.175 | 6.24 | 3.18 | 3.06 | 225 (25/200) | PROJECTED/CONFIRMED |
| WPG @ FLA | 2026-10-30T23:00:00Z | T-90m | 0.626 | 0.374 | 0.167 | 6.13 | 3.47 | 2.66 | 222 (25/197) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-90m | 0.474 | 0.526 | 0.173 | 6.46 | 3.16 | 3.30 | 229 (25/204) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.400 | 0.455 | 0.444 | 46 | 55 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.472 | 0.535 | 0.522 | 55 | 48 | no | +0.031 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.626 | 0.675 | 0.665 | 68 | 33 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.860 | 0.900 | 0.893 | 91 | 11 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.687 | 0.735 | 0.726 | 75 | 28 | no | +0.019 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.961 | 0.985 | 0.982 | 99 | 2 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.268 | 0.315 | 0.305 | 33 | 70 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.548 | 0.585 | 0.578 | 59 | 42 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.184 | 0.155 | 0.160 | 16 | 85 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.767 | 0.795 | 0.790 | 80 | 21 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.132 | 0.155 | 0.150 | 16 | 85 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.104 | 0.085 | 0.089 | 9 | 92 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.438 | 0.465 | 0.460 | 47 | 54 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT30NJVGK-NJ3 | game_spread | 0.158 | 0.175 | 0.172 | 18 | 83 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.054 | 0.040 | 0.043 | 5 | 97 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.294 | 0.275 | 0.279 | 28 | 73 |  | -0.000 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.474 | 0.495 | 0.491 | 50 | 51 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.526 | 0.505 | 0.509 | 51 | 50 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.162 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.248 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-9 | game_total | 0.188 | 0.175 | 0.178 | 18 | 83 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.396 | 0.425 | 0.419 | 44 | 59 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK3 | game_spread | 0.182 | 0.195 | 0.192 | 20 | 81 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK4 | team_total | 0.403 | 0.385 | 0.389 | 39 | 62 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK3 | team_total | 0.622 | 0.605 | 0.608 | 61 | 40 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-NJ | game_winner | 0.478 | 0.495 | 0.492 | 50 | 51 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-VGK | game_winner | 0.522 | 0.505 | 0.508 | 51 | 50 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.879 | 0.885 | 0.884 | 89 | 12 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-10 | game_total | 0.089 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.079 | 0.075 | 0.076 | 8 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-3 | game_total | 0.964 | 0.970 | 0.969 | 98 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK6 | team_total | 0.100 | 0.090 | 0.092 | 10 | 92 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.737 | 0.720 | 0.723 | 73 | 29 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.649 | 0.630 | 0.634 | 64 | 38 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.500 | 0.485 | 0.488 | 49 | 52 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-8 | game_total | 0.266 | 0.250 | 0.253 | 26 | 76 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-5 | game_total | 0.776 | 0.785 | 0.783 | 79 | 22 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.286 | 0.270 | 0.273 | 28 | 74 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.098 | 0.095 | 0.096 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.098 | 0.090 | 0.092 | 10 | 92 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-4 | game_total | 0.860 | 0.865 | 0.864 | 87 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.217 | 0.230 | 0.227 | 24 | 78 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.189 | 0.195 | 0.194 | 20 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.820 | 0.825 | 0.824 | 83 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.116 | 0.105 | 0.107 | 12 | 91 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.137 | 0.125 | 0.127 | 14 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.210 | 0.200 | 0.202 | 21 | 81 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.615 | 0.625 | 0.623 | 63 | 38 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.172 | 0.180 | 0.178 | 19 | 83 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.605 | 0.595 | 0.597 | 60 | 41 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.435 | 0.425 | 0.427 | 43 | 58 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.240 | 0.230 | 0.232 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-6 | game_total | 0.564 | 0.555 | 0.557 | 56 | 45 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK2 | game_spread | 0.301 | 0.295 | 0.296 | 30 | 71 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.270 | 0.275 | 0.274 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2 | team_total | 0.803 | 0.810 | 0.809 | 82 | 20 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.310 | 0.305 | 0.306 | 31 | 70 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-7 | game_total | 0.452 | 0.445 | 0.446 | 45 | 56 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ2 | game_spread | 0.272 | 0.275 | 0.274 | 28 | 73 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK5 | team_total | 0.227 | 0.210 | 0.213 | 23 | 81 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.805 | 0.810 | 0.809 | 82 | 20 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ4 | team_total | 0.379 | 0.390 | 0.388 | 40 | 62 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.837 | 0.840 | 0.839 | 85 | 17 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ6 | team_total | 0.090 | 0.085 | 0.086 | 10 | 93 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.491 | 0.485 | 0.486 | 49 | 52 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK2 | team_total | 0.819 | 0.820 | 0.820 | 83 | 19 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ5 | team_total | 0.199 | 0.200 | 0.200 | 21 | 81 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3 | team_total | 0.595 | 0.595 | 0.595 | 60 | 41 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT30NJVGK-NJ | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-VGK | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-NJ2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-VGK2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 0.522 | 0.581 | 0.175 | 0.221 | 6.24 | 6.12 | 1.004/0.950 | KXNHLGAME-26OCT30NJVGK-NJ -0.059 |
| WPG @ FLA | 0.626 | 0.590 | 0.167 | 0.213 | 6.13 | 6.16 | 0.992/0.998 | KXNHLGAME-26OCT30WPGFLA-FLA -0.036 |
| SEA @ CGY | 0.474 | 0.467 | 0.173 | 0.217 | 6.46 | 6.35 | 1.006/1.006 | KXNHLTOTAL-26OCT30SEACGY-6 -0.028 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 5c · p 0.0887 (adj 0.0778) · $5.44 · thesis VGK:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 65c · p 0.7047 (adj 0.6898) · $16.62 · thesis NJD:SUPPRESSED
- Connor Brown: 1+ goals YES @ 13c · p 0.1636 (adj 0.154) · $4.82 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ assists NO @ 55c · p 0.6338 (adj 0.5894) · $13.38 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 59c · p 0.6794 (adj 0.6558) · $14.62 · thesis FLA:SUPPRESSED
- Elias Salomonsson: 1+ goals NO @ 91c · p 0.9499 (adj 0.9387) · $14.62 · thesis WPG:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 63c · p 0.698 (adj 0.6785) · $14.57 · thesis FLA:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 55c · p 0.636 (adj 0.5905) · $6.2 · thesis GAME:TIGHT
- Ben Meyers: 1+ goals YES @ 12c · p 0.1568 (adj 0.1463) · $5.03 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.221 (adj 0.2082) · $5.16 · thesis SEA:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2219 (adj 0.2127) · $3.43 · thesis CGY:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 14c · p 0.1718 (adj 0.1588) · $2.7 · thesis SEA:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ VGK** · priced 169/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 27.8, exp saves 24.48 (sd 6.58), pull risk 0.05
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 27.32, exp saves 23.33 (sd 6.51), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.242 | 0.365 | 37/64 | +0.102 | STANDARD |
| Jack Eichel: 1+ assists | 0.441 | 0.555 | 56/45 | +0.092 | STANDARD |
| Mitch Marner: 1+ assists | 0.400 | 0.510 | 52/50 | +0.082 | STANDARD |
| Luke Evangelista: 1+ points | 0.396 | 0.505 | 51/50 | +0.087 | STANDARD |
| Jack Eichel: 2+ points | 0.251 | 0.355 | 37/66 | +0.073 | STANDARD |
| Jack Hughes: 2+ points | 0.192 | 0.290 | 30/72 | +0.074 | STANDARD |

**WPG @ FLA** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 25.38, exp saves 22.34 (sd 6.1), pull risk 0.048
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.78 (sd 6.7), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.327 | 0.455 | 46/55 | +0.106 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.481 | 0.605 | 61/40 | +0.102 | STANDARD |
| Brady Tkachuk: 2+ points | 0.199 | 0.310 | 32/70 | +0.086 | STANDARD |
| Sam Reinhart: 1+ points | 0.530 | 0.640 | 65/37 | +0.083 | STANDARD |
| Sam Reinhart: 2+ points | 0.171 | 0.280 | 29/73 | +0.085 | STANDARD |
| Brady Tkachuk: 1+ points | 0.558 | 0.665 | 67/34 | +0.086 | STANDARD |

**SEA @ CGY** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.63, exp saves 23.8 (sd 6.59), pull risk 0.065
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.77 (sd 6.82), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 27+ saves | 0.331 | 0.405 | 42/61 | +0.042 |  |
| Berkly Catton: 1+ points | 0.440 | 0.380 | 39/63 | +0.033 | STANDARD |
| Brandon Montour: 1+ assists | 0.377 | 0.320 | 33/69 | +0.031 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.172 | 0.120 | 14/90 | +0.023 | STANDARD |
| Berkly Catton: 1+ goals | 0.221 | 0.170 | 18/84 | +0.031 | STANDARD |
| Jani Nyman: 1+ goals | 0.149 | 0.100 | 13/93 | +0.011 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
