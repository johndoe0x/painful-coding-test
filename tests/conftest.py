from collections.abc import Generator
from pathlib import Path
from shutil import copyfile

import pytest
from sqlalchemy import Engine

from neetcode_dashboard.calendar_engine import HolidayRule, load_holiday_rules
from neetcode_dashboard.config import Settings
from neetcode_dashboard.db.engine import create_sqlite_engine
from neetcode_dashboard.db.migrations import upgrade_database
from neetcode_dashboard.db.seed import sync_holiday_rules
from neetcode_dashboard.event_store import EventStore, EventToAppend
from neetcode_dashboard.time import utc_now

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def holiday_path() -> Path:
    return ROOT / "data" / "holidays.json"


@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    return tmp_path / "data" / "tracker.sqlite3"


@pytest.fixture
def holiday_rules(holiday_path: Path) -> tuple[HolidayRule, ...]:
    return load_holiday_rules(holiday_path)


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    project_root = tmp_path / "dashboard"
    holiday_destination = project_root / "data" / "holidays.json"
    holiday_destination.parent.mkdir(parents=True)
    copyfile(ROOT / "data" / "holidays.json", holiday_destination)
    return Settings(project_root=project_root)


@pytest.fixture
def migrated_engine(
    database_path: Path,
    holiday_rules: tuple[HolidayRule, ...],
) -> Generator[Engine]:
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)
    sync_holiday_rules(engine, holiday_rules)
    yield engine
    engine.dispose()


@pytest.fixture
def populated_database(
    database_path: Path,
    holiday_rules: tuple[HolidayRule, ...],
) -> Path:
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)
    sync_holiday_rules(engine, holiday_rules)
    store = EventStore(engine)
    store.append(EventToAppend("system", "APP_STARTED", {"mode": "FOUNDATION_ONLY"}, utc_now()))
    store.append(EventToAppend("system", "CALENDAR_READY", {"days": 365}, utc_now()))
    engine.dispose()
    return database_path
