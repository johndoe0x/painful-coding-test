"""
PB0439 — 간격 인덱스와 값

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 step으로 0번부터 선택한 인덱스와 값을 tuple로 반환한다.

연습 초점
---------
step 순회에서 인덱스 보존

구현할 함수
-----------
def stepped_index_value_pairs(values: list[str], step: int) -> list[tuple[int, str]]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- stepped_index_value_pairs(['a', 'b', 'c', 'd'], 2) == [(0, 'a'), (2, 'c')]
- stepped_index_value_pairs([], 2) == []
- stepped_index_value_pairs(['x'], 3) == [(0, 'x')]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0439 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def stepped_index_value_pairs(values: list[str], step: int) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: PB0439")


def self_test() -> None:
    assert stepped_index_value_pairs(['a', 'b', 'c', 'd'], 2) == [(0, 'a'), (2, 'c')]
    assert stepped_index_value_pairs([], 2) == []
    assert stepped_index_value_pairs(['x'], 3) == [(0, 'x')]
