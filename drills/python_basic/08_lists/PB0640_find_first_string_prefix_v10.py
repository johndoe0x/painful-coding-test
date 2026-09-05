"""
PB0640 — 접두사가 맞는 첫 문자열

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
prefix로 시작하는 첫 문자열을 반환하고 없으면 None을 반환한다.

연습 초점
---------
리스트 선형 탐색과 str.startswith 조건을 결합한다.

구현할 함수
-----------
def first_string_with_prefix(values: list[str], prefix: str) -> str | None:

예시 및 필수 테스트
-------------------
- first_string_with_prefix(['cat', 'car', 'dog'], 'ca') == 'cat'
- first_string_with_prefix(['apple', 'banana'], 'z') is None
- first_string_with_prefix(['', 'a'], '') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0640 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_string_with_prefix(values: list[str], prefix: str) -> str | None:
    raise NotImplementedError("TODO: PB0640")


def self_test() -> None:
    assert first_string_with_prefix(['cat', 'car', 'dog'], 'ca') == 'cat'
    assert first_string_with_prefix(['apple', 'banana'], 'z') is None
    assert first_string_with_prefix(['', 'a'], '') == ''
