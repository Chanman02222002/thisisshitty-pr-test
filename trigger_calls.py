from __future__ import annotations

import argparse
import json

from edge_cases import run_runnable_edge_cases
from integrations import run_integrations
from services import TRIGGERS, run_all_calls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeat", type=int, default=1)
    parser.add_argument("--include-edge-cases", action="store_true")
    args = parser.parse_args()
    if args.repeat < 1 or args.repeat > 25:
        parser.error("--repeat must be between 1 and 25")

    runs = [run_all_calls() for _ in range(args.repeat)]
    out = {
        "runs": runs,
        "calls_per_run": len(TRIGGERS),
        "expected_calls": args.repeat * len(TRIGGERS),
    }
    if args.include_edge_cases:
        out["edge_cases"] = run_runnable_edge_cases()
        out["integrations"] = run_integrations()
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
