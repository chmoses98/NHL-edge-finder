# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T11:12:47Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +19.30 | +5.41 | +17.75 | 0.659 | -36.13 | -49.36 | 44.52 |
| B thesis-diversified (joint) ← optimiser card | 149.06 | +18.04 | +6.33 | +18.57 | 0.686 | -29.04 | -43.01 | 56.62 |
| C best expression per thesis | 123.67 | +14.26 | +5.09 | +12.54 | 0.703 | -22.18 | -43.94 | 45.21 |
| R FUNDED research stakes | 37.00 | +4.04 | +1.51 | +3.55 | 0.638 | -9.01 | -12.73 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_NSH_win | p_overtime | goals | shots BOS/NSH | BOS/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.64 | 0.36 | 0.00 | 6.07 | 28.1/28.0 | 25.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.50 | 6.0 | 28.0/28.0 | 24.5/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.38 | 29.7/29.6 | 24.3/22.6 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.082 | 0.69 | 0.31 | 0.00 | 6.06 | 32.8/22.0 | 19.4/28.2 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.46 | 5.96 | 33.1/22.6 | 19.4/29.7 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.060 | 0.70 | 0.30 | 0.00 | 9.4 | 34.6/23.6 | 18.7/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 7.5 goals scored YES | 24 | 0.298 | 0.267 | +0.045 | +0.014 | $3.31 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored YES | 55 | 0.611 | 0.578 | +0.043 | +0.010 | $1.97 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: Broad expression KXNHLTOTAL-26OCT22NSHBOS-8|yes selected over broad KXNHLTOTAL-26OCT22NSHBOS-9|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.75 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTOTAL-26OCT22NSHBOS-6|yes: DUPLICATIVE (phi 0.52); failure: NSH offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-9|yes; why: KXNHLTOTAL-26OCT22NSHBOS-9|yes has the higher standalone adjusted growth (2.92 vs 0.97 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.428); relationships: KXNHLTOTAL-26OCT22NSHBOS-8|yes: DUPLICATIVE (phi 0.52); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.298): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes — Broad expression KXNHLTOTAL-26OCT22NSHBOS-8|yes selected over broad KXNHLTOTAL-26OCT22NSHBOS-9|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.75 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis BOS:OFFENSE_4PLUS (p 0.4752): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTOTAL-26OCT22NSHBOS-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NSH:SUPPRESSED (p 0.4347, phi -0.412)
- KXNHLTOTAL-26OCT22NSHBOS-6|yes: FUNDED_RESEARCH; family MIXED; loses 12% of the draws where the thesis happens; opposing: failure thesis GAME:LOW_EVENT (p 0.2135, phi -0.652)
- override: Broad expression KXNHLTOTAL-26OCT22NSHBOS-8|yes selected over broad KXNHLTOTAL-26OCT22NSHBOS-9|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.75 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.85 (adj +0.86) on $18.64, P(profit) 0.298, adj growth 5.4 bp · B EV +0.74 (adj +0.22) on $5.28, P(profit) 0.298, adj growth 1.9 bp · C EV +0.92 (adj +0.30) on $3.83, P(profit) 0.2229, adj growth 2.6 bp · R EV +0.26 (adj +0.07) on $2.00, P(profit) 0.298, adj growth 2.5 bp

## NYR @ TOR  ·  10000 joint draws  ·  416 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYR_win | p_overtime | goals | shots TOR/NYR | TOR/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.01 | 27.3/27.6 | 23.9/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.46 | 5.93 | 27.3/27.5 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.51 | 0.49 | 0.00 | 9.38 | 28.9/29.0 | 23.0/22.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.076 | 0.46 | 0.54 | 0.00 | 6.07 | 21.8/32.7 | 28.9/18.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.45 | 0.55 | 0.48 | 5.88 | 21.9/32.6 | 29.3/18.8 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 6.03 | 32.2/22.0 | 19.1/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  428 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.02 | 27.0/26.7 | 23.6/22.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.117 | 0.66 | 0.34 | 0.00 | 5.99 | 32.0/20.9 | 18.2/27.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.46 | 5.94 | 27.0/26.5 | 23.1/23.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.54 | 0.46 | 0.50 | 5.87 | 32.2/21.2 | 18.0/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.58 | 0.42 | 0.00 | 9.35 | 28.7/28.2 | 22.4/22.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.070 | 0.65 | 0.35 | 0.00 | 9.27 | 34.3/22.6 | 17.9/26.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  438 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_ANA_win | p_overtime | goals | shots NJD/ANA | NJD/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 28.7/28.6 | 25.1/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.46 | 5.9 | 28.9/28.7 | 25.5/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.56 | 0.44 | 0.00 | 9.29 | 30.1/30.0 | 24.1/23.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.089 | 0.62 | 0.38 | 0.00 | 6.0 | 34.0/22.7 | 19.8/29.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.52 | 0.48 | 0.47 | 5.9 | 34.1/22.9 | 19.8/30.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.32 | 35.7/24.0 | 19.1/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 2.5 goals NO | 70 | 0.791 | 0.743 | +0.077 | +0.029 | $17.80 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 19 | 0.250 | 0.217 | +0.049 | +0.017 | $1.32 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 48 | 0.561 | 0.518 | +0.063 | +0.020 | $1.33 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ2|no; why: higher confidence-adjusted growth (8.78 vs 5.35 bp); relationships: KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: REINFORCING (phi 0.496); failure: NJD wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.78 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.296); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: REINFORCING (phi 0.406); failure: NJD wins (incl. OT/SO)
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (8.78 vs 3.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.496); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: REINFORCING (phi 0.496); KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: REINFORCING (phi 0.406); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS (p 0.4635): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.2501): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis NJD:SUPPRESSED (p 0.3556): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- KXNHLSPREAD-26OCT22ANANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3229, phi -0.743)
- KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.5365, phi -0.621)
- KXNHLTEAMTOTAL-26OCT22ANANJ-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4294, phi -0.98)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT22ANANJ-NJ2|no less than the minimum stake; KXNHLSPREAD-26OCT22ANANJ-ANA3|yes kept

portfolios: A EV +2.51 (adj +0.76) on $19.32, P(profit) 0.5138, adj growth 6.5 bp · B EV +2.40 (adj +0.87) on $20.45, P(profit) 0.7914, adj growth 8.0 bp · C EV +2.15 (adj +0.80) on $20.00, P(profit) 0.7914, adj growth 7.3 bp · R EV +0.91 (adj +0.32) on $7.00, P(profit) 0.5664, adj growth 11.2 bp

## FLA @ PIT  ·  10000 joint draws  ·  444 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.65 | 0.35 | 0.00 | 6.02 | 26.9/26.9 | 24.1/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.48 | 5.98 | 26.9/26.7 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.63 | 0.37 | 0.00 | 9.37 | 28.6/28.6 | 23.2/21.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.72 | 0.28 | 0.00 | 6.09 | 31.7/21.6 | 19.0/26.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.56 | 0.44 | 0.48 | 5.95 | 32.2/21.6 | 18.4/28.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.23 | 33.6/22.7 | 18.3/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 12 | 0.155 | 0.146 | +0.028 | +0.019 | $4.00 | FUNDED_RESEARCH | $2 | PIT:WINS_BY_2PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 71 | 0.792 | 0.748 | +0.067 | +0.024 | $16.24 | FUNDED_RESEARCH | $5 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 16 | 0.193 | 0.185 | +0.024 | +0.015 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 82 | 0.881 | 0.846 | +0.051 | +0.015 | $3.04 | FUNDED_RESEARCH | $1 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no; why: higher confidence-adjusted growth (6.84 vs 6.29 bp); despite a smaller raw edge (+0.028 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLSPREAD-26OCT22FLAPIT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.094); failure: PIT offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3|no; why: higher confidence-adjusted growth (6.29 vs 3.66 bp); wins across more scripts (relative breadth 0.996 vs 0.76); relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLSPREAD-26OCT22FLAPIT-FLA3|no: DUPLICATIVE (phi 0.717); failure: FLA wins by 2+
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no has the higher standalone adjusted growth (6.29 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.144); they share one thesis budget; relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLSPREAD-26OCT22FLAPIT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.116); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22FLAPIT-FLA2|no; why: Broad expression KXNHLSPREAD-26OCT22FLAPIT-FLA3|no selected over broad KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.094); KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: DUPLICATIVE (phi 0.717); KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.116); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.3742): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no (same contract)
- thesis PIT:WINS (p 0.5952): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no (same contract)
- thesis FLA:SUPPRESSED (p 0.4354): highest fidelity KXNHLSPREAD-26OCT22FLAPIT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22FLAPIT-FLA2|no — Broad expression KXNHLSPREAD-26OCT22FLAPIT-FLA3|no selected over broad KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT22FLAPIT-PITBLIZOTTE46-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3004, phi -0.183)
- KXNHLSPREAD-26OCT22FLAPIT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2084, phi -1.0)
- KXNHLGOAL-26OCT22FLAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:WINS (p 0.4048, phi -0.205)
- KXNHLSPREAD-26OCT22FLAPIT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2084, phi -0.717)
- override: Broad expression KXNHLSPREAD-26OCT22FLAPIT-FLA3|no selected over broad KXNHLTEAMTOTAL-26OCT22FLAPIT-FLA3|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.07 (adj +0.63) on $19.32, P(profit) 0.6173, adj growth 5.5 bp · B EV +2.98 (adj +1.46) on $26.37, P(profit) 0.2971, adj growth 12.9 bp · C EV +1.85 (adj +0.66) on $20.00, P(profit) 0.7916, adj growth 6.0 bp · R EV +0.96 (adj +0.48) on $8.00, P(profit) 0.8075, adj growth 15.5 bp

## LAK @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_LAK_win | p_overtime | goals | shots NYI/LAK | NYI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.94 | 27.2/27.2 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.49 | 0.51 | 0.48 | 5.89 | 27.3/27.1 | 23.9/24.1 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.080 | 0.61 | 0.39 | 0.00 | 5.98 | 32.1/21.7 | 18.9/27.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.53 | 0.47 | 0.45 | 5.85 | 32.4/21.8 | 18.6/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.55 | 0.45 | 0.00 | 9.14 | 29.0/28.8 | 23.5/22.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.070 | 0.54 | 0.46 | 0.00 | 3.46 | 25.9/26.0 | 24.3/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.02 | 26.5/26.7 | 23.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.49 | 5.97 | 26.2/26.6 | 23.1/22.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.092 | 0.42 | 0.58 | 0.00 | 6.01 | 21.1/31.8 | 28.0/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.50 | 0.50 | 0.00 | 9.3 | 28.2/28.5 | 22.4/22.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.48 | 0.52 | 0.50 | 5.9 | 20.9/31.5 | 28.2/17.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 9.28 | 22.2/33.2 | 26.4/17.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.63 | 0.37 | 0.00 | 5.96 | 26.0/25.7 | 22.8/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.8 | 26.2/25.9 | 22.7/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 5.93 | 30.8/20.2 | 17.7/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.59 | 0.41 | 0.46 | 5.87 | 31.2/20.7 | 17.8/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 9.2 | 27.3/27.1 | 21.8/20.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.46 | 2.8 | 24.3/24.4 | 22.9/22.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 71 | 0.776 | 0.740 | +0.051 | +0.016 | $11.38 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 59 | 0.660 | 0.622 | +0.053 | +0.015 | $2.61 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (2.78 vs 2.17 bp); despite a smaller raw edge (+0.051 vs +0.053/contract); wins across more scripts (relative breadth 0.983 vs 0.864); relationships: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no: DUPLICATIVE (phi 0.749); failure: DAL wins by 2+
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no has the higher standalone adjusted growth (2.78 vs 2.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.749); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: DUPLICATIVE (phi 0.749); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4478): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3404, phi -0.749)
- KXNHLSPREAD-26OCT22WPGDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3404, phi -1.0)

portfolios: A EV +1.22 (adj +0.37) on $15.45, P(profit) 0.6596, adj growth 3.2 bp · B EV +1.03 (adj +0.32) on $14.00, P(profit) 0.7756, adj growth 2.8 bp · C EV +1.11 (adj +0.35) on $15.76, P(profit) 0.7756, adj growth 3.0 bp · R EV +0.30 (adj +0.09) on $4.00, P(profit) 0.7756, adj growth 3.2 bp

## MIN @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.43 | 0.57 | 0.00 | 5.99 | 29.1/29.5 | 25.5/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.49 | 0.51 | 0.47 | 5.93 | 29.3/29.5 | 26.1/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.16 | 30.8/31.0 | 24.4/25.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.080 | 0.38 | 0.62 | 0.00 | 5.96 | 23.6/34.7 | 30.3/20.6 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.43 | 0.57 | 0.45 | 5.92 | 23.6/35.1 | 31.8/20.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.41 | 0.59 | 0.00 | 3.46 | 28.1/28.5 | 26.3/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 1.5 goals NO | 59 | 0.680 | 0.633 | +0.073 | +0.026 | $11.23 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 72 | 0.795 | 0.752 | +0.060 | +0.018 | $2.94 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary over 3.5 goals scored YES | 27 | 0.344 | 0.302 | +0.061 | +0.018 | $2.53 | FUNDED_RESEARCH | $1 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (6.11 vs 3.73 bp); relationships: KXNHLSPREAD-26OCT22MINCGY-MIN3|no: DUPLICATIVE (phi 0.742); KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes: REINFORCING (phi 0.409); failure: MIN wins by 2+
- **Minnesota wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 3.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.742); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: DUPLICATIVE (phi 0.742); KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes: REINFORCING (phi 0.314); failure: MIN wins by 2+
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.11 vs 3.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.409); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: REINFORCING (phi 0.409); KXNHLSPREAD-26OCT22MINCGY-MIN3|no: REINFORCING (phi 0.314); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.4524): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.335): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.2365): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- KXNHLSPREAD-26OCT22MINCGY-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -1.0)
- KXNHLSPREAD-26OCT22MINCGY-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3196, phi -0.742)
- KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.446, phi -0.65)

portfolios: A EV +2.69 (adj +0.85) on $19.32, P(profit) 0.6998, adj growth 7.3 bp · B EV +2.14 (adj +0.71) on $16.70, P(profit) 0.6804, adj growth 6.4 bp · C EV +2.09 (adj +0.73) on $17.29, P(profit) 0.6804, adj growth 6.5 bp · R EV +0.66 (adj +0.22) on $5.00, P(profit) 0.6804, adj growth 7.6 bp

## CAR @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.9 | 24.8/23.2 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.110 | 0.55 | 0.45 | 0.00 | 6.03 | 21.8/33.5 | 30.1/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.63 | 0.37 | 0.00 | 9.49 | 28.9/29.4 | 24.0/21.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.47 | 6.0 | 27.4/28.1 | 24.8/24.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.97 | 22.0/33.7 | 30.4/18.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.34 | 23.3/35.0 | 28.8/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 69 | 0.764 | 0.725 | +0.059 | +0.019 | $9.94 | FUNDED_RESEARCH | $3 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Edmonton wins by over 1.5 goals YES | 28 | 0.347 | 0.311 | +0.053 | +0.017 | $3.01 | FUNDED_RESEARCH | $1 | EDM:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 80 | 0.855 | 0.825 | +0.044 | +0.014 | $5.42 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes; why: higher confidence-adjusted growth (4.01 vs 3.06 bp); wins across more scripts (relative breadth 1.008 vs 0.535); relationships: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.406); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: DUPLICATIVE (phi 0.74); failure: CAR wins by 2+
- **Edmonton wins by over 1.5 goals YES** — thesis: EDM wins by 2+; alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-CAR2|no has the higher standalone adjusted growth (4.01 vs 3.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.406); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.406); KXNHLSPREAD-26OCT22CAREDM-CAR3|no: DUPLICATIVE (phi 0.3); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-CAR2|no has the higher standalone adjusted growth (4.01 vs 2.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.740); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.74); KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.3); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:WINS (p 0.5634): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- thesis EDM:WINS_BY_2PLUS (p 0.3474): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-CAR2|no (same contract)
- KXNHLSPREAD-26OCT22CAREDM-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -1.0)
- KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4366, phi -0.642)
- KXNHLSPREAD-26OCT22CAREDM-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2361, phi -0.74)

portfolios: A EV +2.03 (adj +0.65) on $19.32, P(profit) 0.3474, adj growth 5.6 bp · B EV +1.67 (adj +0.54) on $18.36, P(profit) 0.7639, adj growth 4.8 bp · C EV +1.51 (adj +0.50) on $18.04, P(profit) 0.7639, adj growth 4.4 bp · R EV +0.54 (adj +0.18) on $6.00, P(profit) 0.7639, adj growth 6.0 bp

## UTA @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 6.0 | 27.4/27.7 | 24.2/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.45 | 0.55 | 0.00 | 6.03 | 21.8/32.9 | 29.1/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.93 | 27.5/28.1 | 24.8/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 9.35 | 28.7/29.2 | 22.9/22.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.46 | 0.54 | 0.46 | 5.95 | 21.8/32.7 | 29.5/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.074 | 0.44 | 0.56 | 0.00 | 9.29 | 23.2/34.7 | 27.8/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Utah wins by over 2.5 goals NO | 74 | 0.817 | 0.776 | +0.064 | +0.023 | $17.37 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah wins by over 1.5 goals NO | 62 | 0.705 | 0.660 | +0.068 | +0.024 | $4.43 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 22 | 0.281 | 0.245 | +0.049 | +0.013 | $1.31 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Utah wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA2|no; why: higher confidence-adjusted growth (6.10 vs 5.22 bp); despite a smaller raw edge (+0.064 vs +0.068/contract); relationships: KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.731); KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: REINFORCING (phi 0.295); failure: UTA wins by 2+
- **Utah wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (6.10 vs 5.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.731); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: DUPLICATIVE (phi 0.731); KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: DUPLICATIVE (phi 0.404); failure: UTA wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: Broad expression KXNHLSPREAD-26OCT22UTASEA-SEA2|yes selected over broad KXNHLSPREAD-26OCT22UTASEA-SEA3|yes because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.62 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: REINFORCING (phi 0.295); KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.404); failure: UTA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS (p 0.4936): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2807): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22UTASEA-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2951, phi -0.731)
- KXNHLSPREAD-26OCT22UTASEA-UTA2|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2951, phi -1.0)
- KXNHLSPREAD-26OCT22UTASEA-SEA2|yes: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS (p 0.5064, phi -0.633)
- override: Broad expression KXNHLSPREAD-26OCT22UTASEA-SEA2|yes selected over broad KXNHLSPREAD-26OCT22UTASEA-SEA3|yes because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.62 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.19 (adj +0.68) on $19.32, P(profit) 0.4076, adj growth 5.9 bp · B EV +2.22 (adj +0.76) on $23.12, P(profit) 0.7049, adj growth 6.8 bp · C EV +1.69 (adj +0.60) on $20.00, P(profit) 0.8173, adj growth 5.5 bp · R EV +0.42 (adj +0.15) on $5.00, P(profit) 0.8173, adj growth 5.5 bp

## DET @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 6.05 | 21.7/33.5 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.8 | 24.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.94 | 27.5/28.1 | 24.8/24.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.50 | 5.91 | 21.8/33.5 | 30.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.34 | 29.0/29.5 | 23.7/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.2 | 23.2/35.2 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 22 | 0.310 | 0.262 | +0.078 | +0.030 | $4.15 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver wins by over 2.5 goals YES | 13 | 0.197 | 0.161 | +0.059 | +0.023 | $1.86 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VAN:WINS_BY_2PLUS | DIRECT (0.63) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 62 | 0.751 | 0.663 | +0.115 | +0.026 | $4.87 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 74 | 0.850 | 0.775 | +0.096 | +0.022 | $13.89 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: higher confidence-adjusted growth (11.22 vs 9.48 bp); relationships: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: DUPLICATIVE (phi 0.738); KXNHLSPREAD-26OCT22DETVAN-DET2|no: DUPLICATIVE (phi 0.385); KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.282); failure: DET wins (incl. OT/SO)
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (11.22 vs 9.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.738); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: DUPLICATIVE (phi 0.738); KXNHLSPREAD-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.285); KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.208); failure: DET wins (incl. OT/SO)
- **Detroit wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (11.22 vs 6.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.385); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: DUPLICATIVE (phi 0.385); KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: REINFORCING (phi 0.285); KXNHLSPREAD-26OCT22DETVAN-DET3|no: DUPLICATIVE (phi 0.731); failure: DET wins by 2+
- **Detroit wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (11.22 vs 5.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.282); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: REINFORCING (phi 0.282); KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: REINFORCING (phi 0.208); KXNHLSPREAD-26OCT22DETVAN-DET2|no: DUPLICATIVE (phi 0.731); failure: DET wins by 2+

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.3098): highest fidelity KXNHLSPREAD-26OCT22DETVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22DETVAN-VAN2|yes: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS (p 0.4617, phi -0.62)
- KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; loses 37% of the draws where the thesis happens; opposing: failure thesis DET:WINS (p 0.4617, phi -0.458)
- KXNHLSPREAD-26OCT22DETVAN-DET2|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.6 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2486, phi -1.0)
- KXNHLSPREAD-26OCT22DETVAN-DET3|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.5 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2486, phi -0.731)

portfolios: A EV +3.74 (adj +0.61) on $19.32, P(profit) 0.6508, adj growth 5.2 bp · B EV +4.84 (adj +1.45) on $24.78, P(profit) 0.7514, adj growth 12.9 bp · C EV +2.94 (adj +1.15) on $8.75, P(profit) 0.3098, adj growth 10.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22DETVAN-VAN|yes == KXNHLGAME-26OCT22DETVAN-DET|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
