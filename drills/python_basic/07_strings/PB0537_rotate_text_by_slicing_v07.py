"""
PB0537 — 문자열 왼쪽 회전하기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
빈 문자열은 그대로 반환하고, 그 외에는 amount를 길이로 나눈 나머지만큼 왼쪽으로 회전한다.

연습 초점
---------
두 슬라이스를 순서를 바꿔 결합하고 큰 회전량을 정규화한다.

구현할 함수
-----------
def rotate_text_left(text: str, amount: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- rotate_text_left('abcdef', 2) == 'cdefab'
- rotate_text_left('abc', 4) == 'bca'
- rotate_text_left('', 3) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0537 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rotate_text_left(text: str, amount: int) -> str:
    raise NotImplementedError("TODO: PB0537")


def self_test() -> None:
    assert rotate_text_left('abcdef', 2) == 'cdefab'
    assert rotate_text_left('abc', 4) == 'bca'
    assert rotate_text_left('', 3) == ''
