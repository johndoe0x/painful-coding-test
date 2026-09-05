"""
PB0347 — 절댓값 분기 계산

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
number가 음수면 부호를 반전하고 아니면 그대로 반환한다.

연습 초점
---------
계산식이 다른 if-else 분기

구현할 함수
-----------
def absolute_with_if_else(number: int) -> int:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- absolute_with_if_else(-7) == 7
- absolute_with_if_else(0) == 0
- absolute_with_if_else(5) == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0347 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def absolute_with_if_else(number: int) -> int:
    raise NotImplementedError("TODO: PB0347")


def self_test() -> None:
    assert absolute_with_if_else(-7) == 7
    assert absolute_with_if_else(0) == 0
    assert absolute_with_if_else(5) == 5
