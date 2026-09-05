"""
PB0809 — 문자열 목록의 특정 정수

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: try

문제
----
texts[index]를 int로 변환한다. IndexError 또는 ValueError면 None을 반환한다.

연습 초점
---------
조회와 변환의 두 오류 경계

구현할 함수
-----------
def exc_int_at_or_none(texts: list[str], index: int) -> int | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_int_at_or_none(['10', '20'], 1) == 20
- exc_int_at_or_none(['x'], 0) is None
- exc_int_at_or_none([], 0) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0809 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_int_at_or_none(texts: list[str], index: int) -> int | None:
    raise NotImplementedError("TODO: PB0809")


def self_test() -> None:
    assert exc_int_at_or_none(['10', '20'], 1) == 20
    assert exc_int_at_or_none(['x'], 0) is None
    assert exc_int_at_or_none([], 0) is None
