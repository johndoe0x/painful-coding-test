"""
PB0820 — 유효한 비율만 합산

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 10 / 10
Time cap: 150 seconds
Source checks: try, multiple_except

문제
----
각 pair를 float로 변환해 나눈다. ValueError나 ZeroDivisionError가 난 pair만 건너뛰고 나머지 결과를 합한다.

연습 초점
---------
반복문 내부 다중 except와 continue

구현할 함수
-----------
def exc_sum_valid_ratios(pairs: list[tuple[str, str]]) -> float:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_sum_valid_ratios([('6', '2'), ('1', '0'), ('x', '2')]) == 3.0
- exc_sum_valid_ratios([]) == 0.0
- exc_sum_valid_ratios([('1', '2'), ('3', '2')]) == 2.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0820 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_sum_valid_ratios(pairs: list[tuple[str, str]]) -> float:
    raise NotImplementedError("TODO: PB0820")


def self_test() -> None:
    assert exc_sum_valid_ratios([('6', '2'), ('1', '0'), ('x', '2')]) == 3.0
    assert exc_sum_valid_ratios([]) == 0.0
    assert exc_sum_valid_ratios([('1', '2'), ('3', '2')]) == 2.0
