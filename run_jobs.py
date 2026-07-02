"""Batch harness: warms up every service module and reports coverage."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
for _p in (_ROOT / "vendor", _ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import asyncio
import importlib
import inspect
import pkgutil


def _value_for(annotation):
    a = annotation if isinstance(annotation, str) else getattr(annotation, "__name__", str(annotation))
    if a == "str":
        return "sample text"
    if a.startswith("list"):
        return ["alpha", "beta"]
    if a.startswith("dict"):
        return {"event": "test"}
    if a == "bool":
        return True
    if a in ("int",):
        return 1
    if a in ("float",):
        return 0.5
    return _MISSING


_MISSING = object()


def _args_for(func):
    args = []
    for name, p in inspect.signature(func).parameters.items():
        if name == "self":
            continue
        if p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
            continue
        if p.default is not inspect.Parameter.empty:
            break
        val = _value_for(p.annotation)
        if val is _MISSING:
            return None
        args.append(val)
    return args


def _invoke(func):
    args = _args_for(func)
    if args is None:
        return None
    if inspect.iscoroutinefunction(func):
        return asyncio.run(func(*args))
    return func(*args)


def exercise():
    import beacon
    ran, failed = 0, []
    for info in pkgutil.walk_packages(beacon.__path__, "beacon."):
        module = importlib.import_module(info.name)
        for _n, obj in inspect.getmembers(module):
            if inspect.isfunction(obj) and obj.__module__ == info.name:
                try:
                    if _args_for(obj) is None:
                        continue
                    _invoke(obj)
                    ran += 1
                except Exception as exc:  # noqa: BLE001
                    failed.append(f"{info.name}.{obj.__name__}: {exc!r}")
            elif inspect.isclass(obj) and obj.__module__ == info.name:
                try:
                    instance = obj()
                except Exception:  # noqa: BLE001
                    continue
                for mname, method in inspect.getmembers(instance, inspect.ismethod):
                    if mname.startswith("_"):
                        continue
                    try:
                        if _args_for(method) is None:
                            continue
                        _invoke(method)
                        ran += 1
                    except Exception as exc:  # noqa: BLE001
                        failed.append(f"{info.name}.{obj.__name__}.{mname}: {exc!r}")
    return ran, failed


def main() -> int:
    ran, failed = exercise()
    print(f"exercised {ran} service callables")
    if failed:
        print(f"{len(failed)} callables failed:")
        for line in failed:
            print("  -", line)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
