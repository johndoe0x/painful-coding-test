"""
PB0565 — 비율을 퍼센트로 표시하기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
0 이상인 ratio를 퍼센트로 바꾸어 소수점 한 자리와 '%'를 붙여 반환한다.

연습 초점
---------
f-string의 퍼센트 형식 지정자를 사용한다.

구현할 함수
-----------
def format_percentage(ratio: float) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_percentage(0.125) == '12.5%'
- format_percentage(1.0) == '100.0%'
- format_percentage(0.0) == '0.0%'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0565 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_percentage(ratio: float) -> str:
    raise NotImplementedError("TODO: PB0565")


def self_test() -> None:
    assert format_percentage(0.125) == '12.5%'
    assert format_percentage(1.0) == '100.0%'
    assert format_percentage(0.0) == '0.0%'
