"""Create append-only system events.

Revision ID: 0002_system_events
Revises: 0001_calendar_exceptions
Create Date: 2026-08-06
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0002_system_events"
down_revision: str | None = "0001_calendar_exceptions"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "system_events",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("stream_id", sa.String(length=200), nullable=False),
        sa.Column("event_seq", sa.Integer(), nullable=False),
        sa.Column("event_type", sa.String(length=100), nullable=False),
        sa.Column("schema_version", sa.Integer(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
        sa.Column("payload_sha256", sa.String(length=64), nullable=False),
        sa.Column("previous_event_sha256", sa.String(length=64), nullable=True),
        sa.Column("event_sha256", sa.String(length=64), nullable=False),
        sa.Column("occurred_at_utc", sa.String(length=32), nullable=False),
        sa.Column("received_at_utc", sa.String(length=32), nullable=False),
        sa.Column("study_date", sa.Date(), nullable=False),
        sa.CheckConstraint("event_seq > 0", name="ck_system_events_event_seq"),
        sa.CheckConstraint("schema_version > 0", name="ck_system_events_schema_version"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("event_sha256", name="uq_system_events_event_sha256"),
        sa.UniqueConstraint(
            "stream_id",
            "event_seq",
            name="uq_system_events_stream_sequence",
        ),
    )
    op.create_index("ix_system_events_event_type", "system_events", ["event_type"])
    op.create_index(
        "ix_system_events_occurred_at_utc",
        "system_events",
        ["occurred_at_utc"],
    )
    op.create_index("ix_system_events_stream_sequence", "system_events", ["stream_id", "event_seq"])
    op.create_index("ix_system_events_study_date", "system_events", ["study_date"])
    op.execute(
        """
        CREATE TRIGGER system_events_reject_update
        BEFORE UPDATE ON system_events
        BEGIN
            SELECT RAISE(ABORT, 'system_events are append-only');
        END
        """
    )
    op.execute(
        """
        CREATE TRIGGER system_events_reject_delete
        BEFORE DELETE ON system_events
        BEGIN
            SELECT RAISE(ABORT, 'system_events are append-only');
        END
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS system_events_reject_delete")
    op.execute("DROP TRIGGER IF EXISTS system_events_reject_update")
    op.drop_index("ix_system_events_study_date", table_name="system_events")
    op.drop_index("ix_system_events_stream_sequence", table_name="system_events")
    op.drop_index("ix_system_events_occurred_at_utc", table_name="system_events")
    op.drop_index("ix_system_events_event_type", table_name="system_events")
    op.drop_table("system_events")
