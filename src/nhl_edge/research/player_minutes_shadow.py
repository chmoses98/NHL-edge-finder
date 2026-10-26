"""Prospective ``player-minutes-1.0`` records: pregame ice-time and power-play-time projections with their observed inputs and, later, the outcomes (RESEARCH_ONLY).

Registration: ``docs/research/player_minutes/PREREGISTRATION.md``. A separate versioned schema, a separate orphan branch (``player-minutes-data``) and a separate set of
hypotheses from the WORKLOAD_V1_LC shots test, whose code and rule this module does not change: it reuses only the generic write-once helpers of ``workload_shadow_run``.
Nothing here is published, priced or routed.

Per (game, candidate skater) one write-once record holds
* ``predictions``: ``M0`` = WORKLOAD_V1's own expected minutes by game state (unchanged ``workload_v1.skater_predictions``), ``M1`` = ``M0`` total times
  ``exp(b * log((last3 + 1) / (M0 + 1)))`` with ``b`` frozen in ``data/params/minutes-v1.json``;
* ``inputs``: everything observed before the drop that a later hypothesis might use -- the last three dressed games' minutes, the newest ``context/lines`` and
  ``context/injuries`` rows for the player with their own timestamps and sources, the incumbent's expected minutes as captured, and the snapshot instants;
* provenance: ``predicted_at_utc``, ``pregame`` (at least 10 minutes before the drop), model/inputs fingerprints, code commit.
Outcomes (official ice time by state and shots) are written later, once per game, to separate write-once ``outcomes/`` files; a prediction record is never modified.
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

from nhl_edge.research import workload_shadow as S
from nhl_edge.research import workload_shadow_run as LCR
from nhl_edge.timeutil import iso, parse_iso, utcnow

SCHEMA = "player-minutes-1.0"
MODEL_ID = "MINUTES_V1"
PARAMS_PATH = "data/params/minutes-v1.json"
REGISTRATION = "docs/research/player_minutes/PREREGISTRATION.md"
HORIZON_H = LCR.HORIZON_H
LOOKS = (10_000, 30_000, 60_000)
DECISION_LOOK, FINAL_LOOK = 30_000, 60_000
SEED = 20261024
N_BOOT = 4000
MIN_PP_PAIRS = 10_000
# hypothesis -> required relative change in squared error; it passes when the upper 95% bound is below it
REQUIRED = {"H1": -0.02, "H2": -0.03, "H3": -0.005}


def load_params(path: Path | None = None) -> dict[str, Any]:
    return json.loads(Path(path or PARAMS_PATH).read_text())


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# model
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def last3_minutes(players: pd.DataFrame, before_date_int: int) -> dict[int, tuple[float, int]]:
    """player_id -> (mean ice time in minutes over his last three regular-season games with ice time, dated strictly before the game day; number of such games, at most 3)."""
    if not len(players) or not {"game_type", "game_date", "toi_s", "player_id", "game_id"} <= set(players.columns):
        return {}
    p = players[pd.to_numeric(players["game_type"], errors="coerce") == 2].copy()
    p["date_int"] = p["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
    p["toi"] = pd.to_numeric(p["toi_s"], errors="coerce")
    p = p[(p["date_int"] < before_date_int) & (p["toi"] > 0)].sort_values(["player_id", "date_int", "game_id"])
    out: dict[int, tuple[float, int]] = {}
    for pid, g in p.groupby("player_id"):
        tail = g["toi"].tail(3).to_numpy(float) / 60.0
        out[int(pid)] = (float(tail.mean()), int(len(tail)))
    return out


def usage_adjusted(m0_toi: np.ndarray, last3: np.ndarray, n_known: np.ndarray, b: float, clip: tuple[float, float] = (-1.0, 1.0)) -> np.ndarray:
    """M1: total ice time scaled by exp(b * log((last3 + 1) / (M0 + 1))); players with fewer than three known games keep M0."""
    x = np.where(n_known >= 3, np.log((np.nan_to_num(last3) + 1.0) / (np.asarray(m0_toi, float) + 1.0)), 0.0)
    return np.asarray(m0_toi, float) * np.exp(np.clip(b * x, clip[0], clip[1]))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# observed inputs
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def read_inputs(archive: Path, now: datetime) -> dict[str, Any]:
    """Newest ``context/lines`` and ``context/injuries`` partitions observed at or before ``now`` (never a later one), with their own metadata.
    These are optional enrichments: a partition that cannot be read is recorded as such and never blocks the projections."""
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.simulate import _read_latest

    led = Ledger(archive)
    out: dict[str, Any] = {}
    for key, kind in (("lines", "context/lines"), ("injuries", "context/injuries")):
        try:
            rows, meta = _read_latest(led, kind, now)
            out[key], out[f"{key}_meta"] = rows, {k: meta.get(k) for k in ("path", "observed_at_utc", "age_min")}
        except Exception as e:      # noqa: BLE001 - truncated gzip (EOFError), bad json, missing file
            out[key], out[f"{key}_meta"] = [], {"error": f"{type(e).__name__}: {str(e)[:120]}"}
    return out


def incumbent_capture(archive: Path, now: datetime, game_ids: set[int]) -> dict[tuple[int, int], dict[str, Any]]:
    """PLAYER_SIM_V1's expected total / power-play minutes for (game, player), from its own immutable ``predictions_player`` rows archived at or before ``now`` (the newest one).
    Only players the production engine priced have one; the others simply have no value (never imputed)."""
    from nhl_edge.archive.ledger import Ledger

    led = Ledger(archive)
    lo = (now - timedelta(days=3)).strftime("%Y-%m-%d")
    best: dict[tuple[int, int], dict[str, Any]] = {}
    for r in led.iter_rows("predictions_player", dt_from=lo):
        try:
            gid, pid = int(r["game_id"]), int(r["player_id"])
        except (KeyError, TypeError, ValueError):
            continue
        at = r.get("predicted_at_utc")
        if gid not in game_ids or not at or parse_iso(at) > now or r.get("meta_expected_toi_min") is None:
            continue
        cur = best.get((gid, pid))
        if cur is None or parse_iso(at) > parse_iso(cur["at"]):
            best[(gid, pid)] = {"toi_min": float(r["meta_expected_toi_min"]), "pp_min": None if r.get("meta_expected_pp_toi_min") is None else float(r["meta_expected_pp_toi_min"]), "at": at}
    return best


def _lines_for(rows: list[dict[str, Any]], pid: int) -> list[dict[str, Any]]:
    keep = ("category", "unit", "slot", "lines_updated_at_utc", "lines_source", "observed_at_utc", "injury_status", "game_time_decision", "resolution")
    return [{k: r.get(k) for k in keep} for r in rows if r.get("player_id") == pid]


def _injury_index(rows: list[dict[str, Any]]) -> dict[tuple[int, str], list[dict[str, Any]]]:
    from nhl_edge.data.lines import fold

    keep = ("status", "type", "detail", "return_date", "reported", "source")
    idx: dict[tuple[int, str], list[dict[str, Any]]] = {}
    for r in rows:
        try:
            idx.setdefault((int(r["team_id"]), fold(r.get("player_name"))), []).append({k: r.get(k) for k in keep})
        except (KeyError, TypeError, ValueError):
            continue
    return idx


def build_rows(pred: pd.DataFrame, games: list[dict[str, Any]], fit: S.Fit, params: dict[str, Any], players: pd.DataFrame, observed: dict[str, Any],
               incumbent: dict[tuple[int, int], dict[str, Any]], predicted_at_utc: str, code_commit: str) -> list[dict[str, Any]]:
    from nhl_edge.data.lines import fold

    start = {int(g["game_id"]): g["start_time_utc"] for g in games}
    di = int(str(games[0]["game_date_et"]).replace("-", ""))
    recent = last3_minutes(players, di)
    last3 = np.array([recent.get(int(p), (np.nan, 0))[0] for p in pred["player_id"]], float)
    nk = np.array([recent.get(int(p), (np.nan, 0))[1] for p in pred["player_id"]], int)
    m0 = pred["wl_toi"].to_numpy(float)
    m1 = usage_adjusted(m0, last3, nk, float(params["usage_coef"]), (float(params["multiplier_clip"][0]), float(params["multiplier_clip"][1])))
    inj = _injury_index(observed.get("injuries") or [])
    msha = S.model_sha(fit)
    out = []
    for i, r in enumerate(pred.itertuples(index=False)):
        gid, pid = int(r.game_id), int(r.player_id)
        cap = incumbent.get((gid, pid))
        inputs = {"last3_toi_min": None if nk[i] == 0 else round(float(last3[i]), 4), "n_known_recent_games": int(nk[i]),
                  "lines": _lines_for(observed.get("lines") or [], pid), "injury": inj.get((int(r.team_id), fold(str(r.name))), []),
                  "incumbent_toi_min": None if cap is None else cap["toi_min"], "incumbent_pp_min": None if cap is None else cap["pp_min"], "incumbent_at_utc": None if cap is None else cap["at"],
                  "lines_snapshot": observed.get("lines_meta"), "injuries_snapshot": observed.get("injuries_meta")}
        out.append({"schema": SCHEMA, "model_id": MODEL_ID, "game_id": gid, "game_start_utc": start[gid], "predicted_at_utc": predicted_at_utc,
                    "pregame": S._pregame(predicted_at_utc, start[gid]), "player_id": pid, "name": str(r.name), "pos": str(r.pos), "team_id": int(r.team_id), "opp_id": int(r.opp_id),
                    "is_home": bool(r.is_home),
                    "predictions": {"M0_toi_min": round(float(m0[i]), 5), "M1_toi_min": round(float(m1[i]), 5), "pp_min": round(float(pred["wl_toi_pp"].iloc[i]), 5),
                                    "sh_min": round(float(pred["wl_toi_sh"].iloc[i]), 5), "ev_min": round(float(pred["wl_toi_evreg"].iloc[i]), 5), "ot_min": round(float(pred["wl_toi_ot"].iloc[i]), 5)},
                    "inputs": inputs, "usage_coef": float(params["usage_coef"]), "model_sha256": msha,
                    "inputs_sha256": hashlib.sha256(json.dumps(inputs, sort_keys=True, default=str).encode()).hexdigest(), "code_commit": code_commit, "conditional_on": "dressing",
                    "authority": "research_only", "role": "shadow"})
    return out


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# predict
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def predict(archive: Path, history: Path, out: Path, now: datetime | None = None, code_commit: str = "", params_path: Path | None = None,
            workload_prereg: Path | None = None) -> dict[str, Any]:
    """Write-once records for the games that start within the horizon and have none yet. Same eligibility rules as the LC runner (horizon, pregame margin, activation fingerprint, per-day isolation)."""
    now = now or utcnow()
    params = load_params(params_path)
    live, sched = LCR.read_archive(archive, now)
    t = S.load_tables(history, live)
    sk, tg = S.build_tables(t)
    done = LCR.existing_games(out)
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
            missed.append(int(g["game_id"]))
        else:
            todo.append(g)
    report: dict[str, Any] = {"now_utc": iso(now), "games_written": [], "games_already_recorded": skipped, "games_missed_started": missed, "rows": 0, "errors": []}
    by_day: dict[str, list[dict[str, Any]]] = {}
    for g in todo:
        by_day.setdefault(str(g["game_date_et"]), []).append(g)
    observed: dict[str, Any] = {"lines": [], "injuries": [], "lines_meta": None, "injuries_meta": None}
    incumbent: dict[tuple[int, int], dict[str, Any]] = {}
    if by_day:                                  # optional enrichments: a bad row or file is recorded, never allowed to stop the projections
        try:
            observed = read_inputs(archive, now)
        except Exception as e:      # noqa: BLE001
            report["errors_optional"] = [f"inputs: {type(e).__name__}: {str(e)[:160]}"]
        try:
            incumbent = incumbent_capture(archive, now, {int(g["game_id"]) for gs in by_day.values() for g in gs})
        except Exception as e:      # noqa: BLE001
            report.setdefault("errors_optional", []).append(f"incumbent: {type(e).__name__}: {str(e)[:160]}")
    act = out / "activation.json"
    pp = workload_prereg or Path("docs/research/workload_v1/preregistration.json")
    for day, games in sorted(by_day.items()):
        try:
            pred, fit = S.predict_day(sk, tg, games, t["players"], t["goalies"], pp, season=2026)
            msha = S.model_sha(fit)
            if act.exists():
                frozen = json.loads(act.read_text()).get("model_sha256")
                if frozen and frozen != msha:
                    raise RuntimeError(f"model fingerprint {msha[:12]} differs from the one frozen at activation {frozen[:12]}: refusing to write (the model may not change during the test)")
            rows = build_rows(pred, games, fit, params, t["players"], observed, incumbent, iso(now), code_commit)
            if not rows:
                continue
            LCR.write_once(out, f"records/dt={day}/minutes_{now.strftime('%Y%m%dT%H%M%SZ')}_{day.replace('-', '')}.jsonl.gz", rows)
            report["games_written"] += sorted({int(r["game_id"]) for r in rows})
            report["rows"] += len(rows)
            if not act.exists():
                act.write_text(json.dumps({"activation_utc": iso(now), "schema": SCHEMA, "code_commit": code_commit, "model_sha256": msha, "usage_coef": params["usage_coef"],
                                           "registration": REGISTRATION}, indent=1))
        except Exception as e:      # one bad day must not stop the other days, and what was already written must still be published
            report["errors"].append(f"{day}: {type(e).__name__}: {e}")
    cov = out / "coverage"
    cov.mkdir(parents=True, exist_ok=True)
    (cov / f"coverage_{now.strftime('%Y%m%dT%H%M%SZ')}.json").write_text(json.dumps(report, indent=1))
    report["guard"] = guard(out)
    return report


def guard(out: Path) -> list[str]:
    """Everything the LC guard checks (listed files unchanged and present, no unlisted record) plus the same for outcomes."""
    bad = LCR.guard(out)
    listed: set[str] = set()
    mp = out / "MANIFEST.jsonl"
    if mp.exists():
        listed = {json.loads(line)["path"] for line in mp.read_text().splitlines() if line.strip()}
    for sub in ("outcomes", "incumbent"):
        if (out / sub).exists():
            for p in sorted((out / sub).rglob("*.jsonl.gz")):
                rel = p.relative_to(out).as_posix()
                if rel not in listed:
                    bad.append(f"unlisted: {rel}")
    return bad


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# outcomes
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def _games_in(out: Path, sub: str) -> set[int]:
    seen: set[int] = set()
    if (out / sub).exists():
        for p in sorted((out / sub).rglob("*.jsonl.gz")):
            with gzip.open(p, "rt", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        seen.add(int(json.loads(line)["game_id"]))
    return seen


def incumbent_last_predrop(archive: Path, starts: dict[int, str], now: datetime) -> dict[tuple[int, int], dict[str, Any]]:
    """For each (game, player) the NEWEST PLAYER_SIM_V1 ``predictions_player`` row whose own ``predicted_at_utc`` is before that game's puck drop (and not after ``now``): its expected total
    and power-play minutes with the row's timestamp. These are immutable, time-stamped archive rows; nothing is recomputed and no row made after the drop is eligible."""
    from nhl_edge.archive.ledger import Ledger

    if not starts:
        return {}
    first = min(parse_iso(v) for v in starts.values()) - timedelta(days=1)
    best: dict[tuple[int, int], dict[str, Any]] = {}
    for r in Ledger(archive).iter_rows("predictions_player", dt_from=first.strftime("%Y-%m-%d")):
        try:
            gid, pid = int(r["game_id"]), int(r["player_id"])
        except (KeyError, TypeError, ValueError):
            continue
        at = r.get("predicted_at_utc")
        if gid not in starts or not at or r.get("meta_expected_toi_min") is None:
            continue
        try:
            t_at = parse_iso(at)
        except ValueError:          # one malformed timestamp must not lose the comparator of every game
            continue
        if t_at >= parse_iso(starts[gid]) or t_at > now:
            continue
        cur = best.get((gid, pid))
        if cur is None or t_at > parse_iso(cur["at"]):
            best[(gid, pid)] = {"toi_min": float(r["meta_expected_toi_min"]), "pp_min": None if r.get("meta_expected_pp_toi_min") is None else float(r["meta_expected_pp_toi_min"]), "at": at}
    return best


CAPTURE_DELAY_H = 4.0          # a game is captured only this long after its drop, so the last pre-drop archive push has landed
CAPTURE_GRACE_DAYS = 7.0       # after this long without any archive partition for the game, explicit nulls are written (reason recorded)


def _has_partition(archive: Path, start_iso: str) -> bool:
    d = parse_iso(start_iso)
    return any((Path(archive) / "predictions_player" / f"dt={(d + timedelta(days=k)).strftime('%Y-%m-%d')}").exists() for k in (-1, 0))


def capture_incumbent(archive: Path, out: Path, now: datetime | None = None) -> dict[str, Any]:
    """Supplementary comparator for H2 (NOT the registered one): once a recorded game has started, write once, per game date, the incumbent's latest pre-drop expected minutes for every
    candidate of that game, with explicit missing values for candidates the production engine never priced. Games whose archive partitions are no longer in the checkout are reported, not guessed."""
    now = now or utcnow()
    rec = load_dir(out, "records")
    if not len(rec):
        return {"games_captured": [], "pending": []}
    done = _games_in(out, "incumbent")
    g = rec.drop_duplicates("game_id")[["game_id", "game_start_utc"]]
    cand = {int(a): b for a, b in zip(g["game_id"], g["game_start_utc"], strict=True) if int(a) not in done and parse_iso(b) + timedelta(hours=CAPTURE_DELAY_H) <= now}
    # a game whose archive partitions are not in the checkout is NOT captured as all-null: it waits (and is reported) until the grace period has passed
    starts = {gid: b for gid, b in cand.items() if _has_partition(archive, b) or parse_iso(b) + timedelta(days=CAPTURE_GRACE_DAYS) <= now}
    waiting = sorted(set(cand) - set(starts))
    best = incumbent_last_predrop(archive, starts, now)
    captured: list[int] = []
    for day, grp in rec[rec["game_id"].astype(int).isin(starts)].drop_duplicates(["game_id", "player_id"]).groupby(rec["game_start_utc"].astype(str).str[:10]):
        rows = []
        for r in grp.itertuples():
            b = best.get((int(r.game_id), int(r.player_id)))
            rows.append({"game_id": int(r.game_id), "player_id": int(r.player_id), "game_start_utc": r.game_start_utc, "inc_toi_min": None if b is None else b["toi_min"],
                         "inc_pp_min": None if b is None else b["pp_min"], "incumbent_predicted_at_utc": None if b is None else b["at"],
                         "incumbent_lead_min": None if b is None else round((parse_iso(r.game_start_utc) - parse_iso(b["at"])).total_seconds() / 60, 1), "captured_at_utc": iso(now),
                         "reason": None if b is not None else ("archive_window_expired" if not _has_partition(archive, r.game_start_utc) else "not_priced")})
        LCR.write_once(out, f"incumbent/dt={day}/incumbent_{now.strftime('%Y%m%dT%H%M%SZ')}.jsonl.gz", rows)
        captured += sorted({r["game_id"] for r in rows})
    return {"games_captured": captured, "waiting_for_archive": waiting, "pending": sorted(set(starts) - set(captured)), "n_games_with_any_incumbent_row": len({k[0] for k in best})}


def settle(archive: Path, out: Path, now: datetime | None = None) -> dict[str, Any]:
    """Append the official outcomes (ice time by state, shots) of every recorded game that is now final and has none yet. Write-once, per game date."""
    now = now or utcnow()
    live, _ = LCR.read_archive(archive, now)
    todo = _games_in(out, "records") - _games_in(out, "outcomes")
    pl = S._latest_snapshot_per_game(live.get("players") or [])
    written: list[int] = []
    if len(pl) and todo:
        pl = pl[pd.to_numeric(pl["game_id"], errors="coerce").isin(todo) & (pd.to_numeric(pl["game_type"], errors="coerce") == 2)]
        cols = ["game_id", "player_id", "team_id", "toi_s", "toi_ev_s", "toi_pp_s", "toi_sh_s", "sog", "shifts_ok"]
        for day, grp in pl.groupby(pl["game_date"].astype(str)):
            rows = [{**{k: (None if pd.isna(v) else (v.item() if hasattr(v, "item") else v)) for k, v in zip(cols, rec, strict=True)}, "settled_at_utc": iso(now)}
                    for rec in grp.reindex(columns=cols).itertuples(index=False)]
            LCR.write_once(out, f"outcomes/dt={day}/outcomes_{now.strftime('%Y%m%dT%H%M%SZ')}.jsonl.gz", rows)
            written += sorted({int(r["game_id"]) for r in rows})
    try:
        inc = capture_incumbent(archive, out, now)
    except Exception as e:      # noqa: BLE001 - the supplementary comparator never blocks settlement
        inc = {"error": f"{type(e).__name__}: {str(e)[:160]}"}
    return {"games_with_outcomes_written": written, "pending": sorted(todo - set(written)), "incumbent_capture": inc, "guard": guard(out)}


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# scoring (the registered hypotheses)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def load_dir(out: Path, sub: str) -> pd.DataFrame:
    """All rows under ``out/sub``; each carries ``written_at_utc`` from the append-only manifest (a record can only have existed after its file was written)."""
    written: dict[str, str] = {}
    mp = out / "MANIFEST.jsonl"
    if mp.exists():
        for line in mp.read_text().splitlines():
            if line.strip():
                e = json.loads(line)
                written[e["path"]] = e["written_at_utc"]
    rows: list[dict[str, Any]] = []
    if (out / sub).exists():
        for p in sorted((out / sub).rglob("*.jsonl.gz")):
            rel = p.relative_to(out).as_posix()
            with gzip.open(p, "rt", encoding="utf-8") as f:
                rows += [{**json.loads(line), "written_at_utc": written.get(rel)} for line in f if line.strip()]
    return pd.DataFrame(rows)


def incumbent_toi(pf_dir: Path) -> pd.DataFrame:
    """PLAYER_SIM_V1 ``toi_minutes``: the last forecast archived before the drop, per (game, player) -- the same rule as the LC shots comparator."""
    rows = []
    base = Path(pf_dir) / "forecasts" / "nhl"
    for p in sorted(base.rglob("*.jsonl.gz")) if base.exists() else []:
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                if r.get("family") == "toi_minutes" and r.get("model_id") == "PLAYER_SIM_V1" and r.get("archived_utc") and r.get("game_start_utc") and r["archived_utc"] < r["game_start_utc"]:
                    rows.append({"game_id": int(r["game_id"]), "player_id": int(r["entity_id"]), "inc_toi": float(r["mean"]), "archived_utc": r["archived_utc"]})
    if not rows:
        return pd.DataFrame(columns=["game_id", "player_id", "inc_toi"])
    d = pd.DataFrame(rows).sort_values("archived_utc")
    return d.groupby(["game_id", "player_id"], as_index=False).tail(1).drop(columns="archived_utc")


def _ratio_ci(a: np.ndarray, b: np.ndarray, game: np.ndarray, n_boot: int = N_BOOT) -> dict[str, float]:
    """Relative change of mean squared error mean(a)/mean(b) - 1 with a game-clustered bootstrap (ratio of cluster sums)."""
    _, inv = np.unique(game, return_inverse=True)
    sa, sb = np.bincount(inv, weights=a), np.bincount(inv, weights=b)
    idx = np.random.default_rng(SEED).integers(0, len(sa), size=(n_boot, len(sa)))
    r = sa[idx].sum(1) / sb[idx].sum(1) - 1.0
    return {"relative_change": float(a.mean() / b.mean() - 1.0), "lo95": float(np.quantile(r, 0.025)), "hi95": float(np.quantile(r, 0.975)), "n": int(len(a)), "n_games": int(len(sa))}


def paired_sample(rec: pd.DataFrame, outc: pd.DataFrame, inc: pd.DataFrame, frozen_model_sha: str | None = None) -> pd.DataFrame:
    """Pregame records of the frozen model, joined to the official outcome (he played) and to the comparators, in the registered order."""
    if not len(rec) or not len(outc):
        return pd.DataFrame()
    pre = LCR.eligible_records(rec, frozen_model_sha)[0]       # pregame by its own clock AND written (per the manifest) before the drop, by the frozen model
    pre = pre.drop_duplicates(["game_id", "player_id"])
    if not len(pre):
        return pd.DataFrame()
    pred = pd.json_normalize(pre["predictions"].tolist()).add_prefix("p_")
    inp = pd.json_normalize(pre["inputs"].tolist())[["incumbent_pp_min"]].rename(columns={"incumbent_pp_min": "inc_pp"})
    base = pd.concat([pre.reset_index(drop=True)[["game_id", "player_id", "game_start_utc"]], pred, inp], axis=1)
    o = outc.drop_duplicates(["game_id", "player_id"])[["game_id", "player_id", "toi_s", "toi_pp_s", "shifts_ok"]]
    m = base.merge(o, on=["game_id", "player_id"], how="inner")
    m = m[pd.to_numeric(m["toi_s"], errors="coerce") > 0].merge(inc, on=["game_id", "player_id"], how="inner")
    return m.sort_values(["game_start_utc", "game_id", "player_id"], kind="mergesort").reset_index(drop=True)


def score_frame(m: pd.DataFrame, limit: int | None = None, with_pass: bool = False) -> dict[str, Any]:
    """The registered hypotheses on the first ``limit`` paired player-games (all of them when None). ``with_pass`` adds the registered pass flags: only a decision or final look carries them."""
    if limit is not None:
        m = m.iloc[:limit]
    out: dict[str, Any] = {"n_paired": int(len(m))}
    if len(m):
        out["sample_sha256"] = hashlib.sha256("\n".join(f"{g}|{p}" for g, p in zip(m["game_id"], m["player_id"], strict=True)).encode()).hexdigest()
        out["last_key"] = {"game_start_utc": str(m["game_start_utc"].iloc[-1]), "game_id": int(m["game_id"].iloc[-1]), "player_id": int(m["player_id"].iloc[-1])}
    if len(m) < 200:
        out["verdict"] = f"INCONCLUSIVE AT n={len(m)}"
        return out
    need = ["toi_s", "inc_toi", "p_M0_toi_min", "p_M1_toi_min"]
    finite = np.isfinite(m[need].apply(pd.to_numeric, errors="coerce").to_numpy(float)).all(axis=1)
    out["n_nonfinite_dropped"] = int((~finite).sum())
    m = m[finite]
    game = m["game_id"].to_numpy()
    y = pd.to_numeric(m["toi_s"]).to_numpy(float) / 60.0
    inc, m0, m1 = (m[c].to_numpy(float) for c in ("inc_toi", "p_M0_toi_min", "p_M1_toi_min"))
    sq = lambda p, t: (np.asarray(p, float) - t) ** 2  # noqa: E731
    out["toi"] = {"mse_incumbent": float(sq(inc, y).mean()), "mse_M0": float(sq(m0, y).mean()), "mse_M1": float(sq(m1, y).mean()), "bias_incumbent": float((inc - y).mean()),
                  "bias_M0": float((m0 - y).mean()), "bias_M1": float((m1 - y).mean())}
    h: dict[str, Any] = {"H1": _ratio_ci(sq(m0, y), sq(inc, y), game), "H3": _ratio_ci(sq(m1, y), sq(m0, y), game)}
    ypp = pd.to_numeric(m["toi_pp_s"], errors="coerce").to_numpy(float) / 60.0
    inc_pp = pd.to_numeric(m["inc_pp"], errors="coerce").to_numpy(float)
    pp0 = pd.to_numeric(m["p_pp_min"], errors="coerce").to_numpy(float)
    ok = m["shifts_ok"].fillna(False).astype(bool).to_numpy() & np.isfinite(inc_pp) & np.isfinite(ypp) & np.isfinite(pp0)
    if ok.sum() >= MIN_PP_PAIRS:
        h["H2"] = _ratio_ci(sq(pp0, ypp)[ok], sq(inc_pp, ypp)[ok], game[ok])
        out["pp"] = {"mse_incumbent": float(sq(inc_pp, ypp)[ok].mean()), "mse_M0": float(sq(pp0, ypp)[ok].mean()), "bias_incumbent": float((inc_pp - ypp)[ok].mean()), "bias_M0": float((pp0 - ypp)[ok].mean())}
    else:
        h["H2"] = {"n": int(ok.sum()), "verdict": f"INCONCLUSIVE AT n={int(ok.sum())} (fewer than {MIN_PP_PAIRS:,} pairs with a captured incumbent power-play value)"}
    for k, v in h.items():
        if "hi95" in v:
            v["required_relative_change"] = REQUIRED[k]
            if with_pass:
                v["pass"] = bool(v["hi95"] < REQUIRED[k])
    out["hypotheses"] = h
    out["verdict"] = "; ".join(f"{k}: {'PASS' if v.get('pass') else v.get('verdict', 'NOT MET')}" for k, v in sorted(h.items())) if with_pass else "descriptive (no decision at this sample)"
    return out


def registered_verdicts(looks: dict[int, dict[str, Any]]) -> dict[str, str]:
    """Per hypothesis, as registered: supported at the decision look; otherwise carried to the final look; otherwise not supported. Nothing is said before the decision look."""
    out = {}
    for k in sorted(REQUIRED):
        d, f = looks.get(DECISION_LOOK, {}).get("hypotheses", {}).get(k), looks.get(FINAL_LOOK, {}).get("hypotheses", {}).get(k)
        if d is None:
            out[k] = "OPEN (decision look not yet reached)"
        elif d.get("pass"):
            out[k] = f"SUPPORTED at the decision look ({DECISION_LOOK:,})"
        elif f is None:
            out[k] = f"NOT MET at the decision look ({d.get('verdict') or 'upper bound not below the requirement'}); carried to the final look ({FINAL_LOOK:,})"
        else:
            out[k] = f"SUPPORTED at the final look ({FINAL_LOOK:,})" if f.get("pass") else f"NOT SUPPORTED at the final look ({FINAL_LOOK:,})"
    return out


def look_deferral(m: pd.DataFrame, n: int, rec: pd.DataFrame, outc: pd.DataFrame, now: datetime) -> str | None:
    """A look is computed only once every recorded game starting at or before its N-th pair has its outcome (games more than 7 days old that never settled are ignored), so the first N pairs
    are final and the look can be recomputed from the finished data. Returns the reason to wait, or None."""
    if len(m) < n:
        return f"only {len(m):,} paired"
    t_n = parse_iso(str(m["game_start_utc"].iloc[n - 1]))
    pre = rec[rec["pregame"].astype(bool)].drop_duplicates("game_id")
    settled = set(outc["game_id"]) if len(outc) else set()
    waiting = [int(g) for g, st in zip(pre["game_id"], pre["game_start_utc"], strict=True) if g not in settled and parse_iso(st) <= t_n and now - parse_iso(st) < timedelta(days=7)]
    return f"{len(waiting)} recorded game(s) up to the look's last pair have no outcome yet" if waiting else None


def supplementary_h2(rec: pd.DataFrame, outc: pd.DataFrame, incd: pd.DataFrame, frozen_model_sha: str | None = None) -> dict[str, Any]:
    """SUPPLEMENTARY, descriptive, clearly NOT the registered H2: power-play minutes of M0 vs the incumbent's newest expected power-play minutes that existed before the drop (``capture_incumbent``).
    Reports paired coverage, why candidates are missing, and how the covered players differ from the uncovered ones (selection)."""
    if not len(rec) or not len(outc) or not len(incd):
        return {"label": "supplementary (not the registered H2)", "n_dressed": 0, "verdict": "no data yet"}
    pre = LCR.eligible_records(rec, frozen_model_sha)[0].drop_duplicates(["game_id", "player_id"])
    pred = pd.json_normalize(pre["predictions"].tolist()).add_prefix("p_")
    inp = pd.json_normalize(pre["inputs"].tolist())[["incumbent_pp_min"]].rename(columns={"incumbent_pp_min": "reg_pp"})
    base = pd.concat([pre.reset_index(drop=True)[["game_id", "player_id", "pos"]], pred, inp], axis=1)
    o = outc.drop_duplicates(["game_id", "player_id"])[["game_id", "player_id", "toi_s", "toi_pp_s", "shifts_ok"]]
    d = base.merge(o, on=["game_id", "player_id"], how="inner")
    captured_games = set(incd["game_id"].astype(int))
    d = d[(pd.to_numeric(d["toi_s"], errors="coerce") > 0) & d["game_id"].astype(int).isin(captured_games)].merge(
        incd.drop_duplicates(["game_id", "player_id"])[["game_id", "player_id", "inc_toi_min", "inc_pp_min", "incumbent_lead_min"]], on=["game_id", "player_id"], how="left")
    if not len(d):
        return {"label": "supplementary (not the registered H2)", "n_dressed": 0, "verdict": "no settled games with a captured comparator yet"}
    d["has_row"] = d["inc_toi_min"].notna()
    d["has_pp"] = pd.to_numeric(d["inc_pp_min"], errors="coerce").notna()
    ypp = pd.to_numeric(d["toi_pp_s"], errors="coerce") / 60.0
    ok = d["has_pp"] & d["shifts_ok"].fillna(False).astype(bool) & ypp.notna() & pd.to_numeric(d["p_pp_min"], errors="coerce").notna()
    out: dict[str, Any] = {"label": "supplementary (not the registered H2)", "n_dressed": int(len(d)), "n_with_incumbent_row": int(d["has_row"].sum()), "n_with_incumbent_pp": int(d["has_pp"].sum()),
                           "n_pairs": int(ok.sum()), "coverage_of_dressed": round(float(ok.sum()) / len(d), 4), "n_games": int(d["game_id"].nunique()),
                           "registered_captured_coverage_of_dressed": round(float((d["reg_pp"].notna() & d["shifts_ok"].fillna(False).astype(bool) & ypp.notna() & pd.to_numeric(d["p_pp_min"], errors="coerce").notna()).mean()), 4),
                           "missing": {"no_incumbent_row": int((~d["has_row"]).sum()), "row_without_pp": int((d["has_row"] & ~d["has_pp"]).sum()), "shifts_not_ok": int((d["has_pp"] & ~d["shifts_ok"].fillna(False).astype(bool)).sum())}}
    out["missing"]["other"] = int((~ok).sum()) - sum(out["missing"].values())
    rl = (pd.to_datetime(pre["game_start_utc"], utc=True, errors="coerce") - pd.to_datetime(pre["predicted_at_utc"], utc=True, errors="coerce")).dt.total_seconds() / 60.0
    out["record_lead_min"] = {"median": float(rl.median()), "min": float(rl.min())}
    lead = pd.to_numeric(d.loc[d["has_pp"], "incumbent_lead_min"], errors="coerce").dropna()
    if len(lead):
        out["incumbent_lead_min"] = {"median": float(lead.median()), "min": float(lead.min()), "max": float(lead.max())}
    sel = {}
    for name, mask in (("covered", ok), ("not_covered", ~ok), ("never_priced", ~d["has_pp"])):
        g = d[mask]
        sel[name] = {"n": int(len(g)), "share_defense": None if not len(g) else round(float((g["pos"] == "D").mean()), 3),
                     "mean_M0_toi_min": None if not len(g) else round(float(pd.to_numeric(g["p_M0_toi_min"], errors="coerce").mean()), 2),
                     "mean_actual_toi_min": None if not len(g) else round(float(pd.to_numeric(g["toi_s"], errors="coerce").mean() / 60.0), 2),
                     "mean_actual_pp_min": None if not len(g) else round(float((pd.to_numeric(g["toi_pp_s"], errors="coerce") / 60.0).mean()), 3)}
    out["selection"] = sel
    out["lead_note"] = "the incumbent row can be written seconds before the drop (warm-up and confirmed lines visible to it); the minutes records are written ~10 hours before (see record_lead_min): the comparison favours the incumbent"
    if ok.sum() >= 200:
        y, inc, m0 = ypp[ok].to_numpy(float), pd.to_numeric(d.loc[ok, "inc_pp_min"]).to_numpy(float), pd.to_numeric(d.loc[ok, "p_pp_min"]).to_numpy(float)
        out["relative_change_M0_vs_incumbent"] = _ratio_ci((m0 - y) ** 2, (inc - y) ** 2, d.loc[ok, "game_id"].to_numpy())
        out["mse"] = {"incumbent": float(((inc - y) ** 2).mean()), "M0": float(((m0 - y) ** 2).mean()), "bias_incumbent": float((inc - y).mean()), "bias_M0": float((m0 - y).mean())}
    else:
        out["verdict"] = f"INCONCLUSIVE AT n={int(ok.sum())}"
    return out


def render(res: dict[str, Any], looks: dict[int, dict[str, Any]], activation: dict[str, Any] | None, counts: dict[str, int], coverage: dict[str, Any] | None = None,
           supp: dict[str, Any] | None = None) -> str:
    L = ["# player-minutes-1.0 scoreboard (research only)", "", f"Registration: `{REGISTRATION}`. Activation: {activation.get('activation_utc') if activation else 'not yet'}.", "",
         f"Records: {counts['records']:,} (counting: {counts['eligible']:,}) · outcomes: {counts['outcomes']:,} · paired with an incumbent TOI forecast: {res.get('n_paired', 0):,}"]
    if counts.get("dressed"):
        L.append(f"Settled candidates {counts['settled_candidates']:,} · played {counts['dressed']:,} · of those with the incumbent's pregame TOI forecast {counts['paired']:,} ({counts['paired'] / counts['dressed']:.0%}) · with a captured power-play value {counts['paired_with_captured_pp']:,}")
    if coverage and coverage.get("activated"):
        L.append(f"Collection: games since activation {coverage['games_since_activation']} · recorded {coverage['recorded']} · missed {len(coverage['missed'])} · pending {coverage['pending']} · "
                 f"coverage of started games {coverage['coverage_of_started']} · median lead {coverage['median_lead_min']} min" + (f" · missed: {', '.join(coverage['missed'])}" if coverage["missed"] else ""))
    L.append("")
    if "hypotheses" in res:
        L += ["Cumulative, **descriptive only** (no decision is taken from it):", "", "| hypothesis | relative change in squared error | 95% interval | n |", "|---|---|---|---|"]
        for k, v in sorted(res["hypotheses"].items()):
            L.append(f"| {k} | {v['relative_change']:+.2%} | {v['lo95']:+.2%} … {v['hi95']:+.2%} | {v['n']:,} |" if "hi95" in v else f"| {k} | | | {v['verdict']} |")
        t = res["toi"]
        L += ["", f"Total ice time MSE: incumbent {t['mse_incumbent']:.3f} · M0 {t['mse_M0']:.3f} · M1 {t['mse_M1']:.3f}; bias (pred − actual): {t['bias_incumbent']:+.3f} / {t['bias_M0']:+.3f} / {t['bias_M1']:+.3f} min"]
    else:
        L.append(f"Not enough paired data yet: {res.get('verdict')}.")
    L += ["", "Registered verdicts (decision look 30,000 / final look 60,000): " + "; ".join(f"{k}: {v}" for k, v in registered_verdicts(looks).items())]
    if looks:
        L.append("Looks computed (each once, never rewritten): " + ", ".join(f"{n:,}{' (descriptive)' if n not in (DECISION_LOOK, FINAL_LOOK) else ''}" for n in sorted(looks)))
    if supp and supp.get("n_dressed"):
        sel = supp["selection"]
        L += ["", "**Supplementary power-play comparison (not the registered H2; descriptive; comparator = the incumbent's newest expected power-play minutes that existed before the drop)**", "",
              f"Dressed players in games with a captured comparator: {supp['n_dressed']:,} · with an incumbent row {supp['n_with_incumbent_row']:,} · with a power-play value {supp['n_with_incumbent_pp']:,} · paired {supp['n_pairs']:,} "
              f"({supp['coverage_of_dressed']:.0%} of dressed; the registered record-time comparator covers {supp['registered_captured_coverage_of_dressed']:.0%}) · missing: {supp['missing']}"]
        if "relative_change_M0_vs_incumbent" in supp:
            r = supp["relative_change_M0_vs_incumbent"]
            L.append(f"M0 vs incumbent power-play minutes: {r['relative_change']:+.2%} in squared error (95% interval {r['lo95']:+.2%} … {r['hi95']:+.2%}, n={r['n']:,}); no pass/fail is attached to it.")
        else:
            L.append(supp.get("verdict", ""))
        if "record_lead_min" in supp:
            L.append(f"Information asymmetry: the incumbent value was written a median {supp.get('incumbent_lead_min', {}).get('median', float('nan')):.0f} min before the drop; the minutes records a median {supp['record_lead_min']['median']:.0f} min before it (the comparison favours the incumbent).")
        L.append(f"Selection: covered n={sel['covered']['n']:,} (defense {sel['covered']['share_defense']}, mean M0 TOI {sel['covered']['mean_M0_toi_min']}, actual PP {sel['covered']['mean_actual_pp_min']}) vs "
                 f"not covered n={sel['not_covered']['n']:,} (defense {sel['not_covered']['share_defense']}, mean M0 TOI {sel['not_covered']['mean_M0_toi_min']}, actual PP {sel['not_covered']['mean_actual_pp_min']}).")
    L += ["", "Research only: nothing here is published, priced or routed; promotion of any ice-time model needs the owner's explicit approval."]
    return "\n".join(L) + "\n"


def coverage_counts(eligible: pd.DataFrame, outc: pd.DataFrame, m: pd.DataFrame) -> dict[str, int]:
    """Display only: how many counting records belong to a settled game, how many of those players played, and how many of those have the comparators the hypotheses need."""
    if not len(eligible) or not len(outc):
        return {"settled_candidates": 0, "dressed": 0, "paired": int(len(m)), "paired_with_captured_pp": 0}
    settled = eligible[eligible["game_id"].isin(set(outc["game_id"]))].drop_duplicates(["game_id", "player_id"])
    played = outc[pd.to_numeric(outc["toi_s"], errors="coerce") > 0].drop_duplicates(["game_id", "player_id"])
    dressed = settled.merge(played[["game_id", "player_id"]], on=["game_id", "player_id"])
    pp = int(pd.to_numeric(m["inc_pp"], errors="coerce").notna().sum()) if len(m) and "inc_pp" in m.columns else 0
    return {"settled_candidates": int(len(settled)), "dressed": int(len(dressed)), "paired": int(len(m)), "paired_with_captured_pp": pp}


def score(archive: Path, pf: Path, out: Path, now: datetime | None = None) -> dict[str, Any]:
    now = now or utcnow()
    rec, outc = load_dir(out, "records"), load_dir(out, "outcomes")
    act_p = out / "activation.json"
    activation = json.loads(act_p.read_text()) if act_p.exists() else None
    frozen = activation.get("model_sha256") if activation else None
    m = paired_sample(rec, outc, incumbent_toi(pf), frozen)
    eligible = LCR.eligible_records(rec, frozen)[0] if len(rec) else rec
    counts = {"records": int(len(rec)), "eligible": int(len(eligible)), "outcomes": int(len(outc))}
    counts.update(coverage_counts(eligible, outc, m))
    res = score_frame(m) if len(m) else {"n_paired": 0, "verdict": "INCONCLUSIVE AT n=0"}
    looks: dict[int, dict[str, Any]] = {}
    waiting: dict[int, str] = {}
    for n in LOOKS:
        p = out / "looks" / f"look_{n}.json"
        if p.exists():
            looks[n] = json.loads(p.read_text())
        elif len(m) >= n:
            why = look_deferral(m, n, rec, outc, now)
            if why:
                waiting[n] = why
                continue
            payload = {"look": n, "computed_utc": iso(now), "decision_look": n in (DECISION_LOOK, FINAL_LOOK), **score_frame(m, n, with_pass=n in (DECISION_LOOK, FINAL_LOOK))}
            if LCR.write_look(out, n, payload):
                looks[n] = payload
    try:
        coverage = LCR.coverage_audit(archive, out, rec, now)
    except Exception as e:      # noqa: BLE001 - a missing schedule view must not stop the scoreboard
        coverage = {"activated": False, "error": f"{type(e).__name__}: {str(e)[:120]}"}
    verdicts = registered_verdicts(looks)
    try:
        supp = supplementary_h2(rec, outc, load_dir(out, "incumbent"), frozen)
    except Exception as e:      # noqa: BLE001 - the supplementary block must never stop the registered scoreboard
        supp = {"label": "supplementary (not the registered H2)", "n_dressed": 0, "error": f"{type(e).__name__}: {str(e)[:160]}"}
    sb = out / "scoreboard"
    sb.mkdir(parents=True, exist_ok=True)
    (sb / "latest.json").write_text(json.dumps({"as_of_utc": iso(now), "supplementary_h2": supp, "cumulative_descriptive": res, "registered_verdicts": verdicts, "looks": sorted(looks), "looks_waiting": waiting, "counts": counts,
                                                "collection": {k: v for k, v in coverage.items() if k != "games"}}, indent=1, default=float))
    (sb / "latest.md").write_text(render(res, looks, activation, counts, coverage, supp))
    return {"result": res, "looks": sorted(looks), "looks_waiting": waiting, "verdicts": verdicts, "counts": counts, "guard": guard(out)}


def main(argv: list[str] | None = None) -> int:
    import argparse
    import subprocess

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.player_minutes_shadow")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("predict")
    p.add_argument("--archive", required=True)
    p.add_argument("--history", default="data/history")
    p.add_argument("--out", required=True)
    s = sub.add_parser("settle")
    s.add_argument("--archive", required=True)
    s.add_argument("--out", required=True)
    c = sub.add_parser("score")
    c.add_argument("--archive", required=True)
    c.add_argument("--pf", required=True)
    c.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "predict":
        try:
            commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
        except OSError:
            commit = ""
        rep = predict(Path(a.archive), Path(a.history), Path(a.out), code_commit=commit)
        print(json.dumps(rep, indent=1)[:2500])
        return 2 if rep["guard"] else (3 if rep["errors"] else 0)
    if a.cmd == "settle":
        rep = settle(Path(a.archive), Path(a.out))
        print(json.dumps(rep, indent=1)[:1500])
        return 2 if rep["guard"] else 0
    rep = score(Path(a.archive), Path(a.pf), Path(a.out))
    print((Path(a.out) / "scoreboard" / "latest.md").read_text())
    return 2 if rep["guard"] else 0


if __name__ == "__main__":
    sys.exit(main())
