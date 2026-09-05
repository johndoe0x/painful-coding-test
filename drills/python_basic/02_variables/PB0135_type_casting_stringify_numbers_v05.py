"""
PB0135 — 숫자를 문자열로

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 정수를 str로 변환한 새 리스트를 반환하세요.

연습 초점
---------
숫자에서 문자열로 명시적 변환

구현할 함수
-----------
def cast_numbers_to_strings(numbers: list[int]) -> list[str]:

예시 및 필수 테스트
-------------------
- cast_numbers_to_strings([1, -2]) == ['1', '-2']
- cast_numbers_to_strings([]) == []
- cast_numbers_to_strings([0]) == ['0']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0135 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_numbers_to_strings(numbers: list[int]) -> list[str]:
    raise NotImplementedError("TODO: PB0135")


def self_test() -> None:
    assert cast_numbers_to_strings([1, -2]) == ['1', '-2']
    assert cast_numbers_to_strings([]) == []
    assert cast_numbers_to_strings([0]) == ['0']
