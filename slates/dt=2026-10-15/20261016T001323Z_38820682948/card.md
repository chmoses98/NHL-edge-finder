# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T00:13:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +20.93 | +4.02 | +20.73 | 0.742 | -27.78 | -45.27 | 33.32 |
| B thesis-diversified (joint) ← optimiser card | 67.94 | +14.52 | +6.93 | +8.24 | 0.578 | -34.79 | -45.42 | 60.32 |
| C best expression per thesis | 53.40 | +12.96 | +3.68 | +14.04 | 0.704 | -24.63 | -27.60 | 32.19 |
| R FUNDED research stakes | 6.00 | +0.36 | +0.21 | -0.25 | 0.345 | -6.00 | -6.00 | 0.00 |

## UTA @ EDM  ·  10000 joint draws  ·  472 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.01 | 27.6/27.5 | 24.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 9.48 | 29.4/29.4 | 24.0/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 6.03 | 28.0/27.8 | 24.5/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.07 | 32.5/22.0 | 19.3/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 9.5 | 34.3/23.3 | 18.6/26.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.55 | 0.45 | 0.47 | 5.97 | 32.8/22.2 | 19.1/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mattias Ekholm: 1+ goals YES | 8 | 0.127 | 0.113 | +0.042 | +0.028 | $7.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 16 | 0.216 | 0.200 | +0.047 | +0.030 | $8.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.440 | 0.359 | +0.105 | +0.024 | $10.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ goals YES | 43 | 0.470 | 0.458 | +0.023 | +0.011 | $4.75 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | DIRECT (0.61) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes; why: higher confidence-adjusted growth (21.01 vs 13.85 bp); despite a smaller raw edge (+0.042 vs +0.047/contract); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.121); KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (13.85 vs 5.64 bp); despite a smaller raw edge (+0.047 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.073); KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (5.39 vs 2.79 bp); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.121); KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.073); KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.61 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.499): highest fidelity KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes — Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.61 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis EDM:WINS (p 0.5762): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4009): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.135)
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.201)
- KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.499, phi -0.326)
- KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 38% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.3)
- override: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMCMCDAVID97-1|yes selected over player prop KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.61 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +13.71 (adj +2.45) on $50.00, P(profit) 0.783, adj growth 20.0 bp · B EV +9.50 (adj +4.72) on $31.32, P(profit) 0.6461, adj growth 40.6 bp · C EV +11.46 (adj +3.51) on $48.03, P(profit) 0.7104, adj growth 30.7 bp · R EV +0.10 (adj +0.05) on $2.00, P(profit) 0.4705, adj growth 1.5 bp

## CGY @ VGK  ·  10000 joint draws  ·  472 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.73 | 0.27 | 0.00 | 6.03 | 28.5/28.0 | 25.5/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.115 | 0.81 | 0.19 | 0.00 | 6.0 | 33.8/22.0 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.46 | 5.89 | 28.4/27.8 | 24.4/24.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.60 | 0.40 | 0.44 | 5.88 | 33.8/22.4 | 19.4/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 9.23 | 29.9/29.3 | 24.3/22.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.080 | 0.80 | 0.20 | 0.00 | 9.2 | 35.6/23.2 | 19.4/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.740 | 0.724 | +0.045 | +0.029 | $15.00 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.085 | 0.079 | +0.021 | +0.015 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 65 | 0.777 | 0.691 | +0.111 | +0.025 | $15.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Aydar Suniev: 1+ goals YES | 16 | 0.190 | 0.180 | +0.021 | +0.011 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (8.45 vs 1.48 bp); despite a smaller raw edge (+0.045 vs +0.117/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15CGYVGK-VGKBMCNABB3-1|yes; why: higher confidence-adjusted growth (7.81 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.056/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (6.24 vs 1.48 bp); despite a smaller raw edge (+0.111 vs +0.117/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VGK offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15CGYVGK-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (1.76 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:SUPPRESSED (p 0.2881): highest fidelity KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.5061): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:OFFENSE_4PLUS (p 0.2554): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.21)
- KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.107)
- KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.212)
- KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5331, phi -0.219)

portfolios: A EV +7.22 (adj +1.57) on $50.00, P(profit) 0.6503, adj growth 13.3 bp · B EV +5.02 (adj +2.21) on $36.62, P(profit) 0.6799, adj growth 19.7 bp · C EV +1.50 (adj +0.17) on $5.37, P(profit) 0.5336, adj growth 1.4 bp · R EV +0.26 (adj +0.16) on $4.00, P(profit) 0.74, adj growth 6.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
