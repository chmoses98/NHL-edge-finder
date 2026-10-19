# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T17:01:47Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.03 | +30.95 | +10.73 | +24.92 | 0.644 | -46.17 | -68.43 | 86.29 |
| B thesis-diversified (joint) ← optimiser card | 122.54 | +19.03 | +10.65 | +9.48 | 0.572 | -41.64 | -54.86 | 92.04 |
| C best expression per thesis | 53.29 | +18.29 | +9.37 | -2.65 | 0.496 | -34.72 | -37.16 | 79.97 |
| R FUNDED research stakes | 20.00 | +3.40 | +1.96 | -1.19 | 0.343 | -8.48 | -8.48 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  418 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.567 / away 0.433

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.57 | 0.43 | 0.00 | 6.05 | 26.8/27.0 | 23.7/22.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.49 | 0.51 | 0.00 | 6.04 | 21.3/32.4 | 28.7/17.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.43 | 5.95 | 26.9/27.5 | 24.3/23.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.49 | 5.91 | 21.4/32.7 | 29.4/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.38 | 28.4/28.9 | 23.3/21.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.077 | 0.49 | 0.51 | 0.00 | 9.22 | 22.8/34.1 | 27.4/17.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.228 | 0.205 | +0.080 | +0.056 | $14.65 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.134 | 0.124 | +0.028 | +0.018 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 9 | 0.119 | 0.110 | +0.024 | +0.014 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 69 | 0.758 | 0.719 | +0.053 | +0.014 | $13.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes; why: higher confidence-adjusted growth (53.11 vs 1.83 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (53.11 vs 7.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (4.70 vs 0.82 bp); despite a smaller raw edge (+0.024 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: NYR offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19ANANYR-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (2.11 vs 0.55 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3536): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:NET_HIGH_VOLUME (p 0.2611): highest fidelity KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4002, phi -0.236)
- KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4002, phi -0.169)
- KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3536, phi -0.154)
- KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4336, phi -0.21)

portfolios: A EV +10.62 (adj +5.76) on $50.00, P(profit) 0.428, adj growth 49.2 bp · B EV +10.99 (adj +7.15) on $36.41, P(profit) 0.4138, adj growth 61.0 bp · C EV +9.82 (adj +6.11) on $35.56, P(profit) 0.2281, adj growth 52.0 bp · R EV +2.15 (adj +1.52) on $4.00, P(profit) 0.2281, adj growth 50.9 bp

## COL @ PHI  ·  10000 joint draws  ·  380 bet sides mapped, 31 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.140 | 0.38 | 0.62 | 0.00 | 5.97 | 21.2/33.5 | 29.2/18.4 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.47 | 0.53 | 0.47 | 5.91 | 21.5/33.4 | 30.1/18.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 5.98 | 26.9/27.7 | 24.0/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.48 | 0.52 | 0.50 | 5.88 | 27.0/27.9 | 24.5/23.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.079 | 0.35 | 0.65 | 0.00 | 9.09 | 22.5/35.5 | 27.8/17.9 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.072 | 0.39 | 0.61 | 0.00 | 3.42 | 20.0/32.0 | 29.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 2+ goals NO | 87 | 0.916 | 0.902 | +0.039 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.798 | 0.711 | +0.112 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ goals NO | 56 | 0.620 | 0.603 | +0.043 | +0.025 | $9.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 2+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI3|yes; why: higher confidence-adjusted growth (12.47 vs 12.41 bp); despite a smaller raw edge (+0.039 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.0 vs 0.471); relationships: KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.386); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (38.70 vs 6.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.139); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.191); failure: COL wins by 2+
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI3|yes; why: KXNHLSPREAD-26OCT19COLPHI-PHI3|yes has the higher standalone adjusted growth (12.41 vs 5.76 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.152); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.386); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.191); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3165): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT19COLPHI-PHINACCIARI52-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SCORES_FIRST (p 0.4723): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2348): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3886, phi -0.232)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.3 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3222, phi -0.73)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3886, phi -0.278)

portfolios: A EV +14.54 (adj +1.71) on $50.00, P(profit) 0.7549, adj growth 12.3 bp · B EV +4.83 (adj +1.71) on $49.07, P(profit) 0.7502, adj growth 15.4 bp · C EV +6.47 (adj +2.11) on $4.60, P(profit) 0.1873, adj growth 17.9 bp · R EV +1.04 (adj +0.33) on $10.00, P(profit) 0.7502, adj growth 12.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  436 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.550 / away 0.450

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.03 | 28.0/28.3 | 24.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.48 | 5.97 | 28.2/28.6 | 25.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.52 | 0.48 | 0.00 | 9.33 | 29.8/30.1 | 23.9/23.4 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.087 | 0.49 | 0.51 | 0.00 | 6.04 | 22.3/33.5 | 29.7/18.9 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.49 | 0.51 | 0.46 | 5.93 | 22.3/33.3 | 29.9/19.1 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 9.26 | 24.0/35.3 | 28.6/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ goals YES | 20 | 0.231 | 0.222 | +0.020 | +0.011 | $3.37 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (1.57 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3853): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3942, phi -0.217)

portfolios: A EV +0.60 (adj +0.33) on $6.34, P(profit) 0.2312, adj growth 2.5 bp · B EV +0.32 (adj +0.17) on $3.37, P(profit) 0.2312, adj growth 1.5 bp · C EV +0.32 (adj +0.17) on $3.37, P(profit) 0.2312, adj growth 1.5 bp · R EV +0.09 (adj +0.05) on $1.00, P(profit) 0.2312, adj growth 1.8 bp

## PIT @ UTA  ·  10000 joint draws  ·  474 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.06 | 27.5/27.3 | 24.2/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.114 | 0.62 | 0.38 | 0.00 | 9.48 | 28.8/28.6 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.47 | 6.0 | 27.3/27.2 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.70 | 0.30 | 0.00 | 6.01 | 32.1/21.3 | 18.7/27.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.58 | 0.42 | 0.43 | 5.96 | 32.2/21.8 | 18.6/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.67 | 0.33 | 0.00 | 9.42 | 33.9/23.1 | 18.3/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 20 | 0.246 | 0.231 | +0.035 | +0.020 | $6.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.151 | 0.142 | +0.023 | +0.014 | $3.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.164 | 0.152 | +0.026 | +0.014 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Mikhail Sergachev: 1+ goals NO | 85 | 0.879 | 0.870 | +0.021 | +0.011 | $20.00 | FUNDED_RESEARCH | $5 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1|yes; why: higher confidence-adjusted growth (5.02 vs 0.00 bp); despite a smaller raw edge (+0.035 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT19PITUTA-UTAMSERGACHEV98-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: UTA offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (3.98 vs 1.94 bp); despite a smaller raw edge (+0.023 vs +0.024/contract); relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-UTAMSERGACHEV98-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PIT offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (5.02 vs 3.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-UTAMSERGACHEV98-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense suppressed (<= 2 goals)
- **Mikhail Sergachev: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19PITUTA-UTACKELLER9-2|no; why: higher confidence-adjusted growth (2.08 vs 0.19 bp); despite a smaller raw edge (+0.021 vs +0.063/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.493): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3668): highest fidelity KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3006): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT19PITUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3006, phi -0.212)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4145, phi -0.196)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3006, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-UTAMSERGACHEV98-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.493, phi -0.137)

portfolios: A EV +5.18 (adj +2.93) on $33.69, P(profit) 0.4678, adj growth 22.2 bp · B EV +2.89 (adj +1.62) on $33.69, P(profit) 0.4221, adj growth 14.1 bp · C EV +1.68 (adj +0.98) on $9.76, P(profit) 0.3594, adj growth 8.5 bp · R EV +0.12 (adj +0.06) on $5.00, P(profit) 0.8795, adj growth 2.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
