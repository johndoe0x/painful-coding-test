"""
PB0808 — 실수 변환 후 소수점 형식화

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: try

문제
----
text를 float로 변환해 소수점 digits자리 문자열로 반환한다. ValueError면 None이다.

연습 초점
---------
변환 예외 처리 후 동적 format specifier

구현할 함수
-----------
def exc_fixed_float_or_none(text: str, digits: int) -> str | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_fixed_float_or_none('3.1415', 2) == '3.14'
- exc_fixed_float_or_none('bad', 2) is None
- exc_fixed_float_or_none('2', 0) == '2'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0808 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_fixed_float_or_none(text: str, digits: int) -> str | None:
    raise NotImplementedError("TODO: PB0808")


def self_test() -> None:
    assert exc_fixed_float_or_none('3.1415', 2) == '3.14'
    assert exc_fixed_float_or_none('bad', 2) is None
    assert exc_fixed_float_or_none('2', 0) == '2'
