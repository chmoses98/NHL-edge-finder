# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T00:14:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +29.71 | +5.60 | +29.30 | 0.672 | -44.58 | -63.63 | 37.38 |
| B thesis-diversified (joint) ← optimiser card | 57.97 | +9.94 | +5.11 | +3.98 | 0.525 | -33.79 | -33.79 | 44.28 |
| C best expression per thesis | 59.14 | +12.62 | +4.13 | +15.34 | 0.608 | -31.51 | -32.59 | 36.01 |
| R FUNDED research stakes | 8.00 | +0.56 | +0.33 | -0.42 | 0.381 | -8.00 | -8.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.646 / away 0.354

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.73 | 0.27 | 0.00 | 6.03 | 33.8/21.9 | 19.5/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.06 | 28.4/27.9 | 25.1/24.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.102 | 0.72 | 0.28 | 0.00 | 9.42 | 35.8/23.6 | 19.1/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.67 | 0.33 | 0.00 | 9.4 | 30.1/29.4 | 24.2/22.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.56 | 0.44 | 0.50 | 5.99 | 34.4/22.6 | 19.4/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.52 | 0.48 | 0.45 | 5.94 | 28.5/28.0 | 24.7/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Fedor Svechkov: 1+ goals YES | 10 | 0.141 | 0.128 | +0.035 | +0.022 | $5.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.143 | 0.134 | +0.026 | +0.017 | $4.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 51 | 0.568 | 0.552 | +0.041 | +0.025 | $13.22 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 26 | 0.307 | 0.294 | +0.033 | +0.020 | $6.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (10.79 vs 4.55 bp); relationships: KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: COL offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16PITCOL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (6.00 vs 0.34 bp); despite a smaller raw edge (+0.026 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: PIT offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no; why: Player prop expression KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.79 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (4.55 vs 0.49 bp); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.27): highest fidelity KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no — Player prop expression KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.79 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis PIT:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes (same contract)
- thesis PIT:WINS (p 0.3739): highest fidelity KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.27, phi -0.142)
- KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4473, phi -0.205)
- KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.286)
- KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.27, phi -0.207)
- override: Player prop expression KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.79 vs 0.77 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +16.14 (adj +2.20) on $50.00, P(profit) 0.5454, adj growth 13.9 bp · B EV +4.64 (adj +2.90) on $29.87, P(profit) 0.3903, adj growth 25.1 bp · C EV +7.74 (adj +2.42) on $32.11, P(profit) 0.5545, adj growth 21.1 bp · R EV +0.31 (adj +0.19) on $4.00, P(profit) 0.568, adj growth 6.4 bp

## BOS @ ANA  ·  10000 joint draws  ·  454 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.498 / away 0.502

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.122 | 0.59 | 0.41 | 0.00 | 6.11 | 34.6/22.3 | 19.3/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.55 | 0.45 | 0.00 | 6.07 | 28.8/28.2 | 24.8/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.53 | 0.47 | 0.00 | 9.54 | 30.2/29.5 | 23.4/23.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.103 | 0.64 | 0.36 | 0.00 | 9.39 | 35.8/23.5 | 18.5/28.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.54 | 0.46 | 0.47 | 6.0 | 34.0/22.1 | 18.9/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.54 | 0.46 | 0.47 | 5.99 | 28.8/28.1 | 24.7/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.235 | 0.170 | +0.087 | +0.022 | $4.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.133 | 0.122 | +0.027 | +0.016 | $4.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 62 | 0.676 | 0.659 | +0.040 | +0.023 | $15.39 | FUNDED_RESEARCH | $4 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 15 | 0.182 | 0.173 | +0.024 | +0.014 | $3.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes; why: higher confidence-adjusted growth (7.97 vs 4.05 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.884 vs 0.323); relationships: KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT16BOSANA-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (7.97 vs 5.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT16BOSANA-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (5.02 vs 2.21 bp); despite a smaller raw edge (+0.040 vs +0.096/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT16BOSANA-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: BOS offense succeeds (4+ goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT16BOSANA-9|yes; why: KXNHLTOTAL-26OCT16BOSANA-9|yes has the higher standalone adjusted growth (3.49 vs 3.27 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.114); relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4805): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3771): highest fidelity KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.3416): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4|yes [DIRECT], best adjusted EV KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3137, phi -0.214)
- KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3137, phi -0.16)
- KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4104, phi -0.252)
- KXNHLGOAL-26OCT16BOSANA-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3771, phi -0.176)

portfolios: A EV +13.57 (adj +3.40) on $50.00, P(profit) 0.4541, adj growth 23.5 bp · B EV +5.30 (adj +2.21) on $28.10, P(profit) 0.4201, adj growth 19.2 bp · C EV +4.88 (adj +1.71) on $27.03, P(profit) 0.7732, adj growth 14.9 bp · R EV +0.25 (adj +0.14) on $4.00, P(profit) 0.676, adj growth 5.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
