from pathlib import Path

from alembic import command
from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from sqlalchemy import Engine
from sqlalchemy.engine import URL

PROJECT_ROOT = Path(__file__).resolve().parents[3]


def upgrade_database(path: Path) -> None:
    database_path = path.expanduser().resolve()
    database_path.parent.mkdir(parents=True, exist_ok=True)
    command.upgrade(_alembic_config(database_path), "head")


def current_revision(engine: Engine) -> str | None:
    with engine.connect() as connection:
        return MigrationContext.configure(connection).get_current_revision()


def _alembic_config(database_path: Path) -> Config:
    config = Config(str(PROJECT_ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(PROJECT_ROOT / "migrations"))
    url = URL.create("sqlite+pysqlite", database=str(database_path)).render_as_string(
        hide_password=False
    )
    config.set_main_option("sqlalchemy.url", url.replace("%", "%%"))
    return config
