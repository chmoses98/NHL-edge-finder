# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-26T16:18:27Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2878 · contracts joined: 661 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 586, 'OK': 48, 'NO_EDGE': 27}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 90, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 187, 'game_overtime': 3, 'player_points': 121, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 2026-10-26T23:00:00Z | T-6h | 0.590 | 0.410 | 0.175 | 6.10 | 3.33 | 2.77 | 218 (25/193) | CONFIRMED/PROJECTED |
| TOR @ CGY | 2026-10-27T00:30:00Z | T-6h | 0.551 | 0.449 | 0.173 | 6.30 | 3.30 | 3.00 | 228 (25/203) | CONFIRMED/PROJECTED |
| DET @ EDM | 2026-10-27T01:30:00Z | T-6h | 0.606 | 0.394 | 0.166 | 6.44 | 3.56 | 2.87 | 215 (25/190) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.363 | 0.505 | 0.476 | 51 | 50 | no | +0.120 | OK |
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.551 | 0.425 | 0.450 | 43 | 58 | yes | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.576 | 0.705 | 0.681 | 72 | 31 | no | +0.099 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.142 | 0.255 | 0.228 | 26 | 75 | no | +0.095 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.449 | 0.565 | 0.542 | 57 | 44 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.245 | 0.355 | 0.331 | 36 | 65 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.330 | 0.235 | 0.252 | 24 | 77 | yes | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.192 | 0.295 | 0.272 | 31 | 72 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.792 | 0.875 | 0.861 | 88 | 13 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.463 | 0.535 | 0.521 | 54 | 47 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.202 | 0.145 | 0.155 | 15 | 86 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.862 | 0.915 | 0.906 | 92 | 9 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.084 | 0.140 | 0.127 | 15 | 87 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.784 | 0.835 | 0.826 | 84 | 17 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.578 | 0.640 | 0.628 | 65 | 37 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.494 | 0.550 | 0.539 | 56 | 46 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA3 | game_spread | 0.117 | 0.155 | 0.147 | 16 | 85 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.601 | 0.645 | 0.636 | 65 | 36 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.650 | 0.605 | 0.614 | 61 | 40 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.276 | 0.320 | 0.311 | 33 | 69 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.435 | 0.390 | 0.399 | 40 | 62 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.700 | 0.740 | 0.732 | 75 | 27 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR4 | team_total | 0.443 | 0.400 | 0.409 | 41 | 61 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.878 | 0.905 | 0.900 | 91 | 10 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.289 | 0.330 | 0.322 | 34 | 68 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA2 | game_spread | 0.212 | 0.245 | 0.238 | 25 | 76 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.195 | 0.225 | 0.219 | 23 | 78 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA2 | team_total | 0.755 | 0.785 | 0.779 | 79 | 22 | no | +0.013 | OK |
| KXNHLGAME-26OCT26LANYR-LA | game_winner | 0.410 | 0.445 | 0.438 | 45 | 56 | no | +0.013 | OK |
| KXNHLGAME-26OCT26LANYR-NYR | game_winner | 0.590 | 0.555 | 0.562 | 56 | 45 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR3 | team_total | 0.659 | 0.625 | 0.632 | 63 | 38 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.092 | 0.115 | 0.110 | 12 | 89 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.242 | 0.210 | 0.216 | 22 | 80 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.207 | 0.235 | 0.229 | 24 | 77 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR2 | game_spread | 0.365 | 0.335 | 0.341 | 34 | 67 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA3 | team_total | 0.524 | 0.555 | 0.549 | 56 | 45 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.115 | 0.090 | 0.095 | 10 | 92 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.258 | 0.285 | 0.279 | 29 | 72 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.865 | 0.885 | 0.881 | 89 | 12 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.838 | 0.815 | 0.820 | 82 | 19 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR6 | team_total | 0.113 | 0.095 | 0.098 | 10 | 91 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA4 | team_total | 0.309 | 0.340 | 0.334 | 35 | 67 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.148 | 0.170 | 0.165 | 18 | 84 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT26LANYR-10 | game_total | 0.077 | 0.065 | 0.067 | 7 | 94 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.294 | 0.320 | 0.315 | 33 | 69 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR3 | game_spread | 0.231 | 0.215 | 0.218 | 22 | 79 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.208 | 0.195 | 0.198 | 20 | 81 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.772 | 0.785 | 0.782 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR2 | team_total | 0.844 | 0.835 | 0.837 | 84 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA6 | team_total | 0.063 | 0.065 | 0.065 | 7 | 94 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.551 | 0.570 | 0.566 | 58 | 44 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR5 | team_total | 0.245 | 0.225 | 0.229 | 24 | 79 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.392 | 0.405 | 0.402 | 41 | 60 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.103 | 0.110 | 0.108 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-8 | game_total | 0.243 | 0.230 | 0.233 | 24 | 78 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.118 | 0.115 | 0.116 | 12 | 89 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.334 | 0.350 | 0.347 | 36 | 66 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-6 | game_total | 0.547 | 0.535 | 0.537 | 54 | 47 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-3 | game_total | 0.961 | 0.960 | 0.960 | 97 | 5 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA5 | team_total | 0.153 | 0.165 | 0.162 | 18 | 85 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-9 | game_total | 0.168 | 0.160 | 0.162 | 17 | 85 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.172 | 0.185 | 0.182 | 20 | 83 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-4 | game_total | 0.847 | 0.845 | 0.845 | 85 | 16 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.073 | 0.070 | 0.071 | 8 | 94 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.394 | 0.385 | 0.387 | 39 | 62 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.606 | 0.615 | 0.613 | 62 | 39 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-5 | game_total | 0.761 | 0.765 | 0.764 | 77 | 24 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-7 | game_total | 0.432 | 0.425 | 0.426 | 43 | 58 |  | -0.016 | NO_EDGE |
| KXNHL1P-26OCT26LANYR-LA | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-NYR | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-TIE | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-LA2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-NYR2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 0.590 | 0.546 | 0.175 | 0.218 | 6.10 | 6.07 | 1.012/0.992 | KXNHLGAME-26OCT26LANYR-LA +0.044 |
| TOR @ CGY | 0.551 | 0.504 | 0.173 | 0.218 | 6.30 | 6.39 | 0.978/0.978 | KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 +0.048 |
| DET @ EDM | 0.606 | 0.651 | 0.166 | 0.203 | 6.44 | 6.62 | 1.009/1.002 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 10 recommended · full analysis in card.md / packet.json `thesis_card`

- Pavel Dorofeyev: 1+ goals NO @ 67c · p 0.7224 (adj 0.7081) · $17.9 · thesis NYR:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 66c · p 0.8003 (adj 0.6961) · $19.51 · thesis LAK:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1658 (adj 0.1518) · $6.5 · thesis TOR:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 12c · p 0.1576 (adj 0.1444) · $4.48 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 10c · p 0.1281 (adj 0.1198) · $3.48 · thesis CGY:OFFENSE_4PLUS
- William Nylander: 1+ goals NO @ 64c · p 0.6852 (adj 0.6726) · $12.41 · thesis TOR:SUPPRESSED
- Connor McDavid: 2+ assists NO @ 63c · p 0.7478 (adj 0.668) · $19.85 · thesis EDM:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.4916 (adj 0.4458) · $9.12 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.299 (adj 0.288) · $7.73 · thesis EDM:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ assists YES @ 25c · p 0.3129 (adj 0.2764) · $4.07 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NYR** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: James Reimer (CONFIRMED) exp shots 28.09, exp saves 24.45 (sd 6.63), pull risk 0.056
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.31, exp saves 22.64 (sd 6.35), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.200 | 0.360 | 38/66 | +0.125 | STANDARD |
| Mats Zuccarello: 1+ points | 0.352 | 0.465 | 47/54 | +0.091 | STANDARD |
| Mats Zuccarello: 2+ points | 0.071 | 0.145 | 18/89 | +0.032 | STANDARD |
| Sean Durzi: 1+ assists | 0.226 | 0.295 | 31/72 | +0.040 | STANDARD |
| Artemi Panarin: 2+ points | 0.219 | 0.285 | 30/73 | +0.037 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.278 | 0.335 | 34/67 | +0.037 | STANDARD |

**TOR @ CGY** · priced 173/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.89, exp saves 24.85 (sd 6.89), pull risk 0.065
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.56, exp saves 27.35 (sd 7.25), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ points | 0.367 | 0.485 | 51/54 | +0.076 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.315 | 0.425 | 43/58 | +0.088 | STANDARD |
| William Nylander: 2+ points | 0.230 | 0.330 | 35/69 | +0.065 | STANDARD |
| Kirill Marchenko: 1+ points | 0.513 | 0.610 | 64/42 | +0.050 | STANDARD |
| Auston Matthews: 1+ assists | 0.374 | 0.470 | 48/54 | +0.069 | STANDARD |
| Auston Matthews: 2+ points | 0.244 | 0.335 | 34/67 | +0.070 | STANDARD |

**DET @ EDM** · priced 158/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.49, exp saves 24.14 (sd 6.49), pull risk 0.053
- DET net: John Gibson (PROJECTED) exp shots 28.12, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.252 | 0.375 | 38/63 | +0.101 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.396 | 0.285 | 30/73 | +0.081 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.303 | 0.410 | 42/60 | +0.080 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.575 | 0.470 | 49/55 | +0.067 | STANDARD |
| Connor McDavid: 2+ points | 0.467 | 0.560 | 57/45 | +0.066 | STANDARD |
| Leon Draisaitl: 2+ points | 0.373 | 0.465 | 48/55 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
