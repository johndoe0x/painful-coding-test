from collections.abc import Sequence

from sqlalchemy import Engine, select

from neetcode_dashboard.calendar_engine import HolidayRule
from neetcode_dashboard.db.engine import session_factory
from neetcode_dashboard.db.models import CalendarException
from neetcode_dashboard.time import utc_now

FROZEN_PLAN_ORIGIN = "frozen_plan"


def sync_holiday_rules(engine: Engine, rules: Sequence[HolidayRule]) -> None:
    sessions = session_factory(engine)
    with sessions.begin() as session:
        for rule in rules:
            existing = session.scalar(
                select(CalendarException).where(CalendarException.date == rule.date)
            )
            if existing is None:
                session.add(_calendar_exception(rule))
                continue
            if existing.origin != FROZEN_PLAN_ORIGIN:
                continue
            _refresh_static_fields(existing, rule)


def _calendar_exception(rule: HolidayRule) -> CalendarException:
    now = utc_now()
    return CalendarException(
        date=rule.date,
        kind=rule.kind,
        name_ko=rule.name_ko,
        name_en=rule.name_en,
        planned_minutes=rule.planned_minutes,
        source=rule.source,
        source_as_of=rule.source_as_of,
        active=rule.active,
        origin=FROZEN_PLAN_ORIGIN,
        created_at_utc=now,
        updated_at_utc=now,
    )


def _refresh_static_fields(existing: CalendarException, rule: HolidayRule) -> None:
    static_values: dict[str, object] = {
        "kind": rule.kind,
        "name_ko": rule.name_ko,
        "name_en": rule.name_en,
        "planned_minutes": rule.planned_minutes,
        "source": rule.source,
        "source_as_of": rule.source_as_of,
        "active": rule.active,
    }
    changed = False
    for field, value in static_values.items():
        if getattr(existing, field) != value:
            setattr(existing, field, value)
            changed = True
    if changed:
        existing.updated_at_utc = utc_now()
