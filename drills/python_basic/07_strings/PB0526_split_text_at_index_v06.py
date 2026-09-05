"""
PB0526 — 한 위치에서 문자열 나누기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
Python 슬라이스 규칙에 따라 index 앞부분과 index 이후 부분을 tuple로 반환한다.

연습 초점
---------
같은 경계를 끝 인덱스와 시작 인덱스로 사용한다.

구현할 함수
-----------
def split_text_at(text: str, index: int) -> tuple[str, str]:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- split_text_at('python', 2) == ('py', 'thon')
- split_text_at('abc', 0) == ('', 'abc')
- split_text_at('abc', 10) == ('abc', '')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0526 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_text_at(text: str, index: int) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0526")


def self_test() -> None:
    assert split_text_at('python', 2) == ('py', 'thon')
    assert split_text_at('abc', 0) == ('', 'abc')
    assert split_text_at('abc', 10) == ('abc', '')
