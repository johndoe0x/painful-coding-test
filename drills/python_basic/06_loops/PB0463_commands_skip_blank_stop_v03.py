"""
PB0463 — 빈 명령 건너뛰기

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
빈 문자열은 continue하고 'STOP'을 만나면 break하며 그전 명령을 소문자로 반환한다.

연습 초점
---------
continue 필터와 break 종료 순서

구현할 함수
-----------
def commands_skip_blank_stop(commands: list[str]) -> list[str]:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- commands_skip_blank_stop(['RUN', '', 'WAIT', 'STOP', 'GO']) == ['run', 'wait']
- commands_skip_blank_stop([]) == []
- commands_skip_blank_stop(['STOP']) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0463 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def commands_skip_blank_stop(commands: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0463")


def self_test() -> None:
    assert commands_skip_blank_stop(['RUN', '', 'WAIT', 'STOP', 'GO']) == ['run', 'wait']
    assert commands_skip_blank_stop([]) == []
    assert commands_skip_blank_stop(['STOP']) == []
