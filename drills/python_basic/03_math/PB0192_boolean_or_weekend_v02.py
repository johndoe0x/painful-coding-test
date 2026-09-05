"""
PB0192 — 주말 판별

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
day가 'Saturday' 또는 'Sunday'이면 True를 반환하세요.

연습 초점
---------
두 허용 값 중 하나인지 OR로 검사

구현할 함수
-----------
def is_weekend(day: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- is_weekend('Saturday') is True
- is_weekend('') is False
- is_weekend('Monday') is False and is_weekend('Sunday') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0192 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_weekend(day: str) -> bool:
    raise NotImplementedError("TODO: PB0192")


def self_test() -> None:
    assert is_weekend('Saturday') is True
    assert is_weekend('') is False
    assert is_weekend('Monday') is False and is_weekend('Sunday') is True
