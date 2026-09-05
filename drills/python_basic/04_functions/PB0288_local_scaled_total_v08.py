"""
PB0288 — 지역 배율 합계

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
지역 total에 각 value*factor를 누적해 반환한다.

연습 초점
---------
반복 계산에 한정된 지역 변수 사용

구현할 함수
-----------
def local_scaled_total(values: list[int], factor: int) -> int:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- local_scaled_total([1, 2, 3], 2) == 12
- local_scaled_total([], 5) == 0
- local_scaled_total([-2, 4], -1) == -2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0288 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def local_scaled_total(values: list[int], factor: int) -> int:
    raise NotImplementedError("TODO: PB0288")


def self_test() -> None:
    assert local_scaled_total([1, 2, 3], 2) == 12
    assert local_scaled_total([], 5) == 0
    assert local_scaled_total([-2, 4], -1) == -2
