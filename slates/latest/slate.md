# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-14T00:14:51Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 7 · markets on board: 5523 · contracts joined: 1747 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 1572, 'OK': 86, 'NO_EDGE': 89}
families: {'period_winner': 63, 'period_spread': 42, 'period_total': 63, 'player_assists': 290, 'game_early_goal': 7, 'first_goal': 256, 'game_winner': 14, 'player_goals': 434, 'game_overtime': 7, 'player_points': 396, 'goalie_saves': 14, 'game_spread': 28, 'team_total': 70, 'game_total': 63}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ WPG | 2026-10-14T00:15:00Z | T-<10m | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 242 (25/217) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-10m | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 238 (25/213) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-30m | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 246 (25/221) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-30m | 0.674 | 0.326 | 0.152 | 6.79 | 3.98 | 2.81 | 242 (25/217) | PROBABLE/CONFIRMED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-90m | 0.645 | 0.355 | 0.171 | 6.36 | 3.64 | 2.72 | 257 (25/232) | CONFIRMED/PROBABLE |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-90m | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 245 (25/220) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-90m | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.533 | 0.445 | 0.463 | 45 | 56 | yes | +0.066 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.326 | 0.405 | 0.389 | 41 | 60 | no | +0.057 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.674 | 0.595 | 0.611 | 60 | 41 | yes | +0.057 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.461 | 0.385 | 0.400 | 39 | 62 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.371 | 0.300 | 0.314 | 31 | 71 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.165 | 0.225 | 0.212 | 23 | 78 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.585 | 0.598 | 59 | 42 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.577 | 0.515 | 0.527 | 52 | 49 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA6 | team_total | 0.208 | 0.145 | 0.156 | 16 | 87 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 | team_total | 0.539 | 0.595 | 0.584 | 60 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.766 | 0.715 | 0.726 | 72 | 29 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-8 | game_total | 0.304 | 0.255 | 0.264 | 26 | 75 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.127 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 | team_total | 0.324 | 0.375 | 0.364 | 38 | 63 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.199 | 0.155 | 0.163 | 16 | 85 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT13MINWPG-MIN2 | game_spread | 0.247 | 0.295 | 0.285 | 30 | 71 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR4 | team_total | 0.316 | 0.370 | 0.359 | 38 | 64 | no | +0.028 | OK |
| KXNHLGAME-26OCT13MINWPG-MIN | game_winner | 0.456 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLGAME-26OCT13MINWPG-WPG | game_winner | 0.544 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.359 | 0.315 | 0.324 | 32 | 69 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR3 | team_total | 0.531 | 0.580 | 0.570 | 59 | 43 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT13TORUTA-8 | game_total | 0.346 | 0.305 | 0.313 | 31 | 70 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ2 | team_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.021 | OK |
| KXNHLGAME-26OCT13BOSSJ-BOS | game_winner | 0.587 | 0.545 | 0.554 | 55 | 46 | yes | +0.020 | OK |
| KXNHLGAME-26OCT13BOSSJ-SJ | game_winner | 0.413 | 0.455 | 0.446 | 46 | 55 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT13MINWPG-5 | game_total | 0.759 | 0.795 | 0.788 | 80 | 21 | no | +0.020 | OK |
| KXNHLGAME-26OCT13CGYANA-ANA | game_winner | 0.645 | 0.605 | 0.613 | 61 | 40 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT13TORUTA-10 | game_total | 0.135 | 0.105 | 0.111 | 11 | 90 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13COLDAL-DAL4 | team_total | 0.355 | 0.395 | 0.387 | 40 | 61 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR2 | team_total | 0.761 | 0.795 | 0.788 | 80 | 21 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA2 | team_total | 0.905 | 0.870 | 0.878 | 88 | 14 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13COLDAL-DAL5 | team_total | 0.181 | 0.215 | 0.208 | 22 | 79 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN2 | team_total | 0.782 | 0.815 | 0.809 | 82 | 19 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH2 | team_total | 0.838 | 0.800 | 0.808 | 81 | 21 | yes | +0.017 | OK |
| KXNHLSPREAD-26OCT13CGYANA-CGY2 | game_spread | 0.172 | 0.205 | 0.198 | 21 | 80 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-9 | game_total | 0.217 | 0.180 | 0.187 | 19 | 83 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT13MINWPG-MIN3 | game_spread | 0.144 | 0.180 | 0.172 | 19 | 83 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT13EDMLA-LA3 | game_spread | 0.135 | 0.165 | 0.159 | 17 | 84 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ5 | team_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN3 | team_total | 0.561 | 0.595 | 0.588 | 60 | 41 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN5 | team_total | 0.177 | 0.215 | 0.207 | 23 | 80 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT13COLDAL-DAL3 | team_total | 0.572 | 0.605 | 0.598 | 61 | 40 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT13CGYANA-10 | game_total | 0.097 | 0.075 | 0.079 | 8 | 93 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT13CGYANA-CGY3 | game_spread | 0.092 | 0.115 | 0.110 | 12 | 89 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT13CGYANA-9 | game_total | 0.201 | 0.175 | 0.180 | 18 | 83 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-6 | game_total | 0.608 | 0.575 | 0.582 | 58 | 43 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT13COLDAL-4 | game_total | 0.831 | 0.855 | 0.850 | 86 | 15 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT13TORUTA-9 | game_total | 0.253 | 0.220 | 0.226 | 23 | 79 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-10 | game_total | 0.106 | 0.080 | 0.085 | 9 | 93 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS3 | game_spread | 0.231 | 0.205 | 0.210 | 21 | 80 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-5 | game_total | 0.769 | 0.795 | 0.790 | 80 | 21 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-4 | game_total | 0.853 | 0.875 | 0.871 | 88 | 13 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-7 | game_total | 0.497 | 0.465 | 0.471 | 47 | 54 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-VGK4 | team_total | 0.394 | 0.430 | 0.423 | 44 | 58 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT13COLDAL-5 | game_total | 0.738 | 0.765 | 0.760 | 77 | 24 | no | +0.009 | OK |
| KXNHLGAME-26OCT13CGYANA-CGY | game_winner | 0.355 | 0.385 | 0.379 | 39 | 62 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA5 | team_total | 0.303 | 0.275 | 0.280 | 28 | 73 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT13MINWPG-6 | game_total | 0.545 | 0.575 | 0.569 | 58 | 43 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT13CGYANA-8 | game_total | 0.281 | 0.255 | 0.260 | 26 | 75 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT13COLDAL-DAL3 | game_spread | 0.163 | 0.185 | 0.180 | 19 | 82 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-VGK2 | team_total | 0.813 | 0.840 | 0.835 | 85 | 17 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR5 | team_total | 0.163 | 0.195 | 0.188 | 21 | 82 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-7 | game_total | 0.446 | 0.475 | 0.469 | 48 | 53 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS3 | team_total | 0.662 | 0.635 | 0.640 | 64 | 37 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT13MINWPG-4 | game_total | 0.846 | 0.865 | 0.861 | 87 | 14 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA6 | team_total | 0.154 | 0.130 | 0.135 | 14 | 88 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT13MINWPG-WPG2 | game_spread | 0.319 | 0.295 | 0.300 | 30 | 71 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT13COLDAL-7 | game_total | 0.398 | 0.425 | 0.420 | 43 | 58 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS6 | team_total | 0.121 | 0.100 | 0.104 | 11 | 91 | yes | +0.004 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.496 | 0.474 | 0.178 | 0.221 | 5.91 | 6.20 | 0.994/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.059 |
| VGK @ NSH | 0.533 | 0.507 | 0.171 | 0.217 | 6.49 | 6.20 | 1.002/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.054 |
| TOR @ UTA | 0.674 | 0.597 | 0.152 | 0.209 | 6.79 | 6.40 | 0.991/0.956 | KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 -0.092 |
| CGY @ ANA | 0.645 | 0.631 | 0.171 | 0.210 | 6.36 | 6.41 | 1.016/1.002 | KXNHLTEAMTOTAL-26OCT13CGYANA-CGY2 +0.018 |
| EDM @ LAK | 0.440 | 0.480 | 0.173 | 0.218 | 6.27 | 6.25 | 0.995/0.994 | KXNHLSPREAD-26OCT13EDMLA-EDM2 -0.043 |
| BOS @ SJS | 0.413 | 0.507 | 0.175 | 0.216 | 6.17 | 6.40 | 1.039/0.956 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 +0.094 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1353 (adj 0.1252) · $3.42 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 21c · p 0.3052 (adj 0.2401) · $3.74 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ assists NO @ 53c · p 0.6116 (adj 0.5683) · $8.88 · thesis MIN:SUPPRESSED
- Morgan Barron: 1+ goals YES @ 11c · p 0.1379 (adj 0.1297) · $2.34 · thesis WPG:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 8c · p 0.1355 (adj 0.1204) · $5.73 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 2+ goals YES @ 2c · p 0.0364 (adj 0.0323) · $1.27 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 20c · p 0.256 (adj 0.2408) · $4.62 · thesis COL:OFFENSE_4PLUS
- Gabriel Landeskog: 1+ goals YES @ 19c · p 0.2351 (adj 0.2226) · $4.42 · thesis COL:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 4c · p 0.0651 (adj 0.0551) · $1.81 · thesis NSH:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 71c · p 0.7616 (adj 0.7475) · $13.88 · thesis VGK:SUPPRESSED
- Brady Skjei: 1+ assists YES @ 23c · p 0.308 (adj 0.2615) · $3.87 · thesis NSH:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0695 (adj 0.0634) · $1.66 · thesis VGK:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 8c · p 0.1093 (adj 0.1007) · $2.62 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ assists YES @ 24c · p 0.3101 (adj 0.2701) · $3.65 · thesis TOR:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6552) · $9.03 · thesis UTA:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 64c · p 0.6829 (adj 0.6709) · $8.34 · thesis TOR:SUPPRESSED
- Tim Washe: 1+ goals YES @ 9c · p 0.149 (adj 0.133) · $6.23 · thesis ANA:OFFENSE_4PLUS
- A.J. Greer: 2+ goals YES @ 2c · p 0.0442 (adj 0.0382) · $2.33 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1395 (adj 0.1284) · $4.0 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 7c · p 0.0996 (adj 0.091) · $2.67 · thesis ANA:OFFENSE_4PLUS
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9098 (adj 0.8624) · $13.88 · thesis LAK:SUPPRESSED
- Mattias Ekholm: 1+ assists YES @ 28c · p 0.3533 (adj 0.3116) · $4.55 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ goals NO @ 57c · p 0.6135 (adj 0.6014) · $6.95 · thesis EDM:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 25c · p 0.2859 (adj 0.2757) · $3.08 · thesis LAK:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $4.84 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 55c · p 0.7032 (adj 0.6004) · $13.88 · thesis BOS:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.148 (adj 0.1372) · $3.83 · thesis BOS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2154 (adj 0.2028) · $4.47 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ WPG** · priced 188/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Samberg: 1+ points | 0.329 | 0.140 | 26/98 | +0.056 | STANDARD |
| Alex Iafallo: 1+ assists | 0.287 | 0.105 | 19/98 | +0.086 | STANDARD |
| Dylan Samberg: 1+ assists | 0.283 | 0.130 | 24/98 | +0.030 | STANDARD |
| Dylan DeMelo: 1+ assists | 0.262 | 0.110 | 20/98 | +0.050 | STANDARD |
| Alex Iafallo: 1+ points | 0.419 | 0.285 | 30/73 | +0.105 | STANDARD |
| Jared Spurgeon: 1+ assists | 0.319 | 0.185 | 29/92 | +0.015 | STANDARD |

**COL @ DAL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brent Burns: 1+ assists | 0.269 | 0.125 | 23/98 | +0.026 | STANDARD |
| Roope Hintz: 1+ assists | 0.286 | 0.395 | 40/61 | +0.088 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.286 | 0.385 | 39/62 | +0.077 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.409 | 0.505 | 52/51 | +0.063 | STANDARD |
| Mikko Rantanen: 1+ points | 0.568 | 0.655 | 66/35 | +0.066 | STANDARD |
| Miro Heiskanen: 1+ points | 0.450 | 0.535 | 54/47 | +0.063 | STANDARD |

**VGK @ NSH** · priced 194/195 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Hanifin: 1+ assists | 0.260 | 0.100 | 18/98 | +0.070 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 2+ points | 0.216 | 0.340 | 35/67 | +0.099 | STANDARD |
| Nicolas Hague: 1+ assists | 0.193 | 0.075 | 12/97 | +0.066 | STANDARD |
| Brayden McNabb: 1+ assists | 0.243 | 0.125 | 23/98 | +0.000 | STANDARD |
| Jack Eichel: 1+ points | 0.583 | 0.695 | 70/31 | +0.092 | STANDARD |

**TOR @ UTA** · priced 190/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 25.03, exp saves 21.92 (sd 6.07), pull risk 0.052
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.85, exp saves 26.98 (sd 7.41), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Barrett Hayton: 1+ assists | 0.258 | 0.130 | 24/98 | +0.005 | STANDARD |
| Anthony Stolarz: 29+ saves | 0.416 | 0.295 | 53/94 | -0.131 |  |
| Jake McCabe: 1+ assists | 0.226 | 0.110 | 20/98 | +0.015 | STANDARD |
| Darren Raddysh: 1+ assists | 0.319 | 0.425 | 43/58 | +0.084 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.510 | 52/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.212 | 0.310 | 32/70 | +0.074 | STANDARD |

**CGY @ ANA** · priced 198/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 26.29, exp saves 23.15 (sd 6.3), pull risk 0.047
- CGY net: Dustin Wolf (PROBABLE) exp shots 31.79, exp saves 26.75 (sd 7.4), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ assists | 0.294 | 0.100 | 18/98 | +0.104 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.237 | 0.075 | 12/97 | +0.110 | STANDARD |
| Noah Warren: 1+ points | 0.341 | 0.190 | 20/82 | +0.130 | PRIOR_HEAVY |
| Zach Whitecloud: 1+ assists | 0.223 | 0.080 | 13/97 | +0.085 | STANDARD |
| Tim Washe: 1+ assists | 0.256 | 0.115 | 21/98 | +0.034 | STANDARD |
| Adam Klapka: 1+ points | 0.298 | 0.160 | 23/91 | +0.056 | STANDARD |

**EDM @ LAK** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 28.16, exp saves 24.3 (sd 6.72), pull risk 0.065
- EDM net: Devon Levi (CONFIRMED) exp shots 27.62, exp saves 23.94 (sd 6.59), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ assists | 0.244 | 0.070 | 12/98 | +0.116 | STANDARD |
| Joel Edmundson: 1+ points | 0.297 | 0.135 | 15/88 | +0.138 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.435 | 0.595 | 60/41 | +0.138 | STANDARD |
| Connor McDavid: 1+ assists | 0.481 | 0.625 | 63/38 | +0.122 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.215 | 0.075 | 13/98 | +0.077 | STANDARD |
| Connor McDavid: 2+ points | 0.337 | 0.475 | 48/53 | +0.115 | STANDARD |

**BOS @ SJS** · priced 219/226 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.44), pull risk 0.069
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.58, exp saves 23.85 (sd 6.47), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.396 | 0.555 | 56/45 | +0.137 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.297 | 0.455 | 46/55 | +0.136 | STANDARD |
| Jeremy Swayman: 25+ saves | 0.455 | 0.300 | 54/94 | -0.102 |  |
| Nikita Zadorov: 1+ assists | 0.230 | 0.095 | 17/98 | +0.050 | STANDARD |
| Sam Dickinson: 1+ assists | 0.215 | 0.080 | 14/98 | +0.066 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.550 | 56/46 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
