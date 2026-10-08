# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T15:41:27Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3934 · contracts joined: 1912 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 1662, 'OK': 168, 'NO_EDGE': 82}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 229, 'game_early_goal': 10, 'first_goal': 350, 'game_winner': 20, 'player_goals': 527, 'game_overtime': 10, 'player_points': 296, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-6h | 0.508 | 0.492 | 0.181 | 6.12 | 3.08 | 3.04 | 93 (25/68) | PROJECTED/PROJECTED |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-6h | 0.569 | 0.431 | 0.181 | 6.06 | 3.25 | 2.81 | 174 (25/149) | PROBABLE/PROJECTED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-6h | 0.588 | 0.412 | 0.168 | 6.52 | 3.55 | 2.97 | 169 (25/144) | CONFIRMED/PROJECTED |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-6h | 0.604 | 0.396 | 0.166 | 6.23 | 3.45 | 2.78 | 214 (25/189) | PROBABLE/PROJECTED |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-6h | 0.557 | 0.443 | 0.179 | 5.93 | 3.14 | 2.79 | 206 (25/181) | PROBABLE/PROJECTED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-6h | 0.673 | 0.327 | 0.160 | 6.61 | 3.88 | 2.73 | 216 (25/191) | PROBABLE/PROJECTED |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-6h | 0.604 | 0.397 | 0.175 | 5.83 | 3.24 | 2.60 | 200 (25/175) | PROBABLE/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-6h | 0.619 | 0.381 | 0.169 | 6.42 | 3.59 | 2.83 | 203 (25/178) | PROJECTED/PROJECTED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-6h | 0.432 | 0.568 | 0.183 | 5.76 | 2.66 | 3.10 | 209 (25/184) | PROJECTED/PROJECTED |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-6h | 0.681 | 0.319 | 0.153 | 6.78 | 4.01 | 2.77 | 228 (25/203) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.385 | 0.535 | 0.505 | 54 | 47 | no | +0.127 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.206 | 0.335 | 0.306 | 34 | 67 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.610 | 0.735 | 0.712 | 74 | 27 | no | +0.106 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.338 | 0.465 | 0.439 | 47 | 54 | no | +0.104 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.432 | 0.315 | 0.337 | 32 | 69 | yes | +0.097 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.568 | 0.685 | 0.663 | 69 | 32 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.199 | 0.315 | 0.289 | 32 | 69 | no | +0.096 | OK |
| KXNHLTOTAL-26OCT08COLCGY-6 | game_total | 0.483 | 0.585 | 0.565 | 59 | 42 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.316 | 0.415 | 0.394 | 42 | 59 | no | +0.077 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.327 | 0.235 | 0.252 | 24 | 77 | yes | +0.074 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.471 | 0.375 | 0.394 | 38 | 63 | yes | +0.074 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.569 | 0.475 | 0.494 | 48 | 53 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.813 | 0.895 | 0.882 | 90 | 11 | no | +0.070 | OK |
| KXNHLTOTAL-26OCT08COLCGY-7 | game_total | 0.374 | 0.465 | 0.446 | 47 | 54 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.382 | 0.290 | 0.307 | 30 | 72 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.455 | 0.545 | 0.527 | 55 | 46 | no | +0.067 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.673 | 0.755 | 0.740 | 76 | 25 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.224 | 0.305 | 0.288 | 31 | 70 | no | +0.061 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.431 | 0.515 | 0.498 | 52 | 49 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT08COLCGY-5 | game_total | 0.718 | 0.795 | 0.781 | 80 | 21 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.517 | 0.435 | 0.451 | 44 | 57 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.536 | 0.625 | 0.608 | 64 | 39 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.583 | 0.505 | 0.521 | 51 | 50 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.298 | 0.225 | 0.239 | 23 | 78 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.123 | 0.195 | 0.179 | 20 | 81 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.213 | 0.135 | 0.148 | 15 | 88 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.319 | 0.400 | 0.383 | 41 | 61 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL6 | team_total | 0.087 | 0.165 | 0.146 | 18 | 85 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.345 | 0.275 | 0.288 | 28 | 73 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.293 | 0.225 | 0.238 | 23 | 78 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.774 | 0.700 | 0.716 | 71 | 31 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT08COLCGY-8 | game_total | 0.198 | 0.270 | 0.254 | 28 | 74 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.332 | 0.265 | 0.278 | 27 | 74 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.342 | 0.275 | 0.288 | 28 | 73 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT08COLCGY-4 | game_total | 0.815 | 0.875 | 0.865 | 88 | 13 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.299 | 0.230 | 0.243 | 24 | 78 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.765 | 0.830 | 0.818 | 84 | 18 | no | +0.045 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.681 | 0.615 | 0.629 | 62 | 39 | yes | +0.045 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.319 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.749 | 0.685 | 0.699 | 69 | 32 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL6 | team_total | 0.150 | 0.095 | 0.104 | 10 | 91 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.149 | 0.095 | 0.104 | 10 | 91 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.252 | 0.195 | 0.206 | 20 | 81 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT08SJSTL-6 | game_total | 0.597 | 0.535 | 0.548 | 54 | 47 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT08SJSTL-9 | game_total | 0.208 | 0.155 | 0.165 | 16 | 85 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT08SJSTL-7 | game_total | 0.484 | 0.425 | 0.437 | 43 | 58 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT08COLCGY-9 | game_total | 0.132 | 0.185 | 0.173 | 19 | 82 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB4 | team_total | 0.396 | 0.455 | 0.443 | 46 | 55 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.653 | 0.595 | 0.607 | 60 | 41 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.153 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-8 | game_total | 0.267 | 0.215 | 0.225 | 22 | 79 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.911 | 0.865 | 0.876 | 87 | 14 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.118 | 0.075 | 0.082 | 8 | 93 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF3 | team_total | 0.639 | 0.585 | 0.596 | 59 | 42 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.160 | 0.115 | 0.123 | 12 | 89 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.081 | 0.125 | 0.115 | 13 | 88 | no | +0.032 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLGAME-26OCT08UTABOS-BOS | game_winner | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT08MINTB-6 | game_total | 0.512 | 0.565 | 0.555 | 57 | 44 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL5 | team_total | 0.158 | 0.210 | 0.199 | 22 | 80 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-9 | game_total | 0.188 | 0.145 | 0.153 | 15 | 86 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL4 | team_total | 0.496 | 0.445 | 0.455 | 45 | 56 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI3 | game_spread | 0.229 | 0.275 | 0.265 | 28 | 73 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT6 | team_total | 0.131 | 0.095 | 0.101 | 10 | 91 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL3 | team_total | 0.700 | 0.655 | 0.664 | 66 | 35 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT08MINTB-4 | game_total | 0.827 | 0.865 | 0.858 | 87 | 14 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.541 | 0.495 | 0.504 | 50 | 51 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT08SJSTL-5 | game_total | 0.796 | 0.755 | 0.764 | 76 | 25 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF3 | game_spread | 0.213 | 0.175 | 0.182 | 18 | 83 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-7 | game_total | 0.449 | 0.405 | 0.414 | 41 | 60 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN3 | game_spread | 0.086 | 0.055 | 0.060 | 6 | 95 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.726 | 0.765 | 0.757 | 77 | 24 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT08DALBUF-4 | game_total | 0.841 | 0.875 | 0.869 | 88 | 13 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI2 | game_spread | 0.372 | 0.415 | 0.406 | 42 | 59 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT08MINTB-7 | game_total | 0.402 | 0.445 | 0.436 | 45 | 56 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.304 | 0.265 | 0.272 | 27 | 74 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT08SJSTL-STL2 | game_spread | 0.396 | 0.355 | 0.363 | 36 | 65 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN6 | team_total | 0.062 | 0.030 | 0.035 | 4 | 98 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF5 | team_total | 0.231 | 0.190 | 0.198 | 20 | 82 | yes | +0.020 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 0.508 | 0.499 | 0.181 | 0.215 | 6.12 | 6.47 | 0.968/0.992 | KXNHLTOTAL-26OCT08UTABOS-7 +0.060 |
| DAL @ BUF | 0.569 | 0.532 | 0.181 | 0.215 | 6.06 | 6.18 | 1.000/0.986 | KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 +0.048 |
| NSH @ MTL | 0.588 | 0.569 | 0.168 | 0.212 | 6.52 | 6.60 | 0.983/1.000 | KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH3 +0.030 |
| PHI @ OTT | 0.604 | 0.591 | 0.166 | 0.220 | 6.23 | 5.89 | 0.980/0.991 | KXNHLTOTAL-26OCT08PHIOTT-6 -0.058 |
| MIN @ TBL | 0.557 | 0.527 | 0.179 | 0.218 | 5.93 | 6.35 | 0.979/1.003 | KXNHLTOTAL-26OCT08MINTB-7 +0.076 |
| VAN @ CAR | 0.673 | 0.616 | 0.160 | 0.205 | 6.61 | 6.58 | 1.000/1.020 | KXNHLSPREAD-26OCT08VANCAR-CAR2 -0.060 |
| CHI @ NYI | 0.604 | 0.611 | 0.175 | 0.213 | 5.83 | 6.24 | 0.951/1.003 | KXNHLTOTAL-26OCT08CHINYI-7 +0.075 |
| SJS @ STL | 0.619 | 0.565 | 0.169 | 0.215 | 6.42 | 6.43 | 0.993/1.034 | KXNHLGAME-26OCT08SJSTL-SJ +0.054 |
| COL @ CGY | 0.432 | 0.434 | 0.183 | 0.212 | 5.76 | 6.27 | 0.986/0.973 | KXNHLTOTAL-26OCT08COLCGY-7 +0.086 |
| TOR @ VGK | 0.681 | 0.649 | 0.153 | 0.203 | 6.78 | 6.34 | 1.003/0.978 | KXNHLTOTAL-26OCT08TORVGK-6 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 34 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4969 (adj 0.4609) · $2.46 · thesis GAME:HIGH_EVENT
- Justin Danforth: 1+ goals YES @ 7c · p 0.1188 (adj 0.1016) · $2.35 · thesis BUF:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 15c · p 0.2106 (adj 0.1942) · $3.76 · thesis BUF:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 87c · p 0.9002 (adj 0.8914) · $7.95 · thesis DAL:SUPPRESSED
- Zach Benson: 1+ goals YES @ 22c · p 0.2556 (adj 0.2455) · $1.77 · thesis BUF:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 24c · p 0.2964 (adj 0.2811) · $3.65 · thesis NSH:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 12c · p 0.1563 (adj 0.146) · $2.03 · thesis MTL:WINS_BY_2PLUS
- Nils Hoglander: 1+ goals NO @ 81c · p 0.8439 (adj 0.8342) · $7.01 · thesis NSH:SUPPRESSED
- Chris Kreider: 1+ assists NO @ 69c · p 0.7964 (adj 0.7175) · $5.32 · thesis MTL:SUPPRESSED
- William Eklund: 1+ assists NO @ 62c · p 0.7849 (adj 0.6712) · $5.97 · thesis OTT:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 11c · p 0.1479 (adj 0.1359) · $1.95 · thesis PHI:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1135 (adj 0.1014) · $1.61 · thesis OTT:OFFENSE_4PLUS
- Carter Yakemchuk: 1+ assists NO @ 64c · p 0.7703 (adj 0.6824) · $5.97 · thesis OTT:SUPPRESSED
- Ilya Mikheyev: 1+ goals YES @ 15c · p 0.2004 (adj 0.1865) · $3.33 · thesis TBL:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 58c · p 0.7246 (adj 0.6274) · $7.87 · thesis TBL:SUPPRESSED
- Michael McCarron: 1+ goals YES @ 9c · p 0.1242 (adj 0.1119) · $1.61 · thesis MIN:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 40c · p 0.4911 (adj 0.443) · $4.06 · thesis TBL:SUPPRESSED
- Carolina wins by over 2.5 goals NO @ 59c · p 0.7362 (adj 0.6379) · $6.45 · thesis GAME:TIGHT
- Nikolaj Ehlers: 1+ goals NO @ 70c · p 0.7599 (adj 0.7424) · $6.45 · thesis CAR:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 64c · p 0.7013 (adj 0.6847) · $5.48 · thesis CAR:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 11c · p 0.1573 (adj 0.1442) · $2.86 · thesis CHI:OFFENSE_4PLUS
- Calum Ritchie: 1+ assists YES @ 27c · p 0.3515 (adj 0.3057) · $3.03 · thesis NYI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7214 (adj 0.6295) · $6.91 · thesis CHI:SUPPRESSED
- Bo Horvat: 1+ goals NO @ 62c · p 0.6727 (adj 0.6583) · $6.3 · thesis NYI:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.7987 (adj 0.7569) · $7.95 · thesis SJS:SUPPRESSED
- Collin Graf: 1+ goals YES @ 15c · p 0.1915 (adj 0.1774) · $2.01 · thesis SJS:OFFENSE_4PLUS
- Mason McTavish: 1+ assists NO @ 70c · p 0.771 (adj 0.733) · $7.95 · thesis STL:SUPPRESSED
- Full Game: Over 7.5 goals scored YES @ 23c · p 0.2839 (adj 0.2545) · $1.91 · thesis GAME:HIGH_EVENT
- Martin Necas: 1+ goals NO @ 61c · p 0.7036 (adj 0.6789) · $5.97 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.6435 (adj 0.6189) · $5.97 · thesis COL:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0943 (adj 0.082) · $2.41 · thesis VGK:OFFENSE_4PLUS
- Marc Gatcomb: 1+ goals YES @ 11c · p 0.1462 (adj 0.1346) · $1.77 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ assists YES @ 29c · p 0.3729 (adj 0.329) · $2.76 · thesis VGK:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 66c · p 0.7043 (adj 0.692) · $5.16 · thesis TOR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 36/42 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.45, exp saves 24.51 (sd 6.77), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.34, exp saves 22.54 (sd 6.31), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 2+ goals | 0.061 | 0.075 | 9/94 | -0.005 | STANDARD |
| JJ Peterka: First Goalscorer | 0.038 | 0.050 | 5/ | -0.016 | STANDARD |
| Nick Schmaltz: First Goalscorer | 0.060 | 0.070 | 6/ | -0.004 | STANDARD |
| David Pastrnak: First Goalscorer | 0.060 | 0.070 | 7/ | -0.014 | STANDARD |
| James Hagens: First Goalscorer | 0.031 | 0.040 | 4/ | -0.012 | PRIOR_HEAVY |
| Dylan Guenther: First Goalscorer | 0.061 | 0.070 | 7/ | -0.013 | STANDARD |

**DAL @ BUF** · priced 115/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 25.45, exp saves 22.13 (sd 6.08), pull risk 0.053
- DAL net: Jake Oettinger (PROJECTED) exp shots 27.04, exp saves 23.32 (sd 6.53), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Power: 1+ assists | 0.385 | 0.310 | 32/70 | +0.050 | STANDARD |
| Zach Benson: 1+ points | 0.534 | 0.460 | 47/55 | +0.046 | STANDARD |
| Justin Danforth: 1+ goals | 0.119 | 0.050 | 7/97 | +0.044 | STANDARD |
| Jiri Kulich: 1+ goals | 0.211 | 0.145 | 15/86 | +0.052 | STANDARD |
| Zach Benson: 1+ assists | 0.369 | 0.305 | 32/71 | +0.034 | STANDARD |
| Tage Thompson: 1+ assists | 0.355 | 0.415 | 42/59 | +0.038 | STANDARD |

**NSH @ MTL** · priced 114/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.02, exp saves 24.31 (sd 6.59), pull risk 0.058
- NSH net: Juuse Saros (PROJECTED) exp shots 27.64, exp saves 23.63 (sd 6.6), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ points | 0.401 | 0.525 | 53/48 | +0.102 | STANDARD |
| Chris Kreider: 1+ assists | 0.204 | 0.325 | 34/69 | +0.091 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.476 | 0.370 | 39/65 | +0.070 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.354 | 0.250 | 26/76 | +0.081 | STANDARD |
| Nick Suzuki: 1+ assists | 0.511 | 0.595 | 61/42 | +0.052 | STANDARD |
| Chris Kreider: 2+ points | 0.097 | 0.165 | 18/85 | +0.044 | STANDARD |

**PHI @ OTT** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROBABLE) exp shots 23.58, exp saves 20.6 (sd 5.79), pull risk 0.046
- PHI net: Joseph Woll (PROJECTED) exp shots 28.92, exp saves 24.85 (sd 6.81), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.215 | 0.390 | 40/62 | +0.148 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.284 | 0.455 | 47/56 | +0.138 | PRIOR_HEAVY |
| William Eklund: 1+ points | 0.396 | 0.550 | 56/46 | +0.127 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.230 | 0.365 | 37/64 | +0.114 | PRIOR_HEAVY |
| William Eklund: 2+ points | 0.088 | 0.195 | 21/82 | +0.082 | STANDARD |
| Carter Yakemchuk: 2+ points | 0.043 | 0.135 | 15/88 | +0.070 | PRIOR_HEAVY |

**MIN @ TBL** · priced 153/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROBABLE) exp shots 26.09, exp saves 22.6 (sd 6.28), pull risk 0.063
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.6, exp saves 25.48 (sd 6.92), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.275 | 0.425 | 43/58 | +0.128 | STANDARD |
| John Carlson: 1+ points | 0.359 | 0.505 | 52/51 | +0.113 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.509 | 0.605 | 61/40 | +0.074 | STANDARD |
| Nikita Kucherov: 2+ points | 0.327 | 0.420 | 43/59 | +0.066 | STANDARD |
| John Carlson: 2+ points | 0.076 | 0.160 | 18/86 | +0.056 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.163 | 0.245 | 26/77 | +0.055 | STANDARD |

**VAN @ CAR** · priced 165/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.48, exp saves 19.7 (sd 5.71), pull risk 0.056
- VAN net: Kevin Lankinen (PROJECTED) exp shots 32.08, exp saves 27.05 (sd 7.51), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.353 | 0.515 | 53/50 | +0.129 | STANDARD |
| Sebastian Aho: 1+ points | 0.546 | 0.675 | 68/33 | +0.109 | STANDARD |
| Sebastian Aho: 2+ points | 0.189 | 0.315 | 32/69 | +0.107 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.425 | 0.535 | 55/48 | +0.078 | STANDARD |
| Sebastian Aho: 2+ assists | 0.069 | 0.175 | 19/84 | +0.081 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.346 | 0.445 | 46/57 | +0.066 | STANDARD |

**CHI @ NYI** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 24.34, exp saves 21.41 (sd 5.93), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.5 (sd 7.18), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.279 | 0.420 | 43/59 | +0.114 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.227 | 0.340 | 35/67 | +0.088 | STANDARD |
| Kyle Palmieri: 1+ points | 0.427 | 0.530 | 54/48 | +0.075 | STANDARD |
| Patrick Kane: 1+ points | 0.456 | 0.555 | 57/46 | +0.067 | STANDARD |
| Calum Ritchie: 1+ assists | 0.351 | 0.260 | 27/75 | +0.068 | STANDARD |
| Patrick Kane: 2+ points | 0.130 | 0.205 | 22/81 | +0.049 | STANDARD |

**SJS @ STL** · priced 152/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 25.77, exp saves 22.28 (sd 6.19), pull risk 0.06
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.07, exp saves 23.04 (sd 6.56), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dmitry Orlov: 1+ assists | 0.354 | 0.265 | 29/76 | +0.049 | STANDARD |
| Mason Marchment: 1+ assists | 0.227 | 0.315 | 33/70 | +0.058 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.201 | 0.285 | 29/72 | +0.065 | PRIOR_HEAVY |
| Dmitry Orlov: 1+ points | 0.397 | 0.315 | 33/70 | +0.052 | STANDARD |
| Adam Jiricek: 1+ points | 0.312 | 0.390 | 41/63 | +0.041 | PRIOR_HEAVY |
| Mason McTavish: 1+ assists | 0.229 | 0.305 | 31/70 | +0.056 | STANDARD |

**COL @ CGY** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 32.7, exp saves 27.87 (sd 7.48), pull risk 0.073
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.32, exp saves 22.97 (sd 6.27), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.282 | 0.525 | 54/49 | +0.211 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.454 | 0.660 | 67/35 | +0.180 | STANDARD |
| Cale Makar: 1+ assists | 0.401 | 0.590 | 60/42 | +0.162 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.122 | 0.300 | 31/71 | +0.154 | STANDARD |
| Cale Makar: 1+ points | 0.498 | 0.670 | 68/34 | +0.146 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.085 | 0.245 | 25/76 | +0.142 | STANDARD |

**TOR @ VGK** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 24.89, exp saves 21.95 (sd 6.02), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.39, exp saves 26.52 (sd 7.32), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.282 | 0.400 | 41/61 | +0.092 | STANDARD |
| Gavin McKenna: 1+ points | 0.302 | 0.415 | 43/60 | +0.081 | PRIOR_HEAVY |
| Gavin McKenna: 1+ assists | 0.182 | 0.290 | 30/72 | +0.084 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.262 | 0.370 | 38/64 | +0.082 | STANDARD |
| Darren Raddysh: 1+ points | 0.374 | 0.480 | 50/54 | +0.069 | STANDARD |
| Kirill Marchenko: 1+ points | 0.441 | 0.545 | 57/48 | +0.061 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
