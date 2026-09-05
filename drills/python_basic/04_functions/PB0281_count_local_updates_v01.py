"""
PB0281 — 지역 양수 카운터

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
함수 내부 카운터만 사용해 양수 개수를 반환한다.

연습 초점
---------
전역 상태 없이 지역 변수 갱신

구현할 함수
-----------
def count_local_updates(values: list[int]) -> int:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- count_local_updates([-1, 2, 3]) == 2
- count_local_updates([]) == 0
- count_local_updates([0, -2]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0281 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_local_updates(values: list[int]) -> int:
    raise NotImplementedError("TODO: PB0281")


def self_test() -> None:
    assert count_local_updates([-1, 2, 3]) == 2
    assert count_local_updates([]) == 0
    assert count_local_updates([0, -2]) == 0
