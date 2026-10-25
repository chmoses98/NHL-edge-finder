# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T23:19:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +20.18 | +4.84 | +22.40 | 0.642 | -56.07 | -77.17 | 34.31 |
| B thesis-diversified (joint) ← optimiser card | 92.58 | +9.88 | +3.90 | +11.12 | 0.746 | -23.99 | -39.78 | 35.67 |
| C best expression per thesis | 52.14 | +9.72 | +4.99 | +7.18 | 0.558 | -28.86 | -28.86 | 43.99 |
| R FUNDED research stakes | 15.00 | +1.59 | +0.59 | +2.75 | 0.724 | -3.95 | -8.61 | 0.00 |

## COL @ NSH  ·  10000 joint draws  ·  464 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.127 | 0.28 | 0.72 | 0.00 | 6.03 | 22.7/35.2 | 30.1/20.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.34 | 0.66 | 0.00 | 6.0 | 28.6/29.3 | 25.0/25.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.45 | 0.55 | 0.46 | 5.87 | 23.1/35.6 | 32.1/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.48 | 5.95 | 28.7/29.4 | 26.1/25.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.095 | 0.27 | 0.73 | 0.00 | 9.29 | 24.2/37.0 | 28.1/19.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.35 | 0.65 | 0.00 | 9.23 | 30.0/30.8 | 23.8/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 77 | 0.815 | 0.802 | +0.032 | +0.020 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 77 | 0.866 | 0.800 | +0.084 | +0.018 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.135 | 0.127 | +0.018 | +0.010 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Colorado over 3.5 goals scored NO | 43 | 0.496 | 0.461 | +0.049 | +0.013 | $4.37 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (5.08 vs 4.92 bp); despite a smaller raw edge (+0.032 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: REINFORCING (phi 0.169); failure: COL offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT25COLNSH-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (4.20 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: MOSTLY_INDEPENDENT (phi -0.023); failure: NSH offense succeeds (4+ goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH wins by 2+; alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.38 vs 2.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: MOSTLY_INDEPENDENT (phi 0.038); failure: NSH offense suppressed (<= 2 goals)
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: REINFORCING (phi 0.169); KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.038); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3001): highest fidelity KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no — Broad expression KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4215): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.1875): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.169)
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3199, phi -0.162)
- KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4609, phi -0.213)
- KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.976)
- override: Broad expression KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.14 (adj +1.80) on $50.00, P(profit) 0.5352, adj growth 13.4 bp · B EV +3.88 (adj +1.35) on $47.19, P(profit) 0.7445, adj growth 12.1 bp · C EV +2.37 (adj +0.78) on $17.29, P(profit) 0.4958, adj growth 6.9 bp · R EV +0.43 (adj +0.19) on $7.00, P(profit) 0.4372, adj growth 6.4 bp

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 30 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.368 / away 0.632

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.117 | 0.50 | 0.50 | 0.00 | 6.01 | 22.0/34.4 | 30.5/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.56 | 0.44 | 0.00 | 6.08 | 27.8/28.5 | 25.1/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.47 | 0.53 | 0.45 | 5.9 | 22.4/34.4 | 30.9/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.98 | 27.9/28.7 | 25.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.41 | 29.4/30.3 | 24.4/23.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.084 | 0.48 | 0.52 | 0.00 | 9.26 | 23.9/35.8 | 29.3/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 2+ goals NO | 85 | 0.915 | 0.897 | +0.056 | +0.038 | $15.00 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.638 | +0.062 | +0.041 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 1.5 goals NO | 58 | 0.731 | 0.630 | +0.134 | +0.033 | $15.39 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (27.41 vs 16.69 bp); despite a smaller raw edge (+0.056 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.008 vs 0.466); relationships: KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.221); failure: MIN offense succeeds (4+ goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (27.41 vs 15.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.177); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (27.41 vs 9.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.221); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.221); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: REINFORCING (phi 0.177); failure: MIN wins by 2+

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.263)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.6 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2687, phi -1.0)

portfolios: A EV +14.05 (adj +3.04) on $50.00, P(profit) 0.6263, adj growth 20.9 bp · B EV +6.00 (adj +2.55) on $45.39, P(profit) 0.5193, adj growth 23.6 bp · C EV +7.36 (adj +4.21) on $34.85, P(profit) 0.3543, adj growth 37.1 bp · R EV +1.16 (adj +0.40) on $8.00, P(profit) 0.6963, adj growth 14.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
