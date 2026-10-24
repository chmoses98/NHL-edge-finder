"""Gates G7 (runtime), G8 (reproducibility) and G10 (live non-inferiority) for the V2 overtime / regulation-tie projection (RESEARCH_ONLY, read-only).

Procedures and thresholds are those of ``docs/research/overtime_promotion/PREREGISTRATION_G7_G10.md``; nothing here activates or changes a model. G9 (publication
contract) is covered by ``tests/test_overtime_g9.py`` and ``tests/test_projection_registry.py``.

    python -m nhl_edge.research.overtime_gates runtime --status STATUS_worker.json
    python -m nhl_edge.research.overtime_gates replay  --archive <data-archive checkout> --limit 400
    python -m nhl_edge.research.overtime_gates live    --archive <data-archive checkout> --out report
"""

from __future__ import annotations

import gzip
import json
import subprocess
import sys
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np

# --- registered constants (PREREGISTRATION_G7_G10.md); change only by a dated amendment written before the affected data exists ---------------------------------
T0 = datetime(2026, 10, 26, 0, 0, tzinfo=UTC)          # first eligible scheduled start
PREGAME_MARGIN_MIN = 10.0
NI_MARGIN = 0.0010                                      # promotion.NON_INFERIORITY["brier_ot"]
PRIMARY_N = 1050
EXTENSION_N = 1600
HARM_LOOKS = (250, 500, 750)
HARM_CI = 0.99
FINAL_CI = 0.95
CALIBRATION_TOL = 0.03
MIN_PAIR_COVERAGE = 0.90
MAX_FALLBACK = 0.05
N_BOOT = 4000
SEED = 20261024
RUNTIME_BUDGET_S = 300.0
STAGE_BUDGET_S = 150.0


def _dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# G7 — runtime
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def worker_runtime(status: dict[str, Any]) -> dict[str, Any]:
    """Whole-cycle ``duration_s`` of capture-worker cycles that ran ``simulate`` (which includes every shadow arm), from ``STATUS_worker.json``."""
    d = np.array([float(c["duration_s"]) for c in status.get("cycles", []) if "simulate" in (c.get("jobs_run") or []) and c.get("duration_s") is not None])
    if not len(d):
        return {"n_cycles": 0}
    return {"n_cycles": int(len(d)), "median_s": float(np.median(d)), "p95_s": float(np.quantile(d, 0.95)), "max_s": float(d.max()), "share_over_budget": float((d > RUNTIME_BUDGET_S).mean()),
            "budget_s": RUNTIME_BUDGET_S, "pass": bool(np.quantile(d, 0.95) <= RUNTIME_BUDGET_S)}


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# G8 — reproducibility
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
_CHILD = r"""
import hashlib, json, sys
from nhl_edge.sim.engine import TeamParams
from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2
r = simulate_game_v2(TeamParams(1, 'HOM', 3.05), TeamParams(2, 'AWY', 2.85), seed=987654321, n_sims=20000, params=load_params())
print(hashlib.sha256(json.dumps(r.summary(), sort_keys=True, default=float).encode()).hexdigest())
"""


def process_determinism(hash_seeds: Iterable[str] = ("0", "1", "12345")) -> dict[str, Any]:
    """The same inputs and seed give a byte-identical V2 game summary in fresh processes whatever ``PYTHONHASHSEED`` is."""
    import os

    out = {}
    for hs in hash_seeds:
        env = dict(os.environ, PYTHONHASHSEED=hs)
        p = subprocess.run([sys.executable, "-I", "-c", _CHILD], capture_output=True, text=True, env=env, check=False)
        out[hs] = p.stdout.strip() if p.returncode == 0 else f"ERROR {p.stderr.strip()[-200:]}"
    return {"hashes": out, "identical": len(set(out.values())) == 1 and not any(v.startswith("ERROR") for v in out.values())}


def _slate_files(archive: Path) -> list[Path]:
    return sorted((Path(archive) / "slates").glob("dt=*/*/slate.json"))


def archive_replay(archive: Path, params_path: Path | None = None, limit: int = 400, since: str | None = None) -> dict[str, Any]:
    """Re-run ``simulate_game_v2`` from the lambdas, seed and ``n_sims`` stored in archived live V2 game blocks and compare with the archived probabilities exactly."""
    from nhl_edge.sim.engine import TeamParams
    from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

    prm = load_params(params_path)
    checked = mism = 0
    examples: list[dict[str, Any]] = []
    for f in reversed(_slate_files(archive)):
        if since and f.parent.parent.name < f"dt={since}":
            continue
        s = json.loads(f.read_text())
        blocks = (s.get("v2_shadow") or {}).get("blocks") or []
        games = {str(g["game_id"]): g for g in s.get("games", [])}
        for b in blocks:
            g = games.get(str(b["game_id"]))
            det = b.get("detail") or {}
            if g is None or "lam_home" not in det or g.get("seed") is None or not s.get("n_sims"):
                continue
            seed = int(g["seed"]) ^ 0x5F3759DF
            r = simulate_game_v2(TeamParams(int(g["home_team_id"]), g["home"], det["lam_home"]), TeamParams(int(g["away_team_id"]), g["away"], det["lam_away"]), seed=seed,
                                 n_sims=int(s["n_sims"]), params=prm)
            sm = r.summary()
            bad = {k: (sm[k], b["v2"][k]) for k in ("p_home_win", "p_reg_tie", "p_overtime") if sm[k] != b["v2"][k]}
            checked += 1
            if bad:
                mism += 1
                if len(examples) < 5:
                    examples.append({"slate": str(f.parent.name), "game_id": b["game_id"], "diff": bad})
            if checked >= limit:
                break
        if checked >= limit:
            break
    return {"checked": checked, "mismatches": mism, "examples": examples, "pass": bool(checked >= 50 and mism == 0), "params_fitted_at": prm.provenance.get("fitted_at_utc")}


def training_reproduces(history: Path, params_path: Path, features_path: Path, season: int = 2026) -> dict[str, Any]:
    """``fit_live_params`` on the pinned history regenerates the committed V2 parameter files (every field but the fit timestamp)."""
    import tempfile

    from nhl_edge.research.walk_forward_v2 import fit_live_params

    feat = json.loads(Path(features_path).read_text())
    with tempfile.TemporaryDirectory() as td:
        new = fit_live_params(Path(history), Path(td), season, bool(feat.get("use_special_teams", True)), str(feat.get("goalie_model", "true_talent")))
    old_sim = json.loads(Path(params_path).read_text())

    def strip(d: dict[str, Any]) -> dict[str, Any]:
        d = json.loads(json.dumps(d, default=float))
        d.pop("fitted_at_utc", None)
        (d.get("provenance") or {}).pop("fitted_at_utc", None)
        return d
    sim_ok = strip(new["sim"]) == strip(old_sim)
    feat_ok = strip(new["features"]) == strip(feat)
    return {"sim_params_identical": sim_ok, "feature_params_identical": feat_ok, "pass": bool(sim_ok and feat_ok)}


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# G10 — live non-inferiority
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class Pair:
    game_id: str
    date_et: str
    start: datetime
    snapshot: datetime
    p1: float
    p2: float


def pairs_from_slates(slates: Iterable[dict[str, Any]], margin_min: float = PREGAME_MARGIN_MIN) -> tuple[list[Pair], dict[str, int]]:
    """Per game, the latest slate snapshot generated at least ``margin_min`` before the start that carries both V1 and V2 numbers (V1 from the shadow block's ``v1``
    entry, so the pair stays valid after a promotion changes the published fields)."""
    best: dict[str, Pair] = {}
    seen: set[str] = set()
    for s in slates:
        gen = _dt(s.get("generated_at_utc"))
        if gen is None:
            continue
        games = {str(g["game_id"]): g for g in s.get("games", [])}
        for b in (s.get("v2_shadow") or {}).get("blocks") or []:
            gid = str(b.get("game_id"))
            g = games.get(gid)
            if g is None:
                continue
            start = _dt(g.get("start_time_utc"))
            seen.add(gid)
            v1, v2 = (b.get("v1") or {}).get("p_reg_tie"), (b.get("v2") or {}).get("p_overtime")
            if start is None or v1 is None or v2 is None or not (np.isfinite(v1) and np.isfinite(v2)):
                continue
            if (start - gen).total_seconds() < margin_min * 60:
                continue
            cand = Pair(gid, str(g.get("date_et") or s.get("date_et")), start, gen, float(v1), float(v2))
            if gid not in best or gen > best[gid].snapshot:
                best[gid] = cand
    return sorted(best.values(), key=lambda p: (p.start, p.game_id)), {"games_seen_in_v2_blocks": len(seen), "games_with_pregame_pair": len(best)}


def outcomes_from_results(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    """game_id -> 1 if the game ended in OT or SO, 0 if in regulation; final regular-season games only; the latest observation of a game wins (stat corrections)."""
    latest: dict[str, tuple[str, dict[str, Any]]] = {}
    for r in rows:
        if r.get("status") != "final" or str(r.get("game_id", ""))[4:6] != "02":
            continue
        obs = str(r.get("_observed_at_utc") or "")
        gid = str(r["game_id"])
        if gid not in latest or obs >= latest[gid][0]:
            latest[gid] = (obs, r)
    return {g: int(str(r.get("last_period_type")) in ("OT", "SO")) for g, (_, r) in latest.items() if r.get("last_period_type")}


def _boot_mean_ci(delta: np.ndarray, clusters: np.ndarray, level: float, n_boot: int = N_BOOT, seed: int = SEED) -> tuple[float, float]:
    _, inv = np.unique(clusters, return_inverse=True)
    s = np.bincount(inv, weights=delta)
    c = np.bincount(inv).astype(float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(s), size=(n_boot, len(s)))
    m = s[idx].sum(1) / c[idx].sum(1)
    a = (1 - level) / 2
    return float(np.quantile(m, a)), float(np.quantile(m, 1 - a))


def evaluate_live(pairs: list[Pair], outcome: dict[str, int], eligible_games: int | None = None, t0: datetime = T0, fallback_rate: float | None = None) -> dict[str, Any]:
    """Apply the registered G10 rule to the paired games with start >= t0 that have a final outcome. Negative delta = V2 better than V1."""
    rows = [p for p in pairs if p.start >= t0 and p.game_id in outcome]
    n = len(rows)
    out: dict[str, Any] = {"t0": t0.isoformat(), "n_paired_settled": n, "primary_n": PRIMARY_N, "extension_n": EXTENSION_N, "looks": {}}
    if n == 0:
        out.update(status="NO_DATA", verdict="IN PROGRESS (0 paired games)")
        return out
    y = np.array([outcome[p.game_id] for p in rows], float)
    p1, p2 = np.array([p.p1 for p in rows]), np.array([p.p2 for p in rows])
    delta = (p2 - y) ** 2 - (p1 - y) ** 2
    days = np.array([p.date_et for p in rows])
    out.update(delta_mean=float(delta.mean()), brier_v1=float(((p1 - y) ** 2).mean()), brier_v2=float(((p2 - y) ** 2).mean()), mean_p1=float(p1.mean()), mean_p2=float(p2.mean()),
               observed_rate=float(y.mean()), calibration_gap_v2=float(abs(p2.mean() - y.mean())))
    failed_at = None
    for k in HARM_LOOKS:
        if n >= k:
            lo, hi = _boot_mean_ci(delta[:k], days[:k], HARM_CI)
            harm = lo > 0
            out["looks"][str(k)] = {"n": k, "delta": float(delta[:k].mean()), "lo99": lo, "hi99": hi, "significantly_worse": bool(harm)}
            if harm and failed_at is None:
                failed_at = k
    cov = (n / eligible_games) if eligible_games else None
    out["pair_coverage"] = cov
    out["fallback_rate"] = fallback_rate
    if failed_at is not None:
        out.update(status="FAILED_HARM", verdict=f"FAILS (V2 significantly worse at the {failed_at}-game harm look)")
        return out
    def look(label: str, k: int) -> dict[str, Any]:
        lo, hi = _boot_mean_ci(delta[:k], days[:k], FINAL_CI)
        checks = {"upper95_below_margin": hi < NI_MARGIN, "delta_negative": float(delta[:k].mean()) < 0,
                  "calibration_within_tol": abs(float(p2[:k].mean() - y[:k].mean())) <= CALIBRATION_TOL,
                  "pair_coverage_ok": cov is None or cov >= MIN_PAIR_COVERAGE, "fallback_ok": fallback_rate is None or fallback_rate <= MAX_FALLBACK}
        out["looks"][label] = {"n": k, "delta": float(delta[:k].mean()), "lo95": lo, "hi95": hi, "checks": checks, "pass": bool(all(checks.values()))}
        return out["looks"][label]

    if n >= PRIMARY_N:
        prim = look("primary", PRIMARY_N)
        if prim["pass"]:
            out.update(status="PASS", verdict=f"PASS at the primary look (n={PRIMARY_N})")
            return out
        others_ok = all(v for c, v in prim["checks"].items() if c != "upper95_below_margin")
        if others_ok and not prim["checks"]["upper95_below_margin"]:        # Δ̄ < 0 but the upper bound did not clear the margin: the one registered extension
            if n < EXTENSION_N:
                out.update(status="EXTENSION", verdict=f"NOT DECISIVE at n={PRIMARY_N}; the registered extension look is at n={EXTENSION_N}")
                return out
            ext = look("extension", EXTENSION_N)
            if ext["pass"]:
                out.update(status="PASS", verdict=f"PASS at the extension look (n={EXTENSION_N})")
            else:
                out.update(status="FAILED", verdict=f"FAILS at the extension look (n={EXTENSION_N}): {[c for c, v in ext['checks'].items() if not v]}")
            return out
        out.update(status="FAILED", verdict=f"FAILS at the primary look (n={PRIMARY_N}): {[c for c, v in prim['checks'].items() if not v]}")
        return out
    out.update(status="IN_PROGRESS", verdict=f"IN PROGRESS ({n}/{PRIMARY_N} paired settled games)")
    return out


def load_results(archive: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for p in sorted((Path(archive) / "results").glob("dt=*/*.jsonl.gz")):
        with gzip.open(p, "rt", encoding="utf-8") as f:
            rows += [json.loads(line) for line in f if line.strip()]
    return rows


def iter_slates(archive: Path, since: str | None = None) -> Iterable[dict[str, Any]]:
    for f in _slate_files(archive):
        if since and f.parent.parent.name < f"dt={since}":
            continue
        yield json.loads(f.read_text())


def eligible_counts(archive: Path, t0: datetime = T0) -> int:
    """Regular-season games scheduled to start at or after t0 that appear in any slate (the denominator of the pair-coverage check)."""
    seen = {}
    for s in iter_slates(archive, since=t0.strftime("%Y-%m-%d")):
        for g in s.get("games", []):
            st = _dt(g.get("start_time_utc"))
            if st and st >= t0:
                seen[str(g["game_id"])] = st
    return len(seen)


def render(rep: dict[str, Any]) -> str:
    L = ["# G10 live non-inferiority — V2 overtime vs V1 (RESEARCH_ONLY, registered rule)", "",
         f"* eligible from {rep['t0']} · paired settled games **{rep['n_paired_settled']}** · registered primary look {rep['primary_n']} · extension {rep['extension_n']}",
         f"* **status: {rep['status']} — {rep['verdict']}**"]
    if rep.get("delta_mean") is not None:
        L += [f"* mean Brier(OT): V1 {rep['brier_v1']:.5f} · V2 {rep['brier_v2']:.5f} · paired Δ (V2 − V1) {rep['delta_mean']:+.5f} · mean P(OT) V1 {rep['mean_p1']:.3f} / V2 {rep['mean_p2']:.3f} / observed {rep['observed_rate']:.3f}"]
    for k, v in rep.get("looks", {}).items():
        if "lo99" in v:
            L.append(f"* harm look {k}: Δ {v['delta']:+.5f}, 99% [{v['lo99']:+.5f}, {v['hi99']:+.5f}] — {'SIGNIFICANTLY WORSE' if v['significantly_worse'] else 'no harm signal'}")
        else:
            L.append(f"* {k} look (n={v['n']}): Δ {v['delta']:+.5f}, 95% [{v['lo95']:+.5f}, {v['hi95']:+.5f}] — checks {v['checks']} → {'PASS' if v['pass'] else 'not passed'}")
    L += ["", f"Pair coverage {rep.get('pair_coverage')} · fallback rate {rep.get('fallback_rate')}. Only games starting at or after the registration date count toward the decision; the report never switches anything."]
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.overtime_gates")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("runtime")
    r.add_argument("--status", required=True)
    sub.add_parser("determinism")
    rp = sub.add_parser("replay")
    rp.add_argument("--archive", required=True)
    rp.add_argument("--limit", type=int, default=400)
    rp.add_argument("--since")
    lv = sub.add_parser("live")
    lv.add_argument("--archive", required=True)
    lv.add_argument("--out")
    lv.add_argument("--t0", default=T0.isoformat())
    a = ap.parse_args(argv)
    if a.cmd == "runtime":
        print(json.dumps(worker_runtime(json.loads(Path(a.status).read_text())), indent=1))
    elif a.cmd == "determinism":
        print(json.dumps(process_determinism(), indent=1))
    elif a.cmd == "replay":
        print(json.dumps(archive_replay(Path(a.archive), limit=a.limit, since=a.since), indent=1))
    else:
        t0 = _dt(a.t0) or T0
        pairs, cnt = pairs_from_slates(iter_slates(Path(a.archive), since=t0.strftime("%Y-%m-%d")))
        elig = eligible_counts(Path(a.archive), t0)
        rep = evaluate_live(pairs, outcomes_from_results(load_results(Path(a.archive))), eligible_games=elig or None, t0=t0)
        rep["counts"] = cnt | {"eligible_games_scheduled": elig, "generated_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")}
        print(render(rep))
        if a.out:
            Path(a.out + ".json").write_text(json.dumps(rep, indent=1, default=float))
            Path(a.out + ".md").write_text(render(rep))
    return 0


if __name__ == "__main__":
    sys.exit(main())
