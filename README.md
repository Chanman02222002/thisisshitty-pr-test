# Beacon customer platform — backend

Service layer for the Beacon customer platform. Modules under `beacon/` back the
support, sales, marketing, search, analytics and moderation surfaces.

## Layout

| Path | Role |
| --- | --- |
| `beacon/llm/` | Provider client construction and the shared model registry. |
| `beacon/support/` | Support-desk automation (summaries, triage, agents, pipelines). |
| `beacon/sales/` | Revenue workflows (lead scoring, outreach). |
| `beacon/marketing/` | Content and copy generation. |
| `beacon/search/` | Embedding and indexing helpers. |
| `beacon/analytics/` | Report narration and insights. |
| `beacon/integrations/` | Anthropic, Gemini, Cohere, Bedrock, litellm, LangChain, Azure. |
| `beacon/ops/` | Batch and scheduled jobs. |
| `beacon/common/` | Shared data-access, HTTP, billing and scoring utilities. |
| `app.py` | Flask entry point. |
| `run_jobs.py` | Batch harness / warm-up runner. |

## Develop

```bash
pip install -r requirements.txt
pytest -q
python run_jobs.py
```

Provider SDKs are vendored under `vendor/` so the service layer runs in local
and CI environments without external credentials.
