# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T16:17:54Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4036 · contracts joined: 2384 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2109, 'OK': 130, 'NO_EDGE': 145}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 314, 'game_early_goal': 11, 'first_goal': 394, 'game_winner': 22, 'player_goals': 686, 'game_overtime': 11, 'player_points': 426, 'game_spread': 44, 'team_total': 110, 'game_total': 99, 'goalie_saves': 3}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-6h | 0.513 | 0.487 | 0.170 | 6.53 | 3.31 | 3.22 | 214 (25/189) | PROBABLE/PROJECTED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-6h | 0.513 | 0.487 | 0.179 | 6.06 | 3.06 | 3.00 | 210 (25/185) | PROBABLE/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-6h | 0.749 | 0.251 | 0.140 | 6.33 | 4.00 | 2.33 | 210 (25/185) | PROJECTED/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-6h | 0.560 | 0.440 | 0.182 | 5.95 | 3.17 | 2.78 | 223 (25/198) | PROJECTED/PROJECTED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-6h | 0.444 | 0.556 | 0.181 | 6.08 | 2.86 | 3.22 | 216 (25/191) | PROBABLE/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-6h | 0.617 | 0.384 | 0.169 | 6.00 | 3.36 | 2.64 | 226 (25/201) | PROJECTED/PROJECTED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-6h | 0.464 | 0.536 | 0.170 | 6.47 | 3.10 | 3.37 | 222 (25/197) | PROJECTED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-6h | 0.446 | 0.554 | 0.178 | 6.02 | 2.85 | 3.17 | 202 (25/177) | PROBABLE/PROJECTED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-6h | 0.598 | 0.402 | 0.173 | 6.40 | 3.52 | 2.89 | 211 (25/186) | CONFIRMED/PROJECTED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-6h | 0.608 | 0.392 | 0.162 | 7.02 | 3.87 | 3.15 | 231 (25/206) | PROJECTED/PROJECTED |
| NSH @ COL | 2026-11-06T02:30:00Z | T-6h | 0.652 | 0.348 | 0.160 | 6.61 | 3.80 | 2.81 | 219 (25/194) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV05STLNJ-STL | game_winner | 0.440 | 0.335 | 0.355 | 34 | 67 | yes | +0.084 | OK |
| KXNHLGAME-26NOV05STLNJ-NJ | game_winner | 0.560 | 0.665 | 0.645 | 67 | 34 | no | +0.084 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.444 | 0.355 | 0.372 | 36 | 65 | yes | +0.068 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.556 | 0.645 | 0.628 | 65 | 36 | no | +0.068 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.487 | 0.575 | 0.558 | 58 | 43 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ2 | game_spread | 0.332 | 0.415 | 0.398 | 42 | 59 | no | +0.061 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ3 | game_spread | 0.205 | 0.285 | 0.268 | 29 | 72 | no | +0.061 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.385 | 0.465 | 0.449 | 47 | 54 | no | +0.058 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.513 | 0.435 | 0.450 | 44 | 57 | yes | +0.056 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.329 | 0.405 | 0.389 | 41 | 60 | no | +0.055 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.273 | 0.345 | 0.330 | 35 | 66 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.402 | 0.335 | 0.348 | 34 | 67 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.622 | 0.690 | 0.677 | 70 | 32 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.402 | 0.475 | 0.460 | 49 | 54 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.363 | 0.430 | 0.416 | 44 | 58 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.216 | 0.275 | 0.263 | 28 | 73 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.415 | 0.480 | 0.467 | 49 | 53 | no | +0.038 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL2 | game_spread | 0.227 | 0.175 | 0.185 | 18 | 83 | yes | +0.037 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.249 | 0.305 | 0.293 | 31 | 70 | no | +0.037 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.598 | 0.655 | 0.644 | 66 | 35 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.287 | 0.235 | 0.245 | 24 | 77 | yes | +0.035 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.213 | 0.165 | 0.174 | 17 | 84 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.583 | 0.635 | 0.625 | 64 | 37 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.373 | 0.440 | 0.426 | 46 | 58 | no | +0.030 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.251 | 0.205 | 0.214 | 21 | 80 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.376 | 0.425 | 0.415 | 43 | 58 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.536 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05CARNYI-NYI2 | game_spread | 0.238 | 0.195 | 0.203 | 20 | 81 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.796 | 0.845 | 0.836 | 86 | 17 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 | team_total | 0.551 | 0.505 | 0.514 | 51 | 50 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.172 | 0.135 | 0.142 | 14 | 87 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.828 | 0.870 | 0.862 | 88 | 14 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.582 | 0.635 | 0.625 | 65 | 38 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.376 | 0.330 | 0.339 | 34 | 68 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.597 | 0.550 | 0.560 | 56 | 46 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG3 | team_total | 0.686 | 0.735 | 0.726 | 75 | 28 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5 | team_total | 0.168 | 0.130 | 0.137 | 14 | 88 | yes | +0.020 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.304 | 0.265 | 0.272 | 27 | 74 | yes | +0.020 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.617 | 0.575 | 0.583 | 58 | 43 | yes | +0.019 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.384 | 0.425 | 0.417 | 43 | 58 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.749 | 0.785 | 0.778 | 79 | 22 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.151 | 0.190 | 0.182 | 20 | 82 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 | team_total | 0.333 | 0.295 | 0.302 | 30 | 71 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.627 | 0.675 | 0.666 | 69 | 34 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL4 | team_total | 0.310 | 0.270 | 0.278 | 28 | 74 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI3 | team_total | 0.496 | 0.535 | 0.527 | 54 | 47 | no | +0.016 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.513 | 0.475 | 0.483 | 48 | 53 | yes | +0.016 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.487 | 0.525 | 0.517 | 53 | 48 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.173 | 0.205 | 0.198 | 21 | 80 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.911 | 0.940 | 0.935 | 95 | 7 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.468 | 0.505 | 0.498 | 51 | 50 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.152 | 0.120 | 0.126 | 13 | 89 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.328 | 0.295 | 0.301 | 30 | 71 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.786 | 0.815 | 0.809 | 82 | 19 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG2 | team_total | 0.859 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN3 | game_spread | 0.119 | 0.095 | 0.100 | 10 | 91 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 | team_total | 0.390 | 0.435 | 0.426 | 45 | 58 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-NYR6 | team_total | 0.119 | 0.095 | 0.099 | 10 | 91 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5 | team_total | 0.224 | 0.190 | 0.196 | 20 | 82 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.282 | 0.315 | 0.308 | 32 | 69 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI4 | team_total | 0.282 | 0.320 | 0.312 | 33 | 69 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.591 | 0.625 | 0.618 | 63 | 38 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-MTL6 | team_total | 0.119 | 0.095 | 0.099 | 10 | 91 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ2 | team_total | 0.818 | 0.860 | 0.852 | 88 | 16 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI2 | game_spread | 0.196 | 0.225 | 0.219 | 23 | 78 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.206 | 0.240 | 0.233 | 25 | 77 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4 | team_total | 0.336 | 0.300 | 0.307 | 31 | 71 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL6 | team_total | 0.064 | 0.040 | 0.044 | 5 | 97 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET6 | team_total | 0.085 | 0.060 | 0.064 | 7 | 95 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.778 | 0.815 | 0.808 | 83 | 20 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.226 | 0.265 | 0.257 | 28 | 75 | no | +0.011 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.256 | 0.285 | 0.279 | 29 | 72 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT3 | team_total | 0.604 | 0.635 | 0.629 | 64 | 37 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5 | team_total | 0.285 | 0.320 | 0.313 | 33 | 69 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN6 | team_total | 0.073 | 0.050 | 0.054 | 6 | 96 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK5 | team_total | 0.189 | 0.225 | 0.217 | 24 | 79 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV05BOSPIT-6 | game_total | 0.605 | 0.635 | 0.629 | 64 | 37 | no | +0.009 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.513 | 0.522 | 0.170 | 0.218 | 6.53 | 6.54 | 0.948/0.998 | KXNHLSPREAD-26NOV05UTAMTL-UTA2 -0.015 |
| VGK @ DET | 0.513 | 0.451 | 0.179 | 0.215 | 6.06 | 6.28 | 1.020/1.004 | KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 +0.068 |
| CHI @ TBL | 0.749 | 0.718 | 0.140 | 0.189 | 6.33 | 6.39 | 0.958/1.026 | KXNHLTEAMTOTAL-26NOV05CHITB-CHI3 +0.043 |
| STL @ NJD | 0.560 | 0.558 | 0.182 | 0.217 | 5.95 | 6.19 | 0.960/0.993 | KXNHLTOTAL-26NOV05STLNJ-7 +0.048 |
| CAR @ NYI | 0.444 | 0.473 | 0.181 | 0.219 | 6.08 | 6.38 | 0.974/0.990 | KXNHLTOTAL-26NOV05CARNYI-7 +0.057 |
| PHI @ NYR | 0.617 | 0.539 | 0.169 | 0.225 | 6.00 | 5.98 | 0.987/0.992 | KXNHLGAME-26NOV05PHINYR-NYR -0.078 |
| BOS @ PIT | 0.464 | 0.518 | 0.170 | 0.220 | 6.47 | 6.69 | 1.033/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.068 |
| DAL @ CBJ | 0.446 | 0.523 | 0.178 | 0.224 | 6.02 | 6.15 | 1.000/0.987 | KXNHLGAME-26NOV05DALCBJ-DAL -0.077 |
| VAN @ WPG | 0.598 | 0.542 | 0.173 | 0.221 | 6.40 | 6.34 | 1.004/1.026 | KXNHLGAME-26NOV05VANWPG-VAN +0.056 |
| ANA @ EDM | 0.608 | 0.581 | 0.162 | 0.200 | 7.02 | 7.28 | 1.010/1.016 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4 +0.047 |
| NSH @ COL | 0.652 | 0.661 | 0.160 | 0.204 | 6.61 | 6.65 | 0.977/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.021 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Lawson Crouse: 1+ goals YES @ 18c · p 0.2267 (adj 0.2113) · $3.3 · thesis UTA:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 13c · p 0.1624 (adj 0.153) · $2.14 · thesis MTL:WINS_BY_2PLUS
- Noah Dobson: 1+ assists YES @ 32c · p 0.4005 (adj 0.3553) · $3.27 · thesis MTL:OFFENSE_4PLUS
- Chris Kreider: 1+ goals YES @ 19c · p 0.2289 (adj 0.2129) · $1.66 · thesis MTL:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0773 (adj 0.0655) · $1.36 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ assists YES @ 29c · p 0.3555 (adj 0.3177) · $2.12 · thesis VGK:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.2442 (adj 0.2294) · $4.06 · thesis CHI:OFFENSE_4PLUS
- Nikita Kucherov: 2+ assists NO @ 71c · p 0.7942 (adj 0.7471) · $10.14 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.5 (adj 0.4575) · $2.15 · thesis GAME:TIGHT
- Victor Hedman: 1+ goals NO @ 90c · p 0.9259 (adj 0.9169) · $10.14 · thesis DIFFUSE
- Robert Thomas: 1+ goals YES @ 21c · p 0.2703 (adj 0.2515) · $4.7 · thesis STL:OFFENSE_4PLUS
- Connor McMichael: 1+ goals YES @ 16c · p 0.1949 (adj 0.1837) · $2.08 · thesis STL:OFFENSE_4PLUS
- Dylan Holloway: 1+ goals YES @ 23c · p 0.2702 (adj 0.2576) · $2.4 · thesis STL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.6578 (adj 0.6434) · $5.83 · thesis NJD:SUPPRESSED
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1768 (adj 0.1626) · $3.43 · thesis NYI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7355 (adj 0.7179) · $10.1 · thesis CAR:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2598 (adj 0.2411) · $2.98 · thesis NYI:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 68c · p 0.7477 (adj 0.7114) · $7.59 · thesis PHI:SUPPRESSED
- Tye Kartye: 1+ assists YES @ 24c · p 0.3014 (adj 0.2632) · $1.7 · thesis NYR:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1887 (adj 0.1715) · $4.72 · thesis PIT:WINS_BY_2PLUS
- Rickard Rakell: 2+ goals YES @ 6c · p 0.0925 (adj 0.0806) · $1.62 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 33c · p 0.3909 (adj 0.3719) · $3.33 · thesis PIT:OFFENSE_4PLUS
- Ben Kindel: 1+ assists NO @ 70c · p 0.7601 (adj 0.725) · $6.68 · thesis PIT:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2885 (adj 0.2689) · $5.85 · thesis CBJ:OFFENSE_4PLUS
- Cole Sillinger: 1+ goals YES @ 14c · p 0.1784 (adj 0.1626) · $1.86 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.1082 (adj 0.0961) · $1.38 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2094 (adj 0.1946) · $2.1 · thesis CBJ:WINS_BY_2PLUS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2284 (adj 0.2101) · $4.4 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.2114 (adj 0.1973) · $4.17 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 14c · p 0.1851 (adj 0.1701) · $3.12 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 12c · p 0.1553 (adj 0.1427) · $2.18 · thesis VAN:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1266 (adj 0.1162) · $2.83 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 6c · p 0.0845 (adj 0.0771) · $1.67 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.2019 (adj 0.1889) · $2.96 · thesis ANA:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3193 (adj 0.3057) · $4.1 · thesis EDM:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 70c · p 0.7923 (adj 0.7437) · $10.62 · thesis NSH:SUPPRESSED
- Nathan MacKinnon: 1+ assists NO @ 39c · p 0.4689 (adj 0.4269) · $4.34 · thesis COL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROBABLE) exp shots 28.98, exp saves 25.14 (sd 6.82), pull risk 0.06
- UTA net: Sebastian Cossa (PROJECTED) exp shots 25.81, exp saves 22.19 (sd 6.28), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Dobson: 1+ assists | 0.401 | 0.310 | 32/70 | +0.065 | STANDARD |
| Logan Cooley: 1+ points | 0.517 | 0.605 | 62/41 | +0.056 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.504 | 0.585 | 60/43 | +0.049 | STANDARD |
| Chris Kreider: 1+ points | 0.433 | 0.355 | 36/65 | +0.057 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.263 | 0.335 | 35/68 | +0.042 | STANDARD |
| Chris Kreider: 1+ assists | 0.266 | 0.195 | 20/81 | +0.055 | STANDARD |

**VGK @ DET** · priced 153/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROBABLE) exp shots 26.45, exp saves 22.67 (sd 6.43), pull risk 0.073
- VGK net: Carter Hart (PROJECTED) exp shots 27.41, exp saves 23.73 (sd 6.45), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.425 | 0.520 | 54/50 | +0.057 | STANDARD |
| Jack Eichel: 1+ assists | 0.444 | 0.520 | 53/49 | +0.049 | STANDARD |
| Ivan Barbashev: 1+ assists | 0.355 | 0.280 | 29/73 | +0.051 | STANDARD |
| Ivan Barbashev: 1+ points | 0.500 | 0.425 | 43/58 | +0.053 | STANDARD |
| Jack Eichel: 2+ points | 0.244 | 0.315 | 33/70 | +0.041 | STANDARD |
| Lucas Raymond: 1+ assists | 0.357 | 0.425 | 44/59 | +0.036 | STANDARD |

**CHI @ TBL** · priced 148/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.1, exp saves 20.67 (sd 5.73), pull risk 0.041
- CHI net: Arvid Soderblom (PROJECTED) exp shots 30.41, exp saves 25.28 (sd 7.26), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 2+ points | 0.395 | 0.500 | 51/51 | +0.078 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.206 | 0.300 | 31/71 | +0.070 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.583 | 0.660 | 67/35 | +0.052 | STANDARD |
| Nikita Kucherov: 3+ points | 0.155 | 0.220 | 23/79 | +0.044 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.446 | 0.385 | 40/63 | +0.029 | STANDARD |
| Connor Bedard: 2+ points | 0.195 | 0.255 | 27/76 | +0.032 | STANDARD |

**STL @ NJD** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 24.87, exp saves 21.56 (sd 6.06), pull risk 0.055
- STL net: Joel Hofer (PROJECTED) exp shots 30.21, exp saves 25.98 (sd 7.14), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.238 | 0.360 | 37/65 | +0.096 | STANDARD |
| Jack Hughes: 1+ assists | 0.401 | 0.515 | 53/50 | +0.082 | STANDARD |
| Luke Evangelista: 1+ assists | 0.249 | 0.355 | 37/66 | +0.076 | STANDARD |
| Dylan Holloway: 1+ points | 0.540 | 0.460 | 47/55 | +0.052 | STANDARD |
| Luke Evangelista: 1+ points | 0.406 | 0.485 | 50/53 | +0.046 | STANDARD |
| Robert Thomas: 1+ goals | 0.270 | 0.195 | 21/82 | +0.049 | STANDARD |

**CAR @ NYI** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (PROBABLE) exp shots 29.43, exp saves 25.26 (sd 6.85), pull risk 0.066
- CAR net: Brandon Bussi (PROJECTED) exp shots 24.49, exp saves 21.2 (sd 6.05), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.495 | 0.620 | 64/40 | +0.088 | STANDARD |
| Sebastian Aho: 1+ assists | 0.316 | 0.430 | 45/59 | +0.077 | STANDARD |
| Brayden Schenn: 1+ points | 0.509 | 0.425 | 44/59 | +0.051 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.497 | 0.580 | 60/44 | +0.045 | STANDARD |
| Seth Jarvis: 1+ assists | 0.285 | 0.365 | 38/65 | +0.049 | STANDARD |
| Sebastian Aho: 2+ points | 0.151 | 0.230 | 26/80 | +0.037 | STANDARD |

**PHI @ NYR** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 25.8, exp saves 22.54 (sd 6.17), pull risk 0.05
- PHI net: Joseph Woll (PROJECTED) exp shots 26.19, exp saves 22.64 (sd 6.26), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ points | 0.418 | 0.495 | 51/52 | +0.045 | STANDARD |
| Tye Kartye: 1+ assists | 0.301 | 0.225 | 24/79 | +0.049 | STANDARD |
| Travis Konecny: 1+ assists | 0.252 | 0.325 | 33/68 | +0.052 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.476 | 0.540 | 55/47 | +0.037 | STANDARD |
| Christian Dvorak: 1+ points | 0.451 | 0.390 | 41/63 | +0.024 | STANDARD |
| Travis Sanheim: 1+ points | 0.368 | 0.310 | 32/70 | +0.033 | STANDARD |

**BOS @ PIT** · priced 163/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.87, exp saves 22.2 (sd 6.33), pull risk 0.071
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.09 (sd 6.88), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ goals | 0.391 | 0.315 | 33/70 | +0.045 | STANDARD |
| JJ Peterka: 1+ assists | 0.272 | 0.345 | 36/67 | +0.043 | STANDARD |
| David Pastrnak: 1+ assists | 0.462 | 0.535 | 55/48 | +0.040 | STANDARD |
| Pavel Zacha: 1+ assists | 0.362 | 0.435 | 45/58 | +0.041 | STANDARD |
| Ben Kindel: 1+ assists | 0.240 | 0.310 | 32/70 | +0.045 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.400 | 0.470 | 48/54 | +0.043 | STANDARD |

**DAL @ CBJ** · priced 147/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROBABLE) exp shots 25.44, exp saves 22.07 (sd 6.15), pull risk 0.058
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.62, exp saves 22.07 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.288 | 0.210 | 22/80 | +0.056 | STANDARD |
| Charlie Coyle: 1+ points | 0.564 | 0.495 | 52/53 | +0.026 | STANDARD |
| Charlie Coyle: 2+ points | 0.208 | 0.140 | 17/89 | +0.029 | STANDARD |
| Cole Sillinger: 1+ goals | 0.178 | 0.115 | 14/91 | +0.030 | STANDARD |
| Valeri Nichushkin: 1+ goals | 0.211 | 0.150 | 18/88 | +0.020 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.209 | 0.150 | 17/87 | +0.030 | STANDARD |

**VAN @ WPG** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 24.76, exp saves 21.5 (sd 6.07), pull risk 0.058
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.31, exp saves 25.1 (sd 6.85), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 1+ goals | 0.239 | 0.140 | 24/96 | -0.014 | STANDARD |
| Elias Pettersson (#25): 1+ goals | 0.063 | 0.160 | 31/99 | -0.053 | STANDARD |
| Neal Pionk: 1+ points | 0.461 | 0.550 | 56/46 | +0.062 | STANDARD |
| Kyle Connor: 1+ assists | 0.432 | 0.510 | 53/51 | +0.041 | STANDARD |
| Kyle Connor: 2+ points | 0.309 | 0.385 | 40/63 | +0.045 | STANDARD |
| Linus Karlsson: 1+ goals | 0.228 | 0.155 | 17/86 | +0.049 | STANDARD |

**ANA @ EDM** · priced 179/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.9, exp saves 24.11 (sd 6.81), pull risk 0.079
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.83, exp saves 23.49 (sd 6.9), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.383 | 0.545 | 56/47 | +0.129 | STANDARD |
| Leon Draisaitl: 3+ points | 0.150 | 0.280 | 30/74 | +0.097 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.157 | 0.275 | 29/74 | +0.089 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.510 | 0.615 | 62/39 | +0.083 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.373 | 0.270 | 28/74 | +0.079 | STANDARD |
| Connor McDavid: 1+ assists | 0.603 | 0.705 | 71/30 | +0.083 | STANDARD |

**NSH @ COL** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.73, exp saves 22.66 (sd 6.18), pull risk 0.047
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.24 (sd 7.61), pull risk 0.096

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.208 | 0.305 | 31/70 | +0.078 | STANDARD |
| Mavrik Bourque: 1+ points | 0.352 | 0.440 | 45/57 | +0.061 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.383 | 0.470 | 49/55 | +0.050 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.531 | 0.615 | 62/39 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.240 | 26/78 | +0.035 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.146 | 0.210 | 23/81 | +0.033 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
