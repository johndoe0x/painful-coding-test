"""
PB0155 — 첫 값 또는 None

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
values가 비면 None, 아니면 첫 원소를 반환하세요.

연습 초점
---------
빈 컬렉션의 sentinel 값

구현할 함수
-----------
def first_or_none(values: list[object]) -> object | None:

예시 및 필수 테스트
-------------------
- first_or_none([0, 1]) == 0
- first_or_none([]) is None
- first_or_none([None]) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0155 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_or_none(values: list[object]) -> object | None:
    raise NotImplementedError("TODO: PB0155")


def self_test() -> None:
    assert first_or_none([0, 1]) == 0
    assert first_or_none([]) is None
    assert first_or_none([None]) is None
