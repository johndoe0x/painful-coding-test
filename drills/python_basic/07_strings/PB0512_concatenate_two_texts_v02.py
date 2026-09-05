"""
PB0512 — 두 문자열 바로 붙이기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
left 뒤에 right를 그대로 붙인 문자열을 반환한다.

연습 초점
---------
+ 연산자의 문자열 결합 동작과 빈 문자열을 확인한다.

구현할 함수
-----------
def concatenate_text(left: str, right: str) -> str:

예시 및 필수 테스트
-------------------
- concatenate_text('hello', 'world') == 'helloworld'
- concatenate_text('', 'x') == 'x'
- concatenate_text('a', '') == 'a'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0512 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def concatenate_text(left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0512")


def self_test() -> None:
    assert concatenate_text('hello', 'world') == 'helloworld'
    assert concatenate_text('', 'x') == 'x'
    assert concatenate_text('a', '') == 'a'
