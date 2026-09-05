"""
PB0538 — 세 글자 블록의 첫 글자

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
block_size가 양수라고 가정하고 각 block_size 길이 블록의 첫 글자들을 반환한다.

연습 초점
---------
0에서 시작하는 가변 step 슬라이스를 블록 선택으로 해석한다.

구현할 함수
-----------
def block_starts(text: str, block_size: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- block_starts('abcdefghij', 3) == 'adgj'
- block_starts('abc', 5) == 'a'
- block_starts('', 2) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0538 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def block_starts(text: str, block_size: int) -> str:
    raise NotImplementedError("TODO: PB0538")


def self_test() -> None:
    assert block_starts('abcdefghij', 3) == 'adgj'
    assert block_starts('abc', 5) == 'a'
    assert block_starts('', 2) == ''
