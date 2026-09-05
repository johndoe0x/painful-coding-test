"""
PB0377 — 첫 Truthy 문자열

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: if

문제
----
first, second, third 순서에서 처음 truthy인 문자열을 반환하고 모두 falsy면 빈 문자열을 반환한다.

연습 초점
---------
or 연산의 피연산자 반환 규칙

구현할 함수
-----------
def choose_first_truthy_text(first: str, second: str, third: str) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- choose_first_truthy_text('', 'two', 'three') == 'two'
- choose_first_truthy_text('one', 'two', '') == 'one'
- choose_first_truthy_text('', '', '') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0377 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def choose_first_truthy_text(first: str, second: str, third: str) -> str:
    raise NotImplementedError("TODO: PB0377")


def self_test() -> None:
    assert choose_first_truthy_text('', 'two', 'three') == 'two'
    assert choose_first_truthy_text('one', 'two', '') == 'one'
    assert choose_first_truthy_text('', '', '') == ''
