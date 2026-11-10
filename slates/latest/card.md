# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T02:43:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 45.20 | +5.08 | +2.60 | -4.21 | 0.448 | -17.22 | -45.20 | 21.29 |
| B thesis-diversified (joint) ← optimiser card | 35.96 | +3.86 | +1.87 | -7.98 | 0.448 | -11.05 | -35.96 | 16.45 |
| C best expression per thesis | 25.46 | +2.54 | +1.08 | +2.53 | 0.836 | -25.46 | -25.46 | 9.52 |
| R FUNDED research stakes | 2.00 | +0.28 | +0.17 | -2.00 | 0.229 | -2.00 | -2.00 | 0.00 |

## NYI @ SJS  ·  10000 joint draws  ·  476 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.440 / away 0.560

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_NYI_win | p_overtime | goals | shots SJS/NYI | SJS/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.50 | 0.50 | 0.00 | 6.02 | 27.6/27.8 | 24.2/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.52 | 0.48 | 0.46 | 5.97 | 27.8/28.0 | 24.8/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 9.21 | 29.0/29.4 | 23.2/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.074 | 0.44 | 0.56 | 0.00 | 6.03 | 22.1/32.6 | 28.4/18.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.46 | 0.54 | 0.49 | 5.92 | 22.0/32.6 | 29.1/18.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.55 | 0.45 | 0.00 | 6.03 | 32.7/22.1 | 18.9/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ assists NO | 70 | 0.778 | 0.736 | +0.063 | +0.022 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Michael Misa: 1+ goals YES | 19 | 0.229 | 0.218 | +0.028 | +0.017 | $5.54 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 18 | 0.216 | 0.205 | +0.025 | +0.015 | $4.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 21 | 0.248 | 0.237 | +0.026 | +0.016 | $5.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (5.08 vs 0.76 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (4.08 vs 3.22 bp); relationships: KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes has the higher standalone adjusted growth (4.08 vs 3.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes has the higher standalone adjusted growth (4.08 vs 3.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3926): highest fidelity KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3896): highest fidelity KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26NOV09NYISJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3896, phi -0.214)
- KXNHLGOAL-26NOV09NYISJ-SJMMISA77-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3926, phi -0.207)
- KXNHLGOAL-26NOV09NYISJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3926, phi -0.213)
- KXNHLGOAL-26NOV09NYISJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3926, phi -0.205)

portfolios: A EV +5.08 (adj +2.60) on $45.20, P(profit) 0.4479, adj growth 21.3 bp · B EV +3.86 (adj +1.87) on $35.96, P(profit) 0.4479, adj growth 16.4 bp · C EV +2.54 (adj +1.08) on $25.46, P(profit) 0.836, adj growth 9.5 bp · R EV +0.28 (adj +0.17) on $2.00, P(profit) 0.2292, adj growth 5.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
