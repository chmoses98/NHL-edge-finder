# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-26T18:01:19Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2907 · contracts joined: 690 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 615, 'OK': 50, 'NO_EDGE': 25}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 101, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 137, 'goalie_saves': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 2026-10-26T23:00:00Z | T-3h | 0.595 | 0.405 | 0.177 | 6.12 | 3.35 | 2.77 | 224 (25/199) | CONFIRMED/PROBABLE |
| TOR @ CGY | 2026-10-27T00:30:00Z | T-6h | 0.555 | 0.445 | 0.173 | 6.33 | 3.33 | 3.00 | 237 (25/212) | CONFIRMED/PROBABLE |
| DET @ EDM | 2026-10-27T01:30:00Z | T-6h | 0.606 | 0.394 | 0.166 | 6.44 | 3.56 | 2.87 | 229 (25/204) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.361 | 0.490 | 0.464 | 50 | 52 | no | +0.101 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.579 | 0.700 | 0.677 | 71 | 31 | no | +0.096 | OK |
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.555 | 0.445 | 0.467 | 45 | 56 | yes | +0.088 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.445 | 0.555 | 0.533 | 56 | 45 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.142 | 0.245 | 0.221 | 25 | 76 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.246 | 0.345 | 0.324 | 35 | 66 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.191 | 0.290 | 0.268 | 30 | 72 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.332 | 0.245 | 0.261 | 25 | 76 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.792 | 0.870 | 0.857 | 88 | 14 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.866 | 0.915 | 0.907 | 92 | 9 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.494 | 0.555 | 0.543 | 56 | 45 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.206 | 0.155 | 0.164 | 16 | 85 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.784 | 0.835 | 0.826 | 84 | 17 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.086 | 0.135 | 0.124 | 14 | 87 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.489 | 0.545 | 0.534 | 55 | 46 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.469 | 0.530 | 0.518 | 54 | 48 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.799 | 0.845 | 0.837 | 85 | 16 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA3 | game_spread | 0.110 | 0.155 | 0.145 | 16 | 85 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.654 | 0.605 | 0.615 | 61 | 40 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.289 | 0.335 | 0.326 | 34 | 67 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.441 | 0.395 | 0.404 | 40 | 61 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.580 | 0.630 | 0.620 | 64 | 38 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.601 | 0.650 | 0.640 | 66 | 36 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA2 | game_spread | 0.206 | 0.245 | 0.237 | 25 | 76 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR4 | team_total | 0.447 | 0.400 | 0.409 | 41 | 61 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.199 | 0.235 | 0.227 | 24 | 77 | no | +0.019 | OK |
| KXNHLGAME-26OCT26LANYR-LA | game_winner | 0.405 | 0.445 | 0.437 | 45 | 56 | no | +0.018 | OK |
| KXNHLGAME-26OCT26LANYR-NYR | game_winner | 0.595 | 0.555 | 0.563 | 56 | 45 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR3 | team_total | 0.664 | 0.625 | 0.633 | 63 | 38 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.258 | 0.295 | 0.287 | 30 | 71 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.700 | 0.740 | 0.732 | 75 | 27 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.878 | 0.905 | 0.900 | 91 | 10 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.279 | 0.315 | 0.308 | 32 | 69 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.294 | 0.325 | 0.319 | 33 | 68 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.207 | 0.240 | 0.233 | 25 | 77 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR2 | game_spread | 0.365 | 0.335 | 0.341 | 34 | 67 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA3 | team_total | 0.524 | 0.555 | 0.549 | 56 | 45 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.839 | 0.815 | 0.820 | 82 | 19 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.095 | 0.115 | 0.111 | 12 | 89 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.865 | 0.885 | 0.881 | 89 | 12 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR5 | team_total | 0.250 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.249 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT26LANYR-10 | game_total | 0.081 | 0.065 | 0.068 | 7 | 94 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA4 | team_total | 0.311 | 0.340 | 0.334 | 35 | 67 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.148 | 0.175 | 0.169 | 19 | 84 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.551 | 0.575 | 0.570 | 58 | 43 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA2 | team_total | 0.756 | 0.780 | 0.775 | 79 | 23 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.392 | 0.415 | 0.410 | 42 | 59 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.967 | 0.975 | 0.974 | 98 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR6 | team_total | 0.117 | 0.095 | 0.099 | 11 | 92 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.334 | 0.355 | 0.351 | 36 | 65 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.208 | 0.195 | 0.198 | 20 | 81 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR2 | team_total | 0.846 | 0.830 | 0.833 | 84 | 18 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-2 | game_total | 0.982 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.772 | 0.785 | 0.782 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-8 | game_total | 0.248 | 0.230 | 0.234 | 24 | 78 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.118 | 0.125 | 0.123 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT26LANYR-NYR3 | game_spread | 0.227 | 0.215 | 0.217 | 22 | 79 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA6 | team_total | 0.062 | 0.070 | 0.068 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-6 | game_total | 0.551 | 0.535 | 0.538 | 54 | 47 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-9 | game_total | 0.173 | 0.165 | 0.167 | 17 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.103 | 0.110 | 0.108 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA5 | team_total | 0.151 | 0.165 | 0.162 | 18 | 85 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-4 | game_total | 0.848 | 0.845 | 0.846 | 85 | 16 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.172 | 0.185 | 0.182 | 20 | 83 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.394 | 0.385 | 0.387 | 39 | 62 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.606 | 0.615 | 0.613 | 62 | 39 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-5 | game_total | 0.760 | 0.765 | 0.764 | 77 | 24 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-7 | game_total | 0.434 | 0.425 | 0.427 | 43 | 58 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.073 | 0.075 | 0.075 | 9 | 94 |  | -0.016 | NO_EDGE |
| KXNHL1P-26OCT26LANYR-LA | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-NYR | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-TIE | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-LA2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-NYR2 | period_spread |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 0.595 | 0.549 | 0.177 | 0.222 | 6.12 | 6.07 | 1.012/0.993 | KXNHLGAME-26OCT26LANYR-LA +0.046 |
| TOR @ CGY | 0.555 | 0.506 | 0.173 | 0.222 | 6.33 | 6.40 | 0.978/0.983 | KXNHLGAME-26OCT26TORCGY-CGY -0.049 |
| DET @ EDM | 0.606 | 0.651 | 0.166 | 0.203 | 6.44 | 6.62 | 1.009/1.002 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Laferriere: 1+ goals YES @ 26c · p 0.3128 (adj 0.2984) · $8.33 · thesis LAK:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7111 (adj 0.6971) · $16.97 · thesis NYR:SUPPRESSED
- Tye Kartye: 1+ goals YES @ 15c · p 0.18 (adj 0.1713) · $3.39 · thesis NYR:OFFENSE_4PLUS
- Artemi Panarin: 1+ goals YES @ 30c · p 0.3417 (adj 0.33) · $5.51 · thesis LAK:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1598 (adj 0.1411) · $6.17 · thesis TOR:OFFENSE_4PLUS
- Gavin McKenna: 1+ assists NO @ 67c · p 0.7572 (adj 0.7086) · $20.0 · thesis TOR:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 13c · p 0.1661 (adj 0.1533) · $4.14 · thesis CGY:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 58c · p 0.6183 (adj 0.6075) · $4.4 · thesis TOR:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 11c · p 0.1437 (adj 0.1328) · $4.25 · thesis DET:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 63c · p 0.747 (adj 0.6677) · $19.99 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.3033 (adj 0.2912) · $9.22 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.49 (adj 0.445) · $8.97 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NYR** · priced 165/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: James Reimer (CONFIRMED) exp shots 28.09, exp saves 24.44 (sd 6.63), pull risk 0.054
- LAK net: Darcy Kuemper (PROBABLE) exp shots 26.31, exp saves 22.65 (sd 6.33), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.333 | 0.215 | 24/81 | +0.080 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.383 | 0.285 | 31/74 | +0.058 | STANDARD |
| Drew Doughty: 1+ points | 0.325 | 0.260 | 29/77 | +0.020 | STANDARD |
| Artemi Panarin: 1+ assists | 0.399 | 0.460 | 47/55 | +0.033 | STANDARD |
| Trevor Moore: 1+ points | 0.420 | 0.360 | 37/65 | +0.034 | STANDARD |
| J.T. Miller: 1+ assists | 0.365 | 0.425 | 44/59 | +0.028 | STANDARD |

**TOR @ CGY** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.89, exp saves 24.88 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.56, exp saves 27.24 (sd 7.27), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ points | 0.510 | 0.645 | 65/36 | +0.113 | STANDARD |
| Gavin McKenna: 1+ points | 0.356 | 0.485 | 50/53 | +0.096 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Auston Matthews: 1+ assists | 0.373 | 0.470 | 48/54 | +0.070 | STANDARD |
| Gavin McKenna: 1+ assists | 0.243 | 0.340 | 35/67 | +0.072 | STANDARD |
| William Nylander: 2+ points | 0.230 | 0.325 | 34/69 | +0.065 | STANDARD |

**DET @ EDM** · priced 165/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.49, exp saves 24.14 (sd 6.49), pull risk 0.053
- DET net: John Gibson (PROJECTED) exp shots 28.12, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.253 | 0.375 | 38/63 | +0.101 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.304 | 0.415 | 43/60 | +0.079 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.401 | 0.290 | 30/72 | +0.086 | STANDARD |
| Connor McDavid: 2+ points | 0.466 | 0.575 | 58/43 | +0.087 | STANDARD |
| Connor McDavid: 3+ points | 0.211 | 0.315 | 33/70 | +0.074 | STANDARD |
| Leon Draisaitl: 2+ points | 0.377 | 0.480 | 49/53 | +0.076 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
