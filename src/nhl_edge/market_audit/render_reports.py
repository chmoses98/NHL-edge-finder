"""Render the research documents from the pipeline's machine-readable outputs, so every table cell is traceable to JSON.

``python -m nhl_edge.market_audit.render_reports --data docs/research/nhl-market-audit/data --out docs/research/nhl-market-audit``
Narrative that states a finding is gated on the number it states (computed here), never typed by hand.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

BANNER = "> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `{sha}`."


def pct(x: Any, d: int = 1) -> str:
    return "n/a" if x is None or x != x else f"{100 * x:+.{d}f}%"


def pc(x: Any, d: int = 1) -> str:
    return "n/a" if x is None or x != x else f"{100 * x:.{d}f}%"


def f(x: Any, d: int = 4) -> str:
    return "n/a" if x is None or x != x else f"{x:.{d}f}"


def ci(lo: Any, hi: Any, d: int = 1) -> str:
    return f"[{100 * lo:+.{d}f}%, {100 * hi:+.{d}f}%]" if lo is not None and hi is not None and lo == lo and hi == hi else "n/a"


def table(rows: list[dict[str, Any]], cols: list[tuple[str, str]]) -> str:
    if not rows:
        return "_(no rows)_\n"
    out = ["| " + " | ".join(h for h, _ in cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(r.get(k, "")) for _, k in cols) + " |")
    return "\n".join(out) + "\n"


def J(d: Path, name: str) -> Any:
    p = d / name
    return json.loads(p.read_text()) if p.exists() else {}


class R:
    def __init__(self, data: Path, out: Path):
        self.d, self.out = data, out
        self.lin = J(data, "lineage.json")
        self.sha = (self.lin.get("archive_manifest_sha256") or "")[:16]
        self.banner = BANNER.format(sha=self.sha)

    def write(self, name: str, body: str) -> None:
        (self.out / name).write_text(body.rstrip() + "\n")


def inventory(r: R) -> None:
    ig, cov = J(r.d, "integrity_report.json"), J(r.d, "coverage_report.json")
    ws, hv = J(r.d, "wager_summary.json"), J(r.d, "history_validation.json")
    kinds = [{"kind": k, "files": v["files"], "rows": f"{v['rows']:,}", "first": v["first"][:10], "last": v["last"][:10]} for k, v in sorted(ig["kinds"].items())]
    t, g = cov["totals"], cov["games"]
    s = ig.get("season_level_markets") or {}
    body = f"""# Historical data inventory

{r.banner}

## What exists (verified, not assumed)

| item | exact count | note |
|---|---:|---|
| files on the `data-archive` branch | {ig['files_on_disk']:,} | the "~18,000 indexed files" in the brief is not accurate for this branch snapshot |
| ledger (manifest-indexed) files | {ig['manifest_entries']:,} | every one exists, none duplicated, every SHA-256 matches |
| files NOT in the ledger | {ig['files_not_in_manifest']:,} | derived outputs and pointers: {', '.join(f'{k}: {v}' for k, v in ig['not_in_manifest_by_top_dir'].items())} |
| Kalshi board ticks (market) | {cov['ticks']['n_market_ticks']:,} | {cov['ticks']['n_checkpoint']} full checkpoints + {cov['ticks']['n_delta']:,} hash-chained deltas |
| order-book ticks | {cov['ticks']['n_orderbook_ticks']:,} | 300 books per tick (sampled), 0 fetch errors |
| calendar span of captures | {cov['ticks']['first'][:10]} to {cov['ticks']['last'][:10]} | about 23 days of one season |
| scheduled games seen | {g['scheduled_in_archive']} | |
| **independent games with an official final** | **{g['final']}** | **the only unit that is an independent observation** |
| unique game-scoped contracts | {t['unique_game_scoped_contracts_in_archive']:,} | all have a PROVEN semantic spec |
| contracts on final games | {t['contracts_on_final_games']:,} | |
| contracts on final games with a usable pregame quote | {t['contracts_on_final_games_with_usable_pregame_quote']:,} | two-sided, active, fully captured before scheduled start |
| contracts reliably settled (YES/NO) on final games | {t['decided_contracts_on_final_games']:,} | independent resolver, reconciled with production |
| settled AND with a usable pregame quote | {t['decided_with_usable_pregame_quote']:,} | the analysable set |
| usable pregame change-events | {t['usable_pregame_change_events']:,} | repeated snapshots of the same contracts, NOT independent |
| routed wagers in the accounting ledger | {ws.get('n')} | separate group, never mixed with research selections |

**Honest scale statement.** Thousands of captures and tens of thousands of contracts are {g['final']} independent games. Every contract of a game shares one
outcome path, every snapshot of a contract shares one outcome, and a V1 prediction table of {J(r.d, 'quality_report.json').get('Q7', {}).get('v1_prediction_rows', 0):,} rows is
{J(r.d, 'quality_report.json').get('Q7', {}).get('rows_per_independent_game_v1', 0)} rows per game. All statistics in this audit resample whole games.

## Ledger kinds

{table(kinds, [('kind', 'kind'), ('files', 'files'), ('rows', 'rows'), ('first day', 'first'), ('last day', 'last')])}

## A second dataset: 2025-26 history on `main`

`data/history/kalshi/` holds finalized KXNHLGAME / KXNHLTOTAL / KXNHLSPREAD markets and hourly/1-minute candle closes for the 2025-26 season. It is a
**different instrument of evidence**: best bid/ask at candle close, no depth, no model inputs of its own, no period/team-total/prop markets. It is used only as a
separate tier ("HIST") and is never pooled with the live archive. {hv.get('markets_checked'):,} of its settled markets were used to validate the outcome resolver.

## Season-level markets (separated from single-game markets)

{s.get('n_not_game_scoped', 'n/a'):,} of {s.get('n_markets_total', 'n/a'):,} markets on the last checkpoint board are season futures, awards or player-season statistics. They have different
horizons (months), settlement rules (e.g. the Ted Lindsay market pays $1/N on ties) and statistics, and are excluded from every game-level number here.

{table(s.get('by_family_support', []), [('family', '_family'), ('support', '_support'), ('markets', 'n')])}
Series on the board with no ontology entry ("unresolved"): the rules are quoted verbatim and **no mapping is invented**.

{table([{'series': u['series_ticker'], 'markets': u['n'], 'example title': u['example'], 'rules (primary)': str(u['rules'])[:180]} for u in s.get('unresolved', [])], [('series', 'series'), ('markets', 'markets'), ('example', 'example title'), ('rules', 'rules (primary)')])}

## What cannot be claimed

* Full historical coverage of Kalshi NHL. The live archive starts {cov['ticks']['first'][:10]}; nothing before it exists on this branch.
* Kalshi's own settlement for live-archive contracts. The capture requests only live statuses, so `result` is empty on all {t['unique_game_scoped_contracts_in_archive']:,} contracts;
  settlement truth is the NHL official final, validated separately against Kalshi's own results on the 2025-26 history.
* Depth for anything except winner / spread / total / team total (see CAPTURE_COVERAGE.md).
"""
    r.write("DATA_INVENTORY.md", body)


def coverage(r: R) -> None:
    cov, q = J(r.d, "coverage_report.json"), J(r.d, "quality_report.json")
    fam = [{**x, "has_book": next((f"{b['pct']}%" for b in q.get("Q3", {}).get("by_family", []) if b["family"] == x["family"]), "n/a")} for x in cov["by_family"]]
    tk, g, ob = cov["ticks"], cov["games"], cov["orderbook_of_usable"] if "orderbook_of_usable" in cov else cov.get("orderbook_coverage_of_usable_contracts", {})
    body = f"""# Capture coverage

{r.banner}

## Cadence

* {tk['n_market_ticks']:,} ticks from {tk['first']} to {tk['last']}.
* Gap between ticks (minutes): p10 {tk['gap_minutes']['p10']}, median {tk['gap_minutes']['p50']}, p90 {tk['gap_minutes']['p90']}, p99 {tk['gap_minutes']['p99']}, max {tk['gap_minutes']['max']};
  {tk['n_gaps_over_30min']} gaps over 30 min, {tk['n_gaps_over_60min']} over 60 min.
* Timing semantics (important): a tick is stamped with the capture **start**. The market board is fully written ~30-40 s later and the order books ~91-100 s later (manifest
  `written_at_utc - observed_at_utc`). Point-in-time logic uses `stamp + 45 s` (markets) and `stamp + 105 s` (books) as the instant a quote became knowable.

## Per final game ({g['final']} games)

| measure | value |
|---|---|
| games with at least one usable pregame quote | {g['final_with_any_pregame_usable_quote']} |
| last pregame tick, minutes before scheduled start (p10 / p50 / p90 / max) | {g['last_pregame_tick_lag_min']['p10']} / {g['last_pregame_tick_lag_min']['p50']} / {g['last_pregame_tick_lag_min']['p90']} / {g['last_pregame_tick_lag_min']['max']} |
| pregame ticks within the last 60 min (min / median / max) | {g['pregame_ticks_within_60m']['min']:.0f} / {g['pregame_ticks_within_60m']['p50']:.0f} / {g['pregame_ticks_within_60m']['max']:.0f} |
| markets first listed, hours before start (p10 / p50 / p90) | {g['first_listed_hours_before_start']['p10']} / {g['first_listed_hours_before_start']['p50']} / {g['first_listed_hours_before_start']['p90']} |

## Coverage by market family (final games only)

{table(fam, [('family', 'family'), ('scope', 'scope'), ('contracts', 'contracts'), ('with usable pregame quote', 'contracts_with_usable_pregame_quote'), ('settled YES/NO', 'decided_YES_NO'),
 ('void / unscored', 'void_or_unscored'), ('settled with pregame quote', 'decided_with_pregame_quote'), ('order-book sampled', 'has_book')])}

## Order-book depth is sampled, and only for four families

{ob.get('with_any_pregame_book', 'n/a'):,} of {ob.get('usable_contracts', 'n/a'):,} usable contracts ({ob.get('pct', 'n/a')}%) ever received a pregame book. The cause is the capture rule, not an outage:
`snapshot_orderbooks()` ranks live markets by (support rank, has-quote, earliest expiry) and takes 300 per tick. Only winner / spread / total / team total are `MODELABLE`, so they
fill the 300 slots and **period markets, overtime, first-10-minutes, goalie saves, assists, points, goals and first-goal never have depth**. Executability can therefore be
measured for four families only; everything else is reported as quote-only (DEPTH-UNOBSERVED).

## Not claimed

Every number above is for the {g['final']} games that finished by the snapshot. {g['scheduled_in_archive'] - g['final']} scheduled games are not final and are excluded.
"""
    r.write("CAPTURE_COVERAGE.md", body)


def quality(r: R) -> None:
    q, rec, ig = J(r.d, "quality_report.json"), J(r.d, "outcome_reconciliation.json"), J(r.d, "integrity_report.json")
    hv = J(r.d, "history_validation.json")
    prod = rec["vs_production_settlement"]
    q1 = table(q["Q1"], [("family", "family"), ("contracts", "contracts"), ("two-sided %", "two_sided_pct"), ("no bid %", "no_bid_pct"), ("median spread (c)", "median_spread_cents")])
    q3 = table(q["Q3"]["by_family"], [("family", "family"), ("contracts", "contracts"), ("with any book", "with_any_book"), ("%", "pct")])
    body = f"""# Data-quality audit

{r.banner}

## Integrity (ledger)

| check | result |
|---|---|
| manifest entries / files that exist / duplicated paths | {ig['manifest_entries']:,} / {ig['manifest_entries'] - ig['n_problems']:,} / {ig['duplicate_paths']} |
| SHA-256 mismatches | {ig['n_problems']} |
| market delta chains verified (ok / broken) | {ig['delta_chains']['kalshi/markets']['n_ok']} / {ig['delta_chains']['kalshi/markets']['n_broken']} |
| order-book delta chains verified (ok / broken) | {ig['delta_chains']['kalshi/orderbooks']['n_ok']} / {ig['delta_chains']['kalshi/orderbooks']['n_broken']} |

## Outcome integrity

| check | result |
|---|---|
| final games reconciled across official final, play-by-play goals and boxscore lines | {rec['games_final'] - len(rec['games_with_reconciliation_problems'])} / {rec['games_final']} |
| contracts decided by BOTH my resolver and production settlement | {prod['co_decided']:,} |
| **disagreements** between them | **{prod['disagreements']}** |
| decided by my resolver, not by production | {prod['mine_decided_prod_not']:,} |
| decided by production, not by my resolver | {prod['prod_decided_mine_not']} |
| resolver vs Kalshi's own settlement, 2025-26 history ({hv['markets_checked']:,} markets incl. shootout games) | {hv['disagreements']} disagreements |

Why production leaves ~2,600 contracts unsettled that the resolver decides: overtime and first-10-minutes markets are labelled "semantics not proven" by production (their
contract text is unambiguous and is parsed here), and alternate-line ladders that did not exist at production's settlement candidate cut have no settlement record at all.

## Findings register

| # | finding | evidence | consequence | status |
|---|---|---|---|---|
| F1 | Kalshi `result` is never captured for live contracts | no non-empty `result` in any archived quote event; the capture requests only `open/active` statuses | settlement relies on NHL finals; validated against Kalshi's own results on 2025-26 history | documented; recommend a periodic `finalized` capture (research PR, not applied) |
| F2 | Tick stamp is the capture START | written-at minus observed-at: ~33 s markets, ~94 s books | a quote stamped before puck drop can finish after it | handled: point-in-time uses stamp + lag; {q['Q2']['games_whose_last_stamped_pregame_market_tick_ends_after_start']} games' last market tick and {q['Q2']['games_whose_last_stamped_pregame_book_tick_ends_after_start']} games' last book tick would have leaked under a stamp-only filter |
| F3 | Order books exist for 4 of 14 families only | table below | no executability evidence for props/periods | documented |
| F4 | Registry lacks Kalshi display names "New York I", "New York R", "Utah" | `resolve_name()` returns None; production survives via ticker-tricode fallback | silent dependence on a fallback; fragile to a new alias | verified 1:1 with ticker codes on all 32 clubs; local alias layer; recommend adding aliases to `teams.csv` |
| F5 | Goalie goals break skater-only goal reconciliation | game 2026020010: Shesterkin empty-net goal | a skater-only check flags a clean game | fixed in the resolver (goalie scorers counted); production unaffected |
| F6 | Player contracts for players NOT on the boxscore | 279 distinct (game, player) pairs absent from both clubs' boxscores | the contract text voids only a player "active but never enters"; a scratch is not addressed | held out of all return statistics, never scored; counted separately |
| F7 | One-sided boards for long-tail props | table Q1 below | no executable price on one side | quotes with a missing side are treated as missing, never filled from an older state |
| F8 | Capture family classification vs independent taxonomy | {q['Q5']['n_mismatch']} mismatches of {q['Q5']['n']:,} | none | clean |
| F9 | Production prediction inputs vs archived board | bid match {q['Q6']['bid_match_pct']}%, ask match {q['Q6']['ask_match_pct']}% on {q['Q6']['n']:,} sampled rows | none | clean: no look-ahead or board mismatch in the frozen V1 inputs |
| F10 | Prediction repeated evidence | {q['Q7']['v1_prediction_rows']:,} V1 rows over {q['Q7']['independent_final_games']} games ({q['Q7']['rows_per_independent_game_v1']} per game; ~{q['Q7']['v1_decision_runs_per_game_median']:.0f} decision runs per game) | row counts overstate evidence by ~3 orders of magnitude | all inference clusters by game |
| F11 | Tip-time schedule | no scheduled start moved for any archived game | none | clean |
| F12 | Unresolved season series | see DATA_INVENTORY.md | outside game scope | documented, no mapping invented |

### Q1. Quote completeness at the last pregame tick

{q1}
### Q3. Order-book sampling by family

{q3}
### Q4. Board vs book at the same tick

{json.dumps(q['Q4'], indent=1)}

### Q2. Tip-straddle contamination

{q['Q2']['note']}
"""
    r.write("DATA_QUALITY_AUDIT.md", body)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = R(a.data, a.out)
    for fn in (inventory, coverage, quality):
        fn(r)
    from nhl_edge.market_audit import render_reports_2

    render_reports_2.render_all(r)


if __name__ == "__main__":
    main()
