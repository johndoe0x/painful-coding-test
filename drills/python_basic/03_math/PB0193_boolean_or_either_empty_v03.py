"""
PB0193 — 둘 중 빈 문자열

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
left 또는 right 중 하나라도 빈 문자열이면 True를 반환하세요.

연습 초점
---------
OR와 빈 값 조건

구현할 함수
-----------
def either_text_empty(left: str, right: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- either_text_empty('', 'x') is True
- either_text_empty('', '') is True
- either_text_empty('a', 'b') is False and either_text_empty('x', '') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0193 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def either_text_empty(left: str, right: str) -> bool:
    raise NotImplementedError("TODO: PB0193")


def self_test() -> None:
    assert either_text_empty('', 'x') is True
    assert either_text_empty('', '') is True
    assert either_text_empty('a', 'b') is False and either_text_empty('x', '') is True
