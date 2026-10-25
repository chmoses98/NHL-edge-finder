# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T11:34:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2646 · contracts joined: 734 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 609, 'OK': 83, 'NO_EDGE': 42}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 80, 'game_early_goal': 5, 'first_goal': 109, 'game_winner': 10, 'player_goals': 186, 'game_overtime': 5, 'player_points': 104, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 2026-10-25T19:00:00Z | T-6h | 0.495 | 0.505 | 0.186 | 6.04 | 3.00 | 3.03 | 221 (25/196) | PROJECTED/CONFIRMED |
| NYI @ DAL | 2026-10-25T22:00:00Z | T-6h | 0.566 | 0.434 | 0.188 | 5.52 | 2.95 | 2.56 | 211 (25/186) | PROJECTED/PROJECTED |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-6h | 0.464 | 0.536 | 0.180 | 5.94 | 2.87 | 3.07 | 200 (25/175) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-12h | 0.382 | 0.618 | 0.170 | 6.08 | 2.66 | 3.41 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-12h | 0.460 | 0.540 | 0.170 | 6.75 | 3.24 | 3.52 | 51 (25/26) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT25FLACHI-FLA2 | game_spread | 0.283 | 0.405 | 0.379 | 41 | 60 | no | +0.100 | OK |
| KXNHLGAME-26OCT25FLACHI-CHI | game_winner | 0.495 | 0.375 | 0.398 | 38 | 63 | yes | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA4 | team_total | 0.373 | 0.490 | 0.466 | 50 | 52 | no | +0.089 | OK |
| KXNHLGAME-26OCT25FLACHI-FLA | game_winner | 0.505 | 0.615 | 0.594 | 62 | 39 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA3 | game_spread | 0.169 | 0.275 | 0.251 | 28 | 73 | no | +0.087 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.457 | 0.575 | 0.552 | 59 | 44 | no | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 | team_total | 0.590 | 0.705 | 0.683 | 72 | 31 | no | +0.085 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.540 | 0.635 | 0.617 | 64 | 37 | no | +0.074 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.460 | 0.365 | 0.383 | 37 | 64 | yes | +0.074 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.330 | 0.425 | 0.405 | 43 | 58 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.252 | 0.345 | 0.325 | 35 | 66 | no | +0.073 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.541 | 0.635 | 0.617 | 64 | 37 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA5 | team_total | 0.194 | 0.295 | 0.273 | 31 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.264 | 0.365 | 0.343 | 38 | 65 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.209 | 0.295 | 0.276 | 30 | 71 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.428 | 0.515 | 0.497 | 52 | 49 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.419 | 0.325 | 0.343 | 34 | 69 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.350 | 0.440 | 0.421 | 45 | 57 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI2 | game_spread | 0.273 | 0.195 | 0.209 | 20 | 81 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.675 | 0.765 | 0.748 | 78 | 25 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA2 | team_total | 0.802 | 0.880 | 0.867 | 89 | 13 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.628 | 0.540 | 0.558 | 55 | 47 | yes | +0.060 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.392 | 0.475 | 0.458 | 48 | 53 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.196 | 0.275 | 0.258 | 28 | 73 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.160 | 0.173 | 17 | 85 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.755 | 0.825 | 0.812 | 83 | 18 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.243 | 0.320 | 0.304 | 33 | 69 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.844 | 0.910 | 0.899 | 92 | 10 | no | +0.050 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.434 | 0.360 | 0.374 | 37 | 65 | yes | +0.048 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.566 | 0.640 | 0.626 | 65 | 37 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.258 | 0.185 | 0.198 | 20 | 83 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.327 | 0.395 | 0.381 | 40 | 61 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.124 | 0.195 | 0.179 | 21 | 82 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.582 | 0.650 | 0.637 | 66 | 36 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.853 | 0.905 | 0.896 | 91 | 10 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.168 | 0.225 | 0.213 | 23 | 78 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA6 | team_total | 0.082 | 0.145 | 0.130 | 16 | 87 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.793 | 0.850 | 0.840 | 86 | 16 | no | +0.037 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.618 | 0.675 | 0.664 | 68 | 33 | no | +0.037 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.382 | 0.325 | 0.336 | 33 | 68 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.111 | 0.060 | 0.068 | 7 | 95 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI3 | game_spread | 0.163 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT25FLACHI-6 | game_total | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.824 | 0.770 | 0.782 | 78 | 24 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4 | team_total | 0.364 | 0.315 | 0.325 | 32 | 69 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.677 | 0.730 | 0.720 | 74 | 28 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.219 | 0.170 | 0.179 | 18 | 84 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.156 | 0.110 | 0.118 | 12 | 90 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.078 | 0.115 | 0.106 | 12 | 89 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT25FLACHI-4 | game_total | 0.839 | 0.875 | 0.868 | 88 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI3 | team_total | 0.580 | 0.530 | 0.540 | 54 | 48 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25FLACHI-7 | game_total | 0.420 | 0.470 | 0.460 | 48 | 54 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI2 | team_total | 0.794 | 0.755 | 0.763 | 76 | 25 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.072 | 0.110 | 0.101 | 12 | 90 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.441 | 0.485 | 0.476 | 49 | 52 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.191 | 0.155 | 0.162 | 16 | 85 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.537 | 0.495 | 0.503 | 50 | 51 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.252 | 0.210 | 0.218 | 22 | 80 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI6 | team_total | 0.084 | 0.055 | 0.060 | 6 | 95 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.783 | 0.820 | 0.813 | 83 | 19 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.341 | 0.300 | 0.308 | 31 | 71 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.338 | 0.375 | 0.367 | 38 | 63 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT25FLACHI-5 | game_total | 0.754 | 0.790 | 0.783 | 80 | 22 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT25MINVAN-5 | game_total | 0.833 | 0.805 | 0.811 | 81 | 20 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.110 | 0.135 | 0.130 | 14 | 87 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.129 | 0.100 | 0.105 | 11 | 91 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-10 | game_total | 0.044 | 0.065 | 0.060 | 7 | 94 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25FLACHI-8 | game_total | 0.235 | 0.270 | 0.263 | 28 | 74 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.117 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.862 | 0.885 | 0.881 | 89 | 12 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.646 | 0.610 | 0.617 | 62 | 40 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI5 | team_total | 0.189 | 0.155 | 0.161 | 17 | 86 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.938 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.959 | 0.980 | 0.977 | 99 | 3 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.143 | 0.165 | 0.160 | 17 | 84 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25FLACHI-9 | game_total | 0.164 | 0.190 | 0.184 | 20 | 82 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.477 | 0.515 | 0.507 | 53 | 50 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI6 | team_total | 0.048 | 0.035 | 0.037 | 4 | 97 | yes | +0.005 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 0.495 | 0.474 | 0.186 | 0.223 | 6.04 | 6.28 | 1.003/0.991 | KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 +0.047 |
| NYI @ DAL | 0.566 | 0.549 | 0.188 | 0.222 | 5.52 | 6.01 | 0.986/0.956 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.086 |
| MTL @ WPG | 0.464 | 0.481 | 0.180 | 0.222 | 5.94 | 6.25 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.053 |
| COL @ NSH | 0.382 | 0.394 | 0.170 | 0.213 | 6.08 | 6.47 | 0.994/0.973 | KXNHLTOTAL-26OCT25COLNSH-7 +0.067 |
| MIN @ VAN | 0.460 | 0.522 | 0.170 | 0.214 | 6.75 | 6.50 | 1.025/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.072 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Schwindt: 1+ goals YES @ 10c · p 0.1511 (adj 0.1283) · $5.85 · thesis FLA:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6953 (adj 0.6765) · $19.29 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 73c · p 0.809 (adj 0.767) · $20.0 · thesis CHI:WINS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1584 (adj 0.1451) · $4.38 · thesis CHI:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1662 (adj 0.1522) · $3.19 · thesis NYI:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 73c · p 0.7956 (adj 0.7603) · $13.05 · thesis GAME:TIGHT
- New York I over 3.5 goals scored YES @ 26c · p 0.33 (adj 0.29) · $2.26 · thesis NYI:OFFENSE_4PLUS
- Bo Horvat: 1+ goals YES @ 28c · p 0.321 (adj 0.3058) · $2.58 · thesis NYI:OFFENSE_4PLUS
- Colorado wins by over 1.5 goals NO @ 53c · p 0.6119 (adj 0.5685) · $7.59 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7335 (adj 0.6943) · $7.62 · thesis GAME:TIGHT
- Vancouver wins by over 2.5 goals YES @ 12c · p 0.1986 (adj 0.1543) · $3.71 · thesis VAN:WINS_BY_2PLUS
- Minnesota wins by over 1.5 goals NO @ 58c · p 0.7386 (adj 0.6323) · $15.82 · thesis VAN:WINS
- Vancouver over 4.5 goals scored YES @ 17c · p 0.2505 (adj 0.2052) · $2.16 · thesis VAN:OFFENSE_4PLUS
- Minnesota wins by over 2.5 goals NO @ 71c · p 0.8322 (adj 0.7495) · $5.74 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CHI** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.49, exp saves 24.39 (sd 6.74), pull risk 0.066
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.46, exp saves 21.17 (sd 6.11), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.482 | 0.605 | 63/42 | +0.081 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.325 | 0.440 | 45/57 | +0.088 | STANDARD |
| Sam Reinhart: 1+ assists | 0.300 | 0.410 | 43/61 | +0.073 | STANDARD |
| Patrick Kane: 1+ assists | 0.319 | 0.425 | 44/59 | +0.074 | STANDARD |
| Brady Tkachuk: 1+ points | 0.531 | 0.635 | 66/39 | +0.062 | STANDARD |
| Cole Schwindt: 1+ goals | 0.151 | 0.060 | 10/98 | +0.045 | STANDARD |

**NYI @ DAL** · priced 155/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.15 (sd 6.06), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.22, exp saves 22.6 (sd 6.21), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ points | 0.607 | 0.475 | 73/78 | -0.137 | STANDARD |
| Brayden Schenn: 1+ goals | 0.241 | 0.125 | 17/92 | +0.061 | STANDARD |
| Jason Robertson: 2+ points | 0.275 | 0.170 | 32/98 | -0.061 | STANDARD |
| David Perron: 1+ goals | 0.165 | 0.075 | 13/98 | +0.027 | STANDARD |
| Kyle Palmieri: 1+ goals | 0.247 | 0.165 | 21/88 | +0.025 | STANDARD |
| Miro Heiskanen: 1+ points | 0.495 | 0.575 | 61/46 | +0.027 | STANDARD |

**MTL @ WPG** · priced 145/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.39), pull risk 0.059
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.54, exp saves 23.94 (sd 6.53), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Connor: 2+ points | 0.282 | 0.175 | 33/98 | -0.063 | STANDARD |
| Kyle Connor: 1+ goals | 0.391 | 0.285 | 40/83 | -0.026 | STANDARD |
| Mark Scheifele: 2+ points | 0.277 | 0.175 | 33/98 | -0.068 | STANDARD |
| Josh Anderson: 1+ goals | 0.212 | 0.110 | 16/94 | +0.042 | STANDARD |
| Chris Kreider: 1+ goals | 0.217 | 0.120 | 22/98 | -0.015 | STANDARD |
| Alex Iafallo: 1+ goals | 0.170 | 0.075 | 13/98 | +0.032 | STANDARD |

**COL @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 32.01, exp saves 27.22 (sd 7.51), pull risk 0.086
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.47, exp saves 23.17 (sd 6.3), pull risk 0.053

**MIN @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.99, exp saves 26.89 (sd 7.1), pull risk 0.062
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.19 (sd 6.24), pull risk 0.067

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
