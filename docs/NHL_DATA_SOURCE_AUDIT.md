# NHL data source audit

Probed from a GitHub Actions runner on 2026-09-29 (`docs/probe/probe_results.md`, `docs/probe/samples/`). The build
container itself could reach none of these hosts (organisation network policy), so every shape below was verified on
the runner.

| source | URL family | provides | depth | update | runner | auth | timestamps | failure modes | role |
|---|---|---|---|---|---|---|---|---|---|
| NHL api-web | `api-web.nhle.com/v1/schedule/{date}`, `/score/{date}`, `/gamecenter/{id}/boxscore`, `/landing`, `/play-by-play`, `/roster/{abbrev}/current`, `/standings/now` | schedule (ids, UTC starts, gameState/gameScheduleState, teams), live scores, final score + `gameOutcome.lastPeriodType` (REG/OT/SO), goalie lines with `starter`, rosters | current + past seasons by id | live | 200 | none | `startTimeUTC`; no feed timestamp, we stamp fetch time | team id changes (Utah 59 -> 68); `odds` partner prices embedded in schedule (quarantined) | PRODUCTION |
| NHL stats REST | `api.nhle.com/stats/rest/en/team/summary`, `/goalie/summary`, `/game` (cayenneExp season/gameType) | GF/GA, PP%, PK%, shots; goalie SV%, shots, starts; game list with `period` (3/4/5) and scores | all seasons | daily | 200 | none | none; fetch-stamped | new season returns empty `data` until games exist | PRODUCTION (results, goalie fallback) |
| MoneyPuck | `moneypuck.com/moneypuck/playerData/seasonSummary/{yr}/regular/{teams,goalies,skaters,lines}.csv`, `careers/gameByGame/all_teams.csv` | team xG by situation, goalie xG vs goals, team game-by-game with xG since 2008 | 2008+ | daily in season | 200 | none | none; `Last-Modified` header kept | new-season `teams.csv` 404 until games exist; `goalies.csv` empty; all_teams.csv is tens of MB | PRODUCTION (ratings), history |
| MoneyPuck shots | `peter-tanner.com/moneypuck/downloads/shots_{yr}.zip` | shot-level xG | 2007+ | daily | 200 (HEAD) | none | | `moneypuck.com/data/shots/...` 404s | RESEARCH (not ingested) |
| Kalshi public REST | `api.elections.kalshi.com/trade-api/v2` and `external-api.kalshi.com/trade-api/v2`: `/series`, `/markets`, `/events`, `/markets/{t}/orderbook`, `/exchange/status`, `/search/filters_by_sport` | NHL series, markets with dollar quotes, order books, results | settled markets queryable | live | 200 both hosts | none for reads | `updated_time`, `close_time`, `expected_expiration_time` | series listing is large (paginate 200); short tricodes | PRODUCTION |
| DailyFaceoff | `dailyfaceoff.com/starting-goalies/{date}` | starting goalies with news strength (Confirmed/Likely/Unconfirmed) and news timestamp | today/tomorrow | intraday | 200 (browser UA) | none | `NewsCreatedAt`, `dateGmt` | HTML with `__NEXT_DATA__` JSON; shape may drift (parser tolerant, raw page archived); carries sportsbook lines (stripped) | OPTIONAL enrichment (goalie status) |
| ESPN injuries | `site.api.espn.com/apis/site/v2/sports/hockey/nhl/injuries` | injury list per team | current | daily | 200 | none | `date` per entry | 1.2 MB payload | OPTIONAL enrichment |
| ESPN scoreboard | `site.api.espn.com/.../hockey/nhl/scoreboard?dates=` | schedule fallback | current | live | 200 | none | | not wired | fallback (not wired) |
| Rotowire lineups | `rotowire.com/hockey/nhl-lineups.php` | goalies/lines HTML | current | intraday | 200 | none | | HTML scrape | not used |

Failure handling: every optional source failure is recorded in `STATUS_context.json.errors` and the refresh continues.
Schedule failure leaves the previous schedule snapshot in force (the conductor keeps using the latest partition).
