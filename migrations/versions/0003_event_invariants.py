"""Harden append-only event invariants.

Revision ID: 0003_event_invariants
Revises: 0002_system_events
Create Date: 2026-08-06
"""

from collections.abc import Sequence

from alembic import op

revision: str = "0003_event_invariants"
down_revision: str | None = "0002_system_events"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TRIGGER system_events_reject_insert_collision
        BEFORE INSERT ON system_events
        WHEN EXISTS (
            SELECT 1
            FROM system_events
            WHERE id = NEW.id
               OR (stream_id = NEW.stream_id AND event_seq = NEW.event_seq)
               OR event_sha256 = NEW.event_sha256
        )
        BEGIN
            SELECT RAISE(ABORT, 'system_events are append-only');
        END
        """
    )


def downgrade() -> None:
    op.execute("DROP TRIGGER IF EXISTS system_events_reject_insert_collision")
