# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T00:56:18Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +9.12 | +2.49 | +8.77 | 0.602 | -30.95 | -30.95 | 20.01 |
| B thesis-diversified (joint) ← optimiser card | 29.91 | +5.40 | +2.16 | +0.29 | 0.665 | -29.91 | -29.91 | 18.81 |
| C best expression per thesis | 18.29 | +4.04 | +1.45 | +7.18 | 0.641 | -18.29 | -18.29 | 12.65 |
| R FUNDED research stakes | 2.00 | +0.19 | +0.11 | -2.00 | 0.300 | -2.00 | -2.00 | 0.00 |

## DET @ EDM  ·  10000 joint draws  ·  512 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_DET_win | p_overtime | goals | shots EDM/DET | EDM/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.136 | 0.71 | 0.29 | 0.00 | 6.05 | 27.9/27.8 | 25.3/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.69 | 0.31 | 0.00 | 9.46 | 29.3/29.4 | 24.3/21.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.47 | 5.98 | 28.0/27.8 | 24.3/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.76 | 0.24 | 0.00 | 6.03 | 32.7/22.0 | 19.6/27.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.065 | 0.78 | 0.22 | 0.00 | 9.39 | 34.7/23.3 | 19.3/26.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.60 | 0.40 | 0.46 | 5.97 | 33.2/22.3 | 19.2/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ assists YES | 30 | 0.391 | 0.343 | +0.076 | +0.028 | $10.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 30 | 0.376 | 0.336 | +0.061 | +0.021 | $9.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.64) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.300 | 0.288 | +0.026 | +0.015 | $6.69 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 16 | 0.190 | 0.181 | +0.020 | +0.012 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (8.02 vs 2.64 bp); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (4.37 vs 1.83 bp); despite a smaller raw edge (+0.061 vs +0.090/contract); relationships: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.19); KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (8.02 vs 2.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.19); KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (8.02 vs 2.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5294): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2642): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.232)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 36% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.323)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.217)
- KXNHLGOAL-26OCT26DETEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.17)

portfolios: A EV +9.12 (adj +2.49) on $50.00, P(profit) 0.6022, adj growth 20.0 bp · B EV +5.40 (adj +2.16) on $29.91, P(profit) 0.665, adj growth 18.8 bp · C EV +4.04 (adj +1.45) on $18.29, P(profit) 0.6411, adj growth 12.7 bp · R EV +0.19 (adj +0.11) on $2.00, P(profit) 0.2997, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
