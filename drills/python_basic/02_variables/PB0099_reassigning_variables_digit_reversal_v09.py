"""
PB0099 — 숫자 뒤집기 누적

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
number가 0 이상일 때 result와 남은 number를 재할당하며 십진수 자릿수를 뒤집으세요.

연습 초점
---------
두 상태 변수의 반복 갱신

구현할 함수
-----------
def reverse_digits(number: int) -> int:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- reverse_digits(1203) == 3021
- reverse_digits(0) == 0
- reverse_digits(7) == 7

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0099 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_digits(number: int) -> int:
    raise NotImplementedError("TODO: PB0099")


def self_test() -> None:
    assert reverse_digits(1203) == 3021
    assert reverse_digits(0) == 0
    assert reverse_digits(7) == 7
