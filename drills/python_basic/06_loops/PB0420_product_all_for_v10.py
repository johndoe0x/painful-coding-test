"""
PB0420 — for 전체 곱

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: for

문제
----
1에서 시작해 for로 모든 정수를 곱하며 빈 리스트는 1을 반환한다.

연습 초점
---------
곱셈 누적값의 항등원

구현할 함수
-----------
def product_all_for(numbers: list[int]) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- product_all_for([2, 3, 4]) == 24
- product_all_for([]) == 1
- product_all_for([-2, 0, 5]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0420 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def product_all_for(numbers: list[int]) -> int:
    raise NotImplementedError("TODO: PB0420")


def self_test() -> None:
    assert product_all_for([2, 3, 4]) == 24
    assert product_all_for([]) == 1
    assert product_all_for([-2, 0, 5]) == 0
