# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-13T00:33:49Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 4 · markets on board: 3824 · contracts joined: 851 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 751, 'OK': 60, 'NO_EDGE': 40}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 111, 'game_early_goal': 4, 'first_goal': 141, 'game_winner': 8, 'player_goals': 243, 'game_overtime': 4, 'player_points': 144, 'goalie_saves': 8, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ CHI | 2026-11-13T01:00:00Z | T-10m | 0.454 | 0.546 | 0.182 | 5.94 | 2.83 | 3.11 | 214 (25/189) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-10m | 0.600 | 0.400 | 0.184 | 5.77 | 3.19 | 2.57 | 213 (25/188) | CONFIRMED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-60m | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 223 (25/198) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-90m | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 201 (25/176) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV12BUFCHI-6 | game_total | 0.518 | 0.635 | 0.612 | 64 | 37 | no | +0.096 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.407 | 0.525 | 0.501 | 53 | 48 | no | +0.095 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.390 | 0.505 | 0.482 | 51 | 50 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF3 | team_total | 0.609 | 0.695 | 0.679 | 70 | 31 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.735 | 0.815 | 0.801 | 82 | 19 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV12NYILA-5 | game_total | 0.695 | 0.775 | 0.760 | 78 | 23 | no | +0.062 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.224 | 0.305 | 0.288 | 31 | 70 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5 | team_total | 0.209 | 0.285 | 0.268 | 29 | 72 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.812 | 0.875 | 0.864 | 88 | 13 | no | +0.050 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.855 | 0.844 | 86 | 15 | no | +0.048 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.829 | 0.885 | 0.875 | 89 | 12 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.800 | 0.788 | 81 | 21 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-9 | game_total | 0.154 | 0.205 | 0.194 | 21 | 80 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF3 | game_spread | 0.193 | 0.250 | 0.238 | 26 | 76 | no | +0.034 | OK |
| KXNHLGAME-26NOV12STLUTA-STL | game_winner | 0.489 | 0.545 | 0.534 | 55 | 46 | no | +0.034 | OK |
| KXNHLGAME-26NOV12STLUTA-UTA | game_winner | 0.511 | 0.455 | 0.466 | 46 | 55 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.235 | 0.225 | 24 | 77 | no | +0.028 | OK |
| KXNHLGAME-26NOV12BUFCHI-BUF | game_winner | 0.546 | 0.595 | 0.585 | 60 | 41 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.319 | 0.365 | 0.356 | 37 | 64 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV12STLUTA-STL2 | game_spread | 0.272 | 0.315 | 0.306 | 32 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12NYILA-9 | game_total | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.091 | 0.125 | 0.118 | 13 | 88 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV12STLUTA-STL3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-5 | game_total | 0.716 | 0.760 | 0.752 | 77 | 25 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI4 | team_total | 0.326 | 0.365 | 0.357 | 37 | 64 | no | +0.018 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.454 | 0.415 | 0.423 | 42 | 59 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-7 | game_total | 0.376 | 0.415 | 0.407 | 42 | 59 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL4 | team_total | 0.407 | 0.445 | 0.437 | 45 | 56 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI3 | game_spread | 0.126 | 0.160 | 0.153 | 17 | 85 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-UTA5 | team_total | 0.214 | 0.185 | 0.191 | 19 | 82 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-CHI2 | game_spread | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA5 | team_total | 0.185 | 0.215 | 0.209 | 22 | 79 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI5 | team_total | 0.138 | 0.175 | 0.167 | 19 | 84 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA2 | team_total | 0.798 | 0.830 | 0.824 | 84 | 18 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-WPG3 | team_total | 0.482 | 0.520 | 0.512 | 53 | 49 | no | +0.011 | OK |
| KXNHLSPREAD-26NOV12STLUTA-UTA2 | game_spread | 0.294 | 0.265 | 0.271 | 27 | 74 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-STL2 | team_total | 0.800 | 0.830 | 0.824 | 84 | 18 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV12WPGDAL-WPG3 | game_spread | 0.103 | 0.125 | 0.120 | 13 | 88 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA3 | team_total | 0.585 | 0.615 | 0.609 | 62 | 39 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-10 | game_total | 0.067 | 0.085 | 0.081 | 9 | 92 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-UTA6 | team_total | 0.093 | 0.075 | 0.078 | 8 | 93 | yes | +0.008 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI2 | game_spread | 0.230 | 0.255 | 0.250 | 26 | 75 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-WPG4 | team_total | 0.270 | 0.300 | 0.294 | 31 | 71 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL3 | team_total | 0.628 | 0.655 | 0.650 | 66 | 35 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL2 | team_total | 0.826 | 0.850 | 0.845 | 86 | 16 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI6 | team_total | 0.052 | 0.065 | 0.062 | 7 | 94 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV12NYILA-2 | game_total | 0.975 | 0.990 | 0.988 |  | 2 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV12NYILA-10 | game_total | 0.053 | 0.070 | 0.066 | 8 | 94 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV12NYILA-3 | game_total | 0.944 | 0.960 | 0.957 | 97 | 5 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-3 | game_total | 0.955 | 0.975 | 0.972 | 99 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV12STLUTA-8 | game_total | 0.254 | 0.235 | 0.239 | 24 | 77 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI3 | team_total | 0.542 | 0.565 | 0.560 | 57 | 44 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-STL6 | team_total | 0.086 | 0.075 | 0.077 | 8 | 93 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-8 | game_total | 0.198 | 0.220 | 0.216 | 23 | 79 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26NOV12WPGDAL-DAL3 | game_spread | 0.227 | 0.250 | 0.245 | 26 | 76 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV12WPGDAL-9 | game_total | 0.132 | 0.145 | 0.142 | 15 | 86 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI2 | team_total | 0.768 | 0.785 | 0.782 | 79 | 22 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-DAL5 | team_total | 0.218 | 0.240 | 0.235 | 25 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI5 | team_total | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12STLUTA-STL4 | team_total | 0.374 | 0.400 | 0.395 | 41 | 61 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV12BUFCHI-2 | game_total | 0.980 | 0.990 | 0.989 |  | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV12WPGDAL-3 | game_total | 0.948 | 0.960 | 0.958 | 97 | 5 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV12BUFCHI-CHI3 | game_spread | 0.136 | 0.125 | 0.127 | 13 | 88 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV12STLUTA-7 | game_total | 0.444 | 0.425 | 0.429 | 43 | 58 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26NOV12NYILA-LA | game_winner | 0.554 | 0.535 | 0.539 | 54 | 47 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26NOV12NYILA-NYI | game_winner | 0.446 | 0.465 | 0.461 | 47 | 54 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV12STLUTA-UTA3 | game_spread | 0.176 | 0.165 | 0.167 | 17 | 84 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA6 | team_total | 0.079 | 0.085 | 0.084 | 9 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV12STLUTA-10 | game_total | 0.081 | 0.075 | 0.076 | 8 | 93 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12WPGDAL-WPG2 | team_total | 0.721 | 0.740 | 0.736 | 75 | 27 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV12STLUTA-STL5 | team_total | 0.194 | 0.205 | 0.203 | 21 | 80 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV12STLUTA-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV12STLUTA-2 | game_total | 0.984 | 0.990 | 0.989 |  | 2 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ CHI | 0.454 | 0.484 | 0.182 | 0.220 | 5.94 | 6.22 | 0.990/0.989 | KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI3 +0.058 |
| WPG @ DAL | 0.600 | 0.586 | 0.184 | 0.209 | 5.77 | 6.12 | 0.994/1.001 | KXNHLTOTAL-26NOV12WPGDAL-7 +0.061 |
| STL @ UTA | 0.511 | 0.532 | 0.172 | 0.220 | 6.17 | 6.40 | 0.993/0.993 | KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4 +0.044 |
| NYI @ LAK | 0.554 | 0.551 | 0.185 | 0.221 | 5.66 | 5.99 | 0.990/0.956 | KXNHLTOTAL-26NOV12NYILA-5 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Tyler Bertuzzi: 1+ goals YES @ 24c · p 0.2868 (adj 0.2738) · $7.34 · thesis CHI:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 60c · p 0.6527 (adj 0.6383) · $11.1 · thesis BUF:SUPPRESSED
- Buffalo over 4.5 goals scored NO @ 72c · p 0.7872 (adj 0.7511) · $9.42 · thesis CHI:WINS
- Full Game: Over 5.5 goals scored NO @ 37c · p 0.4383 (adj 0.4017) · $4.54 · thesis GAME:LOW_EVENT
- Josh Morrissey: 1+ assists NO @ 59c · p 0.7432 (adj 0.6404) · $20.0 · thesis WPG:SUPPRESSED
- Jamie Benn: 1+ goals YES @ 16c · p 0.1996 (adj 0.1885) · $5.62 · thesis DAL:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 27c · p 0.318 (adj 0.3048) · $7.05 · thesis DAL:OFFENSE_4PLUS
- Cole Perfetti: 1+ assists YES @ 30c · p 0.3621 (adj 0.3286) · $5.75 · thesis WPG:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2462 (adj 0.2284) · $11.12 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 13c · p 0.1824 (adj 0.1681) · $8.11 · thesis UTA:OFFENSE_4PLUS
- Liam O'Brien: 1+ goals YES @ 7c · p 0.0945 (adj 0.0859) · $2.82 · thesis UTA:OFFENSE_4PLUS
- Daniil But: 1+ goals NO @ 81c · p 0.8462 (adj 0.8359) · $20.0 · thesis UTA:SUPPRESSED
- Andre Lee: 1+ goals YES @ 8c · p 0.1318 (adj 0.1176) · $7.94 · thesis LAK:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 65c · p 0.8509 (adj 0.7171) · $20.0 · thesis LAK:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 6c · p 0.083 (adj 0.0748) · $2.65 · thesis LAK:WINS_BY_2PLUS
- Trevor Moore: 1+ goals YES @ 17c · p 0.2056 (adj 0.1955) · $4.73 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ CHI** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.67, exp saves 25.66 (sd 6.84), pull risk 0.063
- BUF net: Alex Lyon (PROJECTED) exp shots 25.13, exp saves 21.69 (sd 6.06), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ assists | 0.422 | 0.535 | 54/47 | +0.091 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.518 | 0.630 | 64/38 | +0.086 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.169 | 0.275 | 29/74 | +0.078 | STANDARD |
| Tage Thompson: 2+ points | 0.209 | 0.305 | 31/70 | +0.076 | STANDARD |
| Tage Thompson: 1+ points | 0.564 | 0.655 | 66/35 | +0.070 | STANDARD |
| Connor Bedard: 1+ assists | 0.438 | 0.525 | 53/48 | +0.065 | STANDARD |

**WPG @ DAL** · priced 159/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.66 (sd 6.03), pull risk 0.048
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.72, exp saves 22.89 (sd 6.34), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.257 | 0.415 | 42/59 | +0.136 | STANDARD |
| Josh Morrissey: 1+ points | 0.337 | 0.470 | 48/54 | +0.106 | STANDARD |
| Mikko Rantanen: 2+ points | 0.243 | 0.320 | 33/69 | +0.052 | STANDARD |
| Josh Morrissey: 2+ points | 0.062 | 0.135 | 15/88 | +0.051 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.525 | 53/48 | +0.050 | STANDARD |
| Cole Perfetti: 1+ assists | 0.362 | 0.295 | 30/71 | +0.047 | STANDARD |

**STL @ UTA** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.26), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.65, exp saves 24.64 (sd 6.73), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.450 | 0.330 | 34/68 | +0.094 | STANDARD |
| Robert Thomas: 1+ assists | 0.431 | 0.540 | 55/47 | +0.082 | STANDARD |
| Jack McBain: 1+ points | 0.387 | 0.280 | 29/73 | +0.083 | STANDARD |
| Clayton Keller: 1+ assists | 0.478 | 0.575 | 58/43 | +0.075 | STANDARD |
| MacKenzie Weegar: 1+ assists | 0.367 | 0.285 | 29/72 | +0.062 | STANDARD |
| MacKenzie Weegar: 1+ points | 0.422 | 0.340 | 35/67 | +0.056 | STANDARD |

**NYI @ LAK** · priced 133/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.98, exp saves 23.62 (sd 6.37), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.46, exp saves 24.61 (sd 6.69), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.149 | 0.355 | 36/65 | +0.185 | STANDARD |
| Mats Zuccarello: 1+ points | 0.313 | 0.475 | 48/53 | +0.140 | STANDARD |
| Mats Zuccarello: 2+ points | 0.058 | 0.155 | 17/86 | +0.074 | STANDARD |
| Alex Laferriere: 1+ points | 0.608 | 0.535 | 55/48 | +0.040 | STANDARD |
| Alex Laferriere: 1+ assists | 0.431 | 0.365 | 37/64 | +0.045 | STANDARD |
| Mats Zuccarello: 2+ assists | 0.011 | 0.075 | 9/94 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
