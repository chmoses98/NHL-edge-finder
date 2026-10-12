# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T11:24:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +11.91 | +2.91 | +8.19 | 0.689 | -39.70 | -45.35 | 22.60 |
| B thesis-diversified (joint) ← optimiser card | 67.96 | +7.00 | +2.46 | +2.99 | 0.661 | -22.81 | -26.23 | 22.48 |
| C best expression per thesis | 51.24 | +6.66 | +2.39 | +2.63 | 0.615 | -27.54 | -30.94 | 21.32 |
| R FUNDED research stakes | 11.00 | +0.93 | +0.42 | +3.46 | 0.548 | -4.27 | -9.80 | 0.00 |

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

## OTT @ NJD  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card


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
| Jack Hughes: 1+ goals NO | 63 | 0.705 | 0.682 | +0.058 | +0.036 | $16.16 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.179 | 0.154 | +0.041 | +0.017 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 73 | 0.862 | 0.763 | +0.118 | +0.019 | $16.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Timo Meier: 1+ goals NO | 73 | 0.777 | 0.761 | +0.033 | +0.018 | $13.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (12.44 vs 3.62 bp); despite a smaller raw edge (+0.058 vs +0.118/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NJD offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT12OTTNJ-NJ2|no; why: higher confidence-adjusted growth (4.94 vs 2.31 bp); despite a smaller raw edge (+0.041 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT12OTTNJ-4|no; why: higher confidence-adjusted growth (4.32 vs 0.30 bp); wins across more scripts (relative breadth 1.001 vs 0.365); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: OTT offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4523): highest fidelity KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis OTT:OFFENSE_4PLUS (p 0.3514): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5157): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3286, phi -0.24)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4273, phi -0.224)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3514, phi -0.167)
- KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3286, phi -0.218)
- override: Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.92 (adj +1.76) on $50.00, P(profit) 0.7274, adj growth 16.0 bp · B EV +5.63 (adj +2.04) on $49.59, P(profit) 0.543, adj growth 18.7 bp · C EV +5.38 (adj +1.98) on $34.07, P(profit) 0.5271, adj growth 17.7 bp · R EV +0.45 (adj +0.28) on $5.00, P(profit) 0.7047, adj growth 10.1 bp

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
