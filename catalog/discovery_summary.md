# Kalshi NHL discovery summary

- discovered_at: `2026-11-11T23:51:24Z`  ontology: `2026.09.29.2`  requests: 159
- series enumerated: 16226; NHL series: 78; markets scanned: 3395

## Support states (coverage invariant)

| support | markets |
|---|---:|
| MODELABLE | 545 |
| BUILDABLE | 17 |
| RESEARCH | 2492 |
| UNMODELABLE | 286 |
| UNRESOLVED | 55 |

## NHL series

| series | family | support | fee | unopened | open | closed | settled | strike_types | parse |
|---|---|---|---|---:|---:|---:|---:|---|---|
| KXCANADACUP | season_champion | RESEARCH | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXCONNSMYTHE | season_awards | UNMODELABLE | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXESPYNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNBANHL | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNEXTTEAMNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHL1P | period_winner | RESEARCH | quadratic/1 | 0 | 51 | 0 | 0 | structured | {'high': 51} |
| KXNHL1PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL1PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 34 | 0 | 0 | greater | {'high': 34} |
| KXNHL1PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 51 | 0 | 0 | greater | {'high': 51} |
| KXNHL1STTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2OT | game_multi_overtime | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2P | period_winner | RESEARCH | quadratic/1 | 0 | 51 | 0 | 0 | structured | {'high': 51} |
| KXNHL2PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 34 | 0 | 0 | greater | {'high': 34} |
| KXNHL2PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 51 | 0 | 0 | greater | {'high': 51} |
| KXNHL30COMEBACK | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3P | period_winner | RESEARCH | quadratic/1 | 0 | 51 | 0 | 0 | structured | {'high': 51} |
| KXNHL3PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 34 | 0 | 0 | greater | {'high': 34} |
| KXNHL3PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 51 | 0 | 0 | greater | {'high': 51} |
| KXNHL4NATIONS | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLADAMS | season_awards | UNMODELABLE | quadratic/1 | 0 | 32 | 0 | 0 | custom | {'low': 32} |
| KXNHLANYGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLAST | player_assists | RESEARCH | quadratic/1 | 0 | 205 | 0 | 0 | greater | {'high': 205} |
| KXNHLATLANTIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLCALDER | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured,custom | {'low': 40} |
| KXNHLCENTRAL | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLDRAFTPICK | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLDRAFTTOP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLEAST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLEXPANSION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXNHLF10G | game_early_goal | RESEARCH | quadratic/1 | 0 | 17 | 0 | 0 | greater_or_equal | {'high': 17} |
| KXNHLFINALSEXACT | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLFIRSTGOAL | first_goal | RESEARCH | quadratic/1 | 0 | 215 | 0 | 0 | structured | {'high': 215} |
| KXNHLGAME | game_winner | MODELABLE | quadratic_with_maker_fees/1 | 0 | 102 | 0 | 0 | structured | {'high': 102} |
| KXNHLGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 370 | 0 | 0 | greater | {'high': 370} |
| KXNHLHART | season_awards | UNMODELABLE | quadratic/1 | 0 | 39 | 0 | 0 | structured | {'low': 39} |
| KXNHLLINDSAY | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 38 | 0 | 0 | structured | {'low': 38} |
| KXNHLMENTION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLMETROPOLITAN | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLMVP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTGM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNORRIS | season_awards | UNMODELABLE | quadratic/1 | 0 | 35 | 0 | 0 | structured | {'low': 35} |
| KXNHLOT | game_overtime | BUILDABLE | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'high': 17} |
| KXNHLOVERTIME | game_overtime | BUILDABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPACIFIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLPLAYOFF | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPLAYOFFGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPRES | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPRICE | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPSEASONGOALS | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'low': 17} |
| KXNHLPTS | player_points | RESEARCH | quadratic/1 | 0 | 285 | 0 | 0 | greater | {'high': 285} |
| KXNHLRECORDWORST | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLRETIRE | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLRICHARD | season_awards | UNMODELABLE | quadratic/1 | 0 | 44 | 0 | 0 | structured | {'low': 44} |
| KXNHLROSS | season_awards | UNMODELABLE | quadratic/1 | 0 | 47 | 0 | 0 | structured | {'low': 47} |
| KXNHLSAVE | goalie_saves | RESEARCH | quadratic/1 | 0 | 14 | 0 | 0 | greater | {'high': 14} |
| KXNHLSAVES | goalie_saves | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSEASONGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 87 | 0 | 0 | greater,structured | {'low': 87} |
| KXNHLSEASONPPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 90 | 0 | 0 | greater | {'low': 90} |
| KXNHLSEASONPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 320 | 0 | 0 | greater_or_equal | {'low': 320} |
| KXNHLSERIES | playoff_series | RESEARCH | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESGAMES | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESOT | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSCORE | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSPREAD | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOAL | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOALS | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSPREAD | game_spread | MODELABLE | quadratic/1 | 0 | 84 | 0 | 0 | greater | {'high': 84} |
| KXNHLTEAMTOTAL | team_total | MODELABLE | quadratic/1 | 0 | 170 | 0 | 0 | greater | {'high': 170} |
| KXNHLTOTAL | game_total | MODELABLE | quadratic/1 | 0 | 189 | 0 | 0 | greater | {'high': 189} |
| KXNHLVEZINA | season_awards | UNMODELABLE | quadratic/1 | 0 | 48 | 0 | 0 | structured | {'low': 48} |
| KXNHLWEST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLWINS | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLWSTREAK | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXTEAMSINSC | season_champion | RESEARCH | quadratic/1 | 0 | 256 | 0 | 0 | custom | {'low': 256} |

## Title templates per series

### KXCANADACUP — Canada winning Stanley Cup
- (1) Will a Canadian team win the NAME® by the end of the # season?
- samples: KXCANADACUP-30
- sample fields: `{"ticker": "KXCANADACUP-30", "event_ticker": "KXCANADACUP-30", "market_type": "binary", "title": "Will a Canadian team win the Stanley Cup\u00ae by the end of the 2030 season?", "subtitle": "Before 2031", "yes_sub_title": "Before 2031", "no_sub_title": "Before 2031", "status": "active", "open_time": "2025-06-13T14:00:00Z", "close_time": "2030-06-30T03:59:00Z", "expected_expiration_time": "2030-06-30T14:00:00Z", "result": "", "rules_primary": "If a Canadian hockey team wins the Stanley Cup\u00ae after Issuance and before Jun 30, 2030, then the market resolves to Yes."}`

### KXCONNSMYTHE — Conn Smythe trophy

### KXESPYNHL — BEST NHL PLAYER‬

### KXNBANHL — NBA + NHL Champion Combo

### KXNEXTTEAMNHL — Next Team NHL

### KXNHL — Stanley Cup
- (30) NAME win the #-# NAME® Finals?
- (1) NAME. NAME win the #-# NAME® Finals?
- (1) Will Montréal Canadiens win the #-# NAME® Finals?
- samples: KXNHL-27-WSH, KXNHL-27-WPG, KXNHL-27-VGK, KXNHL-27-VAN, KXNHL-27-UTA, KXNHL-27-TOR
- sample fields: `{"ticker": "KXNHL-27-WSH", "event_ticker": "KXNHL-27", "market_type": "binary", "title": "Will Washington Capitals win the 2026-27 Stanley Cup\u00ae Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-06-15T03:40:00Z", "close_time": "2029-06-30T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals wins the 2026-27 Stanley Cup\u00ae Finals, then the marke`

### KXNHL1P — NHL 1st Period Winner
- (17) #st period tie
- (5) NAME wins the #st period
- (2) Utah wins the #st period
- (2) Buffalo wins the #st period
- (1) NAME I wins the #st period
- (1) St. Louis wins the #st period
- (1) Chicago wins the #st period
- (1) Winnipeg wins the #st period
- samples: KXNHL1P-26NOV12NYILA-TIE, KXNHL1P-26NOV12NYILA-NYI, KXNHL1P-26NOV12NYILA-LA, KXNHL1P-26NOV12STLUTA-UTA, KXNHL1P-26NOV12STLUTA-TIE, KXNHL1P-26NOV12STLUTA-STL
- sample fields: `{"ticker": "KXNHL1P-26NOV12NYILA-TIE", "event_ticker": "KXNHL1P-26NOV12NYILA", "market_type": "binary", "title": "1st period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If neither team wins the 1st period of the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 2026, then the market resolve`

### KXNHL1PBTTS — NHL Both Teams to Score in 1st Period

### KXNHL1PSPREAD — 1st Period Spread
- (5) NAME wins #st Period by over # goals
- (2) Utah wins #st Period by over # goals
- (2) Buffalo wins #st Period by over # goals
- (1) NAME I wins #st Period by over # goals
- (1) St. Louis wins #st Period by over # goals
- (1) Chicago wins #st Period by over # goals
- (1) Winnipeg wins #st Period by over # goals
- (1) Dallas wins #st Period by over # goals
- samples: KXNHL1PSPREAD-26NOV12NYILA-NYI2, KXNHL1PSPREAD-26NOV12NYILA-LA2, KXNHL1PSPREAD-26NOV12STLUTA-UTA2, KXNHL1PSPREAD-26NOV12STLUTA-STL2, KXNHL1PSPREAD-26NOV12BUFCHI-CHI2, KXNHL1PSPREAD-26NOV12BUFCHI-BUF2
- sample fields: `{"ticker": "KXNHL1PSPREAD-26NOV12NYILA-NYI2", "event_ticker": "KXNHL1PSPREAD-26NOV12NYILA", "market_type": "binary", "title": "New York I wins 1st Period by over 1.5 goals", "yes_sub_title": "New York I wins by over 1.5 goals", "no_sub_title": "New York I wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "03f52887-5bb7-4b51-954e-433f73474350"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If New York I wins `

### KXNHL1PTOTAL — NHL 1st Period Total
- (51) #st Period: Over # goals scored
- samples: KXNHL1PTOTAL-26NOV12NYILA-3, KXNHL1PTOTAL-26NOV12NYILA-2, KXNHL1PTOTAL-26NOV12NYILA-1, KXNHL1PTOTAL-26NOV12STLUTA-3, KXNHL1PTOTAL-26NOV12STLUTA-2, KXNHL1PTOTAL-26NOV12STLUTA-1
- sample fields: `{"ticker": "KXNHL1PTOTAL-26NOV12NYILA-3", "event_ticker": "KXNHL1PTOTAL-26NOV12NYILA", "market_type": "binary", "title": "1st Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 1st Period of the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 20`

### KXNHL1STTEAM — All NHL First Team

### KXNHL2OT — NHL Double Overtime

### KXNHL2P — NHL 2nd Period Winner
- (17) #nd period tie
- (5) NAME wins the #nd period
- (2) Utah wins the #nd period
- (2) Buffalo wins the #nd period
- (1) NAME I wins the #nd period
- (1) St. Louis wins the #nd period
- (1) Chicago wins the #nd period
- (1) Winnipeg wins the #nd period
- samples: KXNHL2P-26NOV12NYILA-TIE, KXNHL2P-26NOV12NYILA-NYI, KXNHL2P-26NOV12NYILA-LA, KXNHL2P-26NOV12STLUTA-UTA, KXNHL2P-26NOV12STLUTA-TIE, KXNHL2P-26NOV12STLUTA-STL
- sample fields: `{"ticker": "KXNHL2P-26NOV12NYILA-TIE", "event_ticker": "KXNHL2P-26NOV12NYILA", "market_type": "binary", "title": "2nd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If neither team wins the 2nd period of the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 2026, then the market resolve`

### KXNHL2PBTTS — NHL Both Teams to Score in 2nd Period

### KXNHL2PSPREAD — 2nd Period Spread
- (5) NAME wins #nd Period by over # goals
- (2) Utah wins #nd Period by over # goals
- (2) Buffalo wins #nd Period by over # goals
- (1) NAME I wins #nd Period by over # goals
- (1) St. Louis wins #nd Period by over # goals
- (1) Chicago wins #nd Period by over # goals
- (1) Winnipeg wins #nd Period by over # goals
- (1) Dallas wins #nd Period by over # goals
- samples: KXNHL2PSPREAD-26NOV12NYILA-NYI2, KXNHL2PSPREAD-26NOV12NYILA-LA2, KXNHL2PSPREAD-26NOV12STLUTA-UTA2, KXNHL2PSPREAD-26NOV12STLUTA-STL2, KXNHL2PSPREAD-26NOV12BUFCHI-CHI2, KXNHL2PSPREAD-26NOV12BUFCHI-BUF2
- sample fields: `{"ticker": "KXNHL2PSPREAD-26NOV12NYILA-NYI2", "event_ticker": "KXNHL2PSPREAD-26NOV12NYILA", "market_type": "binary", "title": "New York I wins 2nd Period by over 1.5 goals", "yes_sub_title": "New York I wins by over 1.5 goals", "no_sub_title": "New York I wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "03f52887-5bb7-4b51-954e-433f73474350"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If New York I wins `

### KXNHL2PTOTAL — 2nd Period Total
- (51) #nd Period: Over # goals scored
- samples: KXNHL2PTOTAL-26NOV12NYILA-3, KXNHL2PTOTAL-26NOV12NYILA-2, KXNHL2PTOTAL-26NOV12NYILA-1, KXNHL2PTOTAL-26NOV12STLUTA-3, KXNHL2PTOTAL-26NOV12STLUTA-2, KXNHL2PTOTAL-26NOV12STLUTA-1
- sample fields: `{"ticker": "KXNHL2PTOTAL-26NOV12NYILA-3", "event_ticker": "KXNHL2PTOTAL-26NOV12NYILA", "market_type": "binary", "title": "2nd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 2nd Period of the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 20`

### KXNHL30COMEBACK — NHL 3-0 Series Comeback

### KXNHL3P — NHL 3rd Period Winner
- (17) #rd period tie
- (5) NAME wins the #rd period
- (2) Utah wins the #rd period
- (2) Buffalo wins the #rd period
- (1) NAME I wins the #rd period
- (1) St. Louis wins the #rd period
- (1) Chicago wins the #rd period
- (1) Winnipeg wins the #rd period
- samples: KXNHL3P-26NOV12NYILA-TIE, KXNHL3P-26NOV12NYILA-NYI, KXNHL3P-26NOV12NYILA-LA, KXNHL3P-26NOV12STLUTA-UTA, KXNHL3P-26NOV12STLUTA-TIE, KXNHL3P-26NOV12STLUTA-STL
- sample fields: `{"ticker": "KXNHL3P-26NOV12NYILA-TIE", "event_ticker": "KXNHL3P-26NOV12NYILA", "market_type": "binary", "title": "3rd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If neither team wins the 3rd period (excluding overtime) of the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 2026, th`

### KXNHL3PBTTS — NHL Both Teams to Score in 3rd Period

### KXNHL3PSPREAD — NHL 3rd Period Spread
- (5) NAME wins #rd Period by over # goals
- (2) Utah wins #rd Period by over # goals
- (2) Buffalo wins #rd Period by over # goals
- (1) NAME I wins #rd Period by over # goals
- (1) St. Louis wins #rd Period by over # goals
- (1) Chicago wins #rd Period by over # goals
- (1) Winnipeg wins #rd Period by over # goals
- (1) Dallas wins #rd Period by over # goals
- samples: KXNHL3PSPREAD-26NOV12NYILA-NYI2, KXNHL3PSPREAD-26NOV12NYILA-LA2, KXNHL3PSPREAD-26NOV12STLUTA-UTA2, KXNHL3PSPREAD-26NOV12STLUTA-STL2, KXNHL3PSPREAD-26NOV12BUFCHI-CHI2, KXNHL3PSPREAD-26NOV12BUFCHI-BUF2
- sample fields: `{"ticker": "KXNHL3PSPREAD-26NOV12NYILA-NYI2", "event_ticker": "KXNHL3PSPREAD-26NOV12NYILA", "market_type": "binary", "title": "New York I wins 3rd Period by over 1.5 goals", "yes_sub_title": "New York I wins by over 1.5 goals", "no_sub_title": "New York I wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "03f52887-5bb7-4b51-954e-433f73474350"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If New York I wins `

### KXNHL3PTOTAL — 3rd Period Total
- (51) #rd Period: Over # goals scored
- samples: KXNHL3PTOTAL-26NOV12NYILA-3, KXNHL3PTOTAL-26NOV12NYILA-2, KXNHL3PTOTAL-26NOV12NYILA-1, KXNHL3PTOTAL-26NOV12STLUTA-3, KXNHL3PTOTAL-26NOV12STLUTA-2, KXNHL3PTOTAL-26NOV12STLUTA-1
- sample fields: `{"ticker": "KXNHL3PTOTAL-26NOV12NYILA-3", "event_ticker": "KXNHL3PTOTAL-26NOV12NYILA", "market_type": "binary", "title": "3rd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 3rd Period of the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 20`

### KXNHL4NATIONS — 4 nations face off

### KXNHLADAMS — NHL Jack Adams Award
- (29) NAME: NAME wins
- (1) NAME: Todd McLellan wins
- (1) NAME: Peter DeBoer wins
- (1) NAME: NAME. Louis wins
- samples: KXNHLADAMS-27-TMCL, KXNHLADAMS-27-TGRE, KXNHLADAMS-27-SKEE, KXNHLADAMS-27-SCAR, KXNHLADAMS-27-SARN, KXNHLADAMS-27-RWAR
- sample fields: `{"ticker": "KXNHLADAMS-27-TMCL", "event_ticker": "KXNHLADAMS-27", "market_type": "binary", "title": "Jack Adams Award: Todd McLellan wins", "subtitle": "::", "yes_sub_title": "Todd McLellan", "no_sub_title": "Todd McLellan", "strike_type": "custom", "custom_strike": {"Person": "Todd McLellan"}, "status": "active", "open_time": "2026-09-28T22:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Todd McLellan wins the NHL Jack Adams Award in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLANYGOAL — Pro Hockey Goalscorer

### KXNHLAST — Pro Hockey Assists
- (188) NAME: #+ assists
- (3) Jackson LaCombe: #+ assists
- (3) Connor McDavid: #+ assists
- (2) Ryan McLeod: #+ assists
- (2) Ryan O'Reilly: #+ assists
- (2) J.T. Miller: #+ assists
- (2) NAME D'Astous: #+ assists
- (1) Jack McBain: #+ assists
- samples: KXNHLAST-26NOV11NYRCGY-NYRMPETTERSSON26-1, KXNHLAST-26NOV11NYRCGY-CGYZWHITECLOUD28-1, KXNHLAST-26NOV11NYRCGY-CGYYSHARANGOVICH17-1, KXNHLAST-26NOV11NYRCGY-CGYMPOSPISIL76-1, KXNHLAST-26NOV11NYRCGY-CGYASUNIEV61-1, KXNHLAST-26NOV11NSHANA-NSHSWRIGHT51-1
- sample fields: `{"ticker": "KXNHLAST-26NOV11NYRCGY-NYRMPETTERSSON26-1", "event_ticker": "KXNHLAST-26NOV11NYRCGY", "market_type": "binary", "title": "Marcus Pettersson: 1+ assists", "yes_sub_title": "Marcus Pettersson: 1+", "no_sub_title": "Marcus Pettersson: 1+", "strike_type": "greater", "floor_strike": 0.5, "custom_strike": {"hockey_player": "cc5eb619-4a9a-47f7-8833-2ade58a3bea8", "hockey_team": "9979553a-3962-4169-b2c3-510ba6d931d2"}, "status": "active", "open_time": "2026-11-11T22:37:00Z", "close_time": "2026-11-14T00:30:00Z", "expected_expiration_time": "2026-11-12T06:30:00Z", "result": "", "rules_primar`

### KXNHLATLANTIC — NHL Atlantic Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLATLANTIC-27-TOR, KXNHLATLANTIC-27-TB, KXNHLATLANTIC-27-OTT, KXNHLATLANTIC-27-MTL, KXNHLATLANTIC-27-FLA, KXNHLATLANTIC-27-DET
- sample fields: `{"ticker": "KXNHLATLANTIC-27-TOR", "event_ticker": "KXNHLATLANTIC-27", "market_type": "binary", "title": "Will the Toronto Maple Leafs win the Atlantic Division?", "yes_sub_title": "Toronto Maple Leafs", "no_sub_title": "Toronto Maple Leafs", "strike_type": "structured", "custom_strike": {"hockey_team": "f61f9daa-407b-4c46-96e8-feee19cd6f51"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Toronto Maple Leafs win the 2026-27 NHL Atlantic Division, then the `

### KXNHLCALDER — NHL Calder Memorial Trophy
- (36) NAME: NAME wins
- (1) NAME: Viggo Björck wins
- (1) NAME: NAME-Nygård wins
- (1) NAME: Gavin McKenna wins
- (1) NAME: Adam Engström wins
- samples: KXNHLCALDER-27-ZBUIUM24, KXNHLCALDER-27-VEKLUND, KXNHLCALDER-27-VBJORCK, KXNHLCALDER-27-TLINDSTEIN, KXNHLCALDER-27-TIGINLA, KXNHLCALDER-27-TCONNELLY
- sample fields: `{"ticker": "KXNHLCALDER-27-ZBUIUM24", "event_ticker": "KXNHLCALDER-27", "market_type": "binary", "title": "Calder Memorial Trophy: Zeev Buium wins", "subtitle": "::", "yes_sub_title": "Zeev Buium", "no_sub_title": "Zeev Buium", "strike_type": "structured", "custom_strike": {"hockey_player": "4e4ad45c-1cda-4e0b-89c3-4e6c27740027"}, "status": "active", "open_time": "2026-09-30T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zeev Buium wins the NHL Calder Memorial Trophy in the 2026-27 NHL season, then the ma`

### KXNHLCENTRAL — NHL Central Division Winner
- (7) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLCENTRAL-27-WPG, KXNHLCENTRAL-27-UTA, KXNHLCENTRAL-27-STL, KXNHLCENTRAL-27-NSH, KXNHLCENTRAL-27-MIN, KXNHLCENTRAL-27-DAL
- sample fields: `{"ticker": "KXNHLCENTRAL-27-WPG", "event_ticker": "KXNHLCENTRAL-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Central Division?", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Central Division, then the market resolves to Yes."}`

### KXNHLDRAFTPICK — Pro Hockey Draft Pick

### KXNHLDRAFTTOP — Pro Hockey Top Pick

### KXNHLEAST — Eastern Conference Championship
- (16) Will the NAME win the NAME?
- samples: KXNHLEAST-27-WSH, KXNHLEAST-27-TOR, KXNHLEAST-27-TB, KXNHLEAST-27-PIT, KXNHLEAST-27-PHI, KXNHLEAST-27-OTT
- sample fields: `{"ticker": "KXNHLEAST-27-WSH", "event_ticker": "KXNHLEAST-27", "market_type": "binary", "title": "Will the Washington Capitals win the Eastern Conference Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Eastern Conference Finals, t`

### KXNHLEXPANSION — NHL Expansion
- (1) NAME receive an NHL expansion team before #?
- samples: KXNHLEXPANSION-27JAN01HOU-Y
- sample fields: `{"ticker": "KXNHLEXPANSION-27JAN01HOU-Y", "event_ticker": "KXNHLEXPANSION-27JAN01HOU", "market_type": "binary", "title": "Will Houston receive an NHL expansion team before 2027?", "yes_sub_title": "Houston to get an expansion team before 2027", "no_sub_title": "Houston to get an expansion team before 2027", "status": "active", "open_time": "2026-09-01T01:00:00Z", "close_time": "2027-01-01T04:59:00Z", "expected_expiration_time": "2027-01-01T15:00:00Z", "result": "", "rules_primary": "If the NHL officially announces the award of an expansion team franchise to Houston before Jan 1, 2027, then the`

### KXNHLF10G — NHL Goal in First 10 Minutes
- (17) Either team to score in the first # minutes
- samples: KXNHLF10G-26NOV12NYILA-Y, KXNHLF10G-26NOV12STLUTA-Y, KXNHLF10G-26NOV12BUFCHI-Y, KXNHLF10G-26NOV12WPGDAL-Y, KXNHLF10G-26NOV12DETFLA-Y, KXNHLF10G-26NOV12COLOTT-Y
- sample fields: `{"ticker": "KXNHLF10G-26NOV12NYILA-Y", "event_ticker": "KXNHLF10G-26NOV12NYILA", "market_type": "binary", "title": "Either team to score in the first 10 minutes", "yes_sub_title": "Goal in first 10 min", "no_sub_title": "Goal in first 10 min", "strike_type": "greater_or_equal", "floor_strike": 1, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If at least 1 goal is scored by either New York I or Los Angeles during the first 10 minutes of the first period (from 0:00`

### KXNHLFINALSEXACT — NHL Championship Series Score

### KXNHLFIRSTGOAL — NHL First Goal
- (200) NAME: NAME
- (1) Rutger McGroarty: NAME
- (1) Ryan O'Reilly: NAME
- (1) Roger McQueen: NAME
- (1) Jackson LaCombe: NAME
- (1) Brayden McNabb: NAME
- (1) Nick DeSimone: NAME
- (1) MacKenzie Weegar: NAME
- samples: KXNHLFIRSTGOAL-26NOV11PITSJ-SJSDICKINSON6, KXNHLFIRSTGOAL-26NOV11PITSJ-SJMKESSELRING7, KXNHLFIRSTGOAL-26NOV11PITSJ-SJJTROUBA65, KXNHLFIRSTGOAL-26NOV11PITSJ-SJDORLOV9, KXNHLFIRSTGOAL-26NOV11PITSJ-SJDNURSE25, KXNHLFIRSTGOAL-26NOV11NSHANA-NSHSWRIGHT51
- sample fields: `{"ticker": "KXNHLFIRSTGOAL-26NOV11PITSJ-SJSDICKINSON6", "event_ticker": "KXNHLFIRSTGOAL-26NOV11PITSJ", "market_type": "binary", "title": "Sam Dickinson: First Goalscorer", "yes_sub_title": "Sam Dickinson", "no_sub_title": "Sam Dickinson", "strike_type": "structured", "custom_strike": {"hockey_player": "2899afb9-e319-4ae2-bea2-9bdf6deaa709", "hockey_team": "eb4bc183-5966-40eb-8bdb-3dd922ad1752"}, "status": "active", "open_time": "2026-11-11T21:52:00Z", "close_time": "2026-11-14T03:00:00Z", "expected_expiration_time": "2026-11-12T09:00:00Z", "result": "", "rules_primary": "If Sam Dickinson score`

### KXNHLGAME — NHL Game
- (13) NAME wins
- (4) Calgary wins
- (4) Vegas wins
- (4) Dallas wins
- (4) Nashville wins
- (4) Anaheim wins
- (4) Philadelphia wins
- (4) Buffalo wins
- samples: KXNHLGAME-26NOV17CGYSJ-SJ, KXNHLGAME-26NOV17CGYSJ-CGY, KXNHLGAME-26NOV17DALVGK-VGK, KXNHLGAME-26NOV17DALVGK-DAL, KXNHLGAME-26NOV17NSHMIN-NSH, KXNHLGAME-26NOV17NSHMIN-MIN
- sample fields: `{"ticker": "KXNHLGAME-26NOV17CGYSJ-SJ", "event_ticker": "KXNHLGAME-26NOV17CGYSJ", "market_type": "binary", "title": "San Jose wins", "yes_sub_title": "San Jose", "no_sub_title": "San Jose", "strike_type": "structured", "custom_strike": {"hockey_team": "eb4bc183-5966-40eb-8bdb-3dd922ad1752"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-20T03:00:00Z", "expected_expiration_time": "2026-11-18T06:00:00Z", "result": "", "rules_primary": "If San Jose wins the Calgary vs San Jose NHL game originally scheduled for Nov 17, 2026, then the market resolves to Yes."}`

### KXNHLGOAL — NHL Goalscorer
- (343) NAME: #+ goals
- (3) Ryan O'Reilly: #+ goals
- (3) Connor McDavid: #+ goals
- (2) Rutger McGroarty: #+ goals
- (2) Roger McQueen: #+ goals
- (2) Jackson LaCombe: #+ goals
- (2) MacKenzie Weegar: #+ goals
- (2) Jack McBain: #+ goals
- samples: KXNHLGOAL-26NOV11NSHANA-NSHSWRIGHT51-2, KXNHLGOAL-26NOV11NSHANA-NSHSWRIGHT51-1, KXNHLGOAL-26NOV11NSHANA-NSHDHUNT48-1, KXNHLGOAL-26NOV11NSHANA-ANASCOLANGELO12-2, KXNHLGOAL-26NOV11NSHANA-ANASCOLANGELO12-1, KXNHLGOAL-26NOV11PITSJ-SJZOSTAPCHUK63-1
- sample fields: `{"ticker": "KXNHLGOAL-26NOV11NSHANA-NSHSWRIGHT51-2", "event_ticker": "KXNHLGOAL-26NOV11NSHANA", "market_type": "binary", "title": "Shane Wright: 2+ goals", "yes_sub_title": "Shane Wright: 2+", "no_sub_title": "Shane Wright: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "12706eeb-fdb7-42b4-95ff-a280c658304b", "hockey_team": "fcfd0b58-cc0a-448e-8f4b-6ddeab8f339f"}, "status": "active", "open_time": "2026-11-11T19:52:00Z", "close_time": "2026-11-14T03:00:00Z", "expected_expiration_time": "2026-11-12T09:00:00Z", "result": "", "rules_primary": "If Shane Wrigh`

### KXNHLHART — NHL Hart Memorial Trophy
- (28) Who will win NAME?
- (10) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- samples: KXNHLHART-27-TSTUTZLE18, KXNHLHART-27-SAHO20, KXNHLHART-27-CKELLER9, KXNHLHART-27-MNECAS88, KXNHLHART-27-LCARLSSON91, KXNHLHART-27-JLACOMBE2
- sample fields: `{"ticker": "KXNHLHART-27-TSTUTZLE18", "event_ticker": "KXNHLHART-27", "market_type": "binary", "title": "Hart Memorial Trophy: Tim Stutzle wins", "yes_sub_title": "Tim Stutzle", "no_sub_title": "Tim Stutzle", "strike_type": "structured", "custom_strike": {"hockey_player": "6df1e248-2084-4229-aa7d-9d6beb8f6b57"}, "status": "active", "open_time": "2026-11-11T16:00:00Z", "close_time": "2027-06-30T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Tim Stutzle wins the NHL Hart Memorial Trophy in the 2026-27 NHL season, then the market resolves to Yes`

### KXNHLLINDSAY — NHL Ted Lindsay Winner
- (35) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLLINDSAY-27-TSTUTZLE18, KXNHLLINDSAY-27-SAHO20, KXNHLLINDSAY-27-CKELLER9, KXNHLLINDSAY-27-MNECAS88, KXNHLLINDSAY-27-LCARLSSON91, KXNHLLINDSAY-27-JLACOMBE2
- sample fields: `{"ticker": "KXNHLLINDSAY-27-TSTUTZLE18", "event_ticker": "KXNHLLINDSAY-27", "market_type": "binary", "title": "Ted Lindsay Award: Tim Stutzle wins", "yes_sub_title": "Tim Stutzle", "no_sub_title": "Tim Stutzle", "strike_type": "structured", "custom_strike": {"hockey_player": "6df1e248-2084-4229-aa7d-9d6beb8f6b57"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Tim Stutzle wins the NHL Ted Lindsay Award in the 2026-27 NHL season, then the market resolves to Yes`

### KXNHLMENTION — NHL Announcer Mentions

### KXNHLMETROPOLITAN — NHL Metropolitan Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLMETROPOLITAN-27-WSH, KXNHLMETROPOLITAN-27-PIT, KXNHLMETROPOLITAN-27-PHI, KXNHLMETROPOLITAN-27-NYR, KXNHLMETROPOLITAN-27-NYI, KXNHLMETROPOLITAN-27-NJ
- sample fields: `{"ticker": "KXNHLMETROPOLITAN-27-WSH", "event_ticker": "KXNHLMETROPOLITAN-27", "market_type": "binary", "title": "Will the Washington Capitals win the Metropolitan Division?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Metropolitan Div`

### KXNHLMVP — NHL Hart Memorial Trophy Winner

### KXNHLNEXTGM — Next NHL GM

### KXNHLNEXTTEAM — NHL Next Team

### KXNHLNORRIS — NHL James Norris Memorial Trophy
- (33) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Charlie McAvoy wins
- samples: KXNHLNORRIS-27-SGOSTISBEHERE4, KXNHLNORRIS-27-SJONES3, KXNHLNORRIS-27-MSEIDER53, KXNHLNORRIS-27-JCHYCHRUN6, KXNHLNORRIS-27-DRADDYSH43, KXNHLNORRIS-27-ZWERENSKI8
- sample fields: `{"ticker": "KXNHLNORRIS-27-SGOSTISBEHERE4", "event_ticker": "KXNHLNORRIS-27", "market_type": "binary", "title": "James Norris Memorial Trophy: Shayne Gostisbehere wins", "yes_sub_title": "Shayne Gostisbehere", "no_sub_title": "Shayne Gostisbehere", "strike_type": "structured", "custom_strike": {"hockey_player": "c07b1390-6d72-4439-8337-a892678d90d5"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Shayne Gostisbehere wins the NHL James Norris Memorial Trophy in`

### KXNHLOT — NHL Overtime
- (17) Game goes to overtime
- samples: KXNHLOT-26NOV12NYILA-1, KXNHLOT-26NOV12STLUTA-1, KXNHLOT-26NOV12BUFCHI-1, KXNHLOT-26NOV12WPGDAL-1, KXNHLOT-26NOV12DETFLA-1, KXNHLOT-26NOV12COLOTT-1
- sample fields: `{"ticker": "KXNHLOT-26NOV12NYILA-1", "event_ticker": "KXNHLOT-26NOV12NYILA", "market_type": "binary", "title": "Game goes to overtime", "yes_sub_title": "Game goes to overtime", "no_sub_title": "Game goes to overtime", "strike_type": "greater", "floor_strike": 0.5, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If at least 1 overtime period is played in the New York I vs Los Angeles NHL game originally scheduled for Nov 12, 2026, then the market resolves to Yes."}`

### KXNHLOVERTIME — NHL Overtime

### KXNHLPACIFIC — NHL Pacific Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLPACIFIC-27-VGK, KXNHLPACIFIC-27-VAN, KXNHLPACIFIC-27-SJ, KXNHLPACIFIC-27-SEA, KXNHLPACIFIC-27-LA, KXNHLPACIFIC-27-EDM
- sample fields: `{"ticker": "KXNHLPACIFIC-27-VGK", "event_ticker": "KXNHLPACIFIC-27", "market_type": "binary", "title": "Will the Vegas Golden Knights win the Pacific Division?", "yes_sub_title": "Vegas Golden Knights", "no_sub_title": "Vegas Golden Knights", "strike_type": "structured", "custom_strike": {"hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Vegas Golden Knights win the 2026-27 NHL Pacific Division, then the `

### KXNHLPLAYOFF — Playoff Qualifier
- (30) Will the NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the St. NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the Montréal Canadiens qualify for the playoffs in the #-# NHL season?
- samples: KXNHLPLAYOFF-27-WSH, KXNHLPLAYOFF-27-WPG, KXNHLPLAYOFF-27-VGK, KXNHLPLAYOFF-27-VAN, KXNHLPLAYOFF-27-UTA, KXNHLPLAYOFF-27-TOR
- sample fields: `{"ticker": "KXNHLPLAYOFF-27-WSH", "event_ticker": "KXNHLPLAYOFF-27", "market_type": "binary", "title": "Will the Washington Capitals qualify for the playoffs in the 2026-27 NHL season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals qualify for the playoffs `

### KXNHLPLAYOFFGOALS — NHL Playoffs Goal Leader (by Round)

### KXNHLPRES — NHL President's Trophy Winner
- (30) Will the NAME win the Presidents' Trophy?
- (1) Will the St. NAME win the Presidents' Trophy?
- (1) Will the Montréal Canadiens win the Presidents' Trophy?
- samples: KXNHLPRES-27-WSH, KXNHLPRES-27-WPG, KXNHLPRES-27-VGK, KXNHLPRES-27-VAN, KXNHLPRES-27-UTA, KXNHLPRES-27-TOR
- sample fields: `{"ticker": "KXNHLPRES-27-WSH", "event_ticker": "KXNHLPRES-27", "market_type": "binary", "title": "Will the Washington Capitals win the Presidents' Trophy?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-14T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Presidents' Trophy, then the market`

### KXNHLPRICE — NHL Ticket Prices

### KXNHLPSEASONGOALS — Player Goals Scored in Season
- (17) NAME: #+ goals in #-# NHL regular season?
- samples: KXNHLPSEASONGOALS-27MCELEBRINI71-60, KXNHLPSEASONGOALS-27MCELEBRINI71-55, KXNHLPSEASONGOALS-27MCELEBRINI71-50, KXNHLPSEASONGOALS-27MCELEBRINI71-45, KXNHLPSEASONGOALS-27MCELEBRINI71-40, KXNHLPSEASONGOALS-27MCELEBRINI71-35
- sample fields: `{"ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71-60", "event_ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71", "market_type": "binary", "title": "Macklin Celebrini: 60+ goals in 2026-27 NHL regular season?", "subtitle": "Macklin Celebrini", "yes_sub_title": "60+ goals", "no_sub_title": "60+ goals", "strike_type": "greater", "floor_strike": 59.5, "custom_strike": {"hockey_player": "264560c4-3624-4c01-924e-879a08799f16"}, "status": "active", "open_time": "2026-10-09T01:30:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Mac`

### KXNHLPTS — Pro Hockey Points
- (262) NAME: #+ points
- (5) Connor McDavid: #+ points
- (3) Ryan O'Reilly: #+ points
- (3) Jackson LaCombe: #+ points
- (3) J.T. Miller: #+ points
- (2) Jack McBain: #+ points
- (2) Ryan McLeod: #+ points
- (2) MacKenzie Weegar: #+ points
- samples: KXNHLPTS-26NOV11NYRCGY-NYRMPETTERSSON26-1, KXNHLPTS-26NOV11NYRCGY-CGYZWHITECLOUD28-1, KXNHLPTS-26NOV11NYRCGY-CGYYSHARANGOVICH17-2, KXNHLPTS-26NOV11NYRCGY-CGYYSHARANGOVICH17-1, KXNHLPTS-26NOV11NYRCGY-CGYMPOSPISIL76-2, KXNHLPTS-26NOV11NYRCGY-CGYMPOSPISIL76-1
- sample fields: `{"ticker": "KXNHLPTS-26NOV11NYRCGY-NYRMPETTERSSON26-1", "event_ticker": "KXNHLPTS-26NOV11NYRCGY", "market_type": "binary", "title": "Marcus Pettersson: 1+ points", "yes_sub_title": "Marcus Pettersson: 1+", "no_sub_title": "Marcus Pettersson: 1+", "strike_type": "greater", "floor_strike": 0.5, "custom_strike": {"hockey_player": "cc5eb619-4a9a-47f7-8833-2ade58a3bea8", "hockey_team": "9979553a-3962-4169-b2c3-510ba6d931d2"}, "status": "active", "open_time": "2026-11-11T22:37:00Z", "close_time": "2026-11-14T00:30:00Z", "expected_expiration_time": "2026-11-12T06:30:00Z", "result": "", "rules_primary`

### KXNHLRECORDWORST — Worst NHL Record
- (30) Will the NAME have the worst regular season record in the #-# season?
- (1) Will the St. NAME have the worst regular season record in the #-# season?
- (1) Will the Montréal Canadiens have the worst regular season record in the #-# season?
- samples: KXNHLRECORDWORST-27-WSH, KXNHLRECORDWORST-27-WPG, KXNHLRECORDWORST-27-VGK, KXNHLRECORDWORST-27-VAN, KXNHLRECORDWORST-27-UTA, KXNHLRECORDWORST-27-TOR
- sample fields: `{"ticker": "KXNHLRECORDWORST-27-WSH", "event_ticker": "KXNHLRECORDWORST-27", "market_type": "binary", "title": "Will the Washington Capitals have the worst regular season record in the 2026-27 season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-29T16:00:00Z", "close_time": "2027-05-31T14:00:00Z", "expected_expiration_time": "2027-05-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals have the `

### KXNHLRETIRE — NHL Retire

### KXNHLRICHARD — NHL Maurice "Rocket" Richard Trophy
- (41) Maurice "Rocket" NAME: NAME wins
- (1) Maurice "Rocket" NAME: Nathan MacKinnon wins
- (1) Maurice "Rocket" NAME: Connor McDavid wins
- (1) Maurice "Rocket" NAME: Alex DeBrincat wins
- samples: KXNHLRICHARD-27-MMICHKOV39, KXNHLRICHARD-27-LSTANKOVEN22, KXNHLRICHARD-27-ATUCH89, KXNHLRICHARD-27-CGAUTHIER61, KXNHLRICHARD-27-ZHYMAN18, KXNHLRICHARD-27-WNYLANDER88
- sample fields: `{"ticker": "KXNHLRICHARD-27-MMICHKOV39", "event_ticker": "KXNHLRICHARD-27", "market_type": "binary", "title": "Maurice \"Rocket\" Richard Trophy: Matvei Michkov wins", "yes_sub_title": "Matvei Michkov", "no_sub_title": "Matvei Michkov", "strike_type": "structured", "custom_strike": {"hockey_player": "3b72da3e-53e9-4436-8cf2-195612050ff6"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Matvei Michkov wins the NHL Maurice \"Rocket\" Richard Award in the 2026-27 `

### KXNHLROSS — NHL Art Ross Trophy
- (44) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLROSS-27-MNECAS88, KXNHLROSS-27-LCARLSSON91, KXNHLROSS-27-JLACOMBE2, KXNHLROSS-27-BSENNECKE45, KXNHLROSS-27-AFOX23, KXNHLROSS-27-CGAUTHIER61
- sample fields: `{"ticker": "KXNHLROSS-27-MNECAS88", "event_ticker": "KXNHLROSS-27", "market_type": "binary", "title": "Art Ross Trophy: Martin Necas wins", "yes_sub_title": "Martin Necas", "no_sub_title": "Martin Necas", "strike_type": "structured", "custom_strike": {"hockey_player": "f27d857e-40f4-4ef2-8b89-8f545335f410"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Martin Necas wins the NHL Art Ross Trophy in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLSAVE — Goaltender Saves
- (14) NAME: #+ saves
- samples: KXNHLSAVE-26NOV11PITSJ-SJYASKAROV30-26, KXNHLSAVE-26NOV11PITSJ-PITSMURASHOV1-25, KXNHLSAVE-26NOV11UTAVGK-UTASCOSSA33-25, KXNHLSAVE-26NOV11UTAVGK-VGKCHART79-24, KXNHLSAVE-26NOV11NSHANA-NSHJANNUNEN29-28, KXNHLSAVE-26NOV11NSHANA-ANALBROSSOIT31-23
- sample fields: `{"ticker": "KXNHLSAVE-26NOV11PITSJ-SJYASKAROV30-26", "event_ticker": "KXNHLSAVE-26NOV11PITSJ", "market_type": "binary", "title": "Yaroslav Askarov: 26+ saves", "yes_sub_title": "Yaroslav Askarov: 26+", "no_sub_title": "Yaroslav Askarov: 26+", "strike_type": "greater", "floor_strike": 25.5, "custom_strike": {"hockey_player": "d9975a58-bdda-4de9-9933-549069713e00", "hockey_team": "eb4bc183-5966-40eb-8bdb-3dd922ad1752"}, "status": "active", "open_time": "2026-11-11T21:50:00Z", "close_time": "2026-11-14T03:00:00Z", "expected_expiration_time": "2026-11-12T06:00:00Z", "result": "", "rules_primary": `

### KXNHLSAVES — Pro Hockey Saves

### KXNHLSEASONGOALS — Player to score X Goals in Season
- (81) NAME: #+ goals in #-# NHL regular season?
- (2) Nathan MacKinnon: #+ goals in #-# NHL regular season?
- (2) Connor McDavid: #+ goals in #-# NHL regular season?
- (2) Alex DeBrincat: #+ goals in #-# NHL regular season?
- samples: KXNHLSEASONGOALS-27C40-BTKACHUK8, KXNHLSEASONGOALS-27C20-WSMITH2, KXNHLSEASONGOALS-27C20-SCROSBY87, KXNHLSEASONGOALS-27C20-PKANE88, KXNHLSEASONGOALS-27C20-MSCHAEFER48, KXNHLSEASONGOALS-27C20-FNAZAR91
- sample fields: `{"ticker": "KXNHLSEASONGOALS-27C40-BTKACHUK8", "event_ticker": "KXNHLSEASONGOALS-27C40", "market_type": "binary", "title": "Brady Tkachuk: 40+ goals in 2026-27 NHL regular season?", "subtitle": "Brady Tkachuk:: FLA Panthers", "yes_sub_title": "Brady Tkachuk", "no_sub_title": "Brady Tkachuk", "strike_type": "greater", "floor_strike": 39.5, "custom_strike": {"hockey_player": "3d7e2b4d-d4a8-4fe2-904f-fbfb0773ed66"}, "status": "active", "open_time": "2026-10-14T16:35:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If B`

### KXNHLSEASONPPTS — Season Player Points
- (84) NAME: #+ points in #-# NHL regular season?
- (3) Nathan MacKinnon: #+ points in #-# NHL regular season?
- (3) Connor McDavid: #+ points in #-# NHL regular season?
- samples: KXNHLSEASONPPTS-27C110-ZWERENSKI8, KXNHLSEASONPPTS-27C110-WNYLANDER88, KXNHLSEASONPPTS-27C110-WJOHNSTON53, KXNHLSEASONPPTS-27C110-TSTUTZLE18, KXNHLSEASONPPTS-27C110-SCROSBY87, KXNHLSEASONPPTS-27C110-NSUZUKI14
- sample fields: `{"ticker": "KXNHLSEASONPPTS-27C110-ZWERENSKI8", "event_ticker": "KXNHLSEASONPPTS-27C110", "market_type": "binary", "title": "Zach Werenski: 110+ points in 2026-27 NHL regular season?", "subtitle": "Zach Werenski:: Columbus Blue Jackets", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "greater", "floor_strike": 109.5, "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_pr`

### KXNHLSEASONPTS — NHL Season Point Totals
- (10) Will the WSH Capitals NHL team earn at least # points in the #-# regular season?
- (10) Will the WPG Jets NHL team earn at least # points in the #-# regular season?
- (10) Will the VGK NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the VAN Canucks NHL team earn at least # points in the #-# regular season?
- (10) Will the UTA Mammoth NHL team earn at least # points in the #-# regular season?
- (10) Will the TOR NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the TB Lightning NHL team earn at least # points in the #-# regular season?
- (10) Will the STL Blues NHL team earn at least # points in the #-# regular season?
- samples: KXNHLSEASONPTS-27WSH-95, KXNHLSEASONPTS-27WSH-90, KXNHLSEASONPTS-27WSH-85, KXNHLSEASONPTS-27WSH-80, KXNHLSEASONPTS-27WSH-75, KXNHLSEASONPTS-27WSH-70
- sample fields: `{"ticker": "KXNHLSEASONPTS-27WSH-95", "event_ticker": "KXNHLSEASONPTS-27WSH", "market_type": "binary", "title": "Will the WSH Capitals NHL team earn at least 95 points in the 2026-27 regular season?", "yes_sub_title": "95+ points", "no_sub_title": "95+ points", "strike_type": "greater_or_equal", "floor_strike": 95, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:47:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-18T14:00:00Z", "result": "", "rules_primary": "If the WSH Capitals earn at le`

### KXNHLSERIES — NHL Series Winner

### KXNHLSERIESGAMES — NHL Series Total Games

### KXNHLSERIESOT — NHL Series Overtime

### KXNHLSERIESSCORE — NHL Series Exact Score

### KXNHLSERIESSPREAD — NHL Series Game Spread

### KXNHLSERIESTOTALGOAL — NHL Series Total Goals

### KXNHLSERIESTOTALGOALS — NHL Series Total Goals

### KXNHLSPREAD — NHL Spread
- (10) NAME wins by over # goals
- (4) Winnipeg wins by over # goals
- (4) Chicago wins by over # goals
- (4) Seattle wins by over # goals
- (4) Carolina wins by over # goals
- (4) Vegas wins by over # goals
- (4) Nashville wins by over # goals
- (4) NAME R wins by over # goals
- samples: KXNHLSPREAD-26NOV14WPGCHI-WPG3, KXNHLSPREAD-26NOV14WPGCHI-WPG2, KXNHLSPREAD-26NOV14WPGCHI-CHI3, KXNHLSPREAD-26NOV14WPGCHI-CHI2, KXNHLSPREAD-26NOV14SEACAR-SEA3, KXNHLSPREAD-26NOV14SEACAR-SEA2
- sample fields: `{"ticker": "KXNHLSPREAD-26NOV14WPGCHI-WPG3", "event_ticker": "KXNHLSPREAD-26NOV14WPGCHI", "market_type": "binary", "title": "Winnipeg wins by over 2.5 goals", "yes_sub_title": "Winnipeg wins by over 2.5 goals", "no_sub_title": "Winnipeg wins by over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-11-11T23:05:00Z", "close_time": "2026-11-16T20:30:00Z", "expected_expiration_time": "2026-11-14T23:30:00Z", "result": "", "rules_primary": "If Winnipeg wins by over 2.5 goals in `

### KXNHLTEAMTOTAL — NHL Team Goals Scored During Game
- (25) NAME over # goals scored
- (10) Utah over # goals scored
- (10) Buffalo over # goals scored
- (5) NAME I over # goals scored
- (5) St. Louis over # goals scored
- (5) Chicago over # goals scored
- (5) Winnipeg over # goals scored
- (5) Dallas over # goals scored
- samples: KXNHLTEAMTOTAL-26NOV12NYILA-NYI6, KXNHLTEAMTOTAL-26NOV12NYILA-NYI5, KXNHLTEAMTOTAL-26NOV12NYILA-NYI4, KXNHLTEAMTOTAL-26NOV12NYILA-NYI3, KXNHLTEAMTOTAL-26NOV12NYILA-NYI2, KXNHLTEAMTOTAL-26NOV12NYILA-LA6
- sample fields: `{"ticker": "KXNHLTEAMTOTAL-26NOV12NYILA-NYI6", "event_ticker": "KXNHLTEAMTOTAL-26NOV12NYILA", "market_type": "binary", "title": "New York I over 5.5 goals scored", "yes_sub_title": "New York I over 5.5", "no_sub_title": "New York I over 5.5", "strike_type": "greater", "floor_strike": 5.5, "custom_strike": {"hockey_team": "03f52887-5bb7-4b51-954e-433f73474350"}, "status": "active", "open_time": "2026-11-11T05:06:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T06:00:00Z", "result": "", "rules_primary": "If New York I scores over 5.5 goals in the New York I vs `

### KXNHLTOTAL — NHL Total Goals
- (189) NAME: Over # goals scored
- samples: KXNHLTOTAL-26NOV14WPGCHI-9, KXNHLTOTAL-26NOV14WPGCHI-8, KXNHLTOTAL-26NOV14WPGCHI-7, KXNHLTOTAL-26NOV14WPGCHI-6, KXNHLTOTAL-26NOV14WPGCHI-5, KXNHLTOTAL-26NOV14WPGCHI-4
- sample fields: `{"ticker": "KXNHLTOTAL-26NOV14WPGCHI-9", "event_ticker": "KXNHLTOTAL-26NOV14WPGCHI", "market_type": "binary", "title": "Full Game: Over 8.5 goals scored", "yes_sub_title": "Over 8.5 goals scored", "no_sub_title": "Over 8.5 goals scored", "strike_type": "greater", "floor_strike": 8.5, "status": "active", "open_time": "2026-11-11T23:05:00Z", "close_time": "2026-11-16T20:30:00Z", "expected_expiration_time": "2026-11-14T23:30:00Z", "result": "", "rules_primary": "If the teams collectively score more than 8.5 goals in the Winnipeg vs Chicago NHL game originally scheduled for Nov 14, 2026, then the `

### KXNHLVEZINA — NHL Vezina Trophy
- (48) NAME: NAME wins
- samples: KXNHLVEZINA-27-CHART79, KXNHLVEZINA-27-DVLADAR80, KXNHLVEZINA-27-DLEVI27, KXNHLVEZINA-27-JFOWLER32, KXNHLVEZINA-27-JDOBES75, KXNHLVEZINA-27-JWALLSTEDT30
- sample fields: `{"ticker": "KXNHLVEZINA-27-CHART79", "event_ticker": "KXNHLVEZINA-27", "market_type": "binary", "title": "Vezina Trophy: Carter Hart wins", "yes_sub_title": "Carter Hart", "no_sub_title": "Carter Hart", "strike_type": "structured", "custom_strike": {"hockey_player": "7290548a-8894-46f2-ab77-699d8822fb63"}, "status": "active", "open_time": "2026-11-11T16:15:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Carter Hart wins the NHL Vezina Trophy in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLWEST — Western Conference Champion
- (15) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLWEST-27-WPG, KXNHLWEST-27-VGK, KXNHLWEST-27-VAN, KXNHLWEST-27-UTA, KXNHLWEST-27-STL, KXNHLWEST-27-SJ
- sample fields: `{"ticker": "KXNHLWEST-27-WPG", "event_ticker": "KXNHLWEST-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Western Conference Finals?", "subtitle": "Winnipeg Jets", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Western Conference Fina`

### KXNHLWINS — NHL wins 

### KXNHLWSTREAK — Longest NHL win streak in regular season
- (30) Will the NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the St. NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the Montréal Canadiens have the longest winning streak in the #-# NHL regular season?
- samples: KXNHLWSTREAK-27-WSH, KXNHLWSTREAK-27-WPG, KXNHLWSTREAK-27-VGK, KXNHLWSTREAK-27-VAN, KXNHLWSTREAK-27-UTA, KXNHLWSTREAK-27-TOR
- sample fields: `{"ticker": "KXNHLWSTREAK-27-WSH", "event_ticker": "KXNHLWSTREAK-27", "market_type": "binary", "title": "Will the Washington Capitals have the longest winning streak in the 2026-27 NHL regular season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals has the longes`

### KXTEAMSINSC — Teams in Stanley Cup
- (1) Will WSH Capitals vs WPG Jets be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VGK NAME be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VAN Canucks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs UTA Mammoth be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs STL Blues be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SJ Sharks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SEA Kraken be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs NSH Predators be the matchup in the #-# NAME?
- samples: KXTEAMSINSC-27-WSHWPG, KXTEAMSINSC-27-WSHVGK, KXTEAMSINSC-27-WSHVAN, KXTEAMSINSC-27-WSHUTA, KXTEAMSINSC-27-WSHSTL, KXTEAMSINSC-27-WSHSJ
- sample fields: `{"ticker": "KXTEAMSINSC-27-WSHWPG", "event_ticker": "KXTEAMSINSC-27", "market_type": "binary", "title": "Will WSH Capitals vs WPG Jets be the matchup in the 2026-27 Stanley Cup Final?", "yes_sub_title": "WSH Capitals vs WPG Jets", "no_sub_title": "WSH Capitals vs WPG Jets", "strike_type": "custom", "custom_strike": {"Matchup": "WSH Capitals vs WPG Jets"}, "status": "active", "open_time": "2026-09-11T22:00:00Z", "close_time": "2027-06-15T14:00:00Z", "expected_expiration_time": "2027-06-15T14:00:00Z", "result": "", "rules_primary": "If WSH Capitals vs WPG Jets is confirmed to be the matchup in t`

## UNRESOLVED samples

- `KXNHLLINDSAY-27-TSTUTZLE18` — Ted Lindsay Award: Tim Stutzle wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-SAHO20` — Ted Lindsay Award: Sebastian Aho wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CKELLER9` — Ted Lindsay Award: Clayton Keller wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MNECAS88` — Ted Lindsay Award: Martin Necas wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-LCARLSSON91` — Ted Lindsay Award: Leo Carlsson wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JLACOMBE2` — Ted Lindsay Award: Jackson LaCombe wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-BSENNECKE45` — Ted Lindsay Award: Beckett Sennecke wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AFOX23` — Ted Lindsay Award: Adam Fox wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CGAUTHIER61` — Ted Lindsay Award: Cutter Gauthier wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-EBOUCHARD2` — Ted Lindsay Award: Evan Bouchard wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-WNYLANDER88` — Ted Lindsay Award: William Nylander wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-SCROSBY87` — Ted Lindsay Award: Sidney Crosby wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-QHUGHES43` — Ted Lindsay Award: Quinn Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-PDOROFEYEV16` — Ted Lindsay Award: Pavel Dorofeyev wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NSUZUKI14` — Ted Lindsay Award: Nick Suzuki wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NMACKINNON29` — Ted Lindsay Award: Nathan MacKinnon wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NKUCHEROV86` — Ted Lindsay Award: Nikita Kucherov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MTKACHUK19` — Ted Lindsay Award: Matthew Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MRANTANEN96` — Ted Lindsay Award: Mikko Rantanen wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MMARNER93` — Ted Lindsay Award: Mitch Marner wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MCELEBRINI71` — Ted Lindsay Award: Macklin Celebrini wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-LDRAISAITL29` — Ted Lindsay Award: Leon Draisaitl wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KKAPRIZOV97` — Ted Lindsay Award: Kirill Kaprizov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KCONNOR81` — Ted Lindsay Award: Kyle Connor wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JHUGHES86` — Ted Lindsay Award: Jack Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JEICHEL9` — Ted Lindsay Award: Jack Eichel wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-ISHESTERKIN31` — Ted Lindsay Award: Igor Shesterkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-DPASTRNAK88` — Ted Lindsay Award: David Pastrnak wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMCDAVID97` — Ted Lindsay Award: Connor McDavid wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMAKAR8` — Ted Lindsay Award: Cale Makar wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CHELLEBUYCK37` — Ted Lindsay Award: Connor Hellebuyck wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CCAUFIELD13` — Ted Lindsay Award: Cole Caufield wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CBEDARD98` — Ted Lindsay Award: Connor Bedard wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-BTKACHUK7` — Ted Lindsay Award: Brady Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AVASILEVSKIY88` — Ted Lindsay Award: Andrei Vasilevskiy wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-APANARIN72` — Ted Lindsay Award: Artemi Panarin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AOVECHKIN8` — Ted Lindsay Award: Alex Ovechkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AMATTHEWS34` — Ted Lindsay Award: Auston Matthews wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-60` — Macklin Celebrini: 60+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-55` — Macklin Celebrini: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-50` — Macklin Celebrini: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-45` — Macklin Celebrini: 45+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-40` — Macklin Celebrini: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-35` — Macklin Celebrini: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-30` — Macklin Celebrini: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-25` — Macklin Celebrini: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-20` — Macklin Celebrini: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-55` — Alex Ovechkin: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-50` — Alex Ovechkin: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-40` — Alex Ovechkin: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-35` — Alex Ovechkin: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-30` — Alex Ovechkin: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-25` — Alex Ovechkin: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-20` — Alex Ovechkin: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-15` — Alex Ovechkin: 15+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title

## Series decisions (hockey-related)

- NHL  `KXNHLSERIESSPREAD` NHL Series Game Spread — ticker prefix KXNHL
- NHL  `KXNHLPLAYOFF` Playoff Qualifier — ticker prefix KXNHL
- NHL  `KXNHLFINALSEXACT` NHL Championship Series Score — ticker prefix KXNHL
- skip `KXWOMHOCKEYFGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLSEASONPPTS` Season Player Points — ticker prefix KXNHL
- skip `KXNCAAHOCKEY` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLVEZINA` NHL Vezina Trophy — ticker prefix KXNHL
- NHL  `KXNHLOT` NHL Overtime — ticker prefix KXNHL
- NHL  `KXNHLNEXTTEAM` NHL Next Team — ticker prefix KXNHL
- skip `KXWOMHOCKEYTOTAL` Winter Olympics Men's Hockey Goal Total — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLOVERTIME` NHL Overtime — ticker prefix KXNHL
- skip `KXNCAAH` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXESPYNHL` BEST NHL PLAYER‬ — title mentions NHL
- NHL  `KXNHL1STTEAM` All NHL First Team — ticker prefix KXNHL
- skip `KXAHL` AHL Champion — non-NHL hockey marker 'AHL'
- skip `KXWOMHOCKEYGOAL` Olympic Hockey Goalscorer — non-NHL hockey marker 'OLYMPIC'
- skip `KXDEL` DEL Champion — non-NHL hockey marker 'DEL '
- NHL  `KXNHL2OT` NHL Double Overtime — ticker prefix KXNHL
- NHL  `KXNHLFIRSTGOAL` NHL First Goal — ticker prefix KXNHL
- NHL  `KXNHLPTS` Pro Hockey Points — ticker prefix KXNHL
- skip `KXWOMHOCKEY` Winter Olympics Men's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLCALDER` NHL Calder Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLEAST` Eastern Conference Championship — ticker prefix KXNHL
- NHL  `KXNHLWEST` Western Conference Champion — ticker prefix KXNHL
- NHL  `KXNHLMVP` NHL Hart Memorial Trophy Winner — ticker prefix KXNHL
- skip `KXIIHFGAME` IIHF Game — non-NHL hockey marker 'IIHF'
- skip `KXELH` ELH Champion — no NHL marker
- NHL  `KXNHLHART` NHL Hart Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLSPREAD` NHL Spread — ticker prefix KXNHL
- NHL  `KXNHLTOTAL` NHL Total Goals — ticker prefix KXNHL
- NHL  `KXNHLDRAFTTOP` Pro Hockey Top Pick — ticker prefix KXNHL
- NHL  `KXNHL` Stanley Cup — ticker prefix KXNHL
- NHL  `KXNHL2PBTTS` NHL Both Teams to Score in 2nd Period — ticker prefix KXNHL
- NHL  `KXNHL1PBTTS` NHL Both Teams to Score in 1st Period — ticker prefix KXNHL
- NHL  `KXNHL1PSPREAD` 1st Period Spread — ticker prefix KXNHL
- NHL  `KXNHLAST` Pro Hockey Assists — ticker prefix KXNHL
- skip `KXWOHOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- skip `KXNCAAHOCKEYGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNEXTTEAMNHL` Next Team NHL — title mentions NHL
- skip `KXLIGMAGGAME` Ligue Magnus Game — no NHL marker
- skip `KXSHLGAME` SHL Game — non-NHL hockey marker 'SHL'
- NHL  `KXNHL30COMEBACK` NHL 3-0 Series Comeback — ticker prefix KXNHL
- NHL  `KXNHLROSS` NHL Art Ross Trophy — ticker prefix KXNHL
- NHL  `KXNHLLINDSAY` NHL Ted Lindsay Winner — ticker prefix KXNHL
- skip `KXINTHOCKEY` International Hockey — no NHL marker
- skip `KXWOMHOCKEYFIRSTGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLMENTION` NHL Announcer Mentions — ticker prefix KXNHL
- NHL  `KXNHLSERIESSCORE` NHL Series Exact Score — ticker prefix KXNHL
- NHL  `KXNHL3PSPREAD` NHL 3rd Period Spread — ticker prefix KXNHL
- NHL  `KXNHLRECORDWORST` Worst NHL Record — ticker prefix KXNHL
- skip `KXWOMHOCKEYSPREAD` Winter Olympics Men's Hockey Spread — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLNORRIS` NHL James Norris Memorial Trophy — ticker prefix KXNHL
- skip `KXLIIGA` Liiga Champion — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHLNEXTGM` Next NHL GM — ticker prefix KXNHL
- NHL  `KXNHLSERIES` NHL Series Winner — ticker prefix KXNHL
- NHL  `KXTEAMSINSC` Teams in Stanley Cup — NHL trophy/futures marker
- NHL  `KXNHLSERIESTOTALGOALS` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHLPRICE` NHL Ticket Prices — ticker prefix KXNHL
- NHL  `KXNHL3PBTTS` NHL Both Teams to Score in 3rd Period — ticker prefix KXNHL
- NHL  `KXNHLSEASONPTS` NHL Season Point Totals — ticker prefix KXNHL
- skip `KXLIIGAGAME` Liiga Game — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHLGAME` NHL Game — ticker prefix KXNHL
- skip `KXEARNINGSMENTIONHLT` HILTON — no NHL marker
- NHL  `KXNHLANYGOAL` Pro Hockey Goalscorer — ticker prefix KXNHL
- NHL  `KXNHLSERIESGAMES` NHL Series Total Games — ticker prefix KXNHL
- NHL  `KXNHLRICHARD` NHL Maurice "Rocket" Richard Trophy — ticker prefix KXNHL
- NHL  `KXNHLCENTRAL` NHL Central Division Winner — ticker prefix KXNHL
- skip `KXEUCHLGAME` Champions League Hockey — non-NHL hockey marker 'CHL'
- NHL  `KXNHLSAVE` Goaltender Saves — ticker prefix KXNHL
- skip `KXPHLGAME` Polish Hockey Game — no NHL marker
- NHL  `KXNHLPLAYOFFGOALS` NHL Playoffs Goal Leader (by Round) — ticker prefix KXNHL
- NHL  `KXNHL2PTOTAL` 2nd Period Total — ticker prefix KXNHL
- skip `KXKHLGAME` KHL Game — non-NHL hockey marker 'KHL'
- NHL  `KXNHLSERIESOT` NHL Series Overtime — ticker prefix KXNHL
- NHL  `KXNHLDRAFTPICK` Pro Hockey Draft Pick — ticker prefix KXNHL
- NHL  `KXNHLF10G` NHL Goal in First 10 Minutes — ticker prefix KXNHL
- NHL  `KXNHL2PSPREAD` 2nd Period Spread — ticker prefix KXNHL
- NHL  `KXNHLPRES` NHL President's Trophy Winner — ticker prefix KXNHL
- NHL  `KXNHL1P` NHL 1st Period Winner — ticker prefix KXNHL
- NHL  `KXNHL1PTOTAL` NHL 1st Period Total — ticker prefix KXNHL
- NHL  `KXNHLTEAMTOTAL` NHL Team Goals Scored During Game — ticker prefix KXNHL
- NHL  `KXNHLMETROPOLITAN` NHL Metropolitan Division Winner — ticker prefix KXNHL
- skip `KXHOBEYBAKER` Hobey Baker Award — no NHL marker
- NHL  `KXNHLEXPANSION` NHL Expansion — ticker prefix KXNHL
- NHL  `KXNHLATLANTIC` NHL Atlantic Division Winner — ticker prefix KXNHL
- NHL  `KXNHLPACIFIC` NHL Pacific Division Winner — ticker prefix KXNHL
- skip `KXNCAAHGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- skip `KXWOWHOCKEY` Winter Olympics Women's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLSERIESTOTALGOAL` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHLSEASONGOALS` Player to score X Goals in Season — ticker prefix KXNHL
- skip `KXNLGAME` National League Game — no NHL marker
- NHL  `KXNHLSAVES` Pro Hockey Saves — ticker prefix KXNHL
- NHL  `KXNBANHL` NBA + NHL Champion Combo — title mentions NHL
- skip `KXKHL` KHL Champion — non-NHL hockey marker 'KHL'
- NHL  `KXCANADACUP` Canada winning Stanley Cup — NHL trophy/futures marker
- skip `KXAHLGAME` AHL Game — non-NHL hockey marker 'AHL'
- skip `KXIIHF` Who will win IIHF championship? — non-NHL hockey marker 'IIHF'
- skip `KXWO-HOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLRETIRE` NHL Retire — ticker prefix KXNHL
- NHL  `KXNHL3PTOTAL` 3rd Period Total — ticker prefix KXNHL
- skip `KXELHGAME` ELH Game — no NHL marker
- skip `KXIIHFCHAMP` IIHF World Championship winner — non-NHL hockey marker 'IIHF'
- NHL  `KXNHLADAMS` NHL Jack Adams Award — ticker prefix KXNHL
- NHL  `KXNHL3P` NHL 3rd Period Winner — ticker prefix KXNHL
- NHL  `KXNHLGOAL` NHL Goalscorer — ticker prefix KXNHL
- skip `KXDELGAME` DEL Game — non-NHL hockey marker 'DEL '
- skip `KXNL` National League Champion — no NHL marker
- NHL  `KXCONNSMYTHE` Conn Smythe trophy — NHL trophy/futures marker
- skip `KXSHL` SHL Champion — non-NHL hockey marker 'SHL'
- skip `KXWOMHOCKEYMVP` Men's Winter Olympics Hockey MVP — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLPSEASONGOALS` Player Goals Scored in Season — ticker prefix KXNHL
- NHL  `KXNHLWSTREAK` Longest NHL win streak in regular season — ticker prefix KXNHL
- NHL  `KXNHL2P` NHL 2nd Period Winner — ticker prefix KXNHL
- NHL  `KXNHLWINS` NHL wins  — ticker prefix KXNHL
- NHL  `KXNHL4NATIONS` 4 nations face off — ticker prefix KXNHL
