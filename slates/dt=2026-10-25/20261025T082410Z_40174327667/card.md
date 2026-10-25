# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T08:24:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +21.76 | +5.18 | +16.50 | 0.628 | -56.70 | -77.90 | 32.83 |
| B thesis-diversified (joint) ← optimiser card | 72.10 | +9.91 | +3.63 | +8.49 | 0.671 | -22.61 | -41.00 | 32.00 |
| C best expression per thesis | 75.57 | +9.38 | +3.15 | +15.86 | 0.660 | -26.07 | -33.93 | 27.91 |
| R FUNDED research stakes | 21.00 | +2.89 | +1.05 | +1.41 | 0.599 | -7.56 | -12.60 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 4 on card


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
| Ryan Greene: 1+ goals YES | 11 | 0.155 | 0.137 | +0.039 | +0.020 | $4.14 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 73 | 0.810 | 0.767 | +0.066 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Cole Schwindt: 1+ goals YES | 10 | 0.146 | 0.123 | +0.039 | +0.017 | $4.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Chicago wins by over 1.5 goals YES | 19 | 0.258 | 0.221 | +0.057 | +0.021 | $4.18 | FUNDED_RESEARCH | $2 | CHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (8.15 vs 6.39 bp); despite a smaller raw edge (+0.039 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT25FLACHI-FLA3|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: REINFORCING (phi 0.152); failure: CHI offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes; why: higher confidence-adjusted growth (6.39 vs 5.72 bp); wins across more scripts (relative breadth 1.013 vs 0.541); relationships: KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.18); KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: REINFORCING (phi 0.286); failure: FLA wins by 2+
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (6.28 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.18); KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: FLA offense suppressed (<= 2 goals)
- **Chicago wins by over 1.5 goals YES** — thesis: CHI wins by 2+; alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25FLACHI-FLA3|no has the higher standalone adjusted growth (6.39 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: REINFORCING (phi 0.152); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: REINFORCING (phi 0.286); KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: FLA wins (incl. OT/SO)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3631): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis CHI:WINS (p 0.4731): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2577): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4148, phi -0.198)
- KXNHLSPREAD-26OCT25FLACHI-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3033, phi -0.735)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3798, phi -0.18)
- KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5269, phi -0.622)

portfolios: A EV +4.23 (adj +1.02) on $39.47, P(profit) 0.6577, adj growth 8.3 bp · B EV +6.13 (adj +2.52) on $33.20, P(profit) 0.4606, adj growth 22.1 bp · C EV +4.29 (adj +1.49) on $33.60, P(profit) 0.6091, adj growth 13.4 bp · R EV +1.67 (adj +0.70) on $9.00, P(profit) 0.349, adj growth 21.6 bp

## NYI @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


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
| Dallas wins by over 2.5 goals NO | 73 | 0.794 | 0.759 | +0.050 | +0.016 | $16.81 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: higher confidence-adjusted growth (2.81 vs 1.28 bp); wins across more scripts (relative breadth 1.004 vs 0.895); relationships: only recommended bet in this game; failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis GAME:TIGHT (p 0.4414): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL3|no (same contract)
- KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3283, phi -0.729)

portfolios: A EV +2.20 (adj +0.63) on $31.58, P(profit) 0.6717, adj growth 4.4 bp · B EV +1.13 (adj +0.35) on $16.81, P(profit) 0.7938, adj growth 3.1 bp · C EV +1.13 (adj +0.35) on $16.81, P(profit) 0.7938, adj growth 3.1 bp · R EV +0.34 (adj +0.10) on $5.00, P(profit) 0.7938, adj growth 3.6 bp

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

## COL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


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
| Colorado wins by over 2.5 goals NO | 67 | 0.754 | 0.707 | +0.068 | +0.021 | $16.81 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nashville wins by over 1.5 goals YES | 17 | 0.216 | 0.191 | +0.036 | +0.011 | $1.36 | FUNDED_RESEARCH | $1 | NSH:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (4.63 vs 1.96 bp); despite a smaller raw edge (+0.068 vs +0.084/contract); wins across more scripts (relative breadth 1.011 vs 0.9); relationships: KXNHLSPREAD-26OCT25COLNSH-NSH2|yes: DUPLICATIVE (phi 0.3); failure: COL wins by 2+
- **Nashville wins by over 1.5 goals YES** — thesis: NSH wins by 2+; alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (4.63 vs 1.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.300); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.3); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4254): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis COL:SUPPRESSED (p 0.3188): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.216): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3586, phi -0.765)
- KXNHLSPREAD-26OCT25COLNSH-NSH2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.5848, phi -0.623)

portfolios: A EV +5.06 (adj +1.18) on $39.47, P(profit) 0.6774, adj growth 7.5 bp · B EV +1.94 (adj +0.60) on $18.16, P(profit) 0.7536, adj growth 5.3 bp · C EV +1.85 (adj +0.58) on $18.64, P(profit) 0.7536, adj growth 5.1 bp · R EV +0.70 (adj +0.21) on $6.00, P(profit) 0.7536, adj growth 7.0 bp

## MIN @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 1 on card


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
| Minnesota wins by over 1.5 goals NO | 58 | 0.705 | 0.621 | +0.108 | +0.024 | $3.93 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (7.18 vs 5.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.403); relationships: only recommended bet in this game; failure: MIN wins by 2+

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2794): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:WINS (p 0.4933): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis MIN:SUPPRESSED (p 0.369): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.0 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2947, phi -1.0)

portfolios: A EV +10.28 (adj +2.35) on $39.47, P(profit) 0.4933, adj growth 12.6 bp · B EV +0.71 (adj +0.16) on $3.93, P(profit) 0.7053, adj growth 1.5 bp · C EV +2.10 (adj +0.73) on $6.52, P(profit) 0.2794, adj growth 6.3 bp · R EV +0.18 (adj +0.04) on $1.00, P(profit) 0.7053, adj growth 1.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
