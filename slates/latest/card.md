# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T04:08:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +23.07 | +6.12 | +22.67 | 0.654 | -47.76 | -64.78 | 46.54 |
| B thesis-diversified (joint) ← optimiser card | 106.18 | +14.89 | +4.75 | +14.39 | 0.660 | -28.86 | -41.53 | 41.67 |
| C best expression per thesis | 62.58 | +12.28 | +3.90 | +4.75 | 0.653 | -22.49 | -33.67 | 34.04 |
| R FUNDED research stakes | 31.00 | +4.51 | +1.44 | +4.07 | 0.641 | -8.21 | -12.18 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.01 | 28.0/28.4 | 25.3/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.46 | 5.91 | 27.7/28.2 | 25.1/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.102 | 0.55 | 0.45 | 0.00 | 6.0 | 22.2/33.6 | 30.1/18.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.53 | 0.47 | 0.49 | 5.86 | 22.2/33.7 | 30.5/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.61 | 0.39 | 0.00 | 9.25 | 29.2/29.8 | 24.3/22.6 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.059 | 0.56 | 0.44 | 0.00 | 9.18 | 23.9/35.7 | 29.2/18.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_CAR_win | p_overtime | goals | shots WPG/CAR | WPG/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.132 | 0.40 | 0.60 | 0.00 | 6.01 | 20.8/32.8 | 28.8/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.47 | 0.53 | 0.49 | 6.02 | 21.0/32.8 | 29.3/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.50 | 0.50 | 0.00 | 6.02 | 26.4/27.1 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.50 | 0.50 | 0.50 | 5.92 | 26.5/27.1 | 23.8/23.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.090 | 0.40 | 0.60 | 0.00 | 9.24 | 22.3/34.4 | 27.4/17.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 9.34 | 27.9/28.7 | 22.4/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg wins by over 1.5 goals YES | 20 | 0.265 | 0.230 | +0.053 | +0.019 | $3.92 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 74 | 0.811 | 0.773 | +0.058 | +0.019 | $17.95 | FUNDED_RESEARCH | $5 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: higher confidence-adjusted growth (4.53 vs 4.52 bp); despite a smaller raw edge (+0.053 vs +0.058/contract); relationships: KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.29); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes has the higher standalone adjusted growth (4.53 vs 4.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.290); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.29); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS_BY_2PLUS (p 0.2647): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR3|no (same contract)
- thesis WPG:WINS (p 0.4783): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR3|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3742): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5217, phi -0.627)
- KXNHLSPREAD-26OCT17CARWPG-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3028, phi -0.733)

portfolios: A EV +3.77 (adj +1.25) on $27.78, P(profit) 0.6972, adj growth 9.6 bp · B EV +2.36 (adj +0.81) on $21.86, P(profit) 0.811, adj growth 7.1 bp · C EV +1.34 (adj +0.47) on $5.31, P(profit) 0.2647, adj growth 4.1 bp · R EV +0.64 (adj +0.22) on $6.00, P(profit) 0.811, adj growth 7.6 bp

## VAN @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.72 | 0.28 | 0.00 | 6.05 | 33.3/20.7 | 18.3/28.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.58 | 0.42 | 0.49 | 5.88 | 33.4/21.0 | 17.9/30.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 9.2 | 35.1/22.3 | 18.1/26.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.66 | 0.34 | 0.00 | 6.01 | 27.4/26.5 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.52 | 0.48 | 0.45 | 5.97 | 27.5/26.8 | 23.6/24.2 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.073 | 0.69 | 0.31 | 0.00 | 3.49 | 31.8/19.6 | 18.3/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 11 | 0.179 | 0.142 | +0.063 | +0.025 | $3.62 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 44 | 0.599 | 0.489 | +0.142 | +0.032 | $3.27 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 1.5 goals scored NO | 8 | 0.131 | 0.103 | +0.046 | +0.018 | $1.61 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | FRAGILE (0.41) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 58 | 0.722 | 0.626 | +0.125 | +0.029 | $11.19 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT17VANTB-VAN2|yes selected over broad KXNHLSPREAD-26OCT17VANTB-VAN3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.57 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.382); KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no: REINFORCING (phi 0.45); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.29); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB3|no; why: Broad expression KXNHLSPREAD-26OCT17VANTB-TB2|no selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no because adjusted EV is 1.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17VANTB-VAN2|yes: DUPLICATIVE (phi 0.382); KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.317); KXNHLSPREAD-26OCT17VANTB-TB3|no: DUPLICATIVE (phi 0.759); failure: TBL wins by 2+
- **Tampa Bay over 1.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN3|yes has the higher standalone adjusted growth (17.01 vs 8.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.383); relationships: KXNHLSPREAD-26OCT17VANTB-VAN2|yes: REINFORCING (phi 0.45); KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.317); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.241); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (9.04 vs 7.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.759); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-VAN2|yes: REINFORCING (phi 0.29); KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.759); KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no: REINFORCING (phi 0.241); failure: TBL wins by 2+

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, TBL shot control · high event (8+) · decided (2+) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.1795): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3154): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17VANTB-TB4|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no kept
- thesis VAN:WINS (p 0.368): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- KXNHLSPREAD-26OCT17VANTB-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.632, phi -0.613)
- KXNHLSPREAD-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.9 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4006, phi -1.0)
- KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; loses 58% of the draws where the thesis happens; opposing: failure thesis TBL:WINS (p 0.632, phi -0.459)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.7 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4006, phi -0.759)
- override: Broad expression KXNHLSPREAD-26OCT17VANTB-TB2|no selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no because adjusted EV is 1.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT17VANTB-VAN2|yes selected over broad KXNHLSPREAD-26OCT17VANTB-VAN3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.57 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17VANTB-TB4|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no kept

portfolios: A EV +8.66 (adj +1.62) on $27.78, P(profit) 0.5414, adj growth 12.1 bp · B EV +6.16 (adj +1.90) on $19.68, P(profit) 0.5994, adj growth 16.5 bp · C EV +6.21 (adj +1.91) on $14.22, P(profit) 0.5994, adj growth 16.5 bp · R EV +2.01 (adj +0.64) on $6.00, P(profit) 0.5994, adj growth 20.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.54 | 0.46 | 0.00 | 6.04 | 27.6/27.0 | 23.6/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.60 | 0.40 | 0.00 | 5.95 | 32.7/21.4 | 18.5/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.48 | 5.97 | 27.9/27.4 | 24.1/24.4 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.43 | 5.9 | 33.0/21.6 | 18.5/29.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.23 | 29.0/28.5 | 22.7/22.9 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.073 | 0.58 | 0.42 | 0.00 | 9.23 | 34.5/23.1 | 17.9/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Seattle wins by over 1.5 goals YES | 19 | 0.254 | 0.219 | +0.053 | +0.018 | $3.90 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 73 | 0.799 | 0.762 | +0.055 | +0.018 | $14.89 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no; why: higher confidence-adjusted growth (4.64 vs 3.80 bp); despite a smaller raw edge (+0.053 vs +0.055/contract); relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: REINFORCING (phi 0.292); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes has the higher standalone adjusted growth (4.64 vs 3.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.292); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes: REINFORCING (phi 0.292); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS_BY_2PLUS (p 0.2536): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes (same contract)
- thesis SEA:WINS (p 0.4726): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.36): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5274, phi -0.616)
- KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3098, phi -0.749)

portfolios: A EV +3.86 (adj +1.28) on $27.78, P(profit) 0.6902, adj growth 9.8 bp · B EV +2.13 (adj +0.72) on $18.79, P(profit) 0.7989, adj growth 6.4 bp · C EV +1.36 (adj +0.48) on $5.17, P(profit) 0.2536, adj growth 4.1 bp · R EV +0.56 (adj +0.19) on $5.00, P(profit) 0.7989, adj growth 6.6 bp

## NYI @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.02 | 28.0/28.6 | 25.3/24.4 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.115 | 0.48 | 0.52 | 0.00 | 6.0 | 22.2/34.2 | 30.4/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.46 | 5.93 | 27.8/28.3 | 24.9/24.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.47 | 5.94 | 22.4/34.2 | 30.9/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.57 | 0.43 | 0.00 | 9.29 | 29.4/30.0 | 24.2/22.5 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.072 | 0.48 | 0.52 | 0.00 | 9.42 | 24.0/36.0 | 29.3/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.56 | 0.44 | 0.00 | 6.0 | 27.1/27.6 | 24.3/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.50 | 5.97 | 27.1/27.4 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.36 | 28.6/28.9 | 23.0/22.3 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.090 | 0.47 | 0.53 | 0.00 | 5.96 | 21.8/32.7 | 29.0/18.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.49 | 0.51 | 0.45 | 5.94 | 21.8/32.8 | 29.2/18.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.061 | 0.45 | 0.55 | 0.00 | 9.3 | 23.3/34.3 | 27.5/17.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.51 | 0.49 | 0.00 | 6.06 | 27.8/27.4 | 23.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.47 | 5.96 | 27.9/27.4 | 24.1/24.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.096 | 0.59 | 0.41 | 0.00 | 6.03 | 32.7/21.6 | 18.6/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.52 | 0.48 | 0.43 | 5.91 | 33.1/21.9 | 18.7/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.51 | 0.49 | 0.00 | 9.27 | 29.4/29.1 | 23.1/23.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.066 | 0.59 | 0.41 | 0.00 | 9.14 | 34.8/23.3 | 18.2/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.50 | 0.50 | 0.00 | 5.96 | 25.7/26.0 | 22.6/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.47 | 5.83 | 25.8/26.3 | 23.0/22.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.102 | 0.43 | 0.57 | 0.00 | 5.95 | 20.6/31.3 | 27.4/17.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.49 | 0.51 | 0.47 | 5.75 | 20.3/31.2 | 28.1/17.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.48 | 0.52 | 0.00 | 3.44 | 24.7/25.2 | 23.3/22.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.48 | 0.52 | 0.45 | 2.71 | 24.4/24.6 | 23.1/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 1.5 goals NO | 66 | 0.721 | 0.688 | +0.045 | +0.012 | $10.10 | FUNDED_RESEARCH | $3 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 1.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17OTTPHI-OTT3|no; why: higher confidence-adjusted growth (1.52 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:WINS (p 0.483): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17OTTPHI-OTT2|no (same contract)
- KXNHLSPREAD-26OCT17OTTPHI-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2789, phi -1.0)

portfolios: A EV +0.75 (adj +0.20) on $11.11, P(profit) 0.7211, adj growth 1.8 bp · B EV +0.68 (adj +0.18) on $10.10, P(profit) 0.7211, adj growth 1.6 bp · C EV +0.68 (adj +0.18) on $10.10, P(profit) 0.7211, adj growth 1.6 bp · R EV +0.20 (adj +0.05) on $3.00, P(profit) 0.7211, adj growth 1.9 bp

## NYR @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.120 | 0.66 | 0.34 | 0.00 | 6.02 | 32.0/20.9 | 18.1/27.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.58 | 0.42 | 0.00 | 6.0 | 26.9/26.3 | 23.1/22.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.46 | 5.86 | 32.3/21.0 | 17.8/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.48 | 0.52 | 0.46 | 5.9 | 27.0/26.5 | 23.3/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.57 | 0.43 | 0.00 | 9.21 | 28.1/27.5 | 22.0/21.8 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.062 | 0.67 | 0.33 | 0.00 | 9.17 | 33.7/22.1 | 17.5/26.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.46 | 0.54 | 0.00 | 6.0 | 25.6/26.2 | 22.6/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.49 | 5.86 | 25.4/25.9 | 22.7/22.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.107 | 0.38 | 0.62 | 0.00 | 6.01 | 20.0/31.0 | 26.7/17.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.46 | 0.54 | 0.49 | 5.84 | 20.2/31.1 | 27.8/17.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.45 | 0.55 | 0.00 | 9.32 | 27.1/27.6 | 21.4/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.065 | 0.38 | 0.62 | 0.00 | 9.25 | 21.8/33.2 | 25.8/16.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 72 | 0.802 | 0.759 | +0.068 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.686 | 0.640 | +0.069 | +0.024 | $2.92 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 3.5 goals scored YES | 29 | 0.357 | 0.321 | +0.053 | +0.017 | $2.61 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL2|no; why: higher confidence-adjusted growth (6.77 vs 5.24 bp); despite a smaller raw edge (+0.068 vs +0.069/contract); relationships: KXNHLSPREAD-26OCT17DALCHI-DAL2|no: DUPLICATIVE (phi 0.734); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes: REINFORCING (phi 0.311); failure: DAL wins by 2+
- **Dallas wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (6.77 vs 5.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.734); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: DUPLICATIVE (phi 0.734); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes: REINFORCING (phi 0.399); failure: DAL wins by 2+
- **Chicago over 3.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (6.77 vs 2.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.311); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: REINFORCING (phi 0.311); KXNHLSPREAD-26OCT17DALCHI-DAL2|no: REINFORCING (phi 0.399); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS (p 0.4623): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3466): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2448): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- KXNHLSPREAD-26OCT17DALCHI-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3139, phi -0.734)
- KXNHLSPREAD-26OCT17DALCHI-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3139, phi -1.0)
- KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4371, phi -0.657)

portfolios: A EV +3.49 (adj +1.17) on $27.78, P(profit) 0.7096, adj growth 9.4 bp · B EV +2.64 (adj +0.92) on $25.53, P(profit) 0.8022, adj growth 8.2 bp · C EV +1.85 (adj +0.67) on $20.00, P(profit) 0.8022, adj growth 6.1 bp · R EV +0.75 (adj +0.26) on $7.00, P(profit) 0.6983, adj growth 9.0 bp

## STL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.49 | 0.51 | 0.00 | 6.04 | 27.2/27.3 | 23.7/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.45 | 5.93 | 27.5/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.52 | 0.48 | 0.00 | 9.33 | 29.0/29.0 | 23.0/22.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.45 | 0.55 | 0.00 | 5.96 | 21.9/32.5 | 28.8/18.6 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.0 | 32.7/21.9 | 18.8/28.5 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.52 | 0.48 | 0.47 | 5.9 | 32.6/22.1 | 18.9/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.53 | 0.47 | 0.00 | 5.97 | 28.1/27.6 | 24.3/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.48 | 5.89 | 28.2/27.8 | 24.5/25.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.56 | 0.44 | 0.00 | 6.03 | 33.5/21.9 | 18.8/29.5 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.57 | 0.43 | 0.49 | 5.87 | 33.4/22.1 | 18.9/30.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.51 | 0.49 | 0.00 | 9.24 | 29.4/29.0 | 23.2/23.4 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 9.18 | 35.4/23.5 | 18.4/28.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.54 | 0.46 | 0.00 | 6.08 | 27.3/27.3 | 23.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 9.47 | 29.3/29.2 | 23.4/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.48 | 5.98 | 27.5/27.5 | 24.3/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 6.09 | 33.0/22.1 | 19.2/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.067 | 0.64 | 0.36 | 0.00 | 9.41 | 34.3/23.3 | 18.4/26.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.46 | 5.96 | 32.8/22.0 | 18.8/29.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.65 | 0.35 | 0.00 | 6.06 | 27.5/27.3 | 24.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.54 | 0.46 | 0.46 | 5.95 | 27.6/27.5 | 24.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.66 | 0.34 | 0.00 | 9.39 | 29.1/28.6 | 23.6/22.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.087 | 0.70 | 0.30 | 0.00 | 6.02 | 32.5/21.6 | 19.1/27.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.54 | 0.46 | 0.47 | 5.91 | 32.5/21.9 | 18.7/29.1 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.068 | 0.73 | 0.27 | 0.00 | 9.35 | 34.0/22.9 | 18.4/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 1.5 goals NO | 54 | 0.617 | 0.571 | +0.059 | +0.013 | $3.97 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 67 | 0.735 | 0.697 | +0.049 | +0.012 | $4.33 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas over 3.5 goals scored NO | 44 | 0.502 | 0.468 | +0.044 | +0.011 | $1.92 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17PITVGK-VGK3|no; why: higher confidence-adjusted growth (1.58 vs 1.41 bp); relationships: KXNHLSPREAD-26OCT17PITVGK-VGK3|no: DUPLICATIVE (phi 0.762); KXNHLTEAMTOTAL-26OCT17PITVGK-VGK4|no: REINFORCING (phi 0.56); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17PITVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17PITVGK-VGK2|no has the higher standalone adjusted growth (1.58 vs 1.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.762); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17PITVGK-VGK2|no: DUPLICATIVE (phi 0.762); KXNHLTEAMTOTAL-26OCT17PITVGK-VGK4|no: REINFORCING (phi 0.513); failure: VGK wins by 2+
- **Vegas over 3.5 goals scored NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17PITVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17PITVGK-VGK2|no has the higher standalone adjusted growth (1.58 vs 1.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.560); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17PITVGK-VGK2|no: REINFORCING (phi 0.56); KXNHLSPREAD-26OCT17PITVGK-VGK3|no: REINFORCING (phi 0.513); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.414): highest fidelity KXNHLSPREAD-26OCT17PITVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17PITVGK-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.3049): highest fidelity KXNHLSPREAD-26OCT17PITVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17PITVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17PITVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3835, phi -1.0)
- KXNHLSPREAD-26OCT17PITVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3835, phi -0.762)
- KXNHLTEAMTOTAL-26OCT17PITVGK-VGK4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4879, phi -0.979)

portfolios: A EV +2.54 (adj +0.60) on $27.78, P(profit) 0.653, adj growth 3.9 bp · B EV +0.92 (adj +0.22) on $10.22, P(profit) 0.653, adj growth 1.9 bp · C EV +0.82 (adj +0.19) on $7.78, P(profit) 0.6165, adj growth 1.6 bp · R EV +0.35 (adj +0.08) on $4.00, P(profit) 0.653, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
