"""
PB0456 — 체커보드 만들기

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
중첩 for로 (행+열)이 짝수면 '#', 홀수면 '.'인 보드를 반환한다.

연습 초점
---------
중첩 인덱스의 결합 조건

구현할 함수
-----------
def checkerboard_nested(rows: int, columns: int) -> list[list[str]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- checkerboard_nested(2, 3) == [['#', '.', '#'], ['.', '#', '.']]
- checkerboard_nested(0, 2) == []
- checkerboard_nested(1, 1) == [['#']]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0456 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def checkerboard_nested(rows: int, columns: int) -> list[list[str]]:
    raise NotImplementedError("TODO: PB0456")


def self_test() -> None:
    assert checkerboard_nested(2, 3) == [['#', '.', '#'], ['.', '#', '.']]
    assert checkerboard_nested(0, 2) == []
    assert checkerboard_nested(1, 1) == [['#']]
