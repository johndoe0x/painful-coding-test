"""
PB0131 — 필드 타입 변환

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
age_text는 int, score_text는 float로 변환해 tuple로 반환하세요.

연습 초점
---------
문자열을 목적 타입으로 명시적 변환

구현할 함수
-----------
def convert_fields(age_text: str, score_text: str) -> tuple[int, float]:

예시 및 필수 테스트
-------------------
- convert_fields('21', '98.5') == (21, 98.5)
- convert_fields('0', '0') == (0, 0.0)
- convert_fields('-1', '-2.5') == (-1, -2.5)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0131 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def convert_fields(age_text: str, score_text: str) -> tuple[int, float]:
    raise NotImplementedError("TODO: PB0131")


def self_test() -> None:
    assert convert_fields('21', '98.5') == (21, 98.5)
    assert convert_fields('0', '0') == (0, 0.0)
    assert convert_fields('-1', '-2.5') == (-1, -2.5)
