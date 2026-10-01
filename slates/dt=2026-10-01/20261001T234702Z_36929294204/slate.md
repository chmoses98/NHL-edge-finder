# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-01T23:47:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 5 · markets on board: 3345 · contracts joined: 891 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 766, 'OK': 68, 'NO_EDGE': 57}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 135, 'game_early_goal': 5, 'first_goal': 161, 'game_winner': 10, 'player_goals': 161, 'game_overtime': 5, 'player_points': 174, 'goalie_saves': 5, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ NSH | 2026-10-02T00:00:00Z | T-10m | 0.458 | 0.542 | 0.166 | 6.53 | 3.13 | 3.40 | 176 (25/151) | CONFIRMED/CONFIRMED |
| SEA @ CGY | 2026-10-02T01:00:00Z | T-60m | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 201 (25/176) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-90m | 0.627 | 0.373 | 0.175 | 6.14 | 3.47 | 2.66 | 162 (25/137) | PROBABLE/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-90m | 0.412 | 0.588 | 0.168 | 6.71 | 3.07 | 3.63 | 166 (25/141) | PROBABLE/CONFIRMED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-90m | 0.514 | 0.486 | 0.170 | 6.62 | 3.36 | 3.25 | 186 (25/161) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.514 | 0.425 | 0.443 | 43 | 58 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.241 | 0.325 | 0.307 | 33 | 68 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.369 | 0.455 | 0.437 | 46 | 55 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.164 | 0.245 | 0.227 | 25 | 76 | no | +0.063 | OK |
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.486 | 0.565 | 0.549 | 57 | 44 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.305 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.656 | 0.585 | 0.600 | 59 | 42 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 53 | 48 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.588 | 0.655 | 0.642 | 66 | 35 | no | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.412 | 0.345 | 0.358 | 35 | 66 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.441 | 0.370 | 0.384 | 38 | 64 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.470 | 0.535 | 0.522 | 54 | 47 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.320 | 0.332 | 33 | 69 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.203 | 0.150 | 0.160 | 16 | 86 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.261 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT01MINNSH-7 | game_total | 0.501 | 0.445 | 0.456 | 45 | 56 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.192 | 0.145 | 0.154 | 15 | 86 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.223 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.128 | 0.080 | 0.088 | 9 | 93 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH3 | team_total | 0.609 | 0.550 | 0.562 | 56 | 46 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH4 | team_total | 0.397 | 0.340 | 0.351 | 35 | 67 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT01MINNSH-8 | game_total | 0.304 | 0.255 | 0.264 | 26 | 75 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT01MINNSH-9 | game_total | 0.221 | 0.175 | 0.184 | 18 | 83 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.839 | 0.790 | 0.801 | 80 | 22 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.711 | 0.755 | 0.747 | 76 | 25 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT01FLASJ-10 | game_total | 0.122 | 0.085 | 0.091 | 9 | 92 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01FLASJ-8 | game_total | 0.319 | 0.275 | 0.283 | 28 | 73 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5 | team_total | 0.214 | 0.170 | 0.178 | 18 | 84 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA5 | team_total | 0.272 | 0.315 | 0.306 | 32 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01MINNSH-10 | game_total | 0.108 | 0.075 | 0.081 | 8 | 93 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.422 | 0.465 | 0.456 | 47 | 54 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.634 | 0.680 | 0.671 | 69 | 33 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.802 | 0.760 | 0.769 | 77 | 25 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.505 | 0.550 | 0.541 | 56 | 46 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT01MINNSH-6 | game_total | 0.615 | 0.575 | 0.583 | 58 | 43 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT01MINNSH-NSH2 | game_spread | 0.260 | 0.225 | 0.232 | 23 | 78 | yes | +0.018 | OK |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.373 | 0.335 | 0.342 | 34 | 67 | yes | +0.017 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.308 | 0.350 | 0.341 | 36 | 66 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.091 | 0.060 | 0.065 | 7 | 95 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.232 | 0.275 | 0.266 | 29 | 74 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA3 | team_total | 0.683 | 0.720 | 0.713 | 73 | 29 | no | +0.012 | OK |
| KXNHLGAME-26OCT01MINNSH-MIN | game_winner | 0.542 | 0.575 | 0.568 | 58 | 43 | no | +0.011 | OK |
| KXNHLGAME-26OCT01MINNSH-NSH | game_winner | 0.458 | 0.425 | 0.432 | 43 | 58 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT01SEACGY-SEA3 | game_spread | 0.150 | 0.175 | 0.170 | 18 | 83 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH2 | team_total | 0.812 | 0.780 | 0.787 | 79 | 23 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-NSH6 | team_total | 0.095 | 0.070 | 0.074 | 8 | 94 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-9 | game_total | 0.242 | 0.215 | 0.220 | 22 | 79 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.831 | 0.860 | 0.855 | 87 | 15 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT01MINNSH-MIN3 | game_spread | 0.208 | 0.235 | 0.229 | 24 | 77 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.126 | 0.105 | 0.109 | 11 | 90 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM2 | team_total | 0.875 | 0.900 | 0.895 | 91 | 11 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT01MINNSH-5 | game_total | 0.809 | 0.785 | 0.790 | 79 | 22 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY3 | team_total | 0.614 | 0.585 | 0.591 | 59 | 42 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-5 | game_total | 0.764 | 0.785 | 0.781 | 79 | 22 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA6 | team_total | 0.109 | 0.130 | 0.126 | 14 | 88 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT01SEACGY-8 | game_total | 0.246 | 0.225 | 0.229 | 23 | 78 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-CHI2 | game_spread | 0.183 | 0.165 | 0.169 | 17 | 84 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT01MINNSH-MIN6 | team_total | 0.129 | 0.110 | 0.114 | 12 | 90 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-4 | game_total | 0.850 | 0.865 | 0.862 | 87 | 14 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA2 | team_total | 0.862 | 0.880 | 0.876 | 89 | 13 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY5 | team_total | 0.212 | 0.190 | 0.194 | 20 | 82 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-6 | game_total | 0.553 | 0.575 | 0.571 | 58 | 43 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-SEA2 | team_total | 0.789 | 0.810 | 0.806 | 82 | 20 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-4 | game_total | 0.894 | 0.905 | 0.903 | 91 | 10 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY6 | team_total | 0.095 | 0.080 | 0.083 | 9 | 93 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT01MINNSH-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT01SEACGY-CGY2 | game_spread | 0.303 | 0.285 | 0.289 | 29 | 72 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT01SEACGY-SEA2 | game_spread | 0.258 | 0.275 | 0.271 | 28 | 73 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT01SEACGY-SEA | game_winner | 0.474 | 0.495 | 0.491 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT01SEACGY-CGY | game_winner | 0.525 | 0.505 | 0.509 | 51 | 50 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-10 | game_total | 0.083 | 0.075 | 0.076 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT01SEACGY-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-10 | game_total | 0.124 | 0.115 | 0.117 | 12 | 89 |  | -0.003 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ NSH | 0.458 | 0.476 | 0.166 | 0.219 | 6.53 | 6.50 | 1.004/0.991 | KXNHLSPREAD-26OCT01MINNSH-MIN2 -0.027 |
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.627 | 0.652 | 0.175 | 0.205 | 6.14 | 6.49 | 0.990/1.003 | KXNHLTOTAL-26OCT01CHIUTA-7 +0.064 |
| EDM @ VAN | 0.412 | 0.446 | 0.168 | 0.214 | 6.71 | 6.52 | 1.026/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.040 |
| FLA @ SJS | 0.514 | 0.549 | 0.170 | 0.216 | 6.62 | 6.41 | 1.039/0.991 | KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 19 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Hartman: 1+ goals YES @ 23c · p 0.2743 (adj 0.262) · $4.3 · thesis MIN:OFFENSE_4PLUS
- Jared Spurgeon: 1+ goals NO @ 91c · p 0.935 (adj 0.9275) · $13.84 · thesis MIN:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 18c · p 0.2122 (adj 0.2029) · $2.58 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 26c · p 0.2986 (adj 0.2877) · $3.29 · thesis NSH:OFFENSE_4PLUS
- Brandon Montour: 1+ goals NO @ 83c · p 0.8924 (adj 0.8755) · $10.46 · thesis SEA:SUPPRESSED
- Freddy Gaudreau: 1+ goals YES @ 10c · p 0.1359 (adj 0.1257) · $3.66 · thesis SEA:OFFENSE_4PLUS
- Jared McCann: 1+ assists NO @ 64c · p 0.7306 (adj 0.6828) · $10.3 · thesis SEA:SUPPRESSED
- Adam Klapka: 1+ goals YES @ 10c · p 0.1308 (adj 0.1218) · $2.86 · thesis CGY:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1664 (adj 0.1535) · $4.92 · thesis CHI:OFFENSE_4PLUS
- MacKenzie Weegar: 1+ goals NO @ 89c · p 0.9254 (adj 0.9153) · $13.84 · thesis DIFFUSE
- Patrick Kane: 1+ assists NO @ 62c · p 0.7454 (adj 0.6574) · $12.11 · thesis CHI:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 22c · p 0.2593 (adj 0.247) · $3.4 · thesis UTA:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 31c · p 0.4762 (adj 0.3649) · $6.82 · thesis EDM:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 16c · p 0.2153 (adj 0.2002) · $6.03 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 67c · p 0.8312 (adj 0.7167) · $13.84 · thesis EDM:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 21c · p 0.257 (adj 0.244) · $4.75 · thesis VAN:OFFENSE_4PLUS
- Aleksander Barkov: 1+ assists NO @ 51c · p 0.6916 (adj 0.5671) · $9.79 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 76c · p 0.852 (adj 0.8035) · $12.23 · thesis SJS:WINS
- Sam Reinhart: 1+ goals NO @ 67c · p 0.7369 (adj 0.7189) · $10.97 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ NSH** · priced 123/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 29.8, exp saves 25.56 (sd 7.02), pull risk 0.072
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.26, exp saves 25.35 (sd 6.89), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonathan Marchessault: 1+ assists | 0.357 | 0.250 | 27/77 | +0.074 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.491 | 0.385 | 40/63 | +0.074 | STANDARD |
| Max Shabanov: 1+ points | 0.369 | 0.460 | 48/56 | +0.053 | STANDARD |
| Filip Forsberg: 2+ points | 0.240 | 0.170 | 25/91 | -0.023 | STANDARD |
| Ryan O'Reilly: 1+ points | 0.598 | 0.540 | 56/48 | +0.021 | STANDARD |
| Steven Stamkos: 1+ assists | 0.388 | 0.330 | 34/68 | +0.032 | STANDARD |

**SEA @ CGY** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.69, exp saves 24.08 (sd 6.53), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.93, exp saves 24.93 (sd 6.79), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.255 | 0.105 | 20/99 | +0.043 | STANDARD |
| Connor Zary: 1+ assists | 0.267 | 0.130 | 25/99 | +0.004 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.260 | 0.135 | 26/99 | -0.013 | STANDARD |
| Jared McCann: 1+ points | 0.447 | 0.555 | 57/46 | +0.076 | STANDARD |
| Jared McCann: 1+ assists | 0.269 | 0.365 | 37/64 | +0.074 | STANDARD |
| Adam Klapka: 1+ points | 0.304 | 0.210 | 25/83 | +0.041 | STANDARD |

**CHI @ UTA** · priced 111/111 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 24.86, exp saves 21.85 (sd 6.02), pull risk 0.047
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.89 (sd 7.02), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 22+ saves | 0.515 | 0.310 | 54/92 | -0.042 |  |
| Patrick Kane: 1+ assists | 0.255 | 0.390 | 40/62 | +0.109 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.224 | 0.350 | 36/66 | +0.100 | STANDARD |
| Frank Nazar: 1+ assists | 0.334 | 0.215 | 23/80 | +0.091 | STANDARD |
| Frank Nazar: 1+ points | 0.472 | 0.365 | 38/65 | +0.075 | STANDARD |
| Patrick Kane: 1+ points | 0.436 | 0.540 | 56/48 | +0.066 | STANDARD |

**EDM @ VAN** · priced 115/115 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.37, exp saves 26.01 (sd 7.19), pull risk 0.072
- EDM net: Devon Levi (CONFIRMED) exp shots 26.05, exp saves 22.61 (sd 6.28), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.169 | 0.345 | 36/67 | +0.146 | STANDARD |
| Leon Draisaitl: 2+ points | 0.309 | 0.485 | 50/53 | +0.143 | STANDARD |
| Connor McDavid: 1+ assists | 0.524 | 0.695 | 70/31 | +0.151 | STANDARD |
| Connor McDavid: 2+ points | 0.392 | 0.545 | 56/47 | +0.121 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.439 | 0.590 | 60/42 | +0.124 | STANDARD |
| Mattias Ekholm: 1+ points | 0.458 | 0.330 | 35/69 | +0.092 | STANDARD |

**FLA @ SJS** · priced 135/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.16, exp saves 23.68 (sd 6.44), pull risk 0.058
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.2, exp saves 22.4 (sd 6.33), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.308 | 0.500 | 51/51 | +0.164 | STANDARD |
| Aleksander Barkov: 1+ points | 0.459 | 0.630 | 64/38 | +0.144 | STANDARD |
| Brady Tkachuk: 1+ points | 0.466 | 0.625 | 64/39 | +0.128 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.390 | 40/62 | +0.112 | STANDARD |
| Brady Tkachuk: 2+ points | 0.134 | 0.255 | 27/76 | +0.093 | STANDARD |
| Sam Reinhart: 1+ points | 0.505 | 0.615 | 63/40 | +0.078 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
