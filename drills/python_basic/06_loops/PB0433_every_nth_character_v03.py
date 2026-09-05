"""
PB0433 — n칸마다 문자

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 step으로 0번 인덱스부터 step 간격의 문자를 이어 붙여 반환한다.

연습 초점
---------
인덱스 range의 step

구현할 함수
-----------
def every_nth_character(text: str, step: int) -> str:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- every_nth_character('abcdefg', 2) == 'aceg'
- every_nth_character('', 3) == ''
- every_nth_character('abc', 5) == 'a'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0433 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def every_nth_character(text: str, step: int) -> str:
    raise NotImplementedError("TODO: PB0433")


def self_test() -> None:
    assert every_nth_character('abcdefg', 2) == 'aceg'
    assert every_nth_character('', 3) == ''
    assert every_nth_character('abc', 5) == 'a'
