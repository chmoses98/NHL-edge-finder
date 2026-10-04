# NHL slate 2026-10-04 — RESEARCH_ONLY

generated 2026-10-04T20:15:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 4 · markets on board: 2631 · contracts joined: 703 (unjoined to any game: 1527)
gates: {'UNSUPPORTED': 603, 'OK': 73, 'NO_EDGE': 27}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 97, 'game_early_goal': 4, 'first_goal': 136, 'game_winner': 8, 'player_goals': 135, 'game_overtime': 4, 'player_points': 124, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ NYR | 2026-10-04T22:00:00Z | T-90m | 0.558 | 0.442 | 0.174 | 6.22 | 3.29 | 2.92 | 174 (25/149) | PROJECTED/PROJECTED |
| FLA @ ANA | 2026-10-05T00:00:00Z | T-3h | 0.576 | 0.424 | 0.167 | 6.73 | 3.63 | 3.10 | 186 (25/161) | PROJECTED/PROJECTED |
| CGY @ SEA | 2026-10-05T00:00:00Z | T-3h | 0.586 | 0.414 | 0.173 | 6.20 | 3.37 | 2.83 | 172 (25/147) | PROJECTED/PROJECTED |
| VGK @ VAN | 2026-10-05T01:00:00Z | T-3h | 0.442 | 0.558 | 0.169 | 6.88 | 3.24 | 3.64 | 171 (25/146) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN4 | team_total | 0.416 | 0.245 | 0.275 | 25 | 76 | yes | +0.153 | OK |
| KXNHLGAME-26OCT04VGKVAN-VAN | game_winner | 0.442 | 0.280 | 0.310 | 29 | 73 | yes | +0.137 | OK |
| KXNHLGAME-26OCT04VGKVAN-VGK | game_winner | 0.558 | 0.720 | 0.690 | 73 | 29 | no | +0.137 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2 | game_spread | 0.348 | 0.505 | 0.473 | 51 | 50 | no | +0.135 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN3 | team_total | 0.629 | 0.475 | 0.506 | 48 | 53 | yes | +0.132 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VGK3 | game_spread | 0.227 | 0.365 | 0.335 | 37 | 64 | no | +0.116 | OK |
| KXNHLGAME-26OCT04FLAANA-ANA | game_winner | 0.576 | 0.445 | 0.471 | 45 | 56 | yes | +0.109 | OK |
| KXNHLGAME-26OCT04FLAANA-FLA | game_winner | 0.424 | 0.555 | 0.529 | 56 | 45 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN5 | team_total | 0.234 | 0.110 | 0.129 | 12 | 90 | yes | +0.107 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA2 | game_spread | 0.365 | 0.245 | 0.267 | 25 | 76 | yes | +0.102 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN2 | game_spread | 0.244 | 0.135 | 0.153 | 14 | 87 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA4 | team_total | 0.501 | 0.385 | 0.408 | 39 | 62 | yes | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2 | team_total | 0.827 | 0.710 | 0.737 | 72 | 30 | yes | +0.093 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA3 | team_total | 0.704 | 0.595 | 0.618 | 60 | 41 | yes | +0.087 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-8 | game_total | 0.362 | 0.265 | 0.283 | 27 | 74 | yes | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA5 | team_total | 0.309 | 0.210 | 0.228 | 22 | 80 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA2 | game_spread | 0.230 | 0.325 | 0.304 | 33 | 68 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT04FLAANA-FLA3 | game_spread | 0.133 | 0.225 | 0.204 | 23 | 78 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT04FLAANA-ANA3 | game_spread | 0.245 | 0.165 | 0.179 | 17 | 84 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-7 | game_total | 0.559 | 0.475 | 0.492 | 48 | 53 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA6 | team_total | 0.163 | 0.090 | 0.102 | 10 | 92 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN6 | team_total | 0.110 | 0.040 | 0.049 | 5 | 97 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-6 | game_total | 0.664 | 0.585 | 0.601 | 59 | 42 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-9 | game_total | 0.267 | 0.190 | 0.204 | 20 | 82 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT04VGKVAN-VAN3 | game_spread | 0.144 | 0.085 | 0.095 | 9 | 92 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA3 | team_total | 0.596 | 0.665 | 0.652 | 67 | 34 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA5 | team_total | 0.210 | 0.265 | 0.253 | 27 | 74 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-10 | game_total | 0.138 | 0.095 | 0.103 | 10 | 91 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK3 | team_total | 0.706 | 0.755 | 0.746 | 76 | 25 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-5 | game_total | 0.842 | 0.795 | 0.805 | 80 | 21 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-ANA2 | team_total | 0.870 | 0.820 | 0.831 | 83 | 19 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-8 | game_total | 0.258 | 0.215 | 0.223 | 22 | 79 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA2 | team_total | 0.805 | 0.855 | 0.846 | 87 | 16 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR4 | team_total | 0.431 | 0.385 | 0.394 | 39 | 62 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT04FLAANA-8 | game_total | 0.336 | 0.295 | 0.303 | 30 | 71 | yes | +0.021 | OK |
| KXNHLGAME-26OCT04UTANYR-NYR | game_winner | 0.558 | 0.515 | 0.524 | 52 | 49 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK4 | team_total | 0.503 | 0.545 | 0.537 | 55 | 46 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA4 | team_total | 0.383 | 0.425 | 0.417 | 43 | 58 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR3 | team_total | 0.646 | 0.605 | 0.613 | 61 | 40 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR6 | team_total | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA6 | team_total | 0.123 | 0.095 | 0.100 | 10 | 91 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT04FLAANA-9 | game_total | 0.248 | 0.215 | 0.221 | 22 | 79 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-6 | game_total | 0.563 | 0.525 | 0.533 | 53 | 48 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-8 | game_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT04UTANYR-10 | game_total | 0.088 | 0.065 | 0.069 | 7 | 94 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT04UTANYR-9 | game_total | 0.182 | 0.155 | 0.160 | 16 | 85 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-6 | game_total | 0.558 | 0.525 | 0.532 | 53 | 48 | yes | +0.011 | OK |
| KXNHLGAME-26OCT04UTANYR-UTA | game_winner | 0.442 | 0.475 | 0.468 | 48 | 53 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-9 | game_total | 0.180 | 0.155 | 0.160 | 16 | 85 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-4 | game_total | 0.860 | 0.835 | 0.840 | 84 | 17 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT04UTANYR-UTA2 | game_spread | 0.237 | 0.265 | 0.259 | 27 | 74 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-7 | game_total | 0.447 | 0.415 | 0.421 | 42 | 59 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04UTANYR-7 | game_total | 0.447 | 0.415 | 0.421 | 42 | 59 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-10 | game_total | 0.084 | 0.065 | 0.068 | 7 | 94 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA5 | team_total | 0.251 | 0.225 | 0.230 | 23 | 78 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04UTANYR-NYR5 | team_total | 0.241 | 0.210 | 0.216 | 22 | 80 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK2 | team_total | 0.874 | 0.895 | 0.891 | 90 | 11 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-4 | game_total | 0.905 | 0.880 | 0.885 | 89 | 13 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT04UTANYR-UTA3 | game_spread | 0.134 | 0.155 | 0.150 | 16 | 85 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-3 | game_total | 0.978 | 0.965 | 0.968 | 97 | 4 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT04FLAANA-FLA6 | team_total | 0.098 | 0.120 | 0.115 | 13 | 89 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT04UTANYR-5 | game_total | 0.778 | 0.755 | 0.760 | 76 | 25 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-5 | game_total | 0.777 | 0.755 | 0.760 | 76 | 25 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT04FLAANA-6 | game_total | 0.641 | 0.615 | 0.620 | 62 | 39 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT04UTANYR-2 | game_total | 0.985 | 0.975 | 0.977 | 98 | 3 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY6 | team_total | 0.067 | 0.050 | 0.053 | 6 | 96 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY3 | team_total | 0.541 | 0.515 | 0.520 | 52 | 49 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT04CGYSEA-3 | game_total | 0.964 | 0.955 | 0.957 | 96 | 5 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT04FLAANA-10 | game_total | 0.129 | 0.110 | 0.114 | 12 | 90 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5 | team_total | 0.313 | 0.335 | 0.331 | 34 | 67 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA2 | team_total | 0.850 | 0.835 | 0.838 | 84 | 17 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK6 | team_total | 0.160 | 0.175 | 0.172 | 18 | 83 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT04VGKVAN-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-SEA3 | team_total | 0.665 | 0.645 | 0.649 | 65 | 36 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT04UTANYR-4 | game_total | 0.858 | 0.845 | 0.848 | 85 | 16 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT04UTANYR-NYR2 | game_spread | 0.334 | 0.315 | 0.319 | 32 | 69 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT04FLAANA-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04UTANYR-UTA5 | team_total | 0.177 | 0.160 | 0.163 | 17 | 85 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY2 | team_total | 0.769 | 0.750 | 0.754 | 76 | 26 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT04CGYSEA-CGY4 | team_total | 0.321 | 0.305 | 0.308 | 31 | 70 |  | -0.004 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ NYR | 0.558 | 0.550 | 0.174 | 0.217 | 6.22 | 6.31 | 0.957/0.992 | KXNHLTOTAL-26OCT04UTANYR-7 +0.023 |
| FLA @ ANA | 0.576 | 0.576 | 0.167 | 0.212 | 6.73 | 6.61 | 1.024/1.008 | KXNHLTOTAL-26OCT04FLAANA-8 -0.023 |
| CGY @ SEA | 0.586 | 0.581 | 0.173 | 0.218 | 6.20 | 6.08 | 1.005/0.997 | KXNHLTOTAL-26OCT04CGYSEA-8 -0.021 |
| VGK @ VAN | 0.442 | 0.436 | 0.169 | 0.216 | 6.88 | 6.33 | 1.021/1.003 | KXNHLTOTAL-26OCT04VGKVAN-8 -0.092 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Vincent Trocheck: 1+ assists NO @ 71c · p 0.8492 (adj 0.7522) · $15.29 · thesis UTA:SUPPRESSED
- Jack McBain: 1+ goals YES @ 10c · p 0.1318 (adj 0.1226) · $3.26 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.1958 (adj 0.1856) · $3.62 · thesis UTA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ assists NO @ 69c · p 0.7919 (adj 0.7224) · $13.19 · thesis NYR:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7139 (adj 0.6942) · $14.39 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 78c · p 0.8651 (adj 0.82) · $14.39 · thesis ANA:WINS
- A.J. Greer: 1+ goals YES @ 21c · p 0.2639 (adj 0.2492) · $5.56 · thesis ANA:OFFENSE_4PLUS
- Eetu Luostarinen: 1+ goals YES @ 15c · p 0.187 (adj 0.1765) · $3.88 · thesis FLA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1631 (adj 0.1473) · $5.69 · thesis SEA:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 84c · p 0.8878 (adj 0.8746) · $14.91 · thesis SEA:SUPPRESSED
- Zayne Parekh: 1+ goals NO @ 87c · p 0.8982 (adj 0.8886) · $14.91 · thesis CGY:SUPPRESSED
- Shane Wright: 1+ goals YES @ 17c · p 0.2016 (adj 0.1925) · $2.71 · thesis SEA:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 14c · p 0.2051 (adj 0.1876) · $7.32 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 20c · p 0.2713 (adj 0.2522) · $8.43 · thesis VAN:OFFENSE_4PLUS
- Vegas wins by over 1.5 goals NO @ 50c · p 0.6582 (adj 0.5521) · $7.79 · thesis GAME:TIGHT
- Tomas Hertl: 1+ goals NO @ 70c · p 0.7541 (adj 0.7393) · $14.67 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ NYR** · priced 123/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 27.44, exp saves 23.89 (sd 6.51), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.14, exp saves 21.62 (sd 6.09), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.151 | 0.300 | 31/71 | +0.125 | STANDARD |
| Vincent Trocheck: 1+ points | 0.314 | 0.440 | 45/57 | +0.099 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.208 | 0.315 | 32/69 | +0.087 | STANDARD |
| Karel Vejmelka: 24+ saves | 0.374 | 0.290 | 52/94 | -0.163 |  |
| Pavel Dorofeyev: 1+ points | 0.457 | 0.530 | 54/48 | +0.045 | STANDARD |
| Vincent Trocheck: 2+ points | 0.054 | 0.125 | 13/88 | +0.058 | STANDARD |

**FLA @ ANA** · priced 131/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 26.07, exp saves 22.88 (sd 6.28), pull risk 0.059
- FLA net: Jacob Markstrom (PROJECTED) exp shots 29.88, exp saves 25.4 (sd 7.12), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Markstrom: 25+ saves | 0.553 | 0.300 | 55/95 | -0.014 |  |
| Alex Killorn: 1+ points | 0.534 | 0.390 | 41/63 | +0.107 | STANDARD |
| Alex Killorn: 1+ assists | 0.381 | 0.250 | 26/76 | +0.107 | STANDARD |
| Brady Tkachuk: 1+ points | 0.477 | 0.600 | 62/42 | +0.086 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.565 | 0.460 | 47/55 | +0.078 | STANDARD |
| Jackson LaCombe: 1+ points | 0.636 | 0.535 | 55/48 | +0.069 | STANDARD |

**CGY @ SEA** · priced 119/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.8, exp saves 24.45 (sd 6.48), pull risk 0.046
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.47, exp saves 24.5 (sd 6.74), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jared McCann: 2+ points | 0.142 | 0.215 | 23/80 | +0.046 | STANDARD |
| Jared McCann: 1+ points | 0.490 | 0.560 | 57/45 | +0.042 | STANDARD |
| Simon Nemec: 1+ assists | 0.186 | 0.250 | 26/76 | +0.041 | STANDARD |
| Joel Farabee: 1+ points | 0.473 | 0.410 | 42/60 | +0.036 | STANDARD |
| Ryan Winterton: 1+ goals | 0.163 | 0.100 | 11/91 | +0.046 | STANDARD |
| Joel Farabee: 1+ assists | 0.321 | 0.260 | 27/75 | +0.038 | STANDARD |

**VGK @ VAN** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.79, exp saves 24.6 (sd 6.8), pull risk 0.074
- VGK net: Adin Hill (PROJECTED) exp shots 25.38, exp saves 22.14 (sd 6.18), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adin Hill: 19+ saves | 0.730 | 0.295 | 54/95 | +0.172 |  |
| Jack Eichel: 2+ points | 0.240 | 0.385 | 39/62 | +0.124 | STANDARD |
| Jack Eichel: 1+ points | 0.605 | 0.730 | 74/28 | +0.101 | STANDARD |
| Mitch Marner: 2+ points | 0.202 | 0.325 | 34/69 | +0.093 | STANDARD |
| Tom Willander: 1+ points | 0.348 | 0.225 | 24/79 | +0.095 | STANDARD |
| Tom Willander: 1+ assists | 0.301 | 0.185 | 19/82 | +0.101 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
