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
import sys
from uuid import uuid4


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from generate_bank import CHAPTERS, ROOT, SEEDS, Seed
from python_basic.source_checks import CHECK_DESCRIPTIONS
from quality_catalog import BASELINE_SOURCE_CHECKS, TEMPLATES, ChallengeTemplate
from diversity_catalog import REPLACEMENTS
from regenerate_variants import TESTS


MANIFEST_PATH = ROOT / "generated_manifest.json"
REPORT_PATH = ROOT / "REGENERATION_REPORT.md"
PROBLEM_PATTERN = re.compile(r"CI(?P<number>\d{4})_.*\.py$")
SELF_TEST_PATTERN = re.compile(r"^def self_test\(\) -> None:\s*$", re.MULTILINE)
SCHEMA_VERSION = 1
SCAFFOLD_VERSION = 1


@dataclass(frozen=True)
class Exercise:
    slug: str
    title: str
    signature: str
    task: str
    focus: str
    tests: tuple[str, str, str]
    source_checks: tuple[str, ...]
    time_cap: int


@dataclass(frozen=True)
class ProblemBuild:
    problem_id: str
    seed: Seed
    seed_number: int
    variant_number: int
    exercise: Exercise
    relative_path: Path
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


def function_name(signature: str) -> str:
    module = ast.parse(f"{signature}\n    pass")
    function = module.body[0]
    if not isinstance(function, ast.FunctionDef):
        raise ValueError(f"invalid signature: {signature}")
    return function.name


def normalized_test_suite(name: str, tests: tuple[str, ...]) -> tuple[str, ...]:
    """Exact AST comparison after renaming the callable, not semantic equivalence."""
    class RenameTarget(ast.NodeTransformer):
        def visit_Name(self, node: ast.Name) -> ast.Name:
            if node.id == name:
                return ast.copy_location(ast.Name(id="__FN__", ctx=node.ctx), node)
            return node

    return tuple(
        ast.dump(RenameTarget().visit(ast.parse(test, mode="eval")), include_attributes=False)
        for test in tests
    )


def baseline_exercise(seed: Seed) -> Exercise:
    tests = TESTS[seed.slug][:3]
    if len(tests) != 3:
        raise RuntimeError(f"{seed.slug}: baseline needs three tests")
    return Exercise(
        slug=f"{seed.slug}_baseline",
        title=f"{seed.title} — 기본 계약",
        signature=seed.signature,
        task=seed.task,
        focus="핵심 Python API와 대표 경계값을 빈 화면에서 재구현",
        tests=tuple(tests),
        source_checks=BASELINE_SOURCE_CHECKS.get(seed.slug, ()),
        time_cap=180,
    )


CHAPTER_PREFIX = {
    "Sorting": "sorting",
    "Pythonic Code": "pythonic",
    "Lists": "lists",
    "Stacks and Queues": "stack_queue",
    "2-D Lists": "grid",
    "Hashmaps and Hashsets": "hashing",
    "Heaps / Priority Queues": "heap",
    "Sorted Dicts and Sorted Sets": "sorted_structure",
}


def template_exercise(
    seed: Seed,
    template: ChallengeTemplate,
    repetition: int,
) -> Exercise:
    target_name = (
        f"{CHAPTER_PREFIX[seed.chapter]}_r{repetition:02d}_{template.slug}"
    )
    return Exercise(
        slug=target_name,
        title=f"{template.title} — 반복 세트 {repetition}",
        signature=f"def {target_name}{template.signature_suffix}",
        task=(
            f"{template.task} 이 파일은 {seed.chapter} 챕터의 반복 세트 "
            f"{repetition}이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다."
        ),
        focus=template.focus,
        tests=tuple(test.replace("__FN__", target_name) for test in template.tests),
        source_checks=template.source_checks,
        time_cap=template.time_cap,
    )


def replacement_exercise(original: Exercise, template: ChallengeTemplate) -> Exercise:
    """Keep the problem ID while giving a new concept a descriptive entry point."""
    chapter_prefix = function_name(original.signature).split("_r", 1)[0]
    target_name = f"{chapter_prefix}_bridge_{template.slug}"
    return Exercise(
        slug=target_name,
        title=template.title,
        signature=f"def {target_name}{template.signature_suffix}",
        task=template.task,
        focus=template.focus,
        tests=tuple(test.replace("__FN__", target_name) for test in template.tests),
        source_checks=template.source_checks,
        time_cap=template.time_cap,
    )


def render_docstring(build: ProblemBuild) -> str:
    exercise = build.exercise
    checks_text = ", ".join(exercise.source_checks)
    source_checks_line = "Source checks:"
    if checks_text:
        source_checks_line += f" {checks_text}"
    lines = [
        '"""',
        f"{build.problem_id} — {exercise.title}",
        "",
        f"Chapter: {build.seed.chapter}",
        f"Seed: {build.seed_number:02d} / 40",
        f"Variant: {build.variant_number:02d} / 20",
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
    if exercise.source_checks:
        lines.extend(
            [
                "",
                "필수 구현 방식",
                "--------------",
                *(f"- {CHECK_DESCRIPTIONS[name]}" for name in exercise.source_checks),
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
            "2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.",
            "3. 필요한 표준 라이브러리 import를 직접 작성한다.",
            "4. 입력별 정답을 if문으로 나열하지 않는다.",
            "5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.",
            f"6. 저장소 루트에서 `python3 -B -m python_coding {build.problem_id} --strict`를 실행한다.",
            "7. 실행 코드에서 NotImplementedError를 모두 제거한다.",
            '"""',
        ]
    )
    return "\n".join(lines)


def render_solution(build: ProblemBuild) -> str:
    return (
        f"{build.exercise.signature}\n"
        f"    raise NotImplementedError(\"TODO: {build.problem_id}\")"
    )


def render_self_test(build: ProblemBuild) -> str:
    assertions = "\n".join(f"    assert {test}" for test in build.exercise.tests)
    return f"def self_test() -> None:\n{assertions}"


def render_problem(build: ProblemBuild, solution: str | None = None) -> str:
    parts = [render_docstring(build)]
    actual_solution = solution.strip() if solution is not None else render_solution(build)
    if "from __future__ import annotations" not in actual_solution:
        parts.append("from __future__ import annotations")
    parts.append(actual_solution)
    parts.append(render_self_test(build))
    return "\n\n\n".join(parts).rstrip() + "\n"


def contract_digest(build: ProblemBuild) -> str:
    payload = {
        "problem_id": build.problem_id,
        "seed": asdict(build.seed),
        "seed_number": build.seed_number,
        "variant_number": build.variant_number,
        "exercise": asdict(build.exercise),
        "source_check_descriptions": {
            name: CHECK_DESCRIPTIONS[name]
            for name in build.exercise.source_checks
        },
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return digest(encoded)


def build_catalog() -> list[ProblemBuild]:
    builds: list[ProblemBuild] = []
    chapter_repetitions: dict[str, int] = {}
    for seed_number, seed in enumerate(SEEDS, start=1):
        repetition = chapter_repetitions.get(seed.chapter, 0) + 1
        chapter_repetitions[seed.chapter] = repetition
        exercises = [baseline_exercise(seed)] + [
            template_exercise(seed, template, repetition)
            for template in TEMPLATES[seed.chapter]
        ]
        if len(exercises) != 20:
            raise RuntimeError(f"{seed.slug}: expected 20 exercises")
        for variant_number, exercise in enumerate(exercises, start=1):
            number = (seed_number - 1) * 20 + variant_number
            problem_id = f"CI{number:04d}"
            if number in REPLACEMENTS:
                if variant_number == 1 or repetition < 2:
                    raise RuntimeError(f"{problem_id}: only repeated non-baseline slots may be replaced")
                exercise = replacement_exercise(exercise, REPLACEMENTS[number])
            suffix = "baseline" if variant_number == 1 else exercise.slug
            relative_path = (
                Path(CHAPTERS[seed.chapter])
                / f"{problem_id}_{suffix}_v{variant_number:02d}.py"
            )
            placeholder = ProblemBuild(
                problem_id=problem_id,
                seed=seed,
                seed_number=seed_number,
                variant_number=variant_number,
                exercise=exercise,
                relative_path=relative_path,
                contract_sha256="",
                starter_source="",
                starter_sha256="",
            )
            starter_source = render_problem(placeholder)
            ast.parse(starter_source, filename=str(relative_path))
            contract = contract_digest(placeholder)
            builds.append(
                ProblemBuild(
                    **{
                        **placeholder.__dict__,
                        "contract_sha256": contract,
                        "starter_source": starter_source,
                        "starter_sha256": digest(starter_source),
                    }
                )
            )
    if len(builds) != 800:
        raise RuntimeError(f"expected 800 builds, found {len(builds)}")
    unknown_replacements = set(REPLACEMENTS) - set(range(1, len(builds) + 1))
    if unknown_replacements:
        raise RuntimeError(f"unknown replacement IDs: {sorted(unknown_replacements)}")
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
    for path in ROOT.rglob("CI*.py"):
        if "_preserved_answers" in path.parts:
            continue
        match = PROBLEM_PATTERN.fullmatch(path.name)
        if match is None:
            continue
        problem_id = f"CI{int(match.group('number')):04d}"
        result.setdefault(problem_id, []).append(path)
    return result


def extract_solution_block(source: str, expected_signature: str) -> str | None:
    self_test = SELF_TEST_PATTERN.search(source)
    before_tests = source[: self_test.start()].rstrip() if self_test else source.rstrip()
    if not before_tests.startswith('"""'):
        return None
    docstring_end = before_tests.find('"""', 3)
    if docstring_end == -1:
        return None
    solution = before_tests[docstring_end + 3 :].strip()
    expected_name = function_name(expected_signature)
    if re.search(rf"^def {re.escape(expected_name)}\s*\(", solution, re.MULTILINE) is None:
        return None
    return solution


def archive_path(problem_id: str, previous_path: Path, source: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
    source_tag = digest(source)[:10]
    safe_name = previous_path.relative_to(ROOT).as_posix().replace("/", "__")
    return Path("_preserved_answers") / (
        f"{timestamp}_{problem_id}_{source_tag}_{safe_name}"
    )


def plan_actions(builds: list[ProblemBuild]) -> list[WriteAction]:
    manifest = load_manifest()
    manifest_problems = manifest["problems"]
    assert isinstance(manifest_problems, dict)
    existing = existing_problems()
    actions: list[WriteAction] = []

    for build in builds:
        paths = existing.pop(build.problem_id, [])
        if len(paths) > 1:
            joined = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            raise RuntimeError(f"duplicate {build.problem_id}: {joined}")
        previous_path = paths[0] if paths else None
        previous_source = (
            previous_path.read_text(encoding="utf-8") if previous_path else None
        )
        entry = manifest_problems.get(build.problem_id)

        if (
            int(build.problem_id[2:]) in REPLACEMENTS
            and previous_path is not None
            and previous_path != ROOT / build.relative_path
            and (
                not isinstance(entry, dict)
                or digest(previous_source) != entry.get("starter_sha256")
            )
        ):
            raise RuntimeError(
                f"{build.problem_id}: replacement rename requires a manifest-confirmed pristine file; "
                "learner work was left untouched"
            )

        if previous_source is not None and isinstance(entry, dict):
            same_contract = entry.get("contract_sha256") == build.contract_sha256
            same_scaffold = entry.get("scaffold_version") == SCAFFOLD_VERSION
            if same_contract and same_scaffold:
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
                        "updated_pristine",
                    )
                )
                continue
            archived = archive_path(build.problem_id, previous_path, previous_source)
            if same_contract:
                solution = extract_solution_block(
                    previous_source,
                    build.exercise.signature,
                )
                source = (
                    render_problem(build, solution)
                    if solution is not None
                    else build.starter_source
                )
                reason = "preserved_scaffold_update" if solution else "archived_unmigratable"
            else:
                source = build.starter_source
                reason = "archived_changed_contract"
            actions.append(
                WriteAction(
                    build,
                    source,
                    previous_path,
                    f"{archived.as_posix()}\0{previous_source}",
                    reason,
                )
            )
            continue

        if previous_source is None:
            actions.append(WriteAction(build, build.starter_source, None, None, "created"))
            continue
        # Without a manifest, a TODO substring is not evidence of pristine work:
        # a learner may have written imports, comments, or a partial solution.
        if previous_source == build.starter_source:
            actions.append(
                WriteAction(
                    build,
                    build.starter_source,
                    previous_path,
                    None,
                    "migrated_pristine",
                )
            )
            continue

        archived = archive_path(build.problem_id, previous_path, previous_source)
        solution = extract_solution_block(previous_source, build.exercise.signature)
        source = render_problem(build, solution) if solution else build.starter_source
        reason = "preserved_user_work" if solution else "archived_unmigratable"
        actions.append(
            WriteAction(
                build,
                source,
                previous_path,
                f"{archived.as_posix()}\0{previous_source}",
                reason,
            )
        )

    extras = [path for paths in existing.values() for path in paths]
    if extras:
        joined = ", ".join(str(path.relative_to(ROOT)) for path in extras[:5])
        raise RuntimeError(f"unexpected CI files: {joined}")
    return actions


def render_index(builds: list[ProblemBuild]) -> str:
    lines = [
        "# Python Coding Interview 800 Problem Index",
        "",
        "800개 고정 ID에 기본 계약, 추가 개념, 선택 복습을 배치했습니다. 파일 수는 고유 알고리즘 수가 아닙니다.",
        "",
    ]
    current_seed = 0
    for build in builds:
        if build.seed_number != current_seed:
            if current_seed:
                lines.append("")
            current_seed = build.seed_number
            lines.extend([f"## {build.seed.chapter} — {build.seed.title}", ""])
        lines.append(
            f"- [{build.problem_id} — {build.exercise.title}]"
            f"({build.relative_path.as_posix()})"
        )
    return "\n".join(lines).rstrip() + "\n"


def render_manifest(builds: list[ProblemBuild]) -> str:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "scaffold_version": SCAFFOLD_VERSION,
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


def render_report(builds: list[ProblemBuild], actions: list[WriteAction]) -> str:
    action_counts: dict[str, int] = {}
    check_counts: dict[str, int] = {}
    for action in actions:
        action_counts[action.reason] = action_counts.get(action.reason, 0) + 1
    for build in builds:
        for check in build.exercise.source_checks:
            check_counts[check] = check_counts.get(check, 0) + 1
    normalized_shapes = {
        normalized_test_suite(function_name(build.exercise.signature), build.exercise.tests)
        for build in builds
    }
    lines = [
        "# Python Coding Quality Regeneration Report",
        "",
        "## Historical baseline (before the earlier contract migration)",
        "",
        "- Files: 800",
        "- Unique primary function contracts: 40",
        "- Unique self-test suites: 160",
        "- v02-v20 descriptions requested extra helpers or algorithms that their tests did not call",
        "",
        "## Current generated inventory",
        "",
        f"- Files: {len(builds)}",
        f"- Unique function names: {len({function_name(build.exercise.signature) for build in builds})}",
        f"- Unique problem statements: {len({build.exercise.task for build in builds})}",
        f"- Unique test suites: {len({build.exercise.tests for build in builds})}",
        f"- Exact normalized test-suite shapes: {len(normalized_shapes)} (not a count of unique algorithms)",
        f"- Repeated test-suite slots: {len(builds) - len(normalized_shapes)}",
        f"- Diverse replacement slots: {len(REPLACEMENTS)}",
        f"- Required asserts: {len(builds) * 3}",
        f"- Source-checked problems: {sum(bool(build.exercise.source_checks) for build in builds)} (instructional checks, not correctness or complexity proof)",
        "",
        "## Regeneration Actions",
        "",
    ]
    lines.extend(f"- {name}: {count}" for name, count in sorted(action_counts.items()))
    lines.extend(["", "## Required API Coverage", ""])
    lines.extend(f"- {name}: {count}" for name, count in sorted(check_counts.items()))
    return "\n".join(lines).rstrip() + "\n"


def apply_actions(
    actions: list[WriteAction],
    index_source: str,
    manifest_source: str,
    report_source: str,
) -> None:
    transaction = uuid4().hex
    scratch = WORKSPACE_ROOT / ".tmp"
    scratch.mkdir(exist_ok=True)
    stage = scratch / f"coding-stage-{transaction}"
    backup = scratch / f"coding-backup-{transaction}"
    stage.mkdir()
    backup.mkdir()
    touched: set[Path] = set()
    created: set[Path] = set()

    try:
        for action in actions:
            staged = stage / action.build.relative_path
            staged.parent.mkdir(parents=True, exist_ok=True)
            staged.write_text(action.source, encoding="utf-8")
            if action.archive_source is not None:
                archive_name, archived_source = action.archive_source.split("\0", 1)
                archive = stage / archive_name
                archive.parent.mkdir(parents=True, exist_ok=True)
                archive.write_text(archived_source, encoding="utf-8")
        (stage / "INDEX.md").write_text(index_source, encoding="utf-8")
        (stage / MANIFEST_PATH.name).write_text(manifest_source, encoding="utf-8")
        (stage / REPORT_PATH.name).write_text(report_source, encoding="utf-8")

        for action in actions:
            destination = ROOT / action.build.relative_path
            for original in {destination, action.previous_path} - {None}:
                assert isinstance(original, Path)
                if original.exists() and original not in touched:
                    saved = backup / original.relative_to(ROOT)
                    saved.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(original, saved)
                    touched.add(original)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.exists():
                created.add(destination)
            os.replace(stage / action.build.relative_path, destination)
            if action.previous_path and action.previous_path != destination:
                action.previous_path.unlink()
            if action.archive_source is not None:
                archive_name, _ = action.archive_source.split("\0", 1)
                archive_destination = ROOT / archive_name
                archive_destination.parent.mkdir(parents=True, exist_ok=True)
                if not archive_destination.exists():
                    created.add(archive_destination)
                os.replace(stage / archive_name, archive_destination)

        for name in ("INDEX.md", MANIFEST_PATH.name, REPORT_PATH.name):
            destination = ROOT / name
            if destination.exists() and destination not in touched:
                saved = backup / name
                saved.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(destination, saved)
                touched.add(destination)
            if not destination.exists():
                created.add(destination)
            os.replace(stage / name, destination)
    except Exception:
        for path in created:
            if path.exists():
                path.unlink()
        for original in touched:
            saved = backup / original.relative_to(ROOT)
            if saved.exists():
                original.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(saved, original)
        raise
    finally:
        shutil.rmtree(stage, ignore_errors=True)
        shutil.rmtree(backup, ignore_errors=True)


def main() -> None:
    builds = build_catalog()
    actions = plan_actions(builds)
    apply_actions(
        actions,
        render_index(builds),
        render_manifest(builds),
        render_report(builds, actions),
    )
    counts: dict[str, int] = {}
    for action in actions:
        counts[action.reason] = counts.get(action.reason, 0) + 1
    print("problems=800")
    for reason in sorted(counts):
        print(f"{reason}={counts[reason]}")
    print(f"manifest={MANIFEST_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
