from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

import pytest
from sqlalchemy import Engine, text
from sqlalchemy.exc import DatabaseError

from neetcode_dashboard.event_store import (
    EventStore,
    EventToAppend,
    EventValidationError,
)


def test_events_are_sequenced_and_hash_chained(migrated_engine: Engine) -> None:
    store = EventStore(migrated_engine)
    first = store.append(
        EventToAppend(
            "system",
            "APP_STARTED",
            {"mode": "FOUNDATION_ONLY"},
            datetime(2026, 8, 5, 15, 0, tzinfo=UTC),
        )
    )
    second = store.append(
        EventToAppend(
            "system",
            "CALENDAR_READY",
            {"days": 365},
            datetime(2026, 8, 5, 15, 1, tzinfo=UTC),
        )
    )

    assert (first.event_seq, second.event_seq) == (1, 2)
    assert first.study_date.isoformat() == "2026-08-06"
    assert second.previous_event_sha256 == first.event_sha256
    assert [event.event_type for event in store.read_stream("system")] == [
        "APP_STARTED",
        "CALENDAR_READY",
    ]


def test_each_stream_has_an_independent_sequence(migrated_engine: Engine) -> None:
    store = EventStore(migrated_engine)
    occurred_at = datetime(2026, 8, 6, tzinfo=UTC)

    first_system = store.append(EventToAppend("system", "READY", {}, occurred_at))
    first_backup = store.append(EventToAppend("backup", "CREATED", {}, occurred_at))

    assert first_system.event_seq == 1
    assert first_backup.event_seq == 1
    assert first_system.previous_event_sha256 is None
    assert first_backup.previous_event_sha256 is None


def test_canonical_payload_hash_ignores_dictionary_key_order(migrated_engine: Engine) -> None:
    store = EventStore(migrated_engine)
    occurred_at = datetime(2026, 8, 6, tzinfo=UTC)

    first = store.append(EventToAppend("first", "DATA", {"b": 2, "a": 1}, occurred_at))
    second = store.append(EventToAppend("second", "DATA", {"a": 1, "b": 2}, occurred_at))

    assert first.payload_sha256 == second.payload_sha256


def test_event_value_objects_are_frozen(migrated_engine: Engine) -> None:
    event = EventStore(migrated_engine).append(
        EventToAppend("system", "READY", {}, datetime(2026, 8, 6, tzinfo=UTC))
    )

    with pytest.raises(FrozenInstanceError):
        event.event_type = "CHANGED"  # type: ignore[misc]


def test_reading_missing_stream_returns_empty_tuple(migrated_engine: Engine) -> None:
    store = EventStore(migrated_engine)
    store.append(EventToAppend("system", "READY", {}, datetime(2026, 8, 6, tzinfo=UTC)))

    assert store.read_stream("missing") == ()


def test_invalid_event_inputs_are_rejected() -> None:
    occurred_at = datetime(2026, 8, 6, tzinfo=UTC)

    with pytest.raises(EventValidationError, match="stream_id"):
        EventToAppend("", "READY", {}, occurred_at)
    with pytest.raises(EventValidationError, match="event_type"):
        EventToAppend("system", "", {}, occurred_at)
    with pytest.raises(EventValidationError, match="schema_version"):
        EventToAppend("system", "READY", {}, occurred_at, schema_version=0)
    with pytest.raises(EventValidationError, match="timezone-aware"):
        EventToAppend("system", "READY", {}, datetime(2026, 8, 6))
    with pytest.raises(EventValidationError, match="JSON"):
        EventToAppend("system", "READY", {"value": object()}, occurred_at)


def test_database_rejects_event_update_and_delete(migrated_engine: Engine) -> None:
    store = EventStore(migrated_engine)
    event = store.append(
        EventToAppend("system", "APP_STARTED", {}, datetime(2026, 8, 6, tzinfo=UTC))
    )

    with (
        pytest.raises(DatabaseError, match="append-only"),
        migrated_engine.begin() as connection,
    ):
        connection.execute(
            text("UPDATE system_events SET event_type='CHANGED' WHERE id=:id"),
            {"id": event.id},
        )
    with (
        pytest.raises(DatabaseError, match="append-only"),
        migrated_engine.begin() as connection,
    ):
        connection.execute(
            text("DELETE FROM system_events WHERE id=:id"),
            {"id": event.id},
        )
