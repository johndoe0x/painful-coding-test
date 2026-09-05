"""
PB0818 — 딕셔너리 값 나눗셈

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
mapping[key]/divisor를 계산한다. KeyError와 ZeroDivisionError를 missing과 zero로 구분한다.

연습 초점
---------
컨테이너 조회와 산술 예외 분리

구현할 함수
-----------
def exc_divide_mapping_status(mapping: dict[str, int], key: str, divisor: int) -> tuple[str, float | None]:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_divide_mapping_status({'a': 8}, 'a', 2) == ('ok', 4.0)
- exc_divide_mapping_status({}, 'a', 2) == ('missing', None)
- exc_divide_mapping_status({'a': 8}, 'a', 0) == ('zero', None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0818 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_divide_mapping_status(mapping: dict[str, int], key: str, divisor: int) -> tuple[str, float | None]:
    raise NotImplementedError("TODO: PB0818")


def self_test() -> None:
    assert exc_divide_mapping_status({'a': 8}, 'a', 2) == ('ok', 4.0)
    assert exc_divide_mapping_status({}, 'a', 2) == ('missing', None)
    assert exc_divide_mapping_status({'a': 8}, 'a', 0) == ('zero', None)
