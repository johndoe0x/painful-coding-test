"""
PB0146 — 숫자 크기 비교

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
사전식 문자열 비교가 아니라 float 값으로 변환해 left가 더 큰지 반환하세요.

연습 초점
---------
표현 타입과 비교 의미 일치

구현할 함수
-----------
def greater_numeric_text(left: str, right: str) -> bool:

예시 및 필수 테스트
-------------------
- greater_numeric_text('10', '2') is True
- greater_numeric_text('0', '0') is False
- greater_numeric_text('-1', '-2') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0146 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def greater_numeric_text(left: str, right: str) -> bool:
    raise NotImplementedError("TODO: PB0146")


def self_test() -> None:
    assert greater_numeric_text('10', '2') is True
    assert greater_numeric_text('0', '0') is False
    assert greater_numeric_text('-1', '-2') is True
