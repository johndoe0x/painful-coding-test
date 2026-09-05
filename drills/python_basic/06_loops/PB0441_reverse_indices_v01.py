"""
PB0441 — 역순 인덱스

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
range를 사용해 length-1부터 0까지 인덱스를 반환하며 length가 0 이하면 빈 리스트를 반환한다.

연습 초점
---------
음수 step의 역순 인덱스

구현할 함수
-----------
def reverse_indices(length: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_indices(4) == [3, 2, 1, 0]
- reverse_indices(0) == []
- reverse_indices(1) == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0441 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_indices(length: int) -> list[int]:
    raise NotImplementedError("TODO: PB0441")


def self_test() -> None:
    assert reverse_indices(4) == [3, 2, 1, 0]
    assert reverse_indices(0) == []
    assert reverse_indices(1) == [0]
