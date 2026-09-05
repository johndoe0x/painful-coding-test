"""
PB0348 — 불리언 문자열 변환

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
flag가 참이면 'true', 아니면 'false'를 반환한다.

연습 초점
---------
불리언의 두 가능성을 if-else로 처리

구현할 함수
-----------
def boolean_word_if_else(flag: bool) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- boolean_word_if_else(True) == 'true'
- boolean_word_if_else(False) == 'false'
- boolean_word_if_else(not False) == 'true'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0348 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def boolean_word_if_else(flag: bool) -> str:
    raise NotImplementedError("TODO: PB0348")


def self_test() -> None:
    assert boolean_word_if_else(True) == 'true'
    assert boolean_word_if_else(False) == 'false'
    assert boolean_word_if_else(not False) == 'true'
