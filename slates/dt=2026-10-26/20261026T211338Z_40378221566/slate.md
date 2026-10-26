# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-26T21:13:38Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2902 · contracts joined: 685 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 610, 'OK': 45, 'NO_EDGE': 30}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 99, 'game_early_goal': 3, 'first_goal': 108, 'game_winner': 6, 'player_goals': 185, 'game_overtime': 3, 'player_points': 135, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 2026-10-26T23:00:00Z | T-90m | 0.595 | 0.405 | 0.177 | 6.12 | 3.35 | 2.77 | 217 (25/192) | CONFIRMED/PROBABLE |
| TOR @ CGY | 2026-10-27T00:30:00Z | T-3h | 0.555 | 0.445 | 0.173 | 6.33 | 3.33 | 3.00 | 237 (25/212) | CONFIRMED/PROBABLE |
| DET @ EDM | 2026-10-27T01:30:00Z | T-3h | 0.607 | 0.393 | 0.166 | 6.55 | 3.63 | 2.93 | 231 (25/206) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.361 | 0.490 | 0.464 | 50 | 52 | no | +0.101 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.445 | 0.555 | 0.533 | 56 | 45 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.579 | 0.695 | 0.673 | 71 | 32 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.246 | 0.345 | 0.324 | 35 | 66 | no | +0.079 | OK |
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.555 | 0.455 | 0.475 | 46 | 55 | yes | +0.078 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.142 | 0.235 | 0.214 | 24 | 77 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.332 | 0.245 | 0.261 | 25 | 76 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.191 | 0.280 | 0.260 | 29 | 73 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.792 | 0.870 | 0.857 | 88 | 14 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.866 | 0.915 | 0.907 | 92 | 9 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.206 | 0.155 | 0.164 | 16 | 85 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.784 | 0.840 | 0.830 | 85 | 17 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.469 | 0.525 | 0.514 | 53 | 48 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA3 | game_spread | 0.110 | 0.155 | 0.145 | 16 | 85 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.811 | 0.855 | 0.847 | 86 | 15 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.654 | 0.605 | 0.615 | 61 | 40 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.086 | 0.130 | 0.120 | 14 | 88 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.441 | 0.395 | 0.404 | 40 | 61 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.580 | 0.630 | 0.620 | 64 | 38 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.199 | 0.235 | 0.227 | 24 | 77 | no | +0.019 | OK |
| KXNHLGAME-26OCT26LANYR-LA | game_winner | 0.405 | 0.445 | 0.437 | 45 | 56 | no | +0.018 | OK |
| KXNHLGAME-26OCT26LANYR-NYR | game_winner | 0.595 | 0.555 | 0.563 | 56 | 45 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR3 | team_total | 0.664 | 0.625 | 0.633 | 63 | 38 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT26LANYR-10 | game_total | 0.081 | 0.055 | 0.059 | 6 | 95 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.618 | 0.655 | 0.648 | 66 | 35 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.507 | 0.545 | 0.537 | 55 | 46 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.279 | 0.320 | 0.312 | 33 | 69 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.302 | 0.335 | 0.328 | 34 | 67 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA2 | game_spread | 0.206 | 0.240 | 0.233 | 25 | 77 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR6 | team_total | 0.117 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR4 | team_total | 0.447 | 0.415 | 0.421 | 42 | 59 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR2 | game_spread | 0.365 | 0.335 | 0.341 | 34 | 67 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.884 | 0.905 | 0.901 | 91 | 10 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.839 | 0.815 | 0.820 | 82 | 19 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR5 | team_total | 0.250 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.249 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.259 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT26LANYR-8 | game_total | 0.248 | 0.220 | 0.225 | 23 | 79 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA4 | team_total | 0.311 | 0.335 | 0.330 | 34 | 67 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.713 | 0.740 | 0.735 | 75 | 27 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA2 | team_total | 0.756 | 0.775 | 0.771 | 78 | 23 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.990 | 0.990 |  | 1 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.967 | 0.975 | 0.974 | 98 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.872 | 0.885 | 0.883 | 89 | 12 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA3 | team_total | 0.524 | 0.550 | 0.545 | 56 | 46 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.095 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.345 | 0.365 | 0.361 | 37 | 64 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.116 | 0.125 | 0.123 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR2 | team_total | 0.846 | 0.835 | 0.837 | 84 | 17 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-2 | game_total | 0.982 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.112 | 0.105 | 0.106 | 11 | 90 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT26LANYR-NYR3 | game_spread | 0.227 | 0.215 | 0.217 | 22 | 79 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.389 | 0.405 | 0.402 | 41 | 60 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-6 | game_total | 0.551 | 0.535 | 0.538 | 54 | 47 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-4 | game_total | 0.848 | 0.855 | 0.854 | 86 | 15 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-9 | game_total | 0.173 | 0.160 | 0.162 | 17 | 85 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.225 | 0.240 | 0.237 | 25 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.077 | 0.075 | 0.075 | 8 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.313 | 0.325 | 0.323 | 33 | 68 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.562 | 0.580 | 0.576 | 59 | 43 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.180 | 0.190 | 0.188 | 20 | 82 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA5 | team_total | 0.151 | 0.160 | 0.158 | 17 | 85 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA6 | team_total | 0.062 | 0.060 | 0.060 | 7 | 95 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-5 | game_total | 0.760 | 0.765 | 0.764 | 77 | 24 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-7 | game_total | 0.434 | 0.425 | 0.427 | 43 | 58 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.607 | 0.615 | 0.613 | 62 | 39 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.156 | 0.165 | 0.163 | 18 | 85 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.205 | 0.205 | 0.205 | 21 | 80 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.393 | 0.395 | 0.395 | 40 | 61 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT26LANYR-LA | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-NYR | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-TIE | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-LA2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-NYR2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 0.595 | 0.549 | 0.177 | 0.222 | 6.12 | 6.07 | 1.012/0.993 | KXNHLGAME-26OCT26LANYR-LA +0.046 |
| TOR @ CGY | 0.555 | 0.506 | 0.173 | 0.222 | 6.33 | 6.40 | 0.978/0.983 | KXNHLGAME-26OCT26TORCGY-CGY -0.049 |
| DET @ EDM | 0.607 | 0.645 | 0.166 | 0.207 | 6.55 | 6.65 | 1.022/1.000 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Laferriere: 1+ goals YES @ 26c · p 0.3128 (adj 0.2984) · $8.29 · thesis LAK:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7111 (adj 0.6971) · $18.24 · thesis NYR:SUPPRESSED
- Artemi Panarin: 1+ goals YES @ 30c · p 0.3417 (adj 0.33) · $5.53 · thesis LAK:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 23c · p 0.3326 (adj 0.2562) · $4.3 · thesis NYR:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 12c · p 0.1661 (adj 0.1533) · $6.78 · thesis CGY:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 80c · p 0.8487 (adj 0.8353) · $18.52 · thesis TOR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1598 (adj 0.1461) · $5.06 · thesis TOR:OFFENSE_4PLUS
- Auston Matthews: 1+ assists NO @ 54c · p 0.6274 (adj 0.5812) · $11.48 · thesis TOR:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 30c · p 0.3908 (adj 0.3429) · $10.88 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 63c · p 0.7528 (adj 0.6697) · $19.21 · thesis EDM:SUPPRESSED
- Connor McDavid: 1+ assists NO @ 30c · p 0.376 (adj 0.3355) · $5.7 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.2997 (adj 0.2885) · $7.67 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NYR** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: James Reimer (CONFIRMED) exp shots 28.09, exp saves 24.44 (sd 6.63), pull risk 0.054
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.31, exp saves 22.65 (sd 6.33), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.333 | 0.215 | 23/80 | +0.090 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.383 | 0.285 | 30/73 | +0.068 | STANDARD |
| Trevor Moore: 1+ points | 0.420 | 0.355 | 36/65 | +0.044 | STANDARD |
| Artemi Panarin: 1+ assists | 0.399 | 0.460 | 47/55 | +0.033 | STANDARD |
| Sean Durzi: 1+ assists | 0.232 | 0.290 | 30/72 | +0.034 | STANDARD |
| Alex Laferriere: 1+ goals | 0.313 | 0.255 | 26/75 | +0.039 | STANDARD |

**TOR @ CGY** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.89, exp saves 24.88 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.56, exp saves 27.24 (sd 7.27), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ points | 0.356 | 0.490 | 50/52 | +0.106 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Colton Sissons: 1+ points | 0.295 | 0.185 | 28/91 | +0.001 | STANDARD |
| Kirill Marchenko: 1+ points | 0.510 | 0.620 | 63/39 | +0.083 | STANDARD |
| Gavin McKenna: 1+ assists | 0.243 | 0.350 | 36/66 | +0.081 | STANDARD |
| William Nylander: 2+ points | 0.230 | 0.325 | 34/69 | +0.065 | STANDARD |

**DET @ EDM** · priced 167/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.49, exp saves 24.09 (sd 6.52), pull risk 0.053
- DET net: Michal Postava (CONFIRMED) exp shots 28.12, exp saves 23.68 (sd 6.88), pull risk 0.092

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.363 | 0.515 | 52/49 | +0.129 | STANDARD |
| Connor McDavid: 2+ assists | 0.247 | 0.375 | 38/63 | +0.106 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.293 | 0.410 | 43/61 | +0.080 | STANDARD |
| Connor McDavid: 2+ points | 0.469 | 0.580 | 59/43 | +0.084 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.507 | 0.610 | 62/40 | +0.076 | STANDARD |
| Connor McDavid: 3+ points | 0.209 | 0.310 | 32/70 | +0.076 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
