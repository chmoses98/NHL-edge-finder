# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-26T15:01:47Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2868 · contracts joined: 651 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 576, 'OK': 48, 'NO_EDGE': 27}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 87, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 115, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 2026-10-26T23:00:00Z | T-6h | 0.610 | 0.390 | 0.176 | 5.99 | 3.34 | 2.65 | 209 (25/184) | PROJECTED/PROJECTED |
| TOR @ CGY | 2026-10-27T00:30:00Z | T-6h | 0.536 | 0.464 | 0.173 | 6.41 | 3.31 | 3.10 | 227 (25/202) | PROJECTED/PROJECTED |
| DET @ EDM | 2026-10-27T01:30:00Z | T-6h | 0.606 | 0.394 | 0.166 | 6.44 | 3.56 | 2.87 | 215 (25/190) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.536 | 0.425 | 0.447 | 43 | 58 | yes | +0.089 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.464 | 0.575 | 0.553 | 58 | 43 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.262 | 0.365 | 0.343 | 37 | 64 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.597 | 0.700 | 0.681 | 71 | 31 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.159 | 0.255 | 0.233 | 26 | 75 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.386 | 0.490 | 0.469 | 50 | 52 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.210 | 0.300 | 0.280 | 31 | 71 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.318 | 0.235 | 0.250 | 24 | 77 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.808 | 0.875 | 0.863 | 88 | 13 | no | +0.054 | OK |
| KXNHLGAME-26OCT26LANYR-LA | game_winner | 0.390 | 0.455 | 0.442 | 46 | 55 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR2 | game_spread | 0.385 | 0.325 | 0.337 | 33 | 68 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.197 | 0.145 | 0.154 | 15 | 86 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA3 | team_total | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.872 | 0.915 | 0.908 | 92 | 9 | no | +0.033 | OK |
| KXNHLGAME-26OCT26LANYR-NYR | game_winner | 0.610 | 0.555 | 0.566 | 56 | 45 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA4 | team_total | 0.284 | 0.335 | 0.324 | 34 | 67 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.483 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.096 | 0.145 | 0.134 | 16 | 87 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA3 | game_spread | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA2 | team_total | 0.736 | 0.780 | 0.772 | 79 | 23 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.648 | 0.600 | 0.610 | 61 | 41 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA2 | game_spread | 0.197 | 0.235 | 0.227 | 24 | 77 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.437 | 0.390 | 0.399 | 40 | 62 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.595 | 0.640 | 0.631 | 65 | 37 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.494 | 0.535 | 0.527 | 54 | 47 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR4 | team_total | 0.445 | 0.405 | 0.413 | 41 | 60 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.878 | 0.905 | 0.900 | 91 | 10 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.289 | 0.330 | 0.322 | 34 | 68 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.245 | 0.210 | 0.217 | 22 | 80 | yes | +0.013 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR3 | game_spread | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.799 | 0.830 | 0.824 | 84 | 18 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.287 | 0.320 | 0.313 | 33 | 69 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.258 | 0.285 | 0.279 | 29 | 72 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.865 | 0.885 | 0.881 | 89 | 12 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.114 | 0.090 | 0.094 | 10 | 92 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA5 | team_total | 0.134 | 0.165 | 0.158 | 18 | 85 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR6 | team_total | 0.113 | 0.095 | 0.098 | 10 | 91 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.700 | 0.730 | 0.724 | 74 | 28 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.835 | 0.810 | 0.815 | 82 | 20 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR3 | team_total | 0.660 | 0.630 | 0.636 | 64 | 38 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.489 | 0.515 | 0.510 | 52 | 49 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.601 | 0.630 | 0.624 | 64 | 38 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.100 | 0.115 | 0.112 | 12 | 89 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.205 | 0.225 | 0.221 | 23 | 78 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.207 | 0.225 | 0.221 | 23 | 78 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT26LANYR-5 | game_total | 0.747 | 0.765 | 0.761 | 77 | 24 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.968 | 0.975 | 0.974 | 98 | 3 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-6 | game_total | 0.526 | 0.545 | 0.541 | 55 | 46 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR2 | team_total | 0.846 | 0.830 | 0.833 | 84 | 18 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.118 | 0.125 | 0.123 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-10 | game_total | 0.068 | 0.065 | 0.066 | 7 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR5 | team_total | 0.246 | 0.225 | 0.229 | 24 | 79 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-4 | game_total | 0.838 | 0.845 | 0.844 | 85 | 16 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.148 | 0.165 | 0.162 | 18 | 85 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA6 | team_total | 0.054 | 0.060 | 0.059 | 7 | 95 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.294 | 0.310 | 0.307 | 32 | 70 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-2 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.392 | 0.405 | 0.402 | 41 | 60 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.103 | 0.110 | 0.108 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-3 | game_total | 0.957 | 0.960 | 0.959 | 97 | 5 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.334 | 0.350 | 0.347 | 36 | 66 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-7 | game_total | 0.413 | 0.425 | 0.423 | 43 | 58 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.073 | 0.070 | 0.071 | 8 | 94 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.394 | 0.385 | 0.387 | 39 | 62 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.606 | 0.615 | 0.613 | 62 | 39 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.208 | 0.205 | 0.206 | 21 | 80 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.772 | 0.785 | 0.782 | 80 | 23 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-9 | game_total | 0.157 | 0.160 | 0.159 | 17 | 85 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.551 | 0.560 | 0.558 | 57 | 45 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-8 | game_total | 0.231 | 0.230 | 0.230 | 24 | 78 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.172 | 0.175 | 0.174 | 19 | 84 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT26LANYR-LA | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-NYR | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-TIE | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-LA2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-NYR2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 0.610 | 0.557 | 0.176 | 0.223 | 5.99 | 6.01 | 0.987/0.992 | KXNHLSPREAD-26OCT26LANYR-NYR2 -0.054 |
| TOR @ CGY | 0.536 | 0.499 | 0.173 | 0.217 | 6.41 | 6.41 | 0.986/0.978 | KXNHLGAME-26OCT26TORCGY-CGY -0.037 |
| DET @ EDM | 0.606 | 0.651 | 0.166 | 0.203 | 6.44 | 6.62 | 1.009/1.002 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 10 recommended · full analysis in card.md / packet.json `thesis_card`

- Mats Zuccarello: 1+ assists NO @ 64c · p 0.8038 (adj 0.6941) · $20.0 · thesis LAK:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 67c · p 0.7198 (adj 0.7061) · $16.41 · thesis NYR:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 11c · p 0.156 (adj 0.1395) · $5.29 · thesis CGY:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 79c · p 0.8448 (adj 0.8274) · $19.88 · thesis TOR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1616 (adj 0.1487) · $6.01 · thesis TOR:OFFENSE_4PLUS
- Toronto wins by over 2.5 goals NO @ 75c · p 0.8162 (adj 0.7806) · $18.81 · thesis CGY:WINS
- Filip Hallander: 1+ goals YES @ 11c · p 0.1421 (adj 0.1291) · $3.21 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 67c · p 0.7478 (adj 0.7014) · $16.24 · thesis EDM:SUPPRESSED
- Ryan Nugent-Hopkins: 1+ assists NO @ 59c · p 0.6969 (adj 0.6209) · $9.09 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.299 (adj 0.2855) · $5.32 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NYR** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 28.09, exp saves 24.55 (sd 6.64), pull risk 0.05
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.31, exp saves 22.61 (sd 6.33), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.196 | 0.365 | 37/64 | +0.148 | STANDARD |
| Mats Zuccarello: 1+ points | 0.353 | 0.485 | 50/53 | +0.100 | STANDARD |
| Mats Zuccarello: 2+ points | 0.066 | 0.155 | 18/87 | +0.057 | STANDARD |
| Artemi Panarin: 2+ points | 0.214 | 0.275 | 29/74 | +0.032 | STANDARD |
| Artemi Panarin: 1+ assists | 0.386 | 0.445 | 45/56 | +0.037 | STANDARD |
| Sean Durzi: 1+ assists | 0.233 | 0.290 | 31/73 | +0.024 | STANDARD |

**TOR @ CGY** · priced 172/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 28.89, exp saves 24.83 (sd 6.8), pull risk 0.067
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.56, exp saves 27.29 (sd 7.26), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ assists | 0.319 | 0.430 | 44/58 | +0.084 | STANDARD |
| Gavin McKenna: 1+ points | 0.368 | 0.475 | 49/54 | +0.075 | STANDARD |
| Kirill Marchenko: 2+ points | 0.160 | 0.265 | 30/77 | +0.058 | STANDARD |
| Kirill Marchenko: 1+ points | 0.511 | 0.615 | 65/42 | +0.052 | STANDARD |
| Auston Matthews: 1+ assists | 0.370 | 0.470 | 48/54 | +0.072 | STANDARD |
| William Nylander: 2+ points | 0.240 | 0.335 | 35/68 | +0.065 | STANDARD |

**DET @ EDM** · priced 158/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.49, exp saves 24.14 (sd 6.49), pull risk 0.053
- DET net: John Gibson (PROJECTED) exp shots 28.12, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Nugent-Hopkins: 1+ assists | 0.303 | 0.420 | 43/59 | +0.090 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.396 | 0.290 | 31/73 | +0.071 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.508 | 0.610 | 62/40 | +0.075 | STANDARD |
| Connor McDavid: 2+ points | 0.467 | 0.565 | 58/45 | +0.066 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.575 | 0.480 | 50/54 | +0.057 | STANDARD |
| Connor McDavid: 2+ assists | 0.252 | 0.345 | 36/67 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
