from pathlib import Path

from fastapi.testclient import TestClient

from neetcode_dashboard.app import create_app
from neetcode_dashboard.config import Settings


def test_health_reports_foundation_and_verified_dependencies(settings: Settings) -> None:
    with TestClient(create_app(settings)) as client:
        response = client.get("/api/health")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    body = response.json()
    assert body["status"] == "ok"
    assert body["mode"] == "FOUNDATION_ONLY"
    assert body["database"] == {
        "integrity": "ok",
        "revision": "0002_system_events",
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
    with TestClient(create_app(settings)) as client:
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
    assert "<script" not in response.text
    assert "https://" not in response.text
    assert "http://" not in response.text


def test_startup_creates_only_local_runtime_artifacts(settings: Settings) -> None:
    with TestClient(create_app(settings)):
        pass

    assert settings.database_path.is_file()
    assert settings.backup_dir.is_dir()
    assert Path(f"{settings.database_path}-wal").exists() is False
    assert Path(f"{settings.database_path}-shm").exists() is False
