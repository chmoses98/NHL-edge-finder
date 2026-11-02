# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-02T15:08:07Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2825 · contracts joined: 865 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 765, 'OK': 59, 'NO_EDGE': 41}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 118, 'game_early_goal': 4, 'first_goal': 146, 'game_winner': 8, 'player_goals': 241, 'game_overtime': 4, 'player_points': 156, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 2026-11-03T00:00:00Z | T-6h | 0.564 | 0.436 | 0.176 | 6.24 | 3.32 | 2.91 | 218 (25/193) | PROJECTED/PROJECTED |
| DET @ FLA | 2026-11-03T00:00:00Z | T-6h | 0.549 | 0.451 | 0.175 | 6.13 | 3.22 | 2.91 | 216 (25/191) | PROJECTED/PROJECTED |
| COL @ CHI | 2026-11-03T01:00:00Z | T-6h | 0.373 | 0.627 | 0.173 | 6.17 | 2.67 | 3.49 | 216 (25/191) | PROJECTED/PROJECTED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-6h | 0.532 | 0.468 | 0.169 | 6.54 | 3.38 | 3.17 | 215 (25/190) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.474 | 0.565 | 0.547 | 57 | 44 | no | +0.068 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA3 | game_spread | 0.195 | 0.275 | 0.258 | 28 | 73 | no | +0.061 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS2 | game_spread | 0.346 | 0.275 | 0.289 | 28 | 73 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 | team_total | 0.343 | 0.415 | 0.400 | 42 | 59 | no | +0.050 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA2 | game_spread | 0.325 | 0.395 | 0.381 | 40 | 61 | no | +0.048 | OK |
| KXNHLGAME-26NOV02VGKBOS-BOS | game_winner | 0.564 | 0.495 | 0.509 | 50 | 51 | yes | +0.047 | OK |
| KXNHLGAME-26NOV02VGKBOS-VGK | game_winner | 0.436 | 0.505 | 0.491 | 51 | 50 | no | +0.047 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK2 | game_spread | 0.231 | 0.295 | 0.281 | 30 | 71 | no | +0.045 | OK |
| KXNHLGAME-26NOV02DETFLA-DET | game_winner | 0.451 | 0.385 | 0.398 | 39 | 62 | yes | +0.044 | OK |
| KXNHLGAME-26NOV02DETFLA-FLA | game_winner | 0.549 | 0.615 | 0.602 | 62 | 39 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET4 | team_total | 0.347 | 0.280 | 0.293 | 29 | 73 | yes | +0.042 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.265 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK3 | game_spread | 0.131 | 0.190 | 0.177 | 20 | 82 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.688 | 0.750 | 0.738 | 76 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET5 | team_total | 0.175 | 0.125 | 0.134 | 13 | 88 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 | team_total | 0.558 | 0.615 | 0.604 | 62 | 39 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET3 | team_total | 0.561 | 0.505 | 0.516 | 51 | 50 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK2 | team_total | 0.778 | 0.830 | 0.821 | 84 | 18 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.852 | 0.895 | 0.887 | 90 | 11 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET2 | game_spread | 0.241 | 0.190 | 0.200 | 20 | 82 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.277 | 0.335 | 0.323 | 35 | 68 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3 | team_total | 0.654 | 0.605 | 0.615 | 61 | 40 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS3 | game_spread | 0.218 | 0.175 | 0.183 | 18 | 83 | yes | +0.027 | OK |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.627 | 0.675 | 0.666 | 68 | 33 | no | +0.027 | OK |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.373 | 0.325 | 0.334 | 33 | 68 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS4 | team_total | 0.440 | 0.390 | 0.400 | 40 | 62 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.765 | 0.805 | 0.797 | 81 | 20 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK5 | team_total | 0.177 | 0.220 | 0.211 | 23 | 79 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS5 | team_total | 0.242 | 0.200 | 0.208 | 21 | 81 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET6 | team_total | 0.073 | 0.040 | 0.045 | 5 | 97 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.864 | 0.905 | 0.898 | 92 | 11 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 | team_total | 0.414 | 0.460 | 0.451 | 47 | 55 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.311 | 0.270 | 0.278 | 28 | 74 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.556 | 0.595 | 0.587 | 60 | 41 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET2 | team_total | 0.779 | 0.740 | 0.748 | 75 | 27 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.226 | 0.195 | 0.201 | 20 | 81 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA2 | team_total | 0.827 | 0.865 | 0.858 | 88 | 15 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5 | team_total | 0.141 | 0.115 | 0.120 | 12 | 89 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA3 | team_total | 0.632 | 0.670 | 0.663 | 68 | 34 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET3 | game_spread | 0.138 | 0.115 | 0.119 | 12 | 89 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA5 | team_total | 0.227 | 0.260 | 0.253 | 27 | 75 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS6 | team_total | 0.114 | 0.085 | 0.090 | 10 | 93 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.615 | 0.585 | 0.591 | 59 | 42 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.133 | 0.155 | 0.150 | 16 | 85 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.124 | 0.105 | 0.109 | 11 | 90 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.504 | 0.475 | 0.481 | 48 | 53 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.103 | 0.080 | 0.084 | 9 | 93 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV02DETFLA-6 | game_total | 0.554 | 0.525 | 0.531 | 53 | 48 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-3 | game_total | 0.964 | 0.980 | 0.978 | 99 | 3 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI2 | game_spread | 0.184 | 0.160 | 0.165 | 17 | 85 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI3 | game_spread | 0.099 | 0.085 | 0.088 | 9 | 92 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.057 | 0.040 | 0.043 | 5 | 97 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-4 | game_total | 0.859 | 0.875 | 0.872 | 88 | 13 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV02COLCHI-10 | game_total | 0.082 | 0.095 | 0.092 | 10 | 91 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV02DETFLA-7 | game_total | 0.439 | 0.415 | 0.420 | 42 | 59 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.223 | 0.195 | 0.200 | 21 | 82 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.442 | 0.465 | 0.460 | 47 | 54 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV02CGYSJ-SJ3 | game_spread | 0.198 | 0.215 | 0.212 | 22 | 79 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS2 | team_total | 0.839 | 0.820 | 0.824 | 83 | 19 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI4 | team_total | 0.294 | 0.270 | 0.275 | 28 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK6 | team_total | 0.076 | 0.085 | 0.083 | 9 | 92 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.180 | 0.195 | 0.192 | 20 | 81 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-8 | game_total | 0.251 | 0.235 | 0.238 | 24 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-9 | game_total | 0.175 | 0.160 | 0.163 | 17 | 85 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26NOV02CGYSJ-SJ | game_winner | 0.532 | 0.515 | 0.518 | 52 | 49 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY3 | game_spread | 0.156 | 0.165 | 0.163 | 17 | 84 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.963 | 0.975 | 0.973 | 99 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.111 | 0.100 | 0.102 | 11 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ4 | team_total | 0.450 | 0.430 | 0.434 | 44 | 58 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-10 | game_total | 0.078 | 0.070 | 0.072 | 8 | 94 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-5 | game_total | 0.776 | 0.790 | 0.787 | 80 | 22 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ5 | team_total | 0.255 | 0.240 | 0.243 | 25 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.256 | 0.270 | 0.267 | 28 | 74 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2 | team_total | 0.733 | 0.720 | 0.723 | 73 | 29 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY2 | game_spread | 0.263 | 0.255 | 0.256 | 26 | 75 |  | -0.011 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 0.564 | 0.511 | 0.176 | 0.214 | 6.24 | 6.47 | 0.969/1.004 | KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 +0.071 |
| DET @ FLA | 0.549 | 0.565 | 0.175 | 0.214 | 6.13 | 6.34 | 0.999/1.016 | KXNHLTOTAL-26NOV02DETFLA-7 +0.038 |
| COL @ CHI | 0.373 | 0.351 | 0.173 | 0.201 | 6.17 | 6.53 | 1.004/0.977 | KXNHLTOTAL-26NOV02COLCHI-7 +0.067 |
| CGY @ SJS | 0.532 | 0.562 | 0.169 | 0.218 | 6.54 | 6.42 | 1.035/0.998 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY3 -0.033 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- William Borgen: 1+ goals YES @ 5c · p 0.0724 (adj 0.0655) · $2.88 · thesis BOS:WINS_BY_2PLUS
- Sam Reinhart: 1+ goals NO @ 63c · p 0.7054 (adj 0.6853) · $17.03 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1276 (adj 0.1144) · $4.74 · thesis FLA:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 62c · p 0.6762 (adj 0.6597) · $12.97 · thesis FLA:SUPPRESSED
- Detroit over 3.5 goals scored YES @ 29c · p 0.3614 (adj 0.3207) · $5.68 · thesis DET:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2685 (adj 0.2526) · $11.41 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 61c · p 0.6929 (adj 0.6464) · $17.37 · thesis CHI:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 54c · p 0.6226 (adj 0.5763) · $12.63 · thesis CHI:SUPPRESSED
- Frank Nazar: 1+ goals YES @ 18c · p 0.215 (adj 0.2037) · $4.99 · thesis CHI:OFFENSE_4PLUS
- Dmitry Orlov: 1+ goals NO @ 91c · p 0.9345 (adj 0.9271) · $20.0 · thesis DIFFUSE
- Michael Misa: 1+ goals YES @ 19c · p 0.2274 (adj 0.2143) · $4.05 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BOS** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.5, exp saves 24.64 (sd 6.73), pull risk 0.064
- VGK net: Carter Hart (PROJECTED) exp shots 26.12, exp saves 22.53 (sd 6.36), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.412 | 0.525 | 53/48 | +0.091 | STANDARD |
| Mitch Marner: 1+ points | 0.545 | 0.655 | 67/36 | +0.079 | STANDARD |
| Jack Eichel: 1+ assists | 0.438 | 0.540 | 55/47 | +0.075 | STANDARD |
| Hampus Lindholm: 1+ points | 0.342 | 0.250 | 27/77 | +0.058 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.293 | 0.205 | 22/81 | +0.061 | STANDARD |
| Jack Eichel: 2+ points | 0.239 | 0.325 | 34/69 | +0.056 | STANDARD |

**DET @ FLA** · priced 155/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 26.78, exp saves 23.29 (sd 6.33), pull risk 0.055
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.16, exp saves 23.23 (sd 6.38), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.525 | 0.640 | 65/37 | +0.089 | STANDARD |
| Sam Reinhart: 1+ assists | 0.324 | 0.430 | 44/58 | +0.079 | STANDARD |
| Sam Reinhart: 2+ points | 0.172 | 0.260 | 28/76 | +0.056 | STANDARD |
| Sam Reinhart: 1+ goals | 0.295 | 0.375 | 38/63 | +0.059 | STANDARD |
| Lucas Raymond: 1+ assists | 0.344 | 0.415 | 43/60 | +0.040 | STANDARD |
| Brady Tkachuk: 2+ points | 0.197 | 0.265 | 28/75 | +0.040 | STANDARD |

**COL @ CHI** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 31.92, exp saves 26.88 (sd 7.43), pull risk 0.088
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.7, exp saves 21.74 (sd 6.01), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.307 | 0.400 | 41/61 | +0.066 | STANDARD |
| Connor Bedard: 1+ assists | 0.377 | 0.470 | 48/54 | +0.065 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.522 | 0.610 | 62/40 | +0.061 | STANDARD |
| Connor Bedard: 2+ points | 0.205 | 0.285 | 30/73 | +0.051 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.381 | 0.460 | 47/55 | +0.052 | STANDARD |
| Connor Bedard: 1+ points | 0.563 | 0.630 | 64/38 | +0.041 | STANDARD |

**CGY @ SJS** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.38, exp saves 24.78 (sd 6.66), pull risk 0.051
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.99, exp saves 24.8 (sd 6.85), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ points | 0.663 | 0.555 | 73/62 | -0.081 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.437 | 0.530 | 55/49 | +0.055 | STANDARD |
| Macklin Celebrini: 2+ points | 0.305 | 0.385 | 40/63 | +0.049 | STANDARD |
| Ivar Stenberg: 1+ points | 0.391 | 0.470 | 50/56 | +0.032 | STANDARD |
| Collin Graf: 1+ assists | 0.319 | 0.245 | 26/77 | +0.046 | STANDARD |
| Ivar Stenberg: 2+ points | 0.091 | 0.165 | 18/85 | +0.050 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
