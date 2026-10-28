"""Runs one real production instant through a source tree and dumps the normalised published documents (slates, predictions*) so two trees (e.g. main vs a branch, or default vs an approved registry) can be compared byte for byte.

    PYTHONPATH=src python scripts/team_minutes_golden.py 2026-10-24T16:14:03Z <tag> 300 [approved]

See scripts/team_minutes_replay.py for the scratch paths."""
# ruff: noqa: E701, E702, E401, E402
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

os.environ["NHL_EDGE_PLAYER_SHADOW"] = "1"; os.environ["NHL_EDGE_V2_SHADOW"] = "1"
from nhl_edge.archive.ledger import Ledger
from nhl_edge.workflows.simulate import run_simulate

inst, tag, n_sims = sys.argv[1], sys.argv[2], int(sys.argv[3])
if len(sys.argv) > 4 and sys.argv[4] == "approved":
    from nhl_edge import projection_registry as PR
    tmp = Path("/tmp/claude-0/tm/registry_approved.json")
    tmp.write_text(json.dumps({"schema": "projection-registry-1", "targets": {"player_team_minutes": {"published_model": "team-minutes-1.0", "candidate": "team-minutes-1.0",
        "approval": {"approved_by": "contract-check", "approved_at_utc": "2026-10-26T00:00:00Z", "evidence": "docs/research/team_minutes/GO_NO_GO.md"}}}}))
    PR.REGISTRY_PATH = tmp
SRC = Path("/tmp/claude-0/arch"); DATA = Path("/home/user/wt-pm/data"); W = Path("/tmp/claude-0/tm/golden") / tag
if W.exists(): shutil.rmtree(W)
W.mkdir(parents=True)
for e in SRC.iterdir():
    if e.name != ".git": subprocess.run(["cp", "-al", str(e), str(W / e.name)], check=True)
now = datetime.fromisoformat(inst.replace("Z", "+00:00"))
t0 = time.time(); rc = run_simulate(W, DATA, date=None, n_sims=n_sims, now=now); dt = time.time() - t0
led = Ledger(W)
drop = ("prediction_id", "_run_id", "run_id", "input_snapshot_ids", "generated_at_utc")
def norm(o):
    if isinstance(o, dict): return {k: norm(v) for k, v in o.items() if k not in drop}
    if isinstance(o, list): return [norm(v) for v in o]
    return o
out = {}
for kind in ("predictions", "predictions_v2", "predictions_player", "thesis_games", "thesis_decisions", "evaluations_player"):
    rows = [norm(r) for r in led.iter_rows(kind) if r.get("_observed_at_utc") == inst and not str(r.get("_run_id", "")).isdigit()]
    out[kind] = sorted(rows, key=lambda r: json.dumps(r, sort_keys=True, default=str))
out["slate"] = norm(json.loads((W / "slates" / "latest" / "slate.json").read_text()))
out["packet"] = norm(json.loads((W / "slates" / "latest" / "packet.json").read_text()))
out["slate_md"] = (W / "slates" / "latest" / "slate.md").read_text()
Path(f"/tmp/claude-0/tm/golden_{tag}.json").write_text(json.dumps(out, sort_keys=True, default=str))
print(json.dumps({"tag": tag, "rc": rc, "seconds": round(dt, 1), "counts": {k: len(v) for k, v in out.items() if isinstance(v, list)}}))
