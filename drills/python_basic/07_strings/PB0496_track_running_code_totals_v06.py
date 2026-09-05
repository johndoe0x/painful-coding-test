"""
PB0496 — 문자 코드 누적 합

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: for

문제
----
각 문자를 처리한 직후까지의 ord 누적 합을 리스트로 반환한다.

연습 초점
---------
반복할 때마다 누적 상태를 갱신하고 결과에 추가한다.

구현할 함수
-----------
def running_codepoint_totals(text: str) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- running_codepoint_totals('ABC') == [65, 131, 198]
- running_codepoint_totals('a!') == [97, 130]
- running_codepoint_totals('') == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0496 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def running_codepoint_totals(text: str) -> list[int]:
    raise NotImplementedError("TODO: PB0496")


def self_test() -> None:
    assert running_codepoint_totals('ABC') == [65, 131, 198]
    assert running_codepoint_totals('a!') == [97, 130]
    assert running_codepoint_totals('') == []
