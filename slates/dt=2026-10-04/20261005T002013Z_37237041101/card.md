# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T00:20:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +14.15 | +3.17 | +12.84 | 0.603 | -30.95 | -50.00 | 24.30 |
| B thesis-diversified (joint) ← optimiser card | 43.62 | +8.92 | +4.00 | +8.08 | 0.500 | -27.98 | -43.62 | 34.74 |
| C best expression per thesis | 25.79 | +8.57 | +3.81 | -2.47 | 0.347 | -25.79 | -25.79 | 32.86 |
| R FUNDED research stakes | 10.00 | +2.05 | +0.63 | +2.79 | 0.602 | -10.00 | -10.00 | 0.00 |

## VGK @ VAN  ·  10000 joint draws  ·  338 bet sides mapped, 32 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.286 / away 0.714

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_VGK_win | p_overtime | goals | shots VAN/VGK | VAN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.39 | 0.61 | 0.00 | 6.05 | 27.0/27.6 | 23.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.45 | 5.96 | 27.0/27.4 | 24.1/23.8 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.102 | 0.34 | 0.66 | 0.00 | 5.98 | 21.5/32.7 | 28.1/18.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.49 | 0.51 | 0.46 | 5.91 | 21.6/32.6 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.41 | 0.59 | 0.00 | 9.31 | 28.2/28.7 | 22.1/22.6 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.071 | 0.32 | 0.68 | 0.00 | 9.23 | 22.6/34.1 | 26.4/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 20 | 0.271 | 0.252 | +0.060 | +0.041 | $10.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Vancouver wins YES | 28 | 0.436 | 0.331 | +0.141 | +0.037 | $5.30 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Vegas wins by over 1.5 goals NO | 50 | 0.658 | 0.552 | +0.141 | +0.035 | $8.10 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tomas Hertl: 1+ goals NO | 70 | 0.754 | 0.739 | +0.039 | +0.025 | $19.31 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: higher confidence-adjusted growth (21.74 vs 15.60 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.927 vs 0.485); relationships: KXNHLGAME-26OCT04VGKVAN-VAN|yes: REINFORCING (phi 0.18); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: REINFORCING (phi 0.15); KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Vancouver wins YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: Broad expression KXNHLGAME-26OCT04VGKVAN-VAN|yes selected over broad KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no because adjusted EV is 1.4 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: REINFORCING (phi 0.18); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: DUPLICATIVE (phi 0.633); KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi 0.117); failure: VGK wins (incl. OT/SO)
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT04VGKVAN-VGK3|no; why: higher confidence-adjusted growth (10.51 vs 7.93 bp); relationships: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: REINFORCING (phi 0.15); KXNHLGAME-26OCT04VGKVAN-VAN|yes: DUPLICATIVE (phi 0.633); KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi 0.116); failure: VGK wins by 2+
- **Tomas Hertl: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes; why: KXNHLSPREAD-26OCT04VGKVAN-VAN3|yes has the higher standalone adjusted growth (15.60 vs 6.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.091); relationships: KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGAME-26OCT04VGKVAN-VAN|yes: MOSTLY_INDEPENDENT (phi 0.117); KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: MOSTLY_INDEPENDENT (phi 0.116); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3419): highest fidelity KXNHLTEAMTOTAL-26OCT04VGKVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2214): highest fidelity KXNHLGAME-26OCT04VGKVAN-VGK|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT04VGKVAN-VGK|no (same contract)
- thesis VAN:WINS (p 0.4356): highest fidelity KXNHLGAME-26OCT04VGKVAN-VGK|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT04VGKVAN-VGK|no (same contract)
- KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4363, phi -0.247)
- KXNHLGAME-26OCT04VGKVAN-VAN|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.1 pts; opposing: failure thesis VGK:WINS (p 0.5644, phi -1.0)
- KXNHLSPREAD-26OCT04VGKVAN-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.3 pts; opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3418, phi -1.0)
- KXNHLGOAL-26OCT04VGKVAN-VGKTHERTL48-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4399, phi -0.206)
- override: Broad expression KXNHLGAME-26OCT04VGKVAN-VAN|yes selected over broad KXNHLTEAMTOTAL-26OCT04VGKVAN-VGK5|no because adjusted EV is 1.4 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +14.15 (adj +3.17) on $50.00, P(profit) 0.6025, adj growth 24.3 bp · B EV +8.92 (adj +4.00) on $43.62, P(profit) 0.5002, adj growth 34.7 bp · C EV +8.57 (adj +3.81) on $25.79, P(profit) 0.3475, adj growth 32.9 bp · R EV +2.05 (adj +0.63) on $10.00, P(profit) 0.6021, adj growth 21.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT04VGKVAN-VGK|no == KXNHLGAME-26OCT04VGKVAN-VAN|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
