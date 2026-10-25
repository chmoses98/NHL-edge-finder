# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T22:32:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 3 · markets on board: 2835 · contracts joined: 719 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 644, 'OK': 56, 'NO_EDGE': 19}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 112, 'game_early_goal': 3, 'first_goal': 109, 'game_winner': 6, 'player_goals': 188, 'game_overtime': 3, 'player_points': 151, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ WPG | 2026-10-25T23:00:00Z | T-10m | 0.454 | 0.546 | 0.178 | 5.86 | 2.79 | 3.07 | 254 (25/229) | PROJECTED/CONFIRMED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-60m | 0.373 | 0.627 | 0.168 | 6.00 | 2.60 | 3.40 | 237 (25/212) | PROBABLE/PROBABLE |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-3h | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.454 | 0.580 | 0.555 | 59 | 43 | no | +0.099 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.257 | 0.360 | 0.338 | 37 | 65 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.673 | 0.770 | 0.752 | 78 | 24 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.417 | 0.320 | 0.339 | 33 | 69 | yes | +0.072 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.552 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.448 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.627 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 16 | 85 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.231 | 0.315 | 0.297 | 32 | 69 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.533 | 0.615 | 0.599 | 62 | 39 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.750 | 0.830 | 0.816 | 84 | 18 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.256 | 0.335 | 0.318 | 34 | 67 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.416 | 0.495 | 0.479 | 50 | 51 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.223 | 0.300 | 0.283 | 31 | 71 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.837 | 0.900 | 0.889 | 91 | 11 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.119 | 0.175 | 0.162 | 18 | 83 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.855 | 0.910 | 0.901 | 92 | 10 | no | +0.039 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.038 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.351 | 0.295 | 0.306 | 30 | 71 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.770 | 0.781 | 78 | 24 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.727 | 0.775 | 0.766 | 78 | 23 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 | team_total | 0.316 | 0.365 | 0.355 | 37 | 64 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG3 | team_total | 0.536 | 0.590 | 0.579 | 60 | 42 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.095 | 0.102 | 10 | 91 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.210 | 0.219 | 22 | 80 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.065 | 0.072 | 8 | 95 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.071 | 0.110 | 0.101 | 12 | 90 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.115 | 0.121 | 12 | 89 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG2 | team_total | 0.756 | 0.800 | 0.792 | 81 | 21 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.821 | 0.860 | 0.853 | 87 | 15 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-6 | game_total | 0.505 | 0.545 | 0.537 | 55 | 46 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.735 | 0.728 | 74 | 27 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.867 | 0.895 | 0.890 | 90 | 11 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.134 | 0.170 | 0.162 | 18 | 84 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG2 | game_spread | 0.241 | 0.275 | 0.268 | 28 | 73 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.510 | 0.518 | 52 | 50 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-7 | game_total | 0.393 | 0.425 | 0.419 | 43 | 58 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.625 | 0.631 | 63 | 38 | yes | +0.009 | OK |
| KXNHLGAME-26OCT25MTLWPG-MTL | game_winner | 0.546 | 0.515 | 0.521 | 52 | 49 | yes | +0.009 | OK |
| KXNHLGAME-26OCT25MTLWPG-WPG | game_winner | 0.454 | 0.485 | 0.479 | 49 | 52 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5 | team_total | 0.298 | 0.330 | 0.323 | 34 | 68 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-3 | game_total | 0.952 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG5 | team_total | 0.156 | 0.185 | 0.179 | 20 | 83 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-MTL2 | game_spread | 0.318 | 0.295 | 0.300 | 30 | 71 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL2 | team_total | 0.807 | 0.825 | 0.821 | 83 | 18 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH2 | team_total | 0.724 | 0.745 | 0.741 | 75 | 26 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT25MINVAN-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG6 | team_total | 0.065 | 0.080 | 0.077 | 9 | 93 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-2 | game_total | 0.979 | 0.985 | 0.984 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT25COLNSH-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-5 | game_total | 0.837 | 0.825 | 0.828 | 83 | 18 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH3 | team_total | 0.486 | 0.510 | 0.505 | 52 | 50 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-4 | game_total | 0.902 | 0.890 | 0.893 | 90 | 12 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT25MTLWPG-9 | game_total | 0.146 | 0.155 | 0.153 | 16 | 85 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT25MTLWPG-8 | game_total | 0.214 | 0.230 | 0.227 | 24 | 78 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH5 | team_total | 0.129 | 0.135 | 0.134 | 14 | 87 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT25MTLWPG-10 | game_total | 0.063 | 0.070 | 0.069 | 8 | 94 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH4 | team_total | 0.273 | 0.285 | 0.283 | 29 | 72 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL4 | team_total | 0.381 | 0.400 | 0.396 | 41 | 61 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL6 | team_total | 0.087 | 0.085 | 0.085 | 9 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-3 | game_total | 0.978 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT25COLNSH-NSH3 | game_spread | 0.095 | 0.095 | 0.095 | 10 | 91 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT25MTLWPG-MTL3 | game_spread | 0.192 | 0.195 | 0.194 | 20 | 81 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH6 | team_total | 0.051 | 0.050 | 0.050 | 6 | 96 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL3 | team_total | 0.602 | 0.610 | 0.608 | 62 | 40 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL5 | team_total | 0.199 | 0.200 | 0.200 | 21 | 81 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN6 | team_total | 0.152 | 0.155 | 0.154 | 17 | 86 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT25MTLWPG-MTL | period_winner |  | 0.330 |  | 35 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT25MTLWPG-TIE | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT25MTLWPG-WPG | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT25MTLWPG-MTL2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT25MTLWPG-WPG2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ WPG | 0.454 | 0.484 | 0.178 | 0.222 | 5.86 | 6.28 | 1.001/0.983 | KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 +0.072 |
| COL @ NSH | 0.373 | 0.394 | 0.168 | 0.214 | 6.00 | 6.46 | 0.991/0.972 | KXNHLTOTAL-26OCT25COLNSH-7 +0.079 |
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Alexandre Carrier: 1+ goals YES @ 4c · p 0.0636 (adj 0.0565) · $3.05 · thesis MTL:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1716 (adj 0.16) · $5.88 · thesis WPG:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 89c · p 0.9208 (adj 0.9106) · $20.0 · thesis WPG:SUPPRESSED
- Mark Scheifele: 1+ goals YES @ 30c · p 0.3396 (adj 0.3285) · $4.68 · thesis WPG:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 77c · p 0.8146 (adj 0.8022) · $19.28 · thesis COL:SUPPRESSED
- Mavrik Bourque: 1+ assists NO @ 77c · p 0.8662 (adj 0.8004) · $19.28 · thesis NSH:SUPPRESSED
- Adam Edstrom: 1+ goals YES @ 11c · p 0.1346 (adj 0.1272) · $2.49 · thesis NSH:WINS_BY_2PLUS
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7324 (adj 0.6987) · $8.94 · thesis GAME:TIGHT
- Kirill Kaprizov: 2+ goals NO @ 85c · p 0.9148 (adj 0.8973) · $15.0 · thesis MIN:SUPPRESSED
- Matt Boldy: 1+ goals NO @ 58c · p 0.6593 (adj 0.6382) · $15.0 · thesis MIN:SUPPRESSED
- Minnesota wins by over 1.5 goals NO @ 58c · p 0.7313 (adj 0.6297) · $15.39 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ WPG** · priced 199/203 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.92 (sd 6.37), pull risk 0.062
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.54, exp saves 23.94 (sd 6.52), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kaiden Guhle: 1+ assists | 0.224 | 0.120 | 22/98 | -0.008 | STANDARD |
| Dylan DeMelo: 1+ assists | 0.211 | 0.110 | 20/98 | -0.001 | STANDARD |
| Stuart Skinner: 26+ saves | 0.335 | 0.435 | 45/58 | +0.068 |  |
| Dylan Samberg: 1+ points | 0.311 | 0.215 | 25/82 | +0.048 | STANDARD |
| Dylan Samberg: 1+ assists | 0.266 | 0.175 | 22/87 | +0.033 | STANDARD |
| Oliver Kapanen: 1+ points | 0.371 | 0.455 | 46/55 | +0.062 | STANDARD |

**COL @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROBABLE) exp shots 32.01, exp saves 27.18 (sd 7.46), pull risk 0.085
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.47, exp saves 23.19 (sd 6.3), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| Cale Makar: 2+ points | 0.193 | 0.295 | 31/72 | +0.073 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.134 | 0.235 | 24/77 | +0.084 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Cale Makar: 1+ assists | 0.459 | 0.555 | 57/46 | +0.063 | STANDARD |
| Cale Makar: 1+ points | 0.562 | 0.655 | 66/35 | +0.072 | STANDARD |

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.268 | 0.420 | 44/60 | +0.115 | STANDARD |
| Liam Ohgren: 1+ assists | 0.264 | 0.115 | 21/98 | +0.042 | STANDARD |
| Matt Boldy: 2+ points | 0.241 | 0.375 | 39/64 | +0.103 | STANDARD |
| Quinn Hughes: 2+ points | 0.221 | 0.355 | 37/66 | +0.103 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.650 | 66/36 | +0.105 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.628 | 0.755 | 77/26 | +0.099 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
