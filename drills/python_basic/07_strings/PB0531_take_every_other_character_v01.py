"""
PB0531 — 한 글자씩 건너뛰기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
0번 인덱스부터 두 칸 간격으로 선택한 문자열을 반환한다.

연습 초점
---------
슬라이스의 step 자리에 2를 사용한다.

구현할 함수
-----------
def every_other(text: str) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- every_other('abcdef') == 'ace'
- every_other('abcde') == 'ace'
- every_other('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0531 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def every_other(text: str) -> str:
    raise NotImplementedError("TODO: PB0531")


def self_test() -> None:
    assert every_other('abcdef') == 'ace'
    assert every_other('abcde') == 'ace'
    assert every_other('') == ''
