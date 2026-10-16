# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-16T08:27:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2475 · contracts joined: 102 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 52, 'NO_EDGE': 43, 'OK': 7}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'game_early_goal': 2, 'game_winner': 4, 'game_overtime': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 2026-10-17T01:00:00Z | T-12h | 0.639 | 0.361 | 0.160 | 6.70 | 3.82 | 2.88 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ ANA | 2026-10-17T02:00:00Z | T-12h | 0.489 | 0.511 | 0.167 | 6.32 | 3.12 | 3.19 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.182 | 0.205 | 0.200 | 21 | 80 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT16PITCOL-COL3 | game_spread | 0.290 | 0.315 | 0.310 | 32 | 69 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.890 | 0.905 | 0.902 | 91 | 10 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.172 | 0.155 | 0.158 | 16 | 85 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.871 | 0.885 | 0.882 | 89 | 12 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.075 | 0.055 | 0.058 | 7 | 96 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.840 | 0.836 | 85 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.094 | 0.080 | 0.083 | 9 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.125 | 0.115 | 0.117 | 12 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.968 | 0.965 | 0.966 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.977 | 0.970 | 0.971 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.361 | 0.345 | 0.348 | 35 | 66 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.639 | 0.655 | 0.652 | 66 | 35 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.166 | 0.175 | 0.173 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.185 | 0.175 | 0.177 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.101 | 0.095 | 0.096 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.101 | 0.095 | 0.096 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.774 | 0.765 | 0.767 | 77 | 24 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.336 | 0.320 | 0.323 | 33 | 69 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.274 | 0.265 | 0.267 | 27 | 74 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.893 | 0.895 | 0.895 | 90 | 11 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.242 | 0.235 | 0.236 | 24 | 77 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.332 | 0.325 | 0.326 | 33 | 68 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.466 | 0.475 | 0.473 | 48 | 53 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.301 | 0.295 | 0.296 | 30 | 71 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.280 | 0.275 | 0.276 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.814 | 0.820 | 0.819 | 83 | 19 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.194 | 0.195 | 0.195 | 20 | 81 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.582 | 0.575 | 0.576 | 58 | 43 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.090 | 0.090 | 0.090 | 10 | 92 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.185 | 0.180 | 0.181 | 19 | 83 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.541 | 0.555 | 0.552 | 57 | 46 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.511 | 0.515 | 0.514 | 52 | 49 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.529 | 0.525 | 0.526 | 53 | 48 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.213 | 0.205 | 0.207 | 22 | 81 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.787 | 0.790 | 0.789 | 80 | 22 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.624 | 0.630 | 0.629 | 64 | 38 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.642 | 0.640 | 0.640 | 65 | 37 |  | -0.024 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.823 | 0.825 | 0.825 | 84 | 19 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.228 | 0.225 | 0.226 | 24 | 79 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.549 | 0.550 | 0.550 | 56 | 46 |  | -0.026 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.742 | 0.750 | 0.748 | 77 | 27 |  | -0.026 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.341 | 0.350 | 0.348 | 37 | 67 |  | -0.026 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.489 | 0.490 | 0.490 | 50 | 52 |  | -0.027 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.392 | 0.395 | 0.394 | 41 | 62 |  | -0.028 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.607 | 0.605 | 0.605 | 62 | 41 |  | -0.029 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.410 | 0.410 | 0.410 | 43 | 61 |  | -0.037 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.400 |  | 42 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.580 |  | 59 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.265 |  | 29 | 76 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.275 |  | 30 | 75 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.055 |  | 9 | 98 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.645 |  | 67 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.370 |  | 39 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.470 |  | 49 | 55 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.275 |  | 30 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.915 |  | 94 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.680 |  | 70 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.415 |  | 44 | 61 |  |  | UNSUPPORTED |
| KXNHLF10G-26OCT16PITCOL-Y | game_early_goal |  | 0.595 |  | 61 | 42 |  |  | UNSUPPORTED |
| KXNHLOT-26OCT16PITCOL-1 | game_overtime |  | 0.210 |  | 22 | 80 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-ANA | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-BOS | period_winner |  | 0.335 |  | 36 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16BOSANA-ANA2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.639 | 0.623 | 0.160 | 0.206 | 6.70 | 6.66 | 0.976/1.033 | KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 -0.023 |
| BOS @ ANA | 0.489 | 0.531 | 0.167 | 0.213 | 6.32 | 6.70 | 1.024/0.968 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.95, exp saves 22.74 (sd 6.28), pull risk 0.058
- PIT net: Arturs Silovs (PROJECTED) exp shots 30.66, exp saves 25.82 (sd 7.3), pull risk 0.091

**BOS @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.7, exp saves 22.25 (sd 6.24), pull risk 0.067
- BOS net: Jeremy Swayman (PROJECTED) exp shots 31.08, exp saves 26.51 (sd 7.27), pull risk 0.083

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
