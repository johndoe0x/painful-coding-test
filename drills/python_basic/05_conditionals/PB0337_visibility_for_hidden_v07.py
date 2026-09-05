"""
PB0337 — 숨김 상태 라벨

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 label을 'visible'로 정하고 hidden이면 if 안에서 'hidden'으로 바꿔 반환한다.

연습 초점
---------
블록 안 문자열 재할당의 범위

구현할 함수
-----------
def visibility_for_hidden(hidden: bool) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- visibility_for_hidden(True) == 'hidden'
- visibility_for_hidden(False) == 'visible'
- visibility_for_hidden(not True) == 'visible'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0337 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def visibility_for_hidden(hidden: bool) -> str:
    raise NotImplementedError("TODO: PB0337")


def self_test() -> None:
    assert visibility_for_hidden(True) == 'hidden'
    assert visibility_for_hidden(False) == 'visible'
    assert visibility_for_hidden(not True) == 'visible'
