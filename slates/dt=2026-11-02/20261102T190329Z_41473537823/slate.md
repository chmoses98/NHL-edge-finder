# NHL slate 2026-11-02 — RESEARCH_ONLY

generated 2026-11-02T19:03:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2862 · contracts joined: 902 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 802, 'OK': 67, 'NO_EDGE': 33}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 134, 'game_early_goal': 4, 'first_goal': 143, 'game_winner': 8, 'player_goals': 238, 'game_overtime': 4, 'player_points': 179, 'goalie_saves': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 2026-11-03T00:00:00Z | T-3h | 0.587 | 0.413 | 0.173 | 6.12 | 3.32 | 2.79 | 234 (25/209) | CONFIRMED/PROJECTED |
| DET @ FLA | 2026-11-03T00:00:00Z | T-3h | 0.521 | 0.479 | 0.176 | 6.26 | 3.21 | 3.06 | 221 (25/196) | CONFIRMED/CONFIRMED |
| COL @ CHI | 2026-11-03T01:00:00Z | T-3h | 0.378 | 0.622 | 0.170 | 6.14 | 2.68 | 3.46 | 222 (25/197) | PROBABLE/PROJECTED |
| CGY @ SJS | 2026-11-03T02:00:00Z | T-6h | 0.539 | 0.461 | 0.168 | 6.58 | 3.42 | 3.17 | 225 (25/200) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET4 | team_total | 0.376 | 0.275 | 0.294 | 28 | 73 | yes | +0.082 | OK |
| KXNHLGAME-26NOV02VGKBOS-VGK | game_winner | 0.413 | 0.515 | 0.494 | 52 | 49 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET3 | team_total | 0.596 | 0.490 | 0.512 | 50 | 52 | yes | +0.079 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK4 | team_total | 0.315 | 0.415 | 0.394 | 42 | 59 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 | team_total | 0.530 | 0.625 | 0.607 | 63 | 38 | no | +0.073 | OK |
| KXNHLGAME-26NOV02DETFLA-DET | game_winner | 0.479 | 0.385 | 0.403 | 39 | 62 | yes | +0.072 | OK |
| KXNHLGAME-26NOV02DETFLA-FLA | game_winner | 0.521 | 0.615 | 0.597 | 62 | 39 | no | +0.072 | OK |
| KXNHLGAME-26NOV02VGKBOS-BOS | game_winner | 0.587 | 0.495 | 0.514 | 50 | 51 | yes | +0.069 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA2 | game_spread | 0.305 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS2 | game_spread | 0.362 | 0.275 | 0.291 | 28 | 73 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL4 | team_total | 0.470 | 0.560 | 0.542 | 57 | 45 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET5 | team_total | 0.198 | 0.120 | 0.133 | 13 | 89 | yes | +0.060 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK2 | game_spread | 0.216 | 0.295 | 0.278 | 30 | 71 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV02DETFLA-FLA3 | game_spread | 0.188 | 0.265 | 0.248 | 27 | 74 | no | +0.059 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-VGK3 | game_spread | 0.120 | 0.195 | 0.178 | 20 | 81 | no | +0.059 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK2 | team_total | 0.758 | 0.830 | 0.817 | 84 | 18 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL3 | team_total | 0.682 | 0.750 | 0.737 | 76 | 26 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET2 | team_total | 0.805 | 0.735 | 0.750 | 75 | 28 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK5 | team_total | 0.159 | 0.220 | 0.207 | 23 | 79 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV02VGKBOS-BOS3 | game_spread | 0.229 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL5 | team_total | 0.271 | 0.330 | 0.318 | 34 | 68 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL3 | game_spread | 0.261 | 0.320 | 0.308 | 33 | 69 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-DET6 | team_total | 0.086 | 0.040 | 0.047 | 5 | 97 | yes | +0.033 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-8 | game_total | 0.316 | 0.265 | 0.275 | 27 | 74 | yes | +0.032 | OK |
| KXNHLTOTAL-26NOV02COLCHI-4 | game_total | 0.852 | 0.895 | 0.887 | 90 | 11 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV02DETFLA-DET3 | game_spread | 0.156 | 0.115 | 0.122 | 12 | 89 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV02DETFLA-6 | game_total | 0.574 | 0.525 | 0.535 | 53 | 48 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL2 | team_total | 0.858 | 0.905 | 0.897 | 92 | 11 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 | team_total | 0.409 | 0.460 | 0.450 | 47 | 55 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-8 | game_total | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS4 | team_total | 0.441 | 0.390 | 0.400 | 40 | 62 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV02DETFLA-7 | game_total | 0.460 | 0.415 | 0.424 | 42 | 59 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV02COLCHI-COL2 | game_spread | 0.400 | 0.445 | 0.436 | 45 | 56 | no | +0.023 | OK |
| KXNHLGAME-26NOV02COLCHI-CHI | game_winner | 0.378 | 0.335 | 0.343 | 34 | 67 | yes | +0.022 | OK |
| KXNHLGAME-26NOV02COLCHI-COL | game_winner | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS5 | team_total | 0.243 | 0.205 | 0.212 | 21 | 80 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV02COLCHI-6 | game_total | 0.552 | 0.595 | 0.586 | 60 | 41 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS3 | team_total | 0.656 | 0.610 | 0.619 | 62 | 40 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-9 | game_total | 0.230 | 0.195 | 0.202 | 20 | 81 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-5 | game_total | 0.760 | 0.795 | 0.788 | 80 | 21 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA2 | team_total | 0.824 | 0.865 | 0.857 | 88 | 15 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA3 | team_total | 0.628 | 0.670 | 0.662 | 68 | 34 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-6 | game_total | 0.622 | 0.585 | 0.593 | 59 | 42 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-4 | game_total | 0.848 | 0.875 | 0.870 | 88 | 13 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-7 | game_total | 0.511 | 0.470 | 0.478 | 48 | 54 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV02COLCHI-5 | game_total | 0.765 | 0.800 | 0.793 | 81 | 21 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ6 | team_total | 0.127 | 0.100 | 0.105 | 11 | 91 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV02COLCHI-7 | game_total | 0.433 | 0.465 | 0.459 | 47 | 54 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY6 | team_total | 0.105 | 0.080 | 0.085 | 9 | 93 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI2 | game_spread | 0.189 | 0.165 | 0.170 | 17 | 84 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS6 | team_total | 0.115 | 0.090 | 0.095 | 10 | 92 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV02CGYSJ-10 | game_total | 0.113 | 0.090 | 0.094 | 10 | 92 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-6 | game_total | 0.547 | 0.575 | 0.569 | 58 | 43 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV02DETFLA-9 | game_total | 0.186 | 0.160 | 0.165 | 17 | 85 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV02COLCHI-CHI3 | game_spread | 0.100 | 0.085 | 0.088 | 9 | 92 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV02DETFLA-FLA5 | team_total | 0.225 | 0.255 | 0.249 | 27 | 76 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ4 | team_total | 0.460 | 0.430 | 0.436 | 44 | 58 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ3 | team_total | 0.668 | 0.640 | 0.646 | 65 | 37 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY5 | team_total | 0.223 | 0.195 | 0.200 | 21 | 82 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-BOS2 | team_total | 0.842 | 0.820 | 0.824 | 83 | 19 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-COL6 | team_total | 0.130 | 0.155 | 0.150 | 17 | 86 | no | +0.001 | OK |
| KXNHLGAME-26NOV02CGYSJ-SJ | game_winner | 0.539 | 0.515 | 0.520 | 52 | 49 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV02VGKBOS-7 | game_total | 0.432 | 0.455 | 0.450 | 46 | 55 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI5 | team_total | 0.138 | 0.115 | 0.119 | 13 | 90 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK6 | team_total | 0.065 | 0.090 | 0.084 | 11 | 93 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV02DETFLA-10 | game_total | 0.085 | 0.065 | 0.069 | 8 | 95 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV02CGYSJ-SJ5 | team_total | 0.263 | 0.235 | 0.240 | 25 | 78 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-5 | game_total | 0.781 | 0.760 | 0.764 | 77 | 25 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV02CGYSJ-CGY3 | game_spread | 0.153 | 0.165 | 0.162 | 17 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV02VGKBOS-9 | game_total | 0.172 | 0.185 | 0.182 | 19 | 82 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-8 | game_total | 0.250 | 0.270 | 0.266 | 28 | 74 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-9 | game_total | 0.173 | 0.185 | 0.183 | 19 | 82 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02CGYSJ-4 | game_total | 0.884 | 0.870 | 0.873 | 88 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-3 | game_total | 0.961 | 0.970 | 0.968 | 98 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV02COLCHI-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV02DETFLA-4 | game_total | 0.863 | 0.850 | 0.853 | 86 | 16 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV02COLCHI-CHI6 | team_total | 0.058 | 0.045 | 0.047 | 6 | 97 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VGK @ BOS | 0.587 | 0.516 | 0.173 | 0.220 | 6.12 | 6.44 | 0.957/1.004 | KXNHLTEAMTOTAL-26NOV02VGKBOS-VGK3 +0.090 |
| DET @ FLA | 0.521 | 0.562 | 0.176 | 0.213 | 6.26 | 6.41 | 1.016/1.025 | KXNHLTEAMTOTAL-26NOV02DETFLA-FLA4 +0.046 |
| COL @ CHI | 0.378 | 0.359 | 0.170 | 0.203 | 6.14 | 6.51 | 0.996/0.977 | KXNHLTOTAL-26NOV02COLCHI-7 +0.071 |
| CGY @ SJS | 0.539 | 0.565 | 0.168 | 0.218 | 6.58 | 6.45 | 1.035/1.007 | KXNHLTEAMTOTAL-26NOV02CGYSJ-CGY4 -0.032 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden McNabb: 1+ goals YES @ 5c · p 0.077 (adj 0.0665) · $2.93 · thesis VGK:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 15c · p 0.1854 (adj 0.1753) · $4.62 · thesis BOS:OFFENSE_4PLUS
- Braeden Bowman: 1+ goals YES @ 14c · p 0.1711 (adj 0.1621) · $3.79 · thesis VGK:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 63c · p 0.6997 (adj 0.681) · $20.0 · thesis FLA:SUPPRESSED
- Ben Chiarot: 1+ goals YES @ 3c · p 0.0518 (adj 0.0451) · $2.85 · thesis DET:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1257 (adj 0.113) · $4.37 · thesis FLA:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 35c · p 0.398 (adj 0.3848) · $7.44 · thesis DET:OFFENSE_4PLUS
- Patrick Kane: 2+ assists NO @ 90c · p 0.9534 (adj 0.9217) · $20.0 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 22c · p 0.2692 (adj 0.2531) · $6.81 · thesis CHI:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 78c · p 0.8154 (adj 0.8041) · $13.94 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ assists NO @ 41c · p 0.4772 (adj 0.4386) · $4.29 · thesis COL:SUPPRESSED
- Zach Whitecloud: 1+ goals YES @ 2c · p 0.0412 (adj 0.0347) · $2.61 · thesis DIFFUSE
- Ivar Stenberg: 1+ goals NO @ 77c · p 0.8228 (adj 0.8071) · $20.0 · thesis SJS:SUPPRESSED
- Michael Misa: 1+ goals YES @ 18c · p 0.2232 (adj 0.2099) · $5.71 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 24c · p 0.2825 (adj 0.2694) · $5.35 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VGK @ BOS** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.5, exp saves 24.64 (sd 6.72), pull risk 0.065
- VGK net: Carter Hart (PROJECTED) exp shots 26.12, exp saves 22.46 (sd 6.33), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brayden McNabb: 1+ assists | 0.276 | 0.130 | 24/98 | +0.023 | STANDARD |
| Mitch Marner: 1+ assists | 0.400 | 0.525 | 53/48 | +0.102 | STANDARD |
| Mitch Marner: 1+ points | 0.536 | 0.645 | 66/37 | +0.078 | STANDARD |
| Jack Eichel: 1+ assists | 0.432 | 0.530 | 54/48 | +0.071 | STANDARD |
| Hampus Lindholm: 1+ points | 0.341 | 0.245 | 26/77 | +0.067 | STANDARD |
| Jack Eichel: 2+ points | 0.237 | 0.330 | 34/68 | +0.068 | STANDARD |

**DET @ FLA** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 26.78, exp saves 23.19 (sd 6.37), pull risk 0.062
- DET net: Daniil Tarasov (CONFIRMED) exp shots 27.16, exp saves 23.26 (sd 6.52), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Daniil Tarasov: 26+ saves | 0.352 | 0.455 | 47/56 | +0.071 |  |
| Sam Reinhart: 1+ assists | 0.326 | 0.420 | 43/59 | +0.067 | STANDARD |
| Sam Reinhart: 2+ points | 0.178 | 0.255 | 27/76 | +0.049 | STANDARD |
| Sam Reinhart: 1+ goals | 0.300 | 0.375 | 38/63 | +0.053 | STANDARD |
| Sam Reinhart: 1+ points | 0.525 | 0.595 | 61/42 | +0.038 | STANDARD |
| Sam Bennett: 1+ points | 0.554 | 0.485 | 50/53 | +0.037 | STANDARD |

**COL @ CHI** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.92, exp saves 26.83 (sd 7.52), pull risk 0.09
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.7, exp saves 21.75 (sd 6.0), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.303 | 0.390 | 41/63 | +0.051 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.375 | 0.460 | 47/55 | +0.058 | STANDARD |
| Spencer Knight: 29+ saves | 0.411 | 0.495 | 51/52 | +0.052 |  |
| Connor Bedard: 1+ assists | 0.382 | 0.460 | 48/56 | +0.041 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.523 | 0.600 | 61/41 | +0.050 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.169 | 0.235 | 26/79 | +0.029 | STANDARD |

**CGY @ SJS** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.38, exp saves 24.69 (sd 6.71), pull risk 0.055
- CGY net: Dustin Wolf (CONFIRMED) exp shots 28.99, exp saves 24.73 (sd 6.99), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ points | 0.259 | 0.120 | 22/98 | +0.027 | STANDARD |
| Collin Graf: 1+ assists | 0.297 | 0.185 | 21/84 | +0.075 | STANDARD |
| Michael Kesselring: 1+ points | 0.310 | 0.200 | 27/87 | +0.026 | STANDARD |
| Collin Graf: 1+ points | 0.446 | 0.340 | 35/67 | +0.080 | STANDARD |
| Macklin Celebrini: 2+ points | 0.296 | 0.390 | 40/62 | +0.068 | STANDARD |
| Michael Misa: 1+ points | 0.475 | 0.385 | 40/63 | +0.058 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
