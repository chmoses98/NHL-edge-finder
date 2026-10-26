# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-26T15:01:47Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.00 | +17.40 | +4.94 | +16.68 | 0.673 | -34.35 | -47.71 | 41.43 |
| B thesis-diversified (joint) ← optimiser card | 120.27 | +15.10 | +5.91 | +17.80 | 0.618 | -28.38 | -42.16 | 52.49 |
| C best expression per thesis | 87.35 | +10.61 | +3.34 | +9.75 | 0.705 | -23.18 | -37.08 | 29.93 |
| R FUNDED research stakes | 16.00 | +1.08 | +0.53 | +4.08 | 0.563 | -7.44 | -9.45 | 0.00 |

## LAK @ NYR  ·  10000 joint draws  ·  412 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_LAK_win | p_overtime | goals | shots NYR/LAK | NYR/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.60 | 0.40 | 0.00 | 5.99 | 27.0/27.3 | 24.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.45 | 5.88 | 27.0/27.3 | 24.1/23.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.082 | 0.55 | 0.45 | 0.00 | 5.92 | 21.8/32.3 | 28.9/18.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.49 | 0.51 | 0.46 | 5.85 | 21.8/32.6 | 29.3/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 9.24 | 28.3/28.8 | 23.3/21.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.55 | 0.45 | 0.00 | 3.51 | 26.2/26.2 | 24.4/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 64 | 0.804 | 0.694 | +0.148 | +0.038 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 67 | 0.720 | 0.706 | +0.034 | +0.021 | $16.41 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (14.05 vs 0.51 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: LAK offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26LANYR-NYRJMILLER8-1|no; why: higher confidence-adjusted growth (4.33 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.457): highest fidelity KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.3816): highest fidelity KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT26LANYR-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3188, phi -0.205)
- KXNHLGOAL-26OCT26LANYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3971, phi -0.205)

portfolios: A EV +5.50 (adj +1.76) on $40.00, P(profit) 0.582, adj growth 15.9 bp · B EV +5.32 (adj +1.65) on $36.41, P(profit) 0.582, adj growth 15.1 bp · C EV +5.32 (adj +1.65) on $36.41, P(profit) 0.582, adj growth 15.1 bp · R EV +0.25 (adj +0.15) on $5.00, P(profit) 0.7198, adj growth 5.2 bp

## TOR @ CGY  ·  10000 joint draws  ·  442 bet sides mapped, 16 +EV candidates, 4 on card


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
| Jonathan Castagna: 1+ goals YES | 11 | 0.156 | 0.140 | +0.039 | +0.023 | $5.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 79 | 0.845 | 0.827 | +0.043 | +0.026 | $19.88 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 12 | 0.162 | 0.149 | +0.034 | +0.021 | $6.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Toronto wins by over 2.5 goals NO | 75 | 0.816 | 0.781 | +0.053 | +0.018 | $18.81 | FUNDED_RESEARCH | $5 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR3|no; why: higher confidence-adjusted growth (10.66 vs 3.72 bp); despite a smaller raw edge (+0.039 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: MOSTLY_INDEPENDENT (phi 0.111); failure: CGY offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (9.22 vs 4.50 bp); despite a smaller raw edge (+0.043 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: MOSTLY_INDEPENDENT (phi 0.133); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26TORCGY-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (8.79 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT26TORCGY-TOR3|no: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: TOR offense suppressed (<= 2 goals)
- **Toronto wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT26TORCGY-TOR2|no; why: Broad expression KXNHLSPREAD-26OCT26TORCGY-TOR3|no selected over player prop KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis TOR:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no — Broad expression KXNHLSPREAD-26OCT26TORCGY-TOR3|no selected over player prop KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:OFFENSE_4PLUS (p 0.4028): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4983): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT26TORCGY-TOR2|no (same contract)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.385, phi -0.189)
- KXNHLGOAL-26OCT26TORCGY-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4023, phi -0.162)
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3803, phi -0.193)
- KXNHLSPREAD-26OCT26TORCGY-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2848, phi -0.752)
- override: Broad expression KXNHLSPREAD-26OCT26TORCGY-TOR3|no selected over player prop KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.51 (adj +1.34) on $50.00, P(profit) 0.6297, adj growth 11.0 bp · B EV +5.77 (adj +3.10) on $50.00, P(profit) 0.2793, adj growth 27.2 bp · C EV +3.25 (adj +1.06) on $28.69, P(profit) 0.5762, adj growth 9.3 bp · R EV +0.62 (adj +0.28) on $10.00, P(profit) 0.7082, adj growth 9.9 bp

## DET @ EDM  ·  10000 joint draws  ·  414 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.72 | 0.28 | 0.00 | 6.05 | 27.9/27.7 | 25.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.72 | 0.28 | 0.00 | 9.39 | 29.4/29.4 | 24.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.56 | 0.44 | 0.46 | 6.04 | 27.8/27.9 | 24.6/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.087 | 0.75 | 0.25 | 0.00 | 6.03 | 32.9/22.1 | 19.8/27.8 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.78 | 0.22 | 0.00 | 9.43 | 34.4/23.6 | 19.3/25.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.60 | 0.40 | 0.47 | 5.96 | 32.8/22.2 | 19.1/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Hallander: 1+ goals YES | 11 | 0.142 | 0.129 | +0.025 | +0.012 | $3.21 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 67 | 0.748 | 0.701 | +0.062 | +0.016 | $16.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 59 | 0.697 | 0.621 | +0.090 | +0.014 | $9.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.299 | 0.285 | +0.025 | +0.012 | $5.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (3.13 vs 1.59 bp); despite a smaller raw edge (+0.025 vs +0.025/contract); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT26DETEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (2.58 vs 1.79 bp); despite a smaller raw edge (+0.062 vs +0.090/contract); relationships: KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT26DETEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi 0.068); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.212); failure: EDM offense succeeds (4+ goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (2.58 vs 1.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.068); they share one thesis budget; relationships: KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.068); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (1.59 vs 0.70 bp); despite a smaller raw edge (+0.025 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLAST-26OCT26DETEDM-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2609): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5412): highest fidelity KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26OCT26DETEDM-EDMFHALLANDER11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.154)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.337)
- KXNHLAST-26OCT26DETEDM-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5412, phi -0.21)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2609, phi -0.225)

portfolios: A EV +6.39 (adj +1.84) on $50.00, P(profit) 0.7131, adj growth 14.5 bp · B EV +4.01 (adj +1.16) on $33.86, P(profit) 0.7062, adj growth 10.1 bp · C EV +2.04 (adj +0.63) on $22.25, P(profit) 0.7478, adj growth 5.5 bp · R EV +0.22 (adj +0.10) on $1.00, P(profit) 0.1421, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
