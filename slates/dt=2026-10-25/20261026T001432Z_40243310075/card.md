# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T00:14:32Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +14.48 | +3.19 | +22.23 | 0.626 | -50.00 | -50.00 | 22.19 |
| B thesis-diversified (joint) ← optimiser card | 30.00 | +2.77 | +1.49 | +6.87 | 0.603 | -14.98 | -14.98 | 14.14 |
| C best expression per thesis | 34.84 | +7.12 | +4.04 | -11.81 | 0.354 | -11.81 | -34.84 | 35.41 |
| R FUNDED research stakes | 4.00 | +0.21 | +0.14 | +0.61 | 0.915 | +0.61 | -4.00 | 0.00 |

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 33 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.366 / away 0.634

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
| Kirill Kaprizov: 2+ goals NO | 86 | 0.915 | 0.900 | +0.046 | +0.031 | $13.04 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.638 | +0.062 | +0.041 | $13.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 51 | 0.624 | 0.543 | +0.097 | +0.016 | $3.91 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: DUPLICATIVE (phi 0.393); failure: MIN offense succeeds (4+ goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (19.38 vs 15.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over broad KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.74 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: DUPLICATIVE (phi 0.393); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense succeeds (4+ goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.263)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.31)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-1|no selected over broad KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.74 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.48 (adj +3.19) on $50.00, P(profit) 0.6263, adj growth 22.2 bp · B EV +2.77 (adj +1.49) on $30.00, P(profit) 0.6032, adj growth 14.1 bp · C EV +7.12 (adj +4.04) on $34.84, P(profit) 0.3543, adj growth 35.4 bp · R EV +0.21 (adj +0.14) on $4.00, P(profit) 0.9148, adj growth 5.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
