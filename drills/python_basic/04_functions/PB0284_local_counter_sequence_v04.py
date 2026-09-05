"""
PB0284 — 지역 카운터 수열

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
지역 counter를 0부터 limit까지 증가시키며 값을 담아 반환한다.

연습 초점
---------
호출마다 새로 생성되는 지역 상태

구현할 함수
-----------
def local_counter_sequence(limit: int) -> list[int]:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- local_counter_sequence(3) == [0, 1, 2, 3]
- local_counter_sequence(0) == [0]
- local_counter_sequence(-1) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0284 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def local_counter_sequence(limit: int) -> list[int]:
    raise NotImplementedError("TODO: PB0284")


def self_test() -> None:
    assert local_counter_sequence(3) == [0, 1, 2, 3]
    assert local_counter_sequence(0) == [0]
    assert local_counter_sequence(-1) == []
