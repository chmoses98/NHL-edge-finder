# NHL slate 2026-10-12 — RESEARCH_ONLY

generated 2026-10-12T17:17:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 3150 · contracts joined: 447 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 397, 'NO_EDGE': 36, 'OK': 14}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 60, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 127, 'game_overtime': 2, 'player_points': 83, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ NJD | 2026-10-12T23:00:00Z | T-3h | 0.526 | 0.474 | 0.175 | 6.11 | 3.14 | 2.97 | 224 (25/199) | CONFIRMED/CONFIRMED |
| VGK @ MIN | 2026-10-13T00:00:00Z | T-6h | 0.543 | 0.457 | 0.181 | 6.06 | 3.16 | 2.90 | 223 (25/198) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT12VGKMIN-MIN | game_winner | 0.543 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK2 | game_spread | 0.246 | 0.285 | 0.277 | 29 | 72 | no | +0.020 | OK |
| KXNHLGAME-26OCT12VGKMIN-VGK | game_winner | 0.457 | 0.495 | 0.487 | 50 | 51 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK3 | game_spread | 0.145 | 0.175 | 0.169 | 18 | 83 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-MIN2 | game_spread | 0.319 | 0.285 | 0.292 | 29 | 72 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 | team_total | 0.342 | 0.375 | 0.368 | 38 | 63 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK3 | team_total | 0.562 | 0.595 | 0.588 | 60 | 41 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK2 | team_total | 0.778 | 0.805 | 0.800 | 81 | 20 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK5 | team_total | 0.173 | 0.200 | 0.194 | 21 | 81 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN3 | team_total | 0.621 | 0.595 | 0.600 | 60 | 41 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN5 | team_total | 0.215 | 0.195 | 0.199 | 20 | 81 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK6 | team_total | 0.072 | 0.090 | 0.086 | 10 | 92 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT12VGKMIN-5 | game_total | 0.755 | 0.775 | 0.771 | 78 | 23 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ6 | team_total | 0.096 | 0.085 | 0.087 | 9 | 92 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT12VGKMIN-4 | game_total | 0.843 | 0.860 | 0.857 | 87 | 15 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN4 | team_total | 0.403 | 0.380 | 0.385 | 39 | 63 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-10 | game_total | 0.080 | 0.070 | 0.072 | 8 | 94 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ3 | game_spread | 0.184 | 0.200 | 0.197 | 21 | 81 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-6 | game_total | 0.538 | 0.555 | 0.552 | 56 | 45 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-4 | game_total | 0.847 | 0.855 | 0.853 | 86 | 15 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT6 | team_total | 0.079 | 0.070 | 0.072 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT12VGKMIN-MIN3 | game_spread | 0.194 | 0.185 | 0.187 | 19 | 82 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-9 | game_total | 0.168 | 0.175 | 0.174 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ2 | game_spread | 0.303 | 0.315 | 0.313 | 32 | 69 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN6 | team_total | 0.098 | 0.085 | 0.087 | 10 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-8 | game_total | 0.245 | 0.235 | 0.237 | 24 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ5 | team_total | 0.213 | 0.205 | 0.207 | 21 | 80 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-9 | game_total | 0.171 | 0.160 | 0.162 | 17 | 85 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-10 | game_total | 0.074 | 0.075 | 0.075 | 8 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ4 | team_total | 0.397 | 0.385 | 0.387 | 39 | 62 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT3 | game_spread | 0.151 | 0.155 | 0.154 | 16 | 85 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-8 | game_total | 0.237 | 0.245 | 0.243 | 25 | 76 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3 | team_total | 0.615 | 0.605 | 0.607 | 61 | 40 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT2 | game_spread | 0.261 | 0.255 | 0.256 | 26 | 75 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-7 | game_total | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN2 | team_total | 0.817 | 0.810 | 0.811 | 82 | 20 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-5 | game_total | 0.761 | 0.765 | 0.764 | 77 | 24 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT5 | team_total | 0.184 | 0.180 | 0.181 | 19 | 83 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT2 | team_total | 0.792 | 0.790 | 0.790 | 80 | 22 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-6 | game_total | 0.546 | 0.545 | 0.545 | 55 | 46 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-NJ | game_winner | 0.526 | 0.525 | 0.525 | 53 | 48 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-OTT | game_winner | 0.474 | 0.475 | 0.475 | 48 | 53 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT3 | team_total | 0.575 | 0.575 | 0.575 | 58 | 43 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ2 | team_total | 0.812 | 0.815 | 0.814 | 83 | 20 |  | -0.023 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-7 | game_total | 0.434 | 0.430 | 0.431 | 44 | 58 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT4 | team_total | 0.358 | 0.360 | 0.360 | 37 | 65 |  | -0.024 | NO_EDGE |
| KXNHL1P-26OCT12OTTNJ-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12OTTNJ-OTT | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12OTTNJ-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12OTTNJ-NJ2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12OTTNJ-OTT2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT12OTTNJ-1 | period_total |  | 0.815 |  | 82 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT12OTTNJ-2 | period_total |  | 0.515 |  | 52 | 49 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT12OTTNJ-3 | period_total |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT12OTTNJ-NJ | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT12OTTNJ-OTT | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT12OTTNJ-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT12OTTNJ-NJ2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT12OTTNJ-OTT2 | period_spread |  | 0.115 |  | 12 | 89 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT12OTTNJ-1 | period_total |  | 0.885 |  | 90 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT12OTTNJ-2 | period_total |  | 0.590 |  | 60 | 42 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT12OTTNJ-3 | period_total |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT12OTTNJ-NJ | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT12OTTNJ-OTT | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT12OTTNJ-TIE | period_winner |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT12OTTNJ-NJ2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT12OTTNJ-OTT2 | period_spread |  | 0.150 |  | 16 | 86 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT12OTTNJ-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT12OTTNJ-2 | period_total |  | 0.635 |  | 65 | 38 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT12OTTNJ-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12OTTNJ-NJAMANTHA39-1 | player_assists |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12OTTNJ-NJDHAMILTON7-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12OTTNJ-NJDHAMILTON7-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12OTTNJ-NJERODRIGUES17-1 | player_assists |  | 0.140 |  | 26 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12OTTNJ-NJJBRATT63-1 | player_assists |  | 0.450 |  | 46 | 56 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT12OTTNJ-NJJBRATT63-2 | player_assists |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| OTT @ NJD | 0.526 | 0.477 | 0.175 | 0.228 | 6.11 | 5.86 | 0.996/0.968 | KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ4 -0.064 |
| VGK @ MIN | 0.543 | 0.532 | 0.181 | 0.218 | 6.06 | 6.16 | 0.991/1.003 | KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 +0.022 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Jack Hughes: 1+ goals NO @ 64c · p 0.7127 (adj 0.6933) · $19.67 · thesis NJD:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1715 (adj 0.1599) · $5.82 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 72c · p 0.8634 (adj 0.7604) · $19.67 · thesis OTT:SUPPRESSED
- Cody Glass: 1+ goals YES @ 11c · p 0.1496 (adj 0.136) · $4.85 · thesis NJD:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0742 (adj 0.0707) · $4.44 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 53c · p 0.6065 (adj 0.5657) · $11.15 · thesis VGK:SUPPRESSED
- Michael McCarron: 1+ goals YES @ 9c · p 0.113 (adj 0.106) · $2.76 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ assists NO @ 53c · p 0.6026 (adj 0.5638) · $9.7 · thesis MIN:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**OTT @ NJD** · priced 171/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (CONFIRMED) exp shots 27.04, exp saves 23.31 (sd 6.49), pull risk 0.057
- OTT net: Linus Ullmark (CONFIRMED) exp shots 28.15, exp saves 24.53 (sd 6.56), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nico Daws: 23+ saves | 0.544 | 0.305 | 56/95 | -0.033 |  |
| Linus Ullmark: 26+ saves | 0.431 | 0.260 | 47/95 | -0.056 |  |
| Andre Burakovsky: 1+ points | 0.266 | 0.425 | 44/59 | +0.127 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.137 | 0.295 | 31/72 | +0.129 | STANDARD |
| Jack Hughes: 1+ assists | 0.363 | 0.520 | 53/49 | +0.129 | STANDARD |
| Jack Hughes: 2+ points | 0.189 | 0.335 | 35/68 | +0.115 | STANDARD |

**VGK @ MIN** · priced 170/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.04, exp saves 25.33 (sd 6.81), pull risk 0.054
- VGK net: Carter Hart (PROJECTED) exp shots 27.87, exp saves 24.03 (sd 6.63), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jesper Wallstedt: 27+ saves | 0.424 | 0.280 | 50/94 | -0.094 |  |
| Jack Eichel: 1+ assists | 0.416 | 0.545 | 55/46 | +0.107 | STANDARD |
| Jack Eichel: 1+ points | 0.580 | 0.685 | 69/32 | +0.085 | STANDARD |
| Trevor Connelly: 1+ assists | 0.177 | 0.280 | 30/74 | +0.069 | PRIOR_HEAVY |
| Jack Eichel: 2+ points | 0.216 | 0.315 | 32/69 | +0.079 | STANDARD |
| Trevor Connelly: 1+ points | 0.325 | 0.415 | 43/60 | +0.059 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
