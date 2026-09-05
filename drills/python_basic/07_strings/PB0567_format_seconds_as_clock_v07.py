"""
PB0567 — 초를 시계 형식으로 표시하기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
0 이상인 total_seconds를 분과 초로 나누어 'MM:SS' 형식으로 반환한다.

연습 초점
---------
계산한 정수를 f-string에서 두 자리 0 채움으로 표현한다.

구현할 함수
-----------
def format_duration(total_seconds: int) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_duration(65) == '01:05'
- format_duration(9) == '00:09'
- format_duration(3599) == '59:59'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0567 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_duration(total_seconds: int) -> str:
    raise NotImplementedError("TODO: PB0567")


def self_test() -> None:
    assert format_duration(65) == '01:05'
    assert format_duration(9) == '00:09'
    assert format_duration(3599) == '59:59'
