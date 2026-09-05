"""
PB0271 — 실수 리스트 평균

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 실수 리스트의 평균을 반환한다.

연습 초점
---------
list[float] 입력과 float 반환 타입 힌트

구현할 함수
-----------
def average(numbers: list[float]) -> float:

예시 및 필수 테스트
-------------------
- average([2.0, 4.0]) == 3.0
- average([5.5]) == 5.5
- average([-2.0, 2.0]) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0271 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def average(numbers: list[float]) -> float:
    raise NotImplementedError("TODO: PB0271")


def self_test() -> None:
    assert average([2.0, 4.0]) == 3.0
    assert average([5.5]) == 5.5
    assert average([-2.0, 2.0]) == 0.0
