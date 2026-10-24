# NHL slate 2026-10-23 — RESEARCH_ONLY

generated 2026-10-24T00:25:54Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 1 · markets on board: 2791 · contracts joined: 236 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 211, 'NO_EDGE': 6, 'OK': 19}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 36, 'game_early_goal': 1, 'first_goal': 38, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 45, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ COL | 2026-10-24T01:00:00Z | T-30m | 0.522 | 0.478 | 0.176 | 5.94 | 3.05 | 2.89 | 236 (25/211) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT23TBCOL-5 | game_total | 0.741 | 0.825 | 0.810 | 83 | 18 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT23TBCOL-7 | game_total | 0.406 | 0.495 | 0.477 | 50 | 51 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT23TBCOL-6 | game_total | 0.516 | 0.595 | 0.579 | 60 | 41 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 | team_total | 0.372 | 0.445 | 0.430 | 45 | 56 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB4 | team_total | 0.340 | 0.405 | 0.392 | 41 | 60 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT23TBCOL-4 | game_total | 0.831 | 0.890 | 0.880 | 90 | 12 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB5 | team_total | 0.170 | 0.225 | 0.213 | 23 | 78 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT23TBCOL-8 | game_total | 0.221 | 0.280 | 0.268 | 29 | 73 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB3 | team_total | 0.559 | 0.620 | 0.608 | 63 | 39 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT23TBCOL-9 | game_total | 0.151 | 0.195 | 0.185 | 20 | 81 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL5 | team_total | 0.198 | 0.245 | 0.235 | 26 | 77 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB2 | team_total | 0.780 | 0.820 | 0.812 | 83 | 19 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL2 | team_total | 0.802 | 0.840 | 0.833 | 85 | 17 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL3 | team_total | 0.597 | 0.640 | 0.632 | 65 | 37 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT23TBCOL-10 | game_total | 0.070 | 0.095 | 0.089 | 10 | 91 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT23TBCOL-3 | game_total | 0.955 | 0.975 | 0.972 | 98 | 3 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT23TBCOL-TB3 | game_spread | 0.149 | 0.175 | 0.169 | 18 | 83 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT23TBCOL-COL3 | game_spread | 0.180 | 0.205 | 0.200 | 21 | 80 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL6 | team_total | 0.086 | 0.110 | 0.105 | 12 | 90 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT23TBCOL-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB6 | team_total | 0.070 | 0.085 | 0.082 | 10 | 93 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL2 | game_spread | 0.304 | 0.315 | 0.313 | 32 | 69 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-TB2 | game_spread | 0.259 | 0.265 | 0.264 | 27 | 74 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-COL | game_winner | 0.522 | 0.525 | 0.524 | 53 | 48 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-TB | game_winner | 0.478 | 0.475 | 0.476 | 48 | 53 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT23TBCOL-COL | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23TBCOL-TB | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23TBCOL-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23TBCOL-COL2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23TBCOL-TB2 | period_spread |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23TBCOL-1 | period_total |  | 0.860 |  | 88 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23TBCOL-2 | period_total |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23TBCOL-3 | period_total |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23TBCOL-COL | period_winner |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23TBCOL-TB | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23TBCOL-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23TBCOL-COL2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23TBCOL-TB2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23TBCOL-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23TBCOL-2 | period_total |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23TBCOL-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23TBCOL-COL | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23TBCOL-TB | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23TBCOL-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23TBCOL-COL2 | period_spread |  | 0.175 |  | 20 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23TBCOL-TB2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23TBCOL-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23TBCOL-2 | period_total |  | 0.670 |  | 69 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23TBCOL-3 | period_total |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLALEHKONEN62-1 | player_assists |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLALEHKONEN62-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLBNELSON11-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLBNELSON11-2 | player_assists |  | 0.045 |  | 8 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLCMAKAR8-1 | player_assists |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLCMAKAR8-2 | player_assists |  | 0.165 |  | 19 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLCMAKAR8-3 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLDTOEWS7-1 | player_assists |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLDTOEWS7-2 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLGLANDESKOG92-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLGLANDESKOG92-2 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLJSCHWARTZ71-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLMNECAS88-1 | player_assists |  | 0.440 |  | 45 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLMNECAS88-2 | player_assists |  | 0.115 |  | 14 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLNKADRI91-1 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLNKADRI91-2 | player_assists |  | 0.075 |  | 10 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLNMACKINNON29-1 | player_assists |  | 0.590 |  | 60 | 42 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLNMACKINNON29-2 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLNMACKINNON29-3 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-COLTHUGHES13-1 | player_assists |  | 0.215 |  | 22 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBACIRELLI71-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBBHAGEL38-1 | player_assists |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBBHAGEL38-2 | player_assists |  | 0.085 |  | 11 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBBPOINT21-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBBPOINT21-2 | player_assists |  | 0.070 |  | 10 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBCDASTOUS51-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBCDASTOUS51-2 | player_assists |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBGGONCALVES93-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBGGONCALVES93-2 | player_assists |  | 0.035 |  | 5 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBJCARLSON74-1 | player_assists |  | 0.355 |  | 37 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23TBCOL-TBJCARLSON74-2 | player_assists |  | 0.070 |  | 10 | 96 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ COL | 0.522 | 0.573 | 0.176 | 0.214 | 5.94 | 6.24 | 0.978/0.946 | KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 +0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Josh Manson: 1+ goals YES @ 4c · p 0.062 (adj 0.0565) · $3.22 · thesis COL:OFFENSE_4PLUS
- Brayden Point: 1+ goals YES @ 27c · p 0.3075 (adj 0.2969) · $5.6 · thesis TBL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 27c · p 0.3072 (adj 0.2966) · $4.46 · thesis COL:OFFENSE_4PLUS
- Tampa Bay over 4.5 goals scored NO @ 78c · p 0.8296 (adj 0.8023) · $17.03 · thesis COL:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ COL** · priced 166/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.7, exp saves 23.25 (sd 6.41), pull risk 0.053
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 29.24, exp saves 25.14 (sd 6.8), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.441 | 0.555 | 56/45 | +0.092 | STANDARD |
| Nikita Kucherov: 2+ points | 0.292 | 0.405 | 41/60 | +0.091 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.476 | 0.585 | 59/42 | +0.087 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.336 | 0.445 | 46/57 | +0.077 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.494 | 0.590 | 60/42 | +0.069 | STANDARD |
| Andrei Vasilevskiy: 28+ saves | 0.355 | 0.450 | 47/57 | +0.058 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
