# NHL slate 2026-10-23 — RESEARCH_ONLY

generated 2026-10-23T23:06:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2820 · contracts joined: 463 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 413, 'OK': 37, 'NO_EDGE': 13}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 68, 'game_early_goal': 2, 'first_goal': 76, 'game_winner': 4, 'player_goals': 127, 'game_overtime': 2, 'player_points': 86, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 2026-10-24T00:00:00Z | T-30m | 0.469 | 0.531 | 0.179 | 5.91 | 2.87 | 3.04 | 227 (25/202) | CONFIRMED/CONFIRMED |
| TBL @ COL | 2026-10-24T01:00:00Z | T-90m | 0.522 | 0.478 | 0.176 | 5.94 | 3.05 | 2.89 | 236 (25/211) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4 | team_total | 0.372 | 0.500 | 0.474 | 51 | 51 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL3 | team_total | 0.592 | 0.695 | 0.676 | 70 | 31 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT23TBCOL-5 | game_total | 0.741 | 0.825 | 0.810 | 83 | 18 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT23TBCOL-7 | game_total | 0.406 | 0.495 | 0.477 | 50 | 51 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-5 | game_total | 0.734 | 0.815 | 0.801 | 82 | 19 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL3 | game_spread | 0.177 | 0.255 | 0.238 | 26 | 75 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT23TBCOL-6 | game_total | 0.516 | 0.600 | 0.584 | 61 | 41 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL2 | game_spread | 0.299 | 0.375 | 0.359 | 38 | 63 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL2 | team_total | 0.799 | 0.865 | 0.853 | 87 | 14 | no | +0.053 | OK |
| KXNHLGAME-26OCT23MTLCHI-MTL | game_winner | 0.531 | 0.605 | 0.591 | 61 | 40 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT23TBCOL-4 | game_total | 0.831 | 0.895 | 0.884 | 90 | 11 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 | team_total | 0.372 | 0.445 | 0.430 | 45 | 56 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-7 | game_total | 0.402 | 0.475 | 0.460 | 48 | 53 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-6 | game_total | 0.513 | 0.590 | 0.575 | 60 | 42 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL5 | team_total | 0.197 | 0.275 | 0.258 | 29 | 74 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-4 | game_total | 0.827 | 0.885 | 0.875 | 89 | 12 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB4 | team_total | 0.340 | 0.410 | 0.396 | 42 | 60 | no | +0.043 | OK |
| KXNHLGAME-26OCT23MTLCHI-CHI | game_winner | 0.469 | 0.405 | 0.418 | 41 | 60 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-8 | game_total | 0.220 | 0.275 | 0.263 | 28 | 73 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT23TBCOL-8 | game_total | 0.221 | 0.280 | 0.268 | 29 | 73 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB3 | team_total | 0.559 | 0.620 | 0.608 | 63 | 39 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-9 | game_total | 0.150 | 0.195 | 0.185 | 20 | 81 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL2 | team_total | 0.802 | 0.845 | 0.837 | 85 | 16 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT23TBCOL-9 | game_total | 0.151 | 0.195 | 0.185 | 20 | 81 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-CHI2 | game_spread | 0.259 | 0.215 | 0.223 | 22 | 79 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL5 | team_total | 0.198 | 0.245 | 0.235 | 26 | 77 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB2 | team_total | 0.780 | 0.820 | 0.812 | 83 | 19 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL6 | team_total | 0.085 | 0.120 | 0.112 | 13 | 89 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT23TBCOL-COL3 | game_spread | 0.180 | 0.215 | 0.208 | 22 | 79 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL3 | team_total | 0.597 | 0.635 | 0.628 | 64 | 37 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-3 | game_total | 0.954 | 0.980 | 0.976 | 99 | 3 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT23TBCOL-3 | game_total | 0.955 | 0.980 | 0.976 | 99 | 3 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT23TBCOL-TB3 | game_spread | 0.149 | 0.175 | 0.169 | 18 | 83 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB5 | team_total | 0.170 | 0.205 | 0.198 | 22 | 81 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT23TBCOL-10 | game_total | 0.070 | 0.090 | 0.086 | 10 | 92 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-10 | game_total | 0.063 | 0.080 | 0.076 | 9 | 93 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI4 | team_total | 0.334 | 0.355 | 0.351 | 36 | 65 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT23TBCOL-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL6 | team_total | 0.086 | 0.105 | 0.101 | 12 | 91 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT23MTLCHI-CHI3 | game_spread | 0.146 | 0.135 | 0.137 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB6 | team_total | 0.070 | 0.080 | 0.078 | 9 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI2 | team_total | 0.777 | 0.785 | 0.783 | 79 | 22 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL2 | game_spread | 0.304 | 0.315 | 0.313 | 32 | 69 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-TB | game_winner | 0.478 | 0.465 | 0.468 | 47 | 54 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI3 | team_total | 0.554 | 0.565 | 0.563 | 57 | 44 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT23MTLCHI-2 | game_total | 0.979 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-TB2 | game_spread | 0.259 | 0.265 | 0.264 | 27 | 74 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI5 | team_total | 0.165 | 0.170 | 0.169 | 18 | 84 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI6 | team_total | 0.067 | 0.065 | 0.065 | 8 | 95 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-COL | game_winner | 0.522 | 0.525 | 0.524 | 53 | 48 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT23MTLCHI-CHI | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-MTL | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.095 |  | 10 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.860 |  | 87 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-CHI | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-MTL | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-CHI | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-MTL | period_winner |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-TIE | period_winner |  | 0.255 |  | 28 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1 | player_assists |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1 | player_assists |  | 0.460 |  | 47 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-2 | player_assists |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-2 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 0.469 | 0.495 | 0.179 | 0.221 | 5.91 | 6.30 | 0.987/0.983 | KXNHLTOTAL-26OCT23MTLCHI-7 +0.064 |
| TBL @ COL | 0.522 | 0.573 | 0.176 | 0.214 | 5.94 | 6.24 | 0.978/0.946 | KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 +0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 25c · p 0.2962 (adj 0.2834) · $6.24 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 57c · p 0.6861 (adj 0.6074) · $15.12 · thesis CHI:SUPPRESSED
- Spencer Knight: 27+ saves NO @ 50c · p 0.6594 (adj 0.5361) · $10.47 · thesis CHI:NET_LOW_VOLUME
- Montreal wins by over 2.5 goals NO @ 75c · p 0.8103 (adj 0.7776) · $18.16 · thesis CHI:WINS
- Brayden Point: 1+ goals YES @ 27c · p 0.3075 (adj 0.2969) · $4.57 · thesis TBL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 27c · p 0.3072 (adj 0.2941) · $3.41 · thesis COL:OFFENSE_4PLUS
- Andrei Vasilevskiy: 28+ saves NO @ 57c · p 0.645 (adj 0.5975) · $6.53 · thesis TBL:NET_LOW_VOLUME

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ CHI** · priced 171/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.77, exp saves 23.95 (sd 6.55), pull risk 0.065
- MTL net: Jacob Fowler (CONFIRMED) exp shots 25.85, exp saves 22.36 (sd 6.29), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 27+ saves | 0.341 | 0.505 | 51/50 | +0.142 |  |
| Oliver Kapanen: 1+ points | 0.377 | 0.505 | 51/50 | +0.105 | STANDARD |
| Patrick Kane: 1+ assists | 0.314 | 0.435 | 44/57 | +0.099 | STANDARD |
| Connor Bedard: 1+ points | 0.561 | 0.655 | 66/35 | +0.073 | STANDARD |
| Josh Anderson: 1+ assists | 0.253 | 0.160 | 18/86 | +0.062 | STANDARD |
| Connor Bedard: 1+ assists | 0.368 | 0.460 | 47/55 | +0.064 | STANDARD |

**TBL @ COL** · priced 166/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.7, exp saves 23.25 (sd 6.41), pull risk 0.053
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 29.24, exp saves 25.14 (sd 6.8), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.441 | 0.550 | 56/46 | +0.082 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.336 | 0.445 | 46/57 | +0.077 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.476 | 0.575 | 60/45 | +0.057 | STANDARD |
| Cale Makar: 1+ points | 0.543 | 0.640 | 65/37 | +0.070 | STANDARD |
| Andrei Vasilevskiy: 28+ saves | 0.355 | 0.450 | 47/57 | +0.058 |  |
| Nikita Kucherov: 2+ points | 0.292 | 0.385 | 39/62 | +0.071 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
