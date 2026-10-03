# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T23:55:12Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.86 | +8.58 | +27.79 | 0.761 | -22.51 | -35.87 | 76.97 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +23.42 | +10.17 | +20.52 | 0.721 | -21.75 | -34.52 | 94.70 |
| C best expression per thesis | 150.01 | +25.66 | +10.16 | +20.68 | 0.704 | -25.69 | -37.77 | 92.45 |
| R FUNDED research stakes | 17.00 | +2.38 | +1.40 | +0.56 | 0.510 | -7.58 | -9.76 | 0.00 |

## DAL @ NSH  ·  10000 joint draws  ·  326 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.439 / away 0.561

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 5.98 | 27.1/27.4 | 24.0/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.51 | 0.49 | 0.46 | 5.89 | 27.1/27.4 | 24.0/23.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 6.01 | 21.6/31.9 | 27.9/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 9.21 | 28.7/28.8 | 23.1/22.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.46 | 0.54 | 0.49 | 5.9 | 21.6/32.1 | 28.7/18.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.49 | 2.86 | 25.4/25.6 | 24.1/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mikko Rantanen: 1+ goals NO | 69 | 0.752 | 0.735 | +0.047 | +0.030 | $12.61 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 79 | 0.851 | 0.818 | +0.049 | +0.016 | $9.99 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.216 | 0.206 | +0.026 | +0.015 | $2.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jason Robertson: 1+ goals NO | 62 | 0.659 | 0.647 | +0.022 | +0.010 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-2|no; why: higher confidence-adjusted growth (9.66 vs 9.48 bp); despite a smaller raw edge (+0.047 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: DAL offense succeeds (4+ goals)
- **Dallas wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: KXNHLSPREAD-26OCT03DALNSH-DAL2|no has the higher standalone adjusted growth (3.88 vs 3.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.715); relationships: KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.141); failure: DAL wins by 2+
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: KXNHLSPREAD-26OCT03DALNSH-DAL2|no has the higher standalone adjusted growth (3.88 vs 3.38 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.146); relationships: KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NSH offense suppressed (<= 2 goals)
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no; why: Player prop expression KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.81 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis DAL:SUPPRESSED (p 0.4393): highest fidelity KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no — Player prop expression KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.81 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NSH:WINS (p 0.5269): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3762): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT03DALNSH-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.225)
- KXNHLSPREAD-26OCT03DALNSH-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.255, phi -0.715)
- KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3986, phi -0.214)
- KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3461, phi -0.252)
- override: Player prop expression KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.81 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.75 (adj +0.77) on $30.00, P(profit) 0.6297, adj growth 6.5 bp · B EV +1.94 (adj +1.01) on $28.92, P(profit) 0.7029, adj growth 9.5 bp · C EV +2.25 (adj +1.11) on $30.08, P(profit) 0.5898, adj growth 10.1 bp · R EV +0.45 (adj +0.23) on $7.00, P(profit) 0.6623, adj growth 8.6 bp

## BOS @ MIN  ·  10000 joint draws  ·  334 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.646 / away 0.353

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.69 | 0.31 | 0.00 | 5.99 | 29.0/28.6 | 25.9/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.56 | 0.44 | 0.43 | 5.91 | 29.1/28.7 | 25.4/25.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.102 | 0.75 | 0.25 | 0.00 | 6.04 | 34.3/22.6 | 20.3/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.66 | 0.34 | 0.00 | 9.37 | 30.4/30.1 | 25.0/23.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.081 | 0.75 | 0.25 | 0.00 | 9.33 | 35.8/24.1 | 19.8/27.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.55 | 0.45 | 0.49 | 5.91 | 34.3/23.1 | 20.0/30.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 11 | 0.151 | 0.140 | +0.034 | +0.023 | $3.73 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 5 | 0.082 | 0.069 | +0.029 | +0.015 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 71 | 0.835 | 0.747 | +0.110 | +0.023 | $12.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Max Shabanov: 1+ assists NO | 68 | 0.792 | 0.713 | +0.097 | +0.018 | $11.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (10.66 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT03BOSMIN-MINMSHABANOV49-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: MIN offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (10.12 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03BOSMIN-MINMSHABANOV49-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: MIN offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03BOSMIN-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (5.68 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT03BOSMIN-MINMSHABANOV49-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: BOS offense succeeds (4+ goals)
- **Max Shabanov: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03BOSMIN-MINMSHABANOV49-1|no; why: higher confidence-adjusted growth (3.19 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, MIN shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.4699): highest fidelity KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3137): highest fidelity KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-BOSCMITTELSTADT11-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.5074): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2862, phi -0.135)
- KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2862, phi -0.12)
- KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3137, phi -0.207)
- KXNHLAST-26OCT03BOSMIN-MINMSHABANOV49-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.2 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.5074, phi -0.194)

portfolios: A EV +6.65 (adj +2.72) on $30.00, P(profit) 0.2215, adj growth 23.8 bp · B EV +5.82 (adj +2.06) on $30.30, P(profit) 0.7427, adj growth 18.9 bp · C EV +3.27 (adj +0.89) on $21.49, P(profit) 0.8685, adj growth 8.1 bp · R EV +0.29 (adj +0.19) on $1.00, P(profit) 0.151, adj growth 7.0 bp

## STL @ COL  ·  10000 joint draws  ·  334 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.158 | 0.71 | 0.29 | 0.00 | 6.04 | 33.7/21.4 | 18.8/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.57 | 0.43 | 0.47 | 5.91 | 34.1/21.8 | 18.6/30.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.108 | 0.75 | 0.25 | 0.00 | 9.44 | 35.5/22.8 | 18.4/27.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.68 | 0.32 | 0.00 | 6.04 | 28.3/27.3 | 24.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.55 | 0.45 | 0.50 | 6.01 | 28.4/27.5 | 24.2/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.67 | 0.33 | 0.00 | 9.43 | 29.6/28.7 | 23.3/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins NO | 28 | 0.369 | 0.327 | +0.075 | +0.033 | $5.68 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Pius Suter: 1+ goals YES | 11 | 0.148 | 0.138 | +0.031 | +0.021 | $2.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Connor McMichael: 1+ assists NO | 78 | 0.850 | 0.812 | +0.058 | +0.021 | $12.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.606 | 0.591 | +0.039 | +0.024 | $6.50 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (11.03 vs 6.12 bp); despite a smaller raw edge (+0.075 vs +0.122/contract); relationships: KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: REINFORCING (phi 0.169); KXNHLAST-26OCT03STLCOL-STLCMCMICHAEL77-1|no: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.196); failure: COL wins (incl. OT/SO)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (11.03 vs 8.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.169); they share one thesis budget; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.169); KXNHLAST-26OCT03STLCOL-STLCMCMICHAEL77-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: STL offense suppressed (<= 2 goals)
- **Connor McMichael: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03STLCOL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (5.62 vs 3.12 bp); despite a smaller raw edge (+0.058 vs +0.059/contract); relationships: KXNHLGAME-26OCT03STLCOL-COL|no: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: Player prop expression KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no selected over player prop KXNHLPTS-26OCT03STLCOL-COLCMAKAR8-2|no because adjusted EV is 0.2 pts higher while thesis capture is 0.80 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.196); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT03STLCOL-STLCMCMICHAEL77-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:WINS (p 0.3688): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3093): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.2955): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — Player prop expression KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no selected over player prop KXNHLPTS-26OCT03STLCOL-COLCMAKAR8-2|no because adjusted EV is 0.2 pts higher while thesis capture is 0.80 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6312, phi -1.0)
- KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4716, phi -0.205)
- KXNHLAST-26OCT03STLCOL-STLCMCMICHAEL77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3093, phi -0.18)
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5047, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no selected over player prop KXNHLPTS-26OCT03STLCOL-COLCMAKAR8-2|no because adjusted EV is 0.2 pts higher while thesis capture is 0.80 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +7.93 (adj +1.36) on $30.00, P(profit) 0.618, adj growth 11.5 bp · B EV +3.60 (adj +1.74) on $27.71, P(profit) 0.412, adj growth 16.1 bp · C EV +4.30 (adj +1.53) on $44.79, P(profit) 0.66, adj growth 14.1 bp · R EV +0.65 (adj +0.30) on $4.00, P(profit) 0.3688, adj growth 10.9 bp

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 28.1/28.2 | 24.9/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.94 | 28.4/28.4 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.37 | 29.8/29.9 | 24.3/23.1 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.66 | 0.34 | 0.00 | 6.01 | 32.8/22.3 | 19.6/28.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.067 | 0.53 | 0.47 | 0.00 | 6.01 | 22.6/33.3 | 29.5/19.0 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.46 | 5.94 | 22.8/33.6 | 30.2/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zayne Parekh: 1+ goals NO | 85 | 0.900 | 0.885 | +0.041 | +0.026 | $11.40 | FUNDED_RESEARCH | $3 | CGY:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 25 | 0.309 | 0.293 | +0.046 | +0.030 | $5.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Paul Cotter: 1+ goals NO | 83 | 0.872 | 0.861 | +0.032 | +0.021 | $11.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 22 | 0.263 | 0.251 | +0.031 | +0.019 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CGYVAN-CGY2|no; why: higher confidence-adjusted growth (12.36 vs 0.30 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: CGY offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (10.23 vs 4.43 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)
- **Paul Cotter: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no; why: higher confidence-adjusted growth (6.99 vs 0.00 bp); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (10.23 vs 4.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes (same contract)
- thesis CGY:SUPPRESSED (p 0.4316): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VAN:SUPPRESSED (p 0.3529): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.347, phi -0.129)
- KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.246)
- KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4345, phi -0.147)
- KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.236)

portfolios: A EV +2.67 (adj +1.70) on $30.00, P(profit) 0.4875, adj growth 15.7 bp · B EV +2.38 (adj +1.52) on $31.54, P(profit) 0.451, adj growth 14.4 bp · C EV +1.56 (adj +1.02) on $8.86, P(profit) 0.3095, adj growth 9.0 bp · R EV +0.14 (adj +0.09) on $3.00, P(profit) 0.8998, adj growth 3.5 bp

## LAK @ SJS  ·  10000 joint draws  ·  308 bet sides mapped, 16 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.52 | 0.48 | 0.00 | 6.02 | 27.1/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.92 | 27.4/27.8 | 24.5/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.53 | 0.47 | 0.00 | 9.28 | 29.0/29.4 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.50 | 0.50 | 0.00 | 5.99 | 22.0/32.6 | 28.8/18.7 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.47 | 0.53 | 0.52 | 5.9 | 22.0/33.0 | 29.6/18.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 5.93 | 32.2/21.8 | 18.9/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 58 | 0.818 | 0.660 | +0.221 | +0.063 | $12.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 13 | 0.197 | 0.179 | +0.059 | +0.041 | $6.71 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 67 | 0.808 | 0.715 | +0.123 | +0.030 | $12.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (36.20 vs 6.61 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (29.95 vs 0.94 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.04); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (9.04 vs 2.94 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4192): highest fidelity KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3857): highest fidelity KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4059): highest fidelity KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no (same contract)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 24.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3649, phi -0.197)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4059, phi -0.211)
- KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3857, phi -0.212)

portfolios: A EV +7.86 (adj +2.03) on $30.00, P(profit) 0.8437, adj growth 19.4 bp · B EV +9.68 (adj +3.84) on $31.54, P(profit) 0.7324, adj growth 35.9 bp · C EV +14.27 (adj +5.61) on $44.79, P(profit) 0.7545, adj growth 51.2 bp · R EV +0.85 (adj +0.59) on $2.00, P(profit) 0.1968, adj growth 21.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
