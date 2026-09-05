"""
PB0705 — 오른쪽 우선 병합

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 딕셔너리를 합치되 같은 key는 right의 value를 사용한다. 원본은 바꾸지 않는다.

연습 초점
---------
dict unpacking 또는 update 우선순위

구현할 함수
-----------
def dict_merge_prefer_right(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((left := {'a': 1}), (right := {'a': 2, 'b': 3}), dict_merge_prefer_right(left, right) == {'a': 2, 'b': 3} and left == {'a': 1} and right == {'a': 2, 'b': 3})[-1] is True
- dict_merge_prefer_right({}, {}) == {}
- dict_merge_prefer_right({'x': 1}, {}) == {'x': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0705 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_merge_prefer_right(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0705")


def self_test() -> None:
    assert ((left := {'a': 1}), (right := {'a': 2, 'b': 3}), dict_merge_prefer_right(left, right) == {'a': 2, 'b': 3} and left == {'a': 1} and right == {'a': 2, 'b': 3})[-1] is True
    assert dict_merge_prefer_right({}, {}) == {}
    assert dict_merge_prefer_right({'x': 1}, {}) == {'x': 1}
