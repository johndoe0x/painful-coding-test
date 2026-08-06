from __future__ import annotations

import json
import os
import secrets
import shutil
import sqlite3
import tempfile
from contextlib import suppress
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from typing import cast

from neetcode_dashboard import __version__
from neetcode_dashboard.db.engine import apply_sqlite_pragmas
from neetcode_dashboard.time import utc_now

BACKUP_FORMAT_VERSION = 1
EXPECTED_PLAN_SHA256 = "1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_FIELDS = frozenset(
    {
        "format_version",
        "application_version",
        "schema_revision",
        "created_at_utc",
        "source_plan_sha256",
        "database_file",
        "database_sha256",
        "integrity_check",
        "event_count",
        "holiday_count",
    }
)


class BackupVerificationError(RuntimeError):
    """Raised when a backup or restore candidate cannot be proven safe."""


@dataclass(frozen=True, slots=True)
class BackupManifest:
    format_version: int
    application_version: str
    schema_revision: str
    created_at_utc: datetime
    source_plan_sha256: str
    database_file: str
    database_sha256: str
    integrity_check: str
    event_count: int
    holiday_count: int


@dataclass(frozen=True, slots=True)
class BackupArtifact:
    database_path: Path
    manifest_path: Path


@dataclass(frozen=True, slots=True)
class _DatabaseSnapshot:
    integrity_check: str
    schema_revision: str
    event_count: int
    holiday_count: int


def create_verified_backup(
    source_database: Path,
    backup_dir: Path,
    *,
    application_version: str = __version__,
) -> BackupArtifact:
    source = source_database.expanduser().resolve()
    if not source.is_file():
        raise BackupVerificationError(f"source database does not exist: {source}")
    if not application_version.strip():
        raise BackupVerificationError("application version must be non-empty")

    destination_dir = backup_dir.expanduser().resolve()
    destination_dir.mkdir(parents=True, exist_ok=True)
    created_at = utc_now()
    identifier = f"{created_at:%Y%m%dT%H%M%S%fZ}-{secrets.token_hex(4)}"
    final_database = destination_dir / f"backup-{identifier}.sqlite3"
    final_manifest = destination_dir / f"backup-{identifier}.manifest.json"
    temporary_database = _temporary_path(destination_dir, ".sqlite3.tmp")
    temporary_manifest = _temporary_path(destination_dir, ".manifest.json.tmp")
    published_database = False
    published_manifest = False

    try:
        _copy_with_sqlite_backup(source, temporary_database)
        snapshot = _inspect_database(temporary_database)
        database_sha256 = _file_sha256(temporary_database)
        manifest = BackupManifest(
            format_version=BACKUP_FORMAT_VERSION,
            application_version=application_version.strip(),
            schema_revision=snapshot.schema_revision,
            created_at_utc=created_at,
            source_plan_sha256=_verified_plan_sha256(),
            database_file=final_database.name,
            database_sha256=database_sha256,
            integrity_check=snapshot.integrity_check,
            event_count=snapshot.event_count,
            holiday_count=snapshot.holiday_count,
        )
        temporary_manifest.write_bytes(_manifest_bytes(manifest))
        _fsync_file(temporary_database)
        _fsync_file(temporary_manifest)

        os.replace(temporary_database, final_database)
        published_database = True
        _fsync_directory(destination_dir)
        os.replace(temporary_manifest, final_manifest)
        published_manifest = True
        _fsync_directory(destination_dir)

        artifact = BackupArtifact(final_database, final_manifest)
        verify_backup(artifact)
        return artifact
    except BaseException:
        _remove_generated_file(temporary_database)
        _remove_generated_file(temporary_manifest)
        _remove_sqlite_sidecars(temporary_database)
        if published_manifest:
            _remove_generated_file(final_manifest)
        if published_database:
            _remove_generated_file(final_database)
            _remove_sqlite_sidecars(final_database)
        raise


def verify_backup(artifact: BackupArtifact) -> BackupManifest:
    database_path = artifact.database_path.expanduser().resolve()
    manifest_path = artifact.manifest_path.expanduser().resolve()
    if not database_path.is_file():
        raise BackupVerificationError(f"backup database does not exist: {database_path}")
    if not manifest_path.is_file():
        raise BackupVerificationError(f"backup manifest does not exist: {manifest_path}")
    _reject_sqlite_sidecars(database_path, "backup")

    manifest = _read_manifest(manifest_path)
    if manifest.database_file != database_path.name:
        raise BackupVerificationError("manifest database filename does not match the artifact")
    if manifest.source_plan_sha256 != _verified_plan_sha256():
        raise BackupVerificationError("manifest source plan SHA-256 does not match PLAN.md")

    actual_sha256 = _file_sha256(database_path)
    if actual_sha256 != manifest.database_sha256:
        raise BackupVerificationError("backup database SHA-256 mismatch")
    snapshot = _inspect_database(database_path)
    if _file_sha256(database_path) != manifest.database_sha256:
        raise BackupVerificationError("backup database SHA-256 changed during verification")
    _verify_snapshot(manifest, snapshot)
    return manifest


def restore_verified_backup(artifact: BackupArtifact, destination: Path) -> Path:
    manifest = verify_backup(artifact)
    source = artifact.database_path.expanduser().resolve()
    target = destination.expanduser().resolve()
    if source == target:
        raise BackupVerificationError("restore destination cannot overwrite the backup artifact")
    _reject_sqlite_sidecars(target, "restore destination")
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary_destination = _temporary_path(target.parent, f".{target.name}.restore.tmp")

    try:
        shutil.copyfile(source, temporary_destination)
        _fsync_file(temporary_destination)
        if _file_sha256(temporary_destination) != manifest.database_sha256:
            raise BackupVerificationError("restore candidate SHA-256 mismatch")
        snapshot = _inspect_database(temporary_destination)
        if _file_sha256(temporary_destination) != manifest.database_sha256:
            raise BackupVerificationError("restore candidate SHA-256 changed during verification")
        _verify_snapshot(manifest, snapshot)

        os.replace(temporary_destination, target)
        _fsync_directory(target.parent)
        return target
    except BaseException:
        _remove_generated_file(temporary_destination)
        _remove_sqlite_sidecars(temporary_destination)
        raise


def _copy_with_sqlite_backup(source: Path, destination: Path) -> None:
    source_connection = _open_existing_database(source)
    destination_connection = sqlite3.connect(
        destination,
        timeout=5.0,
        autocommit=True,
        check_same_thread=False,
    )
    try:
        apply_sqlite_pragmas(destination_connection)
        source_connection.backup(destination_connection)
        destination_connection.execute("PRAGMA wal_checkpoint(TRUNCATE)").close()
    except sqlite3.Error as error:
        raise BackupVerificationError(f"SQLite backup failed: {error}") from error
    finally:
        destination_connection.close()
        source_connection.close()
    _remove_sqlite_sidecars(destination)


def _inspect_database(path: Path) -> _DatabaseSnapshot:
    connection = _open_existing_database(path)
    try:
        integrity_rows = connection.execute("PRAGMA integrity_check").fetchall()
        integrity_values = [_row_text(row, 0, "integrity_check") for row in integrity_rows]
        integrity_check = "ok" if integrity_values == ["ok"] else "; ".join(integrity_values)
        revision_row = connection.execute("SELECT version_num FROM alembic_version").fetchone()
        if revision_row is None:
            raise BackupVerificationError("database has no Alembic revision")
        schema_revision = _row_text(revision_row, 0, "schema_revision")
        event_count = _query_count(connection, "SELECT COUNT(*) FROM system_events")
        holiday_count = _query_count(connection, "SELECT COUNT(*) FROM calendar_exceptions")
    except sqlite3.Error as error:
        raise BackupVerificationError(f"database inspection failed: {error}") from error
    finally:
        connection.close()

    return _DatabaseSnapshot(
        integrity_check=integrity_check,
        schema_revision=schema_revision,
        event_count=event_count,
        holiday_count=holiday_count,
    )


def _open_existing_database(path: Path) -> sqlite3.Connection:
    database_path = path.expanduser().resolve()
    if not database_path.is_file():
        raise BackupVerificationError(f"database does not exist: {database_path}")
    try:
        connection = sqlite3.connect(
            f"{database_path.as_uri()}?mode=rw",
            uri=True,
            timeout=5.0,
            autocommit=True,
            check_same_thread=False,
        )
    except sqlite3.Error as error:
        raise BackupVerificationError(f"unable to open database: {error}") from error
    try:
        apply_sqlite_pragmas(connection)
        return connection
    except sqlite3.Error as error:
        connection.close()
        raise BackupVerificationError(f"unable to open database: {error}") from error


def _verify_snapshot(manifest: BackupManifest, snapshot: _DatabaseSnapshot) -> None:
    if snapshot.integrity_check != manifest.integrity_check or snapshot.integrity_check != "ok":
        raise BackupVerificationError("database integrity check mismatch")
    if snapshot.schema_revision != manifest.schema_revision:
        raise BackupVerificationError("database schema revision mismatch")
    if snapshot.event_count != manifest.event_count:
        raise BackupVerificationError("database event count mismatch")
    if snapshot.holiday_count != manifest.holiday_count:
        raise BackupVerificationError("database holiday count mismatch")


def _manifest_bytes(manifest: BackupManifest) -> bytes:
    record = {
        "application_version": manifest.application_version,
        "created_at_utc": _format_utc(manifest.created_at_utc),
        "database_file": manifest.database_file,
        "database_sha256": manifest.database_sha256,
        "event_count": manifest.event_count,
        "format_version": manifest.format_version,
        "holiday_count": manifest.holiday_count,
        "integrity_check": manifest.integrity_check,
        "schema_revision": manifest.schema_revision,
        "source_plan_sha256": manifest.source_plan_sha256,
    }
    return (
        json.dumps(
            record,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _read_manifest(path: Path) -> BackupManifest:
    try:
        raw = cast(object, json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as error:
        raise BackupVerificationError(f"unable to read backup manifest: {error}") from error
    if not isinstance(raw, dict) or not all(isinstance(key, str) for key in raw):
        raise BackupVerificationError("backup manifest must be a JSON object")
    record = cast(dict[str, object], raw)
    if set(record) != MANIFEST_FIELDS:
        raise BackupVerificationError("backup manifest fields do not match the format")

    format_version = _manifest_int(record, "format_version")
    if format_version != BACKUP_FORMAT_VERSION:
        raise BackupVerificationError("unsupported backup manifest format version")
    created_at = _parse_utc(_manifest_text(record, "created_at_utc"))
    source_plan_sha256 = _manifest_hash(record, "source_plan_sha256")
    database_sha256 = _manifest_hash(record, "database_sha256")
    event_count = _manifest_int(record, "event_count")
    holiday_count = _manifest_int(record, "holiday_count")
    if event_count < 0 or holiday_count < 0:
        raise BackupVerificationError("backup manifest row counts cannot be negative")

    return BackupManifest(
        format_version=format_version,
        application_version=_manifest_text(record, "application_version"),
        schema_revision=_manifest_text(record, "schema_revision"),
        created_at_utc=created_at,
        source_plan_sha256=source_plan_sha256,
        database_file=_manifest_text(record, "database_file"),
        database_sha256=database_sha256,
        integrity_check=_manifest_text(record, "integrity_check"),
        event_count=event_count,
        holiday_count=holiday_count,
    )


def _verified_plan_sha256() -> str:
    plan_path = PROJECT_ROOT / "PLAN.md"
    if not plan_path.is_file():
        raise BackupVerificationError("repository PLAN.md is missing")
    digest = _file_sha256(plan_path)
    if digest != EXPECTED_PLAN_SHA256:
        raise BackupVerificationError("repository PLAN.md SHA-256 is not the frozen contract")
    return digest


def _file_sha256(path: Path) -> str:
    digest = sha256()
    try:
        with path.open("rb") as source:
            for chunk in iter(lambda: source.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as error:
        raise BackupVerificationError(f"unable to hash {path}: {error}") from error
    return digest.hexdigest()


def _temporary_path(directory: Path, suffix: str) -> Path:
    descriptor, raw_path = tempfile.mkstemp(prefix=".neetcode-", suffix=suffix, dir=directory)
    os.close(descriptor)
    return Path(raw_path)


def _fsync_file(path: Path) -> None:
    with path.open("rb") as file_handle:
        os.fsync(file_handle.fileno())


def _fsync_directory(path: Path) -> None:
    descriptor = os.open(path, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _reject_sqlite_sidecars(database_path: Path, label: str) -> None:
    sidecars = [Path(f"{database_path}-wal"), Path(f"{database_path}-shm")]
    if any(sidecar.exists() for sidecar in sidecars):
        raise BackupVerificationError(f"{label} has an active or unclean SQLite sidecar")


def _remove_sqlite_sidecars(database_path: Path) -> None:
    _remove_generated_file(Path(f"{database_path}-wal"))
    _remove_generated_file(Path(f"{database_path}-shm"))


def _remove_generated_file(path: Path) -> None:
    with suppress(OSError):
        path.unlink(missing_ok=True)


def _query_count(connection: sqlite3.Connection, query: str) -> int:
    row = connection.execute(query).fetchone()
    if row is None:
        raise BackupVerificationError("database count query returned no row")
    value = cast(object, row[0])
    if not isinstance(value, int) or isinstance(value, bool):
        raise BackupVerificationError("database count query returned a non-integer")
    return value


def _row_text(row: tuple[object, ...], index: int, field: str) -> str:
    value = row[index]
    if not isinstance(value, str) or not value:
        raise BackupVerificationError(f"database {field} is not text")
    return value


def _manifest_text(record: dict[str, object], field: str) -> str:
    value = record[field]
    if not isinstance(value, str) or not value.strip():
        raise BackupVerificationError(f"manifest {field} must be non-empty text")
    return value.strip()


def _manifest_int(record: dict[str, object], field: str) -> int:
    value = record[field]
    if not isinstance(value, int) or isinstance(value, bool):
        raise BackupVerificationError(f"manifest {field} must be an integer")
    return value


def _manifest_hash(record: dict[str, object], field: str) -> str:
    value = _manifest_text(record, field)
    if len(value) != 64 or any(character not in "0123456789abcdef" for character in value):
        raise BackupVerificationError(f"manifest {field} must be a lowercase SHA-256")
    return value


def _format_utc(value: datetime) -> str:
    return value.astimezone(UTC).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _parse_utc(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise BackupVerificationError("manifest created_at_utc is invalid") from error
    if parsed.tzinfo is None or parsed.utcoffset() != datetime.min.replace(tzinfo=UTC).utcoffset():
        raise BackupVerificationError("manifest created_at_utc must be UTC")
    return parsed.astimezone(UTC)
