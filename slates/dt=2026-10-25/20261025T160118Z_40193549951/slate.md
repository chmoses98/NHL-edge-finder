# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T16:01:18Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2984 · contracts joined: 1072 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 947, 'OK': 86, 'NO_EDGE': 39}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 140, 'game_early_goal': 5, 'first_goal': 181, 'game_winner': 10, 'player_goals': 311, 'game_overtime': 5, 'player_points': 182, 'goalie_saves': 3, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 2026-10-25T19:00:00Z | T-90m | 0.495 | 0.505 | 0.186 | 6.04 | 3.00 | 3.03 | 222 (25/197) | PROJECTED/CONFIRMED |
| NYI @ DAL | 2026-10-25T22:00:00Z | T-3h | 0.566 | 0.434 | 0.188 | 5.52 | 2.95 | 2.56 | 214 (25/189) | PROJECTED/PROJECTED |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-6h | 0.464 | 0.536 | 0.180 | 5.94 | 2.87 | 3.07 | 204 (25/179) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-6h | 0.382 | 0.618 | 0.170 | 6.08 | 2.66 | 3.41 | 232 (25/207) | PROJECTED/PROJECTED |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-6h | 0.460 | 0.540 | 0.170 | 6.75 | 3.24 | 3.52 | 200 (25/175) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT25FLACHI-FLA2 | game_spread | 0.283 | 0.415 | 0.387 | 42 | 59 | no | +0.110 | OK |
| KXNHLGAME-26OCT25FLACHI-FLA | game_winner | 0.505 | 0.635 | 0.610 | 64 | 37 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA4 | team_total | 0.373 | 0.500 | 0.474 | 51 | 51 | no | +0.099 | OK |
| KXNHLGAME-26OCT25FLACHI-CHI | game_winner | 0.495 | 0.375 | 0.398 | 38 | 63 | yes | +0.098 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA3 | game_spread | 0.169 | 0.285 | 0.258 | 29 | 72 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 | team_total | 0.590 | 0.710 | 0.688 | 72 | 30 | no | +0.095 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.457 | 0.570 | 0.548 | 58 | 44 | no | +0.086 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.540 | 0.645 | 0.625 | 65 | 36 | no | +0.084 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.460 | 0.355 | 0.375 | 36 | 65 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.330 | 0.425 | 0.405 | 43 | 58 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.252 | 0.345 | 0.325 | 35 | 66 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.675 | 0.770 | 0.753 | 78 | 24 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA5 | team_total | 0.194 | 0.295 | 0.273 | 31 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.264 | 0.360 | 0.339 | 37 | 65 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.628 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.209 | 0.300 | 0.280 | 31 | 71 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.755 | 0.835 | 0.821 | 84 | 17 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.419 | 0.325 | 0.343 | 34 | 69 | yes | +0.064 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI2 | game_spread | 0.273 | 0.195 | 0.209 | 20 | 81 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA2 | team_total | 0.802 | 0.875 | 0.862 | 88 | 13 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.196 | 0.275 | 0.258 | 28 | 73 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.258 | 0.185 | 0.198 | 19 | 82 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 17 | 86 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.428 | 0.510 | 0.493 | 52 | 50 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.350 | 0.430 | 0.413 | 44 | 58 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.541 | 0.620 | 0.605 | 63 | 39 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.392 | 0.465 | 0.450 | 47 | 54 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.844 | 0.905 | 0.895 | 91 | 10 | no | +0.050 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.618 | 0.685 | 0.672 | 69 | 32 | no | +0.047 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.382 | 0.315 | 0.328 | 32 | 69 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.327 | 0.395 | 0.381 | 40 | 61 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.175 | 0.240 | 0.226 | 25 | 77 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.243 | 0.305 | 0.292 | 31 | 70 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.582 | 0.650 | 0.637 | 66 | 36 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.853 | 0.910 | 0.901 | 92 | 10 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA6 | team_total | 0.082 | 0.140 | 0.126 | 15 | 87 | no | +0.040 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.434 | 0.375 | 0.387 | 38 | 63 | yes | +0.037 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.566 | 0.625 | 0.613 | 63 | 38 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.111 | 0.060 | 0.068 | 7 | 95 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.124 | 0.180 | 0.168 | 19 | 83 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI3 | game_spread | 0.163 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT25FLACHI-6 | game_total | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.824 | 0.770 | 0.782 | 78 | 24 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.168 | 0.220 | 0.209 | 23 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4 | team_total | 0.364 | 0.310 | 0.320 | 32 | 70 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.677 | 0.725 | 0.716 | 73 | 28 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.219 | 0.175 | 0.183 | 18 | 83 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.156 | 0.110 | 0.118 | 12 | 90 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.793 | 0.845 | 0.836 | 86 | 17 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.341 | 0.290 | 0.300 | 30 | 72 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT25FLACHI-5 | game_total | 0.754 | 0.795 | 0.787 | 80 | 21 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI3 | team_total | 0.580 | 0.530 | 0.540 | 54 | 48 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI2 | team_total | 0.794 | 0.750 | 0.759 | 76 | 26 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI5 | team_total | 0.189 | 0.145 | 0.153 | 16 | 87 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.252 | 0.210 | 0.218 | 22 | 80 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.686 | 0.730 | 0.722 | 74 | 28 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.078 | 0.110 | 0.103 | 12 | 90 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.477 | 0.520 | 0.511 | 53 | 49 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25FLACHI-7 | game_total | 0.420 | 0.455 | 0.448 | 46 | 55 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25FLACHI-4 | game_total | 0.839 | 0.870 | 0.864 | 88 | 14 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.110 | 0.135 | 0.130 | 14 | 87 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.129 | 0.100 | 0.105 | 11 | 91 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.072 | 0.110 | 0.101 | 13 | 91 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-10 | game_total | 0.044 | 0.065 | 0.060 | 7 | 94 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25FLACHI-8 | game_total | 0.235 | 0.265 | 0.259 | 27 | 74 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.441 | 0.475 | 0.468 | 48 | 53 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.191 | 0.165 | 0.170 | 17 | 84 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.537 | 0.500 | 0.507 | 51 | 51 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.646 | 0.610 | 0.617 | 62 | 40 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.938 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.959 | 0.980 | 0.977 | 99 | 3 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25FLACHI-3 | game_total | 0.960 | 0.975 | 0.973 | 98 | 3 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.143 | 0.170 | 0.164 | 18 | 84 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25FLACHI-9 | game_total | 0.164 | 0.190 | 0.184 | 20 | 82 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.783 | 0.810 | 0.805 | 82 | 20 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.338 | 0.365 | 0.360 | 37 | 64 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI6 | team_total | 0.048 | 0.035 | 0.037 | 4 | 97 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.827 | 0.850 | 0.846 | 86 | 16 | no | +0.004 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 0.495 | 0.474 | 0.186 | 0.223 | 6.04 | 6.28 | 1.003/0.991 | KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 +0.047 |
| NYI @ DAL | 0.566 | 0.549 | 0.188 | 0.222 | 5.52 | 6.01 | 0.986/0.956 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.086 |
| MTL @ WPG | 0.464 | 0.481 | 0.180 | 0.222 | 5.94 | 6.25 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.053 |
| COL @ NSH | 0.382 | 0.394 | 0.170 | 0.213 | 6.08 | 6.47 | 0.994/0.973 | KXNHLTOTAL-26OCT25COLNSH-7 +0.067 |
| MIN @ VAN | 0.460 | 0.522 | 0.170 | 0.214 | 6.75 | 6.50 | 1.025/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.072 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 18 recommended · full analysis in card.md / packet.json `thesis_card`

- Brady Tkachuk: 1+ goals NO @ 61c · p 0.6932 (adj 0.6712) · $19.29 · thesis FLA:SUPPRESSED
- Cole Schwindt: 1+ goals YES @ 10c · p 0.1518 (adj 0.1288) · $5.21 · thesis FLA:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 23c · p 0.2865 (adj 0.2711) · $8.79 · thesis CHI:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 19c · p 0.2415 (adj 0.2236) · $6.49 · thesis CHI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 17c · p 0.2413 (adj 0.2172) · $9.84 · thesis NYI:OFFENSE_4PLUS
- Kyle Palmieri: 1+ goals YES @ 19c · p 0.2469 (adj 0.2289) · $7.96 · thesis NYI:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 9c · p 0.1275 (adj 0.1131) · $4.0 · thesis NYI:OFFENSE_4PLUS
- Logan Stanley: 1+ goals YES @ 4c · p 0.0571 (adj 0.0528) · $2.28 · thesis NYI:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 4c · p 0.061 (adj 0.0532) · $2.27 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3351 (adj 0.3201) · $5.4 · thesis WPG:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 18c · p 0.2118 (adj 0.2026) · $3.64 · thesis MTL:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 78c · p 0.8659 (adj 0.8179) · $19.29 · thesis NSH:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7335 (adj 0.6943) · $14.5 · thesis GAME:TIGHT
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6119 (adj 0.5735) · $1.65 · thesis GAME:TIGHT
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2255 (adj 0.2079) · $10.28 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1545 (adj 0.1409) · $5.88 · thesis VAN:OFFENSE_4PLUS
- Matt Boldy: 1+ goals NO @ 59c · p 0.6546 (adj 0.636) · $17.45 · thesis MIN:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 19c · p 0.2343 (adj 0.2207) · $5.78 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CHI** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.49, exp saves 24.39 (sd 6.74), pull risk 0.066
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.46, exp saves 21.17 (sd 6.11), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Akira Schmid: 22+ saves | 0.469 | 0.280 | 51/95 | -0.058 |  |
| Sam Reinhart: 1+ points | 0.486 | 0.610 | 62/40 | +0.097 | STANDARD |
| Brady Tkachuk: 1+ points | 0.534 | 0.645 | 65/36 | +0.090 | STANDARD |
| Seth Jones: 1+ points | 0.438 | 0.540 | 55/47 | +0.075 | STANDARD |
| Patrick Kane: 1+ assists | 0.319 | 0.420 | 44/60 | +0.064 | STANDARD |
| Sam Reinhart: 1+ assists | 0.301 | 0.400 | 42/62 | +0.063 | STANDARD |

**NYI @ DAL** · priced 158/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.15 (sd 6.06), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.22, exp saves 22.6 (sd 6.21), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Logan Stanley: 1+ points | 0.275 | 0.145 | 26/97 | +0.002 | STANDARD |
| Logan Stanley: 1+ assists | 0.232 | 0.125 | 24/99 | -0.021 | STANDARD |
| Brayden Schenn: 1+ goals | 0.241 | 0.145 | 17/88 | +0.061 | STANDARD |
| David Perron: 1+ goals | 0.165 | 0.080 | 14/98 | +0.017 | STANDARD |
| Ilya Sorokin: 25+ saves | 0.366 | 0.285 | 51/94 | -0.161 |  |
| Miro Heiskanen: 1+ assists | 0.435 | 0.515 | 53/50 | +0.048 | STANDARD |

**MTL @ WPG** · priced 149/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.39), pull risk 0.059
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.54, exp saves 23.94 (sd 6.53), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Oliver Kapanen: 1+ points | 0.366 | 0.445 | 46/57 | +0.046 | STANDARD |
| Alex Iafallo: 1+ goals | 0.170 | 0.100 | 14/94 | +0.021 | STANDARD |
| Cole Perfetti: 2+ points | 0.188 | 0.120 | 18/94 | -0.003 | STANDARD |
| Mark Scheifele: 1+ goals | 0.335 | 0.275 | 29/74 | +0.031 | STANDARD |
| Cole Perfetti: 1+ assists | 0.384 | 0.325 | 35/70 | +0.018 | STANDARD |
| Viggo Bjorck: 1+ goals | 0.139 | 0.080 | 13/97 | +0.001 | STANDARD |

**COL @ NSH** · priced 178/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 32.01, exp saves 27.22 (sd 7.51), pull risk 0.086
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.47, exp saves 23.17 (sd 6.3), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.134 | 0.230 | 24/78 | +0.074 | STANDARD |
| Cale Makar: 1+ assists | 0.453 | 0.545 | 56/47 | +0.059 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.368 | 0.460 | 48/56 | +0.054 | STANDARD |
| Cale Makar: 1+ points | 0.559 | 0.650 | 68/38 | +0.044 | STANDARD |
| Cale Makar: 2+ points | 0.199 | 0.285 | 31/74 | +0.048 | STANDARD |
| Jonathan Marchessault: 1+ goals | 0.197 | 0.120 | 18/94 | +0.007 | STANDARD |

**MIN @ VAN** · priced 143/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.99, exp saves 26.89 (sd 7.1), pull risk 0.062
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.19 (sd 6.24), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 22+ saves | 0.538 | 0.275 | 48/93 | +0.040 |  |
| Kirill Kaprizov: 2+ points | 0.267 | 0.410 | 43/61 | +0.107 | STANDARD |
| Quinn Hughes: 2+ points | 0.220 | 0.355 | 37/66 | +0.105 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.645 | 66/37 | +0.096 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.373 | 0.495 | 51/52 | +0.090 | STANDARD |
| Matt Boldy: 2+ points | 0.248 | 0.370 | 39/65 | +0.086 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
