# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-02T05:14:48Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2164 · contracts joined: 204 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 104, 'OK': 57, 'NO_EDGE': 43}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'game_early_goal': 4, 'game_winner': 8, 'game_overtime': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 2026-11-03T00:00:00Z | T-12h | 0.566 | 0.434 | 0.173 | 6.23 | 3.32 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ FLA | 2026-11-03T00:00:00Z | T-12h | 0.548 | 0.452 | 0.174 | 6.12 | 3.21 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| COL @ CHI | 2026-11-03T01:00:00Z | T-12h | 0.371 | 0.629 | 0.171 | 6.15 | 2.67 | 3.49 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-12h | 0.533 | 0.467 | 0.174 | 6.54 | 3.38 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV02VGKBOS-BOS2 | game_spread | 0.343 | 0.275 | 0.288 | 28 | 73 | yes | +0.049 | OK |
| KXNHLGAME-26NOV02VGKBOS-BOS | game_winner | 0.566 | 0.495 | 0.509 | 50 | 51 | yes | +0.048 | OK |
| KXNHLGAME-26NOV02VGKBOS-VGK | game_winner | 0.434 | 0.505 | 0.491 | 51 | 50 | no | +0.048 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA3 | game_spread | 0.201 | 0.265 | 0.251 | 27 | 74 | no | +0.045 | OK |
| KXNHLGAME-26NOV02DETFLA-DET | game_winner | 0.452 | 0.385 | 0.398 | 39 | 62 | yes | +0.045 | OK |
| KXNHLGAME-26NOV02DETFLA-FLA | game_winner | 0.548 | 0.615 | 0.602 | 62 | 39 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.472 | 0.545 | 0.530 | 56 | 47 | no | +0.041 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK3 | game_spread | 0.130 | 0.190 | 0.176 | 20 | 82 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.403 | 0.465 | 0.452 | 47 | 54 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA2 | game_spread | 0.325 | 0.385 | 0.373 | 39 | 62 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET4 | team_total | 0.342 | 0.280 | 0.292 | 29 | 73 | yes | +0.037 | OK |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.629 | 0.685 | 0.674 | 69 | 32 | no | +0.035 | OK |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.371 | 0.315 | 0.326 | 32 | 69 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 | team_total | 0.341 | 0.405 | 0.392 | 42 | 61 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.264 | 0.320 | 0.308 | 33 | 69 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET2 | game_spread | 0.242 | 0.190 | 0.200 | 20 | 82 | yes | +0.031 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK2 | game_spread | 0.235 | 0.285 | 0.275 | 29 | 72 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.689 | 0.740 | 0.730 | 75 | 27 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 | team_total | 0.556 | 0.615 | 0.603 | 63 | 40 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET5 | team_total | 0.175 | 0.130 | 0.138 | 14 | 88 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET3 | team_total | 0.560 | 0.500 | 0.512 | 52 | 52 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK2 | team_total | 0.778 | 0.825 | 0.816 | 84 | 19 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.274 | 0.325 | 0.314 | 34 | 69 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK5 | team_total | 0.177 | 0.220 | 0.211 | 23 | 79 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET6 | team_total | 0.072 | 0.040 | 0.045 | 5 | 97 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA3 | team_total | 0.628 | 0.670 | 0.662 | 68 | 34 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS3 | game_spread | 0.216 | 0.180 | 0.187 | 19 | 83 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.226 | 0.195 | 0.201 | 20 | 81 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.308 | 0.275 | 0.281 | 28 | 73 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.440 | 0.475 | 0.468 | 48 | 53 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET3 | game_spread | 0.139 | 0.115 | 0.120 | 12 | 89 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.862 | 0.885 | 0.881 | 89 | 12 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.852 | 0.880 | 0.875 | 89 | 13 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 | team_total | 0.413 | 0.455 | 0.446 | 47 | 56 | no | +0.010 | OK |
| KXNHLGAME-26NOV02CGYSJ-CGY | game_winner | 0.467 | 0.435 | 0.441 | 44 | 57 | yes | +0.010 | OK |
| KXNHLGAME-26NOV02CGYSJ-SJ | game_winner | 0.533 | 0.565 | 0.559 | 57 | 44 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.554 | 0.590 | 0.583 | 60 | 42 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.133 | 0.155 | 0.150 | 16 | 85 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.103 | 0.075 | 0.080 | 9 | 94 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET2 | team_total | 0.780 | 0.745 | 0.752 | 76 | 27 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3 | team_total | 0.653 | 0.610 | 0.619 | 63 | 41 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS4 | team_total | 0.443 | 0.400 | 0.408 | 42 | 62 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS6 | team_total | 0.111 | 0.090 | 0.094 | 10 | 92 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.763 | 0.785 | 0.781 | 79 | 22 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.502 | 0.475 | 0.480 | 48 | 53 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA2 | team_total | 0.827 | 0.845 | 0.841 | 85 | 16 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-4 | game_total | 0.858 | 0.875 | 0.872 | 88 | 13 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.057 | 0.040 | 0.043 | 5 | 97 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS5 | team_total | 0.245 | 0.215 | 0.221 | 23 | 80 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI2 | game_spread | 0.183 | 0.160 | 0.164 | 17 | 85 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY4 | team_total | 0.399 | 0.365 | 0.372 | 38 | 65 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.254 | 0.275 | 0.271 | 28 | 73 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA5 | team_total | 0.225 | 0.250 | 0.245 | 26 | 76 | no | +0.002 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI3 | game_spread | 0.097 | 0.085 | 0.087 | 9 | 92 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.223 | 0.195 | 0.200 | 21 | 82 | yes | +0.001 | OK |
| KXNHLSPREAD-26NOV02CGYSJ-SJ3 | game_spread | 0.198 | 0.220 | 0.215 | 23 | 79 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS2 | team_total | 0.840 | 0.820 | 0.824 | 83 | 19 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-5 | game_total | 0.811 | 0.795 | 0.798 | 80 | 21 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY2 | game_spread | 0.262 | 0.240 | 0.244 | 25 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK6 | team_total | 0.077 | 0.090 | 0.087 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY3 | team_total | 0.614 | 0.590 | 0.595 | 60 | 42 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-SJ2 | game_spread | 0.318 | 0.335 | 0.331 | 34 | 67 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.613 | 0.590 | 0.595 | 60 | 42 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI4 | team_total | 0.290 | 0.270 | 0.274 | 28 | 74 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-5 | game_total | 0.772 | 0.785 | 0.782 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.962 | 0.975 | 0.973 | 99 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-8 | game_total | 0.248 | 0.235 | 0.238 | 24 | 77 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.122 | 0.115 | 0.116 | 12 | 89 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.111 | 0.100 | 0.102 | 11 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-9 | game_total | 0.173 | 0.160 | 0.163 | 17 | 85 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-3 | game_total | 0.964 | 0.970 | 0.969 | 98 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.177 | 0.190 | 0.187 | 20 | 82 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-10 | game_total | 0.082 | 0.095 | 0.092 | 11 | 92 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5 | team_total | 0.141 | 0.125 | 0.128 | 14 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-5 | game_total | 0.763 | 0.755 | 0.757 | 76 | 25 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-8 | game_total | 0.264 | 0.255 | 0.257 | 26 | 75 |  | -0.009 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 0.566 | 0.515 | 0.173 | 0.219 | 6.23 | 6.46 | 0.969/1.004 | KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 +0.070 |
| DET @ FLA | 0.548 | 0.563 | 0.174 | 0.217 | 6.12 | 6.33 | 0.999/1.016 | KXNHLTOTAL-26NOV02DETFLA-7 +0.040 |
| COL @ CHI | 0.371 | 0.352 | 0.171 | 0.199 | 6.15 | 6.52 | 1.004/0.977 | KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 +0.063 |
| CGY @ SJS | 0.533 | 0.559 | 0.174 | 0.213 | 6.54 | 6.41 | 1.035/0.998 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 -0.028 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 2 recommended · full analysis in card.md / packet.json `thesis_card`

- Detroit over 4.5 goals scored YES @ 14c · p 0.1897 (adj 0.1598) · $2.0 · thesis DET:OFFENSE_4PLUS
- Detroit over 3.5 goals scored YES @ 29c · p 0.355 (adj 0.3175) · $2.29 · thesis DET:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BOS** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.5, exp saves 24.63 (sd 6.71), pull risk 0.066
- VGK net: Carter Hart (PROJECTED) exp shots 26.12, exp saves 22.48 (sd 6.36), pull risk 0.069

**DET @ FLA** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- FLA net: Akira Schmid (PROJECTED) exp shots 26.78, exp saves 23.25 (sd 6.32), pull risk 0.057
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.16, exp saves 23.24 (sd 6.44), pull risk 0.069

**COL @ CHI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CHI net: Spencer Knight (PROJECTED) exp shots 31.92, exp saves 26.86 (sd 7.51), pull risk 0.091
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.7, exp saves 21.75 (sd 6.0), pull risk 0.05

**CGY @ SJS** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.38, exp saves 24.69 (sd 6.68), pull risk 0.055
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.99, exp saves 24.81 (sd 6.93), pull risk 0.072

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
