# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-29T01:12:24Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 1 · markets on board: 3346 · contracts joined: 229 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 204, 'OK': 18, 'NO_EDGE': 7}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 33, 'game_early_goal': 1, 'first_goal': 36, 'game_winner': 2, 'player_goals': 66, 'game_overtime': 1, 'player_points': 41, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ SEA | 2026-10-29T02:00:00Z | T-30m | 0.572 | 0.428 | 0.165 | 6.84 | 3.67 | 3.17 | 229 (25/204) | PROBABLE/CONFIRMED |

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
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.613 | 0.680 | 0.667 | 69 | 33 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.813 | 0.865 | 0.856 | 87 | 14 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.166 | 0.105 | 0.115 | 12 | 91 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.218 | 0.280 | 0.267 | 29 | 73 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.876 | 0.830 | 0.840 | 84 | 18 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.141 | 0.105 | 0.111 | 11 | 90 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.353 | 0.315 | 0.323 | 32 | 69 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.104 | 0.135 | 0.128 | 15 | 88 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.263 | 0.240 | 0.244 | 25 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-7 | game_total | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.992 | 0.990 | 0.990 |  | 1 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-6 | game_total | 0.653 | 0.635 | 0.639 | 64 | 37 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.901 | 0.910 | 0.908 | 92 | 10 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-3 | game_total | 0.979 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.835 | 0.840 | 0.839 | 85 | 17 |  | -0.015 | NO_EDGE |
| KXNHL1P-26OCT28TORSEA-SEA | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT28TORSEA-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT28TORSEA-TOR | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT28TORSEA-SEA2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT28TORSEA-TOR2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT28TORSEA-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT28TORSEA-2 | period_total |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT28TORSEA-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT28TORSEA-SEA | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT28TORSEA-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT28TORSEA-TOR | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT28TORSEA-SEA2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT28TORSEA-TOR2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT28TORSEA-1 | period_total |  | 0.910 |  | 95 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT28TORSEA-2 | period_total |  | 0.635 |  | 64 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT28TORSEA-3 | period_total |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT28TORSEA-SEA | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT28TORSEA-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT28TORSEA-TOR | period_winner |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT28TORSEA-SEA2 | period_spread |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT28TORSEA-TOR2 | period_spread |  | 0.185 |  | 21 | 84 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT28TORSEA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT28TORSEA-2 | period_total |  | 0.695 |  | 71 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT28TORSEA-3 | period_total |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEABCATTON27-1 | player_assists |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEABCATTON27-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEABMCMANN74-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEABMCMANN74-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEABMONTOUR62-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEABMONTOUR62-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEACSTEPHENSON9-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEACSTEPHENSON9-2 | player_assists |  | 0.065 |  | 10 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAJEBERLE7-1 | player_assists |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAJEBERLE7-2 | player_assists |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAKKAKKO84-1 | player_assists |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAKKAKKO84-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAMBENIERS10-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAMBENIERS10-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAMSAMOSKEVICH11-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAMSAMOSKEVICH11-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAVDUNN29-1 | player_assists |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-SEAVDUNN29-2 | player_assists |  | 0.095 |  | 12 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORAMATTHEWS34-1 | player_assists |  | 0.500 |  | 51 | 51 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORAMATTHEWS34-2 | player_assists |  | 0.135 |  | 16 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORDRADDYSH43-1 | player_assists |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORDRADDYSH43-2 | player_assists |  | 0.115 |  | 14 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORECOWAN53-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORECOWAN53-2 | player_assists |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORGMCKENNA92-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORGMCKENNA92-2 | player_assists |  | 0.075 |  | 10 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORJROSLOVIC96-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORJROSLOVIC96-2 | player_assists |  | 0.055 |  | 8 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORMRIELLY44-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORMRIELLY44-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT28TORSEA-TORNPAUL20-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ SEA | 0.572 | 0.560 | 0.165 | 0.210 | 6.84 | 6.67 | 1.019/0.988 | KXNHLTOTAL-26OCT28TORSEA-8 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 10c · p 0.1554 (adj 0.1403) · $8.37 · thesis TOR:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1598 (adj 0.1461) · $7.35 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 16c · p 0.219 (adj 0.203) · $9.15 · thesis SEA:OFFENSE_4PLUS
- Mackie Samoskevich: 1+ goals YES @ 20c · p 0.2484 (adj 0.2351) · $7.52 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TOR @ SEA** · priced 172/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROBABLE) exp shots 28.75, exp saves 24.87 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.18, exp saves 25.64 (sd 7.12), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.374 | 0.500 | 51/51 | +0.098 | STANDARD |
| Gavin McKenna: 1+ points | 0.437 | 0.545 | 55/46 | +0.086 | STANDARD |
| Auston Matthews: 2+ points | 0.261 | 0.365 | 37/64 | +0.083 | STANDARD |
| William Nylander: 1+ assists | 0.394 | 0.480 | 49/53 | +0.059 | STANDARD |
| William Nylander: 2+ points | 0.231 | 0.315 | 32/69 | +0.064 | STANDARD |
| Gavin McKenna: 1+ assists | 0.299 | 0.380 | 39/63 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
