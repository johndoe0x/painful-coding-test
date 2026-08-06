"""Create calendar exceptions.

Revision ID: 0001_calendar_exceptions
Revises:
Create Date: 2026-08-06
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001_calendar_exceptions"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "calendar_exceptions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("kind", sa.String(length=64), nullable=False),
        sa.Column("name_ko", sa.String(length=200), nullable=False),
        sa.Column("name_en", sa.String(length=240), nullable=False),
        sa.Column("planned_minutes", sa.Integer(), nullable=False),
        sa.Column("source", sa.String(length=500), nullable=False),
        sa.Column("source_as_of", sa.Date(), nullable=False),
        sa.Column("active", sa.Boolean(), server_default=sa.text("1"), nullable=False),
        sa.Column(
            "origin",
            sa.String(length=32),
            server_default=sa.text("'frozen_plan'"),
            nullable=False,
        ),
        sa.Column(
            "created_at_utc",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at_utc",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.CheckConstraint(
            "planned_minutes > 0 AND planned_minutes <= 1440",
            name="ck_calendar_exceptions_planned_minutes",
        ),
        sa.CheckConstraint(
            "origin IN ('frozen_plan', 'manual')",
            name="ck_calendar_exceptions_origin",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("date", name="uq_calendar_exceptions_date"),
    )
    op.create_index("ix_calendar_exceptions_active", "calendar_exceptions", ["active"])
    op.create_index("ix_calendar_exceptions_date", "calendar_exceptions", ["date"])


def downgrade() -> None:
    op.drop_index("ix_calendar_exceptions_date", table_name="calendar_exceptions")
    op.drop_index("ix_calendar_exceptions_active", table_name="calendar_exceptions")
    op.drop_table("calendar_exceptions")
