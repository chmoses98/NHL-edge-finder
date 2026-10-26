"""Scores the team-minute allocation SHADOW (RESEARCH_ONLY): candidate ``team-minutes-1.0`` vs the published ``team-minutes-0`` on current games.

Inputs are the archive kind ``player_tm_shadow`` (one row per dressed skater per run, BOTH allocations' published-field equivalents computed from the same shares at the same
instant, so the two arms always carry identical pregame timestamps and identical lineups) and the settled ``player_events/players`` rows. For every (game, player) the NEWEST row
whose own ``predicted_at_utc`` is before that game's puck drop is used (rows made after the drop are ineligible); players who did not play are excluded for both arms.

Reported (descriptive; no pass/fail, no promotion): n, bias, MSE and game-clustered paired intervals for total / PP / SH / EV ice time, Poisson deviance of the expected shots,
calibration slopes, and the lead time of the rows used. Nothing here writes to the archive.

    python -m nhl_edge.research.team_minutes_shadow --archive <archive root> [--rows replay.json ...] --out out/team_minutes_shadow.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import timedelta
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import player_diagnosis as PD
from nhl_edge.research.minutes_propagation import poisson_dev
from nhl_edge.timeutil import parse_iso

ARMS = ("legacy", "cand")
TARGETS = {"toi": "toi_s", "pp": "toi_pp_s", "sh": "toi_sh_s", "ev": "toi_ev_s"}


def load_rows(archive: Path | None, extra: list[Path]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if archive is not None:
        from nhl_edge.archive.ledger import Ledger

        rows += list(Ledger(archive).iter_rows("player_tm_shadow"))
    for f in extra:
        rows += json.loads(Path(f).read_text())
    return pd.DataFrame(rows)


def load_actuals(archive: Path) -> pd.DataFrame:
    from nhl_edge.archive.ledger import Ledger

    d = pd.DataFrame(list(Ledger(archive).iter_rows("player_events/players")))
    if d.empty:
        return d
    d = d[(d["game_type"] == 2) & d["shifts_ok"].astype(bool) & (pd.to_numeric(d["toi_s"], errors="coerce") > 0)].copy()
    d["_o"] = d["_observed_at_utc"]
    d = d.sort_values("_o").drop_duplicates(["game_id", "player_id"], keep="last")          # the newest snapshot of a settled game
    d["game_id"] = d["game_id"].astype(str)
    d["player_id"] = d["player_id"].astype(int)
    return d


def last_pregame(rows: pd.DataFrame, min_lead_min: float = 0.0) -> pd.DataFrame:
    r = rows[rows["pregame"].astype(bool) & (pd.to_numeric(rows["minutes_to_start"], errors="coerce") > min_lead_min)].copy()
    r["game_id"] = r["game_id"].astype(str)
    r["player_id"] = r["player_id"].astype(int)
    r["_t"] = r["predicted_at_utc"].map(parse_iso)
    r["start_utc"] = [t + timedelta(minutes=float(m)) for t, m in zip(r["_t"], r["minutes_to_start"])]
    return r.sort_values("_t").drop_duplicates(["game_id", "player_id"], keep="last")


def calib_slope(pred: np.ndarray, y: np.ndarray) -> float:
    return float(np.polyfit(pred, y, 1)[0]) if len(pred) > 2 and pred.std() > 0 else float("nan")


def compare(rows: pd.DataFrame, actuals: pd.DataFrame, n_boot: int = PD.N_BOOT, min_lead_min: float = 0.0) -> dict[str, Any]:
    pre = last_pregame(rows, min_lead_min)
    m = pre.merge(actuals, on=["game_id", "player_id"], how="inner", suffixes=("", "_act"))
    out: dict[str, Any] = {"n_shadow_rows_used": int(len(pre)), "n_paired_with_outcome": int(len(m)), "n_games": int(m["game_id"].nunique()) if len(m) else 0,
                           "coverage_of_shadow_rows": float(len(m) / len(pre)) if len(pre) else None,
                           "lead_minutes": {k: float(v) for k, v in pd.to_numeric(m["minutes_to_start"], errors="coerce").describe(percentiles=[.1, .5, .9])[["min", "10%", "50%", "90%", "max"]].items()} if len(m) else {}}
    if len(m) < 30:
        out["note"] = "fewer than 30 paired player-games: nothing is estimated"
        return out
    game = m["game_id"].to_numpy()
    y = {k: pd.to_numeric(m[c], errors="coerce").to_numpy(float) / 60.0 for k, c in TARGETS.items()}
    y["sog"] = pd.to_numeric(m["sog"], errors="coerce").to_numpy(float)
    pred = {a: {"toi": m[f"{a}_toi"].to_numpy(float), "pp": m[f"{a}_pp"].to_numpy(float), "sh": m[f"{a}_sh"].to_numpy(float), "ev": m[f"{a}_ev"].to_numpy(float), "sog": m[f"{a}_sog"].to_numpy(float)} for a in ARMS}
    res: dict[str, Any] = {}
    for a in ARMS:
        res[a] = {"mean_pred": {k: float(v.mean()) for k, v in pred[a].items()}, "bias": {k: float((pred[a][k] - y[k]).mean()) for k in y},
                  "mse": {k: float(((pred[a][k] - y[k]) ** 2).mean()) for k in y if k != "sog"}, "sog_poisson_deviance": float(poisson_dev(y["sog"], pred[a]["sog"]).mean()),
                  "calibration_slope": {k: calib_slope(pred[a][k], y[k]) for k in ("toi", "pp", "sog")}}
    vs = {}
    for k in y:
        if k == "sog":
            vs["sog_poisson_deviance"] = PD.paired_game_ci(poisson_dev(y[k], pred["cand"][k]) - poisson_dev(y[k], pred["legacy"][k]), game, n_boot=n_boot)
        else:
            vs[f"mse_{k}"] = PD.paired_game_ci((pred["cand"][k] - y[k]) ** 2 - (pred["legacy"][k] - y[k]) ** 2, game, n_boot=n_boot)
    res["cand_minus_legacy"] = vs
    res["mean_actual"] = {k: float(v.mean()) for k, v in y.items()}
    pos = m["pos"].astype(str).to_numpy()
    res["by_position_bias_toi"] = {p: {a: float((pred[a]["toi"][pos == p] - y["toi"][pos == p]).mean()) for a in ARMS} | {"n": int((pos == p).sum())} for p in sorted(set(pos))}
    out["results"] = res
    out["identical_timestamps"] = bool(m["candidate_version"].nunique() == 1)
    return out


def merged_pairs(rows: pd.DataFrame, actuals: pd.DataFrame, min_lead_min: float = 0.0) -> pd.DataFrame:
    return last_pregame(rows, min_lead_min).merge(actuals, on=["game_id", "player_id"], how="inner", suffixes=("", "_act"))


def representatives(m: pd.DataFrame) -> list[dict[str, Any]]:
    """Archetype players chosen by fixed rules from the paired rows (no cherry-picking): who is chosen depends only on the published-template minutes."""
    if m.empty:
        return []
    F, D = m[m["pos"] == "F"], m[m["pos"] == "D"]
    near = lambda d, col, v: d.iloc[(d[col] - v).abs().argsort().iloc[0]]  # noqa: E731
    picks = [("top-line forward (most ice time)", F.loc[F["legacy_toi"].idxmax()]), ("top-six forward (75th percentile of ice time)", near(F, "legacy_toi", F["legacy_toi"].quantile(0.75))),
             ("fourth-line forward (nearest 10 min)", near(F, "legacy_toi", 10.0)), ("top-pair defenceman (most ice time)", D.loc[D["legacy_toi"].idxmax()]),
             ("third-pair defenceman (nearest 15 min)", near(D, "legacy_toi", 15.0)), ("power-play forward (most PP minutes)", F.loc[F["legacy_pp"].idxmax()]),
             ("power-play defenceman (most PP minutes)", D.loc[D["legacy_pp"].idxmax()]), ("penalty-kill defenceman (most SH minutes)", D.loc[D["legacy_sh"].idxmax()])]
    picks += [("largest PP increase under the candidate", m.loc[(m["cand_pp"] - m["legacy_pp"]).idxmax()])]
    pr = m[m["projection_quality"] == "PRIOR_HEAVY"]
    if len(pr):
        picks.append(("prior-heavy (little NHL history) skater", pr.iloc[0]))
    out = []
    for label, r in picks:
        out.append({"archetype": label, "name": r["name"], "team": r["team"], "pos": r["pos"], "game_id": r["game_id"], "lead_min": round(float(r["minutes_to_start"]), 1), "quality": r["projection_quality"],
                    "legacy": {k: round(float(r[f"legacy_{k}"]), 2) for k in ("toi", "ev", "pp", "sh", "sog")}, "candidate": {k: round(float(r[f"cand_{k}"]), 2) for k in ("toi", "ev", "pp", "sh", "sog")},
                    "actual": {"toi": round(float(r["toi_s"]) / 60, 2), "ev": round(float(r["toi_ev_s"]) / 60, 2), "pp": round(float(r["toi_pp_s"]) / 60, 2), "sh": round(float(r["toi_sh_s"]) / 60, 2), "sog": int(r["sog"])},
                    "team_pp_minutes": {"legacy": round(float(r["legacy_team_pp"]), 2), "candidate": round(float(r["cand_team_pp"]), 2)},
                    "team_sh_minutes": {"legacy": round(float(r["legacy_team_sh"]), 2), "candidate": round(float(r["cand_team_sh"]), 2)}})
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--rows", type=Path, nargs="*", default=[], help="additional row files (e.g. replays)")
    ap.add_argument("--no-archive-rows", action="store_true", help="use only --rows (replays) as shadow rows; the archive still supplies the settled outcomes")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--n-boot", type=int, default=PD.N_BOOT)
    ap.add_argument("--min-lead", type=float, default=0.0)
    a = ap.parse_args(argv)
    rows = load_rows(None if a.no_archive_rows else a.archive, a.rows)
    actuals = load_actuals(a.archive)
    res = compare(rows, actuals, a.n_boot, a.min_lead) if len(rows) else {"note": "no player_tm_shadow rows"}
    if len(rows):
        res["representative_players"] = representatives(merged_pairs(rows, actuals, a.min_lead))
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=1, sort_keys=True))
    print(json.dumps(res, indent=1, sort_keys=True)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
