"""
PB0188 — 증감 명령

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
'up'이면 += 1, 'down'이면 -= 1을 적용하세요.

연습 초점
---------
+=와 -=를 조건에 따라 사용

구현할 함수
-----------
def apply_counter_commands(start: int, commands: list[str]) -> int:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- apply_counter_commands(0, ['up', 'up', 'down']) == 1
- apply_counter_commands(5, []) == 5
- apply_counter_commands(0, ['down']) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0188 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_counter_commands(start: int, commands: list[str]) -> int:
    raise NotImplementedError("TODO: PB0188")


def self_test() -> None:
    assert apply_counter_commands(0, ['up', 'up', 'down']) == 1
    assert apply_counter_commands(5, []) == 5
    assert apply_counter_commands(0, ['down']) == -1
