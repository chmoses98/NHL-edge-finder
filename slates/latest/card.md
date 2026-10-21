# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T16:14:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +11.26 | +2.92 | +13.56 | 0.627 | -25.96 | -39.21 | 25.46 |
| B thesis-diversified (joint) ← optimiser card | 59.35 | +6.55 | +2.97 | +8.67 | 0.580 | -29.32 | -32.69 | 26.11 |
| C best expression per thesis | 68.57 | +7.56 | +2.35 | +7.33 | 0.646 | -17.57 | -30.55 | 21.16 |
| R FUNDED research stakes | 11.00 | +1.07 | +0.52 | +1.10 | 0.571 | -6.41 | -9.66 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  472 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.122 | 0.62 | 0.38 | 0.00 | 5.97 | 32.2/20.9 | 18.1/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.58 | 0.42 | 0.00 | 6.0 | 27.2/26.8 | 23.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.46 | 5.88 | 26.9/26.3 | 23.2/23.6 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.58 | 0.42 | 0.48 | 5.86 | 32.6/21.0 | 18.0/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.17 | 28.4/27.8 | 22.4/22.1 | even strength |
| BUF shot control · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.47 | 2.77 | 30.8/19.4 | 18.0/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 8 | 0.108 | 0.100 | +0.022 | +0.014 | $3.42 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 60 | 0.669 | 0.632 | +0.053 | +0.015 | $4.31 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 73 | 0.787 | 0.756 | +0.044 | +0.012 | $3.23 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 3.5 goals scored NO | 52 | 0.588 | 0.552 | +0.051 | +0.014 | $4.43 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: higher confidence-adjusted growth (5.64 vs 2.21 bp); despite a smaller raw edge (+0.022 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: MOSTLY_INDEPENDENT (phi 0.106); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: MOSTLY_INDEPENDENT (phi 0.023); failure: PHI offense suppressed (<= 2 goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: higher confidence-adjusted growth (2.21 vs 1.77 bp); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.106); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.74); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.551); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF3|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-2|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.74); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.52); failure: BUF wins by 2+
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.551); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: REINFORCING (phi 0.52); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BUF:SUPPRESSED (p 0.3827): highest fidelity KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no — Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF3|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-2|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:OFFENSE_4PLUS (p 0.3107): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4408): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4749, phi -0.185)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3305, phi -1.0)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3305, phi -0.74)
- KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3999, phi -0.976)
- override: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF3|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-2|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.44 (adj +1.16) on $50.00, P(profit) 0.7318, adj growth 9.7 bp · B EV +1.88 (adj +0.85) on $15.39, P(profit) 0.564, adj growth 7.4 bp · C EV +3.26 (adj +0.66) on $18.57, P(profit) 0.6311, adj growth 5.8 bp · R EV +0.68 (adj +0.29) on $6.00, P(profit) 0.564, adj growth 9.4 bp

## FLA @ OTT  ·  10000 joint draws  ·  432 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 5.97 | 26.4/26.3 | 23.4/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.47 | 5.88 | 26.3/26.3 | 23.1/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.086 | 0.69 | 0.31 | 0.00 | 6.05 | 31.2/21.0 | 18.3/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.61 | 0.39 | 0.00 | 9.21 | 28.3/28.0 | 22.8/21.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.54 | 0.46 | 0.48 | 5.91 | 31.4/21.1 | 18.0/28.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.058 | 0.69 | 0.31 | 0.00 | 9.27 | 33.6/22.7 | 18.0/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 65 | 0.717 | 0.697 | +0.051 | +0.031 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.668 | 0.619 | +0.071 | +0.022 | $15.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 16 | 0.198 | 0.185 | +0.029 | +0.015 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 18 | 0.216 | 0.201 | +0.026 | +0.010 | $3.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21FLAOTT-FLASJONES3-1|no; why: higher confidence-adjusted growth (9.33 vs 4.35 bp); despite a smaller raw edge (+0.051 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: FLA offense succeeds (4+ goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT21FLAOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (4.39 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: OTT offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: higher confidence-adjusted growth (3.59 vs 3.30 bp); despite a smaller raw edge (+0.028 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: Player prop expression KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes selected over broad KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.32 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4611): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.3554): highest fidelity KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:WINS (p 0.5731): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT21FLAOTT-FLASJONES3-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3205, phi -0.251)
- KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4289, phi -0.241)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3554, phi -0.192)
- KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3554, phi -0.211)
- override: Player prop expression KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes selected over broad KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.32 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.82 (adj +1.76) on $50.00, P(profit) 0.6521, adj growth 15.8 bp · B EV +4.67 (adj +2.12) on $43.96, P(profit) 0.6195, adj growth 18.7 bp · C EV +4.30 (adj +1.69) on $50.00, P(profit) 0.692, adj growth 15.4 bp · R EV +0.38 (adj +0.23) on $5.00, P(profit) 0.7172, adj growth 8.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
