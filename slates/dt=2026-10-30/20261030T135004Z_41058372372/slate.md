# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T13:50:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2826 · contracts joined: 643 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 568, 'NO_EDGE': 56, 'OK': 19}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 87, 'game_early_goal': 3, 'first_goal': 97, 'game_winner': 6, 'player_goals': 190, 'game_overtime': 3, 'player_points': 116, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 2026-10-30T22:00:00Z | T-6h | 0.521 | 0.479 | 0.174 | 6.26 | 3.20 | 3.06 | 221 (25/196) | PROJECTED/PROJECTED |
| WPG @ FLA | 2026-10-30T23:00:00Z | T-6h | 0.630 | 0.370 | 0.170 | 6.12 | 3.47 | 2.65 | 203 (25/178) | PROJECTED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-6h | 0.488 | 0.512 | 0.177 | 6.42 | 3.17 | 3.26 | 219 (25/194) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.263 | 0.320 | 0.308 | 33 | 69 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.405 | 0.455 | 0.445 | 46 | 55 | no | +0.028 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.630 | 0.675 | 0.666 | 68 | 33 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.271 | 0.320 | 0.310 | 33 | 69 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.473 | 0.520 | 0.511 | 53 | 49 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.686 | 0.730 | 0.722 | 74 | 28 | no | +0.019 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.370 | 0.335 | 0.342 | 34 | 67 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.860 | 0.890 | 0.885 | 90 | 12 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.181 | 0.155 | 0.160 | 16 | 85 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.131 | 0.160 | 0.154 | 17 | 85 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.135 | 0.115 | 0.119 | 12 | 89 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.962 | 0.975 | 0.973 | 98 | 3 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.763 | 0.785 | 0.781 | 79 | 22 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.550 | 0.575 | 0.570 | 58 | 43 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.797 | 0.820 | 0.816 | 83 | 19 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.850 | 0.865 | 0.862 | 87 | 14 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.736 | 0.715 | 0.719 | 72 | 29 | yes | +0.002 | OK |
| KXNHLSPREAD-26OCT30NJVGK-NJ3 | game_spread | 0.159 | 0.175 | 0.172 | 18 | 83 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.054 | 0.040 | 0.042 | 5 | 97 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.874 | 0.885 | 0.883 | 89 | 12 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.163 | 0.180 | 0.176 | 19 | 83 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.078 | 0.085 | 0.084 | 9 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.102 | 0.090 | 0.092 | 10 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.436 | 0.455 | 0.451 | 46 | 55 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK6 | team_total | 0.102 | 0.090 | 0.092 | 10 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.207 | 0.195 | 0.197 | 20 | 81 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.184 | 0.200 | 0.197 | 21 | 81 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-10 | game_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ6 | team_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-3 | game_total | 0.964 | 0.970 | 0.969 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.110 | 0.100 | 0.102 | 11 | 91 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK3 | game_spread | 0.188 | 0.195 | 0.194 | 20 | 81 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.097 | 0.095 | 0.095 | 10 | 91 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-4 | game_total | 0.861 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-7 | game_total | 0.458 | 0.445 | 0.448 | 45 | 56 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.498 | 0.480 | 0.484 | 49 | 53 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.284 | 0.270 | 0.273 | 28 | 74 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-9 | game_total | 0.191 | 0.180 | 0.182 | 19 | 83 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.830 | 0.845 | 0.842 | 86 | 17 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.218 | 0.230 | 0.228 | 24 | 78 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-5 | game_total | 0.779 | 0.785 | 0.784 | 79 | 22 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK2 | team_total | 0.821 | 0.830 | 0.828 | 84 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK3 | team_total | 0.624 | 0.615 | 0.617 | 62 | 39 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.250 | 0.255 | 0.254 | 26 | 75 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2 | team_total | 0.802 | 0.810 | 0.808 | 82 | 20 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK4 | team_total | 0.413 | 0.400 | 0.403 | 41 | 61 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.300 | 0.295 | 0.296 | 30 | 71 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.598 | 0.605 | 0.604 | 61 | 40 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.639 | 0.645 | 0.644 | 65 | 36 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.488 | 0.495 | 0.494 | 50 | 51 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.398 | 0.410 | 0.408 | 42 | 60 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.289 | 0.280 | 0.282 | 29 | 73 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK5 | team_total | 0.227 | 0.215 | 0.217 | 23 | 80 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-8 | game_total | 0.268 | 0.260 | 0.262 | 27 | 75 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ2 | game_spread | 0.268 | 0.265 | 0.266 | 27 | 74 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-NJ | game_winner | 0.479 | 0.485 | 0.484 | 49 | 52 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-VGK | game_winner | 0.521 | 0.515 | 0.516 | 52 | 49 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.278 | 0.275 | 0.276 | 28 | 73 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.821 | 0.820 | 0.820 | 83 | 19 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ5 | team_total | 0.202 | 0.195 | 0.196 | 21 | 82 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.617 | 0.615 | 0.615 | 62 | 39 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.512 | 0.515 | 0.514 | 52 | 49 |  | -0.020 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK2 | game_spread | 0.305 | 0.305 | 0.305 | 31 | 70 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3 | team_total | 0.596 | 0.595 | 0.595 | 60 | 41 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.484 | 0.485 | 0.485 | 49 | 52 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ4 | team_total | 0.377 | 0.380 | 0.379 | 39 | 63 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.099 | 0.100 | 0.100 | 12 | 92 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.421 | 0.420 | 0.420 | 43 | 59 |  | -0.027 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-6 | game_total | 0.570 | 0.570 | 0.570 | 58 | 44 |  | -0.027 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.235 | 0.235 | 0.235 | 25 | 78 |  | -0.027 | NO_EDGE |
| KXNHL1P-26OCT30NJVGK-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-VGK | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-NJ2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-VGK2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 0.521 | 0.584 | 0.174 | 0.218 | 6.26 | 6.14 | 1.004/0.960 | KXNHLGAME-26OCT30NJVGK-NJ -0.063 |
| WPG @ FLA | 0.630 | 0.594 | 0.170 | 0.212 | 6.12 | 6.19 | 0.999/0.998 | KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 +0.043 |
| SEA @ CGY | 0.488 | 0.475 | 0.177 | 0.218 | 6.42 | 6.34 | 0.998/1.006 | KXNHLTOTAL-26OCT30SEACGY-6 -0.022 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Jack Hughes: 1+ goals NO @ 65c · p 0.7215 (adj 0.7024) · $20.0 · thesis NJD:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0819 (adj 0.0702) · $3.74 · thesis VGK:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 11c · p 0.1363 (adj 0.1272) · $2.8 · thesis NJD:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 51c · p 0.6105 (adj 0.5419) · $8.86 · thesis VGK:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 11c · p 0.1518 (adj 0.1389) · $5.26 · thesis WPG:OFFENSE_4PLUS
- Florida wins by over 1.5 goals NO @ 55c · p 0.6404 (adj 0.5927) · $13.0 · thesis GAME:TIGHT
- Sam Reinhart: 1+ goals NO @ 64c · p 0.696 (adj 0.6783) · $13.42 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 11c · p 0.1414 (adj 0.131) · $4.49 · thesis FLA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 12c · p 0.1533 (adj 0.1437) · $4.37 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 18c · p 0.2107 (adj 0.2018) · $3.38 · thesis SEA:OFFENSE_4PLUS
- Matvei Gridin: 1+ goals NO @ 73c · p 0.7635 (adj 0.7539) · $9.69 · thesis CGY:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ VGK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 27.8, exp saves 24.54 (sd 6.52), pull risk 0.047
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 27.32, exp saves 23.3 (sd 6.55), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.226 | 0.365 | 38/65 | +0.108 | STANDARD |
| Jack Eichel: 1+ points | 0.621 | 0.490 | 70/72 | -0.094 | STANDARD |
| Luke Evangelista: 1+ points | 0.379 | 0.500 | 52/52 | +0.084 | STANDARD |
| Mitch Marner: 1+ points | 0.532 | 0.640 | 66/38 | +0.071 | STANDARD |
| Jack Hughes: 1+ assists | 0.352 | 0.460 | 47/55 | +0.080 | STANDARD |
| Jack Eichel: 1+ assists | 0.449 | 0.555 | 57/46 | +0.074 | STANDARD |

**WPG @ FLA** · priced 151/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 25.38, exp saves 22.33 (sd 6.07), pull risk 0.047
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.74 (sd 6.68), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.328 | 0.460 | 47/55 | +0.105 | STANDARD |
| Brady Tkachuk: 1+ points | 0.560 | 0.670 | 68/34 | +0.084 | STANDARD |
| Brady Tkachuk: 2+ points | 0.201 | 0.305 | 33/72 | +0.065 | STANDARD |
| Sam Reinhart: 2+ points | 0.176 | 0.280 | 32/76 | +0.051 | STANDARD |
| Brady Tkachuk: 1+ goals | 0.317 | 0.420 | 43/59 | +0.076 | STANDARD |
| Sam Reinhart: 1+ points | 0.532 | 0.635 | 65/38 | +0.071 | STANDARD |

**SEA @ CGY** · priced 165/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 27.63, exp saves 23.79 (sd 6.62), pull risk 0.068
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.74 (sd 6.84), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ goals | 0.168 | 0.085 | 16/99 | -0.002 | STANDARD |
| Vince Dunn: 1+ assists | 0.362 | 0.415 | 43/60 | +0.021 | STANDARD |
| Vince Dunn: 1+ points | 0.440 | 0.490 | 50/52 | +0.022 | STANDARD |
| Brandon Montour: 1+ points | 0.458 | 0.415 | 43/60 | +0.011 | STANDARD |
| Joel Farabee: 2+ points | 0.172 | 0.215 | 24/81 | +0.007 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.268 | 0.225 | 25/80 | +0.004 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
