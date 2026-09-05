"""
PB0484 — 양 끝 글자 합치기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
빈 문자열이면 '', 한 글자면 그 글자, 그 외에는 첫 글자와 마지막 글자를 이어 반환한다.

연습 초점
---------
길이에 따른 분기 후 양 끝 인덱스를 조합한다.

구현할 함수
-----------
def edge_characters(text: str) -> str:

예시 및 필수 테스트
-------------------
- edge_characters('planet') == 'pt'
- edge_characters('Z') == 'Z'
- edge_characters('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0484 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def edge_characters(text: str) -> str:
    raise NotImplementedError("TODO: PB0484")


def self_test() -> None:
    assert edge_characters('planet') == 'pt'
    assert edge_characters('Z') == 'Z'
    assert edge_characters('') == ''
