"""Tests for the NHL Projection Foundation challenger stack (research/projection_foundation/nhl)."""
import gzip
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

PF = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PF))

from pf_core import pit  # noqa: E402

from nhl import data, incumbent, inventory, ladder  # noqa: E402

RESULTS = PF / "results"
ROOT = PF.parents[1]


# --------------------------------------------------------------------------- synthetic skater frame
def _synthetic(seed=0, n_players=60, n_games=50, seasons=(2021, 2022, 2023)):
    rng = np.random.default_rng(seed)
    rows = []
    for s in seasons:
        start = pd.Timestamp(f"{s}-10-10")
        for g in range(n_games):
            date = start + pd.Timedelta(days=2 * g)
            for p in range(n_players):
                rate = 0.05 + 0.10 * (p % 6) / 5  # SOG per non-PP minute, persistent by player
                toi_np = 12 + 6 * (p % 3) / 2 + rng.normal(0, 1)
                toi_pp = (3.0 if p % 4 == 0 else 0.2) + rng.normal(0, 0.3)
                toi_pp = max(toi_pp, 0)
                sog_np = rng.poisson(rate * toi_np)
                sog_pp = rng.poisson(0.2 * toi_pp)
                rows.append({"player_id": p, "game_id": s * 10000 + g * 100 + p // 2, "season": s, "game_date": date,
                             "toi_np": toi_np, "toi_pp": toi_pp, "toi": toi_np + toi_pp, "sog_np": sog_np,
                             "sog_pp": sog_pp, "sog": sog_np + sog_pp, "is_home": bool(p % 2),
                             "role": "F1" if p % 3 == 0 else "F3", "pp_role": "PP1" if p % 4 == 0 else "noPP"})
    sk = pd.DataFrame(rows)
    sk = pit.sort_chrono(sk, "player_id", "game_date", "game_id")
    sk = pit.lagged_features(sk, "player_id", ["sog", "sog_np", "sog_pp", "toi", "toi_np", "toi_pp"],
                             halflives=(3, 10, 30), season_col="season")
    sk = pit.sort_chrono(sk, "player_id", "game_date", "game_id")
    sk["toi_np_E"] = sk["toi_np_ewm10"].fillna(13.0)
    sk["toi_pp_E"] = sk["toi_pp_ewm10"].fillna(1.0)
    sk["sog_for_oppf"] = 1.0 + 0.1 * np.sin(np.arange(len(sk)))
    return sk


def test_skater_ladder_recovers_rates_and_is_point_in_time():
    sk = _synthetic()
    log = []
    ladder.skater_ladder(sk, "sog", log)
    for m in "ABCD":
        assert sk[f"mu_sog_{m}"].notna().all()
        assert (sk[f"mu_sog_{m}"] >= 0).all()
    late = sk[(sk["season"] == 2023) & (sk["toi_n"] > 60)]
    # player-level C mean tracks the true rate ordering
    r = late.groupby("player_id")[["mu_sog_C", "sog"]].mean()
    assert np.corrcoef(r["mu_sog_C"], r["sog"])[0, 1] > 0.9
    # poison the outcomes of the final date: earlier predictions must not move
    last = sk["game_date"].max()
    sk2 = _synthetic()
    sk2.loc[sk2["game_date"] == last, ["sog", "sog_np", "sog_pp"]] = 99
    # recompute the lagged features on the poisoned raw data
    raw = sk2[["player_id", "game_id", "season", "game_date", "toi_np", "toi_pp", "toi", "sog_np", "sog_pp", "sog",
               "is_home", "role", "pp_role"]].copy()
    raw = pit.lagged_features(pit.sort_chrono(raw, "player_id", "game_date", "game_id"), "player_id",
                              ["sog", "sog_np", "sog_pp", "toi", "toi_np", "toi_pp"], halflives=(3, 10, 30),
                              season_col="season")
    raw = pit.sort_chrono(raw, "player_id", "game_date", "game_id")
    raw["toi_np_E"] = raw["toi_np_ewm10"].fillna(13.0)
    raw["toi_pp_E"] = raw["toi_pp_ewm10"].fillna(1.0)
    raw["sog_for_oppf"] = 1.0 + 0.1 * np.sin(np.arange(len(raw)))
    ladder.skater_ladder(raw, "sog", [])
    before = sk["game_date"] < last
    for m in "ABCD":
        assert np.allclose(sk.loc[before, f"mu_sog_{m}"], raw.loc[before, f"mu_sog_{m}"]), m


def test_stack_weights_fit_on_development_only():
    sk = _synthetic()
    ladder.skater_ladder(sk, "sog", [])
    sk["mu_sog_E"] = sk["mu_sog_D"] * 1.01
    sk["toi_n"] = sk["sog_n"]
    sk2 = sk.copy()
    sk2.loc[sk2["season"] == 2023, "sog"] = 0  # validation outcomes must not affect the weights
    a = ladder.stack_F(sk, "sog")
    b = ladder.stack_F(sk2, "sog")
    assert np.allclose(a["weights"], b["weights"])
    assert abs(sum(a["weights"]) - 1) < 1e-9


# --------------------------------------------------------------------------- data
def _write_jsonl_gz(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")


def test_archive_newest_snapshot_supersedes_and_regular_season_only(tmp_path, monkeypatch):
    base = {"home_team_id": 1, "away_team_id": 2, "season": 2026, "game_date": "2026-10-01", "player_id": 7,
            "team_id": 1, "toi_s": 600}
    rows_old = [{**base, "game_id": 2026020050, "game_type": 2, "goals": 0, "_observed_at_utc": "2026-10-02T01:00:00Z"}]
    rows_new = [{**base, "game_id": 2026020050, "game_type": 2, "goals": 1, "_observed_at_utc": "2026-10-02T03:00:00Z"},
                {**base, "game_id": 2026010001, "game_type": 1, "goals": 5, "_observed_at_utc": "2026-10-02T03:00:00Z"}]
    _write_jsonl_gz(tmp_path / "player_events" / "players" / "dt=2026-10-02" / "a.jsonl.gz", rows_old)
    _write_jsonl_gz(tmp_path / "player_events" / "players" / "dt=2026-10-02" / "b.jsonl.gz", rows_new)
    monkeypatch.setattr(data, "ARCHIVE", tmp_path)
    data.load_kind.cache_clear()
    try:
        d = data.load_kind("players", (2026,))
        x = d[d["game_id"] == 2026020050]
        assert len(x) == 1 and int(x["goals"].iloc[0]) == 1
        assert (d["game_type"] == 2).all()
    finally:
        data.load_kind.cache_clear()


def test_future_placeholder_rows_are_appended_then_cleared():
    data.set_future({"players": pd.DataFrame([{"game_id": 2099020001, "game_type": 2, "season": 2026,
                                               "game_date": "2099-01-01", "player_id": 1, "team_id": 1}])})
    try:
        d = data.load_kind("players", (2026,))
        assert 2099020001 in set(d["game_id"])
    finally:
        data.set_future({})
    assert 2099020001 not in set(data.load_kind("players", (2026,))["game_id"])


# --------------------------------------------------------------------------- incumbent
def test_incumbent_one_row_per_player_game_from_last_pregame_snapshot(monkeypatch):
    def row(t, fam, thr, p, mins, exp):
        return {"game_id": 2026020010, "player_id": 8470000.0, "family": fam, "threshold": thr, "p_player": p,
                "predicted_at_utc": t, "pregame": True, "minutes_to_start": mins, "meta_expected_toi_min": 18.0,
                "meta_expected_pp_toi_min": 2.0, "meta_expected_shots": 2.5, "meta_expected_goals": exp,
                "meta_expected_assists": 0.4, "meta_expected_points": 0.7, "meta_expected_saves": None,
                "meta_projection_quality": "STANDARD", "meta_deployment_source": "LINES_PROJECTED"}
    fake = pd.DataFrame([row("2026-10-05T10:00:00Z", "player_goals", 0.5, 0.30, 600, 0.30),
                         row("2026-10-05T22:00:00Z", "player_goals", 0.5, 0.33, 30, 0.33),
                         row("2026-10-05T22:00:00Z", "player_goals", 1.5, 0.05, 30, 0.33),
                         row("2026-10-05T23:30:00Z", "player_goals", 0.5, 0.90, -5, 0.90)])  # in-game: excluded
    monkeypatch.setattr(inventory, "CACHE_PP", lambda: fake)
    sk, gl = incumbent.prospective()
    assert len(sk) == 1
    r = sk.iloc[0]
    assert r["inc_goals"] == pytest.approx(0.33)
    assert r["inc_p_goals_1"] == pytest.approx(0.33) and r["inc_p_goals_2"] == pytest.approx(0.05)


def test_rps_is_sum_of_rung_briers():
    y = np.array([0, 1, 3])
    p = {1: np.array([0.3, 0.6, 0.9]), 2: np.array([0.1, 0.2, 0.5])}
    exp = (0.3 ** 2 + 0.1 ** 2, 0.4 ** 2 + 0.2 ** 2, 0.1 ** 2 + 0.5 ** 2)
    assert np.allclose(incumbent.rps(p, y, [1, 2]), exp)


# --------------------------------------------------------------------------- outputs
def test_workflow_parses_and_is_inert_and_secret_free():
    import yaml
    wf = ROOT / ".github" / "workflows" / "projection-foundation.yml"
    d = yaml.safe_load(wf.read_text())
    on = d.get("on", d.get(True))
    assert "schedule" in on and "workflow_dispatch" in on
    text = wf.read_text()
    assert "secrets." not in text
    assert "projection-data" in text and "timeout-minutes" in text


@pytest.mark.skipif(not (RESULTS / "summary.json").exists(), reason="run nhl.run_walkforward first")
def test_summary_follows_contract():
    s = json.load(open(RESULTS / "summary.json"))
    assert s["schema"] == "sift.projection_foundation.sport_summary.v1" and s["sport"] == "NHL"
    for k in ("splits", "inventory", "families", "experiments", "error_investigations", "opponent_adjustment",
              "opportunity", "calibration", "failed_experiments", "gate", "priorities"):
        assert k in s, k
    for f in s["families"]:
        assert f["readiness"] in ("READY", "SHADOW VALIDATION", "NEEDS IMPROVEMENT", "INSUFFICIENT DATA")
        for m in f["models"]:
            for k in ("model", "split", "n_obs", "n_clusters", "mae", "rmse", "bias", "crps", "cover_80", "verdict"):
                assert k in m
    for r in s["inventory"]:
        assert r["pit_class"] in ("archived", "reconstructable", "retrospective", "missing")


@pytest.mark.skipif(not (RESULTS / "projections_latest.json").exists(), reason="run nhl.project first")
def test_projections_latest_contract():
    p = json.load(open(RESULTS / "projections_latest.json"))
    assert p["schema"] == "sift.projections.v1" and p["sport"] == "NHL"
    assert p["model"]["authority"] == "research_only"
    assert p["data_asof_utc"] < max(g["start_utc"] for g in p["games"])
    for x in p["players"]:
        th = [x["thresholds"][k] for k in sorted(x["thresholds"], key=float)]
        assert all(0 <= v <= 1 for v in th)
        assert all(th[i + 1] <= th[i] + 1e-9 for i in range(len(th) - 1))
        assert x["gate"]["status"] in ("PASS", "REVIEW", "BLOCK")
        assert x["p10"] <= x["median"] <= x["p90"]
