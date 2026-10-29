# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-29T00:18:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 3 · markets on board: 3262 · contracts joined: 715 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 640, 'OK': 53, 'NO_EDGE': 22}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 114, 'game_early_goal': 3, 'first_goal': 108, 'game_winner': 6, 'player_goals': 186, 'game_overtime': 3, 'player_points': 148, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ EDM | 2026-10-29T00:30:00Z | T-10m | 0.576 | 0.424 | 0.175 | 6.33 | 3.41 | 2.92 | 253 (25/228) | CONFIRMED/CONFIRMED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-30m | 0.578 | 0.422 | 0.173 | 6.13 | 3.31 | 2.81 | 233 (25/208) | CONFIRMED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-90m | 0.572 | 0.428 | 0.165 | 6.84 | 3.67 | 3.17 | 229 (25/204) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.572 | 0.445 | 0.470 | 45 | 56 | yes | +0.105 | OK |
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.428 | 0.545 | 0.522 | 55 | 46 | no | +0.095 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.367 | 0.255 | 0.275 | 26 | 75 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.235 | 0.335 | 0.313 | 34 | 67 | no | +0.079 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.137 | 0.225 | 0.205 | 23 | 78 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.508 | 0.410 | 0.429 | 42 | 60 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.711 | 0.625 | 0.643 | 63 | 38 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.314 | 0.230 | 0.245 | 24 | 78 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.241 | 0.165 | 0.178 | 17 | 84 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.455 | 0.535 | 0.519 | 54 | 47 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.399 | 0.475 | 0.460 | 48 | 53 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.223 | 0.295 | 0.280 | 30 | 71 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.613 | 0.685 | 0.671 | 69 | 32 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.166 | 0.100 | 0.111 | 11 | 91 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.354 | 0.425 | 0.411 | 43 | 58 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.671 | 0.740 | 0.727 | 75 | 27 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.260 | 0.330 | 0.315 | 34 | 68 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.218 | 0.280 | 0.267 | 29 | 73 | no | +0.038 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.424 | 0.365 | 0.376 | 37 | 64 | yes | +0.037 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.576 | 0.635 | 0.624 | 64 | 37 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.765 | 0.815 | 0.806 | 82 | 19 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.438 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.787 | 0.835 | 0.826 | 84 | 17 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.551 | 0.605 | 0.594 | 61 | 40 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.813 | 0.865 | 0.856 | 88 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.867 | 0.905 | 0.898 | 91 | 10 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.876 | 0.835 | 0.844 | 84 | 17 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.850 | 0.885 | 0.879 | 89 | 12 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.585 | 0.625 | 0.617 | 63 | 38 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.353 | 0.315 | 0.323 | 32 | 69 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.227 | 0.190 | 0.197 | 20 | 82 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.126 | 0.160 | 0.153 | 17 | 85 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.765 | 0.795 | 0.789 | 80 | 21 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.141 | 0.110 | 0.116 | 12 | 90 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.321 | 0.360 | 0.352 | 37 | 65 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.224 | 0.255 | 0.249 | 26 | 75 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.841 | 0.870 | 0.865 | 88 | 14 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.104 | 0.125 | 0.120 | 13 | 88 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.277 | 0.305 | 0.299 | 31 | 70 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.172 | 0.195 | 0.190 | 20 | 81 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.435 | 0.465 | 0.459 | 47 | 54 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.248 | 0.275 | 0.270 | 28 | 73 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.647 | 0.680 | 0.674 | 69 | 33 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY3 | team_total | 0.564 | 0.535 | 0.541 | 54 | 47 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT28NJCOL-10 | game_total | 0.079 | 0.095 | 0.092 | 10 | 91 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.963 | 0.975 | 0.973 | 98 | 3 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.986 | 0.990 | 0.989 |  | 1 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.967 | 0.980 | 0.978 | 99 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.246 | 0.270 | 0.265 | 28 | 74 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.198 | 0.220 | 0.215 | 23 | 79 | no | +0.000 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.127 | 0.115 | 0.117 | 12 | 89 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.543 | 0.565 | 0.561 | 57 | 44 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.094 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.263 | 0.240 | 0.244 | 25 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-7 | game_total | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.221 | 0.235 | 0.232 | 24 | 77 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-6 | game_total | 0.653 | 0.635 | 0.639 | 64 | 37 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.125 | 0.135 | 0.133 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY5 | team_total | 0.176 | 0.160 | 0.163 | 17 | 85 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.835 | 0.845 | 0.843 | 85 | 16 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL6 | team_total | 0.117 | 0.125 | 0.123 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.157 | 0.175 | 0.171 | 19 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.901 | 0.905 | 0.904 | 91 | 10 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY4 | team_total | 0.347 | 0.335 | 0.337 | 34 | 67 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY6 | team_total | 0.075 | 0.070 | 0.071 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-3 | game_total | 0.979 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY2 | team_total | 0.780 | 0.775 | 0.776 | 78 | 23 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26OCT28NJCOL-NJ | game_winner | 0.422 | 0.425 | 0.424 | 43 | 58 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT28NJCOL-COL | game_winner | 0.578 | 0.575 | 0.576 | 58 | 43 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-COL2 | game_spread | 0.354 | 0.355 | 0.355 | 36 | 65 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT28CGYEDM-CGY | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT28CGYEDM-EDM | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT28CGYEDM-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT28CGYEDM-CGY2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT28CGYEDM-EDM2 | period_spread |  | 0.175 |  | 18 | 83 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ EDM | 0.576 | 0.660 | 0.175 | 0.195 | 6.33 | 6.74 | 1.023/0.978 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.110 |
| NJD @ COL | 0.578 | 0.625 | 0.173 | 0.215 | 6.13 | 6.34 | 0.979/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.061 |
| TOR @ SEA | 0.572 | 0.560 | 0.165 | 0.210 | 6.84 | 6.67 | 1.019/0.988 | KXNHLTOTAL-26OCT28TORSEA-8 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Formenton: 1+ goals YES @ 14c · p 0.2067 (adj 0.1863) · $9.95 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 7c · p 0.1086 (adj 0.0927) · $4.06 · thesis CGY:OFFENSE_4PLUS
- Ryan Nugent-Hopkins: 1+ assists NO @ 60c · p 0.6892 (adj 0.6421) · $19.37 · thesis EDM:SUPPRESSED
- Connor McDavid: 1+ goals YES @ 46c · p 0.5124 (adj 0.498) · $11.64 · thesis EDM:OFFENSE_4PLUS
- Nicolas Roy: 1+ assists NO @ 79c · p 0.8998 (adj 0.8252) · $20.0 · thesis COL:SUPPRESSED
- Jake Allen: 27+ saves NO @ 53c · p 0.6034 (adj 0.5642) · $9.77 · thesis NJD:NET_LOW_VOLUME
- Mackenzie Blackwood: 27+ saves NO @ 51c · p 0.615 (adj 0.5435) · $9.17 · thesis COL:NET_LOW_VOLUME
- Jack Hughes: 1+ assists NO @ 54c · p 0.643 (adj 0.5728) · $9.47 · thesis NJD:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1554 (adj 0.1403) · $8.38 · thesis TOR:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 16c · p 0.219 (adj 0.203) · $9.16 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1598 (adj 0.1449) · $6.98 · thesis SEA:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ goals YES @ 20c · p 0.2484 (adj 0.2351) · $7.52 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CGY @ EDM** · priced 195/202 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.03, exp saves 23.73 (sd 6.47), pull risk 0.051
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.57, exp saves 25.62 (sd 7.41), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.245 | 0.360 | 37/65 | +0.089 | STANDARD |
| Adam Klapka: 1+ assists | 0.217 | 0.105 | 19/98 | +0.016 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.482 | 0.375 | 38/63 | +0.086 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.316 | 0.210 | 22/80 | +0.084 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.672 | 0.570 | 58/44 | +0.075 | STANDARD |
| Connor McDavid: 1+ assists | 0.614 | 0.715 | 72/29 | +0.082 | STANDARD |

**NJD @ COL** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 28.33, exp saves 24.84 (sd 6.56), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.75 (sd 6.93), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.224 | 0.345 | 36/67 | +0.091 | STANDARD |
| Nicolas Roy: 1+ assists | 0.100 | 0.215 | 22/79 | +0.098 | STANDARD |
| Mackenzie Blackwood: 27+ saves | 0.385 | 0.495 | 50/51 | +0.088 |  |
| Jack Hughes: 1+ assists | 0.357 | 0.465 | 47/54 | +0.086 | STANDARD |
| Jack Hughes: 1+ points | 0.532 | 0.620 | 63/39 | +0.061 | STANDARD |
| Luke Evangelista: 1+ points | 0.380 | 0.465 | 48/55 | +0.053 | STANDARD |

**TOR @ SEA** · priced 172/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROBABLE) exp shots 28.75, exp saves 24.87 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.18, exp saves 25.64 (sd 7.12), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.374 | 0.500 | 51/51 | +0.098 | STANDARD |
| Gavin McKenna: 1+ points | 0.437 | 0.545 | 56/47 | +0.075 | STANDARD |
| Auston Matthews: 2+ points | 0.261 | 0.360 | 37/65 | +0.073 | STANDARD |
| William Nylander: 2+ points | 0.231 | 0.320 | 33/69 | +0.064 | STANDARD |
| William Nylander: 1+ assists | 0.394 | 0.480 | 49/53 | +0.059 | STANDARD |
| Gavin McKenna: 1+ assists | 0.299 | 0.380 | 39/63 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
