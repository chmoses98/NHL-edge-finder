# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T23:23:10Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 4 · markets on board: 4059 · contracts joined: 846 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 746, 'NO_EDGE': 52, 'OK': 48}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 113, 'game_early_goal': 4, 'first_goal': 139, 'game_winner': 8, 'player_goals': 240, 'game_overtime': 4, 'player_points': 144, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ NYI | 2026-10-08T23:30:00Z | T-<10m | 0.645 | 0.355 | 0.170 | 6.02 | 3.47 | 2.55 | 201 (25/176) | CONFIRMED/CONFIRMED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-30m | 0.599 | 0.401 | 0.172 | 6.17 | 3.41 | 2.77 | 205 (25/180) | CONFIRMED/CONFIRMED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-90m | 0.435 | 0.565 | 0.183 | 5.61 | 2.61 | 3.00 | 211 (25/186) | CONFIRMED/PROBABLE |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-90m | 0.653 | 0.347 | 0.153 | 7.06 | 4.05 | 3.01 | 229 (25/204) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.362 | 0.545 | 0.508 | 55 | 46 | no | +0.160 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.586 | 0.745 | 0.716 | 75 | 26 | no | +0.141 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.184 | 0.330 | 0.297 | 34 | 68 | no | +0.120 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.195 | 0.335 | 0.303 | 34 | 67 | no | +0.119 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.326 | 0.465 | 0.436 | 47 | 54 | no | +0.116 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.435 | 0.305 | 0.329 | 31 | 70 | yes | +0.110 | OK |
| KXNHLTOTAL-26OCT08COLCGY-6 | game_total | 0.461 | 0.585 | 0.560 | 59 | 42 | no | +0.102 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.565 | 0.685 | 0.662 | 69 | 32 | no | +0.100 | OK |
| KXNHLTOTAL-26OCT08COLCGY-7 | game_total | 0.349 | 0.465 | 0.441 | 47 | 54 | no | +0.094 | OK |
| KXNHLTOTAL-26OCT08COLCGY-5 | game_total | 0.695 | 0.795 | 0.777 | 80 | 21 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.800 | 0.890 | 0.875 | 90 | 12 | no | +0.073 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.386 | 0.295 | 0.312 | 30 | 71 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL6 | team_total | 0.080 | 0.170 | 0.147 | 18 | 84 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT08COLCGY-8 | game_total | 0.178 | 0.265 | 0.246 | 27 | 74 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.290 | 0.205 | 0.220 | 21 | 80 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.389 | 0.300 | 0.317 | 31 | 71 | yes | +0.064 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.222 | 0.145 | 0.158 | 15 | 86 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.595 | 0.510 | 0.527 | 52 | 50 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT08COLCGY-4 | game_total | 0.795 | 0.870 | 0.857 | 88 | 14 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.779 | 0.705 | 0.721 | 71 | 30 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.157 | 0.095 | 0.105 | 10 | 91 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT08COLCGY-9 | game_total | 0.120 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.587 | 0.515 | 0.530 | 52 | 49 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.696 | 0.625 | 0.640 | 63 | 38 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.218 | 0.145 | 0.158 | 16 | 87 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.445 | 0.385 | 0.397 | 39 | 62 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.119 | 0.075 | 0.082 | 8 | 93 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.910 | 0.865 | 0.875 | 87 | 14 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT08TORVGK-4 | game_total | 0.918 | 0.885 | 0.892 | 89 | 12 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT08TORVGK-5 | game_total | 0.859 | 0.825 | 0.832 | 83 | 18 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT08COLCGY-3 | game_total | 0.941 | 0.965 | 0.961 | 97 | 4 | no | +0.016 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.347 | 0.385 | 0.377 | 39 | 62 | no | +0.016 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT08COLCGY-10 | game_total | 0.051 | 0.080 | 0.073 | 9 | 93 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.100 | 0.125 | 0.120 | 13 | 88 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.178 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT08TORVGK-3 | game_total | 0.982 | 0.965 | 0.969 | 97 | 4 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL6 | team_total | 0.126 | 0.100 | 0.105 | 11 | 91 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR5 | team_total | 0.197 | 0.175 | 0.179 | 18 | 83 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT08COLCGY-2 | game_total | 0.973 | 0.985 | 0.983 | 99 | 2 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT08CHINYI-CHI3 | game_spread | 0.090 | 0.105 | 0.102 | 11 | 90 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY4 | team_total | 0.277 | 0.255 | 0.259 | 26 | 75 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 | team_total | 0.491 | 0.455 | 0.462 | 47 | 56 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT08TORVGK-2 | game_total | 0.994 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-TOR6 | team_total | 0.088 | 0.070 | 0.073 | 8 | 94 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT08SJSTL-STL2 | game_spread | 0.377 | 0.355 | 0.359 | 36 | 65 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT08SJSTL-3 | game_total | 0.964 | 0.955 | 0.957 | 96 | 5 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT08CHINYI-10 | game_total | 0.074 | 0.065 | 0.067 | 7 | 94 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT08SJSTL-SJ3 | game_spread | 0.113 | 0.125 | 0.123 | 13 | 88 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.252 | 0.230 | 0.234 | 24 | 78 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT08CHINYI-CHI2 | game_spread | 0.171 | 0.185 | 0.182 | 19 | 82 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT08CHINYI-CHI | game_winner | 0.355 | 0.375 | 0.371 | 38 | 63 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT08CHINYI-NYI | game_winner | 0.645 | 0.625 | 0.629 | 63 | 38 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.748 | 0.765 | 0.762 | 77 | 24 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-CHI3 | team_total | 0.474 | 0.495 | 0.491 | 50 | 51 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-6 | game_total | 0.555 | 0.535 | 0.539 | 54 | 47 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-CHI2 | team_total | 0.709 | 0.730 | 0.726 | 74 | 28 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-10 | game_total | 0.082 | 0.070 | 0.072 | 8 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI3 | team_total | 0.683 | 0.665 | 0.669 | 67 | 34 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT08CHINYI-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.259 | 0.240 | 0.244 | 25 | 77 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-9 | game_total | 0.176 | 0.160 | 0.163 | 17 | 85 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-7 | game_total | 0.442 | 0.425 | 0.428 | 43 | 58 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI4 | team_total | 0.472 | 0.455 | 0.458 | 46 | 55 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT08SJSTL-SJ2 | game_spread | 0.204 | 0.215 | 0.213 | 22 | 79 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY2 | team_total | 0.728 | 0.715 | 0.718 | 72 | 29 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL2 | team_total | 0.853 | 0.840 | 0.843 | 85 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI5 | team_total | 0.268 | 0.255 | 0.257 | 26 | 75 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT08CHINYI-3 | game_total | 0.957 | 0.955 | 0.955 | 96 | 5 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL3 | team_total | 0.669 | 0.655 | 0.658 | 66 | 35 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-NYI6 | team_total | 0.132 | 0.120 | 0.122 | 13 | 89 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-CHI4 | team_total | 0.263 | 0.275 | 0.273 | 28 | 73 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY6 | team_total | 0.046 | 0.040 | 0.041 | 5 | 97 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-CHI6 | team_total | 0.045 | 0.045 | 0.045 | 5 | 96 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT08SJSTL-STL | game_winner | 0.599 | 0.585 | 0.588 | 59 | 42 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT08CHINYI-4 | game_total | 0.839 | 0.845 | 0.844 | 85 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT08CHINYI-CHI5 | team_total | 0.122 | 0.130 | 0.128 | 14 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT08SJSTL-4 | game_total | 0.859 | 0.850 | 0.852 | 86 | 16 |  | -0.010 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ NYI | 0.645 | 0.632 | 0.170 | 0.207 | 6.02 | 6.33 | 0.947/1.041 | KXNHLTOTAL-26OCT08CHINYI-7 +0.052 |
| SJS @ STL | 0.599 | 0.565 | 0.172 | 0.215 | 6.17 | 6.36 | 0.976/1.021 | KXNHLTEAMTOTAL-26OCT08SJSTL-SJ3 +0.050 |
| COL @ CGY | 0.435 | 0.433 | 0.183 | 0.218 | 5.61 | 6.25 | 0.978/0.972 | KXNHLTOTAL-26OCT08COLCGY-7 +0.111 |
| TOR @ VGK | 0.653 | 0.658 | 0.153 | 0.201 | 7.06 | 6.35 | 1.003/0.983 | KXNHLTOTAL-26OCT08TORVGK-6 -0.115 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 10c · p 0.155 (adj 0.14) · $7.75 · thesis CHI:OFFENSE_4PLUS
- Kyle Palmieri: 1+ assists NO @ 67c · p 0.7642 (adj 0.7146) · $18.47 · thesis NYI:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 59c · p 0.7222 (adj 0.633) · $17.82 · thesis CHI:SUPPRESSED
- Casey Cizikas: 1+ goals YES @ 11c · p 0.1402 (adj 0.1301) · $3.24 · thesis NYI:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 7c · p 0.1005 (adj 0.0916) · $3.96 · thesis STL:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 70c · p 0.789 (adj 0.7395) · $18.91 · thesis SJS:SUPPRESSED
- Pius Suter: 1+ goals YES @ 14c · p 0.1762 (adj 0.1659) · $4.59 · thesis STL:OFFENSE_4PLUS
- Dmitry Orlov: 1+ assists YES @ 26c · p 0.3387 (adj 0.2944) · $6.62 · thesis SJS:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.644 (adj 0.6218) · $14.18 · thesis COL:SUPPRESSED
- Martin Necas: 1+ goals NO @ 63c · p 0.7006 (adj 0.6817) · $14.18 · thesis COL:SUPPRESSED
- Scott Wedgewood: 22+ saves YES @ 51c · p 0.5877 (adj 0.5464) · $9.85 · thesis COL:NET_HIGH_VOLUME
- Brayden McNabb: 1+ goals YES @ 6c · p 0.088 (adj 0.0797) · $3.55 · thesis VGK:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 81c · p 0.8577 (adj 0.8445) · $18.91 · thesis TOR:SUPPRESSED
- Braeden Bowman: 1+ goals YES @ 17c · p 0.207 (adj 0.1965) · $4.45 · thesis VGK:OFFENSE_4PLUS
- Marc Gatcomb: 1+ goals YES @ 12c · p 0.1521 (adj 0.1416) · $3.52 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ NYI** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.34, exp saves 21.44 (sd 5.92), pull risk 0.049
- CHI net: Arvid Soderblom (CONFIRMED) exp shots 30.03, exp saves 25.42 (sd 7.13), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.278 | 0.415 | 42/59 | +0.115 | STANDARD |
| Calum Ritchie: 1+ assists | 0.351 | 0.250 | 27/77 | +0.067 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.236 | 0.335 | 34/67 | +0.079 | STANDARD |
| Patrick Kane: 1+ points | 0.456 | 0.545 | 55/46 | +0.066 | STANDARD |
| Kyle Palmieri: 1+ points | 0.440 | 0.525 | 54/49 | +0.052 | STANDARD |
| Calum Ritchie: 1+ points | 0.494 | 0.415 | 43/60 | +0.047 | STANDARD |

**SJS @ STL** · priced 152/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 25.77, exp saves 22.39 (sd 6.07), pull risk 0.051
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.07, exp saves 23.1 (sd 6.65), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Nedeljkovic: 26+ saves | 0.351 | 0.475 | 49/54 | +0.091 |  |
| Mason Marchment: 1+ assists | 0.211 | 0.310 | 32/70 | +0.074 | STANDARD |
| Adam Jiricek: 1+ points | 0.300 | 0.395 | 41/62 | +0.063 | PRIOR_HEAVY |
| Dmitry Orlov: 1+ assists | 0.339 | 0.250 | 26/76 | +0.065 | STANDARD |
| Mason McTavish: 1+ assists | 0.217 | 0.300 | 31/71 | +0.059 | STANDARD |
| Kiefer Sherwood: 1+ points | 0.405 | 0.330 | 34/68 | +0.049 | STANDARD |

**COL @ CGY** · priced 160/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 32.7, exp saves 27.85 (sd 7.5), pull risk 0.072
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.32, exp saves 22.94 (sd 6.27), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.279 | 0.540 | 55/47 | +0.234 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.119 | 0.325 | 34/69 | +0.176 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.451 | 0.645 | 65/36 | +0.173 | STANDARD |
| Cale Makar: 2+ points | 0.149 | 0.335 | 35/68 | +0.155 | STANDARD |
| Cale Makar: 1+ assists | 0.409 | 0.590 | 60/42 | +0.154 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.644 | 0.820 | 84/20 | +0.145 | STANDARD |

**TOR @ VGK** · priced 175/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 24.89, exp saves 21.96 (sd 6.01), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.39, exp saves 26.49 (sd 7.38), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Marchenko: 1+ points | 0.421 | 0.555 | 57/46 | +0.101 | STANDARD |
| Mitch Marner: 1+ assists | 0.442 | 0.575 | 59/44 | +0.101 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.244 | 0.375 | 39/64 | +0.100 | STANDARD |
| Mitch Marner: 2+ points | 0.233 | 0.355 | 36/65 | +0.101 | STANDARD |
| Jack Eichel: 2+ points | 0.274 | 0.385 | 40/63 | +0.079 | STANDARD |
| Darren Raddysh: 1+ points | 0.365 | 0.475 | 48/53 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
