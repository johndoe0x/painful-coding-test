"""
PB0532 — 홀수 인덱스 글자 모으기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
1번 인덱스부터 두 칸 간격으로 선택한 문자열을 반환한다.

연습 초점
---------
시작점 1과 step 2가 있는 슬라이스를 사용한다.

구현할 함수
-----------
def odd_index_characters(text: str) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- odd_index_characters('abcdef') == 'bdf'
- odd_index_characters('abcde') == 'bd'
- odd_index_characters('a') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0532 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def odd_index_characters(text: str) -> str:
    raise NotImplementedError("TODO: PB0532")


def self_test() -> None:
    assert odd_index_characters('abcdef') == 'bdf'
    assert odd_index_characters('abcde') == 'bd'
    assert odd_index_characters('a') == ''
