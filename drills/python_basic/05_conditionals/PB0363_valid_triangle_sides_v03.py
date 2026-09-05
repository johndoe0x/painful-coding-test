"""
PB0363 — 삼각형 성립 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
세 변이 모두 양수이고 어느 두 변의 합도 나머지 변보다 클 때 True를 반환한다.

연습 초점
---------
여러 비교 조건을 and로 결합

구현할 함수
-----------
def valid_triangle_sides(a: float, b: float, c: float) -> bool:

예시 및 필수 테스트
-------------------
- valid_triangle_sides(3.0, 4.0, 5.0) is True
- valid_triangle_sides(1.0, 2.0, 3.0) is False
- valid_triangle_sides(-1.0, 2.0, 2.0) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0363 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def valid_triangle_sides(a: float, b: float, c: float) -> bool:
    raise NotImplementedError("TODO: PB0363")


def self_test() -> None:
    assert valid_triangle_sides(3.0, 4.0, 5.0) is True
    assert valid_triangle_sides(1.0, 2.0, 3.0) is False
    assert valid_triangle_sides(-1.0, 2.0, 2.0) is False
