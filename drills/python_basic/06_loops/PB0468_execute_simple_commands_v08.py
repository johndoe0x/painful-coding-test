"""
PB0468 — 단순 명령 처리

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
'quit'에서 break하고 'noop'은 continue하며 그전 다른 명령은 대문자로 반환한다.

연습 초점
---------
명령 스트림의 중단과 무시

구현할 함수
-----------
def execute_simple_commands(commands: list[str]) -> list[str]:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- execute_simple_commands(['run', 'noop', 'save', 'quit', 'load']) == ['RUN', 'SAVE']
- execute_simple_commands([]) == []
- execute_simple_commands(['quit']) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0468 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def execute_simple_commands(commands: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0468")


def self_test() -> None:
    assert execute_simple_commands(['run', 'noop', 'save', 'quit', 'load']) == ['RUN', 'SAVE']
    assert execute_simple_commands([]) == []
    assert execute_simple_commands(['quit']) == []
