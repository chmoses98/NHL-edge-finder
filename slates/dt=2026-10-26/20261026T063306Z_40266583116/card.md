# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T06:33:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +4.56 | +1.31 | +28.84 | 0.571 | -50.00 | -50.00 | 8.57 |
| B thesis-diversified (joint) ← optimiser card | 22.67 | +2.10 | +0.70 | +3.54 | 0.822 | -22.67 | -22.67 | 6.16 |
| C best expression per thesis | 20.00 | +1.53 | +0.53 | +6.21 | 0.822 | -20.00 | -20.00 | 4.78 |
| R FUNDED research stakes | 7.00 | +0.80 | +0.26 | -0.45 | 0.370 | -7.00 | -7.00 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_LAK_win | p_overtime | goals | shots NYR/LAK | NYR/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.60 | 0.40 | 0.00 | 5.97 | 27.1/27.4 | 24.1/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.45 | 5.87 | 27.1/27.5 | 24.3/23.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.082 | 0.53 | 0.47 | 0.00 | 5.95 | 21.6/32.7 | 29.1/18.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.47 | 5.77 | 21.6/32.8 | 29.5/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.60 | 0.40 | 0.00 | 9.19 | 28.6/28.9 | 23.4/21.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 3.45 | 25.7/26.0 | 24.4/23.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_TOR_win | p_overtime | goals | shots CGY/TOR | CGY/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.02 | 30.1/29.8 | 26.2/26.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.45 | 5.93 | 29.9/29.6 | 26.2/26.4 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.095 | 0.52 | 0.48 | 0.00 | 6.01 | 35.7/24.1 | 20.8/31.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.50 | 0.50 | 0.00 | 9.29 | 31.7/31.1 | 24.7/25.2 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.54 | 0.46 | 0.48 | 5.92 | 35.9/24.0 | 20.7/32.5 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.064 | 0.57 | 0.43 | 0.00 | 9.25 | 37.3/25.4 | 20.2/30.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 75 | 0.822 | 0.783 | +0.059 | +0.020 | $20.00 | FUNDED_RESEARCH | $5 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto over 2.5 goals scored NO | 30 | 0.370 | 0.330 | +0.055 | +0.015 | $1.28 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Toronto over 1.5 goals scored NO | 13 | 0.172 | 0.148 | +0.034 | +0.011 | $1.39 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR2|no; why: higher confidence-adjusted growth (4.96 vs 2.65 bp); despite a smaller raw edge (+0.059 vs +0.059/contract); relationships: KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3|no: DUPLICATIVE (phi 0.357); KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2|no: REINFORCING (phi 0.212); failure: TOR wins by 2+
- **Toronto over 2.5 goals scored NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT26TORCGY-TOR3|no has the higher standalone adjusted growth (4.96 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.357); they share one thesis budget; relationships: KXNHLSPREAD-26OCT26TORCGY-TOR3|no: DUPLICATIVE (phi 0.357); KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2|no: DUPLICATIVE (phi 0.594); failure: TOR offense succeeds (4+ goals)
- **Toronto over 1.5 goals scored NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT26TORCGY-TOR3|no has the higher standalone adjusted growth (4.96 vs 2.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.212); they share one thesis budget; relationships: KXNHLSPREAD-26OCT26TORCGY-TOR3|no: REINFORCING (phi 0.212); KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3|no: DUPLICATIVE (phi 0.594); failure: TOR wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CGY shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.4954): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR3|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3791): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR3|no (same contract)
- KXNHLSPREAD-26OCT26TORCGY-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2847, phi -0.739)
- KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3|no: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.406, phi -0.633)
- KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2|no: FUNDED_RESEARCH; family MIXED; loses 55% of the draws where the thesis happens; opposing: failure thesis TOR:WINS (p 0.5046, phi -0.429)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2|no kept
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3|no kept

portfolios: A EV +4.56 (adj +1.31) on $50.00, P(profit) 0.5707, adj growth 8.6 bp · B EV +2.10 (adj +0.70) on $22.67, P(profit) 0.8216, adj growth 6.2 bp · C EV +1.53 (adj +0.53) on $20.00, P(profit) 0.8216, adj growth 4.8 bp · R EV +0.80 (adj +0.26) on $7.00, P(profit) 0.3699, adj growth 8.1 bp

## DET @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.71 | 0.29 | 0.00 | 6.06 | 27.6/27.5 | 24.8/23.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.72 | 0.28 | 0.00 | 9.36 | 29.6/29.6 | 24.6/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.56 | 0.44 | 0.47 | 5.99 | 27.8/27.9 | 24.6/24.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.082 | 0.76 | 0.24 | 0.00 | 6.08 | 32.5/21.9 | 19.7/27.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.065 | 0.79 | 0.21 | 0.00 | 9.44 | 35.0/23.4 | 19.5/26.2 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.060 | 0.66 | 0.34 | 0.00 | 6.01 | 22.8/33.1 | 30.0/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
