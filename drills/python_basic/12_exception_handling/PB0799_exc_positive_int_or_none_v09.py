"""
PB0799 — 양의 정수만 허용

Chapter: Exception Handling
Topic: Try Except
Seed: 80 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: try

문제
----
int 변환 후 값이 0 이하이면 직접 ValueError를 발생시킨다. ValueError는 잡아서 None을 반환한다.

연습 초점
---------
검증 실패를 예외로 통합

구현할 함수
-----------
def exc_positive_int_or_none(text: str) -> int | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_positive_int_or_none('5') == 5
- exc_positive_int_or_none('0') is None
- exc_positive_int_or_none('bad') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0799 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_positive_int_or_none(text: str) -> int | None:
    raise NotImplementedError("TODO: PB0799")


def self_test() -> None:
    assert exc_positive_int_or_none('5') == 5
    assert exc_positive_int_or_none('0') is None
    assert exc_positive_int_or_none('bad') is None
