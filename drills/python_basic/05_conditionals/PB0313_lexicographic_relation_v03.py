"""
PB0313 — 사전식 문자열 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열의 사전식 비교 결과를 'before', 'same', 'after' 중 하나로 반환한다.

연습 초점
---------
문자열에 대한 비교 연산

구현할 함수
-----------
def lexicographic_relation(left: str, right: str) -> str:

예시 및 필수 테스트
-------------------
- lexicographic_relation('apple', 'banana') == 'before'
- lexicographic_relation('code', 'code') == 'same'
- lexicographic_relation('z', 'a') == 'after'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0313 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def lexicographic_relation(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0313")


def self_test() -> None:
    assert lexicographic_relation('apple', 'banana') == 'before'
    assert lexicographic_relation('code', 'code') == 'same'
    assert lexicographic_relation('z', 'a') == 'after'
