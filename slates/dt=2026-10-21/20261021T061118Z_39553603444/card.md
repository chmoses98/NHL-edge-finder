# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T06:11:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 60.00 | +3.61 | +1.10 | +18.22 | 0.615 | -33.11 | -33.11 | 8.84 |
| B thesis-diversified (joint) ← optimiser card | 37.88 | +2.20 | +0.69 | +10.32 | 0.689 | -19.58 | -19.58 | 6.13 |
| C best expression per thesis | 33.61 | +1.93 | +0.60 | +8.78 | 0.689 | -15.31 | -15.31 | 5.47 |
| R FUNDED research stakes | 11.00 | +0.65 | +0.20 | +3.12 | 0.689 | -5.62 | -5.62 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.118 | 0.65 | 0.35 | 0.00 | 5.99 | 32.4/20.9 | 18.1/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.59 | 0.41 | 0.00 | 6.02 | 26.9/26.3 | 23.2/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.45 | 5.91 | 27.4/26.7 | 23.4/24.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.56 | 0.44 | 0.45 | 5.84 | 32.2/21.1 | 17.9/29.0 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.068 | 0.67 | 0.33 | 0.00 | 9.14 | 33.6/22.0 | 17.4/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.56 | 0.44 | 0.00 | 9.18 | 28.6/28.1 | 22.2/22.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 2.5 goals NO | 73 | 0.788 | 0.757 | +0.044 | +0.013 | $13.61 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no; why: higher confidence-adjusted growth (1.87 vs 0.83 bp); despite a smaller raw edge (+0.044 vs +0.047/contract); wins across more scripts (relative breadth 0.988 vs 0.859); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BUF wins by 2+

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.4498): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF3|no (same contract)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -0.741)

portfolios: A EV +1.19 (adj +0.34) on $20.00, P(profit) 0.7881, adj growth 2.8 bp · B EV +0.81 (adj +0.23) on $13.61, P(profit) 0.7881, adj growth 2.1 bp · C EV +0.81 (adj +0.23) on $13.61, P(profit) 0.7881, adj growth 2.1 bp · R EV +0.24 (adj +0.07) on $4.00, P(profit) 0.7881, adj growth 2.4 bp

## FLA @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.61 | 0.39 | 0.00 | 6.01 | 26.6/26.3 | 23.4/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.92 | 26.6/26.5 | 23.2/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.088 | 0.67 | 0.33 | 0.00 | 5.94 | 31.2/20.7 | 18.2/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.62 | 0.38 | 0.00 | 9.12 | 28.1/27.9 | 22.7/21.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.46 | 5.88 | 31.7/21.1 | 18.0/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.58 | 0.42 | 0.00 | 3.45 | 25.3/25.2 | 23.6/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 82 | 0.877 | 0.846 | +0.046 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 72 | 0.782 | 0.748 | +0.048 | +0.014 | $4.27 | FUNDED_RESEARCH | $2 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (3.77 vs 2.30 bp); despite a smaller raw edge (+0.046 vs +0.048/contract); relationships: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: DUPLICATIVE (phi 0.71); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.77 vs 2.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.710); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: DUPLICATIVE (phi 0.71); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:WINS (p 0.5747): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA3|no (same contract)
- KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -0.71)
- KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -1.0)

portfolios: A EV +2.42 (adj +0.76) on $40.00, P(profit) 0.7818, adj growth 6.0 bp · B EV +1.39 (adj +0.46) on $24.27, P(profit) 0.7818, adj growth 4.1 bp · C EV +1.12 (adj +0.37) on $20.00, P(profit) 0.8767, adj growth 3.4 bp · R EV +0.41 (adj +0.13) on $7.00, P(profit) 0.7818, adj growth 4.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
