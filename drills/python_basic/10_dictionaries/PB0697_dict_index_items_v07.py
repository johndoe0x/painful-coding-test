"""
PB0697 — 인덱스로 항목 저장

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 항목을 0부터 시작하는 인덱스 key에 연결한다.

연습 초점
---------
enumerate로 key-value 생성

구현할 함수
-----------
def dict_index_items(items: list[str]) -> dict[int, str]:

예시 및 필수 테스트
-------------------
- dict_index_items(['a', 'b']) == {0: 'a', 1: 'b'}
- dict_index_items([]) == {}
- dict_index_items(['x']) == {0: 'x'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0697 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_index_items(items: list[str]) -> dict[int, str]:
    raise NotImplementedError("TODO: PB0697")


def self_test() -> None:
    assert dict_index_items(['a', 'b']) == {0: 'a', 1: 'b'}
    assert dict_index_items([]) == {}
    assert dict_index_items(['x']) == {0: 'x'}
