# NHL slate 2026-10-04 — RESEARCH_ONLY

generated 2026-10-04T09:56:31Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2287 · contracts joined: 332 (unjoined to any game: 1554)
gates: {'UNSUPPORTED': 207, 'OK': 69, 'NO_EDGE': 56}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 12, 'game_early_goal': 5, 'first_goal': 17, 'game_winner': 10, 'player_goals': 33, 'game_overtime': 5, 'player_points': 15, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ DET | 2026-10-04T17:00:00Z | T-6h | 0.559 | 0.441 | 0.181 | 5.76 | 3.05 | 2.71 | 128 (25/103) | PROJECTED/PROJECTED |
| UTA @ NYR | 2026-10-04T22:00:00Z | T-12h | 0.535 | 0.465 | 0.181 | 6.11 | 3.16 | 2.95 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ ANA | 2026-10-05T00:00:00Z | T-12h | 0.562 | 0.438 | 0.171 | 6.48 | 3.44 | 3.04 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-10-05T00:00:00Z | T-12h | 0.546 | 0.454 | 0.183 | 5.90 | 3.08 | 2.82 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ VAN | 2026-10-05T01:00:00Z | T-12h | 0.427 | 0.573 | 0.167 | 6.71 | 3.11 | 3.60 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3 | team_total | 0.605 | 0.475 | 0.501 | 48 | 53 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4 | team_total | 0.389 | 0.270 | 0.292 | 28 | 74 | yes | +0.095 | OK |
| KXNHLGAME-26OCT04FLAANA-FLA | game_winner | 0.438 | 0.555 | 0.532 | 56 | 45 | no | +0.094 | OK |
| KXNHLGAME-26OCT04FLAANA-ANA | game_winner | 0.562 | 0.445 | 0.468 | 45 | 56 | yes | +0.094 | OK |
| KXNHLGAME-26OCT04VGKVAN-VAN | game_winner | 0.427 | 0.315 | 0.336 | 32 | 69 | yes | +0.092 | OK |
| KXNHLGAME-26OCT04VGKVAN-VGK | game_winner | 0.573 | 0.685 | 0.664 | 69 | 32 | no | +0.092 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2 | game_spread | 0.358 | 0.465 | 0.443 | 47 | 54 | no | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5 | team_total | 0.212 | 0.120 | 0.135 | 13 | 89 | yes | +0.074 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA2 | game_spread | 0.347 | 0.255 | 0.272 | 26 | 75 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN2 | game_spread | 0.230 | 0.145 | 0.160 | 15 | 86 | yes | +0.071 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK3 | game_spread | 0.234 | 0.325 | 0.305 | 33 | 68 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA2 | game_spread | 0.241 | 0.325 | 0.307 | 33 | 68 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4 | team_total | 0.373 | 0.455 | 0.438 | 46 | 55 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA3 | game_spread | 0.139 | 0.220 | 0.202 | 23 | 79 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3 | team_total | 0.588 | 0.670 | 0.654 | 68 | 34 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2 | team_total | 0.807 | 0.730 | 0.747 | 74 | 28 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5 | team_total | 0.198 | 0.265 | 0.250 | 27 | 74 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG4 | team_total | 0.300 | 0.370 | 0.355 | 38 | 64 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5 | team_total | 0.275 | 0.210 | 0.222 | 22 | 80 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4 | team_total | 0.460 | 0.390 | 0.404 | 40 | 62 | yes | +0.043 | OK |
| KXNHLGAME-26OCT04WPGDET-DET | game_winner | 0.559 | 0.495 | 0.508 | 50 | 51 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA3 | game_spread | 0.221 | 0.165 | 0.175 | 17 | 84 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN3 | game_spread | 0.137 | 0.085 | 0.094 | 9 | 92 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN6 | team_total | 0.094 | 0.045 | 0.052 | 5 | 96 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-8 | game_total | 0.332 | 0.275 | 0.286 | 28 | 73 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG3 | team_total | 0.515 | 0.585 | 0.571 | 60 | 43 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT04WPGDET-WPG2 | game_spread | 0.231 | 0.285 | 0.274 | 29 | 72 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-6 | game_total | 0.642 | 0.585 | 0.597 | 59 | 42 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-7 | game_total | 0.531 | 0.475 | 0.486 | 48 | 53 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA2 | team_total | 0.797 | 0.855 | 0.845 | 87 | 16 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 | team_total | 0.669 | 0.610 | 0.622 | 62 | 40 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-9 | game_total | 0.244 | 0.195 | 0.204 | 20 | 81 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG2 | team_total | 0.746 | 0.805 | 0.794 | 82 | 21 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT04WPGDET-WPG3 | game_spread | 0.128 | 0.175 | 0.165 | 18 | 83 | no | +0.032 | OK |
| KXNHLGAME-26OCT04WPGDET-WPG | game_winner | 0.441 | 0.495 | 0.484 | 50 | 51 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG5 | team_total | 0.142 | 0.185 | 0.176 | 19 | 82 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-5 | game_total | 0.829 | 0.785 | 0.794 | 79 | 22 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA6 | team_total | 0.139 | 0.095 | 0.103 | 11 | 92 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT04WPGDET-5 | game_total | 0.715 | 0.760 | 0.751 | 77 | 25 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT04CGYSEA-SEA3 | game_spread | 0.188 | 0.225 | 0.217 | 23 | 78 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT04WPGDET-6 | game_total | 0.483 | 0.530 | 0.521 | 54 | 48 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT04WPGDET-7 | game_total | 0.375 | 0.420 | 0.411 | 43 | 59 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT04WPGDET-4 | game_total | 0.813 | 0.850 | 0.843 | 86 | 16 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT04WPGDET-DET2 | game_spread | 0.322 | 0.285 | 0.292 | 29 | 72 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK3 | team_total | 0.700 | 0.735 | 0.728 | 74 | 27 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA6 | team_total | 0.088 | 0.120 | 0.113 | 13 | 89 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-10 | game_total | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 | team_total | 0.500 | 0.540 | 0.532 | 55 | 47 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK2 | team_total | 0.872 | 0.895 | 0.891 | 90 | 11 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT04WPGDET-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT04CGYSEA-SEA2 | game_spread | 0.315 | 0.350 | 0.343 | 36 | 66 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT04WPGDET-10 | game_total | 0.056 | 0.075 | 0.071 | 8 | 93 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA4 | team_total | 0.384 | 0.425 | 0.417 | 44 | 59 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04WPGDET-WPG6 | team_total | 0.057 | 0.080 | 0.075 | 9 | 93 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT04WPGDET-8 | game_total | 0.200 | 0.225 | 0.220 | 23 | 78 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA2 | team_total | 0.848 | 0.815 | 0.822 | 83 | 20 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA3 | team_total | 0.607 | 0.640 | 0.633 | 65 | 37 | no | +0.007 | OK |
| KXNHLGAME-26OCT04CGYSEA-SEA | game_winner | 0.546 | 0.575 | 0.569 | 58 | 43 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT04FLAANA-4 | game_total | 0.876 | 0.895 | 0.891 | 90 | 11 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5 | team_total | 0.299 | 0.330 | 0.324 | 34 | 68 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT04WPGDET-9 | game_total | 0.136 | 0.155 | 0.151 | 16 | 85 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-UTA6 | team_total | 0.079 | 0.060 | 0.063 | 7 | 95 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-3 | game_total | 0.975 | 0.965 | 0.967 | 97 | 4 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT04WPGDET-DET3 | game_spread | 0.193 | 0.175 | 0.178 | 18 | 83 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT04UTANYR-10 | game_total | 0.077 | 0.065 | 0.067 | 7 | 94 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT04FLAANA-5 | game_total | 0.799 | 0.825 | 0.820 | 84 | 19 | no | +0.000 | OK |
| KXNHLSPREAD-26OCT04UTANYR-NYR3 | game_spread | 0.188 | 0.205 | 0.202 | 21 | 80 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-2 | game_total | 0.991 | 0.975 | 0.980 | 99 | 4 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA5 | team_total | 0.198 | 0.225 | 0.219 | 24 | 79 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6 | team_total | 0.151 | 0.165 | 0.162 | 17 | 84 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04UTANYR-UTA5 | team_total | 0.180 | 0.160 | 0.164 | 17 | 85 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-CGY2 | game_spread | 0.242 | 0.220 | 0.224 | 23 | 79 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY6 | team_total | 0.064 | 0.055 | 0.057 | 6 | 95 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA2 | team_total | 0.810 | 0.835 | 0.830 | 85 | 18 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA6 | team_total | 0.086 | 0.100 | 0.097 | 11 | 91 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT04UTANYR-6 | game_total | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-CGY3 | game_spread | 0.136 | 0.125 | 0.127 | 13 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT04CGYSEA-4 | game_total | 0.833 | 0.845 | 0.843 | 85 | 16 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT04CGYSEA-5 | game_total | 0.740 | 0.760 | 0.756 | 77 | 25 |  | -0.003 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ DET | 0.559 | 0.539 | 0.181 | 0.234 | 5.76 | 6.00 | 1.003/0.988 | KXNHLTOTAL-26OCT04WPGDET-7 +0.047 |
| UTA @ NYR | 0.535 | 0.522 | 0.181 | 0.216 | 6.11 | 6.32 | 0.957/0.992 | KXNHLTOTAL-26OCT04UTANYR-7 +0.037 |
| FLA @ ANA | 0.562 | 0.572 | 0.171 | 0.213 | 6.48 | 6.56 | 1.024/0.998 | KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 +0.024 |
| CGY @ SEA | 0.546 | 0.581 | 0.183 | 0.220 | 5.90 | 6.12 | 1.005/0.986 | KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA4 +0.050 |
| VGK @ VAN | 0.427 | 0.456 | 0.167 | 0.219 | 6.71 | 6.36 | 1.025/1.003 | KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 -0.064 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Perfetti: 1+ goals NO @ 73c · p 0.7939 (adj 0.7767) · $20.0 · thesis WPG:SUPPRESSED
- Neal Pionk: 1+ goals NO @ 90c · p 0.9407 (adj 0.928) · $20.0 · thesis DIFFUSE
- J.T. Compher: 1+ goals YES @ 14c · p 0.1799 (adj 0.1674) · $5.24 · thesis DET:OFFENSE_4PLUS
- Anaheim wins by over 2.5 goals YES @ 17c · p 0.2385 (adj 0.2017) · $3.87 · thesis ANA:WINS_BY_2PLUS
- Florida wins by over 2.5 goals NO @ 79c · p 0.8675 (adj 0.8237) · $19.83 · thesis ANA:WINS
- Anaheim over 3.5 goals scored YES @ 40c · p 0.4848 (adj 0.4374) · $2.39 · thesis ANA:OFFENSE_4PLUS
- Florida over 4.5 goals scored NO @ 74c · p 0.8077 (adj 0.7713) · $7.77 · thesis ANA:WINS
- Vancouver wins by over 1.5 goals YES @ 15c · p 0.2405 (adj 0.1928) · $6.89 · thesis VAN:WINS_BY_2PLUS
- Vegas wins by over 1.5 goals NO @ 54c · p 0.6819 (adj 0.5864) · $6.66 · thesis VAN:WINS
- Vegas wins by over 2.5 goals NO @ 68c · p 0.7944 (adj 0.7168) · $3.9 · thesis VAN:WINS
- Vegas over 5.5 goals scored NO @ 84c · p 0.8894 (adj 0.8622) · $7.94 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ DET** · priced 76/77 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 26.21, exp saves 22.99 (sd 6.2), pull risk 0.051
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.88, exp saves 24.1 (sd 6.57), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Perfetti: 1+ goals | 0.206 | 0.275 | 28/73 | +0.050 | STANDARD |
| Neal Pionk: 1+ points | 0.283 | 0.350 | 37/67 | +0.031 | STANDARD |
| Josh Morrissey: 1+ points | 0.450 | 0.515 | 53/50 | +0.032 | STANDARD |
| Mark Scheifele: 1+ assists | 0.446 | 0.505 | 53/52 | +0.017 | STANDARD |
| Neal Pionk: 1+ goals | 0.059 | 0.110 | 12/90 | +0.034 | STANDARD |
| J.T. Compher: 1+ goals | 0.180 | 0.130 | 14/88 | +0.031 | STANDARD |

**UTA @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.44, exp saves 23.85 (sd 6.51), pull risk 0.059
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.14, exp saves 21.73 (sd 6.11), pull risk 0.063

**FLA @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.07, exp saves 22.88 (sd 6.21), pull risk 0.056
- FLA net: Akira Schmid (PROJECTED) exp shots 29.88, exp saves 25.46 (sd 7.08), pull risk 0.082

**CGY @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.8, exp saves 24.38 (sd 6.52), pull risk 0.049
- CGY net: Devin Cooley (PROJECTED) exp shots 28.47, exp saves 24.39 (sd 6.81), pull risk 0.072

**VGK @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.79, exp saves 24.74 (sd 6.81), pull risk 0.069
- VGK net: Carter Hart (PROJECTED) exp shots 25.38, exp saves 22.07 (sd 6.14), pull risk 0.057

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
