"""
PB0138 — 문자 코드 왕복

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
number_text를 int로 변환한 뒤 chr로 해당 유니코드 문자를 반환하세요.

연습 초점
---------
문자열·정수·문자 사이 변환

구현할 함수
-----------
def cast_code_point(number_text: str) -> str:

예시 및 필수 테스트
-------------------
- cast_code_point('65') == 'A'
- cast_code_point('48') == '0'
- cast_code_point('32') == ' '

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0138 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_code_point(number_text: str) -> str:
    raise NotImplementedError("TODO: PB0138")


def self_test() -> None:
    assert cast_code_point('65') == 'A'
    assert cast_code_point('48') == '0'
    assert cast_code_point('32') == ' '
