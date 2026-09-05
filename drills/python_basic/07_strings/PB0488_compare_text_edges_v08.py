"""
PB0488 — 같은 양 끝인지 비교하기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 문자열이 모두 비어 있지 않고 첫 글자끼리와 마지막 글자끼리가 모두 같을 때 True를 반환한다.

연습 초점
---------
각 문자열의 0번과 -1번 인덱스를 안전하게 비교한다.

구현할 함수
-----------
def same_edge_characters(left: str, right: str) -> bool:

예시 및 필수 테스트
-------------------
- same_edge_characters('start', 'street') is True
- same_edge_characters('cat', 'car') is False
- same_edge_characters('', '') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0488 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def same_edge_characters(left: str, right: str) -> bool:
    raise NotImplementedError("TODO: PB0488")


def self_test() -> None:
    assert same_edge_characters('start', 'street') is True
    assert same_edge_characters('cat', 'car') is False
    assert same_edge_characters('', '') is False
