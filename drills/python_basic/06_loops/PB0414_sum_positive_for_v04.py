"""
PB0414 — for 양수 합계

Chapter: Loops
Topic: For Loops
Seed: 42 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for로 숫자를 순회해 양수만 합산한다.

연습 초점
---------
for 내부 조건과 누적값

구현할 함수
-----------
def sum_positive_for(numbers: list[int]) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- sum_positive_for([-1, 2, 3]) == 5
- sum_positive_for([]) == 0
- sum_positive_for([0, -2]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0414 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_positive_for(numbers: list[int]) -> int:
    raise NotImplementedError("TODO: PB0414")


def self_test() -> None:
    assert sum_positive_for([-1, 2, 3]) == 5
    assert sum_positive_for([]) == 0
    assert sum_positive_for([0, -2]) == 0
