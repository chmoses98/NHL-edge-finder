"""Runner for the WORKLOAD_V1_LC prospective shadow test: write-once pregame records + the scoreboard (RESEARCH_ONLY).

    python -m nhl_edge.research.workload_shadow_run predict --archive DIR --history data/history --out BRANCH_DIR
    python -m nhl_edge.research.workload_shadow_run score   --archive DIR --pf PF_DIR --out BRANCH_DIR

``predict`` reads only SETTLED events and the latest schedule snapshot of the archive, builds outcome-free stub rows for the games that start within the horizon and
have no record yet, and writes them once under ``records/dt=<ET date>/``. A record is never rewritten or deleted (``guard`` re-checks every file against the manifest).
``score`` joins records to the official shots on goal and to the incumbent's published pregame forecast and applies the frozen rule of
docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md. Nothing here reads the market, the betting engine or the app contract.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_shadow as S
from nhl_edge.research import workload_v1 as W
from nhl_edge.timeutil import iso, parse_iso, utcnow

SHADOW_PARAMS = "data/params/workload-lc-1.0.json"
HORIZON_H = 14.0                                  # a game becomes eligible 14 h before its drop: the first run after that is the best-informed one before the drop
LOOKS = (10_000, 20_000, 30_000, 60_000)         # interim (descriptive) / interim / DECISION / final
DECISION_LOOKS = (30_000, 60_000)
MIN_COMPARATOR_COVERAGE = 0.80      # Amendment 1: a decision look needs a pregame incumbent forecast for at least this share of scored player-games
EARLY_FAIL_BIAS = 0.10


# ------------------------------------------------------------------------------------------------------------------ immutable writes
def _sha(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def write_once(out: Path, rel: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    p = out / rel
    if p.exists():
        raise FileExistsError(f"refusing to overwrite {rel}")
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, separators=(",", ":")) + "\n")
    tmp.replace(p)
    entry = {"path": rel, "rows": len(rows), "sha256": _sha(p), "written_at_utc": iso(utcnow())}
    with (out / "MANIFEST.jsonl").open("a") as m:
        m.write(json.dumps(entry) + "\n")
    return entry


def guard(out: Path) -> list[str]:
    """Problems with the immutable record set: a listed file that changed or vanished, or a record file nobody listed."""
    bad: list[str] = []
    listed: dict[str, str] = {}
    mp = out / "MANIFEST.jsonl"
    if mp.exists():
        for line in mp.read_text().splitlines():
            if line.strip():
                e = json.loads(line)
                listed[e["path"]] = e["sha256"]
    for rel, sha in listed.items():
        p = out / rel
        if not p.exists():
            bad.append(f"missing: {rel}")
        elif _sha(p) != sha:
            bad.append(f"modified: {rel}")
    for p in sorted((out / "records").rglob("*.jsonl.gz")) if (out / "records").exists() else []:
        rel = p.relative_to(out).as_posix()
        if rel not in listed:
            bad.append(f"unlisted: {rel}")
    return bad


# ------------------------------------------------------------------------------------------------------------------ archive access
def _read_all_tagged(ledger: Any, kind: str, cutoff: datetime) -> list[dict[str, Any]]:
    """Like ``simulate._read_all`` but every row carries the instant its archive file was observed (``_observed_at_utc``), so re-ingested games can be told apart."""
    from nhl_edge.workflows.simulate import entry_observed_at

    out: list[dict[str, Any]] = []
    for e in ledger.manifest():
        seen = entry_observed_at(e)
        if e.kind != kind or seen > cutoff:
            continue
        with gzip.open(ledger.root / e.path, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    r["_observed_at_utc"] = iso(seen)
                    out.append(r)
    return out


def read_archive(archive: Path, now: datetime) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.simulate import _read_latest

    ledger = Ledger(archive)
    live = {k: _read_all_tagged(ledger, f"player_events/{k}", now) for k in S.TABLES}
    sched, _meta = _read_latest(ledger, "context/schedule", now)
    return live, sched


def existing_games(out: Path) -> set[int]:
    seen: set[int] = set()
    for p in sorted((out / "records").rglob("*.jsonl.gz")) if (out / "records").exists() else []:
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    seen.add(int(json.loads(line)["game_id"]))
    return seen


# ------------------------------------------------------------------------------------------------------------------ predict
def predict(archive: Path, history: Path, out: Path, now: datetime | None = None, code_commit: str = "", params_path: Path | None = None) -> dict[str, Any]:
    now = now or utcnow()
    live, sched = read_archive(archive, now)
    t = S.load_tables(history, live)
    sk, tg = S.build_tables(t)
    done = existing_games(out)
    todo, missed, skipped = [], [], []
    for g in sched:
        if g.get("season_type") != "regular" or g.get("status") not in ("not_started", None):
            continue
        start = parse_iso(g["start_time_utc"])
        if start - now > timedelta(hours=HORIZON_H):
            continue
        if int(g["game_id"]) in done:
            skipped.append(int(g["game_id"]))
        elif start - now < timedelta(minutes=S.PREGAME_MARGIN_MIN):
            missed.append(int(g["game_id"]))          # started, or too close to the drop for a prediction to count as pregame
        else:
            todo.append(g)
    report: dict[str, Any] = {"now_utc": iso(now), "games_written": [], "games_already_recorded": skipped, "games_missed_started": missed, "rows": 0}
    pp = params_path or Path("docs/research/workload_v1/preregistration.json")
    by_day: dict[str, list[dict[str, Any]]] = {}
    for g in todo:
        by_day.setdefault(str(g["game_date_et"]), []).append(g)
    act = out / "activation.json"
    errors: list[str] = []
    for day, games in sorted(by_day.items()):
        try:
            pred, fit = S.predict_day(sk, tg, games, t["players"], t["goalies"], pp, season=2026)
            msha = S.model_sha(fit)
            if act.exists():
                frozen = json.loads(act.read_text()).get("model_sha256")
                if frozen and frozen != msha:
                    raise RuntimeError(f"model fingerprint {msha[:12]} differs from the one frozen at activation {frozen[:12]}: refusing to write (the model may not change during the test)")
            rows = S.records(pred, games, fit, iso(now), code_commit)
            if not rows:
                continue
            rel = f"records/dt={day}/workload_{now.strftime('%Y%m%dT%H%M%SZ')}_{day.replace('-', '')}.jsonl.gz"
            write_once(out, rel, rows)
            report["games_written"] += sorted({int(r["game_id"]) for r in rows})
            report["rows"] += len(rows)
            if not act.exists():
                act.write_text(json.dumps({"activation_utc": iso(now), "code_commit": code_commit, "inputs_sha256": fit.prediction_inputs_sha, "model_sha256": msha, "alpha": fit.alpha,
                                           "registration": "docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md"}, indent=1))
        except Exception as e:      # one bad day must not stop the other days, and what was already written must still be published
            errors.append(f"{day}: {type(e).__name__}: {e}")
    report["errors"] = errors
    cov = out / "coverage"
    cov.mkdir(parents=True, exist_ok=True)
    (cov / f"coverage_{now.strftime('%Y%m%dT%H%M%SZ')}.json").write_text(json.dumps(report, indent=1))
    report["guard"] = guard(out)
    return report


# ------------------------------------------------------------------------------------------------------------------ score
def load_records(out: Path) -> pd.DataFrame:
    """All records, each with the instant its file was written (from the append-only manifest; a record can only have existed after that)."""
    written: dict[str, str] = {}
    mp = out / "MANIFEST.jsonl"
    if mp.exists():
        for line in mp.read_text().splitlines():
            if line.strip():
                e = json.loads(line)
                written[e["path"]] = e["written_at_utc"]
    rows = []
    for p in sorted((out / "records").rglob("*.jsonl.gz")) if (out / "records").exists() else []:
        rel = p.relative_to(out).as_posix()
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    r["written_at_utc"] = written.get(rel)
                    rows.append(r)
    return pd.DataFrame(rows)


def incumbent_forecasts(pf_dir: Path) -> pd.DataFrame:
    """Last PRE-DROP incumbent (PLAYER_SIM_V1) shots forecast per (game, player) from the projection-data forecast archive."""
    rows = []
    for p in sorted((pf_dir / "forecasts" / "nhl").rglob("*.jsonl.gz")) if (pf_dir / "forecasts" / "nhl").exists() else []:
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                if r.get("family") == "shots" and r.get("model_id") == "PLAYER_SIM_V1" and r.get("archived_utc") and r.get("game_start_utc") and r["archived_utc"] < r["game_start_utc"]:
                    rows.append({"game_id": int(r["game_id"]), "player_id": int(r["entity_id"]), "champ_mean": float(r["mean"]), "archived_utc": r["archived_utc"]})
    if not rows:
        return pd.DataFrame(columns=["game_id", "player_id", "champ_mean", "archived_utc"])
    d = pd.DataFrame(rows).sort_values("archived_utc")
    return d.groupby(["game_id", "player_id"], as_index=False).tail(1)


def actuals(live_players: list[dict[str, Any]]) -> pd.DataFrame:
    if not live_players:
        return pd.DataFrame(columns=["game_id", "player_id", "y_sog"])
    d = pd.DataFrame(live_players)
    d = d[pd.to_numeric(d["game_type"], errors="coerce") == 2]
    return pd.DataFrame({"game_id": pd.to_numeric(d["game_id"]).astype(int), "player_id": pd.to_numeric(d["player_id"]).astype(int), "y_sog": pd.to_numeric(d["sog"], errors="coerce")}).dropna()


def eligible_records(rec: pd.DataFrame, frozen_model_sha: str | None = None) -> tuple[pd.DataFrame, dict[str, int]]:
    """Records that count: made pregame by their own clock AND written (per the append-only manifest) before the drop, by the frozen model. Others are kept and listed."""
    if not len(rec):
        return rec, {"late": 0, "written_after_drop": 0, "other_model": 0}
    ok = rec["pregame"].astype(bool)
    n_late = int((~ok).sum())
    if "written_at_utc" in rec.columns:
        w = pd.to_datetime(rec["written_at_utc"], utc=True, errors="coerce")
        st = pd.to_datetime(rec["game_start_utc"], utc=True, errors="coerce")
        after = ok & ~(w < st)
    else:
        after = pd.Series(False, index=rec.index)
    n_after = int(after.sum())
    ok = ok & ~after
    other = pd.Series(False, index=rec.index)
    if frozen_model_sha and "model_sha256" in rec.columns:
        other = ok & (rec["model_sha256"] != frozen_model_sha)
    n_other = int(other.sum())
    return rec[ok & ~other], {"late": n_late, "written_after_drop": n_after, "other_model": n_other}


def score_frame(rec: pd.DataFrame, act: pd.DataFrame, inc: pd.DataFrame, shadow_params: dict[str, Any], n_boot: int = 2000, limit: int | None = None,
                frozen_model_sha: str | None = None) -> dict[str, Any]:
    """The frozen rule. ``rec`` records, ``act`` official SOG of dressed skaters, ``inc`` the incumbent's pregame forecasts.

    ``limit`` scores exactly the first ``limit`` paired player-games in (game start, game, player) order, i.e. the sample of a registered look; ``None`` scores everything so far.
    """
    pre, excl = eligible_records(rec, frozen_model_sha)
    pre = pre.drop_duplicates(["game_id", "player_id"]) if len(pre) else pre
    m = pre.merge(act, on=["game_id", "player_id"], how="inner")
    out: dict[str, Any] = {"n_records_pregame": int(len(pre)), "n_late_records_excluded": excl["late"], "n_records_written_after_drop_excluded": excl["written_after_drop"],
                           "n_records_other_model_excluded": excl["other_model"], "n_scored_dressed": int(len(m)), "n_candidates_not_dressing": int(len(pre) - len(m)), "looks": {}}
    paired = m.merge(inc, on=["game_id", "player_id"], how="inner")
    if len(paired):
        paired = paired.sort_values(["game_start_utc", "game_id", "player_id"], kind="mergesort").reset_index(drop=True)
    if limit is not None and len(paired) >= limit:
        paired = paired.iloc[:limit].reset_index(drop=True)
        m = m[m["game_start_utc"] <= paired["game_start_utc"].iloc[-1]]            # coverage is judged over the same stretch of the season
    out["n_scored_in_sample"] = int(len(m))
    out["n_paired_with_incumbent"] = int(len(paired))
    n = len(paired)
    out["look_reached"] = max([x for x in LOOKS if n >= x], default=None)
    if n < 200:
        out["verdict"] = f"INCONCLUSIVE AT n={n}"
        return out
    y = paired["y_sog"].to_numpy(float)
    gid = paired["game_id"].to_numpy()
    K = W.SOG_K
    pm_lc = np.vstack(paired["pmf"].to_numpy()).astype(float)
    ch_mean = paired["champ_mean"].to_numpy(float)
    pmfs = {"LC": pm_lc, "WORKLOAD_V1_RAW": E.nb_pmf(paired["raw_mean"].to_numpy(float), float(shadow_params.get("alpha_workload_v1_raw", paired["alpha"].iloc[0])), K), "CHAMPION": E.poisson_pmf(ch_mean, K),
            "BASELINE": E.poisson_pmf(paired["base_mean"].to_numpy(float), K)}
    a_ch = shadow_params.get("alpha_champion_nb")
    if a_ch is not None:
        pmfs["CHAMPION_NB"] = E.nb_pmf(ch_mean, float(a_ch), K)
    rows = {a: E.score_arm(p, y, [1, 2, 3, 4, 5]) for a, p in pmfs.items()}
    out["arms"] = {a: E.summarize(r) for a, r in rows.items()}
    diffs = {f"LC_minus_{b}": E.bootstrap_diff(gid, rows["LC"], rows[b], n_boot) for b in rows if b != "LC"}
    out["diffs"] = diffs
    sub = {}
    for pos in ("F", "D"):
        k = (paired["pos"] == pos).to_numpy()
        sub[pos] = {a: E.summarize({kk: v[k] for kk, v in rows[a].items()}) for a in rows if k.any()}
    out["subgroups"] = sub
    lc = out["arms"]["LC"]
    ref_nb = "CHAMPION_NB" if "CHAMPION_NB" in rows else None
    checks = {"crps_vs_champion_ci_upper_lt_0": diffs["LC_minus_CHAMPION"]["crps"]["ci95"][1] < 0,
              "rmse_vs_champion_ci_upper_lt_0": diffs["LC_minus_CHAMPION"]["rmse"]["ci95"][1] < 0,
              "abs_bias_le_0.05": abs(lc["bias"]) <= 0.05, "coverage80_in_band": 0.77 <= lc["coverage80"] <= 0.83}
    if ref_nb:
        checks["crps_vs_champion_nb_ci_upper_lt_0"] = diffs["LC_minus_CHAMPION_NB"]["crps"]["ci95"][1] < 0
        checks["ladder_brier_vs_champion_nb_ci_upper_lt_0"] = diffs["LC_minus_CHAMPION_NB"]["ladder_brier"]["ci95"][1] < 0
        checks["no_position_worse_crps_than_champion_nb"] = all(sub[p]["LC"]["crps"] <= sub[p]["CHAMPION_NB"]["crps"] for p in sub)
    out["original_rule_checks"] = checks
    out["original_rule_complete"] = ref_nb is not None
    out["lc_development_checks"] = {"abs_bias_le_0.02": abs(lc["bias"]) <= 0.02, "crps_give_back_le_0.001": diffs["LC_minus_WORKLOAD_V1_RAW"]["crps"]["ci95"][1] <= 0.001}
    early_fail = abs(lc["bias"]) > EARLY_FAIL_BIAS or diffs["LC_minus_CHAMPION"]["crps"]["ci95"][0] > 0
    look = out["look_reached"]
    coverage = len(paired) / max(len(m), 1)
    out["comparator_coverage"] = coverage
    if look in DECISION_LOOKS and coverage < MIN_COMPARATOR_COVERAGE:
        out["verdict"] = f"INCONCLUSIVE (comparator coverage {coverage:.2f} < {MIN_COMPARATOR_COVERAGE:.2f})"
    elif early_fail and look is not None:
        out["verdict"] = "FAILS FROZEN RULE (early-failure criterion)"
    elif look in DECISION_LOOKS and ref_nb:
        out["verdict"] = "MEETS FROZEN RULE (recommendation to a human only)" if all(checks.values()) else "FAILS FROZEN RULE"
    else:
        out["verdict"] = f"INCONCLUSIVE AT n={n} (decision look at {DECISION_LOOKS[0]})"
    return out


def render(sc: dict[str, Any]) -> str:
    L = ["# WORKLOAD_V1_LC — prospective shadow scoreboard", "", "RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive",
         "", f"* pregame records {sc['n_records_pregame']} · late records excluded {sc['n_late_records_excluded']} · scored (dressed) {sc['n_scored_dressed']} · candidates who did not dress {sc['n_candidates_not_dressing']} · paired with the incumbent's pregame forecast {sc['n_paired_with_incumbent']}",
         f"* **verdict: {sc['verdict']}**", "* registered looks computed so far: " + ("; ".join(k + ": " + v["verdict"] for k, v in sc.get("looks", {}).items()) or "none"), ""]
    if "arms" in sc:
        L += ["| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for a, v in sc["arms"].items():
            L.append(f"| {a} | {v['n']} | {v['bias']:+.4f} | {v['mae']:.4f} | {v['rmse']:.4f} | {v['crps']:.4f} | {v['ladder_brier']:.5f} | {v['coverage80']:.3f} |")
        L += ["", "| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |", "|---|---|---|"]
        for k, d in sc["diffs"].items():
            L.append(f"| {k[len('LC_minus_'):]} | {d['crps']['diff']:+.5f} [{d['crps']['ci95'][0]:+.5f}, {d['crps']['ci95'][1]:+.5f}] | {d['rmse']['diff']:+.5f} [{d['rmse']['ci95'][0]:+.5f}, {d['rmse']['ci95'][1]:+.5f}] |")
        L += ["", "Frozen original rule: " + ", ".join(f"{k}={'PASS' if v else 'FAIL'}" for k, v in sc["original_rule_checks"].items()) + ("" if sc["original_rule_complete"] else "  (CHAMPION_NB checks pending: frozen dispersion not yet recorded)"),
              "LC development checks: " + ", ".join(f"{k}={'PASS' if v else 'FAIL'}" for k, v in sc["lc_development_checks"].items())]
    return "\n".join(L) + "\n"


def write_look(out: Path, n: int, payload: dict[str, Any]) -> bool:
    """A look is computed once, on exactly its registered sample, and never rewritten (exclusive create)."""
    p = out / "looks" / f"look_{n}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        with p.open("x") as f:
            f.write(json.dumps(payload, indent=1, default=float))
    except FileExistsError:
        return False
    return True


def sticky_verdict(looks: dict[int, dict[str, Any]], cumulative: str) -> str:
    early = [n for n, v in sorted(looks.items()) if str(v.get("verdict", "")).startswith("FAILS FROZEN RULE (early")]
    if early:
        return f"FAILS FROZEN RULE (early-failure criterion at look {early[0]:,}); the test is stopped"
    if 60_000 in looks:
        return f"FINAL LOOK (60,000): {looks[60_000]['verdict']}"
    if 30_000 in looks:
        return f"DECISION LOOK (30,000): {looks[30_000]['verdict']} (final look at 60,000 pending)"
    return cumulative


def run_score(archive: Path, pf: Path, out: Path, now: datetime | None = None, params_path: Path | None = None) -> dict[str, Any]:
    now = now or utcnow()
    live, _ = read_archive(archive, now)
    rec = load_records(out)
    shadow = json.loads((params_path or Path(SHADOW_PARAMS)).read_text()) if (params_path or Path(SHADOW_PARAMS)).exists() else {}
    act_p = out / "activation.json"
    frozen = json.loads(act_p.read_text()).get("model_sha256") if act_p.exists() else None
    if not len(rec):
        sc: dict[str, Any] = {"n_records_pregame": 0, "n_late_records_excluded": 0, "n_scored_dressed": 0, "n_candidates_not_dressing": 0, "n_paired_with_incumbent": 0,
                              "verdict": "INCONCLUSIVE AT n=0", "looks": {}}
    else:
        act, inc = actuals(live["players"]), incumbent_forecasts(pf)
        sc = score_frame(rec, act, inc, shadow, frozen_model_sha=frozen)
        sc["cumulative_verdict"] = sc["verdict"]
        looks: dict[int, dict[str, Any]] = {}
        for n in LOOKS:
            f = out / "looks" / f"look_{n}.json"
            if f.exists():
                looks[n] = json.loads(f.read_text())
        stopped = any(str(v.get("verdict", "")).startswith("FAILS FROZEN RULE (early") for v in looks.values())
        for n in LOOKS:
            if n in looks or stopped or sc["n_paired_with_incumbent"] < n:
                continue
            lk = score_frame(rec, act, inc, shadow, limit=n, frozen_model_sha=frozen)
            lk["look"] = n
            lk["computed_at_utc"] = iso(now)
            if write_look(out, n, lk):
                looks[n] = lk
            stopped = str(lk.get("verdict", "")).startswith("FAILS FROZEN RULE (early")
        sc["looks"] = {str(n): {"verdict": v["verdict"], "computed_at_utc": v.get("computed_at_utc"), "n": v["n_paired_with_incumbent"]} for n, v in sorted(looks.items())}
        sc["verdict"] = sticky_verdict(looks, sc["verdict"])
    sc["generated_at_utc"] = iso(now)
    sc["guard"] = guard(out)
    d = out / "scoreboard"
    d.mkdir(parents=True, exist_ok=True)
    (d / "latest.json").write_text(json.dumps(sc, indent=1, default=float))
    (d / "latest.md").write_text(render(sc))
    return sc


def main(argv: list[str] | None = None) -> int:
    import argparse
    import subprocess

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.workload_shadow_run")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("predict")
    p.add_argument("--archive", required=True)
    p.add_argument("--history", default="data/history")
    p.add_argument("--out", required=True)
    sc = sub.add_parser("score")
    sc.add_argument("--archive", required=True)
    sc.add_argument("--pf", required=True)
    sc.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "predict":
        try:
            commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
        except OSError:
            commit = ""
        rep = predict(Path(a.archive), Path(a.history), Path(a.out), code_commit=commit)
        print(json.dumps(rep, indent=1)[:2000])
        if rep["errors"]:
            print("predict errors:", *rep["errors"], sep="\n  ")
        return 2 if rep["guard"] else (3 if rep["errors"] else 0)
    res = run_score(Path(a.archive), Path(a.pf), Path(a.out))
    print(render(res)[:3000] if "arms" in res else json.dumps(res)[:800])
    return 2 if res["guard"] else 0


if __name__ == "__main__":
    sys.exit(main())
