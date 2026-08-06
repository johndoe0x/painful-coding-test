import json
import sqlite3
from pathlib import Path

import pytest

from neetcode_dashboard.backup import (
    BackupVerificationError,
    create_verified_backup,
    restore_verified_backup,
    verify_backup,
)


def test_backup_and_restore_preserve_committed_rows(
    populated_database: Path,
    tmp_path: Path,
) -> None:
    artifact = create_verified_backup(populated_database, tmp_path / "backups")

    manifest = verify_backup(artifact)

    assert manifest.integrity_check == "ok"
    assert manifest.schema_revision == "0002_system_events"
    assert manifest.event_count == 2
    assert manifest.holiday_count == 22
    restored = tmp_path / "restored" / "tracker.sqlite3"
    restore_verified_backup(artifact, restored)
    with sqlite3.connect(restored) as connection:
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
