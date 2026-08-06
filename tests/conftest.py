from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def holiday_path() -> Path:
    return ROOT / "data" / "holidays.json"


@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    return tmp_path / "data" / "tracker.sqlite3"


@pytest.fixture
def holiday_rules(holiday_path: Path):  # type: ignore[no-untyped-def]
    from neetcode_dashboard.calendar_engine import load_holiday_rules

    return load_holiday_rules(holiday_path)
