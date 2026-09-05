"""
PB0775 — 콜론 범위 표현

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
'start:stop:step' 세 정수를 파싱해 list(range(start, stop, step))을 반환한다.

연습 초점
---------
문자열 필드 unpacking과 range

구현할 함수
-----------
def input_parse_range(text: str) -> list[int]:

예시 및 필수 테스트
-------------------
- input_parse_range('1:6:2') == [1, 3, 5]
- input_parse_range('0:0:1') == []
- input_parse_range('5:0:-2') == [5, 3, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0775 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_range(text: str) -> list[int]:
    raise NotImplementedError("TODO: PB0775")


def self_test() -> None:
    assert input_parse_range('1:6:2') == [1, 3, 5]
    assert input_parse_range('0:0:1') == []
    assert input_parse_range('5:0:-2') == [5, 3, 1]
