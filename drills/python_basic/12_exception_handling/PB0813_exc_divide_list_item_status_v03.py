"""
PB0813 — 목록 값 나눗셈 상태

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
성공하면 ('ok', 결과), IndexError면 ('bad_index', None), ZeroDivisionError면 ('zero_divisor', None)를 반환한다.

연습 초점
---------
IndexError와 ZeroDivisionError 구별

구현할 함수
-----------
def exc_divide_list_item_status(values: list[int], index: int, divisor: int) -> tuple[str, float | None]:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_divide_list_item_status([10], 0, 2) == ('ok', 5.0)
- exc_divide_list_item_status([], 0, 2) == ('bad_index', None)
- exc_divide_list_item_status([10], 0, 0) == ('zero_divisor', None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0813 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_divide_list_item_status(values: list[int], index: int, divisor: int) -> tuple[str, float | None]:
    raise NotImplementedError("TODO: PB0813")


def self_test() -> None:
    assert exc_divide_list_item_status([10], 0, 2) == ('ok', 5.0)
    assert exc_divide_list_item_status([], 0, 2) == ('bad_index', None)
    assert exc_divide_list_item_status([10], 0, 0) == ('zero_divisor', None)
