"""
PB0688 — 정확히 한 번 나온 값

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
values에서 정확히 한 번만 등장한 문자열을 set으로 반환한다.

연습 초점
---------
seen과 repeated set의 차집합

구현할 함수
-----------
def set_exactly_once(values: list[str]) -> set[str]:

예시 및 필수 테스트
-------------------
- set_exactly_once(['a', 'b', 'a', 'c']) == {'b', 'c'}
- set_exactly_once([]) == set()
- set_exactly_once(['x', 'x']) == set()

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0688 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_exactly_once(values: list[str]) -> set[str]:
    raise NotImplementedError("TODO: PB0688")


def self_test() -> None:
    assert set_exactly_once(['a', 'b', 'a', 'c']) == {'b', 'c'}
    assert set_exactly_once([]) == set()
    assert set_exactly_once(['x', 'x']) == set()
