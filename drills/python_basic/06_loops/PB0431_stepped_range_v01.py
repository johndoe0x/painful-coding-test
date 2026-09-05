"""
PB0431 — 간격 있는 range

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0이 아닌 step으로 range(start, stop, step)을 리스트로 반환한다.

연습 초점
---------
range의 세 번째 step 인자

구현할 함수
-----------
def stepped_range(start: int, stop: int, step: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- stepped_range(1, 8, 3) == [1, 4, 7]
- stepped_range(5, 5, 2) == []
- stepped_range(5, -1, -2) == [5, 3, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0431 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def stepped_range(start: int, stop: int, step: int) -> list[int]:
    raise NotImplementedError("TODO: PB0431")


def self_test() -> None:
    assert stepped_range(1, 8, 3) == [1, 4, 7]
    assert stepped_range(5, 5, 2) == []
    assert stepped_range(5, -1, -2) == [5, 3, 1]
