import json
from dataclasses import FrozenInstanceError
from datetime import date
from pathlib import Path

import pytest

from neetcode_dashboard.calendar_engine import (
    CalendarDataError,
    load_holiday_rules,
    planned_minutes,
    summarize_plan,
)


def test_plan_capacity_matches_frozen_master_plan(holiday_path: Path) -> None:
    holidays = load_holiday_rules(holiday_path)

    summary = summarize_plan(holidays)

    assert summary.days == 365
    assert summary.base_minutes == 1_304 * 60
    assert summary.adjusted_minutes == 1_292 * 60
    assert len(holidays) == 22


def test_named_holidays_override_weekday_and_sunday(holiday_path: Path) -> None:
    holidays = load_holiday_rules(holiday_path)

    assert planned_minutes(date(2026, 8, 17), holidays) == 180
    assert planned_minutes(date(2027, 2, 7), holidays) == 180
    assert planned_minutes(date(2027, 5, 3), holidays) == 180
    assert planned_minutes(date(2027, 7, 19), holidays) == 180


def test_bilingual_holiday_names_match_frozen_master_plan(holiday_path: Path) -> None:
    holidays = load_holiday_rules(holiday_path)

    assert [(rule.date.isoformat(), rule.name_ko, rule.name_en) for rule in holidays] == [
        ("2026-08-15", "광복절", "Liberation Day"),
        ("2026-08-17", "광복절 대체공휴일", "Substitute holiday for Liberation Day"),
        ("2026-09-24", "추석 연휴", "Chuseok holiday"),
        ("2026-09-25", "추석", "Chuseok"),
        ("2026-09-26", "추석 연휴", "Chuseok holiday"),
        ("2026-10-03", "개천절", "National Foundation Day"),
        (
            "2026-10-05",
            "개천절 대체공휴일",
            "Substitute holiday for National Foundation Day",
        ),
        ("2026-10-09", "한글날", "Hangeul Day"),
        ("2026-12-25", "기독탄신일", "Christmas Day"),
        ("2027-01-01", "신정", "New Year's Day"),
        ("2027-02-06", "설날 연휴", "Seollal holiday"),
        ("2027-02-07", "설날", "Seollal"),
        ("2027-02-08", "설날 연휴", "Seollal holiday"),
        ("2027-02-09", "설날 대체공휴일", "Substitute holiday for Seollal"),
        ("2027-03-01", "3·1절", "Independence Movement Day"),
        ("2027-05-01", "노동절", "Labor Day"),
        ("2027-05-03", "노동절 대체공휴일", "Substitute holiday for Labor Day"),
        ("2027-05-05", "어린이날", "Children's Day"),
        ("2027-05-13", "부처님오신날", "Buddha's Birthday"),
        ("2027-06-06", "현충일", "Memorial Day"),
        ("2027-07-17", "제헌절", "Constitution Day"),
        (
            "2027-07-19",
            "제헌절 대체공휴일",
            "Substitute holiday for Constitution Day",
        ),
    ]


def test_monthly_adjusted_hours_match_master_plan(holiday_path: Path) -> None:
    summary = summarize_plan(load_holiday_rules(holiday_path))

    assert summary.monthly_adjusted_minutes == {
        "2026-08": 91 * 60,
        "2026-09": 106 * 60,
        "2026-10": 109 * 60,
        "2026-11": 106 * 60,
        "2026-12": 111 * 60,
        "2027-01": 108 * 60,
        "2027-02": 99 * 60,
        "2027-03": 111 * 60,
        "2027-04": 108 * 60,
        "2027-05": 106 * 60,
        "2027-06": 109 * 60,
        "2027-07": 110 * 60,
        "2027-08": 18 * 60,
    }


def test_loaded_rules_and_summary_are_immutable(holiday_path: Path) -> None:
    holidays = load_holiday_rules(holiday_path)
    summary = summarize_plan(holidays)

    assert isinstance(holidays, tuple)
    with pytest.raises(FrozenInstanceError):
        holidays[0].planned_minutes = 120  # type: ignore[misc]
    with pytest.raises(TypeError):
        summary.monthly_adjusted_minutes["2026-08"] = 0  # type: ignore[index]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("planned_minutes", 0, "planned_minutes"),
        ("name_ko", "", "bilingual"),
        ("name_en", "", "bilingual"),
    ],
)
def test_invalid_holiday_records_are_rejected(
    tmp_path: Path,
    holiday_path: Path,
    field: str,
    value: object,
    message: str,
) -> None:
    records = json.loads(holiday_path.read_text(encoding="utf-8"))
    records[0][field] = value
    invalid_path = tmp_path / "holidays.json"
    invalid_path.write_text(json.dumps(records), encoding="utf-8")

    with pytest.raises(CalendarDataError, match=message):
        load_holiday_rules(invalid_path)


def test_duplicate_holiday_dates_are_rejected(tmp_path: Path, holiday_path: Path) -> None:
    records = json.loads(holiday_path.read_text(encoding="utf-8"))
    records.append(records[0])
    invalid_path = tmp_path / "holidays.json"
    invalid_path.write_text(json.dumps(records), encoding="utf-8")

    with pytest.raises(CalendarDataError, match="duplicate"):
        load_holiday_rules(invalid_path)
