# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T19:28:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.38 | +9.38 | +27.66 | 0.696 | -37.67 | -54.49 | 79.31 |
| B thesis-diversified (joint) ← optimiser card | 134.64 | +23.70 | +13.11 | +15.35 | 0.619 | -47.83 | -61.57 | 112.56 |
| C best expression per thesis | 110.54 | +21.33 | +10.10 | +12.97 | 0.600 | -37.42 | -49.44 | 87.76 |
| R FUNDED research stakes | 17.00 | +3.21 | +1.80 | -1.04 | 0.491 | -9.71 | -11.24 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  456 bet sides mapped, 6 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 14 | 0.216 | 0.196 | +0.068 | +0.047 | $10.39 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| A.J. Greer: 2+ goals YES | 1 | 0.029 | 0.024 | +0.018 | +0.013 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.330 | 0.293 | +0.057 | +0.019 | $6.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Taylor Raddysh: 1+ goals YES | 9 | 0.117 | 0.108 | +0.021 | +0.012 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (37.60 vs 2.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: DUPLICATIVE (phi 0.329); KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (37.60 vs 32.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.329); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: DUPLICATIVE (phi 0.329); KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: ANA offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (4.01 vs 0.18 bp); despite a smaller raw edge (+0.057 vs +0.081/contract); alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.035); failure: NYR offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes has the higher standalone adjusted growth (4.01 vs 3.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.035); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.035); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3856): highest fidelity KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.446): highest fidelity KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3431): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.219)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.129)
- KXNHLAST-26OCT19ANANYR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3431, phi -0.256)
- KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3431, phi -0.151)

portfolios: A EV +9.06 (adj +4.31) on $37.50, P(profit) 0.5595, adj growth 36.9 bp · B EV +9.64 (adj +6.32) on $21.27, P(profit) 0.5364, adj growth 52.6 bp · C EV +7.83 (adj +4.64) on $30.13, P(profit) 0.4092, adj growth 39.8 bp · R EV +1.37 (adj +0.96) on $3.00, P(profit) 0.216, adj growth 32.9 bp

## COL @ PHI  ·  10000 joint draws  ·  436 bet sides mapped, 31 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.323 / away 0.677

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
| Nathan MacKinnon: 2+ goals NO | 86 | 0.919 | 0.903 | +0.050 | +0.034 | $17.14 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.623 | 0.603 | +0.055 | +0.036 | $12.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.796 | 0.711 | +0.110 | +0.025 | $17.30 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 2+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes; why: higher confidence-adjusted growth (23.21 vs 13.51 bp); despite a smaller raw edge (+0.050 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.562); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: DUPLICATIVE (phi 0.382); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.183); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (23.21 vs 11.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.382); they share one thesis budget; relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: DUPLICATIVE (phi 0.382); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.19); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (42.22 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: REINFORCING (phi 0.183); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.19); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4691): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3134): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT19COLPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2308): highest fidelity KXNHLSPREAD-26OCT19COLPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes (same contract)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.259)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.293)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.1 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3232, phi -0.733)

portfolios: A EV +11.10 (adj +1.22) on $37.50, P(profit) 0.7611, adj growth 9.5 bp · B EV +5.03 (adj +2.13) on $47.30, P(profit) 0.5327, adj growth 19.5 bp · C EV +7.81 (adj +2.79) on $24.67, P(profit) 0.2431, adj growth 24.7 bp · R EV +1.09 (adj +0.38) on $10.00, P(profit) 0.7514, adj growth 14.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  464 bet sides mapped, 5 +EV candidates, 4 on card

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
| Mason Marchment: 1+ assists NO | 70 | 0.784 | 0.734 | +0.069 | +0.020 | $18.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Teddy Blueger: 1+ goals YES | 11 | 0.144 | 0.131 | +0.027 | +0.014 | $3.53 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.233 | 0.223 | +0.022 | +0.012 | $3.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.781 | 0.746 | +0.047 | +0.011 | $11.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.18 vs 1.47 bp); relationships: KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: SJS offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT19SJTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (3.94 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (1.95 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: second expression of the same thesis: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (4.18 vs 1.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3893): highest fidelity KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3899): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:NET_LOW_VOLUME (p 0.4099): highest fidelity KXNHLSAVE-26OCT19SJTOR-SJYASKAROV30-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT19SJTOR-SJYASKAROV30-26|no (same contract)
- KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.201)
- KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3635, phi -0.168)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3893, phi -0.231)
- KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.209)

portfolios: A EV +3.86 (adj +1.17) on $37.50, P(profit) 0.487, adj growth 10.0 bp · B EV +3.74 (adj +1.32) on $37.29, P(profit) 0.7019, adj growth 11.6 bp · C EV +2.84 (adj +0.85) on $29.03, P(profit) 0.577, adj growth 7.5 bp · R EV +0.23 (adj +0.12) on $1.00, P(profit) 0.1441, adj growth 4.0 bp

## PIT @ UTA  ·  10000 joint draws  ·  482 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.621 / away 0.379

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
| Bryan Rust: 1+ goals YES | 28 | 0.345 | 0.328 | +0.051 | +0.033 | $11.15 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.158 | 0.147 | +0.030 | +0.020 | $5.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.169 | 0.157 | +0.031 | +0.019 | $5.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.321 | 0.306 | +0.037 | +0.022 | $7.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (11.65 vs 8.29 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.756); relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes has the higher standalone adjusted growth (11.65 vs 7.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1|yes; why: higher confidence-adjusted growth (6.49 vs 0.96 bp); despite a smaller raw edge (+0.031 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: UTA offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes has the higher standalone adjusted growth (11.65 vs 5.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3756): highest fidelity KXNHLAST-26OCT19PITUTA-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.2965): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.5017): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.278)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.185)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.2965, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.272)

portfolios: A EV +5.35 (adj +2.68) on $37.50, P(profit) 0.5686, adj growth 22.9 bp · B EV +5.29 (adj +3.34) on $28.78, P(profit) 0.5414, adj growth 29.0 bp · C EV +2.84 (adj +1.82) on $26.71, P(profit) 0.345, adj growth 15.8 bp · R EV +0.52 (adj +0.34) on $3.00, P(profit) 0.345, adj growth 11.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
