"""
PB0573 — 같은 값으로 리스트 채우기

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
value는 int, float, bool, str, tuple, None처럼 변경할 수 없는 값이고 count는 0 이상이라고 가정한다. value를 count번 담은 리스트를 반환한다.

연습 초점
---------
가변 객체의 참조 공유 문제 없이 불변 값을 정해진 횟수만큼 배치한다.

구현할 함수
-----------
def repeated_values(value: object, count: int) -> list[object]:

예시 및 필수 테스트
-------------------
- repeated_values('x', 3) == ['x', 'x', 'x']
- repeated_values(0, 1) == [0]
- repeated_values(True, 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0573 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeated_values(value: object, count: int) -> list[object]:
    raise NotImplementedError("TODO: PB0573")


def self_test() -> None:
    assert repeated_values('x', 3) == ['x', 'x', 'x']
    assert repeated_values(0, 1) == [0]
    assert repeated_values(True, 0) == []
