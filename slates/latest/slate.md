# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T16:52:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2840 · contracts joined: 657 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 582, 'NO_EDGE': 55, 'OK': 20}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 92, 'game_early_goal': 3, 'first_goal': 97, 'game_winner': 6, 'player_goals': 191, 'game_overtime': 3, 'player_points': 122, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'goalie_saves': 2}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 2026-10-30T22:00:00Z | T-3h | 0.521 | 0.479 | 0.174 | 6.26 | 3.20 | 3.06 | 221 (25/196) | PROJECTED/PROJECTED |
| WPG @ FLA | 2026-10-30T23:00:00Z | T-6h | 0.626 | 0.374 | 0.167 | 6.13 | 3.47 | 2.66 | 207 (25/182) | CONFIRMED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-6h | 0.474 | 0.526 | 0.173 | 6.46 | 3.16 | 3.30 | 229 (25/204) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.472 | 0.540 | 0.526 | 55 | 47 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.400 | 0.455 | 0.444 | 46 | 55 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.263 | 0.320 | 0.308 | 33 | 69 | no | +0.032 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.626 | 0.675 | 0.665 | 68 | 33 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.268 | 0.325 | 0.313 | 34 | 69 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.687 | 0.735 | 0.726 | 75 | 28 | no | +0.019 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.548 | 0.585 | 0.578 | 59 | 42 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.184 | 0.155 | 0.160 | 16 | 85 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.860 | 0.895 | 0.889 | 91 | 12 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.137 | 0.110 | 0.115 | 12 | 90 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.132 | 0.160 | 0.154 | 17 | 85 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK4 | team_total | 0.413 | 0.385 | 0.390 | 39 | 62 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.438 | 0.465 | 0.460 | 47 | 54 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.500 | 0.475 | 0.480 | 48 | 53 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.054 | 0.045 | 0.047 | 5 | 96 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.767 | 0.790 | 0.786 | 80 | 22 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT30NJVGK-NJ3 | game_spread | 0.159 | 0.175 | 0.172 | 18 | 83 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT30NJVGK-9 | game_total | 0.191 | 0.175 | 0.178 | 18 | 83 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.294 | 0.275 | 0.279 | 28 | 73 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.162 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.248 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.104 | 0.095 | 0.097 | 10 | 91 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK3 | team_total | 0.624 | 0.605 | 0.609 | 61 | 40 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.079 | 0.085 | 0.084 | 9 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK6 | team_total | 0.102 | 0.090 | 0.092 | 10 | 92 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.310 | 0.295 | 0.298 | 30 | 71 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.805 | 0.820 | 0.817 | 83 | 19 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-8 | game_total | 0.268 | 0.250 | 0.253 | 26 | 76 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-10 | game_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.837 | 0.850 | 0.847 | 86 | 16 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ6 | team_total | 0.090 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.879 | 0.885 | 0.884 | 89 | 12 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-VGK | game_winner | 0.521 | 0.505 | 0.508 | 51 | 50 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-3 | game_total | 0.964 | 0.970 | 0.969 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.737 | 0.720 | 0.723 | 73 | 29 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-6 | game_total | 0.570 | 0.555 | 0.558 | 56 | 45 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.286 | 0.265 | 0.269 | 28 | 75 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.098 | 0.095 | 0.096 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK3 | game_spread | 0.188 | 0.195 | 0.194 | 20 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.217 | 0.230 | 0.227 | 24 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-4 | game_total | 0.861 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.189 | 0.200 | 0.198 | 21 | 81 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-7 | game_total | 0.458 | 0.445 | 0.448 | 45 | 56 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.820 | 0.825 | 0.824 | 83 | 18 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.474 | 0.485 | 0.483 | 49 | 52 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.526 | 0.515 | 0.517 | 52 | 49 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-5 | game_total | 0.779 | 0.785 | 0.784 | 79 | 22 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.210 | 0.205 | 0.206 | 21 | 80 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK2 | team_total | 0.821 | 0.830 | 0.828 | 84 | 18 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ2 | game_spread | 0.268 | 0.275 | 0.274 | 28 | 73 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.605 | 0.595 | 0.597 | 60 | 41 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.435 | 0.425 | 0.427 | 43 | 58 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3 | team_total | 0.596 | 0.605 | 0.603 | 61 | 40 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.240 | 0.230 | 0.232 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.396 | 0.410 | 0.407 | 42 | 60 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ4 | team_total | 0.377 | 0.390 | 0.387 | 40 | 62 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2 | team_total | 0.802 | 0.810 | 0.808 | 82 | 20 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.270 | 0.275 | 0.274 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK5 | team_total | 0.227 | 0.215 | 0.217 | 23 | 80 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-NJ | game_winner | 0.479 | 0.485 | 0.484 | 49 | 52 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.649 | 0.645 | 0.646 | 65 | 36 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.098 | 0.095 | 0.096 | 11 | 92 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ5 | team_total | 0.202 | 0.200 | 0.200 | 21 | 81 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK2 | game_spread | 0.305 | 0.305 | 0.305 | 31 | 70 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.615 | 0.615 | 0.615 | 62 | 39 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.491 | 0.490 | 0.490 | 50 | 52 |  | -0.027 | NO_EDGE |
| KXNHL1P-26OCT30NJVGK-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-VGK | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-NJ2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-VGK2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 0.521 | 0.584 | 0.174 | 0.218 | 6.26 | 6.14 | 1.004/0.960 | KXNHLGAME-26OCT30NJVGK-NJ -0.063 |
| WPG @ FLA | 0.626 | 0.590 | 0.167 | 0.213 | 6.13 | 6.16 | 0.992/0.998 | KXNHLGAME-26OCT30WPGFLA-FLA -0.036 |
| SEA @ CGY | 0.474 | 0.471 | 0.173 | 0.211 | 6.46 | 6.35 | 1.006/1.006 | KXNHLTOTAL-26OCT30SEACGY-6 -0.021 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Jack Hughes: 1+ goals NO @ 65c · p 0.7215 (adj 0.7024) · $15.08 · thesis NJD:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 64c · p 0.7736 (adj 0.6835) · $14.92 · thesis NJD:SUPPRESSED
- Connor Brown: 1+ goals YES @ 13c · p 0.1625 (adj 0.1531) · $4.08 · thesis NJD:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 73c · p 0.7881 (adj 0.7566) · $9.37 · thesis VGK:WINS
- Brady Tkachuk: 1+ goals NO @ 59c · p 0.6794 (adj 0.6558) · $20.0 · thesis FLA:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 11c · p 0.1489 (adj 0.1367) · $5.38 · thesis WPG:OFFENSE_4PLUS
- Elias Salomonsson: 1+ assists NO @ 75c · p 0.8098 (adj 0.7774) · $19.59 · thesis WPG:SUPPRESSED
- Mark Scheifele: 1+ goals YES @ 28c · p 0.3154 (adj 0.3053) · $4.4 · thesis WPG:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 12c · p 0.1566 (adj 0.1462) · $5.09 · thesis SEA:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.133 (adj 0.1198) · $3.42 · thesis CGY:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 19c · p 0.2213 (adj 0.2122) · $3.5 · thesis CGY:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ VGK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 27.8, exp saves 24.54 (sd 6.52), pull risk 0.047
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 27.32, exp saves 23.3 (sd 6.55), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.226 | 0.365 | 37/64 | +0.117 | STANDARD |
| Luke Evangelista: 1+ points | 0.379 | 0.500 | 51/51 | +0.094 | STANDARD |
| Mitch Marner: 1+ assists | 0.390 | 0.505 | 52/51 | +0.083 | STANDARD |
| Jack Hughes: 1+ assists | 0.352 | 0.455 | 46/55 | +0.080 | STANDARD |
| Jack Hughes: 1+ points | 0.534 | 0.635 | 64/37 | +0.080 | STANDARD |
| Mitch Marner: 1+ points | 0.532 | 0.630 | 64/38 | +0.071 | STANDARD |

**WPG @ FLA** · priced 155/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 25.38, exp saves 22.34 (sd 6.1), pull risk 0.048
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.78 (sd 6.7), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.327 | 0.455 | 47/56 | +0.096 | STANDARD |
| Sam Reinhart: 2+ points | 0.171 | 0.285 | 30/73 | +0.085 | STANDARD |
| Brady Tkachuk: 2+ points | 0.199 | 0.305 | 32/71 | +0.076 | STANDARD |
| Sam Reinhart: 1+ points | 0.530 | 0.630 | 65/39 | +0.063 | STANDARD |
| Brady Tkachuk: 1+ goals | 0.321 | 0.415 | 42/59 | +0.072 | STANDARD |
| Brady Tkachuk: 1+ points | 0.558 | 0.650 | 66/36 | +0.066 | STANDARD |

**SEA @ CGY** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.63, exp saves 23.76 (sd 6.63), pull risk 0.066
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.76 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dustin Wolf: 27+ saves | 0.329 | 0.400 | 41/61 | +0.044 |  |
| Matt Coronato: 2+ points | 0.178 | 0.235 | 25/78 | +0.030 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.175 | 0.120 | 16/92 | +0.005 | STANDARD |
| Jonathan Castagna: 1+ goals | 0.133 | 0.080 | 10/94 | +0.027 | PRIOR_HEAVY |
| Berkly Catton: 1+ points | 0.437 | 0.385 | 41/64 | +0.010 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.357 | 0.310 | 32/70 | +0.022 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
