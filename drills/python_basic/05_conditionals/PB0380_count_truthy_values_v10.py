"""
PB0380 — Truthy 값 개수

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: if

문제
----
각 원소를 조건으로 평가해 truthy인 값의 개수를 반환한다.

연습 초점
---------
서로 다른 타입의 truthiness 반복 확인

구현할 함수
-----------
def count_truthy_values(values: list[object]) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- count_truthy_values([1, 0, '', 'x']) == 2
- count_truthy_values([]) == 0
- count_truthy_values([None, [], [0]]) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0380 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_truthy_values(values: list[object]) -> int:
    raise NotImplementedError("TODO: PB0380")


def self_test() -> None:
    assert count_truthy_values([1, 0, '', 'x']) == 2
    assert count_truthy_values([]) == 0
    assert count_truthy_values([None, [], [0]]) == 1
