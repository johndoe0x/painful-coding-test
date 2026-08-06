from collections.abc import Generator
from pathlib import Path

import pytest
from sqlalchemy import Engine

from neetcode_dashboard.calendar_engine import HolidayRule, load_holiday_rules
from neetcode_dashboard.db.engine import create_sqlite_engine
from neetcode_dashboard.db.migrations import upgrade_database
from neetcode_dashboard.db.seed import sync_holiday_rules

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
def migrated_engine(
    database_path: Path,
    holiday_rules: tuple[HolidayRule, ...],
) -> Generator[Engine]:
    upgrade_database(database_path)
    engine = create_sqlite_engine(database_path)
    sync_holiday_rules(engine, holiday_rules)
    yield engine
    engine.dispose()
