"""
PB0247 — 리스트 배율 적용

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
values의 모든 원소에 factor를 곱한 새 리스트를 반환한다.

연습 초점
---------
컬렉션과 설정값 매개변수 조합

구현할 함수
-----------
def scale_each_value(values: list[int], factor: int) -> list[int]:

예시 및 필수 테스트
-------------------
- scale_each_value([1, 2, 3], 2) == [2, 4, 6]
- scale_each_value([], 9) == []
- scale_each_value([-2, 4], -1) == [2, -4]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0247 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def scale_each_value(values: list[int], factor: int) -> list[int]:
    raise NotImplementedError("TODO: PB0247")


def self_test() -> None:
    assert scale_each_value([1, 2, 3], 2) == [2, 4, 6]
    assert scale_each_value([], 9) == []
    assert scale_each_value([-2, 4], -1) == [2, -4]
