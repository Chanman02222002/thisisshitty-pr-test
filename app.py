"""Flask entry point for the Beacon backend."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
for _p in (_ROOT / "vendor", _ROOT):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from flask import Flask, jsonify, request

from beacon.support.summaries import summarize_ticket as _svc0
from beacon.sales.scoring import score_lead as _svc1
from beacon.marketing.content import draft_blog_post as _svc2


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"ok": True})

    @app.post("/summarize_ticket")
    def _route_0():
        payload = request.get_json(silent=True) or {}
        text = payload.get("text", "")
        return jsonify({"result": _svc0(text)})

    @app.post("/score_lead")
    def _route_1():
        payload = request.get_json(silent=True) or {}
        text = payload.get("text", "")
        return jsonify({"result": _svc1(text)})

    @app.post("/draft_blog_post")
    def _route_2():
        payload = request.get_json(silent=True) or {}
        text = payload.get("text", "")
        return jsonify({"result": _svc2(text)})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
