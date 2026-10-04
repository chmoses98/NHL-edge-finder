# NHL slate 2026-10-04 — RESEARCH_ONLY

generated 2026-10-04T23:29:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 3 · markets on board: 2592 · contracts joined: 529 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 454, 'OK': 56, 'NO_EDGE': 19}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 73, 'game_early_goal': 3, 'first_goal': 101, 'game_winner': 6, 'player_goals': 100, 'game_overtime': 3, 'player_points': 97, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ ANA | 2026-10-05T00:00:00Z | T-30m | 0.594 | 0.406 | 0.163 | 6.77 | 3.68 | 3.09 | 186 (25/161) | PROJECTED/CONFIRMED |
| CGY @ SEA | 2026-10-05T00:00:00Z | T-30m | 0.589 | 0.411 | 0.178 | 6.21 | 3.38 | 2.83 | 172 (25/147) | PROJECTED/PROJECTED |
| VGK @ VAN | 2026-10-05T01:00:00Z | T-90m | 0.440 | 0.560 | 0.162 | 6.87 | 3.23 | 3.63 | 171 (25/146) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4 | team_total | 0.416 | 0.245 | 0.275 | 25 | 76 | yes | +0.152 | OK |
| KXNHLGAME-26OCT04VGKVAN-VGK | game_winner | 0.560 | 0.725 | 0.695 | 73 | 28 | no | +0.146 | OK |
| KXNHLGAME-26OCT04VGKVAN-VAN | game_winner | 0.440 | 0.275 | 0.305 | 28 | 73 | yes | +0.146 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3 | team_total | 0.628 | 0.465 | 0.498 | 47 | 54 | yes | +0.141 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2 | game_spread | 0.349 | 0.505 | 0.473 | 51 | 50 | no | +0.134 | OK |
| KXNHLGAME-26OCT04FLAANA-ANA | game_winner | 0.594 | 0.445 | 0.475 | 45 | 56 | yes | +0.126 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK3 | game_spread | 0.224 | 0.365 | 0.334 | 37 | 64 | no | +0.120 | OK |
| KXNHLGAME-26OCT04FLAANA-FLA | game_winner | 0.406 | 0.545 | 0.517 | 55 | 46 | no | +0.116 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA2 | game_spread | 0.379 | 0.245 | 0.269 | 25 | 76 | yes | +0.116 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5 | team_total | 0.232 | 0.110 | 0.129 | 12 | 90 | yes | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2 | team_total | 0.828 | 0.705 | 0.733 | 71 | 30 | yes | +0.103 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN2 | game_spread | 0.247 | 0.135 | 0.153 | 14 | 87 | yes | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4 | team_total | 0.512 | 0.395 | 0.418 | 40 | 61 | yes | +0.096 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA2 | game_spread | 0.226 | 0.325 | 0.303 | 33 | 68 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 | team_total | 0.714 | 0.615 | 0.636 | 62 | 39 | yes | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5 | team_total | 0.319 | 0.215 | 0.234 | 23 | 80 | yes | +0.076 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-8 | game_total | 0.360 | 0.265 | 0.283 | 27 | 74 | yes | +0.076 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA3 | game_spread | 0.247 | 0.165 | 0.179 | 17 | 84 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-7 | game_total | 0.553 | 0.465 | 0.483 | 47 | 54 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA3 | game_spread | 0.134 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA6 | team_total | 0.169 | 0.095 | 0.107 | 10 | 91 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN3 | game_spread | 0.146 | 0.075 | 0.086 | 8 | 93 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3 | team_total | 0.597 | 0.675 | 0.660 | 68 | 33 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN6 | team_total | 0.110 | 0.040 | 0.049 | 5 | 97 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-9 | game_total | 0.268 | 0.190 | 0.204 | 20 | 82 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-6 | game_total | 0.660 | 0.585 | 0.600 | 59 | 42 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA2 | team_total | 0.806 | 0.865 | 0.855 | 87 | 14 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK3 | team_total | 0.705 | 0.765 | 0.754 | 77 | 24 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5 | team_total | 0.208 | 0.265 | 0.253 | 27 | 74 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA2 | team_total | 0.876 | 0.820 | 0.833 | 83 | 19 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-10 | game_total | 0.142 | 0.095 | 0.103 | 10 | 91 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4 | team_total | 0.378 | 0.435 | 0.423 | 44 | 57 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-5 | game_total | 0.841 | 0.795 | 0.805 | 80 | 21 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT04FLAANA-8 | game_total | 0.343 | 0.295 | 0.304 | 30 | 71 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK2 | team_total | 0.874 | 0.905 | 0.899 | 91 | 10 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA6 | team_total | 0.124 | 0.095 | 0.100 | 10 | 91 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT04FLAANA-9 | game_total | 0.249 | 0.215 | 0.222 | 22 | 79 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT04FLAANA-6 | game_total | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-8 | game_total | 0.257 | 0.225 | 0.231 | 23 | 78 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY3 | team_total | 0.541 | 0.505 | 0.512 | 51 | 50 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-6 | game_total | 0.561 | 0.525 | 0.532 | 53 | 48 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA6 | team_total | 0.099 | 0.125 | 0.119 | 13 | 88 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT04FLAANA-10 | game_total | 0.129 | 0.105 | 0.110 | 11 | 90 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA5 | team_total | 0.254 | 0.225 | 0.231 | 23 | 78 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-7 | game_total | 0.447 | 0.415 | 0.421 | 42 | 59 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY4 | team_total | 0.324 | 0.295 | 0.301 | 30 | 71 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-9 | game_total | 0.179 | 0.155 | 0.160 | 16 | 85 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-10 | game_total | 0.084 | 0.065 | 0.068 | 7 | 94 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-4 | game_total | 0.903 | 0.885 | 0.889 | 89 | 12 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-5 | game_total | 0.779 | 0.755 | 0.760 | 76 | 25 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5 | team_total | 0.309 | 0.335 | 0.330 | 34 | 67 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY6 | team_total | 0.066 | 0.050 | 0.053 | 6 | 96 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-4 | game_total | 0.860 | 0.845 | 0.848 | 85 | 16 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT04FLAANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6 | team_total | 0.160 | 0.175 | 0.172 | 18 | 83 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY5 | team_total | 0.158 | 0.140 | 0.143 | 15 | 87 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY2 | team_total | 0.769 | 0.750 | 0.754 | 76 | 26 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT04VGKVAN-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-7 | game_total | 0.542 | 0.525 | 0.528 | 53 | 48 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-3 | game_total | 0.976 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT04CGYSEA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-4 | game_total | 0.900 | 0.895 | 0.896 | 90 | 11 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-CGY3 | game_spread | 0.119 | 0.125 | 0.124 | 13 | 88 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT04CGYSEA-3 | game_total | 0.965 | 0.965 | 0.965 | 97 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA4 | team_total | 0.449 | 0.430 | 0.434 | 44 | 58 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA2 | team_total | 0.851 | 0.840 | 0.842 | 85 | 17 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-5 | game_total | 0.831 | 0.825 | 0.826 | 83 | 18 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-SEA3 | game_spread | 0.230 | 0.235 | 0.234 | 24 | 77 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA3 | team_total | 0.663 | 0.650 | 0.653 | 66 | 36 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-CGY2 | game_spread | 0.212 | 0.215 | 0.214 | 22 | 79 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT04CGYSEA-CGY | game_winner | 0.411 | 0.405 | 0.406 | 41 | 60 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26OCT04CGYSEA-SEA | game_winner | 0.589 | 0.585 | 0.586 | 59 | 42 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT04CGYSEA-SEA2 | game_spread | 0.363 | 0.365 | 0.365 | 37 | 64 |  | -0.019 | NO_EDGE |
| KXNHL1P-26OCT04FLAANA-ANA | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT04FLAANA-FLA | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT04FLAANA-TIE | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT04FLAANA-ANA2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT04FLAANA-FLA2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ ANA | 0.594 | 0.584 | 0.163 | 0.206 | 6.77 | 6.63 | 1.024/1.014 | KXNHLTOTAL-26OCT04FLAANA-8 -0.025 |
| CGY @ SEA | 0.589 | 0.581 | 0.178 | 0.218 | 6.21 | 6.08 | 1.005/0.997 | KXNHLTOTAL-26OCT04CGYSEA-6 -0.021 |
| VGK @ VAN | 0.440 | 0.436 | 0.162 | 0.216 | 6.87 | 6.33 | 1.021/1.003 | KXNHLTOTAL-26OCT04VGKVAN-8 -0.090 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 20c · p 0.27 (adj 0.2513) · $10.51 · thesis ANA:OFFENSE_4PLUS
- Matthew Tkachuk: 1+ goals NO @ 65c · p 0.732 (adj 0.7103) · $15.0 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 64c · p 0.7185 (adj 0.6976) · $15.0 · thesis FLA:SUPPRESSED
- Eetu Luostarinen: 1+ goals YES @ 15c · p 0.1786 (adj 0.1702) · $2.98 · thesis FLA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1631 (adj 0.1486) · $7.93 · thesis SEA:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8878 (adj 0.8746) · $19.78 · thesis SEA:SUPPRESSED
- Simon Nemec: 1+ assists NO @ 75c · p 0.8135 (adj 0.7792) · $19.34 · thesis CGY:SUPPRESSED
- Brennan Othmann: 1+ goals YES @ 11c · p 0.1382 (adj 0.1274) · $2.95 · thesis CGY:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 14c · p 0.2051 (adj 0.1876) · $9.84 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 20c · p 0.2713 (adj 0.2522) · $11.21 · thesis VAN:OFFENSE_4PLUS
- Vegas wins by over 1.5 goals NO @ 50c · p 0.6582 (adj 0.5521) · $9.49 · thesis GAME:TIGHT
- Mitch Marner: 1+ goals NO @ 68c · p 0.7373 (adj 0.7217) · $19.46 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ ANA** · priced 131/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.07, exp saves 22.87 (sd 6.25), pull risk 0.059
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 29.88, exp saves 25.4 (sd 7.14), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.537 | 0.385 | 40/63 | +0.120 | STANDARD |
| Brady Tkachuk: 1+ points | 0.462 | 0.605 | 62/41 | +0.111 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.253 | 0.385 | 40/63 | +0.101 | STANDARD |
| Alex Killorn: 1+ assists | 0.374 | 0.250 | 26/76 | +0.101 | STANDARD |
| Sam Reinhart: 1+ points | 0.508 | 0.625 | 63/38 | +0.095 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.567 | 0.455 | 46/55 | +0.090 | STANDARD |

**CGY @ SEA** · priced 119/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.8, exp saves 24.45 (sd 6.48), pull risk 0.046
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.47, exp saves 24.5 (sd 6.74), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jared McCann: 1+ points | 0.490 | 0.565 | 57/44 | +0.052 | STANDARD |
| Jared McCann: 2+ points | 0.142 | 0.215 | 23/80 | +0.046 | STANDARD |
| Simon Nemec: 1+ assists | 0.186 | 0.255 | 26/75 | +0.050 | STANDARD |
| Joel Farabee: 1+ points | 0.473 | 0.410 | 42/60 | +0.036 | STANDARD |
| Joel Farabee: 1+ assists | 0.321 | 0.260 | 27/75 | +0.038 | STANDARD |
| Simon Nemec: 1+ points | 0.259 | 0.320 | 33/69 | +0.036 | STANDARD |

**VGK @ VAN** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.79, exp saves 24.6 (sd 6.8), pull risk 0.074
- VGK net: Adin Hill (PROJECTED) exp shots 25.38, exp saves 22.14 (sd 6.18), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adin Hill: 19+ saves | 0.730 | 0.310 | 55/93 | +0.162 |  |
| Kevin Lankinen: 30+ saves | 0.225 | 0.410 | 41/ | -0.202 |  |
| Jack Eichel: 2+ points | 0.240 | 0.385 | 40/63 | +0.114 | STANDARD |
| Mitch Marner: 2+ points | 0.202 | 0.335 | 35/68 | +0.103 | STANDARD |
| Jack Eichel: 1+ points | 0.605 | 0.735 | 75/28 | +0.101 | STANDARD |
| Tom Willander: 1+ points | 0.348 | 0.220 | 23/79 | +0.105 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
