"""
PB0368 — 직사각형 내부 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
left<=x<=right이고 top<=y<=bottom이면 경계를 포함해 True를 반환한다.

연습 초점
---------
두 축의 연쇄 비교를 and로 결합

구현할 함수
-----------
def point_inside_rectangle(x: int, y: int, left: int, top: int, right: int, bottom: int) -> bool:

예시 및 필수 테스트
-------------------
- point_inside_rectangle(2, 3, 0, 0, 5, 5) is True
- point_inside_rectangle(5, 5, 0, 0, 5, 5) is True
- point_inside_rectangle(-1, 2, 0, 0, 5, 5) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0368 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def point_inside_rectangle(x: int, y: int, left: int, top: int, right: int, bottom: int) -> bool:
    raise NotImplementedError("TODO: PB0368")


def self_test() -> None:
    assert point_inside_rectangle(2, 3, 0, 0, 5, 5) is True
    assert point_inside_rectangle(5, 5, 0, 0, 5, 5) is True
    assert point_inside_rectangle(-1, 2, 0, 0, 5, 5) is False
