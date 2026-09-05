"""
PB0807 — 정확히 두 token unpack

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: try

문제
----
split 결과를 정확히 두 변수에 unpack한다. 개수가 달라 ValueError가 나면 None을 반환한다.

연습 초점
---------
sequence unpacking의 ValueError 처리

구현할 함수
-----------
def exc_unpack_pair_or_none(line: str) -> tuple[str, str] | None:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_unpack_pair_or_none('a b') == ('a', 'b')
- exc_unpack_pair_or_none('a') is None
- exc_unpack_pair_or_none('a b c') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0807 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_unpack_pair_or_none(line: str) -> tuple[str, str] | None:
    raise NotImplementedError("TODO: PB0807")


def self_test() -> None:
    assert exc_unpack_pair_or_none('a b') == ('a', 'b')
    assert exc_unpack_pair_or_none('a') is None
    assert exc_unpack_pair_or_none('a b c') is None
