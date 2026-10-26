# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T13:22:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 90.00 | +10.30 | +2.49 | +10.29 | 0.650 | -23.79 | -40.92 | 20.90 |
| B thesis-diversified (joint) ← optimiser card | 66.74 | +9.11 | +2.93 | +15.15 | 0.603 | -15.72 | -35.87 | 25.65 |
| C best expression per thesis | 56.41 | +7.04 | +1.87 | +20.18 | 0.519 | -26.37 | -30.84 | 16.54 |
| R FUNDED research stakes | 13.00 | +1.33 | +0.59 | +2.15 | 0.580 | -7.16 | -7.16 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  412 bet sides mapped, 2 +EV candidates, 2 on card


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
| Mats Zuccarello: 1+ assists NO | 65 | 0.803 | 0.690 | +0.137 | +0.025 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 67 | 0.717 | 0.703 | +0.032 | +0.018 | $14.39 | FUNDED_RESEARCH | $4 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (5.94 vs 0.56 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: LAK offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT26LANYR-NYRSDURZI5-1|no; why: higher confidence-adjusted growth (3.15 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.040/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4602): highest fidelity KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.383): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3162, phi -0.197)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3935, phi -0.208)

portfolios: A EV +5.04 (adj +1.25) on $40.00, P(profit) 0.5751, adj growth 10.9 bp · B EV +4.78 (adj +1.11) on $34.39, P(profit) 0.5751, adj growth 9.9 bp · C EV +4.78 (adj +1.11) on $34.39, P(profit) 0.5751, adj growth 9.9 bp · R EV +0.19 (adj +0.10) on $4.00, P(profit) 0.7174, adj growth 3.5 bp

## TOR @ CGY  ·  10000 joint draws  ·  442 bet sides mapped, 11 +EV candidates, 4 on card


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
| Jonathan Castagna: 1+ goals YES | 11 | 0.156 | 0.137 | +0.039 | +0.020 | $4.64 | FUNDED_RESEARCH | $2 | CGY:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 12 | 0.162 | 0.142 | +0.034 | +0.015 | $4.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Toronto wins by over 2.5 goals NO | 75 | 0.816 | 0.781 | +0.053 | +0.018 | $17.53 | FUNDED_RESEARCH | $5 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto over 4.5 goals scored NO | 71 | 0.771 | 0.735 | +0.046 | +0.011 | $5.72 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (8.45 vs 3.72 bp); despite a smaller raw edge (+0.039 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no: MOSTLY_INDEPENDENT (phi 0.01); failure: CGY offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26TORCGY-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (4.41 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no: INTENTIONAL_DIVERSIFIER (phi -0.179); failure: TOR offense suppressed (<= 2 goals)
- **Toronto wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR2|no; why: higher confidence-adjusted growth (3.72 vs 3.50 bp); despite a smaller raw edge (+0.053 vs +0.059/contract); relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no: REINFORCING (phi 0.525); failure: TOR wins by 2+
- **Toronto over 4.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no selected over broad KXNHLTOTAL-26OCT26TORCGY-4|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.60 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.179); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: REINFORCING (phi 0.525); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CGY:OFFENSE_4PLUS (p 0.4028): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4983): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.385, phi -0.189)
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3803, phi -0.193)
- KXNHLSPREAD-26OCT26TORCGY-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2848, phi -0.752)
- KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no: FUNDED_RESEARCH; family MIXED; loses 5% of the draws where the thesis happens; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4023, phi -0.665)
- override: Broad expression KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5|no selected over broad KXNHLTOTAL-26OCT26TORCGY-4|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.60 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.26 (adj +1.24) on $50.00, P(profit) 0.6297, adj growth 10.0 bp · B EV +4.34 (adj +1.82) on $32.35, P(profit) 0.2922, adj growth 15.8 bp · C EV +2.27 (adj +0.76) on $22.02, P(profit) 0.8303, adj growth 6.7 bp · R EV +1.15 (adj +0.49) on $9.00, P(profit) 0.7505, adj growth 15.4 bp

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
