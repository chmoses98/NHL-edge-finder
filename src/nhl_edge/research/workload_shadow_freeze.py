"""Freeze the comparator dispersions of the WORKLOAD_V1_LC prospective test (RESEARCH_ONLY).

The registration fits the NegBin dispersion of every non-Poisson comparator on the 2025 season, exactly as the original rule fitted it on the previous season. The
incumbent's expected shots and the exponentially weighted baseline are recomputed for 2025 with the retrospective harness (derived champion stand-in) and their
dispersions are written, once, to ``data/params/workload-lc-1.0.json`` together with the hashes of the frozen inputs. The file is registered in the integrity registry,
so changing it after activation fails CI.

    python -m nhl_edge.research.workload_shadow_freeze --history data/history --cache out/workload_v1_replication_cache --out data/params/workload-lc-1.0.json
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_experiment as X
from nhl_edge.research import workload_level_cal as LC
from nhl_edge.research import workload_replication as R
from nhl_edge.research import workload_shadow as S
from nhl_edge.research import workload_v1 as W
from nhl_edge.timeutil import iso, utcnow

VERSION = "workload-lc-1.0"


def freeze(history: Path, cache: Path, prereg: Path) -> dict:
    pre = json.loads(prereg.read_text())
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    derived = R.derive_wf(history, [2022, 2023, 2024, 2025])
    ctx = R.ReplicationCtx(history, cache, "derived", derived)
    c = W.fit_constants(ctx.sk, ctx.tg, ctx.data.goalies, S.TRAIN_SEASONS)
    m = X._sk_frames(ctx, [S.DISPERSION_SEASON], prm, c)[S.DISPERSION_SEASON]
    y = m["y_sog"].to_numpy()
    return {"version": VERSION, "authority": "RESEARCH_ONLY", "role": "SHADOW", "model_id": S.MODEL_ID,
            "train_seasons": S.TRAIN_SEASONS, "dispersion_season": S.DISPERSION_SEASON, "n_dispersion_rows": int(len(m)),
            "alpha_champion_nb": E.fit_nb_alpha(y, m["ch_sog"].to_numpy()), "alpha_baseline": E.fit_nb_alpha(y, m["base_sog"].to_numpy()),
            "alpha_workload_v1_raw": E.fit_nb_alpha(y, m["wl_sog"].to_numpy()),
            "level_calibration": {"half_life_days": LC.H_DAYS, "prior_shots": LC.K_SHOTS},
            "preregistration_sha256": hashlib.sha256(prereg.read_bytes()).hexdigest(), "constants": c.to_dict(),
            "registration": "docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md", "generated_at_utc": iso(utcnow())}


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.workload_shadow_freeze")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache")
    ap.add_argument("--prereg", default="docs/research/workload_v1/preregistration.json")
    ap.add_argument("--out", default="data/params/workload-lc-1.0.json")
    a = ap.parse_args(argv)
    out = Path(a.out)
    if out.exists():
        raise SystemExit(f"{out} exists: a frozen parameter file is never rewritten; create a new version instead")
    p = freeze(Path(a.history), Path(a.cache) / "derived", Path(a.prereg))
    out.write_text(json.dumps(p, indent=1, default=float) + "\n")
    print(json.dumps({k: v for k, v in p.items() if k != "constants"}, indent=1, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
