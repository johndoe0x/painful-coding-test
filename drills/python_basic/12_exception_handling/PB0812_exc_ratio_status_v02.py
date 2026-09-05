"""
PB0812 — 비율 계산 상태 구분

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
정상이면 'ok:<결과>', ValueError면 'invalid_number', ZeroDivisionError면 'division_by_zero'를 반환한다.

연습 초점
---------
예외 타입별 서로 다른 복구 결과

구현할 함수
-----------
def exc_ratio_status(left: str, right: str) -> str:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_ratio_status('6', '2') == 'ok:3.0'
- exc_ratio_status('x', '2') == 'invalid_number'
- exc_ratio_status('1', '0') == 'division_by_zero'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0812 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_ratio_status(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0812")


def self_test() -> None:
    assert exc_ratio_status('6', '2') == 'ok:3.0'
    assert exc_ratio_status('x', '2') == 'invalid_number'
    assert exc_ratio_status('1', '0') == 'division_by_zero'
