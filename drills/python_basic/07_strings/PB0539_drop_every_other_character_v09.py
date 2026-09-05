"""
PB0539 — 첫 글자를 버리고 번갈아 선택하기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
drop과 step이 양수라고 가정해 앞 drop글자를 제외한 뒤 남은 문자열에서 step 간격으로 선택한다.

연습 초점
---------
슬라이스 시작과 보폭을 실제 요구사항으로 변환한다.

구현할 함수
-----------
def drop_then_stride(text: str, drop: int, step: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- drop_then_stride('abcdefgh', 2, 2) == 'ceg'
- drop_then_stride('python', 1, 3) == 'yo'
- drop_then_stride('abc', 5, 2) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0539 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def drop_then_stride(text: str, drop: int, step: int) -> str:
    raise NotImplementedError("TODO: PB0539")


def self_test() -> None:
    assert drop_then_stride('abcdefgh', 2, 2) == 'ceg'
    assert drop_then_stride('python', 1, 3) == 'yo'
    assert drop_then_stride('abc', 5, 2) == ''
