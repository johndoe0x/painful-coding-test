"""
PB0703 — 카운터 증가

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 key의 값을 amount만큼 늘린다. 없는 key는 0에서 시작한다.

연습 초점
---------
get 기본값과 갱신

구현할 함수
-----------
def dict_increment_value(counts: dict[str, int], key: str, amount: int = 1) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 2}), dict_increment_value(items, 'a') == {'a': 3} and items == {'a': 2})[-1] is True
- dict_increment_value({}, 'x', 3) == {'x': 3}
- dict_increment_value({'a': 2}, 'b', -1) == {'a': 2, 'b': -1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0703 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_increment_value(counts: dict[str, int], key: str, amount: int = 1) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0703")


def self_test() -> None:
    assert ((items := {'a': 2}), dict_increment_value(items, 'a') == {'a': 3} and items == {'a': 2})[-1] is True
    assert dict_increment_value({}, 'x', 3) == {'x': 3}
    assert dict_increment_value({'a': 2}, 'b', -1) == {'a': 2, 'b': -1}
