# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T23:42:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +19.83 | +4.85 | +24.92 | 0.637 | -58.67 | -72.09 | 32.66 |
| B thesis-diversified (joint) ← optimiser card | 65.00 | +5.51 | +2.72 | +5.83 | 0.623 | -21.62 | -30.39 | 24.98 |
| C best expression per thesis | 46.36 | +8.45 | +4.47 | -2.29 | 0.353 | -23.34 | -25.32 | 39.17 |
| R FUNDED research stakes | 13.00 | +0.80 | +0.39 | +2.44 | 0.617 | -3.95 | -8.39 | 0.00 |

## COL @ NSH  ·  10000 joint draws  ·  464 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.130 | 0.30 | 0.70 | 0.00 | 6.02 | 22.7/35.3 | 30.6/20.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.35 | 0.65 | 0.00 | 6.02 | 28.7/29.5 | 25.2/25.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.46 | 5.93 | 22.9/35.4 | 31.8/19.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.47 | 0.53 | 0.47 | 5.93 | 28.4/29.4 | 26.0/25.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.096 | 0.29 | 0.71 | 0.00 | 9.32 | 24.4/37.1 | 28.3/19.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.33 | 0.67 | 0.00 | 9.4 | 30.2/30.9 | 23.6/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 77 | 0.815 | 0.803 | +0.033 | +0.020 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 66 | 0.733 | 0.694 | +0.058 | +0.018 | $10.71 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.138 | 0.130 | +0.021 | +0.013 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Colorado over 3.5 goals scored NO | 43 | 0.500 | 0.463 | +0.053 | +0.015 | $1.24 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (5.39 vs 3.67 bp); despite a smaller raw edge (+0.033 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.018 vs 0.882); relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: REINFORCING (phi 0.189); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.67 vs 3.43 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.755); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: REINFORCING (phi 0.523); failure: COL wins by 2+
- **Adam Edstrom: 1+ goals YES** — thesis: NSH wins by 2+; alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.67 vs 3.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.142); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT25COLNSH-COL3|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: MOSTLY_INDEPENDENT (phi 0.054); failure: NSH offense suppressed (<= 2 goals)
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: Broad expression KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.72 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: REINFORCING (phi 0.189); KXNHLSPREAD-26OCT25COLNSH-COL3|no: REINFORCING (phi 0.523); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.054); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis COL:SUPPRESSED (p 0.3049): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no — Broad expression KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.72 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4164): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.1942): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- KXNHLGOAL-26OCT25COLNSH-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4893, phi -0.19)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3894, phi -0.755)
- KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4518, phi -0.196)
- KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4893, phi -0.979)
- override: Broad expression KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no selected over player prop KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.72 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.79 (adj +1.81) on $50.00, P(profit) 0.5363, adj growth 11.8 bp · B EV +2.45 (adj +1.19) on $35.00, P(profit) 0.6519, adj growth 10.5 bp · C EV +1.33 (adj +0.43) on $11.52, P(profit) 0.6106, adj growth 3.8 bp · R EV +0.59 (adj +0.25) on $9.00, P(profit) 0.6205, adj growth 8.6 bp

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 33 +EV candidates, 3 on card

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
| Kirill Kaprizov: 2+ goals NO | 86 | 0.915 | 0.900 | +0.046 | +0.031 | $12.24 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.638 | +0.062 | +0.041 | $12.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 50 | 0.624 | 0.540 | +0.107 | +0.023 | $5.51 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: DUPLICATIVE (phi 0.393); failure: MIN offense succeeds (4+ goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (19.38 vs 15.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT25MINVAN-MINOMAATTA3-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.80 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: DUPLICATIVE (phi 0.393); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT25MINVAN-MINOMAATTA3-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.80 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VAN:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.263)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.9 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.31)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT25MINVAN-MINOMAATTA3-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.80 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.05 (adj +3.04) on $50.00, P(profit) 0.6263, adj growth 20.9 bp · B EV +3.07 (adj +1.53) on $30.00, P(profit) 0.6032, adj growth 14.5 bp · C EV +7.12 (adj +4.04) on $34.84, P(profit) 0.3543, adj growth 35.4 bp · R EV +0.21 (adj +0.14) on $4.00, P(profit) 0.9148, adj growth 5.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
