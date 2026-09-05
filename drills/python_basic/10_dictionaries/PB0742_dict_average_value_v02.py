"""
PB0742 — value 평균

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있으면 0.0, 아니면 모든 value의 평균을 반환한다.

연습 초점
---------
values 합계와 개수

구현할 함수
-----------
def dict_average_value(mapping: dict[str, float]) -> float:

예시 및 필수 테스트
-------------------
- dict_average_value({'a': 2.0, 'b': 4.0}) == 3.0
- dict_average_value({}) == 0.0
- dict_average_value({'x': -1.0, 'y': 1.0}) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0742 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_average_value(mapping: dict[str, float]) -> float:
    raise NotImplementedError("TODO: PB0742")


def self_test() -> None:
    assert dict_average_value({'a': 2.0, 'b': 4.0}) == 3.0
    assert dict_average_value({}) == 0.0
    assert dict_average_value({'x': -1.0, 'y': 1.0}) == 0.0
