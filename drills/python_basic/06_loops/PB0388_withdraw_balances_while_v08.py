"""
PB0388 — 반복 출금 잔액

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 amount를 balance에서 뺄 수 있는 동안 while로 출금하고 매번 남은 잔액을 반환한다.

연습 초점
---------
조건 충족 동안 상태 차감

구현할 함수
-----------
def withdraw_balances_while(balance: int, amount: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- withdraw_balances_while(10, 3) == [7, 4, 1]
- withdraw_balances_while(2, 3) == []
- withdraw_balances_while(6, 2) == [4, 2, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0388 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def withdraw_balances_while(balance: int, amount: int) -> list[int]:
    raise NotImplementedError("TODO: PB0388")


def self_test() -> None:
    assert withdraw_balances_while(10, 3) == [7, 4, 1]
    assert withdraw_balances_while(2, 3) == []
    assert withdraw_balances_while(6, 2) == [4, 2, 0]
