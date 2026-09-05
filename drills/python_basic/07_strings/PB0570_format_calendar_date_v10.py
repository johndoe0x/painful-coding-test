"""
PB0570 — 날짜를 0 채움 형식으로 표시하기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
유효한 날짜 구성요소를 'YYYY-MM-DD' 형태로 0을 채워 반환한다.

연습 초점
---------
정수별 최소 너비와 0 채움 형식 지정자를 사용한다.

구현할 함수
-----------
def format_date(year: int, month: int, day: int) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_date(2026, 8, 24) == '2026-08-24'
- format_date(7, 1, 2) == '0007-01-02'
- format_date(1999, 12, 31) == '1999-12-31'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0570 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_date(year: int, month: int, day: int) -> str:
    raise NotImplementedError("TODO: PB0570")


def self_test() -> None:
    assert format_date(2026, 8, 24) == '2026-08-24'
    assert format_date(7, 1, 2) == '0007-01-02'
    assert format_date(1999, 12, 31) == '1999-12-31'
