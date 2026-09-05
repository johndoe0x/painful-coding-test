"""
PB0326 — 5의 배수 표시

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: if

문제
----
기본 결과는 'plain'이며 number가 5의 배수일 때만 'multiple'을 반환한다.

연습 초점
---------
나머지 조건을 단일 if에 사용

구현할 함수
-----------
def mark_if_multiple_of_five(number: int) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- mark_if_multiple_of_five(10) == 'multiple'
- mark_if_multiple_of_five(7) == 'plain'
- mark_if_multiple_of_five(0) == 'multiple'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0326 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mark_if_multiple_of_five(number: int) -> str:
    raise NotImplementedError("TODO: PB0326")


def self_test() -> None:
    assert mark_if_multiple_of_five(10) == 'multiple'
    assert mark_if_multiple_of_five(7) == 'plain'
    assert mark_if_multiple_of_five(0) == 'multiple'
