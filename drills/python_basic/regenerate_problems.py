from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shutil
import textwrap
from uuid import uuid4

from catalog import EXERCISES, Exercise
from generate_bank import CHAPTERS, SEEDS, Seed
from source_checks import CHECK_DESCRIPTIONS, checks_for_seed


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "catalog" / "generated_manifest.json"
PROBLEM_PATTERN = re.compile(r"PB(?P<number>\d{4})_.*\.py$")
SELF_TEST_PATTERN = re.compile(r"^def self_test\(\) -> None:\s*$", re.MULTILINE)
SCHEMA_VERSION = 1
SCAFFOLD_VERSION = 3


@dataclass(frozen=True)
class ProblemBuild:
    problem_id: str
    seed: Seed
    seed_number: int
    variant_number: int
    exercise: Exercise
    relative_path: Path
    source_checks: tuple[str, ...]
    contract_sha256: str
    starter_source: str
    starter_sha256: str


@dataclass(frozen=True)
class WriteAction:
    build: ProblemBuild
    source: str
    previous_path: Path | None
    archive_source: str | None
    reason: str


def digest(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def render_docstring(build: ProblemBuild) -> str:
    exercise = build.exercise
    checks_text = ", ".join(build.source_checks)
    source_checks_line = "Source checks:"
    if checks_text:
        source_checks_line += f" {checks_text}"
    lines = [
        '"""',
        f"{build.problem_id} — {exercise.title}",
        "",
        f"Chapter: {build.seed.chapter}",
        f"Topic: {build.seed.title}",
        f"Seed: {build.seed_number:02d} / 82",
        f"Variant: {build.variant_number:02d} / 10",
        f"Time cap: {exercise.time_cap} seconds",
        source_checks_line,
        "",
        "문제",
        "----",
        exercise.task,
        "",
        "연습 초점",
        "---------",
        exercise.focus,
        "",
        "구현할 함수",
        "-----------",
        exercise.signature,
    ]
    if build.source_checks:
        lines.extend(
            [
                "",
                "필수 구현 방식",
                "--------------",
                *(f"- {CHECK_DESCRIPTIONS[name]}" for name in build.source_checks),
            ]
        )
    lines.extend(
        [
            "",
            "예시 및 필수 테스트",
            "-------------------",
            *("- " + test.replace("\\", "\\\\") for test in exercise.tests),
            "",
            "완료 조건",
            "---------",
            "1. 위 함수 이름과 시그니처를 유지한다.",
            "2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.",
            "3. 입력별 정답을 if문으로 나열하지 않는다.",
            f"4. 저장소 루트에서 `python3 -B -m python_basic {build.problem_id} --strict`를 실행한다.",
            "5. 실행 코드에서 NotImplementedError를 모두 제거한다.",
            '"""',
        ]
    )
    return "\n".join(lines)


def render_solution(build: ProblemBuild) -> str:
    body = build.exercise.starter_body or (
        f'raise NotImplementedError("TODO: {build.problem_id}")'
    )
    return f"{build.exercise.signature}\n{textwrap.indent(body, '    ')}"


def render_self_test(build: ProblemBuild) -> str:
    assertions = "\n".join(f"    assert {test}" for test in build.exercise.tests)
    return f"def self_test() -> None:\n{assertions}"


def render_problem(build: ProblemBuild, solution: str | None = None) -> str:
    parts = [render_docstring(build)]
    if (
        build.exercise.prelude.strip()
        and (solution is None or build.exercise.prelude.strip() not in solution)
    ):
        parts.append(build.exercise.prelude.strip())
    parts.append(solution.strip() if solution is not None else render_solution(build))
    parts.append(render_self_test(build))
    return "\n\n\n".join(parts).rstrip() + "\n"


def contract_digest(
    problem_id: str,
    seed: Seed,
    seed_number: int,
    variant_number: int,
    exercise: Exercise,
    source_checks: tuple[str, ...],
) -> str:
    payload = {
        "problem_id": problem_id,
        "seed": asdict(seed),
        "seed_number": seed_number,
        "variant_number": variant_number,
        "exercise": asdict(exercise),
        "source_checks": source_checks,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return digest(encoded)


def build_catalog() -> list[ProblemBuild]:
    builds: list[ProblemBuild] = []
    problem_number = 0
    for seed_number, seed in enumerate(SEEDS, start=1):
        exercises = EXERCISES.get(seed.slug)
        if exercises is None or len(exercises) != 10:
            raise RuntimeError(f"{seed.slug}: expected 10 exercises")
        for variant_number, exercise in enumerate(exercises, start=1):
            problem_number += 1
            problem_id = f"PB{problem_number:04d}"
            relative_path = (
                Path(CHAPTERS[seed.chapter])
                / f"{problem_id}_{exercise.slug}_v{variant_number:02d}.py"
            )
            source_checks = checks_for_seed(seed.slug)
            placeholder = ProblemBuild(
                problem_id=problem_id,
                seed=seed,
                seed_number=seed_number,
                variant_number=variant_number,
                exercise=exercise,
                relative_path=relative_path,
                source_checks=source_checks,
                contract_sha256="",
                starter_source="",
                starter_sha256="",
            )
            starter_source = render_problem(placeholder)
            ast.parse(starter_source, filename=str(relative_path))
            builds.append(
                ProblemBuild(
                    problem_id=problem_id,
                    seed=seed,
                    seed_number=seed_number,
                    variant_number=variant_number,
                    exercise=exercise,
                    relative_path=relative_path,
                    source_checks=source_checks,
                    contract_sha256=contract_digest(
                        problem_id,
                        seed,
                        seed_number,
                        variant_number,
                        exercise,
                        source_checks,
                    ),
                    starter_source=starter_source,
                    starter_sha256=digest(starter_source),
                )
            )
    if len(builds) != 820:
        raise RuntimeError(f"expected 820 builds, found {len(builds)}")
    return builds


def load_manifest() -> dict[str, object]:
    if not MANIFEST_PATH.exists():
        return {"schema_version": SCHEMA_VERSION, "problems": {}}
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION:
        raise RuntimeError("unsupported generated manifest schema")
    if not isinstance(data.get("problems"), dict):
        raise RuntimeError("generated manifest has no problems mapping")
    return data


def existing_problems() -> dict[str, list[Path]]:
    result: dict[str, list[Path]] = {}
    for path in ROOT.rglob("PB*.py"):
        if "_preserved_answers" in path.parts:
            continue
        match = PROBLEM_PATTERN.fullmatch(path.name)
        if match is None:
            continue
        problem_id = f"PB{int(match.group('number')):04d}"
        result.setdefault(problem_id, []).append(path)
    return result


def has_pristine_not_implemented(source: str, problem_id: str) -> bool:
    expected = f'raise NotImplementedError("TODO: {problem_id}")'
    return expected in source and source.count("NotImplementedError") == 2


def extract_solution_block(source: str, expected_signature: str) -> str | None:
    match = SELF_TEST_PATTERN.search(source)
    if match is None:
        return None
    before_self_test = source[: match.start()].rstrip()
    docstring_end = before_self_test.find('"""', 3)
    if not before_self_test.startswith('"""') or docstring_end == -1:
        return None
    solution = before_self_test[docstring_end + 3 :].strip()
    signature_pattern = re.compile(
        rf"^\s*{re.escape(expected_signature)}\s*$",
        re.MULTILINE,
    )
    if signature_pattern.search(solution) is None:
        return None
    return solution


def archive_relative_path(
    problem_id: str,
    previous_path: Path,
    timestamp: str,
    source: str,
) -> Path:
    relative_name = previous_path.relative_to(ROOT).as_posix().replace("/", "__")
    source_tag = digest(source)[:10]
    return (
        Path("_preserved_answers")
        / f"{timestamp}_{problem_id}_{source_tag}_{relative_name}"
    )


def render_index(builds: list[ProblemBuild]) -> str:
    lines = [
        "# Python Basic 820 Problem Index",
        "",
        "82개 주제 × 주제별 맞춤 문제 10개 = 820개입니다.",
        "",
    ]
    current_chapter = ""
    for build in builds:
        if build.seed.chapter != current_chapter:
            if current_chapter:
                lines.append("")
            current_chapter = build.seed.chapter
            lines.extend([f"## {current_chapter}", ""])
        lines.append(
            f"- [{build.problem_id} — {build.exercise.title}]"
            f"({build.relative_path.as_posix()})"
        )
    return "\n".join(lines).rstrip() + "\n"


def manifest_payload(builds: list[ProblemBuild]) -> str:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "problems": {
            build.problem_id: {
                "path": build.relative_path.as_posix(),
                "contract_sha256": build.contract_sha256,
                "scaffold_version": SCAFFOLD_VERSION,
                "starter_sha256": build.starter_sha256,
            }
            for build in builds
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def plan_actions(
    builds: list[ProblemBuild],
    manifest: dict[str, object],
) -> list[WriteAction]:
    existing = existing_problems()
    manifest_problems = manifest["problems"]
    assert isinstance(manifest_problems, dict)
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    actions: list[WriteAction] = []

    for build in builds:
        paths = existing.pop(build.problem_id, [])
        entry = manifest_problems.get(build.problem_id)
        if isinstance(entry, dict):
            managed = ROOT / entry["path"]
            # A missing canonical file never authorizes moving a personal draft.
            paths = [managed] if managed in paths else []
        elif len(paths) > 1:
            joined = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            raise RuntimeError(f"ambiguous {build.problem_id}: {joined}")
        previous_path = paths[0] if paths else None
        previous_source = (
            previous_path.read_text(encoding="utf-8") if previous_path is not None else None
        )
        entry = manifest_problems.get(build.problem_id)

        if previous_source is not None and isinstance(entry, dict):
            if entry.get("contract_sha256") == build.contract_sha256:
                if entry.get("scaffold_version") != SCAFFOLD_VERSION:
                    if digest(previous_source) == entry.get("starter_sha256"):
                        actions.append(
                            WriteAction(
                                build,
                                build.starter_source,
                                previous_path,
                                None,
                                "updated_pristine_scaffold",
                            )
                        )
                        continue
                    solution = extract_solution_block(
                        previous_source,
                        build.exercise.signature,
                    )
                    archive = archive_relative_path(
                        build.problem_id,
                        previous_path,
                        timestamp,
                        previous_source,
                    )
                    next_source = (
                        build.starter_source
                        if solution is None
                        else render_problem(build, solution)
                    )
                    reason = (
                        "archived_unmigratable_scaffold"
                        if solution is None
                        else "preserved_user_scaffold_update"
                    )
                    actions.append(
                        WriteAction(
                            build,
                            next_source,
                            previous_path,
                            f"{archive.as_posix()}\0{previous_source}",
                            reason,
                        )
                    )
                    continue
                actions.append(
                    WriteAction(build, previous_source, previous_path, None, "unchanged")
                )
                continue
            if digest(previous_source) == entry.get("starter_sha256"):
                actions.append(
                    WriteAction(
                        build,
                        build.starter_source,
                        previous_path,
                        None,
                        "updated_pristine_starter",
                    )
                )
                continue
            archive = archive_relative_path(
                build.problem_id,
                previous_path,
                timestamp,
                previous_source,
            )
            actions.append(
                WriteAction(
                    build,
                    build.starter_source,
                    previous_path,
                    f"{archive.as_posix()}\0{previous_source}",
                    "archived_changed_contract",
                )
            )
            continue

        if previous_source is None:
            actions.append(
                WriteAction(build, build.starter_source, None, None, "created")
            )
            continue

        if previous_source == build.starter_source:
            actions.append(
                WriteAction(
                    build,
                    build.starter_source,
                    previous_path,
                    None,
                    "migrated_pristine_starter",
                )
            )
            continue

        solution = extract_solution_block(previous_source, build.exercise.signature)
        archive = archive_relative_path(
            build.problem_id,
            previous_path,
            timestamp,
            previous_source,
        )
        if solution is None:
            next_source = build.starter_source
            reason = "archived_unmigratable_work"
        else:
            next_source = render_problem(
                build,
                solution,
            )
            reason = "preserved_user_work"
        actions.append(
            WriteAction(
                build,
                next_source,
                previous_path,
                f"{archive.as_posix()}\0{previous_source}",
                reason,
            )
        )

    extras = [path for paths in existing.values() for path in paths]
    if extras:
        joined = ", ".join(str(path.relative_to(ROOT)) for path in extras[:5])
        raise RuntimeError(f"unexpected problem files remain: {joined}")
    return actions


def apply_actions(
    actions: list[WriteAction],
    index_source: str,
    manifest_source: str,
) -> None:
    transaction_id = uuid4().hex
    scratch = ROOT.parent / ".tmp"
    scratch.mkdir(exist_ok=True)
    stage = scratch / f"basic-stage-{transaction_id}"
    backup = scratch / f"basic-backup-{transaction_id}"
    stage.mkdir()
    backup.mkdir()
    touched: set[Path] = set()
    created: set[Path] = set()
    removed_previous_paths: set[Path] = set()

    try:
        for action in actions:
            staged_path = stage / action.build.relative_path
            staged_path.parent.mkdir(parents=True, exist_ok=True)
            staged_path.write_text(action.source, encoding="utf-8")
            if action.archive_source is not None:
                archive_name, archive_source = action.archive_source.split("\0", 1)
                archive_path = stage / archive_name
                archive_path.parent.mkdir(parents=True, exist_ok=True)
                archive_path.write_text(archive_source, encoding="utf-8")

        (stage / "INDEX.md").write_text(index_source, encoding="utf-8")
        staged_manifest = stage / MANIFEST_PATH.relative_to(ROOT)
        staged_manifest.parent.mkdir(parents=True, exist_ok=True)
        staged_manifest.write_text(manifest_source, encoding="utf-8")

        for action in actions:
            destination = ROOT / action.build.relative_path
            previous_path = action.previous_path
            for original in {destination, previous_path} - {None}:
                assert isinstance(original, Path)
                if original.exists() and original not in touched:
                    backup_path = backup / original.relative_to(ROOT)
                    backup_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(original, backup_path)
                    touched.add(original)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                created.add(destination)
            os.replace(stage / action.build.relative_path, destination)
            if previous_path is not None and previous_path != destination:
                previous_path.unlink()
                removed_previous_paths.add(previous_path)
            if action.archive_source is not None:
                archive_name, _ = action.archive_source.split("\0", 1)
                archive_destination = ROOT / archive_name
                archive_destination.parent.mkdir(parents=True, exist_ok=True)
                if not archive_destination.exists():
                    created.add(archive_destination)
                os.replace(stage / archive_name, archive_destination)

        for relative in (Path("INDEX.md"), MANIFEST_PATH.relative_to(ROOT)):
            destination = ROOT / relative
            if destination.exists() and destination not in touched:
                backup_path = backup / relative
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(destination, backup_path)
                touched.add(destination)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                created.add(destination)
            os.replace(stage / relative, destination)
    except Exception:
        for destination in created:
            if destination.exists():
                destination.unlink()
        for original in touched:
            backup_path = backup / original.relative_to(ROOT)
            if backup_path.exists():
                original.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(backup_path, original)
        for removed in removed_previous_paths:
            backup_path = backup / removed.relative_to(ROOT)
            if backup_path.exists():
                removed.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(backup_path, removed)
        raise
    finally:
        shutil.rmtree(stage, ignore_errors=True)
        shutil.rmtree(backup, ignore_errors=True)


def main() -> None:
    builds = build_catalog()
    manifest = load_manifest()
    actions = plan_actions(builds, manifest)
    index_source = render_index(builds)
    manifest_source = manifest_payload(builds)
    ast.parse("\n".join(build.starter_source for build in builds))
    apply_actions(actions, index_source, manifest_source)

    counts: dict[str, int] = {}
    for action in actions:
        counts[action.reason] = counts.get(action.reason, 0) + 1
    print("problems=820")
    for reason in sorted(counts):
        print(f"{reason}={counts[reason]}")
    print(f"manifest={MANIFEST_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
