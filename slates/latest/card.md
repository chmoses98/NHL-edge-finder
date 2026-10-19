# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T07:59:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +9.15 | +2.23 | +2.51 | 0.692 | -50.00 | -50.00 | 13.80 |
| B thesis-diversified (joint) ← optimiser card | 21.38 | +2.93 | +0.80 | +3.36 | 0.720 | -21.38 | -21.38 | 6.96 |
| C best expression per thesis | 17.83 | +2.54 | +0.78 | -1.94 | 0.377 | -17.83 | -17.83 | 6.86 |
| R FUNDED research stakes | 6.00 | +0.82 | +0.22 | +0.98 | 0.720 | -6.00 | -6.00 | 0.00 |

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

## COL @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


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
| Philadelphia wins by over 1.5 goals YES | 17 | 0.231 | 0.198 | +0.051 | +0.018 | $3.65 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 4.5 goals scored NO | 71 | 0.790 | 0.742 | +0.065 | +0.018 | $10.60 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 69 | 0.798 | 0.721 | +0.093 | +0.016 | $7.13 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no; why: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no has the higher standalone adjusted growth (5.96 vs 4.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.461); relationships: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.27); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.276); failure: COL wins (incl. OT/SO)
- **Colorado over 4.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no; why: KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no has the higher standalone adjusted growth (5.96 vs 3.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.402); relationships: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: REINFORCING (phi 0.27); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.536); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no; why: Broad expression KXNHLSPREAD-26OCT19COLPHI-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: REINFORCING (phi 0.276); KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: REINFORCING (phi 0.536); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.3909): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no — Broad expression KXNHLSPREAD-26OCT19COLPHI-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:WINS_BY_2PLUS (p 0.2312): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLSPREAD-26OCT19COLPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.5533, phi -0.61)
- KXNHLTEAMTOTAL-26OCT19COLPHI-COL5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.649)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.8 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3194, phi -0.735)
- override: Broad expression KXNHLSPREAD-26OCT19COLPHI-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL3|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.15 (adj +2.23) on $50.00, P(profit) 0.6921, adj growth 13.8 bp · B EV +2.93 (adj +0.80) on $21.38, P(profit) 0.7197, adj growth 7.0 bp · C EV +2.54 (adj +0.78) on $17.83, P(profit) 0.377, adj growth 6.9 bp · R EV +0.82 (adj +0.22) on $6.00, P(profit) 0.7197, adj growth 7.6 bp

## SJS @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.05 | 28.0/28.4 | 25.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.45 | 5.91 | 28.0/28.3 | 25.1/24.5 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.088 | 0.48 | 0.52 | 0.00 | 5.98 | 22.2/33.6 | 29.8/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.53 | 0.47 | 0.00 | 9.37 | 29.8/30.0 | 24.0/23.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.51 | 5.92 | 22.6/33.9 | 30.4/19.5 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.51 | 0.49 | 0.00 | 9.32 | 24.1/35.2 | 28.6/18.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, SJS shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
