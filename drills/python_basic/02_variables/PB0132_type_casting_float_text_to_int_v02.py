"""
PB0132 — 실수 문자열을 정수로

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
'12.0' 같은 문자열을 먼저 float로, 그다음 int로 변환하세요.

연습 초점
---------
단계적인 타입 캐스팅

구현할 함수
-----------
def cast_whole_number(text: str) -> int:

예시 및 필수 테스트
-------------------
- cast_whole_number('12.0') == 12
- cast_whole_number('0.0') == 0
- cast_whole_number('-3.9') == -3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0132 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_whole_number(text: str) -> int:
    raise NotImplementedError("TODO: PB0132")


def self_test() -> None:
    assert cast_whole_number('12.0') == 12
    assert cast_whole_number('0.0') == 0
    assert cast_whole_number('-3.9') == -3
