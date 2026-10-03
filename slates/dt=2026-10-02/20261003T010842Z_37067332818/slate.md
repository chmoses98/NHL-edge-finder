# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-03T01:08:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 1 · markets on board: 3309 · contracts joined: 183 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 158, 'OK': 19, 'NO_EDGE': 6}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 27, 'game_early_goal': 1, 'first_goal': 34, 'game_winner': 2, 'player_goals': 34, 'game_overtime': 1, 'player_points': 35, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ VGK | 2026-10-03T02:00:00Z | T-30m | 0.589 | 0.411 | 0.169 | 6.46 | 3.52 | 2.94 | 183 (25/158) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.483 | 0.575 | 0.557 | 58 | 43 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.689 | 0.755 | 0.743 | 76 | 25 | no | +0.048 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.411 | 0.345 | 0.358 | 35 | 66 | yes | +0.045 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.589 | 0.655 | 0.642 | 66 | 35 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.242 | 0.305 | 0.292 | 31 | 70 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.372 | 0.435 | 0.422 | 44 | 57 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.289 | 0.345 | 0.333 | 35 | 66 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.863 | 0.895 | 0.889 | 90 | 11 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.606 | 0.645 | 0.637 | 65 | 36 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.143 | 0.180 | 0.172 | 19 | 83 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.876 | 0.905 | 0.900 | 91 | 10 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.217 | 0.185 | 0.191 | 19 | 82 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-3 | game_total | 0.971 | 0.985 | 0.983 | 99 | 2 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.298 | 0.325 | 0.320 | 33 | 68 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.123 | 0.105 | 0.108 | 11 | 90 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA4 | team_total | 0.349 | 0.325 | 0.330 | 33 | 68 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA5 | team_total | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-10 | game_total | 0.103 | 0.115 | 0.113 | 12 | 89 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.213 | 0.225 | 0.223 | 23 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA6 | team_total | 0.080 | 0.070 | 0.072 | 8 | 94 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA2 | team_total | 0.782 | 0.775 | 0.776 | 78 | 23 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA3 | team_total | 0.565 | 0.555 | 0.557 | 56 | 45 |  | -0.013 | NO_EDGE |
| KXNHL1P-26OCT02ANAVGK-ANA | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT02ANAVGK-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT02ANAVGK-VGK | period_winner |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT02ANAVGK-ANA2 | period_spread |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT02ANAVGK-VGK2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT02ANAVGK-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT02ANAVGK-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT02ANAVGK-3 | period_total |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT02ANAVGK-ANA | period_winner |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT02ANAVGK-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT02ANAVGK-VGK | period_winner |  | 0.430 |  | 45 | 59 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT02ANAVGK-ANA2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT02ANAVGK-VGK2 | period_spread |  | 0.185 |  | 21 | 84 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT02ANAVGK-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT02ANAVGK-2 | period_total |  | 0.650 |  | 67 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT02ANAVGK-3 | period_total |  | 0.365 |  | 39 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT02ANAVGK-ANA | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT02ANAVGK-TIE | period_winner |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT02ANAVGK-VGK | period_winner |  | 0.450 |  | 47 | 57 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT02ANAVGK-ANA2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT02ANAVGK-VGK2 | period_spread |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT02ANAVGK-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT02ANAVGK-2 | period_total |  | 0.690 |  | 70 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT02ANAVGK-3 | period_total |  | 0.420 |  | 44 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1 | player_assists |  | 0.220 |  | 23 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANABSENNECKE45-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANABSENNECKE45-2 | player_assists |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANACGAUTHIER61-1 | player_assists |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANACGAUTHIER61-2 | player_assists |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANAJLACOMBE2-1 | player_assists |  | 0.425 |  | 43 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANAJLACOMBE2-2 | player_assists |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1 | player_assists |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANAMGRANLUND64-1 | player_assists |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-ANAMGRANLUND64-2 | player_assists |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKIBARBASHEV49-1 | player_assists |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKIBARBASHEV49-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKJEICHEL9-1 | player_assists |  | 0.560 |  | 57 | 45 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKJEICHEL9-2 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKJEICHEL9-3 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKMMARNER93-1 | player_assists |  | 0.525 |  | 53 | 48 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKMMARNER93-2 | player_assists |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKMSTONE61-1 | player_assists |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKMSTONE61-2 | player_assists |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1 | player_assists |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-2 | player_assists |  | 0.060 |  | 7 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKSTHEODORE27-1 | player_assists |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKSTHEODORE27-2 | player_assists |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKTHERTL48-1 | player_assists |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKTHERTL48-2 | player_assists |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02ANAVGK-VGKWKARLSSON71-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLF10G-26OCT02ANAVGK-Y | game_early_goal |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT02ANAVGK-ANAAGREER18 | first_goal |  | 0.040 |  | 4 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT02ANAVGK-ANAAKILLORN17 | first_goal |  | 0.030 |  | 4 |  |  |  | UNSUPPORTED |
| KXNHLFIRSTGOAL-26OCT02ANAVGK-ANABSENNECKE45 | first_goal |  | 0.060 |  | 5 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ VGK | 0.589 | 0.597 | 0.169 | 0.212 | 6.46 | 6.41 | 1.003/1.015 | KXNHLTOTAL-26OCT02ANAVGK-6 -0.016 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Tim Washe: 1+ goals YES @ 7c · p 0.1141 (adj 0.1018) · $6.2 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2329 (adj 0.2184) · $8.04 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 23c · p 0.3635 (adj 0.2702) · $6.77 · thesis ANA:OFFENSE_4PLUS
- Braeden Bowman: 1+ goals YES @ 15c · p 0.1953 (adj 0.1827) · $6.64 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ VGK** · priced 130/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 28.77, exp saves 25.15 (sd 6.74), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.58, exp saves 23.43 (sd 6.66), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Hart: 24+ saves | 0.596 | 0.425 | 51/66 | +0.068 |  |
| Alex Killorn: 1+ points | 0.510 | 0.365 | 38/65 | +0.113 | STANDARD |
| Alex Killorn: 1+ assists | 0.363 | 0.220 | 23/79 | +0.121 | STANDARD |
| Lukas Dostal: 28+ saves | 0.262 | 0.375 | 47/72 | +0.004 |  |
| Leo Carlsson: 1+ assists | 0.293 | 0.405 | 41/60 | +0.090 | STANDARD |
| Jack Eichel: 1+ assists | 0.460 | 0.560 | 57/45 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
