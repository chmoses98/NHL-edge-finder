# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-29T00:44:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 2 · markets on board: 3254 · contracts joined: 462 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 412, 'NO_EDGE': 15, 'OK': 35}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 68, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 127, 'game_overtime': 2, 'player_points': 88, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ COL | 2026-10-29T01:00:00Z | T-10m | 0.578 | 0.422 | 0.173 | 6.13 | 3.31 | 2.81 | 233 (25/208) | CONFIRMED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-60m | 0.572 | 0.428 | 0.165 | 6.84 | 3.67 | 3.17 | 229 (25/204) | PROBABLE/CONFIRMED |

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
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.399 | 0.475 | 0.460 | 48 | 53 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.613 | 0.685 | 0.671 | 69 | 32 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.166 | 0.100 | 0.111 | 11 | 91 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.813 | 0.870 | 0.860 | 88 | 14 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.218 | 0.280 | 0.267 | 29 | 73 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.765 | 0.815 | 0.806 | 82 | 19 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.438 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.551 | 0.605 | 0.594 | 61 | 40 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.876 | 0.835 | 0.844 | 84 | 17 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.141 | 0.105 | 0.111 | 11 | 90 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.850 | 0.885 | 0.879 | 89 | 12 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.353 | 0.315 | 0.323 | 32 | 69 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.765 | 0.795 | 0.789 | 80 | 21 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.321 | 0.360 | 0.352 | 37 | 65 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.224 | 0.255 | 0.249 | 26 | 75 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.841 | 0.870 | 0.865 | 88 | 14 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.104 | 0.125 | 0.120 | 13 | 88 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.172 | 0.195 | 0.190 | 20 | 81 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.435 | 0.465 | 0.459 | 47 | 54 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.248 | 0.275 | 0.270 | 28 | 73 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.647 | 0.680 | 0.674 | 69 | 33 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT28NJCOL-10 | game_total | 0.079 | 0.095 | 0.092 | 10 | 91 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.963 | 0.975 | 0.973 | 98 | 3 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.901 | 0.920 | 0.916 | 93 | 9 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.246 | 0.270 | 0.265 | 28 | 74 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.543 | 0.565 | 0.561 | 57 | 44 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.263 | 0.240 | 0.244 | 25 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-7 | game_total | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.221 | 0.235 | 0.232 | 24 | 77 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-6 | game_total | 0.653 | 0.635 | 0.639 | 64 | 37 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.125 | 0.135 | 0.133 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.835 | 0.850 | 0.847 | 86 | 16 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL6 | team_total | 0.117 | 0.125 | 0.123 | 13 | 88 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.157 | 0.175 | 0.171 | 19 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-3 | game_total | 0.979 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT28NJCOL-NJ | game_winner | 0.422 | 0.425 | 0.424 | 43 | 58 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT28NJCOL-COL | game_winner | 0.578 | 0.575 | 0.576 | 58 | 43 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-COL2 | game_spread | 0.354 | 0.355 | 0.355 | 36 | 65 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT28NJCOL-COL | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT28NJCOL-NJ | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT28NJCOL-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT28NJCOL-COL2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT28NJCOL-NJ2 | period_spread |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT28NJCOL-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT28NJCOL-2 | period_total |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT28NJCOL-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT28NJCOL-COL | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT28NJCOL-NJ | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT28NJCOL-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT28NJCOL-COL2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT28NJCOL-NJ2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT28NJCOL-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT28NJCOL-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT28NJCOL-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT28NJCOL-COL | period_winner |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT28NJCOL-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT28NJCOL-TIE | period_winner |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT28NJCOL-COL2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT28NJCOL-NJ2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT28NJCOL-1 | period_total |  | 0.895 |  | 93 | 14 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT28NJCOL-2 | period_total |  | 0.675 |  | 69 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT28NJCOL-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28NJCOL-COLALEHKONEN62-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28NJCOL-COLALEHKONEN62-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28NJCOL-COLBNELSON11-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28NJCOL-COLBNELSON11-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28NJCOL-COLCMAKAR8-1 | player_assists |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28NJCOL-COLCMAKAR8-2 | player_assists |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ COL | 0.578 | 0.625 | 0.173 | 0.215 | 6.13 | 6.34 | 0.979/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.061 |
| TOR @ SEA | 0.572 | 0.560 | 0.165 | 0.210 | 6.84 | 6.67 | 1.019/0.988 | KXNHLTOTAL-26OCT28TORSEA-8 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Nicolas Roy: 1+ assists NO @ 79c · p 0.8998 (adj 0.8252) · $20.0 · thesis COL:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 66c · p 0.7765 (adj 0.6943) · $16.73 · thesis NJD:SUPPRESSED
- Amadeus Lombardi: 1+ goals YES @ 10c · p 0.1235 (adj 0.1164) · $2.8 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ assists NO @ 54c · p 0.643 (adj 0.5696) · $7.1 · thesis NJD:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1554 (adj 0.1403) · $8.38 · thesis TOR:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 16c · p 0.219 (adj 0.203) · $9.16 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1598 (adj 0.1449) · $6.98 · thesis SEA:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ goals YES @ 20c · p 0.2484 (adj 0.2351) · $7.52 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ COL** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 28.33, exp saves 24.84 (sd 6.56), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.75 (sd 6.93), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.224 | 0.350 | 36/66 | +0.101 | STANDARD |
| Nicolas Roy: 1+ assists | 0.100 | 0.215 | 22/79 | +0.098 | STANDARD |
| Jack Hughes: 1+ assists | 0.357 | 0.470 | 48/54 | +0.086 | STANDARD |
| Mackenzie Blackwood: 27+ saves | 0.385 | 0.480 | 50/54 | +0.058 |  |
| Jack Hughes: 1+ points | 0.532 | 0.620 | 63/39 | +0.061 | STANDARD |
| Luke Evangelista: 1+ points | 0.380 | 0.465 | 47/54 | +0.063 | STANDARD |

**TOR @ SEA** · priced 172/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROBABLE) exp shots 28.75, exp saves 24.87 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.18, exp saves 25.64 (sd 7.12), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.374 | 0.500 | 51/51 | +0.098 | STANDARD |
| Auston Matthews: 2+ points | 0.261 | 0.365 | 37/64 | +0.083 | STANDARD |
| Gavin McKenna: 1+ points | 0.437 | 0.540 | 55/47 | +0.075 | STANDARD |
| William Nylander: 1+ assists | 0.394 | 0.490 | 50/52 | +0.069 | STANDARD |
| William Nylander: 2+ points | 0.231 | 0.315 | 32/69 | +0.064 | STANDARD |
| Gavin McKenna: 1+ assists | 0.299 | 0.380 | 39/63 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
