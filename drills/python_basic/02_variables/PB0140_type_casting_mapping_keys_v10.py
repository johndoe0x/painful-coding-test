"""
PB0140 — 문자열 키를 정수로

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 key를 int로, value를 float로 변환한 새 딕셔너리를 반환하세요.

연습 초점
---------
딕셔너리 항목의 일괄 타입 변환

구현할 함수
-----------
def cast_mapping_keys(mapping: dict[str, str]) -> dict[int, float]:

예시 및 필수 테스트
-------------------
- cast_mapping_keys({'1': '2.5'}) == {1: 2.5}
- cast_mapping_keys({}) == {}
- cast_mapping_keys({'0': '0'}) == {0: 0.0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0140 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_mapping_keys(mapping: dict[str, str]) -> dict[int, float]:
    raise NotImplementedError("TODO: PB0140")


def self_test() -> None:
    assert cast_mapping_keys({'1': '2.5'}) == {1: 2.5}
    assert cast_mapping_keys({}) == {}
    assert cast_mapping_keys({'0': '0'}) == {0: 0.0}
