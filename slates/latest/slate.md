# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-27T13:10:49Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3878 · contracts joined: 1927 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1652, 'OK': 134, 'NO_EDGE': 141}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 240, 'game_early_goal': 11, 'first_goal': 292, 'game_winner': 22, 'player_goals': 507, 'game_overtime': 11, 'player_points': 327, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 2026-10-27T23:00:00Z | T-6h | 0.506 | 0.494 | 0.195 | 5.42 | 2.73 | 2.69 | 231 (25/206) | PROJECTED/PROJECTED |
| BOS @ CAR | 2026-10-28T00:00:00Z | T-6h | 0.585 | 0.415 | 0.174 | 6.21 | 3.39 | 2.83 | 231 (25/206) | PROJECTED/PROJECTED |
| LAK @ CHI | 2026-10-28T00:00:00Z | T-6h | 0.502 | 0.498 | 0.188 | 5.58 | 2.80 | 2.78 | 210 (25/185) | PROJECTED/PROJECTED |
| MTL @ STL | 2026-10-28T00:00:00Z | T-6h | 0.578 | 0.422 | 0.168 | 6.06 | 3.27 | 2.79 | 221 (25/196) | PROJECTED/PROJECTED |
| NYI @ NSH | 2026-10-28T00:00:00Z | T-6h | 0.530 | 0.470 | 0.177 | 6.19 | 3.19 | 3.00 | 217 (25/192) | PROJECTED/PROJECTED |
| NJD @ DAL | 2026-10-28T00:00:00Z | T-6h | 0.549 | 0.451 | 0.183 | 5.69 | 2.99 | 2.70 | 225 (25/200) | PROJECTED/PROJECTED |
| FLA @ WPG | 2026-10-28T00:00:00Z | T-6h | 0.531 | 0.469 | 0.179 | 5.95 | 3.06 | 2.90 | 223 (25/198) | PROJECTED/PROJECTED |
| MIN @ UTA | 2026-10-28T01:00:00Z | T-6h | 0.543 | 0.457 | 0.179 | 6.29 | 3.28 | 3.00 | 216 (25/191) | PROJECTED/PROJECTED |
| OTT @ VGK | 2026-10-28T02:00:00Z | T-12h | 0.596 | 0.405 | 0.168 | 6.66 | 3.65 | 3.01 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-12h | 0.638 | 0.362 | 0.159 | 6.80 | 3.85 | 2.95 | 51 (25/26) | PROJECTED/PROJECTED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-12h | 0.473 | 0.527 | 0.168 | 6.68 | 3.25 | 3.43 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT27CBJPHI-5 | game_total | 0.665 | 0.755 | 0.738 | 76 | 25 | no | +0.072 | OK |
| KXNHLTOTAL-26OCT27LACHI-7 | game_total | 0.342 | 0.440 | 0.420 | 45 | 57 | no | +0.071 | OK |
| KXNHLTOTAL-26OCT27LACHI-6 | game_total | 0.454 | 0.550 | 0.531 | 56 | 46 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ3 | team_total | 0.515 | 0.605 | 0.587 | 61 | 40 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT27LACHI-5 | game_total | 0.691 | 0.775 | 0.760 | 78 | 23 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ4 | team_total | 0.292 | 0.380 | 0.362 | 39 | 63 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA4 | team_total | 0.315 | 0.400 | 0.382 | 41 | 61 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-6 | game_total | 0.425 | 0.505 | 0.489 | 51 | 50 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-7 | game_total | 0.318 | 0.395 | 0.379 | 40 | 61 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA3 | team_total | 0.539 | 0.620 | 0.604 | 63 | 39 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA3 | team_total | 0.561 | 0.635 | 0.621 | 64 | 37 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ2 | team_total | 0.747 | 0.820 | 0.807 | 83 | 19 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA5 | team_total | 0.147 | 0.220 | 0.204 | 23 | 79 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT27LACHI-4 | game_total | 0.791 | 0.860 | 0.848 | 87 | 15 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-4 | game_total | 0.771 | 0.835 | 0.824 | 84 | 17 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA4 | team_total | 0.337 | 0.410 | 0.395 | 42 | 60 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT27LACHI-8 | game_total | 0.173 | 0.240 | 0.225 | 25 | 77 | no | +0.044 | OK |
| KXNHLGAME-26OCT27FLAWPG-FLA | game_winner | 0.469 | 0.535 | 0.522 | 54 | 47 | no | +0.043 | OK |
| KXNHLGAME-26OCT27FLAWPG-WPG | game_winner | 0.531 | 0.465 | 0.478 | 47 | 54 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL3 | team_total | 0.532 | 0.595 | 0.583 | 60 | 41 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA3 | game_spread | 0.149 | 0.205 | 0.193 | 21 | 80 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-8 | game_total | 0.159 | 0.215 | 0.203 | 22 | 79 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ3 | game_spread | 0.140 | 0.195 | 0.183 | 20 | 81 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA2 | game_spread | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA2 | team_total | 0.762 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL4 | team_total | 0.318 | 0.375 | 0.363 | 38 | 63 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ5 | team_total | 0.134 | 0.195 | 0.181 | 21 | 82 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT27LACHI-9 | game_total | 0.115 | 0.170 | 0.158 | 18 | 84 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ2 | game_spread | 0.260 | 0.315 | 0.303 | 32 | 69 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR3 | game_spread | 0.233 | 0.290 | 0.278 | 30 | 72 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ4 | team_total | 0.293 | 0.350 | 0.338 | 36 | 66 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA2 | team_total | 0.779 | 0.835 | 0.825 | 85 | 18 | no | +0.031 | OK |
| KXNHLGAME-26OCT27MTLSTL-MTL | game_winner | 0.422 | 0.475 | 0.464 | 48 | 53 | no | +0.030 | OK |
| KXNHLGAME-26OCT27MTLSTL-STL | game_winner | 0.578 | 0.525 | 0.536 | 53 | 48 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT27NJDAL-5 | game_total | 0.707 | 0.755 | 0.746 | 76 | 25 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA5 | team_total | 0.169 | 0.220 | 0.209 | 23 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL2 | team_total | 0.761 | 0.815 | 0.805 | 83 | 20 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI4 | team_total | 0.316 | 0.370 | 0.359 | 38 | 64 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-WPG2 | game_spread | 0.301 | 0.255 | 0.264 | 26 | 75 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-9 | game_total | 0.104 | 0.150 | 0.140 | 16 | 86 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-MTL3 | game_spread | 0.124 | 0.165 | 0.156 | 17 | 84 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-STL2 | game_spread | 0.350 | 0.305 | 0.314 | 31 | 70 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI3 | team_total | 0.538 | 0.585 | 0.576 | 59 | 42 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-MTL2 | game_spread | 0.224 | 0.265 | 0.256 | 27 | 74 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.195 | 0.235 | 0.227 | 24 | 77 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-5 | game_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ3 | game_spread | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR4 | team_total | 0.452 | 0.500 | 0.490 | 51 | 51 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR3 | team_total | 0.665 | 0.710 | 0.701 | 72 | 30 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR2 | game_spread | 0.364 | 0.405 | 0.397 | 41 | 60 | no | +0.020 | OK |
| KXNHLGAME-26OCT27CBJPHI-CBJ | game_winner | 0.494 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLGAME-26OCT27CBJPHI-PHI | game_winner | 0.506 | 0.465 | 0.473 | 47 | 54 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-5 | game_total | 0.739 | 0.775 | 0.768 | 78 | 23 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT27NJDAL-8 | game_total | 0.189 | 0.225 | 0.218 | 23 | 78 | no | +0.019 | OK |
| KXNHLGAME-26OCT27BOSCAR-BOS | game_winner | 0.415 | 0.375 | 0.383 | 38 | 63 | yes | +0.018 | OK |
| KXNHLGAME-26OCT27BOSCAR-CAR | game_winner | 0.585 | 0.625 | 0.617 | 63 | 38 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI5 | team_total | 0.151 | 0.195 | 0.186 | 21 | 82 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA2 | game_spread | 0.268 | 0.305 | 0.297 | 31 | 70 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ3 | team_total | 0.515 | 0.560 | 0.551 | 57 | 45 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA6 | team_total | 0.058 | 0.085 | 0.079 | 9 | 92 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-10 | game_total | 0.040 | 0.065 | 0.059 | 7 | 94 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27NJDAL-7 | game_total | 0.367 | 0.410 | 0.401 | 42 | 60 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27NJDAL-4 | game_total | 0.804 | 0.840 | 0.833 | 85 | 17 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-7 | game_total | 0.427 | 0.465 | 0.457 | 47 | 54 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL5 | team_total | 0.154 | 0.195 | 0.186 | 21 | 82 | no | +0.015 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.527 | 0.565 | 0.558 | 57 | 44 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ6 | team_total | 0.051 | 0.075 | 0.069 | 8 | 93 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-6 | game_total | 0.518 | 0.555 | 0.548 | 56 | 45 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT27LACHI-3 | game_total | 0.944 | 0.970 | 0.966 | 98 | 4 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-PHI4 | team_total | 0.301 | 0.340 | 0.332 | 35 | 67 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-6 | game_total | 0.540 | 0.575 | 0.568 | 58 | 43 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA6 | team_total | 0.072 | 0.095 | 0.090 | 10 | 91 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-3 | game_total | 0.935 | 0.965 | 0.960 | 98 | 5 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT27NYINSH-8 | game_total | 0.254 | 0.220 | 0.227 | 23 | 79 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI2 | team_total | 0.767 | 0.800 | 0.794 | 81 | 21 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.313 | 0.345 | 0.339 | 35 | 66 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ2 | team_total | 0.747 | 0.780 | 0.774 | 79 | 23 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT27NJDAL-3 | game_total | 0.947 | 0.970 | 0.966 | 98 | 4 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-4 | game_total | 0.841 | 0.870 | 0.865 | 88 | 14 | no | +0.010 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 0.506 | 0.529 | 0.195 | 0.227 | 5.42 | 5.74 | 0.993/0.964 | KXNHLTOTAL-26OCT27CBJPHI-7 +0.059 |
| BOS @ CAR | 0.585 | 0.566 | 0.174 | 0.208 | 6.21 | 6.68 | 0.997/0.968 | KXNHLTOTAL-26OCT27BOSCAR-7 +0.078 |
| LAK @ CHI | 0.502 | 0.472 | 0.188 | 0.220 | 5.58 | 6.02 | 1.003/0.989 | KXNHLTOTAL-26OCT27LACHI-7 +0.082 |
| MTL @ STL | 0.578 | 0.582 | 0.168 | 0.214 | 6.06 | 6.43 | 0.993/0.976 | KXNHLTOTAL-26OCT27MTLSTL-7 +0.061 |
| NYI @ NSH | 0.530 | 0.524 | 0.177 | 0.221 | 6.19 | 6.35 | 1.000/0.969 | KXNHLTOTAL-26OCT27NYINSH-7 +0.033 |
| NJD @ DAL | 0.549 | 0.558 | 0.183 | 0.224 | 5.69 | 6.01 | 0.986/0.973 | KXNHLTOTAL-26OCT27NJDAL-7 +0.057 |
| FLA @ WPG | 0.531 | 0.537 | 0.179 | 0.214 | 5.95 | 6.13 | 1.001/0.998 | KXNHLTOTAL-26OCT27FLAWPG-7 +0.031 |
| MIN @ UTA | 0.543 | 0.569 | 0.179 | 0.216 | 6.29 | 6.42 | 0.992/0.995 | KXNHLTEAMTOTAL-26OCT27MINUTA-UTA4 +0.042 |
| OTT @ VGK | 0.596 | 0.586 | 0.168 | 0.213 | 6.66 | 6.34 | 1.004/1.051 | KXNHLTOTAL-26OCT27OTTVGK-8 -0.054 |
| VAN @ ANA | 0.638 | 0.599 | 0.159 | 0.205 | 6.80 | 6.80 | 1.024/1.026 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.043 |
| BUF @ SJS | 0.473 | 0.529 | 0.168 | 0.221 | 6.68 | 6.50 | 1.034/0.998 | KXNHLGAME-26OCT27BUFSJ-BUF -0.057 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 29 recommended · full analysis in card.md / packet.json `thesis_card`

- Travis Sanheim: 1+ goals YES @ 8c · p 0.12 (adj 0.1087) · $3.02 · thesis PHI:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 14c · p 0.1891 (adj 0.1731) · $3.54 · thesis CBJ:WINS_BY_2PLUS
- Conor Garland: 1+ goals NO @ 84c · p 0.8844 (adj 0.8708) · $10.68 · thesis CBJ:SUPPRESSED
- Damon Severson: 1+ goals YES @ 8c · p 0.1177 (adj 0.102) · $2.01 · thesis CBJ:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 21c · p 0.2775 (adj 0.2581) · $6.02 · thesis BOS:OFFENSE_4PLUS
- Seth Jarvis: 1+ assists NO @ 65c · p 0.7298 (adj 0.6799) · $7.4 · thesis CAR:SUPPRESSED
- Full Game: Over 6.5 goals scored YES @ 47c · p 0.5385 (adj 0.5017) · $3.78 · thesis GAME:HIGH_EVENT
- Charlie McAvoy: 1+ assists NO @ 57c · p 0.6322 (adj 0.5986) · $6.93 · thesis BOS:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.081 (adj 0.0695) · $1.89 · thesis LAK:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 54c · p 0.6901 (adj 0.5893) · $10.68 · thesis CHI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 12c · p 0.159 (adj 0.143) · $2.28 · thesis CHI:OFFENSE_4PLUS
- Erik Gustafsson: 1+ assists NO @ 61c · p 0.7309 (adj 0.6458) · $8.09 · thesis LAK:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 25c · p 0.2963 (adj 0.2835) · $3.32 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 14c · p 0.1769 (adj 0.1614) · $1.76 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 35c · p 0.4232 (adj 0.3791) · $1.84 · thesis STL:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 14c · p 0.1734 (adj 0.1638) · $2.34 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2482 (adj 0.2374) · $3.3 · thesis NYI:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1648 (adj 0.1499) · $1.71 · thesis NSH:OFFENSE_4PLUS
- Victor Eklund: 1+ assists NO @ 70c · p 0.8002 (adj 0.7286) · $10.6 · thesis NYI:SUPPRESSED
- Connor Brown: 1+ goals YES @ 11c · p 0.1689 (adj 0.1529) · $5.1 · thesis NJD:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1249 (adj 0.1087) · $1.76 · thesis NJD:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 69c · p 0.7911 (adj 0.7221) · $9.0 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 56c · p 0.6304 (adj 0.5927) · $6.58 · thesis NJD:SUPPRESSED
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3376 (adj 0.3245) · $3.34 · thesis WPG:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7389 (adj 0.7242) · $7.83 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 79c · p 0.8497 (adj 0.8174) · $7.36 · thesis WPG:WINS
- Sam Reinhart: 1+ assists NO @ 64c · p 0.7072 (adj 0.6711) · $5.15 · thesis FLA:SUPPRESSED
- Buffalo wins by over 2.5 goals NO @ 77c · p 0.8365 (adj 0.8008) · $10.09 · thesis SJS:WINS
- San Jose wins by over 1.5 goals YES @ 25c · p 0.3168 (adj 0.2809) · $2.0 · thesis SJS:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ PHI** · priced 172/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 27.63, exp saves 24.06 (sd 6.47), pull risk 0.048
- CBJ net: Jet Greaves (PROJECTED) exp shots 25.48, exp saves 22.1 (sd 6.13), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Werenski: 1+ assists | 0.443 | 0.590 | 61/43 | +0.110 | STANDARD |
| Zach Werenski: 2+ points | 0.194 | 0.310 | 34/72 | +0.072 | STANDARD |
| Zach Werenski: 1+ points | 0.546 | 0.655 | 69/38 | +0.057 | STANDARD |
| Travis Sanheim: 1+ points | 0.420 | 0.315 | 33/70 | +0.074 | STANDARD |
| Denver Barkey: 1+ assists | 0.307 | 0.215 | 24/81 | +0.055 | STANDARD |
| Travis Sanheim: 1+ assists | 0.342 | 0.250 | 27/77 | +0.058 | STANDARD |

**BOS @ CAR** · priced 173/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.29, exp saves 20.3 (sd 5.96), pull risk 0.067
- BOS net: Jeremy Swayman (PROJECTED) exp shots 32.38, exp saves 27.52 (sd 7.59), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sean Walker: 1+ points | 0.411 | 0.300 | 33/73 | +0.066 | STANDARD |
| Sean Walker: 1+ assists | 0.338 | 0.230 | 26/80 | +0.064 | STANDARD |
| K'Andre Miller: 1+ points | 0.425 | 0.320 | 35/71 | +0.059 | STANDARD |
| Casey Mittelstadt: 1+ points | 0.405 | 0.300 | 31/71 | +0.080 | STANDARD |
| K'Andre Miller: 1+ assists | 0.369 | 0.265 | 28/75 | +0.075 | STANDARD |
| Seth Jarvis: 1+ assists | 0.270 | 0.370 | 39/65 | +0.064 | STANDARD |

**LAK @ CHI** · priced 156/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.78, exp saves 24.8 (sd 6.73), pull risk 0.059
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.18, exp saves 21.9 (sd 6.22), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.310 | 0.465 | 47/54 | +0.133 | STANDARD |
| Patrick Kane: 1+ points | 0.476 | 0.615 | 63/40 | +0.107 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.269 | 0.400 | 41/61 | +0.104 | STANDARD |
| Erik Gustafsson: 1+ points | 0.320 | 0.450 | 47/57 | +0.093 | STANDARD |
| Connor Bedard: 1+ assists | 0.378 | 0.470 | 48/54 | +0.065 | STANDARD |
| Artemi Panarin: 1+ assists | 0.399 | 0.490 | 50/52 | +0.064 | STANDARD |

**MTL @ STL** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.31, exp saves 22.97 (sd 6.32), pull risk 0.056
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.26, exp saves 23.13 (sd 6.58), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Philip Broberg: 1+ assists | 0.423 | 0.335 | 35/68 | +0.057 | STANDARD |
| Philip Broberg: 1+ points | 0.486 | 0.400 | 42/62 | +0.049 | STANDARD |
| Jake Neighbours: 1+ assists | 0.321 | 0.240 | 26/78 | +0.048 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.244 | 0.165 | 19/86 | +0.043 | STANDARD |
| Oliver Kapanen: 1+ assists | 0.223 | 0.295 | 31/72 | +0.043 | STANDARD |
| Oliver Kapanen: 1+ points | 0.366 | 0.435 | 46/59 | +0.027 | STANDARD |

**NYI @ NSH** · priced 160/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 28.8, exp saves 24.86 (sd 6.85), pull risk 0.06
- NYI net: Semyon Varlamov (PROJECTED) exp shots 27.04, exp saves 23.37 (sd 6.56), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ assists | 0.200 | 0.310 | 32/70 | +0.086 | STANDARD |
| Emil Heineman: 1+ assists | 0.269 | 0.170 | 20/86 | +0.058 | STANDARD |
| Matthew Wood: 1+ points | 0.405 | 0.310 | 34/72 | +0.049 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.333 | 0.255 | 27/76 | +0.049 | STANDARD |
| Ondrej Palat: 1+ goals | 0.158 | 0.080 | 12/96 | +0.030 | STANDARD |
| Mavrik Bourque: 1+ goals | 0.211 | 0.140 | 17/89 | +0.031 | STANDARD |

**NJD @ DAL** · priced 164/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.96, exp saves 23.53 (sd 6.41), pull risk 0.054
- NJD net: Jake Allen (PROJECTED) exp shots 26.01, exp saves 22.54 (sd 6.3), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.209 | 0.315 | 32/69 | +0.086 | STANDARD |
| Luke Evangelista: 1+ points | 0.365 | 0.460 | 47/55 | +0.068 | STANDARD |
| Thomas Harley: 1+ assists | 0.417 | 0.330 | 34/68 | +0.061 | STANDARD |
| Jack Hughes: 1+ assists | 0.370 | 0.445 | 45/56 | +0.053 | STANDARD |
| Thomas Harley: 1+ points | 0.475 | 0.400 | 43/63 | +0.028 | STANDARD |
| Jack Hughes: 1+ points | 0.548 | 0.620 | 65/41 | +0.025 | STANDARD |

**FLA @ WPG** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.13, exp saves 23.53 (sd 6.49), pull risk 0.055
- FLA net: Akira Schmid (PROJECTED) exp shots 26.32, exp saves 22.67 (sd 6.32), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.476 | 0.570 | 60/46 | +0.046 | STANDARD |
| Seth Jones: 1+ assists | 0.359 | 0.450 | 46/56 | +0.064 | STANDARD |
| Seth Jones: 1+ points | 0.414 | 0.500 | 53/53 | +0.039 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.436 | 0.520 | 53/49 | +0.057 | STANDARD |
| Brady Tkachuk: 1+ points | 0.500 | 0.575 | 60/45 | +0.032 | STANDARD |
| Sam Reinhart: 1+ assists | 0.293 | 0.365 | 37/64 | +0.051 | STANDARD |

**MIN @ UTA** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.57), pull risk 0.056
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.67, exp saves 24.52 (sd 6.8), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 2+ goals | 0.013 | 0.495 | 98/99 | -0.004 | STANDARD |
| Kirill Kaprizov: 4+ points | 0.017 | 0.495 | 97/98 | +0.002 | STANDARD |
| Michael McCarron: 1+ goals | 0.117 | 0.500 | 98/98 | -0.098 | STANDARD |
| Clayton Keller: 1+ points | 0.599 | 0.360 | 70/98 | -0.116 | STANDARD |
| Dylan Guenther: 1+ points | 0.562 | 0.330 | 64/98 | -0.094 | STANDARD |
| Nick Schmaltz: 1+ points | 0.555 | 0.325 | 63/98 | -0.091 | STANDARD |

**OTT @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.26, exp saves 22.89 (sd 6.32), pull risk 0.053
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.79, exp saves 22.83 (sd 6.49), pull risk 0.074

**VAN @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 23.87, exp saves 20.89 (sd 5.94), pull risk 0.059
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.6, exp saves 26.65 (sd 7.58), pull risk 0.096

**BUF @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.51, exp saves 24.66 (sd 6.74), pull risk 0.066
- BUF net: Colten Ellis (PROJECTED) exp shots 27.09, exp saves 23.32 (sd 6.57), pull risk 0.071

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
