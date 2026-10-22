# Information-driven market opportunities: goalie confirmations and other news

> RESEARCH ONLY. `M-INFO-1` (revision 2), 151 LIVE games, 302 team-games. The prior audit declared goalie-confirmation repricing **untestable** ("no timestamp of when the starter became public"). That is not quite right: `goalie_observations` rows carry the *source's own* report time (`source_reported_at_utc`) for 74% of pregame confirmations. It is a lower bound on when the fact was public, not proof of when the market learned it — but it is enough for a descriptive event study, and enough to measure how late our own capture is.

## What timestamped information the archive holds

| information | timestamps | usable as "known at" |
|---|---|---|
| Daily Faceoff starting-goalie status (PROJECTED / PROBABLE / CONFIRMED) | our observation time (≈ hourly, ≈ 11,000 pregame rows) and, for **33% of all rows and every one of the 223 pregame first confirmations**, the source's report time | observation: yes (a ceiling on when *we* knew); source time: a floor on when it was public |
| actual starter | boxscore, post-start | label only. The archived `starter` flag is unreliable (False for 76 of 151 games' goalies who played the whole game), so the goalie of record = most ice time |
| lines / injuries (ESPN, DFO lines) | `lines_updated_at_utc`, `reported` per row | partially; no pregame scratches timeline |
| sportsbook moneylines (NHL-API partners: FanDuel, DraftKings, Sportradar, Tipsport, Veikkaus, Doxxbet) | our snapshot time (≈ hourly; American and decimal odds mixed by provider — normalised) | yes, hourly resolution |
| Kalshi quotes | 15-minute board ticks, +45 s availability lag | yes, 15-minute resolution |

## Findings

1. **How often does the expected goalie change?** 94 of 302 team-games (31%) were confirmed as a goalie *other* than the one first projected; 74% were confirmed pregame in our capture at all; of the 223 confirmations (all carry a source time), 32 changed the starter named in the immediately preceding observation (the rest repeated it). Late news is common: by the source's own timestamps the median confirmation is reported ≈ 7.4 hours before the drop, but 25% are reported less than 2.5 hours before.
2. **How fast are we?** Our capture lags the source's own report by a median of **27.6 minutes** (p25 14.1, p75 43.1); **only 26%** of confirmations were captured within 15 minutes. Any strategy that depends on acting within minutes of a goalie report is not feasible with the current cadence.
3. **Does the Kalshi moneyline move?** For the 32 starter-change events vs 186 same-goalie confirmations (placebo = the same windows three hours earlier; post-windows forced to end ≥ 5 minutes before the drop): mean |move| is 0.09–0.33 cents at 15–120 minutes for CHANGE events and 0.10–0.43 cents for SAME events (placebo 0.04–0.36). The CHANGE − SAME difference is −0.004 [−0.10, +0.11] cents at 15 minutes and −0.19 [−0.35, −0.001] at 60 minutes (*smaller* for changes; one interval, uncorrected, n = 29). **There is no detectable repricing of the moneyline mid in response to goalie changes at 15-minute resolution.** Possible reasons (not distinguishable here): the market had already priced the likely backup; the source timestamp lags the real news; the quality gap between the two goalies is small for most changes; moves faster than 15 minutes are invisible.
4. **Our own model.** V1's goalie factor is the status-weighted mix `w·named + (1−w)·alternative`; the ladder is well-calibrated (`M-GOALIE-1`). Where the goalie of record differed from the named one at the cut (17 of 151 games), the share of extreme misses was 29% vs 16% otherwise — a pointer, at n = 17, that unannounced changes are costly for the forecast.

**Conclusion.** A news-based edge **has not been backtested and cannot be from this archive**: the archive can say when a fact was public (floor) and when we knew it, but not when the market learned it, and the cadence is too coarse. The descriptive study gives no hint that Kalshi lags the news; it gives clear evidence that *we* lag the source.

## Other candidate events (not testable today)

Lineup scratches, line-combination changes, injuries and rest decisions: DFO lines and ESPN injuries are archived with their own update times but not at a cadence or coverage that supports an event study (the injury feed's `reported` field is not tied to a game; no pregame-scratch timeline exists). In-game information is out of scope.

## Minimal timestamped capture — proposal (separate production-capture PR; **not activated**)

Goal: be able to say, for each goalie/lineup fact, *when it first appeared at the source and when we first saw it*, at 1–3 minute resolution around the window that matters (10:00 ET to puck drop), at near-zero cost.

1. **No new workflow cadence.** The `capture_worker` chain already runs continuously; add one **conditional** low-cost poll (a single GET of the DFO starting-goalies page, ~100 KB) to each worker cycle during the pregame window instead of a cron workflow (a separate 5-minute workflow would cost roughly 3,000+ Actions minutes a month at one billed minute per run, against a 2,000-minute free allowance).
2. **Event log, not snapshots.** Diff each poll against the last state and append only changes to `context/goalie_events/dt=…/` with `source_reported_at_utc`, `first_seen_utc`, `previous_name`, `name`, `status`, `latency_min`, response sha256 — the pure diff function and tests are in the proposal branch.
3. **Keep the lawful/low-cost sources:** DFO page (already used), NHL API schedule/rosters/boxscore (free), ESPN injuries (already used). No vendor feeds.
4. **Shadow study before any use:** run the log for ≥ 4 weeks with no model change; evaluate (a) capture latency distribution, (b) Kalshi/sportsbook repricing at ≤ 5-minute resolution around events, (c) whether V1's goalie factor updated with a confirmed change beats the stale one *after* the market has moved. Only a pre-registered result of (c) beating the market could justify any use.
5. **Needs approval:** it is a change to production capture. The branch `claude/goalie-capture-proposal` is draft-only and not wired into any job.
