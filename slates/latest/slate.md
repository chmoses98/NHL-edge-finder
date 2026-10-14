# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-14T01:01:45Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 3 · markets on board: 5308 · contracts joined: 779 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 704, 'OK': 27, 'NO_EDGE': 48}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 139, 'game_early_goal': 3, 'first_goal': 112, 'game_winner': 6, 'player_goals': 186, 'game_overtime': 3, 'player_points': 183, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ ANA | 2026-10-14T01:45:00Z | T-30m | 0.645 | 0.355 | 0.171 | 6.36 | 3.64 | 2.72 | 257 (25/232) | CONFIRMED/PROBABLE |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-60m | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 245 (25/220) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-90m | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 | team_total | 0.539 | 0.595 | 0.584 | 60 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 | team_total | 0.324 | 0.375 | 0.364 | 38 | 63 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.170 | 0.159 | 18 | 84 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.359 | 0.315 | 0.324 | 32 | 69 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ2 | team_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.021 | OK |
| KXNHLGAME-26OCT13BOSSJ-BOS | game_winner | 0.587 | 0.545 | 0.554 | 55 | 46 | yes | +0.020 | OK |
| KXNHLGAME-26OCT13BOSSJ-SJ | game_winner | 0.413 | 0.455 | 0.446 | 46 | 55 | no | +0.020 | OK |
| KXNHLGAME-26OCT13CGYANA-ANA | game_winner | 0.645 | 0.605 | 0.613 | 61 | 40 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT13CGYANA-CGY2 | game_spread | 0.172 | 0.205 | 0.198 | 21 | 80 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT13EDMLA-LA3 | game_spread | 0.135 | 0.165 | 0.159 | 17 | 84 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ5 | team_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT13CGYANA-10 | game_total | 0.097 | 0.075 | 0.079 | 8 | 93 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT13CGYANA-CGY3 | game_spread | 0.092 | 0.115 | 0.110 | 12 | 89 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT13CGYANA-9 | game_total | 0.201 | 0.175 | 0.180 | 18 | 83 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS3 | game_spread | 0.231 | 0.205 | 0.210 | 21 | 80 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-5 | game_total | 0.769 | 0.795 | 0.790 | 80 | 21 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-4 | game_total | 0.853 | 0.875 | 0.871 | 88 | 13 | no | +0.009 | OK |
| KXNHLGAME-26OCT13CGYANA-CGY | game_winner | 0.355 | 0.385 | 0.379 | 39 | 62 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA5 | team_total | 0.303 | 0.270 | 0.276 | 28 | 74 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT13CGYANA-8 | game_total | 0.281 | 0.255 | 0.260 | 26 | 75 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS3 | team_total | 0.662 | 0.635 | 0.640 | 64 | 37 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA6 | team_total | 0.154 | 0.130 | 0.135 | 14 | 88 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS6 | team_total | 0.121 | 0.100 | 0.104 | 11 | 91 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT13CGYANA-7 | game_total | 0.472 | 0.445 | 0.450 | 45 | 56 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA3 | team_total | 0.718 | 0.685 | 0.692 | 70 | 33 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA4 | team_total | 0.510 | 0.480 | 0.486 | 49 | 53 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM3 | team_total | 0.656 | 0.635 | 0.639 | 64 | 37 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT13CGYANA-6 | game_total | 0.587 | 0.565 | 0.569 | 57 | 44 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT13EDMLA-LA2 | game_spread | 0.237 | 0.255 | 0.251 | 26 | 75 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS5 | team_total | 0.252 | 0.230 | 0.234 | 24 | 78 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT13CGYANA-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ6 | team_total | 0.067 | 0.080 | 0.077 | 9 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM6 | team_total | 0.115 | 0.100 | 0.103 | 11 | 91 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-10 | game_total | 0.083 | 0.075 | 0.076 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-7 | game_total | 0.446 | 0.465 | 0.461 | 47 | 54 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-6 | game_total | 0.557 | 0.575 | 0.571 | 58 | 43 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-4 | game_total | 0.866 | 0.875 | 0.873 | 88 | 13 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA3 | team_total | 0.567 | 0.585 | 0.581 | 59 | 42 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT13CGYANA-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT13EDMLA-EDM2 | game_spread | 0.340 | 0.325 | 0.328 | 33 | 68 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS2 | team_total | 0.844 | 0.835 | 0.837 | 84 | 17 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM5 | team_total | 0.248 | 0.230 | 0.233 | 24 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13CGYANA-CGY3 | team_total | 0.512 | 0.495 | 0.498 | 50 | 51 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA2 | team_total | 0.784 | 0.800 | 0.797 | 81 | 21 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-3 | game_total | 0.964 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-8 | game_total | 0.267 | 0.255 | 0.257 | 26 | 75 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-5 | game_total | 0.785 | 0.795 | 0.793 | 80 | 21 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13CGYANA-CGY2 | team_total | 0.744 | 0.755 | 0.753 | 76 | 25 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-3 | game_total | 0.965 | 0.965 | 0.965 | 97 | 4 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT13CGYANA-ANA2 | game_spread | 0.419 | 0.405 | 0.408 | 41 | 60 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-9 | game_total | 0.177 | 0.185 | 0.183 | 19 | 82 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT13CGYANA-4 | game_total | 0.870 | 0.875 | 0.874 | 88 | 13 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT13EDMLA-EDM | game_winner | 0.560 | 0.545 | 0.548 | 55 | 46 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT13EDMLA-LA | game_winner | 0.440 | 0.455 | 0.452 | 46 | 55 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA4 | team_total | 0.352 | 0.370 | 0.366 | 38 | 64 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13CGYANA-ANA2 | team_total | 0.879 | 0.865 | 0.868 | 88 | 15 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-8 | game_total | 0.255 | 0.265 | 0.263 | 27 | 74 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-10 | game_total | 0.087 | 0.085 | 0.085 | 9 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT13CGYANA-5 | game_total | 0.788 | 0.795 | 0.794 | 80 | 21 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA6 | team_total | 0.076 | 0.080 | 0.079 | 9 | 93 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13CGYANA-CGY4 | team_total | 0.296 | 0.310 | 0.307 | 32 | 70 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA5 | team_total | 0.181 | 0.190 | 0.188 | 20 | 82 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS4 | team_total | 0.444 | 0.435 | 0.437 | 44 | 57 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13CGYANA-CGY6 | team_total | 0.061 | 0.060 | 0.060 | 7 | 95 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-9 | game_total | 0.187 | 0.185 | 0.185 | 19 | 82 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13CGYANA-CGY5 | team_total | 0.147 | 0.150 | 0.149 | 16 | 86 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM2 | team_total | 0.843 | 0.840 | 0.841 | 85 | 17 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT13CGYANA-ANA3 | game_spread | 0.278 | 0.275 | 0.276 | 28 | 73 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT13EDMLA-EDM3 | game_spread | 0.214 | 0.215 | 0.215 | 22 | 79 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-7 | game_total | 0.462 | 0.465 | 0.464 | 47 | 54 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-6 | game_total | 0.577 | 0.575 | 0.575 | 58 | 43 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM4 | team_total | 0.441 | 0.440 | 0.440 | 45 | 57 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT13CGYANA-ANA | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT13CGYANA-CGY | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT13CGYANA-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT13CGYANA-ANA2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT13CGYANA-CGY2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CGY @ ANA | 0.645 | 0.631 | 0.171 | 0.210 | 6.36 | 6.41 | 1.016/1.002 | KXNHLTEAMTOTAL-26OCT13CGYANA-CGY2 +0.018 |
| EDM @ LAK | 0.440 | 0.480 | 0.173 | 0.218 | 6.27 | 6.25 | 0.995/0.994 | KXNHLSPREAD-26OCT13EDMLA-EDM2 -0.043 |
| BOS @ SJS | 0.413 | 0.507 | 0.175 | 0.216 | 6.17 | 6.40 | 1.039/0.956 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 +0.094 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Tim Washe: 1+ goals YES @ 9c · p 0.149 (adj 0.133) · $8.97 · thesis ANA:OFFENSE_4PLUS
- A.J. Greer: 2+ goals YES @ 2c · p 0.0442 (adj 0.0382) · $3.37 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1395 (adj 0.1259) · $7.46 · thesis ANA:OFFENSE_4PLUS
- Pavel Mintyukov: 1+ goals YES @ 7c · p 0.0996 (adj 0.091) · $3.85 · thesis ANA:OFFENSE_4PLUS
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9098 (adj 0.8624) · $20.0 · thesis LAK:SUPPRESSED
- Mattias Ekholm: 1+ assists YES @ 28c · p 0.3533 (adj 0.3116) · $6.36 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.5647 (adj 0.4449) · $8.41 · thesis EDM:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 25c · p 0.2859 (adj 0.2757) · $4.54 · thesis LAK:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $6.98 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 55c · p 0.7032 (adj 0.6004) · $20.0 · thesis BOS:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.148 (adj 0.1372) · $5.52 · thesis BOS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2154 (adj 0.2028) · $6.44 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CGY @ ANA** · priced 198/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 26.29, exp saves 23.15 (sd 6.3), pull risk 0.047
- CGY net: Dustin Wolf (PROBABLE) exp shots 31.79, exp saves 26.75 (sd 7.4), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ assists | 0.294 | 0.095 | 17/98 | +0.114 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.237 | 0.080 | 13/97 | +0.100 | STANDARD |
| Noah Warren: 1+ points | 0.341 | 0.185 | 20/83 | +0.130 | PRIOR_HEAVY |
| Zach Whitecloud: 1+ assists | 0.223 | 0.080 | 13/97 | +0.085 | STANDARD |
| Tim Washe: 1+ assists | 0.256 | 0.115 | 21/98 | +0.034 | STANDARD |
| Jeff Malott: 1+ points | 0.299 | 0.175 | 23/88 | +0.057 | STANDARD |

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
| Jeremy Swayman: 25+ saves | 0.455 | 0.295 | 53/94 | -0.092 |  |
| Charlie McAvoy: 1+ points | 0.396 | 0.555 | 56/45 | +0.137 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.297 | 0.455 | 46/55 | +0.136 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.555 | 57/46 | +0.103 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.230 | 0.095 | 17/98 | +0.050 | STANDARD |
| Sam Dickinson: 1+ assists | 0.215 | 0.080 | 14/98 | +0.066 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
