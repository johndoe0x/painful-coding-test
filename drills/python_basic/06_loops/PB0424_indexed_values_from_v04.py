"""
PB0424 — 지정 위치부터 인덱스 쌍

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(values)라고 가정하고 for와 range(start, len(values))로 인덱스와 값을 tuple로 반환한다.

연습 초점
---------
유효한 start가 있는 인덱스 순회

구현할 함수
-----------
def indexed_values_from(values: list[str], start: int) -> list[tuple[int, str]]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- indexed_values_from(['a', 'b', 'c'], 1) == [(1, 'b'), (2, 'c')]
- indexed_values_from([], 0) == []
- indexed_values_from(['x'], 1) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0424 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def indexed_values_from(values: list[str], start: int) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: PB0424")


def self_test() -> None:
    assert indexed_values_from(['a', 'b', 'c'], 1) == [(1, 'b'), (2, 'c')]
    assert indexed_values_from([], 0) == []
    assert indexed_values_from(['x'], 1) == []
