"""
PB0273 — 이름 인덱스 사전

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 이름을 마지막 등장 인덱스에 연결한 딕셔너리를 반환한다.

연습 초점
---------
list와 dict 제네릭 타입 힌트

구현할 함수
-----------
def index_names_typed(names: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- index_names_typed(['a', 'b']) == {'a': 0, 'b': 1}
- index_names_typed([]) == {}
- index_names_typed(['a', 'a']) == {'a': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0273 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def index_names_typed(names: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0273")


def self_test() -> None:
    assert index_names_typed(['a', 'b']) == {'a': 0, 'b': 1}
    assert index_names_typed([]) == {}
    assert index_names_typed(['a', 'a']) == {'a': 1}
