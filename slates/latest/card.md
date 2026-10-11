# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T08:22:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +22.58 | +4.98 | +25.22 | 0.625 | -68.08 | -90.20 | 27.49 |
| B thesis-diversified (joint) ← optimiser card | 53.72 | +9.12 | +3.05 | +9.48 | 0.631 | -24.11 | -31.52 | 26.84 |
| C best expression per thesis | 47.15 | +7.97 | +2.62 | +2.30 | 0.626 | -20.61 | -30.53 | 23.18 |
| R FUNDED research stakes | 17.00 | +2.90 | +0.96 | +2.74 | 0.604 | -8.88 | -10.36 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.60 | 0.40 | 0.00 | 6.04 | 27.5/27.1 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.48 | 5.93 | 27.4/27.3 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.60 | 0.40 | 0.00 | 9.29 | 29.3/28.9 | 23.5/22.7 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.65 | 0.35 | 0.00 | 6.02 | 32.5/21.7 | 19.0/28.2 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.56 | 0.44 | 0.49 | 5.93 | 32.8/21.7 | 18.5/29.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 9.32 | 34.6/23.0 | 18.3/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington wins by over 1.5 goals NO | 57 | 0.652 | 0.609 | +0.065 | +0.021 | $9.70 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Washington wins by over 2.5 goals NO | 70 | 0.767 | 0.731 | +0.052 | +0.016 | $4.06 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 18 | 0.229 | 0.202 | +0.038 | +0.012 | $1.41 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no; why: higher confidence-adjusted growth (4.12 vs 2.85 bp); relationships: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT11SEAWSH-SEA2|yes: DUPLICATIVE (phi 0.398); failure: WSH wins by 2+
- **Washington wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no has the higher standalone adjusted growth (4.12 vs 2.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.755); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT11SEAWSH-SEA2|yes: DUPLICATIVE (phi 0.3); failure: WSH wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no has the higher standalone adjusted growth (4.12 vs 1.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.398); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: DUPLICATIVE (phi 0.398); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: DUPLICATIVE (phi 0.3); failure: WSH wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS (p 0.4296): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2288): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.348, phi -1.0)
- KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.348, phi -0.755)
- KXNHLSPREAD-26OCT11SEAWSH-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS (p 0.5704, phi -0.628)

portfolios: A EV +5.85 (adj +1.83) on $50.00, P(profit) 0.652, adj growth 9.6 bp · B EV +1.65 (adj +0.53) on $15.17, P(profit) 0.652, adj growth 4.7 bp · C EV +1.49 (adj +0.49) on $13.45, P(profit) 0.652, adj growth 4.3 bp · R EV +0.68 (adj +0.22) on $6.00, P(profit) 0.652, adj growth 6.8 bp

## VAN @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.61 | 0.39 | 0.00 | 5.99 | 26.7/26.5 | 23.4/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.96 | 26.8/26.6 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.27 | 28.1/27.8 | 22.6/21.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.092 | 0.71 | 0.29 | 0.00 | 6.0 | 31.3/20.8 | 18.3/26.7 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.55 | 0.45 | 0.50 | 5.97 | 31.7/21.1 | 17.9/28.3 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.060 | 0.70 | 0.30 | 0.00 | 9.22 | 33.0/22.2 | 17.6/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver over 4.5 goals scored YES | 11 | 0.184 | 0.142 | +0.068 | +0.025 | $3.96 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 15 | 0.219 | 0.182 | +0.060 | +0.023 | $2.52 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York R wins by over 1.5 goals NO | 52 | 0.649 | 0.562 | +0.111 | +0.024 | $5.06 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York R wins by over 2.5 goals NO | 66 | 0.767 | 0.694 | +0.091 | +0.018 | $3.84 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6|yes; why: higher confidence-adjusted growth (13.38 vs 9.03 bp); wins across more scripts (relative breadth 0.541 vs 0.346); relationships: KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.488); KXNHLSPREAD-26OCT11VANNYR-NYR2|no: REINFORCING (phi 0.314); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: REINFORCING (phi 0.242); failure: NYR wins (incl. OT/SO)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes has the higher standalone adjusted growth (13.38 vs 8.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.488); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes: REINFORCING (phi 0.488); KXNHLSPREAD-26OCT11VANNYR-NYR2|no: DUPLICATIVE (phi 0.39); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: REINFORCING (phi 0.293); failure: NYR wins (incl. OT/SO)
- **New York R wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR3|no; why: higher confidence-adjusted growth (5.23 vs 3.37 bp); relationships: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes: REINFORCING (phi 0.314); KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: DUPLICATIVE (phi 0.39); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: DUPLICATIVE (phi 0.75); failure: NYR wins by 2+
- **New York R wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR2|no; why: Broad expression KXNHLSPREAD-26OCT11VANNYR-NYR3|no selected over broad KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes: REINFORCING (phi 0.242); KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.293); KXNHLSPREAD-26OCT11VANNYR-NYR2|no: DUPLICATIVE (phi 0.75); failure: NYR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2807): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2194): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis NYR:WINS (p 0.5731, phi -0.436)
- KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS (p 0.5731, phi -0.614)
- KXNHLSPREAD-26OCT11VANNYR-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.4 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.3512, phi -1.0)
- KXNHLSPREAD-26OCT11VANNYR-NYR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.2 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.3512, phi -0.75)
- override: Broad expression KXNHLSPREAD-26OCT11VANNYR-NYR3|no selected over broad KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +11.24 (adj +1.76) on $50.00, P(profit) 0.5377, adj growth 8.6 bp · B EV +4.82 (adj +1.56) on $15.39, P(profit) 0.2851, adj growth 13.5 bp · C EV +4.61 (adj +1.44) on $13.70, P(profit) 0.6554, adj growth 12.5 bp · R EV +1.51 (adj +0.48) on $5.00, P(profit) 0.6554, adj growth 16.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.151 | 0.43 | 0.57 | 0.00 | 5.97 | 20.4/32.6 | 28.7/17.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.47 | 0.53 | 0.50 | 5.89 | 20.4/32.7 | 29.3/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.53 | 0.47 | 0.00 | 5.99 | 25.8/26.5 | 23.3/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.47 | 5.94 | 26.2/27.0 | 23.7/23.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.086 | 0.43 | 0.57 | 0.00 | 9.16 | 21.8/34.5 | 27.5/16.7 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.079 | 0.45 | 0.55 | 0.47 | 2.81 | 19.4/31.3 | 29.7/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 74 | 0.824 | 0.780 | +0.071 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 20 | 0.263 | 0.229 | +0.051 | +0.018 | $3.16 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes; why: higher confidence-adjusted growth (8.11 vs 4.04 bp); wins across more scripts (relative breadth 1.019 vs 0.55); relationships: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: REINFORCING (phi 0.276); failure: CAR wins by 2+
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (8.11 vs 4.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.276); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11CARPHI-CAR3|no: REINFORCING (phi 0.276); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:WINS (p 0.478): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.2626): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3491): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT11CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2868, phi -0.728)
- KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.522, phi -0.624)

portfolios: A EV +5.49 (adj +1.39) on $50.00, P(profit) 0.5513, adj growth 9.4 bp · B EV +2.65 (adj +0.96) on $23.16, P(profit) 0.8242, adj growth 8.7 bp · C EV +1.88 (adj +0.69) on $20.00, P(profit) 0.8242, adj growth 6.4 bp · R EV +0.71 (adj +0.26) on $6.00, P(profit) 0.8242, adj growth 9.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
