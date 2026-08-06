from dataclasses import replace
from pathlib import Path

from alembic import command
from alembic.config import Config
from sqlalchemy import text

from neetcode_dashboard.calendar_engine import HolidayRule
from neetcode_dashboard.db.engine import create_sqlite_engine, database_health
from neetcode_dashboard.db.migrations import current_revision, upgrade_database
from neetcode_dashboard.db.seed import sync_holiday_rules


def test_every_connection_has_required_pragmas(database_path: Path) -> None:
    engine = create_sqlite_engine(database_path)

    for _ in range(2):
        with engine.connect() as connection:
            assert connection.scalar(text("PRAGMA foreign_keys")) == 1
            assert str(connection.scalar(text("PRAGMA journal_mode"))).lower() == "wal"
            assert connection.scalar(text("PRAGMA synchronous")) == 2
            assert connection.scalar(text("PRAGMA busy_timeout")) == 5_000
            assert connection.scalar(text("PRAGMA recursive_triggers")) == 1

    engine.dispose()


def test_plain_alembic_cli_honors_runtime_project_root(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repository_root = Path(__file__).resolve().parents[1]
    runtime_root = tmp_path / "runtime"
    fallback_database = tmp_path / "data" / "tracker.sqlite3"
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("NEETCODE_PROJECT_ROOT", str(runtime_root))

    command.upgrade(Config(str(repository_root / "alembic.ini")), "head")

    assert (runtime_root / "data" / "tracker.sqlite3").is_file()
    assert not fallback_database.exists()


def test_migration_and_holiday_seed_are_idempotent(
    database_path: Path,
    holiday_rules: tuple[HolidayRule, ...],
) -> None:
    upgrade_database(database_path)
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)

    sync_holiday_rules(engine, holiday_rules)
    sync_holiday_rules(engine, holiday_rules)
    health = database_health(engine)

    assert health.integrity == "ok"
    assert health.revision == "0003_event_invariants"
    assert current_revision(engine) == "0003_event_invariants"
    assert health.holiday_count == 22
    engine.dispose()


def test_static_holiday_fields_refresh_when_source_changes(
    database_path: Path,
    holiday_rules: tuple[HolidayRule, ...],
) -> None:
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)
    sync_holiday_rules(engine, holiday_rules)
    revised = replace(
        holiday_rules[0],
        name_en="Liberation Day (revised source)",
        source="Revised calendar source",
    )

    sync_holiday_rules(engine, (revised, *holiday_rules[1:]))

    with engine.connect() as connection:
        row = connection.execute(
            text("SELECT name_en, source FROM calendar_exceptions WHERE date = '2026-08-15'")
        ).one()
    assert tuple(row) == ("Liberation Day (revised source)", "Revised calendar source")
    engine.dispose()


def test_manual_override_is_never_overwritten_by_static_seed(
    database_path: Path,
    holiday_rules: tuple[HolidayRule, ...],
) -> None:
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)
    sync_holiday_rules(engine, holiday_rules)
    with engine.begin() as connection:
        connection.execute(
            text(
                "UPDATE calendar_exceptions "
                "SET origin = 'manual', planned_minutes = 240, name_en = 'Manual override' "
                "WHERE date = '2026-08-15'"
            )
        )

    sync_holiday_rules(engine, holiday_rules)

    with engine.connect() as connection:
        row = connection.execute(
            text(
                "SELECT origin, planned_minutes, name_en FROM calendar_exceptions "
                "WHERE date = '2026-08-15'"
            )
        ).one()
    assert tuple(row) == ("manual", 240, "Manual override")
    engine.dispose()
