from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from alembic.runtime.migration import MigrationContext
from sqlalchemy import Engine, create_engine, event, text
from sqlalchemy.engine import URL
from sqlalchemy.engine.interfaces import DBAPIConnection
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import ConnectionPoolEntry


@dataclass(frozen=True, slots=True)
class DatabaseHealth:
    integrity: str
    revision: str | None
    holiday_count: int


def create_sqlite_engine(path: Path) -> Engine:
    database_path = path.expanduser().resolve()
    database_path.parent.mkdir(parents=True, exist_ok=True)
    url = URL.create("sqlite+pysqlite", database=str(database_path))
    engine = create_engine(
        url,
        connect_args={"autocommit": False, "check_same_thread": False},
    )

    @event.listens_for(engine, "connect")
    def configure_sqlite_connection(
        dbapi_connection: DBAPIConnection,
        _connection_record: ConnectionPoolEntry,
    ) -> None:
        if not isinstance(dbapi_connection, sqlite3.Connection):
            raise TypeError("dashboard persistence requires sqlite3 connections")

        previous_autocommit = dbapi_connection.autocommit
        dbapi_connection.autocommit = True
        try:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA synchronous=FULL")
            cursor.execute("PRAGMA busy_timeout=5000")
            cursor.close()
        finally:
            dbapi_connection.autocommit = previous_autocommit

    return engine


def session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, expire_on_commit=False)


def database_health(engine: Engine) -> DatabaseHealth:
    with engine.connect() as connection:
        integrity = str(connection.scalar(text("PRAGMA integrity_check")))
        revision = MigrationContext.configure(connection).get_current_revision()
        holiday_count = int(
            connection.scalar(text("SELECT COUNT(*) FROM calendar_exceptions")) or 0
        )
    return DatabaseHealth(
        integrity=integrity,
        revision=revision,
        holiday_count=holiday_count,
    )
