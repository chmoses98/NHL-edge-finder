# NHL slate 2026-10-01 — RESEARCH_ONLY

generated 2026-10-02T01:27:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 8 · simulated (not started): 3 · markets on board: 3700 · contracts joined: 514 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 439, 'NO_EDGE': 31, 'OK': 44}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 78, 'game_early_goal': 3, 'first_goal': 92, 'game_winner': 6, 'player_goals': 92, 'game_overtime': 3, 'player_points': 96, 'goalie_saves': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ UTA | 2026-10-02T01:30:00Z | T-<10m | 0.659 | 0.341 | 0.160 | 6.32 | 3.67 | 2.65 | 162 (25/137) | PROBABLE/CONFIRMED |
| EDM @ VAN | 2026-10-02T02:00:00Z | T-30m | 0.412 | 0.588 | 0.168 | 6.71 | 3.07 | 3.63 | 166 (25/141) | PROBABLE/CONFIRMED |
| FLA @ SJS | 2026-10-02T02:00:00Z | T-30m | 0.514 | 0.486 | 0.170 | 6.62 | 3.36 | 3.25 | 186 (25/161) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT01FLASJ-FLA | game_winner | 0.486 | 0.575 | 0.557 | 58 | 43 | no | +0.067 | OK |
| KXNHLGAME-26OCT01FLASJ-SJ | game_winner | 0.514 | 0.425 | 0.443 | 43 | 58 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3 | game_spread | 0.241 | 0.325 | 0.307 | 33 | 68 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-EDM2 | game_spread | 0.369 | 0.455 | 0.437 | 46 | 55 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA3 | game_spread | 0.164 | 0.245 | 0.227 | 25 | 76 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT01FLASJ-FLA2 | game_spread | 0.278 | 0.355 | 0.339 | 36 | 65 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ4 | team_total | 0.441 | 0.365 | 0.380 | 37 | 64 | yes | +0.055 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ2 | game_spread | 0.305 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3 | team_total | 0.656 | 0.585 | 0.600 | 59 | 42 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 | team_total | 0.505 | 0.575 | 0.561 | 58 | 43 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN3 | team_total | 0.595 | 0.525 | 0.539 | 53 | 48 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-EDM | game_winner | 0.588 | 0.655 | 0.642 | 66 | 35 | no | +0.047 | OK |
| KXNHLGAME-26OCT01EDMVAN-VAN | game_winner | 0.412 | 0.345 | 0.358 | 35 | 66 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN4 | team_total | 0.382 | 0.315 | 0.328 | 32 | 69 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN5 | team_total | 0.203 | 0.155 | 0.164 | 16 | 85 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN2 | game_spread | 0.223 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ6 | team_total | 0.128 | 0.080 | 0.088 | 9 | 93 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 | team_total | 0.422 | 0.475 | 0.464 | 48 | 53 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-SJ2 | team_total | 0.839 | 0.790 | 0.801 | 80 | 22 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5 | team_total | 0.308 | 0.355 | 0.345 | 36 | 65 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM3 | team_total | 0.711 | 0.760 | 0.751 | 77 | 25 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT01FLASJ-10 | game_total | 0.122 | 0.085 | 0.091 | 9 | 92 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT01FLASJ-8 | game_total | 0.319 | 0.275 | 0.283 | 28 | 73 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT01FLASJ-SJ3 | game_spread | 0.192 | 0.150 | 0.158 | 16 | 86 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT01FLASJ-9 | game_total | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA3 | team_total | 0.634 | 0.680 | 0.671 | 69 | 33 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN2 | team_total | 0.802 | 0.760 | 0.769 | 77 | 25 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT01EDMVAN-VAN3 | game_spread | 0.126 | 0.095 | 0.101 | 10 | 91 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM2 | team_total | 0.875 | 0.905 | 0.899 | 91 | 10 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-VAN6 | team_total | 0.091 | 0.060 | 0.065 | 7 | 95 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA5 | team_total | 0.232 | 0.270 | 0.262 | 28 | 74 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM6 | team_total | 0.157 | 0.185 | 0.179 | 19 | 82 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-9 | game_total | 0.242 | 0.215 | 0.220 | 22 | 79 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA2 | team_total | 0.831 | 0.860 | 0.855 | 87 | 15 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA3 | game_spread | 0.289 | 0.315 | 0.310 | 32 | 69 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-8 | game_total | 0.278 | 0.255 | 0.260 | 26 | 75 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-9 | game_total | 0.195 | 0.175 | 0.179 | 18 | 83 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT01FLASJ-FLA6 | team_total | 0.109 | 0.125 | 0.122 | 13 | 88 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-3 | game_total | 0.976 | 0.985 | 0.984 | 99 | 2 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 | team_total | 0.510 | 0.535 | 0.530 | 54 | 47 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT01CHIUTA-3 | game_total | 0.966 | 0.975 | 0.973 | 98 | 3 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA5 | team_total | 0.313 | 0.340 | 0.334 | 35 | 67 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT01CHIUTA-UTA2 | game_spread | 0.432 | 0.455 | 0.450 | 46 | 55 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT01EDMVAN-4 | game_total | 0.894 | 0.905 | 0.903 | 91 | 10 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-10 | game_total | 0.095 | 0.085 | 0.087 | 9 | 92 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-2 | game_total | 0.990 | 0.990 | 0.990 |  | 1 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI3 | team_total | 0.495 | 0.475 | 0.479 | 48 | 53 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA3 | team_total | 0.719 | 0.740 | 0.736 | 75 | 27 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-10 | game_total | 0.124 | 0.115 | 0.117 | 12 | 89 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-8 | game_total | 0.332 | 0.315 | 0.318 | 32 | 69 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26OCT01CHIUTA-CHI | game_winner | 0.341 | 0.325 | 0.328 | 33 | 68 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT01CHIUTA-UTA | game_winner | 0.659 | 0.675 | 0.672 | 68 | 33 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-3 | game_total | 0.976 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-5 | game_total | 0.826 | 0.835 | 0.833 | 84 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI4 | team_total | 0.288 | 0.275 | 0.278 | 28 | 73 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT01CHIUTA-CHI3 | game_spread | 0.089 | 0.085 | 0.086 | 9 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA2 | team_total | 0.881 | 0.885 | 0.884 | 89 | 12 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI6 | team_total | 0.055 | 0.050 | 0.051 | 6 | 96 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-6 | game_total | 0.582 | 0.595 | 0.592 | 60 | 41 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-4 | game_total | 0.864 | 0.865 | 0.865 | 87 | 14 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI5 | team_total | 0.136 | 0.130 | 0.131 | 14 | 88 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-4 | game_total | 0.886 | 0.890 | 0.889 | 90 | 12 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-6 | game_total | 0.642 | 0.635 | 0.636 | 64 | 37 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-6 | game_total | 0.622 | 0.615 | 0.616 | 62 | 39 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-5 | game_total | 0.814 | 0.815 | 0.815 | 82 | 19 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT01CHIUTA-CHI2 | game_spread | 0.165 | 0.160 | 0.161 | 17 | 85 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-5 | game_total | 0.783 | 0.785 | 0.785 | 79 | 22 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT01FLASJ-7 | game_total | 0.512 | 0.505 | 0.506 | 51 | 50 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT01CHIUTA-7 | game_total | 0.470 | 0.475 | 0.474 | 48 | 53 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT01EDMVAN-7 | game_total | 0.532 | 0.535 | 0.534 | 54 | 47 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-CHI2 | team_total | 0.731 | 0.730 | 0.730 | 74 | 28 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA6 | team_total | 0.164 | 0.165 | 0.165 | 19 | 86 |  | -0.032 | NO_EDGE |
| KXNHL1P-26OCT01CHIUTA-CHI | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT01CHIUTA-TIE | period_winner |  | 0.325 |  | 35 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT01CHIUTA-UTA | period_winner |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT01CHIUTA-CHI2 | period_spread |  | 0.065 |  | 9 | 96 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT01CHIUTA-UTA2 | period_spread |  | 0.160 |  | 19 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ UTA | 0.659 | 0.671 | 0.160 | 0.194 | 6.32 | 6.59 | 0.990/1.041 | KXNHLTEAMTOTAL-26OCT01CHIUTA-UTA4 +0.048 |
| EDM @ VAN | 0.412 | 0.446 | 0.168 | 0.214 | 6.71 | 6.52 | 1.026/0.994 | KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM4 -0.040 |
| FLA @ SJS | 0.514 | 0.549 | 0.170 | 0.216 | 6.62 | 6.41 | 1.039/0.991 | KXNHLTEAMTOTAL-26OCT01FLASJ-FLA4 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 12c · p 0.1671 (adj 0.1541) · $7.01 · thesis CHI:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 22c · p 0.265 (adj 0.2513) · $6.56 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 66c · p 0.7744 (adj 0.6935) · $18.55 · thesis UTA:SUPPRESSED
- Anders Lee: 1+ goals YES @ 24c · p 0.2779 (adj 0.2672) · $5.44 · thesis UTA:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 31c · p 0.4762 (adj 0.3649) · $8.55 · thesis EDM:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 16c · p 0.2153 (adj 0.2002) · $8.07 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 67c · p 0.8312 (adj 0.7167) · $19.64 · thesis EDM:SUPPRESSED
- Edmonton wins by over 2.5 goals NO @ 68c · p 0.7726 (adj 0.7238) · $13.74 · thesis VAN:WINS
- Kiefer Sherwood: 1+ goals YES @ 15c · p 0.2154 (adj 0.1978) · $10.14 · thesis SJS:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 76c · p 0.852 (adj 0.8035) · $19.93 · thesis SJS:WINS
- Sam Reinhart: 1+ goals NO @ 67c · p 0.7369 (adj 0.7189) · $19.93 · thesis FLA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ UTA** · priced 111/111 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 24.86, exp saves 21.87 (sd 6.08), pull risk 0.048
- CHI net: Arvid Soderblom (CONFIRMED) exp shots 29.49, exp saves 24.79 (sd 7.05), pull risk 0.094

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.262 | 0.395 | 41/62 | +0.102 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.226 | 0.350 | 36/66 | +0.099 | STANDARD |
| Frank Nazar: 1+ points | 0.465 | 0.360 | 38/66 | +0.069 | STANDARD |
| Patrick Kane: 2+ points | 0.116 | 0.220 | 22/ | -0.117 | STANDARD |
| Nick Schmaltz: 2+ points | 0.257 | 0.155 | 24/93 | +0.004 | STANDARD |
| Patrick Kane: 1+ points | 0.443 | 0.540 | 56/48 | +0.060 | STANDARD |

**EDM @ VAN** · priced 115/115 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.37, exp saves 26.01 (sd 7.19), pull risk 0.072
- EDM net: Devon Levi (CONFIRMED) exp shots 26.05, exp saves 22.61 (sd 6.28), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.169 | 0.345 | 36/67 | +0.146 | STANDARD |
| Leon Draisaitl: 2+ points | 0.309 | 0.485 | 50/53 | +0.143 | STANDARD |
| Connor McDavid: 1+ assists | 0.524 | 0.695 | 70/31 | +0.151 | STANDARD |
| Connor McDavid: 2+ points | 0.392 | 0.550 | 56/46 | +0.131 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.439 | 0.590 | 60/42 | +0.124 | STANDARD |
| Connor McDavid: 3+ points | 0.156 | 0.295 | 31/72 | +0.110 | STANDARD |

**FLA @ SJS** · priced 135/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.16, exp saves 23.68 (sd 6.44), pull risk 0.058
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.2, exp saves 22.4 (sd 6.33), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aleksander Barkov: 1+ assists | 0.308 | 0.485 | 50/53 | +0.144 | STANDARD |
| Aleksander Barkov: 1+ points | 0.459 | 0.635 | 65/38 | +0.144 | STANDARD |
| Brady Tkachuk: 1+ points | 0.466 | 0.625 | 64/39 | +0.128 | STANDARD |
| Aleksander Barkov: 2+ points | 0.122 | 0.275 | 29/74 | +0.124 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.251 | 0.390 | 40/62 | +0.112 | STANDARD |
| Brady Tkachuk: 2+ points | 0.134 | 0.255 | 27/76 | +0.093 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
