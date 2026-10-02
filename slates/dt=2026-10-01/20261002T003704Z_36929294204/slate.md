# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-02T00:37:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 4 · markets on board: 3282 · contracts joined: 715 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 615, 'NO_EDGE': 43, 'OK': 57}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 110, 'game_early_goal': 4, 'first_goal': 128, 'game_winner': 8, 'player_goals': 128, 'game_overtime': 4, 'player_points': 141, 'goalie_saves': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CGY | 2026-10-02T01:00:00Z | T-10m | 0.525 | 0.474 | 0.181 | 6.10 | 3.13 | 2.97 | 201 (25/176) | CONFIRMED/PROJECTED |
| CHI @ UTA | 2026-10-02T01:30:00Z | T-30m | 0.627 | 0.373 | 0.175 | 6.14 | 3.47 | 2.66 | 162 (25/137) | PROBABLE/PROJECTED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-60m | 0.412 | 0.588 | 0.168 | 6.71 | 3.07 | 3.63 | 166 (25/141) | PROBABLE/CONFIRMED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-60m | 0.514 | 0.486 | 0.170 | 6.62 | 3.36 | 3.25 | 186 (25/161) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.486 | 0.575 | 0.557 | 58 | 43 | no | +0.067 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.514 | 0.425 | 0.443 | 43 | 58 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.241 | 0.325 | 0.307 | 33 | 68 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.369 | 0.455 | 0.437 | 46 | 55 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.164 | 0.245 | 0.227 | 25 | 76 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.305 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.656 | 0.585 | 0.600 | 59 | 42 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 53 | 48 | yes | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.588 | 0.655 | 0.642 | 66 | 35 | no | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.412 | 0.345 | 0.358 | 35 | 66 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.441 | 0.370 | 0.384 | 38 | 64 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.470 | 0.535 | 0.522 | 54 | 47 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.258 | 0.195 | 0.207 | 21 | 82 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.320 | 0.332 | 33 | 69 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.203 | 0.155 | 0.164 | 16 | 85 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.261 | 0.315 | 0.304 | 32 | 69 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.192 | 0.145 | 0.154 | 15 | 86 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.223 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.128 | 0.080 | 0.088 | 9 | 93 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.839 | 0.790 | 0.801 | 80 | 22 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.308 | 0.355 | 0.345 | 36 | 65 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.711 | 0.755 | 0.747 | 76 | 25 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT01FLASJ-10 | game_total | 0.122 | 0.085 | 0.091 | 9 | 92 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT01FLASJ-8 | game_total | 0.319 | 0.275 | 0.283 | 28 | 73 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA5 | team_total | 0.272 | 0.315 | 0.306 | 32 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.422 | 0.465 | 0.456 | 47 | 54 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.634 | 0.680 | 0.671 | 69 | 33 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.802 | 0.760 | 0.769 | 77 | 25 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM2 | team_total | 0.875 | 0.905 | 0.899 | 91 | 10 | no | +0.019 | OK |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.373 | 0.335 | 0.342 | 34 | 67 | yes | +0.017 | OK |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.091 | 0.065 | 0.070 | 7 | 94 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.232 | 0.275 | 0.266 | 29 | 74 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA3 | team_total | 0.683 | 0.720 | 0.713 | 73 | 29 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM6 | team_total | 0.157 | 0.185 | 0.179 | 19 | 82 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT01SEACGY-SEA3 | game_spread | 0.150 | 0.175 | 0.170 | 18 | 83 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY6 | team_total | 0.095 | 0.075 | 0.079 | 8 | 93 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-9 | game_total | 0.242 | 0.215 | 0.220 | 22 | 79 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.831 | 0.860 | 0.855 | 87 | 15 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.126 | 0.105 | 0.109 | 11 | 90 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY3 | team_total | 0.614 | 0.585 | 0.591 | 59 | 42 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT01SEACGY-10 | game_total | 0.079 | 0.065 | 0.068 | 7 | 94 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-5 | game_total | 0.764 | 0.785 | 0.781 | 79 | 22 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT01SEACGY-9 | game_total | 0.173 | 0.155 | 0.158 | 16 | 85 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA6 | team_total | 0.109 | 0.125 | 0.122 | 13 | 88 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT01SEACGY-8 | game_total | 0.246 | 0.225 | 0.229 | 23 | 78 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-CHI2 | game_spread | 0.183 | 0.165 | 0.169 | 17 | 84 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-3 | game_total | 0.976 | 0.985 | 0.984 | 99 | 2 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI6 | team_total | 0.055 | 0.045 | 0.047 | 5 | 96 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-4 | game_total | 0.850 | 0.865 | 0.862 | 87 | 14 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA2 | team_total | 0.862 | 0.880 | 0.876 | 89 | 13 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY5 | team_total | 0.212 | 0.190 | 0.194 | 20 | 82 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-6 | game_total | 0.553 | 0.575 | 0.571 | 58 | 43 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-4 | game_total | 0.894 | 0.905 | 0.903 | 91 | 10 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-2 | game_total | 0.990 | 0.990 | 0.990 |  | 1 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT01SEACGY-CGY2 | game_spread | 0.303 | 0.285 | 0.289 | 29 | 72 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT01SEACGY-SEA2 | game_spread | 0.258 | 0.275 | 0.271 | 28 | 73 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT01SEACGY-SEA | game_winner | 0.474 | 0.495 | 0.491 | 50 | 51 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT01SEACGY-CGY | game_winner | 0.525 | 0.505 | 0.509 | 51 | 50 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-10 | game_total | 0.083 | 0.075 | 0.076 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT01SEACGY-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-10 | game_total | 0.124 | 0.115 | 0.117 | 12 | 89 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-8 | game_total | 0.332 | 0.315 | 0.318 | 32 | 69 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI4 | team_total | 0.290 | 0.270 | 0.274 | 28 | 74 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT01SEACGY-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY4 | team_total | 0.391 | 0.370 | 0.374 | 38 | 64 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-3 | game_total | 0.976 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-5 | game_total | 0.826 | 0.835 | 0.833 | 84 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01SEACGY-CGY2 | team_total | 0.815 | 0.800 | 0.803 | 81 | 21 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01SEACGY-SEA6 | team_total | 0.079 | 0.075 | 0.076 | 8 | 93 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT01CHIUTA-CHI3 | game_spread | 0.098 | 0.095 | 0.096 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI3 | team_total | 0.499 | 0.480 | 0.484 | 49 | 53 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI5 | team_total | 0.139 | 0.130 | 0.132 | 14 | 88 |  | -0.010 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ CGY | 0.525 | 0.512 | 0.181 | 0.225 | 6.10 | 6.12 | 1.005/1.005 | KXNHLSPREAD-26OCT01SEACGY-CGY2 -0.016 |
| CHI @ UTA | 0.627 | 0.652 | 0.175 | 0.205 | 6.14 | 6.49 | 0.990/1.003 | KXNHLTOTAL-26OCT01CHIUTA-7 +0.064 |
| EDM @ VAN | 0.412 | 0.446 | 0.168 | 0.214 | 6.71 | 6.52 | 1.026/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.040 |
| FLA @ SJS | 0.514 | 0.549 | 0.170 | 0.216 | 6.62 | 6.41 | 1.039/0.991 | KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Brandon Montour: 1+ goals NO @ 83c · p 0.8924 (adj 0.8755) · $15.33 · thesis SEA:SUPPRESSED
- Freddy Gaudreau: 1+ goals YES @ 10c · p 0.1359 (adj 0.1257) · $3.9 · thesis SEA:OFFENSE_4PLUS
- Adam Klapka: 1+ goals YES @ 10c · p 0.1308 (adj 0.1218) · $3.17 · thesis CGY:OFFENSE_4PLUS
- Maxim Tsyplakov: 1+ goals NO @ 86c · p 0.8952 (adj 0.8851) · $15.33 · thesis CGY:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 12c · p 0.1664 (adj 0.1535) · $5.43 · thesis CHI:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 21c · p 0.2593 (adj 0.2457) · $6.09 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 66c · p 0.7758 (adj 0.694) · $13.66 · thesis UTA:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 62c · p 0.7454 (adj 0.6541) · $11.44 · thesis CHI:SUPPRESSED
- Connor McDavid: 1+ assists NO @ 31c · p 0.4762 (adj 0.3649) · $6.55 · thesis EDM:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 16c · p 0.2153 (adj 0.2002) · $6.19 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 67c · p 0.8312 (adj 0.7167) · $15.05 · thesis EDM:SUPPRESSED
- Edmonton wins by over 2.5 goals NO @ 68c · p 0.7726 (adj 0.7238) · $10.54 · thesis VAN:WINS
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2154 (adj 0.1978) · $7.83 · thesis SJS:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 76c · p 0.852 (adj 0.8035) · $15.33 · thesis SJS:WINS
- Aleksander Barkov: 1+ assists NO @ 53c · p 0.6916 (adj 0.5768) · $11.88 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 67c · p 0.711 (adj 0.6995) · $2.29 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ CGY** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 27.69, exp saves 24.08 (sd 6.53), pull risk 0.055
- SEA net: Joey Daccord (PROJECTED) exp shots 28.93, exp saves 24.93 (sd 6.79), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.255 | 0.105 | 20/99 | +0.043 | STANDARD |
| Connor Zary: 1+ assists | 0.267 | 0.125 | 24/99 | +0.014 | STANDARD |
| Yegor Sharangovich: 1+ assists | 0.260 | 0.135 | 26/99 | -0.013 | STANDARD |
| Jared McCann: 1+ points | 0.447 | 0.555 | 57/46 | +0.076 | STANDARD |
| Kevin Bahl: 1+ assists | 0.211 | 0.115 | 22/99 | -0.021 | STANDARD |
| Jared McCann: 1+ assists | 0.269 | 0.360 | 37/65 | +0.065 | STANDARD |

**CHI @ UTA** · priced 111/111 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 24.86, exp saves 21.85 (sd 6.02), pull risk 0.047
- CHI net: Spencer Knight (PROJECTED) exp shots 29.49, exp saves 24.89 (sd 7.02), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 22+ saves | 0.515 | 0.310 | 54/92 | -0.042 |  |
| Patrick Kane: 1+ assists | 0.255 | 0.395 | 41/62 | +0.109 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.224 | 0.350 | 36/66 | +0.100 | STANDARD |
| Frank Nazar: 1+ assists | 0.334 | 0.220 | 24/80 | +0.081 | STANDARD |
| Patrick Kane: 1+ points | 0.436 | 0.545 | 56/47 | +0.076 | STANDARD |
| Frank Nazar: 1+ points | 0.472 | 0.365 | 38/65 | +0.075 | STANDARD |

**EDM @ VAN** · priced 115/115 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.37, exp saves 26.01 (sd 7.19), pull risk 0.072
- EDM net: Devon Levi (CONFIRMED) exp shots 26.05, exp saves 22.61 (sd 6.28), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.169 | 0.345 | 36/67 | +0.146 | STANDARD |
| Connor McDavid: 1+ assists | 0.524 | 0.695 | 70/31 | +0.151 | STANDARD |
| Leon Draisaitl: 2+ points | 0.309 | 0.480 | 50/54 | +0.134 | STANDARD |
| Connor McDavid: 2+ points | 0.392 | 0.545 | 56/47 | +0.121 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.439 | 0.590 | 60/42 | +0.124 | STANDARD |
| Mattias Ekholm: 1+ points | 0.458 | 0.325 | 34/69 | +0.103 | STANDARD |

**FLA @ SJS** · priced 135/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.16, exp saves 23.68 (sd 6.44), pull risk 0.058
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.2, exp saves 22.4 (sd 6.33), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.308 | 0.485 | 50/53 | +0.144 | STANDARD |
| Aleksander Barkov: 1+ points | 0.459 | 0.630 | 64/38 | +0.144 | STANDARD |
| Brady Tkachuk: 1+ points | 0.466 | 0.625 | 64/39 | +0.128 | STANDARD |
| Aleksander Barkov: 2+ points | 0.122 | 0.275 | 29/74 | +0.124 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.390 | 40/62 | +0.112 | STANDARD |
| Brady Tkachuk: 2+ points | 0.134 | 0.255 | 27/76 | +0.093 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
