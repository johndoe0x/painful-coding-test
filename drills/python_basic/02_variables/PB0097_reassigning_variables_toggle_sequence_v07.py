"""
PB0097 — 상태 여러 번 반전

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
state 변수를 toggle_count번 논리 부정해 최종 상태를 반환하세요.

연습 초점
---------
불리언 변수의 반복 재할당

구현할 함수
-----------
def apply_toggles(initial: bool, toggle_count: int) -> bool:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- apply_toggles(True, 3) is False
- apply_toggles(False, 0) is False
- apply_toggles(False, 2) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0097 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_toggles(initial: bool, toggle_count: int) -> bool:
    raise NotImplementedError("TODO: PB0097")


def self_test() -> None:
    assert apply_toggles(True, 3) is False
    assert apply_toggles(False, 0) is False
    assert apply_toggles(False, 2) is False
