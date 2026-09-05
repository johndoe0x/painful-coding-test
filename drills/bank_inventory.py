"""Resolve managed exercises without consuming a learner's extra draft files."""

from __future__ import annotations

import json
from pathlib import Path
import re


BANKS = {
    "PB": ("python_basic", "catalog/generated_manifest.json"),
    "CI": ("python_coding", "generated_manifest.json"),
}


def managed_paths(root: Path, prefix: str) -> dict[str, Path]:
    bank_name, manifest_name = BANKS[prefix]
    bank = root / bank_name
    manifest = json.loads((bank / manifest_name).read_text(encoding="utf-8"))
    result = {}
    for problem_id, entry in manifest["problems"].items():
        if re.fullmatch(prefix + r"\d{4}", problem_id) is None:
            raise ValueError(f"Invalid managed problem ID: {problem_id}")
        relative = Path(entry["path"])
        path = bank / relative
        if (
            relative.is_absolute()
            or ".." in relative.parts
            or not path.resolve().is_relative_to(bank.resolve())
            or not path.name.startswith(problem_id + "_")
            or path.suffix != ".py"
            or "_preserved_answers" in relative.parts
        ):
            raise ValueError(f"Invalid managed problem path: {problem_id}")
        result[problem_id] = path
    return result


def find_managed_problem(root: Path, problem_id: str) -> Path:
    path = managed_paths(root, problem_id[:2]).get(problem_id)
    if path is None or not path.is_file():
        raise ValueError(f"Managed problem file is missing: {problem_id}")
    return path
