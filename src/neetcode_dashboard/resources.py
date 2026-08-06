from __future__ import annotations

from importlib.resources import files
from pathlib import Path
from typing import Literal

ResourceName = Literal["PLAN.md", "alembic.ini", "holidays.json", "migrations"]

_SOURCE_ROOT = Path(__file__).resolve().parents[2]
_SOURCE_PATHS: dict[ResourceName, Path] = {
    "PLAN.md": Path("PLAN.md"),
    "alembic.ini": Path("alembic.ini"),
    "holidays.json": Path("data/holidays.json"),
    "migrations": Path("migrations"),
}
_BUNDLED_PATHS: dict[ResourceName, Path] = {
    "PLAN.md": Path("PLAN.md"),
    "alembic.ini": Path("alembic.ini"),
    "holidays.json": Path("holidays.json"),
    "migrations": Path("migrations"),
}


def resource_path(name: ResourceName) -> Path:
    """Resolve frozen resources from a checkout or an installed wheel."""
    bundled = files("neetcode_dashboard").joinpath("_bundled", _BUNDLED_PATHS[name])
    if isinstance(bundled, Path) and bundled.exists():
        return bundled.resolve()

    source_path = (_SOURCE_ROOT / _SOURCE_PATHS[name]).resolve()
    if source_path.exists():
        return source_path
    raise RuntimeError(f"required bundled resource is unavailable: {name}")
