# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T10:36:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +9.73 | +2.35 | +26.99 | 0.576 | -52.02 | -70.00 | 15.11 |
| B thesis-diversified (joint) ← optimiser card | 29.54 | +4.43 | +1.12 | +5.19 | 0.705 | -19.32 | -29.53 | 9.90 |
| C best expression per thesis | 20.67 | +3.59 | +0.80 | +7.16 | 0.681 | -20.66 | -20.66 | 7.06 |
| R FUNDED research stakes | 11.00 | +1.63 | +0.41 | +1.70 | 0.705 | -6.81 | -11.00 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.57 | 0.43 | 0.00 | 6.03 | 26.8/27.3 | 24.1/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.104 | 0.49 | 0.51 | 0.00 | 6.03 | 21.2/32.6 | 28.9/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.47 | 5.96 | 26.5/27.0 | 23.8/23.2 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.45 | 0.55 | 0.46 | 5.98 | 21.3/32.8 | 29.3/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.36 | 28.5/29.0 | 23.5/22.0 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 9.32 | 22.8/34.3 | 28.0/17.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.137 | 0.39 | 0.61 | 0.00 | 6.0 | 21.4/33.4 | 29.2/18.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.46 | 0.54 | 0.47 | 5.86 | 21.5/33.8 | 30.5/18.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 5.94 | 26.9/27.8 | 24.1/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.48 | 0.52 | 0.48 | 5.88 | 27.0/27.9 | 24.7/23.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.080 | 0.36 | 0.64 | 0.00 | 9.08 | 22.6/35.2 | 27.8/18.0 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.071 | 0.41 | 0.59 | 0.00 | 3.46 | 20.0/32.2 | 29.9/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 1.5 goals NO | 55 | 0.681 | 0.593 | +0.113 | +0.025 | $4.39 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 68 | 0.798 | 0.718 | +0.102 | +0.023 | $12.19 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 17 | 0.231 | 0.198 | +0.051 | +0.018 | $3.03 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 4.5 goals scored NO | 71 | 0.790 | 0.742 | +0.065 | +0.018 | $5.05 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT19COLPHI-COL3|no; why: higher confidence-adjusted growth (5.64 vs 5.34 bp); relationships: KXNHLSPREAD-26OCT19COLPHI-COL3|no: DUPLICATIVE (phi 0.735); KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: DUPLICATIVE (phi 0.376); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.507); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT19COLPHI-COL2|no has the higher standalone adjusted growth (5.64 vs 5.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.735); they share one thesis budget; relationships: KXNHLSPREAD-26OCT19COLPHI-COL2|no: DUPLICATIVE (phi 0.735); KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: REINFORCING (phi 0.276); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.536); failure: COL wins by 2+
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT19COLPHI-COL2|no has the higher standalone adjusted growth (5.64 vs 4.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.376); they share one thesis budget; relationships: KXNHLSPREAD-26OCT19COLPHI-COL2|no: DUPLICATIVE (phi 0.376); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.276); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.27); failure: COL wins (incl. OT/SO)
- **Colorado over 4.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: Broad expression KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.44 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT19COLPHI-COL2|no: REINFORCING (phi 0.507); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.536); KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: REINFORCING (phi 0.27); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.2312): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.3909): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — Broad expression KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.44 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT19COLPHI-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.6 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3194, phi -1.0)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.3 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3194, phi -0.735)
- KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.5533, phi -0.61)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.44 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.94 (adj +1.92) on $50.00, P(profit) 0.6453, adj growth 13.0 bp · B EV +3.99 (adj +1.02) on $24.66, P(profit) 0.6806, adj growth 9.0 bp · C EV +3.15 (adj +0.70) on $15.79, P(profit) 0.6806, adj growth 6.1 bp · R EV +1.45 (adj +0.37) on $9.00, P(profit) 0.6806, adj growth 12.2 bp

## SJS @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.05 | 28.0/28.4 | 25.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.45 | 5.91 | 28.0/28.3 | 25.1/24.5 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.088 | 0.48 | 0.52 | 0.00 | 5.98 | 22.2/33.6 | 29.8/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.53 | 0.47 | 0.00 | 9.37 | 29.8/30.0 | 24.0/23.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.51 | 5.92 | 22.6/33.9 | 30.4/19.5 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.51 | 0.49 | 0.00 | 9.32 | 24.1/35.2 | 28.6/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 6.5 goals scored NO | 46 | 0.520 | 0.488 | +0.043 | +0.010 | $4.88 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-4|no; why: higher confidence-adjusted growth (0.91 vs 0.81 bp); wins across more scripts (relative breadth 0.741 vs 0.352); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, SJS shot control · normal event (5-7) · decided (2+) 0.09.
- thesis SJS:SUPPRESSED (p 0.4022): highest fidelity KXNHLTOTAL-26OCT19SJTOR-7|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no (same contract)
- KXNHLTOTAL-26OCT19SJTOR-7|no: FUNDED_RESEARCH; family MIXED; loses 17% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2767, phi -0.644)

portfolios: A EV +1.79 (adj +0.43) on $20.00, P(profit) 0.5202, adj growth 2.1 bp · B EV +0.44 (adj +0.10) on $4.88, P(profit) 0.5202, adj growth 0.9 bp · C EV +0.44 (adj +0.10) on $4.88, P(profit) 0.5202, adj growth 0.9 bp · R EV +0.18 (adj +0.04) on $2.00, P(profit) 0.5202, adj growth 1.4 bp

## PIT @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.63 | 0.37 | 0.00 | 6.05 | 27.2/27.0 | 24.0/23.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.62 | 0.38 | 0.00 | 9.45 | 28.9/28.5 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.47 | 6.03 | 27.4/27.3 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.085 | 0.68 | 0.32 | 0.00 | 6.0 | 32.2/21.3 | 18.7/27.6 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.54 | 0.46 | 0.47 | 5.96 | 32.2/21.7 | 18.3/28.8 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.70 | 0.30 | 0.00 | 9.38 | 34.0/23.2 | 18.6/26.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
