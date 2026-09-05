"""
PB0427 — 시작 이후 대상 위치

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(values)라고 가정하고 for와 range(start, len(values))로 target이 등장하는 인덱스만 반환한다.

연습 초점
---------
유효한 검색 시작 위치로 range 제한

구현할 함수
-----------
def target_positions_from(values: list[int], target: int, start: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- target_positions_from([1, 2, 1, 1], 1, 1) == [2, 3]
- target_positions_from([], 1, 0) == []
- target_positions_from([2, 2], 2, 2) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0427 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def target_positions_from(values: list[int], target: int, start: int) -> list[int]:
    raise NotImplementedError("TODO: PB0427")


def self_test() -> None:
    assert target_positions_from([1, 2, 1, 1], 1, 1) == [2, 3]
    assert target_positions_from([], 1, 0) == []
    assert target_positions_from([2, 2], 2, 2) == []
