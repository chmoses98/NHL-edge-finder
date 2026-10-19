# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T21:10:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +31.76 | +8.73 | +29.86 | 0.714 | -34.29 | -52.77 | 73.15 |
| B thesis-diversified (joint) ← optimiser card | 139.39 | +24.91 | +13.89 | +16.88 | 0.620 | -45.03 | -56.77 | 119.45 |
| C best expression per thesis | 132.12 | +24.16 | +10.98 | +14.47 | 0.613 | -38.01 | -49.45 | 95.45 |
| R FUNDED research stakes | 17.00 | +2.31 | +0.96 | +2.95 | 0.599 | -4.34 | -10.76 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  470 bet sides mapped, 9 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 14 | 0.216 | 0.196 | +0.068 | +0.047 | $10.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| A.J. Greer: 2+ goals YES | 1 | 0.029 | 0.024 | +0.018 | +0.013 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Taylor Raddysh: 1+ goals YES | 9 | 0.117 | 0.109 | +0.021 | +0.013 | $3.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Dylan Garand: 25+ saves YES | 45 | 0.536 | 0.488 | +0.068 | +0.021 | $10.86 | FUNDED_RESEARCH | $3 | NYR:NET_HIGH_VOLUME | DIRECT (0.94) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (37.60 vs 3.12 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: DUPLICATIVE (phi 0.329); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (37.60 vs 32.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.329); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: DUPLICATIVE (phi 0.329); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: ANA offense suppressed (<= 2 goals)
- **Taylor Raddysh: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (4.33 vs 1.26 bp); despite a smaller raw edge (+0.021 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR offense suppressed (<= 2 goals)
- **Dylan Garand: 25+ saves YES** — thesis: NYR net faces heavy volume (33+ shots; ANA pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR net faces light volume (<= 25 shots; ANA suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3856): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:NET_HIGH_VOLUME (p 0.2588): highest fidelity KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3431): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.219)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.129)
- KXNHLGOAL-26OCT19ANANYR-NYRTRADDYSH14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3431, phi -0.151)
- KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: FUNDED_RESEARCH; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:NET_LOW_VOLUME (p 0.3094, phi -0.701)

portfolios: A EV +10.84 (adj +4.37) on $37.50, P(profit) 0.4847, adj growth 36.9 bp · B EV +10.14 (adj +6.53) on $26.58, P(profit) 0.3095, adj growth 54.3 bp · C EV +9.01 (adj +4.81) on $37.05, P(profit) 0.5385, adj growth 41.2 bp · R EV +0.44 (adj +0.13) on $3.00, P(profit) 0.5357, adj growth 4.4 bp

## COL @ PHI  ·  10000 joint draws  ·  440 bet sides mapped, 39 +EV candidates, 3 on card

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
| T.J. Hughes: 1+ goals NO | 79 | 0.853 | 0.836 | +0.051 | +0.034 | $16.12 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.623 | 0.603 | +0.055 | +0.036 | $13.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.796 | 0.711 | +0.110 | +0.025 | $16.50 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **T.J. Hughes: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (23.21 vs 16.38 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.013); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT19COLPHI-COL3|no: MOSTLY_INDEPENDENT (phi 0.124); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (23.21 vs 11.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.382); relationships: KXNHLGOAL-26OCT19COLPHI-COLTHUGHES13-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.19); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (42.22 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT19COLPHI-COLTHUGHES13-1|no: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.19); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4691): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3134): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2308): highest fidelity KXNHLSPREAD-26OCT19COLPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-PHI2|yes (same contract)
- KXNHLGOAL-26OCT19COLPHI-COLTHUGHES13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.175)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.293)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.1 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3232, phi -0.733)

portfolios: A EV +11.54 (adj +1.43) on $37.50, P(profit) 0.7611, adj growth 11.6 bp · B EV +5.04 (adj +2.18) on $46.50, P(profit) 0.5327, adj growth 20.0 bp · C EV +7.81 (adj +2.79) on $24.67, P(profit) 0.2431, adj growth 24.7 bp · R EV +1.12 (adj +0.40) on $10.00, P(profit) 0.6965, adj growth 14.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  464 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

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
| Mason Marchment: 1+ assists NO | 70 | 0.784 | 0.739 | +0.069 | +0.025 | $19.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Teddy Blueger: 1+ goals YES | 11 | 0.144 | 0.131 | +0.027 | +0.014 | $3.53 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.233 | 0.223 | +0.022 | +0.012 | $3.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.781 | 0.746 | +0.047 | +0.011 | $10.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (6.59 vs 1.47 bp); relationships: KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: SJS offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT19SJTOR-TORCSISSONS15-1|yes; why: higher confidence-adjusted growth (3.94 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT19SJTOR-SJMKESSELRING7-1|yes; why: higher confidence-adjusted growth (1.95 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.035/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: second expression of the same thesis: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (6.59 vs 1.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3893): highest fidelity KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3899): highest fidelity KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes (same contract)
- thesis TOR:OFFENSE_4PLUS (p 0.4224): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.201)
- KXNHLGOAL-26OCT19SJTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3635, phi -0.168)
- KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3893, phi -0.231)
- KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.209)

portfolios: A EV +3.93 (adj +1.58) on $37.50, P(profit) 0.7388, adj growth 13.5 bp · B EV +3.76 (adj +1.46) on $37.29, P(profit) 0.7019, adj growth 13.0 bp · C EV +2.32 (adj +0.91) on $23.73, P(profit) 0.7838, adj growth 8.1 bp · R EV +0.23 (adj +0.12) on $1.00, P(profit) 0.1441, adj growth 4.0 bp

## PIT @ UTA  ·  10000 joint draws  ·  494 bet sides mapped, 10 +EV candidates, 4 on card

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
| Connor Dewar: 1+ goals YES | 11 | 0.156 | 0.142 | +0.039 | +0.025 | $6.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 28 | 0.345 | 0.325 | +0.051 | +0.031 | $10.22 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.169 | 0.157 | +0.031 | +0.019 | $5.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.320 | 0.306 | +0.036 | +0.022 | $7.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes; why: higher confidence-adjusted growth (13.12 vs 9.84 bp); despite a smaller raw edge (+0.039 vs +0.051/contract); relationships: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: PIT offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (13.12 vs 9.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1|yes; why: higher confidence-adjusted growth (6.49 vs 1.51 bp); despite a smaller raw edge (+0.031 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (13.12 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3756): highest fidelity KXNHLAST-26OCT19PITUTA-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.2965): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no (same contract)
- thesis PIT:NET_LOW_VOLUME (p 0.3663): highest fidelity KXNHLSAVE-26OCT19PITUTA-PITASILOVS37-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT19PITUTA-PITASILOVS37-26|no (same contract)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.209)
- KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.277)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.2965, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.272)

portfolios: A EV +5.45 (adj +1.35) on $37.50, P(profit) 0.5868, adj growth 11.2 bp · B EV +5.98 (adj +3.72) on $29.02, P(profit) 0.54, adj growth 32.1 bp · C EV +5.02 (adj +2.47) on $46.67, P(profit) 0.4327, adj growth 21.5 bp · R EV +0.52 (adj +0.31) on $3.00, P(profit) 0.3447, adj growth 10.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
