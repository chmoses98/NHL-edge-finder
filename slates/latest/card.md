# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T22:51:34Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +37.18 | +10.43 | +34.42 | 0.741 | -33.51 | -50.49 | 88.57 |
| B thesis-diversified (joint) ← optimiser card | 140.22 | +35.77 | +17.37 | +26.86 | 0.669 | -44.88 | -64.59 | 148.43 |
| C best expression per thesis | 142.52 | +33.50 | +13.28 | +27.51 | 0.693 | -37.38 | -53.72 | 115.78 |
| R FUNDED research stakes | 18.00 | +2.89 | +1.38 | +3.01 | 0.581 | -9.03 | -12.16 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  482 bet sides mapped, 10 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 14 | 0.216 | 0.196 | +0.068 | +0.047 | $10.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| A.J. Greer: 2+ goals YES | 1 | 0.029 | 0.024 | +0.018 | +0.013 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 24 | 0.334 | 0.285 | +0.081 | +0.032 | $9.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Dylan Garand: 25+ saves YES | 45 | 0.536 | 0.490 | +0.068 | +0.023 | $11.46 | FUNDED_RESEARCH | $3 | NYR:NET_HIGH_VOLUME | DIRECT (0.94) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (37.60 vs 3.12 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: DUPLICATIVE (phi 0.329); KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (37.60 vs 32.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.329); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: DUPLICATIVE (phi 0.329); KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: ANA offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (11.62 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: MOSTLY_INDEPENDENT (phi 0.037); failure: NYR offense suppressed (<= 2 goals)
- **Dylan Garand: 25+ saves YES** — thesis: NYR net faces heavy volume (33+ shots; ANA pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.037); failure: NYR net faces light volume (<= 25 shots; ANA suppressed)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3856): highest fidelity KXNHLAST-26OCT19ANANYR-ANAAKILLORN17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.446): highest fidelity KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYR:NET_HIGH_VOLUME (p 0.2588): highest fidelity KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.219)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3979, phi -0.129)
- KXNHLAST-26OCT19ANANYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3431, phi -0.243)
- KXNHLSAVE-26OCT19ANANYR-NYRDGARAND33-25|yes: FUNDED_RESEARCH; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:NET_LOW_VOLUME (p 0.3094, phi -0.701)

portfolios: A EV +10.84 (adj +5.21) on $37.50, P(profit) 0.4847, adj growth 45.3 bp · B EV +12.40 (adj +7.28) on $32.86, P(profit) 0.4783, adj growth 60.9 bp · C EV +11.00 (adj +5.83) on $50.00, P(profit) 0.4556, adj growth 50.6 bp · R EV +0.44 (adj +0.15) on $3.00, P(profit) 0.5357, adj growth 5.1 bp

## COL @ PHI  ·  10000 joint draws  ·  466 bet sides mapped, 39 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.323 / away 0.677

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.137 | 0.39 | 0.61 | 0.00 | 5.93 | 21.1/33.4 | 29.2/18.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.45 | 0.55 | 0.46 | 5.87 | 21.4/33.8 | 30.4/18.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.43 | 0.57 | 0.00 | 5.99 | 26.9/27.6 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.50 | 0.50 | 0.47 | 5.9 | 26.9/27.8 | 24.7/23.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.079 | 0.34 | 0.66 | 0.00 | 9.16 | 22.8/35.6 | 28.1/18.1 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.077 | 0.41 | 0.59 | 0.00 | 3.45 | 20.1/32.2 | 29.9/18.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ assists NO | 41 | 0.601 | 0.467 | +0.174 | +0.040 | $13.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ goals NO | 54 | 0.618 | 0.597 | +0.060 | +0.040 | $16.81 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.796 | 0.711 | +0.110 | +0.025 | $15.01 | FUNDED_RESEARCH | $4 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (14.98 vs 14.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.139); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.195); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.172); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no; why: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-2|no has the higher standalone adjusted growth (14.98 vs 13.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.376); relationships: KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no: REINFORCING (phi 0.195); KXNHLSPREAD-26OCT19COLPHI-COL3|no: REINFORCING (phi 0.201); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (42.22 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: REINFORCING (phi 0.201); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4692): highest fidelity KXNHL1P-26OCT19COLPHI-COL|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3134): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2308): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT19COLPHI-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.268)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3872, phi -0.295)
- KXNHLSPREAD-26OCT19COLPHI-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.1 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3232, phi -0.733)

portfolios: A EV +11.58 (adj +1.82) on $37.50, P(profit) 0.7671, adj growth 15.6 bp · B EV +9.60 (adj +2.99) on $45.01, P(profit) 0.7111, adj growth 26.3 bp · C EV +11.55 (adj +3.34) on $31.62, P(profit) 0.6039, adj growth 29.5 bp · R EV +1.19 (adj +0.50) on $9.00, P(profit) 0.5309, adj growth 17.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-PHI|yes == KXNHLGAME-26OCT19COLPHI-COL|no

## SJS @ TOR  ·  10000 joint draws  ·  480 bet sides mapped, 9 +EV candidates, 4 on card

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
| Sam Dickinson: 1+ goals YES | 4 | 0.063 | 0.057 | +0.020 | +0.015 | $3.50 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Troy Stecher: 1+ assists YES | 14 | 0.240 | 0.165 | +0.092 | +0.017 | $3.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | CALIBRATION_WARNING | D |
| Mason Marchment: 1+ assists NO | 71 | 0.784 | 0.742 | +0.059 | +0.018 | $16.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 34 | 0.405 | 0.370 | +0.049 | +0.014 | $6.42 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Dickinson: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19SJTOR-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (10.82 vs 1.95 bp); despite a smaller raw edge (+0.020 vs +0.022/contract); relationships: KXNHLAST-26OCT19SJTOR-TORTSTECHER28-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.038); KXNHLTOTAL-26OCT19SJTOR-6|no: INTENTIONAL_DIVERSIFIER (phi -0.076); failure: SJS offense suppressed (<= 2 goals)
- **Troy Stecher: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT19SJTOR-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (4.77 vs 1.07 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19SJTOR-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLTOTAL-26OCT19SJTOR-6|no: INTENTIONAL_DIVERSIFIER (phi -0.152); failure: TOR offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: KXNHLTOTAL-26OCT19SJTOR-5|no has the higher standalone adjusted growth (3.74 vs 3.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.122); relationships: KXNHLGOAL-26OCT19SJTOR-SJSDICKINSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLAST-26OCT19SJTOR-TORTSTECHER28-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLTOTAL-26OCT19SJTOR-6|no: MOSTLY_INDEPENDENT (phi 0.127); failure: SJS offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.91 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT19SJTOR-SJSDICKINSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.076); KXNHLAST-26OCT19SJTOR-TORTSTECHER28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.152); KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.127); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.4224): highest fidelity KXNHLAST-26OCT19SJTOR-TORTSTECHER28-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19SJTOR-TORTSTECHER28-1|yes (same contract)
- thesis GAME:LOW_EVENT (p 0.2114): highest fidelity KXNHLTOTAL-26OCT19SJTOR-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-5|no — Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.91 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:SUPPRESSED (p 0.3893): highest fidelity KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no (same contract)
- KXNHLGOAL-26OCT19SJTOR-SJSDICKINSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3893, phi -0.111)
- KXNHLAST-26OCT19SJTOR-TORTSTECHER28-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 65% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3635, phi -0.21)
- KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3899, phi -0.201)
- KXNHLTOTAL-26OCT19SJTOR-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2882, phi -0.525)
- override: Broad expression KXNHLTOTAL-26OCT19SJTOR-6|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.91 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.95 (adj +1.74) on $37.50, P(profit) 0.4611, adj growth 13.5 bp · B EV +6.40 (adj +2.30) on $30.76, P(profit) 0.5208, adj growth 19.8 bp · C EV +5.58 (adj +1.38) on $21.11, P(profit) 0.5671, adj growth 12.0 bp · R EV +0.75 (adj +0.42) on $3.00, P(profit) 0.4515, adj growth 13.9 bp

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
| Jack McBain: 1+ goals YES | 12 | 0.169 | 0.156 | +0.042 | +0.028 | $7.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.156 | 0.143 | +0.039 | +0.026 | $6.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 28 | 0.345 | 0.325 | +0.051 | +0.031 | $10.15 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.320 | 0.306 | +0.036 | +0.022 | $7.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1|yes; why: higher confidence-adjusted growth (15.29 vs 2.19 bp); despite a smaller raw edge (+0.042 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes; why: higher confidence-adjusted growth (14.44 vs 9.84 bp); despite a smaller raw edge (+0.039 vs +0.051/contract); relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: PIT offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.44 vs 9.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (14.44 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3756): highest fidelity KXNHLAST-26OCT19PITUTA-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.2965): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no (same contract)
- thesis PIT:NET_LOW_VOLUME (p 0.3663): highest fidelity KXNHLSAVE-26OCT19PITUTA-PITASILOVS37-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT19PITUTA-PITASILOVS37-26|no (same contract)
- KXNHLGOAL-26OCT19PITUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.2965, phi -0.168)
- KXNHLGOAL-26OCT19PITUTA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.209)
- KXNHLGOAL-26OCT19PITUTA-PITBRUST17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.277)
- KXNHLGOAL-26OCT19PITUTA-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4038, phi -0.272)

portfolios: A EV +5.80 (adj +1.66) on $37.50, P(profit) 0.5868, adj growth 14.2 bp · B EV +7.37 (adj +4.80) on $31.59, P(profit) 0.54, adj growth 41.4 bp · C EV +5.37 (adj +2.73) on $39.79, P(profit) 0.5787, adj growth 23.6 bp · R EV +0.52 (adj +0.31) on $3.00, P(profit) 0.3447, adj growth 10.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
