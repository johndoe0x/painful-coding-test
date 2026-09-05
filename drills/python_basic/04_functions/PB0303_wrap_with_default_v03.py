"""
PB0303 — 기본 괄호 감싸기

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
left와 right로 text를 감싸며 생략된 인자는 대괄호를 사용한다.

연습 초점
---------
여러 기본 인자와 위치 인자

구현할 함수
-----------
def wrap_with_default(text: str, left: str = '[', right: str = ']') -> str:

예시 및 필수 테스트
-------------------
- wrap_with_default('x') == '[x]'
- wrap_with_default('x', '(') == '(x]'
- wrap_with_default('', '<', '>') == '<>'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0303 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def wrap_with_default(text: str, left: str = '[', right: str = ']') -> str:
    raise NotImplementedError("TODO: PB0303")


def self_test() -> None:
    assert wrap_with_default('x') == '[x]'
    assert wrap_with_default('x', '(') == '(x]'
    assert wrap_with_default('', '<', '>') == '<>'
