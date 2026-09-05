"""
PB0186 — +=로 문장 만들기

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
text에 각 token을 +=로 이어 붙이세요.

연습 초점
---------
문자열의 += 재할당

구현할 함수
-----------
def append_tokens(start: str, tokens: list[str]) -> str:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- append_tokens('a', ['b', 'c']) == 'abc'
- append_tokens('', []) == ''
- append_tokens('', ['x']) == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0186 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_tokens(start: str, tokens: list[str]) -> str:
    raise NotImplementedError("TODO: PB0186")


def self_test() -> None:
    assert append_tokens('a', ['b', 'c']) == 'abc'
    assert append_tokens('', []) == ''
    assert append_tokens('', ['x']) == 'x'
