"""
PB0311 — 두 정수 관계

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
a가 b보다 작으면 'less', 같으면 'equal', 크면 'greater'를 반환한다.

연습 초점
---------
<, ==, > 비교 연산자

구현할 함수
-----------
def compare_numbers(a: int, b: int) -> str:

예시 및 필수 테스트
-------------------
- compare_numbers(2, 5) == 'less'
- compare_numbers(3, 3) == 'equal'
- compare_numbers(-1, -4) == 'greater'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0311 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def compare_numbers(a: int, b: int) -> str:
    raise NotImplementedError("TODO: PB0311")


def self_test() -> None:
    assert compare_numbers(2, 5) == 'less'
    assert compare_numbers(3, 3) == 'equal'
    assert compare_numbers(-1, -4) == 'greater'
