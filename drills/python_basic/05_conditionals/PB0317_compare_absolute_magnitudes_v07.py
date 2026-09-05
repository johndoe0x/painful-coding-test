"""
PB0317 — 절댓값 크기 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
절댓값이 더 작은 쪽을 'left' 또는 'right'로 반환하고 같으면 'equal'을 반환한다.

연습 초점
---------
절댓값에 대한 대소·동등 비교

구현할 함수
-----------
def compare_absolute_magnitudes(left: int, right: int) -> str:

예시 및 필수 테스트
-------------------
- compare_absolute_magnitudes(-3, 5) == 'left'
- compare_absolute_magnitudes(-7, 7) == 'equal'
- compare_absolute_magnitudes(10, -2) == 'right'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0317 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def compare_absolute_magnitudes(left: int, right: int) -> str:
    raise NotImplementedError("TODO: PB0317")


def self_test() -> None:
    assert compare_absolute_magnitudes(-3, 5) == 'left'
    assert compare_absolute_magnitudes(-7, 7) == 'equal'
    assert compare_absolute_magnitudes(10, -2) == 'right'
