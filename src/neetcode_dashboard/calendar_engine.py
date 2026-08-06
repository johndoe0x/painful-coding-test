from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date as Date
from datetime import timedelta
from pathlib import Path
from types import MappingProxyType
from typing import Literal, cast

PLAN_START = Date(2026, 8, 6)
PLAN_END = Date(2027, 8, 5)
PLAN_DAY_COUNT = 365

HolidayKind = Literal["named_public_holiday", "holiday_period", "substitute_holiday"]
VALID_HOLIDAY_KINDS: frozenset[str] = frozenset(
    {"named_public_holiday", "holiday_period", "substitute_holiday"}
)
REQUIRED_HOLIDAY_FIELDS = frozenset(
    {
        "date",
        "kind",
        "name_ko",
        "name_en",
        "planned_minutes",
        "source",
        "source_as_of",
        "active",
    }
)


class CalendarDataError(ValueError):
    """Raised when the frozen calendar source is malformed or ambiguous."""


@dataclass(frozen=True, slots=True)
class HolidayRule:
    date: Date
    kind: HolidayKind
    name_ko: str
    name_en: str
    planned_minutes: int
    source: str
    source_as_of: Date
    active: bool


@dataclass(frozen=True, slots=True)
class CalendarDay:
    date: Date
    base_minutes: int
    planned_minutes: int
    holiday: HolidayRule | None


@dataclass(frozen=True, slots=True)
class CalendarSummary:
    start_date: Date
    end_date: Date
    days: int
    base_minutes: int
    adjusted_minutes: int
    monthly_adjusted_minutes: Mapping[str, int]
    calendar_days: tuple[CalendarDay, ...]


def load_holiday_rules(path: Path) -> tuple[HolidayRule, ...]:
    try:
        raw_data = cast(object, json.loads(path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as error:
        raise CalendarDataError(f"unable to load holiday data from {path}: {error}") from error

    if not isinstance(raw_data, list):
        raise CalendarDataError("holiday data must be a JSON array")

    rules: list[HolidayRule] = []
    seen_dates: set[Date] = set()
    for index, item in enumerate(cast(list[object], raw_data)):
        record = _holiday_record(item, index)
        rule = _parse_holiday_rule(record, index)
        if rule.date in seen_dates:
            raise CalendarDataError(f"duplicate holiday date: {rule.date.isoformat()}")
        seen_dates.add(rule.date)
        rules.append(rule)

    return tuple(rules)


def planned_minutes(day: Date, holidays: Sequence[HolidayRule]) -> int:
    holiday = _index_holidays(holidays).get(day)
    if holiday is not None and holiday.active:
        return holiday.planned_minutes
    return _base_minutes(day)


def summarize_plan(holidays: Sequence[HolidayRule]) -> CalendarSummary:
    day_count = (PLAN_END - PLAN_START).days + 1
    if day_count != PLAN_DAY_COUNT:
        raise CalendarDataError(f"plan interval must contain {PLAN_DAY_COUNT} inclusive days")

    holidays_by_date = _index_holidays(holidays)
    calendar_days: list[CalendarDay] = []
    monthly_adjusted_minutes: dict[str, int] = {}
    base_total = 0
    adjusted_total = 0

    current = PLAN_START
    while current <= PLAN_END:
        base = _base_minutes(current)
        rule = holidays_by_date.get(current)
        active_rule = rule if rule is not None and rule.active else None
        adjusted = active_rule.planned_minutes if active_rule is not None else base
        month = current.strftime("%Y-%m")

        base_total += base
        adjusted_total += adjusted
        monthly_adjusted_minutes[month] = monthly_adjusted_minutes.get(month, 0) + adjusted
        calendar_days.append(
            CalendarDay(
                date=current,
                base_minutes=base,
                planned_minutes=adjusted,
                holiday=active_rule,
            )
        )
        current += timedelta(days=1)

    return CalendarSummary(
        start_date=PLAN_START,
        end_date=PLAN_END,
        days=day_count,
        base_minutes=base_total,
        adjusted_minutes=adjusted_total,
        monthly_adjusted_minutes=MappingProxyType(monthly_adjusted_minutes.copy()),
        calendar_days=tuple(calendar_days),
    )


def _holiday_record(item: object, index: int) -> dict[str, object]:
    if not isinstance(item, dict) or not all(isinstance(key, str) for key in item):
        raise CalendarDataError(f"holiday record {index} must be a JSON object")
    record = cast(dict[str, object], item)
    fields = set(record)
    if fields != REQUIRED_HOLIDAY_FIELDS:
        missing = sorted(REQUIRED_HOLIDAY_FIELDS - fields)
        extra = sorted(fields - REQUIRED_HOLIDAY_FIELDS)
        raise CalendarDataError(
            f"holiday record {index} has invalid fields; missing={missing}, extra={extra}"
        )
    return record


def _parse_holiday_rule(record: Mapping[str, object], index: int) -> HolidayRule:
    raw_date = _required_text(record, "date", index)
    try:
        holiday_date = Date.fromisoformat(raw_date)
    except ValueError as error:
        raise CalendarDataError(f"holiday record {index} has an invalid date") from error
    if not PLAN_START <= holiday_date <= PLAN_END:
        raise CalendarDataError(f"holiday date is outside the plan interval: {raw_date}")

    raw_kind = _required_text(record, "kind", index)
    if raw_kind not in VALID_HOLIDAY_KINDS:
        raise CalendarDataError(f"holiday record {index} has an invalid kind: {raw_kind}")

    name_ko = _required_bilingual_name(record, "name_ko", index)
    name_en = _required_bilingual_name(record, "name_en", index)
    raw_minutes = record["planned_minutes"]
    if (
        not isinstance(raw_minutes, int)
        or isinstance(raw_minutes, bool)
        or not 1 <= raw_minutes <= 1_440
    ):
        raise CalendarDataError(
            f"holiday record {index} planned_minutes must be between 1 and 1440"
        )

    source = _required_text(record, "source", index)
    raw_source_as_of = _required_text(record, "source_as_of", index)
    try:
        source_as_of = Date.fromisoformat(raw_source_as_of)
    except ValueError as error:
        raise CalendarDataError(f"holiday record {index} has an invalid source_as_of") from error

    active = record["active"]
    if not isinstance(active, bool):
        raise CalendarDataError(f"holiday record {index} active must be a boolean")

    return HolidayRule(
        date=holiday_date,
        kind=cast(HolidayKind, raw_kind),
        name_ko=name_ko,
        name_en=name_en,
        planned_minutes=raw_minutes,
        source=source,
        source_as_of=source_as_of,
        active=active,
    )


def _required_text(record: Mapping[str, object], field: str, index: int) -> str:
    value = record[field]
    if not isinstance(value, str) or not value.strip():
        raise CalendarDataError(f"holiday record {index} {field} must be non-empty text")
    return value.strip()


def _required_bilingual_name(record: Mapping[str, object], field: str, index: int) -> str:
    value = record[field]
    if not isinstance(value, str) or not value.strip():
        raise CalendarDataError(f"holiday record {index} requires non-empty bilingual names")
    return value.strip()


def _index_holidays(holidays: Sequence[HolidayRule]) -> dict[Date, HolidayRule]:
    indexed: dict[Date, HolidayRule] = {}
    for rule in holidays:
        if rule.date in indexed:
            raise CalendarDataError(f"duplicate holiday date: {rule.date.isoformat()}")
        indexed[rule.date] = rule
    return indexed


def _base_minutes(day: Date) -> int:
    weekday = day.weekday()
    if weekday < 5:
        return 240
    if weekday == 5:
        return 180
    return 120
