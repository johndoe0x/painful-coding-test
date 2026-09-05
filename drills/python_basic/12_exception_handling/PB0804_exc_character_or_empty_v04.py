"""
PB0804 — 문자열 안전 인덱스

Chapter: Exception Handling
Topic: Error Catching
Seed: 81 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: try

문제
----
text[index]를 반환하고 IndexError면 빈 문자열을 반환한다.

연습 초점
---------
문자열에서도 발생하는 IndexError 처리

구현할 함수
-----------
def exc_character_or_empty(text: str, index: int) -> str:

필수 구현 방식
--------------
- try-except를 사용한다.

예시 및 필수 테스트
-------------------
- exc_character_or_empty('abc', 1) == 'b'
- exc_character_or_empty('', 0) == ''
- exc_character_or_empty('abc', -1) == 'c'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0804 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exc_character_or_empty(text: str, index: int) -> str:
    raise NotImplementedError("TODO: PB0804")


def self_test() -> None:
    assert exc_character_or_empty('abc', 1) == 'b'
    assert exc_character_or_empty('', 0) == ''
    assert exc_character_or_empty('abc', -1) == 'c'
