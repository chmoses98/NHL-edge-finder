# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-18T00:50:01Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 3 · markets on board: 3894 · contracts joined: 654 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 579, 'OK': 39, 'NO_EDGE': 36}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 90, 'game_early_goal': 3, 'first_goal': 110, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 109, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ LAK | 2026-10-18T01:00:00Z | T-<10m | 0.511 | 0.489 | 0.187 | 5.60 | 2.83 | 2.77 | 218 (25/193) | PROBABLE/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-60m | 0.560 | 0.440 | 0.169 | 6.72 | 3.56 | 3.16 | 221 (25/196) | PROBABLE/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-60m | 0.600 | 0.400 | 0.156 | 6.86 | 3.78 | 3.09 | 215 (25/190) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.326 | 0.415 | 0.397 | 42 | 59 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.547 | 0.635 | 0.618 | 64 | 37 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.690 | 0.765 | 0.751 | 77 | 24 | no | +0.057 | OK |
| KXNHLGAME-26OCT17BOSLA-BOS | game_winner | 0.489 | 0.415 | 0.430 | 42 | 59 | yes | +0.052 | OK |
| KXNHLGAME-26OCT17BOSLA-LA | game_winner | 0.511 | 0.585 | 0.570 | 59 | 42 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA5 | team_total | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA2 | team_total | 0.772 | 0.835 | 0.824 | 84 | 17 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA3 | game_spread | 0.162 | 0.225 | 0.211 | 23 | 78 | no | +0.046 | OK |
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.400 | 0.335 | 0.348 | 34 | 67 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK3 | game_spread | 0.262 | 0.325 | 0.312 | 33 | 68 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.351 | 0.415 | 0.402 | 42 | 59 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.461 | 0.525 | 0.512 | 53 | 48 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17BOSLA-4 | game_total | 0.790 | 0.845 | 0.835 | 85 | 16 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT5 | team_total | 0.209 | 0.155 | 0.165 | 16 | 85 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT4 | team_total | 0.382 | 0.320 | 0.332 | 33 | 69 | yes | +0.036 | OK |
| KXNHLGAME-26OCT17PITVGK-VGK | game_winner | 0.600 | 0.655 | 0.644 | 66 | 35 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA2 | game_spread | 0.281 | 0.335 | 0.324 | 34 | 67 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT17BOSLA-8 | game_total | 0.180 | 0.225 | 0.215 | 23 | 78 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK2 | game_spread | 0.395 | 0.445 | 0.435 | 45 | 56 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT3 | team_total | 0.594 | 0.545 | 0.555 | 55 | 46 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT17PITVGK-PIT2 | game_spread | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT2 | team_total | 0.804 | 0.765 | 0.773 | 77 | 24 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT17BOSLA-9 | game_total | 0.120 | 0.155 | 0.147 | 16 | 85 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA6 | team_total | 0.064 | 0.095 | 0.088 | 10 | 91 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT6 | team_total | 0.095 | 0.065 | 0.070 | 7 | 94 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT17BOSLA-3 | game_total | 0.942 | 0.965 | 0.961 | 97 | 4 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT17PITVGK-10 | game_total | 0.138 | 0.115 | 0.119 | 12 | 89 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT17PITVGK-8 | game_total | 0.356 | 0.325 | 0.331 | 33 | 68 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT17PITVGK-9 | game_total | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT17BOSLA-BOS2 | game_spread | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-8 | game_total | 0.333 | 0.305 | 0.310 | 31 | 70 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT17PITVGK-PIT3 | game_spread | 0.124 | 0.100 | 0.105 | 11 | 91 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT17BOSLA-10 | game_total | 0.049 | 0.070 | 0.065 | 8 | 94 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT17BOSLA-2 | game_total | 0.973 | 0.985 | 0.983 | 99 | 2 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-9 | game_total | 0.245 | 0.225 | 0.229 | 23 | 78 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT17EDMUTA-EDM3 | game_spread | 0.148 | 0.165 | 0.162 | 17 | 84 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT17EDMUTA-10 | game_total | 0.129 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT17PITVGK-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK4 | team_total | 0.533 | 0.555 | 0.551 | 56 | 45 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT17PITVGK-4 | game_total | 0.906 | 0.895 | 0.897 | 90 | 11 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK5 | team_total | 0.336 | 0.360 | 0.355 | 37 | 65 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM6 | team_total | 0.104 | 0.090 | 0.093 | 10 | 92 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT17BOSLA-BOS3 | game_spread | 0.146 | 0.135 | 0.137 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17BOSLA-BOS6 | team_total | 0.059 | 0.065 | 0.064 | 7 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-6 | game_total | 0.662 | 0.645 | 0.648 | 65 | 36 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-7 | game_total | 0.553 | 0.535 | 0.539 | 54 | 47 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-5 | game_total | 0.825 | 0.835 | 0.833 | 84 | 17 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK3 | team_total | 0.732 | 0.750 | 0.746 | 76 | 26 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK2 | team_total | 0.888 | 0.905 | 0.902 | 92 | 11 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-6 | game_total | 0.640 | 0.625 | 0.628 | 63 | 38 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT17EDMUTA-UTA3 | game_spread | 0.224 | 0.235 | 0.233 | 24 | 77 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT17PITVGK-5 | game_total | 0.843 | 0.835 | 0.837 | 84 | 17 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA3 | team_total | 0.698 | 0.680 | 0.684 | 69 | 33 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM5 | team_total | 0.224 | 0.215 | 0.217 | 22 | 79 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17BOSLA-BOS4 | team_total | 0.313 | 0.325 | 0.323 | 33 | 68 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-3 | game_total | 0.977 | 0.980 | 0.979 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA6 | team_total | 0.149 | 0.140 | 0.142 | 15 | 87 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA4 | team_total | 0.488 | 0.475 | 0.478 | 48 | 53 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK6 | team_total | 0.180 | 0.190 | 0.188 | 20 | 82 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17BOSLA-BOS2 | team_total | 0.758 | 0.770 | 0.768 | 78 | 24 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-4 | game_total | 0.895 | 0.900 | 0.899 | 91 | 11 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17BOSLA-BOS3 | team_total | 0.534 | 0.545 | 0.543 | 55 | 46 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM2 | team_total | 0.812 | 0.820 | 0.818 | 83 | 19 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA2 | team_total | 0.865 | 0.875 | 0.873 | 89 | 14 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT17EDMUTA-EDM2 | game_spread | 0.243 | 0.245 | 0.245 | 25 | 76 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT17EDMUTA-UTA2 | game_spread | 0.349 | 0.345 | 0.346 | 35 | 66 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17BOSLA-BOS5 | team_total | 0.149 | 0.150 | 0.150 | 16 | 86 |  | -0.017 | NO_EDGE |
| KXNHLGAME-26OCT17EDMUTA-UTA | game_winner | 0.560 | 0.565 | 0.564 | 57 | 44 |  | -0.017 | NO_EDGE |
| KXNHLGAME-26OCT17EDMUTA-EDM | game_winner | 0.440 | 0.435 | 0.436 | 44 | 57 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-UTA5 | team_total | 0.287 | 0.280 | 0.281 | 29 | 73 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT17EDMUTA-7 | game_total | 0.530 | 0.525 | 0.526 | 53 | 48 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 | team_total | 0.399 | 0.395 | 0.396 | 40 | 61 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM3 | team_total | 0.612 | 0.615 | 0.614 | 62 | 39 |  | -0.019 | NO_EDGE |
| KXNHL1P-26OCT17BOSLA-BOS | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT17BOSLA-LA | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT17BOSLA-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT17BOSLA-BOS2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT17BOSLA-LA2 | period_spread |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ LAK | 0.511 | 0.540 | 0.187 | 0.222 | 5.60 | 6.05 | 0.988/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.560 | 0.528 | 0.169 | 0.214 | 6.72 | 6.89 | 0.991/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.047 |
| PIT @ VGK | 0.600 | 0.630 | 0.156 | 0.204 | 6.86 | 6.49 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-6 -0.061 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Tanner Jeannot: 1+ goals YES @ 7c · p 0.1009 (adj 0.0907) · $4.06 · thesis BOS:OFFENSE_4PLUS
- Artemi Panarin: 2+ assists NO @ 84c · p 0.9078 (adj 0.8664) · $20.0 · thesis LAK:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 59c · p 0.6746 (adj 0.6298) · $18.77 · thesis BOS:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 19c · p 0.2332 (adj 0.2186) · $6.49 · thesis BOS:OFFENSE_4PLUS
- Nate Schmidt: 1+ goals YES @ 4c · p 0.0666 (adj 0.0575) · $3.22 · thesis UTA:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 71c · p 0.7978 (adj 0.7514) · $20.0 · thesis EDM:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 20c · p 0.2454 (adj 0.2328) · $6.56 · thesis UTA:OFFENSE_4PLUS
- Zach Hyman: 1+ goals YES @ 31c · p 0.358 (adj 0.3448) · $8.94 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7344 (adj 0.7196) · $17.87 · thesis VGK:SUPPRESSED
- Evgeni Malkin: 1+ assists NO @ 63c · p 0.7155 (adj 0.6703) · $15.54 · thesis PIT:SUPPRESSED
- Adin Hill: 22+ saves YES @ 48c · p 0.6173 (adj 0.5216) · $10.7 · thesis VGK:NET_HIGH_VOLUME
- Bryan Rust: 1+ goals YES @ 24c · p 0.286 (adj 0.272) · $5.89 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BOS @ LAK** · priced 159/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROBABLE) exp shots 25.88, exp saves 22.58 (sd 6.19), pull risk 0.052
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.56 (sd 6.91), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.395 | 0.530 | 54/48 | +0.108 | STANDARD |
| Artemi Panarin: 2+ points | 0.225 | 0.335 | 35/68 | +0.080 | STANDARD |
| Marat Khusnutdinov: 1+ points | 0.344 | 0.250 | 26/76 | +0.070 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.321 | 0.230 | 25/79 | +0.058 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.325 | 0.415 | 42/59 | +0.068 | STANDARD |
| Artemi Panarin: 2+ assists | 0.092 | 0.175 | 19/84 | +0.058 | STANDARD |

**EDM @ UTA** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 27.03, exp saves 23.36 (sd 6.59), pull risk 0.068
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.563 | 0.685 | 69/32 | +0.101 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.229 | 0.350 | 36/66 | +0.095 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.450 | 0.565 | 58/45 | +0.083 | STANDARD |
| Mattias Ekholm: 1+ points | 0.432 | 0.320 | 33/69 | +0.087 | STANDARD |
| Connor McDavid: 2+ points | 0.380 | 0.490 | 50/52 | +0.082 | STANDARD |
| Leon Draisaitl: 2+ points | 0.286 | 0.390 | 40/62 | +0.077 | STANDARD |

**PIT @ VGK** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.53, exp saves 23.38 (sd 6.31), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.77), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adin Hill: 22+ saves | 0.617 | 0.470 | 48/54 | +0.120 |  |
| Jack Eichel: 1+ assists | 0.469 | 0.615 | 62/39 | +0.125 | STANDARD |
| Jack Eichel: 2+ points | 0.277 | 0.420 | 43/59 | +0.116 | STANDARD |
| Jack Eichel: 1+ points | 0.639 | 0.765 | 77/24 | +0.108 | STANDARD |
| Mitch Marner: 2+ points | 0.227 | 0.345 | 36/67 | +0.087 | STANDARD |
| Jack Eichel: 2+ assists | 0.139 | 0.255 | 26/75 | +0.098 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
