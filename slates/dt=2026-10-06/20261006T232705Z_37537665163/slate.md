# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T23:27:05Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 4 · markets on board: 3592 · contracts joined: 814 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 714, 'OK': 63, 'NO_EDGE': 37}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 99, 'game_early_goal': 4, 'first_goal': 140, 'game_winner': 8, 'player_goals': 244, 'game_overtime': 4, 'player_points': 123, 'goalie_saves': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ NYR | 2026-10-06T23:30:00Z | T-<10m | 0.629 | 0.371 | 0.175 | 5.97 | 3.40 | 2.58 | 207 (25/182) | CONFIRMED/CONFIRMED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-30m | 0.426 | 0.574 | 0.182 | 5.78 | 2.67 | 3.12 | 199 (25/174) | PROBABLE/CONFIRMED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-90m | 0.503 | 0.497 | 0.174 | 6.38 | 3.21 | 3.17 | 198 (25/173) | PROBABLE/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-90m | 0.557 | 0.443 | 0.172 | 6.25 | 3.31 | 2.94 | 210 (25/185) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.503 | 0.375 | 0.400 | 38 | 63 | yes | +0.107 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.497 | 0.615 | 0.592 | 62 | 39 | no | +0.097 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.286 | 0.385 | 0.364 | 39 | 62 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.624 | 0.525 | 0.545 | 53 | 48 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.172 | 0.265 | 0.244 | 27 | 74 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.291 | 0.205 | 0.221 | 21 | 80 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.412 | 0.315 | 0.334 | 33 | 70 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.229 | 0.150 | 0.164 | 16 | 86 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.651 | 0.575 | 0.591 | 58 | 43 | yes | +0.054 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.557 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.434 | 0.365 | 0.378 | 37 | 64 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.181 | 0.125 | 0.135 | 13 | 88 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.240 | 0.300 | 0.287 | 31 | 71 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.620 | 0.675 | 0.664 | 68 | 33 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.106 | 0.060 | 0.067 | 7 | 95 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.211 | 0.165 | 0.173 | 17 | 84 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.823 | 0.765 | 0.778 | 78 | 25 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI3 | game_spread | 0.095 | 0.135 | 0.126 | 14 | 87 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT06STLCHI-6 | game_total | 0.490 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLGAME-26OCT06NYINYR-NYI | game_winner | 0.371 | 0.415 | 0.406 | 42 | 59 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.820 | 0.855 | 0.848 | 86 | 15 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI2 | game_spread | 0.177 | 0.215 | 0.207 | 22 | 79 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.352 | 0.395 | 0.386 | 40 | 61 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-8 | game_total | 0.284 | 0.245 | 0.253 | 25 | 76 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT06STLCHI-5 | game_total | 0.717 | 0.755 | 0.748 | 76 | 25 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.218 | 0.255 | 0.247 | 26 | 75 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.241 | 0.195 | 0.204 | 21 | 82 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.115 | 0.080 | 0.086 | 9 | 93 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.404 | 0.445 | 0.437 | 45 | 56 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.840 | 0.795 | 0.805 | 81 | 22 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR3 | game_spread | 0.259 | 0.225 | 0.232 | 23 | 78 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.567 | 0.605 | 0.597 | 61 | 40 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT06FLALA-9 | game_total | 0.185 | 0.155 | 0.161 | 16 | 85 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT06STLCHI-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR2 | game_spread | 0.402 | 0.365 | 0.372 | 37 | 64 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT06STLCHI-7 | game_total | 0.378 | 0.415 | 0.408 | 42 | 59 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR4 | team_total | 0.451 | 0.415 | 0.422 | 42 | 59 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT06FLALA-10 | game_total | 0.089 | 0.065 | 0.069 | 7 | 94 | yes | +0.014 | OK |
| KXNHLSPREAD-26OCT06STLCHI-CHI3 | game_spread | 0.118 | 0.145 | 0.139 | 15 | 86 | no | +0.013 | OK |
| KXNHLGAME-26OCT06NYINYR-NYR | game_winner | 0.629 | 0.595 | 0.602 | 60 | 41 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-9 | game_total | 0.203 | 0.175 | 0.180 | 18 | 83 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT06FLALA-8 | game_total | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-7 | game_total | 0.476 | 0.445 | 0.451 | 45 | 56 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT06STLCHI-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR6 | team_total | 0.124 | 0.100 | 0.105 | 11 | 91 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT06STLCHI-CHI5 | team_total | 0.134 | 0.155 | 0.151 | 16 | 85 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYI4 | team_total | 0.269 | 0.295 | 0.290 | 30 | 71 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA2 | team_total | 0.783 | 0.815 | 0.809 | 83 | 20 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR3 | team_total | 0.672 | 0.645 | 0.650 | 65 | 36 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT06FLALA-6 | game_total | 0.573 | 0.545 | 0.551 | 55 | 46 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT06STLCHI-CHI3 | team_total | 0.508 | 0.535 | 0.530 | 54 | 47 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT06STLCHI-CHI4 | team_total | 0.292 | 0.320 | 0.314 | 33 | 69 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR5 | team_total | 0.256 | 0.235 | 0.239 | 24 | 77 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR2 | team_total | 0.852 | 0.830 | 0.835 | 84 | 18 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK6 | team_total | 0.101 | 0.120 | 0.116 | 13 | 89 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-10 | game_total | 0.098 | 0.080 | 0.083 | 9 | 93 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT06STLCHI-STL4 | team_total | 0.391 | 0.415 | 0.410 | 42 | 59 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYI6 | team_total | 0.046 | 0.060 | 0.057 | 7 | 95 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT06STLCHI-STL3 | game_spread | 0.207 | 0.225 | 0.221 | 23 | 78 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT06STLCHI-CHI2 | team_total | 0.736 | 0.765 | 0.759 | 78 | 25 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-6 | game_total | 0.587 | 0.565 | 0.569 | 57 | 44 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-7 | game_total | 0.456 | 0.435 | 0.439 | 44 | 57 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT06NYINYR-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA5 | team_total | 0.181 | 0.205 | 0.200 | 22 | 81 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT06STLCHI-10 | game_total | 0.059 | 0.065 | 0.064 | 7 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-3 | game_total | 0.969 | 0.965 | 0.966 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-2 | game_total | 0.987 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT06NYINYR-9 | game_total | 0.155 | 0.145 | 0.147 | 15 | 86 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYI5 | team_total | 0.127 | 0.145 | 0.141 | 16 | 87 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYI2 | team_total | 0.721 | 0.740 | 0.736 | 75 | 27 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT06NYINYR-10 | game_total | 0.069 | 0.060 | 0.062 | 7 | 95 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT06STLCHI-8 | game_total | 0.204 | 0.220 | 0.217 | 23 | 79 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT06VGKSEA-5 | game_total | 0.796 | 0.785 | 0.787 | 79 | 22 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT06FLALA-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT06STLCHI-CHI6 | team_total | 0.053 | 0.055 | 0.055 | 6 | 95 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT06NYINYR-2 | game_total | 0.984 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYI @ NYR | 0.629 | 0.588 | 0.175 | 0.220 | 5.97 | 5.93 | 0.934/0.977 | KXNHLSPREAD-26OCT06NYINYR-NYR2 -0.052 |
| STL @ CHI | 0.426 | 0.434 | 0.182 | 0.217 | 5.78 | 6.13 | 0.995/0.976 | KXNHLTOTAL-26OCT06STLCHI-7 +0.061 |
| VGK @ SEA | 0.503 | 0.485 | 0.174 | 0.223 | 6.38 | 6.10 | 1.001/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.045 |
| FLA @ LAK | 0.557 | 0.580 | 0.172 | 0.220 | 6.25 | 5.96 | 0.995/1.014 | KXNHLTOTAL-26OCT06FLALA-6 -0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Ondrej Palat: 1+ goals YES @ 8c · p 0.1112 (adj 0.1021) · $3.75 · thesis NYI:OFFENSE_4PLUS
- Tye Kartye: 1+ goals YES @ 12c · p 0.154 (adj 0.1442) · $3.79 · thesis NYR:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3272 (adj 0.2886) · $3.61 · thesis NYR:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 70c · p 0.7383 (adj 0.7275) · $10.54 · thesis NYI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 11c · p 0.1687 (adj 0.1528) · $7.66 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7383 (adj 0.6354) · $16.9 · thesis CHI:SUPPRESSED
- Mason McTavish: 1+ assists NO @ 70c · p 0.7863 (adj 0.7381) · $16.9 · thesis STL:SUPPRESSED
- Philip Broberg: 1+ goals YES @ 7c · p 0.1003 (adj 0.0877) · $2.56 · thesis STL:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 10c · p 0.1407 (adj 0.1293) · $4.81 · thesis SEA:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1144 (adj 0.1046) · $3.9 · thesis SEA:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 70c · p 0.7599 (adj 0.7437) · $17.61 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 74c · p 0.8189 (adj 0.777) · $16.49 · thesis SEA:WINS
- Sam Reinhart: 1+ goals NO @ 68c · p 0.7706 (adj 0.7467) · $17.61 · thesis FLA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.7886 (adj 0.6855) · $17.61 · thesis LAK:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2745 (adj 0.2621) · $6.26 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYI @ NYR** · priced 154/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.05, exp saves 24.57 (sd 6.5), pull risk 0.044
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 25.47, exp saves 21.89 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Palmieri: 1+ assists | 0.171 | 0.280 | 30/74 | +0.075 | STANDARD |
| Semyon Varlamov: 24+ saves | 0.389 | 0.485 | 54/57 | +0.024 |  |
| Kyle Palmieri: 1+ points | 0.350 | 0.440 | 46/58 | +0.053 | STANDARD |
| Matias Maccelli: 1+ assists | 0.183 | 0.265 | 29/76 | +0.044 | STANDARD |
| Gabe Perreault: 1+ assists | 0.320 | 0.240 | 26/78 | +0.046 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.379 | 0.300 | 31/71 | +0.054 | STANDARD |

**STL @ CHI** · priced 148/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.19, exp saves 23.24 (sd 6.49), pull risk 0.067
- STL net: Joel Hofer (CONFIRMED) exp shots 25.55, exp saves 22.31 (sd 6.13), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 23+ saves | 0.547 | 0.305 | 55/94 | -0.020 |  |
| Patrick Kane: 1+ assists | 0.262 | 0.420 | 43/59 | +0.131 | STANDARD |
| Patrick Kane: 1+ points | 0.444 | 0.570 | 58/44 | +0.099 | STANDARD |
| Bowen Byram: 1+ assists | 0.229 | 0.335 | 34/67 | +0.085 | STANDARD |
| Bowen Byram: 1+ points | 0.316 | 0.420 | 43/59 | +0.077 | STANDARD |
| Mason McTavish: 1+ points | 0.392 | 0.495 | 51/52 | +0.071 | STANDARD |

**VGK @ SEA** · priced 143/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.49, exp saves 24.64 (sd 6.77), pull risk 0.058
- VGK net: Adin Hill (PROJECTED) exp shots 25.65, exp saves 22.19 (sd 6.17), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joey Daccord: 25+ saves | 0.503 | 0.295 | 54/95 | -0.055 |  |
| Jack Eichel: 2+ points | 0.206 | 0.355 | 37/66 | +0.118 | STANDARD |
| Jack Eichel: 1+ assists | 0.407 | 0.535 | 55/48 | +0.096 | STANDARD |
| Mitch Marner: 1+ assists | 0.385 | 0.505 | 52/51 | +0.088 | STANDARD |
| Mitch Marner: 1+ points | 0.530 | 0.645 | 66/37 | +0.084 | STANDARD |
| Jack Eichel: 1+ points | 0.570 | 0.685 | 69/32 | +0.095 | STANDARD |

**FLA @ LAK** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 26.39, exp saves 23.09 (sd 6.23), pull risk 0.049
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.81, exp saves 23.61 (sd 6.55), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.211 | 0.370 | 38/64 | +0.132 | STANDARD |
| Brady Tkachuk: 1+ points | 0.422 | 0.565 | 59/46 | +0.100 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.370 | 39/65 | +0.102 | STANDARD |
| Sam Reinhart: 1+ points | 0.460 | 0.590 | 61/43 | +0.093 | STANDARD |
| Artemi Panarin: 1+ assists | 0.390 | 0.515 | 52/49 | +0.103 | STANDARD |
| Alex Laferriere: 1+ assists | 0.387 | 0.265 | 27/74 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
