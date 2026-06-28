from __future__ import annotations
import argparse, json
from services import TRIGGERS, run_all_calls

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--repeat', type=int, default=1)
    args = parser.parse_args()
    if args.repeat < 1 or args.repeat > 25: parser.error('--repeat must be between 1 and 25')
    runs = [run_all_calls() for _ in range(args.repeat)]
    print(json.dumps({'runs':runs,'calls_per_run':len(TRIGGERS),'expected_tracking_events':args.repeat*len(TRIGGERS)}, indent=2, sort_keys=True))
    return 0
if __name__ == '__main__': raise SystemExit(main())
