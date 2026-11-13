# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-13T00:08:50Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 5 · markets on board: 3921 · contracts joined: 1071 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 946, 'OK': 71, 'NO_EDGE': 54}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 141, 'game_early_goal': 5, 'first_goal': 177, 'game_winner': 10, 'player_goals': 302, 'game_overtime': 5, 'player_points': 186, 'goalie_saves': 10, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ FLA | 2026-11-13T00:30:00Z | T-10m | 0.573 | 0.427 | 0.176 | 6.08 | 3.27 | 2.82 | 223 (25/198) | CONFIRMED/PROJECTED |
| BUF @ CHI | 2026-11-13T01:00:00Z | T-30m | 0.454 | 0.546 | 0.182 | 5.94 | 2.83 | 3.11 | 214 (25/189) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-30m | 0.600 | 0.400 | 0.184 | 5.77 | 3.19 | 2.57 | 213 (25/188) | CONFIRMED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-90m | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 223 (25/198) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-90m | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 198 (25/173) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.407 | 0.515 | 0.493 | 52 | 49 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.390 | 0.495 | 0.474 | 50 | 51 | no | +0.082 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-6 | game_total | 0.518 | 0.615 | 0.596 | 62 | 39 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF3 | team_total | 0.609 | 0.695 | 0.679 | 70 | 31 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.735 | 0.815 | 0.801 | 82 | 19 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV12NYILA-5 | game_total | 0.695 | 0.775 | 0.760 | 78 | 23 | no | +0.062 | OK |
| KXNHLGAME-26NOV12DETFLA-DET | game_winner | 0.427 | 0.345 | 0.361 | 35 | 66 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5 | team_total | 0.209 | 0.285 | 0.268 | 29 | 72 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA3 | game_spread | 0.213 | 0.285 | 0.270 | 29 | 72 | no | +0.053 | OK |
| KXNHLGAME-26NOV12DETFLA-FLA | game_winner | 0.573 | 0.645 | 0.631 | 65 | 36 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA2 | game_spread | 0.344 | 0.415 | 0.400 | 42 | 59 | no | +0.049 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.855 | 0.844 | 86 | 15 | no | +0.048 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.829 | 0.885 | 0.875 | 89 | 12 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.224 | 0.285 | 0.272 | 29 | 72 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.800 | 0.788 | 81 | 21 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.812 | 0.870 | 0.860 | 88 | 14 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-9 | game_total | 0.154 | 0.205 | 0.194 | 21 | 80 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF3 | game_spread | 0.193 | 0.250 | 0.238 | 26 | 76 | no | +0.034 | OK |
| KXNHLGAME-26NOV12STLUTA-STL | game_winner | 0.489 | 0.545 | 0.534 | 55 | 46 | no | +0.034 | OK |
| KXNHLGAME-26NOV12STLUTA-UTA | game_winner | 0.511 | 0.455 | 0.466 | 46 | 55 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.235 | 0.225 | 24 | 77 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-FLA4 | team_total | 0.425 | 0.475 | 0.465 | 48 | 53 | no | +0.028 | OK |
| KXNHLGAME-26NOV12BUFCHI-BUF | game_winner | 0.546 | 0.595 | 0.585 | 60 | 41 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.319 | 0.365 | 0.356 | 37 | 64 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV12STLUTA-STL2 | game_spread | 0.272 | 0.315 | 0.306 | 32 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12NYILA-9 | game_total | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV12DETFLA-DET2 | game_spread | 0.222 | 0.185 | 0.192 | 19 | 82 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-5 | game_total | 0.716 | 0.760 | 0.752 | 77 | 25 | no | +0.020 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.454 | 0.415 | 0.423 | 42 | 59 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-7 | game_total | 0.376 | 0.415 | 0.407 | 42 | 59 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL4 | team_total | 0.407 | 0.445 | 0.437 | 45 | 56 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI3 | game_spread | 0.126 | 0.160 | 0.153 | 17 | 85 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-UTA5 | team_total | 0.214 | 0.185 | 0.191 | 19 | 82 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-CHI2 | game_spread | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA5 | team_total | 0.185 | 0.215 | 0.209 | 22 | 79 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-FLA5 | team_total | 0.234 | 0.265 | 0.259 | 27 | 74 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI5 | team_total | 0.138 | 0.180 | 0.171 | 20 | 84 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-FLA3 | team_total | 0.642 | 0.675 | 0.669 | 68 | 33 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET5 | team_total | 0.160 | 0.130 | 0.136 | 14 | 88 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA2 | team_total | 0.798 | 0.830 | 0.824 | 84 | 18 | no | +0.011 | OK |
| KXNHLSPREAD-26NOV12STLUTA-STL3 | game_spread | 0.158 | 0.185 | 0.179 | 19 | 82 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-WPG3 | team_total | 0.482 | 0.520 | 0.512 | 53 | 49 | no | +0.011 | OK |
| KXNHLSPREAD-26NOV12STLUTA-UTA2 | game_spread | 0.294 | 0.265 | 0.271 | 27 | 74 | yes | +0.011 | OK |
| KXNHLSPREAD-26NOV12WPGDAL-WPG3 | game_spread | 0.103 | 0.125 | 0.120 | 13 | 88 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI4 | team_total | 0.326 | 0.360 | 0.353 | 37 | 65 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA3 | team_total | 0.585 | 0.615 | 0.609 | 62 | 39 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-10 | game_total | 0.067 | 0.090 | 0.085 | 10 | 92 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-UTA6 | team_total | 0.093 | 0.075 | 0.078 | 8 | 93 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET4 | team_total | 0.322 | 0.285 | 0.292 | 30 | 73 | yes | +0.007 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI2 | game_spread | 0.230 | 0.255 | 0.250 | 26 | 75 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-FLA2 | team_total | 0.834 | 0.865 | 0.859 | 88 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-WPG4 | team_total | 0.270 | 0.300 | 0.294 | 31 | 71 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL3 | team_total | 0.628 | 0.655 | 0.650 | 66 | 35 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI6 | team_total | 0.052 | 0.065 | 0.062 | 7 | 94 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV12NYILA-2 | game_total | 0.975 | 0.990 | 0.988 |  | 2 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV12NYILA-10 | game_total | 0.053 | 0.070 | 0.066 | 8 | 94 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV12NYILA-3 | game_total | 0.944 | 0.960 | 0.957 | 97 | 5 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-3 | game_total | 0.955 | 0.975 | 0.972 | 99 | 4 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET6 | team_total | 0.066 | 0.050 | 0.053 | 6 | 96 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.091 | 0.110 | 0.106 | 12 | 90 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV12STLUTA-8 | game_total | 0.254 | 0.235 | 0.239 | 24 | 77 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV12DETFLA-DET2 | team_total | 0.765 | 0.745 | 0.749 | 75 | 26 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI3 | team_total | 0.542 | 0.565 | 0.560 | 57 | 44 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV12DETFLA-4 | game_total | 0.840 | 0.855 | 0.852 | 86 | 15 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-8 | game_total | 0.198 | 0.220 | 0.216 | 23 | 79 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26NOV12WPGDAL-DAL3 | game_spread | 0.227 | 0.245 | 0.241 | 25 | 76 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV12WPGDAL-9 | game_total | 0.132 | 0.145 | 0.142 | 15 | 86 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI2 | team_total | 0.768 | 0.785 | 0.782 | 79 | 22 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL5 | team_total | 0.218 | 0.240 | 0.235 | 25 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12STLUTA-STL2 | team_total | 0.800 | 0.825 | 0.820 | 84 | 19 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI5 | team_total | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV12DETFLA-5 | game_total | 0.758 | 0.780 | 0.776 | 79 | 23 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12STLUTA-STL4 | team_total | 0.374 | 0.400 | 0.395 | 41 | 61 |  | -0.001 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ FLA | 0.573 | 0.576 | 0.176 | 0.220 | 6.08 | 6.26 | 0.992/1.015 | KXNHLTOTAL-26NOV12DETFLA-7 +0.035 |
| BUF @ CHI | 0.454 | 0.484 | 0.182 | 0.220 | 5.94 | 6.22 | 0.990/0.989 | KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI3 +0.058 |
| WPG @ DAL | 0.600 | 0.586 | 0.184 | 0.209 | 5.77 | 6.12 | 0.994/1.001 | KXNHLTOTAL-26NOV12WPGDAL-7 +0.061 |
| STL @ UTA | 0.511 | 0.532 | 0.172 | 0.220 | 6.17 | 6.40 | 0.993/0.993 | KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4 +0.044 |
| NYI @ LAK | 0.554 | 0.551 | 0.185 | 0.221 | 5.66 | 5.99 | 0.990/0.956 | KXNHLTOTAL-26NOV12NYILA-5 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Schwindt: 1+ goals YES @ 8c · p 0.1066 (adj 0.0987) · $3.05 · thesis FLA:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6835 (adj 0.6689) · $14.14 · thesis FLA:SUPPRESSED
- Niko Mikkola: 1+ goals YES @ 5c · p 0.0699 (adj 0.0637) · $2.18 · thesis FLA:OFFENSE_4PLUS
- J.T. Compher: 1+ goals YES @ 13c · p 0.1605 (adj 0.1516) · $3.47 · thesis DET:OFFENSE_4PLUS
- Buffalo over 3.5 goals scored NO @ 51c · p 0.5998 (adj 0.5524) · $7.15 · thesis BUF:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 24c · p 0.2868 (adj 0.2738) · $6.22 · thesis CHI:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 60c · p 0.6527 (adj 0.6383) · $8.3 · thesis BUF:SUPPRESSED
- Rasmus Dahlin: 1+ goals NO @ 80c · p 0.8362 (adj 0.8259) · $12.14 · thesis BUF:SUPPRESSED
- Josh Morrissey: 1+ assists NO @ 59c · p 0.7432 (adj 0.6404) · $18.39 · thesis WPG:SUPPRESSED
- Jamie Benn: 1+ goals YES @ 16c · p 0.1996 (adj 0.1885) · $5.17 · thesis DAL:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 27c · p 0.318 (adj 0.3048) · $6.49 · thesis DAL:OFFENSE_4PLUS
- Cole Perfetti: 1+ assists YES @ 30c · p 0.3621 (adj 0.3286) · $5.29 · thesis WPG:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2462 (adj 0.2284) · $10.23 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 13c · p 0.1824 (adj 0.1681) · $7.47 · thesis UTA:OFFENSE_4PLUS
- Liam O'Brien: 1+ goals YES @ 7c · p 0.0945 (adj 0.0871) · $2.91 · thesis UTA:OFFENSE_4PLUS
- Kevin Stenlund: 1+ goals YES @ 8c · p 0.1041 (adj 0.0968) · $2.78 · thesis UTA:OFFENSE_4PLUS
- Andre Lee: 1+ goals YES @ 8c · p 0.1318 (adj 0.1176) · $7.3 · thesis LAK:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 65c · p 0.8509 (adj 0.7171) · $18.39 · thesis LAK:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 27c · p 0.3125 (adj 0.3006) · $5.55 · thesis LAK:OFFENSE_4PLUS
- Erik Haula: 1+ goals YES @ 15c · p 0.1784 (adj 0.1701) · $3.36 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**DET @ FLA** · priced 161/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 27.02, exp saves 23.58 (sd 6.37), pull risk 0.052
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.83, exp saves 23.78 (sd 6.68), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Tkachuk: 1+ assists | 0.480 | 0.560 | 57/45 | +0.053 | STANDARD |
| Brady Tkachuk: 1+ points | 0.560 | 0.635 | 64/37 | +0.053 | STANDARD |
| Lucas Raymond: 1+ assists | 0.351 | 0.425 | 43/58 | +0.052 | STANDARD |
| Brady Tkachuk: 2+ points | 0.198 | 0.270 | 29/75 | +0.039 | STANDARD |
| Aaron Ekblad: 1+ points | 0.392 | 0.320 | 33/69 | +0.046 | STANDARD |
| Aaron Ekblad: 1+ assists | 0.331 | 0.260 | 27/75 | +0.047 | STANDARD |

**BUF @ CHI** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.67, exp saves 25.66 (sd 6.84), pull risk 0.063
- BUF net: Alex Lyon (PROJECTED) exp shots 25.13, exp saves 21.69 (sd 6.06), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ assists | 0.422 | 0.540 | 55/47 | +0.091 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.518 | 0.630 | 64/38 | +0.086 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.169 | 0.270 | 28/74 | +0.078 | STANDARD |
| Tage Thompson: 1+ points | 0.564 | 0.655 | 66/35 | +0.070 | STANDARD |
| Connor Bedard: 1+ assists | 0.438 | 0.525 | 53/48 | +0.065 | STANDARD |
| Tage Thompson: 2+ points | 0.209 | 0.295 | 30/71 | +0.067 | STANDARD |

**WPG @ DAL** · priced 159/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.66 (sd 6.03), pull risk 0.048
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.72, exp saves 22.89 (sd 6.34), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.257 | 0.415 | 42/59 | +0.136 | STANDARD |
| Josh Morrissey: 1+ points | 0.337 | 0.470 | 48/54 | +0.106 | STANDARD |
| Josh Morrissey: 2+ points | 0.062 | 0.140 | 15/87 | +0.060 | STANDARD |
| Mikko Rantanen: 2+ points | 0.243 | 0.315 | 33/70 | +0.043 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.525 | 53/48 | +0.050 | STANDARD |
| Josh Morrissey: 2+ assists | 0.036 | 0.105 | 12/91 | +0.049 | STANDARD |

**STL @ UTA** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.26), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.65, exp saves 24.64 (sd 6.73), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.450 | 0.325 | 34/69 | +0.094 | STANDARD |
| Jack McBain: 1+ points | 0.387 | 0.275 | 29/74 | +0.083 | STANDARD |
| Robert Thomas: 1+ assists | 0.431 | 0.540 | 55/47 | +0.082 | STANDARD |
| Clayton Keller: 1+ assists | 0.478 | 0.575 | 58/43 | +0.075 | STANDARD |
| MacKenzie Weegar: 1+ assists | 0.367 | 0.280 | 29/73 | +0.062 | STANDARD |
| Lawson Crouse: 1+ assists | 0.272 | 0.190 | 20/82 | +0.061 | STANDARD |

**NYI @ LAK** · priced 133/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.98, exp saves 23.62 (sd 6.37), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.46, exp saves 24.61 (sd 6.69), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.149 | 0.355 | 36/65 | +0.185 | STANDARD |
| Mats Zuccarello: 1+ points | 0.313 | 0.475 | 48/53 | +0.140 | STANDARD |
| Mats Zuccarello: 2+ points | 0.058 | 0.155 | 17/86 | +0.074 | STANDARD |
| Alex Laferriere: 1+ points | 0.608 | 0.535 | 55/48 | +0.040 | STANDARD |
| Alex Laferriere: 1+ assists | 0.431 | 0.365 | 37/64 | +0.045 | STANDARD |
| Mats Zuccarello: 2+ assists | 0.011 | 0.075 | 9/94 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
