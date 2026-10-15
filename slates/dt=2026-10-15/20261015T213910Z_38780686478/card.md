# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T21:39:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +24.54 | +5.77 | +24.84 | 0.831 | -8.29 | -17.11 | 54.34 |
| B thesis-diversified (joint) ← optimiser card | 147.28 | +16.36 | +7.08 | +16.23 | 0.773 | -11.19 | -19.49 | 68.40 |
| C best expression per thesis | 150.01 | +22.79 | +8.25 | +20.59 | 0.780 | -13.07 | -23.24 | 78.20 |
| R FUNDED research stakes | 22.00 | +1.97 | +0.97 | +1.66 | 0.638 | -4.48 | -6.18 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  480 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.521 / away 0.479

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.50 | 0.50 | 0.00 | 6.06 | 28.1/28.8 | 25.2/24.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.110 | 0.48 | 0.52 | 0.00 | 6.0 | 22.2/34.0 | 30.2/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.49 | 5.95 | 28.2/28.9 | 25.4/24.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.48 | 5.92 | 22.4/34.5 | 31.2/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 9.36 | 29.3/30.2 | 23.9/22.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.086 | 0.45 | 0.55 | 0.00 | 9.39 | 23.7/36.0 | 29.0/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 86 | 0.915 | 0.899 | +0.047 | +0.030 | $6.68 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 60 | 0.642 | 0.630 | +0.026 | +0.014 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 59 | 0.628 | 0.617 | +0.021 | +0.010 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (18.03 vs 2.96 bp); despite a smaller raw edge (+0.047 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15BUFTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: Player prop expression KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.81 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15BUFTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: BUF offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no; why: Player prop expression KXNHLGOAL-26OCT15BUFTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.81 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3639): highest fidelity KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3752): highest fidelity KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no (same contract)
- thesis TOR:NET_HIGH_VOLUME (p 0.3635): highest fidelity KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes (same contract)
- KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4055, phi -0.117)
- KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4055, phi -0.256)
- KXNHLGOAL-26OCT15BUFTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4115, phi -0.276)
- override: Player prop expression KXNHLGOAL-26OCT15BUFTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.81 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.81 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.50 (adj +0.34) on $13.64, P(profit) 0.6133, adj growth 3.2 bp · B EV +0.56 (adj +0.34) on $11.85, P(profit) 0.5873, adj growth 3.3 bp · C EV +1.85 (adj +0.44) on $17.69, P(profit) 0.6694, adj growth 4.2 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.915, adj growth 2.8 bp

## NYI @ OTT  ·  10000 joint draws  ·  458 bet sides mapped, 10 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 5.98 | 26.8/26.8 | 23.9/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.44 | 5.9 | 26.9/26.6 | 23.5/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.097 | 0.69 | 0.31 | 0.00 | 6.02 | 31.9/21.0 | 18.3/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.23 | 28.5/28.2 | 23.1/21.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.57 | 0.43 | 0.46 | 5.82 | 31.8/21.5 | 18.4/28.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 3.42 | 25.5/25.5 | 24.0/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 9 | 0.123 | 0.113 | +0.027 | +0.018 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.014 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Semyon Varlamov: 26+ saves NO | 55 | 0.631 | 0.588 | +0.064 | +0.021 | $4.20 | FUNDED_RESEARCH | $2 | NYI:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (7.56 vs 0.60 bp); despite a smaller raw edge (+0.027 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.334); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSAVE-26OCT15NYIOTT-NYISVARLAMOV40-26|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (3.91 vs 0.60 bp); despite a smaller raw edge (+0.025 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.334); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSAVE-26OCT15NYIOTT-NYISVARLAMOV40-26|no: MOSTLY_INDEPENDENT (phi -0.009); failure: NYI offense suppressed (<= 2 goals)
- **Semyon Varlamov: 26+ saves NO** — thesis: NYI net faces light volume (<= 25 shots; OTT suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT15NYIOTT-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: NYI net faces heavy volume (33+ shots; OTT pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYI:NET_LOW_VOLUME (p 0.4018): highest fidelity KXNHLSAVE-26OCT15NYIOTT-NYISVARLAMOV40-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT15NYIOTT-NYISVARLAMOV40-26|no (same contract)
- thesis OTT:SUPPRESSED (p 0.349): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.2978): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4937, phi -0.183)
- KXNHLGOAL-26OCT15NYIOTT-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4937, phi -0.2)
- KXNHLSAVE-26OCT15NYIOTT-NYISVARLAMOV40-26|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NYI:NET_HIGH_VOLUME (p 0.1928, phi -0.554)

portfolios: A EV +1.16 (adj +0.28) on $13.64, P(profit) 0.7478, adj growth 2.7 bp · B EV +1.13 (adj +0.56) on $6.96, P(profit) 0.7288, adj growth 5.4 bp · C EV +0.84 (adj +0.25) on $9.22, P(profit) 0.4679, adj growth 2.3 bp · R EV +0.22 (adj +0.07) on $2.00, P(profit) 0.6308, adj growth 2.7 bp

## SEA @ TBL  ·  10000 joint draws  ·  436 bet sides mapped, 35 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.705 / away 0.295

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.136 | 0.68 | 0.32 | 0.00 | 6.0 | 32.8/21.2 | 18.5/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.59 | 0.41 | 0.00 | 5.98 | 27.3/26.6 | 23.4/23.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.45 | 5.82 | 33.0/21.5 | 18.4/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.95 | 27.4/26.8 | 23.5/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 9.18 | 34.4/22.6 | 18.1/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 9.15 | 28.6/28.0 | 22.5/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ goals NO | 83 | 0.881 | 0.867 | +0.041 | +0.027 | $4.41 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 52 | 0.680 | 0.570 | +0.143 | +0.032 | $3.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.640 | 0.626 | +0.034 | +0.020 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (12.10 vs 10.14 bp); despite a smaller raw edge (+0.041 vs +0.132/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TBL offense succeeds (4+ goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no has the higher standalone adjusted growth (10.14 vs 9.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.098); relationships: KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.143); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.143); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3553): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2152): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4164): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT15SEATB-TBJCARLSON74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.138)
- KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.0 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.243)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.26)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.43 (adj +0.87) on $13.64, P(profit) 0.6253, adj growth 8.0 bp · B EV +1.26 (adj +0.42) on $10.03, P(profit) 0.599, adj growth 4.1 bp · C EV +2.55 (adj +0.68) on $8.20, P(profit) 0.5551, adj growth 6.4 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.8809, adj growth 2.5 bp

## VAN @ FLA  ·  10000 joint draws  ·  422 bet sides mapped, 34 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.715 / away 0.285

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.118 | 0.68 | 0.32 | 0.00 | 6.02 | 32.7/21.1 | 18.4/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.61 | 0.39 | 0.00 | 6.02 | 27.2/26.7 | 23.7/23.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.45 | 5.96 | 32.6/21.4 | 18.2/29.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.49 | 6.0 | 27.5/26.9 | 23.5/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.59 | 0.41 | 0.00 | 9.35 | 28.9/28.4 | 22.7/22.4 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.087 | 0.67 | 0.33 | 0.00 | 9.22 | 34.4/22.5 | 17.8/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 61 | 0.701 | 0.677 | +0.074 | +0.050 | $5.01 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 61 | 0.697 | 0.674 | +0.070 | +0.047 | $5.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Jake DeBrusk: 1+ goals YES | 26 | 0.321 | 0.305 | +0.048 | +0.031 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 64 | 0.767 | 0.681 | +0.111 | +0.025 | $3.17 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (24.00 vs 23.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.143); relationships: KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.184); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (24.00 vs 20.76 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.172); failure: FLA offense succeeds (4+ goals)
- **Jake DeBrusk: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes; why: Player prop expression KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes selected over broad KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes because adjusted EV is 1.0 pts higher while thesis capture is 0.43 vs 0.99 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.16); failure: VAN offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (28.92 vs 6.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.248); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: REINFORCING (phi 0.184); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: REINFORCING (phi 0.16); failure: FLA wins by 2+

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3482): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.224): highest fidelity KXNHLSPREAD-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-VAN2|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2973): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4608, phi -0.244)
- KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4608, phi -0.234)
- KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4311, phi -0.274)
- KXNHLSPREAD-26OCT15VANFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.2 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3547, phi -0.743)
- override: Player prop expression KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes selected over broad KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes because adjusted EV is 1.0 pts higher while thesis capture is 0.43 vs 0.99 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.82 (adj +0.81) on $13.64, P(profit) 0.5357, adj growth 7.3 bp · B EV +2.12 (adj +1.18) on $15.69, P(profit) 0.6229, adj growth 11.5 bp · C EV +5.22 (adj +2.73) on $11.97, P(profit) 0.383, adj growth 25.6 bp · R EV +0.40 (adj +0.20) on $3.00, P(profit) 0.7005, adj growth 7.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  434 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.544 / away 0.456

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.129 | 0.54 | 0.46 | 0.00 | 5.99 | 33.0/21.1 | 17.9/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.47 | 5.87 | 33.0/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.48 | 0.52 | 0.00 | 6.02 | 27.3/26.7 | 23.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.50 | 5.94 | 27.4/26.7 | 23.4/24.1 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.17 | 34.8/22.8 | 17.4/28.1 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.070 | 0.55 | 0.45 | 0.00 | 3.46 | 31.5/20.0 | 18.4/29.5 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ assists NO | 47 | 0.616 | 0.518 | +0.129 | +0.030 | $5.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 13 | 0.163 | 0.153 | +0.025 | +0.015 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.671 | 0.657 | +0.035 | +0.021 | $4.87 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.327 | 0.291 | +0.053 | +0.017 | $1.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: higher confidence-adjusted growth (8.10 vs 7.28 bp); relationships: KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (4.38 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.026/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (8.10 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NJD offense succeeds (4+ goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: higher confidence-adjusted growth (3.31 vs 0.67 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4147): highest fidelity KXNHLAST-26OCT15NYRNJ-NJJBRATT63-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3686): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3686, phi -0.264)
- KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4147, phi -0.2)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3686, phi -0.24)
- KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4207, phi -0.271)

portfolios: A EV +2.06 (adj +0.47) on $13.64, P(profit) 0.7409, adj growth 4.5 bp · B EV +2.25 (adj +0.76) on $13.34, P(profit) 0.6227, adj growth 7.3 bp · C EV +2.09 (adj +0.53) on $8.52, P(profit) 0.616, adj growth 5.1 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6712, adj growth 2.4 bp

## PHI @ DET  ·  10000 joint draws  ·  438 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.54 | 0.46 | 0.00 | 5.93 | 32.3/21.1 | 18.0/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.50 | 0.50 | 0.00 | 5.96 | 27.2/26.8 | 23.3/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.84 | 32.9/21.3 | 18.2/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.49 | 5.89 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 3.44 | 26.3/25.6 | 23.8/24.5 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.77 | 31.2/20.3 | 18.8/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 83 | 0.887 | 0.870 | +0.047 | +0.030 | $6.68 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.810 | +0.030 | +0.018 | $6.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.014 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 20 | 0.233 | 0.223 | +0.022 | +0.012 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (15.37 vs 3.46 bp); despite a smaller raw edge (+0.047 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (4.31 vs 0.78 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.988 vs 0.35); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: PHI offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (3.38 vs 1.95 bp); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (3.38 vs 1.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:SUPPRESSED (p 0.4542): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLTEAMTOTAL-26OCT15PHIDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.153)
- KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3214, phi -0.199)
- KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.23)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)

portfolios: A EV +0.88 (adj +0.37) on $13.64, P(profit) 0.6049, adj growth 3.6 bp · B EV +0.96 (adj +0.59) on $15.97, P(profit) 0.7759, adj growth 5.7 bp · C EV +1.09 (adj +0.51) on $16.12, P(profit) 0.6654, adj growth 4.8 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.8871, adj growth 2.9 bp

## WPG @ CHI  ·  10000 joint draws  ·  472 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.0 | 26.4/26.6 | 23.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.91 | 26.4/26.7 | 23.4/23.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.097 | 0.45 | 0.55 | 0.00 | 5.96 | 21.1/31.9 | 28.0/17.9 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.50 | 0.50 | 0.49 | 5.92 | 21.2/31.8 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.49 | 0.51 | 0.00 | 9.32 | 28.0/28.2 | 22.1/21.9 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.059 | 0.43 | 0.57 | 0.00 | 9.15 | 22.4/33.5 | 26.4/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nino Niederreiter: 1+ assists NO | 79 | 0.875 | 0.830 | +0.073 | +0.028 | $5.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.792 | 0.778 | +0.039 | +0.024 | $5.60 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ goals NO | 65 | 0.702 | 0.688 | +0.036 | +0.022 | $4.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Nino Niederreiter: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4|no; why: higher confidence-adjusted growth (11.07 vs 0.13 bp); wins across more scripts (relative breadth 1.006 vs 0.896); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: WPG offense succeeds (4+ goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (7.09 vs 4.70 bp); relationships: KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no; why: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.84 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4051): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3726): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.4041): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3743, phi -0.178)
- KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3726, phi -0.209)
- KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3726, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.84 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.40 (adj +0.42) on $13.64, P(profit) 0.6383, adj growth 4.1 bp · B EV +1.04 (adj +0.53) on $15.68, P(profit) 0.4839, adj growth 5.1 bp · C EV +0.68 (adj +0.42) on $10.72, P(profit) 0.7922, adj growth 4.0 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7922, adj growth 2.5 bp

## SJS @ NSH  ·  10000 joint draws  ·  452 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.04 | 27.9/27.9 | 24.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 6.01 | 27.7/27.7 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.29 | 29.3/29.2 | 23.4/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.58 | 0.42 | 0.00 | 5.97 | 32.2/22.0 | 18.9/28.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.50 | 0.50 | 0.00 | 6.0 | 22.3/32.8 | 29.1/18.9 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.47 | 5.86 | 32.6/22.4 | 19.4/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jayden Struble: 1+ goals NO | 94 | 0.962 | 0.955 | +0.018 | +0.011 | $6.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Juuse Saros: 26+ saves NO | 52 | 0.606 | 0.560 | +0.068 | +0.023 | $4.01 | FUNDED_RESEARCH | $2 | NSH:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ goals YES | 21 | 0.252 | 0.241 | +0.031 | +0.019 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.786 | 0.717 | +0.081 | +0.012 | $4.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Jayden Struble: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense succeeds (4+ goals)
- **Juuse Saros: 26+ saves NO** — thesis: NSH net faces light volume (<= 25 shots; SJS suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT15SJNSH-NSHJSTRUBLE47-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.055); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: NSH net faces heavy volume (33+ shots; SJS pressure)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (4.51 vs 0.71 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15SJNSH-NSHJSTRUBLE47-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: MOSTLY_INDEPENDENT (phi 0.055); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: Player prop expression KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no selected over player prop KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.90 vs 0.75 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT15SJNSH-NSHJSTRUBLE47-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:NET_LOW_VOLUME (p 0.3789): highest fidelity KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3851): highest fidelity KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no — Player prop expression KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no selected over player prop KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.90 vs 0.75 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- KXNHLGOAL-26OCT15SJNSH-NSHJSTRUBLE47-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.4364, phi -0.081)
- KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NSH:NET_HIGH_VOLUME (p 0.1967, phi -0.543)
- KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3851, phi -0.221)
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.395, phi -0.204)
- override: Player prop expression KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no selected over player prop KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.90 vs 0.75 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +2.39 (adj +0.51) on $13.64, P(profit) 0.6534, adj growth 4.9 bp · B EV +1.38 (adj +0.48) on $16.71, P(profit) 0.5585, adj growth 4.6 bp · C EV +1.71 (adj +0.59) on $20.66, P(profit) 0.5585, adj growth 5.6 bp · R EV +0.25 (adj +0.09) on $2.00, P(profit) 0.6059, adj growth 3.2 bp

## STL @ MIN  ·  10000 joint draws  ·  460 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.58 | 0.42 | 0.00 | 6.04 | 27.7/27.4 | 23.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.46 | 5.99 | 27.7/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.58 | 0.42 | 0.00 | 9.3 | 29.3/29.1 | 23.3/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.9 | 19.2/28.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.53 | 0.47 | 0.48 | 5.93 | 32.7/22.1 | 18.9/29.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.21 | 34.7/23.4 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 10 | 0.136 | 0.123 | +0.029 | +0.017 | $1.50 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.138 | 0.122 | +0.032 | +0.016 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 19 | 0.232 | 0.219 | +0.032 | +0.018 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 2+ assists NO | 74 | 0.799 | 0.767 | +0.046 | +0.014 | $6.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (6.28 vs 4.60 bp); despite a smaller raw edge (+0.029 vs +0.032/contract); relationships: KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: MIN offense suppressed (<= 2 goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (5.93 vs 4.60 bp); relationships: KXNHLGOAL-26OCT15STLMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no: INTENTIONAL_DIVERSIFIER (phi -0.058); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (4.60 vs 2.90 bp); despite a smaller raw edge (+0.032 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15STLMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 2+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (2.25 vs 1.37 bp); relationships: KXNHLGOAL-26OCT15STLMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.058); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3552): highest fidelity KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3426): highest fidelity KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no (same contract)
- KXNHLGOAL-26OCT15STLMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.151)
- KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.153)
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.209)
- KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4345, phi -0.342)

portfolios: A EV +1.78 (adj +0.59) on $13.64, P(profit) 0.692, adj growth 5.4 bp · B EV +1.57 (adj +0.76) on $11.66, P(profit) 0.3837, adj growth 7.3 bp · C EV +1.19 (adj +0.55) on $12.43, P(profit) 0.4092, adj growth 5.2 bp · R EV +0.28 (adj +0.16) on $1.00, P(profit) 0.1356, adj growth 5.4 bp

## UTA @ EDM  ·  10000 joint draws  ·  472 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.01 | 27.6/27.5 | 24.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 9.48 | 29.4/29.4 | 24.0/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 6.03 | 28.0/27.8 | 24.5/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.07 | 32.5/22.0 | 19.3/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 9.5 | 34.3/23.3 | 18.6/26.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.55 | 0.45 | 0.47 | 5.97 | 32.8/22.2 | 19.1/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 16 | 0.216 | 0.200 | +0.047 | +0.030 | $2.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 69 | 0.803 | 0.726 | +0.098 | +0.021 | $6.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 31 | 0.355 | 0.343 | +0.030 | +0.018 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ goals YES | 43 | 0.470 | 0.459 | +0.023 | +0.012 | $1.66 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.61) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (13.85 vs 6.78 bp); despite a smaller raw edge (+0.047 vs +0.114/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (4.81 vs 3.63 bp); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.222); KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.49 vs 0.60 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.222); KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.61 vs 0.18 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.499): highest fidelity KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes — Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.49 vs 0.60 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis EDM:WINS (p 0.5762): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.3659): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.201)
- KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.499, phi -0.319)
- KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.264)
- KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 38% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.3)
- override: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.49 vs 0.60 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.61 vs 0.18 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.33 (adj +0.75) on $13.64, P(profit) 0.638, adj growth 7.1 bp · B EV +2.07 (adj +0.91) on $13.96, P(profit) 0.4092, adj growth 8.7 bp · C EV +4.07 (adj +1.23) on $20.66, P(profit) 0.4345, adj growth 11.8 bp · R EV +0.05 (adj +0.03) on $1.00, P(profit) 0.4705, adj growth 1.0 bp

## CGY @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.730 / away 0.270

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.73 | 0.27 | 0.00 | 6.03 | 28.5/28.0 | 25.5/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.115 | 0.81 | 0.19 | 0.00 | 6.0 | 33.8/22.0 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.46 | 5.89 | 28.4/27.8 | 24.4/24.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.60 | 0.40 | 0.44 | 5.88 | 33.8/22.4 | 19.4/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 9.23 | 29.9/29.3 | 24.3/22.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.080 | 0.80 | 0.20 | 0.00 | 9.2 | 35.6/23.2 | 19.4/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.740 | 0.724 | +0.045 | +0.029 | $5.01 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 64 | 0.777 | 0.685 | +0.120 | +0.028 | $5.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Carter Hart: 21+ saves YES | 55 | 0.672 | 0.583 | +0.105 | +0.016 | $2.68 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:NET_HIGH_VOLUME | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Vegas wins 3rd Period by over 1.5 goals NO | 70 | 0.788 | 0.728 | +0.074 | +0.013 | $2.72 | FUNDED_RESEARCH | $1 | CGY:WINS | DIRECT (0.97) | EVIDENCE_THIN | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (8.45 vs 2.51 bp); relationships: KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no: MOSTLY_INDEPENDENT (phi 0.111); failure: VGK offense succeeds (4+ goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (7.88 vs 2.51 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no: MOSTLY_INDEPENDENT (phi 0.088); failure: VGK offense succeeds (4+ goals)
- **Carter Hart: 21+ saves YES** — thesis: VGK net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no: MOSTLY_INDEPENDENT (phi -0.033); failure: VGK net faces light volume (<= 25 shots; CGY suppressed)
- **Vegas wins 3rd Period by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (1.81 vs 0.37 bp); despite a smaller raw edge (+0.074 vs +0.107/contract); evidence EVIDENCE_THIN vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:SUPPRESSED (p 0.2881): highest fidelity KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:NET_HIGH_VOLUME (p 0.1388): highest fidelity KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21|yes (same contract)
- thesis CGY:WINS (p 0.3302): highest fidelity KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no [DIRECT], best adjusted EV KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no (same contract)
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.21)
- KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.212)
- KXNHLSAVE-26OCT15CGYVGK-VGKCHART79-21|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis VGK:NET_LOW_VOLUME (p 0.48, phi -0.625)
- KXNHL3PSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4435, phi -0.43)

portfolios: A EV +1.78 (adj +0.36) on $13.64, P(profit) 0.8284, adj growth 3.5 bp · B EV +2.02 (adj +0.55) on $15.43, P(profit) 0.7257, adj growth 5.3 bp · C EV +1.51 (adj +0.32) on $13.82, P(profit) 0.7967, adj growth 3.1 bp · R EV +0.23 (adj +0.10) on $3.00, P(profit) 0.6032, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
