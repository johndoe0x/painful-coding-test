"""
PB0723 — ID로 레코드 색인

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 03 / 10
Time cap: 150 seconds
Source checks:

문제
----
각 record의 정수 id를 key로 사용한다. 같은 id가 다시 나오면 마지막 record를 저장한다.

연습 초점
---------
딕셔너리 리스트 순회와 동적 key 색인

구현할 함수
-----------
def dict_index_records_by_id(records: list[dict[str, object]]) -> dict[int, dict[str, object]]:

예시 및 필수 테스트
-------------------
- dict_index_records_by_id([{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]) == {1: {'id': 1, 'name': 'A'}, 2: {'id': 2, 'name': 'B'}}
- dict_index_records_by_id([]) == {}
- dict_index_records_by_id([{'id': 1, 'name': 'A'}, {'id': 1, 'name': 'Z'}]) == {1: {'id': 1, 'name': 'Z'}}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0723 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_index_records_by_id(records: list[dict[str, object]]) -> dict[int, dict[str, object]]:
    raise NotImplementedError("TODO: PB0723")


def self_test() -> None:
    assert dict_index_records_by_id([{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]) == {1: {'id': 1, 'name': 'A'}, 2: {'id': 2, 'name': 'B'}}
    assert dict_index_records_by_id([]) == {}
    assert dict_index_records_by_id([{'id': 1, 'name': 'A'}, {'id': 1, 'name': 'Z'}]) == {1: {'id': 1, 'name': 'Z'}}
