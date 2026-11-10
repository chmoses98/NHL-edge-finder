# NHL slate 2026-11-09 — RESEARCH_ONLY

generated 2026-11-10T02:43:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 1 · markets on board: 2698 · contracts joined: 243 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 218, 'NO_EDGE': 16, 'OK': 9}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 44, 'game_early_goal': 1, 'first_goal': 33, 'game_winner': 2, 'player_goals': 57, 'game_overtime': 1, 'player_points': 56, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ SJS | 2026-11-10T03:00:00Z | T-10m | 0.420 | 0.580 | 0.176 | 6.16 | 2.83 | 3.33 | 243 (25/218) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV09NYISJ-5 | game_total | 0.765 | 0.805 | 0.797 | 81 | 20 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV09NYISJ-6 | game_total | 0.553 | 0.595 | 0.587 | 60 | 41 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV09NYISJ-SJ3 | game_spread | 0.123 | 0.155 | 0.148 | 16 | 85 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ2 | team_total | 0.766 | 0.800 | 0.793 | 81 | 21 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV09NYISJ-4 | game_total | 0.850 | 0.875 | 0.870 | 88 | 13 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV09NYISJ-7 | game_total | 0.443 | 0.475 | 0.469 | 48 | 53 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ4 | team_total | 0.325 | 0.360 | 0.353 | 37 | 65 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ3 | team_total | 0.544 | 0.575 | 0.569 | 58 | 43 | no | +0.009 | OK |
| KXNHLSPREAD-26NOV09NYISJ-SJ2 | game_spread | 0.218 | 0.235 | 0.231 | 24 | 77 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ5 | team_total | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI4 | team_total | 0.437 | 0.460 | 0.455 | 47 | 55 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-2 | game_total | 0.985 | 0.980 | 0.981 |  | 2 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-NYI | game_winner | 0.580 | 0.565 | 0.568 | 57 | 44 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-3 | game_total | 0.965 | 0.965 | 0.965 | 97 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-8 | game_total | 0.254 | 0.265 | 0.263 | 27 | 74 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-9 | game_total | 0.178 | 0.190 | 0.187 | 20 | 82 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-10 | game_total | 0.083 | 0.085 | 0.085 | 9 | 92 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI6 | team_total | 0.119 | 0.110 | 0.112 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ6 | team_total | 0.065 | 0.065 | 0.065 | 7 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI3 | team_total | 0.654 | 0.670 | 0.667 | 68 | 34 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI2 | team_total | 0.842 | 0.855 | 0.852 | 87 | 16 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI3 | game_spread | 0.221 | 0.230 | 0.228 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI2 | game_spread | 0.352 | 0.345 | 0.346 | 35 | 66 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI5 | team_total | 0.247 | 0.245 | 0.245 | 25 | 76 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-SJ | game_winner | 0.420 | 0.425 | 0.424 | 43 | 58 |  | -0.017 | NO_EDGE |
| KXNHL1P-26NOV09NYISJ-NYI | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09NYISJ-SJ | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09NYISJ-TIE | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09NYISJ-NYI2 | period_spread |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09NYISJ-SJ2 | period_spread |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09NYISJ-1 | period_total |  | 0.845 |  | 86 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09NYISJ-2 | period_total |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09NYISJ-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09NYISJ-NYI | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09NYISJ-SJ | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09NYISJ-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV09NYISJ-NYI2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV09NYISJ-SJ2 | period_spread |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09NYISJ-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09NYISJ-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09NYISJ-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09NYISJ-NYI | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09NYISJ-SJ | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09NYISJ-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV09NYISJ-NYI2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV09NYISJ-SJ2 | period_spread |  | 0.130 |  | 14 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09NYISJ-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09NYISJ-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09NYISJ-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIADUCLAIR11-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIAPELECH3-1 | player_assists |  | 0.190 |  | 20 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIBHORVAT14-1 | player_assists |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIBHORVAT14-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIBSCHENN10-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIBSCHENN10-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIJPAGEAU44-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIJPAGEAU44-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIKPALMIERI21-1 | player_assists |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIKPALMIERI21-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYILSTANLEY8-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIMSCHAEFER48-1 | player_assists |  | 0.520 |  | 53 | 49 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIMSCHAEFER48-2 | player_assists |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIOPALAT81-1 | player_assists |  | 0.195 |  | 20 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYISHOLMSTROM92-1 | player_assists |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYISHOLMSTROM92-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYITDEANGELO77-1 | player_assists |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYITDEANGELO77-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIVEKLUND73-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-NYIVEKLUND73-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJAWENNBERG21-1 | player_assists |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJAWENNBERG21-2 | player_assists |  |  |  | 9 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJCGRAF51-1 | player_assists |  | 0.180 |  | 19 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJDNURSE25-1 | player_assists |  | 0.200 |  | 21 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJDORLOV9-1 | player_assists |  | 0.270 |  | 29 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJDORLOV9-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJISTENBERG41-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJJTROUBA65-1 | player_assists |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJKSHERWOOD44-1 | player_assists |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09NYISJ-SJMCELEBRINI71-1 | player_assists |  | 0.545 |  | 55 | 46 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ SJS | 0.420 | 0.502 | 0.176 | 0.216 | 6.16 | 6.31 | 1.039/0.947 | KXNHLGAME-26NOV09NYISJ-SJ +0.082 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Ivar Stenberg: 1+ assists NO @ 70c · p 0.7778 (adj 0.7364) · $20.0 · thesis SJS:SUPPRESSED
- Michael Misa: 1+ goals YES @ 19c · p 0.2292 (adj 0.2181) · $5.54 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 18c · p 0.2156 (adj 0.2055) · $4.9 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 21c · p 0.2481 (adj 0.2373) · $5.52 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYI @ SJS** · priced 189/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.92, exp saves 24.2 (sd 6.59), pull risk 0.063
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.14, exp saves 23.54 (sd 6.54), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.282 | 0.180 | 20/84 | +0.071 | STANDARD |
| Ivar Stenberg: 1+ points | 0.373 | 0.470 | 48/54 | +0.070 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.448 | 0.545 | 55/46 | +0.074 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.222 | 0.305 | 31/70 | +0.063 | STANDARD |
| Macklin Celebrini: 2+ points | 0.284 | 0.360 | 38/66 | +0.041 | STANDARD |
| Matthew Schaefer: 1+ points | 0.567 | 0.640 | 65/37 | +0.047 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
