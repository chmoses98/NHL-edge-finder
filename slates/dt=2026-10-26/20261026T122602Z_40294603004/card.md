# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T12:26:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 89.58 | +11.70 | +3.58 | -2.86 | 0.478 | -33.34 | -59.55 | 25.59 |
| B thesis-diversified (joint) ← optimiser card | 56.31 | +7.15 | +1.99 | +12.44 | 0.659 | -26.28 | -29.56 | 17.77 |
| C best expression per thesis | 56.41 | +7.04 | +1.96 | +20.18 | 0.519 | -26.38 | -30.85 | 17.52 |
| R FUNDED research stakes | 11.00 | +1.01 | +0.37 | +3.13 | 0.628 | -5.16 | -5.76 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  406 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_LAK_win | p_overtime | goals | shots NYR/LAK | NYR/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.53 | 0.47 | 0.48 | 5.91 | 27.1/27.5 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 5.96 | 27.1/27.4 | 24.3/23.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.089 | 0.52 | 0.48 | 0.00 | 6.03 | 21.7/32.4 | 28.7/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.12 | 28.5/28.8 | 23.3/22.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.47 | 5.81 | 22.0/33.0 | 29.9/18.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.58 | 0.42 | 0.00 | 3.52 | 26.2/26.1 | 24.5/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 65 | 0.803 | 0.694 | +0.137 | +0.028 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 67 | 0.717 | 0.703 | +0.032 | +0.018 | $14.39 | FUNDED_RESEARCH | $4 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (7.62 vs 0.56 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: LAK offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT26LANYR-NYRSDURZI5-1|no; why: higher confidence-adjusted growth (3.15 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.040/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4602): highest fidelity KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.383): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.8 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3162, phi -0.197)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3935, phi -0.208)

portfolios: A EV +5.04 (adj +1.35) on $40.00, P(profit) 0.5751, adj growth 11.9 bp · B EV +4.78 (adj +1.20) on $34.39, P(profit) 0.5751, adj growth 10.9 bp · C EV +4.78 (adj +1.20) on $34.39, P(profit) 0.5751, adj growth 10.9 bp · R EV +0.19 (adj +0.10) on $4.00, P(profit) 0.7174, adj growth 3.5 bp

## TOR @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_TOR_win | p_overtime | goals | shots CGY/TOR | CGY/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.02 | 30.2/29.7 | 26.0/26.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.97 | 30.1/29.7 | 26.4/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.49 | 0.51 | 0.00 | 9.34 | 31.5/31.3 | 24.9/25.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.094 | 0.56 | 0.44 | 0.00 | 6.03 | 35.6/23.8 | 20.6/31.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.54 | 0.46 | 0.48 | 5.97 | 35.9/24.3 | 21.1/32.4 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.064 | 0.53 | 0.47 | 0.00 | 9.31 | 37.6/25.4 | 19.9/30.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Toronto wins by over 2.5 goals NO | 75 | 0.816 | 0.781 | +0.053 | +0.018 | $13.53 | FUNDED_RESEARCH | $4 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 3.5 goals scored NO | 9 | 0.130 | 0.108 | +0.035 | +0.012 | $2.47 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | DIRECT (0.60) | EVIDENCE_MIXED | D |
| Toronto wins by over 1.5 goals NO | 64 | 0.715 | 0.675 | +0.059 | +0.019 | $5.92 | FUNDED_RESEARCH | $2 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR2|no; why: higher confidence-adjusted growth (3.72 vs 3.50 bp); despite a smaller raw edge (+0.053 vs +0.059/contract); relationships: KXNHLTOTAL-26OCT26TORCGY-4|no: INTENTIONAL_DIVERSIFIER (phi 0.076); KXNHLSPREAD-26OCT26TORCGY-TOR2|no: DUPLICATIVE (phi 0.752); failure: TOR wins by 2+
- **Full Game: Over 3.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no; why: higher confidence-adjusted growth (3.57 vs 0.77 bp); despite a smaller raw edge (+0.035 vs +0.046/contract); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLSPREAD-26OCT26TORCGY-TOR3|no: INTENTIONAL_DIVERSIFIER (phi 0.076); KXNHLSPREAD-26OCT26TORCGY-TOR2|no: INTENTIONAL_DIVERSIFIER (phi 0.092); failure: CGY offense succeeds (4+ goals)
- **Toronto wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT26TORCGY-TOR3|no has the higher standalone adjusted growth (3.72 vs 3.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.752); they share one thesis budget; relationships: KXNHLSPREAD-26OCT26TORCGY-TOR3|no: DUPLICATIVE (phi 0.752); KXNHLTOTAL-26OCT26TORCGY-4|no: INTENTIONAL_DIVERSIFIER (phi 0.092); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CGY:WINS (p 0.4983): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2168): highest fidelity KXNHLTOTAL-26OCT26TORCGY-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT26TORCGY-4|no (same contract)
- KXNHLSPREAD-26OCT26TORCGY-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2848, phi -0.752)
- KXNHLTOTAL-26OCT26TORCGY-4|no: FUNDED_RESEARCH; family MIXED; loses 40% of the draws where the thesis happens; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.4028, phi -0.318)
- KXNHLSPREAD-26OCT26TORCGY-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2848, phi -1.0)

portfolios: A EV +6.66 (adj +2.23) on $49.58, P(profit) 0.7384, adj growth 13.7 bp · B EV +2.37 (adj +0.79) on $21.92, P(profit) 0.7384, adj growth 6.9 bp · C EV +2.27 (adj +0.76) on $22.02, P(profit) 0.8303, adj growth 6.7 bp · R EV +0.82 (adj +0.27) on $7.00, P(profit) 0.7384, adj growth 9.0 bp

## DET @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.72 | 0.28 | 0.00 | 6.05 | 27.9/27.7 | 25.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.72 | 0.28 | 0.00 | 9.39 | 29.4/29.4 | 24.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.56 | 0.44 | 0.46 | 6.04 | 27.8/27.9 | 24.6/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.087 | 0.75 | 0.25 | 0.00 | 6.03 | 32.9/22.1 | 19.8/27.8 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.78 | 0.22 | 0.00 | 9.43 | 34.4/23.6 | 19.3/25.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.60 | 0.40 | 0.47 | 5.96 | 32.8/22.2 | 19.1/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
