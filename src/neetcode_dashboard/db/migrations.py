from pathlib import Path

from alembic import command
from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from sqlalchemy import Engine
from sqlalchemy.engine import URL

from neetcode_dashboard.resources import resource_path


def upgrade_database(path: Path) -> None:
    database_path = path.expanduser().resolve()
    database_path.parent.mkdir(parents=True, exist_ok=True)
    command.upgrade(_alembic_config(database_path), "head")


def current_revision(engine: Engine) -> str | None:
    with engine.connect() as connection:
        return MigrationContext.configure(connection).get_current_revision()


def _alembic_config(database_path: Path) -> Config:
    config = Config(str(resource_path("alembic.ini")))
    config.set_main_option("script_location", str(resource_path("migrations")))
    config.attributes["database_path"] = database_path
    url = URL.create("sqlite+pysqlite", database=str(database_path)).render_as_string(
        hide_password=False
    )
    config.set_main_option("sqlalchemy.url", url.replace("%", "%%"))
    return config
