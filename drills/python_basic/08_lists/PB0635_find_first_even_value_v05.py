"""
PB0635 — 첫 짝수 값 찾기

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
왼쪽부터 처음 만나는 짝수를 반환하고 없으면 None을 반환한다.

연습 초점
---------
값 조건을 만족하는 첫 원소에서 검색을 종료한다.

구현할 함수
-----------
def first_even_value(values: list[int]) -> int | None:

예시 및 필수 테스트
-------------------
- first_even_value([1, 5, 4, 2]) == 4
- first_even_value([1, 3]) is None
- first_even_value([0]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0635 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_even_value(values: list[int]) -> int | None:
    raise NotImplementedError("TODO: PB0635")


def self_test() -> None:
    assert first_even_value([1, 5, 4, 2]) == 4
    assert first_even_value([1, 3]) is None
    assert first_even_value([0]) == 0
