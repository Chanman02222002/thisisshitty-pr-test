import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for _p in (ROOT / "vendor", ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
