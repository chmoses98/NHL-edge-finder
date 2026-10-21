"""Reproducible, resumable, idempotent audit pipeline (RESEARCH_ONLY).

    python -m nhl_edge.market_audit.pipeline --archive <data-archive checkout> --accounting <accounting-data checkout> \
        --history <repo>/data/history --repo <repo root> --work <derived dir> --out <docs/.../data> [--force] [--only step,step]

* Reads the archive and ledger READ-ONLY; writes only under ``--work`` (large parquet, not committed) and ``--out`` (small JSON/CSV).
* Each step records the SHA-256 of its inputs' fingerprint in ``<work>/.steps/<step>.json`` and is skipped when unchanged, so a
  re-run after new captures only redoes what depends on them, and a crash resumes at the failed step.
* ``lineage.json`` binds every output to the archive manifest digest, git commit and package versions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.archive.delta import read_rows
from nhl_edge.archive.ledger import Ledger
from nhl_edge.archive.reconstruct import verify_archive
from nhl_edge.market_audit import (
    AUDIT_VERSION,
    coverage,
    dataset,
    games,
    model_audit,
    quality,
    run_matchup,
    run_registry,
    run_shadow,
    streams,
    thesis_replay,
    wagers,
)
from nhl_edge.market_audit import efficiency as E
from nhl_edge.market_audit.history_validation import summarize, validate

DEPS = {"integrity": ["streams.py"], "streams": ["streams.py"], "tables": ["games.py", "dataset.py", "taxonomy.py", "outcomes.py"],
        "history_validation": ["history_validation.py", "outcomes.py", "taxonomy.py"], "raw": ["games.py"], "panels": ["efficiency.py", "history_validation.py"],
        "coverage": ["coverage.py"], "quality": ["quality.py"], "efficiency": ["efficiency.py"], "power": ["efficiency.py", "hypotheses.py"],
        "registry": ["hypotheses.py", "run_registry.py", "efficiency.py"], "model_audit": ["model_audit.py", "run_registry.py", "efficiency.py"],
        "matchup": ["matchup_study.py", "run_matchup.py", "efficiency.py"], "thesis_replay": ["thesis_replay.py", "efficiency.py"],
        "wagers": ["wagers.py", "efficiency.py"], "case_oct20": ["case_study.py"], "execution": ["execution.py", "hypotheses.py"], "sensitivity": ["sensitivity.py", "hypotheses.py"],
        "shadow": ["run_shadow.py", "expression_engine.py"], "lineage": []}
STEPS = ["integrity", "streams", "tables", "history_validation", "raw", "panels", "coverage", "quality", "efficiency", "power", "registry", "model_audit", "matchup",
         "thesis_replay", "wagers", "case_oct20", "execution", "sensitivity", "shadow", "lineage"]


def _sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Ctx:
    def __init__(self, a: argparse.Namespace):
        self.archive, self.accounting, self.history = a.archive, a.accounting, a.history
        self.repo, self.work, self.out = a.repo, a.work, a.out
        self.work.mkdir(parents=True, exist_ok=True)
        self.out.mkdir(parents=True, exist_ok=True)
        (self.work / ".steps").mkdir(exist_ok=True)
        self.manifest_sha = _sha(self.archive / "manifest.jsonl")
        self.acct_sha = hashlib.sha256(b"".join(_sha(p).encode() for p in sorted((self.accounting / "data" / "accounting").glob("*.jsonl")))).hexdigest()

    def fingerprint(self, step: str) -> str:
        """Hash of (archive manifest, ledger, this step's own modules, and the fingerprints of every EARLIER step).

        A code edit therefore re-runs only the steps that depend on the edited module and everything downstream of them; the
        5-minute streaming step is not repeated because a later report module changed.
        """
        mods = "".join(_sha(Path(__file__).parent / f) for f in sorted(set(DEPS.get(step, [])) | {"__init__.py"}))
        upstream = ""
        for s in STEPS[: STEPS.index(step)]:
            upstream += self._fp_own(s)
        return hashlib.sha256(f"{AUDIT_VERSION}|{self.manifest_sha}|{self.acct_sha}|{mods}|{upstream}|{step}".encode()).hexdigest()

    def _fp_own(self, step: str) -> str:
        mods = "".join(_sha(Path(__file__).parent / f) for f in sorted(set(DEPS.get(step, [])) | {"__init__.py"}))
        return hashlib.sha256(f"{step}|{mods}".encode()).hexdigest()

    def pq(self, name: str) -> pd.DataFrame:
        return pd.read_parquet(self.work / f"{name}.parquet")

    def put(self, name: str, df: pd.DataFrame) -> None:
        df.to_parquet(self.work / f"{name}.parquet", index=False)

    def dump(self, name: str, obj: Any) -> None:
        (self.out / name).write_text(json.dumps(obj, indent=1, default=str))


def s_integrity(c: Ctx) -> None:
    led = Ledger(c.archive)
    man = led.manifest()
    problems = led.verify()
    paths = [e.path for e in man]
    disk = {str(p.relative_to(c.archive)) for p in c.archive.rglob("*") if p.is_file() and ".git" not in p.parts}
    non_ledger = sorted(disk - set(paths))
    top: dict[str, int] = {}
    for n in non_ledger:
        top[n.split("/")[0]] = top.get(n.split("/")[0], 0) + 1
    chains = {k: verify_archive(c.archive, checkpoint_kind=k, delta_kind=d) for k, d in (("kalshi/markets", "kalshi/markets_delta"), ("kalshi/orderbooks", "kalshi/orderbooks_delta"))}
    kinds: dict[str, dict[str, Any]] = {}
    for e in man:
        k = kinds.setdefault(e.kind, {"files": 0, "rows": 0, "first": e.observed_at_utc, "last": e.observed_at_utc})
        k["files"] += 1
        k["rows"] += e.rows or 0
        k["first"], k["last"] = min(k["first"], e.observed_at_utc), max(k["last"], e.observed_at_utc)
    ck = max((e for e in man if e.kind == "kalshi/markets"), key=lambda e: e.observed_at_utc)
    board = pd.DataFrame(read_rows(c.archive / ck.path))
    season: dict[str, Any] = {}
    if len(board):
        board["game_scoped"] = board["ticker"].map(streams.is_game_scoped)
        sl = board[~board["game_scoped"]]
        season = {"checkpoint": ck.path, "n_markets_total": int(len(board)), "n_game_scoped": int(board["game_scoped"].sum()), "n_not_game_scoped": int(len(sl)),
                  "by_family_support": sl.groupby(["_family", "_support"]).size().reset_index(name="n").to_dict("records"),
                  "unresolved": sl[sl["_support"] == "UNRESOLVED"].groupby("series_ticker").agg(n=("ticker", "size"), example=("title", "first"), rules=("rules_primary", "first")).reset_index().to_dict("records"),
                  "note": "season futures/awards/player-season stats are a different instrument class (horizon months, different settlement, tie rules) and are EXCLUDED from every game-level statistic."}
    c.dump("integrity_report.json", {"season_level_markets": season, "manifest_entries": len(man), "duplicate_paths": len(paths) - len(set(paths)), "problems": problems[:50], "n_problems": len(problems),
                                     "files_on_disk": len(disk), "files_not_in_manifest": len(non_ledger), "not_in_manifest_by_top_dir": top,
                                     "delta_chains": {k: {x: v[x] for x in ("n_chains", "n_ok", "n_broken")} for k, v in chains.items()}, "kinds": kinds,
                                     "manifest_sha256": c.manifest_sha})


def s_streams(c: Ctx) -> None:
    a = streams.stream_market_events(c.archive)
    b = streams.stream_book_events(c.archive)
    for k, v in {**a, **b}.items():
        c.put(k, v)


def s_tables(c: Ctx) -> None:
    g = games.build_games(c.archive)
    c.put("games", g)
    cm, specs, meta = dataset.build_contract_master(c.pq("market_static"), g)
    facts = dataset.load_facts(c.archive, g)
    oc = dataset.resolve_all(cm, specs, facts)
    c.put("contract_master", cm)
    c.put("outcomes_audit", oc)
    recon = {gid: f.problems() for gid, f in facts.items() if f.is_final and f.problems()}
    sett = games.read_kind(c.archive, "settlements")
    sett = sett.sort_values("settled_at_utc").groupby("ticker").tail(1)[["ticker", "outcome", "reason", "engine_version"]].rename(columns={"outcome": "prod", "reason": "prod_reason"})
    m = oc.merge(cm[["ticker", "family"]], on="ticker").merge(sett, on="ticker", how="left")
    both = m[m["outcome"].isin(["YES", "NO"]) & m["prod"].isin(["YES", "NO"])]
    c.dump("outcome_reconciliation.json", {
        "contract_master": meta, "games_final": int(g["is_final"].sum()), "games_with_reconciliation_problems": recon,
        "resolver_outcomes": oc["outcome"].value_counts().to_dict(),
        "outcomes_by_family": m.groupby(["family", "outcome"]).size().unstack(fill_value=0).to_dict("index"),
        "vs_production_settlement": {"co_decided": int(len(both)), "disagreements": int((both["outcome"] != both["prod"]).sum()),
                                     "mine_decided_prod_not": int((m["outcome"].isin(["YES", "NO"]) & ~m["prod"].isin(["YES", "NO"])).sum()),
                                     "prod_decided_mine_not": int((~m["outcome"].isin(["YES", "NO"]) & m["prod"].isin(["YES", "NO"])).sum()),
                                     "mine_decided_prod_not_by_family_and_prod_status": m[m["outcome"].isin(["YES", "NO"]) & ~m["prod"].isin(["YES", "NO"])]
                                     .assign(prod=lambda d: d["prod"].fillna("NO_RECORD")).groupby(["family", "prod"]).size().reset_index(name="n").to_dict("records")},
        "taxonomy": cm.groupby(["series", "family", "kind", "period", "semantics_status"]).size().reset_index(name="n").to_dict("records")})


def s_history_validation(c: Ctx) -> None:
    df = validate(c.history)
    s = summarize(df)
    d = df[df["kalshi_result"].isin(["yes", "no"]) & df["mine"].isin(["YES", "NO"])]
    c.dump("history_validation.json", {"markets_checked": int(len(d)), "disagreements": int((d["kalshi_result"].str.upper() != d["mine"]).sum()),
                                       "by_series_and_ending": s.to_dict("records"), "kalshi_scalar_results": int((df["kalshi_result"] == "scalar").sum()),
                                       "unjoined": df["mine"].isin(["NO_GAME_JOIN", "NO_TEAM_JOIN", "NO_SUBJECT"]).sum().item()})


def _flatten_nested(df: pd.DataFrame) -> pd.DataFrame:
    """Parquet cannot store empty structs: serialise any dict/list cell to JSON text (lossless; parse on read)."""
    for col in df.columns:
        if df[col].map(lambda v: isinstance(v, (dict, list))).any():
            df[col] = df[col].map(lambda v: json.dumps(v, default=str) if isinstance(v, (dict, list)) else v)
    return df


def s_raw(c: Ctx) -> None:
    for k in ("predictions", "predictions_v2", "predictions_player", "evaluations", "thesis_decisions", "thesis_postmortems", "thesis_games"):
        df = games.read_kind(c.archive, k)
        if k == "thesis_decisions":  # extract the one survival field the shadow replay needs before flattening
            df["mass_survived"] = df["script_survival"].map(lambda s: s.get("mass_survived") if isinstance(s, dict) else None)
        c.put(f"raw_{k}", _flatten_nested(df))


def s_panels(c: Ctx) -> None:
    ev, cm, g, oc, st = c.pq("quote_events"), c.pq("contract_master"), c.pq("games"), c.pq("outcomes_audit"), c.pq("market_static")
    c.put("live_panel", E.with_returns(E.build_live_panel(ev, cm, g, oc, st)))
    p = E.build_history_panel(c.history)
    gm = pd.concat([pd.read_parquet(p_) for p_ in sorted((c.history / "nhl").glob("games_*.parquet"))])[["game_id", "game_type"]].drop_duplicates("game_id")
    p = p.merge(gm, on="game_id", how="left")
    reg = p[(p["game_type"] == 2) & (p["game_date"] >= "2025-10-01") & (p["game_date"] <= "2026-04-17") & (p["quote_age_min"] <= 60)]
    c.put("hist_reg_panel", E.with_returns(reg))


def s_coverage(c: Ctx) -> None:
    rep = coverage.coverage_report(c.pq("quote_events"), c.pq("contract_master"), c.pq("games"), c.pq("ticks_markets"), c.pq("ticks_orderbooks"),
                                   c.pq("book_events"), c.pq("outcomes_audit"))
    c.dump("coverage_report.json", rep)


def s_quality(c: Ctx) -> None:
    ev, cm, g = c.pq("quote_events"), c.pq("contract_master"), c.pq("games")
    p1, td = c.pq("raw_predictions"), c.pq("raw_thesis_decisions")
    rep = {"Q1": quality.q1_onesided(ev, cm, g), "Q2": quality.q2_straddle(c.pq("ticks_markets"), c.pq("ticks_orderbooks"), g),
           "Q3": quality.q3_book_sampling(c.pq("book_events"), cm, ev, g), "Q4": quality.q4_board_vs_book(ev, c.pq("book_events")),
           "Q5": quality.q5_family_classification(c.pq("market_static"), cm), "Q6": quality.q6_prediction_inputs(p1, ev), "Q7": quality.q7_repeated_evidence(p1, td, g)}
    c.dump("quality_report.json", rep)


def s_efficiency(c: Ctx) -> None:
    import numpy as np

    hist = c.pq("hist_reg_panel")
    hist = hist[(hist["game_date"] >= "2025-10-01") & (hist["game_date"] <= "2026-04-17")]
    live = c.pq("live_panel")
    if "subject_team_id" not in live:
        live["subject_team_id"] = np.nan
    c.dump("market_efficiency.json", {"HIST_2025_26": E.efficiency_report(hist, "HIST_2025_26", with_months=True), "LIVE_2026_27": E.efficiency_report(live, "LIVE_2026_27")})


def s_power(c: Ctx) -> None:
    import numpy as np

    from nhl_edge.market_audit import hypotheses as H

    hist = c.pq("hist_reg_panel")
    hist = hist[(hist["game_date"] >= "2025-10-01") & (hist["game_date"] <= "2026-04-17") & (hist["horizon_min"] == 60)].copy()
    hist["early_season"], hist["move"], hist["model_gap"] = False, np.nan, np.nan
    out = {}
    for hid in ("M1", "M2", "M3", "M4", "M5"):
        h = H.BY_ID[hid]
        s = H.side_columns(hist[h.select(hist)], h.side)
        out[hid] = E.power_table(s, "cost", "pnl")
    c.dump("power_analysis.json", out)


def s_registry(c: Ctx) -> None:
    run_registry.run(c.work, c.repo / "docs/research/walk_forward_v2_wf2_20260929_games.csv", c.out / "hypothesis_results.json")


def s_model_audit(c: Ctx) -> None:
    res: dict[str, Any] = {}
    hist = c.pq("hist_reg_panel")
    hist = hist[(hist["game_date"] >= "2025-10-01") & (hist["game_date"] <= "2026-04-17") & (hist["horizon_min"] == 60)].copy()
    hist = run_registry.hist_model_gaps(hist, c.repo / "docs/research/walk_forward_v2_wf2_20260929_games.csv")
    for arm, col in (("V1", "model_gap_v1"), ("V2", "model_gap_v2")):
        h = hist[hist[col].notna()].copy()
        h["p"] = h["mid"] + h[col]
        for kind in ("winner", "total", "spread"):
            res[f"HIST|{arm}|{kind}"] = model_audit.compare(h[h["kind"] == kind], "p", f"HIST {arm} {kind}")
        res[f"HIST|{arm}|all"] = model_audit.compare(h, "p", f"HIST {arm} all")
    live = c.pq("live_panel")
    live = live[live["horizon_min"] == 60].copy()
    for fn, col, new in (("raw_predictions", "p_data_only", "p_v1"), ("raw_predictions_v2", "p_data_only_v2", "p_v2"), ("raw_predictions_player", "p_player", "p_player")):
        pr = c.pq(fn)[["ticker", "predicted_at_utc", col]]
        pr = pr[pr[col].notna()].assign(pa=lambda d: pd.to_datetime(d["predicted_at_utc"], utc=True)).sort_values("pa")
        q = live[["ticker", "cut"]].drop_duplicates("ticker").sort_values("cut")
        m = pd.merge_asof(q, pr[["ticker", "pa", col]], left_on="cut", right_on="pa", by="ticker", direction="backward")
        assert (m["pa"].dropna() <= m.loc[m["pa"].notna(), "cut"]).all(), "a prediction after the cut leaked into the audit"
        live = live.merge(m[["ticker", col]].rename(columns={col: new}), on="ticker", how="left")
    for kind in ("winner", "spread", "total", "team_total", "period_winner", "period_spread", "period_total"):
        x = live[live["kind"] == kind]
        res[f"LIVE|V1|{kind}"] = model_audit.compare(x, "p_v1", f"LIVE V1 {kind}")
        res[f"LIVE|V2|{kind}"] = model_audit.compare(x, "p_v2", f"LIVE V2 {kind}")
    pl = live[live["kind"] == "player_stat"].merge(c.pq("contract_master")[["ticker", "family"]], on="ticker", suffixes=("", "_c"))
    for fam, x in pl.groupby("family_c"):
        res[f"LIVE|PLAYER_SIM|{fam}"] = model_audit.compare(x, "p_player", f"LIVE PLAYER_SIM {fam}")
    res["LIVE|V1|four_families"] = model_audit.compare(live[live["kind"].isin(["winner", "spread", "total", "team_total"])], "p_v1", "LIVE V1 four families")
    c.dump("model_audit.json", res)


def s_matchup(c: Ctx) -> None:
    c.dump("matchup_study.json", run_matchup.run(c.work, c.history, c.repo / "data/identity/teams.csv"))


def s_thesis_replay(c: Ctx) -> None:
    d = thesis_replay.prepare(c.pq("raw_thesis_decisions"), c.pq("outcomes_audit"))
    res: dict[str, Any] = {}
    variants = {"S0_everything_considered": pd.Series(True, index=d.index), "S1_first_FUNDED": d["funded"], "S2_first_chosen": d["chosen"]}
    for name, mask in variants.items():
        sel = thesis_replay.first_snapshot(d, mask)
        for scope, f in (("all", sel), ("ex_goalscorer", sel[~sel["family"].isin(thesis_replay.GOAL_SCORER)]), ("goalscorer_only", sel[sel["family"].isin(thesis_replay.GOAL_SCORER)])):
            res[f"{name}|{scope}"] = thesis_replay.score(f, f"{name}|{scope}")
    fc = thesis_replay.last_card(d).groupby("logical_wager_key", as_index=False).tail(1)
    res["S3_final_card|all"] = thesis_replay.score(fc, "S3_final_card|all")
    res["S3_final_card|ex_goalscorer"] = thesis_replay.score(fc[~fc["family"].isin(thesis_replay.GOAL_SCORER)], "S3_final_card|ex_goalscorer")
    allc = thesis_replay.first_snapshot(d, variants["S0_everything_considered"])
    s2, s1 = thesis_replay.first_snapshot(d, d["chosen"]), thesis_replay.first_snapshot(d, d["funded"])
    res["by_family_S2"] = {f: thesis_replay.score(x, f) for f, x in s2.groupby("family")}
    res["matched_control_S2"] = thesis_replay.matched_control_test(s2, allc)
    res["matched_control_S2_ex_goalscorer"] = thesis_replay.matched_control_test(s2[~s2["family"].isin(thesis_replay.GOAL_SCORER)], allc[~allc["family"].isin(thesis_replay.GOAL_SCORER)])
    res["matched_control_S1"] = thesis_replay.matched_control_test(s1, allc)
    res["ev_quintiles_all_candidates"] = thesis_replay.ev_quintiles(allc)
    res["ev_quintiles_ex_goalscorer"] = thesis_replay.ev_quintiles(allc[~allc["family"].isin(thesis_replay.GOAL_SCORER)])
    c.dump("thesis_replay.json", res)


def s_wagers(c: Ctx) -> None:
    led = wagers.load_ledger(c.accounting)
    p1 = c.pq("raw_predictions")[["ticker", "predicted_at_utc", "p_data_only"]]
    p2 = c.pq("raw_predictions_v2")[["ticker", "predicted_at_utc", "p_data_only_v2"]]
    a = wagers.audit_wagers(led, c.pq("contract_master"), c.pq("games"), c.pq("outcomes_audit"), c.pq("quote_events"), c.pq("raw_thesis_decisions"), p1, p2)
    a.to_csv(c.out / "wager_audit.csv", index=False)
    d = a[a["ledger_result"].isin(["WON", "LOST"])].copy()
    d["p_mkt_win"] = d["board_mid_yes"].where(d["side"] == "YES", 1 - d["board_mid_yes"])
    d["exp_pl"] = d["contracts"] * d["p_mkt_win"] - d["stake"]
    d["var"] = d["contracts"] ** 2 * d["p_mkt_win"] * (1 - d["p_mkt_win"])
    z = float((d["net_pl"].sum() - d["exp_pl"].sum()) / (d["var"].sum() ** 0.5))
    d["after_start"] = d["min_after_start"] > 0
    d["thesis_covered"] = d["n_thesis_decisions"] > 0
    grp = {k: d.groupby(k).agg(n=("stake", "size"), stake=("stake", "sum"), net_pl=("net_pl", "sum"), expected_pl_at_market=("exp_pl", "sum")).round(2).reset_index().to_dict("records")
           for k in ("after_start", "thesis_covered", "family")}
    r = d[d["board_age_min"] <= 6]
    o20 = a[a["executed_at"].dt.strftime("%Y-%m-%d") == "2026-10-20"]
    c.dump("wager_summary.json", {**wagers.pnl_summary(a), "expected_pl_at_market_mid": float(d["exp_pl"].sum()), "sd_pl_at_market": float(d["var"].sum() ** 0.5),
                                  "z_realized_vs_expected": z, "ledger_vs_resolver_disagreements": int((a["mine_agrees_with_ledger"] == False).sum()),  # noqa: E712
                                  "groups": grp, "n_boards_le_6min_old": int(len(r)), "mean_slippage_vs_displayed_ask_cents": float(100 * r["slippage_vs_board"].mean()),
                                  "oct20": o20.assign(executed_at=o20["executed_at"].astype(str), start=o20["start"].astype(str), board_tick=o20["board_tick"].astype(str)).to_dict("records")})


def s_case_oct20(c: Ctx) -> None:
    from nhl_edge.market_audit import case_study

    led = wagers.load_ledger(c.accounting)
    sf, spm = games.read_kind(c.archive, "script_forecasts"), games.read_kind(c.archive, "script_postmortems")
    for df in (sf, spm):
        df["game_id"] = df["game_id"].astype(str)
    res = case_study.case_for_date("2026-10-20", led, c.pq("contract_master"), c.pq("games"), c.pq("outcomes_audit"), c.pq("quote_events"), c.pq("raw_thesis_decisions"),
                                   c.pq("raw_predictions"), c.pq("raw_predictions_v2"), c.pq("raw_thesis_games"), sf, spm)
    c.dump("oct20_case.json", res)


def s_execution(c: Ctx) -> None:
    import numpy as np

    from nhl_edge.market_audit import execution as X
    from nhl_edge.market_audit import hypotheses as H

    live = c.pq("live_panel")
    l60 = live[(live["horizon_min"] == 60) & live["kind"].isin(["winner", "spread", "total", "team_total"])].copy()
    bk = X.book_at_cut(c.pq("book_events"), l60[["ticker", "cut"]].drop_duplicates("ticker"))
    l60 = l60.merge(bk[["ticker", "yes_levels", "no_levels", "observed_at"]].rename(columns={"observed_at": "observed_at_book"}), on="ticker", how="left")
    res: dict[str, Any] = {}
    for hid in ("M1", "M2", "M3", "M4", "M5", "M7", "M8"):
        h = H.BY_ID[hid]
        sel = l60[h.select(l60.assign(early_season=False, move=np.nan, model_gap=np.nan))].copy()
        sel = sel[sel["yes_levels"].notna()]
        sel["buy_yes"] = h.side == "yes"
        sel["touch_price"] = np.where(sel["buy_yes"], sel["yes_ask"], sel["no_ask"])
        p = X.price_orders(sel, sel["buy_yes"])
        cost = p["touch_price"] + H.taker_fee(p["touch_price"])
        res[hid] = {"games": int(p["game_id"].nunique()), "touch_roi": float((np.where(p["buy_yes"], p["y"], 1 - p["y"]) - cost).sum() / cost.sum()),
                    "n50_contracts": X.book_walk_roi(p, 50), "n200_contracts": X.book_walk_roi(p, 200)}
    c.dump("execution_walk.json", res)


def s_sensitivity(c: Ctx) -> None:
    import numpy as np

    from nhl_edge.market_audit import hypotheses as H
    from nhl_edge.market_audit import sensitivity as S

    hist = c.pq("hist_reg_panel")
    hist = hist[(hist["game_date"] >= "2025-10-01") & (hist["game_date"] <= "2026-04-17")].copy()
    live = c.pq("live_panel")
    for df in (hist, live):
        df["early_season"], df["move"], df["model_gap"] = False, np.nan, np.nan
    res = {f"{t}|{hid}": S.roi_grid(df, H.BY_ID[hid], horizons=(60, 10, 0) if t == "LIVE" else (60, 0))
           for t, df in (("HIST_ALL", hist), ("LIVE", live)) for hid in ("M1", "M2", "M3", "M4", "M5")}
    c.dump("sensitivity.json", res)


def s_shadow(c: Ctx) -> None:
    summ, cards = run_shadow.run(c.work, c.out / "hypothesis_results.json", c.out / "model_audit.json")
    c.dump("shadow_summary.json", summ)
    c.dump("shadow_cards_sample.json", cards[:40])


def s_lineage(c: Ctx) -> None:
    try:
        sha = subprocess.run(["git", "-C", str(c.repo), "rev-parse", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        sha = ""
    arch_head = ""
    try:
        arch_head = subprocess.run(["git", "-C", str(c.archive), "rev-parse", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        pass
    derived = {p.name: {"sha256": _sha(p), "bytes": p.stat().st_size} for p in sorted(c.work.glob("*.parquet"))}
    outputs = {p.name: _sha(p) for p in sorted(c.out.glob("*")) if p.is_file() and p.name != "lineage.json"}
    c.dump("lineage.json", {"audit_version": AUDIT_VERSION, "code_commit": sha, "archive_manifest_sha256": c.manifest_sha, "archive_checkout_head": arch_head,
                            "accounting_ledger_sha256": c.acct_sha, "python": platform.python_version(), "pandas": pd.__version__,
                            "derived_tables": derived, "outputs_sha256": outputs,
                            "note": "derived parquet tables are reproducible from the archive bytes + this code; they are not committed (size). "
                                    "Source records are never modified; a changed manifest digest means a different archive snapshot."})


FUNCS = {"integrity": s_integrity, "streams": s_streams, "tables": s_tables, "history_validation": s_history_validation, "raw": s_raw, "panels": s_panels,
         "coverage": s_coverage, "quality": s_quality, "efficiency": s_efficiency, "power": s_power, "registry": s_registry, "model_audit": s_model_audit, "matchup": s_matchup, "thesis_replay": s_thesis_replay,
         "wagers": s_wagers, "case_oct20": s_case_oct20, "execution": s_execution, "sensitivity": s_sensitivity, "shadow": s_shadow, "lineage": s_lineage}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--accounting", type=Path, required=True)
    ap.add_argument("--history", type=Path, required=True)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--work", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    a = ap.parse_args(argv)
    c = Ctx(a)
    only = [s for s in a.only.split(",") if s]
    for step in STEPS:
        if only and step not in only:
            continue
        marker = c.work / ".steps" / f"{step}.json"
        fp = c.fingerprint(step)
        if step != "lineage" and marker.exists() and not a.force and json.loads(marker.read_text()).get("fingerprint") == fp:
            print(f"[skip] {step} (unchanged inputs)")
            continue
        t = time.time()
        FUNCS[step](c)
        marker.write_text(json.dumps({"fingerprint": fp, "seconds": round(time.time() - t, 1)}))
        print(f"[done] {step} {time.time() - t:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
