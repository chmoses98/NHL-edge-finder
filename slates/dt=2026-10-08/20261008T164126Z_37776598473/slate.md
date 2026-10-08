# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T16:41:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3938 · contracts joined: 1916 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 1666, 'OK': 173, 'NO_EDGE': 77}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 229, 'game_early_goal': 10, 'first_goal': 350, 'game_winner': 20, 'player_goals': 527, 'game_overtime': 10, 'player_points': 296, 'game_spread': 40, 'team_total': 100, 'game_total': 90, 'goalie_saves': 4}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-6h | 0.522 | 0.478 | 0.178 | 5.99 | 3.06 | 2.93 | 93 (25/68) | CONFIRMED/PROBABLE |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-6h | 0.569 | 0.431 | 0.181 | 6.06 | 3.25 | 2.81 | 174 (25/149) | PROBABLE/PROJECTED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-6h | 0.590 | 0.410 | 0.168 | 6.54 | 3.56 | 2.97 | 170 (25/145) | CONFIRMED/PROBABLE |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-6h | 0.603 | 0.397 | 0.169 | 6.26 | 3.46 | 2.80 | 214 (25/189) | CONFIRMED/PROBABLE |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-6h | 0.552 | 0.448 | 0.175 | 5.88 | 3.09 | 2.79 | 207 (25/182) | PROBABLE/CONFIRMED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-6h | 0.680 | 0.320 | 0.154 | 6.67 | 3.94 | 2.73 | 217 (25/192) | PROBABLE/PROBABLE |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-6h | 0.608 | 0.392 | 0.176 | 5.79 | 3.23 | 2.56 | 201 (25/176) | CONFIRMED/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-6h | 0.620 | 0.380 | 0.166 | 6.38 | 3.59 | 2.79 | 203 (25/178) | PROBABLE/PROJECTED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-6h | 0.432 | 0.568 | 0.183 | 5.76 | 2.66 | 3.10 | 209 (25/184) | PROJECTED/PROJECTED |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-6h | 0.681 | 0.319 | 0.153 | 6.78 | 4.01 | 2.77 | 228 (25/203) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.385 | 0.535 | 0.505 | 54 | 47 | no | +0.127 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.206 | 0.335 | 0.306 | 34 | 67 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.610 | 0.740 | 0.716 | 75 | 27 | no | +0.106 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.199 | 0.330 | 0.300 | 34 | 68 | no | +0.106 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.338 | 0.465 | 0.439 | 47 | 54 | no | +0.104 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.432 | 0.315 | 0.337 | 32 | 69 | yes | +0.097 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.568 | 0.685 | 0.663 | 69 | 32 | no | +0.097 | OK |
| KXNHLTOTAL-26OCT08COLCGY-5 | game_total | 0.718 | 0.805 | 0.789 | 81 | 20 | no | +0.071 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.569 | 0.475 | 0.494 | 48 | 53 | yes | +0.071 | OK |
| KXNHLTOTAL-26OCT08COLCGY-6 | game_total | 0.483 | 0.580 | 0.561 | 59 | 43 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.324 | 0.415 | 0.396 | 42 | 59 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT08COLCGY-7 | game_total | 0.374 | 0.465 | 0.446 | 47 | 54 | no | +0.069 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.320 | 0.235 | 0.251 | 24 | 77 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.471 | 0.385 | 0.402 | 39 | 62 | yes | +0.064 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.224 | 0.305 | 0.288 | 31 | 70 | no | +0.061 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.431 | 0.515 | 0.498 | 52 | 49 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.463 | 0.545 | 0.529 | 55 | 46 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.774 | 0.695 | 0.712 | 70 | 31 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.813 | 0.890 | 0.877 | 90 | 12 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.516 | 0.435 | 0.451 | 44 | 57 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.300 | 0.225 | 0.239 | 23 | 78 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.536 | 0.620 | 0.604 | 63 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.382 | 0.295 | 0.312 | 31 | 72 | yes | +0.057 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.583 | 0.505 | 0.521 | 51 | 50 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.123 | 0.195 | 0.179 | 20 | 81 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.319 | 0.400 | 0.383 | 41 | 61 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL6 | team_total | 0.087 | 0.165 | 0.146 | 18 | 85 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.345 | 0.275 | 0.288 | 28 | 73 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT08COLCGY-8 | game_total | 0.198 | 0.270 | 0.254 | 28 | 74 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB4 | team_total | 0.384 | 0.455 | 0.441 | 46 | 55 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.332 | 0.265 | 0.278 | 27 | 74 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.342 | 0.275 | 0.288 | 28 | 73 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT08COLCGY-4 | game_total | 0.815 | 0.875 | 0.865 | 88 | 13 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-8 | game_total | 0.268 | 0.205 | 0.217 | 21 | 80 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.765 | 0.830 | 0.818 | 84 | 18 | no | +0.045 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.681 | 0.615 | 0.629 | 62 | 39 | yes | +0.045 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.319 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLGAME-26OCT08UTABOS-BOS | game_winner | 0.522 | 0.455 | 0.468 | 46 | 55 | yes | +0.044 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.478 | 0.545 | 0.532 | 55 | 46 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.213 | 0.145 | 0.157 | 16 | 87 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.149 | 0.090 | 0.100 | 10 | 92 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.296 | 0.235 | 0.246 | 24 | 77 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-7 | game_total | 0.459 | 0.395 | 0.408 | 40 | 61 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.747 | 0.685 | 0.698 | 69 | 32 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.252 | 0.195 | 0.206 | 20 | 81 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.283 | 0.225 | 0.236 | 23 | 78 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT08COLCGY-9 | game_total | 0.132 | 0.185 | 0.173 | 19 | 82 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL3 | team_total | 0.702 | 0.645 | 0.657 | 65 | 36 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.153 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-6 | game_total | 0.573 | 0.515 | 0.527 | 52 | 49 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.911 | 0.865 | 0.876 | 87 | 14 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.118 | 0.075 | 0.082 | 8 | 93 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT08MINTB-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-9 | game_total | 0.192 | 0.145 | 0.154 | 15 | 86 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.715 | 0.765 | 0.755 | 77 | 24 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF3 | team_total | 0.639 | 0.580 | 0.592 | 59 | 43 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.081 | 0.125 | 0.115 | 13 | 88 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT08MINTB-6 | game_total | 0.511 | 0.565 | 0.554 | 57 | 44 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL6 | team_total | 0.149 | 0.100 | 0.108 | 11 | 91 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.158 | 0.115 | 0.123 | 12 | 89 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL5 | team_total | 0.158 | 0.210 | 0.199 | 22 | 80 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA2 | game_spread | 0.265 | 0.315 | 0.305 | 32 | 69 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA3 | game_spread | 0.150 | 0.195 | 0.185 | 20 | 81 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT08VANCAR-8 | game_total | 0.334 | 0.285 | 0.294 | 29 | 72 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT08VANCAR-9 | game_total | 0.240 | 0.195 | 0.203 | 20 | 81 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08UTABOS-UTA2 | team_total | 0.781 | 0.830 | 0.821 | 84 | 18 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT08CHINYI-4 | game_total | 0.813 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.311 | 0.265 | 0.274 | 27 | 74 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT08UTABOS-BOS2 | game_spread | 0.300 | 0.255 | 0.264 | 26 | 75 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.653 | 0.605 | 0.615 | 61 | 40 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT08SJSTL-STL2 | game_spread | 0.403 | 0.355 | 0.364 | 36 | 65 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT08MINTB-4 | game_total | 0.825 | 0.865 | 0.858 | 87 | 14 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08UTABOS-UTA4 | team_total | 0.348 | 0.395 | 0.385 | 40 | 61 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL4 | team_total | 0.493 | 0.440 | 0.451 | 45 | 57 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08UTABOS-UTA3 | team_total | 0.568 | 0.620 | 0.610 | 63 | 39 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB5 | team_total | 0.202 | 0.250 | 0.240 | 26 | 76 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT08MINTB-8 | game_total | 0.212 | 0.255 | 0.246 | 26 | 75 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT08MINTB-7 | game_total | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 0.522 | 0.510 | 0.178 | 0.213 | 5.99 | 6.45 | 0.955/0.999 | KXNHLTOTAL-26OCT08UTABOS-7 +0.084 |
| DAL @ BUF | 0.569 | 0.532 | 0.181 | 0.215 | 6.06 | 6.18 | 1.000/0.986 | KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 +0.048 |
| NSH @ MTL | 0.590 | 0.566 | 0.168 | 0.210 | 6.54 | 6.60 | 0.983/1.002 | KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH4 +0.027 |
| PHI @ OTT | 0.603 | 0.598 | 0.169 | 0.226 | 6.26 | 5.87 | 0.968/0.991 | KXNHLTOTAL-26OCT08PHIOTT-6 -0.075 |
| MIN @ TBL | 0.552 | 0.521 | 0.175 | 0.223 | 5.88 | 6.32 | 0.979/0.991 | KXNHLTOTAL-26OCT08MINTB-7 +0.074 |
| VAN @ CAR | 0.680 | 0.615 | 0.154 | 0.205 | 6.67 | 6.59 | 1.000/1.026 | KXNHLSPREAD-26OCT08VANCAR-CAR2 -0.067 |
| CHI @ NYI | 0.608 | 0.619 | 0.176 | 0.210 | 5.79 | 6.23 | 0.947/1.003 | KXNHLTOTAL-26OCT08CHINYI-7 +0.080 |
| SJS @ STL | 0.620 | 0.571 | 0.166 | 0.218 | 6.38 | 6.42 | 0.984/1.034 | KXNHLSPREAD-26OCT08SJSTL-STL2 -0.054 |
| COL @ CGY | 0.432 | 0.434 | 0.183 | 0.212 | 5.76 | 6.27 | 0.986/0.973 | KXNHLTOTAL-26OCT08COLCGY-7 +0.086 |
| TOR @ VGK | 0.681 | 0.649 | 0.153 | 0.203 | 6.78 | 6.34 | 1.003/0.978 | KXNHLTOTAL-26OCT08TORVGK-6 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Boston over 3.5 goals scored YES @ 36c · p 0.425 (adj 0.39) · $1.7 · thesis BOS:OFFENSE_4PLUS
- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4935 (adj 0.4592) · $1.31 · thesis GAME:HIGH_EVENT
- Justin Danforth: 1+ goals YES @ 7c · p 0.1188 (adj 0.1016) · $2.39 · thesis BUF:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 15c · p 0.2106 (adj 0.193) · $3.7 · thesis BUF:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 12c · p 0.157 (adj 0.1427) · $1.6 · thesis BUF:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 13c · p 0.18 (adj 0.1638) · $2.82 · thesis MTL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 24c · p 0.2955 (adj 0.2804) · $3.7 · thesis NSH:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 12c · p 0.1581 (adj 0.1473) · $2.13 · thesis MTL:WINS_BY_2PLUS
- Nils Hoglander: 1+ goals NO @ 80c · p 0.842 (adj 0.8302) · $8.21 · thesis NSH:SUPPRESSED
- William Eklund: 1+ assists NO @ 62c · p 0.7816 (adj 0.6701) · $6.54 · thesis OTT:SUPPRESSED
- Carter Yakemchuk: 1+ assists NO @ 63c · p 0.7629 (adj 0.67) · $5.77 · thesis OTT:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 8c · p 0.1099 (adj 0.0974) · $1.27 · thesis OTT:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 13c · p 0.162 (adj 0.1527) · $1.65 · thesis PHI:OFFENSE_4PLUS
- Ilya Mikheyev: 1+ goals YES @ 15c · p 0.1991 (adj 0.1856) · $3.2 · thesis TBL:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 18c · p 0.231 (adj 0.217) · $3.1 · thesis MIN:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 58c · p 0.7237 (adj 0.627) · $8.21 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 40c · p 0.4915 (adj 0.4433) · $4.08 · thesis TBL:SUPPRESSED
- Andrei Svechnikov: 1+ goals NO @ 63c · p 0.698 (adj 0.6797) · $8.21 · thesis CAR:SUPPRESSED
- Carolina wins by over 1.5 goals NO @ 46c · p 0.6072 (adj 0.5083) · $3.02 · thesis GAME:TIGHT
- Carolina wins by over 2.5 goals NO @ 59c · p 0.7282 (adj 0.6351) · $3.84 · thesis GAME:TIGHT
- Ryan Greene: 1+ goals YES @ 11c · p 0.1545 (adj 0.1421) · $2.71 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7266 (adj 0.6313) · $7.61 · thesis CHI:SUPPRESSED
- Calum Ritchie: 1+ assists YES @ 27c · p 0.3499 (adj 0.3049) · $3.02 · thesis NYI:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 62c · p 0.6723 (adj 0.658) · $6.39 · thesis NYI:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.8002 (adj 0.7576) · $8.21 · thesis SJS:SUPPRESSED
- Collin Graf: 1+ goals YES @ 15c · p 0.1896 (adj 0.1784) · $2.43 · thesis SJS:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 7c · p 0.0992 (adj 0.0869) · $1.28 · thesis STL:OFFENSE_4PLUS
- Mason McTavish: 1+ assists NO @ 70c · p 0.7758 (adj 0.7354) · $8.21 · thesis STL:SUPPRESSED
- Martin Necas: 1+ goals NO @ 61c · p 0.7036 (adj 0.6789) · $6.16 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 55c · p 0.6435 (adj 0.6189) · $6.16 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6624 (adj 0.5796) · $3.28 · thesis GAME:TIGHT
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0943 (adj 0.0832) · $1.74 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ assists YES @ 29c · p 0.3729 (adj 0.329) · $3.08 · thesis VGK:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 81c · p 0.854 (adj 0.8405) · $7.55 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 66c · p 0.7043 (adj 0.692) · $4.76 · thesis TOR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 36/42 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.45, exp saves 24.61 (sd 6.85), pull risk 0.062
- UTA net: Sebastian Cossa (PROBABLE) exp shots 26.34, exp saves 22.54 (sd 6.33), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: First Goalscorer | 0.035 | 0.050 | 5/ | -0.019 | STANDARD |
| Logan Cooley: First Goalscorer | 0.048 | 0.060 | 6/ | -0.016 | STANDARD |
| Nick Schmaltz: First Goalscorer | 0.060 | 0.070 | 7/ | -0.014 | STANDARD |
| James Hagens: First Goalscorer | 0.031 | 0.040 | 4/ | -0.012 | PRIOR_HEAVY |
| Dylan Guenther: First Goalscorer | 0.062 | 0.070 | 7/ | -0.013 | STANDARD |
| Hampus Lindholm: First Goalscorer | 0.013 | 0.020 | 2/ | -0.008 | STANDARD |

**DAL @ BUF** · priced 115/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 25.45, exp saves 22.13 (sd 6.08), pull risk 0.053
- DAL net: Jake Oettinger (PROJECTED) exp shots 27.04, exp saves 23.32 (sd 6.53), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Power: 1+ assists | 0.385 | 0.305 | 32/71 | +0.050 | STANDARD |
| Zach Benson: 1+ points | 0.534 | 0.460 | 47/55 | +0.046 | STANDARD |
| Jiri Kulich: 1+ goals | 0.211 | 0.140 | 15/87 | +0.052 | STANDARD |
| Justin Danforth: 1+ goals | 0.119 | 0.050 | 7/97 | +0.044 | STANDARD |
| Zach Benson: 1+ assists | 0.369 | 0.305 | 32/71 | +0.034 | STANDARD |
| Tage Thompson: 1+ assists | 0.355 | 0.415 | 42/59 | +0.038 | STANDARD |

**NSH @ MTL** · priced 113/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.02, exp saves 24.28 (sd 6.54), pull risk 0.061
- NSH net: Juuse Saros (PROBABLE) exp shots 27.64, exp saves 23.6 (sd 6.64), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Juuse Saros: 27+ saves | 0.325 | 0.485 | 51/54 | +0.118 |  |
| Chris Kreider: 1+ assists | 0.205 | 0.330 | 35/69 | +0.090 | STANDARD |
| Chris Kreider: 1+ points | 0.411 | 0.525 | 53/48 | +0.092 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.480 | 0.385 | 40/63 | +0.063 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.352 | 0.260 | 27/75 | +0.068 | STANDARD |
| Nick Suzuki: 1+ assists | 0.518 | 0.600 | 61/41 | +0.055 | STANDARD |

**PHI @ OTT** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (CONFIRMED) exp shots 23.58, exp saves 20.62 (sd 5.81), pull risk 0.044
- PHI net: Joseph Woll (PROBABLE) exp shots 28.92, exp saves 24.86 (sd 6.79), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.218 | 0.390 | 40/62 | +0.145 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.293 | 0.445 | 46/57 | +0.120 | PRIOR_HEAVY |
| William Eklund: 1+ points | 0.399 | 0.545 | 56/47 | +0.114 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.237 | 0.380 | 39/63 | +0.117 | PRIOR_HEAVY |
| William Eklund: 2+ points | 0.092 | 0.180 | 19/83 | +0.068 | STANDARD |
| Carter Yakemchuk: 2+ points | 0.047 | 0.130 | 15/89 | +0.056 | PRIOR_HEAVY |

**MIN @ TBL** · priced 154/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROBABLE) exp shots 26.09, exp saves 22.6 (sd 6.27), pull risk 0.06
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.6, exp saves 25.56 (sd 6.93), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.276 | 0.425 | 43/58 | +0.127 | STANDARD |
| John Carlson: 1+ points | 0.361 | 0.505 | 52/51 | +0.112 | STANDARD |
| Nikita Kucherov: 2+ points | 0.318 | 0.425 | 44/59 | +0.075 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.508 | 0.605 | 61/40 | +0.075 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.154 | 0.250 | 27/77 | +0.064 | STANDARD |
| John Carlson: 2+ points | 0.075 | 0.165 | 18/85 | +0.066 | STANDARD |

**VAN @ CAR** · priced 166/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.48, exp saves 19.72 (sd 5.67), pull risk 0.055
- VAN net: Kevin Lankinen (PROBABLE) exp shots 32.08, exp saves 27.11 (sd 7.43), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.347 | 0.525 | 53/48 | +0.155 | STANDARD |
| Sebastian Aho: 1+ points | 0.537 | 0.675 | 68/33 | +0.117 | STANDARD |
| Sebastian Aho: 2+ points | 0.186 | 0.315 | 32/69 | +0.109 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.429 | 0.535 | 55/48 | +0.073 | STANDARD |
| Zeev Buium: 1+ assists | 0.284 | 0.180 | 19/83 | +0.083 | STANDARD |
| Sebastian Aho: 2+ assists | 0.072 | 0.170 | 18/84 | +0.079 | STANDARD |

**CHI @ NYI** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.34, exp saves 21.45 (sd 5.96), pull risk 0.047
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.51 (sd 7.12), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.273 | 0.420 | 43/59 | +0.120 | STANDARD |
| Ilya Sorokin: 24+ saves | 0.351 | 0.495 | 53/54 | +0.092 |  |
| Kyle Palmieri: 1+ assists | 0.223 | 0.340 | 35/67 | +0.092 | STANDARD |
| Kyle Palmieri: 1+ points | 0.424 | 0.525 | 54/49 | +0.068 | STANDARD |
| Patrick Kane: 1+ points | 0.456 | 0.550 | 56/46 | +0.067 | STANDARD |
| Calum Ritchie: 1+ assists | 0.350 | 0.260 | 27/75 | +0.066 | STANDARD |

**SJS @ STL** · priced 152/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROBABLE) exp shots 25.77, exp saves 22.34 (sd 6.18), pull risk 0.054
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.07, exp saves 23.08 (sd 6.65), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason Marchment: 1+ assists | 0.220 | 0.310 | 32/70 | +0.065 | STANDARD |
| Dmitry Orlov: 1+ assists | 0.346 | 0.260 | 28/76 | +0.052 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.200 | 0.285 | 29/72 | +0.066 | PRIOR_HEAVY |
| Adam Jiricek: 1+ points | 0.309 | 0.390 | 41/63 | +0.044 | PRIOR_HEAVY |
| Mason McTavish: 1+ assists | 0.224 | 0.305 | 31/70 | +0.061 | STANDARD |
| Dmitry Orlov: 1+ points | 0.392 | 0.315 | 33/70 | +0.046 | STANDARD |

**COL @ CGY** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 32.7, exp saves 27.87 (sd 7.48), pull risk 0.073
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.32, exp saves 22.97 (sd 6.27), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.282 | 0.525 | 53/48 | +0.221 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.454 | 0.655 | 66/35 | +0.180 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.085 | 0.265 | 28/75 | +0.152 | STANDARD |
| Cale Makar: 1+ assists | 0.401 | 0.580 | 59/43 | +0.152 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.122 | 0.300 | 31/71 | +0.154 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.646 | 0.810 | 83/21 | +0.132 | STANDARD |

**TOR @ VGK** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 24.89, exp saves 21.95 (sd 6.02), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.39, exp saves 26.52 (sd 7.32), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ points | 0.302 | 0.415 | 43/60 | +0.081 | PRIOR_HEAVY |
| Gavin McKenna: 1+ assists | 0.182 | 0.290 | 30/72 | +0.084 | PRIOR_HEAVY |
| Darren Raddysh: 1+ assists | 0.282 | 0.390 | 41/63 | +0.072 | STANDARD |
| Kirill Marchenko: 1+ points | 0.441 | 0.545 | 56/47 | +0.071 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.262 | 0.365 | 38/65 | +0.072 | STANDARD |
| Darren Raddysh: 1+ points | 0.374 | 0.475 | 49/54 | +0.069 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
