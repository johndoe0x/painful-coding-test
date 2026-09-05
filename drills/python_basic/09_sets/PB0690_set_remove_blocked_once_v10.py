"""
PB0690 — 차단값 제외 후 중복 제거

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
blocked 값은 버리고 나머지는 최초 등장 한 번씩만 순서대로 반환한다.

연습 초점
---------
필터링과 seen set 결합

구현할 함수
-----------
def set_remove_blocked_once(values: list[str], blocked: set[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- set_remove_blocked_once(['a', 'x', 'a', 'b'], {'x'}) == ['a', 'b']
- set_remove_blocked_once([], {'x'}) == []
- set_remove_blocked_once(['x', 'x'], {'x'}) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0690 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_remove_blocked_once(values: list[str], blocked: set[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0690")


def self_test() -> None:
    assert set_remove_blocked_once(['a', 'x', 'a', 'b'], {'x'}) == ['a', 'b']
    assert set_remove_blocked_once([], {'x'}) == []
    assert set_remove_blocked_once(['x', 'x'], {'x'}) == []
