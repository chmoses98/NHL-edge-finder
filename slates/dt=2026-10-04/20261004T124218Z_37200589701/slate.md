# NHL slate 2026-10-04 — RESEARCH_ONLY

generated 2026-10-04T12:42:18Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2661 · contracts joined: 706 (unjoined to any game: 1554)
gates: {'UNSUPPORTED': 581, 'OK': 75, 'NO_EDGE': 50}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 85, 'game_early_goal': 5, 'first_goal': 120, 'game_winner': 10, 'player_goals': 135, 'game_overtime': 5, 'player_points': 111, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ DET | 2026-10-04T17:00:00Z | T-3h | 0.560 | 0.440 | 0.182 | 5.89 | 3.12 | 2.78 | 128 (25/103) | PROJECTED/PROJECTED |
| UTA @ NYR | 2026-10-04T22:00:00Z | T-6h | 0.558 | 0.442 | 0.174 | 6.22 | 3.29 | 2.92 | 172 (25/147) | PROJECTED/PROJECTED |
| FLA @ ANA | 2026-10-05T00:00:00Z | T-6h | 0.563 | 0.437 | 0.170 | 6.63 | 3.52 | 3.11 | 184 (25/159) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-10-05T00:00:00Z | T-6h | 0.540 | 0.460 | 0.181 | 5.92 | 3.08 | 2.84 | 171 (25/146) | PROJECTED/PROJECTED |
| VGK @ VAN | 2026-10-05T01:00:00Z | T-12h | 0.410 | 0.590 | 0.164 | 6.78 | 3.09 | 3.69 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3 | team_total | 0.599 | 0.470 | 0.496 | 48 | 54 | yes | +0.101 | OK |
| KXNHLGAME-26OCT04FLAANA-ANA | game_winner | 0.563 | 0.445 | 0.469 | 45 | 56 | yes | +0.096 | OK |
| KXNHLGAME-26OCT04FLAANA-FLA | game_winner | 0.437 | 0.555 | 0.531 | 56 | 45 | no | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4 | team_total | 0.387 | 0.265 | 0.287 | 28 | 75 | yes | +0.093 | OK |
| KXNHLGAME-26OCT04VGKVAN-VGK | game_winner | 0.590 | 0.695 | 0.675 | 70 | 31 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA2 | game_spread | 0.351 | 0.255 | 0.273 | 26 | 75 | yes | +0.077 | OK |
| KXNHLGAME-26OCT04VGKVAN-VAN | game_winner | 0.410 | 0.315 | 0.333 | 32 | 69 | yes | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5 | team_total | 0.209 | 0.120 | 0.135 | 13 | 89 | yes | +0.071 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA3 | game_spread | 0.143 | 0.225 | 0.206 | 23 | 78 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN2 | game_spread | 0.223 | 0.145 | 0.159 | 15 | 86 | yes | +0.064 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2 | game_spread | 0.379 | 0.465 | 0.447 | 47 | 54 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA2 | game_spread | 0.243 | 0.325 | 0.308 | 33 | 68 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3 | team_total | 0.595 | 0.675 | 0.660 | 68 | 33 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA3 | game_spread | 0.227 | 0.155 | 0.168 | 16 | 85 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK3 | game_spread | 0.249 | 0.325 | 0.309 | 33 | 68 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-7 | game_total | 0.542 | 0.460 | 0.476 | 47 | 55 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2 | team_total | 0.804 | 0.725 | 0.742 | 74 | 29 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4 | team_total | 0.477 | 0.395 | 0.411 | 41 | 62 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-8 | game_total | 0.344 | 0.275 | 0.288 | 28 | 73 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4 | team_total | 0.385 | 0.455 | 0.441 | 46 | 55 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5 | team_total | 0.288 | 0.215 | 0.228 | 23 | 80 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-6 | game_total | 0.650 | 0.580 | 0.594 | 59 | 43 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-9 | game_total | 0.254 | 0.195 | 0.206 | 20 | 81 | yes | +0.043 | OK |
| KXNHLGAME-26OCT04WPGDET-DET | game_winner | 0.560 | 0.495 | 0.508 | 50 | 51 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN6 | team_total | 0.094 | 0.040 | 0.048 | 5 | 97 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 | team_total | 0.686 | 0.615 | 0.630 | 63 | 40 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5 | team_total | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.035 | OK |
| KXNHLGAME-26OCT04WPGDET-WPG | game_winner | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG3 | team_total | 0.531 | 0.585 | 0.574 | 59 | 42 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT04WPGDET-WPG2 | game_spread | 0.234 | 0.285 | 0.274 | 29 | 72 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN3 | game_spread | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA6 | team_total | 0.147 | 0.095 | 0.104 | 11 | 92 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT04WPGDET-WPG3 | game_spread | 0.131 | 0.175 | 0.165 | 18 | 83 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-5 | game_total | 0.830 | 0.785 | 0.795 | 79 | 22 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-10 | game_total | 0.134 | 0.095 | 0.102 | 10 | 91 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG4 | team_total | 0.316 | 0.370 | 0.359 | 38 | 64 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT04WPGDET-DET2 | game_spread | 0.329 | 0.285 | 0.294 | 29 | 72 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA2 | team_total | 0.808 | 0.855 | 0.846 | 87 | 16 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT04CGYSEA-SEA3 | game_spread | 0.185 | 0.225 | 0.217 | 23 | 78 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG2 | team_total | 0.759 | 0.805 | 0.796 | 82 | 21 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA2 | team_total | 0.859 | 0.815 | 0.825 | 83 | 20 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG5 | team_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT04UTANYR-6 | game_total | 0.563 | 0.525 | 0.533 | 53 | 48 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-8 | game_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-10 | game_total | 0.088 | 0.065 | 0.069 | 7 | 94 | yes | +0.013 | OK |
| KXNHLGAME-26OCT04CGYSEA-SEA | game_winner | 0.540 | 0.575 | 0.568 | 58 | 43 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT04UTANYR-9 | game_total | 0.182 | 0.155 | 0.160 | 16 | 85 | yes | +0.012 | OK |
| KXNHLSPREAD-26OCT04CGYSEA-CGY2 | game_spread | 0.243 | 0.215 | 0.221 | 22 | 79 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT04FLAANA-8 | game_total | 0.326 | 0.295 | 0.301 | 30 | 71 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT04CGYSEA-SEA2 | game_spread | 0.314 | 0.350 | 0.343 | 36 | 66 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT04UTANYR-7 | game_total | 0.447 | 0.410 | 0.417 | 42 | 60 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR3 | team_total | 0.646 | 0.610 | 0.617 | 62 | 40 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR5 | team_total | 0.241 | 0.210 | 0.216 | 22 | 80 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET3 | team_total | 0.616 | 0.585 | 0.591 | 59 | 42 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA4 | team_total | 0.384 | 0.425 | 0.417 | 44 | 59 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR6 | team_total | 0.113 | 0.090 | 0.094 | 10 | 92 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET4 | team_total | 0.393 | 0.365 | 0.371 | 37 | 64 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA6 | team_total | 0.098 | 0.120 | 0.115 | 13 | 89 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET5 | team_total | 0.206 | 0.185 | 0.189 | 19 | 82 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT04WPGDET-DET3 | game_spread | 0.195 | 0.175 | 0.179 | 18 | 83 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-3 | game_total | 0.976 | 0.965 | 0.968 | 97 | 4 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG6 | team_total | 0.061 | 0.075 | 0.072 | 8 | 93 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT04WPGDET-5 | game_total | 0.733 | 0.760 | 0.755 | 77 | 25 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT04WPGDET-3 | game_total | 0.954 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT04WPGDET-4 | game_total | 0.827 | 0.850 | 0.846 | 86 | 16 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT04WPGDET-6 | game_total | 0.510 | 0.535 | 0.530 | 54 | 47 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-4 | game_total | 0.899 | 0.880 | 0.884 | 89 | 13 | yes | +0.003 | OK |
| KXNHLGAME-26OCT04CGYSEA-CGY | game_winner | 0.460 | 0.435 | 0.440 | 44 | 57 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET6 | team_total | 0.087 | 0.075 | 0.077 | 8 | 93 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY6 | team_total | 0.065 | 0.055 | 0.057 | 6 | 95 | yes | +0.002 | OK |
| KXNHLGAME-26OCT04UTANYR-NYR | game_winner | 0.558 | 0.535 | 0.540 | 54 | 47 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA5 | team_total | 0.198 | 0.220 | 0.215 | 23 | 79 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-UTA6 | team_total | 0.075 | 0.060 | 0.063 | 7 | 95 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-2 | game_total | 0.982 | 0.975 | 0.977 | 98 | 3 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-2 | game_total | 0.991 | 0.980 | 0.983 | 99 | 3 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA2 | team_total | 0.810 | 0.835 | 0.830 | 85 | 18 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 | team_total | 0.513 | 0.545 | 0.539 | 56 | 47 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA3 | team_total | 0.604 | 0.635 | 0.629 | 65 | 38 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT04UTANYR-4 | game_total | 0.858 | 0.845 | 0.848 | 85 | 16 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-CGY3 | game_spread | 0.137 | 0.125 | 0.127 | 13 | 88 |  | -0.001 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ DET | 0.560 | 0.540 | 0.182 | 0.221 | 5.89 | 6.02 | 1.003/0.988 | KXNHLTEAMTOTAL-26OCT04WPGDET-WPG3 +0.032 |
| UTA @ NYR | 0.558 | 0.550 | 0.174 | 0.217 | 6.22 | 6.31 | 0.957/0.992 | KXNHLTOTAL-26OCT04UTANYR-7 +0.023 |
| FLA @ ANA | 0.563 | 0.573 | 0.170 | 0.217 | 6.63 | 6.59 | 1.024/0.998 | KXNHLSPREAD-26OCT04FLAANA-FLA2 -0.019 |
| CGY @ SEA | 0.540 | 0.580 | 0.181 | 0.222 | 5.92 | 6.05 | 1.005/0.986 | KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA3 +0.044 |
| VGK @ VAN | 0.410 | 0.427 | 0.164 | 0.209 | 6.78 | 6.33 | 1.025/1.003 | KXNHLTOTAL-26OCT04VGKVAN-8 -0.072 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Neal Pionk: 1+ goals NO @ 90c · p 0.9396 (adj 0.9284) · $13.5 · thesis WPG:SUPPRESSED
- Cole Perfetti: 1+ goals NO @ 73c · p 0.7901 (adj 0.7738) · $13.5 · thesis WPG:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 14c · p 0.1752 (adj 0.1639) · $3.87 · thesis DET:OFFENSE_4PLUS
- Tye Kartye: 1+ goals YES @ 10c · p 0.1419 (adj 0.1289) · $5.23 · thesis NYR:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 70c · p 0.8492 (adj 0.7425) · $18.0 · thesis UTA:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 71c · p 0.7856 (adj 0.7378) · $12.84 · thesis NYR:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 19c · p 0.2665 (adj 0.2461) · $11.53 · thesis ANA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 65c · p 0.7134 (adj 0.6938) · $18.0 · thesis FLA:SUPPRESSED
- Alex Killorn: 1+ assists YES @ 24c · p 0.3736 (adj 0.277) · $5.32 · thesis ANA:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 12c · p 0.1527 (adj 0.1408) · $3.27 · thesis FLA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1648 (adj 0.1498) · $5.27 · thesis SEA:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 86c · p 0.8925 (adj 0.8806) · $18.0 · thesis SEA:SUPPRESSED
- Vancouver wins by over 1.5 goals YES @ 15c · p 0.2257 (adj 0.1854) · $4.67 · thesis VAN:WINS_BY_2PLUS
- Vegas wins by over 2.5 goals NO @ 68c · p 0.7704 (adj 0.7227) · $17.01 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ DET** · priced 76/77 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 26.21, exp saves 22.92 (sd 6.23), pull risk 0.052
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.88, exp saves 24.07 (sd 6.6), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Neal Pionk: 1+ points | 0.283 | 0.350 | 37/67 | +0.031 | STANDARD |
| Cole Perfetti: 1+ goals | 0.210 | 0.275 | 28/73 | +0.046 | STANDARD |
| Mark Scheifele: 1+ assists | 0.440 | 0.505 | 52/51 | +0.033 | STANDARD |
| Josh Morrissey: 2+ points | 0.122 | 0.175 | 19/84 | +0.028 | STANDARD |
| Josh Morrissey: 1+ points | 0.464 | 0.515 | 53/50 | +0.018 | STANDARD |
| Kyle Connor: 1+ assists | 0.397 | 0.445 | 46/57 | +0.016 | STANDARD |

**UTA @ NYR** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.44, exp saves 23.89 (sd 6.51), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.14, exp saves 21.62 (sd 6.09), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.151 | 0.315 | 33/70 | +0.135 | STANDARD |
| Vincent Trocheck: 1+ points | 0.314 | 0.430 | 45/59 | +0.079 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.214 | 0.310 | 33/71 | +0.061 | STANDARD |
| Clayton Keller: 2+ points | 0.219 | 0.140 | 25/97 | -0.044 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.464 | 0.540 | 56/48 | +0.039 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.130 | 0.200 | 22/82 | +0.040 | STANDARD |

**FLA @ ANA** · priced 129/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.07, exp saves 22.87 (sd 6.15), pull risk 0.057
- FLA net: Akira Schmid (PROJECTED) exp shots 29.88, exp saves 25.44 (sd 7.09), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ assists | 0.374 | 0.225 | 24/79 | +0.121 | STANDARD |
| Alex Killorn: 1+ points | 0.529 | 0.385 | 41/64 | +0.102 | STANDARD |
| Carter Verhaeghe: 1+ assists | 0.369 | 0.255 | 27/76 | +0.085 | STANDARD |
| Aaron Ekblad: 1+ assists | 0.337 | 0.230 | 25/79 | +0.074 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.567 | 0.465 | 49/56 | +0.060 | STANDARD |
| Jackson LaCombe: 1+ points | 0.636 | 0.540 | 56/48 | +0.059 | STANDARD |

**CGY @ SEA** · priced 118/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.8, exp saves 24.46 (sd 6.56), pull risk 0.046
- CGY net: Devin Cooley (PROJECTED) exp shots 28.47, exp saves 24.45 (sd 6.75), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Simon Nemec: 1+ assists | 0.185 | 0.265 | 29/76 | +0.042 | STANDARD |
| Jared McCann: 1+ points | 0.484 | 0.560 | 58/46 | +0.039 | STANDARD |
| Jared McCann: 2+ points | 0.139 | 0.205 | 23/82 | +0.031 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.131 | 0.065 | 12/99 | +0.004 | STANDARD |
| Matty Beniers: 1+ assists | 0.356 | 0.295 | 31/72 | +0.031 | STANDARD |
| Ryan Winterton: 1+ goals | 0.165 | 0.105 | 12/91 | +0.037 | STANDARD |

**VGK @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.79, exp saves 24.64 (sd 6.83), pull risk 0.072
- VGK net: Carter Hart (PROJECTED) exp shots 25.38, exp saves 22.18 (sd 6.09), pull risk 0.052

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
