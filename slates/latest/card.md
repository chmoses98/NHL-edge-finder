# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T12:09:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.20 | +11.05 | +23.58 | 0.680 | -37.19 | -52.59 | 97.20 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +23.03 | +11.27 | +19.88 | 0.677 | -32.50 | -45.11 | 102.28 |
| C best expression per thesis | 136.42 | +17.10 | +7.46 | +13.66 | 0.643 | -37.28 | -48.13 | 65.42 |
| R FUNDED research stakes | 33.00 | +4.25 | +1.84 | +2.47 | 0.616 | -7.87 | -10.88 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_CHI_win | p_overtime | goals | shots BOS/CHI | BOS/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.75 | 0.25 | 0.00 | 6.06 | 27.0/26.5 | 24.1/22.4 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.117 | 0.78 | 0.22 | 0.00 | 6.04 | 32.4/21.0 | 18.8/27.0 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.092 | 0.81 | 0.19 | 0.00 | 9.34 | 34.1/22.5 | 18.5/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.56 | 0.44 | 0.48 | 5.91 | 26.9/26.5 | 23.4/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.73 | 0.27 | 0.00 | 9.38 | 28.8/28.4 | 23.7/21.0 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.60 | 0.40 | 0.48 | 5.96 | 32.4/21.4 | 18.3/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $5.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.149 | 0.132 | +0.032 | +0.015 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.265 | 0.250 | +0.033 | +0.018 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 76 | 0.794 | 0.784 | +0.021 | +0.011 | $8.63 | FUNDED_RESEARCH | $3 | CHI:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31CHIBOS-7|yes; why: higher confidence-adjusted growth (12.42 vs 0.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.684); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: BOS offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (4.46 vs 3.95 bp); despite a smaller raw edge (+0.032 vs +0.033/contract); relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31CHIBOS-7|yes; why: higher confidence-adjusted growth (3.95 vs 0.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.684); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CHI offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no; why: Player prop expression KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, BOS shot control · normal event (5-7) · decided (2+) 0.12, BOS shot control · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.281): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.51): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.5414): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2565, phi -0.182)
- KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.208)
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.276)
- KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.281, phi -0.196)
- override: Player prop expression KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.19 (adj +1.56) on $18.34, P(profit) 0.4216, adj growth 14.2 bp · B EV +2.85 (adj +1.66) on $20.44, P(profit) 0.4683, adj growth 15.1 bp · C EV +1.13 (adj +0.61) on $18.02, P(profit) 0.265, adj growth 5.3 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.7937, adj growth 1.5 bp

## STL @ DET  ·  10000 joint draws  ·  378 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_STL_win | p_overtime | goals | shots DET/STL | DET/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.48 | 0.52 | 0.00 | 5.99 | 27.5/27.2 | 23.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.51 | 5.93 | 27.5/27.2 | 23.9/24.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.100 | 0.52 | 0.48 | 0.00 | 5.99 | 32.4/21.3 | 18.0/28.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.48 | 5.92 | 32.6/21.8 | 18.5/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.47 | 0.53 | 0.00 | 9.24 | 29.1/28.7 | 22.4/23.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 9.13 | 34.3/22.9 | 17.8/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| J.T. Compher: 1+ goals YES | 11 | 0.154 | 0.137 | +0.037 | +0.020 | $3.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 7 | 0.105 | 0.090 | +0.030 | +0.015 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 35 | 0.408 | 0.393 | +0.043 | +0.027 | $7.08 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.329 | 0.316 | +0.035 | +0.021 | $5.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (8.50 vs 6.70 bp); despite a smaller raw edge (+0.038 vs +0.043/contract); relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: DET offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (7.11 vs 6.70 bp); despite a smaller raw edge (+0.030 vs +0.043/contract); relationships: KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (6.70 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: DET offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes; why: higher confidence-adjusted growth (4.86 vs 0.57 bp); despite a smaller raw edge (+0.035 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3659): highest fidelity KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3777): highest fidelity KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes (same contract)
- KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.18)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.171)
- KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.316)
- KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.287)

portfolios: A EV +3.71 (adj +2.06) on $17.59, P(profit) 0.3407, adj growth 18.5 bp · B EV +3.49 (adj +1.97) on $18.06, P(profit) 0.5489, adj growth 17.8 bp · C EV +2.12 (adj +1.32) on $18.00, P(profit) 0.6067, adj growth 11.5 bp · R EV +0.23 (adj +0.15) on $2.00, P(profit) 0.4085, adj growth 5.3 bp

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_TBL_win | p_overtime | goals | shots NSH/TBL | NSH/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 6.0 | 27.3/27.8 | 24.2/23.6 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.111 | 0.40 | 0.60 | 0.00 | 5.97 | 21.6/33.3 | 29.0/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.48 | 5.96 | 27.5/28.0 | 24.7/24.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.44 | 0.56 | 0.48 | 5.88 | 22.0/33.6 | 30.2/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.46 | 0.54 | 0.00 | 9.29 | 29.1/29.5 | 23.5/23.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 9.22 | 22.9/35.0 | 27.6/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $13.40 | FUNDED_RESEARCH | $4 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan O'Reilly: 1+ goals YES | 27 | 0.313 | 0.299 | +0.029 | +0.015 | $2.84 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (4.09 vs 2.18 bp); relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: TBL wins by 2+
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TBNSH-TB3|no has the higher standalone adjusted growth (4.09 vs 2.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)

portfolios: A EV +1.52 (adj +0.55) on $18.34, P(profit) 0.7148, adj growth 4.9 bp · B EV +1.28 (adj +0.48) on $16.24, P(profit) 0.8091, adj growth 4.4 bp · C EV +1.48 (adj +0.49) on $20.00, P(profit) 0.8091, adj growth 4.4 bp · R EV +0.30 (adj +0.10) on $4.00, P(profit) 0.8091, adj growth 3.6 bp

## EDM @ NYI  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_EDM_win | p_overtime | goals | shots NYI/EDM | NYI/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.49 | 0.51 | 0.00 | 6.05 | 27.7/27.7 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.45 | 0.56 | 0.00 | 9.46 | 29.2/29.2 | 22.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.46 | 5.98 | 27.7/27.6 | 24.1/24.3 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 6.06 | 32.4/21.9 | 18.6/28.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.063 | 0.38 | 0.62 | 0.00 | 6.03 | 22.2/32.1 | 27.9/19.3 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.44 | 5.88 | 32.3/21.6 | 18.5/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mattias Ekholm: 1+ goals YES | 7 | 0.123 | 0.105 | +0.049 | +0.030 | $4.57 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.182 | 0.160 | +0.055 | +0.033 | $5.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 22 | 0.274 | 0.257 | +0.042 | +0.025 | $5.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 17 | 0.214 | 0.195 | +0.034 | +0.015 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (27.97 vs 2.55 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.822 vs 0.368); relationships: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: EDM offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (20.90 vs 7.36 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes has the higher standalone adjusted growth (20.90 vs 7.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes has the higher standalone adjusted growth (20.90 vs 3.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4191): highest fidelity KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4481): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-9|yes [FRAGILE], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3296): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-9|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes (same contract)
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.156)
- KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.212)
- KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.226)
- KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.225)

portfolios: A EV +6.19 (adj +3.33) on $18.34, P(profit) 0.4268, adj growth 29.2 bp · B EV +6.83 (adj +4.09) on $18.09, P(profit) 0.4749, adj growth 36.7 bp · C EV +4.03 (adj +2.27) on $10.69, P(profit) 0.3612, adj growth 19.4 bp · R EV +1.30 (adj +0.81) on $2.00, P(profit) 0.1232, adj growth 26.6 bp

## BUF @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 6.0 | 27.9/27.9 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.51 | 0.49 | 0.45 | 5.89 | 28.1/27.8 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.21 | 29.4/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.03 | 32.6/22.3 | 19.3/28.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.064 | 0.52 | 0.48 | 0.00 | 5.99 | 22.5/32.7 | 29.1/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.48 | 5.97 | 33.0/22.4 | 19.1/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 2.5 goals NO | 80 | 0.863 | 0.829 | +0.052 | +0.018 | $13.89 | FUNDED_RESEARCH | $4 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Corey Perry: 1+ goals YES | 14 | 0.183 | 0.165 | +0.034 | +0.016 | $2.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.013 | $2.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Andre Lee: 1+ goals YES | 10 | 0.131 | 0.117 | +0.025 | +0.011 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Buffalo wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (4.54 vs 2.54 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.076); failure: BUF wins by 2+
- **Corey Perry: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 4.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.091); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 3.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.091); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: LAK offense suppressed (<= 2 goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 2.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.076); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.076); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:WINS (p 0.5431): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- KXNHLSPREAD-26OCT31BUFLA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2349, phi -0.719)
- KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.18)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.183)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.162)

portfolios: A EV +2.13 (adj +0.85) on $18.34, P(profit) 0.2901, adj growth 7.7 bp · B EV +2.32 (adj +1.00) on $20.69, P(profit) 0.378, adj growth 9.2 bp · C EV +1.27 (adj +0.44) on $20.00, P(profit) 0.8629, adj growth 4.0 bp · R EV +0.25 (adj +0.09) on $4.00, P(profit) 0.8629, adj growth 3.3 bp

## OTT @ SJS  ·  10000 joint draws  ·  432 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.49 | 0.51 | 0.00 | 6.03 | 27.0/27.3 | 23.7/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 6.01 | 27.1/27.5 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.44 | 28.6/28.8 | 22.6/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.091 | 0.46 | 0.54 | 0.00 | 6.03 | 21.5/32.4 | 28.6/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.44 | 0.56 | 0.44 | 5.89 | 21.6/32.6 | 28.9/18.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.064 | 0.45 | 0.55 | 0.00 | 9.37 | 22.9/33.9 | 26.9/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ MTL  ·  10000 joint draws  ·  432 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.05 | 27.1/27.4 | 24.0/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.56 | 0.44 | 0.00 | 9.37 | 28.9/29.1 | 23.4/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.47 | 5.96 | 27.2/27.7 | 24.3/23.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.50 | 0.50 | 0.00 | 6.06 | 21.7/32.6 | 28.9/18.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.49 | 0.51 | 0.46 | 5.98 | 21.9/32.4 | 29.1/18.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.064 | 0.50 | 0.50 | 0.00 | 9.3 | 23.3/34.7 | 28.0/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.166 | 0.145 | +0.038 | +0.018 | $3.17 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31PITMTL-PIT6|yes; why: higher confidence-adjusted growth (6.33 vs 0.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.867 vs 0.307); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.374, phi -0.199)

portfolios: A EV +1.20 (adj +0.57) on $4.02, P(profit) 0.1656, adj growth 5.0 bp · B EV +0.95 (adj +0.45) on $3.17, P(profit) 0.1656, adj growth 4.1 bp · C EV +1.37 (adj +0.65) on $4.57, P(profit) 0.1656, adj growth 5.6 bp · R EV +0.30 (adj +0.14) on $1.00, P(profit) 0.1656, adj growth 5.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  400 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_TOR_win | p_overtime | goals | shots VAN/TOR | VAN/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.05 | 28.3/28.4 | 24.9/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.47 | 5.96 | 28.5/28.7 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 9.38 | 29.9/30.0 | 23.7/23.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.47 | 0.53 | 0.00 | 6.06 | 22.3/33.3 | 29.2/19.0 | even strength |
| TOR shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.46 | 0.54 | 0.47 | 6.0 | 22.9/33.4 | 30.1/19.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 6.05 | 33.0/22.8 | 19.6/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 73 | 0.821 | 0.773 | +0.077 | +0.029 | $13.89 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gavin McKenna: 1+ goals NO | 74 | 0.784 | 0.768 | +0.031 | +0.015 | $8.72 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 22 | 0.269 | 0.244 | +0.037 | +0.013 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 17 | 0.211 | 0.191 | +0.031 | +0.011 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Toronto wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (9.91 vs 4.87 bp); wins across more scripts (relative breadth 1.029 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.112); failure: TOR wins by 2+
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR3|no has the higher standalone adjusted growth (9.91 vs 2.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.139); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: TOR offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR3|no has the higher standalone adjusted growth (9.91 vs 1.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.120); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: Player prop expression KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes selected over broad KXNHLSPREAD-26OCT31TORVAN-VAN2|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.34 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS (p 0.4991): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- KXNHLSPREAD-26OCT31TORVAN-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2836, phi -0.742)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.209)
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)
- override: Player prop expression KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes selected over broad KXNHLSPREAD-26OCT31TORVAN-VAN2|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.34 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.76 (adj +0.83) on $18.34, P(profit) 0.5523, adj growth 7.2 bp · B EV +2.44 (adj +0.93) on $26.41, P(profit) 0.7378, adj growth 8.7 bp · C EV +2.08 (adj +0.79) on $20.00, P(profit) 0.8211, adj growth 7.3 bp · R EV +0.54 (adj +0.22) on $7.00, P(profit) 0.6658, adj growth 8.0 bp

## CBJ @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.56 | 0.44 | 0.00 | 6.0 | 26.0/25.9 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.9 | 26.5/26.2 | 22.8/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.090 | 0.62 | 0.38 | 0.00 | 5.91 | 31.0/20.5 | 17.6/26.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.55 | 0.45 | 0.49 | 5.85 | 30.8/20.8 | 17.6/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.57 | 0.43 | 0.00 | 9.26 | 28.1/27.7 | 22.2/21.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.54 | 0.46 | 0.47 | 2.84 | 24.6/24.4 | 22.9/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Columbus over 3.5 goals scored YES | 26 | 0.327 | 0.288 | +0.053 | +0.015 | $2.45 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 74 | 0.805 | 0.768 | +0.052 | +0.014 | $8.92 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus over 3.5 goals scored YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no; why: higher confidence-adjusted growth (2.44 vs 2.38 bp); relationships: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: REINFORCING (phi 0.297); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no; why: higher confidence-adjusted growth (2.38 vs 1.78 bp); despite a smaller raw edge (+0.052 vs +0.054/contract); wins across more scripts (relative breadth 0.993 vs 0.884); relationships: KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes: REINFORCING (phi 0.297); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes (same contract)
- thesis GAME:TIGHT (p 0.4546): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.65)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3096, phi -0.734)

portfolios: A EV +2.09 (adj +0.57) on $18.34, P(profit) 0.3268, adj growth 4.7 bp · B EV +1.09 (adj +0.30) on $11.37, P(profit) 0.8053, adj growth 2.8 bp · C EV +1.57 (adj +0.43) on $16.37, P(profit) 0.8053, adj growth 3.8 bp · R EV +0.40 (adj +0.11) on $4.00, P(profit) 0.3183, adj growth 3.9 bp

## CGY @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.151 | 0.80 | 0.20 | 0.00 | 6.04 | 35.8/22.7 | 20.5/30.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.122 | 0.82 | 0.18 | 0.00 | 9.38 | 37.7/24.0 | 20.1/28.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.61 | 0.39 | 0.47 | 5.92 | 36.2/23.1 | 20.0/32.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.77 | 0.23 | 0.00 | 6.06 | 29.8/28.8 | 26.4/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.77 | 0.23 | 0.00 | 9.43 | 31.3/30.2 | 25.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.48 | 5.95 | 30.0/29.3 | 26.1/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary over 3.5 goals scored YES | 21 | 0.280 | 0.237 | +0.058 | +0.016 | $1.89 | FUNDED_RESEARCH | $1 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 1.5 goals NO | 41 | 0.521 | 0.446 | +0.094 | +0.018 | $1.01 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary over 1.5 goals scored YES | 64 | 0.736 | 0.670 | +0.080 | +0.014 | $4.97 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Colorado over 5.5 goals scored NO | 75 | 0.807 | 0.774 | +0.044 | +0.011 | $7.65 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (3.08 vs 3.06 bp); despite a smaller raw edge (+0.058 vs +0.094/contract); relationships: KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.424); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: DUPLICATIVE (phi 0.373); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: MOSTLY_INDEPENDENT (phi -0.02); failure: CGY offense suppressed (<= 2 goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: higher confidence-adjusted growth (3.06 vs 1.93 bp); relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: REINFORCING (phi 0.424); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: REINFORCING (phi 0.417); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: REINFORCING (phi 0.415); failure: COL wins by 2+
- **Calgary over 1.5 goals scored YES** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (3.08 vs 1.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.373); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: DUPLICATIVE (phi 0.373); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.417); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: MOSTLY_INDEPENDENT (phi -0.047); failure: CGY offense suppressed (<= 2 goals)
- **Colorado over 5.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (3.08 vs 1.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.020); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.415); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: high-event game (8+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CGY:OFFENSE_4PLUS (p 0.2704): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.1381): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis CGY:WINS (p 0.2997): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.637)
- KXNHLSPREAD-26OCT31CGYCOL-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.6 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4794, phi -1.0)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.586)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.3121, phi -0.577)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes kept

portfolios: A EV +3.40 (adj +0.73) on $18.34, P(profit) 0.5595, adj growth 5.9 bp · B EV +1.76 (adj +0.39) on $15.53, P(profit) 0.6431, adj growth 3.6 bp · C EV +2.05 (adj +0.46) on $8.77, P(profit) 0.5595, adj growth 4.0 bp · R EV +0.84 (adj +0.18) on $6.00, P(profit) 0.5138, adj growth 6.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
