# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T01:36:40Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +23.29 | +5.63 | +10.43 | 0.544 | -46.93 | -60.06 | 37.97 |
| B thesis-diversified (joint) ← optimiser card | 96.27 | +11.70 | +5.26 | +11.62 | 0.634 | -28.85 | -40.13 | 47.65 |
| C best expression per thesis | 50.17 | +10.21 | +3.55 | +4.92 | 0.718 | -25.32 | -25.32 | 30.85 |
| R FUNDED research stakes | 16.00 | +2.29 | +0.78 | +2.32 | 0.710 | -5.31 | -10.18 | 0.00 |

## DET @ CGY  ·  10000 joint draws  ·  450 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_DET_win | p_overtime | goals | shots CGY/DET | CGY/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 5.98 | 28.1/28.4 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.45 | 5.87 | 28.6/28.7 | 25.6/25.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 5.95 | 22.8/34.1 | 30.3/19.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.87 | 22.7/34.2 | 30.7/19.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 9.22 | 30.2/30.6 | 24.5/23.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.54 | 0.46 | 0.00 | 3.49 | 27.4/27.7 | 25.8/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Moritz Seider: 1+ goals NO | 85 | 0.906 | 0.890 | +0.047 | +0.032 | $19.17 | FUNDED_RESEARCH | $5 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ben Jones: 1+ goals NO | 85 | 0.902 | 0.887 | +0.043 | +0.029 | $19.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 18 | 0.230 | 0.216 | +0.039 | +0.026 | $7.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 11 | 0.149 | 0.136 | +0.032 | +0.019 | $4.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (18.36 vs 6.46 bp); despite a smaller raw edge (+0.047 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense succeeds (4+ goals)
- **Ben Jones: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT24DETCGY-CGYBJONES39-1|no; why: higher confidence-adjusted growth (14.99 vs 2.47 bp); despite a smaller raw edge (+0.043 vs +0.125/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CGY offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes; why: higher confidence-adjusted growth (9.20 vs 7.37 bp); relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes has the higher standalone adjusted growth (9.20 vs 7.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4323): highest fidelity KXNHLTEAMTOTAL-26OCT24DETCGY-DET4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT24DETCGY-DETVARVIDSSON33-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:SUPPRESSED (p 0.4213): highest fidelity KXNHLPTS-26OCT24DETCGY-CGYBJONES39-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT24DETCGY-CGYBJONES39-1|no (same contract)
- KXNHLGOAL-26OCT24DETCGY-DETMSEIDER53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3499, phi -0.155)
- KXNHLGOAL-26OCT24DETCGY-CGYBJONES39-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.3555, phi -0.143)
- KXNHLGOAL-26OCT24DETCGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.197)
- KXNHLGOAL-26OCT24DETCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4213, phi -0.186)

portfolios: A EV +6.15 (adj +1.61) on $50.00, P(profit) 0.7576, adj growth 14.6 bp · B EV +4.72 (adj +3.03) on $50.00, P(profit) 0.3421, adj growth 27.7 bp · C EV +6.87 (adj +2.19) on $43.87, P(profit) 0.6585, adj growth 19.1 bp · R EV +0.27 (adj +0.18) on $5.00, P(profit) 0.9056, adj growth 7.1 bp

## MIN @ SEA  ·  10000 joint draws  ·  440 bet sides mapped, 29 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.389 / away 0.611

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_MIN_win | p_overtime | goals | shots SEA/MIN | SEA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 6.02 | 28.6/28.9 | 25.6/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.47 | 5.95 | 28.5/29.1 | 25.7/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 9.29 | 30.0/30.6 | 24.9/23.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.093 | 0.53 | 0.47 | 0.00 | 5.98 | 22.9/34.5 | 30.8/19.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.46 | 5.91 | 23.0/34.3 | 30.8/19.9 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.059 | 0.49 | 0.51 | 0.00 | 9.23 | 24.3/35.9 | 29.0/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 2+ goals NO | 87 | 0.919 | 0.904 | +0.041 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Minnesota wins NO | 37 | 0.535 | 0.424 | +0.148 | +0.038 | $9.21 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | CALIBRATION_WARNING | A |
| Minnesota wins by over 1.5 goals NO | 60 | 0.747 | 0.648 | +0.130 | +0.031 | $10.25 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Matt Boldy: 1+ goals NO | 60 | 0.648 | 0.635 | +0.032 | +0.018 | $6.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 14.39 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.107); relationships: KXNHLGAME-26OCT24MINSEA-MIN|no: REINFORCING (phi 0.185); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: REINFORCING (phi 0.202); KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 13.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.459); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.185); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: DUPLICATIVE (phi 0.624); KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: REINFORCING (phi 0.211); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes has the higher standalone adjusted growth (14.63 vs 9.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.286); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: REINFORCING (phi 0.202); KXNHLGAME-26OCT24MINSEA-MIN|no: DUPLICATIVE (phi 0.624); KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: REINFORCING (phi 0.191); failure: MIN wins by 2+
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT24MINSEA-SEA3|yes; why: Player prop expression KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGAME-26OCT24MINSEA-MIN|no: REINFORCING (phi 0.211); KXNHLSPREAD-26OCT24MINSEA-MIN2|no: REINFORCING (phi 0.191); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4115): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT24MINSEA-SEA|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3116): highest fidelity KXNHLGAME-26OCT24MINSEA-SEA|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT24MINSEA-SEA|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4218): highest fidelity KXNHLTEAMTOTAL-26OCT24MINSEA-MIN5|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT24MINSEA-SEA|yes — Player prop expression KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT24MINSEA-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.248)
- KXNHLGAME-26OCT24MINSEA-MIN|no: FUNDED_RESEARCH; family WARNING; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.0 pts; opposing: failure thesis MIN:WINS (p 0.4654, phi -1.0)
- KXNHLSPREAD-26OCT24MINSEA-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.2 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2531, phi -1.0)
- KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3593, phi -0.288)
- override: Player prop expression KXNHLGOAL-26OCT24MINSEA-MINMBOLDY12-1|no selected over player prop KXNHLAST-26OCT24MINSEA-MINMBOLDY12-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +17.14 (adj +4.02) on $50.00, P(profit) 0.579, adj growth 23.4 bp · B EV +6.98 (adj +2.23) on $46.27, P(profit) 0.6464, adj growth 20.0 bp · C EV +3.34 (adj +1.36) on $6.30, P(profit) 0.1949, adj growth 11.7 bp · R EV +2.02 (adj +0.60) on $11.00, P(profit) 0.5346, adj growth 21.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT24MINSEA-SEA|yes == KXNHLGAME-26OCT24MINSEA-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
