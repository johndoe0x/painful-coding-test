"""
PB0563 — 점수와 만점 표시하기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
'<name>: <score>/<maximum>' 형식으로 반환한다.

연습 초점
---------
여러 타입의 값을 f-string 한 줄에 삽입한다.

구현할 함수
-----------
def format_score_line(name: str, score: int, maximum: int) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_score_line('Ada', 95, 100) == 'Ada: 95/100'
- format_score_line('Kim', 0, 10) == 'Kim: 0/10'
- format_score_line('', 3, 5) == ': 3/5'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0563 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_score_line(name: str, score: int, maximum: int) -> str:
    raise NotImplementedError("TODO: PB0563")


def self_test() -> None:
    assert format_score_line('Ada', 95, 100) == 'Ada: 95/100'
    assert format_score_line('Kim', 0, 10) == 'Kim: 0/10'
    assert format_score_line('', 3, 5) == ': 3/5'
