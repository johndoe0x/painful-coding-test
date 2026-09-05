"""
PB0340 — 배터리 절약 모드

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 mode를 'normal'로 정하고 percent가 20 미만이면 if 안에서 'saving'으로 바꿔 반환한다.

연습 초점
---------
경계 조건과 지역 변수 유효 범위

구현할 함수
-----------
def battery_mode_below_threshold(percent: int) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- battery_mode_below_threshold(19) == 'saving'
- battery_mode_below_threshold(20) == 'normal'
- battery_mode_below_threshold(0) == 'saving'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0340 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def battery_mode_below_threshold(percent: int) -> str:
    raise NotImplementedError("TODO: PB0340")


def self_test() -> None:
    assert battery_mode_below_threshold(19) == 'saving'
    assert battery_mode_below_threshold(20) == 'normal'
    assert battery_mode_below_threshold(0) == 'saving'
