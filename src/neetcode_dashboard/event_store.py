from __future__ import annotations

import json
import sqlite3
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from datetime import date as Date
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import cast

from sqlalchemy import Engine

from neetcode_dashboard.db.engine import apply_sqlite_pragmas
from neetcode_dashboard.time import study_date, utc_now


class EventValidationError(ValueError):
    """Raised when an event cannot be represented canonically."""


class EventIntegrityError(RuntimeError):
    """Raised when stored event evidence does not verify."""


@dataclass(frozen=True, slots=True)
class EventToAppend:
    stream_id: str
    event_type: str
    payload: Mapping[str, object]
    occurred_at_utc: datetime
    schema_version: int = 1

    def __post_init__(self) -> None:
        stream_id = _required_identifier("stream_id", self.stream_id)
        event_type = _required_identifier("event_type", self.event_type)
        if (
            not isinstance(self.schema_version, int)
            or isinstance(self.schema_version, bool)
            or self.schema_version < 1
        ):
            raise EventValidationError("schema_version must be a positive integer")
        if self.occurred_at_utc.tzinfo is None or self.occurred_at_utc.utcoffset() is None:
            raise EventValidationError("occurred_at_utc must be timezone-aware")

        payload = _normalize_payload(self.payload)
        object.__setattr__(self, "stream_id", stream_id)
        object.__setattr__(self, "event_type", event_type)
        object.__setattr__(self, "payload", payload)
        object.__setattr__(self, "occurred_at_utc", self.occurred_at_utc.astimezone(UTC))


@dataclass(frozen=True, slots=True)
class StoredEvent:
    id: int
    stream_id: str
    event_seq: int
    event_type: str
    schema_version: int
    payload: Mapping[str, object]
    payload_json: str
    payload_sha256: str
    previous_event_sha256: str | None
    event_sha256: str
    occurred_at_utc: datetime
    received_at_utc: datetime
    study_date: Date


class EventStore:
    def __init__(self, engine: Engine) -> None:
        if engine.dialect.name != "sqlite":
            raise ValueError("EventStore requires a SQLite engine")
        database = engine.url.database
        if database is None or database == ":memory:":
            raise ValueError("EventStore requires a file-backed SQLite database")
        self._database_path = Path(database).expanduser().resolve()

    def append(self, event: EventToAppend) -> StoredEvent:
        payload_json = _canonical_payload_json(event.payload)
        payload_sha256 = sha256(payload_json.encode("utf-8")).hexdigest()
        occurred_at_utc = _format_utc(event.occurred_at_utc)
        received_at = utc_now()
        received_at_utc = _format_utc(received_at)
        local_study_date = study_date(event.occurred_at_utc)
        connection = self._connect()

        try:
            connection.execute("BEGIN IMMEDIATE")
            latest = connection.execute(
                """
                SELECT event_seq, event_sha256
                FROM system_events
                WHERE stream_id = ?
                ORDER BY event_seq DESC
                LIMIT 1
                """,
                (event.stream_id,),
            ).fetchone()
            if latest is None:
                event_seq = 1
                previous_event_sha256 = None
            else:
                event_seq = _row_int(latest, "event_seq") + 1
                previous_event_sha256 = _row_text(latest, "event_sha256")

            event_sha256 = _event_sha256(
                stream_id=event.stream_id,
                event_seq=event_seq,
                event_type=event.event_type,
                schema_version=event.schema_version,
                payload_json=payload_json,
                payload_sha256=payload_sha256,
                previous_event_sha256=previous_event_sha256,
                occurred_at_utc=occurred_at_utc,
                received_at_utc=received_at_utc,
                local_study_date=local_study_date.isoformat(),
            )
            cursor = connection.execute(
                """
                INSERT INTO system_events (
                    stream_id, event_seq, event_type, schema_version,
                    payload_json, payload_sha256, previous_event_sha256,
                    event_sha256, occurred_at_utc, received_at_utc, study_date
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event.stream_id,
                    event_seq,
                    event.event_type,
                    event.schema_version,
                    payload_json,
                    payload_sha256,
                    previous_event_sha256,
                    event_sha256,
                    occurred_at_utc,
                    received_at_utc,
                    local_study_date.isoformat(),
                ),
            )
            row_id = cursor.lastrowid
            cursor.close()
            if row_id is None:
                raise EventIntegrityError("SQLite did not return an event row id")
            connection.execute("COMMIT")
        except BaseException:
            if connection.in_transaction:
                connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()

        return StoredEvent(
            id=row_id,
            stream_id=event.stream_id,
            event_seq=event_seq,
            event_type=event.event_type,
            schema_version=event.schema_version,
            payload=event.payload,
            payload_json=payload_json,
            payload_sha256=payload_sha256,
            previous_event_sha256=previous_event_sha256,
            event_sha256=event_sha256,
            occurred_at_utc=event.occurred_at_utc,
            received_at_utc=received_at,
            study_date=local_study_date,
        )

    def read_stream(self, stream_id: str) -> tuple[StoredEvent, ...]:
        normalized_stream_id = _required_identifier("stream_id", stream_id)
        connection = self._connect()
        try:
            rows = connection.execute(
                """
                SELECT id, stream_id, event_seq, event_type, schema_version,
                       payload_json, payload_sha256, previous_event_sha256,
                       event_sha256, occurred_at_utc, received_at_utc, study_date
                FROM system_events
                WHERE stream_id = ?
                ORDER BY event_seq ASC
                """,
                (normalized_stream_id,),
            ).fetchall()
        finally:
            connection.close()

        events = tuple(_stored_event_from_row(row) for row in rows)
        _verify_hash_chain(normalized_stream_id, events)
        return events

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            self._database_path,
            timeout=5.0,
            autocommit=True,
            check_same_thread=False,
        )
        try:
            apply_sqlite_pragmas(connection)
            connection.row_factory = sqlite3.Row
            return connection
        except BaseException:
            connection.close()
            raise


def _required_identifier(field: str, value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EventValidationError(f"{field} must be non-empty text")
    return value.strip()


def _normalize_payload(payload: object) -> Mapping[str, object]:
    if not isinstance(payload, Mapping):
        raise EventValidationError("payload must be a JSON object")
    canonical = _canonical_payload_json(cast(Mapping[str, object], payload))
    decoded = cast(object, json.loads(canonical))
    if not isinstance(decoded, dict):
        raise EventValidationError("payload must be a JSON object")
    return MappingProxyType(cast(dict[str, object], decoded))


def _canonical_payload_json(payload: Mapping[str, object]) -> str:
    try:
        return json.dumps(
            dict(payload),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as error:
        raise EventValidationError(f"payload must be JSON-serializable: {error}") from error


def _event_sha256(
    *,
    stream_id: str,
    event_seq: int,
    event_type: str,
    schema_version: int,
    payload_json: str,
    payload_sha256: str,
    previous_event_sha256: str | None,
    occurred_at_utc: str,
    received_at_utc: str,
    local_study_date: str,
) -> str:
    material = json.dumps(
        {
            "event_seq": event_seq,
            "event_type": event_type,
            "occurred_at_utc": occurred_at_utc,
            "payload_json": payload_json,
            "payload_sha256": payload_sha256,
            "previous_event_sha256": previous_event_sha256,
            "received_at_utc": received_at_utc,
            "schema_version": schema_version,
            "stream_id": stream_id,
            "study_date": local_study_date,
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return sha256(material.encode("utf-8")).hexdigest()


def _stored_event_from_row(row: sqlite3.Row) -> StoredEvent:
    payload_json = _row_text(row, "payload_json")
    payload = _normalize_payload(cast(object, json.loads(payload_json)))
    return StoredEvent(
        id=_row_int(row, "id"),
        stream_id=_row_text(row, "stream_id"),
        event_seq=_row_int(row, "event_seq"),
        event_type=_row_text(row, "event_type"),
        schema_version=_row_int(row, "schema_version"),
        payload=payload,
        payload_json=payload_json,
        payload_sha256=_row_text(row, "payload_sha256"),
        previous_event_sha256=_row_optional_text(row, "previous_event_sha256"),
        event_sha256=_row_text(row, "event_sha256"),
        occurred_at_utc=_parse_utc(_row_text(row, "occurred_at_utc")),
        received_at_utc=_parse_utc(_row_text(row, "received_at_utc")),
        study_date=Date.fromisoformat(_row_text(row, "study_date")),
    )


def _verify_hash_chain(stream_id: str, events: tuple[StoredEvent, ...]) -> None:
    previous_event_sha256: str | None = None
    for expected_sequence, event in enumerate(events, start=1):
        if event.stream_id != stream_id or event.event_seq != expected_sequence:
            raise EventIntegrityError(f"event sequence is not contiguous for stream {stream_id}")
        if event.previous_event_sha256 != previous_event_sha256:
            raise EventIntegrityError(f"previous event hash mismatch for stream {stream_id}")

        canonical_payload = _canonical_payload_json(event.payload)
        if canonical_payload != event.payload_json:
            raise EventIntegrityError(f"non-canonical payload for stream {stream_id}")
        expected_payload_sha256 = sha256(canonical_payload.encode("utf-8")).hexdigest()
        if expected_payload_sha256 != event.payload_sha256:
            raise EventIntegrityError(f"payload hash mismatch for stream {stream_id}")

        expected_event_sha256 = _event_sha256(
            stream_id=event.stream_id,
            event_seq=event.event_seq,
            event_type=event.event_type,
            schema_version=event.schema_version,
            payload_json=event.payload_json,
            payload_sha256=event.payload_sha256,
            previous_event_sha256=event.previous_event_sha256,
            occurred_at_utc=_format_utc(event.occurred_at_utc),
            received_at_utc=_format_utc(event.received_at_utc),
            local_study_date=event.study_date.isoformat(),
        )
        if expected_event_sha256 != event.event_sha256:
            raise EventIntegrityError(f"event hash mismatch for stream {stream_id}")
        previous_event_sha256 = event.event_sha256


def _format_utc(value: datetime) -> str:
    return value.astimezone(UTC).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _parse_utc(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise EventIntegrityError(f"invalid UTC timestamp: {value}") from error
    if parsed.tzinfo is None or parsed.utcoffset() != datetime.min.replace(tzinfo=UTC).utcoffset():
        raise EventIntegrityError(f"timestamp is not UTC: {value}")
    return parsed.astimezone(UTC)


def _row_int(row: sqlite3.Row, field: str) -> int:
    value = cast(object, row[field])
    if not isinstance(value, int) or isinstance(value, bool):
        raise EventIntegrityError(f"{field} is not an integer")
    return value


def _row_text(row: sqlite3.Row, field: str) -> str:
    value = cast(object, row[field])
    if not isinstance(value, str):
        raise EventIntegrityError(f"{field} is not text")
    return value


def _row_optional_text(row: sqlite3.Row, field: str) -> str | None:
    value = cast(object, row[field])
    if value is None:
        return None
    if not isinstance(value, str):
        raise EventIntegrityError(f"{field} is not nullable text")
    return value
