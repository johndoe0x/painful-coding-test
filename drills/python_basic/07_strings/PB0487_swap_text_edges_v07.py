"""
PB0487 — 양 끝 글자 자리 바꾸기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
길이가 2 이상이면 첫 글자와 마지막 글자의 자리를 바꾼 새 문자열을 만들고, 더 짧으면 그대로 반환한다.

연습 초점
---------
인덱싱으로 양 끝을 읽고 가운데 부분과 재조합한다.

구현할 함수
-----------
def swap_edge_characters(text: str) -> str:

예시 및 필수 테스트
-------------------
- swap_edge_characters('abcd') == 'dbca'
- swap_edge_characters('a') == 'a'
- swap_edge_characters('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0487 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def swap_edge_characters(text: str) -> str:
    raise NotImplementedError("TODO: PB0487")


def self_test() -> None:
    assert swap_edge_characters('abcd') == 'dbca'
    assert swap_edge_characters('a') == 'a'
    assert swap_edge_characters('') == ''
