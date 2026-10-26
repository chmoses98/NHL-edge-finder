# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-26T01:09:01Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 1 · markets on board: 2617 · contracts joined: 228 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 203, 'OK': 20, 'NO_EDGE': 5}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 34, 'game_early_goal': 1, 'first_goal': 35, 'game_winner': 2, 'player_goals': 60, 'game_overtime': 1, 'player_points': 46, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ VAN | 2026-10-26T02:00:00Z | T-30m | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.417 | 0.325 | 0.343 | 33 | 68 | yes | +0.072 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.552 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.448 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.627 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 16 | 85 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.223 | 0.305 | 0.287 | 31 | 70 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.765 | 0.778 | 77 | 24 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.351 | 0.305 | 0.314 | 31 | 70 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.065 | 0.072 | 8 | 95 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.115 | 0.121 | 12 | 89 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.735 | 0.728 | 74 | 27 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.867 | 0.900 | 0.894 | 91 | 11 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.100 | 0.106 | 11 | 91 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.515 | 0.522 | 52 | 49 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.625 | 0.631 | 63 | 38 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5 | team_total | 0.298 | 0.330 | 0.323 | 34 | 68 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25MINVAN-5 | game_total | 0.837 | 0.825 | 0.828 | 83 | 18 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-4 | game_total | 0.902 | 0.895 | 0.896 | 90 | 11 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-3 | game_total | 0.978 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-2 | game_total | 0.991 | 0.990 | 0.990 |  | 2 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN6 | team_total | 0.152 | 0.155 | 0.154 | 17 | 86 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT25MINVAN-MIN | period_winner |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT25MINVAN-TIE | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT25MINVAN-VAN | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT25MINVAN-MIN2 | period_spread |  | 0.155 |  | 16 | 85 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT25MINVAN-VAN2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT25MINVAN-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT25MINVAN-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT25MINVAN-3 | period_total |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT25MINVAN-MIN | period_winner |  | 0.445 |  | 45 | 56 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT25MINVAN-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT25MINVAN-VAN | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT25MINVAN-MIN2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT25MINVAN-VAN2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT25MINVAN-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT25MINVAN-2 | period_total |  | 0.635 |  | 65 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT25MINVAN-3 | period_total |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT25MINVAN-MIN | period_winner |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT25MINVAN-TIE | period_winner |  | 0.250 |  | 27 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT25MINVAN-VAN | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT25MINVAN-MIN2 | period_spread |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT25MINVAN-VAN2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT25MINVAN-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT25MINVAN-2 | period_total |  | 0.675 |  | 69 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT25MINVAN-3 | period_total |  | 0.400 |  | 42 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINBBRINK10-1 | player_assists |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINBBRINK10-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINBCOLEMAN20-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINDYUROV22-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINJBRODIN25-1 | player_assists |  | 0.225 |  | 25 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINJERIKSSONEK14-1 | player_assists |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINJERIKSSONEK14-2 | player_assists |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINJSPURGEON46-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINJSPURGEON46-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINKKAPRIZOV97-1 | player_assists |  | 0.520 |  | 53 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINKKAPRIZOV97-2 | player_assists |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINKKAPRIZOV97-3 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINMBOLDY12-1 | player_assists |  | 0.510 |  | 52 | 50 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINMBOLDY12-2 | player_assists |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINOMAATTA3-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINQHUGHES43-1 | player_assists |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINQHUGHES43-2 | player_assists |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINQHUGHES43-3 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-MINYTRENIN13-1 | player_assists |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANBBOESER6-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANBBOESER6-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANBGALLAGHER7-1 | player_assists |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANDOCONNOR18-1 | player_assists |  | 0.200 |  | 22 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANFCHYTIL77-1 | player_assists |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANFCHYTIL77-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANFHRONEK17-1 | player_assists |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANFHRONEK17-2 | player_assists |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANJDEBRUSK74-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANJLEKKERIMKI88-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANLOHGREN92-1 | player_assists |  | 0.185 |  | 21 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT25MINVAN-VANMROSSI23-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Matt Boldy: 1+ goals NO @ 57c · p 0.6593 (adj 0.6357) · $15.0 · thesis MIN:SUPPRESSED
- Kirill Kaprizov: 2+ goals NO @ 86c · p 0.9148 (adj 0.8998) · $15.0 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 58c · p 0.7313 (adj 0.6297) · $15.38 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.268 | 0.415 | 43/60 | +0.115 | STANDARD |
| Quinn Hughes: 2+ points | 0.221 | 0.360 | 37/65 | +0.113 | STANDARD |
| Matt Boldy: 2+ points | 0.241 | 0.375 | 38/63 | +0.113 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.650 | 66/36 | +0.105 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.628 | 0.755 | 78/27 | +0.089 | STANDARD |
| Quinn Hughes: 1+ points | 0.585 | 0.710 | 72/30 | +0.100 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
