"""
PB0387 — 같은 선행 문자 제거

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: while

문제
----
한 글자인 character와 같은 문자가 text 앞에 이어지는 동안 while로 제거한다.

연습 초점
---------
복합 경계 조건을 가진 while

구현할 함수
-----------
def drop_leading_character_while(text: str, character: str) -> str:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- drop_leading_character_while('---name', '-') == 'name'
- drop_leading_character_while('name', '-') == 'name'
- drop_leading_character_while('', 'x') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0387 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def drop_leading_character_while(text: str, character: str) -> str:
    raise NotImplementedError("TODO: PB0387")


def self_test() -> None:
    assert drop_leading_character_while('---name', '-') == 'name'
    assert drop_leading_character_while('name', '-') == 'name'
    assert drop_leading_character_while('', 'x') == ''
