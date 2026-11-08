# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T22:32:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 4 · markets on board: 2673 · contracts joined: 892 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 792, 'NO_EDGE': 30, 'OK': 70}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 124, 'game_early_goal': 4, 'first_goal': 144, 'game_winner': 8, 'player_goals': 254, 'game_overtime': 4, 'player_points': 160, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ WPG | 2026-11-08T23:00:00Z | T-10m | 0.422 | 0.578 | 0.182 | 5.89 | 2.72 | 3.17 | 210 (25/185) | PROBABLE/CONFIRMED |
| NJD @ TOR | 2026-11-09T00:00:00Z | T-60m | 0.452 | 0.548 | 0.175 | 6.55 | 3.11 | 3.44 | 221 (25/196) | CONFIRMED/CONFIRMED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-60m | 0.566 | 0.434 | 0.190 | 5.42 | 2.91 | 2.50 | 231 (25/206) | CONFIRMED/CONFIRMED |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-90m | 0.605 | 0.395 | 0.156 | 7.22 | 3.97 | 3.25 | 230 (25/205) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.251 | 0.380 | 0.352 | 39 | 63 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.462 | 0.585 | 0.561 | 59 | 42 | no | +0.101 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.709 | 0.805 | 0.788 | 81 | 20 | no | +0.080 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.662 | 0.755 | 0.738 | 76 | 25 | no | +0.075 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.213 | 0.305 | 0.285 | 31 | 70 | no | +0.073 | OK |
| KXNHLTOTAL-26NOV08TBWPG-6 | game_total | 0.502 | 0.595 | 0.577 | 60 | 41 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.110 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.423 | 0.515 | 0.497 | 52 | 49 | no | +0.069 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.566 | 0.475 | 0.493 | 48 | 53 | yes | +0.069 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.069 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.399 | 0.315 | 0.331 | 32 | 69 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.211 | 0.135 | 0.148 | 14 | 87 | yes | +0.063 | OK |
| KXNHLTOTAL-26NOV08TBWPG-7 | game_total | 0.391 | 0.475 | 0.458 | 48 | 53 | no | +0.062 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.058 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.316 | 0.395 | 0.379 | 40 | 61 | no | +0.058 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.605 | 0.525 | 0.541 | 53 | 48 | yes | +0.057 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.395 | 0.475 | 0.459 | 48 | 53 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.113 | 0.195 | 0.176 | 21 | 82 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.767 | 0.840 | 0.827 | 85 | 17 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.605 | 0.535 | 0.549 | 54 | 47 | yes | +0.047 | OK |
| KXNHLTOTAL-26NOV08TBWPG-5 | game_total | 0.732 | 0.800 | 0.787 | 81 | 21 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.378 | 0.310 | 0.323 | 32 | 70 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG4 | team_total | 0.302 | 0.365 | 0.352 | 37 | 64 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV08TBWPG-8 | game_total | 0.215 | 0.275 | 0.262 | 28 | 73 | no | +0.042 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.273 | 0.210 | 0.222 | 22 | 80 | yes | +0.041 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.325 | 0.265 | 0.276 | 27 | 74 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.573 | 0.515 | 0.527 | 52 | 49 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB5 | team_total | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG2 | team_total | 0.746 | 0.795 | 0.786 | 80 | 21 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB4 | team_total | 0.400 | 0.460 | 0.448 | 47 | 55 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV08TBWPG-4 | game_total | 0.830 | 0.875 | 0.867 | 88 | 13 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV08TBWPG-9 | game_total | 0.148 | 0.195 | 0.185 | 20 | 81 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB2 | team_total | 0.822 | 0.865 | 0.857 | 87 | 14 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 | team_total | 0.515 | 0.565 | 0.555 | 57 | 44 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.310 | 0.265 | 0.274 | 27 | 74 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.105 | 0.150 | 0.140 | 16 | 86 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.759 | 0.710 | 0.720 | 72 | 30 | yes | +0.025 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.452 | 0.405 | 0.414 | 41 | 60 | yes | +0.025 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.548 | 0.595 | 0.586 | 60 | 41 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.224 | 0.185 | 0.192 | 19 | 82 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.388 | 0.345 | 0.353 | 35 | 66 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.044 | 0.080 | 0.071 | 9 | 93 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.508 | 0.465 | 0.474 | 47 | 54 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.177 | 0.140 | 0.147 | 15 | 87 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG5 | team_total | 0.142 | 0.180 | 0.172 | 19 | 83 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB3 | team_total | 0.627 | 0.665 | 0.658 | 67 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR2 | team_total | 0.809 | 0.775 | 0.782 | 78 | 23 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV08TBWPG-10 | game_total | 0.068 | 0.095 | 0.089 | 10 | 91 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.825 | 0.860 | 0.854 | 87 | 15 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.417 | 0.460 | 0.451 | 47 | 55 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.629 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ3 | game_spread | 0.213 | 0.245 | 0.238 | 25 | 76 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.902 | 0.875 | 0.881 | 88 | 13 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR2 | game_spread | 0.246 | 0.215 | 0.221 | 22 | 79 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-10 | game_total | 0.042 | 0.070 | 0.063 | 8 | 94 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-3 | game_total | 0.934 | 0.960 | 0.956 | 97 | 5 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV08NJTOR-6 | game_total | 0.617 | 0.585 | 0.592 | 59 | 42 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.210 | 0.180 | 0.186 | 19 | 83 | yes | +0.009 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB3 | game_spread | 0.210 | 0.235 | 0.230 | 24 | 77 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV08NJTOR-10 | game_total | 0.111 | 0.090 | 0.094 | 10 | 92 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY3 | game_spread | 0.194 | 0.170 | 0.175 | 18 | 84 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV08TBWPG-WPG3 | game_spread | 0.120 | 0.140 | 0.136 | 15 | 87 | no | +0.002 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB2 | game_spread | 0.343 | 0.365 | 0.360 | 37 | 64 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.236 | 0.260 | 0.255 | 27 | 75 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV08TBWPG-3 | game_total | 0.957 | 0.975 | 0.972 | 99 | 4 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV08NJTOR-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG6 | team_total | 0.058 | 0.070 | 0.067 | 8 | 94 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV08PHICGY-2 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV08NJTOR-NJ2 | game_spread | 0.337 | 0.355 | 0.351 | 36 | 65 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.712 | 0.690 | 0.694 | 70 | 32 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-2 | game_total | 0.987 | 0.975 | 0.978 | 99 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR6 | team_total | 0.092 | 0.075 | 0.078 | 9 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB6 | team_total | 0.098 | 0.110 | 0.107 | 12 | 90 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV08NJTOR-TOR3 | game_spread | 0.144 | 0.135 | 0.137 | 14 | 87 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-4 | game_total | 0.882 | 0.870 | 0.872 | 88 | 14 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ WPG | 0.422 | 0.480 | 0.182 | 0.220 | 5.89 | 6.13 | 1.002/0.946 | KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 +0.069 |
| NJD @ TOR | 0.452 | 0.495 | 0.175 | 0.220 | 6.55 | 6.30 | 0.956/0.949 | KXNHLTEAMTOTAL-26NOV08NJTOR-NJ5 -0.053 |
| PHI @ CGY | 0.566 | 0.511 | 0.190 | 0.219 | 5.42 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.114 |
| PIT @ ANA | 0.605 | 0.637 | 0.156 | 0.192 | 7.22 | 7.14 | 0.986/1.033 | KXNHLSPREAD-26NOV08PITANA-ANA3 +0.036 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Perfetti: 1+ assists YES @ 32c · p 0.3978 (adj 0.3564) · $7.53 · thesis WPG:OFFENSE_4PLUS
- Cole Koepke: 1+ goals YES @ 9c · p 0.1177 (adj 0.1083) · $3.05 · thesis WPG:OFFENSE_4PLUS
- Tampa Bay over 4.5 goals scored NO @ 74c · p 0.7958 (adj 0.7654) · $11.09 · thesis TBL:SUPPRESSED
- John Carlson: 1+ assists NO @ 63c · p 0.6932 (adj 0.6591) · $7.86 · thesis TBL:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1491 (adj 0.1356) · $7.37 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 17c · p 0.2149 (adj 0.2024) · $6.52 · thesis TOR:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 72c · p 0.7723 (adj 0.758) · $20.0 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 12c · p 0.1509 (adj 0.1419) · $4.14 · thesis NJD:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 65c · p 0.7362 (adj 0.6906) · $14.99 · thesis PHI:SUPPRESSED
- Porter Martone: 1+ goals NO @ 77c · p 0.8132 (adj 0.7999) · $15.01 · thesis PHI:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 9c · p 0.1138 (adj 0.1066) · $2.73 · thesis CGY:OFFENSE_4PLUS
- Martin Pospisil: 1+ goals YES @ 11c · p 0.1359 (adj 0.1282) · $3.1 · thesis CGY:OFFENSE_4PLUS
- Anaheim over 5.5 goals scored YES @ 14c · p 0.2163 (adj 0.1757) · $4.59 · thesis GAME:HIGH_EVENT
- Pittsburgh wins by over 1.5 goals NO @ 71c · p 0.8047 (adj 0.7549) · $20.0 · thesis ANA:WINS
- Kaedan Korczak: 1+ goals YES @ 3c · p 0.051 (adj 0.0432) · $2.41 · thesis DIFFUSE
- Beckett Sennecke: 1+ goals YES @ 34c · p 0.4007 (adj 0.3843) · $7.81 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ WPG** · priced 155/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 28.45, exp saves 24.61 (sd 6.73), pull risk 0.058
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 25.75, exp saves 22.35 (sd 6.16), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.476 | 0.615 | 62/39 | +0.118 | STANDARD |
| Nikita Kucherov: 2+ points | 0.290 | 0.400 | 41/61 | +0.083 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.136 | 0.225 | 24/79 | +0.063 | STANDARD |
| John Carlson: 1+ points | 0.386 | 0.470 | 48/54 | +0.056 | STANDARD |
| Cole Perfetti: 1+ assists | 0.398 | 0.315 | 32/69 | +0.063 | STANDARD |
| Victor Hedman: 1+ assists | 0.213 | 0.295 | 30/71 | +0.062 | STANDARD |

**NJD @ TOR** · priced 168/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 32.87, exp saves 28.44 (sd 7.46), pull risk 0.06
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.54, exp saves 22.93 (sd 6.4), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Tavares: 1+ assists | 0.242 | 0.360 | 38/66 | +0.082 | STANDARD |
| Jack Hughes: 2+ points | 0.253 | 0.365 | 38/65 | +0.081 | STANDARD |
| Luke Evangelista: 1+ assists | 0.255 | 0.365 | 37/64 | +0.089 | STANDARD |
| Jack Hughes: 1+ assists | 0.418 | 0.525 | 54/49 | +0.074 | STANDARD |
| John Tavares: 1+ points | 0.457 | 0.545 | 55/46 | +0.066 | STANDARD |
| Evan Rodrigues: 1+ assists | 0.152 | 0.240 | 25/77 | +0.065 | STANDARD |

**PHI @ CGY** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.21 (sd 6.38), pull risk 0.051
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.264 | 0.355 | 36/65 | +0.070 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.505 | 51/50 | +0.054 | STANDARD |
| Porter Martone: 1+ points | 0.399 | 0.465 | 48/55 | +0.034 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.240 | 25/77 | +0.031 | STANDARD |
| Porter Martone: 1+ assists | 0.260 | 0.305 | 31/70 | +0.026 | STANDARD |
| Travis Sanheim: 1+ points | 0.384 | 0.340 | 35/67 | +0.018 | STANDARD |

**PIT @ ANA** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (PROJECTED) exp shots 26.45, exp saves 23.05 (sd 6.45), pull risk 0.064
- PIT net: Arturs Silovs (PROJECTED) exp shots 28.23, exp saves 23.69 (sd 7.01), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Erik Karlsson: 1+ points | 0.502 | 0.590 | 61/43 | +0.051 | STANDARD |
| Sidney Crosby: 1+ assists | 0.368 | 0.455 | 47/56 | +0.055 | STANDARD |
| Ben Kindel: 1+ points | 0.411 | 0.495 | 51/52 | +0.052 | STANDARD |
| Erik Karlsson: 1+ assists | 0.422 | 0.500 | 51/51 | +0.051 | STANDARD |
| Erik Karlsson: 2+ points | 0.158 | 0.230 | 25/79 | +0.040 | STANDARD |
| Beckett Sennecke: 1+ goals | 0.401 | 0.335 | 34/67 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
