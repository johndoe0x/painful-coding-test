"""
PB0218 — 공백 입력 거부

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
text를 strip한 결과가 비어 있지 않은지를 not으로 표현하세요.

연습 초점
---------
정규화된 빈 값의 부정

구현할 함수
-----------
def is_nonblank(text: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- is_nonblank(' hello ') is True
- is_nonblank('') is False
- is_nonblank('   ') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0218 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_nonblank(text: str) -> bool:
    raise NotImplementedError("TODO: PB0218")


def self_test() -> None:
    assert is_nonblank(' hello ') is True
    assert is_nonblank('') is False
    assert is_nonblank('   ') is False
