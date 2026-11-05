# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T17:16:46Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4054 · contracts joined: 2400 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2125, 'OK': 141, 'NO_EDGE': 134}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 320, 'game_early_goal': 11, 'first_goal': 393, 'game_winner': 22, 'player_goals': 684, 'game_overtime': 11, 'player_points': 438, 'goalie_saves': 4, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-6h | 0.515 | 0.485 | 0.178 | 6.52 | 3.31 | 3.21 | 219 (25/194) | CONFIRMED/PROJECTED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-6h | 0.513 | 0.487 | 0.179 | 6.06 | 3.06 | 3.00 | 216 (25/191) | PROBABLE/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-6h | 0.749 | 0.251 | 0.140 | 6.33 | 4.00 | 2.33 | 210 (25/185) | PROJECTED/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-6h | 0.564 | 0.436 | 0.184 | 5.95 | 3.17 | 2.78 | 220 (25/195) | PROBABLE/PROJECTED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-6h | 0.447 | 0.553 | 0.178 | 6.05 | 2.86 | 3.19 | 216 (25/191) | CONFIRMED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-6h | 0.629 | 0.371 | 0.175 | 5.99 | 3.39 | 2.61 | 228 (25/203) | CONFIRMED/CONFIRMED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-6h | 0.452 | 0.548 | 0.176 | 6.53 | 3.10 | 3.43 | 222 (25/197) | CONFIRMED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-6h | 0.445 | 0.555 | 0.180 | 6.04 | 2.85 | 3.19 | 202 (25/177) | CONFIRMED/PROJECTED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-6h | 0.598 | 0.402 | 0.173 | 6.40 | 3.52 | 2.89 | 211 (25/186) | CONFIRMED/PROJECTED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-6h | 0.608 | 0.392 | 0.162 | 7.02 | 3.87 | 3.15 | 234 (25/209) | PROJECTED/PROJECTED |
| NSH @ COL | 2026-11-06T02:30:00Z | T-6h | 0.652 | 0.348 | 0.160 | 6.61 | 3.80 | 2.81 | 222 (25/197) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV05STLNJ-NJ | game_winner | 0.564 | 0.665 | 0.646 | 67 | 34 | no | +0.080 | OK |
| KXNHLGAME-26NOV05STLNJ-STL | game_winner | 0.436 | 0.335 | 0.354 | 34 | 67 | yes | +0.080 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.447 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.553 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ2 | game_spread | 0.334 | 0.425 | 0.406 | 43 | 58 | no | +0.069 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.487 | 0.575 | 0.558 | 58 | 43 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ3 | game_spread | 0.207 | 0.285 | 0.268 | 29 | 72 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.404 | 0.490 | 0.473 | 50 | 52 | no | +0.058 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.325 | 0.405 | 0.388 | 41 | 60 | no | +0.058 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.385 | 0.465 | 0.449 | 47 | 54 | no | +0.058 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.513 | 0.435 | 0.450 | 44 | 57 | yes | +0.056 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.201 | 0.275 | 0.259 | 28 | 73 | no | +0.055 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.273 | 0.345 | 0.330 | 35 | 66 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.406 | 0.480 | 0.465 | 49 | 53 | no | +0.047 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.402 | 0.335 | 0.348 | 34 | 67 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.622 | 0.695 | 0.681 | 71 | 32 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.363 | 0.430 | 0.416 | 44 | 58 | no | +0.040 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.251 | 0.195 | 0.205 | 20 | 81 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.217 | 0.275 | 0.263 | 28 | 73 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL2 | game_spread | 0.227 | 0.175 | 0.185 | 18 | 83 | yes | +0.037 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.249 | 0.305 | 0.293 | 31 | 70 | no | +0.037 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.598 | 0.655 | 0.644 | 66 | 35 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.287 | 0.235 | 0.245 | 24 | 77 | yes | +0.035 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.629 | 0.575 | 0.586 | 58 | 43 | yes | +0.032 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.583 | 0.635 | 0.625 | 64 | 37 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.373 | 0.440 | 0.426 | 46 | 58 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV05CARNYI-NYI2 | game_spread | 0.239 | 0.195 | 0.203 | 20 | 81 | yes | +0.028 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.376 | 0.425 | 0.415 | 43 | 58 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.825 | 0.870 | 0.862 | 88 | 14 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI2 | game_spread | 0.183 | 0.225 | 0.216 | 23 | 78 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI3 | team_total | 0.487 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.098 | 0.135 | 0.127 | 14 | 87 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.796 | 0.845 | 0.836 | 86 | 17 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.172 | 0.135 | 0.142 | 14 | 87 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ2 | team_total | 0.818 | 0.865 | 0.856 | 88 | 15 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.591 | 0.635 | 0.626 | 64 | 37 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 | team_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.213 | 0.170 | 0.178 | 18 | 84 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI4 | team_total | 0.273 | 0.320 | 0.310 | 33 | 69 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.582 | 0.635 | 0.625 | 65 | 38 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.778 | 0.820 | 0.812 | 83 | 19 | no | +0.021 | OK |
| KXNHLGAME-26NOV05BOSPIT-BOS | game_winner | 0.548 | 0.505 | 0.514 | 51 | 50 | yes | +0.021 | OK |
| KXNHLGAME-26NOV05BOSPIT-PIT | game_winner | 0.452 | 0.495 | 0.486 | 50 | 51 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.376 | 0.330 | 0.339 | 34 | 68 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.168 | 0.205 | 0.197 | 21 | 80 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5 | team_total | 0.169 | 0.130 | 0.137 | 14 | 88 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.597 | 0.550 | 0.560 | 56 | 46 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG3 | team_total | 0.686 | 0.735 | 0.726 | 75 | 28 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.625 | 0.675 | 0.665 | 69 | 34 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 | team_total | 0.334 | 0.295 | 0.303 | 30 | 71 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.247 | 0.285 | 0.277 | 29 | 72 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL4 | team_total | 0.313 | 0.265 | 0.274 | 28 | 75 | yes | +0.019 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.749 | 0.785 | 0.778 | 79 | 22 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK5 | team_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.278 | 0.315 | 0.307 | 32 | 69 | no | +0.017 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.515 | 0.475 | 0.483 | 48 | 53 | yes | +0.017 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.485 | 0.525 | 0.517 | 53 | 48 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV05PHINYR-NYR2 | game_spread | 0.393 | 0.355 | 0.362 | 36 | 65 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.220 | 0.265 | 0.256 | 28 | 75 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-NYR6 | team_total | 0.122 | 0.095 | 0.100 | 10 | 91 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3 | team_total | 0.553 | 0.515 | 0.523 | 52 | 49 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-BOS3 | team_total | 0.671 | 0.635 | 0.642 | 64 | 37 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.911 | 0.940 | 0.935 | 95 | 7 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.468 | 0.505 | 0.498 | 51 | 50 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-BOS6 | team_total | 0.131 | 0.100 | 0.106 | 11 | 91 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.329 | 0.295 | 0.302 | 30 | 71 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.152 | 0.120 | 0.126 | 13 | 89 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.786 | 0.815 | 0.809 | 82 | 19 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG2 | team_total | 0.859 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 | team_total | 0.390 | 0.435 | 0.426 | 45 | 58 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN3 | game_spread | 0.119 | 0.095 | 0.100 | 10 | 91 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI2 | team_total | 0.725 | 0.765 | 0.757 | 78 | 25 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-BOS4 | team_total | 0.459 | 0.420 | 0.428 | 43 | 59 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.206 | 0.240 | 0.233 | 25 | 77 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4 | team_total | 0.336 | 0.300 | 0.307 | 31 | 71 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET6 | team_total | 0.085 | 0.060 | 0.064 | 7 | 95 | yes | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.515 | 0.523 | 0.178 | 0.217 | 6.52 | 6.53 | 0.943/0.998 | KXNHLSPREAD-26NOV05UTAMTL-UTA2 -0.015 |
| VGK @ DET | 0.513 | 0.451 | 0.179 | 0.215 | 6.06 | 6.28 | 1.020/1.004 | KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 +0.068 |
| CHI @ TBL | 0.749 | 0.718 | 0.140 | 0.189 | 6.33 | 6.39 | 0.958/1.026 | KXNHLTEAMTOTAL-26NOV05CHITB-CHI3 +0.043 |
| STL @ NJD | 0.564 | 0.560 | 0.184 | 0.216 | 5.95 | 6.18 | 0.954/0.993 | KXNHLTOTAL-26NOV05STLNJ-7 +0.046 |
| CAR @ NYI | 0.447 | 0.470 | 0.178 | 0.221 | 6.05 | 6.40 | 0.978/0.990 | KXNHLTOTAL-26NOV05CARNYI-7 +0.061 |
| PHI @ NYR | 0.629 | 0.540 | 0.175 | 0.224 | 5.99 | 5.98 | 0.988/0.991 | KXNHLGAME-26NOV05PHINYR-NYR -0.090 |
| BOS @ PIT | 0.452 | 0.517 | 0.176 | 0.212 | 6.53 | 6.71 | 1.042/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.072 |
| DAL @ CBJ | 0.445 | 0.516 | 0.180 | 0.224 | 6.04 | 6.19 | 1.008/0.987 | KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3 +0.072 |
| VAN @ WPG | 0.598 | 0.542 | 0.173 | 0.221 | 6.40 | 6.34 | 1.004/1.026 | KXNHLGAME-26NOV05VANWPG-VAN +0.056 |
| ANA @ EDM | 0.608 | 0.581 | 0.162 | 0.200 | 7.02 | 7.28 | 1.010/1.016 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4 +0.047 |
| NSH @ COL | 0.652 | 0.661 | 0.160 | 0.204 | 6.61 | 6.65 | 0.977/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.021 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 39 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Caufield: 1+ assists YES @ 33c · p 0.4125 (adj 0.3688) · $4.08 · thesis MTL:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 67c · p 0.7206 (adj 0.7067) · $8.45 · thesis UTA:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 18c · p 0.22 (adj 0.2075) · $2.44 · thesis UTA:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0773 (adj 0.0667) · $1.39 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ assists YES @ 29c · p 0.3555 (adj 0.3153) · $1.47 · thesis VGK:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.2442 (adj 0.2281) · $3.39 · thesis CHI:OFFENSE_4PLUS
- Nikita Kucherov: 2+ assists NO @ 71c · p 0.7942 (adj 0.7471) · $9.03 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 1.5 goals NO @ 41c · p 0.5 (adj 0.45) · $2.44 · thesis GAME:TIGHT
- Victor Hedman: 1+ goals NO @ 90c · p 0.9259 (adj 0.9169) · $9.04 · thesis DIFFUSE
- Robert Thomas: 1+ goals YES @ 21c · p 0.267 (adj 0.2503) · $3.8 · thesis STL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 60c · p 0.6606 (adj 0.6442) · $7.7 · thesis NJD:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 58c · p 0.6729 (adj 0.624) · $4.98 · thesis STL:WINS
- Connor McMichael: 1+ goals YES @ 16c · p 0.1928 (adj 0.1821) · $1.51 · thesis STL:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7828 (adj 0.7684) · $9.56 · thesis CAR:SUPPRESSED
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1697 (adj 0.1573) · $2.5 · thesis NYI:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 12c · p 0.1581 (adj 0.1436) · $2.08 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2562 (adj 0.2384) · $2.51 · thesis NYI:OFFENSE_4PLUS
- Cole Knuble: 1+ goals YES @ 12c · p 0.1501 (adj 0.1413) · $1.74 · thesis PHI:OFFENSE_4PLUS
- Tye Kartye: 1+ assists YES @ 24c · p 0.306 (adj 0.268) · $2.24 · thesis NYR:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 68c · p 0.7434 (adj 0.7092) · $6.65 · thesis PHI:SUPPRESSED
- Travis Sanheim: 1+ assists YES @ 25c · p 0.3058 (adj 0.2754) · $1.74 · thesis PHI:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.1845 (adj 0.1684) · $3.75 · thesis PIT:WINS_BY_2PLUS
- Rickard Rakell: 1+ goals YES @ 33c · p 0.3899 (adj 0.3712) · $4.43 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 11c · p 0.1494 (adj 0.1321) · $1.71 · thesis PIT:WINS_BY_2PLUS
- Nick Robertson: 1+ goals YES @ 16c · p 0.1912 (adj 0.1809) · $1.49 · thesis PIT:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 22c · p 0.2876 (adj 0.2682) · $5.34 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.215 (adj 0.2) · $2.71 · thesis CBJ:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 16c · p 0.2022 (adj 0.1879) · $2.54 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.107 (adj 0.0953) · $1.21 · thesis CBJ:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2284 (adj 0.2088) · $4.98 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1553 (adj 0.1415) · $2.96 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.2114 (adj 0.1973) · $3.66 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 14c · p 0.1851 (adj 0.1701) · $2.74 · thesis VAN:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 8c · p 0.1266 (adj 0.1137) · $3.33 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 5c · p 0.0845 (adj 0.0709) · $1.79 · thesis ANA:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1292 (adj 0.1157) · $2.38 · thesis EDM:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.2019 (adj 0.1902) · $2.83 · thesis ANA:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 71c · p 0.7923 (adj 0.7461) · $9.56 · thesis NSH:SUPPRESSED
- Nathan MacKinnon: 1+ assists NO @ 39c · p 0.4689 (adj 0.4269) · $3.9 · thesis COL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.98, exp saves 25.11 (sd 6.89), pull risk 0.063
- UTA net: Sebastian Cossa (PROJECTED) exp shots 25.81, exp saves 22.18 (sd 6.26), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.420 | 0.315 | 35/72 | +0.054 | STANDARD |
| Cole Caufield: 1+ assists | 0.412 | 0.325 | 33/68 | +0.067 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.499 | 0.585 | 60/43 | +0.054 | STANDARD |
| Logan Cooley: 1+ points | 0.514 | 0.600 | 61/41 | +0.059 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.250 | 0.330 | 35/69 | +0.045 | STANDARD |
| Clayton Keller: 1+ points | 0.584 | 0.655 | 66/35 | +0.050 | STANDARD |

**VGK @ DET** · priced 157/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROBABLE) exp shots 26.45, exp saves 22.67 (sd 6.43), pull risk 0.073
- VGK net: Carter Hart (PROJECTED) exp shots 27.41, exp saves 23.73 (sd 6.45), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.425 | 0.515 | 53/50 | +0.057 | STANDARD |
| Jack Eichel: 1+ assists | 0.444 | 0.525 | 54/49 | +0.049 | STANDARD |
| Ivan Barbashev: 1+ assists | 0.355 | 0.275 | 29/74 | +0.051 | STANDARD |
| Rasmus Andersson: 1+ points | 0.365 | 0.285 | 31/74 | +0.040 | STANDARD |
| Ivan Barbashev: 1+ points | 0.500 | 0.425 | 43/58 | +0.053 | STANDARD |
| Mitch Marner: 1+ points | 0.558 | 0.630 | 65/39 | +0.035 | STANDARD |

**CHI @ TBL** · priced 148/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.1, exp saves 20.67 (sd 5.73), pull risk 0.041
- CHI net: Arvid Soderblom (PROJECTED) exp shots 30.41, exp saves 25.28 (sd 7.26), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 2+ points | 0.395 | 0.495 | 50/51 | +0.078 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.206 | 0.300 | 31/71 | +0.070 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.583 | 0.665 | 67/34 | +0.062 | STANDARD |
| Nikita Kucherov: 3+ points | 0.155 | 0.225 | 23/78 | +0.053 | STANDARD |
| Tyler Bertuzzi: 1+ goals | 0.244 | 0.180 | 19/83 | +0.043 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.446 | 0.385 | 39/62 | +0.040 | STANDARD |

**STL @ NJD** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROBABLE) exp shots 24.87, exp saves 21.56 (sd 6.03), pull risk 0.053
- STL net: Joel Hofer (PROJECTED) exp shots 30.21, exp saves 25.94 (sd 7.16), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.241 | 0.360 | 37/65 | +0.093 | STANDARD |
| Jack Hughes: 1+ assists | 0.405 | 0.520 | 54/50 | +0.077 | STANDARD |
| Luke Evangelista: 1+ assists | 0.249 | 0.350 | 37/67 | +0.066 | STANDARD |
| Dylan Holloway: 1+ points | 0.532 | 0.445 | 46/57 | +0.054 | STANDARD |
| Luke Evangelista: 1+ points | 0.401 | 0.485 | 51/54 | +0.042 | STANDARD |
| Dylan Holloway: 1+ assists | 0.363 | 0.285 | 29/72 | +0.058 | STANDARD |

**CAR @ NYI** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 29.43, exp saves 25.26 (sd 6.94), pull risk 0.067
- CAR net: Brandon Bussi (PROJECTED) exp shots 24.49, exp saves 21.24 (sd 6.06), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.329 | 0.430 | 45/59 | +0.065 | STANDARD |
| Sebastian Aho: 1+ points | 0.506 | 0.605 | 63/42 | +0.057 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.309 | 0.395 | 41/62 | +0.055 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.494 | 0.580 | 60/44 | +0.049 | STANDARD |
| Tony DeAngelo: 1+ points | 0.381 | 0.300 | 33/73 | +0.036 | STANDARD |
| Simon Holmstrom: 1+ points | 0.515 | 0.435 | 44/57 | +0.057 | STANDARD |

**PHI @ NYR** · priced 176/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 25.8, exp saves 22.51 (sd 6.14), pull risk 0.049
- PHI net: Joseph Woll (CONFIRMED) exp shots 26.19, exp saves 22.68 (sd 6.17), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tye Kartye: 1+ assists | 0.306 | 0.230 | 24/78 | +0.053 | STANDARD |
| Travis Konecny: 1+ points | 0.420 | 0.495 | 51/52 | +0.043 | STANDARD |
| Dylan Garand: 22+ saves | 0.562 | 0.490 | 51/53 | +0.034 |  |
| Travis Sanheim: 1+ points | 0.374 | 0.305 | 32/71 | +0.039 | STANDARD |
| Travis Konecny: 1+ assists | 0.257 | 0.325 | 33/68 | +0.048 | STANDARD |
| Tye Kartye: 1+ points | 0.442 | 0.375 | 39/64 | +0.035 | STANDARD |

**BOS @ PIT** · priced 163/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.87, exp saves 22.23 (sd 6.32), pull risk 0.069
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.04 (sd 6.84), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rickard Rakell: 1+ goals | 0.390 | 0.315 | 33/70 | +0.044 | STANDARD |
| Blake Lizotte: 1+ goals | 0.149 | 0.080 | 11/95 | +0.033 | STANDARD |
| David Pastrnak: 1+ assists | 0.466 | 0.535 | 55/48 | +0.036 | STANDARD |
| JJ Peterka: 1+ assists | 0.273 | 0.340 | 36/68 | +0.032 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.405 | 0.470 | 48/54 | +0.038 | STANDARD |
| Connor Dewar: 1+ goals | 0.184 | 0.120 | 13/89 | +0.047 | STANDARD |

**DAL @ CBJ** · priced 147/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 25.44, exp saves 22.1 (sd 6.11), pull risk 0.055
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.62, exp saves 22.13 (sd 6.25), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.288 | 0.210 | 22/80 | +0.056 | STANDARD |
| Charlie Coyle: 2+ points | 0.212 | 0.140 | 17/89 | +0.032 | STANDARD |
| Charlie Coyle: 1+ points | 0.561 | 0.495 | 52/53 | +0.024 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.215 | 0.155 | 17/86 | +0.035 | STANDARD |
| Cole Sillinger: 1+ goals | 0.173 | 0.115 | 14/91 | +0.025 | STANDARD |
| Sean Monahan: 1+ goals | 0.202 | 0.145 | 16/87 | +0.033 | STANDARD |

**VAN @ WPG** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 24.76, exp saves 21.5 (sd 6.07), pull risk 0.058
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.31, exp saves 25.1 (sd 6.85), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 1+ goals | 0.239 | 0.140 | 24/96 | -0.014 | STANDARD |
| Linus Karlsson: 1+ goals | 0.228 | 0.150 | 16/86 | +0.059 | STANDARD |
| Cole Perfetti: 1+ assists | 0.432 | 0.360 | 38/66 | +0.035 | STANDARD |
| Elias Pettersson (#25): 1+ goals | 0.063 | 0.130 | 25/99 | -0.053 | STANDARD |
| Neal Pionk: 1+ points | 0.469 | 0.535 | 55/48 | +0.034 | STANDARD |
| Kyle Connor: 1+ assists | 0.444 | 0.505 | 52/51 | +0.029 | STANDARD |

**ANA @ EDM** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.9, exp saves 24.11 (sd 6.81), pull risk 0.079
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.83, exp saves 23.49 (sd 6.9), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.383 | 0.530 | 55/49 | +0.109 | STANDARD |
| Leon Draisaitl: 3+ points | 0.150 | 0.275 | 29/74 | +0.097 | STANDARD |
| Connor McDavid: 2+ assists | 0.239 | 0.345 | 36/67 | +0.076 | STANDARD |
| Connor McDavid: 2+ points | 0.465 | 0.570 | 59/45 | +0.068 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.510 | 0.615 | 62/39 | +0.083 | STANDARD |
| Connor McDavid: 1+ assists | 0.603 | 0.705 | 71/30 | +0.083 | STANDARD |

**NSH @ COL** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.73, exp saves 22.66 (sd 6.18), pull risk 0.047
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.24 (sd 7.61), pull risk 0.096

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.208 | 0.300 | 31/71 | +0.068 | STANDARD |
| Mavrik Bourque: 1+ points | 0.352 | 0.440 | 45/57 | +0.061 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.531 | 0.615 | 62/39 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.383 | 0.460 | 47/55 | +0.050 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.240 | 26/78 | +0.035 | STANDARD |
| Cale Makar: 1+ points | 0.603 | 0.670 | 68/34 | +0.041 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
