# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T11:27:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +7.77 | +1.70 | +7.98 | 0.706 | -40.40 | -40.40 | 11.70 |
| B thesis-diversified (joint) ← optimiser card | 34.43 | +5.06 | +1.05 | +17.16 | 0.576 | -12.44 | -34.43 | 9.26 |
| C best expression per thesis | 34.71 | +5.08 | +1.06 | +17.31 | 0.576 | -12.29 | -34.71 | 9.32 |
| R FUNDED research stakes | 4.00 | +0.36 | +0.12 | +2.10 | 0.715 | -4.00 | -4.00 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  406 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_LAK_win | p_overtime | goals | shots NYR/LAK | NYR/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.53 | 0.47 | 0.48 | 5.91 | 27.1/27.5 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 5.96 | 27.1/27.4 | 24.3/23.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.089 | 0.52 | 0.48 | 0.00 | 6.03 | 21.7/32.4 | 28.7/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.12 | 28.5/28.8 | 23.3/22.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.47 | 5.81 | 22.0/33.0 | 29.9/18.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.58 | 0.42 | 0.00 | 3.52 | 26.2/26.1 | 24.5/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 66 | 0.803 | 0.697 | +0.127 | +0.021 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (4.52 vs 0.25 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4602): highest fidelity KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no (same contract)
- KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3162, phi -0.197)

portfolios: A EV +3.76 (adj +0.63) on $20.00, P(profit) 0.8027, adj growth 5.6 bp · B EV +3.76 (adj +0.63) on $20.00, P(profit) 0.8027, adj growth 5.6 bp · C EV +3.76 (adj +0.63) on $20.00, P(profit) 0.8027, adj growth 5.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_TOR_win | p_overtime | goals | shots CGY/TOR | CGY/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.02 | 30.2/29.7 | 26.0/26.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.97 | 30.1/29.7 | 26.4/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.49 | 0.51 | 0.00 | 9.34 | 31.5/31.3 | 24.9/25.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.094 | 0.56 | 0.44 | 0.00 | 6.03 | 35.6/23.8 | 20.6/31.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.54 | 0.46 | 0.48 | 5.97 | 35.9/24.3 | 21.1/32.4 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.064 | 0.53 | 0.47 | 0.00 | 9.31 | 37.6/25.4 | 19.9/30.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 1.5 goals NO | 64 | 0.715 | 0.675 | +0.059 | +0.019 | $14.43 | FUNDED_RESEARCH | $4 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (3.50 vs 1.33 bp); relationships: only recommended bet in this game; failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CGY:WINS (p 0.4983): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3803): highest fidelity KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT26TORCGY-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2848, phi -1.0)

portfolios: A EV +4.01 (adj +1.07) on $50.00, P(profit) 0.5741, adj growth 6.1 bp · B EV +1.30 (adj +0.42) on $14.43, P(profit) 0.7152, adj growth 3.7 bp · C EV +1.32 (adj +0.43) on $14.71, P(profit) 0.7152, adj growth 3.7 bp · R EV +0.36 (adj +0.12) on $4.00, P(profit) 0.7152, adj growth 4.0 bp

## DET @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.72 | 0.28 | 0.00 | 6.05 | 27.9/27.7 | 25.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.72 | 0.28 | 0.00 | 9.39 | 29.4/29.4 | 24.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.56 | 0.44 | 0.46 | 6.04 | 27.8/27.9 | 24.6/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.087 | 0.75 | 0.25 | 0.00 | 6.03 | 32.9/22.1 | 19.8/27.8 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.78 | 0.22 | 0.00 | 9.43 | 34.4/23.6 | 19.3/25.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.60 | 0.40 | 0.47 | 5.96 | 32.8/22.2 | 19.1/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
