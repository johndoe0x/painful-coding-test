"""
PB0438 — 리스트 간격 추출

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(values)이고 stride가 양수라고 가정해 start 인덱스부터 끝까지 stride 간격의 원소를 반환한다.

연습 초점
---------
유효한 컬렉션 시작 인덱스에 step 적용

구현할 함수
-----------
def values_at_stride(values: list[int], start: int, stride: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- values_at_stride([0, 1, 2, 3, 4], 1, 2) == [1, 3]
- values_at_stride([], 0, 3) == []
- values_at_stride([5, 6], 1, 5) == [6]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0438 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def values_at_stride(values: list[int], start: int, stride: int) -> list[int]:
    raise NotImplementedError("TODO: PB0438")


def self_test() -> None:
    assert values_at_stride([0, 1, 2, 3, 4], 1, 2) == [1, 3]
    assert values_at_stride([], 0, 3) == []
    assert values_at_stride([5, 6], 1, 5) == [6]
