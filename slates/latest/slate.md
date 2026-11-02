# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-02T16:22:27Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2841 · contracts joined: 881 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 781, 'OK': 68, 'NO_EDGE': 32}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 127, 'game_early_goal': 4, 'first_goal': 144, 'game_winner': 8, 'player_goals': 238, 'game_overtime': 4, 'player_points': 168, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 2026-11-03T00:00:00Z | T-6h | 0.587 | 0.413 | 0.173 | 6.12 | 3.32 | 2.79 | 216 (25/191) | CONFIRMED/PROJECTED |
| DET @ FLA | 2026-11-03T00:00:00Z | T-6h | 0.528 | 0.472 | 0.176 | 6.28 | 3.22 | 3.05 | 223 (25/198) | CONFIRMED/PROJECTED |
| COL @ CHI | 2026-11-03T01:00:00Z | T-6h | 0.373 | 0.627 | 0.173 | 6.17 | 2.67 | 3.49 | 220 (25/195) | PROJECTED/PROJECTED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-6h | 0.532 | 0.468 | 0.169 | 6.54 | 3.38 | 3.17 | 222 (25/197) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 | team_total | 0.315 | 0.415 | 0.394 | 42 | 59 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET4 | team_total | 0.378 | 0.280 | 0.298 | 29 | 73 | yes | +0.074 | OK |
| KXNHLGAME-26NOV02VGKBOS-BOS | game_winner | 0.587 | 0.495 | 0.514 | 50 | 51 | yes | +0.069 | OK |
| KXNHLGAME-26NOV02VGKBOS-VGK | game_winner | 0.413 | 0.505 | 0.486 | 51 | 50 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.474 | 0.565 | 0.547 | 57 | 44 | no | +0.068 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS2 | game_spread | 0.362 | 0.275 | 0.291 | 28 | 73 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET3 | team_total | 0.594 | 0.505 | 0.523 | 51 | 50 | yes | +0.066 | OK |
| KXNHLGAME-26NOV02DETFLA-DET | game_winner | 0.472 | 0.385 | 0.402 | 39 | 62 | yes | +0.066 | OK |
| KXNHLGAME-26NOV02DETFLA-FLA | game_winner | 0.528 | 0.615 | 0.598 | 62 | 39 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA2 | game_spread | 0.308 | 0.395 | 0.377 | 40 | 61 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET5 | team_total | 0.199 | 0.115 | 0.129 | 13 | 90 | yes | +0.061 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK2 | game_spread | 0.216 | 0.295 | 0.278 | 30 | 71 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA3 | game_spread | 0.189 | 0.270 | 0.252 | 28 | 74 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 | team_total | 0.530 | 0.610 | 0.594 | 62 | 40 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET2 | game_spread | 0.264 | 0.190 | 0.203 | 20 | 82 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK2 | team_total | 0.758 | 0.830 | 0.817 | 84 | 18 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK3 | game_spread | 0.120 | 0.190 | 0.174 | 20 | 82 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.265 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK5 | team_total | 0.159 | 0.220 | 0.207 | 23 | 79 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET2 | team_total | 0.802 | 0.740 | 0.753 | 75 | 27 | yes | +0.039 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS3 | game_spread | 0.229 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.688 | 0.750 | 0.738 | 76 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET6 | team_total | 0.086 | 0.040 | 0.047 | 5 | 97 | yes | +0.032 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.852 | 0.895 | 0.887 | 90 | 11 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3 | team_total | 0.656 | 0.605 | 0.615 | 61 | 40 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET3 | game_spread | 0.156 | 0.115 | 0.122 | 12 | 89 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.277 | 0.335 | 0.323 | 35 | 68 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV02DETFLA-6 | game_total | 0.575 | 0.525 | 0.535 | 53 | 48 | yes | +0.028 | OK |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.373 | 0.325 | 0.334 | 33 | 68 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02DETFLA-8 | game_total | 0.267 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS4 | team_total | 0.441 | 0.390 | 0.400 | 40 | 62 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-7 | game_total | 0.461 | 0.415 | 0.424 | 42 | 59 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.765 | 0.805 | 0.797 | 81 | 20 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS5 | team_total | 0.243 | 0.200 | 0.208 | 21 | 81 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.864 | 0.905 | 0.898 | 92 | 11 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 | team_total | 0.413 | 0.465 | 0.455 | 48 | 55 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.311 | 0.270 | 0.278 | 28 | 74 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.556 | 0.595 | 0.587 | 60 | 41 | no | +0.017 | OK |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA2 | team_total | 0.826 | 0.865 | 0.858 | 88 | 15 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.226 | 0.195 | 0.201 | 20 | 81 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI2 | game_spread | 0.184 | 0.155 | 0.160 | 16 | 85 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-4 | game_total | 0.848 | 0.875 | 0.870 | 88 | 13 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA3 | team_total | 0.631 | 0.670 | 0.662 | 68 | 34 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5 | team_total | 0.141 | 0.115 | 0.120 | 12 | 89 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK6 | team_total | 0.065 | 0.090 | 0.084 | 10 | 92 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV02DETFLA-9 | game_total | 0.189 | 0.160 | 0.166 | 17 | 85 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS6 | team_total | 0.115 | 0.085 | 0.090 | 10 | 93 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-5 | game_total | 0.760 | 0.790 | 0.784 | 80 | 22 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.615 | 0.585 | 0.591 | 59 | 42 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.133 | 0.155 | 0.150 | 16 | 85 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.124 | 0.100 | 0.104 | 11 | 91 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.504 | 0.475 | 0.481 | 48 | 53 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.103 | 0.080 | 0.084 | 9 | 93 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA5 | team_total | 0.231 | 0.260 | 0.254 | 27 | 75 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-6 | game_total | 0.547 | 0.575 | 0.569 | 58 | 43 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV02DETFLA-10 | game_total | 0.090 | 0.065 | 0.069 | 8 | 95 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-3 | game_total | 0.964 | 0.980 | 0.978 | 99 | 3 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI3 | game_spread | 0.099 | 0.085 | 0.088 | 9 | 92 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.057 | 0.040 | 0.043 | 5 | 97 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV02COLCHI-10 | game_total | 0.082 | 0.095 | 0.092 | 10 | 91 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.223 | 0.200 | 0.205 | 21 | 81 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS2 | team_total | 0.842 | 0.820 | 0.824 | 83 | 19 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV02DETFLA-5 | game_total | 0.783 | 0.760 | 0.765 | 77 | 25 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-7 | game_total | 0.432 | 0.455 | 0.450 | 46 | 55 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.442 | 0.465 | 0.460 | 47 | 54 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV02CGYSJ-SJ3 | game_spread | 0.198 | 0.215 | 0.212 | 22 | 79 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.256 | 0.275 | 0.271 | 28 | 73 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI4 | team_total | 0.294 | 0.270 | 0.275 | 28 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-8 | game_total | 0.247 | 0.265 | 0.261 | 27 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.180 | 0.195 | 0.192 | 20 | 81 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26NOV02CGYSJ-SJ | game_winner | 0.532 | 0.515 | 0.518 | 52 | 49 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY3 | game_spread | 0.156 | 0.170 | 0.167 | 18 | 84 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-4 | game_total | 0.863 | 0.850 | 0.853 | 86 | 16 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.963 | 0.975 | 0.973 | 99 | 4 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 0.587 | 0.516 | 0.173 | 0.220 | 6.12 | 6.44 | 0.957/1.004 | KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 +0.090 |
| DET @ FLA | 0.528 | 0.559 | 0.176 | 0.210 | 6.28 | 6.38 | 1.016/1.016 | KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 +0.040 |
| COL @ CHI | 0.373 | 0.351 | 0.173 | 0.201 | 6.17 | 6.53 | 1.004/0.977 | KXNHLTOTAL-26NOV02COLCHI-7 +0.067 |
| CGY @ SJS | 0.532 | 0.562 | 0.169 | 0.218 | 6.54 | 6.42 | 1.035/0.998 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY3 -0.033 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Sam Reinhart: 1+ goals NO @ 63c · p 0.7024 (adj 0.6831) · $16.86 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 62c · p 0.676 (adj 0.6608) · $13.14 · thesis FLA:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 12c · p 0.1547 (adj 0.1435) · $4.27 · thesis DET:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 35c · p 0.3986 (adj 0.3852) · $7.51 · thesis DET:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 22c · p 0.2685 (adj 0.2539) · $7.86 · thesis CHI:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 77c · p 0.8123 (adj 0.8005) · $20.0 · thesis COL:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 54c · p 0.6226 (adj 0.5763) · $14.15 · thesis CHI:SUPPRESSED
- Frank Nazar: 1+ goals YES @ 18c · p 0.215 (adj 0.2037) · $4.22 · thesis CHI:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 76c · p 0.8237 (adj 0.8065) · $20.0 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 24c · p 0.2812 (adj 0.2697) · $5.36 · thesis SJS:OFFENSE_4PLUS
- Michael Misa: 1+ goals YES @ 19c · p 0.2274 (adj 0.2155) · $4.32 · thesis SJS:OFFENSE_4PLUS
- Collin Graf: 1+ assists YES @ 26c · p 0.3193 (adj 0.2872) · $4.13 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BOS** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.5, exp saves 24.64 (sd 6.72), pull risk 0.065
- VGK net: Carter Hart (PROJECTED) exp shots 26.12, exp saves 22.46 (sd 6.33), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.400 | 0.525 | 53/48 | +0.102 | STANDARD |
| Mitch Marner: 1+ points | 0.536 | 0.650 | 66/36 | +0.088 | STANDARD |
| Jack Eichel: 1+ assists | 0.432 | 0.535 | 55/48 | +0.071 | STANDARD |
| Hampus Lindholm: 1+ points | 0.341 | 0.250 | 26/76 | +0.067 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.293 | 0.205 | 22/81 | +0.061 | STANDARD |
| Jack Eichel: 2+ points | 0.237 | 0.325 | 34/69 | +0.058 | STANDARD |

**DET @ FLA** · priced 162/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 26.78, exp saves 23.22 (sd 6.37), pull risk 0.062
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.16, exp saves 23.26 (sd 6.44), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.521 | 0.620 | 63/39 | +0.073 | STANDARD |
| Sam Reinhart: 1+ assists | 0.323 | 0.420 | 43/59 | +0.071 | STANDARD |
| Sam Reinhart: 2+ points | 0.172 | 0.250 | 27/77 | +0.046 | STANDARD |
| Sam Reinhart: 1+ goals | 0.298 | 0.375 | 38/63 | +0.056 | STANDARD |
| Justin Faulk: 1+ assists | 0.307 | 0.240 | 26/78 | +0.033 | STANDARD |
| Emmitt Finnie: 2+ points | 0.175 | 0.110 | 15/93 | +0.016 | STANDARD |

**COL @ CHI** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 31.92, exp saves 26.88 (sd 7.43), pull risk 0.088
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.7, exp saves 21.74 (sd 6.01), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.307 | 0.405 | 42/61 | +0.066 | STANDARD |
| Connor Bedard: 1+ assists | 0.377 | 0.470 | 48/54 | +0.065 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.522 | 0.605 | 61/40 | +0.061 | STANDARD |
| Connor Bedard: 2+ points | 0.205 | 0.285 | 30/73 | +0.051 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.381 | 0.460 | 47/55 | +0.052 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.173 | 0.245 | 26/77 | +0.045 | STANDARD |

**CGY @ SJS** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.38, exp saves 24.78 (sd 6.66), pull risk 0.051
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.99, exp saves 24.8 (sd 6.85), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ points | 0.258 | 0.120 | 22/98 | +0.026 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.225 | 0.110 | 20/98 | +0.014 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.437 | 0.540 | 55/47 | +0.075 | STANDARD |
| Ivar Stenberg: 1+ points | 0.391 | 0.475 | 49/54 | +0.052 | STANDARD |
| Macklin Celebrini: 2+ points | 0.305 | 0.385 | 39/62 | +0.059 | STANDARD |
| Kevin Bahl: 1+ points | 0.281 | 0.205 | 25/84 | +0.018 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
