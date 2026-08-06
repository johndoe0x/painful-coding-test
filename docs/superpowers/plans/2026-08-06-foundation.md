# NeetCode 500 Dashboard Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first runnable local dashboard slice with the frozen master plan, deterministic Asia/Seoul calendar, FastAPI shell, durable SQLite/Alembic foundation, append-only hash-chained events, and verified backup/restore.

**Architecture:** A `src/neetcode_dashboard` Python package owns typed configuration, calendar rules, persistence, event storage, backup/restore, and the FastAPI application factory. SQLite is accessed synchronously through SQLAlchemy 2, schema changes are explicit Alembic revisions, and startup uses FastAPI lifespan to migrate and seed static holiday rules before serving a local-only HTML shell. Foundation remains visibly `FOUNDATION_ONLY`; later curriculum, practice, Codex, voice, and animation slices consume these interfaces without pretending to be complete here.

**Tech Stack:** Python 3.12+, uv, FastAPI, Jinja2, Pydantic Settings, SQLAlchemy 2.0, Alembic, SQLite, pytest, HTTPX TestClient, Ruff, mypy.

## Global Constraints

- Copy `/Users/devan/Desktop/neetcode_500_bilingual_master_plan_2026-08-06_v2.0.md` byte-for-byte to repository-root `PLAN.md`; its SHA-256 must remain `1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96`.
- Preserve the exact study interval `2026-08-06` through `2027-08-05`, 365 inclusive days, 1,304 base hours, 1,292 holiday-adjusted hours, and all 22 named holiday overrides from `PLAN.md` section 1.6.
- Bind runtime HTTP only to `127.0.0.1` or `localhost`; Foundation has no login and no public-hosting mode.
- Core runtime assets must not use a CDN or require network access after dependency installation.
- Every SQLite connection must enforce `foreign_keys=ON`, `journal_mode=WAL`, `synchronous=FULL`, and `busy_timeout=5000`.
- Store event instants as aware UTC timestamps and derive the Asia/Seoul study date explicitly.
- Event history is append-only at the database level; update/delete operations must fail even when attempted with raw SQL.
- Use canonical JSON and SHA-256 for payload and event-chain hashes.
- Use the SQLite backup API, `PRAGMA integrity_check`, a content hash, and an atomic final rename before a backup or restore is accepted.
- Production learning stays disabled; the UI and health API must report `FOUNDATION_ONLY` until later content and grader gates exist.
- Follow test-driven development: every behavior test must be observed failing for the intended missing behavior before production implementation.

## File Structure

```text
.
├── PLAN.md
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
├── alembic.ini
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       ├── 0001_calendar_exceptions.py
│       └── 0002_system_events.py
├── data/
│   └── holidays.json
├── src/neetcode_dashboard/
│   ├── __init__.py
│   ├── __main__.py
│   ├── app.py
│   ├── config.py
│   ├── time.py
│   ├── calendar_engine.py
│   ├── event_store.py
│   ├── backup.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── engine.py
│   │   ├── migrations.py
│   │   ├── models.py
│   │   └── seed.py
│   ├── templates/
│   │   ├── base.html
│   │   └── foundation.html
│   └── static/
│       └── app.css
└── tests/
    ├── conftest.py
    ├── test_repository_contract.py
    ├── test_config.py
    ├── test_calendar_engine.py
    ├── test_database.py
    ├── test_event_store.py
    ├── test_backup.py
    └── test_app.py
```

The package boundary is deliberate: `calendar_engine.py` is pure and knows no database; `db/` owns schema/session mechanics; `event_store.py` owns append-only event semantics; `backup.py` owns filesystem durability; `app.py` only composes these services.

---

### Task 1: Repository Contract and Reproducible Python Project

**Files:**
- Modify: `.gitignore`
- Create: `.python-version`
- Create: `pyproject.toml`
- Create: `README.md`
- Create: `PLAN.md`
- Create: `src/neetcode_dashboard/__init__.py`
- Create: `tests/test_repository_contract.py`
- Create: `uv.lock` through `uv lock`

**Interfaces:**
- Consumes: supplied v2.0 master-plan file and the approved design spec.
- Produces: installable package `neetcode_dashboard`, command `neetcode-dashboard`, locked dependencies, and immutable `PLAN.md` contract.

- [x] **Step 1: Add only static project configuration required to execute tests**

Configuration files are the TDD bootstrap exception. Set `.python-version` to `3.13` and create `pyproject.toml` with this executable contract:

```toml
[build-system]
requires = ["hatchling>=1.27,<2"]
build-backend = "hatchling.build"

[project]
name = "neetcode-500-dashboard"
version = "0.1.0"
description = "Local evidence-first NeetCode 500 learning dashboard"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
  "alembic>=1.18.5,<1.19",
  "fastapi>=0.116,<1",
  "jinja2>=3.1,<4",
  "pydantic-settings>=2.10,<3",
  "sqlalchemy>=2.0.51,<2.1",
  "uvicorn>=0.35,<1",
]

[project.scripts]
neetcode-dashboard = "neetcode_dashboard.__main__:main"

[dependency-groups]
dev = [
  "httpx>=0.28,<1",
  "mypy>=1.17,<2",
  "pytest>=8.4,<9",
  "pytest-cov>=6,<8",
  "ruff>=0.12,<1",
]

[tool.hatch.build.targets.wheel]
packages = ["src/neetcode_dashboard"]

[tool.pytest.ini_options]
addopts = "-ra --strict-markers --strict-config"
testpaths = ["tests"]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM", "RUF"]

[tool.mypy]
python_version = "3.12"
strict = true
packages = ["neetcode_dashboard"]
```

Add `.venv/`, Python caches, coverage artifacts, `.worktrees/`, `data/*.sqlite3*`, `backups/*`, and retained local media to `.gitignore`, while keeping `data/holidays.json` tracked.

- [x] **Step 2: Lock and install dependencies**

Run:

```bash
uv lock
uv sync
```

Expected: `uv.lock` and `.venv` exist, and dependency resolution supports Python 3.12+.

- [x] **Step 3: Write the failing repository-contract test**

```python
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PLAN_HASH = "1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96"


def test_master_plan_is_frozen_byte_for_byte() -> None:
    plan = ROOT / "PLAN.md"
    assert plan.exists()
    assert sha256(plan.read_bytes()).hexdigest() == EXPECTED_PLAN_HASH
```

- [x] **Step 4: Verify RED**

Run: `uv run pytest tests/test_repository_contract.py -q`

Expected: FAIL because repository-root `PLAN.md` does not exist.

- [x] **Step 5: Copy the supplied plan byte-for-byte and add the package marker**

Use a byte-preserving copy from the exact supplied absolute path, then verify with `shasum -a 256 PLAN.md`. Set `src/neetcode_dashboard/__init__.py` to:

```python
__version__ = "0.1.0"
```

README must state the exact `uv sync`, `uv run neetcode-dashboard`, `uv run pytest`, `uv run ruff check .`, and `uv run mypy` commands and clearly label the application as Foundation-only.

- [x] **Step 6: Verify GREEN**

Run: `uv run pytest tests/test_repository_contract.py -q`

Expected: 1 passed.

- [x] **Step 7: Commit**

```bash
git add .gitignore .python-version pyproject.toml uv.lock README.md PLAN.md src/neetcode_dashboard/__init__.py tests/test_repository_contract.py
git commit -m "chore: bootstrap dashboard project"
```

---

### Task 2: Typed Local Configuration and Time Boundary

**Files:**
- Create: `src/neetcode_dashboard/config.py`
- Create: `src/neetcode_dashboard/time.py`
- Create: `tests/test_config.py`
- Create: `tests/conftest.py`

**Interfaces:**
- Consumes: environment variables prefixed `NEETCODE_`.
- Produces: `Settings`, `ensure_runtime_directories(settings)`, `utc_now()`, and `study_date(datetime)`.

- [x] **Step 1: Write failing settings and time tests**

```python
from datetime import UTC, datetime
from pathlib import Path

import pytest
from pydantic import ValidationError

from neetcode_dashboard.config import Settings, ensure_runtime_directories
from neetcode_dashboard.time import study_date


def test_settings_create_local_runtime_paths(tmp_path: Path) -> None:
    settings = Settings(project_root=tmp_path)
    ensure_runtime_directories(settings)
    assert settings.database_path == tmp_path / "data" / "tracker.sqlite3"
    assert settings.backup_dir == tmp_path / "backups"
    assert settings.database_path.parent.is_dir()
    assert settings.backup_dir.is_dir()


def test_non_loopback_host_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        Settings(project_root=tmp_path, host="0.0.0.0")


def test_study_date_is_derived_in_asia_seoul() -> None:
    instant = datetime(2026, 8, 5, 15, 30, tzinfo=UTC)
    assert study_date(instant).isoformat() == "2026-08-06"
```

- [x] **Step 2: Verify RED**

Run: `uv run pytest tests/test_config.py -q`

Expected: collection error because `config` and `time` modules do not exist.

- [x] **Step 3: Implement the minimal typed boundary**

`Settings` must use `SettingsConfigDict(env_prefix="NEETCODE_", extra="forbid")`, accept only `Literal["127.0.0.1", "localhost"]`, constrain the port to `1..65535`, derive `data_dir`, `database_path`, and `backup_dir` from `project_root`, and allow explicit path overrides for tests. `utc_now()` returns an aware UTC value; `study_date()` rejects naive datetimes and converts through `ZoneInfo("Asia/Seoul")`.

- [x] **Step 4: Verify GREEN**

Run: `uv run pytest tests/test_config.py -q`

Expected: 3 passed.

- [x] **Step 5: Commit**

```bash
git add src/neetcode_dashboard/config.py src/neetcode_dashboard/time.py tests/conftest.py tests/test_config.py
git commit -m "feat: add local runtime configuration"
```

---

### Task 3: Deterministic Asia/Seoul Calendar Engine

**Files:**
- Create: `data/holidays.json`
- Create: `src/neetcode_dashboard/calendar_engine.py`
- Create: `tests/test_calendar_engine.py`

**Interfaces:**
- Consumes: the 22 frozen holiday records in `data/holidays.json`.
- Produces: `HolidayRule`, `CalendarDay`, `CalendarSummary`, `load_holiday_rules(path)`, `planned_minutes(day, holidays)`, and `summarize_plan(holidays)`.

- [x] **Step 1: Write failing calendar contract tests**

```python
from datetime import date

from neetcode_dashboard.calendar_engine import load_holiday_rules, planned_minutes, summarize_plan


def test_plan_capacity_matches_frozen_master_plan(holiday_path) -> None:
    holidays = load_holiday_rules(holiday_path)
    summary = summarize_plan(holidays)
    assert summary.days == 365
    assert summary.base_minutes == 1_304 * 60
    assert summary.adjusted_minutes == 1_292 * 60
    assert len(holidays) == 22


def test_named_holidays_override_weekday_and_sunday(holiday_path) -> None:
    holidays = load_holiday_rules(holiday_path)
    assert planned_minutes(date(2026, 8, 17), holidays) == 180
    assert planned_minutes(date(2027, 2, 7), holidays) == 180
    assert planned_minutes(date(2027, 5, 3), holidays) == 180
    assert planned_minutes(date(2027, 7, 19), holidays) == 180


def test_monthly_adjusted_hours_match_master_plan(holiday_path) -> None:
    summary = summarize_plan(load_holiday_rules(holiday_path))
    assert summary.monthly_adjusted_minutes == {
        "2026-08": 91 * 60, "2026-09": 106 * 60, "2026-10": 109 * 60,
        "2026-11": 106 * 60, "2026-12": 111 * 60, "2027-01": 108 * 60,
        "2027-02": 99 * 60, "2027-03": 111 * 60, "2027-04": 108 * 60,
        "2027-05": 106 * 60, "2027-06": 109 * 60, "2027-07": 110 * 60,
        "2027-08": 18 * 60,
    }
```

- [x] **Step 2: Verify RED**

Run: `uv run pytest tests/test_calendar_engine.py -q`

Expected: collection error because `calendar_engine` does not exist.

- [x] **Step 3: Encode the exact holiday dataset**

Create 22 JSON objects for these exact dates:

```text
2026-08-15, 2026-08-17, 2026-09-24, 2026-09-25, 2026-09-26,
2026-10-03, 2026-10-05, 2026-10-09, 2026-12-25, 2027-01-01,
2027-02-06, 2027-02-07, 2027-02-08, 2027-02-09, 2027-03-01,
2027-05-01, 2027-05-03, 2027-05-05, 2027-05-13, 2027-06-06,
2027-07-17, 2027-07-19
```

Each object contains `date`, `kind`, `name_ko`, `name_en`, `planned_minutes: 180`, `source`, `source_as_of`, and `active: true`, using names and classifications exactly from `PLAN.md` section 1.6.

- [x] **Step 4: Implement the pure calendar engine**

Use `PLAN_START = date(2026, 8, 6)` and `PLAN_END = date(2027, 8, 5)`. Base minutes are 240 Monday–Friday, 180 Saturday, and 120 Sunday. Active date overrides win. Reject duplicate dates, out-of-range planned minutes, missing bilingual names, and any plan interval not equal to 365 inclusive days. Return frozen dataclasses so callers cannot mutate a computed result.

- [x] **Step 5: Verify GREEN**

Run: `uv run pytest tests/test_calendar_engine.py -q`

Expected: 3 passed.

- [x] **Step 6: Commit**

```bash
git add data/holidays.json src/neetcode_dashboard/calendar_engine.py tests/test_calendar_engine.py tests/conftest.py
git commit -m "feat: add deterministic study calendar"
```

---

### Task 4: SQLite Engine, Alembic, and Holiday Persistence

**Files:**
- Create: `alembic.ini`
- Create: `migrations/env.py`
- Create: `migrations/script.py.mako`
- Create: `migrations/versions/0001_calendar_exceptions.py`
- Create: `src/neetcode_dashboard/db/__init__.py`
- Create: `src/neetcode_dashboard/db/base.py`
- Create: `src/neetcode_dashboard/db/engine.py`
- Create: `src/neetcode_dashboard/db/migrations.py`
- Create: `src/neetcode_dashboard/db/models.py`
- Create: `src/neetcode_dashboard/db/seed.py`
- Create: `tests/test_database.py`

**Interfaces:**
- Consumes: `Settings.database_path` and `Sequence[HolidayRule]`.
- Produces: `Base`, `CalendarException`, `create_sqlite_engine(path)`, `session_factory(engine)`, `upgrade_database(path)`, `current_revision(engine)`, `database_health(engine)`, and `sync_holiday_rules(engine, rules)`.

- [x] **Step 1: Write failing database tests**

```python
from sqlalchemy import text

from neetcode_dashboard.db.engine import create_sqlite_engine, database_health
from neetcode_dashboard.db.migrations import upgrade_database
from neetcode_dashboard.db.seed import sync_holiday_rules


def test_every_connection_has_required_pragmas(database_path) -> None:
    engine = create_sqlite_engine(database_path)
    with engine.connect() as connection:
        assert connection.scalar(text("PRAGMA foreign_keys")) == 1
        assert str(connection.scalar(text("PRAGMA journal_mode"))).lower() == "wal"
        assert connection.scalar(text("PRAGMA synchronous")) == 2
        assert connection.scalar(text("PRAGMA busy_timeout")) == 5000


def test_migration_and_holiday_seed_are_idempotent(database_path, holiday_rules) -> None:
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)
    sync_holiday_rules(engine, holiday_rules)
    sync_holiday_rules(engine, holiday_rules)
    health = database_health(engine)
    assert health.integrity == "ok"
    assert health.revision == "0001_calendar_exceptions"
    assert health.holiday_count == 22
```

- [x] **Step 2: Verify RED**

Run: `uv run pytest tests/test_database.py -q`

Expected: collection error because `neetcode_dashboard.db` does not exist.

- [x] **Step 3: Implement engine configuration and metadata**

`create_sqlite_engine()` creates the parent directory, uses `sqlite+pysqlite:///...`, `connect_args={"autocommit": False, "check_same_thread": False}`, and a SQLAlchemy `connect` listener that executes the four required PRAGMAs. `Base` extends `DeclarativeBase`. `CalendarException` normalizes filterable fields into columns and enforces one active record per date through a unique date constraint.

- [x] **Step 4: Implement explicit Alembic migration and seed**

The revision creates `calendar_exceptions` with a `CHECK(planned_minutes > 0 AND planned_minutes <= 1440)` constraint and indexes `date` and `active`. `upgrade_database(path)` uses Alembic's programmatic `Config`, points `script_location` at repository `migrations`, sets the escaped SQLite URL, and runs `command.upgrade(config, "head")`. `sync_holiday_rules()` inserts missing rows and updates only static source fields when the JSON source changed; it never deletes historical manual overrides.

- [x] **Step 5: Verify GREEN**

Run: `uv run pytest tests/test_database.py -q`

Expected: 2 passed.

- [x] **Step 6: Commit**

```bash
git add alembic.ini migrations src/neetcode_dashboard/db tests/test_database.py tests/conftest.py
git commit -m "feat: add SQLite migration foundation"
```

---

### Task 5: Append-Only Hash-Chained Event Store

**Files:**
- Modify: `src/neetcode_dashboard/db/models.py`
- Create: `migrations/versions/0002_system_events.py`
- Create: `src/neetcode_dashboard/event_store.py`
- Create: `tests/test_event_store.py`

**Interfaces:**
- Consumes: a migrated SQLAlchemy `Engine` and `EventToAppend`.
- Produces: `EventToAppend`, `StoredEvent`, `EventStore.append(event)`, and `EventStore.read_stream(stream_id)`.

- [x] **Step 1: Write failing event-store tests**

```python
from datetime import UTC, datetime

import pytest
from sqlalchemy import text
from sqlalchemy.exc import DatabaseError

from neetcode_dashboard.event_store import EventStore, EventToAppend


def test_events_are_sequenced_and_hash_chained(migrated_engine) -> None:
    store = EventStore(migrated_engine)
    first = store.append(EventToAppend("system", "APP_STARTED", {"mode": "FOUNDATION_ONLY"}, datetime(2026, 8, 6, tzinfo=UTC)))
    second = store.append(EventToAppend("system", "CALENDAR_READY", {"days": 365}, datetime(2026, 8, 6, 0, 1, tzinfo=UTC)))
    assert (first.event_seq, second.event_seq) == (1, 2)
    assert second.previous_event_sha256 == first.event_sha256
    assert [event.event_type for event in store.read_stream("system")] == ["APP_STARTED", "CALENDAR_READY"]


def test_database_rejects_event_update_and_delete(migrated_engine) -> None:
    store = EventStore(migrated_engine)
    event = store.append(EventToAppend("system", "APP_STARTED", {}, datetime(2026, 8, 6, tzinfo=UTC)))
    with pytest.raises(DatabaseError):
        with migrated_engine.begin() as connection:
            connection.execute(text("UPDATE system_events SET event_type='CHANGED' WHERE id=:id"), {"id": event.id})
    with pytest.raises(DatabaseError):
        with migrated_engine.begin() as connection:
            connection.execute(text("DELETE FROM system_events WHERE id=:id"), {"id": event.id})
```

- [x] **Step 2: Verify RED**

Run: `uv run pytest tests/test_event_store.py -q`

Expected: collection error because `event_store` does not exist.

- [x] **Step 3: Add the event schema and append-only triggers**

Migration `0002_system_events` creates normalized columns `id`, `stream_id`, `event_seq`, `event_type`, `schema_version`, `payload_json`, `payload_sha256`, `previous_event_sha256`, `event_sha256`, `occurred_at_utc`, `received_at_utc`, and `study_date`. Add unique constraints on `(stream_id, event_seq)` and `event_sha256`, plus indexes on stream/sequence, type, UTC instant, and study date. Create `BEFORE UPDATE` and `BEFORE DELETE` triggers that execute `RAISE(ABORT, 'system_events are append-only')`.

- [x] **Step 4: Implement canonical append semantics**

`EventToAppend` and `StoredEvent` are frozen dataclasses. Validate a non-empty stream/type, positive schema version, aware timestamp, and JSON-serializable payload. Canonical payload bytes use `json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))`. `EventStore.append()` opens `BEGIN IMMEDIATE`, reads the latest event, assigns the next sequence, derives Asia/Seoul date, computes payload/event hashes, inserts once, commits, and returns the stored value. `read_stream()` orders strictly by `event_seq` and verifies the hash chain before returning.

- [x] **Step 5: Verify GREEN and migration head**

Run:

```bash
uv run pytest tests/test_event_store.py -q
uv run alembic upgrade head
uv run alembic current
```

Expected: 2 passed and revision `0002_system_events (head)`.

- [x] **Step 6: Commit**

```bash
git add src/neetcode_dashboard/db/models.py migrations/versions/0002_system_events.py src/neetcode_dashboard/event_store.py tests/test_event_store.py tests/conftest.py
git commit -m "feat: add append-only event store"
```

---

### Task 6: Verified SQLite Backup and Restore

**Files:**
- Create: `src/neetcode_dashboard/backup.py`
- Create: `tests/test_backup.py`

**Interfaces:**
- Consumes: source database path, backup directory, application/schema versions.
- Produces: `BackupManifest`, `BackupArtifact`, `create_verified_backup()`, `verify_backup()`, and `restore_verified_backup()`.

- [x] **Step 1: Write failing backup tests**

```python
from pathlib import Path

import pytest

from neetcode_dashboard.backup import BackupVerificationError, create_verified_backup, restore_verified_backup, verify_backup


def test_backup_and_restore_preserve_committed_events(populated_database, tmp_path: Path) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    manifest = verify_backup(artifact)
    assert manifest.integrity_check == "ok"
    assert manifest.event_count == 2
    restored = tmp_path / "restored" / "tracker.sqlite3"
    restore_verified_backup(artifact, restored)
    assert verify_backup(artifact).database_sha256 == manifest.database_sha256
    assert restored.exists()


def test_tampered_backup_is_rejected(populated_database, tmp_path: Path) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    artifact.database_path.write_bytes(artifact.database_path.read_bytes() + b"tampered")
    with pytest.raises(BackupVerificationError, match="SHA-256"):
        verify_backup(artifact)
```

- [x] **Step 2: Verify RED**

Run: `uv run pytest tests/test_backup.py -q`

Expected: collection error because `backup` does not exist.

- [x] **Step 3: Implement atomic backup and verification**

Use `sqlite3.Connection.backup()` from a read connection to a temporary destination. Run `PRAGMA integrity_check`, read `alembic_version`, count events and holiday rows, close both connections, SHA-256 the resulting database, and write a canonical JSON manifest containing format version, app version, schema revision, UTC creation time, source plan hash, database hash, integrity result, and row counts. `fsync` each temporary file and its directory, then `os.replace` into final timestamped names. `verify_backup()` recomputes every value and rejects mismatches.

- [x] **Step 4: Implement fail-closed restore**

`restore_verified_backup()` verifies the artifact first, copies into a sibling temporary file, reruns integrity/hash/revision checks on the temporary file, creates the destination parent, and atomically replaces the destination. It refuses to restore when the destination has `-wal` or `-shm` siblings, which signals an active or unclean database.

- [x] **Step 5: Verify GREEN**

Run: `uv run pytest tests/test_backup.py -q`

Expected: 2 passed.

- [x] **Step 6: Commit**

```bash
git add src/neetcode_dashboard/backup.py tests/test_backup.py tests/conftest.py
git commit -m "feat: add verified database backups"
```

---

### Task 7: Runnable FastAPI Foundation Shell

**Files:**
- Create: `src/neetcode_dashboard/app.py`
- Create: `src/neetcode_dashboard/__main__.py`
- Create: `src/neetcode_dashboard/templates/base.html`
- Create: `src/neetcode_dashboard/templates/foundation.html`
- Create: `src/neetcode_dashboard/static/app.css`
- Create: `tests/test_app.py`

**Interfaces:**
- Consumes: `Settings`, migration/seed services, calendar summary, and database health.
- Produces: `create_app(settings=None) -> FastAPI`, `GET /`, `GET /api/health`, and CLI `neetcode-dashboard`.

- [x] **Step 1: Write failing app tests**

```python
from fastapi.testclient import TestClient

from neetcode_dashboard.app import create_app


def test_health_reports_foundation_and_verified_dependencies(settings) -> None:
    with TestClient(create_app(settings)) as client:
        response = client.get("/api/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["mode"] == "FOUNDATION_ONLY"
    assert body["database"]["integrity"] == "ok"
    assert body["database"]["revision"] == "0002_system_events"
    assert body["calendar"] == {"days": 365, "base_hours": 1304, "adjusted_hours": 1292, "holiday_count": 22}


def test_foundation_page_is_local_and_honest(settings) -> None:
    with TestClient(create_app(settings)) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert "Foundation ready" in response.text
    assert "학습 시작 잠김" in response.text
    assert "https://" not in response.text
    assert "http://" not in response.text
```

- [x] **Step 2: Verify RED**

Run: `uv run pytest tests/test_app.py -q`

Expected: collection error because `app` does not exist.

- [x] **Step 3: Implement lifespan and typed health response**

Use an `@asynccontextmanager` lifespan. Before yielding, ensure runtime directories, upgrade the database, seed holiday rules, compute the calendar summary, and store engine/summary on `app.state`; after yielding, dispose the engine. The health route returns Pydantic response models with no secrets or filesystem paths. A failed migration, seed, integrity check, or calendar contract prevents startup instead of reporting `ok`.

- [x] **Step 4: Implement the offline Midnight Focus shell**

Mount package-local static assets at `/static` and render Jinja2 templates. Show the five eventual navigation areas as disabled previews, exact 365/1,292/22 foundation facts, DB revision/integrity, and a prominent `학습 시작 잠김 · FOUNDATION_ONLY` gate. Use semantic HTML, visible keyboard focus, responsive CSS at 820px and 520px, reduced-motion rules, and no JavaScript or external URLs in Foundation.

- [x] **Step 5: Implement the CLI**

`main()` parses optional `--host` and `--port`, validates them by constructing `Settings`, and calls `uvicorn.run("neetcode_dashboard.app:create_app", factory=True, host=settings.host, port=settings.port)`. Public bind addresses are rejected by the same Pydantic boundary.

- [x] **Step 6: Verify GREEN**

Run: `uv run pytest tests/test_app.py -q`

Expected: 2 passed.

- [x] **Step 7: Commit**

```bash
git add src/neetcode_dashboard/app.py src/neetcode_dashboard/__main__.py src/neetcode_dashboard/templates src/neetcode_dashboard/static tests/test_app.py tests/conftest.py
git commit -m "feat: add runnable foundation dashboard"
```

---

### Task 8: Complete Quality Gate and Operator Documentation

**Files:**
- Modify: `README.md`
- Modify: tests only if a quality command exposes an uncovered, already-specified behavior.

**Interfaces:**
- Consumes: all Foundation tasks.
- Produces: reproducible setup/run/verify/backup instructions and a clean quality gate.

- [x] **Step 1: Add exact operator commands to README**

Document:

```bash
uv sync
uv run alembic upgrade head
uv run neetcode-dashboard --host 127.0.0.1 --port 8000
uv run pytest --cov=neetcode_dashboard --cov-report=term-missing --cov-fail-under=90
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run alembic check
```

Explain where the local database/backups live, how `NEETCODE_PROJECT_ROOT` redirects all runtime state for testing, that restore must occur while the app is stopped, and that Foundation does not yet schedule or grade problems.

- [x] **Step 2: Run the complete verification suite**

Run every command above except the long-running server. Expected: zero test failures, coverage at least 90%, no lint/format/type errors, and no pending Alembic operations.

- [x] **Step 3: Run a real process smoke test**

Start `uv run neetcode-dashboard --host 127.0.0.1 --port 8000` in a managed terminal, wait for startup, request `/api/health`, assert HTTP 200 and `FOUNDATION_ONLY`, request `/`, then stop the process gracefully. Verify `data/tracker.sqlite3` exists, `PRAGMA integrity_check` returns `ok`, and the process emitted no traceback.

- [x] **Step 4: Verify the frozen plan and clean diff**

```bash
shasum -a 256 PLAN.md
git diff --check -- . ':!PLAN.md'
git status -sb
```

Expected plan hash: `1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96`.

- [x] **Step 5: Commit documentation-only adjustments**

```bash
git add README.md
git commit -m "docs: add foundation runbook"
```

Skip this commit only if Task 1's README already matches the final verified commands byte-for-byte and no file changed.

## Self-Review Result

- Spec coverage: Foundation delivery item is covered by Tasks 1–7; full-product requirements are explicitly deferred to their named later slices.
- Placeholder scan: the plan contains no implementation placeholders; all required dates, totals, states, paths, commands, and interfaces are fixed.
- Type consistency: `Settings`, calendar value types, engine/migration functions, event dataclasses/store, backup artifacts, and `create_app()` retain the same names across producer and consumer tasks.
- Scope: curriculum import, attempts, deterministic solution runner, Codex, voice, qualified animations, and learning certification are not stubbed; Foundation reports them locked.

## Post-Review Hardening Amendment

The implementation received an independent evidence-focused review after Task 8. The original task sequence above remains the TDD execution record; the following completed changes are the authoritative final Foundation state:

- [x] Migration head is `0003_event_invariants`, which adds a persistent insert-collision trigger; every application connection also enables `recursive_triggers=ON`.
- [x] Raw `INSERT OR REPLACE`, UPSERT, UPDATE, and DELETE mutation paths have regression coverage.
- [x] Backup creation, verification, and restore verify every event stream plus the required append-only guards.
- [x] The running application and restore operation coordinate through an interprocess database lock; restore rechecks SQLite sidecars immediately before atomic replacement.
- [x] Health and the Foundation page recompute DB readiness, event chains, and event guards on every request and fail closed with a path-free 503 response.
- [x] An application middleware rejects non-loopback clients even if Uvicorn is invoked outside the validated wrapper CLI.
- [x] The source-checkout Alembic CLI follows `NEETCODE_PROJECT_ROOT`, while explicit programmatic database paths retain precedence; installed wheels migrate through the package CLI startup path.
- [x] The wheel bundles `PLAN.md`, the full holiday source, Alembic configuration, and all migrations; an isolated install was exercised through startup, health, and verified backup.
- [x] The full holiday-record source is pinned by SHA-256, and the disabled navigation labels match Today, Calendar, Problems, Certification, and Analytics.
