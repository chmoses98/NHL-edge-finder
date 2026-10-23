# NHL slate 2026-10-23 — RESEARCH_ONLY

generated 2026-10-23T15:53:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2765 · contracts joined: 449 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 399, 'OK': 35, 'NO_EDGE': 15}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 66, 'game_early_goal': 2, 'first_goal': 74, 'game_winner': 4, 'player_goals': 125, 'game_overtime': 2, 'player_points': 82, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 2026-10-24T00:00:00Z | T-6h | 0.481 | 0.519 | 0.184 | 6.00 | 2.94 | 3.06 | 217 (25/192) | PROJECTED/PROJECTED |
| TBL @ COL | 2026-10-24T01:00:00Z | T-6h | 0.538 | 0.462 | 0.176 | 6.07 | 3.16 | 2.92 | 232 (25/207) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4 | team_total | 0.380 | 0.480 | 0.460 | 49 | 53 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL3 | team_total | 0.595 | 0.690 | 0.672 | 70 | 32 | no | +0.070 | OK |
| KXNHLGAME-26OCT23MTLCHI-CHI | game_winner | 0.481 | 0.395 | 0.412 | 40 | 61 | yes | +0.064 | OK |
| KXNHLGAME-26OCT23MTLCHI-MTL | game_winner | 0.519 | 0.605 | 0.588 | 61 | 40 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL2 | game_spread | 0.294 | 0.375 | 0.358 | 38 | 63 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-MTL3 | game_spread | 0.179 | 0.255 | 0.238 | 26 | 75 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL5 | team_total | 0.200 | 0.280 | 0.262 | 29 | 73 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT23TBCOL-7 | game_total | 0.425 | 0.495 | 0.481 | 50 | 51 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL2 | team_total | 0.804 | 0.855 | 0.846 | 86 | 15 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-6 | game_total | 0.528 | 0.590 | 0.578 | 60 | 42 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT23TBCOL-4 | game_total | 0.849 | 0.895 | 0.887 | 90 | 11 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT23TBCOL-6 | game_total | 0.539 | 0.595 | 0.584 | 60 | 41 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-7 | game_total | 0.419 | 0.475 | 0.464 | 48 | 53 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-CHI2 | game_spread | 0.262 | 0.215 | 0.224 | 22 | 79 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-5 | game_total | 0.749 | 0.795 | 0.786 | 80 | 21 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT23TBCOL-5 | game_total | 0.761 | 0.810 | 0.801 | 82 | 20 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-4 | game_total | 0.836 | 0.880 | 0.872 | 89 | 13 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-8 | game_total | 0.231 | 0.275 | 0.266 | 28 | 73 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB3 | team_total | 0.563 | 0.610 | 0.601 | 62 | 40 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB4 | team_total | 0.344 | 0.395 | 0.385 | 41 | 62 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT23TBCOL-8 | game_total | 0.237 | 0.280 | 0.271 | 29 | 73 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL6 | team_total | 0.086 | 0.125 | 0.116 | 14 | 89 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 | team_total | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-9 | game_total | 0.158 | 0.190 | 0.183 | 20 | 82 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-3 | game_total | 0.959 | 0.980 | 0.977 | 99 | 3 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT23TBCOL-3 | game_total | 0.961 | 0.980 | 0.977 | 99 | 3 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB2 | team_total | 0.782 | 0.815 | 0.809 | 83 | 20 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT23MTLCHI-CHI3 | game_spread | 0.154 | 0.135 | 0.139 | 14 | 87 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL3 | team_total | 0.619 | 0.650 | 0.644 | 66 | 36 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT23TBCOL-9 | game_total | 0.165 | 0.190 | 0.185 | 20 | 82 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB5 | team_total | 0.175 | 0.205 | 0.199 | 22 | 81 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL2 | team_total | 0.817 | 0.840 | 0.836 | 85 | 17 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT23TBCOL-TB3 | game_spread | 0.148 | 0.165 | 0.161 | 17 | 84 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL5 | team_total | 0.217 | 0.240 | 0.235 | 25 | 77 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT23TBCOL-10 | game_total | 0.075 | 0.090 | 0.087 | 10 | 92 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT23MTLCHI-10 | game_total | 0.068 | 0.080 | 0.077 | 9 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT23MTLCHI-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT23TBCOL-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL3 | game_spread | 0.195 | 0.210 | 0.207 | 22 | 80 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-TB6 | team_total | 0.073 | 0.080 | 0.079 | 9 | 93 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-TB2 | game_spread | 0.254 | 0.265 | 0.263 | 27 | 74 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT23TBCOL-COL2 | game_spread | 0.315 | 0.325 | 0.323 | 33 | 68 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI6 | team_total | 0.074 | 0.065 | 0.067 | 8 | 95 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI2 | team_total | 0.789 | 0.785 | 0.786 | 79 | 22 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI5 | team_total | 0.177 | 0.165 | 0.167 | 18 | 85 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23TBCOL-COL6 | team_total | 0.099 | 0.105 | 0.104 | 12 | 91 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI3 | team_total | 0.569 | 0.555 | 0.558 | 57 | 46 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT23MTLCHI-CHI4 | team_total | 0.347 | 0.335 | 0.337 | 35 | 68 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-TB | game_winner | 0.462 | 0.465 | 0.464 | 47 | 54 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT23TBCOL-COL | game_winner | 0.538 | 0.535 | 0.536 | 54 | 47 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT23MTLCHI-CHI | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-MTL | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT23MTLCHI-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.835 |  | 85 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.560 |  | 57 | 45 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-CHI | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-MTL | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT23MTLCHI-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.055 |  | 9 | 98 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.895 |  | 93 | 14 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.605 |  | 62 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-CHI | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-MTL | period_winner |  | 0.410 |  | 44 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT23MTLCHI-TIE | period_winner |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-CHI2 | period_spread |  | 0.095 |  | 12 | 93 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT23MTLCHI-MTL2 | period_spread |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-1 | period_total |  | 0.890 |  | 91 | 13 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-2 | period_total |  | 0.670 |  | 69 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT23MTLCHI-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1 | player_assists |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1 | player_assists |  | 0.460 |  | 48 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-2 | player_assists |  | 0.100 |  | 14 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-1 | player_assists |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT23MTLCHI-CHIFNAZAR91-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ CHI | 0.481 | 0.481 | 0.184 | 0.224 | 6.00 | 6.33 | 1.003/0.976 | KXNHLTOTAL-26OCT23MTLCHI-7 +0.056 |
| TBL @ COL | 0.538 | 0.579 | 0.176 | 0.216 | 6.07 | 6.27 | 0.976/0.957 | KXNHLTEAMTOTAL-26OCT23TBCOL-COL4 +0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 5 recommended · full analysis in card.md / packet.json `thesis_card`

- Anton Frondell: 1+ goals YES @ 20c · p 0.2476 (adj 0.2332) · $6.64 · thesis CHI:OFFENSE_4PLUS
- Cole Caufield: 1+ assists NO @ 56c · p 0.6477 (adj 0.6014) · $13.77 · thesis MTL:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 25c · p 0.2979 (adj 0.2847) · $7.21 · thesis CHI:OFFENSE_4PLUS
- Oliver Kapanen: 1+ assists NO @ 69c · p 0.7722 (adj 0.7236) · $16.23 · thesis MTL:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 27c · p 0.3074 (adj 0.2968) · $4.44 · thesis COL:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ CHI** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.77, exp saves 23.93 (sd 6.59), pull risk 0.067
- MTL net: Jacob Fowler (PROJECTED) exp shots 25.85, exp saves 22.38 (sd 6.23), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zachary Bolduc: 1+ points | 0.432 | 0.245 | 41/92 | +0.005 | STANDARD |
| Josh Anderson: 1+ points | 0.409 | 0.235 | 36/89 | +0.032 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.302 | 0.145 | 28/99 | +0.008 | STANDARD |
| Alex Newhook: 1+ assists | 0.294 | 0.150 | 28/98 | +0.000 | STANDARD |
| Josh Anderson: 1+ assists | 0.249 | 0.115 | 22/99 | +0.017 | STANDARD |
| Oliver Kapanen: 1+ points | 0.380 | 0.510 | 52/50 | +0.102 | STANDARD |

**TBL @ COL** · priced 164/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.7, exp saves 23.26 (sd 6.31), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 29.24, exp saves 25.08 (sd 6.81), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| T.J. Hughes: 1+ points | 0.371 | 0.210 | 39/97 | -0.036 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.341 | 0.465 | 47/54 | +0.102 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.471 | 0.580 | 59/43 | +0.082 | STANDARD |
| Nikita Kucherov: 2+ points | 0.286 | 0.375 | 39/64 | +0.058 | STANDARD |
| Jaden Schwartz: 1+ points | 0.377 | 0.290 | 40/82 | -0.040 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.493 | 0.580 | 59/43 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
