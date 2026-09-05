"""
PB0048 — 가려진 sum 함수 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 sum이라는 지역 정수를 만든 뒤 함수처럼 호출해 TypeError가 납니다. 내장 함수 이름을 가리지 않고 numbers의 합을 반환하세요.

연습 초점
---------
내장 함수 이름과 지역 변수 이름의 충돌 제거

구현할 함수
-----------
def corrected_total(numbers: list[int]) -> int:

예시 및 필수 테스트
-------------------
- corrected_total([1, 2, 3]) == 6
- corrected_total([]) == 0
- corrected_total([-1, 1]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0048 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def corrected_total(numbers: list[int]) -> int:
    sum = 0
    return sum(numbers)


def self_test() -> None:
    assert corrected_total([1, 2, 3]) == 6
    assert corrected_total([]) == 0
    assert corrected_total([-1, 1]) == 0
