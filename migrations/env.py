from __future__ import annotations

from pathlib import Path

from alembic import context
from sqlalchemy.engine import make_url

from neetcode_dashboard.db import models  # noqa: F401
from neetcode_dashboard.db.base import Base
from neetcode_dashboard.db.engine import create_sqlite_engine

config = context.config
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    database = make_url(config.get_main_option("sqlalchemy.url")).database
    if database is None:
        raise RuntimeError("Alembic requires a file-backed SQLite database")
    engine = create_sqlite_engine(Path(database))
    try:
        with engine.connect() as connection:
            context.configure(connection=connection, target_metadata=target_metadata)
            with context.begin_transaction():
                context.run_migrations()
    finally:
        engine.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
