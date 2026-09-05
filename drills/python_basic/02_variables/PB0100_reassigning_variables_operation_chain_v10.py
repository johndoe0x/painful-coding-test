"""
PB0100 — 연산 명령 적용

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
각 ('add'|'subtract'|'multiply', 값) 명령에 따라 current를 차례로 재할당하세요.

연습 초점
---------
명령 종류별 상태 갱신

구현할 함수
-----------
def apply_integer_operations(start: int, operations: list[tuple[str, int]]) -> int:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- apply_integer_operations(2, [('add', 3), ('multiply', 4)]) == 20
- apply_integer_operations(5, []) == 5
- apply_integer_operations(0, [('subtract', 2)]) == -2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0100 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_integer_operations(start: int, operations: list[tuple[str, int]]) -> int:
    raise NotImplementedError("TODO: PB0100")


def self_test() -> None:
    assert apply_integer_operations(2, [('add', 3), ('multiply', 4)]) == 20
    assert apply_integer_operations(5, []) == 5
    assert apply_integer_operations(0, [('subtract', 2)]) == -2
