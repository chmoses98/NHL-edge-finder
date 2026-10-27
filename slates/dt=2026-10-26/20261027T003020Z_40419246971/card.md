# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T00:30:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +10.19 | +1.56 | +14.23 | 0.646 | -29.73 | -29.73 | 12.50 |
| B thesis-diversified (joint) ← optimiser card | 31.53 | +5.54 | +1.73 | +2.94 | 0.775 | -29.49 | -31.53 | 15.64 |
| C best expression per thesis | 26.80 | +5.06 | +1.46 | +5.62 | 0.753 | -26.80 | -26.80 | 13.27 |
| R FUNDED research stakes | 1.00 | +0.04 | +0.02 | +0.86 | 0.559 | -1.00 | -1.00 | 0.00 |

## DET @ EDM  ·  10000 joint draws  ·  512 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.136 | 0.71 | 0.29 | 0.00 | 6.05 | 27.9/27.8 | 25.3/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.69 | 0.31 | 0.00 | 9.46 | 29.3/29.4 | 24.3/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.47 | 5.98 | 28.0/27.8 | 24.3/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.76 | 0.24 | 0.00 | 6.03 | 32.7/22.0 | 19.6/27.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.065 | 0.78 | 0.22 | 0.00 | 9.39 | 34.7/23.3 | 19.3/26.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.60 | 0.40 | 0.46 | 5.97 | 33.2/22.3 | 19.2/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor McDavid: 2+ assists NO | 60 | 0.753 | 0.650 | +0.136 | +0.033 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.300 | 0.288 | +0.026 | +0.015 | $6.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 16 | 0.190 | 0.181 | +0.020 | +0.012 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ goals NO | 52 | 0.559 | 0.548 | +0.021 | +0.010 | $1.10 | FUNDED_RESEARCH | $1 | EDM:SUPPRESSED | DIRECT (0.78) | EVIDENCE_STRONGER | D |
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (10.38 vs 4.37 bp); relationships: KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT26DETEDM-EDMLDRAISAITL29-1|no: REINFORCING (phi 0.263); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (2.49 vs 1.85 bp); despite a smaller raw edge (+0.026 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (2.49 vs 2.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT26DETEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: Player prop expression KXNHLGOAL-26OCT26DETEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.78 vs 0.73 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: REINFORCING (phi 0.263); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2642): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5294): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.335)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.217)
- KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.17)
- KXNHLGOAL-26OCT26DETEDM-EDMLDRAISAITL29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.26)
- override: Player prop expression KXNHLGOAL-26OCT26DETEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26OCT26DETEDM-EDMLDRAISAITL29-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.78 vs 0.73 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +10.19 (adj +1.56) on $50.00, P(profit) 0.6465, adj growth 12.5 bp · B EV +5.54 (adj +1.73) on $31.53, P(profit) 0.7754, adj growth 15.6 bp · C EV +5.06 (adj +1.46) on $26.80, P(profit) 0.7528, adj growth 13.3 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.5586, adj growth 0.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
