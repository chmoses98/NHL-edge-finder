# NHL slate 2026-10-04 — RESEARCH_ONLY

generated 2026-10-04T21:53:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 4 · markets on board: 2628 · contracts joined: 703 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 603, 'OK': 70, 'NO_EDGE': 30}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 97, 'game_early_goal': 4, 'first_goal': 136, 'game_winner': 8, 'player_goals': 135, 'game_overtime': 4, 'player_points': 124, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ NYR | 2026-10-04T22:00:00Z | T-<10m | 0.556 | 0.444 | 0.174 | 6.22 | 3.29 | 2.93 | 174 (25/149) | PROJECTED/PROJECTED |
| FLA @ ANA | 2026-10-05T00:00:00Z | T-90m | 0.580 | 0.420 | 0.161 | 6.72 | 3.62 | 3.10 | 186 (25/161) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-10-05T00:00:00Z | T-90m | 0.589 | 0.411 | 0.178 | 6.21 | 3.38 | 2.83 | 172 (25/147) | PROJECTED/PROJECTED |
| VGK @ VAN | 2026-10-05T01:00:00Z | T-3h | 0.440 | 0.560 | 0.162 | 6.87 | 3.23 | 3.63 | 171 (25/146) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4 | team_total | 0.416 | 0.245 | 0.275 | 25 | 76 | yes | +0.152 | OK |
| KXNHLGAME-26OCT04VGKVAN-VAN | game_winner | 0.440 | 0.275 | 0.305 | 28 | 73 | yes | +0.146 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3 | team_total | 0.628 | 0.465 | 0.498 | 47 | 54 | yes | +0.141 | OK |
| KXNHLGAME-26OCT04VGKVAN-VGK | game_winner | 0.560 | 0.720 | 0.691 | 73 | 29 | no | +0.136 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2 | game_spread | 0.349 | 0.505 | 0.473 | 51 | 50 | no | +0.134 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK3 | game_spread | 0.224 | 0.365 | 0.334 | 37 | 64 | no | +0.120 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5 | team_total | 0.232 | 0.105 | 0.124 | 11 | 90 | yes | +0.115 | OK |
| KXNHLGAME-26OCT04FLAANA-ANA | game_winner | 0.580 | 0.445 | 0.472 | 45 | 56 | yes | +0.113 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2 | team_total | 0.828 | 0.705 | 0.733 | 71 | 30 | yes | +0.103 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA2 | game_spread | 0.366 | 0.245 | 0.267 | 25 | 76 | yes | +0.103 | OK |
| KXNHLGAME-26OCT04FLAANA-FLA | game_winner | 0.420 | 0.545 | 0.520 | 55 | 46 | no | +0.103 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN2 | game_spread | 0.247 | 0.135 | 0.153 | 14 | 87 | yes | +0.098 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4 | team_total | 0.499 | 0.385 | 0.407 | 39 | 62 | yes | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 | team_total | 0.704 | 0.595 | 0.618 | 60 | 41 | yes | +0.087 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-8 | game_total | 0.360 | 0.265 | 0.283 | 27 | 74 | yes | +0.076 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA2 | game_spread | 0.231 | 0.325 | 0.305 | 33 | 68 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5 | team_total | 0.306 | 0.215 | 0.231 | 22 | 79 | yes | +0.074 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA3 | game_spread | 0.133 | 0.215 | 0.196 | 22 | 79 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA3 | game_spread | 0.240 | 0.165 | 0.178 | 17 | 84 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN6 | team_total | 0.110 | 0.040 | 0.049 | 5 | 97 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-9 | game_total | 0.268 | 0.190 | 0.204 | 20 | 82 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-7 | game_total | 0.553 | 0.475 | 0.491 | 48 | 53 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA6 | team_total | 0.162 | 0.090 | 0.102 | 10 | 92 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN3 | game_spread | 0.146 | 0.085 | 0.095 | 9 | 92 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3 | team_total | 0.595 | 0.665 | 0.651 | 67 | 34 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-6 | game_total | 0.660 | 0.595 | 0.608 | 60 | 41 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-10 | game_total | 0.142 | 0.095 | 0.103 | 10 | 91 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA2 | team_total | 0.872 | 0.820 | 0.831 | 83 | 19 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK3 | team_total | 0.705 | 0.755 | 0.746 | 76 | 25 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-5 | game_total | 0.841 | 0.795 | 0.805 | 80 | 21 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5 | team_total | 0.211 | 0.255 | 0.246 | 26 | 75 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-8 | game_total | 0.257 | 0.215 | 0.223 | 22 | 79 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT04FLAANA-8 | game_total | 0.337 | 0.295 | 0.303 | 30 | 71 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4 | team_total | 0.381 | 0.425 | 0.416 | 43 | 58 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT04UTANYR-UTA2 | game_spread | 0.235 | 0.275 | 0.267 | 28 | 73 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR4 | team_total | 0.427 | 0.385 | 0.393 | 39 | 62 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR5 | team_total | 0.241 | 0.205 | 0.212 | 21 | 80 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR3 | team_total | 0.645 | 0.605 | 0.613 | 61 | 40 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT04UTANYR-8 | game_total | 0.261 | 0.225 | 0.232 | 23 | 78 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA6 | team_total | 0.124 | 0.095 | 0.100 | 10 | 91 | yes | +0.018 | OK |
| KXNHLGAME-26OCT04UTANYR-NYR | game_winner | 0.556 | 0.515 | 0.523 | 52 | 49 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR6 | team_total | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT04FLAANA-9 | game_total | 0.248 | 0.215 | 0.221 | 22 | 79 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-9 | game_total | 0.184 | 0.155 | 0.160 | 16 | 85 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-6 | game_total | 0.561 | 0.525 | 0.532 | 53 | 48 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT04UTANYR-10 | game_total | 0.087 | 0.065 | 0.069 | 7 | 94 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT04UTANYR-7 | game_total | 0.448 | 0.415 | 0.422 | 42 | 59 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA5 | team_total | 0.254 | 0.225 | 0.231 | 23 | 78 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-7 | game_total | 0.447 | 0.415 | 0.421 | 42 | 59 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY4 | team_total | 0.324 | 0.290 | 0.297 | 30 | 72 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-9 | game_total | 0.179 | 0.155 | 0.160 | 16 | 85 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-10 | game_total | 0.084 | 0.065 | 0.068 | 7 | 94 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT04UTANYR-UTA3 | game_spread | 0.132 | 0.155 | 0.150 | 16 | 85 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK2 | team_total | 0.874 | 0.905 | 0.899 | 92 | 11 | no | +0.009 | OK |
| KXNHLGAME-26OCT04UTANYR-UTA | game_winner | 0.444 | 0.475 | 0.469 | 48 | 53 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR2 | team_total | 0.837 | 0.810 | 0.816 | 82 | 20 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-4 | game_total | 0.903 | 0.880 | 0.885 | 89 | 13 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-5 | game_total | 0.779 | 0.755 | 0.760 | 76 | 25 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5 | team_total | 0.309 | 0.335 | 0.330 | 34 | 67 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA6 | team_total | 0.098 | 0.120 | 0.115 | 13 | 89 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT04UTANYR-6 | game_total | 0.562 | 0.535 | 0.540 | 54 | 47 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY3 | team_total | 0.541 | 0.515 | 0.520 | 52 | 49 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT04FLAANA-10 | game_total | 0.130 | 0.110 | 0.114 | 12 | 90 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT04UTANYR-5 | game_total | 0.775 | 0.755 | 0.759 | 76 | 25 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY6 | team_total | 0.066 | 0.050 | 0.053 | 6 | 96 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-4 | game_total | 0.860 | 0.845 | 0.848 | 85 | 16 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA2 | team_total | 0.851 | 0.830 | 0.834 | 84 | 18 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6 | team_total | 0.160 | 0.175 | 0.172 | 18 | 83 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY5 | team_total | 0.158 | 0.145 | 0.148 | 15 | 86 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT04UTANYR-NYR2 | game_spread | 0.334 | 0.315 | 0.319 | 32 | 69 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-6 | game_total | 0.634 | 0.615 | 0.619 | 62 | 39 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT04UTANYR-4 | game_total | 0.856 | 0.845 | 0.847 | 85 | 16 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA3 | team_total | 0.663 | 0.645 | 0.649 | 65 | 36 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY2 | team_total | 0.769 | 0.750 | 0.754 | 76 | 26 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT04VGKVAN-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT04UTANYR-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ NYR | 0.556 | 0.550 | 0.174 | 0.217 | 6.22 | 6.31 | 0.957/0.992 | KXNHLTOTAL-26OCT04UTANYR-7 +0.021 |
| FLA @ ANA | 0.580 | 0.576 | 0.161 | 0.212 | 6.72 | 6.61 | 1.024/1.008 | KXNHLTOTAL-26OCT04FLAANA-8 -0.024 |
| CGY @ SEA | 0.589 | 0.581 | 0.178 | 0.218 | 6.21 | 6.08 | 1.005/0.997 | KXNHLTOTAL-26OCT04CGYSEA-6 -0.021 |
| VGK @ VAN | 0.440 | 0.436 | 0.162 | 0.216 | 6.87 | 6.33 | 1.021/1.003 | KXNHLTOTAL-26OCT04VGKVAN-8 -0.090 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Vincent Trocheck: 1+ assists NO @ 70c · p 0.8492 (adj 0.749) · $16.48 · thesis UTA:SUPPRESSED
- Jack McBain: 1+ goals YES @ 10c · p 0.1318 (adj 0.1226) · $3.52 · thesis UTA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ assists NO @ 71c · p 0.7919 (adj 0.746) · $16.48 · thesis NYR:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 16c · p 0.1958 (adj 0.1856) · $3.91 · thesis UTA:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.7046 (adj 0.6847) · $16.48 · thesis FLA:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 21c · p 0.2639 (adj 0.2492) · $7.04 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 20c · p 0.249 (adj 0.2343) · $5.8 · thesis ANA:OFFENSE_4PLUS
- Eetu Luostarinen: 1+ goals YES @ 15c · p 0.187 (adj 0.1765) · $4.13 · thesis FLA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1631 (adj 0.1473) · $6.37 · thesis SEA:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8878 (adj 0.8746) · $16.31 · thesis SEA:SUPPRESSED
- Shane Wright: 1+ goals YES @ 16c · p 0.2016 (adj 0.19) · $4.87 · thesis SEA:OFFENSE_4PLUS
- Jared McCann: 1+ goals NO @ 71c · p 0.7458 (adj 0.7356) · $8.41 · thesis SEA:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 13c · p 0.2051 (adj 0.1838) · $9.46 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 20c · p 0.2713 (adj 0.2522) · $9.54 · thesis VAN:OFFENSE_4PLUS
- Vancouver wins YES @ 28c · p 0.4356 (adj 0.3312) · $4.72 · thesis VAN:WINS
- Tomas Hertl: 1+ goals NO @ 70c · p 0.7541 (adj 0.7393) · $16.48 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ NYR** · priced 123/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.44, exp saves 23.89 (sd 6.51), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.14, exp saves 21.62 (sd 6.09), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.151 | 0.305 | 31/70 | +0.135 | STANDARD |
| Igor Shesterkin: 26+ saves | 0.391 | 0.540 | 62/54 | +0.052 |  |
| Vincent Trocheck: 1+ points | 0.314 | 0.445 | 45/56 | +0.109 | STANDARD |
| Karel Vejmelka: 24+ saves | 0.374 | 0.495 | 52/53 | +0.079 |  |
| Pavel Dorofeyev: 1+ assists | 0.208 | 0.300 | 31/71 | +0.067 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.457 | 0.540 | 55/47 | +0.055 | STANDARD |

**FLA @ ANA** · priced 131/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.07, exp saves 22.88 (sd 6.28), pull risk 0.059
- FLA net: Jacob Markstrom (PROJECTED) exp shots 29.88, exp saves 25.4 (sd 7.12), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.534 | 0.385 | 40/63 | +0.117 | STANDARD |
| Alex Killorn: 1+ assists | 0.381 | 0.255 | 27/76 | +0.097 | STANDARD |
| Brady Tkachuk: 1+ points | 0.477 | 0.595 | 61/42 | +0.086 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.565 | 0.455 | 46/55 | +0.088 | STANDARD |
| Lukas Dostal: 25+ saves | 0.380 | 0.270 | 49/95 | -0.127 |  |
| Brady Tkachuk: 1+ assists | 0.262 | 0.370 | 39/65 | +0.072 | STANDARD |

**CGY @ SEA** · priced 119/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.8, exp saves 24.45 (sd 6.48), pull risk 0.046
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.47, exp saves 24.5 (sd 6.74), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jared McCann: 1+ points | 0.490 | 0.560 | 57/45 | +0.042 | STANDARD |
| Jared McCann: 2+ points | 0.142 | 0.210 | 23/81 | +0.037 | STANDARD |
| Simon Nemec: 1+ assists | 0.186 | 0.250 | 26/76 | +0.041 | STANDARD |
| Joel Farabee: 1+ points | 0.473 | 0.410 | 42/60 | +0.036 | STANDARD |
| Ryan Winterton: 1+ goals | 0.163 | 0.100 | 11/91 | +0.046 | STANDARD |
| Simon Nemec: 1+ points | 0.259 | 0.320 | 34/70 | +0.026 | STANDARD |

**VGK @ VAN** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.79, exp saves 24.6 (sd 6.8), pull risk 0.074
- VGK net: Adin Hill (PROJECTED) exp shots 25.38, exp saves 22.14 (sd 6.18), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adin Hill: 19+ saves | 0.730 | 0.305 | 56/95 | +0.152 |  |
| Kevin Lankinen: 30+ saves | 0.225 | 0.410 | 41/ | -0.202 |  |
| Jack Eichel: 2+ points | 0.240 | 0.385 | 39/62 | +0.124 | STANDARD |
| Mitch Marner: 2+ points | 0.202 | 0.335 | 36/69 | +0.093 | STANDARD |
| Tom Willander: 1+ points | 0.348 | 0.225 | 24/79 | +0.095 | STANDARD |
| Jack Eichel: 1+ points | 0.605 | 0.725 | 73/28 | +0.101 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
