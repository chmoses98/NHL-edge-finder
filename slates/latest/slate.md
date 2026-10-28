# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T09:12:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2408 · contracts joined: 204 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 104, 'NO_EDGE': 35, 'OK': 65}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'game_early_goal': 4, 'game_winner': 8, 'game_overtime': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 2026-10-28T23:30:00Z | T-12h | 0.655 | 0.345 | 0.167 | 5.96 | 3.48 | 2.49 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ EDM | 2026-10-29T00:30:00Z | T-12h | 0.599 | 0.401 | 0.168 | 6.37 | 3.51 | 2.86 | 51 (25/26) | PROJECTED/PROJECTED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-12h | 0.576 | 0.424 | 0.174 | 6.15 | 3.31 | 2.84 | 51 (25/26) | PROJECTED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-12h | 0.564 | 0.436 | 0.165 | 6.79 | 3.60 | 3.18 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.564 | 0.475 | 0.493 | 48 | 53 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.351 | 0.275 | 0.289 | 28 | 73 | yes | +0.057 | OK |
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.436 | 0.515 | 0.499 | 52 | 49 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.243 | 0.315 | 0.300 | 32 | 69 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.244 | 0.315 | 0.300 | 32 | 69 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.377 | 0.445 | 0.431 | 45 | 56 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.144 | 0.205 | 0.191 | 21 | 80 | no | +0.045 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.401 | 0.335 | 0.348 | 34 | 67 | yes | +0.045 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.599 | 0.665 | 0.652 | 67 | 34 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.480 | 0.550 | 0.536 | 56 | 46 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.218 | 0.275 | 0.263 | 28 | 73 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.689 | 0.750 | 0.738 | 76 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.493 | 0.425 | 0.439 | 44 | 59 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.281 | 0.345 | 0.332 | 36 | 67 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-7 | game_total | 0.412 | 0.465 | 0.454 | 47 | 54 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.230 | 0.180 | 0.189 | 19 | 83 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.434 | 0.495 | 0.483 | 51 | 52 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.740 | 0.785 | 0.777 | 79 | 22 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.526 | 0.580 | 0.569 | 59 | 43 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.836 | 0.875 | 0.868 | 88 | 13 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.300 | 0.245 | 0.255 | 26 | 77 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.649 | 0.700 | 0.690 | 71 | 31 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL2 | game_spread | 0.347 | 0.395 | 0.385 | 40 | 61 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.698 | 0.645 | 0.656 | 66 | 37 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.137 | 0.180 | 0.171 | 19 | 83 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.273 | 0.320 | 0.310 | 33 | 69 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.472 | 0.525 | 0.514 | 54 | 49 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-8 | game_total | 0.226 | 0.265 | 0.257 | 27 | 74 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.403 | 0.455 | 0.444 | 47 | 56 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.864 | 0.895 | 0.889 | 90 | 11 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.157 | 0.115 | 0.123 | 13 | 90 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.616 | 0.670 | 0.660 | 69 | 35 | no | +0.018 | OK |
| KXNHLGAME-26OCT28NJCOL-NJ | game_winner | 0.424 | 0.385 | 0.393 | 39 | 62 | yes | +0.017 | OK |
| KXNHLGAME-26OCT28NJCOL-COL | game_winner | 0.576 | 0.615 | 0.607 | 62 | 39 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.814 | 0.850 | 0.843 | 86 | 16 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.477 | 0.515 | 0.507 | 52 | 49 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.691 | 0.730 | 0.722 | 74 | 28 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.256 | 0.225 | 0.231 | 23 | 78 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.838 | 0.870 | 0.864 | 88 | 14 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.849 | 0.875 | 0.870 | 88 | 13 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.765 | 0.795 | 0.789 | 80 | 21 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.224 | 0.195 | 0.200 | 20 | 81 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.550 | 0.590 | 0.582 | 60 | 42 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.440 | 0.475 | 0.468 | 48 | 53 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.871 | 0.895 | 0.891 | 90 | 11 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.284 | 0.320 | 0.313 | 33 | 69 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.245 | 0.285 | 0.277 | 30 | 73 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.870 | 0.840 | 0.846 | 85 | 17 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.136 | 0.115 | 0.119 | 12 | 89 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.114 | 0.095 | 0.099 | 10 | 91 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.791 | 0.815 | 0.810 | 82 | 19 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.097 | 0.115 | 0.111 | 12 | 89 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-9 | game_total | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.106 | 0.130 | 0.125 | 14 | 88 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.962 | 0.975 | 0.973 | 98 | 3 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.589 | 0.620 | 0.614 | 63 | 39 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.428 | 0.455 | 0.450 | 46 | 55 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.223 | 0.260 | 0.252 | 28 | 76 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL6 | team_total | 0.118 | 0.140 | 0.135 | 15 | 87 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.860 | 0.885 | 0.880 | 90 | 13 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.347 | 0.320 | 0.325 | 33 | 69 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.957 | 0.975 | 0.972 | 99 | 4 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.285 | 0.305 | 0.301 | 31 | 70 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-PHI3 | game_spread | 0.085 | 0.095 | 0.093 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.155 | 0.150 | 17 | 86 |  | -0.000 | NO_EDGE |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.345 | 0.325 | 0.329 | 33 | 68 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.655 | 0.675 | 0.671 | 68 | 33 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.969 | 0.980 | 0.978 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.895 | 0.910 | 0.907 | 92 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-10 | game_total | 0.067 | 0.085 | 0.081 | 10 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI4 | team_total | 0.249 | 0.270 | 0.266 | 28 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.201 | 0.220 | 0.216 | 23 | 79 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI3 | team_total | 0.456 | 0.485 | 0.479 | 50 | 53 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY6 | team_total | 0.071 | 0.055 | 0.058 | 7 | 96 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY4 | team_total | 0.331 | 0.310 | 0.314 | 32 | 70 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.253 | 0.270 | 0.267 | 28 | 74 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.655 | 0.557 | 0.167 | 0.224 | 5.96 | 6.00 | 0.961/0.992 | KXNHLSPREAD-26OCT28PHIWSH-WSH2 -0.102 |
| CGY @ EDM | 0.599 | 0.667 | 0.168 | 0.200 | 6.37 | 6.73 | 1.009/0.986 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.092 |
| NJD @ COL | 0.576 | 0.622 | 0.174 | 0.212 | 6.15 | 6.33 | 0.977/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.057 |
| TOR @ SEA | 0.564 | 0.551 | 0.165 | 0.214 | 6.79 | 6.60 | 1.016/0.965 | KXNHLTOTAL-26OCT28TORSEA-8 -0.032 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 5 recommended · full analysis in card.md / packet.json `thesis_card`

- Washington over 4.5 goals scored NO @ 69c · p 0.7767 (adj 0.7283) · $17.03 · thesis WSH:SUPPRESSED
- Philadelphia wins by over 1.5 goals YES @ 16c · p 0.2216 (adj 0.1883) · $3.48 · thesis PHI:WINS_BY_2PLUS
- Washington wins by over 1.5 goals NO @ 55c · p 0.6643 (adj 0.5868) · $2.17 · thesis GAME:TIGHT
- Toronto wins by over 2.5 goals NO @ 80c · p 0.8528 (adj 0.8239) · $13.14 · thesis SEA:WINS
- Toronto wins by over 1.5 goals NO @ 69c · p 0.7533 (adj 0.7191) · $5.96 · thesis SEA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.27 (sd 6.06), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 27.44, exp saves 23.58 (sd 6.57), pull risk 0.068

**CGY @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.03, exp saves 23.8 (sd 6.4), pull risk 0.048
- CGY net: Devin Cooley (PROJECTED) exp shots 30.57, exp saves 25.51 (sd 7.45), pull risk 0.105

**NJD @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 28.33, exp saves 24.83 (sd 6.58), pull risk 0.048
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.79 (sd 6.94), pull risk 0.079

**TOR @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.75, exp saves 24.83 (sd 6.78), pull risk 0.065
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.18, exp saves 25.72 (sd 7.05), pull risk 0.076

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
