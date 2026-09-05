"""
PB0316 — 마지막 자릿수 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 정수의 절댓값 기준 마지막 자릿수가 같은지 반환한다.

연습 초점
---------
가공한 두 값의 동등 비교

구현할 함수
-----------
def same_last_digit(left: int, right: int) -> bool:

예시 및 필수 테스트
-------------------
- same_last_digit(27, 7) is True
- same_last_digit(-12, 22) is True
- same_last_digit(10, 11) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0316 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def same_last_digit(left: int, right: int) -> bool:
    raise NotImplementedError("TODO: PB0316")


def self_test() -> None:
    assert same_last_digit(27, 7) is True
    assert same_last_digit(-12, 22) is True
    assert same_last_digit(10, 11) is False
