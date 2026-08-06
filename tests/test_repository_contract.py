from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PLAN_HASH = "1c0cb3c548ffdb5ddd521ef20d0a17489d7148bb3613e024b88bec21b6e91d96"


def test_master_plan_is_frozen_byte_for_byte() -> None:
    plan = ROOT / "PLAN.md"

    assert plan.exists()
    assert sha256(plan.read_bytes()).hexdigest() == EXPECTED_PLAN_HASH
