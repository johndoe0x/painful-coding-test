"""
PB0421 — 시작값이 있는 range

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
range(start, stop)을 사용해 start 이상 stop 미만 정수를 반환한다.

연습 초점
---------
range의 start와 stop 인자

구현할 함수
-----------
def range_from_to(start: int, stop: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- range_from_to(2, 5) == [2, 3, 4]
- range_from_to(3, 3) == []
- range_from_to(-2, 1) == [-2, -1, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0421 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def range_from_to(start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0421")


def self_test() -> None:
    assert range_from_to(2, 5) == [2, 3, 4]
    assert range_from_to(3, 3) == []
    assert range_from_to(-2, 1) == [-2, -1, 0]
