"""
PB0814 — 백분율 파싱 상태

Chapter: Exception Handling
Topic: Multiple Except Blocks
Seed: 82 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: try, multiple_except

문제
----
float 변환 후 part/whole*100을 계산한다. ValueError와 ZeroDivisionError를 각각 invalid, zero_whole 상태로 구분한다.

연습 초점
---------
실수 변환과 0 나눗셈의 예외 분기

구현할 함수
-----------
def exc_percentage_status(part: str, whole: str) -> tuple[str, float | None]:

필수 구현 방식
--------------
- try-except를 사용한다.
- 함수 안에 둘 이상의 except 블록을 사용한다.

예시 및 필수 테스트
-------------------
- exc_percentage_status('1', '4') == ('ok', 25.0)
- exc_percentage_status('x', '4') == ('invalid', None)
- exc_percentage_status('1', '0') == ('zero_whole', None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0814 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_percentage_status(part: str, whole: str) -> tuple[str, float | None]:
    raise NotImplementedError("TODO: PB0814")


def self_test() -> None:
    assert exc_percentage_status('1', '4') == ('ok', 25.0)
    assert exc_percentage_status('x', '4') == ('invalid', None)
    assert exc_percentage_status('1', '0') == ('zero_whole', None)
