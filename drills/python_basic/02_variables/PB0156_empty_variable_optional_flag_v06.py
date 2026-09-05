"""
PB0156 — 선택적 불리언 표시

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
flag가 None이면 'unset', True면 'on', False면 'off'를 반환하세요.

연습 초점
---------
세 상태를 가진 선택적 bool

구현할 함수
-----------
def optional_flag_label(flag: bool | None) -> str:

예시 및 필수 테스트
-------------------
- optional_flag_label(True) == 'on'
- optional_flag_label(False) == 'off'
- optional_flag_label(None) == 'unset'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0156 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_flag_label(flag: bool | None) -> str:
    raise NotImplementedError("TODO: PB0156")


def self_test() -> None:
    assert optional_flag_label(True) == 'on'
    assert optional_flag_label(False) == 'off'
    assert optional_flag_label(None) == 'unset'
