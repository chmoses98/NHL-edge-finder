# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-27T15:46:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4448 · contracts joined: 2497 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2222, 'OK': 151, 'NO_EDGE': 124}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 355, 'game_early_goal': 11, 'first_goal': 399, 'game_winner': 22, 'player_goals': 695, 'game_overtime': 11, 'player_points': 486, 'goalie_saves': 1, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 2026-10-27T23:00:00Z | T-6h | 0.515 | 0.485 | 0.191 | 5.36 | 2.73 | 2.63 | 232 (25/207) | CONFIRMED/PROJECTED |
| BOS @ CAR | 2026-10-28T00:00:00Z | T-6h | 0.591 | 0.409 | 0.175 | 6.20 | 3.39 | 2.81 | 234 (25/209) | PROBABLE/PROJECTED |
| LAK @ CHI | 2026-10-28T00:00:00Z | T-6h | 0.508 | 0.491 | 0.192 | 5.56 | 2.80 | 2.76 | 219 (25/194) | CONFIRMED/PROJECTED |
| MTL @ STL | 2026-10-28T00:00:00Z | T-6h | 0.578 | 0.422 | 0.168 | 6.06 | 3.27 | 2.79 | 231 (25/206) | PROJECTED/PROJECTED |
| NYI @ NSH | 2026-10-28T00:00:00Z | T-6h | 0.530 | 0.470 | 0.177 | 6.19 | 3.19 | 3.00 | 227 (25/202) | PROJECTED/PROJECTED |
| NJD @ DAL | 2026-10-28T00:00:00Z | T-6h | 0.549 | 0.451 | 0.183 | 5.69 | 2.99 | 2.70 | 225 (25/200) | PROJECTED/PROJECTED |
| FLA @ WPG | 2026-10-28T00:00:00Z | T-6h | 0.522 | 0.478 | 0.178 | 5.98 | 3.05 | 2.92 | 223 (25/198) | PROBABLE/PROJECTED |
| MIN @ UTA | 2026-10-28T01:00:00Z | T-6h | 0.543 | 0.457 | 0.179 | 6.29 | 3.28 | 3.00 | 231 (25/206) | PROJECTED/PROJECTED |
| OTT @ VGK | 2026-10-28T02:00:00Z | T-6h | 0.596 | 0.405 | 0.168 | 6.66 | 3.65 | 3.01 | 229 (25/204) | PROJECTED/PROJECTED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-6h | 0.638 | 0.362 | 0.159 | 6.80 | 3.85 | 2.95 | 211 (25/186) | PROJECTED/PROJECTED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-6h | 0.473 | 0.527 | 0.168 | 6.68 | 3.25 | 3.43 | 235 (25/210) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ3 | team_total | 0.500 | 0.605 | 0.584 | 61 | 40 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT27LACHI-6 | game_total | 0.450 | 0.555 | 0.534 | 56 | 45 | no | +0.083 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-5 | game_total | 0.659 | 0.755 | 0.737 | 76 | 25 | no | +0.078 | OK |
| KXNHLTOTAL-26OCT27LACHI-7 | game_total | 0.345 | 0.445 | 0.424 | 45 | 56 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ4 | team_total | 0.280 | 0.380 | 0.359 | 39 | 63 | no | +0.073 | OK |
| KXNHLTOTAL-26OCT27LACHI-5 | game_total | 0.686 | 0.775 | 0.759 | 78 | 23 | no | +0.072 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-6 | game_total | 0.414 | 0.505 | 0.487 | 51 | 50 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA4 | team_total | 0.309 | 0.395 | 0.377 | 40 | 61 | no | +0.064 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-7 | game_total | 0.312 | 0.395 | 0.378 | 40 | 61 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA3 | team_total | 0.536 | 0.615 | 0.600 | 62 | 39 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-4 | game_total | 0.764 | 0.840 | 0.827 | 85 | 17 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ2 | team_total | 0.736 | 0.805 | 0.792 | 81 | 20 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA4 | team_total | 0.341 | 0.415 | 0.400 | 42 | 59 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT27LACHI-4 | game_total | 0.789 | 0.855 | 0.843 | 86 | 15 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL3 | team_total | 0.532 | 0.605 | 0.591 | 61 | 40 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ2 | game_spread | 0.248 | 0.315 | 0.301 | 32 | 69 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA3 | game_spread | 0.152 | 0.215 | 0.201 | 22 | 79 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL4 | team_total | 0.318 | 0.390 | 0.375 | 40 | 62 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA5 | team_total | 0.143 | 0.210 | 0.195 | 22 | 80 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-8 | game_total | 0.153 | 0.215 | 0.201 | 22 | 79 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA3 | team_total | 0.568 | 0.635 | 0.622 | 64 | 37 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT27LACHI-8 | game_total | 0.173 | 0.240 | 0.225 | 25 | 77 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ5 | team_total | 0.127 | 0.195 | 0.179 | 21 | 82 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ3 | game_spread | 0.137 | 0.195 | 0.182 | 20 | 81 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA2 | team_total | 0.758 | 0.820 | 0.809 | 83 | 19 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR3 | game_spread | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.041 | OK |
| KXNHLGAME-26OCT27MTLSTL-MTL | game_winner | 0.422 | 0.485 | 0.472 | 49 | 52 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL2 | team_total | 0.761 | 0.820 | 0.809 | 83 | 19 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA2 | team_total | 0.784 | 0.840 | 0.830 | 85 | 17 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-MTL3 | game_spread | 0.124 | 0.175 | 0.164 | 18 | 83 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT27LACHI-9 | game_total | 0.115 | 0.170 | 0.158 | 18 | 84 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL5 | team_total | 0.154 | 0.210 | 0.198 | 22 | 80 | no | +0.035 | OK |
| KXNHLGAME-26OCT27FLAWPG-WPG | game_winner | 0.522 | 0.465 | 0.476 | 47 | 54 | yes | +0.034 | OK |
| KXNHLGAME-26OCT27FLAWPG-FLA | game_winner | 0.478 | 0.535 | 0.524 | 54 | 47 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-9 | game_total | 0.098 | 0.145 | 0.134 | 15 | 86 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-MTL2 | game_spread | 0.224 | 0.275 | 0.264 | 28 | 73 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA5 | team_total | 0.176 | 0.230 | 0.218 | 24 | 78 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA2 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA3 | game_spread | 0.147 | 0.195 | 0.185 | 20 | 81 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ4 | team_total | 0.293 | 0.350 | 0.338 | 36 | 66 | no | +0.031 | OK |
| KXNHLGAME-26OCT27MTLSTL-STL | game_winner | 0.578 | 0.525 | 0.536 | 53 | 48 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT27NJDAL-5 | game_total | 0.707 | 0.755 | 0.746 | 76 | 25 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 | team_total | 0.454 | 0.510 | 0.499 | 52 | 50 | no | +0.029 | OK |
| KXNHLGAME-26OCT27CBJPHI-CBJ | game_winner | 0.485 | 0.535 | 0.525 | 54 | 47 | no | +0.028 | OK |
| KXNHLGAME-26OCT27CBJPHI-PHI | game_winner | 0.515 | 0.465 | 0.475 | 47 | 54 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI4 | team_total | 0.316 | 0.370 | 0.359 | 38 | 64 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI3 | team_total | 0.537 | 0.590 | 0.580 | 60 | 42 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR2 | game_spread | 0.367 | 0.415 | 0.405 | 42 | 59 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-VGK4 | team_total | 0.513 | 0.465 | 0.474 | 47 | 54 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT27MTLSTL-STL2 | game_spread | 0.350 | 0.305 | 0.314 | 31 | 70 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA2 | game_spread | 0.261 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-WPG2 | game_spread | 0.295 | 0.255 | 0.263 | 26 | 75 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-6 | game_total | 0.521 | 0.565 | 0.556 | 57 | 44 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-5 | game_total | 0.746 | 0.785 | 0.778 | 79 | 22 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-5 | game_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR4 | team_total | 0.451 | 0.500 | 0.490 | 51 | 51 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ2 | team_total | 0.747 | 0.785 | 0.778 | 79 | 22 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ3 | game_spread | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-4 | game_total | 0.841 | 0.875 | 0.869 | 88 | 13 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.313 | 0.355 | 0.346 | 36 | 65 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-10 | game_total | 0.036 | 0.065 | 0.058 | 7 | 94 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ6 | team_total | 0.045 | 0.080 | 0.072 | 9 | 93 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA6 | team_total | 0.056 | 0.085 | 0.078 | 9 | 92 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR3 | team_total | 0.668 | 0.710 | 0.702 | 72 | 30 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ3 | team_total | 0.515 | 0.555 | 0.547 | 56 | 45 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-SJ2 | game_spread | 0.270 | 0.235 | 0.242 | 24 | 77 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI5 | team_total | 0.153 | 0.195 | 0.186 | 21 | 82 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-3 | game_total | 0.930 | 0.960 | 0.955 | 97 | 5 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27LACHI-3 | game_total | 0.941 | 0.970 | 0.966 | 98 | 4 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27NJDAL-4 | game_total | 0.804 | 0.840 | 0.833 | 85 | 17 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-7 | game_total | 0.427 | 0.465 | 0.457 | 47 | 54 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-4 | game_total | 0.836 | 0.865 | 0.860 | 87 | 14 | no | +0.016 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.527 | 0.565 | 0.558 | 57 | 44 | no | +0.015 | OK |
| KXNHLGAME-26OCT27BUFSJ-SJ | game_winner | 0.473 | 0.435 | 0.442 | 44 | 57 | yes | +0.015 | OK |
| KXNHLGAME-26OCT27BOSCAR-BOS | game_winner | 0.409 | 0.375 | 0.382 | 38 | 63 | yes | +0.013 | OK |
| KXNHLGAME-26OCT27BOSCAR-CAR | game_winner | 0.591 | 0.625 | 0.618 | 63 | 38 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-6 | game_total | 0.540 | 0.575 | 0.568 | 58 | 43 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR2 | team_total | 0.850 | 0.880 | 0.874 | 89 | 13 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT27NYINSH-8 | game_total | 0.254 | 0.225 | 0.231 | 23 | 78 | yes | +0.012 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 0.515 | 0.522 | 0.191 | 0.221 | 5.36 | 5.75 | 0.994/0.964 | KXNHLTOTAL-26OCT27CBJPHI-6 +0.066 |
| BOS @ CAR | 0.591 | 0.564 | 0.175 | 0.206 | 6.20 | 6.69 | 1.000/0.968 | KXNHLTOTAL-26OCT27BOSCAR-7 +0.079 |
| LAK @ CHI | 0.508 | 0.475 | 0.192 | 0.219 | 5.56 | 5.98 | 0.988/0.989 | KXNHLTEAMTOTAL-26OCT27LACHI-LA4 +0.071 |
| MTL @ STL | 0.578 | 0.582 | 0.168 | 0.214 | 6.06 | 6.43 | 0.993/0.976 | KXNHLTOTAL-26OCT27MTLSTL-7 +0.061 |
| NYI @ NSH | 0.530 | 0.524 | 0.177 | 0.221 | 6.19 | 6.35 | 1.000/0.969 | KXNHLTOTAL-26OCT27NYINSH-7 +0.033 |
| NJD @ DAL | 0.549 | 0.558 | 0.183 | 0.224 | 5.69 | 6.01 | 0.986/0.973 | KXNHLTOTAL-26OCT27NJDAL-7 +0.057 |
| FLA @ WPG | 0.522 | 0.531 | 0.178 | 0.218 | 5.98 | 6.12 | 0.998/0.998 | KXNHLTEAMTOTAL-26OCT27FLAWPG-WPG3 +0.033 |
| MIN @ UTA | 0.543 | 0.569 | 0.179 | 0.216 | 6.29 | 6.42 | 0.992/0.995 | KXNHLTEAMTOTAL-26OCT27MINUTA-UTA4 +0.042 |
| OTT @ VGK | 0.596 | 0.586 | 0.168 | 0.213 | 6.66 | 6.34 | 1.004/1.051 | KXNHLTOTAL-26OCT27OTTVGK-8 -0.054 |
| VAN @ ANA | 0.638 | 0.599 | 0.159 | 0.205 | 6.80 | 6.80 | 1.024/1.026 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.043 |
| BUF @ SJS | 0.473 | 0.529 | 0.168 | 0.221 | 6.68 | 6.50 | 1.034/0.998 | KXNHLGAME-26OCT27BUFSJ-BUF -0.057 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Travis Sanheim: 1+ goals YES @ 8c · p 0.1185 (adj 0.1076) · $2.42 · thesis PHI:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1951 (adj 0.1826) · $2.87 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.1126 (adj 0.1007) · $1.64 · thesis CBJ:OFFENSE_4PLUS
- Adam Fantilli: 1+ goals NO @ 70c · p 0.7437 (adj 0.7315) · $6.53 · thesis CBJ:SUPPRESSED
- Casey Mittelstadt: 1+ goals YES @ 13c · p 0.1863 (adj 0.1697) · $3.64 · thesis BOS:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 21c · p 0.2746 (adj 0.256) · $4.56 · thesis BOS:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 7c · p 0.1095 (adj 0.0959) · $2.11 · thesis BOS:OFFENSE_4PLUS
- Ian Cole: 1+ goals YES @ 3c · p 0.0541 (adj 0.0468) · $1.39 · thesis CHI:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0764 (adj 0.0685) · $1.51 · thesis LAK:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 55c · p 0.6872 (adj 0.5915) · $6.66 · thesis CHI:SUPPRESSED
- Erik Gustafsson: 1+ assists NO @ 61c · p 0.7334 (adj 0.6499) · $7.56 · thesis LAK:SUPPRESSED
- Pius Suter: 1+ goals YES @ 14c · p 0.1769 (adj 0.1652) · $1.94 · thesis STL:OFFENSE_4PLUS
- Oliver Kapanen: 1+ goals NO @ 78c · p 0.8161 (adj 0.8058) · $7.43 · thesis MTL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 26c · p 0.2963 (adj 0.2847) · $1.62 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3367 (adj 0.3263) · $1.79 · thesis STL:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1648 (adj 0.1548) · $2.05 · thesis NSH:OFFENSE_4PLUS
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2112 (adj 0.1984) · $2.38 · thesis NSH:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 12c · p 0.1575 (adj 0.1431) · $1.93 · thesis NYI:OFFENSE_4PLUS
- Victor Eklund: 1+ assists NO @ 73c · p 0.8002 (adj 0.7576) · $7.1 · thesis NYI:SUPPRESSED
- Connor Brown: 1+ goals YES @ 11c · p 0.1689 (adj 0.1529) · $4.0 · thesis NJD:OFFENSE_4PLUS
- Jamie Benn: 1+ goals YES @ 13c · p 0.1706 (adj 0.158) · $2.41 · thesis DAL:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1249 (adj 0.1099) · $1.51 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 68c · p 0.7182 (adj 0.7074) · $4.06 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 66c · p 0.7178 (adj 0.7021) · $7.3 · thesis FLA:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 14c · p 0.1782 (adj 0.1649) · $1.94 · thesis WPG:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 69c · p 0.739 (adj 0.7242) · $5.74 · thesis FLA:SUPPRESSED
- Cole Koepke: 1+ goals YES @ 9c · p 0.1134 (adj 0.1063) · $1.1 · thesis WPG:WINS_BY_2PLUS
- Quinn Hughes: 1+ assists NO @ 39c · p 0.485 (adj 0.435) · $4.32 · thesis MIN:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 58c · p 0.6345 (adj 0.6184) · $4.21 · thesis MIN:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 19c · p 0.232 (adj 0.2165) · $2.03 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1552 (adj 0.1401) · $1.43 · thesis UTA:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0878 (adj 0.0759) · $1.18 · thesis VGK:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 59c · p 0.712 (adj 0.6294) · $7.28 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 12c · p 0.1492 (adj 0.1406) · $1.72 · thesis OTT:OFFENSE_4PLUS
- Ivan Barbashev: 1+ goals YES @ 21c · p 0.2479 (adj 0.2359) · $1.92 · thesis VGK:OFFENSE_4PLUS
- A.J. Greer: 2+ goals YES @ 2c · p 0.0389 (adj 0.0329) · $1.0 · thesis ANA:OFFENSE_4PLUS
- Max Sasson: 1+ goals YES @ 12c · p 0.1623 (adj 0.1492) · $2.48 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2379 (adj 0.2222) · $2.75 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2134 (adj 0.2001) · $2.47 · thesis VAN:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1775 (adj 0.1619) · $2.46 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 62c · p 0.6821 (adj 0.6653) · $7.76 · thesis BUF:SUPPRESSED
- San Jose wins by over 1.5 goals YES @ 24c · p 0.3168 (adj 0.2759) · $2.14 · thesis SJS:WINS_BY_2PLUS
- Ivar Stenberg: 1+ goals NO @ 77c · p 0.8133 (adj 0.8012) · $8.69 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ PHI** · priced 173/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.63, exp saves 24.08 (sd 6.41), pull risk 0.046
- CBJ net: Jet Greaves (PROJECTED) exp shots 25.48, exp saves 22.12 (sd 6.18), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Werenski: 1+ assists | 0.448 | 0.585 | 59/42 | +0.115 | STANDARD |
| Travis Sanheim: 1+ points | 0.421 | 0.310 | 32/70 | +0.086 | STANDARD |
| Zach Werenski: 2+ points | 0.191 | 0.300 | 32/72 | +0.075 | STANDARD |
| Zach Werenski: 1+ points | 0.557 | 0.655 | 67/36 | +0.067 | STANDARD |
| Valeri Nichushkin: 1+ points | 0.384 | 0.475 | 48/53 | +0.068 | STANDARD |
| Adam Fantilli: 1+ assists | 0.298 | 0.385 | 39/62 | +0.065 | STANDARD |

**BOS @ CAR** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.29, exp saves 20.3 (sd 5.93), pull risk 0.067
- BOS net: Jeremy Swayman (PROJECTED) exp shots 32.38, exp saves 27.54 (sd 7.64), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Casey Mittelstadt: 1+ points | 0.402 | 0.295 | 30/71 | +0.087 | STANDARD |
| Sean Walker: 1+ points | 0.401 | 0.305 | 31/70 | +0.076 | STANDARD |
| Seth Jarvis: 1+ assists | 0.256 | 0.350 | 37/67 | +0.058 | STANDARD |
| Sean Walker: 1+ assists | 0.331 | 0.240 | 26/78 | +0.058 | STANDARD |
| K'Andre Miller: 1+ assists | 0.350 | 0.270 | 28/74 | +0.056 | STANDARD |
| K'Andre Miller: 1+ points | 0.408 | 0.330 | 34/68 | +0.052 | STANDARD |

**LAK @ CHI** · priced 165/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 28.78, exp saves 24.84 (sd 6.75), pull risk 0.059
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.18, exp saves 21.9 (sd 6.11), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.313 | 0.460 | 47/55 | +0.120 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.267 | 0.395 | 40/61 | +0.107 | STANDARD |
| Patrick Kane: 1+ points | 0.478 | 0.605 | 61/40 | +0.105 | STANDARD |
| Erik Gustafsson: 1+ points | 0.322 | 0.420 | 43/59 | +0.071 | STANDARD |
| Artyom Levshunov: 1+ points | 0.333 | 0.240 | 26/78 | +0.060 | STANDARD |
| Connor Bedard: 1+ assists | 0.383 | 0.475 | 48/53 | +0.069 | STANDARD |

**MTL @ STL** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 26.31, exp saves 22.97 (sd 6.32), pull risk 0.056
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.26, exp saves 23.13 (sd 6.58), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ points | 0.420 | 0.315 | 34/71 | +0.065 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.310 | 0.225 | 24/79 | +0.057 | STANDARD |
| Philip Broberg: 1+ assists | 0.423 | 0.340 | 36/68 | +0.047 | STANDARD |
| Jake Neighbours: 1+ assists | 0.321 | 0.240 | 26/78 | +0.048 | STANDARD |
| Philip Broberg: 1+ points | 0.486 | 0.410 | 42/60 | +0.049 | STANDARD |
| Josh Anderson: 1+ points | 0.352 | 0.280 | 31/75 | +0.027 | STANDARD |

**NYI @ NSH** · priced 170/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 28.8, exp saves 24.86 (sd 6.85), pull risk 0.06
- NYI net: Semyon Varlamov (PROJECTED) exp shots 27.04, exp saves 23.37 (sd 6.56), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ points | 0.355 | 0.240 | 27/79 | +0.071 | STANDARD |
| Adam Wilsby: 1+ assists | 0.301 | 0.195 | 22/83 | +0.069 | STANDARD |
| Matthew Wood: 1+ points | 0.405 | 0.315 | 33/70 | +0.060 | STANDARD |
| Victor Eklund: 1+ assists | 0.200 | 0.285 | 30/73 | +0.056 | STANDARD |
| Emil Heineman: 1+ assists | 0.269 | 0.190 | 21/83 | +0.047 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.333 | 0.265 | 27/74 | +0.049 | STANDARD |

**NJD @ DAL** · priced 164/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.96, exp saves 23.53 (sd 6.41), pull risk 0.054
- NJD net: Jake Allen (PROJECTED) exp shots 26.01, exp saves 22.54 (sd 6.3), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.209 | 0.320 | 33/69 | +0.086 | STANDARD |
| Luke Evangelista: 1+ points | 0.365 | 0.460 | 47/55 | +0.068 | STANDARD |
| Thomas Harley: 1+ assists | 0.417 | 0.325 | 34/69 | +0.061 | STANDARD |
| Jack Hughes: 1+ points | 0.548 | 0.630 | 64/38 | +0.056 | STANDARD |
| Jack Hughes: 1+ assists | 0.370 | 0.450 | 46/56 | +0.053 | STANDARD |
| Thomas Harley: 1+ points | 0.476 | 0.400 | 42/62 | +0.039 | STANDARD |

**FLA @ WPG** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 27.13, exp saves 23.62 (sd 6.42), pull risk 0.052
- FLA net: Akira Schmid (PROJECTED) exp shots 26.32, exp saves 22.73 (sd 6.3), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.480 | 0.590 | 60/42 | +0.083 | STANDARD |
| Seth Jones: 1+ points | 0.414 | 0.520 | 53/49 | +0.078 | STANDARD |
| Seth Jones: 1+ assists | 0.357 | 0.455 | 46/55 | +0.076 | STANDARD |
| Brady Tkachuk: 1+ points | 0.501 | 0.595 | 60/41 | +0.072 | STANDARD |
| Sam Reinhart: 1+ assists | 0.293 | 0.385 | 40/63 | +0.061 | STANDARD |
| Sam Reinhart: 2+ points | 0.141 | 0.230 | 25/79 | +0.058 | STANDARD |

**MIN @ UTA** · priced 179/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.66, exp saves 24.15 (sd 6.57), pull risk 0.056
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.67, exp saves 24.52 (sd 6.8), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.258 | 0.375 | 39/64 | +0.085 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.404 | 0.515 | 52/49 | +0.088 | STANDARD |
| Quinn Hughes: 1+ assists | 0.515 | 0.615 | 62/39 | +0.078 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.617 | 0.710 | 73/31 | +0.058 | STANDARD |
| Quinn Hughes: 1+ points | 0.579 | 0.655 | 67/36 | +0.045 | STANDARD |
| Clayton Keller: 1+ assists | 0.454 | 0.525 | 53/48 | +0.049 | STANDARD |

**OTT @ VGK** · priced 175/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.26, exp saves 22.89 (sd 6.32), pull risk 0.053
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.79, exp saves 22.83 (sd 6.49), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.369 | 0.505 | 52/51 | +0.103 | STANDARD |
| Mitch Marner: 1+ assists | 0.402 | 0.535 | 54/47 | +0.110 | STANDARD |
| Jake Sanderson: 1+ assists | 0.288 | 0.415 | 42/59 | +0.105 | STANDARD |
| Shea Theodore: 1+ assists | 0.357 | 0.245 | 27/78 | +0.073 | STANDARD |
| Jack Eichel: 1+ points | 0.634 | 0.525 | 71/66 | -0.091 | STANDARD |
| Mitch Marner: 2+ points | 0.195 | 0.300 | 32/72 | +0.071 | STANDARD |

**VAN @ ANA** · priced 148/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 23.87, exp saves 20.89 (sd 5.94), pull risk 0.059
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.6, exp saves 26.65 (sd 7.58), pull risk 0.096

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Washe: 1+ points | 0.421 | 0.275 | 30/75 | +0.106 | STANDARD |
| Tim Washe: 1+ assists | 0.309 | 0.170 | 20/86 | +0.098 | STANDARD |
| A.J. Greer: 1+ goals | 0.261 | 0.160 | 17/85 | +0.081 | STANDARD |
| Alex Killorn: 1+ points | 0.477 | 0.380 | 40/64 | +0.060 | STANDARD |
| Alex Killorn: 1+ assists | 0.313 | 0.225 | 25/80 | +0.050 | STANDARD |
| Jake DeBrusk: 2+ points | 0.174 | 0.100 | 17/97 | -0.006 | STANDARD |

**BUF @ SJS** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 28.51, exp saves 24.66 (sd 6.74), pull risk 0.066
- BUF net: Colten Ellis (PROJECTED) exp shots 27.09, exp saves 23.32 (sd 6.57), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.432 | 0.580 | 59/43 | +0.121 | STANDARD |
| Ivar Stenberg: 1+ points | 0.414 | 0.545 | 55/46 | +0.108 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.410 | 0.525 | 53/48 | +0.093 | STANDARD |
| Rasmus Dahlin: 1+ points | 0.509 | 0.620 | 63/39 | +0.084 | STANDARD |
| Tage Thompson: 1+ assists | 0.330 | 0.440 | 45/57 | +0.083 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.276 | 0.385 | 40/63 | +0.078 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
