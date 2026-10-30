# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T19:06:00Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2896 · contracts joined: 678 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 603, 'NO_EDGE': 54, 'OK': 21}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 95, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 191, 'game_overtime': 3, 'player_points': 128, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'goalie_saves': 2}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 2026-10-30T22:00:00Z | T-90m | 0.521 | 0.479 | 0.174 | 6.26 | 3.20 | 3.06 | 227 (25/202) | PROJECTED/PROJECTED |
| WPG @ FLA | 2026-10-30T23:00:00Z | T-3h | 0.626 | 0.374 | 0.167 | 6.13 | 3.47 | 2.66 | 222 (25/197) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-3h | 0.474 | 0.526 | 0.173 | 6.46 | 3.16 | 3.30 | 229 (25/204) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.472 | 0.540 | 0.526 | 55 | 47 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.268 | 0.330 | 0.317 | 34 | 68 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.400 | 0.455 | 0.444 | 46 | 55 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.626 | 0.675 | 0.665 | 68 | 33 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.687 | 0.735 | 0.726 | 75 | 28 | no | +0.019 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.548 | 0.585 | 0.578 | 59 | 42 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.184 | 0.155 | 0.160 | 16 | 85 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.860 | 0.895 | 0.889 | 91 | 12 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.767 | 0.795 | 0.790 | 80 | 21 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.132 | 0.155 | 0.150 | 16 | 85 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.104 | 0.085 | 0.089 | 9 | 92 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK4 | team_total | 0.413 | 0.385 | 0.390 | 39 | 62 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.438 | 0.465 | 0.460 | 47 | 54 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT30NJVGK-10 | game_total | 0.090 | 0.075 | 0.078 | 8 | 93 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.500 | 0.475 | 0.480 | 48 | 53 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT30NJVGK-6 | game_total | 0.570 | 0.545 | 0.550 | 55 | 46 | yes | +0.002 | OK |
| KXNHLSPREAD-26OCT30NJVGK-NJ3 | game_spread | 0.159 | 0.175 | 0.172 | 18 | 83 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT30NJVGK-9 | game_total | 0.191 | 0.170 | 0.174 | 18 | 84 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.294 | 0.275 | 0.279 | 28 | 73 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.474 | 0.495 | 0.491 | 50 | 51 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.526 | 0.505 | 0.509 | 51 | 50 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.162 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK3 | team_total | 0.624 | 0.605 | 0.609 | 61 | 40 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.310 | 0.295 | 0.298 | 30 | 71 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.805 | 0.820 | 0.817 | 83 | 19 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-8 | game_total | 0.268 | 0.250 | 0.253 | 26 | 76 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ6 | team_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.879 | 0.885 | 0.884 | 89 | 12 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-NJ | game_winner | 0.479 | 0.495 | 0.492 | 50 | 51 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-VGK | game_winner | 0.521 | 0.505 | 0.508 | 51 | 50 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-3 | game_total | 0.964 | 0.970 | 0.969 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.079 | 0.075 | 0.076 | 8 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.737 | 0.725 | 0.727 | 73 | 28 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.286 | 0.270 | 0.273 | 28 | 74 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.098 | 0.095 | 0.096 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.098 | 0.090 | 0.092 | 10 | 92 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK3 | game_spread | 0.188 | 0.195 | 0.194 | 20 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.217 | 0.230 | 0.227 | 24 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-4 | game_total | 0.861 | 0.865 | 0.864 | 87 | 14 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.189 | 0.200 | 0.198 | 21 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-7 | game_total | 0.458 | 0.445 | 0.448 | 45 | 56 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK2 | game_spread | 0.305 | 0.295 | 0.297 | 30 | 71 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.820 | 0.825 | 0.824 | 83 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.248 | 0.260 | 0.258 | 27 | 75 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.137 | 0.125 | 0.127 | 14 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-5 | game_total | 0.779 | 0.785 | 0.784 | 79 | 22 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.210 | 0.200 | 0.202 | 21 | 81 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ2 | game_spread | 0.268 | 0.275 | 0.274 | 28 | 73 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.615 | 0.625 | 0.623 | 63 | 38 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.605 | 0.595 | 0.597 | 60 | 41 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.240 | 0.230 | 0.232 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.396 | 0.410 | 0.407 | 42 | 60 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ4 | team_total | 0.377 | 0.390 | 0.387 | 40 | 62 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2 | team_total | 0.802 | 0.810 | 0.808 | 82 | 20 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.270 | 0.275 | 0.274 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK6 | team_total | 0.102 | 0.095 | 0.096 | 11 | 92 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK5 | team_total | 0.227 | 0.210 | 0.213 | 23 | 81 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.837 | 0.845 | 0.843 | 86 | 17 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.054 | 0.055 | 0.055 | 7 | 96 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.649 | 0.645 | 0.646 | 65 | 36 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ5 | team_total | 0.202 | 0.200 | 0.200 | 21 | 81 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3 | team_total | 0.596 | 0.595 | 0.595 | 60 | 41 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK2 | team_total | 0.821 | 0.825 | 0.824 | 84 | 19 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.435 | 0.430 | 0.431 | 44 | 58 |  | -0.022 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.491 | 0.490 | 0.490 | 50 | 52 |  | -0.027 | NO_EDGE |
| KXNHL1P-26OCT30NJVGK-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-VGK | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-NJ2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-VGK2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 0.521 | 0.584 | 0.174 | 0.218 | 6.26 | 6.14 | 1.004/0.960 | KXNHLGAME-26OCT30NJVGK-NJ -0.063 |
| WPG @ FLA | 0.626 | 0.590 | 0.167 | 0.213 | 6.13 | 6.16 | 0.992/0.998 | KXNHLGAME-26OCT30WPGFLA-FLA -0.036 |
| SEA @ CGY | 0.474 | 0.467 | 0.173 | 0.217 | 6.46 | 6.35 | 1.006/1.006 | KXNHLTOTAL-26OCT30SEACGY-6 -0.028 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 9 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 5c · p 0.0819 (adj 0.0727) · $4.35 · thesis VGK:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 65c · p 0.7215 (adj 0.7024) · $15.0 · thesis NJD:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 64c · p 0.7736 (adj 0.6835) · $15.0 · thesis NJD:SUPPRESSED
- Connor Brown: 1+ goals YES @ 13c · p 0.1625 (adj 0.1531) · $4.28 · thesis NJD:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 59c · p 0.6794 (adj 0.6558) · $14.62 · thesis FLA:SUPPRESSED
- Elias Salomonsson: 1+ goals NO @ 91c · p 0.9499 (adj 0.9387) · $14.62 · thesis WPG:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 63c · p 0.698 (adj 0.6785) · $14.57 · thesis FLA:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 55c · p 0.636 (adj 0.5905) · $6.2 · thesis GAME:TIGHT
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2219 (adj 0.2127) · $3.6 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ VGK** · priced 175/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 27.8, exp saves 24.54 (sd 6.52), pull risk 0.047
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 27.32, exp saves 23.3 (sd 6.55), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.226 | 0.365 | 37/64 | +0.117 | STANDARD |
| Luke Evangelista: 1+ points | 0.379 | 0.505 | 51/50 | +0.104 | STANDARD |
| Mitch Marner: 1+ assists | 0.390 | 0.510 | 52/50 | +0.093 | STANDARD |
| Jack Hughes: 1+ points | 0.534 | 0.640 | 65/37 | +0.080 | STANDARD |
| Jack Hughes: 1+ assists | 0.352 | 0.455 | 46/55 | +0.080 | STANDARD |
| Jack Eichel: 2+ points | 0.249 | 0.350 | 36/66 | +0.075 | STANDARD |

**WPG @ FLA** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 25.38, exp saves 22.34 (sd 6.1), pull risk 0.048
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.78 (sd 6.7), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.327 | 0.455 | 46/55 | +0.106 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.481 | 0.605 | 61/40 | +0.102 | STANDARD |
| Brady Tkachuk: 2+ points | 0.199 | 0.310 | 32/70 | +0.086 | STANDARD |
| Sam Reinhart: 2+ points | 0.171 | 0.280 | 29/73 | +0.085 | STANDARD |
| Sam Reinhart: 1+ points | 0.530 | 0.635 | 65/38 | +0.073 | STANDARD |
| Brady Tkachuk: 1+ points | 0.558 | 0.655 | 66/35 | +0.076 | STANDARD |

**SEA @ CGY** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.63, exp saves 23.8 (sd 6.59), pull risk 0.065
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.77 (sd 6.82), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 27+ saves | 0.331 | 0.410 | 43/61 | +0.042 |  |
| Freddy Gaudreau: 1+ goals | 0.172 | 0.110 | 14/92 | +0.023 | STANDARD |
| Brandon Montour: 1+ assists | 0.377 | 0.325 | 34/69 | +0.021 | STANDARD |
| Berkly Catton: 1+ points | 0.440 | 0.390 | 40/62 | +0.023 | STANDARD |
| Vince Dunn: 1+ points | 0.435 | 0.485 | 50/53 | +0.017 | STANDARD |
| Vince Dunn: 1+ assists | 0.360 | 0.410 | 42/60 | +0.023 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
