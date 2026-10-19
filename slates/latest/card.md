# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T22:03:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.77 | +8.46 | +29.22 | 0.720 | -33.65 | -50.38 | 71.69 |
| B thesis-diversified (joint) ← optimiser card | 142.90 | +26.09 | +15.14 | +17.27 | 0.614 | -48.29 | -60.40 | 130.09 |
| C best expression per thesis | 112.91 | +23.34 | +10.83 | +13.70 | 0.603 | -37.37 | -49.24 | 93.80 |
| R FUNDED research stakes | 20.00 | +2.24 | +0.94 | +3.19 | 0.576 | -7.01 | -10.52 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  476 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.58 | 0.42 | 0.00 | 6.05 | 26.7/27.3 | 24.0/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.105 | 0.52 | 0.48 | 0.00 | 6.02 | 21.3/32.3 | 28.7/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.45 | 6.05 | 26.8/27.5 | 24.1/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.60 | 0.40 | 0.00 | 9.43 | 28.3/28.8 | 23.2/21.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.49 | 0.51 | 0.47 | 5.94 | 21.3/32.6 | 29.2/18.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.081 | 0.49 | 0.51 | 0.00 | 9.31 | 22.9/34.6 | 28.0/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.216 | 0.196 | +0.068 | +0.047 | $10.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| A.J. Greer: 2+ goals YES | 1 | 0.029 | 0.024 | +0.018 | +0.013 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 8 | 0.117 | 0.104 | +0.032 | +0.019 | $4.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Dylan Garand: 25+ saves YES | 45 | 0.536 | 0.490 | +0.068 | +0.023 | $12.57 | FUNDED_RESEARCH | $4 | NYR:NET_HIGH_VOLUME | DIRECT (0.94) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (37.60 vs 6.92 bp); despite a smaller raw edge (+0.068 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: DUPLICATIVE (phi 0.329); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (37.60 vs 32.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.329); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: DUPLICATIVE (phi 0.329); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (37.60 vs 10.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: ANA offense suppressed (<= 2 goals)
- **Dylan Garand: 25+ saves YES** — thesis: NYR net faces heavy volume (33+ shots; ANA pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: NYR net faces light volume (<= 25 shots; ANA suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3856): highest fidelity KXNHLAST-26OCT19ANANYR-ANABSENNECKE45-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:NET_HIGH_VOLUME (p 0.2588): highest fidelity KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.446): highest fidelity KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.219)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.129)
- KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.162)
- KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: FUNDED_RESEARCH; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:NET_LOW_VOLUME (p 0.3094, phi -0.701)

portfolios: A EV +11.31 (adj +4.73) on $37.50, P(profit) 0.4847, adj growth 40.4 bp · B EV +11.34 (adj +7.21) on $29.39, P(profit) 0.3077, adj growth 60.2 bp · C EV +8.38 (adj +4.74) on $27.13, P(profit) 0.3654, adj growth 40.6 bp · R EV +0.59 (adj +0.20) on $4.00, P(profit) 0.5357, adj growth 6.4 bp

## COL @ PHI  ·  10000 joint draws  ·  440 bet sides mapped, 40 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.324 / away 0.676

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.137 | 0.38 | 0.62 | 0.00 | 5.93 | 21.2/33.4 | 29.3/18.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.45 | 0.55 | 0.46 | 5.87 | 21.4/33.8 | 30.4/18.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.44 | 0.56 | 0.00 | 5.99 | 27.0/27.7 | 23.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.50 | 0.50 | 0.48 | 5.89 | 26.9/27.7 | 24.4/23.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.079 | 0.34 | 0.66 | 0.00 | 9.16 | 22.8/35.6 | 28.0/18.1 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.077 | 0.41 | 0.59 | 0.00 | 3.46 | 20.1/32.2 | 30.0/18.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 2+ goals NO | 87 | 0.919 | 0.905 | +0.041 | +0.027 | $17.13 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.623 | 0.603 | +0.055 | +0.036 | $12.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.796 | 0.711 | +0.110 | +0.025 | $17.30 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 2+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes; why: higher confidence-adjusted growth (15.64 vs 13.51 bp); despite a smaller raw edge (+0.041 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.562); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.382); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.183); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (15.64 vs 11.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.382); they share one thesis budget; relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.382); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.19); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (42.22 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: REINFORCING (phi 0.183); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.19); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4691): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3134): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2308): highest fidelity KXNHLSPREAD-26OCT19COLPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes (same contract)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.259)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.293)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.1 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3232, phi -0.733)

portfolios: A EV +11.10 (adj +1.18) on $37.50, P(profit) 0.7611, adj growth 9.1 bp · B EV +4.84 (adj +1.99) on $47.30, P(profit) 0.5327, adj growth 18.0 bp · C EV +7.58 (adj +2.63) on $24.67, P(profit) 0.2431, adj growth 23.0 bp · R EV +1.04 (adj +0.34) on $10.00, P(profit) 0.7514, adj growth 12.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  464 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.550 / away 0.450

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.06 | 27.8/28.2 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.48 | 5.96 | 28.3/28.4 | 25.1/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.55 | 0.45 | 0.00 | 9.33 | 29.7/29.8 | 23.9/23.3 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.090 | 0.47 | 0.53 | 0.00 | 5.97 | 22.5/33.5 | 29.7/19.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.47 | 0.53 | 0.45 | 5.91 | 22.5/33.8 | 30.4/19.3 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.061 | 0.45 | 0.55 | 0.00 | 9.19 | 24.1/35.6 | 28.7/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ assists NO | 70 | 0.784 | 0.739 | +0.069 | +0.025 | $12.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 78 | 0.818 | 0.807 | +0.026 | +0.015 | $10.40 | FUNDED_RESEARCH | $3 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.233 | 0.223 | +0.022 | +0.012 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.781 | 0.746 | +0.047 | +0.011 | $6.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (6.59 vs 1.47 bp); relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: second expression of the same thesis: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (6.59 vs 2.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.029); they share one thesis budget; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (1.95 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: second expression of the same thesis: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (6.59 vs 1.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3893): highest fidelity KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3899): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.201)
- KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.192)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3893, phi -0.231)
- KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.209)

portfolios: A EV +2.56 (adj +1.00) on $37.50, P(profit) 0.5963, adj growth 9.1 bp · B EV +2.40 (adj +0.96) on $33.75, P(profit) 0.6025, adj growth 8.9 bp · C EV +2.32 (adj +0.91) on $23.73, P(profit) 0.7838, adj growth 8.1 bp · R EV +0.10 (adj +0.06) on $3.00, P(profit) 0.8176, adj growth 2.1 bp

## PIT @ UTA  ·  10000 joint draws  ·  494 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.623 / away 0.378

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.05 | 27.2/27.1 | 24.0/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.61 | 0.39 | 0.00 | 9.41 | 28.9/28.6 | 23.1/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.53 | 0.47 | 0.47 | 6.03 | 27.5/27.3 | 24.0/24.0 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.086 | 0.67 | 0.33 | 0.00 | 6.04 | 31.6/21.2 | 18.6/27.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.70 | 0.30 | 0.00 | 9.36 | 34.2/23.2 | 18.7/26.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.56 | 0.44 | 0.44 | 5.98 | 31.9/21.6 | 18.4/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack McBain: 1+ goals YES | 12 | 0.169 | 0.156 | +0.042 | +0.028 | $7.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.156 | 0.143 | +0.039 | +0.026 | $6.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 28 | 0.345 | 0.327 | +0.051 | +0.033 | $11.04 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.320 | 0.306 | +0.036 | +0.022 | $7.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1|yes; why: higher confidence-adjusted growth (15.29 vs 1.51 bp); despite a smaller raw edge (+0.042 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes; why: higher confidence-adjusted growth (14.44 vs 11.50 bp); despite a smaller raw edge (+0.039 vs +0.051/contract); relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: PIT offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.44 vs 11.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.44 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3756): highest fidelity KXNHLAST-26OCT19PITUTA-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.2965): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTACKELLER9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:NET_LOW_VOLUME (p 0.3663): highest fidelity KXNHLSAVE-26OCT19PITUTA-PITASILOVS37-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT19PITUTA-PITASILOVS37-26|no (same contract)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.2965, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.209)
- KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.277)
- KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.272)

portfolios: A EV +5.80 (adj +1.55) on $37.50, P(profit) 0.5868, adj growth 13.1 bp · B EV +7.51 (adj +4.98) on $32.46, P(profit) 0.54, adj growth 43.0 bp · C EV +5.06 (adj +2.55) on $37.38, P(profit) 0.5787, adj growth 22.1 bp · R EV +0.52 (adj +0.34) on $3.00, P(profit) 0.3447, adj growth 11.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
