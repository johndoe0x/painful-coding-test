"""
PB0534 — 짝수·홀수 위치로 분리하기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
짝수 인덱스 글자 문자열과 홀수 인덱스 글자 문자열을 tuple로 반환한다.

연습 초점
---------
같은 문자열에 시작점만 다른 step 슬라이스 두 개를 적용한다.

구현할 함수
-----------
def split_alternating_characters(text: str) -> tuple[str, str]:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- split_alternating_characters('abcdef') == ('ace', 'bdf')
- split_alternating_characters('abcde') == ('ace', 'bd')
- split_alternating_characters('') == ('', '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0534 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_alternating_characters(text: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0534")


def self_test() -> None:
    assert split_alternating_characters('abcdef') == ('ace', 'bdf')
    assert split_alternating_characters('abcde') == ('ace', 'bd')
    assert split_alternating_characters('') == ('', '')
