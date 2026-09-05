"""
PB0571 — 세 값을 리스트에 담기

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
세 값을 입력받은 순서 그대로 새 리스트에 담아 반환한다.

연습 초점
---------
서로 다른 타입도 한 리스트에 저장할 수 있음을 익힌다.

구현할 함수
-----------
def make_list(first: object, second: object, third: object) -> list[object]:

예시 및 필수 테스트
-------------------
- make_list(1, 'a', True) == [1, 'a', True]
- make_list(None, 2.5, []) == [None, 2.5, []]
- make_list('x', 'y', 'z') == ['x', 'y', 'z']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0571 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_list(first: object, second: object, third: object) -> list[object]:
    raise NotImplementedError("TODO: PB0571")


def self_test() -> None:
    assert make_list(1, 'a', True) == [1, 'a', True]
    assert make_list(None, 2.5, []) == [None, 2.5, []]
    assert make_list('x', 'y', 'z') == ['x', 'y', 'z']
