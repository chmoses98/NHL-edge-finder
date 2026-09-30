"""PLAYER_SIM_V1 shadow arm inside RUN NHL: V1 and V2 rows are identical with it on or off, it prices real-shaped player
contracts coherently, it fails without taking V1 / V2 down, and it never sees a line observation from after the cutoff."""

import json
from datetime import timedelta
from pathlib import Path

import pandas as pd
import pytest

from nhl_edge.archive.ledger import Ledger
from nhl_edge.kalshi.normalize import quote_cents
from nhl_edge.kalshi.ontology import Ontology, classify_market
from nhl_edge.workflows.simulate import run_simulate
from tests.archive_fixture import NOW, build_archive

REPO_DATA = Path(__file__).resolve().parents[1] / "data"
pytestmark = pytest.mark.skipif(not (REPO_DATA / "history" / "players").exists() or not (REPO_DATA / "params" / "player-sim-1.0.json").exists(),
                                reason="player history / params not present")


def _last_lineup(team_id: int) -> pd.DataFrame:
    p = pd.read_parquet(REPO_DATA / "history" / "players" / "players_2025.parquet")
    p = p[(p["team_id"] == team_id) & (p["game_type"] == 2)]
    return p[p["game_id"] == p["game_id"].max()]


def _market(series: str, suffix: str, title: str, floor: float | None, bid: float, ask: float) -> dict:
    onto = Ontology.load()
    m = {"ticker": f"{series}-26SEP29FLACAR-{suffix}", "event_ticker": f"{series}-26SEP29FLACAR", "series_ticker": series, "title": title,
         "yes_sub_title": title.split(":")[0], "strike_type": "greater" if floor is not None else "structured", "floor_strike": floor,
         "custom_strike": {"hockey_player": "x", "hockey_team": "y"}, "status": "active", "market_type": "binary",
         "rules_primary": f"If {title.split(':')[0]} records it in the Florida vs Carolina NHL game originally scheduled for Sep 29, 2026, then the market resolves to Yes.",
         "yes_bid_dollars": f"{bid:.4f}", "yes_ask_dollars": f"{ask:.4f}", "no_bid_dollars": f"{1 - ask:.4f}", "no_ask_dollars": f"{1 - bid:.4f}",
         "close_time": "2026-10-02T02:30:00Z"}
    cls = classify_market(m, onto)
    m["_family"], m["_support"], m["_quote_cents"] = cls.family, str(cls.support), quote_cents(m)
    return m


def _player_fixture(root: Path, with_future_lines: bool = False) -> list[str]:
    led = Ledger(root, run_id="test-run")
    fla, car = _last_lineup(13), _last_lineup(12)
    roster = []
    for df, tid, ab in ((fla, 13, "FLA"), (car, 12, "CAR")):
        for r in df.itertuples(index=False):
            first, last = str(r.name).split(" ", 1) if " " in str(r.name) else ("X", str(r.name))
            roster.append({"player_id": int(r.player_id), "team_id": tid, "team_abbrev": ab, "position": r.position, "first_name": first.rstrip("."),
                           "last_name": last, "sweater": int(r.sweater)})
    roster += [{"player_id": 8475683, "team_id": 13, "team_abbrev": "FLA", "position": "G", "first_name": "Sergei", "last_name": "Bobrovsky", "sweater": 72},
               {"player_id": 8480382, "team_id": 12, "team_abbrev": "CAR", "position": "G", "first_name": "Frederik", "last_name": "Andersen", "sweater": 31}]
    led.append_rows("context/rosters", roster, observed_at=NOW - timedelta(minutes=10))
    top = fla.sort_values("toi_s", ascending=False).iloc[0]
    initial, last = str(top["name"])[0], str(top["name"]).split(" ", 1)[1].replace(" ", "").replace("-", "").upper()
    code = f"FLA{initial}{last}{int(top['sweater'])}"
    full = f"{initial}. {top['name'].split(' ', 1)[1]}"
    mk = [_market("KXNHLPTS", f"{code}-1", f"{full}: 1+ points", 0.5, 0.50, 0.53), _market("KXNHLPTS", f"{code}-2", f"{full}: 2+ points", 1.5, 0.16, 0.19),
          _market("KXNHLGOAL", f"{code}-1", f"{full}: 1+ goals", 0.5, 0.30, 0.33), _market("KXNHLAST", f"{code}-1", f"{full}: 1+ assists", 0.5, 0.35, 0.38),
          _market("KXNHLFIRSTGOAL", code, f"{full}: First Goalscorer", None, 0.08, 0.10),
          _market("KXNHLSAVE", "FLASBOBROVSKY72-25", "Sergei Bobrovsky: 25+ saves", 24.5, 0.40, 0.44),
          _market("KXNHLSAVE", "FLASBOBROVSKY72-28", "Sergei Bobrovsky: 28+ saves", 27.5, 0.20, 0.24)]
    led.append_rows("kalshi/markets", mk, observed_at=NOW - timedelta(minutes=4), meta={"encoding": "checkpoint"})
    if with_future_lines:
        led.append_rows("context/lines", [{"team_id": 13, "team_abbrev": "FLA", "category": "ev", "unit": "f1", "player_id": int(top["player_id"]),
                                           "lines_updated_at_utc": (NOW + timedelta(hours=3)).isoformat(), "lines_source": "Warmups"}],
                        observed_at=NOW + timedelta(hours=3))
    return [m["ticker"] for m in mk]


@pytest.mark.slow
def test_v1_and_v2_are_identical_with_and_without_the_player_shadow(tmp_path, monkeypatch):
    out = {}
    for flag in ("0", "1"):
        monkeypatch.setenv("NHL_EDGE_PLAYER_SHADOW", flag)
        monkeypatch.setenv("NHL_EDGE_V2_SHADOW", "1")
        root = tmp_path / f"a{flag}"
        build_archive(root)
        tickers = _player_fixture(root)
        assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=2000, now=NOW) == 0
        led = Ledger(root)
        strip = lambda rows: [{k: v for k, v in r.items() if k not in ("prediction_id", "_run_id", "_observed_at_utc", "input_snapshot_ids")}  # noqa: E731
                              for r in sorted(rows, key=lambda r: r["ticker"])]
        out[flag] = (strip(led.iter_rows("predictions")), strip(led.iter_rows("predictions_v2")))
        slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
        if flag == "0":
            assert "player_shadow" not in slate and not list(led.iter_rows("predictions_player"))
            continue
        ps = slate["player_shadow"]
        assert "error" not in ps, ps.get("error")
        assert ps["model_version"] == "PLAYER_SIM_V1" and ps["role"] == "SHADOW" and ps["authority"] == "RESEARCH_ONLY"
        rows = {r["ticker"]: r for r in led.iter_rows("predictions_player")}
        assert set(tickers) <= set(rows)
        assert all(r["authority"] == "RESEARCH_ONLY" and r["role"] == "SHADOW" for r in rows.values())
        p1, p2 = rows[tickers[0]]["p_player"], rows[tickers[1]]["p_player"]
        g1, a1 = rows[tickers[2]]["p_player"], rows[tickers[3]]["p_player"]
        assert None not in (p1, p2, g1, a1) and p1 >= p2 and p1 >= max(g1, a1) and p1 <= g1 + a1
        assert 0 < rows[tickers[4]]["p_player"] < g1  # first goal is rarer than any goal
        s25, s28 = rows[tickers[5]]["p_player"], rows[tickers[6]]["p_player"]
        assert s25 is not None and s25 >= s28
        b = [b for b in ps["blocks"] if b.get("home") == "CAR"][0]
        assert sum(1 for x in ps["blocks"] if x.get("error")) == 4  # the other fixture games have no roster: UNPRICEABLE, not guessed
        assert b["invariant_violations"] == [] and b["correlation"]["matrix"] is not None
        packet = json.loads((root / "slates" / "latest" / "packet.json").read_text())
        assert packet["player_shadow"]["contracts"] and "PLAYER_SIM_V1 shadow" in (root / "slates" / "latest" / "slate.md").read_text()
    assert out["0"] == out["1"]


@pytest.mark.slow
def test_player_shadow_failure_never_breaks_v1_or_v2(tmp_path, monkeypatch):
    from nhl_edge.workflows import shadow_player

    def boom(*a, **k):
        raise RuntimeError("synthetic player failure")

    monkeypatch.setattr(shadow_player, "run_player_shadow", boom)
    monkeypatch.setenv("NHL_EDGE_PLAYER_SHADOW", "1")
    root = tmp_path / "a"
    build_archive(root)
    _player_fixture(root)
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert "synthetic player failure" in slate["player_shadow"]["error"] and slate["v2_shadow"].get("error") is None
    assert list(Ledger(root).iter_rows("predictions")) and list(Ledger(root).iter_rows("predictions_v2"))


@pytest.mark.slow
def test_lines_observed_after_the_cutoff_are_invisible(tmp_path, monkeypatch):
    monkeypatch.setenv("NHL_EDGE_PLAYER_SHADOW", "1")
    root = tmp_path / "a"
    build_archive(root)
    _player_fixture(root, with_future_lines=True)
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    b = [b for b in slate["player_shadow"]["blocks"] if b.get("home") == "CAR"][0]
    assert b["lineups"]["away"]["deployment_source"] == "RECENT_SHIFTS"
    assert slate["player_shadow"]["context"]["lines_snapshot"]["path"] is None
