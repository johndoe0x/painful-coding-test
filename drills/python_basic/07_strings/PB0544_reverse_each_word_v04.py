"""
PB0544 — 각 단어 내부 뒤집기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
공백 하나로 구분된 각 단어의 글자 순서만 뒤집고 단어 순서는 유지한다.

연습 초점
---------
여러 문자열 각각에 역순 슬라이스를 적용한 뒤 재결합한다.

구현할 함수
-----------
def reverse_words_inside(sentence: str) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_words_inside('cat dog') == 'tac god'
- reverse_words_inside('Python') == 'nohtyP'
- reverse_words_inside('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0544 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_words_inside(sentence: str) -> str:
    raise NotImplementedError("TODO: PB0544")


def self_test() -> None:
    assert reverse_words_inside('cat dog') == 'tac god'
    assert reverse_words_inside('Python') == 'nohtyP'
    assert reverse_words_inside('') == ''
