from __future__ import annotations

from pathlib import Path
from typing import Annotated, Literal, Self

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def _default_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NEETCODE_", extra="forbid")

    project_root: Path = Field(default_factory=_default_project_root)
    host: Literal["127.0.0.1", "localhost"] = "127.0.0.1"
    port: Annotated[int, Field(ge=1, le=65_535)] = 51_115
    data_dir: Path = Path("data")
    database_path: Path = Path("data/tracker.sqlite3")
    backup_dir: Path = Path("backups")

    @model_validator(mode="after")
    def resolve_runtime_paths(self) -> Self:
        self.project_root = self.project_root.expanduser().resolve()
        self.data_dir = self._resolve_from_project_root(self.data_dir)

        if "database_path" not in self.model_fields_set:
            self.database_path = self.data_dir / "tracker.sqlite3"
        else:
            self.database_path = self._resolve_from_project_root(self.database_path)

        self.backup_dir = self._resolve_from_project_root(self.backup_dir)
        return self

    def _resolve_from_project_root(self, path: Path) -> Path:
        expanded = path.expanduser()
        if expanded.is_absolute():
            return expanded.resolve()
        return (self.project_root / expanded).resolve()


def ensure_runtime_directories(settings: Settings) -> None:
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    settings.database_path.parent.mkdir(parents=True, exist_ok=True)
    settings.backup_dir.mkdir(parents=True, exist_ok=True)
