"""
PB0451 — 중첩 곱셈표

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
중첩 for로 1부터 size까지의 size×size 곱셈표를 만들며 size가 0 이하면 빈 리스트를 반환한다.

연습 초점
---------
행과 열을 만드는 두 반복문

구현할 함수
-----------
def multiplication_table(size: int) -> list[list[int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- multiplication_table(2) == [[1, 2], [2, 4]]
- multiplication_table(0) == []
- multiplication_table(1) == [[1]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0451 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def multiplication_table(size: int) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0451")


def self_test() -> None:
    assert multiplication_table(2) == [[1, 2], [2, 4]]
    assert multiplication_table(0) == []
    assert multiplication_table(1) == [[1]]
