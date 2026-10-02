# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T13:40:41Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3068 · contracts joined: 754 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 629, 'OK': 75, 'NO_EDGE': 50}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 98, 'game_early_goal': 5, 'first_goal': 140, 'game_winner': 10, 'player_goals': 140, 'game_overtime': 5, 'player_points': 120, 'game_spread': 20, 'team_total': 50, 'game_total': 45, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 2026-10-02T22:30:00Z | T-6h | 0.558 | 0.442 | 0.178 | 5.99 | 3.18 | 2.82 | 171 (25/146) | PROJECTED/PROJECTED |
| WSH @ CAR | 2026-10-02T23:00:00Z | T-6h | 0.525 | 0.475 | 0.190 | 5.85 | 3.01 | 2.84 | 186 (25/161) | PROJECTED/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-6h | 0.493 | 0.507 | 0.182 | 5.78 | 2.87 | 2.91 | 174 (25/149) | PROJECTED/PROJECTED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-6h | 0.538 | 0.462 | 0.185 | 5.98 | 3.11 | 2.87 | 172 (25/147) | PROJECTED/PROJECTED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-12h | 0.596 | 0.404 | 0.172 | 6.42 | 3.51 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.538 | 0.635 | 0.616 | 64 | 37 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.310 | 0.405 | 0.385 | 41 | 60 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.190 | 0.275 | 0.256 | 28 | 73 | no | +0.066 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.462 | 0.375 | 0.392 | 38 | 63 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.330 | 0.405 | 0.390 | 41 | 60 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.390 | 0.465 | 0.450 | 47 | 54 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.206 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.607 | 0.685 | 0.670 | 70 | 33 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.248 | 0.185 | 0.196 | 19 | 82 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.496 | 0.570 | 0.555 | 58 | 44 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.367 | 0.440 | 0.425 | 45 | 57 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.585 | 0.650 | 0.637 | 66 | 36 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.729 | 0.785 | 0.774 | 79 | 22 | no | +0.039 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.475 | 0.415 | 0.427 | 42 | 59 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.239 | 0.295 | 0.283 | 30 | 71 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.388 | 0.445 | 0.433 | 45 | 56 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.481 | 0.535 | 0.524 | 54 | 47 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.821 | 0.870 | 0.861 | 88 | 14 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.178 | 0.225 | 0.215 | 23 | 78 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.718 | 0.765 | 0.756 | 77 | 24 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.688 | 0.740 | 0.730 | 75 | 27 | no | +0.029 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.404 | 0.355 | 0.365 | 36 | 65 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.813 | 0.860 | 0.852 | 87 | 15 | no | +0.028 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.525 | 0.575 | 0.565 | 58 | 43 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.190 | 0.240 | 0.229 | 25 | 77 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.297 | 0.345 | 0.335 | 35 | 66 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.558 | 0.610 | 0.600 | 62 | 40 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.142 | 0.105 | 0.112 | 11 | 90 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.212 | 0.260 | 0.250 | 27 | 75 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.146 | 0.185 | 0.177 | 19 | 82 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.381 | 0.425 | 0.416 | 43 | 58 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.167 | 0.210 | 0.201 | 22 | 80 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.283 | 0.335 | 0.324 | 35 | 68 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.800 | 0.840 | 0.833 | 85 | 17 | no | +0.020 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.507 | 0.465 | 0.473 | 47 | 54 | yes | +0.020 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.524 | 0.565 | 0.557 | 57 | 44 | no | +0.018 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.596 | 0.635 | 0.627 | 64 | 37 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.555 | 0.510 | 0.519 | 52 | 50 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.814 | 0.850 | 0.843 | 86 | 16 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.269 | 0.305 | 0.298 | 31 | 70 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.794 | 0.830 | 0.823 | 84 | 18 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.203 | 0.235 | 0.228 | 24 | 77 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.216 | 0.185 | 0.191 | 19 | 82 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.775 | 0.810 | 0.803 | 82 | 20 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.089 | 0.125 | 0.117 | 14 | 89 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.860 | 0.895 | 0.889 | 91 | 12 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.746 | 0.775 | 0.769 | 78 | 23 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.774 | 0.740 | 0.747 | 75 | 27 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.336 | 0.300 | 0.307 | 31 | 71 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT02NYRDET-NYR3 | game_spread | 0.132 | 0.155 | 0.150 | 16 | 85 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.415 | 0.445 | 0.439 | 45 | 56 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.834 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.166 | 0.140 | 0.145 | 15 | 87 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-10 | game_total | 0.059 | 0.075 | 0.071 | 8 | 93 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.951 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.486 | 0.515 | 0.509 | 52 | 49 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG6 | team_total | 0.069 | 0.090 | 0.085 | 10 | 92 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.598 | 0.625 | 0.620 | 63 | 38 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.290 | 0.315 | 0.310 | 32 | 69 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.136 | 0.155 | 0.151 | 16 | 85 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.122 | 0.105 | 0.108 | 11 | 90 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR6 | team_total | 0.080 | 0.100 | 0.096 | 11 | 91 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02STLDAL-9 | game_total | 0.156 | 0.175 | 0.171 | 18 | 83 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-10 | game_total | 0.062 | 0.075 | 0.072 | 8 | 93 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.207 | 0.230 | 0.225 | 24 | 78 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-10 | game_total | 0.102 | 0.115 | 0.112 | 12 | 89 | no | +0.001 | OK |
| KXNHLGAME-26OCT02NYRDET-DET | game_winner | 0.558 | 0.535 | 0.540 | 54 | 47 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT02NYRDET-5 | game_total | 0.747 | 0.770 | 0.766 | 78 | 24 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.141 | 0.165 | 0.160 | 18 | 85 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT02NYRDET-3 | game_total | 0.958 | 0.965 | 0.964 | 97 | 4 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-3 | game_total | 0.968 | 0.975 | 0.974 | 98 | 3 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-10 | game_total | 0.066 | 0.080 | 0.077 | 9 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT02WSHCAR-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 0.558 | 0.538 | 0.178 | 0.215 | 5.99 | 6.13 | 1.003/0.983 | KXNHLTEAMTOTAL-26OCT02NYRDET-NYR3 +0.033 |
| WSH @ CAR | 0.525 | 0.558 | 0.190 | 0.215 | 5.85 | 6.25 | 0.997/0.938 | KXNHLTOTAL-26OCT02WSHCAR-7 +0.074 |
| BOS @ WPG | 0.493 | 0.525 | 0.182 | 0.216 | 5.78 | 6.07 | 0.988/0.968 | KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 +0.061 |
| STL @ DAL | 0.538 | 0.546 | 0.185 | 0.220 | 5.98 | 6.13 | 0.986/0.993 | KXNHLTOTAL-26OCT02STLDAL-7 +0.032 |
| ANA @ VGK | 0.596 | 0.593 | 0.172 | 0.208 | 6.42 | 6.42 | 1.003/1.016 | KXNHLSPREAD-26OCT02ANAVGK-VGK3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Nate Danielson: 1+ goals YES @ 10c · p 0.129 (adj 0.1205) · $2.42 · thesis DET:OFFENSE_4PLUS
- Moritz Seider: 1+ goals NO @ 84c · p 0.8745 (adj 0.8646) · $13.86 · thesis DET:SUPPRESSED
- Sean Durzi: 1+ goals NO @ 91c · p 0.9347 (adj 0.926) · $13.86 · thesis NYR:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.8177 (adj 0.7444) · $7.78 · thesis NYR:SUPPRESSED
- William Carrier: 1+ goals YES @ 8c · p 0.1205 (adj 0.1091) · $4.16 · thesis CAR:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2285 (adj 0.2139) · $5.03 · thesis WSH:OFFENSE_4PLUS
- Mark Jankowski: 1+ goals NO @ 82c · p 0.8598 (adj 0.8486) · $14.36 · thesis CAR:SUPPRESSED
- Alex Tuch: 1+ assists NO @ 78c · p 0.8861 (adj 0.8106) · $14.36 · thesis WSH:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 18c · p 0.2314 (adj 0.216) · $4.19 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.8397 (adj 0.7456) · $11.72 · thesis BOS:SUPPRESSED
- Cole Perfetti: 1+ goals NO @ 73c · p 0.7757 (adj 0.763) · $10.29 · thesis WPG:SUPPRESSED
- Isak Rosen: 1+ goals NO @ 85c · p 0.8837 (adj 0.8728) · $11.72 · thesis WPG:SUPPRESSED
- Dallas wins NO @ 37c · p 0.4591 (adj 0.4121) · $6.58 · thesis STL:WINS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7344 (adj 0.7183) · $12.45 · thesis DAL:SUPPRESSED
- Mason McTavish: 1+ assists NO @ 77c · p 0.8801 (adj 0.7988) · $15.16 · thesis STL:SUPPRESSED
- Dylan Holloway: 1+ goals YES @ 27c · p 0.3078 (adj 0.2946) · $2.08 · thesis STL:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ DET** · priced 116/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 25.06, exp saves 21.87 (sd 6.13), pull risk 0.056
- NYR net: Dylan Garand (PROJECTED) exp shots 28.53, exp saves 24.54 (sd 6.7), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ assists | 0.182 | 0.295 | 31/72 | +0.084 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.413 | 0.510 | 52/50 | +0.069 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.103 | 0.170 | 20/86 | +0.029 | STANDARD |
| Gabe Perreault: 1+ assists | 0.298 | 0.235 | 26/79 | +0.025 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.280 | 0.340 | 36/68 | +0.025 | STANDARD |
| Gabe Perreault: 1+ points | 0.435 | 0.380 | 40/64 | +0.018 | STANDARD |

**WSH @ CAR** · priced 133/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.54, exp saves 20.54 (sd 5.92), pull risk 0.057
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.1 (sd 7.11), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.325 | 0.455 | 47/56 | +0.098 | STANDARD |
| Alex Tuch: 1+ assists | 0.114 | 0.230 | 24/78 | +0.094 | STANDARD |
| Sebastian Aho: 1+ points | 0.509 | 0.615 | 63/40 | +0.074 | STANDARD |
| Sebastian Aho: 2+ points | 0.163 | 0.255 | 28/77 | +0.054 | STANDARD |
| Tom Wilson: 1+ assists | 0.336 | 0.255 | 27/76 | +0.052 | STANDARD |
| Alex Tuch: 1+ points | 0.342 | 0.420 | 44/60 | +0.041 | STANDARD |

**BOS @ WPG** · priced 123/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.1, exp saves 22.68 (sd 6.22), pull risk 0.056
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.24, exp saves 24.33 (sd 6.61), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ assists | 0.160 | 0.305 | 32/71 | +0.115 | STANDARD |
| JJ Peterka: 1+ points | 0.346 | 0.480 | 50/54 | +0.097 | STANDARD |
| Elias Lindholm: 1+ points | 0.498 | 0.395 | 41/62 | +0.071 | STANDARD |
| JJ Peterka: 2+ points | 0.066 | 0.140 | 17/89 | +0.038 | STANDARD |
| Elias Lindholm: 1+ assists | 0.346 | 0.275 | 30/75 | +0.032 | STANDARD |
| Elias Lindholm: 1+ goals | 0.231 | 0.170 | 18/84 | +0.041 | STANDARD |

**STL @ DAL** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.53, exp saves 21.43 (sd 5.95), pull risk 0.051
- STL net: Joel Hofer (PROJECTED) exp shots 26.73, exp saves 22.86 (sd 6.4), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.292 | 0.420 | 44/60 | +0.091 | STANDARD |
| Mason McTavish: 1+ assists | 0.120 | 0.245 | 26/77 | +0.098 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.600 | 62/42 | +0.081 | STANDARD |
| Jason Robertson: 1+ assists | 0.385 | 0.500 | 52/52 | +0.077 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.401 | 0.515 | 53/50 | +0.081 | STANDARD |
| Mason McTavish: 1+ points | 0.292 | 0.400 | 42/62 | +0.071 | STANDARD |

**ANA @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 28.77, exp saves 25.13 (sd 6.71), pull risk 0.055
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.59, exp saves 23.42 (sd 6.74), pull risk 0.078

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
