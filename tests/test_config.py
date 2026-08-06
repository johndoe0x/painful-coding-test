from datetime import UTC, datetime
from pathlib import Path

import pytest
from pydantic import ValidationError

from neetcode_dashboard.config import Settings, ensure_runtime_directories
from neetcode_dashboard.time import study_date, utc_now


def test_settings_create_local_runtime_paths(tmp_path: Path) -> None:
    settings = Settings(project_root=tmp_path)

    ensure_runtime_directories(settings)

    assert settings.database_path == tmp_path / "data" / "tracker.sqlite3"
    assert settings.backup_dir == tmp_path / "backups"
    assert settings.database_path.parent.is_dir()
    assert settings.backup_dir.is_dir()


def test_explicit_runtime_paths_are_preserved(tmp_path: Path) -> None:
    database_path = tmp_path / "custom" / "learning.sqlite3"
    backup_dir = tmp_path / "snapshots"

    settings = Settings(
        project_root=tmp_path,
        database_path=database_path,
        backup_dir=backup_dir,
    )
    ensure_runtime_directories(settings)

    assert settings.database_path == database_path
    assert settings.backup_dir == backup_dir
    assert database_path.parent.is_dir()
    assert backup_dir.is_dir()


def test_non_loopback_host_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        Settings(project_root=tmp_path, host="0.0.0.0")  # type: ignore[arg-type]


def test_port_outside_tcp_range_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        Settings(project_root=tmp_path, port=65_536)


def test_utc_now_is_aware_utc() -> None:
    instant = utc_now()

    assert instant.tzinfo is UTC


def test_study_date_is_derived_in_asia_seoul() -> None:
    instant = datetime(2026, 8, 5, 15, 30, tzinfo=UTC)

    assert study_date(instant).isoformat() == "2026-08-06"


def test_study_date_rejects_naive_datetime() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        study_date(datetime(2026, 8, 6, 0, 30))
