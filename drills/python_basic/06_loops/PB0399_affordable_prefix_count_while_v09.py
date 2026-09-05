"""
PB0399 — 예산으로 살 수 있는 앞 항목

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: while

문제
----
앞에서부터 가격을 지불할 수 있는 동안 while로 차감해 연속 구매 가능한 항목 수를 반환한다.

연습 초점
---------
인덱스·남은 예산·카운터 관리

구현할 함수
-----------
def affordable_prefix_count_while(budget: int, prices: list[int]) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- affordable_prefix_count_while(10, [3, 4, 5]) == 2
- affordable_prefix_count_while(2, [3]) == 0
- affordable_prefix_count_while(0, []) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0399 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def affordable_prefix_count_while(budget: int, prices: list[int]) -> int:
    raise NotImplementedError("TODO: PB0399")


def self_test() -> None:
    assert affordable_prefix_count_while(10, [3, 4, 5]) == 2
    assert affordable_prefix_count_while(2, [3]) == 0
    assert affordable_prefix_count_while(0, []) == 0
