from __future__ import annotations

from datetime import date as Date
from datetime import datetime

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    Index,
    Integer,
    String,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from neetcode_dashboard.db.base import Base


class CalendarException(Base):
    __tablename__ = "calendar_exceptions"
    __table_args__ = (
        CheckConstraint(
            "planned_minutes > 0 AND planned_minutes <= 1440",
            name="ck_calendar_exceptions_planned_minutes",
        ),
        CheckConstraint(
            "origin IN ('frozen_plan', 'manual')",
            name="ck_calendar_exceptions_origin",
        ),
        UniqueConstraint("date", name="uq_calendar_exceptions_date"),
        Index("ix_calendar_exceptions_date", "date"),
        Index("ix_calendar_exceptions_active", "active"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[Date] = mapped_column(nullable=False)
    kind: Mapped[str] = mapped_column(String(64), nullable=False)
    name_ko: Mapped[str] = mapped_column(String(200), nullable=False)
    name_en: Mapped[str] = mapped_column(String(240), nullable=False)
    planned_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    source: Mapped[str] = mapped_column(String(500), nullable=False)
    source_as_of: Mapped[Date] = mapped_column(nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    origin: Mapped[str] = mapped_column(String(32), nullable=False, default="frozen_plan")
    created_at_utc: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    updated_at_utc: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
