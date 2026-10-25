# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T20:14:19Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 4 · markets on board: 3030 · contracts joined: 923 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 823, 'OK': 71, 'NO_EDGE': 29}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 137, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 250, 'game_overtime': 4, 'player_points': 181, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ DAL | 2026-10-25T22:00:00Z | T-90m | 0.552 | 0.448 | 0.187 | 5.45 | 2.89 | 2.57 | 228 (25/203) | PROJECTED/PROBABLE |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-90m | 0.464 | 0.536 | 0.180 | 5.94 | 2.87 | 3.07 | 230 (25/205) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-3h | 0.373 | 0.627 | 0.168 | 6.00 | 2.60 | 3.40 | 237 (25/212) | PROBABLE/PROBABLE |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-3h | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.454 | 0.580 | 0.555 | 59 | 43 | no | +0.099 | OK |
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
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.335 | 0.430 | 0.410 | 44 | 58 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 16 | 85 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.416 | 0.505 | 0.487 | 51 | 50 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.231 | 0.315 | 0.297 | 32 | 69 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.565 | 0.650 | 0.634 | 66 | 36 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.837 | 0.910 | 0.898 | 92 | 10 | no | +0.057 | OK |
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
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.770 | 0.781 | 78 | 24 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.095 | 0.102 | 10 | 91 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.210 | 0.219 | 22 | 80 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.065 | 0.072 | 8 | 95 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.071 | 0.110 | 0.101 | 12 | 90 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.110 | 0.117 | 12 | 90 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.067 | 0.100 | 0.092 | 11 | 91 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.122 | 0.095 | 0.100 | 10 | 91 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5 | team_total | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.827 | 0.855 | 0.850 | 86 | 15 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.320 | 0.355 | 0.348 | 36 | 65 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3 | team_total | 0.480 | 0.445 | 0.452 | 45 | 56 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 | team_total | 0.334 | 0.365 | 0.359 | 37 | 64 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.625 | 0.631 | 63 | 38 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.780 | 0.810 | 0.804 | 82 | 20 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.937 | 0.960 | 0.956 | 97 | 5 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.143 | 0.165 | 0.160 | 17 | 84 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.730 | 0.724 | 74 | 28 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5 | team_total | 0.298 | 0.330 | 0.323 | 34 | 68 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.106 | 0.125 | 0.121 | 13 | 88 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.867 | 0.890 | 0.886 | 90 | 12 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG2 | team_total | 0.775 | 0.800 | 0.795 | 81 | 21 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-3 | game_total | 0.954 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI6 | team_total | 0.046 | 0.030 | 0.033 | 4 | 98 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4 | team_total | 0.267 | 0.240 | 0.245 | 25 | 77 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2 | team_total | 0.718 | 0.695 | 0.700 | 70 | 31 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.430 | 0.455 | 0.450 | 46 | 55 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG3 | team_total | 0.550 | 0.580 | 0.574 | 59 | 43 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH4 | team_total | 0.273 | 0.300 | 0.295 | 31 | 71 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH2 | team_total | 0.724 | 0.745 | 0.741 | 75 | 26 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL2 | team_total | 0.808 | 0.825 | 0.822 | 83 | 18 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT25MINVAN-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-8 | game_total | 0.160 | 0.175 | 0.172 | 18 | 83 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT25MTLWPG-MTL3 | game_spread | 0.180 | 0.195 | 0.192 | 20 | 81 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT25MTLWPG-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT25MTLWPG-WPG2 | game_spread | 0.249 | 0.265 | 0.262 | 27 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT25COLNSH-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-MTL4 | team_total | 0.376 | 0.395 | 0.391 | 40 | 61 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT25MINVAN-5 | game_total | 0.837 | 0.825 | 0.828 | 83 | 18 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT25NYIDAL-2 | game_total | 0.971 | 0.980 | 0.978 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH3 | team_total | 0.486 | 0.510 | 0.505 | 52 | 50 |  | -0.003 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ DAL | 0.552 | 0.549 | 0.187 | 0.221 | 5.45 | 6.00 | 0.986/0.951 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.101 |
| MTL @ WPG | 0.464 | 0.481 | 0.180 | 0.222 | 5.94 | 6.25 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.053 |
| COL @ NSH | 0.373 | 0.394 | 0.168 | 0.214 | 6.00 | 6.46 | 0.991/0.972 | KXNHLTOTAL-26OCT25COLNSH-7 +0.079 |
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Brayden Schenn: 1+ goals YES @ 16c · p 0.2276 (adj 0.2094) · $12.04 · thesis NYI:OFFENSE_4PLUS
- Victor Eklund: 1+ goals YES @ 14c · p 0.2016 (adj 0.1825) · $9.04 · thesis NYI:OFFENSE_4PLUS
- Kyle Palmieri: 1+ goals YES @ 20c · p 0.2401 (adj 0.2288) · $5.75 · thesis NYI:OFFENSE_4PLUS
- Victor Eklund: 1+ assists NO @ 75c · p 0.8197 (adj 0.7773) · $20.0 · thesis NYI:SUPPRESSED
- Alexandre Carrier: 1+ goals YES @ 4c · p 0.0677 (adj 0.0595) · $3.68 · thesis MTL:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1698 (adj 0.1524) · $3.67 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3351 (adj 0.3226) · $6.21 · thesis WPG:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ assists NO @ 41c · p 0.4958 (adj 0.4479) · $6.77 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 53c · p 0.609 (adj 0.567) · $4.52 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7324 (adj 0.6937) · $6.88 · thesis GAME:TIGHT
- Cale Makar: 1+ goals NO @ 78c · p 0.8146 (adj 0.8047) · $11.73 · thesis COL:SUPPRESSED
- Matt Boldy: 1+ goals NO @ 58c · p 0.6593 (adj 0.6382) · $15.0 · thesis MIN:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2236 (adj 0.2002) · $7.2 · thesis VAN:OFFENSE_4PLUS
- Kirill Kaprizov: 2+ goals NO @ 87c · p 0.9148 (adj 0.9011) · $15.0 · thesis MIN:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2315 (adj 0.2174) · $6.8 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYI @ DAL** · priced 172/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.18 (sd 6.11), pull risk 0.047
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.22, exp saves 22.68 (sd 6.22), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.272 | 0.115 | 21/98 | +0.050 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.232 | 0.115 | 17/94 | +0.052 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.426 | 0.520 | 53/49 | +0.067 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.446 | 0.540 | 55/47 | +0.066 | STANDARD |
| Mikko Rantanen: 2+ points | 0.238 | 0.330 | 34/68 | +0.067 | STANDARD |
| Miro Heiskanen: 1+ points | 0.490 | 0.575 | 59/44 | +0.053 | STANDARD |

**MTL @ WPG** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.39), pull risk 0.059
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.54, exp saves 23.94 (sd 6.53), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Stuart Skinner: 26+ saves | 0.331 | 0.460 | 51/59 | +0.062 |  |
| Dylan Samberg: 1+ assists | 0.265 | 0.145 | 23/94 | +0.023 | STANDARD |
| Kaiden Guhle: 1+ assists | 0.236 | 0.130 | 24/98 | -0.017 | STANDARD |
| Oliver Kapanen: 1+ points | 0.366 | 0.455 | 46/55 | +0.066 | STANDARD |
| Zachary Bolduc: 1+ points | 0.407 | 0.330 | 37/71 | +0.020 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.278 | 0.205 | 23/82 | +0.035 | STANDARD |

**COL @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROBABLE) exp shots 32.01, exp saves 27.18 (sd 7.46), pull risk 0.085
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.47, exp saves 23.19 (sd 6.3), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| Cale Makar: 1+ assists | 0.459 | 0.560 | 57/45 | +0.073 | STANDARD |
| Cale Makar: 2+ points | 0.193 | 0.290 | 31/73 | +0.063 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Scott Wedgewood: 22+ saves | 0.608 | 0.525 | 53/48 | +0.060 |  |
| Mavrik Bourque: 1+ assists | 0.134 | 0.215 | 24/81 | +0.045 | STANDARD |

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Liam Ohgren: 1+ points | 0.381 | 0.165 | 31/98 | +0.056 | STANDARD |
| Liam Ohgren: 1+ assists | 0.264 | 0.115 | 21/98 | +0.042 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.268 | 0.415 | 43/60 | +0.115 | STANDARD |
| Brendan Gallagher: 1+ points | 0.271 | 0.130 | 24/98 | +0.018 | STANDARD |
| Yakov Trenin: 1+ points | 0.305 | 0.165 | 27/94 | +0.021 | STANDARD |
| Matt Boldy: 2+ points | 0.241 | 0.375 | 39/64 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
