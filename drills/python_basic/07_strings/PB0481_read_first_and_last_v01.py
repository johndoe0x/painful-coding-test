"""
PB0481 — 첫 글자와 마지막 글자

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 text의 첫 글자와 마지막 글자를 tuple로 반환한다.

연습 초점
---------
0번 인덱스와 -1번 인덱스로 양쪽 끝에 접근한다.

구현할 함수
-----------
def first_last(text: str) -> tuple[str, str]:

예시 및 필수 테스트
-------------------
- first_last('code') == ('c', 'e')
- first_last('A') == ('A', 'A')
- first_last('한글') == ('한', '글')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0481 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_last(text: str) -> tuple[str, str]:
    raise NotImplementedError("TODO: PB0481")


def self_test() -> None:
    assert first_last('code') == ('c', 'e')
    assert first_last('A') == ('A', 'A')
    assert first_last('한글') == ('한', '글')
