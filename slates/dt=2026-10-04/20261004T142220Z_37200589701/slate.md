# NHL slate 2026-10-04 — RESEARCH_ONLY

generated 2026-10-04T14:22:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2779 · contracts joined: 824 (unjoined to any game: 1554)
gates: {'UNSUPPORTED': 699, 'OK': 85, 'NO_EDGE': 40}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 109, 'game_early_goal': 5, 'first_goal': 153, 'game_winner': 10, 'player_goals': 168, 'game_overtime': 5, 'player_points': 139, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ DET | 2026-10-04T17:00:00Z | T-90m | 0.560 | 0.440 | 0.182 | 5.89 | 3.12 | 2.78 | 128 (25/103) | PROJECTED/PROJECTED |
| UTA @ NYR | 2026-10-04T22:00:00Z | T-6h | 0.558 | 0.442 | 0.174 | 6.22 | 3.29 | 2.92 | 172 (25/147) | PROJECTED/PROJECTED |
| FLA @ ANA | 2026-10-05T00:00:00Z | T-6h | 0.576 | 0.424 | 0.167 | 6.73 | 3.63 | 3.10 | 184 (25/159) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-10-05T00:00:00Z | T-6h | 0.586 | 0.414 | 0.173 | 6.20 | 3.37 | 2.83 | 171 (25/146) | PROJECTED/PROJECTED |
| VGK @ VAN | 2026-10-05T01:00:00Z | T-6h | 0.418 | 0.582 | 0.166 | 6.74 | 3.10 | 3.64 | 169 (25/144) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3 | team_total | 0.602 | 0.460 | 0.489 | 47 | 55 | yes | +0.114 | OK |
| KXNHLGAME-26OCT04FLAANA-ANA | game_winner | 0.576 | 0.445 | 0.471 | 45 | 56 | yes | +0.109 | OK |
| KXNHLGAME-26OCT04FLAANA-FLA | game_winner | 0.424 | 0.555 | 0.529 | 56 | 45 | no | +0.109 | OK |
| KXNHLGAME-26OCT04VGKVAN-VAN | game_winner | 0.418 | 0.295 | 0.318 | 30 | 71 | yes | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4 | team_total | 0.387 | 0.255 | 0.279 | 27 | 76 | yes | +0.103 | OK |
| KXNHLGAME-26OCT04VGKVAN-VGK | game_winner | 0.582 | 0.695 | 0.674 | 70 | 31 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA2 | game_spread | 0.365 | 0.255 | 0.275 | 26 | 75 | yes | +0.091 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2 | game_spread | 0.368 | 0.475 | 0.453 | 48 | 53 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4 | team_total | 0.501 | 0.395 | 0.416 | 40 | 61 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5 | team_total | 0.309 | 0.215 | 0.232 | 22 | 79 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK3 | game_spread | 0.238 | 0.335 | 0.314 | 34 | 67 | no | +0.076 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA3 | game_spread | 0.245 | 0.155 | 0.171 | 16 | 85 | yes | +0.076 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA2 | game_spread | 0.230 | 0.325 | 0.304 | 33 | 68 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA3 | game_spread | 0.133 | 0.225 | 0.204 | 23 | 78 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5 | team_total | 0.209 | 0.115 | 0.130 | 13 | 90 | yes | +0.071 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN2 | game_spread | 0.226 | 0.145 | 0.159 | 15 | 86 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 | team_total | 0.704 | 0.610 | 0.630 | 62 | 40 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2 | team_total | 0.805 | 0.715 | 0.735 | 73 | 30 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3 | team_total | 0.596 | 0.675 | 0.660 | 68 | 33 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-7 | game_total | 0.535 | 0.455 | 0.471 | 46 | 55 | yes | +0.057 | OK |
| KXNHLGAME-26OCT04WPGDET-DET | game_winner | 0.560 | 0.485 | 0.500 | 49 | 52 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-6 | game_total | 0.646 | 0.575 | 0.590 | 58 | 43 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA6 | team_total | 0.163 | 0.095 | 0.106 | 11 | 92 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-8 | game_total | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLGAME-26OCT04WPGDET-WPG | game_winner | 0.440 | 0.505 | 0.492 | 51 | 50 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN6 | team_total | 0.094 | 0.040 | 0.048 | 5 | 97 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4 | team_total | 0.383 | 0.450 | 0.436 | 46 | 56 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5 | team_total | 0.210 | 0.265 | 0.253 | 27 | 74 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN3 | game_spread | 0.131 | 0.085 | 0.093 | 9 | 92 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-9 | game_total | 0.246 | 0.195 | 0.205 | 20 | 81 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG3 | team_total | 0.531 | 0.585 | 0.574 | 59 | 42 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT04WPGDET-WPG2 | game_spread | 0.234 | 0.285 | 0.274 | 29 | 72 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG2 | team_total | 0.759 | 0.810 | 0.800 | 82 | 20 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA2 | team_total | 0.870 | 0.815 | 0.827 | 83 | 20 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-5 | game_total | 0.831 | 0.785 | 0.795 | 79 | 22 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT04WPGDET-WPG3 | game_spread | 0.131 | 0.175 | 0.165 | 18 | 83 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG4 | team_total | 0.316 | 0.370 | 0.359 | 38 | 64 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT04UTANYR-6 | game_total | 0.563 | 0.515 | 0.525 | 52 | 49 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA2 | team_total | 0.805 | 0.855 | 0.846 | 87 | 16 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT04WPGDET-DET2 | game_spread | 0.329 | 0.285 | 0.294 | 29 | 72 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-10 | game_total | 0.128 | 0.095 | 0.101 | 10 | 91 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT04FLAANA-8 | game_total | 0.336 | 0.295 | 0.303 | 30 | 71 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT04UTANYR-7 | game_total | 0.447 | 0.405 | 0.413 | 41 | 60 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR5 | team_total | 0.241 | 0.205 | 0.212 | 21 | 80 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG5 | team_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-8 | game_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-8 | game_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 | team_total | 0.507 | 0.550 | 0.541 | 56 | 46 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA6 | team_total | 0.098 | 0.125 | 0.119 | 13 | 88 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR4 | team_total | 0.431 | 0.390 | 0.398 | 40 | 62 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT04WPGDET-5 | game_total | 0.733 | 0.765 | 0.759 | 77 | 24 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT04WPGDET-4 | game_total | 0.827 | 0.855 | 0.850 | 86 | 15 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT04UTANYR-10 | game_total | 0.088 | 0.065 | 0.069 | 7 | 94 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT04UTANYR-9 | game_total | 0.182 | 0.155 | 0.160 | 16 | 85 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-6 | game_total | 0.558 | 0.525 | 0.532 | 53 | 48 | yes | +0.011 | OK |
| KXNHLGAME-26OCT04UTANYR-NYR | game_winner | 0.558 | 0.525 | 0.532 | 53 | 48 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-9 | game_total | 0.180 | 0.150 | 0.156 | 16 | 86 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR3 | team_total | 0.646 | 0.610 | 0.617 | 62 | 40 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA5 | team_total | 0.251 | 0.220 | 0.226 | 23 | 79 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET3 | team_total | 0.616 | 0.585 | 0.591 | 59 | 42 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT04UTANYR-UTA3 | game_spread | 0.134 | 0.155 | 0.150 | 16 | 85 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR6 | team_total | 0.113 | 0.090 | 0.094 | 10 | 92 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5 | team_total | 0.308 | 0.335 | 0.330 | 34 | 67 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA6 | team_total | 0.123 | 0.100 | 0.104 | 11 | 91 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT04FLAANA-9 | game_total | 0.248 | 0.220 | 0.226 | 23 | 79 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK3 | team_total | 0.710 | 0.740 | 0.734 | 75 | 27 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET5 | team_total | 0.206 | 0.185 | 0.189 | 19 | 82 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT04UTANYR-5 | game_total | 0.778 | 0.755 | 0.760 | 76 | 25 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT04WPGDET-DET3 | game_spread | 0.195 | 0.175 | 0.179 | 18 | 83 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-5 | game_total | 0.777 | 0.755 | 0.760 | 76 | 25 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT04FLAANA-6 | game_total | 0.641 | 0.615 | 0.620 | 62 | 39 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG6 | team_total | 0.061 | 0.075 | 0.072 | 8 | 93 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-2 | game_total | 0.985 | 0.975 | 0.977 | 98 | 3 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT04WPGDET-3 | game_total | 0.954 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY6 | team_total | 0.067 | 0.055 | 0.057 | 6 | 95 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT04WPGDET-6 | game_total | 0.510 | 0.535 | 0.530 | 54 | 47 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-3 | game_total | 0.974 | 0.965 | 0.967 | 97 | 4 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-3 | game_total | 0.964 | 0.955 | 0.957 | 96 | 5 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-DET6 | team_total | 0.087 | 0.075 | 0.077 | 8 | 93 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT04FLAANA-10 | game_total | 0.129 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ DET | 0.560 | 0.540 | 0.182 | 0.221 | 5.89 | 6.02 | 1.003/0.988 | KXNHLTEAMTOTAL-26OCT04WPGDET-WPG3 +0.032 |
| UTA @ NYR | 0.558 | 0.550 | 0.174 | 0.217 | 6.22 | 6.31 | 0.957/0.992 | KXNHLTOTAL-26OCT04UTANYR-7 +0.023 |
| FLA @ ANA | 0.576 | 0.576 | 0.167 | 0.212 | 6.73 | 6.61 | 1.024/1.008 | KXNHLTOTAL-26OCT04FLAANA-8 -0.023 |
| CGY @ SEA | 0.586 | 0.581 | 0.173 | 0.218 | 6.20 | 6.08 | 1.005/0.997 | KXNHLTOTAL-26OCT04CGYSEA-8 -0.021 |
| VGK @ VAN | 0.418 | 0.433 | 0.166 | 0.216 | 6.74 | 6.32 | 1.021/1.003 | KXNHLTOTAL-26OCT04VGKVAN-6 -0.072 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 17 recommended · full analysis in card.md / packet.json `thesis_card`

- Vladislav Namestnikov: 1+ goals NO @ 86c · p 0.8982 (adj 0.8874) · $10.07 · thesis WPG:SUPPRESSED
- Isak Rosen: 1+ goals NO @ 86c · p 0.8972 (adj 0.8854) · $10.07 · thesis WPG:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 14c · p 0.1752 (adj 0.1639) · $3.14 · thesis DET:OFFENSE_4PLUS
- Cole Perfetti: 1+ goals NO @ 75c · p 0.7901 (adj 0.7788) · $7.33 · thesis WPG:SUPPRESSED
- Tye Kartye: 1+ goals YES @ 10c · p 0.1419 (adj 0.1289) · $5.37 · thesis NYR:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 10c · p 0.1318 (adj 0.1226) · $3.98 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 71c · p 0.8492 (adj 0.7457) · $18.3 · thesis UTA:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 71c · p 0.7856 (adj 0.7403) · $15.21 · thesis NYR:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 19c · p 0.2639 (adj 0.2442) · $9.3 · thesis ANA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7139 (adj 0.6917) · $16.14 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 78c · p 0.8651 (adj 0.82) · $16.14 · thesis ANA:WINS
- Aaron Ekblad: 1+ assists YES @ 26c · p 0.3275 (adj 0.2863) · $4.19 · thesis FLA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1631 (adj 0.1486) · $5.08 · thesis SEA:OFFENSE_4PLUS
- Shane Wright: 1+ goals YES @ 17c · p 0.2016 (adj 0.19) · $2.7 · thesis SEA:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 14c · p 0.2093 (adj 0.1882) · $9.0 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 21c · p 0.2744 (adj 0.2558) · $8.85 · thesis VAN:OFFENSE_4PLUS
- Vancouver wins by over 1.5 goals YES @ 15c · p 0.2291 (adj 0.187) · $4.17 · thesis VAN:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ DET** · priced 76/77 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 26.21, exp saves 22.92 (sd 6.23), pull risk 0.052
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.88, exp saves 24.07 (sd 6.6), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Neal Pionk: 1+ points | 0.283 | 0.345 | 36/67 | +0.031 | STANDARD |
| Mark Scheifele: 1+ assists | 0.440 | 0.500 | 52/52 | +0.023 | STANDARD |
| Josh Morrissey: 2+ points | 0.122 | 0.175 | 19/84 | +0.028 | STANDARD |
| Josh Morrissey: 1+ points | 0.464 | 0.515 | 53/50 | +0.018 | STANDARD |
| Kyle Connor: 1+ assists | 0.397 | 0.445 | 46/57 | +0.016 | STANDARD |
| Isak Rosen: 1+ goals | 0.103 | 0.150 | 16/86 | +0.029 | STANDARD |

**UTA @ NYR** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.44, exp saves 23.89 (sd 6.51), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.14, exp saves 21.62 (sd 6.09), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.151 | 0.310 | 33/71 | +0.125 | STANDARD |
| Vincent Trocheck: 1+ points | 0.314 | 0.445 | 47/58 | +0.089 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.214 | 0.305 | 32/71 | +0.061 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.464 | 0.535 | 56/49 | +0.029 | STANDARD |
| Vincent Trocheck: 2+ points | 0.054 | 0.125 | 14/89 | +0.049 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.130 | 0.195 | 22/83 | +0.030 | STANDARD |

**FLA @ ANA** · priced 129/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.07, exp saves 22.88 (sd 6.28), pull risk 0.059
- FLA net: Jacob Markstrom (PROJECTED) exp shots 29.88, exp saves 25.4 (sd 7.12), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.534 | 0.380 | 40/64 | +0.117 | STANDARD |
| Alex Killorn: 1+ assists | 0.381 | 0.235 | 25/78 | +0.117 | STANDARD |
| Carter Verhaeghe: 1+ assists | 0.365 | 0.260 | 28/76 | +0.071 | STANDARD |
| Brady Tkachuk: 1+ points | 0.477 | 0.580 | 61/45 | +0.056 | STANDARD |
| Sam Bennett: 1+ assists | 0.397 | 0.295 | 32/73 | +0.062 | STANDARD |
| Jackson LaCombe: 1+ points | 0.636 | 0.535 | 56/49 | +0.059 | STANDARD |

**CGY @ SEA** · priced 118/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.8, exp saves 24.45 (sd 6.48), pull risk 0.046
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.47, exp saves 24.5 (sd 6.74), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Farabee: 1+ points | 0.473 | 0.405 | 42/61 | +0.036 | STANDARD |
| Joel Farabee: 1+ assists | 0.321 | 0.255 | 27/76 | +0.038 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.130 | 0.065 | 12/99 | +0.003 | STANDARD |
| Simon Nemec: 1+ assists | 0.186 | 0.250 | 26/76 | +0.041 | STANDARD |
| Simon Nemec: 1+ points | 0.259 | 0.320 | 34/70 | +0.026 | STANDARD |
| Jared McCann: 1+ points | 0.490 | 0.550 | 57/47 | +0.022 | STANDARD |

**VGK @ VAN** · priced 118/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.79, exp saves 24.64 (sd 6.83), pull risk 0.072
- VGK net: Carter Hart (PROJECTED) exp shots 25.38, exp saves 22.14 (sd 6.09), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tom Willander: 1+ assists | 0.306 | 0.130 | 21/95 | +0.084 | STANDARD |
| Jack Eichel: 2+ points | 0.233 | 0.370 | 39/65 | +0.101 | STANDARD |
| Jack Eichel: 1+ assists | 0.440 | 0.560 | 58/46 | +0.083 | STANDARD |
| Tom Willander: 1+ points | 0.348 | 0.235 | 25/78 | +0.084 | STANDARD |
| Jack Eichel: 1+ points | 0.604 | 0.705 | 73/32 | +0.061 | STANDARD |
| Mitch Marner: 1+ points | 0.569 | 0.670 | 69/35 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
