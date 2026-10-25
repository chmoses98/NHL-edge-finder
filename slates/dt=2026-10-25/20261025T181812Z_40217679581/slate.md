# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T18:18:12Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3061 · contracts joined: 1149 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 1024, 'OK': 89, 'NO_EDGE': 36}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 169, 'game_early_goal': 5, 'first_goal': 182, 'game_winner': 10, 'player_goals': 312, 'game_overtime': 5, 'player_points': 225, 'goalie_saves': 6, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 2026-10-25T19:00:00Z | T-30m | 0.495 | 0.505 | 0.186 | 6.04 | 3.00 | 3.03 | 229 (25/204) | PROJECTED/CONFIRMED |
| NYI @ DAL | 2026-10-25T22:00:00Z | T-3h | 0.552 | 0.448 | 0.187 | 5.45 | 2.89 | 2.57 | 226 (25/201) | PROJECTED/PROBABLE |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-3h | 0.464 | 0.536 | 0.180 | 5.94 | 2.87 | 3.07 | 229 (25/204) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-3h | 0.373 | 0.627 | 0.168 | 6.00 | 2.60 | 3.40 | 237 (25/212) | PROBABLE/PROBABLE |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-6h | 0.448 | 0.552 | 0.170 | 6.81 | 3.23 | 3.58 | 228 (25/203) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT25FLACHI-FLA2 | game_spread | 0.283 | 0.415 | 0.387 | 42 | 59 | no | +0.110 | OK |
| KXNHLGAME-26OCT25FLACHI-CHI | game_winner | 0.495 | 0.365 | 0.390 | 37 | 64 | yes | +0.109 | OK |
| KXNHLGAME-26OCT25FLACHI-FLA | game_winner | 0.505 | 0.635 | 0.610 | 64 | 37 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA4 | team_total | 0.373 | 0.500 | 0.474 | 51 | 51 | no | +0.099 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA3 | game_spread | 0.169 | 0.285 | 0.258 | 29 | 72 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 | team_total | 0.590 | 0.710 | 0.688 | 72 | 30 | no | +0.095 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.454 | 0.570 | 0.547 | 58 | 44 | no | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.335 | 0.435 | 0.414 | 44 | 57 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.257 | 0.360 | 0.338 | 37 | 65 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.673 | 0.770 | 0.752 | 78 | 24 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA5 | team_total | 0.194 | 0.295 | 0.273 | 31 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.417 | 0.320 | 0.339 | 33 | 69 | yes | +0.072 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.448 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.186 | 0.275 | 0.255 | 28 | 73 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.627 | 0.535 | 0.554 | 54 | 47 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.256 | 0.345 | 0.326 | 35 | 66 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.416 | 0.505 | 0.487 | 51 | 50 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.340 | 0.425 | 0.407 | 43 | 58 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI2 | game_spread | 0.273 | 0.195 | 0.209 | 20 | 81 | yes | +0.062 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.552 | 0.635 | 0.619 | 64 | 37 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT25COLNSH-6 | game_total | 0.533 | 0.620 | 0.603 | 63 | 39 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT25COLNSH-5 | game_total | 0.750 | 0.830 | 0.816 | 84 | 18 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.565 | 0.650 | 0.634 | 66 | 36 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT25COLNSH-4 | game_total | 0.837 | 0.905 | 0.894 | 91 | 10 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.236 | 0.155 | 0.169 | 17 | 86 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.163 | 0.240 | 0.223 | 25 | 77 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT25COLNSH-8 | game_total | 0.231 | 0.305 | 0.289 | 31 | 70 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.223 | 0.300 | 0.283 | 31 | 71 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.552 | 0.625 | 0.611 | 63 | 38 | no | +0.051 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.448 | 0.375 | 0.389 | 38 | 63 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA2 | team_total | 0.802 | 0.870 | 0.858 | 88 | 14 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.783 | 0.850 | 0.838 | 86 | 16 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.119 | 0.180 | 0.166 | 19 | 83 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT25COLNSH-9 | game_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA6 | team_total | 0.082 | 0.140 | 0.126 | 15 | 87 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4 | team_total | 0.364 | 0.300 | 0.312 | 31 | 71 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.855 | 0.910 | 0.901 | 92 | 10 | no | +0.039 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.038 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.351 | 0.295 | 0.306 | 30 | 71 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.670 | 0.725 | 0.715 | 73 | 28 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI3 | game_spread | 0.163 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.224 | 0.175 | 0.184 | 18 | 83 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI3 | team_total | 0.580 | 0.520 | 0.532 | 53 | 49 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT25FLACHI-6 | game_total | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.823 | 0.770 | 0.781 | 78 | 24 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI5 | team_total | 0.189 | 0.145 | 0.153 | 15 | 86 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.133 | 0.095 | 0.102 | 10 | 91 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.258 | 0.210 | 0.219 | 22 | 80 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT25FLACHI-5 | game_total | 0.754 | 0.795 | 0.787 | 80 | 21 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.110 | 0.065 | 0.072 | 8 | 95 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.320 | 0.365 | 0.356 | 37 | 64 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT25COLNSH-10 | game_total | 0.071 | 0.110 | 0.101 | 12 | 90 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.150 | 0.110 | 0.117 | 12 | 90 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25FLACHI-4 | game_total | 0.839 | 0.875 | 0.868 | 88 | 13 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.430 | 0.475 | 0.466 | 48 | 53 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI2 | team_total | 0.794 | 0.750 | 0.759 | 76 | 26 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.067 | 0.105 | 0.096 | 12 | 91 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.122 | 0.095 | 0.100 | 10 | 91 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-10 | game_total | 0.041 | 0.065 | 0.059 | 7 | 94 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25FLACHI-7 | game_total | 0.420 | 0.455 | 0.448 | 46 | 55 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25COLNSH-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT25FLACHI-8 | game_total | 0.235 | 0.265 | 0.259 | 27 | 74 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.491 | 0.530 | 0.522 | 54 | 48 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.656 | 0.625 | 0.631 | 63 | 38 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-8 | game_total | 0.160 | 0.190 | 0.184 | 20 | 82 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.780 | 0.810 | 0.804 | 82 | 20 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.937 | 0.955 | 0.952 | 96 | 5 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI6 | team_total | 0.084 | 0.060 | 0.064 | 7 | 95 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT25MTLWPG-WPG3 | game_spread | 0.143 | 0.170 | 0.164 | 18 | 84 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.699 | 0.730 | 0.724 | 74 | 28 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.106 | 0.125 | 0.121 | 13 | 88 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT25FLACHI-9 | game_total | 0.164 | 0.185 | 0.181 | 19 | 82 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.827 | 0.850 | 0.846 | 86 | 16 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5 | team_total | 0.121 | 0.100 | 0.104 | 11 | 91 | yes | +0.004 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 0.495 | 0.474 | 0.186 | 0.223 | 6.04 | 6.28 | 1.003/0.991 | KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 +0.047 |
| NYI @ DAL | 0.552 | 0.549 | 0.187 | 0.221 | 5.45 | 6.00 | 0.986/0.951 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.101 |
| MTL @ WPG | 0.464 | 0.481 | 0.180 | 0.222 | 5.94 | 6.25 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.053 |
| COL @ NSH | 0.373 | 0.394 | 0.168 | 0.214 | 6.00 | 6.46 | 0.991/0.972 | KXNHLTOTAL-26OCT25COLNSH-7 +0.079 |
| MIN @ VAN | 0.448 | 0.520 | 0.170 | 0.217 | 6.81 | 6.51 | 1.030/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.089 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 19 recommended · full analysis in card.md / packet.json `thesis_card`

- Brady Tkachuk: 1+ goals NO @ 61c · p 0.6932 (adj 0.6712) · $20.0 · thesis FLA:SUPPRESSED
- Anton Frondell: 1+ goals YES @ 18c · p 0.2415 (adj 0.2249) · $9.99 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 23c · p 0.2865 (adj 0.2711) · $9.03 · thesis CHI:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 11c · p 0.1518 (adj 0.1301) · $3.36 · thesis FLA:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 16c · p 0.2276 (adj 0.2082) · $10.76 · thesis NYI:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.16 (adj 0.1462) · $4.89 · thesis NYI:OFFENSE_4PLUS
- David Perron: 1+ goals YES @ 13c · p 0.1633 (adj 0.1537) · $4.55 · thesis DAL:OFFENSE_4PLUS
- Anthony Duclair: 1+ goals YES @ 12c · p 0.1511 (adj 0.1421) · $3.93 · thesis NYI:OFFENSE_4PLUS
- Alexandre Carrier: 1+ goals YES @ 4c · p 0.0677 (adj 0.0583) · $3.33 · thesis MTL:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 4c · p 0.061 (adj 0.0532) · $2.32 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3351 (adj 0.3226) · $6.41 · thesis WPG:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 18c · p 0.2118 (adj 0.2026) · $3.78 · thesis MTL:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ assists NO @ 41c · p 0.4958 (adj 0.4479) · $7.32 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 53c · p 0.609 (adj 0.567) · $4.89 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 66c · p 0.7324 (adj 0.6937) · $7.32 · thesis GAME:TIGHT
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2236 (adj 0.2002) · $8.28 · thesis VAN:OFFENSE_4PLUS
- Matt Boldy: 1+ goals NO @ 59c · p 0.6593 (adj 0.6407) · $20.0 · thesis MIN:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2315 (adj 0.2161) · $7.47 · thesis VAN:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 19c · p 0.2411 (adj 0.2258) · $7.17 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CHI** · priced 175/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 28.49, exp saves 24.39 (sd 6.74), pull risk 0.066
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.46, exp saves 21.17 (sd 6.11), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Reinhart: 1+ points | 0.486 | 0.615 | 63/40 | +0.097 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.328 | 0.440 | 45/57 | +0.085 | STANDARD |
| Patrick Kane: 1+ assists | 0.319 | 0.430 | 44/58 | +0.084 | STANDARD |
| Brady Tkachuk: 1+ points | 0.534 | 0.640 | 65/37 | +0.079 | STANDARD |
| Sam Reinhart: 1+ assists | 0.301 | 0.400 | 42/62 | +0.063 | STANDARD |
| Seth Jones: 1+ points | 0.438 | 0.535 | 55/48 | +0.065 | STANDARD |

**NYI @ DAL** · priced 170/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.18 (sd 6.11), pull risk 0.047
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.22, exp saves 22.68 (sd 6.22), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nils Lundkvist: 1+ points | 0.272 | 0.110 | 21/99 | +0.050 | STANDARD |
| Ilya Sorokin: 25+ saves | 0.370 | 0.220 | 43/99 | -0.077 |  |
| Logan Stanley: 1+ points | 0.278 | 0.135 | 26/99 | +0.004 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.232 | 0.095 | 18/99 | +0.042 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.426 | 0.510 | 53/51 | +0.047 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.446 | 0.530 | 55/49 | +0.046 | STANDARD |

**MTL @ WPG** · priced 174/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.39), pull risk 0.059
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.54, exp saves 23.94 (sd 6.53), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alexandre Carrier: 1+ points | 0.318 | 0.145 | 28/99 | +0.023 | STANDARD |
| Dylan Samberg: 1+ assists | 0.265 | 0.120 | 23/99 | +0.023 | STANDARD |
| Kaiden Guhle: 1+ points | 0.280 | 0.140 | 27/99 | -0.003 | STANDARD |
| Adam Lowry: 1+ points | 0.296 | 0.180 | 31/95 | -0.028 | STANDARD |
| Kaiden Guhle: 1+ assists | 0.236 | 0.125 | 24/99 | -0.017 | STANDARD |
| Alex Iafallo: 1+ goals | 0.170 | 0.080 | 13/97 | +0.032 | STANDARD |

**COL @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROBABLE) exp shots 32.01, exp saves 27.18 (sd 7.46), pull risk 0.085
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.47, exp saves 23.19 (sd 6.3), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Scott Wedgewood: 22+ saves | 0.608 | 0.295 | 54/95 | +0.050 |  |
| Justus Annunen: 29+ saves | 0.429 | 0.290 | 52/94 | -0.108 |  |
| Nathan MacKinnon: 2+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Cale Makar: 1+ assists | 0.459 | 0.555 | 57/46 | +0.063 | STANDARD |
| Cale Makar: 2+ points | 0.193 | 0.285 | 31/74 | +0.054 | STANDARD |

**MIN @ VAN** · priced 167/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.99, exp saves 26.85 (sd 7.13), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.64, exp saves 22.17 (sd 6.21), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Calvin Pickard: 22+ saves | 0.545 | 0.270 | 47/93 | +0.057 |  |
| Liam Ohgren: 1+ points | 0.381 | 0.160 | 31/99 | +0.056 | STANDARD |
| Yakov Trenin: 1+ points | 0.305 | 0.140 | 27/99 | +0.021 | STANDARD |
| Liam Ohgren: 1+ assists | 0.264 | 0.110 | 21/99 | +0.042 | STANDARD |
| Brendan Gallagher: 1+ points | 0.271 | 0.125 | 24/99 | +0.018 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.268 | 0.410 | 43/61 | +0.105 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
