# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T05:03:43Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.47 | +6.50 | +23.77 | 0.649 | -50.65 | -71.32 | 48.67 |
| B thesis-diversified (joint) ← optimiser card | 110.00 | +15.16 | +5.04 | +15.62 | 0.673 | -30.08 | -43.17 | 44.23 |
| C best expression per thesis | 81.29 | +13.64 | +4.46 | +19.93 | 0.602 | -28.92 | -32.43 | 39.03 |
| R FUNDED research stakes | 32.00 | +4.57 | +1.52 | +4.29 | 0.665 | -8.93 | -12.70 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  218 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.59 | 0.41 | 0.00 | 5.99 | 27.9/28.2 | 25.2/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.48 | 5.89 | 27.7/28.3 | 25.1/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.102 | 0.56 | 0.44 | 0.00 | 6.01 | 22.3/33.6 | 30.3/18.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.53 | 0.47 | 0.47 | 5.87 | 22.2/33.7 | 30.4/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.60 | 0.40 | 0.00 | 9.31 | 29.2/29.6 | 24.2/22.5 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.060 | 0.55 | 0.45 | 0.00 | 9.09 | 24.0/35.7 | 29.6/18.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_CAR_win | p_overtime | goals | shots WPG/CAR | WPG/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.130 | 0.40 | 0.60 | 0.00 | 6.01 | 20.8/32.9 | 28.8/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.46 | 0.54 | 0.50 | 6.02 | 20.9/32.8 | 29.3/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.50 | 0.50 | 0.00 | 6.02 | 26.3/27.0 | 23.6/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.51 | 0.49 | 0.49 | 5.93 | 26.6/27.1 | 23.9/23.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.087 | 0.40 | 0.60 | 0.00 | 9.24 | 22.2/34.4 | 27.3/17.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.48 | 0.52 | 0.00 | 9.33 | 28.0/28.9 | 22.7/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 61 | 0.697 | 0.651 | +0.070 | +0.024 | $8.61 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 1.5 goals YES | 20 | 0.265 | 0.230 | +0.053 | +0.019 | $3.28 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 74 | 0.811 | 0.773 | +0.058 | +0.019 | $9.84 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: higher confidence-adjusted growth (5.61 vs 4.53 bp); wins across more scripts (relative breadth 0.946 vs 0.559); relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: DUPLICATIVE (phi 0.395); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: DUPLICATIVE (phi 0.733); failure: CAR wins by 2+
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT17CARWPG-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR2|no has the higher standalone adjusted growth (5.61 vs 4.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.395); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-CAR2|no: DUPLICATIVE (phi 0.395); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.29); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR2|no has the higher standalone adjusted growth (5.61 vs 4.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.733); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-CAR2|no: DUPLICATIVE (phi 0.733); KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.29); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis WPG:WINS (p 0.4783): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no (same contract)
- thesis WPG:WINS_BY_2PLUS (p 0.2647): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3742): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17CARWPG-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3028, phi -1.0)
- KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5217, phi -0.627)
- KXNHLSPREAD-26OCT17CARWPG-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3028, phi -0.733)

portfolios: A EV +4.25 (adj +1.47) on $30.00, P(profit) 0.6972, adj growth 11.4 bp · B EV +2.55 (adj +0.88) on $21.74, P(profit) 0.6972, adj growth 7.7 bp · C EV +1.96 (adj +0.68) on $17.40, P(profit) 0.6972, adj growth 6.0 bp · R EV +0.82 (adj +0.28) on $7.00, P(profit) 0.6972, adj growth 9.5 bp

## VAN @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.154 | 0.73 | 0.27 | 0.00 | 6.04 | 33.2/20.7 | 18.2/28.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.129 | 0.57 | 0.43 | 0.49 | 5.9 | 33.4/21.1 | 18.0/30.0 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.103 | 0.74 | 0.26 | 0.00 | 9.23 | 35.1/22.3 | 18.0/26.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.66 | 0.34 | 0.00 | 6.02 | 27.4/26.5 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.53 | 0.47 | 0.44 | 5.96 | 27.5/26.6 | 23.2/24.2 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 3.48 | 31.7/19.8 | 18.6/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 11 | 0.179 | 0.142 | +0.063 | +0.025 | $3.37 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 4.5 goals scored YES | 9 | 0.145 | 0.115 | +0.049 | +0.019 | $2.35 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 58 | 0.722 | 0.626 | +0.125 | +0.029 | $10.02 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 5.5 goals scored NO | 79 | 0.864 | 0.820 | +0.063 | +0.018 | $16.30 | FUNDED_RESEARCH | $5 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT17VANTB-VAN2|yes selected over broad KXNHLSPREAD-26OCT17VANTB-VAN3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.57 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes: REINFORCING (phi 0.469); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.29); KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no: REINFORCING (phi 0.182); failure: TBL wins (incl. OT/SO)
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN3|yes has the higher standalone adjusted growth (17.01 vs 9.00 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.475); relationships: KXNHLSPREAD-26OCT17VANTB-VAN2|yes: REINFORCING (phi 0.469); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.236); KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no: INTENTIONAL_DIVERSIFIER (phi -0.031); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (9.04 vs 7.90 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.759); relationships: KXNHLSPREAD-26OCT17VANTB-VAN2|yes: REINFORCING (phi 0.29); KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes: REINFORCING (phi 0.236); KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no: REINFORCING (phi 0.445); failure: TBL wins by 2+
- **Tampa Bay over 5.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.41 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17VANTB-VAN2|yes: REINFORCING (phi 0.182); KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes: INTENTIONAL_DIVERSIFIER (phi -0.031); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.445); failure: high-event game (8+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.15, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, TBL shot control · high event (8+) · decided (2+) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.1795): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.2838): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17VANTB-VAN3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes kept
- thesis TBL:SUPPRESSED (p 0.3154): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — Broad expression KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.41 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT17VANTB-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS (p 0.632, phi -0.613)
- KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 49% of the draws where the thesis happens; opposing: failure thesis TBL:WINS (p 0.632, phi -0.416)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.7 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4006, phi -0.759)
- KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2526, phi -0.567)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17VANTB-VAN3|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT17VANTB-TB6|no selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.41 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT17VANTB-VAN2|yes selected over broad KXNHLSPREAD-26OCT17VANTB-VAN3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.57 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.82 (adj +1.85) on $30.00, P(profit) 0.5414, adj growth 13.6 bp · B EV +6.37 (adj +2.06) on $32.03, P(profit) 0.7127, adj growth 17.9 bp · C EV +6.21 (adj +1.91) on $14.22, P(profit) 0.5994, adj growth 16.5 bp · R EV +2.07 (adj +0.68) on $10.00, P(profit) 0.7157, adj growth 22.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-VAN|yes == KXNHLGAME-26OCT17VANTB-TB|no

## SEA @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.03 | 27.4/27.0 | 23.6/23.6 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.112 | 0.60 | 0.40 | 0.00 | 5.96 | 32.8/21.5 | 18.6/28.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.97 | 27.8/27.4 | 24.1/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.44 | 5.89 | 33.1/21.7 | 18.5/29.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.53 | 0.47 | 0.00 | 9.23 | 29.2/28.6 | 22.7/23.2 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.25 | 34.6/23.0 | 18.0/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 60 | 0.690 | 0.643 | +0.073 | +0.026 | $15.70 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 73 | 0.799 | 0.762 | +0.055 | +0.018 | $3.17 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no; why: higher confidence-adjusted growth (6.18 vs 3.80 bp); relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: DUPLICATIVE (phi 0.749); failure: FLA wins by 2+
- **Florida wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no has the higher standalone adjusted growth (6.18 vs 3.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.749); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: DUPLICATIVE (phi 0.749); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS (p 0.4726): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2536): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no (same contract)
- KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3098, phi -1.0)
- KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3098, phi -0.749)

portfolios: A EV +3.68 (adj +1.12) on $30.00, P(profit) 0.6902, adj growth 8.3 bp · B EV +2.10 (adj +0.73) on $18.87, P(profit) 0.6902, adj growth 6.5 bp · C EV +2.12 (adj +0.75) on $17.84, P(profit) 0.6902, adj growth 6.6 bp · R EV +0.55 (adj +0.19) on $5.00, P(profit) 0.6902, adj growth 6.7 bp

## NYI @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 6.02 | 28.0/28.6 | 25.2/24.2 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.114 | 0.49 | 0.51 | 0.00 | 5.99 | 22.2/34.1 | 30.5/18.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.47 | 5.92 | 28.0/28.6 | 25.2/24.7 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.47 | 5.93 | 22.3/34.2 | 30.8/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.57 | 0.43 | 0.00 | 9.3 | 29.4/29.9 | 24.1/23.0 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.072 | 0.48 | 0.52 | 0.00 | 9.41 | 23.9/35.9 | 29.1/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.56 | 0.44 | 0.00 | 5.99 | 27.2/27.5 | 24.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.48 | 6.0 | 27.3/27.7 | 24.4/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.38 | 28.6/28.8 | 23.0/22.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.091 | 0.46 | 0.54 | 0.00 | 5.96 | 21.8/32.7 | 28.8/18.7 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.49 | 0.51 | 0.48 | 5.94 | 21.7/32.6 | 29.3/18.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.060 | 0.44 | 0.56 | 0.00 | 9.25 | 23.4/34.6 | 27.5/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.51 | 0.49 | 0.00 | 6.07 | 27.7/27.4 | 23.8/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.47 | 5.96 | 27.9/27.4 | 24.2/24.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.096 | 0.59 | 0.41 | 0.00 | 6.02 | 32.6/21.6 | 18.6/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.52 | 0.48 | 0.43 | 5.91 | 33.0/21.9 | 18.6/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.51 | 0.49 | 0.00 | 9.27 | 29.3/29.1 | 23.0/23.1 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.066 | 0.59 | 0.41 | 0.00 | 9.14 | 34.8/23.3 | 18.2/28.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.51 | 0.49 | 0.00 | 5.96 | 25.7/26.1 | 22.6/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.48 | 5.8 | 25.6/26.1 | 22.9/22.5 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.101 | 0.42 | 0.58 | 0.00 | 5.95 | 20.6/31.3 | 27.2/17.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.46 | 0.54 | 0.48 | 5.76 | 20.4/31.3 | 28.1/17.3 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.45 | 0.55 | 0.46 | 2.75 | 19.0/29.7 | 28.2/17.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 3.46 | 24.7/25.2 | 23.3/22.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.119 | 0.66 | 0.34 | 0.00 | 6.03 | 32.0/20.9 | 18.0/27.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.59 | 0.41 | 0.00 | 6.0 | 26.9/26.3 | 23.2/23.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.55 | 0.45 | 0.46 | 5.86 | 32.3/21.0 | 17.9/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.47 | 5.91 | 26.9/26.5 | 23.2/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.57 | 0.43 | 0.00 | 9.2 | 28.1/27.5 | 21.6/21.8 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.061 | 0.67 | 0.33 | 0.00 | 9.18 | 33.8/22.1 | 17.3/26.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.47 | 0.53 | 0.00 | 6.02 | 25.6/26.0 | 22.4/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.48 | 5.86 | 25.4/25.9 | 22.6/22.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.105 | 0.38 | 0.62 | 0.00 | 5.99 | 20.0/31.1 | 26.6/17.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.50 | 5.86 | 20.3/31.0 | 27.7/17.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.46 | 0.54 | 0.00 | 9.31 | 27.2/27.8 | 21.5/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.067 | 0.37 | 0.63 | 0.00 | 9.26 | 21.8/32.9 | 25.8/16.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 72 | 0.802 | 0.759 | +0.068 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.686 | 0.640 | +0.069 | +0.024 | $2.92 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 3.5 goals scored YES | 29 | 0.357 | 0.321 | +0.053 | +0.017 | $2.61 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL2|no; why: higher confidence-adjusted growth (6.77 vs 5.24 bp); despite a smaller raw edge (+0.068 vs +0.069/contract); relationships: KXNHLSPREAD-26OCT17DALCHI-DAL2|no: DUPLICATIVE (phi 0.734); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes: REINFORCING (phi 0.311); failure: DAL wins by 2+
- **Dallas wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (6.77 vs 5.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.734); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: DUPLICATIVE (phi 0.734); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes: REINFORCING (phi 0.399); failure: DAL wins by 2+
- **Chicago over 3.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (6.77 vs 2.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.311); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: REINFORCING (phi 0.311); KXNHLSPREAD-26OCT17DALCHI-DAL2|no: REINFORCING (phi 0.399); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:WINS (p 0.4623): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3466): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2448): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- KXNHLSPREAD-26OCT17DALCHI-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3139, phi -0.734)
- KXNHLSPREAD-26OCT17DALCHI-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3139, phi -1.0)
- KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4371, phi -0.657)

portfolios: A EV +3.77 (adj +1.27) on $30.00, P(profit) 0.7096, adj growth 10.0 bp · B EV +2.64 (adj +0.92) on $25.53, P(profit) 0.8022, adj growth 8.2 bp · C EV +1.85 (adj +0.67) on $20.00, P(profit) 0.8022, adj growth 6.1 bp · R EV +0.75 (adj +0.26) on $7.00, P(profit) 0.6983, adj growth 9.0 bp

## STL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.02 | 27.4/27.5 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.92 | 27.3/27.4 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.32 | 28.9/29.2 | 23.0/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.071 | 0.58 | 0.42 | 0.00 | 6.04 | 32.0/21.9 | 18.7/27.9 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.068 | 0.43 | 0.57 | 0.00 | 5.95 | 21.8/32.3 | 28.2/18.7 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.45 | 0.55 | 0.45 | 5.87 | 21.9/32.3 | 28.9/18.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.53 | 0.47 | 0.00 | 6.01 | 28.0/27.7 | 24.3/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.48 | 5.91 | 28.2/27.8 | 24.5/24.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.106 | 0.56 | 0.44 | 0.00 | 6.0 | 33.4/21.8 | 18.6/29.6 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.56 | 0.44 | 0.50 | 5.87 | 33.3/21.8 | 18.7/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 9.31 | 29.4/29.1 | 22.8/23.2 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 9.1 | 35.4/23.6 | 18.6/28.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.09 | 27.3/27.3 | 23.9/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 9.46 | 29.3/29.3 | 23.4/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.47 | 5.98 | 27.5/27.5 | 24.2/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 6.08 | 32.9/22.1 | 19.1/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.068 | 0.64 | 0.36 | 0.00 | 9.43 | 34.3/23.3 | 18.3/26.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.062 | 0.48 | 0.52 | 0.00 | 6.05 | 22.0/32.3 | 28.5/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 6.03 | 27.6/27.4 | 24.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.48 | 5.99 | 27.7/27.5 | 24.3/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.65 | 0.35 | 0.00 | 9.38 | 28.9/28.9 | 23.5/22.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.091 | 0.69 | 0.31 | 0.00 | 6.07 | 32.5/21.6 | 19.2/27.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.069 | 0.72 | 0.28 | 0.00 | 9.35 | 34.3/23.1 | 18.7/25.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.52 | 0.48 | 0.44 | 5.84 | 32.5/21.8 | 18.6/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 1.5 goals NO | 53 | 0.617 | 0.568 | +0.069 | +0.021 | $11.83 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17PITVGK-VGK3|no; why: higher confidence-adjusted growth (3.83 vs 1.41 bp); relationships: only recommended bet in this game; failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.414): highest fidelity KXNHLSPREAD-26OCT17PITVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17PITVGK-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.3049): highest fidelity KXNHLSPREAD-26OCT17PITVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17PITVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17PITVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3835, phi -1.0)

portfolios: A EV +2.95 (adj +0.79) on $30.00, P(profit) 0.653, adj growth 5.4 bp · B EV +1.49 (adj +0.45) on $11.83, P(profit) 0.6165, adj growth 3.9 bp · C EV +1.49 (adj +0.45) on $11.83, P(profit) 0.6165, adj growth 3.9 bp · R EV +0.38 (adj +0.11) on $3.00, P(profit) 0.6165, adj growth 4.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
