import sqlite3
from contextlib import closing
from datetime import UTC, datetime
from pathlib import Path

from fastapi.testclient import TestClient

from neetcode_dashboard.app import _verified_holiday_source, create_app
from neetcode_dashboard.config import Settings
from neetcode_dashboard.event_store import EventStore, EventToAppend

LOOPBACK_CLIENT = ("127.0.0.1", 50_000)


def test_health_reports_foundation_and_verified_dependencies(settings: Settings) -> None:
    with TestClient(create_app(settings), client=LOOPBACK_CLIENT) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    body = response.json()
    assert body["status"] == "ok"
    assert body["mode"] == "FOUNDATION_ONLY"
    assert body["database"] == {
        "integrity": "ok",
        "revision": "0003_event_invariants",
        "holiday_count": 22,
    }
    assert body["calendar"] == {
        "days": 365,
        "base_hours": 1_304,
        "adjusted_hours": 1_292,
        "holiday_count": 22,
    }
    assert str(settings.project_root) not in response.text


def test_foundation_page_is_local_honest_and_accessible(settings: Settings) -> None:
    with TestClient(create_app(settings), client=LOOPBACK_CLIENT) as client:
        response = client.get("/")
        stylesheet = client.get("/static/app.css")

    assert response.status_code == 200
    assert stylesheet.status_code == 200
    assert stylesheet.headers["content-type"].startswith("text/css")
    assert "Foundation ready" in response.text
    assert "학습 시작 잠김" in response.text
    assert "FOUNDATION_ONLY" in response.text
    assert "365일" in response.text
    assert "1,292시간" in response.text
    assert 'aria-disabled="true"' in response.text
    for navigation_label in (
        "오늘 / Today",
        "캘린더 / Calendar",
        "문제 / Problems",
        "인증 / Certification",
        "분석 / Analytics",
    ):
        assert navigation_label in response.text
    assert "<script" not in response.text
    assert "https://" not in response.text
    assert "http://" not in response.text


def test_startup_creates_only_local_runtime_artifacts(settings: Settings) -> None:
    with TestClient(create_app(settings), client=LOOPBACK_CLIENT):
        pass

    assert settings.database_path.is_file()
    assert settings.backup_dir.is_dir()
    assert Path(f"{settings.database_path}-wal").exists() is False
    assert Path(f"{settings.database_path}-shm").exists() is False


def test_health_fails_closed_when_database_contract_drifts(settings: Settings) -> None:
    with TestClient(create_app(settings), client=LOOPBACK_CLIENT) as client:
        with closing(sqlite3.connect(settings.database_path)) as connection:
            connection.execute("DELETE FROM calendar_exceptions WHERE date = '2026-08-15'")
            connection.commit()

        response = client.get("/api/health")

    assert response.status_code == 503
    assert response.json() == {"detail": "foundation dependency check failed"}
    assert str(settings.project_root) not in response.text


def test_health_fails_closed_when_event_chain_is_corrupt(settings: Settings) -> None:
    application = create_app(settings)
    with TestClient(application, client=LOOPBACK_CLIENT) as client:
        EventStore(application.state.engine).append(
            EventToAppend("system", "READY", {}, datetime(2026, 8, 6, tzinfo=UTC))
        )
        with closing(sqlite3.connect(settings.database_path)) as connection:
            connection.execute("DROP TRIGGER system_events_reject_update")
            connection.execute("UPDATE system_events SET event_type = 'CHANGED' WHERE id = 1")
            connection.commit()

        response = client.get("/api/health")

    assert response.status_code == 503
    assert response.json() == {"detail": "foundation dependency check failed"}


def test_health_fails_closed_when_append_only_guard_is_missing(settings: Settings) -> None:
    application = create_app(settings)
    with TestClient(application, client=LOOPBACK_CLIENT) as client:
        with closing(sqlite3.connect(settings.database_path)) as connection:
            connection.execute("DROP TRIGGER system_events_reject_insert_collision")
            connection.commit()

        response = client.get("/api/health")

    assert response.status_code == 503
    assert response.json() == {"detail": "foundation dependency check failed"}


def test_application_rejects_non_loopback_clients(settings: Settings) -> None:
    with TestClient(
        create_app(settings),
        client=("192.0.2.10", 50_000),
    ) as client:
        response = client.get("/api/health")

    assert response.status_code == 403
    assert response.json() == {"detail": "loopback clients only"}


def test_holiday_source_requires_the_frozen_full_record_digest(tmp_path: Path) -> None:
    changed_source = tmp_path / "holidays.json"
    changed_source.write_text("[]", encoding="utf-8")

    try:
        _verified_holiday_source(changed_source)
    except RuntimeError as error:
        assert "digest" in str(error)
    else:
        raise AssertionError("changed holiday source was accepted")
