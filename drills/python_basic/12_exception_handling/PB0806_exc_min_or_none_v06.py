"""
PB0806 — 빈 sequence 안전 최솟값

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: try

문제
----
min(values)를 반환하고 빈 리스트로 ValueError가 발생하면 None을 반환한다.

연습 초점
---------
내장 함수가 발생시키는 ValueError 처리

구현할 함수
-----------
def exc_min_or_none(values: list[int]) -> int | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_min_or_none([3, 1, 2]) == 1
- exc_min_or_none([]) is None
- exc_min_or_none([-1]) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0806 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_min_or_none(values: list[int]) -> int | None:
    raise NotImplementedError("TODO: PB0806")


def self_test() -> None:
    assert exc_min_or_none([3, 1, 2]) == 1
    assert exc_min_or_none([]) is None
    assert exc_min_or_none([-1]) == -1
