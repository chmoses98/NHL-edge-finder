# NHL slate 2026-11-13 — RESEARCH_ONLY

generated 2026-11-14T02:17:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 1 · markets on board: 2789 · contracts joined: 226 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 201, 'NO_EDGE': 17, 'OK': 8}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 31, 'game_early_goal': 1, 'first_goal': 37, 'game_winner': 2, 'player_goals': 63, 'game_overtime': 1, 'player_points': 42, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ VGK | 2026-11-14T03:00:00Z | T-30m | 0.597 | 0.403 | 0.169 | 6.39 | 3.51 | 2.88 | 226 (25/201) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV13NSHVGK-10 | game_total | 0.100 | 0.065 | 0.071 | 7 | 94 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-9 | game_total | 0.204 | 0.165 | 0.172 | 17 | 84 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-8 | game_total | 0.285 | 0.245 | 0.253 | 25 | 76 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK6 | team_total | 0.138 | 0.110 | 0.115 | 12 | 90 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-7 | game_total | 0.477 | 0.445 | 0.451 | 45 | 56 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH3 | team_total | 0.553 | 0.525 | 0.531 | 53 | 48 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV13NSHVGK-6 | game_total | 0.593 | 0.565 | 0.571 | 57 | 44 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV13NSHVGK-VGK3 | game_spread | 0.244 | 0.265 | 0.261 | 27 | 74 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK5 | team_total | 0.283 | 0.260 | 0.265 | 27 | 75 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH5 | team_total | 0.168 | 0.145 | 0.149 | 16 | 87 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH6 | team_total | 0.073 | 0.065 | 0.067 | 7 | 94 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-4 | game_total | 0.874 | 0.865 | 0.867 | 87 | 14 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-NSH3 | game_spread | 0.117 | 0.125 | 0.123 | 13 | 88 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV13NSHVGK-5 | game_total | 0.795 | 0.785 | 0.787 | 79 | 22 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK3 | team_total | 0.688 | 0.670 | 0.674 | 68 | 34 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK4 | team_total | 0.480 | 0.465 | 0.468 | 47 | 54 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH2 | team_total | 0.774 | 0.760 | 0.763 | 77 | 25 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-VGK2 | team_total | 0.860 | 0.870 | 0.868 | 88 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV13NSHVGK-NSH4 | team_total | 0.337 | 0.320 | 0.323 | 33 | 69 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26NOV13NSHVGK-VGK | game_winner | 0.597 | 0.585 | 0.587 | 59 | 42 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-NSH2 | game_spread | 0.209 | 0.205 | 0.206 | 21 | 80 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV13NSHVGK-VGK2 | game_spread | 0.378 | 0.375 | 0.376 | 38 | 63 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26NOV13NSHVGK-NSH | game_winner | 0.403 | 0.405 | 0.405 | 41 | 60 |  | -0.020 | NO_EDGE |
| KXNHL1P-26NOV13NSHVGK-NSH | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV13NSHVGK-TIE | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV13NSHVGK-VGK | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV13NSHVGK-NSH2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV13NSHVGK-VGK2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV13NSHVGK-1 | period_total |  | 0.845 |  | 85 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV13NSHVGK-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV13NSHVGK-3 | period_total |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV13NSHVGK-NSH | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV13NSHVGK-TIE | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV13NSHVGK-VGK | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV13NSHVGK-NSH2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV13NSHVGK-VGK2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV13NSHVGK-1 | period_total |  | 0.900 |  | 92 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV13NSHVGK-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV13NSHVGK-3 | period_total |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV13NSHVGK-NSH | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV13NSHVGK-TIE | period_winner |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV13NSHVGK-VGK | period_winner |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV13NSHVGK-NSH2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV13NSHVGK-VGK2 | period_spread |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV13NSHVGK-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV13NSHVGK-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV13NSHVGK-3 | period_total |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHFFORSBERG9-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHFFORSBERG9-2 | player_assists |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHMBOURQUE22-2 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHNHOGLANDER21-1 | player_assists |  | 0.210 |  | 22 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHRJOSI59-1 | player_assists |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHRJOSI59-2 | player_assists |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHRJOSI59-3 | player_assists |  | 0.035 |  | 6 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHROREILLY90-1 | player_assists |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHROREILLY90-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHSSTAMKOS91-1 | player_assists |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHSSTAMKOS91-2 | player_assists |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-NSHSWRIGHT51-1 | player_assists |  | 0.175 |  | 18 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKBHOWDEN21-1 | player_assists |  | 0.175 |  | 18 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKJEICHEL9-1 | player_assists |  | 0.565 |  | 58 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKJEICHEL9-2 | player_assists |  | 0.200 |  | 21 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKJEICHEL9-3 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKMMARNER93-1 | player_assists |  | 0.530 |  | 54 | 48 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKMMARNER93-2 | player_assists |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKMMARNER93-3 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKMSTONE61-1 | player_assists |  | 0.445 |  | 46 | 57 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKMSTONE61-2 | player_assists |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKSTHEODORE27-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKSTHEODORE27-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKTCONNELLY24-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKTHERTL48-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKTHERTL48-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKVOLOFSSON95-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV13NSHVGK-VGKWKARLSSON71-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ VGK | 0.597 | 0.617 | 0.169 | 0.206 | 6.39 | 6.35 | 1.003/1.000 | KXNHLSPREAD-26NOV13NSHVGK-VGK3 +0.024 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Braeden Bowman: 1+ goals YES @ 13c · p 0.1735 (adj 0.1614) · $6.31 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ goals YES @ 21c · p 0.2554 (adj 0.2428) · $6.64 · thesis VGK:OFFENSE_4PLUS
- Victor Olofsson: 1+ goals NO @ 74c · p 0.7803 (adj 0.769) · $15.99 · thesis VGK:SUPPRESSED
- Brett Howden: 1+ goals YES @ 19c · p 0.2237 (adj 0.214) · $3.99 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ VGK** · priced 174/175 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VGK net: Carter Hart (PROJECTED) exp shots 25.55, exp saves 22.46 (sd 6.11), pull risk 0.048
- NSH net: Juuse Saros (PROJECTED) exp shots 29.76, exp saves 25.38 (sd 7.02), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivan Barbashev: 1+ points | 0.539 | 0.440 | 45/57 | +0.072 | STANDARD |
| Jack Eichel: 2+ points | 0.262 | 0.360 | 37/65 | +0.072 | STANDARD |
| Ivan Barbashev: 1+ assists | 0.386 | 0.290 | 30/72 | +0.071 | STANDARD |
| Jack Eichel: 1+ assists | 0.474 | 0.565 | 58/45 | +0.058 | STANDARD |
| Victor Olofsson: 1+ assists | 0.232 | 0.320 | 33/69 | +0.063 | STANDARD |
| Victor Olofsson: 1+ points | 0.400 | 0.480 | 49/53 | +0.052 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
