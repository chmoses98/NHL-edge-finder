# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-08T01:49:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 3 · markets on board: 3558 · contracts joined: 685 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 610, 'OK': 50, 'NO_EDGE': 25}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 102, 'game_early_goal': 3, 'first_goal': 108, 'game_winner': 6, 'player_goals': 186, 'game_overtime': 3, 'player_points': 131, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ COL | 2026-11-08T02:00:00Z | T-10m | 0.626 | 0.374 | 0.167 | 6.20 | 3.51 | 2.69 | 239 (25/214) | CONFIRMED/CONFIRMED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-10m | 0.566 | 0.434 | 0.171 | 6.66 | 3.55 | 3.11 | 221 (25/196) | CONFIRMED/CONFIRMED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-60m | 0.734 | 0.266 | 0.139 | 7.19 | 4.43 | 2.76 | 225 (25/200) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV07PITLA-LA3 | team_total | 0.694 | 0.635 | 0.647 | 64 | 37 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA6 | team_total | 0.144 | 0.095 | 0.103 | 10 | 91 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA5 | team_total | 0.288 | 0.235 | 0.245 | 24 | 77 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.477 | 0.535 | 0.523 | 54 | 47 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL2 | team_total | 0.858 | 0.910 | 0.901 | 92 | 10 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.519 | 0.465 | 0.476 | 47 | 54 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.264 | 0.315 | 0.304 | 32 | 69 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.235 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.434 | 0.485 | 0.475 | 49 | 52 | no | +0.028 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.566 | 0.515 | 0.525 | 52 | 49 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.352 | 0.305 | 0.314 | 31 | 70 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.153 | 0.115 | 0.122 | 12 | 89 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL5 | team_total | 0.281 | 0.335 | 0.324 | 35 | 68 | no | +0.024 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.767 | 0.805 | 0.798 | 81 | 20 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV07DETCOL-6 | game_total | 0.563 | 0.605 | 0.597 | 61 | 40 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA2 | team_total | 0.870 | 0.830 | 0.839 | 84 | 18 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA4 | team_total | 0.487 | 0.440 | 0.449 | 45 | 57 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.405 | 0.365 | 0.373 | 37 | 64 | yes | +0.019 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.626 | 0.665 | 0.657 | 67 | 34 | no | +0.018 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.374 | 0.335 | 0.343 | 34 | 67 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07PITLA-6 | game_total | 0.635 | 0.595 | 0.603 | 60 | 41 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.322 | 0.285 | 0.292 | 29 | 72 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV07PITLA-9 | game_total | 0.237 | 0.205 | 0.211 | 21 | 80 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL3 | team_total | 0.691 | 0.735 | 0.727 | 75 | 28 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV07VANEDM-10 | game_total | 0.172 | 0.145 | 0.150 | 15 | 86 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07PITLA-10 | game_total | 0.119 | 0.095 | 0.099 | 10 | 91 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL2 | game_spread | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT3 | game_spread | 0.138 | 0.165 | 0.159 | 17 | 84 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.065 | 0.040 | 0.044 | 5 | 97 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV07DETCOL-7 | game_total | 0.451 | 0.485 | 0.478 | 49 | 52 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV07DETCOL-9 | game_total | 0.181 | 0.210 | 0.204 | 22 | 80 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV07PITLA-4 | game_total | 0.895 | 0.875 | 0.879 | 88 | 13 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV07VANEDM-9 | game_total | 0.302 | 0.275 | 0.280 | 28 | 73 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV07DETCOL-4 | game_total | 0.855 | 0.880 | 0.875 | 89 | 13 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV07DETCOL-8 | game_total | 0.259 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA3 | game_spread | 0.228 | 0.205 | 0.209 | 21 | 80 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM2 | game_spread | 0.539 | 0.565 | 0.560 | 57 | 44 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV07VANEDM-7 | game_total | 0.601 | 0.575 | 0.580 | 58 | 43 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV07VANEDM-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL6 | team_total | 0.138 | 0.160 | 0.155 | 17 | 85 | no | +0.003 | OK |
| KXNHLSPREAD-26NOV07VANEDM-VAN3 | game_spread | 0.067 | 0.055 | 0.057 | 6 | 95 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM4 | team_total | 0.663 | 0.690 | 0.685 | 70 | 32 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM3 | team_total | 0.829 | 0.850 | 0.846 | 86 | 16 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV07VANEDM-VAN2 | game_spread | 0.129 | 0.110 | 0.114 | 12 | 90 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV07PITLA-7 | game_total | 0.519 | 0.495 | 0.500 | 50 | 51 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM2 | team_total | 0.935 | 0.945 | 0.943 | 95 | 6 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV07PITLA-2 | game_total | 0.991 | 0.980 | 0.983 | 99 | 3 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM6 | team_total | 0.283 | 0.265 | 0.269 | 27 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-6 | game_total | 0.713 | 0.695 | 0.699 | 70 | 31 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN2 | team_total | 0.752 | 0.730 | 0.735 | 74 | 28 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-4 | game_total | 0.928 | 0.935 | 0.934 | 94 | 7 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV07PITLA-5 | game_total | 0.826 | 0.810 | 0.813 | 82 | 20 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV07DETCOL-DET2 | game_spread | 0.185 | 0.175 | 0.177 | 18 | 83 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV07PITLA-3 | game_total | 0.976 | 0.970 | 0.971 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07DETCOL-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-3 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26NOV07DETCOL-DET3 | game_spread | 0.099 | 0.095 | 0.096 | 10 | 91 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-5 | game_total | 0.871 | 0.865 | 0.866 | 87 | 14 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV07DETCOL-3 | game_total | 0.965 | 0.975 | 0.973 | 99 | 4 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET5 | team_total | 0.140 | 0.130 | 0.132 | 14 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET2 | team_total | 0.744 | 0.735 | 0.737 | 74 | 27 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV07DETCOL-10 | game_total | 0.084 | 0.090 | 0.089 | 10 | 92 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET6 | team_total | 0.057 | 0.065 | 0.063 | 8 | 95 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT2 | team_total | 0.809 | 0.815 | 0.814 | 82 | 19 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT5 | team_total | 0.212 | 0.215 | 0.214 | 22 | 79 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT4 | team_total | 0.388 | 0.395 | 0.394 | 40 | 61 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET3 | team_total | 0.510 | 0.505 | 0.506 | 51 | 50 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT3 | team_total | 0.598 | 0.595 | 0.596 | 60 | 41 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT6 | team_total | 0.097 | 0.095 | 0.095 | 11 | 92 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET4 | team_total | 0.293 | 0.290 | 0.291 | 30 | 72 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM5 | team_total | 0.465 | 0.470 | 0.469 | 48 | 54 |  | -0.022 | NO_EDGE |
| KXNHL1P-26NOV07DETCOL-COL | period_winner |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07DETCOL-DET | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07DETCOL-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07DETCOL-COL2 | period_spread |  | 0.150 |  | 18 | 88 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07DETCOL-DET2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ COL | 0.626 | 0.658 | 0.167 | 0.200 | 6.20 | 6.51 | 0.979/1.024 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.064 |
| PIT @ LAK | 0.566 | 0.553 | 0.171 | 0.215 | 6.66 | 6.36 | 0.995/1.012 | KXNHLTOTAL-26NOV07PITLA-6 -0.052 |
| VAN @ EDM | 0.734 | 0.670 | 0.139 | 0.190 | 7.19 | 6.99 | 0.994/1.030 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Sheldon Dries: 1+ goals YES @ 7c · p 0.1032 (adj 0.0936) · $4.6 · thesis DET:OFFENSE_4PLUS
- Carter Mazur: 1+ goals YES @ 6c · p 0.0882 (adj 0.0786) · $3.38 · thesis DET:OFFENSE_4PLUS
- Sam Malinski: 1+ assists YES @ 25c · p 0.3227 (adj 0.2838) · $6.25 · thesis COL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 60c · p 0.6752 (adj 0.6326) · $10.92 · thesis DET:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0738 (adj 0.0666) · $3.12 · thesis LAK:OFFENSE_4PLUS
- Kaedan Korczak: 1+ goals YES @ 4c · p 0.0545 (adj 0.0534) · $2.78 · thesis PIT:OFFENSE_4PLUS
- Ben Kindel: 1+ assists NO @ 69c · p 0.7685 (adj 0.7268) · $20.0 · thesis PIT:SUPPRESSED
- Artemi Panarin: 1+ goals NO @ 63c · p 0.6823 (adj 0.668) · $15.42 · thesis LAK:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3483 (adj 0.3262) · $15.42 · thesis EDM:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2205 (adj 0.2041) · $9.31 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 10c · p 0.1436 (adj 0.1302) · $5.78 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 58c · p 0.7356 (adj 0.628) · $19.49 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**DET @ COL** · priced 179/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.53, exp saves 23.45 (sd 6.36), pull risk 0.05
- DET net: Daniil Tarasov (CONFIRMED) exp shots 30.11, exp saves 25.23 (sd 7.23), pull risk 0.099

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.325 | 0.410 | 42/60 | +0.058 | STANDARD |
| Lucas Raymond: 1+ points | 0.493 | 0.575 | 59/44 | +0.050 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.373 | 0.455 | 46/55 | +0.059 | STANDARD |
| Sam Malinski: 1+ assists | 0.323 | 0.245 | 25/76 | +0.060 | STANDARD |
| Sam Malinski: 1+ points | 0.381 | 0.310 | 32/70 | +0.045 | STANDARD |
| Lucas Raymond: 2+ points | 0.155 | 0.225 | 24/79 | +0.043 | STANDARD |

**PIT @ LAK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 27.28, exp saves 23.69 (sd 6.53), pull risk 0.059
- PIT net: Sergei Murashov (CONFIRMED) exp shots 27.6, exp saves 23.56 (sd 6.65), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.418 | 0.525 | 53/48 | +0.085 | STANDARD |
| Artemi Panarin: 2+ points | 0.240 | 0.345 | 35/66 | +0.084 | STANDARD |
| Ben Kindel: 1+ points | 0.378 | 0.465 | 47/54 | +0.065 | STANDARD |
| Ben Kindel: 1+ assists | 0.232 | 0.315 | 32/69 | +0.064 | STANDARD |
| Erik Karlsson: 1+ points | 0.487 | 0.570 | 58/44 | +0.055 | STANDARD |
| Erik Karlsson: 1+ assists | 0.408 | 0.490 | 50/52 | +0.054 | STANDARD |

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.32 (sd 5.93), pull risk 0.052
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.14, exp saves 25.04 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.264 | 0.430 | 44/58 | +0.139 | STANDARD |
| Connor McDavid: 2+ points | 0.513 | 0.640 | 65/37 | +0.100 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.416 | 0.300 | 31/71 | +0.091 | STANDARD |
| Leon Draisaitl: 2+ points | 0.433 | 0.545 | 56/47 | +0.080 | STANDARD |
| Connor McDavid: 3+ points | 0.254 | 0.365 | 39/66 | +0.071 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.187 | 0.295 | 30/71 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
