"""
PB0776 — 좌표 문자열

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
쉼표로 구분된 x와 y를 float로 변환한다.

연습 초점
---------
두 실수 필드 파싱

구현할 함수
-----------
def input_parse_coordinates(text: str) -> tuple[float, float]:

예시 및 필수 테스트
-------------------
- input_parse_coordinates('1.5,2') == (1.5, 2.0)
- input_parse_coordinates(' 0 , 0 ') == (0.0, 0.0)
- input_parse_coordinates('-1,-2.5') == (-1.0, -2.5)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0776 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_coordinates(text: str) -> tuple[float, float]:
    raise NotImplementedError("TODO: PB0776")


def self_test() -> None:
    assert input_parse_coordinates('1.5,2') == (1.5, 2.0)
    assert input_parse_coordinates(' 0 , 0 ') == (0.0, 0.0)
    assert input_parse_coordinates('-1,-2.5') == (-1.0, -2.5)
