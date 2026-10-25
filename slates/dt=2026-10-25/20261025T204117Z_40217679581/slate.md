# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T20:41:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 4 · markets on board: 3030 · contracts joined: 923 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 823, 'OK': 76, 'NO_EDGE': 24}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 137, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 250, 'game_overtime': 4, 'player_points': 181, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ DAL | 2026-10-25T22:00:00Z | T-60m | 0.552 | 0.448 | 0.187 | 5.45 | 2.89 | 2.57 | 228 (25/203) | PROJECTED/PROBABLE |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-90m | 0.454 | 0.546 | 0.178 | 5.86 | 2.79 | 3.07 | 230 (25/205) | PROJECTED/CONFIRMED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-3h | 0.373 | 0.627 | 0.168 | 6.00 | 2.60 | 3.40 | 237 (25/212) | PROBABLE/PROBABLE |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-3h | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.454 | 0.585 | 0.559 | 60 | 43 | no | +0.099 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.257 | 0.365 | 0.342 | 38 | 65 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.673 | 0.770 | 0.752 | 78 | 24 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.417 | 0.320 | 0.339 | 33 | 69 | yes | +0.072 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.552 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.448 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.186 | 0.275 | 0.255 | 28 | 73 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.533 | 0.625 | 0.607 | 63 | 38 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.750 | 0.835 | 0.820 | 84 | 17 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.627 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.256 | 0.345 | 0.326 | 35 | 66 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.335 | 0.425 | 0.406 | 43 | 58 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.837 | 0.915 | 0.903 | 92 | 9 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 16 | 85 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.416 | 0.505 | 0.487 | 51 | 50 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.231 | 0.315 | 0.297 | 32 | 69 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.565 | 0.650 | 0.634 | 66 | 36 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.223 | 0.300 | 0.283 | 31 | 71 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.552 | 0.625 | 0.611 | 63 | 38 | no | +0.051 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.448 | 0.375 | 0.389 | 38 | 63 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.119 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.855 | 0.915 | 0.905 | 92 | 9 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.783 | 0.850 | 0.838 | 86 | 16 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.163 | 0.230 | 0.215 | 24 | 78 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.038 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.351 | 0.295 | 0.306 | 30 | 71 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.670 | 0.725 | 0.715 | 73 | 28 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.775 | 0.785 | 78 | 23 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 | team_total | 0.316 | 0.365 | 0.355 | 37 | 64 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.095 | 0.102 | 10 | 91 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.210 | 0.219 | 22 | 80 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.065 | 0.072 | 8 | 95 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.071 | 0.110 | 0.101 | 12 | 90 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.110 | 0.117 | 12 | 90 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG2 | team_total | 0.756 | 0.800 | 0.792 | 81 | 21 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.540 | 0.530 | 55 | 47 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.821 | 0.855 | 0.849 | 86 | 15 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.727 | 0.765 | 0.758 | 77 | 24 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.735 | 0.728 | 74 | 27 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.067 | 0.100 | 0.092 | 11 | 91 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG3 | team_total | 0.536 | 0.580 | 0.571 | 59 | 43 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.134 | 0.165 | 0.158 | 17 | 84 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.122 | 0.095 | 0.100 | 10 | 91 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5 | team_total | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.320 | 0.355 | 0.348 | 36 | 65 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3 | team_total | 0.480 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-7 | game_total | 0.393 | 0.425 | 0.419 | 43 | 58 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.625 | 0.631 | 63 | 38 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.780 | 0.810 | 0.804 | 82 | 20 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.937 | 0.960 | 0.956 | 97 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-6 | game_total | 0.505 | 0.535 | 0.529 | 54 | 47 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5 | team_total | 0.298 | 0.330 | 0.323 | 34 | 68 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.106 | 0.125 | 0.121 | 13 | 88 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.867 | 0.890 | 0.886 | 90 | 12 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-3 | game_total | 0.952 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG2 | game_spread | 0.241 | 0.265 | 0.260 | 27 | 74 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-8 | game_total | 0.214 | 0.235 | 0.231 | 24 | 77 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG5 | team_total | 0.156 | 0.180 | 0.175 | 19 | 83 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI6 | team_total | 0.046 | 0.030 | 0.033 | 4 | 98 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4 | team_total | 0.267 | 0.240 | 0.245 | 25 | 77 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2 | team_total | 0.718 | 0.695 | 0.700 | 70 | 31 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL2 | team_total | 0.807 | 0.825 | 0.821 | 83 | 18 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.430 | 0.455 | 0.450 | 46 | 55 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH4 | team_total | 0.273 | 0.300 | 0.295 | 31 | 71 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH2 | team_total | 0.724 | 0.745 | 0.741 | 75 | 26 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT25MINVAN-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-2 | game_total | 0.979 | 0.985 | 0.984 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT25NYIDAL-8 | game_total | 0.160 | 0.175 | 0.172 | 18 | 83 |  | -0.000 | NO_EDGE |
| KXNHLGAME-26OCT25MTLWPG-MTL | game_winner | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT25MTLWPG-WPG | game_winner | 0.454 | 0.475 | 0.471 | 48 | 53 |  | -0.001 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ DAL | 0.552 | 0.549 | 0.187 | 0.221 | 5.45 | 6.00 | 0.986/0.951 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.101 |
| MTL @ WPG | 0.454 | 0.484 | 0.178 | 0.222 | 5.86 | 6.28 | 1.001/0.983 | KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 +0.072 |
| COL @ NSH | 0.373 | 0.394 | 0.168 | 0.214 | 6.00 | 6.46 | 0.991/0.972 | KXNHLTOTAL-26OCT25COLNSH-7 +0.079 |
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden Schenn: 1+ goals YES @ 16c · p 0.2276 (adj 0.2094) · $12.07 · thesis NYI:OFFENSE_4PLUS
- Victor Eklund: 1+ goals YES @ 15c · p 0.2016 (adj 0.1875) · $7.93 · thesis NYI:OFFENSE_4PLUS
- Victor Eklund: 1+ assists NO @ 75c · p 0.8197 (adj 0.7823) · $20.0 · thesis NYI:SUPPRESSED
- Kyle Palmieri: 1+ goals YES @ 20c · p 0.2401 (adj 0.2288) · $5.73 · thesis NYI:OFFENSE_4PLUS
- Alexandre Carrier: 1+ goals YES @ 4c · p 0.0634 (adj 0.0563) · $2.98 · thesis MTL:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1716 (adj 0.16) · $5.81 · thesis WPG:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 4c · p 0.0609 (adj 0.0544) · $2.61 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3396 (adj 0.326) · $7.25 · thesis WPG:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 79c · p 0.8662 (adj 0.8206) · $20.0 · thesis NSH:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 53c · p 0.609 (adj 0.567) · $6.73 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7324 (adj 0.6937) · $8.07 · thesis GAME:TIGHT
- Adam Edstrom: 1+ goals YES @ 11c · p 0.1346 (adj 0.1272) · $2.4 · thesis NSH:WINS_BY_2PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2236 (adj 0.2064) · $8.18 · thesis VAN:OFFENSE_4PLUS
- Kirill Kaprizov: 2+ goals NO @ 86c · p 0.9148 (adj 0.8998) · $15.0 · thesis MIN:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 17c · p 0.2315 (adj 0.2149) · $7.89 · thesis VAN:OFFENSE_4PLUS
- Matt Boldy: 1+ goals NO @ 58c · p 0.6593 (adj 0.6382) · $15.0 · thesis MIN:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYI @ DAL** · priced 172/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.18 (sd 6.11), pull risk 0.047
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.22, exp saves 22.68 (sd 6.22), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.272 | 0.165 | 20/87 | +0.060 | STANDARD |
| Miro Heiskanen: 1+ points | 0.490 | 0.585 | 60/43 | +0.063 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.426 | 0.520 | 53/49 | +0.067 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.446 | 0.540 | 55/47 | +0.066 | STANDARD |
| Mikko Rantanen: 2+ points | 0.238 | 0.330 | 34/68 | +0.067 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.232 | 0.140 | 16/88 | +0.063 | STANDARD |

**MTL @ WPG** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.92 (sd 6.37), pull risk 0.062
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.54, exp saves 23.94 (sd 6.52), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Stuart Skinner: 26+ saves | 0.335 | 0.460 | 51/59 | +0.058 |  |
| Kaiden Guhle: 1+ assists | 0.226 | 0.125 | 23/98 | -0.017 | STANDARD |
| Dylan Samberg: 1+ assists | 0.266 | 0.165 | 22/89 | +0.033 | STANDARD |
| Oliver Kapanen: 1+ points | 0.369 | 0.455 | 46/55 | +0.063 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.277 | 0.205 | 23/82 | +0.035 | STANDARD |
| Zachary Bolduc: 1+ points | 0.404 | 0.335 | 36/69 | +0.028 | STANDARD |

**COL @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROBABLE) exp shots 32.01, exp saves 27.18 (sd 7.46), pull risk 0.085
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.47, exp saves 23.19 (sd 6.3), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| Cale Makar: 1+ assists | 0.459 | 0.560 | 57/45 | +0.073 | STANDARD |
| Cale Makar: 2+ points | 0.193 | 0.290 | 31/73 | +0.063 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.134 | 0.225 | 24/79 | +0.065 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.152 | 0.235 | 26/79 | +0.047 | STANDARD |

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.381 | 0.165 | 31/98 | +0.056 | STANDARD |
| Liam Ohgren: 1+ assists | 0.264 | 0.115 | 21/98 | +0.042 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.268 | 0.415 | 43/60 | +0.115 | STANDARD |
| Matt Boldy: 2+ points | 0.241 | 0.375 | 39/64 | +0.103 | STANDARD |
| Quinn Hughes: 2+ points | 0.221 | 0.355 | 37/66 | +0.103 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.650 | 66/36 | +0.105 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
