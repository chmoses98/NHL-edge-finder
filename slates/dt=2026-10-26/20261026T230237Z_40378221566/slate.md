# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-26T23:02:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2958 · contracts joined: 510 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 460, 'OK': 30, 'NO_EDGE': 20}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 87, 'game_early_goal': 2, 'first_goal': 76, 'game_winner': 4, 'player_goals': 129, 'game_overtime': 2, 'player_points': 112, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ CGY | 2026-10-27T00:30:00Z | T-60m | 0.555 | 0.445 | 0.173 | 6.33 | 3.33 | 3.00 | 237 (25/212) | CONFIRMED/PROBABLE |
| DET @ EDM | 2026-10-27T01:30:00Z | T-90m | 0.607 | 0.393 | 0.166 | 6.55 | 3.63 | 2.93 | 273 (25/248) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.361 | 0.490 | 0.464 | 50 | 52 | no | +0.101 | OK |
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.555 | 0.445 | 0.467 | 45 | 56 | yes | +0.088 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.445 | 0.555 | 0.533 | 56 | 45 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.579 | 0.690 | 0.669 | 70 | 32 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.246 | 0.345 | 0.324 | 35 | 66 | no | +0.079 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.142 | 0.235 | 0.214 | 24 | 77 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.332 | 0.245 | 0.261 | 25 | 76 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.191 | 0.280 | 0.260 | 29 | 73 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.792 | 0.870 | 0.857 | 88 | 14 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.206 | 0.155 | 0.164 | 16 | 85 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.784 | 0.840 | 0.830 | 85 | 17 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.580 | 0.635 | 0.624 | 64 | 37 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.469 | 0.525 | 0.514 | 53 | 48 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.811 | 0.855 | 0.847 | 86 | 15 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.866 | 0.905 | 0.898 | 91 | 10 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.654 | 0.605 | 0.615 | 61 | 40 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.086 | 0.130 | 0.120 | 14 | 88 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.279 | 0.325 | 0.316 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.441 | 0.395 | 0.404 | 40 | 61 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.618 | 0.655 | 0.648 | 66 | 35 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.507 | 0.545 | 0.537 | 55 | 46 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.302 | 0.340 | 0.332 | 35 | 67 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.884 | 0.905 | 0.901 | 91 | 10 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.199 | 0.230 | 0.223 | 24 | 78 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.249 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.259 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.713 | 0.740 | 0.735 | 75 | 27 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.967 | 0.975 | 0.974 | 98 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.116 | 0.095 | 0.099 | 11 | 92 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.839 | 0.820 | 0.824 | 83 | 19 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.095 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.345 | 0.365 | 0.361 | 37 | 64 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.116 | 0.125 | 0.123 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.112 | 0.105 | 0.106 | 11 | 90 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.389 | 0.405 | 0.402 | 41 | 60 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.225 | 0.240 | 0.237 | 25 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.077 | 0.070 | 0.071 | 8 | 94 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.313 | 0.325 | 0.323 | 33 | 68 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.562 | 0.580 | 0.576 | 59 | 43 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.990 | 0.990 |  | 2 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.607 | 0.615 | 0.613 | 62 | 39 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.156 | 0.160 | 0.159 | 17 | 85 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.205 | 0.205 | 0.205 | 21 | 80 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.393 | 0.395 | 0.395 | 40 | 61 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.180 | 0.185 | 0.184 | 20 | 83 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT26TORCGY-CGY | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26TORCGY-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26TORCGY-TOR | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26TORCGY-CGY2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26TORCGY-TOR2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26TORCGY-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26TORCGY-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26TORCGY-3 | period_total |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26TORCGY-CGY | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26TORCGY-TIE | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26TORCGY-TOR | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT26TORCGY-CGY2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT26TORCGY-TOR2 | period_spread |  | 0.150 |  | 16 | 86 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26TORCGY-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26TORCGY-2 | period_total |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26TORCGY-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26TORCGY-CGY | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26TORCGY-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26TORCGY-TOR | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT26TORCGY-CGY2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT26TORCGY-TOR2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26TORCGY-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26TORCGY-2 | period_total |  | 0.675 |  | 68 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26TORCGY-3 | period_total |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-CGYASUNIEV61-1 | player_assists |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-CGYJFARABEE86-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-CGYJFARABEE86-2 | player_assists |  | 0.060 |  | 10 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-CGYKBAHL7-1 | player_assists |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-CGYMCORONATO27-1 | player_assists |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-CGYMCORONATO27-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ CGY | 0.555 | 0.506 | 0.173 | 0.222 | 6.33 | 6.40 | 0.978/0.983 | KXNHLGAME-26OCT26TORCGY-CGY -0.049 |
| DET @ EDM | 0.607 | 0.645 | 0.166 | 0.207 | 6.55 | 6.65 | 1.022/1.000 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 11c · p 0.1598 (adj 0.1411) · $6.05 · thesis TOR:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 12c · p 0.1664 (adj 0.1523) · $6.37 · thesis CGY:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 10c · p 0.1379 (adj 0.1272) · $5.21 · thesis CGY:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 57c · p 0.6183 (adj 0.605) · $10.17 · thesis TOR:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.4933 (adj 0.4466) · $11.03 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.2997 (adj 0.2885) · $6.62 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ assists YES @ 30c · p 0.3908 (adj 0.3253) · $5.25 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ goals NO @ 52c · p 0.5586 (adj 0.5477) · $7.5 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TOR @ CGY** · priced 179/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.89, exp saves 24.88 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.56, exp saves 27.24 (sd 7.27), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ points | 0.356 | 0.490 | 50/52 | +0.106 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.314 | 0.425 | 43/58 | +0.089 | STANDARD |
| Kirill Marchenko: 1+ points | 0.510 | 0.620 | 63/39 | +0.083 | STANDARD |
| William Nylander: 2+ points | 0.230 | 0.330 | 34/68 | +0.075 | STANDARD |
| Gavin McKenna: 1+ assists | 0.243 | 0.340 | 35/67 | +0.072 | STANDARD |
| Auston Matthews: 2+ points | 0.243 | 0.340 | 35/67 | +0.072 | STANDARD |

**DET @ EDM** · priced 207/222 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.49, exp saves 24.09 (sd 6.52), pull risk 0.053
- DET net: Michal Postava (CONFIRMED) exp shots 28.12, exp saves 23.68 (sd 6.88), pull risk 0.092

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.363 | 0.515 | 52/49 | +0.129 | STANDARD |
| Connor McDavid: 2+ points | 0.469 | 0.605 | 61/40 | +0.114 | STANDARD |
| Connor McDavid: 2+ assists | 0.247 | 0.380 | 39/63 | +0.106 | STANDARD |
| Ben Chiarot: 1+ points | 0.263 | 0.150 | 18/88 | +0.073 | STANDARD |
| Albert Johansson: 1+ points | 0.215 | 0.105 | 19/98 | +0.014 | STANDARD |
| Jake Walman: 1+ points | 0.258 | 0.150 | 25/95 | -0.005 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
