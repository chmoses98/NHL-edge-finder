# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T13:02:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +23.16 | +6.77 | +22.21 | 0.731 | -22.18 | -33.94 | 61.41 |
| B thesis-diversified (joint) ← optimiser card | 148.32 | +22.87 | +8.55 | +21.01 | 0.756 | -16.77 | -27.71 | 80.13 |
| C best expression per thesis | 150.00 | +26.57 | +9.86 | +23.80 | 0.742 | -24.03 | -37.04 | 89.98 |
| R FUNDED research stakes | 35.00 | +4.25 | +1.70 | +3.40 | 0.659 | -7.00 | -9.85 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_NSH_win | p_overtime | goals | shots BOS/NSH | BOS/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.64 | 0.36 | 0.00 | 6.07 | 28.1/28.0 | 25.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.50 | 6.0 | 28.0/28.0 | 24.5/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.38 | 29.7/29.6 | 24.3/22.6 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.082 | 0.69 | 0.31 | 0.00 | 6.06 | 32.8/22.0 | 19.4/28.2 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.46 | 5.96 | 33.1/22.6 | 19.4/29.7 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.060 | 0.70 | 0.30 | 0.00 | 9.4 | 34.6/23.6 | 18.7/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie McAvoy: 1+ assists NO | 49 | 0.623 | 0.527 | +0.116 | +0.019 | $6.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Full Game: Over 8.5 goals scored YES | 17 | 0.223 | 0.194 | +0.043 | +0.014 | $1.76 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | DIRECT (0.75) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored YES | 55 | 0.611 | 0.578 | +0.043 | +0.010 | $2.11 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (3.30 vs 0.66 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLTOTAL-26OCT22NSHBOS-9|yes: INTENTIONAL_DIVERSIFIER (phi -0.176); KXNHLTOTAL-26OCT22NSHBOS-6|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: BOS offense succeeds (4+ goals)
- **Full Game: Over 8.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-8|yes; why: higher confidence-adjusted growth (2.92 vs 2.17 bp); despite a smaller raw edge (+0.043 vs +0.045/contract); relationships: KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.176); KXNHLTOTAL-26OCT22NSHBOS-6|yes: DUPLICATIVE (phi 0.428); failure: NSH offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT22NSHBOS-9|yes has the higher standalone adjusted growth (2.92 vs 0.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.428); they share one thesis budget; relationships: KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLTOTAL-26OCT22NSHBOS-9|yes: DUPLICATIVE (phi 0.428); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3147): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.298): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4752): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4752, phi -0.257)
- KXNHLTOTAL-26OCT22NSHBOS-9|yes: FUNDED_RESEARCH; family MIXED; loses 25% of the draws where the thesis happens; opposing: failure thesis NSH:SUPPRESSED (p 0.4347, phi -0.402)
- KXNHLTOTAL-26OCT22NSHBOS-6|yes: FUNDED_RESEARCH; family MIXED; loses 12% of the draws where the thesis happens; opposing: failure thesis GAME:LOW_EVENT (p 0.2135, phi -0.652)

portfolios: A EV +2.69 (adj +0.67) on $15.40, P(profit) 0.4899, adj growth 5.7 bp · B EV +2.08 (adj +0.43) on $10.41, P(profit) 0.7427, adj growth 4.0 bp · C EV +2.78 (adj +0.59) on $12.02, P(profit) 0.7427, adj growth 5.4 bp · R EV +0.32 (adj +0.10) on $2.00, P(profit) 0.2229, adj growth 3.2 bp

## NYR @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYR_win | p_overtime | goals | shots TOR/NYR | TOR/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.01 | 27.3/27.6 | 23.9/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.46 | 5.93 | 27.3/27.5 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.51 | 0.49 | 0.00 | 9.38 | 28.9/29.0 | 23.0/22.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.076 | 0.46 | 0.54 | 0.00 | 6.07 | 21.8/32.7 | 28.9/18.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.45 | 0.55 | 0.48 | 5.88 | 21.9/32.6 | 29.3/18.8 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 6.03 | 32.2/22.0 | 19.1/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  428 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.02 | 27.0/26.7 | 23.6/22.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.117 | 0.66 | 0.34 | 0.00 | 5.99 | 32.0/20.9 | 18.2/27.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.46 | 5.94 | 27.0/26.5 | 23.1/23.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.54 | 0.46 | 0.50 | 5.87 | 32.2/21.2 | 18.0/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.58 | 0.42 | 0.00 | 9.35 | 28.7/28.2 | 22.4/22.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.070 | 0.65 | 0.35 | 0.00 | 9.27 | 34.3/22.6 | 17.9/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jake Sanderson: 1+ assists NO | 56 | 0.716 | 0.608 | +0.139 | +0.031 | $10.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $2.10 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (8.55 vs 0.45 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22SJOTT-SJ3|no; why: higher confidence-adjusted growth (2.88 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis OTT:SUPPRESSED (p 0.3496): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4408): highest fidelity KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes (same contract)
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4408, phi -0.228)
- KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3496, phi -0.194)

portfolios: A EV +1.81 (adj +0.51) on $8.36, P(profit) 0.7773, adj growth 4.9 bp · B EV +2.78 (adj +0.72) on $12.35, P(profit) 0.7773, adj growth 6.8 bp · C EV +3.86 (adj +1.01) on $17.16, P(profit) 0.7773, adj growth 9.2 bp · R EV +0.15 (adj +0.08) on $1.00, P(profit) 0.183, adj growth 2.9 bp

## ANA @ NJD  ·  10000 joint draws  ·  438 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_ANA_win | p_overtime | goals | shots NJD/ANA | NJD/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 28.7/28.6 | 25.1/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.46 | 5.9 | 28.9/28.7 | 25.5/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.56 | 0.44 | 0.00 | 9.29 | 30.1/30.0 | 24.1/23.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.089 | 0.62 | 0.38 | 0.00 | 6.0 | 34.0/22.7 | 19.8/29.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.52 | 0.48 | 0.47 | 5.9 | 34.1/22.9 | 19.8/30.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.32 | 35.7/24.0 | 19.1/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 13 | 0.210 | 0.186 | +0.072 | +0.049 | $5.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 70 | 0.791 | 0.743 | +0.077 | +0.029 | $10.00 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 63 | 0.677 | 0.664 | +0.031 | +0.018 | $4.69 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: higher confidence-adjusted growth (41.81 vs 8.78 bp); despite a smaller raw edge (+0.072 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: ANA offense suppressed (<= 2 goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22ANANJ-ANA2|yes; why: higher confidence-adjusted growth (8.78 vs 3.81 bp); wins across more scripts (relative breadth 1.016 vs 0.535); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.149); failure: NJD wins by 2+
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.84 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLSPREAD-26OCT22ANANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.149); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.368): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.2501): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4635): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- KXNHLGOAL-26OCT22ANANJ-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4108, phi -0.229)
- KXNHLSPREAD-26OCT22ANANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3229, phi -0.743)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4294, phi -0.245)
- override: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.84 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.38 (adj +0.51) on $15.40, P(profit) 0.6771, adj growth 4.8 bp · B EV +4.44 (adj +2.64) on $20.69, P(profit) 0.6401, adj growth 24.4 bp · C EV +5.91 (adj +3.51) on $22.61, P(profit) 0.2102, adj growth 31.5 bp · R EV +0.42 (adj +0.17) on $5.00, P(profit) 0.5643, adj growth 6.5 bp

## FLA @ PIT  ·  10000 joint draws  ·  444 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.65 | 0.35 | 0.00 | 6.02 | 26.9/26.9 | 24.1/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.48 | 5.98 | 26.9/26.7 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.63 | 0.37 | 0.00 | 9.37 | 28.6/28.6 | 23.2/21.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.72 | 0.28 | 0.00 | 6.09 | 31.7/21.6 | 19.0/26.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.56 | 0.44 | 0.48 | 5.95 | 32.2/21.6 | 18.4/28.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.23 | 33.6/22.7 | 18.3/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 63 | 0.701 | 0.682 | +0.055 | +0.036 | $8.20 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 67 | 0.729 | 0.712 | +0.043 | +0.026 | $7.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 11 | 0.155 | 0.135 | +0.038 | +0.018 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 71 | 0.792 | 0.748 | +0.067 | +0.024 | $7.03 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (12.46 vs 7.04 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.147); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no selected over broad KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.86 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: REINFORCING (phi 0.174); failure: FLA offense succeeds (4+ goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2|no; why: higher confidence-adjusted growth (6.82 vs 6.52 bp); despite a smaller raw edge (+0.038 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.824 vs 0.594); relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.111); failure: PIT offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2|no; why: KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2|no has the higher standalone adjusted growth (6.52 vs 6.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.267); relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: REINFORCING (phi 0.174); KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.111); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.4354): highest fidelity KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no selected over broad KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.86 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PIT:WINS_BY_2PLUS (p 0.3742): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.5952): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.342, phi -0.248)
- KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.342, phi -0.252)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3004, phi -0.183)
- KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2084, phi -1.0)
- override: Player prop expression KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no selected over broad KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.86 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.92 (adj +0.75) on $15.40, P(profit) 0.5564, adj growth 6.9 bp · B EV +2.37 (adj +1.23) on $24.13, P(profit) 0.517, adj growth 11.7 bp · C EV +2.12 (adj +1.13) on $16.91, P(profit) 0.7014, adj growth 10.4 bp · R EV +0.44 (adj +0.23) on $5.00, P(profit) 0.5825, adj growth 8.8 bp

## LAK @ NYI  ·  10000 joint draws  ·  400 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_LAK_win | p_overtime | goals | shots NYI/LAK | NYI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.94 | 27.2/27.2 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.49 | 0.51 | 0.48 | 5.89 | 27.3/27.1 | 23.9/24.1 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.080 | 0.61 | 0.39 | 0.00 | 5.98 | 32.1/21.7 | 18.9/27.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.53 | 0.47 | 0.45 | 5.85 | 32.4/21.8 | 18.6/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.55 | 0.45 | 0.00 | 9.14 | 29.0/28.8 | 23.5/22.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.070 | 0.54 | 0.46 | 0.00 | 3.46 | 25.9/26.0 | 24.3/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 65 | 0.836 | 0.699 | +0.170 | +0.033 | $10.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.056 | +0.022 | +0.013 | $1.57 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 12 | 0.153 | 0.138 | +0.026 | +0.010 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 56 | 0.630 | 0.588 | +0.053 | +0.010 | $3.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (10.72 vs 0.96 bp); relationships: KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.039); KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.066); failure: LAK offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (9.20 vs 2.04 bp); despite a smaller raw edge (+0.022 vs +0.026/contract); relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.083); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22LANYI-LATMOORE12-1|yes; why: higher confidence-adjusted growth (2.04 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.039); KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (10.72 vs 0.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.066); they share one thesis budget; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.083); KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4623): highest fidelity KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3123): highest fidelity KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes (same contract)
- KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.1 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3123, phi -0.206)
- KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4623, phi -0.141)
- KXNHLGOAL-26OCT22LANYI-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4623, phi -0.223)
- KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3123, phi -0.275)

portfolios: A EV +3.31 (adj +1.08) on $15.40, P(profit) 0.6568, adj growth 10.1 bp · B EV +4.08 (adj +1.19) on $17.11, P(profit) 0.6437, adj growth 11.2 bp · C EV +4.05 (adj +0.87) on $16.24, P(profit) 0.836, adj growth 8.2 bp · R EV +0.52 (adj +0.31) on $1.00, P(profit) 0.0647, adj growth 10.0 bp

## VGK @ STL  ·  10000 joint draws  ·  440 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.02 | 26.5/26.7 | 23.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.49 | 5.97 | 26.2/26.6 | 23.1/22.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.092 | 0.42 | 0.58 | 0.00 | 6.01 | 21.1/31.8 | 28.0/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.50 | 0.50 | 0.00 | 9.3 | 28.2/28.5 | 22.4/22.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.48 | 0.52 | 0.50 | 5.9 | 20.9/31.5 | 28.2/17.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 9.28 | 22.2/33.2 | 26.4/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mark Stone: 1+ assists NO | 54 | 0.624 | 0.577 | +0.067 | +0.020 | $5.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (3.48 vs 0.74 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3816): highest fidelity KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no (same contract)
- KXNHLAST-26OCT22VGKSTL-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4005, phi -0.279)

portfolios: A EV +0.74 (adj +0.22) on $6.16, P(profit) 0.6244, adj growth 2.0 bp · B EV +0.71 (adj +0.21) on $5.92, P(profit) 0.6244, adj growth 2.0 bp · C EV +0.99 (adj +0.29) on $8.22, P(profit) 0.6244, adj growth 2.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.63 | 0.37 | 0.00 | 5.96 | 26.0/25.7 | 22.8/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.8 | 26.2/25.9 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 5.93 | 30.8/20.2 | 17.7/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.59 | 0.41 | 0.46 | 5.87 | 31.2/20.7 | 17.8/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 9.2 | 27.3/27.1 | 21.8/20.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.46 | 2.8 | 24.3/24.4 | 22.9/22.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 71 | 0.776 | 0.740 | +0.051 | +0.016 | $8.07 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (2.78 vs 1.02 bp); wins across more scripts (relative breadth 0.983 vs 0.864); relationships: only recommended bet in this game; failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4478): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3404, phi -0.749)

portfolios: A EV +0.86 (adj +0.24) on $12.32, P(profit) 0.6596, adj growth 2.1 bp · B EV +0.57 (adj +0.18) on $8.07, P(profit) 0.7756, adj growth 1.7 bp · C EV +0.79 (adj +0.25) on $11.22, P(profit) 0.7756, adj growth 2.2 bp · R EV +0.21 (adj +0.07) on $3.00, P(profit) 0.7756, adj growth 2.4 bp

## MIN @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.43 | 0.57 | 0.00 | 5.99 | 29.1/29.5 | 25.5/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.49 | 0.51 | 0.47 | 5.93 | 29.3/29.5 | 26.1/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.16 | 30.8/31.0 | 24.4/25.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.080 | 0.38 | 0.62 | 0.00 | 5.96 | 23.6/34.7 | 30.3/20.6 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.43 | 0.57 | 0.45 | 5.92 | 23.6/35.1 | 31.8/20.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.41 | 0.59 | 0.00 | 3.46 | 28.1/28.5 | 26.3/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 1.5 goals NO | 59 | 0.680 | 0.633 | +0.073 | +0.026 | $6.94 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 72 | 0.795 | 0.752 | +0.060 | +0.018 | $1.78 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (6.11 vs 3.73 bp); relationships: KXNHLSPREAD-26OCT22MINCGY-MIN3|no: DUPLICATIVE (phi 0.742); failure: MIN wins by 2+
- **Minnesota wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 3.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.742); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: DUPLICATIVE (phi 0.742); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.4524): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- thesis CGY:WINS_BY_2PLUS (p 0.2365): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.335): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22MINCGY-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -1.0)
- KXNHLSPREAD-26OCT22MINCGY-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -0.742)

portfolios: A EV +1.57 (adj +0.48) on $15.40, P(profit) 0.729, adj growth 4.3 bp · B EV +0.99 (adj +0.34) on $8.72, P(profit) 0.6804, adj growth 3.2 bp · C EV +1.49 (adj +0.52) on $12.31, P(profit) 0.6804, adj growth 4.8 bp · R EV +0.32 (adj +0.11) on $3.00, P(profit) 0.6804, adj growth 4.1 bp

## CAR @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.9 | 24.8/23.2 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.110 | 0.55 | 0.45 | 0.00 | 6.03 | 21.8/33.5 | 30.1/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.63 | 0.37 | 0.00 | 9.49 | 28.9/29.4 | 24.0/21.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.47 | 6.0 | 27.4/28.1 | 24.8/24.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.97 | 22.0/33.7 | 30.4/18.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.34 | 23.3/35.0 | 28.8/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 69 | 0.764 | 0.725 | +0.059 | +0.019 | $5.02 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Edmonton wins by over 1.5 goals YES | 28 | 0.347 | 0.311 | +0.053 | +0.017 | $1.47 | FUNDED_RESEARCH | $1 | EDM:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 80 | 0.855 | 0.825 | +0.044 | +0.014 | $2.73 | FUNDED_RESEARCH | $1 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Edmonton over 2.5 goals scored YES | 63 | 0.706 | 0.663 | +0.060 | +0.017 | $2.04 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-EDM3|yes; why: higher confidence-adjusted growth (4.01 vs 3.48 bp); wins across more scripts (relative breadth 1.008 vs 0.498); relationships: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.406); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: DUPLICATIVE (phi 0.74); KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3|yes: REINFORCING (phi 0.499); failure: CAR wins by 2+
- **Edmonton wins by over 1.5 goals YES** — thesis: EDM wins by 2+; alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT22CAREDM-EDM2|yes selected over broad KXNHLSPREAD-26OCT22CAREDM-EDM3|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.68 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.406); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: DUPLICATIVE (phi 0.3); KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3|yes: DUPLICATIVE (phi 0.446); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-CAR2|no has the higher standalone adjusted growth (4.01 vs 2.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.740); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.74); KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.3); KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3|yes: REINFORCING (phi 0.423); failure: CAR wins by 2+
- **Edmonton over 2.5 goals scored YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-CAR2|no has the higher standalone adjusted growth (4.01 vs 2.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.499); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: REINFORCING (phi 0.499); KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.446); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: REINFORCING (phi 0.423); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:WINS (p 0.5634): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- thesis EDM:WINS_BY_2PLUS (p 0.3474): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4827): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22CAREDM-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -1.0)
- KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4366, phi -0.642)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -0.74)
- KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:SUPPRESSED (p 0.3036, phi -0.978)
- override: Broad expression KXNHLSPREAD-26OCT22CAREDM-EDM2|yes selected over broad KXNHLSPREAD-26OCT22CAREDM-EDM3|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.68 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.86 (adj +0.55) on $15.40, P(profit) 0.5132, adj growth 4.7 bp · B EV +1.02 (adj +0.32) on $11.25, P(profit) 0.6412, adj growth 3.0 bp · C EV +1.07 (adj +0.35) on $12.84, P(profit) 0.7639, adj growth 3.2 bp · R EV +0.49 (adj +0.16) on $5.00, P(profit) 0.6412, adj growth 5.5 bp

## UTA @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 6.0 | 27.4/27.7 | 24.2/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.45 | 0.55 | 0.00 | 6.03 | 21.8/32.9 | 29.1/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.93 | 27.5/28.1 | 24.8/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 9.35 | 28.7/29.2 | 22.9/22.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.46 | 0.54 | 0.46 | 5.95 | 21.8/32.7 | 29.5/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.074 | 0.44 | 0.56 | 0.00 | 9.29 | 23.2/34.7 | 27.8/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Utah wins by over 2.5 goals NO | 73 | 0.817 | 0.771 | +0.073 | +0.027 | $10.25 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah wins by over 1.5 goals NO | 61 | 0.705 | 0.655 | +0.078 | +0.028 | $2.81 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 21 | 0.281 | 0.243 | +0.059 | +0.021 | $1.84 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Utah wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA2|no; why: higher confidence-adjusted growth (8.66 vs 7.51 bp); despite a smaller raw edge (+0.073 vs +0.078/contract); relationships: KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.731); KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: REINFORCING (phi 0.295); failure: UTA wins by 2+
- **Utah wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 7.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.731); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: DUPLICATIVE (phi 0.731); KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: DUPLICATIVE (phi 0.404); failure: UTA wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 5.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: REINFORCING (phi 0.295); KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.404); failure: UTA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS (p 0.4936): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2807): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22UTASEA-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2951, phi -0.731)
- KXNHLSPREAD-26OCT22UTASEA-UTA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2951, phi -1.0)
- KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS (p 0.5064, phi -0.633)

portfolios: A EV +2.49 (adj +0.90) on $15.40, P(profit) 0.2807, adj growth 8.1 bp · B EV +1.85 (adj +0.68) on $14.89, P(profit) 0.7049, adj growth 6.4 bp · C EV +1.41 (adj +0.52) on $14.24, P(profit) 0.8173, adj growth 5.0 bp · R EV +0.69 (adj +0.25) on $5.00, P(profit) 0.7049, adj growth 9.1 bp

## DET @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 6.05 | 21.7/33.5 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.8 | 24.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.94 | 27.5/28.1 | 24.8/24.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.50 | 5.91 | 21.8/33.5 | 30.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.34 | 29.0/29.5 | 23.7/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.2 | 23.2/35.2 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 22 | 0.310 | 0.262 | +0.078 | +0.030 | $2.58 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 74 | 0.850 | 0.775 | +0.096 | +0.022 | $6.69 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit over 5.5 goals scored NO | 87 | 0.920 | 0.890 | +0.042 | +0.012 | $5.51 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (11.22 vs 9.48 bp); relationships: KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.282); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: REINFORCING (phi 0.189); failure: DET wins (incl. OT/SO)
- **Detroit wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (11.22 vs 5.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.282); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.282); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: DUPLICATIVE (phi 0.443); failure: DET wins by 2+
- **Detroit over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.189); KXNHLSPREAD-26OCT22DETVAN-DET3|no: DUPLICATIVE (phi 0.443); failure: high-event game (8+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.3098): highest fidelity KXNHLSPREAD-26OCT22DETVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — Broad expression KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS (p 0.4617, phi -0.62)
- KXNHLSPREAD-26OCT22DETVAN-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.5 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2486, phi -0.731)
- KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2641, phi -0.425)
- override: Broad expression KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT22DETVAN-DET2|no selected over broad KXNHLSPREAD-26OCT22DETVAN-VAN3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.53 (adj +0.86) on $15.40, P(profit) 0.5383, adj growth 7.7 bp · B EV +1.98 (adj +0.61) on $14.78, P(profit) 0.8257, adj growth 5.8 bp · C EV +2.09 (adj +0.82) on $6.23, P(profit) 0.3098, adj growth 7.4 bp · R EV +0.69 (adj +0.22) on $5.00, P(profit) 0.3098, adj growth 8.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22DETVAN-DET|no == KXNHLGAME-26OCT22DETVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
