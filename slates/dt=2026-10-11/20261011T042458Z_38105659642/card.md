# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T04:24:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.34 | +5.63 | +27.20 | 0.605 | -71.40 | -98.37 | 26.96 |
| B thesis-diversified (joint) ← optimiser card | 54.43 | +7.53 | +2.28 | +8.20 | 0.610 | -22.66 | -32.23 | 19.93 |
| C best expression per thesis | 45.35 | +7.24 | +2.33 | +3.76 | 0.626 | -19.14 | -32.66 | 20.36 |
| R FUNDED research stakes | 18.00 | +2.71 | +0.84 | +1.71 | 0.615 | -8.62 | -11.42 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.03 | 27.7/27.3 | 24.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.49 | 5.93 | 27.4/27.2 | 23.9/24.1 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.097 | 0.65 | 0.35 | 0.00 | 6.03 | 32.4/21.5 | 18.7/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.32 | 29.3/29.0 | 23.4/22.4 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.48 | 5.92 | 32.7/21.9 | 18.7/29.1 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.070 | 0.68 | 0.32 | 0.00 | 9.25 | 34.5/23.0 | 18.4/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Washington wins by over 1.5 goals NO | 57 | 0.652 | 0.609 | +0.065 | +0.021 | $9.70 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Washington wins by over 2.5 goals NO | 70 | 0.767 | 0.731 | +0.052 | +0.016 | $4.06 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 18 | 0.229 | 0.202 | +0.038 | +0.012 | $1.41 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Washington wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no; why: higher confidence-adjusted growth (4.12 vs 2.85 bp); relationships: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT11SEAWSH-SEA2|yes: DUPLICATIVE (phi 0.398); failure: WSH wins by 2+
- **Washington wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no has the higher standalone adjusted growth (4.12 vs 2.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.755); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT11SEAWSH-SEA2|yes: DUPLICATIVE (phi 0.3); failure: WSH wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no has the higher standalone adjusted growth (4.12 vs 1.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.398); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: DUPLICATIVE (phi 0.398); KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: DUPLICATIVE (phi 0.3); failure: WSH wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:WINS (p 0.4296): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2288): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.348, phi -1.0)
- KXNHLSPREAD-26OCT11SEAWSH-WSH3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.348, phi -0.755)
- KXNHLSPREAD-26OCT11SEAWSH-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS (p 0.5704, phi -0.628)

portfolios: A EV +5.85 (adj +1.83) on $50.00, P(profit) 0.652, adj growth 9.6 bp · B EV +1.65 (adj +0.53) on $15.17, P(profit) 0.652, adj growth 4.7 bp · C EV +1.49 (adj +0.49) on $13.45, P(profit) 0.652, adj growth 4.3 bp · R EV +0.68 (adj +0.22) on $6.00, P(profit) 0.652, adj growth 6.8 bp

## VAN @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.62 | 0.38 | 0.00 | 5.99 | 26.7/26.5 | 23.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.47 | 5.97 | 26.8/26.6 | 23.2/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.3 | 28.2/27.9 | 22.2/21.4 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.091 | 0.69 | 0.31 | 0.00 | 5.98 | 31.2/20.7 | 18.1/26.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.53 | 0.47 | 0.48 | 5.95 | 31.7/21.2 | 18.0/28.4 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.061 | 0.71 | 0.29 | 0.00 | 9.23 | 33.2/22.2 | 17.7/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 15 | 0.219 | 0.182 | +0.060 | +0.023 | $4.80 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York R wins by over 2.5 goals NO | 66 | 0.767 | 0.694 | +0.091 | +0.018 | $9.69 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 2.5 goals scored YES | 45 | 0.573 | 0.487 | +0.106 | +0.019 | $2.00 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes has the higher standalone adjusted growth (13.38 vs 8.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.488); relationships: KXNHLSPREAD-26OCT11VANNYR-NYR3|no: REINFORCING (phi 0.293); KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes: REINFORCING (phi 0.422); failure: NYR wins (incl. OT/SO)
- **New York R wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR2|no; why: KXNHLSPREAD-26OCT11VANNYR-NYR2|no has the higher standalone adjusted growth (3.86 vs 3.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.750); relationships: KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.293); KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes: REINFORCING (phi 0.427); failure: NYR wins by 2+
- **Vancouver over 2.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes selected over broad KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: REINFORCING (phi 0.422); KXNHLSPREAD-26OCT11VANNYR-NYR3|no: REINFORCING (phi 0.427); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — Broad expression KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes selected over broad KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.2807): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2194): highest fidelity KXNHLSPREAD-26OCT11VANNYR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT11VANNYR-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS (p 0.5731, phi -0.614)
- KXNHLSPREAD-26OCT11VANNYR-NYR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.2 pts; opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.3512, phi -0.75)
- KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.3 pts; opposing: failure thesis VAN:SUPPRESSED (p 0.4371, phi -0.979)
- override: Broad expression KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes selected over broad KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +12.09 (adj +1.86) on $50.00, P(profit) 0.5377, adj growth 6.7 bp · B EV +3.58 (adj +1.05) on $16.49, P(profit) 0.536, adj growth 9.1 bp · C EV +4.15 (adj +1.34) on $11.90, P(profit) 0.6554, adj growth 11.6 bp · R EV +1.39 (adj +0.42) on $6.00, P(profit) 0.536, adj growth 13.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.151 | 0.44 | 0.56 | 0.00 | 5.97 | 20.3/32.7 | 28.7/17.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.47 | 0.53 | 0.50 | 5.89 | 20.4/32.8 | 29.4/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.53 | 0.47 | 0.00 | 5.99 | 25.8/26.5 | 23.3/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.47 | 5.92 | 26.2/27.0 | 23.7/23.0 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.083 | 0.43 | 0.57 | 0.00 | 9.18 | 21.7/34.4 | 27.4/16.6 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.079 | 0.45 | 0.55 | 0.47 | 2.81 | 19.3/31.1 | 29.6/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 75 | 0.824 | 0.782 | +0.061 | +0.019 | $19.91 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia wins by over 1.5 goals YES | 20 | 0.263 | 0.226 | +0.051 | +0.015 | $2.85 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes; why: higher confidence-adjusted growth (4.39 vs 2.98 bp); wins across more scripts (relative breadth 1.019 vs 0.546); relationships: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: REINFORCING (phi 0.276); failure: CAR wins by 2+
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (4.39 vs 2.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.276); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11CARPHI-CAR3|no: REINFORCING (phi 0.276); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:WINS (p 0.478): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- thesis PHI:WINS_BY_2PLUS (p 0.2626): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- KXNHLSPREAD-26OCT11CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2868, phi -0.728)
- KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.522, phi -0.624)

portfolios: A EV +7.40 (adj +1.94) on $50.00, P(profit) 0.7132, adj growth 10.7 bp · B EV +2.29 (adj +0.70) on $22.77, P(profit) 0.8242, adj growth 6.2 bp · C EV +1.60 (adj +0.50) on $20.00, P(profit) 0.8242, adj growth 4.5 bp · R EV +0.64 (adj +0.20) on $6.00, P(profit) 0.8242, adj growth 6.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
