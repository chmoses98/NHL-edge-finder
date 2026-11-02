# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-02T21:21:38Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2869 · contracts joined: 909 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 809, 'OK': 66, 'NO_EDGE': 34}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 139, 'game_early_goal': 4, 'first_goal': 141, 'game_winner': 8, 'player_goals': 234, 'game_overtime': 4, 'player_points': 186, 'goalie_saves': 5, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 2026-11-03T00:00:00Z | T-90m | 0.587 | 0.413 | 0.173 | 6.12 | 3.32 | 2.79 | 234 (25/209) | CONFIRMED/PROJECTED |
| DET @ FLA | 2026-11-03T00:00:00Z | T-90m | 0.521 | 0.479 | 0.176 | 6.26 | 3.21 | 3.06 | 221 (25/196) | CONFIRMED/CONFIRMED |
| COL @ CHI | 2026-11-03T01:00:00Z | T-3h | 0.355 | 0.645 | 0.178 | 5.98 | 2.54 | 3.44 | 219 (25/194) | CONFIRMED/PROJECTED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-3h | 0.530 | 0.470 | 0.166 | 6.65 | 3.42 | 3.23 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET3 | team_total | 0.596 | 0.485 | 0.508 | 49 | 52 | yes | +0.089 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET4 | team_total | 0.376 | 0.275 | 0.294 | 28 | 73 | yes | +0.082 | OK |
| KXNHLGAME-26NOV02VGKBOS-VGK | game_winner | 0.413 | 0.515 | 0.494 | 52 | 49 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 | team_total | 0.315 | 0.420 | 0.398 | 43 | 59 | no | +0.078 | OK |
| KXNHLGAME-26NOV02DETFLA-DET | game_winner | 0.479 | 0.385 | 0.403 | 39 | 62 | yes | +0.072 | OK |
| KXNHLGAME-26NOV02DETFLA-FLA | game_winner | 0.521 | 0.615 | 0.597 | 62 | 39 | no | +0.072 | OK |
| KXNHLGAME-26NOV02VGKBOS-BOS | game_winner | 0.587 | 0.495 | 0.514 | 50 | 51 | yes | +0.069 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA2 | game_spread | 0.305 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.466 | 0.555 | 0.537 | 56 | 45 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 | team_total | 0.530 | 0.620 | 0.603 | 63 | 39 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET5 | team_total | 0.198 | 0.120 | 0.133 | 13 | 89 | yes | +0.060 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK2 | game_spread | 0.216 | 0.295 | 0.278 | 30 | 71 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA3 | game_spread | 0.188 | 0.265 | 0.248 | 27 | 74 | no | +0.059 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK3 | game_spread | 0.120 | 0.195 | 0.178 | 20 | 81 | no | +0.059 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS2 | game_spread | 0.362 | 0.285 | 0.300 | 29 | 72 | yes | +0.058 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK2 | team_total | 0.758 | 0.830 | 0.817 | 84 | 18 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.680 | 0.750 | 0.737 | 76 | 26 | no | +0.047 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.527 | 0.595 | 0.582 | 60 | 41 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET2 | team_total | 0.805 | 0.735 | 0.750 | 75 | 28 | yes | +0.042 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.324 | 0.265 | 0.276 | 27 | 74 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.833 | 0.885 | 0.876 | 89 | 12 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK5 | team_total | 0.159 | 0.220 | 0.207 | 23 | 79 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.267 | 0.330 | 0.317 | 34 | 68 | no | +0.038 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.268 | 0.325 | 0.313 | 33 | 68 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.742 | 0.800 | 0.789 | 81 | 21 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET6 | team_total | 0.086 | 0.040 | 0.047 | 5 | 97 | yes | +0.033 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.413 | 0.465 | 0.454 | 47 | 54 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3 | team_total | 0.656 | 0.600 | 0.611 | 61 | 41 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET3 | game_spread | 0.156 | 0.115 | 0.122 | 12 | 89 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS3 | game_spread | 0.229 | 0.180 | 0.189 | 19 | 83 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.856 | 0.905 | 0.897 | 92 | 11 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.634 | 0.585 | 0.595 | 59 | 42 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.524 | 0.475 | 0.485 | 48 | 53 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02DETFLA-6 | game_total | 0.574 | 0.525 | 0.535 | 53 | 48 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 | team_total | 0.409 | 0.460 | 0.450 | 47 | 55 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-8 | game_total | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS4 | team_total | 0.441 | 0.390 | 0.400 | 40 | 62 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.235 | 0.195 | 0.203 | 20 | 81 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-7 | game_total | 0.460 | 0.415 | 0.424 | 42 | 59 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.234 | 0.190 | 0.198 | 20 | 82 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS5 | team_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS6 | team_total | 0.115 | 0.080 | 0.086 | 9 | 93 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA2 | team_total | 0.824 | 0.865 | 0.857 | 88 | 15 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA3 | team_total | 0.628 | 0.670 | 0.662 | 68 | 34 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV02DETFLA-9 | game_total | 0.186 | 0.155 | 0.161 | 16 | 85 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.125 | 0.155 | 0.149 | 16 | 85 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.111 | 0.080 | 0.086 | 9 | 93 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-4 | game_total | 0.848 | 0.875 | 0.870 | 88 | 13 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.233 | 0.270 | 0.262 | 28 | 74 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.156 | 0.185 | 0.179 | 19 | 82 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.410 | 0.445 | 0.438 | 45 | 56 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.117 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.128 | 0.100 | 0.105 | 11 | 91 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK6 | team_total | 0.065 | 0.090 | 0.084 | 10 | 92 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-5 | game_total | 0.760 | 0.790 | 0.784 | 80 | 22 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-6 | game_total | 0.547 | 0.575 | 0.569 | 58 | 43 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ4 | team_total | 0.462 | 0.435 | 0.440 | 44 | 57 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-4 | game_total | 0.891 | 0.870 | 0.874 | 88 | 14 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA5 | team_total | 0.225 | 0.255 | 0.249 | 27 | 76 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ5 | team_total | 0.265 | 0.235 | 0.241 | 25 | 78 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS2 | team_total | 0.842 | 0.820 | 0.824 | 83 | 19 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.956 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ3 | team_total | 0.667 | 0.640 | 0.645 | 65 | 37 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-7 | game_total | 0.432 | 0.455 | 0.450 | 46 | 55 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV02DETFLA-10 | game_total | 0.085 | 0.070 | 0.073 | 8 | 94 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY3 | team_total | 0.626 | 0.595 | 0.601 | 61 | 42 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.355 | 0.335 | 0.339 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.645 | 0.665 | 0.661 | 67 | 34 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-5 | game_total | 0.820 | 0.800 | 0.804 | 81 | 21 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-5 | game_total | 0.781 | 0.760 | 0.764 | 77 | 25 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-3 | game_total | 0.968 | 0.960 | 0.962 | 97 | 5 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-4 | game_total | 0.863 | 0.850 | 0.853 | 86 | 16 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY4 | team_total | 0.411 | 0.390 | 0.394 | 40 | 62 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.047 | 0.040 | 0.041 | 5 | 97 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 0.587 | 0.516 | 0.173 | 0.220 | 6.12 | 6.44 | 0.957/1.004 | KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 +0.090 |
| DET @ FLA | 0.521 | 0.562 | 0.176 | 0.213 | 6.26 | 6.41 | 1.016/1.025 | KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 +0.046 |
| COL @ CHI | 0.355 | 0.362 | 0.178 | 0.201 | 5.98 | 6.48 | 0.989/0.974 | KXNHLTOTAL-26NOV02COLCHI-7 +0.082 |
| CGY @ SJS | 0.530 | 0.559 | 0.166 | 0.212 | 6.65 | 6.46 | 1.040/1.007 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 -0.040 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Mitch Marner: 2+ assists NO @ 84c · p 0.9072 (adj 0.8711) · $19.5 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.077 (adj 0.0665) · $2.93 · thesis VGK:OFFENSE_4PLUS
- JJ Peterka: 2+ assists NO @ 92c · p 0.9613 (adj 0.9382) · $19.5 · thesis BOS:SUPPRESSED
- Nikita Zadorov: 1+ goals YES @ 4c · p 0.0588 (adj 0.0529) · $2.32 · thesis BOS:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 62c · p 0.6997 (adj 0.6785) · $19.5 · thesis FLA:SUPPRESSED
- Ben Chiarot: 1+ goals YES @ 3c · p 0.0522 (adj 0.0454) · $2.82 · thesis DET:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1257 (adj 0.1105) · $3.59 · thesis FLA:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 36c · p 0.3985 (adj 0.3864) · $4.05 · thesis DET:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 77c · p 0.823 (adj 0.8073) · $19.5 · thesis COL:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2608 (adj 0.2468) · $8.23 · thesis CHI:OFFENSE_4PLUS
- Cole Smith: 1+ goals YES @ 7c · p 0.0935 (adj 0.0864) · $2.92 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 62c · p 0.7023 (adj 0.6537) · $15.69 · thesis CHI:SUPPRESSED
- Sam Dickinson: 1+ goals YES @ 5c · p 0.0708 (adj 0.0644) · $2.48 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 78c · p 0.8203 (adj 0.8077) · $19.06 · thesis SJS:SUPPRESSED
- Michael Misa: 1+ goals YES @ 18c · p 0.2175 (adj 0.2056) · $4.34 · thesis SJS:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 17c · p 0.2033 (adj 0.1925) · $3.58 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BOS** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.5, exp saves 24.64 (sd 6.72), pull risk 0.065
- VGK net: Carter Hart (PROJECTED) exp shots 26.12, exp saves 22.46 (sd 6.33), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ assists | 0.276 | 0.130 | 24/98 | +0.023 | STANDARD |
| Mitch Marner: 1+ assists | 0.400 | 0.525 | 53/48 | +0.102 | STANDARD |
| Mitch Marner: 1+ points | 0.536 | 0.640 | 65/37 | +0.078 | STANDARD |
| Jack Eichel: 1+ assists | 0.432 | 0.530 | 54/48 | +0.071 | STANDARD |
| Hampus Lindholm: 1+ points | 0.341 | 0.245 | 26/77 | +0.067 | STANDARD |
| Hampus Lindholm: 1+ assists | 0.293 | 0.205 | 22/81 | +0.061 | STANDARD |

**DET @ FLA** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 26.78, exp saves 23.19 (sd 6.37), pull risk 0.062
- DET net: Daniil Tarasov (CONFIRMED) exp shots 27.16, exp saves 23.26 (sd 6.52), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ assists | 0.326 | 0.425 | 43/58 | +0.077 | STANDARD |
| Sam Reinhart: 2+ points | 0.178 | 0.270 | 28/74 | +0.068 | STANDARD |
| Sam Reinhart: 1+ goals | 0.300 | 0.385 | 39/62 | +0.063 | STANDARD |
| Daniil Tarasov: 26+ saves | 0.352 | 0.435 | 45/58 | +0.051 |  |
| Sam Reinhart: 1+ points | 0.525 | 0.605 | 61/40 | +0.058 | STANDARD |
| Gustav Forsling: 1+ points | 0.340 | 0.260 | 29/77 | +0.035 | STANDARD |

**COL @ CHI** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 31.92, exp saves 26.91 (sd 7.36), pull risk 0.087
- COL net: Scott Wedgewood (PROJECTED) exp shots 24.7, exp saves 21.69 (sd 6.04), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.359 | 0.465 | 47/54 | +0.084 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.496 | 0.600 | 61/41 | +0.077 | STANDARD |
| Patrick Kane: 1+ assists | 0.298 | 0.395 | 41/62 | +0.066 | STANDARD |
| Connor Bedard: 1+ assists | 0.381 | 0.470 | 48/54 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.153 | 0.240 | 26/78 | +0.055 | STANDARD |
| Cale Makar: 2+ points | 0.212 | 0.285 | 30/73 | +0.044 | STANDARD |

**CGY @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.38, exp saves 24.66 (sd 6.72), pull risk 0.057
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.99, exp saves 24.78 (sd 6.97), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.296 | 0.115 | 22/99 | +0.064 | STANDARD |
| Michael Kesselring: 1+ points | 0.312 | 0.150 | 27/97 | +0.028 | STANDARD |
| Sam Dickinson: 1+ assists | 0.243 | 0.105 | 20/99 | +0.031 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.435 | 0.555 | 57/46 | +0.087 | STANDARD |
| Macklin Celebrini: 2+ points | 0.303 | 0.420 | 44/60 | +0.080 | STANDARD |
| Zach Whitecloud: 1+ points | 0.255 | 0.160 | 20/88 | +0.043 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
