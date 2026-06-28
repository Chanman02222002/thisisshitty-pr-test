from __future__ import annotations
import importlib.util
from pathlib import Path
from app import create_app
from services import TRIGGERS, run_all_calls, run_trigger

def test_six_business_call_sites_execute():
    results = run_all_calls()
    assert set(results) == set(TRIGGERS)
    assert len(results) == 6
    assert isinstance(results['summarize'], str)
    assert results['classify'] in {'Hot','Warm','Cold'}
    assert results['extract']['email'] == 'maria.gomez@example.com'
    assert isinstance(results['moderate'], bool)
    assert len(results['embed']) == 8
    assert 'Runtime support reply' in results['runtime-support']

def test_individual_trigger_rejects_unknown_name():
    try: run_trigger('not-a-call')
    except ValueError as exc: assert 'Unknown trigger' in str(exc)
    else: raise AssertionError('Expected ValueError')

def test_http_trigger_all_reports_expected_event_count():
    client = create_app().test_client()
    response = client.post('/trigger-all?repeat=3')
    assert response.status_code == 200
    payload = response.get_json()
    assert payload['ok'] is True
    assert payload['calls_per_run'] == 6
    assert payload['expected_tracking_events'] == 18
    assert len(payload['runs']) == 3

def test_http_individual_trigger():
    client = create_app().test_client()
    response = client.post('/trigger/summarize')
    assert response.status_code == 200
    assert response.get_json()['trigger'] == 'summarize'

def test_generated_tracker_imports_when_aiapitest_pr_adds_it():
    tracker = Path('ai_spend_tracker.py')
    if not tracker.exists(): return
    spec = importlib.util.spec_from_file_location('ai_spend_tracker', tracker)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert callable(module.record_usage)
