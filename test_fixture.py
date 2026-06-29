from __future__ import annotations

import importlib.util
from pathlib import Path

from app import create_app
from edge_cases import run_runnable_edge_cases
from integrations import run_integrations
from services import TRIGGERS, run_all_calls, run_trigger


def test_six_primary_call_sites_execute():
    results = run_all_calls()
    assert set(results) == set(TRIGGERS)
    assert len(results) == 6
    assert isinstance(results["summarize"], str)
    assert isinstance(results["classify"], str)
    assert results["extract"]["email"] == "maria.gomez@example.com"
    assert isinstance(results["moderate"], bool)
    assert len(results["embed"]) == 8
    assert isinstance(results["runtime-support"], str)


def test_individual_trigger_rejects_unknown_name():
    try:
        run_trigger("not-a-call")
    except ValueError as exc:
        assert "Unknown trigger" in str(exc)
    else:
        raise AssertionError("Expected ValueError")


def test_http_trigger_all_reports_expected_call_count():
    client = create_app().test_client()
    response = client.post("/trigger-all?repeat=3")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["ok"] is True
    assert payload["calls_per_run"] == 6
    assert payload["expected_calls"] == 18
    assert len(payload["runs"]) == 3


def test_http_individual_trigger():
    client = create_app().test_client()
    response = client.post("/trigger/summarize")
    assert response.status_code == 200
    assert response.get_json()["trigger"] == "summarize"


def test_all_runnable_edge_cases_execute():
    results = run_runnable_edge_cases()
    # EC01..EC20 are the runnable TRUE-positive edge cases (decoys excluded).
    assert len(results) == 20
    assert results["ec18"] == ("mock-response", "mock-response")
    assert results["ec10"] == ["mock-response", "mock-response"]


def test_all_integration_call_sites_execute():
    results = run_integrations()
    assert len(results) == 6
    assert isinstance(results["in01"], str)
    assert len(results["in05"]) == 8


def test_tracker_absent_until_reapplied():
    # The clean fixture ships WITHOUT the tracker; the scanner re-applies it.
    # If a run has already re-applied it, it must import and expose record_usage.
    tracker = Path("ai_spend_tracker.py")
    if not tracker.exists():
        return
    spec = importlib.util.spec_from_file_location("ai_spend_tracker", tracker)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert callable(module.record_usage)
