# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T13:59:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +22.39 | +6.10 | +21.80 | 0.772 | -16.36 | -26.62 | 56.61 |
| B thesis-diversified (joint) ← optimiser card | 147.69 | +21.63 | +8.40 | +20.42 | 0.763 | -15.99 | -25.67 | 79.57 |
| C best expression per thesis | 149.99 | +21.16 | +7.85 | +20.34 | 0.736 | -19.94 | -31.76 | 73.27 |
| R FUNDED research stakes | 33.00 | +4.25 | +1.95 | +2.29 | 0.631 | -6.83 | -9.48 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card


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
| David Pastrnak: 1+ goals NO | 61 | 0.660 | 0.646 | +0.033 | +0.019 | $5.79 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 49 | 0.623 | 0.527 | +0.116 | +0.019 | $4.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Matthew Wood: 1+ goals YES | 16 | 0.203 | 0.183 | +0.033 | +0.014 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Full Game: Over 7.5 goals scored YES | 24 | 0.298 | 0.267 | +0.045 | +0.014 | $2.48 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (3.54 vs 3.30 bp); despite a smaller raw edge (+0.033 vs +0.116/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLTOTAL-26OCT22NSHBOS-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.162); failure: BOS offense succeeds (4+ goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no has the higher standalone adjusted growth (3.54 vs 3.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.150); they share one thesis budget; relationships: KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLTOTAL-26OCT22NSHBOS-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.198); failure: BOS offense succeeds (4+ goals)
- **Matthew Wood: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: higher confidence-adjusted growth (2.94 vs 2.92 bp); despite a smaller raw edge (+0.033 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.908 vs 0.372); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLTOTAL-26OCT22NSHBOS-8|yes: INTENTIONAL_DIVERSIFIER (phi 0.146); failure: NSH offense suppressed (<= 2 goals)
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: Broad expression KXNHLTOTAL-26OCT22NSHBOS-8|yes selected over broad KXNHLTOTAL-26OCT22NSHBOS-9|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.75 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.162); KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.198); KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: INTENTIONAL_DIVERSIFIER (phi 0.146); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.3147): highest fidelity KXNHLAST-26OCT22NSHBOS-BOSPZACHA18-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3506): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.298): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes — Broad expression KXNHLTOTAL-26OCT22NSHBOS-8|yes selected over broad KXNHLTOTAL-26OCT22NSHBOS-9|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.75 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT22NSHBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4752, phi -0.24)
- KXNHLAST-26OCT22NSHBOS-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4752, phi -0.257)
- KXNHLGOAL-26OCT22NSHBOS-NSHMWOOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4347, phi -0.219)
- KXNHLTOTAL-26OCT22NSHBOS-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NSH:SUPPRESSED (p 0.4347, phi -0.412)
- override: Broad expression KXNHLTOTAL-26OCT22NSHBOS-8|yes selected over broad KXNHLTOTAL-26OCT22NSHBOS-9|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.75 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.28 (adj +0.45) on $13.96, P(profit) 0.4253, adj growth 4.2 bp · B EV +2.13 (adj +0.62) on $14.51, P(profit) 0.6458, adj growth 5.8 bp · C EV +1.46 (adj +0.64) on $13.57, P(profit) 0.7656, adj growth 5.9 bp · R EV +0.28 (adj +0.12) on $3.00, P(profit) 0.7963, adj growth 4.3 bp

## NYR @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYR_win | p_overtime | goals | shots TOR/NYR | TOR/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.01 | 27.3/27.6 | 23.9/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.46 | 5.93 | 27.3/27.5 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.51 | 0.49 | 0.00 | 9.38 | 28.9/29.0 | 23.0/22.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.076 | 0.46 | 0.54 | 0.00 | 6.07 | 21.8/32.7 | 28.9/18.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.45 | 0.55 | 0.48 | 5.88 | 21.9/32.6 | 29.3/18.8 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 6.03 | 32.2/22.0 | 19.1/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Dorofeyev: 1+ assists NO | 69 | 0.763 | 0.719 | +0.058 | +0.014 | $5.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22NYRTOR-NYRMZIBANEJAD93-1|no; why: higher confidence-adjusted growth (2.03 vs 1.02 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NYR:SUPPRESSED (p 0.3965): highest fidelity KXNHLAST-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT22NYRTOR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3835, phi -0.215)

portfolios: A EV +0.46 (adj +0.11) on $5.58, P(profit) 0.7627, adj growth 1.0 bp · B EV +0.46 (adj +0.11) on $5.67, P(profit) 0.7627, adj growth 1.1 bp · C EV +0.64 (adj +0.15) on $7.86, P(profit) 0.7627, adj growth 1.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 2 on card


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
| Jake Sanderson: 1+ assists NO | 56 | 0.716 | 0.602 | +0.139 | +0.024 | $7.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.77 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT22SJOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (5.33 vs 1.59 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT22SJOTT-OTT2|yes; why: higher confidence-adjusted growth (2.88 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.846 vs 0.696); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis OTT:SUPPRESSED (p 0.3496): highest fidelity KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4408): highest fidelity KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes (same contract)
- KXNHLAST-26OCT22SJOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.6 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4408, phi -0.228)
- KXNHLGOAL-26OCT22SJOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3496, phi -0.194)

portfolios: A EV +3.21 (adj +0.56) on $13.17, P(profit) 0.6397, adj growth 5.0 bp · B EV +2.06 (adj +0.46) on $9.22, P(profit) 0.7773, adj growth 4.4 bp · C EV +2.85 (adj +0.64) on $12.77, P(profit) 0.7773, adj growth 5.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  438 bet sides mapped, 11 +EV candidates, 3 on card


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
| New Jersey wins by over 2.5 goals NO | 70 | 0.791 | 0.743 | +0.077 | +0.029 | $8.73 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 63 | 0.677 | 0.664 | +0.031 | +0.018 | $4.52 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 73 | 0.771 | 0.758 | +0.027 | +0.014 | $4.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **New Jersey wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22ANANJ-ANA2|yes; why: higher confidence-adjusted growth (8.78 vs 3.81 bp); wins across more scripts (relative breadth 1.016 vs 0.535); relationships: KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.145); failure: NJD wins by 2+
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.78 vs 3.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.149); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.368): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis ANA:WINS (p 0.4635): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.2501): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- KXNHLSPREAD-26OCT22ANANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3229, phi -0.743)
- KXNHLGOAL-26OCT22ANANJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4294, phi -0.245)
- KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4294, phi -0.22)
- override: Player prop expression KXNHLGOAL-26OCT22ANANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT22ANANJ-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.00 (adj +0.45) on $13.96, P(profit) 0.6662, adj growth 4.3 bp · B EV +1.33 (adj +0.57) on $18.17, P(profit) 0.749, adj growth 5.4 bp · C EV +1.30 (adj +0.48) on $12.08, P(profit) 0.7914, adj growth 4.6 bp · R EV +0.42 (adj +0.17) on $5.00, P(profit) 0.5643, adj growth 6.5 bp

## FLA @ PIT  ·  10000 joint draws  ·  444 bet sides mapped, 11 +EV candidates, 4 on card


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
| Blake Lizotte: 1+ goals YES | 10 | 0.155 | 0.131 | +0.049 | +0.025 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.701 | 0.682 | +0.055 | +0.036 | $8.73 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 71 | 0.792 | 0.748 | +0.067 | +0.024 | $6.62 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Andrei Kuzmenko: 1+ goals YES | 16 | 0.207 | 0.187 | +0.038 | +0.017 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no; why: higher confidence-adjusted growth (13.91 vs 6.29 bp); despite a smaller raw edge (+0.049 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT22FLAPIT-PITAKUZMENKO62-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: PIT offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22FLAPIT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (12.46 vs 7.04 bp); relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT22FLAPIT-PITAKUZMENKO62-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3|no; why: higher confidence-adjusted growth (6.29 vs 4.79 bp); despite a smaller raw edge (+0.067 vs +0.071/contract); wins across more scripts (relative breadth 0.996 vs 0.76); relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT22FLAPIT-PITAKUZMENKO62-1|yes: MOSTLY_INDEPENDENT (phi 0.115); failure: FLA wins by 2+
- **Andrei Kuzmenko: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no has the higher standalone adjusted growth (6.29 vs 4.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.115); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.115); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.4354): highest fidelity KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.3742): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no (same contract)
- thesis PIT:WINS (p 0.5952): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no (same contract)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3004, phi -0.183)
- KXNHLGOAL-26OCT22FLAPIT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.342, phi -0.248)
- KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2084, phi -1.0)
- KXNHLGOAL-26OCT22FLAPIT-PITAKUZMENKO62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3004, phi -0.165)

portfolios: A EV +1.74 (adj +0.66) on $13.96, P(profit) 0.5564, adj growth 6.2 bp · B EV +2.87 (adj +1.45) on $19.61, P(profit) 0.6898, adj growth 13.7 bp · C EV +1.79 (adj +0.85) on $18.12, P(profit) 0.5876, adj growth 8.1 bp · R EV +0.44 (adj +0.23) on $5.00, P(profit) 0.5825, adj growth 8.8 bp

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
| Mats Zuccarello: 1+ assists NO | 65 | 0.836 | 0.699 | +0.170 | +0.033 | $8.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.056 | +0.022 | +0.013 | $1.36 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.246 | 0.236 | +0.025 | +0.014 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 56 | 0.630 | 0.590 | +0.053 | +0.013 | $3.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (10.72 vs 1.48 bp); relationships: KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.066); failure: LAK offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT22LANYI-LATMOORE12-1|yes; why: higher confidence-adjusted growth (9.20 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.031/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.083); failure: LAK offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22LANYI-LA3|no; why: higher confidence-adjusted growth (2.55 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYI offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no; why: second expression of the same thesis: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no has the higher standalone adjusted growth (10.72 vs 1.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.066); they share one thesis budget; relationships: KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.066); KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.083); KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4623): highest fidelity KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.375): highest fidelity KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3123): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT22LANYI-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.1 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3123, phi -0.206)
- KXNHLGOAL-26OCT22LANYI-LAJEDMUNDSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4623, phi -0.141)
- KXNHLGOAL-26OCT22LANYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4067, phi -0.234)
- KXNHLAST-26OCT22LANYI-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3123, phi -0.275)

portfolios: A EV +2.81 (adj +0.97) on $13.96, P(profit) 0.6671, adj growth 9.2 bp · B EV +3.48 (adj +1.06) on $15.65, P(profit) 0.6443, adj growth 10.1 bp · C EV +3.39 (adj +0.77) on $14.81, P(profit) 0.836, adj growth 7.4 bp · R EV +0.52 (adj +0.31) on $1.00, P(profit) 0.0647, adj growth 10.0 bp

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
| Trevor Connelly: 1+ assists NO | 72 | 0.782 | 0.746 | +0.048 | +0.012 | $5.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT22VGKSTL-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (1.63 vs 0.74 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3816): highest fidelity KXNHLAST-26OCT22VGKSTL-VGKTCONNELLY24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT22VGKSTL-VGKTCONNELLY24-1|no (same contract)
- KXNHLAST-26OCT22VGKSTL-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4005, phi -0.215)

portfolios: A EV +0.37 (adj +0.09) on $5.58, P(profit) 0.7823, adj growth 0.9 bp · B EV +0.36 (adj +0.09) on $5.45, P(profit) 0.7823, adj growth 0.8 bp · C EV +0.50 (adj +0.12) on $7.54, P(profit) 0.7823, adj growth 1.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  404 bet sides mapped, 4 +EV candidates, 3 on card


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
| Dylan Samberg: 1+ goals YES | 3 | 0.051 | 0.044 | +0.019 | +0.012 | $1.14 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 21 | 0.265 | 0.248 | +0.043 | +0.027 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 71 | 0.776 | 0.740 | +0.051 | +0.016 | $4.71 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (10.13 vs 8.99 bp); despite a smaller raw edge (+0.019 vs +0.043/contract); relationships: KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.059); failure: WPG offense suppressed (<= 2 goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: higher confidence-adjusted growth (8.99 vs 2.78 bp); despite a smaller raw edge (+0.043 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.141); failure: WPG offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (2.78 vs 1.02 bp); wins across more scripts (relative breadth 0.983 vs 0.864); relationships: KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.059); KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.141); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2894): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4478): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT22WPGDAL-WPGDSAMBERG54-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4926, phi -0.107)
- KXNHLGOAL-26OCT22WPGDAL-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4926, phi -0.265)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3404, phi -0.749)

portfolios: A EV +1.42 (adj +0.63) on $13.96, P(profit) 0.7145, adj growth 5.8 bp · B EV +1.66 (adj +0.95) on $9.26, P(profit) 0.3033, adj growth 8.9 bp · C EV +1.42 (adj +0.72) on $12.04, P(profit) 0.2645, adj growth 6.6 bp · R EV +0.72 (adj +0.43) on $3.00, P(profit) 0.0507, adj growth 13.4 bp

## MIN @ CGY  ·  10000 joint draws  ·  430 bet sides mapped, 7 +EV candidates, 3 on card


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
| Jonathan Castagna: 1+ goals YES | 8 | 0.134 | 0.113 | +0.049 | +0.028 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.613 | 0.590 | +0.055 | +0.032 | $6.37 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 2.5 goals NO | 71 | 0.795 | 0.750 | +0.070 | +0.025 | $6.98 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (21.05 vs 7.11 bp); despite a smaller raw edge (+0.049 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT22MINCGY-MIN3|no: MOSTLY_INDEPENDENT (phi 0.1); failure: CGY offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (9.18 vs 7.11 bp); despite a smaller raw edge (+0.055 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT22MINCGY-MIN3|no: REINFORCING (phi 0.228); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (9.18 vs 7.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.228); they share one thesis budget; relationships: KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.228); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.335): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3746): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no less than the minimum stake; KXNHLAST-26OCT22MINCGY-MINQHUGHES43-1|no kept
- thesis CGY:WINS (p 0.4524): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT22MINCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.198)
- KXNHLGOAL-26OCT22MINCGY-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3955, phi -0.308)
- KXNHLSPREAD-26OCT22MINCGY-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -0.742)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT22MINCGY-MIN4|no less than the minimum stake; KXNHLAST-26OCT22MINCGY-MINQHUGHES43-1|no kept

portfolios: A EV +1.68 (adj +0.62) on $13.96, P(profit) 0.5992, adj growth 5.8 bp · B EV +2.79 (adj +1.45) on $15.93, P(profit) 0.585, adj growth 13.7 bp · C EV +3.94 (adj +2.05) on $22.93, P(profit) 0.585, adj growth 18.8 bp · R EV +0.39 (adj +0.19) on $4.00, P(profit) 0.5318, adj growth 7.0 bp

## CAR @ EDM  ·  10000 joint draws  ·  410 bet sides mapped, 10 +EV candidates, 4 on card


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
| Mattias Ekholm: 1+ goals YES | 8 | 0.119 | 0.102 | +0.034 | +0.017 | $1.61 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 69 | 0.764 | 0.725 | +0.059 | +0.019 | $4.87 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 31 | 0.361 | 0.342 | +0.036 | +0.017 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 80 | 0.855 | 0.825 | +0.044 | +0.014 | $2.17 | FUNDED_RESEARCH | $1 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: higher confidence-adjusted growth (7.85 vs 4.01 bp); despite a smaller raw edge (+0.034 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT22CAREDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.083); failure: EDM offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-EDM3|yes; why: higher confidence-adjusted growth (4.01 vs 3.48 bp); wins across more scripts (relative breadth 1.008 vs 0.498); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT22CAREDM-EDMZHYMAN18-1|yes: REINFORCING (phi 0.166); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: DUPLICATIVE (phi 0.74); failure: CAR wins by 2+
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-CAR2|no has the higher standalone adjusted growth (4.01 vs 3.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.166); they share one thesis budget; relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT22CAREDM-CAR2|no: REINFORCING (phi 0.166); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: MOSTLY_INDEPENDENT (phi 0.137); failure: EDM offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.74); KXNHLGOAL-26OCT22CAREDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4827): highest fidelity KXNHLTEAMTOTAL-26OCT22CAREDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5634): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- thesis EDM:WINS_BY_2PLUS (p 0.3474): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- KXNHLGOAL-26OCT22CAREDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3036, phi -0.136)
- KXNHLSPREAD-26OCT22CAREDM-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -1.0)
- KXNHLGOAL-26OCT22CAREDM-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3036, phi -0.253)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -0.74)
- override: Broad expression KXNHLSPREAD-26OCT22CAREDM-CAR3|no selected over player prop KXNHLAST-26OCT22CAREDM-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.62 (adj +0.38) on $13.96, P(profit) 0.6309, adj growth 3.6 bp · B EV +1.43 (adj +0.61) on $10.95, P(profit) 0.3908, adj growth 5.8 bp · C EV +0.91 (adj +0.30) on $10.90, P(profit) 0.7639, adj growth 2.8 bp · R EV +0.22 (adj +0.07) on $3.00, P(profit) 0.7639, adj growth 2.7 bp

## UTA @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


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
| Utah wins by over 2.5 goals NO | 73 | 0.817 | 0.771 | +0.073 | +0.027 | $8.73 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 21 | 0.281 | 0.243 | +0.059 | +0.021 | $1.96 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Utah wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-SEA2|yes; why: higher confidence-adjusted growth (8.66 vs 5.67 bp); wins across more scripts (relative breadth 1.042 vs 0.539); relationships: KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: REINFORCING (phi 0.295); failure: UTA wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.66 vs 5.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: REINFORCING (phi 0.295); failure: UTA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS (p 0.4936): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2807): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22UTASEA-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2951, phi -0.731)
- KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS (p 0.5064, phi -0.633)

portfolios: A EV +2.17 (adj +0.76) on $13.96, P(profit) 0.2807, adj growth 6.9 bp · B EV +1.38 (adj +0.51) on $10.68, P(profit) 0.8173, adj growth 4.8 bp · C EV +1.19 (adj +0.44) on $12.08, P(profit) 0.8173, adj growth 4.2 bp · R EV +0.56 (adj +0.21) on $4.00, P(profit) 0.8173, adj growth 7.6 bp

## DET @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 12 +EV candidates, 3 on card


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
| Vancouver wins by over 1.5 goals YES | 22 | 0.310 | 0.262 | +0.078 | +0.030 | $2.20 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 74 | 0.850 | 0.775 | +0.096 | +0.022 | $5.70 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit over 5.5 goals scored NO | 87 | 0.920 | 0.890 | +0.042 | +0.012 | $4.69 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (11.22 vs 9.48 bp); relationships: KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.282); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: REINFORCING (phi 0.189); failure: DET wins (incl. OT/SO)
- **Detroit wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (11.22 vs 5.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.282); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.282); KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: DUPLICATIVE (phi 0.443); failure: DET wins by 2+
- **Detroit over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (11.22 vs 2.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.189); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.189); KXNHLSPREAD-26OCT22DETVAN-DET3|no: DUPLICATIVE (phi 0.443); failure: high-event game (8+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.3098): highest fidelity KXNHLSPREAD-26OCT22DETVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT22DETVAN-DET2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no kept
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS (p 0.4617, phi -0.62)
- KXNHLSPREAD-26OCT22DETVAN-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.5 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2486, phi -0.731)
- KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2641, phi -0.425)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT22DETVAN-DET2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT22DETVAN-DET6|no kept
- override: Broad expression KXNHLSPREAD-26OCT22DETVAN-DET2|no selected over broad KXNHLSPREAD-26OCT22DETVAN-VAN3|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.64 (adj +0.42) on $13.96, P(profit) 0.6508, adj growth 3.8 bp · B EV +1.69 (adj +0.52) on $12.59, P(profit) 0.8257, adj growth 4.9 bp · C EV +1.77 (adj +0.69) on $5.29, P(profit) 0.3098, adj growth 6.4 bp · R EV +0.69 (adj +0.22) on $5.00, P(profit) 0.3098, adj growth 8.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22DETVAN-DET|no == KXNHLGAME-26OCT22DETVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
