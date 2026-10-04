# Thesis-card postmortem — RESEARCH_ONLY

evaluated 2026-10-04T20:07:01Z · thesis-postmortem-2.0 · rows (all generations) 3887

All P/L below is **FINAL_CARD_UNIQUE**: per game, only the decisions of the ONE latest complete pregame thesis-card snapshot. Repeated generations are in ALL_PROSPECTIVE_DECISIONS (calibration research, no P/L).

## Slate 2026-10-04: **PARTIAL — 1/5 games evaluated**

scheduled 5 · final 1 · settled 1 · events ingested 1 · thesis-evaluated 1 · final_card_complete False · postmortem_complete False

missing / pending:
- 2026020036: game not started: the snapshot shown is the latest so far, not yet final
- 2026020037: game not started: the snapshot shown is the latest so far, not yet final
- 2026020038: game not started: the snapshot shown is the latest so far, not yet final
- 2026020039: game not started: the snapshot shown is the latest so far, not yet final

> INTERIM (PARTIAL — 1/5 games evaluated): covers evaluated games only; NOT the slate's final ROI

invariant final_card_n 4 <= sum(game card caps) 4: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 4 | 29.33 | -14.65 | -0.499 |
| FUNDED research stakes | 1 | 4.00 | +0.61 | 0.152 |

- THESIS: 3 distinct theses, hit rate 0.000 vs mean p 0.389 (Brier 0.154)
- EXPRESSION: thesis right + won 0 · right + lost 0 · wrong + won 1 · wrong + lost 3
  - by fidelity: DIRECT 1/2; FRAGILE 0/2
  - broad vs player: FRAGILE_PLAYER 1/4 (P/L -14.65)
- PRICE: mean CLV -0.0000 (n 4), mean adjusted EV at entry 0.0161
- MODEL: Brier raw 0.1711 · adjusted 0.1659 · Kalshi mid 0.1513 (n 4)
- PORTFOLIO: funded 1 · shadow on card 3 · mean |phi| among card pairs 0.009 · mean largest thesis share 0.783
- GOVERNANCE: funded player props 1 · shadow player props 3 · large-disagreement gates 0 · overrides 0


#### game 2026020035 WPG @ DET: EVALUATED · snapshot snap-6684bc6e2d07773e9c71 @ 2026-10-04T16:50:59Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT04WPGDET-WPGVNAMESTNIKOV7-1|no | FUNDED_RESEARCH | 4 | 12.75 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | 0.0150 | 1.93 |
| KXNHLGOAL-26OCT04WPGDET-DETJCOMPHER37-1|yes | SHADOW_ONLY | 0 | 3.59 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.59 |
| KXNHLGOAL-26OCT04WPGDET-WPGMBARRON36-1|yes | SHADOW_ONLY | 0 | 2.77 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.77 |
| KXNHLGOAL-26OCT04WPGDET-WPGCPERFETTI91-1|no | SHADOW_ONLY | 0 | 10.22 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0050 | -10.22 |

#### game 2026020036 UTA @ NYR: NOT_STARTED · snapshot snap-45b308b6faa9b2133300 @ 2026-10-04T19:25:58Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT04UTANYR-UTAVTROCHECK16-1|no | SHADOW_ONLY | 0 | 15.42 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT04UTANYR-UTAJMCBAIN22-1|yes | FUNDED_RESEARCH | 1 | 3.30 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT04UTANYR-UTALCROUSE67-1|yes | SHADOW_ONLY | 0 | 3.66 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT04UTANYR-NYRPDOROFEYEV16-1|no | SHADOW_ONLY | 0 | 13.31 | - | - | - | DIRECT | - | - |

#### game 2026020037 FLA @ ANA: NOT_STARTED · snapshot snap-45b308b6faa9b2133300 @ 2026-10-04T19:25:58Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT04FLAANA-FLASREINHART13-1|no | FUNDED_RESEARCH | 4 | 14.52 | - | - | - | DIRECT | - | - |
| KXNHLSPREAD-26OCT04FLAANA-FLA3|no | FUNDED_RESEARCH | 4 | 14.52 | - | - | - | STRUCTURAL | - | - |
| KXNHLGOAL-26OCT04FLAANA-ANAAGREER18-1|yes | SHADOW_ONLY | 0 | 5.61 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT04FLAANA-FLAELUOSTARINEN27-1|yes | SHADOW_ONLY | 0 | 3.91 | - | - | - | FRAGILE | - | - |

#### game 2026020038 CGY @ SEA: NOT_STARTED · snapshot snap-45b308b6faa9b2133300 @ 2026-10-04T19:25:58Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT04CGYSEA-SEARWINTERTON26-1|yes | SHADOW_ONLY | 0 | 4.25 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT04CGYSEA-SEABMONTOUR62-1|no | FUNDED_RESEARCH | 4 | 15.42 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT04CGYSEA-CGYZPAREKH19-1|no | SHADOW_ONLY | 0 | 15.42 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT04CGYSEA-SEASWRIGHT51-1|yes | SHADOW_ONLY | 0 | 2.83 | - | - | - | FRAGILE | - | - |

#### game 2026020039 VGK @ VAN: NOT_STARTED · snapshot snap-45b308b6faa9b2133300 @ 2026-10-04T19:25:58Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT04VGKVAN-VANDOCONNOR18-1|yes | SHADOW_ONLY | 0 | 8.44 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT04VGKVAN-VANMROSSI23-1|yes | SHADOW_ONLY | 0 | 9.58 | - | - | - | FRAGILE | - | - |
| KXNHLSPREAD-26OCT04VGKVAN-VGK2|no | FUNDED_RESEARCH | 2 | 5.76 | - | - | - | STRUCTURAL | - | - |
| KXNHLGOAL-26OCT04VGKVAN-VGKJEICHEL9-1|no | FUNDED_RESEARCH | 4 | 14.07 | - | - | - | DIRECT | - | - |

## Slate 2026-10-03: **COMPLETE — 13/13 games evaluated**

scheduled 13 · final 13 · settled 13 · events ingested 13 · thesis-evaluated 13 · final_card_complete True · postmortem_complete True

invariant final_card_n 47 <= sum(game card caps) 52: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 47 | 292.80 | +22.06 | 0.075 |
| FUNDED research stakes | 14 | 35.00 | +11.06 | 0.316 |

- THESIS: 37 distinct theses, hit rate 0.351 vs mean p 0.399 (Brier 0.195)
- EXPRESSION: thesis right + won 10 · right + lost 8 · wrong + won 6 · wrong + lost 23
  - by fidelity: DIRECT 11/19; FRAGILE 3/24; STRUCTURAL 2/4
  - broad vs player: BROAD 2/4 (P/L -5.84); FRAGILE_PLAYER 14/43 (P/L +27.90)
- PRICE: mean CLV -0.0055 (n 47), mean adjusted EV at entry 0.0301
- MODEL: Brier raw 0.1666 · adjusted 0.1507 · Kalshi mid 0.1440 (n 47)
- PORTFOLIO: funded 14 · shadow on card 33 · mean |phi| among card pairs 0.055 · mean largest thesis share 0.519
- GOVERNANCE: funded player props 10 · shadow player props 33 · large-disagreement gates 10 · overrides 3

  - override: Player prop expression KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
  - override: Player prop expression KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no selected over player prop KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.81 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
  - override: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.73 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

#### game 2026020022 CHI @ BUF: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes | SHADOW_ONLY | 0 | 2.11 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.11 |
| KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no | FUNDED_RESEARCH | 2 | 5.46 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | 0.0100 | -5.46 |
| KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no | SHADOW_ONLY | 0 | 5.35 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0150 | 3.06 |

#### game 2026020023 OTT @ TOR: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes | SHADOW_ONLY | 0 | 1.82 | True | False | THESIS_WRONG_EXPRESSION_WON | FRAGILE | -0.0050 | 17.19 |
| KXNHLGOAL-26OCT03OTTTOR-TORTBLUEGER73-1|yes | SHADOW_ONLY | 0 | 1.48 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.48 |
| KXNHLGOAL-26OCT03OTTTOR-TORAMATTHEWS34-1|no | FUNDED_RESEARCH | 2 | 4.27 | False | True | THESIS_RIGHT_EXPRESSION_LOST | DIRECT | -0.0050 | -4.27 |
| KXNHLAST-26OCT03OTTTOR-OTTWEKLUND27-1|no | SHADOW_ONLY | 0 | 4.99 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0100 | 2.39 |

#### game 2026020024 WSH @ TBL: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no | SHADOW_ONLY | 0 | 5.48 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0100 | -5.48 |
| KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no | SHADOW_ONLY | 0 | 1.64 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | 0.0000 | -1.64 |
| KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes | SHADOW_ONLY | 0 | 2.08 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0150 | -2.08 |

#### game 2026020025 CAR @ PHI: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes | FUNDED_RESEARCH | 1 | 3.50 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.50 |
| KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes | SHADOW_ONLY | 0 | 2.18 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.18 |
| KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes | SHADOW_ONLY | 0 | 1.69 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.69 |
| KXNHLGOAL-26OCT03CARPHI-CARWCARRIER28-1|yes | SHADOW_ONLY | 0 | 1.16 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.16 |

#### game 2026020026 MTL @ PIT: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes | SHADOW_ONLY | 0 | 3.49 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.49 |
| KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes | SHADOW_ONLY | 0 | 3.08 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.08 |
| KXNHLGOAL-26OCT03MTLPIT-PITRRAKELL67-1|yes | FUNDED_RESEARCH | 2 | 4.20 | False | True | THESIS_RIGHT_EXPRESSION_LOST | DIRECT | -0.0050 | -4.20 |

#### game 2026020027 UTA @ CBJ: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no | SHADOW_ONLY | 0 | 5.48 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 2.63 |
| KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes | SHADOW_ONLY | 0 | 3.29 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.29 |
| KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes | SHADOW_ONLY | 0 | 1.65 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.65 |
| KXNHLGOAL-26OCT03UTACBJ-UTALCROUSE67-1|yes | SHADOW_ONLY | 0 | 1.50 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.50 |

#### game 2026020028 SEA @ EDM: EVALUATED · snapshot snap-30aee5e28411a1a4c47a @ 2026-10-03T22:14:41Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes | SHADOW_ONLY | 0 | 3.14 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.14 |
| KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no | SHADOW_ONLY | 0 | 3.98 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0050 | -3.98 |
| KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes | SHADOW_ONLY | 0 | 1.54 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.54 |
| KXNHLGOAL-26OCT03SEAEDM-SEAFGAUDREAU89-1|yes | SHADOW_ONLY | 0 | 1.26 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.26 |

#### game 2026020029 NJD @ NYI: EVALUATED · snapshot snap-4b299c3be3c6698c8e59 @ 2026-10-03T23:05:13Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03NJNYI-NJJHUGHES86-1|no | FUNDED_RESEARCH | 3 | 9.35 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | 0.0000 | 5.12 |
| KXNHLGAME-26OCT03NJNYI-NJ|no | FUNDED_RESEARCH | 2 | 6.81 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 8.08 |
| KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no | SHADOW_ONLY | 0 | 10.37 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0100 | 4.34 |

#### game 2026020030 DAL @ NSH: EVALUATED · snapshot snap-0ddf9d9d83cebba4932c @ 2026-10-03T23:55:12Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03DALNSH-DALMRANTANEN96-1|no | FUNDED_RESEARCH | 4 | 12.61 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 5.28 |
| KXNHLSPREAD-26OCT03DALNSH-DAL3|no | FUNDED_RESEARCH | 3 | 9.99 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 2.47 |
| KXNHLGOAL-26OCT03DALNSH-NSHMBOURQUE22-1|yes | SHADOW_ONLY | 0 | 2.59 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.59 |
| KXNHLGOAL-26OCT03DALNSH-DALJROBERTSON21-1|no | SHADOW_ONLY | 0 | 3.73 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0100 | 2.13 |

#### game 2026020031 BOS @ MIN: EVALUATED · snapshot snap-0ddf9d9d83cebba4932c @ 2026-10-03T23:55:12Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes | FUNDED_RESEARCH | 1 | 3.73 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.73 |
| KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes | SHADOW_ONLY | 0 | 2.20 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0200 | -2.20 |
| KXNHLAST-26OCT03BOSMIN-BOSJPETERKA10-1|no | SHADOW_ONLY | 0 | 12.61 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0100 | 4.80 |
| KXNHLAST-26OCT03BOSMIN-MINMSHABANOV49-1|no | SHADOW_ONLY | 0 | 11.76 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0050 | -11.76 |

#### game 2026020032 STL @ COL: EVALUATED · snapshot snap-c3fc29dbbc1a23a87cd4 @ 2026-10-04T00:43:16Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGAME-26OCT03STLCOL-COL|no | FUNDED_RESEARCH | 3 | 8.97 | False | False | THESIS_WRONG_EXPRESSION_LOST | STRUCTURAL | -0.0050 | -8.97 |
| KXNHLGOAL-26OCT03STLCOL-STLJSNUGGERUD21-1|yes | FUNDED_RESEARCH | 2 | 4.81 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -4.81 |
| KXNHLSPREAD-26OCT03STLCOL-COL3|no | FUNDED_RESEARCH | 2 | 7.42 | False | False | THESIS_WRONG_EXPRESSION_LOST | STRUCTURAL | -0.0050 | -7.42 |
| KXNHLAST-26OCT03STLCOL-STLCMCMICHAEL77-1|no | SHADOW_ONLY | 0 | 20.00 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 5.25 |

#### game 2026020033 CGY @ VAN: EVALUATED · snapshot snap-0ca2d3a28e9345d3b80f @ 2026-10-04T01:31:15Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no | FUNDED_RESEARCH | 5 | 20.00 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | 0.0050 | 3.55 |
| KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes | SHADOW_ONLY | 0 | 10.05 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -10.05 |
| KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes | SHADOW_ONLY | 0 | 6.04 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -6.04 |
| KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes | SHADOW_ONLY | 0 | 3.95 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 15.72 |

#### game 2026020034 LAK @ SJS: EVALUATED · snapshot snap-0ca2d3a28e9345d3b80f @ 2026-10-04T01:31:15Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no | SHADOW_ONLY | 0 | 19.68 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0050 | -19.68 |
| KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes | FUNDED_RESEARCH | 3 | 10.63 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 66.45 |
| KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no | SHADOW_ONLY | 0 | 19.68 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 9.03 |

## Slate 2026-10-02: **COMPLETE — 5/5 games evaluated**

scheduled 5 · final 5 · settled 5 · events ingested 5 · thesis-evaluated 5 · final_card_complete True · postmortem_complete True

invariant final_card_n 20 <= sum(game card caps) 20: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 20 | 182.70 | +133.09 | 0.729 |
| FUNDED research stakes | 6 | 17.00 | +0.19 | 0.011 |

- THESIS: 13 distinct theses, hit rate 0.538 vs mean p 0.399 (Brier 0.293)
- EXPRESSION: thesis right + won 7 · right + lost 6 · wrong + won 3 · wrong + lost 4
  - by fidelity: DIRECT 5/7; FRAGILE 4/12; STRUCTURAL 1/1
  - broad vs player: BROAD 1/1 (P/L +9.69); FRAGILE_PLAYER 9/19 (P/L +123.40)
- PRICE: mean CLV -0.0055 (n 20), mean adjusted EV at entry 0.0248
- MODEL: Brier raw 0.1756 · adjusted 0.1828 · Kalshi mid 0.1983 (n 20)
- PORTFOLIO: funded 6 · shadow on card 14 · mean |phi| among card pairs 0.040 · mean largest thesis share 0.599
- GOVERNANCE: funded player props 5 · shadow player props 14 · large-disagreement gates 4 · overrides 1

  - override: Player prop expression KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes selected over player prop KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.50 vs 0.25 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

#### game 2026020017 NYR @ DET: EVALUATED · snapshot snap-1f536c999460c1ae8aca @ 2026-10-02T21:40:36Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes | SHADOW_ONLY | 0 | 5.35 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -5.35 |
| KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no | FUNDED_RESEARCH | 4 | 14.53 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 2.97 |
| KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes | SHADOW_ONLY | 0 | 2.65 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.65 |
| KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no | SHADOW_ONLY | 0 | 10.73 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 3.89 |

#### game 2026020018 WSH @ CAR: EVALUATED · snapshot snap-f36fcf4ff7fc968f8611 @ 2026-10-02T22:31:35Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes | FUNDED_RESEARCH | 2 | 7.49 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | 0.0050 | -7.49 |
| KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes | SHADOW_ONLY | 0 | 8.52 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -8.52 |
| KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no | SHADOW_ONLY | 0 | 20.00 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 6.21 |
| KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes | SHADOW_ONLY | 0 | 4.55 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0150 | -4.55 |

#### game 2026020019 BOS @ WPG: EVALUATED · snapshot snap-d894c0f94f16bf8871db @ 2026-10-02T23:22:37Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes | SHADOW_ONLY | 0 | 8.25 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -8.25 |
| KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes | SHADOW_ONLY | 0 | 8.21 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 34.93 |
| KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no | SHADOW_ONLY | 0 | 20.00 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0100 | 7.98 |
| KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes | FUNDED_RESEARCH | 2 | 5.00 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | 0.0050 | -5.00 |

#### game 2026020020 STL @ DAL: EVALUATED · snapshot snap-00c8bda1cdf35f5d39cf @ 2026-10-03T00:15:35Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes | SHADOW_ONLY | 0 | 6.75 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 51.01 |
| KXNHLGAME-26OCT02STLDAL-DAL|no | FUNDED_RESEARCH | 2 | 6.10 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 9.69 |
| KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no | FUNDED_RESEARCH | 5 | 20.00 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0150 | 8.77 |
| KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes | SHADOW_ONLY | 0 | 6.92 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -6.92 |

#### game 2026020021 ANA @ VGK: EVALUATED · snapshot snap-a8b6fcd26851526e1617 @ 2026-10-03T01:56:36Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes | FUNDED_RESEARCH | 2 | 6.20 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -6.20 |
| KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes | SHADOW_ONLY | 0 | 8.04 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 34.20 |
| KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes | SHADOW_ONLY | 0 | 6.77 | False | True | THESIS_RIGHT_EXPRESSION_LOST | DIRECT | -0.0100 | -6.77 |
| KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes | SHADOW_ONLY | 0 | 6.64 | True | False | THESIS_WRONG_EXPRESSION_WON | FRAGILE | -0.0050 | 35.14 |

## Slate 2026-10-01: **COMPLETE — 8/8 games evaluated**

scheduled 8 · final 8 · settled 8 · events ingested 8 · thesis-evaluated 8 · final_card_complete True · postmortem_complete True

invariant final_card_n 30 <= sum(game card caps) 32: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 30 | 253.01 | -11.32 | -0.045 |
| FUNDED research stakes | - | - | - | no research layer on these decisions (logged before nhl-card-1.1) |

- THESIS: 23 distinct theses, hit rate 0.391 vs mean p 0.400 (Brier 0.204)
- EXPRESSION: thesis right + won 7 · right + lost 4 · wrong + won 7 · wrong + lost 12
  - by fidelity: DIRECT 8/11; FRAGILE 2/15; STRUCTURAL 4/4
  - broad vs player: BROAD 4/4 (P/L +15.99); FRAGILE_PLAYER 10/26 (P/L -27.31)
- PRICE: mean CLV -0.0062 (n 30), mean adjusted EV at entry 0.0236
- MODEL: Brier raw 0.1302 · adjusted 0.1237 · Kalshi mid 0.1249 (n 30)
- PORTFOLIO: funded 0 · shadow on card 0 · mean |phi| among card pairs 0.063 · mean largest thesis share 0.491
- GOVERNANCE: funded player props 0 · shadow player props 0 · large-disagreement gates 0 · overrides 0


#### game 2026020009 PHI @ NJD: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.33 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0100 | -2.33 |
| KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.25 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.25 |
| KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.81 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.81 |
| KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 1.92 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.92 |

#### game 2026020010 TBL @ NYR: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | LEGACY_NO_RESEARCH_LAYER | - | 9.14 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 6.97 |
| KXNHLSPREAD-26OCT01TBNYR-TB3|no | LEGACY_NO_RESEARCH_LAYER | - | 9.14 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 2.54 |
| KXNHLSPREAD-26OCT01TBNYR-TB2|no | LEGACY_NO_RESEARCH_LAYER | - | 3.28 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 1.57 |

#### game 2026020011 BUF @ CBJ: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 4.65 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -4.65 |
| KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | LEGACY_NO_RESEARCH_LAYER | - | 8.98 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 1.83 |
| KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 4.78 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0150 | 2.97 |
| KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 4.43 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 2.22 |

#### game 2026020012 MIN @ NSH: EVALUATED · snapshot snap-0471fa40e0e6b13c7166 @ 2026-10-01T23:47:02Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 4.30 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -4.30 |
| KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no | LEGACY_NO_RESEARCH_LAYER | - | 13.84 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 1.27 |
| KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.58 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.58 |
| KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.29 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0100 | -3.29 |

#### game 2026020013 CHI @ UTA: EVALUATED · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 7.01 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -7.01 |
| KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 6.56 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0100 | -6.56 |
| KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.55 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0100 | -18.55 |
| KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 5.44 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 16.08 |

#### game 2026020014 SEA @ CGY: EVALUATED · snapshot snap-7c5f74c436d5f9a561e6 @ 2026-10-02T00:37:04Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no | LEGACY_NO_RESEARCH_LAYER | - | 15.33 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 2.92 |
| KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.90 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 32.79 |
| KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.17 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.17 |
| KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 15.33 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 2.32 |

#### game 2026020015 EDM @ VAN: EVALUATED · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no | LEGACY_NO_RESEARCH_LAYER | - | 8.55 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0050 | -8.55 |
| KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 8.07 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -8.07 |
| KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no | LEGACY_NO_RESEARCH_LAYER | - | 19.64 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0150 | -19.64 |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3|no | LEGACY_NO_RESEARCH_LAYER | - | 13.74 | True | False | THESIS_WRONG_EXPRESSION_WON | STRUCTURAL | -0.0050 | 6.02 |

#### game 2026020016 FLA @ SJS: EVALUATED · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 10.14 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -10.14 |
| KXNHLSPREAD-26OCT01FLASJ-FLA3|no | LEGACY_NO_RESEARCH_LAYER | - | 19.93 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 5.86 |
| KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no | LEGACY_NO_RESEARCH_LAYER | - | 19.93 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0000 | 9.14 |

## ALL_PROSPECTIVE_DECISIONS (calibration research; no P/L)

3887 scored rows = 500 unique logical wagers (repeat factor 7.77). every scored pregame decision of every generation (repeated observations of one wager are NOT independent; no P/L here).

| family | rows | unique | Brier all rows | Brier last obs | adjusted | Kalshi mid |
|---|---:|---:|---:|---:|---:|---:|
| first_goal | 2 | 2 | 0.0012 | 0.0012 | 0.0010 | 0.0009 |
| game_spread | 577 | 42 | 0.1520 | 0.1466 | 0.1532 | 0.1638 |
| game_total | 8 | 4 | 0.1985 | 0.1576 | 0.1506 | 0.1455 |
| game_winner | 211 | 26 | 0.2259 | 0.2281 | 0.2429 | 0.2614 |
| goalie_saves | 6 | 2 | 0.1655 | 0.1579 | 0.1946 | 0.2304 |
| period_spread | 1 | 1 | 0.6434 | 0.6434 | 0.5365 | 0.4830 |
| player_assists | 921 | 126 | 0.1902 | 0.1795 | 0.1721 | 0.1724 |
| player_goals | 1634 | 223 | 0.1420 | 0.1407 | 0.1399 | 0.1388 |
| player_points | 120 | 25 | 0.2437 | 0.1984 | 0.1792 | 0.1860 |
| team_total | 407 | 49 | 0.2067 | 0.2112 | 0.2174 | 0.2262 |

_Prospective thesis-card evidence. All P/L is FINAL_CARD_UNIQUE (one latest complete pregame snapshot per game). THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO / GOVERNANCE are kept separate: a right thesis expressed through a contract that lost is not a wrong prediction. A handful of games proves nothing; never tune to one slate._
