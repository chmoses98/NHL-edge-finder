# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-16T11:16:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2475 · contracts joined: 102 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 52, 'NO_EDGE': 45, 'OK': 5}
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
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.871 | 0.885 | 0.882 | 89 | 12 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.075 | 0.060 | 0.063 | 7 | 95 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.094 | 0.085 | 0.087 | 9 | 92 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.125 | 0.115 | 0.117 | 12 | 89 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.823 | 0.835 | 0.833 | 84 | 17 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.968 | 0.965 | 0.966 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.361 | 0.345 | 0.348 | 35 | 66 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.639 | 0.655 | 0.652 | 66 | 35 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.166 | 0.175 | 0.173 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.185 | 0.175 | 0.177 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.101 | 0.095 | 0.096 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.890 | 0.900 | 0.898 | 91 | 11 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.541 | 0.560 | 0.556 | 57 | 45 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.172 | 0.160 | 0.162 | 17 | 85 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.774 | 0.765 | 0.767 | 77 | 24 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.213 | 0.205 | 0.207 | 21 | 80 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.787 | 0.795 | 0.793 | 80 | 21 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.274 | 0.265 | 0.267 | 27 | 74 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.893 | 0.900 | 0.899 | 91 | 11 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.835 | 0.832 | 85 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.242 | 0.235 | 0.236 | 24 | 77 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.332 | 0.325 | 0.326 | 33 | 68 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.466 | 0.475 | 0.473 | 48 | 53 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.642 | 0.635 | 0.636 | 64 | 37 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.301 | 0.295 | 0.296 | 30 | 71 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.280 | 0.275 | 0.276 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.814 | 0.820 | 0.819 | 83 | 19 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.194 | 0.195 | 0.195 | 20 | 81 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.228 | 0.215 | 0.217 | 23 | 80 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.582 | 0.575 | 0.576 | 58 | 43 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.185 | 0.185 | 0.185 | 19 | 82 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.090 | 0.085 | 0.086 | 10 | 93 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.742 | 0.755 | 0.753 | 77 | 26 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.101 | 0.100 | 0.100 | 11 | 91 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.341 | 0.360 | 0.356 | 38 | 66 |  | -0.017 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.489 | 0.485 | 0.486 | 49 | 52 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.511 | 0.515 | 0.514 | 52 | 49 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.529 | 0.525 | 0.526 | 53 | 48 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.549 | 0.545 | 0.546 | 55 | 46 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.336 | 0.325 | 0.327 | 34 | 69 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.607 | 0.610 | 0.609 | 62 | 40 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.392 | 0.395 | 0.394 | 41 | 62 |  | -0.028 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.624 | 0.625 | 0.625 | 64 | 39 |  | -0.031 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.410 | 0.410 | 0.410 | 43 | 61 |  | -0.037 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.400 |  | 42 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.310 |  | 33 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.580 |  | 59 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.275 |  | 30 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.270 |  | 30 | 76 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.050 |  | 8 | 98 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.660 |  | 68 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.390 |  | 41 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.480 |  | 50 | 54 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.270 |  | 30 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.245 |  | 27 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.685 |  | 71 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.415 |  | 44 | 61 |  |  | UNSUPPORTED |
| KXNHLF10G-26OCT16PITCOL-Y | game_early_goal |  | 0.595 |  | 61 | 42 |  |  | UNSUPPORTED |
| KXNHLOT-26OCT16PITCOL-1 | game_overtime |  | 0.210 |  | 22 | 80 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-ANA | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-BOS | period_winner |  | 0.335 |  | 36 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-TIE | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16BOSANA-ANA2 | period_spread |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.639 | 0.623 | 0.160 | 0.206 | 6.70 | 6.66 | 0.976/1.033 | KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 -0.023 |
| BOS @ ANA | 0.489 | 0.531 | 0.167 | 0.213 | 6.32 | 6.70 | 1.024/0.968 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 1 recommended · full analysis in card.md / packet.json `thesis_card`

- Anaheim over 4.5 goals scored YES @ 21c · p 0.2791 (adj 0.2421) · $3.64 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.95, exp saves 22.74 (sd 6.28), pull risk 0.058
- PIT net: Arturs Silovs (PROJECTED) exp shots 30.66, exp saves 25.82 (sd 7.3), pull risk 0.091

**BOS @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 25.7, exp saves 22.25 (sd 6.24), pull risk 0.067
- BOS net: Jeremy Swayman (PROJECTED) exp shots 31.08, exp saves 26.51 (sd 7.27), pull risk 0.083

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
