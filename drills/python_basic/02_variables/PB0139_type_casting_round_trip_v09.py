"""
PB0139 — 정수 문자열 왕복

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
text를 int로 변환한 뒤 다시 str로 변환해 불필요한 선행 0을 제거한 표현을 반환하세요.

연습 초점
---------
캐스팅 왕복이 표현에 미치는 영향

구현할 함수
-----------
def integer_round_trip(text: str) -> str:

예시 및 필수 테스트
-------------------
- integer_round_trip('007') == '7'
- integer_round_trip('0') == '0'
- integer_round_trip('-01') == '-1'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0139 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def integer_round_trip(text: str) -> str:
    raise NotImplementedError("TODO: PB0139")


def self_test() -> None:
    assert integer_round_trip('007') == '7'
    assert integer_round_trip('0') == '0'
    assert integer_round_trip('-01') == '-1'
