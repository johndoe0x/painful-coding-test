import json
import sqlite3
from contextlib import closing
from hashlib import sha256
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import neetcode_dashboard.backup as backup_module
from neetcode_dashboard.app import create_app
from neetcode_dashboard.backup import (
    BackupVerificationError,
    create_verified_backup,
    restore_verified_backup,
    verify_backup,
)
from neetcode_dashboard.config import Settings


def test_backup_and_restore_preserve_committed_rows(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")

    manifest = verify_backup(artifact)

    assert manifest.integrity_check == "ok"
    assert manifest.schema_revision == "0003_event_invariants"
    assert manifest.event_count == 2
    assert manifest.holiday_count == 22
    restored = tmp_path / "restored" / "tracker.sqlite3"
    restore_verified_backup(artifact, restored)
    with closing(sqlite3.connect(restored)) as connection:
        assert connection.execute("SELECT COUNT(*) FROM system_events").fetchone() == (2,)
        assert connection.execute("SELECT COUNT(*) FROM calendar_exceptions").fetchone() == (22,)


def test_tampered_backup_database_is_rejected(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    artifact.database_path.write_bytes(artifact.database_path.read_bytes() + b"tampered")

    with pytest.raises(BackupVerificationError, match="SHA-256"):
        verify_backup(artifact)


def test_tampered_manifest_is_rejected(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    manifest = json.loads(artifact.manifest_path.read_text(encoding="utf-8"))
    manifest["event_count"] = 99
    artifact.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    with pytest.raises(BackupVerificationError, match="event count"):
        verify_backup(artifact)


@pytest.mark.parametrize("sidecar_suffix", ["-wal", "-shm"])
def test_restore_refuses_destination_with_sqlite_sidecar(
    populated_database: Path,
    tmp_path: Path,
    sidecar_suffix: str,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    destination = tmp_path / "restored" / "tracker.sqlite3"
    destination.parent.mkdir(parents=True)
    Path(f"{destination}{sidecar_suffix}").write_bytes(b"active")

    with pytest.raises(BackupVerificationError, match="sidecar"):
        restore_verified_backup(artifact, destination)

    assert not destination.exists()


def test_missing_source_database_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(BackupVerificationError, match="source database does not exist"):
        create_verified_backup(tmp_path / "missing.sqlite3", tmp_path / "backups")


def test_invalid_or_unsupported_manifest_is_rejected(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    artifact.manifest_path.write_text("{", encoding="utf-8")
    with pytest.raises(BackupVerificationError, match="unable to read"):
        verify_backup(artifact)

    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    manifest = json.loads(artifact.manifest_path.read_text(encoding="utf-8"))
    manifest["format_version"] = 99
    artifact.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(BackupVerificationError, match="unsupported"):
        verify_backup(artifact)


def test_restore_cannot_overwrite_backup_artifact(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")

    with pytest.raises(BackupVerificationError, match="cannot overwrite"):
        restore_verified_backup(artifact, artifact.database_path)


def test_backup_creation_rejects_corrupt_event_chain(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    with closing(sqlite3.connect(populated_database)) as connection:
        connection.execute("DROP TRIGGER system_events_reject_update")
        connection.execute("UPDATE system_events SET event_type = 'CHANGED' WHERE id = 1")
        connection.commit()

    with pytest.raises(BackupVerificationError, match="event chain"):
        create_verified_backup(populated_database, tmp_path / "backups")


def test_backup_verification_rejects_rehashed_corrupt_event_chain(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    with closing(sqlite3.connect(artifact.database_path)) as connection:
        connection.execute("DROP TRIGGER system_events_reject_update")
        connection.execute("UPDATE system_events SET event_type = 'CHANGED' WHERE id = 1")
        connection.commit()
    manifest = json.loads(artifact.manifest_path.read_text(encoding="utf-8"))
    manifest["database_sha256"] = sha256(artifact.database_path.read_bytes()).hexdigest()
    artifact.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    with pytest.raises(BackupVerificationError, match="event chain"):
        verify_backup(artifact)


def test_restore_rechecks_destination_sidecars_immediately_before_publish(
    populated_database: Path,
    tmp_path: Path,
    monkeypatch,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")
    destination = tmp_path / "restored" / "tracker.sqlite3"
    original_copyfile = backup_module.shutil.copyfile

    def copyfile_then_activate_destination(source: Path, target: Path) -> str:
        copied = original_copyfile(source, target)
        destination.parent.mkdir(parents=True, exist_ok=True)
        Path(f"{destination}-wal").write_bytes(b"active")
        return copied

    monkeypatch.setattr(backup_module.shutil, "copyfile", copyfile_then_activate_destination)

    with pytest.raises(BackupVerificationError, match="sidecar"):
        restore_verified_backup(artifact, destination)

    assert not destination.exists()


def test_restore_refuses_database_owned_by_running_application(
    settings: Settings,
    tmp_path: Path,
) -> None:
    with TestClient(
        create_app(settings),
        client=("127.0.0.1", 50_000),
    ):
        artifact = create_verified_backup(settings.database_path, tmp_path / "backups")

        with pytest.raises(BackupVerificationError, match="locked by a running app"):
            restore_verified_backup(artifact, settings.database_path)
