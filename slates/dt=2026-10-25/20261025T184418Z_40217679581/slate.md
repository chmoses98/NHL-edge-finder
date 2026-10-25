# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T18:44:18Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3061 · contracts joined: 1149 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1024, 'OK': 95, 'NO_EDGE': 30}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 169, 'game_early_goal': 5, 'first_goal': 182, 'game_winner': 10, 'player_goals': 312, 'game_overtime': 5, 'player_points': 225, 'goalie_saves': 6, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 2026-10-25T19:00:00Z | T-10m | 0.501 | 0.499 | 0.180 | 6.00 | 3.00 | 3.00 | 229 (25/204) | CONFIRMED/CONFIRMED |
| NYI @ DAL | 2026-10-25T22:00:00Z | T-3h | 0.552 | 0.448 | 0.187 | 5.45 | 2.89 | 2.57 | 226 (25/201) | PROJECTED/PROBABLE |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-3h | 0.464 | 0.536 | 0.180 | 5.94 | 2.87 | 3.07 | 229 (25/204) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-3h | 0.373 | 0.627 | 0.168 | 6.00 | 2.60 | 3.40 | 237 (25/212) | PROBABLE/PROBABLE |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-6h | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT25FLACHI-CHI | game_winner | 0.501 | 0.365 | 0.391 | 37 | 64 | yes | +0.115 | OK |
| KXNHLGAME-26OCT25FLACHI-FLA | game_winner | 0.499 | 0.635 | 0.609 | 64 | 37 | no | +0.115 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA2 | game_spread | 0.283 | 0.415 | 0.387 | 42 | 59 | no | +0.110 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA4 | team_total | 0.365 | 0.500 | 0.472 | 51 | 51 | no | +0.108 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 | team_total | 0.581 | 0.705 | 0.682 | 71 | 30 | no | +0.104 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA3 | game_spread | 0.166 | 0.285 | 0.258 | 29 | 72 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.454 | 0.570 | 0.547 | 58 | 44 | no | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA5 | team_total | 0.188 | 0.300 | 0.275 | 31 | 71 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.335 | 0.435 | 0.414 | 44 | 57 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.257 | 0.360 | 0.338 | 37 | 65 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.673 | 0.770 | 0.752 | 78 | 24 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.417 | 0.320 | 0.339 | 33 | 69 | yes | +0.072 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.552 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.448 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.186 | 0.275 | 0.255 | 28 | 73 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.533 | 0.625 | 0.607 | 63 | 38 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.750 | 0.835 | 0.820 | 84 | 17 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.627 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.256 | 0.345 | 0.326 | 35 | 66 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA2 | team_total | 0.794 | 0.875 | 0.861 | 88 | 13 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI2 | game_spread | 0.278 | 0.195 | 0.210 | 20 | 81 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.150 | 0.165 | 16 | 86 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.416 | 0.505 | 0.487 | 51 | 50 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.565 | 0.650 | 0.634 | 66 | 36 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.837 | 0.910 | 0.898 | 92 | 10 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.163 | 0.240 | 0.223 | 25 | 77 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.231 | 0.305 | 0.289 | 31 | 70 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.223 | 0.300 | 0.283 | 31 | 71 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.552 | 0.625 | 0.611 | 63 | 38 | no | +0.051 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.448 | 0.375 | 0.389 | 38 | 63 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.119 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.783 | 0.850 | 0.838 | 86 | 16 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA6 | team_total | 0.082 | 0.140 | 0.126 | 15 | 87 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4 | team_total | 0.365 | 0.305 | 0.317 | 31 | 70 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.855 | 0.910 | 0.901 | 92 | 10 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI3 | game_spread | 0.166 | 0.115 | 0.124 | 12 | 89 | yes | +0.038 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.038 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.351 | 0.295 | 0.306 | 30 | 71 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT25FLACHI-6 | game_total | 0.527 | 0.585 | 0.574 | 59 | 42 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.670 | 0.725 | 0.715 | 73 | 28 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.060 | 0.068 | 7 | 95 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT25FLACHI-5 | game_total | 0.744 | 0.795 | 0.785 | 80 | 21 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI3 | team_total | 0.581 | 0.525 | 0.536 | 53 | 48 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.770 | 0.781 | 78 | 24 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT25FLACHI-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI5 | team_total | 0.188 | 0.145 | 0.153 | 15 | 86 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.095 | 0.102 | 10 | 91 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.210 | 0.219 | 22 | 80 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.320 | 0.365 | 0.356 | 37 | 64 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.071 | 0.110 | 0.101 | 12 | 90 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.110 | 0.117 | 12 | 90 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.430 | 0.475 | 0.466 | 48 | 53 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI2 | team_total | 0.793 | 0.755 | 0.763 | 76 | 25 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT25FLACHI-7 | game_total | 0.414 | 0.455 | 0.447 | 46 | 55 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI6 | team_total | 0.082 | 0.055 | 0.060 | 6 | 95 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.067 | 0.100 | 0.092 | 11 | 91 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.122 | 0.095 | 0.100 | 10 | 91 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-10 | game_total | 0.041 | 0.065 | 0.059 | 7 | 94 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25FLACHI-8 | game_total | 0.232 | 0.265 | 0.258 | 27 | 74 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.530 | 0.522 | 54 | 48 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 | team_total | 0.334 | 0.365 | 0.359 | 37 | 64 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.620 | 0.627 | 63 | 39 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-8 | game_total | 0.160 | 0.190 | 0.184 | 20 | 82 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.780 | 0.810 | 0.804 | 82 | 20 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.937 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25FLACHI-3 | game_total | 0.959 | 0.975 | 0.972 | 98 | 3 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25FLACHI-9 | game_total | 0.162 | 0.185 | 0.180 | 19 | 82 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.143 | 0.170 | 0.164 | 18 | 84 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.730 | 0.724 | 74 | 28 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH3 | team_total | 0.486 | 0.515 | 0.509 | 52 | 49 | no | +0.007 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 0.501 | 0.483 | 0.180 | 0.221 | 6.00 | 6.24 | 0.987/0.991 | KXNHLTOTAL-26OCT25FLACHI-7 +0.049 |
| NYI @ DAL | 0.552 | 0.549 | 0.187 | 0.221 | 5.45 | 6.00 | 0.986/0.951 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.101 |
| MTL @ WPG | 0.464 | 0.481 | 0.180 | 0.222 | 5.94 | 6.25 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.053 |
| COL @ NSH | 0.373 | 0.394 | 0.168 | 0.214 | 6.00 | 6.46 | 0.991/0.972 | KXNHLTOTAL-26OCT25COLNSH-7 +0.079 |
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Sam Reinhart: 1+ goals NO @ 65c · p 0.7374 (adj 0.7143) · $12.57 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 61c · p 0.6963 (adj 0.6735) · $12.57 · thesis FLA:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 23c · p 0.2924 (adj 0.2756) · $7.68 · thesis CHI:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 10c · p 0.1479 (adj 0.1272) · $3.72 · thesis FLA:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 16c · p 0.2276 (adj 0.2094) · $9.33 · thesis NYI:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.16 (adj 0.1462) · $4.12 · thesis NYI:OFFENSE_4PLUS
- Victor Eklund: 1+ goals YES @ 16c · p 0.2016 (adj 0.1875) · $4.27 · thesis NYI:OFFENSE_4PLUS
- David Perron: 1+ goals YES @ 13c · p 0.1633 (adj 0.1537) · $3.86 · thesis DAL:OFFENSE_4PLUS
- Alexandre Carrier: 1+ goals YES @ 4c · p 0.0677 (adj 0.0583) · $2.79 · thesis MTL:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 4c · p 0.061 (adj 0.0532) · $1.95 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3351 (adj 0.3226) · $5.23 · thesis WPG:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 11c · p 0.1407 (adj 0.1293) · $2.73 · thesis MTL:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 79c · p 0.8662 (adj 0.8206) · $15.07 · thesis NSH:SUPPRESSED
- Taylor Makar: 1+ goals NO @ 91c · p 0.9368 (adj 0.9276) · $15.07 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 53c · p 0.609 (adj 0.567) · $5.26 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7324 (adj 0.6937) · $6.49 · thesis GAME:TIGHT
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2236 (adj 0.2039) · $7.91 · thesis VAN:OFFENSE_4PLUS
- Matt Boldy: 1+ goals NO @ 58c · p 0.6593 (adj 0.6382) · $16.76 · thesis MIN:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2315 (adj 0.2174) · $6.6 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2411 (adj 0.2258) · $6.0 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CHI** · priced 175/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 28.49, exp saves 24.46 (sd 6.73), pull risk 0.062
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.46, exp saves 21.2 (sd 5.96), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.487 | 0.615 | 62/39 | +0.107 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.319 | 0.445 | 45/56 | +0.104 | STANDARD |
| Brady Tkachuk: 1+ points | 0.525 | 0.645 | 65/36 | +0.099 | STANDARD |
| Seth Jones: 1+ points | 0.425 | 0.535 | 54/47 | +0.087 | STANDARD |
| Sam Reinhart: 1+ assists | 0.302 | 0.410 | 42/60 | +0.081 | STANDARD |
| Patrick Kane: 1+ assists | 0.325 | 0.430 | 44/58 | +0.078 | STANDARD |

**NYI @ DAL** · priced 170/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.18 (sd 6.11), pull risk 0.047
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.22, exp saves 22.68 (sd 6.22), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.272 | 0.125 | 21/96 | +0.050 | STANDARD |
| Ilya Sorokin: 25+ saves | 0.370 | 0.225 | 43/98 | -0.077 |  |
| Nils Lundkvist: 1+ assists | 0.232 | 0.100 | 18/98 | +0.042 | STANDARD |
| Logan Stanley: 1+ points | 0.278 | 0.155 | 26/95 | +0.004 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.426 | 0.515 | 53/50 | +0.057 | STANDARD |
| Miro Heiskanen: 1+ points | 0.490 | 0.575 | 60/45 | +0.043 | STANDARD |

**MTL @ WPG** · priced 174/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.39), pull risk 0.059
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.54, exp saves 23.94 (sd 6.53), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Samberg: 1+ assists | 0.265 | 0.125 | 23/98 | +0.023 | STANDARD |
| Kaiden Guhle: 1+ assists | 0.236 | 0.130 | 24/98 | -0.017 | STANDARD |
| Oliver Kapanen: 1+ points | 0.366 | 0.455 | 46/55 | +0.066 | STANDARD |
| Alex Iafallo: 1+ goals | 0.170 | 0.090 | 13/95 | +0.032 | STANDARD |
| Zachary Bolduc: 1+ points | 0.407 | 0.330 | 37/71 | +0.020 | STANDARD |
| Cole Perfetti: 2+ points | 0.188 | 0.115 | 17/94 | +0.008 | STANDARD |

**COL @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROBABLE) exp shots 32.01, exp saves 27.18 (sd 7.46), pull risk 0.085
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.47, exp saves 23.19 (sd 6.3), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Cale Makar: 1+ assists | 0.459 | 0.555 | 57/46 | +0.063 | STANDARD |
| Cale Makar: 2+ points | 0.193 | 0.285 | 31/74 | +0.054 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.134 | 0.225 | 24/79 | +0.065 | STANDARD |
| Alexander Kerfoot: 1+ assists | 0.207 | 0.130 | 24/98 | -0.046 | STANDARD |

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 22+ saves | 0.545 | 0.270 | 49/95 | +0.037 |  |
| Liam Ohgren: 1+ points | 0.381 | 0.175 | 31/96 | +0.056 | STANDARD |
| Yakov Trenin: 1+ points | 0.305 | 0.145 | 27/98 | +0.021 | STANDARD |
| Liam Ohgren: 1+ assists | 0.264 | 0.115 | 21/98 | +0.042 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.268 | 0.410 | 43/61 | +0.105 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.655 | 67/36 | +0.105 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
