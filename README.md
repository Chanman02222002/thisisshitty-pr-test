# AIAPITEST scanner fixture

A deliberately hard, **runnable** test repo for the AI API / cost scanner.

The scanner's job on this repo is to:

1. **Detect every AI model call site** across providers and coding styles.
2. **Ignore the decoys** (things that look like model calls but are not).
3. **Propose cheaper-model savings** where appropriate.
4. **(Re)apply the usage tracker** — `ai_spend_tracker.py` plus a `record_usage(...)`
   call after each detected site.

This repo ships in a **clean, pre-scan state**: there is no `ai_spend_tracker.py`
and no tracking instrumentation. The live tracking links (dashboard URL + client
key) were removed on purpose so the scanner re-applies them.

## Layout

| File | Role |
| --- | --- |
| `services.py` | 6 **primary** call sites — the plain, must-always-detect baseline. |
| `edge_cases.py` | 20 hard TRUE-positive cases (`EC01`–`EC20`) + 5 decoys (`EC21`–`EC25`). |
| `integrations.py` | 6 non-OpenAI / wrapper-library call sites (`IN01`–`IN06`). |
| `fake_ai.py` | Offline mock SDKs (OpenAI/Anthropic/Gemini/litellm/LangChain) so it all runs with no keys. |
| `app.py` | Flask wrapper to trigger the primary calls over HTTP. |
| `trigger_calls.py` | CLI runner (`--include-edge-cases` to exercise everything). |
| `test_fixture.py` | pytest suite (also runs in CI). |
| `SCANNER_TRAINING_CONTEXT.md` | **Ground-truth labels** — feed this to the scanner when training/evaluating. |

## Run it

```bash
pip install -r requirements.txt
pytest -q
python trigger_calls.py --include-edge-cases
```

Everything is mock-only; no network calls leave the process.

## Ground truth

Total detectable AI call sites: **33** (6 primary + 21 edge + 6 integrations).
Decoys that must NOT be flagged: **5**. Full per-site labels, difficulty, and
expected savings are in [`SCANNER_TRAINING_CONTEXT.md`](./SCANNER_TRAINING_CONTEXT.md).
