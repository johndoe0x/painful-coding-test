"""
PB0543 — 단어 순서 뒤집기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
공백 하나로 구분된 단어들의 순서만 뒤집어 공백 하나로 다시 연결한다.

연습 초점
---------
split 결과 리스트에 역방향 슬라이스를 적용한다.

구현할 함수
-----------
def reverse_word_order(sentence: str) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_word_order('one two three') == 'three two one'
- reverse_word_order('hello') == 'hello'
- reverse_word_order('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0543 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_word_order(sentence: str) -> str:
    raise NotImplementedError("TODO: PB0543")


def self_test() -> None:
    assert reverse_word_order('one two three') == 'three two one'
    assert reverse_word_order('hello') == 'hello'
    assert reverse_word_order('') == ''
