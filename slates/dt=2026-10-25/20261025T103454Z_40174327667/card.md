# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T10:34:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.25 | +6.48 | +21.94 | 0.619 | -56.58 | -81.26 | 43.03 |
| B thesis-diversified (joint) ← optimiser card | 92.81 | +14.86 | +5.46 | +10.91 | 0.646 | -30.16 | -41.88 | 47.82 |
| C best expression per thesis | 74.67 | +10.57 | +3.68 | +12.22 | 0.664 | -24.69 | -37.75 | 32.51 |
| R FUNDED research stakes | 24.00 | +3.95 | +1.48 | +3.01 | 0.569 | -10.09 | -14.52 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  436 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_FLA_win | p_overtime | goals | shots CHI/FLA | CHI/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.113 | 0.41 | 0.59 | 0.00 | 5.96 | 20.7/31.8 | 27.7/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.92 | 26.4/26.9 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.48 | 0.52 | 0.00 | 6.05 | 26.3/26.8 | 23.1/22.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.46 | 0.54 | 0.46 | 5.97 | 21.1/32.1 | 28.7/17.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.50 | 0.50 | 0.00 | 9.41 | 27.8/28.4 | 22.1/21.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.069 | 0.38 | 0.62 | 0.00 | 9.29 | 22.2/34.3 | 27.1/17.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.155 | 0.142 | +0.039 | +0.025 | $6.17 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 73 | 0.810 | 0.767 | +0.066 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.146 | 0.123 | +0.039 | +0.017 | $4.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.675 | 0.625 | +0.068 | +0.018 | $14.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (12.73 vs 6.39 bp); despite a smaller raw edge (+0.039 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT25FLACHI-FLA3|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT25FLACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.039); failure: CHI offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes; why: higher confidence-adjusted growth (6.39 vs 5.72 bp); wins across more scripts (relative breadth 1.013 vs 0.541); relationships: KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.18); KXNHLAST-26OCT25FLACHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: FLA wins by 2+
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (6.28 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.18); KXNHLAST-26OCT25FLACHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: FLA offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25FLACHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (2.98 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.039); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense succeeds (4+ goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3631): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis CHI:WINS (p 0.4731): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2577): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4148, phi -0.198)
- KXNHLSPREAD-26OCT25FLACHI-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3033, phi -0.735)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3798, phi -0.18)
- KXNHLAST-26OCT25FLACHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3631, phi -0.261)

portfolios: A EV +4.57 (adj +1.02) on $37.50, P(profit) 0.6725, adj growth 9.0 bp · B EV +7.12 (adj +3.08) on $45.29, P(profit) 0.6576, adj growth 27.0 bp · C EV +4.97 (adj +1.74) on $38.31, P(profit) 0.6091, adj growth 15.6 bp · R EV +1.10 (adj +0.58) on $7.00, P(profit) 0.1555, adj growth 19.4 bp

## NYI @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 5.99 | 26.0/25.8 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.89 | 26.1/26.1 | 22.9/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.66 | 0.34 | 0.00 | 5.92 | 30.8/20.4 | 17.8/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 9.18 | 27.6/27.6 | 22.1/21.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.58 | 0.42 | 0.48 | 5.81 | 30.7/20.4 | 17.4/27.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.45 | 2.8 | 24.5/24.6 | 23.2/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 17 | 0.223 | 0.199 | +0.043 | +0.019 | $4.29 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| New York I over 2.5 goals scored YES | 46 | 0.539 | 0.497 | +0.061 | +0.019 | $4.14 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 3.5 goals scored YES | 26 | 0.331 | 0.291 | +0.058 | +0.017 | $2.25 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 61 | 0.672 | 0.638 | +0.045 | +0.012 | $1.91 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes; why: higher confidence-adjusted growth (5.18 vs 3.30 bp); despite a smaller raw edge (+0.043 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: REINFORCING (phi 0.236); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: REINFORCING (phi 0.221); KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.132); failure: NYI offense suppressed (<= 2 goals)
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (5.18 vs 3.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.236); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: REINFORCING (phi 0.236); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: DUPLICATIVE (phi 0.652); KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: REINFORCING (phi 0.465); failure: NYI offense suppressed (<= 2 goals)
- **New York I over 3.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (5.18 vs 3.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.221); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: REINFORCING (phi 0.221); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: DUPLICATIVE (phi 0.652); KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: REINFORCING (phi 0.392); failure: NYI offense suppressed (<= 2 goals)
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no; why: higher confidence-adjusted growth (1.28 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: REINFORCING (phi 0.465); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: REINFORCING (phi 0.392); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3209): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes (same contract)
- thesis GAME:TIGHT (p 0.4414): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4727, phi -0.235)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4727, phi -0.978)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4727, phi -0.667)
- KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3283, phi -1.0)

portfolios: A EV +5.85 (adj +1.96) on $37.50, P(profit) 0.5595, adj growth 12.7 bp · B EV +2.18 (adj +0.79) on $12.59, P(profit) 0.4374, adj growth 6.9 bp · C EV +1.64 (adj +0.63) on $11.20, P(profit) 0.2232, adj growth 5.5 bp · R EV +1.02 (adj +0.37) on $6.00, P(profit) 0.4374, adj growth 11.3 bp

## MTL @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.46 | 0.54 | 0.00 | 6.01 | 27.3/27.1 | 23.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.48 | 5.9 | 27.3/27.3 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.46 | 0.54 | 0.00 | 9.31 | 28.7/28.7 | 22.5/22.8 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.081 | 0.53 | 0.47 | 0.00 | 5.99 | 32.1/21.8 | 18.4/28.5 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.48 | 5.83 | 32.3/21.7 | 18.6/29.0 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.058 | 0.38 | 0.62 | 0.00 | 5.94 | 21.5/31.6 | 27.4/18.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.120 | 0.35 | 0.65 | 0.00 | 5.98 | 22.7/35.5 | 31.1/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.39 | 0.61 | 0.00 | 6.06 | 28.6/29.4 | 25.1/25.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.46 | 0.54 | 0.49 | 5.95 | 22.8/35.2 | 31.8/19.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.45 | 5.93 | 28.7/29.4 | 26.1/25.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.093 | 0.32 | 0.68 | 0.00 | 9.35 | 24.5/37.5 | 29.0/19.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.38 | 0.62 | 0.00 | 9.53 | 30.4/31.1 | 23.8/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 2.5 goals NO | 67 | 0.754 | 0.707 | +0.068 | +0.021 | $16.10 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 3.5 goals scored NO | 44 | 0.519 | 0.474 | +0.061 | +0.017 | $2.92 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (4.63 vs 2.96 bp); despite a smaller raw edge (+0.068 vs +0.094/contract); wins across more scripts (relative breadth 1.011 vs 0.9); relationships: KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: REINFORCING (phi 0.502); failure: COL wins by 2+
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (4.63 vs 2.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.502); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: REINFORCING (phi 0.502); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4254): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis COL:SUPPRESSED (p 0.3188): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:WINS (p 0.4152): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3586, phi -0.765)
- KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4698, phi -0.977)

portfolios: A EV +5.06 (adj +1.27) on $37.50, P(profit) 0.6774, adj growth 8.8 bp · B EV +1.99 (adj +0.61) on $19.02, P(profit) 0.7536, adj growth 5.4 bp · C EV +1.85 (adj +0.58) on $18.64, P(profit) 0.7536, adj growth 5.1 bp · R EV +0.63 (adj +0.19) on $6.00, P(profit) 0.7536, adj growth 6.5 bp

## MIN @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.119 | 0.44 | 0.56 | 0.00 | 5.96 | 22.0/34.0 | 30.0/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.49 | 0.51 | 0.00 | 6.03 | 28.0/28.5 | 24.9/24.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.46 | 5.97 | 22.3/34.3 | 30.9/19.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.45 | 6.01 | 27.9/28.6 | 25.2/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.51 | 0.49 | 0.00 | 9.3 | 29.5/30.2 | 24.2/23.2 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 9.32 | 23.6/36.0 | 28.9/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 20 | 0.279 | 0.235 | +0.068 | +0.024 | $4.84 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 1.5 goals NO | 58 | 0.705 | 0.621 | +0.108 | +0.024 | $11.07 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT25MINVAN-MIN2|no; why: higher confidence-adjusted growth (7.18 vs 5.06 bp); despite a smaller raw edge (+0.068 vs +0.108/contract); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.403); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (7.18 vs 5.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.403); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: DUPLICATIVE (phi 0.403); failure: MIN wins by 2+

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2794): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:WINS (p 0.4933): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis MIN:SUPPRESSED (p 0.369): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.5067, phi -0.631)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.0 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2947, phi -1.0)

portfolios: A EV +9.76 (adj +2.23) on $37.50, P(profit) 0.4933, adj growth 12.5 bp · B EV +3.57 (adj +0.98) on $15.91, P(profit) 0.7053, adj growth 8.5 bp · C EV +2.10 (adj +0.73) on $6.52, P(profit) 0.2794, adj growth 6.3 bp · R EV +1.19 (adj +0.34) on $5.00, P(profit) 0.7053, adj growth 11.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
