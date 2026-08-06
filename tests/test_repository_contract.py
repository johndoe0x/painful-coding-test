import tomllib
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PLAN_HASH = "1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96"


def test_master_plan_is_frozen_byte_for_byte() -> None:
    plan = ROOT / "PLAN.md"

    assert plan.exists()
    assert sha256(plan.read_bytes()).hexdigest() == EXPECTED_PLAN_HASH


def test_wheel_declares_all_non_package_runtime_resources() -> None:
    configuration = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    force_include = configuration["tool"]["hatch"]["build"]["targets"]["wheel"]["force-include"]

    assert force_include == {
        "PLAN.md": "neetcode_dashboard/_bundled/PLAN.md",
        "alembic.ini": "neetcode_dashboard/_bundled/alembic.ini",
        "data/holidays.json": "neetcode_dashboard/_bundled/holidays.json",
        "migrations": "neetcode_dashboard/_bundled/migrations",
    }
