from datetime import UTC, date, datetime
from zoneinfo import ZoneInfo

STUDY_TIME_ZONE = ZoneInfo("Asia/Seoul")


def utc_now() -> datetime:
    return datetime.now(UTC)


def study_date(instant: datetime) -> date:
    if instant.tzinfo is None or instant.utcoffset() is None:
        raise ValueError("study_date requires a timezone-aware datetime")
    return instant.astimezone(STUDY_TIME_ZONE).date()
