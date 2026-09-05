"""
PB0110 — 좌표 쌍 언패킹

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
zip으로 만든 각 (x, y)를 두 변수에 할당해 '(x,y)' 형식 문자열로 반환하세요.

연습 초점
---------
병렬 시퀀스와 다중 할당

구현할 함수
-----------
def combine_coordinates(xs: list[int], ys: list[int]) -> list[str]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- combine_coordinates([1, 2], [3, 4]) == ['(1,3)', '(2,4)']
- combine_coordinates([], []) == []
- combine_coordinates([0, 1], [0]) == ['(0,0)']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0110 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def combine_coordinates(xs: list[int], ys: list[int]) -> list[str]:
    raise NotImplementedError("TODO: PB0110")


def self_test() -> None:
    assert combine_coordinates([1, 2], [3, 4]) == ['(1,3)', '(2,4)']
    assert combine_coordinates([], []) == []
    assert combine_coordinates([0, 1], [0]) == ['(0,0)']
