# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T12:54:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2826 · contracts joined: 643 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 568, 'NO_EDGE': 50, 'OK': 25}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 87, 'game_early_goal': 3, 'first_goal': 97, 'game_winner': 6, 'player_goals': 190, 'game_overtime': 3, 'player_points': 116, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 2026-10-30T22:00:00Z | T-6h | 0.516 | 0.484 | 0.179 | 6.23 | 3.18 | 3.05 | 221 (25/196) | PROJECTED/PROJECTED |
| WPG @ FLA | 2026-10-30T23:00:00Z | T-6h | 0.602 | 0.398 | 0.172 | 6.04 | 3.34 | 2.70 | 203 (25/178) | PROJECTED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-6h | 0.485 | 0.515 | 0.174 | 6.38 | 3.14 | 3.24 | 219 (25/194) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.239 | 0.335 | 0.314 | 34 | 67 | no | +0.076 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.377 | 0.455 | 0.439 | 46 | 55 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.243 | 0.325 | 0.307 | 34 | 69 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.442 | 0.525 | 0.508 | 54 | 49 | no | +0.050 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.602 | 0.665 | 0.653 | 67 | 34 | no | +0.043 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.398 | 0.335 | 0.347 | 34 | 67 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.665 | 0.735 | 0.722 | 75 | 28 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.201 | 0.155 | 0.163 | 16 | 85 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.114 | 0.155 | 0.146 | 16 | 85 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.844 | 0.875 | 0.869 | 88 | 13 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.536 | 0.575 | 0.567 | 58 | 43 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.754 | 0.785 | 0.779 | 79 | 22 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.421 | 0.455 | 0.448 | 46 | 55 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.843 | 0.865 | 0.861 | 87 | 14 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.960 | 0.975 | 0.973 | 98 | 3 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.741 | 0.715 | 0.720 | 72 | 29 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.144 | 0.120 | 0.124 | 13 | 89 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.794 | 0.820 | 0.815 | 83 | 19 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.058 | 0.040 | 0.043 | 5 | 97 | yes | +0.004 | OK |
| KXNHLSPREAD-26OCT30NJVGK-NJ3 | game_spread | 0.156 | 0.175 | 0.171 | 18 | 83 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.110 | 0.095 | 0.098 | 10 | 91 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.072 | 0.085 | 0.082 | 9 | 92 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.870 | 0.885 | 0.882 | 89 | 12 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.295 | 0.265 | 0.271 | 28 | 75 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.236 | 0.255 | 0.251 | 26 | 75 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.160 | 0.175 | 0.172 | 18 | 83 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK2 | team_total | 0.821 | 0.835 | 0.832 | 84 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.506 | 0.480 | 0.485 | 49 | 53 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK3 | game_spread | 0.182 | 0.195 | 0.192 | 20 | 81 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.182 | 0.195 | 0.192 | 20 | 81 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-4 | game_total | 0.856 | 0.870 | 0.867 | 88 | 14 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-3 | game_total | 0.963 | 0.970 | 0.969 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-5 | game_total | 0.774 | 0.785 | 0.783 | 79 | 22 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK6 | team_total | 0.100 | 0.090 | 0.092 | 10 | 92 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ6 | team_total | 0.088 | 0.080 | 0.082 | 9 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.818 | 0.825 | 0.824 | 83 | 18 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.108 | 0.100 | 0.102 | 11 | 91 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-10 | game_total | 0.087 | 0.080 | 0.081 | 9 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.097 | 0.090 | 0.091 | 10 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.097 | 0.090 | 0.091 | 10 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.593 | 0.605 | 0.603 | 61 | 40 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.830 | 0.845 | 0.842 | 86 | 17 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.201 | 0.195 | 0.196 | 20 | 81 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-8 | game_total | 0.263 | 0.255 | 0.257 | 26 | 75 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.296 | 0.305 | 0.303 | 31 | 70 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2 | team_total | 0.800 | 0.810 | 0.808 | 82 | 20 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-7 | game_total | 0.455 | 0.445 | 0.447 | 45 | 56 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.485 | 0.495 | 0.493 | 50 | 51 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.212 | 0.220 | 0.218 | 23 | 79 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.271 | 0.275 | 0.274 | 28 | 73 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-9 | game_total | 0.185 | 0.180 | 0.181 | 19 | 83 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.481 | 0.475 | 0.476 | 48 | 53 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ2 | game_spread | 0.265 | 0.265 | 0.265 | 27 | 74 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK2 | game_spread | 0.304 | 0.305 | 0.305 | 31 | 70 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.613 | 0.615 | 0.615 | 62 | 39 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK4 | team_total | 0.404 | 0.405 | 0.405 | 41 | 60 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK5 | team_total | 0.222 | 0.215 | 0.216 | 23 | 80 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3 | team_total | 0.596 | 0.595 | 0.595 | 60 | 41 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.414 | 0.420 | 0.419 | 43 | 59 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.635 | 0.640 | 0.639 | 65 | 37 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.395 | 0.395 | 0.395 | 40 | 61 |  | -0.022 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-NJ | game_winner | 0.484 | 0.485 | 0.485 | 49 | 52 |  | -0.022 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-VGK | game_winner | 0.516 | 0.515 | 0.515 | 52 | 49 |  | -0.022 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.515 | 0.515 | 0.515 | 52 | 49 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.231 | 0.235 | 0.234 | 25 | 78 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ4 | team_total | 0.377 | 0.380 | 0.379 | 39 | 63 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK3 | team_total | 0.623 | 0.620 | 0.621 | 63 | 39 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ5 | team_total | 0.198 | 0.195 | 0.196 | 21 | 82 |  | -0.024 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.281 | 0.280 | 0.280 | 29 | 73 |  | -0.024 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-6 | game_total | 0.569 | 0.570 | 0.570 | 58 | 44 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT30NJVGK-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-VGK | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-NJ2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-VGK2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 0.516 | 0.585 | 0.179 | 0.215 | 6.23 | 6.10 | 1.004/0.960 | KXNHLGAME-26OCT30NJVGK-VGK +0.069 |
| WPG @ FLA | 0.602 | 0.569 | 0.172 | 0.214 | 6.04 | 6.12 | 0.999/0.998 | KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 +0.049 |
| SEA @ CGY | 0.485 | 0.471 | 0.174 | 0.218 | 6.38 | 6.30 | 0.998/1.006 | KXNHLTOTAL-26OCT30SEACGY-6 -0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 9 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 5c · p 0.0832 (adj 0.0711) · $3.99 · thesis VGK:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 65c · p 0.7191 (adj 0.6993) · $20.0 · thesis NJD:SUPPRESSED
- Mitch Marner: 1+ assists NO @ 50c · p 0.6135 (adj 0.5332) · $9.25 · thesis VGK:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 70c · p 0.7365 (adj 0.7249) · $9.2 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 60c · p 0.686 (adj 0.662) · $15.0 · thesis FLA:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7111 (adj 0.6896) · $15.0 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 67c · p 0.7816 (adj 0.7058) · $10.26 · thesis GAME:TIGHT
- Gabriel Vilardi: 1+ goals YES @ 23c · p 0.266 (adj 0.2558) · $3.28 · thesis WPG:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 12c · p 0.1496 (adj 0.141) · $3.67 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ VGK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 27.8, exp saves 24.49 (sd 6.53), pull risk 0.047
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 27.32, exp saves 23.32 (sd 6.56), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ points | 0.526 | 0.660 | 67/35 | +0.108 | STANDARD |
| Luke Evangelista: 1+ assists | 0.231 | 0.365 | 38/65 | +0.103 | STANDARD |
| Mitch Marner: 1+ assists | 0.387 | 0.510 | 52/50 | +0.096 | STANDARD |
| Jack Eichel: 1+ assists | 0.444 | 0.560 | 57/45 | +0.088 | STANDARD |
| Jack Hughes: 1+ points | 0.532 | 0.645 | 66/37 | +0.082 | STANDARD |
| Jack Hughes: 1+ assists | 0.349 | 0.455 | 46/55 | +0.084 | STANDARD |

**WPG @ FLA** · priced 151/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 25.38, exp saves 22.27 (sd 6.04), pull risk 0.05
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.77 (sd 6.66), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.520 | 0.650 | 66/36 | +0.104 | STANDARD |
| Sam Reinhart: 1+ assists | 0.325 | 0.455 | 47/56 | +0.097 | STANDARD |
| Brady Tkachuk: 1+ points | 0.553 | 0.670 | 68/34 | +0.091 | STANDARD |
| Brady Tkachuk: 2+ points | 0.192 | 0.300 | 33/73 | +0.065 | STANDARD |
| Matthew Tkachuk: 1+ points | 0.642 | 0.540 | 73/65 | -0.101 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.479 | 0.575 | 59/44 | +0.064 | STANDARD |

**SEA @ CGY** · priced 165/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 27.63, exp saves 23.77 (sd 6.63), pull risk 0.068
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.79 (sd 6.81), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.160 | 0.085 | 16/99 | -0.009 | STANDARD |
| Vince Dunn: 1+ assists | 0.350 | 0.415 | 43/60 | +0.033 | STANDARD |
| Vince Dunn: 1+ points | 0.428 | 0.490 | 50/52 | +0.035 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.274 | 0.225 | 25/80 | +0.011 | STANDARD |
| Matty Beniers: 1+ assists | 0.309 | 0.355 | 37/66 | +0.016 | STANDARD |
| Brandon Montour: 1+ points | 0.460 | 0.415 | 43/60 | +0.012 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
