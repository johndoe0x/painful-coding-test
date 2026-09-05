from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Exercise:
    slug: str
    title: str
    signature: str
    task: str
    focus: str
    tests: tuple[str, str, str]
    time_cap: int = 120
    prelude: str = ""
    starter_body: str | None = None


def E(
    slug: str,
    title: str,
    signature: str,
    task: str,
    focus: str,
    test_1: str,
    test_2: str,
    test_3: str,
    time_cap: int = 120,
    *,
    prelude: str = "",
    starter_body: str | None = None,
) -> Exercise:
    """짧고 읽기 쉬운 문제 카탈로그 작성용 생성자."""
    return Exercise(
        slug=slug,
        title=title,
        signature=signature,
        task=task,
        focus=focus,
        tests=(test_1, test_2, test_3),
        time_cap=time_cap,
        prelude=prelude,
        starter_body=starter_body,
    )
