"""
PB0564 — 좌표 표시하기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
각 좌표를 소수점 한 자리로 표시해 '(x, y)' 형식으로 반환한다.

연습 초점
---------
두 실수에 동일한 고정 소수점 형식을 적용한다.

구현할 함수
-----------
def format_coordinates(x: float, y: float) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_coordinates(1, 2) == '(1.0, 2.0)'
- format_coordinates(-1.25, 3.76) == '(-1.2, 3.8)'
- format_coordinates(0.0, 0.0) == '(0.0, 0.0)'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0564 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_coordinates(x: float, y: float) -> str:
    raise NotImplementedError("TODO: PB0564")


def self_test() -> None:
    assert format_coordinates(1, 2) == '(1.0, 2.0)'
    assert format_coordinates(-1.25, 3.76) == '(-1.2, 3.8)'
    assert format_coordinates(0.0, 0.0) == '(0.0, 0.0)'
