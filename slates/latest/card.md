# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T06:39:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +5.43 | +1.58 | +6.03 | 0.669 | -41.23 | -47.98 | 10.11 |
| B thesis-diversified (joint) ← optimiser card | 31.54 | +2.31 | +0.70 | +10.52 | 0.580 | -12.60 | -28.35 | 6.21 |
| C best expression per thesis | 30.34 | +2.23 | +0.69 | +12.30 | 0.580 | -11.39 | -30.33 | 6.08 |
| R FUNDED research stakes | 10.00 | +0.77 | +0.23 | +2.48 | 0.669 | -4.25 | -8.80 | 0.00 |

## FLA @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_FLA_win | p_overtime | goals | shots BUF/FLA | BUF/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.63 | 0.37 | 0.00 | 5.96 | 27.1/26.8 | 23.9/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.47 | 5.94 | 27.0/27.0 | 23.7/23.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.092 | 0.65 | 0.35 | 0.00 | 6.04 | 32.1/21.4 | 18.7/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 9.23 | 28.7/28.5 | 23.4/21.6 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.58 | 0.42 | 0.47 | 5.94 | 32.5/21.8 | 18.8/29.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.54 | 0.46 | 0.00 | 3.48 | 26.0/25.9 | 24.1/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 71 | 0.778 | 0.742 | +0.054 | +0.017 | $14.44 | FUNDED_RESEARCH | $4 | BUF:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 82 | 0.868 | 0.841 | +0.037 | +0.011 | $2.65 | FUNDED_RESEARCH | $1 | BUF:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals YES | 29 | 0.345 | 0.315 | +0.041 | +0.011 | $1.28 | FUNDED_RESEARCH | $1 | BUF:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: BUF wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT12FLABUF-FLA3|no; why: higher confidence-adjusted growth (3.27 vs 1.91 bp); relationships: KXNHLSPREAD-26OCT12FLABUF-FLA3|no: DUPLICATIVE (phi 0.731); KXNHLSPREAD-26OCT12FLABUF-BUF2|yes: DUPLICATIVE (phi 0.388); failure: FLA wins by 2+
- **Florida wins by over 2.5 goals NO** — thesis: BUF wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT12FLABUF-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT12FLABUF-FLA2|no has the higher standalone adjusted growth (3.27 vs 1.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.731); they share one thesis budget; relationships: KXNHLSPREAD-26OCT12FLABUF-FLA2|no: DUPLICATIVE (phi 0.731); KXNHLSPREAD-26OCT12FLABUF-BUF2|yes: REINFORCING (phi 0.283); failure: FLA wins by 2+
- **Buffalo wins by over 1.5 goals YES** — thesis: BUF wins by 2+; alternative: KXNHLSPREAD-26OCT12FLABUF-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT12FLABUF-FLA2|no has the higher standalone adjusted growth (3.27 vs 1.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.388); they share one thesis budget; relationships: KXNHLSPREAD-26OCT12FLABUF-FLA2|no: DUPLICATIVE (phi 0.388); KXNHLSPREAD-26OCT12FLABUF-FLA3|no: REINFORCING (phi 0.283); failure: tight game (one-goal final or OT)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:WINS (p 0.5797): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- thesis BUF:WINS_BY_2PLUS (p 0.3453): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- KXNHLSPREAD-26OCT12FLABUF-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2217, phi -1.0)
- KXNHLSPREAD-26OCT12FLABUF-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2217, phi -0.731)
- KXNHLSPREAD-26OCT12FLABUF-BUF2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.433, phi -0.635)

portfolios: A EV +3.99 (adj +1.15) on $50.00, P(profit) 0.3453, adj growth 6.6 bp · B EV +1.37 (adj +0.42) on $18.37, P(profit) 0.7783, adj growth 3.7 bp · C EV +1.28 (adj +0.41) on $17.17, P(profit) 0.7783, adj growth 3.6 bp · R EV +0.48 (adj +0.14) on $6.00, P(profit) 0.7783, adj growth 4.8 bp

## OTT @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_OTT_win | p_overtime | goals | shots NJD/OTT | NJD/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.46 | 0.54 | 0.00 | 5.97 | 27.7/27.7 | 24.0/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.49 | 0.51 | 0.48 | 5.88 | 27.7/27.6 | 24.3/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.077 | 0.55 | 0.45 | 0.00 | 5.97 | 32.9/22.0 | 18.9/28.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.52 | 0.48 | 0.47 | 5.8 | 32.8/22.2 | 19.1/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.49 | 0.51 | 0.00 | 9.13 | 29.0/28.7 | 22.5/23.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 3.39 | 26.3/26.2 | 24.3/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 68 | 0.745 | 0.710 | +0.050 | +0.015 | $13.17 | FUNDED_RESEARCH | $4 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3|no; why: higher confidence-adjusted growth (2.31 vs 0.69 bp); wins across more scripts (relative breadth 0.926 vs 0.793); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:WINS (p 0.5157): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12OTTNJ-NJ2|no (same contract)
- KXNHLSPREAD-26OCT12OTTNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2547, phi -1.0)

portfolios: A EV +1.44 (adj +0.43) on $20.00, P(profit) 0.7453, adj growth 3.5 bp · B EV +0.95 (adj +0.28) on $13.17, P(profit) 0.7453, adj growth 2.5 bp · C EV +0.95 (adj +0.28) on $13.17, P(profit) 0.7453, adj growth 2.5 bp · R EV +0.29 (adj +0.09) on $4.00, P(profit) 0.7453, adj growth 2.9 bp

## VGK @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_VGK_win | p_overtime | goals | shots MIN/VGK | MIN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.55 | 0.45 | 0.00 | 6.02 | 28.6/28.8 | 25.4/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.46 | 5.88 | 28.2/28.5 | 25.2/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 9.24 | 29.9/30.0 | 24.4/23.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 6.02 | 22.7/33.6 | 30.1/19.1 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.46 | 5.87 | 22.7/33.7 | 30.3/19.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.50 | 0.50 | 0.48 | 2.85 | 27.1/27.1 | 25.6/25.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
