"""
PB0442 — 인덱스로 리스트 역순

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
역순 range 인덱스로 values의 원소를 뒤에서부터 반환한다.

연습 초점
---------
역순 인덱스를 컬렉션 접근에 사용

구현할 함수
-----------
def reverse_values_by_index(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_values_by_index([1, 2, 3]) == [3, 2, 1]
- reverse_values_by_index([]) == []
- reverse_values_by_index([-1]) == [-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0442 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_values_by_index(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0442")


def self_test() -> None:
    assert reverse_values_by_index([1, 2, 3]) == [3, 2, 1]
    assert reverse_values_by_index([]) == []
    assert reverse_values_by_index([-1]) == [-1]
