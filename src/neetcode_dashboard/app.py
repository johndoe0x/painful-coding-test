from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from hashlib import sha256
from ipaddress import ip_address
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Engine
from starlette.responses import Response
from starlette.templating import Jinja2Templates

from neetcode_dashboard.calendar_engine import (
    CalendarSummary,
    load_holiday_rules,
    summarize_plan,
)
from neetcode_dashboard.config import Settings, ensure_runtime_directories
from neetcode_dashboard.db.engine import DatabaseHealth, create_sqlite_engine, database_health
from neetcode_dashboard.db.migrations import upgrade_database
from neetcode_dashboard.db.seed import sync_holiday_rules
from neetcode_dashboard.event_store import EventStore
from neetcode_dashboard.resources import resource_path
from neetcode_dashboard.runtime_lock import acquire_database_runtime_lock

FOUNDATION_MODE: Literal["FOUNDATION_ONLY"] = "FOUNDATION_ONLY"
EXPECTED_REVISION = "0003_event_invariants"
EXPECTED_HOLIDAY_SHA256 = "94954366457290f050c1cfcda9719016f0fa9f2fd4957849061d785c2e517bdc"
PACKAGE_ROOT = Path(__file__).resolve().parent


class DatabaseStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    integrity: Literal["ok"]
    revision: str
    holiday_count: int


class CalendarStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    days: int
    base_hours: int
    adjusted_hours: int
    holiday_count: int


class HealthResponse(BaseModel):
    model_config = ConfigDict(frozen=True)

    status: Literal["ok"]
    mode: Literal["FOUNDATION_ONLY"]
    database: DatabaseStatus
    calendar: CalendarStatus


def create_app(settings: Settings | None = None) -> FastAPI:
    runtime_settings = settings or Settings()

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncIterator[None]:
        ensure_runtime_directories(runtime_settings)
        holiday_rules = load_holiday_rules(_verified_holiday_source(resource_path("holidays.json")))
        calendar_summary = summarize_plan(holiday_rules)
        _require_calendar_contract(calendar_summary, len(holiday_rules))
        with acquire_database_runtime_lock(runtime_settings.database_path):
            upgrade_database(runtime_settings.database_path)
            engine = create_sqlite_engine(runtime_settings.database_path)
            try:
                sync_holiday_rules(engine, holiday_rules)
                _require_database_contract(database_health(engine))
                application.state.engine = engine
                application.state.calendar_summary = calendar_summary
                application.state.holiday_count = len(holiday_rules)
                yield
            finally:
                engine.dispose()

    application = FastAPI(
        title="NeetCode 500 Dashboard",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        lifespan=lifespan,
    )
    application.mount(
        "/static",
        StaticFiles(directory=PACKAGE_ROOT / "static"),
        name="static",
    )
    templates = Jinja2Templates(directory=PACKAGE_ROOT / "templates")

    @application.middleware("http")
    async def enforce_loopback_client(
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        client = request.client
        try:
            is_loopback = client is not None and ip_address(client.host).is_loopback
        except ValueError:
            is_loopback = False
        if not is_loopback:
            return JSONResponse(status_code=403, content={"detail": "loopback clients only"})
        return await call_next(request)

    @application.get("/api/health", response_model=HealthResponse)
    def health_endpoint(request: Request) -> HealthResponse:
        health = _live_database_health(request.app)
        summary = _state_calendar_summary(request.app)
        holiday_count = _state_holiday_count(request.app)
        return HealthResponse(
            status="ok",
            mode=FOUNDATION_MODE,
            database=DatabaseStatus(
                integrity="ok",
                revision=health.revision or "",
                holiday_count=health.holiday_count,
            ),
            calendar=CalendarStatus(
                days=summary.days,
                base_hours=summary.base_minutes // 60,
                adjusted_hours=summary.adjusted_minutes // 60,
                holiday_count=holiday_count,
            ),
        )

    @application.get("/", response_class=HTMLResponse)
    def foundation_page(request: Request) -> Response:
        return templates.TemplateResponse(
            request=request,
            name="foundation.html",
            context={
                "mode": FOUNDATION_MODE,
                "database": _live_database_health(request.app),
                "calendar": _state_calendar_summary(request.app),
                "holiday_count": _state_holiday_count(request.app),
            },
        )

    return application


def _require_calendar_contract(summary: CalendarSummary, holiday_count: int) -> None:
    contract = (
        summary.days,
        summary.base_minutes,
        summary.adjusted_minutes,
        holiday_count,
    )
    if contract != (365, 1_304 * 60, 1_292 * 60, 22):
        raise RuntimeError(f"calendar contract mismatch: {contract}")


def _verified_holiday_source(path: Path) -> Path:
    try:
        digest = sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        raise RuntimeError("frozen holiday source is unavailable") from error
    if digest != EXPECTED_HOLIDAY_SHA256:
        raise RuntimeError("frozen holiday source digest mismatch")
    return path


def _require_database_contract(health: DatabaseHealth) -> None:
    if health.integrity != "ok":
        raise RuntimeError(f"database integrity check failed: {health.integrity}")
    if health.revision != EXPECTED_REVISION:
        raise RuntimeError(f"database revision mismatch: {health.revision}")
    if health.holiday_count != 22:
        raise RuntimeError(f"database holiday seed mismatch: {health.holiday_count}")


def _live_database_health(application: FastAPI) -> DatabaseHealth:
    try:
        engine = _state_engine(application)
        health = database_health(engine)
        _require_database_contract(health)
        EventStore(engine).verify_all()
    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail="foundation dependency check failed",
        ) from error
    return health


def _state_engine(application: FastAPI) -> Engine:
    engine = application.state.engine
    if not isinstance(engine, Engine):
        raise RuntimeError("database engine is unavailable")
    return engine


def _state_calendar_summary(application: FastAPI) -> CalendarSummary:
    summary = application.state.calendar_summary
    if not isinstance(summary, CalendarSummary):
        raise RuntimeError("calendar summary is unavailable")
    return summary


def _state_holiday_count(application: FastAPI) -> int:
    holiday_count = application.state.holiday_count
    if not isinstance(holiday_count, int):
        raise RuntimeError("holiday count is unavailable")
    return holiday_count
