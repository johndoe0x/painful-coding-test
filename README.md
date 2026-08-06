# NeetCode 500 Dashboard

Local, single-user, evidence-first study dashboard for the frozen NeetCode 500 plan.

## Current state

This branch implements the Foundation slice only. Problem scheduling, grading, voice, and
answer-animation features remain locked until their later qualified slices are complete.

## Setup and checks

```bash
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy
```

The runnable server command is added with the FastAPI Foundation shell.
