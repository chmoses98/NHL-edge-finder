# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T04:47:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +21.73 | +6.02 | +19.09 | 0.623 | -57.62 | -81.25 | 40.12 |
| B thesis-diversified (joint) ← optimiser card | 84.61 | +10.01 | +3.39 | +13.82 | 0.633 | -29.38 | -36.99 | 29.77 |
| C best expression per thesis | 57.82 | +6.87 | +2.36 | +16.57 | 0.545 | -28.64 | -30.92 | 20.86 |
| R FUNDED research stakes | 26.00 | +3.52 | +1.17 | +3.07 | 0.619 | -10.57 | -12.36 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_FLA_win | p_overtime | goals | shots CHI/FLA | CHI/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.112 | 0.40 | 0.60 | 0.00 | 5.99 | 20.7/32.0 | 27.7/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.49 | 0.51 | 0.00 | 6.01 | 26.3/26.8 | 23.2/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.48 | 5.97 | 26.5/27.1 | 23.7/23.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.46 | 5.92 | 21.2/32.3 | 28.9/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 9.4 | 27.6/28.4 | 22.1/21.5 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.070 | 0.38 | 0.62 | 0.00 | 9.34 | 22.2/33.9 | 26.4/17.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 73 | 0.810 | 0.767 | +0.066 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago wins by over 1.5 goals YES | 19 | 0.258 | 0.221 | +0.057 | +0.021 | $4.21 | FUNDED_RESEARCH | $2 | CHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes; why: higher confidence-adjusted growth (6.39 vs 5.72 bp); wins across more scripts (relative breadth 1.013 vs 0.539); relationships: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: REINFORCING (phi 0.286); failure: FLA wins by 2+
- **Chicago wins by over 1.5 goals YES** — thesis: CHI wins by 2+; alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25FLACHI-FLA3|no has the higher standalone adjusted growth (6.39 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25FLACHI-FLA3|no: REINFORCING (phi 0.286); failure: FLA wins (incl. OT/SO)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:WINS (p 0.4731): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2577): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis FLA:SUPPRESSED (p 0.3798): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLSPREAD-26OCT25FLACHI-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3033, phi -0.735)
- KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5269, phi -0.622)

portfolios: A EV +6.18 (adj +2.15) on $39.47, P(profit) 0.6967, adj growth 15.2 bp · B EV +2.96 (adj +1.06) on $24.21, P(profit) 0.8096, adj growth 9.4 bp · C EV +1.77 (adj +0.63) on $20.00, P(profit) 0.8096, adj growth 5.8 bp · R EV +1.01 (adj +0.36) on $7.00, P(profit) 0.2577, adj growth 11.9 bp

## NYI @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.56 | 0.44 | 0.00 | 5.98 | 26.0/25.8 | 22.7/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.89 | 26.1/26.1 | 22.9/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.65 | 0.35 | 0.00 | 5.96 | 30.9/20.4 | 17.8/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.58 | 0.42 | 0.00 | 9.21 | 27.5/27.6 | 21.9/21.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.47 | 5.81 | 30.9/20.6 | 17.5/27.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.46 | 2.79 | 24.5/24.6 | 23.2/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 1.5 goals NO | 60 | 0.672 | 0.633 | +0.055 | +0.017 | $9.85 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 2.5 goals scored YES | 47 | 0.539 | 0.499 | +0.051 | +0.012 | $2.32 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no; why: higher confidence-adjusted growth (2.54 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: REINFORCING (phi 0.465); failure: DAL wins by 2+
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no has the higher standalone adjusted growth (2.54 vs 1.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.465); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: REINFORCING (phi 0.465); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis GAME:TIGHT (p 0.4414): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3209): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3283, phi -1.0)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4727, phi -0.978)

portfolios: A EV +3.06 (adj +0.81) on $31.58, P(profit) 0.5386, adj growth 5.1 bp · B EV +1.12 (adj +0.32) on $12.17, P(profit) 0.6717, adj growth 2.8 bp · C EV +1.01 (adj +0.30) on $11.30, P(profit) 0.6717, adj growth 2.7 bp · R EV +0.37 (adj +0.10) on $4.00, P(profit) 0.6717, adj growth 3.5 bp

## MTL @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.47 | 0.53 | 0.00 | 5.99 | 27.2/27.1 | 23.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.49 | 0.51 | 0.48 | 5.94 | 27.3/27.3 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.46 | 0.54 | 0.00 | 9.36 | 28.7/28.7 | 22.5/22.7 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.082 | 0.51 | 0.49 | 0.00 | 5.99 | 31.9/21.7 | 18.3/28.3 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.53 | 0.47 | 0.48 | 5.81 | 32.5/21.7 | 18.7/29.1 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.057 | 0.37 | 0.63 | 0.00 | 5.98 | 21.6/31.7 | 27.3/18.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.34 | 0.66 | 0.00 | 6.0 | 22.8/35.4 | 31.0/20.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.41 | 0.59 | 0.00 | 6.04 | 28.6/29.5 | 25.5/25.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.46 | 0.54 | 0.48 | 5.92 | 22.7/35.1 | 31.7/19.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.47 | 0.53 | 0.46 | 5.96 | 28.7/29.3 | 25.9/25.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.093 | 0.33 | 0.67 | 0.00 | 9.35 | 24.3/37.2 | 29.1/19.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.38 | 0.62 | 0.00 | 9.5 | 30.6/31.6 | 24.3/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 2.5 goals NO | 67 | 0.754 | 0.709 | +0.068 | +0.024 | $19.42 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nashville wins by over 1.5 goals YES | 17 | 0.216 | 0.191 | +0.036 | +0.011 | $1.19 | FUNDED_RESEARCH | $1 | NSH:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no; why: higher confidence-adjusted growth (5.79 vs 1.35 bp); wins across more scripts (relative breadth 1.011 vs 0.892); relationships: KXNHLSPREAD-26OCT25COLNSH-NSH2|yes: DUPLICATIVE (phi 0.3); failure: COL wins by 2+
- **Nashville wins by over 1.5 goals YES** — thesis: NSH wins by 2+; alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (5.79 vs 1.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.300); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.3); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4254): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.216): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:WINS (p 0.4152): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3586, phi -0.765)
- KXNHLSPREAD-26OCT25COLNSH-NSH2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.5848, phi -0.623)

portfolios: A EV +3.83 (adj +1.03) on $39.47, P(profit) 0.5186, adj growth 6.7 bp · B EV +2.17 (adj +0.75) on $20.62, P(profit) 0.7536, adj growth 6.6 bp · C EV +1.99 (adj +0.70) on $20.00, P(profit) 0.7536, adj growth 6.2 bp · R EV +0.70 (adj +0.23) on $6.00, P(profit) 0.7536, adj growth 7.8 bp

## MIN @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.49 | 0.51 | 0.00 | 5.99 | 27.7/28.4 | 24.8/24.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.113 | 0.45 | 0.55 | 0.00 | 5.99 | 22.2/34.2 | 30.2/19.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.46 | 5.94 | 22.2/34.1 | 30.8/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.44 | 6.05 | 28.1/28.8 | 25.3/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.51 | 0.49 | 0.00 | 9.29 | 29.6/30.3 | 24.4/23.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.088 | 0.42 | 0.58 | 0.00 | 9.34 | 23.9/36.2 | 29.1/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 20 | 0.279 | 0.235 | +0.068 | +0.024 | $4.29 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 73 | 0.816 | 0.768 | +0.072 | +0.024 | $19.65 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota over 2.5 goals scored NO | 28 | 0.359 | 0.315 | +0.065 | +0.020 | $1.11 | FUNDED_RESEARCH | $1 | MIN:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Minnesota over 4.5 goals scored NO | 69 | 0.766 | 0.723 | +0.061 | +0.018 | $2.57 | FUNDED_RESEARCH | $1 | VAN:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT25MINVAN-MIN3|no; why: higher confidence-adjusted growth (7.18 vs 6.72 bp); despite a smaller raw edge (+0.068 vs +0.072/contract); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN3|no: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3|no: REINFORCING (phi 0.497); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: DUPLICATIVE (phi 0.313); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (7.18 vs 6.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.296); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3|no: DUPLICATIVE (phi 0.356); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: REINFORCING (phi 0.491); failure: MIN wins by 2+
- **Minnesota over 2.5 goals scored NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3|no selected over broad KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.97 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: REINFORCING (phi 0.497); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: DUPLICATIVE (phi 0.356); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: DUPLICATIVE (phi 0.413); failure: MIN offense succeeds (4+ goals)
- **Minnesota over 4.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (7.18 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.313); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: DUPLICATIVE (phi 0.313); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: REINFORCING (phi 0.491); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3|no: DUPLICATIVE (phi 0.413); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2794): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN3|no (same contract)
- thesis VAN:WINS (p 0.4933): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN3|no (same contract)
- thesis MIN:SUPPRESSED (p 0.369): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN3|no (same contract)
- KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.5067, phi -0.631)
- KXNHLSPREAD-26OCT25MINVAN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2947, phi -0.735)
- KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4133, phi -0.628)
- KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4133, phi -0.658)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25MINVAN-MIN2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3|no selected over broad KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no because adjusted EV is 0.6 pts higher while thesis capture is 0.97 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.66 (adj +2.03) on $39.47, P(profit) 0.4933, adj growth 13.1 bp · B EV +3.75 (adj +1.26) on $27.61, P(profit) 0.7114, adj growth 11.0 bp · C EV +2.10 (adj +0.73) on $6.52, P(profit) 0.2794, adj growth 6.3 bp · R EV +1.44 (adj +0.48) on $9.00, P(profit) 0.4311, adj growth 15.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
