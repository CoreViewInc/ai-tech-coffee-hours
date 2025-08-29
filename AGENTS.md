# Repository Guidelines

## Project Structure & Module Organization
- Root: `main.py` (interactive menu), `pyproject.toml`, `.env(.example)`, `requirements.txt`.
- Sessions: learning modules under `session_1/` and `session_2/`.
  - `session_1/primitives/`: core demos — `shared_utils.py`, `stateless_chat.py`, `stateless_chat_with_context.py`, `stateful_chat.py`, `tools_chat.py`, `artisan_agent.py`.
  - `session_2/rag/`: RAG placeholders (`rag_agent.py`, `importer.py`).
- No dedicated `assets/` or `tests/` directories yet.

## Build, Test, and Development Commands
- Setup: `uv pip install -e .` (Python 3.12+, venv via `uv venv` then `source .venv/bin/activate`).
- Configure: `cp .env.example .env` and fill Azure variables.
- Run all demos: `python main.py`.
- Run a single demo: `python session_1/primitives/stateless_chat.py` (swap filename as needed).
- Tests: no suite yet. If adding, prefer `pytest` and `tests/` (see Testing Guidelines).

## Coding Style & Naming Conventions
- Python: PEP 8, 4‑space indentation, snake_case for modules/functions; PascalCase for classes.
- Entry functions: expose demo via `demonstrate_<topic>()` (imported in `main.py`).
- Tools: name functions `use_<tool>()`, add to both `tools`/`artisan_tools` schemas and `available_functions`/`available_tools` maps.
- Docstrings: brief triple‑quoted summary; keep prints user‑centric for interactive flows.

## Testing Guidelines
- Current state: manual verification via the interactive flows.
- If introducing tests: use `pytest`, place files under `tests/`, name `test_<module>.py`, and prefer small, deterministic units.
- Example: `tests/test_shared_utils.py` for client setup behavior. Run with `pytest -q`.

## Commit & Pull Request Guidelines
- Commits: imperative, concise subject (<72 chars) + context in body.
  - Example: `Add stateless chat with context demo; update menu`
- PRs: include clear description, linked issues, run steps (`python main.py`), and before/after notes or CLI transcript. Keep changes scoped per session (e.g., `session_1/primitives`).

## Security & Configuration Tips
- Secrets: never commit `.env` (ignored by `.gitignore`). Use `.env.example` for new keys.
- Required env: `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_VERSION`, `AZURE_OPENAI_DEPLOYMENT_NAME`.
- Reasonable defaults exist in code, but production runs should supply explicit values.
