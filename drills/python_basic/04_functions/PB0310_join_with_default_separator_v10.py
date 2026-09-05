"""
PB0310 — 기본 구분자 결합

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
words를 separator로 결합하며 separator 생략 시 쉼표를 사용한다.

연습 초점
---------
컬렉션 입력과 기본 문자열 인자

구현할 함수
-----------
def join_with_default_separator(words: list[str], separator: str = ',') -> str:

예시 및 필수 테스트
-------------------
- join_with_default_separator(['a', 'b']) == 'a,b'
- join_with_default_separator(['a', 'b'], '-') == 'a-b'
- join_with_default_separator([]) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0310 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def join_with_default_separator(words: list[str], separator: str = ',') -> str:
    raise NotImplementedError("TODO: PB0310")


def self_test() -> None:
    assert join_with_default_separator(['a', 'b']) == 'a,b'
    assert join_with_default_separator(['a', 'b'], '-') == 'a-b'
    assert join_with_default_separator([]) == ''
