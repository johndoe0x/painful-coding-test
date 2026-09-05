"""
PB0618 — 인덱스·값 쌍 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
각 문자열을 0부터 시작하는 인덱스와 tuple로 묶어 결과 리스트에 append한다.

연습 초점
---------
enumerate로 얻은 복합 값을 리스트 끝에 순서대로 쌓는다.

구현할 함수
-----------
def append_index_pairs(values: list[str]) -> list[tuple[int, str]]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- append_index_pairs(['a', 'b']) == [(0, 'a'), (1, 'b')]
- append_index_pairs(['x']) == [(0, 'x')]
- append_index_pairs([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0618 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_index_pairs(values: list[str]) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: PB0618")


def self_test() -> None:
    assert append_index_pairs(['a', 'b']) == [(0, 'a'), (1, 'b')]
    assert append_index_pairs(['x']) == [(0, 'x')]
    assert append_index_pairs([]) == []
