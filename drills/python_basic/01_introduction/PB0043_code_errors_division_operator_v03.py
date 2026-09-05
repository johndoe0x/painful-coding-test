"""
PB0043 — 정수 나눗셈 연산자 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 //를 사용해 소수 부분을 버립니다. count가 양수일 때 /로 정확한 실수 평균을 반환하세요.

연습 초점
---------
버림 나눗셈과 실수 나눗셈의 결과 차이

구현할 함수
-----------
def corrected_average(total: float, count: int) -> float:

예시 및 필수 테스트
-------------------
- corrected_average(9, 2) == 4.5
- corrected_average(0, 1) == 0.0
- corrected_average(-6, 3) == -2.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0043 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def corrected_average(total: float, count: int) -> float:
    return total // count


def self_test() -> None:
    assert corrected_average(9, 2) == 4.5
    assert corrected_average(0, 1) == 0.0
    assert corrected_average(-6, 3) == -2.0
