# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T00:05:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +15.64 | +3.82 | +21.58 | 0.726 | -35.54 | -40.56 | 32.09 |
| B thesis-diversified (joint) ← optimiser card | 77.83 | +13.28 | +5.28 | +8.15 | 0.619 | -32.30 | -40.93 | 46.07 |
| C best expression per thesis | 72.38 | +11.97 | +4.50 | +3.33 | 0.735 | -29.72 | -40.95 | 39.39 |
| R FUNDED research stakes | 5.00 | +0.31 | +0.18 | -0.62 | 0.300 | -5.00 | -5.00 | 0.00 |

## TOR @ CGY  ·  10000 joint draws  ·  502 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.446 / away 0.554

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_TOR_win | p_overtime | goals | shots CGY/TOR | CGY/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.49 | 0.51 | 0.00 | 6.01 | 30.0/29.7 | 26.2/26.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.46 | 5.9 | 30.1/29.9 | 26.5/26.8 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 5.98 | 35.6/23.7 | 20.5/31.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.52 | 0.48 | 0.00 | 9.31 | 31.7/31.4 | 25.3/25.5 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.54 | 0.46 | 0.47 | 5.91 | 35.9/23.9 | 20.6/32.4 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.066 | 0.50 | 0.50 | 0.00 | 9.31 | 37.6/25.7 | 19.7/30.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jonathan Castagna: 1+ goals YES | 12 | 0.166 | 0.152 | +0.039 | +0.025 | $6.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 12 | 0.160 | 0.145 | +0.032 | +0.018 | $4.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ assists NO | 54 | 0.627 | 0.581 | +0.070 | +0.024 | $12.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Kirill Marchenko: 1+ goals NO | 67 | 0.712 | 0.701 | +0.027 | +0.015 | $9.67 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT26TORCGY-CGYYSHARANGOVICH17-1|yes; why: higher confidence-adjusted growth (11.97 vs 3.01 bp); relationships: KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CGY offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT26TORCGY-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (5.92 vs 0.20 bp); despite a smaller raw edge (+0.032 vs +0.077/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TOR offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no; why: KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no has the higher standalone adjusted growth (5.45 vs 5.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.057); relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.148); failure: TOR offense succeeds (4+ goals)
- **Kirill Marchenko: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no; why: Player prop expression KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no selected over player prop KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.148); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, CGY shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CGY:OFFENSE_4PLUS (p 0.4013): highest fidelity KXNHLSPREAD-26OCT26TORCGY-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.3987): highest fidelity KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3845): highest fidelity KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no — Player prop expression KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no selected over player prop KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT26TORCGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3761, phi -0.192)
- KXNHLGOAL-26OCT26TORCGY-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3845, phi -0.192)
- KXNHLAST-26OCT26TORCGY-TORAMATTHEWS34-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.263)
- KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3987, phi -0.238)
- override: Player prop expression KXNHLGOAL-26OCT26TORCGY-TORKMARCHENKO86-1|no selected over player prop KXNHLAST-26OCT26TORCGY-TORGMCKENNA92-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.85 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.92 (adj +1.58) on $50.00, P(profit) 0.5781, adj growth 12.8 bp · B EV +5.18 (adj +2.67) on $33.71, P(profit) 0.6362, adj growth 23.2 bp · C EV +5.80 (adj +2.73) on $41.98, P(profit) 0.7437, adj growth 23.7 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.7123, adj growth 2.3 bp

## DET @ EDM  ·  10000 joint draws  ·  512 bet sides mapped, 10 +EV candidates, 4 on card

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
| Vasily Podkolzin: 1+ assists YES | 30 | 0.391 | 0.343 | +0.076 | +0.028 | $10.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 62 | 0.753 | 0.663 | +0.116 | +0.027 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 30 | 0.376 | 0.336 | +0.061 | +0.021 | $5.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.64) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.300 | 0.288 | +0.026 | +0.015 | $7.72 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (8.02 vs 2.64 bp); relationships: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (6.79 vs 4.37 bp); relationships: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.445); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.2); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (6.79 vs 4.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.445); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.445); KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (8.02 vs 2.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.2); KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.19); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5294): highest fidelity KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2642): highest fidelity KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no (same contract)
- KXNHLAST-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.232)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.335)
- KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 36% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5294, phi -0.323)
- KXNHLGOAL-26OCT26DETEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2642, phi -0.217)

portfolios: A EV +9.72 (adj +2.24) on $50.00, P(profit) 0.6465, adj growth 19.3 bp · B EV +8.10 (adj +2.61) on $44.12, P(profit) 0.6487, adj growth 22.9 bp · C EV +6.17 (adj +1.77) on $30.40, P(profit) 0.8682, adj growth 15.7 bp · R EV +0.19 (adj +0.11) on $2.00, P(profit) 0.2997, adj growth 3.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
