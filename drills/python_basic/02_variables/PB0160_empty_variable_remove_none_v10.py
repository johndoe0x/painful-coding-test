"""
PB0160 — None만 제거

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
None 원소만 제거하고 0, False, 빈 문자열은 보존하세요.

연습 초점
---------
비어 있음의 정확한 정의

구현할 함수
-----------
def remove_none_values(values: list[object | None]) -> list[object]:

예시 및 필수 테스트
-------------------
- remove_none_values([None, 0, '', False]) == [0, '', False]
- remove_none_values([]) == []
- remove_none_values([None]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0160 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def remove_none_values(values: list[object | None]) -> list[object]:
    raise NotImplementedError("TODO: PB0160")


def self_test() -> None:
    assert remove_none_values([None, 0, '', False]) == [0, '', False]
    assert remove_none_values([]) == []
    assert remove_none_values([None]) == []
