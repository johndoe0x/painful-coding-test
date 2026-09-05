"""
PB0562 — 성명 표시 형식 만들기

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
'<last>, <first>' 형식의 문자열을 반환한다.

연습 초점
---------
f-string 자리의 순서를 입력 매개변수 순서와 다르게 배치한다.

구현할 함수
-----------
def format_person_name(first: str, last: str) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_person_name('Ada', 'Lovelace') == 'Lovelace, Ada'
- format_person_name('Grace', 'Hopper') == 'Hopper, Grace'
- format_person_name('', 'Solo') == 'Solo, '

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0562 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_person_name(first: str, last: str) -> str:
    raise NotImplementedError("TODO: PB0562")


def self_test() -> None:
    assert format_person_name('Ada', 'Lovelace') == 'Lovelace, Ada'
    assert format_person_name('Grace', 'Hopper') == 'Hopper, Grace'
    assert format_person_name('', 'Solo') == 'Solo, '
