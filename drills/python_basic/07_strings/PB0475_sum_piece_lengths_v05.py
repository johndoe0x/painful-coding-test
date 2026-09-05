"""
PB0475 — 조각 문자열 전체 길이

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
parts에 든 모든 문자열 길이의 합을 반환한다.

연습 초점
---------
여러 len 결과를 누적하고 빈 리스트에서는 0을 반환한다.

구현할 함수
-----------
def total_text_length(parts: list[str]) -> int:

예시 및 필수 테스트
-------------------
- total_text_length(['ab', 'cde']) == 5
- total_text_length(['', 'x', '']) == 1
- total_text_length([]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0475 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def total_text_length(parts: list[str]) -> int:
    raise NotImplementedError("TODO: PB0475")


def self_test() -> None:
    assert total_text_length(['ab', 'cde']) == 5
    assert total_text_length(['', 'x', '']) == 1
    assert total_text_length([]) == 0
