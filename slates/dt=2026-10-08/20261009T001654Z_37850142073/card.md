# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T00:16:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +28.39 | +5.19 | +31.90 | 0.704 | -41.04 | -56.72 | 41.59 |
| B thesis-diversified (joint) ← optimiser card | 78.34 | +14.15 | +4.45 | +15.73 | 0.703 | -31.58 | -44.72 | 39.39 |
| C best expression per thesis | 62.06 | +14.43 | +5.48 | +17.38 | 0.587 | -35.51 | -38.79 | 47.65 |
| R FUNDED research stakes | 11.00 | +1.19 | +0.61 | +1.25 | 0.594 | -7.41 | -7.41 | 0.00 |

## COL @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 36 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.324 / away 0.676

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.36 | 0.64 | 0.00 | 6.0 | 22.9/35.5 | 30.9/20.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.48 | 0.52 | 0.50 | 5.91 | 23.1/35.5 | 32.0/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.42 | 0.58 | 0.00 | 5.97 | 28.6/29.5 | 25.5/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.46 | 5.94 | 28.9/29.7 | 26.5/25.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.084 | 0.36 | 0.64 | 0.00 | 9.28 | 24.2/37.2 | 29.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.41 | 0.59 | 0.00 | 9.24 | 30.1/31.2 | 24.5/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 56 | 0.644 | 0.622 | +0.067 | +0.044 | $16.62 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 2+ points NO | 47 | 0.721 | 0.529 | +0.234 | +0.042 | $13.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.94) | CALIBRATION_WARNING | D |
| Colorado wins by over 1.5 goals NO | 54 | 0.662 | 0.580 | +0.105 | +0.022 | $5.60 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (17.82 vs 15.19 bp); despite a smaller raw edge (+0.067 vs +0.234/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no: REINFORCING (phi 0.481); KXNHLSPREAD-26OCT08COLCGY-COL2|no: REINFORCING (phi 0.204); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 2+ points NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no has the higher standalone adjusted growth (17.82 vs 15.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.481); they share one thesis budget; relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: REINFORCING (phi 0.481); KXNHLSPREAD-26OCT08COLCGY-COL2|no: REINFORCING (phi 0.281); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL3|no; why: Broad expression KXNHLSPREAD-26OCT08COLCGY-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT08COLCGY-COL6|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: REINFORCING (phi 0.204); KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no: REINFORCING (phi 0.281); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3484): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.221): highest fidelity KXNHLSPREAD-26OCT08COLCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4375): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — Broad expression KXNHLSPREAD-26OCT08COLCGY-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT08COLCGY-COL6|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.263)
- KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 25.6 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.376)
- KXNHLSPREAD-26OCT08COLCGY-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.7 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3376, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT08COLCGY-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT08COLCGY-COL6|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +21.23 (adj +3.47) on $50.00, P(profit) 0.7613, adj growth 27.2 bp · B EV +9.40 (adj +2.65) on $35.60, P(profit) 0.7122, adj growth 23.5 bp · C EV +10.27 (adj +3.13) on $35.25, P(profit) 0.5976, adj growth 27.5 bp · R EV +0.95 (adj +0.47) on $7.00, P(profit) 0.644, adj growth 16.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08COLCGY-CGY|yes == KXNHLGAME-26OCT08COLCGY-COL|no

## TOR @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.601 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.153 | 0.76 | 0.24 | 0.00 | 5.99 | 34.0/21.4 | 19.1/29.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.59 | 0.41 | 0.48 | 5.92 | 34.3/21.7 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.04 | 28.4/27.7 | 25.0/24.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 9.28 | 36.0/23.0 | 18.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.47 | 0.49 | 5.96 | 28.4/27.7 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.73 | 0.27 | 0.00 | 9.35 | 30.1/29.2 | 24.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Auston Matthews: 1+ goals NO | 65 | 0.704 | 0.690 | +0.038 | +0.024 | $15.70 | FUNDED_RESEARCH | $4 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ assists NO | 60 | 0.685 | 0.640 | +0.068 | +0.023 | $14.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Ivan Barbashev: 1+ assists YES | 31 | 0.383 | 0.344 | +0.058 | +0.019 | $5.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Shea Theodore: 1+ assists YES | 35 | 0.430 | 0.385 | +0.065 | +0.019 | $6.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.51 vs 5.00 bp); despite a smaller raw edge (+0.038 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no has the higher standalone adjusted growth (5.51 vs 5.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: TOR offense succeeds (4+ goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (3.56 vs 3.51 bp); despite a smaller raw edge (+0.058 vs +0.065/contract); relationships: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes: MOSTLY_INDEPENDENT (phi 0.078); failure: VGK offense suppressed (<= 2 goals)
- **Shea Theodore: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes has the higher standalone adjusted growth (3.56 vs 3.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.078); they share one thesis budget; relationships: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.078); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:SUPPRESSED (p 0.5076): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.5093): highest fidelity KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2885): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.277)
- KXNHLAST-26OCT08TORVGK-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.25)
- KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.268)
- KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.251)

portfolios: A EV +7.15 (adj +1.72) on $50.00, P(profit) 0.6584, adj growth 14.4 bp · B EV +4.75 (adj +1.80) on $42.74, P(profit) 0.5663, adj growth 15.9 bp · C EV +4.16 (adj +2.35) on $26.81, P(profit) 0.3122, adj growth 20.1 bp · R EV +0.23 (adj +0.14) on $4.00, P(profit) 0.7044, adj growth 5.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
