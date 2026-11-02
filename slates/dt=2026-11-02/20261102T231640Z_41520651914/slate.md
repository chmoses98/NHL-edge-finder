# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-02T23:16:40Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2900 · contracts joined: 940 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 840, 'OK': 71, 'NO_EDGE': 29}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 153, 'game_early_goal': 4, 'first_goal': 141, 'game_winner': 8, 'player_goals': 234, 'game_overtime': 4, 'player_points': 203, 'goalie_saves': 5, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 2026-11-03T00:00:00Z | T-30m | 0.587 | 0.413 | 0.173 | 6.12 | 3.32 | 2.79 | 265 (25/240) | CONFIRMED/PROJECTED |
| DET @ FLA | 2026-11-03T00:00:00Z | T-30m | 0.521 | 0.479 | 0.176 | 6.26 | 3.21 | 3.06 | 221 (25/196) | CONFIRMED/CONFIRMED |
| COL @ CHI | 2026-11-03T01:00:00Z | T-90m | 0.373 | 0.627 | 0.172 | 6.09 | 2.65 | 3.44 | 219 (25/194) | CONFIRMED/CONFIRMED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-90m | 0.530 | 0.470 | 0.166 | 6.65 | 3.42 | 3.23 | 235 (25/210) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET3 | team_total | 0.596 | 0.485 | 0.508 | 49 | 52 | yes | +0.089 | OK |
| KXNHLGAME-26NOV02DETFLA-FLA | game_winner | 0.521 | 0.625 | 0.605 | 63 | 38 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET4 | team_total | 0.376 | 0.275 | 0.294 | 28 | 73 | yes | +0.082 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.462 | 0.565 | 0.545 | 57 | 44 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 | team_total | 0.315 | 0.415 | 0.394 | 42 | 59 | no | +0.078 | OK |
| KXNHLGAME-26NOV02DETFLA-DET | game_winner | 0.479 | 0.385 | 0.403 | 39 | 62 | yes | +0.072 | OK |
| KXNHLGAME-26NOV02VGKBOS-BOS | game_winner | 0.587 | 0.495 | 0.514 | 50 | 51 | yes | +0.069 | OK |
| KXNHLGAME-26NOV02VGKBOS-VGK | game_winner | 0.413 | 0.505 | 0.486 | 51 | 50 | no | +0.069 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA2 | game_spread | 0.305 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 | team_total | 0.530 | 0.620 | 0.603 | 63 | 39 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET5 | team_total | 0.198 | 0.125 | 0.138 | 13 | 88 | yes | +0.060 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK2 | game_spread | 0.216 | 0.295 | 0.278 | 30 | 71 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA3 | game_spread | 0.188 | 0.265 | 0.248 | 27 | 74 | no | +0.059 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS2 | game_spread | 0.362 | 0.285 | 0.300 | 29 | 72 | yes | +0.058 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET2 | game_spread | 0.268 | 0.190 | 0.204 | 20 | 82 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET2 | team_total | 0.805 | 0.730 | 0.746 | 74 | 28 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK2 | team_total | 0.758 | 0.830 | 0.817 | 84 | 18 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK3 | game_spread | 0.120 | 0.190 | 0.174 | 20 | 82 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.266 | 0.335 | 0.320 | 34 | 67 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.681 | 0.750 | 0.737 | 76 | 26 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.260 | 0.325 | 0.311 | 33 | 68 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.324 | 0.265 | 0.276 | 27 | 74 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK5 | team_total | 0.159 | 0.220 | 0.207 | 23 | 79 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET6 | team_total | 0.086 | 0.045 | 0.051 | 5 | 96 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3 | team_total | 0.656 | 0.605 | 0.615 | 61 | 40 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.844 | 0.885 | 0.878 | 89 | 12 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET3 | game_spread | 0.156 | 0.115 | 0.122 | 12 | 89 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS3 | game_spread | 0.229 | 0.180 | 0.189 | 19 | 83 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA2 | team_total | 0.824 | 0.870 | 0.862 | 88 | 14 | no | +0.028 | OK |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.373 | 0.325 | 0.334 | 33 | 68 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.546 | 0.595 | 0.585 | 60 | 41 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.762 | 0.805 | 0.797 | 81 | 20 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.634 | 0.585 | 0.595 | 59 | 42 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.524 | 0.475 | 0.485 | 48 | 53 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV02DETFLA-6 | game_total | 0.574 | 0.525 | 0.535 | 53 | 48 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.397 | 0.445 | 0.435 | 45 | 56 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.858 | 0.905 | 0.897 | 92 | 11 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 | team_total | 0.409 | 0.460 | 0.450 | 47 | 55 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-8 | game_total | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS4 | team_total | 0.441 | 0.390 | 0.400 | 40 | 62 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.235 | 0.195 | 0.203 | 20 | 81 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-7 | game_total | 0.460 | 0.415 | 0.424 | 42 | 59 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS5 | team_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.128 | 0.095 | 0.101 | 10 | 91 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-5 | game_total | 0.760 | 0.795 | 0.788 | 80 | 21 | no | +0.018 | OK |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA3 | team_total | 0.628 | 0.670 | 0.662 | 68 | 34 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV02DETFLA-9 | game_total | 0.186 | 0.155 | 0.161 | 16 | 85 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.111 | 0.080 | 0.086 | 9 | 93 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.127 | 0.155 | 0.149 | 16 | 85 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-4 | game_total | 0.848 | 0.875 | 0.870 | 88 | 13 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.429 | 0.465 | 0.458 | 47 | 54 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.234 | 0.195 | 0.202 | 21 | 82 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA5 | team_total | 0.225 | 0.260 | 0.253 | 27 | 75 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.117 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK6 | team_total | 0.065 | 0.085 | 0.081 | 9 | 92 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS6 | team_total | 0.115 | 0.090 | 0.095 | 10 | 92 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-6 | game_total | 0.547 | 0.575 | 0.569 | 58 | 43 | no | +0.006 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI2 | game_spread | 0.185 | 0.165 | 0.169 | 17 | 84 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.242 | 0.265 | 0.260 | 27 | 74 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ4 | team_total | 0.462 | 0.435 | 0.440 | 44 | 57 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.165 | 0.185 | 0.181 | 19 | 82 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-3 | game_total | 0.964 | 0.975 | 0.973 | 98 | 3 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI3 | game_spread | 0.099 | 0.085 | 0.088 | 9 | 92 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-4 | game_total | 0.891 | 0.875 | 0.878 | 88 | 13 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.055 | 0.040 | 0.043 | 5 | 97 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ5 | team_total | 0.265 | 0.235 | 0.241 | 25 | 78 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS2 | team_total | 0.842 | 0.820 | 0.824 | 83 | 19 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ3 | team_total | 0.667 | 0.640 | 0.645 | 65 | 37 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-7 | game_total | 0.432 | 0.455 | 0.450 | 46 | 55 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV02DETFLA-10 | game_total | 0.085 | 0.070 | 0.073 | 8 | 94 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-5 | game_total | 0.820 | 0.805 | 0.808 | 81 | 20 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-5 | game_total | 0.781 | 0.760 | 0.764 | 77 | 25 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5 | team_total | 0.137 | 0.120 | 0.123 | 13 | 89 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.960 | 0.970 | 0.968 | 98 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-2 | game_total | 0.987 | 0.980 | 0.982 | 99 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-3 | game_total | 0.968 | 0.965 | 0.966 | 97 | 4 |  | -0.004 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 0.587 | 0.516 | 0.173 | 0.220 | 6.12 | 6.44 | 0.957/1.004 | KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 +0.090 |
| DET @ FLA | 0.521 | 0.562 | 0.176 | 0.213 | 6.26 | 6.41 | 1.016/1.025 | KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 +0.046 |
| COL @ CHI | 0.373 | 0.360 | 0.172 | 0.206 | 6.09 | 6.49 | 0.989/0.980 | KXNHLTOTAL-26NOV02COLCHI-7 +0.071 |
| CGY @ SJS | 0.530 | 0.559 | 0.166 | 0.212 | 6.65 | 6.46 | 1.040/1.007 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 -0.040 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Mitch Marner: 2+ assists NO @ 84c · p 0.9072 (adj 0.8711) · $20.0 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.077 (adj 0.0665) · $3.02 · thesis VGK:OFFENSE_4PLUS
- Nikita Zadorov: 1+ goals YES @ 4c · p 0.0588 (adj 0.0529) · $2.35 · thesis BOS:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 15c · p 0.1854 (adj 0.1753) · $4.66 · thesis BOS:OFFENSE_4PLUS
- Alex DeBrincat: 2+ goals YES @ 6c · p 0.0912 (adj 0.0822) · $4.0 · thesis DET:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 63c · p 0.6997 (adj 0.681) · $20.0 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1257 (adj 0.1155) · $5.05 · thesis FLA:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 35c · p 0.3985 (adj 0.3851) · $2.99 · thesis DET:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 21c · p 0.2647 (adj 0.2498) · $10.28 · thesis CHI:OFFENSE_4PLUS
- Cole Smith: 1+ goals YES @ 7c · p 0.0951 (adj 0.0876) · $3.45 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 62c · p 0.7028 (adj 0.6539) · $15.38 · thesis CHI:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 54c · p 0.6226 (adj 0.5738) · $12.26 · thesis CHI:SUPPRESSED
- Ivar Stenberg: 1+ goals NO @ 77c · p 0.8203 (adj 0.8065) · $20.0 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 24c · p 0.2843 (adj 0.272) · $5.61 · thesis SJS:OFFENSE_4PLUS
- Michael Misa: 1+ goals YES @ 18c · p 0.2175 (adj 0.2069) · $4.94 · thesis SJS:OFFENSE_4PLUS
- Michael Misa: 1+ assists YES @ 26c · p 0.3199 (adj 0.2874) · $4.0 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BOS** · priced 213/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.5, exp saves 24.64 (sd 6.72), pull risk 0.065
- VGK net: Carter Hart (PROJECTED) exp shots 26.12, exp saves 22.46 (sd 6.33), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Zadorov: 1+ points | 0.263 | 0.115 | 21/98 | +0.042 | STANDARD |
| Mark Kastelic: 1+ points | 0.245 | 0.105 | 19/98 | +0.045 | STANDARD |
| Tanner Jeannot: 1+ points | 0.231 | 0.095 | 17/98 | +0.051 | STANDARD |
| Matthew Poitras: 1+ points | 0.253 | 0.125 | 23/98 | +0.011 | STANDARD |
| Mitch Marner: 1+ assists | 0.400 | 0.525 | 53/48 | +0.102 | STANDARD |
| Marc Gatcomb: 1+ points | 0.206 | 0.100 | 18/98 | +0.016 | STANDARD |

**DET @ FLA** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 26.78, exp saves 23.19 (sd 6.37), pull risk 0.062
- DET net: Daniil Tarasov (CONFIRMED) exp shots 27.16, exp saves 23.26 (sd 6.52), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Daniil Tarasov: 26+ saves | 0.352 | 0.470 | 49/55 | +0.081 |  |
| Sam Reinhart: 1+ assists | 0.326 | 0.425 | 43/58 | +0.077 | STANDARD |
| Sam Reinhart: 1+ points | 0.525 | 0.620 | 63/39 | +0.068 | STANDARD |
| Sam Reinhart: 2+ points | 0.178 | 0.265 | 28/75 | +0.059 | STANDARD |
| Sam Reinhart: 1+ goals | 0.300 | 0.375 | 38/63 | +0.053 | STANDARD |
| Brady Tkachuk: 2+ points | 0.198 | 0.265 | 27/74 | +0.048 | STANDARD |

**COL @ CHI** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 31.92, exp saves 26.8 (sd 7.53), pull risk 0.092
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 24.7, exp saves 21.74 (sd 6.05), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.297 | 0.395 | 41/62 | +0.066 | STANDARD |
| Connor Bedard: 1+ assists | 0.377 | 0.475 | 49/54 | +0.065 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.366 | 0.460 | 48/56 | +0.057 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.509 | 0.600 | 61/41 | +0.064 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.157 | 0.240 | 26/78 | +0.051 | STANDARD |
| Spencer Knight: 29+ saves | 0.409 | 0.485 | 49/52 | +0.054 |  |

**CGY @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.38, exp saves 24.66 (sd 6.72), pull risk 0.057
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.99, exp saves 24.78 (sd 6.97), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ assists | 0.243 | 0.090 | 16/98 | +0.073 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.435 | 0.570 | 58/44 | +0.108 | STANDARD |
| Macklin Celebrini: 2+ points | 0.303 | 0.420 | 44/60 | +0.080 | STANDARD |
| Sam Dickinson: 1+ points | 0.296 | 0.185 | 21/84 | +0.074 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.113 | 0.210 | 23/81 | +0.066 | STANDARD |
| Ivar Stenberg: 1+ points | 0.409 | 0.500 | 51/51 | +0.063 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
