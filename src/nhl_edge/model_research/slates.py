"""Compact, point-in-time table of every archived slate run: one row per (run, game).

A slate run is the production simulation at ``generated_at_utc`` using only snapshots written before that instant
(``input_snapshot_ids`` / ``snapshots`` in the packet). ``lam_*`` and ``seed`` are the exact inputs of the V1 simulator, so
the full predictive distribution can be regenerated bit-for-bit with ``nhl_edge.sim.engine.simulate_game``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

V1_KEYS = ("p_home_win", "p_away_win", "p_home_reg_win", "p_away_reg_win", "p_reg_tie", "p_overtime", "p_shootout", "exp_home_goals",
           "exp_away_goals", "exp_total", "total_sd", "margin_sd", "lam_home", "lam_away", "n_sims", "seed", "inputs_trusted")


def _goalie(d: dict[str, Any] | None, pre: str) -> dict[str, Any]:
    d = d or {}
    return {f"{pre}_goalie_status": d.get("status"), f"{pre}_goalie_name": d.get("player_name"), f"{pre}_goalie_id": d.get("player_id"),
            f"{pre}_goalie_conf": d.get("confidence"), f"{pre}_goalie_obs_utc": d.get("observed_at_utc"), f"{pre}_goalie_source": d.get("source")}


def slate_rows(slate_json: Path, last_date_et: str, first_date_et: str = "0000") -> list[dict[str, Any]]:
    s = json.loads(slate_json.read_text())
    if s.get("date_et", "9999") > last_date_et or s.get("date_et", "9999") < first_date_et:
        return []
    v2 = {b["game_id"]: b for b in (s.get("v2_shadow") or {}).get("blocks", [])}
    out = []
    for g in s.get("games", []):
        row: dict[str, Any] = {"run_id": s.get("run_id"), "generated_at_utc": s.get("generated_at_utc"), "slate_date_et": s.get("date_et"),
                               "game_id": str(g["game_id"]), "start_time_utc": g.get("start_time_utc"), "minutes_to_start": g.get("minutes_to_start"),
                               "home": g.get("home"), "away": g.get("away"), "input_reasons": ";".join(g.get("input_reasons") or []),
                               "slate_path": str(slate_json)}
        row.update({f"v1_{k}": g.get(k) for k in V1_KEYS})
        row.update(_goalie(g.get("home_goalie"), "home"))
        row.update(_goalie(g.get("away_goalie"), "away"))
        b = v2.get(str(g["game_id"]))
        if b:
            v = b.get("v2") or {}
            row.update({"v2_lam_home": v.get("lam_home"), "v2_lam_away": v.get("lam_away"), "v2_p_home_win": v.get("p_home_win"),
                        "v2_p_overtime": v.get("p_overtime"), "v2_exp_total": v.get("exp_total")})
        out.append(row)
    return out


def build_slate_table(archive_root: Path, last_date_et: str, first_date_et: str = "0000") -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for p in sorted((Path(archive_root) / "slates").glob("dt=*/*/slate.json")):
        d = p.parent.parent.name.split("=")[1]
        if d > last_date_et or d < first_date_et:
            continue
        rows.extend(slate_rows(p, last_date_et, first_date_et))
    df = pd.DataFrame(rows)
    for c in ("generated_at_utc", "start_time_utc"):
        df[c] = pd.to_datetime(df[c], utc=True)
    return df.sort_values(["game_id", "generated_at_utc"]).reset_index(drop=True)
