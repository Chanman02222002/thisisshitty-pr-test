# Scanner training context — ground truth

Feed this file to the AI API / cost scanner as context when training or
evaluating it against this repo. It is the **answer key**: every AI model call
site, every decoy, the model each site uses, why each case is hard, and the
cheaper model the scanner should propose.

Do not commit live tracking secrets here. The scanner re-applies the tracker
(`ai_spend_tracker.py`) and its `record_usage(...)` instrumentation; the
dashboard URL and client key belong in environment variables
(`AI_SPEND_API_URL`, `AI_SPEND_CLIENT_KEY`), not in source.

## Scoring summary

- **True call sites to detect: 33** — 6 primary + 21 edge + 6 integrations.
- **Decoys that must NOT be flagged: 5.**
- A perfect run flags all 33, none of the 5 decoys, proposes the savings below,
  and re-applies tracking once per detected site.

## What counts as a detection

A "call site" is a single runtime invocation of a model endpoint:
`*.chat.completions.create`, `*.responses.create`, `*.moderations.create`,
`*.embeddings.create`, `*.batches.create`, Anthropic `messages.create`,
Gemini `generate_content`, `litellm.completion`/`embedding`, LangChain
`ChatOpenAI(...).invoke`, and legacy `openai.ChatCompletion.create`.
`model=` may be a literal, a name, a dict/index, an f-string, an env lookup, a
ternary, `**kwargs`, an attribute (`self.model`), or absent (batch).

## Primary call sites — `services.py` (6, all easy)

| id | function | api surface | model expr | resolved | suggest cheaper |
| --- | --- | --- | --- | --- | --- |
| P1 | `summarize_support_ticket` | chat.completions.create | `"gpt-4"` | gpt-4 | gpt-4o-mini |
| P2 | `classify_sales_lead` | chat.completions.create | `"gpt-4-turbo"` | gpt-4-turbo | gpt-4o-mini |
| P3 | `extract_contact_json` | chat.completions.create | `"gpt-4o"` | gpt-4o | gpt-4o-mini |
| P4 | `moderate_customer_message` | moderations.create | `"omni-moderation-latest"` | omni-moderation-latest | (none — moderation) |
| P5 | `embed_knowledge_text` | embeddings.create | `"text-embedding-3-large"` | text-embedding-3-large | text-embedding-3-small |
| P6 | `runtime_support_reply` | responses.create | `os.getenv("SUPPORT_MODEL", "gpt-4o")` | gpt-4o (default) | gpt-4o-mini |

## Edge cases — `edge_cases.py` (21 true sites, EC01–EC20)

| id | function | model expr | resolved | difficulty | why hard |
| --- | --- | --- | --- | --- | --- |
| EC01 | `ec01_model_from_constant` | `DEFAULT_MODEL` | gpt-4 | med | model is a module constant |
| EC02 | `ec02_model_from_dict` | `MODELS[tier]` | gpt-4o-mini / gpt-4o | med | dict lookup, tier is a param |
| EC03 | `ec03_model_from_fstring` | `f"gpt-4o-{variant}"` | gpt-4o-* | med | name built at runtime |
| EC04 | `ec04_model_from_env` | `os.getenv("EC04_MODEL", "gpt-4-turbo")` | gpt-4-turbo | med | env-driven, default literal |
| EC05 | `ec05_aliased_client` | `"gpt-4o"` | gpt-4o | med | client imported as `LLM`, built locally |
| EC06 | `ec06_client_built_inside_function` | `"gpt-3.5-turbo"` | gpt-3.5-turbo | med | client constructed in body |
| EC07 | `_llm_helper` (called by `ec07_call_via_helper`) | `model` param | gpt-4o (from caller) | hard | call in generic helper; model flows in |
| EC08 | `ec08_async_completion` | `"gpt-4o"` | gpt-4o | med | `await async_client...` |
| EC09 | `ec09_streaming` | `"gpt-4o-mini"` | gpt-4o-mini | med | `stream=True`, iterated |
| EC10 | `ec10_call_in_comprehension` | `"gpt-4o-mini"` | gpt-4o-mini | hard | inside a list comprehension |
| EC11 | `ec11_call_in_lambda` | `"gpt-4o-mini"` | gpt-4o-mini | hard | inside a lambda |
| EC12 | `ec12_kwargs_spread` | `params["model"]` via `**params` | gpt-4o | hard | model hidden in spread dict |
| EC13 | `ec13_factory_chain` | `"gpt-4o"` | gpt-4o | hard | chained off `_get_client()` return |
| EC14 | `ec14_batch_api` | (no model kwarg) | n/a | hard | batches.create, model absent |
| EC15 | `ec15_legacy_v0` | `"gpt-3.5-turbo"` | gpt-3.5-turbo | med | legacy `ChatCompletion.create` |
| EC16 | `ec16_decorator_wrapped` | `"gpt-4o"` | gpt-4o | med | call inside decorated fn |
| EC17 | `ec17_weird_formatting` | `"gpt-4o-mini"` | gpt-4o-mini | hard | minified one-liner, `;` |
| EC18 | `ec18_two_calls_one_line` (×2) | `"gpt-4o"` and `"gpt-3.5-turbo"` | both | hard | two calls on one physical line |
| EC19 | `ec19_ternary_model` | `"gpt-4o" if urgent else "gpt-4o-mini"` | both | hard | ternary model selection |
| EC20 | `SupportAgent.reply` | `self.model` | gpt-4o | hard | model is an instance attribute |

## Integrations — `integrations.py` (6, IN01–IN06)

| id | function | provider | api surface | resolved | suggest cheaper |
| --- | --- | --- | --- | --- | --- |
| IN01 | `in01_anthropic_messages` | Anthropic | messages.create | claude-3-opus | claude-3.5-sonnet / claude-3-haiku |
| IN02 | `in02_google_gemini` | Google | GenerativeModel().generate_content | gemini-1.5-pro | gemini-1.5-flash |
| IN03 | `in03_litellm_completion` | litellm | completion | gpt-4o | gpt-4o-mini |
| IN04 | `in04_langchain_invoke` | LangChain | ChatOpenAI().invoke | gpt-4o | gpt-4o-mini |
| IN05 | `in05_litellm_embedding` | litellm | embedding | text-embedding-3-small | (already cheap) |
| IN06 | `in06_legacy_module_call` | OpenAI v0 | openai.ChatCompletion.create | gpt-3.5-turbo | gpt-4o-mini |

## Decoys — must NOT be flagged (5)

| id | function | trap |
| --- | --- | --- |
| EC21 | `ec21_commented_out` | a fully commented-out `create(...)` call |
| EC22 | `ec22_model_name_in_text` | `gpt-4o` / `claude-3-opus` only appear in strings/docstrings |
| EC23 | `ec23_non_ai_create` | `db.records.create(model=...)` and `db.embeddings.create(...)` are DB ops |
| EC24 | `ec24_unrelated_model_key` | a dict whose `"model"` key is a truck (`f-150`), not an LLM |
| EC25 | `ec25_plain_webhook` | `http_session.post(...)` to a non-AI endpoint |

## Expected tracking re-application

For each of the 33 true sites the scanner should insert a tracker call
immediately after the response is produced, e.g.:

```python
response = client.chat.completions.create(model="gpt-4", messages=...)
record_usage("services.py:<line>", response, baseline_model="gpt-4")  # <- re-applied
```

and (re)create `ai_spend_tracker.py` exposing a callable `record_usage` that
logs one JSON line per call (model, token counts, actual vs. baseline cost,
savings) and optionally POSTs to `AI_SPEND_API_URL`. Secrets come from env;
none should be hard-coded.

## Machine-readable ground truth

```json
{
  "true_call_sites": 33,
  "decoys": 5,
  "sites": [
    {"id": "P1", "file": "services.py", "function": "summarize_support_ticket", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4", "model_static": true, "difficulty": "easy", "suggest": "gpt-4o-mini"},
    {"id": "P2", "file": "services.py", "function": "classify_sales_lead", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4-turbo", "model_static": true, "difficulty": "easy", "suggest": "gpt-4o-mini"},
    {"id": "P3", "file": "services.py", "function": "extract_contact_json", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": true, "difficulty": "easy", "suggest": "gpt-4o-mini"},
    {"id": "P4", "file": "services.py", "function": "moderate_customer_message", "provider": "openai", "api": "moderations.create", "model": "omni-moderation-latest", "model_static": true, "difficulty": "easy", "suggest": null},
    {"id": "P5", "file": "services.py", "function": "embed_knowledge_text", "provider": "openai", "api": "embeddings.create", "model": "text-embedding-3-large", "model_static": true, "difficulty": "easy", "suggest": "text-embedding-3-small"},
    {"id": "P6", "file": "services.py", "function": "runtime_support_reply", "provider": "openai", "api": "responses.create", "model": "gpt-4o", "model_static": false, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC01", "file": "edge_cases.py", "function": "ec01_model_from_constant", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4", "model_static": false, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC02", "file": "edge_cases.py", "function": "ec02_model_from_dict", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o-mini|gpt-4o", "model_static": false, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC03", "file": "edge_cases.py", "function": "ec03_model_from_fstring", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o-{variant}", "model_static": false, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC04", "file": "edge_cases.py", "function": "ec04_model_from_env", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4-turbo", "model_static": false, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC05", "file": "edge_cases.py", "function": "ec05_aliased_client", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC06", "file": "edge_cases.py", "function": "ec06_client_built_inside_function", "provider": "openai", "api": "chat.completions.create", "model": "gpt-3.5-turbo", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC07", "file": "edge_cases.py", "function": "_llm_helper", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": false, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "EC08", "file": "edge_cases.py", "function": "ec08_async_completion", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC09", "file": "edge_cases.py", "function": "ec09_streaming", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o-mini", "model_static": true, "difficulty": "medium", "suggest": null},
    {"id": "EC10", "file": "edge_cases.py", "function": "ec10_call_in_comprehension", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o-mini", "model_static": true, "difficulty": "hard", "suggest": null},
    {"id": "EC11", "file": "edge_cases.py", "function": "ec11_call_in_lambda", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o-mini", "model_static": true, "difficulty": "hard", "suggest": null},
    {"id": "EC12", "file": "edge_cases.py", "function": "ec12_kwargs_spread", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": false, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "EC13", "file": "edge_cases.py", "function": "ec13_factory_chain", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": true, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "EC14", "file": "edge_cases.py", "function": "ec14_batch_api", "provider": "openai", "api": "batches.create", "model": null, "model_static": false, "difficulty": "hard", "suggest": null},
    {"id": "EC15", "file": "edge_cases.py", "function": "ec15_legacy_v0", "provider": "openai", "api": "ChatCompletion.create", "model": "gpt-3.5-turbo", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC16", "file": "edge_cases.py", "function": "ec16_decorator_wrapped", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "EC17", "file": "edge_cases.py", "function": "ec17_weird_formatting", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o-mini", "model_static": true, "difficulty": "hard", "suggest": null},
    {"id": "EC18a", "file": "edge_cases.py", "function": "ec18_two_calls_one_line", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": true, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "EC18b", "file": "edge_cases.py", "function": "ec18_two_calls_one_line", "provider": "openai", "api": "chat.completions.create", "model": "gpt-3.5-turbo", "model_static": true, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "EC19", "file": "edge_cases.py", "function": "ec19_ternary_model", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o|gpt-4o-mini", "model_static": false, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "EC20", "file": "edge_cases.py", "function": "SupportAgent.reply", "provider": "openai", "api": "chat.completions.create", "model": "gpt-4o", "model_static": false, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "IN01", "file": "integrations.py", "function": "in01_anthropic_messages", "provider": "anthropic", "api": "messages.create", "model": "claude-3-opus", "model_static": true, "difficulty": "medium", "suggest": "claude-3.5-sonnet"},
    {"id": "IN02", "file": "integrations.py", "function": "in02_google_gemini", "provider": "google", "api": "GenerativeModel.generate_content", "model": "gemini-1.5-pro", "model_static": true, "difficulty": "hard", "suggest": "gemini-1.5-flash"},
    {"id": "IN03", "file": "integrations.py", "function": "in03_litellm_completion", "provider": "litellm", "api": "completion", "model": "gpt-4o", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"},
    {"id": "IN04", "file": "integrations.py", "function": "in04_langchain_invoke", "provider": "langchain", "api": "ChatOpenAI.invoke", "model": "gpt-4o", "model_static": true, "difficulty": "hard", "suggest": "gpt-4o-mini"},
    {"id": "IN05", "file": "integrations.py", "function": "in05_litellm_embedding", "provider": "litellm", "api": "embedding", "model": "text-embedding-3-small", "model_static": true, "difficulty": "medium", "suggest": null},
    {"id": "IN06", "file": "integrations.py", "function": "in06_legacy_module_call", "provider": "openai", "api": "ChatCompletion.create", "model": "gpt-3.5-turbo", "model_static": true, "difficulty": "medium", "suggest": "gpt-4o-mini"}
  ],
  "decoys": [
    {"id": "EC21", "file": "edge_cases.py", "function": "ec21_commented_out", "trap": "commented-out call"},
    {"id": "EC22", "file": "edge_cases.py", "function": "ec22_model_name_in_text", "trap": "model name only in string/docstring"},
    {"id": "EC23", "file": "edge_cases.py", "function": "ec23_non_ai_create", "trap": "db .create(model=...) is a DB op"},
    {"id": "EC24", "file": "edge_cases.py", "function": "ec24_unrelated_model_key", "trap": "'model' dict key is a truck"},
    {"id": "EC25", "file": "edge_cases.py", "function": "ec25_plain_webhook", "trap": "http post to non-AI endpoint"}
  ]
}
```
