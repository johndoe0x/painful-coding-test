"""
PB0199 — 축 위의 좌표

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
x 또는 y가 0이면 좌표축 위이므로 True를 반환하세요.

연습 초점
---------
두 수치 동등 조건의 OR

구현할 함수
-----------
def lies_on_axis(x: int, y: int) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- lies_on_axis(0, 5) is True
- lies_on_axis(0, 0) is True
- lies_on_axis(2, 3) is False and lies_on_axis(5, 0) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0199 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def lies_on_axis(x: int, y: int) -> bool:
    raise NotImplementedError("TODO: PB0199")


def self_test() -> None:
    assert lies_on_axis(0, 5) is True
    assert lies_on_axis(0, 0) is True
    assert lies_on_axis(2, 3) is False and lies_on_axis(5, 0) is True
