"""
PB0574 — 연속 정수 리스트 만들기

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
start <= stop이면 start부터 stop까지 포함한 정수 리스트를, 아니면 빈 리스트를 반환한다.

연습 초점
---------
range 결과를 list로 변환하고 포함 경계를 조정한다.

구현할 함수
-----------
def make_inclusive_numbers(start: int, stop: int) -> list[int]:

예시 및 필수 테스트
-------------------
- make_inclusive_numbers(2, 5) == [2, 3, 4, 5]
- make_inclusive_numbers(-2, 0) == [-2, -1, 0]
- make_inclusive_numbers(4, 3) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0574 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_inclusive_numbers(start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0574")


def self_test() -> None:
    assert make_inclusive_numbers(2, 5) == [2, 3, 4, 5]
    assert make_inclusive_numbers(-2, 0) == [-2, -1, 0]
    assert make_inclusive_numbers(4, 3) == []
