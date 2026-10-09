# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T12:28:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 71.61 | +8.26 | +4.40 | -4.66 | 0.455 | -46.05 | -46.05 | 32.73 |
| B thesis-diversified (joint) ← optimiser card | 39.58 | +4.23 | +2.31 | -2.39 | 0.446 | -20.92 | -26.77 | 20.06 |
| C best expression per thesis | 16.45 | +2.34 | +1.38 | -3.56 | 0.248 | -16.45 | -16.45 | 11.97 |
| R FUNDED research stakes | 9.00 | +0.91 | +0.53 | -0.64 | 0.248 | -5.76 | -9.00 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  398 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SEA_win | p_overtime | goals | shots DET/SEA | DET/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.01 | 27.7/27.3 | 23.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.91 | 28.0/27.4 | 24.2/24.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 5.98 | 33.1/21.6 | 18.6/29.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.47 | 5.92 | 33.4/21.9 | 18.7/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.51 | 0.49 | 0.00 | 9.37 | 29.5/29.2 | 23.1/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 9.17 | 34.9/23.3 | 18.0/28.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ WSH  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NYR_win | p_overtime | goals | shots WSH/NYR | WSH/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.04 | 26.7/26.4 | 23.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.91 | 26.7/26.5 | 23.1/23.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.62 | 0.38 | 0.00 | 5.96 | 31.5/20.9 | 18.0/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.56 | 0.44 | 0.00 | 9.31 | 28.1/28.0 | 22.5/21.6 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.55 | 0.46 | 0.44 | 5.91 | 31.9/21.3 | 18.1/28.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.063 | 0.62 | 0.38 | 0.00 | 9.28 | 33.3/22.2 | 17.3/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 19 | 0.248 | 0.230 | +0.047 | +0.029 | $8.48 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 14 | 0.169 | 0.159 | +0.021 | +0.011 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT09NYRWSH-7|yes; why: higher confidence-adjusted growth (11.30 vs 0.60 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.679); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.30 vs 1.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4179): highest fidelity KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.237)
- KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.17)

portfolios: A EV +4.30 (adj +2.57) on $20.78, P(profit) 0.3741, adj growth 19.6 bp · B EV +2.40 (adj +1.44) on $11.42, P(profit) 0.3741, adj growth 12.4 bp · C EV +2.00 (adj +1.23) on $8.50, P(profit) 0.248, adj growth 10.6 bp · R EV +0.71 (adj +0.43) on $3.00, P(profit) 0.248, adj growth 14.0 bp

## PIT @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PIT_win | p_overtime | goals | shots CBJ/PIT | CBJ/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.59 | 0.41 | 0.00 | 6.02 | 27.5/27.4 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.53 | 0.47 | 0.46 | 5.98 | 27.8/27.8 | 24.4/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.60 | 0.40 | 0.00 | 9.32 | 29.1/29.0 | 23.3/22.1 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 6.01 | 32.3/21.9 | 19.2/27.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.52 | 0.48 | 0.00 | 6.05 | 22.0/32.6 | 28.9/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.48 | 0.52 | 0.51 | 5.88 | 21.9/32.3 | 28.9/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Danton Heinen: 1+ goals YES | 11 | 0.144 | 0.128 | +0.027 | +0.011 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Kent Johnson: 1+ goals NO | 77 | 0.805 | 0.795 | +0.022 | +0.013 | $14.60 | FUNDED_RESEARCH | $4 | CBJ:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (2.71 vs 0.62 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Kent Johnson: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (2.00 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.4501): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CBJ:SUPPRESSED (p 0.3355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.154)
- KXNHLGOAL-26OCT09PITCBJ-CBJKJOHNSON91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4501, phi -0.203)

portfolios: A EV +2.40 (adj +1.07) on $27.77, P(profit) 0.1443, adj growth 7.6 bp · B EV +1.09 (adj +0.51) on $17.45, P(profit) 0.8313, adj growth 4.5 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.11 (adj +0.06) on $4.00, P(profit) 0.8048, adj growth 2.2 bp

## ANA @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_ANA_win | p_overtime | goals | shots WPG/ANA | WPG/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.56 | 0.44 | 0.00 | 6.0 | 27.9/28.2 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.48 | 5.95 | 28.0/28.4 | 25.0/24.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.50 | 0.50 | 0.00 | 6.03 | 22.2/33.7 | 29.9/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.55 | 0.45 | 0.00 | 9.25 | 29.6/30.1 | 24.0/23.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.50 | 5.9 | 22.4/33.8 | 30.6/19.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.060 | 0.50 | 0.50 | 0.00 | 9.3 | 23.8/35.5 | 28.7/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Morgan Barron: 1+ goals YES | 13 | 0.158 | 0.148 | +0.020 | +0.010 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cutter Gauthier: 1+ goals NO | 60 | 0.643 | 0.629 | +0.027 | +0.012 | $7.90 | FUNDED_RESEARCH | $2 | ANA:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (1.93 vs 0.04 bp); despite a smaller raw edge (+0.020 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: WPG offense suppressed (<= 2 goals)
- **Cutter Gauthier: 1+ goals NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-ANALCARLSSON91-1|no; why: higher confidence-adjusted growth (1.33 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:SUPPRESSED (p 0.4004): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.4151): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3725, phi -0.179)
- KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.3835, phi -0.279)

portfolios: A EV +1.56 (adj +0.76) on $23.06, P(profit) 0.6987, adj growth 5.6 bp · B EV +0.74 (adj +0.36) on $10.71, P(profit) 0.6987, adj growth 3.2 bp · C EV +0.34 (adj +0.15) on $7.95, P(profit) 0.6434, adj growth 1.4 bp · R EV +0.09 (adj +0.04) on $2.00, P(profit) 0.6434, adj growth 1.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
