from __future__ import annotations

from pathlib import Path

from alembic import context
from sqlalchemy.engine import URL, make_url

from neetcode_dashboard.config import Settings
from neetcode_dashboard.db import models  # noqa: F401
from neetcode_dashboard.db.base import Base
from neetcode_dashboard.db.engine import create_sqlite_engine

config = context.config
target_metadata = Base.metadata


def configure_database_url() -> None:
    explicit_path = config.attributes.get("database_path")
    if explicit_path is None:
        database_path = Settings().database_path
    elif isinstance(explicit_path, Path):
        database_path = explicit_path.expanduser().resolve()
    else:
        raise RuntimeError("Alembic database_path must be a pathlib.Path")
    database_path.parent.mkdir(parents=True, exist_ok=True)
    url = URL.create("sqlite+pysqlite", database=str(database_path)).render_as_string(
        hide_password=False
    )
    config.set_main_option("sqlalchemy.url", url.replace("%", "%%"))


configure_database_url()


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
