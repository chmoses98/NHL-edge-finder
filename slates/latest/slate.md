# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T15:06:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2981 · contracts joined: 1069 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 944, 'OK': 89, 'NO_EDGE': 36}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 139, 'game_early_goal': 5, 'first_goal': 181, 'game_winner': 10, 'player_goals': 311, 'game_overtime': 5, 'player_points': 181, 'goalie_saves': 2, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 2026-10-25T19:00:00Z | T-3h | 0.495 | 0.505 | 0.186 | 6.04 | 3.00 | 3.03 | 222 (25/197) | PROJECTED/CONFIRMED |
| NYI @ DAL | 2026-10-25T22:00:00Z | T-6h | 0.566 | 0.434 | 0.188 | 5.52 | 2.95 | 2.56 | 211 (25/186) | PROJECTED/PROJECTED |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-6h | 0.464 | 0.536 | 0.180 | 5.94 | 2.87 | 3.07 | 204 (25/179) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-6h | 0.382 | 0.618 | 0.170 | 6.08 | 2.66 | 3.41 | 232 (25/207) | PROJECTED/PROJECTED |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-6h | 0.460 | 0.540 | 0.170 | 6.75 | 3.24 | 3.52 | 200 (25/175) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT25FLACHI-FLA2 | game_spread | 0.283 | 0.415 | 0.387 | 42 | 59 | no | +0.110 | OK |
| KXNHLGAME-26OCT25FLACHI-CHI | game_winner | 0.495 | 0.375 | 0.398 | 38 | 63 | yes | +0.098 | OK |
| KXNHLGAME-26OCT25FLACHI-FLA | game_winner | 0.505 | 0.625 | 0.602 | 63 | 38 | no | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA4 | team_total | 0.373 | 0.495 | 0.470 | 51 | 52 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA3 | game_spread | 0.169 | 0.275 | 0.251 | 28 | 73 | no | +0.087 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 | team_total | 0.590 | 0.705 | 0.683 | 72 | 31 | no | +0.085 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.460 | 0.355 | 0.375 | 36 | 65 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.457 | 0.565 | 0.543 | 58 | 45 | no | +0.076 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.540 | 0.635 | 0.617 | 64 | 37 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.330 | 0.425 | 0.405 | 43 | 58 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.252 | 0.345 | 0.325 | 35 | 66 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.675 | 0.770 | 0.753 | 78 | 24 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA5 | team_total | 0.194 | 0.295 | 0.273 | 31 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.628 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.209 | 0.295 | 0.276 | 30 | 71 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.150 | 0.165 | 16 | 86 | yes | +0.066 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.755 | 0.835 | 0.821 | 84 | 17 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.428 | 0.515 | 0.497 | 52 | 49 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.419 | 0.325 | 0.343 | 34 | 69 | yes | +0.064 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI2 | game_spread | 0.273 | 0.195 | 0.209 | 20 | 81 | yes | +0.062 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.541 | 0.625 | 0.609 | 63 | 38 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.264 | 0.350 | 0.332 | 36 | 66 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA2 | team_total | 0.802 | 0.875 | 0.862 | 88 | 13 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.196 | 0.275 | 0.258 | 28 | 73 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.258 | 0.185 | 0.198 | 19 | 82 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.350 | 0.430 | 0.413 | 44 | 58 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.392 | 0.465 | 0.450 | 47 | 54 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.844 | 0.905 | 0.895 | 91 | 10 | no | +0.050 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.618 | 0.685 | 0.672 | 69 | 32 | no | +0.047 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.382 | 0.315 | 0.328 | 32 | 69 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.327 | 0.395 | 0.381 | 40 | 61 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.243 | 0.305 | 0.292 | 31 | 70 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.582 | 0.650 | 0.637 | 66 | 36 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.853 | 0.910 | 0.901 | 92 | 10 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA6 | team_total | 0.082 | 0.135 | 0.123 | 14 | 87 | no | +0.040 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.434 | 0.375 | 0.387 | 38 | 63 | yes | +0.037 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.566 | 0.625 | 0.613 | 63 | 38 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.793 | 0.850 | 0.840 | 86 | 16 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.124 | 0.180 | 0.168 | 19 | 83 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI3 | game_spread | 0.163 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT25FLACHI-6 | game_total | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.824 | 0.770 | 0.782 | 78 | 24 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.168 | 0.220 | 0.209 | 23 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI5 | team_total | 0.189 | 0.145 | 0.153 | 15 | 86 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4 | team_total | 0.364 | 0.310 | 0.320 | 32 | 70 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.677 | 0.730 | 0.720 | 74 | 28 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.219 | 0.175 | 0.183 | 18 | 83 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.156 | 0.110 | 0.118 | 12 | 90 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.341 | 0.290 | 0.300 | 30 | 72 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.111 | 0.065 | 0.073 | 8 | 95 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT25FLACHI-5 | game_total | 0.754 | 0.795 | 0.787 | 80 | 21 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT25FLACHI-4 | game_total | 0.839 | 0.875 | 0.868 | 88 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI3 | team_total | 0.580 | 0.530 | 0.540 | 54 | 48 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI2 | team_total | 0.794 | 0.755 | 0.763 | 76 | 25 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.537 | 0.495 | 0.503 | 50 | 51 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.252 | 0.210 | 0.218 | 22 | 80 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.686 | 0.730 | 0.722 | 74 | 28 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.646 | 0.605 | 0.613 | 61 | 40 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.783 | 0.820 | 0.813 | 83 | 19 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.078 | 0.110 | 0.103 | 12 | 90 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.338 | 0.375 | 0.367 | 38 | 63 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.477 | 0.520 | 0.511 | 53 | 49 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.827 | 0.855 | 0.850 | 86 | 15 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT25FLACHI-7 | game_total | 0.420 | 0.455 | 0.448 | 46 | 55 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.110 | 0.135 | 0.130 | 14 | 87 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.129 | 0.100 | 0.105 | 11 | 91 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.072 | 0.100 | 0.094 | 11 | 91 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-10 | game_total | 0.044 | 0.065 | 0.060 | 7 | 94 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.441 | 0.475 | 0.468 | 48 | 53 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.191 | 0.165 | 0.170 | 17 | 84 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.862 | 0.890 | 0.885 | 90 | 12 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI6 | team_total | 0.084 | 0.060 | 0.064 | 7 | 95 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.938 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.959 | 0.980 | 0.977 | 99 | 3 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25FLACHI-3 | game_total | 0.960 | 0.975 | 0.973 | 98 | 3 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.143 | 0.170 | 0.164 | 18 | 84 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25FLACHI-9 | game_total | 0.164 | 0.190 | 0.184 | 20 | 82 | no | +0.006 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 0.495 | 0.474 | 0.186 | 0.223 | 6.04 | 6.28 | 1.003/0.991 | KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 +0.047 |
| NYI @ DAL | 0.566 | 0.549 | 0.188 | 0.222 | 5.52 | 6.01 | 0.986/0.956 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.086 |
| MTL @ WPG | 0.464 | 0.481 | 0.180 | 0.222 | 5.94 | 6.25 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.053 |
| COL @ NSH | 0.382 | 0.394 | 0.170 | 0.213 | 6.08 | 6.47 | 0.994/0.973 | KXNHLTOTAL-26OCT25COLNSH-7 +0.067 |
| MIN @ VAN | 0.460 | 0.522 | 0.170 | 0.214 | 6.75 | 6.50 | 1.025/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.072 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 17 recommended · full analysis in card.md / packet.json `thesis_card`

- Sam Reinhart: 1+ goals NO @ 65c · p 0.7312 (adj 0.7084) · $20.0 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 10c · p 0.1518 (adj 0.1301) · $5.84 · thesis FLA:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 19c · p 0.2415 (adj 0.2274) · $8.01 · thesis CHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1584 (adj 0.1451) · $4.74 · thesis CHI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2413 (adj 0.2197) · $8.1 · thesis NYI:OFFENSE_4PLUS
- Kyle Palmieri: 1+ goals YES @ 20c · p 0.2469 (adj 0.2302) · $5.35 · thesis NYI:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7267 (adj 0.7138) · $14.55 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 73c · p 0.7956 (adj 0.7603) · $9.12 · thesis GAME:TIGHT
- Josh Anderson: 1+ goals YES @ 17c · p 0.2118 (adj 0.2001) · $5.95 · thesis MTL:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3351 (adj 0.3213) · $6.07 · thesis WPG:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1698 (adj 0.1486) · $2.7 · thesis WPG:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7335 (adj 0.6943) · $13.89 · thesis GAME:TIGHT
- Nathan MacKinnon: 1+ assists NO @ 41c · p 0.4795 (adj 0.4397) · $3.83 · thesis COL:SUPPRESSED
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1545 (adj 0.1421) · $5.97 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2481 (adj 0.2298) · $7.38 · thesis VAN:OFFENSE_4PLUS
- Minnesota wins by over 1.5 goals NO @ 58c · p 0.7386 (adj 0.6323) · $17.24 · thesis VAN:WINS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2255 (adj 0.2066) · $6.64 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CHI** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.49, exp saves 24.39 (sd 6.74), pull risk 0.066
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.46, exp saves 21.17 (sd 6.11), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Akira Schmid: 22+ saves | 0.469 | 0.285 | 51/94 | -0.058 |  |
| Sam Reinhart: 1+ points | 0.486 | 0.615 | 62/39 | +0.107 | STANDARD |
| Brady Tkachuk: 1+ points | 0.534 | 0.655 | 67/36 | +0.090 | STANDARD |
| Sam Reinhart: 1+ assists | 0.301 | 0.415 | 43/60 | +0.083 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.328 | 0.435 | 44/57 | +0.085 | STANDARD |
| Patrick Kane: 1+ assists | 0.319 | 0.425 | 44/59 | +0.074 | STANDARD |

**NYI @ DAL** · priced 155/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.15 (sd 6.06), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.22, exp saves 22.6 (sd 6.21), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Perron: 1+ goals | 0.165 | 0.075 | 13/98 | +0.027 | STANDARD |
| Brayden Schenn: 1+ goals | 0.241 | 0.155 | 18/87 | +0.051 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.435 | 0.515 | 53/50 | +0.048 | STANDARD |
| Mikko Rantanen: 2+ points | 0.242 | 0.320 | 35/71 | +0.034 | STANDARD |
| Brayden Schenn: 1+ points | 0.462 | 0.385 | 41/64 | +0.035 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.457 | 0.530 | 55/49 | +0.035 | STANDARD |

**MTL @ WPG** · priced 149/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.39), pull risk 0.059
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.54, exp saves 23.94 (sd 6.53), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Oliver Kapanen: 1+ points | 0.366 | 0.455 | 47/56 | +0.056 | STANDARD |
| Alex Iafallo: 1+ goals | 0.170 | 0.085 | 13/96 | +0.032 | STANDARD |
| Cole Perfetti: 2+ points | 0.188 | 0.115 | 17/94 | +0.008 | STANDARD |
| Oliver Kapanen: 1+ assists | 0.216 | 0.275 | 29/74 | +0.030 | STANDARD |
| Viggo Bjorck: 1+ goals | 0.139 | 0.080 | 14/98 | -0.010 | STANDARD |
| Mark Scheifele: 1+ assists | 0.462 | 0.520 | 53/49 | +0.031 | STANDARD |

**COL @ NSH** · priced 178/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 32.01, exp saves 27.22 (sd 7.51), pull risk 0.086
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.47, exp saves 23.17 (sd 6.3), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.134 | 0.240 | 26/78 | +0.074 | STANDARD |
| Cale Makar: 1+ assists | 0.453 | 0.550 | 56/46 | +0.069 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.368 | 0.455 | 47/56 | +0.054 | STANDARD |
| Cale Makar: 1+ points | 0.559 | 0.645 | 68/39 | +0.034 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.520 | 0.600 | 61/41 | +0.053 | STANDARD |
| Nazem Kadri: 1+ assists | 0.348 | 0.415 | 43/60 | +0.035 | STANDARD |

**MIN @ VAN** · priced 143/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.99, exp saves 26.89 (sd 7.1), pull risk 0.062
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.19 (sd 6.24), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 22+ saves | 0.538 | 0.275 | 48/93 | +0.040 |  |
| Kirill Kaprizov: 2+ points | 0.268 | 0.410 | 43/61 | +0.105 | STANDARD |
| Quinn Hughes: 2+ points | 0.223 | 0.350 | 37/67 | +0.092 | STANDARD |
| Quinn Hughes: 1+ assists | 0.522 | 0.645 | 66/37 | +0.092 | STANDARD |
| Matt Boldy: 2+ points | 0.247 | 0.370 | 39/65 | +0.087 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.409 | 0.530 | 55/49 | +0.083 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
