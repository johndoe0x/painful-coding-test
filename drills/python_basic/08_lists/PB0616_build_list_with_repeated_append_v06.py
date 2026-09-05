"""
PB0616 — append로 반복 리스트 만들기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
count가 0 이상이라고 가정하고 리스트 곱셈 없이 value를 count번 append한 리스트를 반환한다.

연습 초점
---------
반복 횟수만큼 append하여 리스트 크기가 변하는 과정을 익힌다.

구현할 함수
-----------
def build_repeated_list(value: int, count: int) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- build_repeated_list(7, 3) == [7, 7, 7]
- build_repeated_list(-1, 1) == [-1]
- build_repeated_list(0, 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0616 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def build_repeated_list(value: int, count: int) -> list[int]:
    raise NotImplementedError("TODO: PB0616")


def self_test() -> None:
    assert build_repeated_list(7, 3) == [7, 7, 7]
    assert build_repeated_list(-1, 1) == [-1]
    assert build_repeated_list(0, 0) == []
